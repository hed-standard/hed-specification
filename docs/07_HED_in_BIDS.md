# 7. HED in BIDS

This section gives an overview of the HED tools. Additional details and links to specific 
tools are available in **Section 8**.


## 7.1. Short and long forms

Tools that are third-generation HED-compliant must be able to handle both short-form and 
long-form versions of HED strings. Analysis tools often need to transform all HED tags to long
form before processing. To this end, mapping functions are being developed in Python, Matlab,
and JavaScript. These libraries also provide mapping from long form to short form. 
As illustrated in the previous sections, the short form is much more readable and compact. 

## 7.2. Event file format (BIDS)

Dataset events are often represented using spreadsheets either in `.tsv` or Excel format. 
The rows of each spreadsheet correspond to events, while the columns contain identifying
information pertaining to the events.  The first row of each spreadsheet usually contains 
column names that document what each column represents. Usually one column contains the 
time of the event. Other columns may contain categorical values, other values, or HED strings.
Categorical column values are chosen from a small, explicitly defined subset. 
Value columns may contain numeric values or other types of values such as file names. 
HED tools assume that event files are spreadsheets, either in BIDS (`.tsv`) format or 
Excel format.

The HED tools require that each column of an event file contains items of the same class 
(categorical or value) and that value columns contain items of the same basic type. Files not
satisfying these requirements may need additional processing before being handled by HED tools.
BIDS (Brain Imaging Data Structure) datasets do have event files that satisfy these criteria.

BIDS uses tab-separated-value (`.tsv`) format for event files, with a required `onset` column
containing the time of the event in seconds. BIDS also requires a `duration` column for event
files. 

````{admonition} **Example:** Excerpt from a BIDS event file:

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


## 7.3. Sidecar format (BIDS)

Systems that handle HED annotation should be capable of defining and using metadata dictionaries
in JSON format to specify HED tags applicable to the values in different columns of an event
file.  BIDS uses JSON dictionaries called sidecars in a particular format. HEDTools assume 
that dictionaries for event metadata are contained in BIDS-compatible sidecars.

BIDS allows the tagging of both categorical and non-categorical columns in these sidecars 
as explained in the [HED appendix](https://github.com/bids-standard/bids-specification/blob/master/src/99-appendices/03-hed.md) of the BIDS
specification. Internally, EEGLAB and CTAGGER use mapping objects that are stored in the EEG
structure. However, these mapping options can be written to or read from BIDS JSON sidecars. 

Each events file spreadsheet column containing categorical values may also have a categorical
dictionary that documents the meaning of the data in that column. HED also provides for the HED
tagging of non-categorical columns as explained below. The following example shows the JSON
sidecar format for annotating the same event file of the previous section. The `"HED"` key 
for the `"trial_type"` column indexes the categorical dictionary associated with the 
`trial_type` column in the event file. 

````{admonition} **Example:** JSON sidecar for annotating the columns of an events file.

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


## 7.4. Levels of validation

Validation of HED annotations is an essential step in using HED for large-scale, reproducible
analysis. Third-generation HED encourages a more detailed and useful documentation of events 
and provides mechanisms for mapping the interrelationships of events and task intent. 
The additional annotation power also requires more extensive validation to assure consistency
across annotations. HED-validators are provided in both Python and JavaScript. 
There is also a MATLAB wrapper for the Python validator functions.

There are five levels of validation: tag level, string level, dictionary level, event level, 
and data-recording level. Previous generations of HED only required validation at the first 
four of these. Since third-generation HED can document relationships across events, 
it also requires an additional level to validate cross-event relationships. 
Validation can also be categorized as syntactic or semantic. Syntactic validation, 
which occurs mainly at the HED tag and HED string levels, tests that the tags are 
properly formed, independently of the HED schema or purpose of the tags. Semantic 
validation tests that the tags are used correctly and that they comply with the relevant schema.
Syntactic validation is usually done initially during the parsing of the HED strings 
into HED tags.


### 7.4.1. HED tag level validation

HED tag level validation checks each individual HED tag against its associated schema. 
The long-form tag must be in the schema. HED tags that take a value (have a # child in the 
schema) must have values that only contain appropriate characters. If the HED tag `#` has a
*unitClass* attribute, the units must comply with those of the specified *unitClass*. 
If the HED tag has additional nodes beyond the leaf node in the schema, the *extensionAllowed* 
attribute must be in effect for the leaf node. 


### 7.4.2. HED string level validation

HED string level validation focuses on the proper formation of HED strings and tag-groups 
within the HED strings. Syntactic HED string validation includes matching of parentheses and
proper delimiting of HED tags by commas. Semantic HED string validation includes verification
that HED definitions have the proper form.


### 7.4.3. HED dictionary level validation

HED dictionary validation assumes that the dictionaries have been written in the JSON format 
of [Section 7.3: Sidecar format (BIDS)](07_HED_in_BIDS.md#73-sidecar-format-bids). 
The validation is similar to HED string evaluation, but the error messages are keyed to
dictionary location rather than to line numbers in the event file or spreadsheet. 
The validator checks that there is exactly one `#` in the HED string annotation associated 
with each non-categorical column. The `#` placeholder should correspond 
to a `#` in the HED schema, indicating that the parent tag expects a value. 
If the placeholder is followed by a units designator, the validator checks that 
these units are consistent with the unit class of the
corresponding `#` in the schema.  The units are not mandatory.


### 7.4.4. HED event-level validation

Dataset formats such as BIDS (Brain Imaging Data Structure) allow users to provide HED tags 
in multiple places. For example, if a study uses local codes to represent different types of
events, the dataset specification often allows users to use the local codes when listing the
events and then provide some format of dictionary mapping local codes to tags. 
During event level validation, all of these tags must be assembled into a HED string 
representing the full HED annotation for that event. 

Several tag attributes are validated at this stage. The expanded event-level HED string
annotating an event must include all tags with the *required* attribute and only one copy
of each tag with the *unique* attribute.


### 7.4.5. HED recording-level validation

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


## 7.5. Analysis tools

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


## 7.6. HED-annotated data in BIDS

[BIDS (Brain Imaging Data Structure)](https://bids.neuroimaging.io/is ) is a specification 
along with supporting tools for organizing and describing brain imaging and behavioral data. 
BIDS supports HED annotation of events. BIDS events appear in tab-separated value (`_events.tsv`)
files in various places in the dataset hierarchy. BIDS event files must have an `onset` column
and a `duration` column. The example in {ref}`**Section 7.2**<bids_file_format>` shows such a
BIDS event file. BIDS also recommends data dictionaries in the form of JSON sidecars to document
the meaning of the data in the event files. The example in Section 7.2 also includes a JSON data 
dictionary.  

HED provides a JavaScript validator in the [hed-javascript](https://github.
com/hed-standard/hed-javascript) repository, which is available as an installable package via 
[npm](https://www.npmjs.com/). The [BIDS validator](https://github.
com/bids-standard/bids-validator) incorporates calls to this package to validate HED tags in BIDS
datasets.

The [hedtools](https://github.com/hed-standard/hed-python/tree/master/hedtools) package includes
input functions that use [Pandas](https://pandas.pydata.org/) data frames to construct internal
representations of HED-annotated event files. Plans are underway to make this package available
on the [PyPI](https://pypi.org/) package index for easy installation.

