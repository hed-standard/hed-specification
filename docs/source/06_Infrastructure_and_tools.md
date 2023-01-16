# 6. Infrastructure and tools

The HED infrastructure includes functions written in Python, Matlab,
and JavaScript that support the use of HED in applications.
This section describes the expected behavior of the HED infrastructure and
its integration into other systems such as [**BIDS**](https://bids.neuroimaging.io/).

This section also specifies how HED-compliant tools should handle various aspects of HED.
In general tools should either explicitly call HED validation to assure that the input
tag strings are valid or should make explicit that they assume the HED has already been validated.
Most tools will use the later approach. 

## 6.1. Basic tag handling

HED-compliant tools should be able to a handle HED string in its equivalent forms
and using various valid syntax as described in this section.

````{warning} 
HED-compliant tools should be able to handle tags in **long-form**,
**short-form** or any valid **intermediate-form**.

````
(parenthesized-hed-strings-anchor)=


````{warning} 
HED-compliant tools should be able to handle arbitrary correctly nested parentheses
and correctly distinguish differences in grouping.

````

(tag-ordering-anchor)=
### 6.1.3 Tag ordering

Any ordering of HED tags at the same level within a HED string is equivalent.

````{warning} 
HED-compliant tools should not rely on the order that HED tags appear within a string during processing.
````

## 6.2. Validation of HED annotations

Validation of HED annotations is an essential step in using HED for large-scale, reproducible
analysis. Third-generation HED (versions >= 8.0.0) encourages detailed documentation of events 
and provides mechanisms for mapping the interrelationships of events and task intent. 
The additional annotation power also requires more extensive validation to assure consistency
across annotations. HED-validators are provided in both Python and JavaScript. 
There is also a MATLAB wrapper for the Python validator functions.

HED distinguishes five levels of validation: [**tag**](tag-validation-anchor),
[**string**](string-validation-anchor),
[**sidecar**](sidecar-validation-anchor), [**event**](event-validation-anchor), 
and [**recording**](recording-validation-anchor).

Previous generations of HED (< 8.0.0) only required validation at the first 
four levels. Since third-generation HED can document relationships across events, 
it also requires an additional dataset level validation to check cross-event relationships. 

Validation can also be categorized as syntactic or semantic. Syntactic validation, 
which occurs mainly at the HED tag and HED string levels, tests that the tags are 
properly formed, independently of the HED schema or purpose of the tags. Semantic 
validation tests that the tags are used correctly and that they comply with the 
requirements of the relevant HED schema.

Syntactic validation is usually done during the initial parsing of the HED strings into HED tags.
Validators are not required to separate syntactic and semantic validation.
Tools are expected to require a valid HED schema for validation or other tag-specific behavior.

(tag-validation-anchor)=
### 6.2.1. Tag validation

HED tag level validation checks each individual HED tag against its associated schema. 
The long-form of the tag must be in the schema under which the tag is being validated. 


See [**Tags that take details**](./03_HED_formats.md#tags-that-take-values) for
additional details about HED schema nodes with placeholders.

See [**Sidecar validation**](sidecar-validation-anchor) for information about the
special role of `#` placeholders in sidecars.

#### 6.2.1.2. Tag values and units

As discussed in the previous section, schema `#` nodes must be leaf nodes
that represent a value to be associated with the node's parent.

If the `#` node has a *unitClass* attribute,
the units must comply with those of the specified *unitClass*.
The value and the units should always be separated by a blank.



(string-validation-anchor)=
### 6.2.2. String validation

HED string level validation focuses on the proper formation of HED strings and tag-groups 
within the HED strings including matching of parentheses and
proper delimiting of HED tags by commas. 

Empty parentheses and multiple commas with no intervening
tags represent empty tags and are invalid, as are HED strings with leading or trailing commas.

Duplicated tags at the same level in a tag-group or at the top level are not allowed.
For example, *(Red, Red, Blue)* is an invalid HED string.

(sidecar-validation-anchor)=
### 6.2.3. Sidecar validation

A sidecar is a dictionary that can be used to associate event file columns
and their values with HED annotations.
This dictionary allows HED tools to assemble HED annotations for each row in an event file.

HED sidecar validation assumes that the dictionaries are saved in JSON format and comply with the
[**BIDS sidecar**](https://bids-specification.readthedocs.io/en/stable/appendices/hed.html) format.

Sidecar validation is similar to HED string validation, but the error messages are keyed to
dictionary location rather than to line numbers in the event file or spreadsheet.

#### 6.2.3.1 Types of sidecar HED entries

A BIDS sidecar is dictionary may have many entries, some of which are ignored by HED tools.

````{Admonition} Three types of JSON sidecar entries of interest to HED tools 
- **Categorical annotations**: are associated with a particular column and provide
individual annotations for each column value. 
The dictionary is not required to provide annotations for every possible
value in the column, although tools may choose to issue a warning if appropriate.  
<p></p>

- **Value annotations**: are associated with a particular column and provide
an annotation that applies to any entry in the column.
The HED annotation must contain a single `#` placeholder,
and each individual column value is substituted for the `#` in the annotation
when the annotation for the entire row is assembled.

<p></p>
 
- **Dummy annotations**: are similar in format to categorical annotations,
but are not associated with any event file columns,
rather these annotations are mainly used for HED definitions.

````

While HED definitions are allowed anywhere,
the recommended style is to separate them into dummy sidecar entries for readability.
The sidecar does not have to provide an HED-relevant entry for every event file column.
Columns with no corresponding entry are skipped during assembly of the HED annotation
for the row.

The following example illustrates the three types of JSON entries that HED tools process.

````{Admonition} Example of three types of sidecar annotation entries.
:class: tip
```json
{
   "trial_type": {
      "LongName": "Event category",
      "Description": "Indicator of type of action that is expected",
      "HED": {
          "go": "Sensory-event, Visual-presentation, (Square, Blue)",
          "stop": "Sensory-event, Visual-presentation, (Square, Red)"
       }
   },
   "response_time": {
       "LongName": "Response time after stimulus",
       "Description": "Time from stimulus presentation until subject presses button",
       "HED": "(Delay/# ms, Agent-action, (Experiment-participant, (Press, Mouse-button))),"
   },
   "dummy_defs": {
        "HED": {
            "MyDef1": "(Definition/Image1, (Image, Face))",
            "MyDef2": "(Definition/Cue1, (Buzz))"
        }
   }
}
```
````

In the example the `trial_type` key references a **categorical annotation**.
Categorical entries have keys corresponding to the event file column names.
The value of a categorical entry is a dictionary which has a `HED` key.
The keys of this second dictionary are the values (`go` and `stop`) that
appear in the `trial_type` column of the event file.
and the values are the HED tags associated with those values.

The `response_time` key references a **value annotation**.
Value entries have keys, one of which is `HED`.
Associated with the `HED` key is a HED annotation value.
There must be exactly one `#` placeholder in the annotation.
The actual value in the col

The `dummy_defs` is an example of a **dummy annotation**.
The value of this entry is a dictionary with a `HED` key
pointing to a dictionary.
A **dummy annotation** is similar in form to a **categorical annotation**,
but its keys do not correspond to any event file column names.
Rather it is used as a container to organize HED definitions.


#### 6.2.3.1 Placeholders in sidecars

Sidecars may have at most 
Sidecars also allow
The validator checks that there is exactly one `#` in the HED string annotation associated 
with each non-categorical column. The `#` placeholder should correspond 
to a `#` in the HED schema, indicating that the parent tag expects a value. 
If the placeholder is followed by a unit designator, the validator checks that 
these units are consistent with the unit class of the
corresponding `#` in the schema.  The units are not mandatory.
If an annotation is not provided for a particular column value,
that entry is skipped when the annotation for a row is assembled.

(event-validation-anchor)=
### 6.2.4. Event validation

Dataset formats such as BIDS (Brain Imaging Data Structure) allow users to provide HED tags 
in multiple places. For example, if a study uses local codes to represent different types of
events, the dataset specification often allows users to use the local codes when listing the
events and then provide some format of dictionary mapping local codes to tags. 
During event level validation, all of these tags must be assembled into a HED string 
representing the full HED annotation for that event. 

Several tag attributes are validated at this stage. The expanded event-level HED string
annotating an event must include all tags with the *required* attribute and only one copy
of each tag with the *unique* attribute.

(recording-validation-anchor)=
### 6.2.5. Recording validation

The introduction of definitions and temporal scope has added additional complexity 
to validation. Instead of being able to validate the HED string for each event individually,
third generation HED validators must also check consistency across all events in the 
data-recording. This validation requires multiple passes through of the assembled HED tags
associated with the data-recording.

Since *Definition* tags can appear anywhere in the event annotations for a data recording, 
an initial scan must be made to assemble all definitions for a data recording and 
to make sure that the definition names are unique. 

To validate temporal scope, the validator must assure that each *Onset* and *Offset* tag 
is associated with an appropriately defined label. The validator must also check to make 
sure that *Onset* and *Offset* tags are properly matched within the data recording.


## 6.3. Analysis tools

Third-generation HED analysis tools also require some additional infrastructure. These tools
should call the HED libraries to fully expand the tags for a data recording before doing
analysis. In addition to converting all HED tags to their long form, the library tools can 
remove the definitions and replace *def/* with the full tag expansion with any defined labels.  

Each event that is within the temporal scope of a scoped event, should have the scoped event
information added to the *Event-context* tag group of the intermediate event upon request.
*Delay* tag expansions as insertions of actual events should also be supported. 
*Duration* tag expansion in which offset events should be inserted should also be supported. 
The HED tools should provide this expansion capability as well as a standardized representation
of events in a data recording to enable tools to use a standard API for accessing tag information.


## 6.4. HED support of BIDS

BIDS dataset events are stored in tab-separated tabular files whose names end in `events.tsv`.
The tabular files must have the column names in the first row.
The remaining rows represent event markers in the timeline of a similarly named data file.
The columns contain categorical values, other types of values, or HED strings.
The first two columns in a BIDS events file are the `onset` and `duration`, respectively.
The `onset` is the time of the event marker,
while the `duration` represents the duration of some aspect of the event.

Categorical column values are chosen from a small, explicitly defined subset. 
Value columns may contain numeric values or other types of values such as file names. 
HED tools assume that event files are spreadsheets, either in BIDS (`.tsv`) format or 
Excel format.

The HED tools require that each column of an event file contains items of the same class 
(categorical or value) and that value columns contain items of the same basic type. Files not
satisfying these requirements may need additional processing before being handled by HED tools.

### 6.4.1. BIDS event files
[BIDS (Brain Imaging Data Structure)](https://bids.neuroimaging.io/is ) is a specification 
along with supporting tools for organizing and describing brain imaging and behavioral data.
BIDS event files  satisfy the criteria of the previous section. 

BIDS supports HED annotation of events. BIDS events appear in tab-separated value (`_events.tsv`)
files in various places in the dataset hierarchy. BIDS event files must have an `onset` column
and a `duration` column. The following shows an excerpt from a BIDS event file:


````{admonition} **Example:** Excerpt from a BIDS event file.

```
onset  duration  trial_type  response_time stim_file
1.2    0.6       go          1.435         images/red_square.jpg
5.6    0.6       stop        1.739         images/blue_square.jpg
```
````

The `trial_type` column contains categorical values, while the `response_time` and `stim_file`
columns contain non-categorical values. In theory `stim_file` could be considered a categorical 
column if there were just a few possible images, but this would not be common usage. 
BIDS allows an optional column named `HED` to contain HED strings relevant for the event 
instance. The above example does not have this column. 

Processing tools read these event files and create their own event representation. 
The Python version of HEDTools uses the Pandas `DataFrame` for its low-level representations. 
For MATLAB programs, the dataset events are often held in `struct` arrays.  
In EEGLAB, for example, the events for an EEG data recording appear in the `EEG.event` 
structure array. The time of the event is given in frames in the `EEG.event.latency` 
field for data that has not been epoched. 


### 6.4.2. BIDS sidecars

BIDS also recommends data dictionaries in the form of JSON sidecars to document
the meaning of the data in the event files.HEDTools assume 
that dictionaries for event metadata are contained in BIDS-compatible sidecars.

BIDS allows the tagging of both categorical and non-categorical columns in these sidecars 
as explained in the [HED appendix](https://github.com/bids-standard/bids-specification/blob/master/src/99-appendices/03-hed.md) of the BIDS
specification. Internally, EEGLAB and CTAGGER use mapping objects that are stored in the EEG
structure. However, these mapping options can be written to or read from BIDS JSON sidecars. 

Each event file spreadsheet column containing categorical values may also have a categorical
dictionary that documents the meaning of the data in that column. HED also provides for the HED
tagging of non-categorical columns as explained below. The following example shows the JSON
sidecar format for annotating the same event file of the previous section. The `"HED"` key 
for the `"trial_type"` column indexes the categorical dictionary associated with the 
`trial_type` column in the event file. 

````{admonition} **Example:** JSON sidecar for annotating the columns of an event file.

```json
{
    "trial_type": {
        "LongName": "Event category",
        "Description": "Indicator of type of action that is expected.",
        "Levels": {
            "go": "A red square is displayed to indicate starting",
            "stop": "A blue square is displayed to indicate stopping."
        },
        "HED": {
            "go": "Sensory-event, Visual-presentation, (Square, Red), (Computer-screen, Center-of), Description/A red square is displayed to indicate starting.",
            "stop": "Sensory-event, Visual-presentation, (Square, Blue), (Computer-screen, Center-of), Description/A blue square is displayed to indicate stopping."
        }
    },
    "response_time": {
        "LongName": "Response time after stimulus",
        "Description": "Time from stimulus until subject presses button.",
        "Units": "ms",
        "HED": "(Delay/# ms, Agent-action, Experiment-participant, Press, Mouse-button, Description/Time from stimulus until subject presses button)"
    },
    "stim_file": {
        "LongName": "Stimulus file name",
        "Description": "Relative path of the stimulus image file",
        "HED": "Pathname/#, Description/Relative path of the stimulus image file"
    }
}
```
````

Non-categorical columns such as `response_time` and `stim_file` have a dictionary “HED” value
consisting of a HED string rather than another dictionary. This HED string must have a single `#` 
placeholder. The corresponding value in the spreadsheet column replaces the `#` when the event
annotation is assembled.

### 6.4.3. HED version in BIDS

The HED version is included as the value of the `"HEDVersion"` key in the 
`dataset_description.json` metadata file located at the top level in a BIDS dataset. 
HEDTools retrieve the appropriate HED schema directly from GitHub when needed. 
The following examples shows how a BIDS user specifies that HED version 8.0.0 is
used for a dataset called "A wonderful experiment". BIDS locates the appropriate 
version of the schema on GitHub and downloads it during the validation process. 
The following examples shows a simple `dataset_description.json`.

````{admonition} **Example:** BIDS dataset description using HED version 8.0.0.

```json
{
   "Name": "A wonderful experiment",
   "BIDSVersion": "1.4.0", 
   "HEDVersion": "8.0.0"
}
```
````


## 6.4.4 BIDS support in HED

HED provides a JavaScript validator in the [hed-javascript](https://github.com/hed-standard/hed-javascript) repository, which is available as an installable package via [npm](https://www.npmjs.com/). 
The [BIDS validator](https://github.com/bids-standard/bids-validator) 
incorporates calls to this package to validate HED tags in BIDS datasets.

The [hedtools](https://pypi.org/project/hedtools/) package includes
input functions that use [Pandas](https://pandas.pydata.org/) data frames to construct internal
representations of HED-annotated event files. 

HED schema developers generally do initial development of the schema using `.mediawiki` format.
The tools to convert schema between `.mediawiki` and `.xml` format are located in the 
`hed.schema` module of the 
[**hedtools**](https://github.com/hed-standard/hed-python/tree/master/hedtools) 
project of the hed-python repository located at  
[https://github.com/hed-standard/hed-python](https://github.com/hed-standard/hed-python). 
All conversions are performed by converting the schema to a `HedSchema` object. 
Then modules `wiki2xml.py` and `xml2wiki.py` provide top-level functions to perform these
conversions. 