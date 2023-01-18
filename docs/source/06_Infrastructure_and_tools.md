# 6. Infrastructure and tools

The HED infrastructure includes functions written in Python, Matlab,
and JavaScript that support the use of HED in applications.
This section describes the expected behavior of the HED infrastructure and
its integration into other systems such as [**BIDS**](https://bids.neuroimaging.io/).

This section also specifies how HED-compliant tools should handle various aspects of HED.
In general, tools should either explicitly call HED validation to assure that the input
tag strings are valid or should make explicit that they assume the HED has already been validated.
Most tools will use the later approach. 

## 6.1. Basic tag handling

HED-compliant tools should be able to a handle HED string in its equivalent forms
and using various valid syntax as described in this section.

### 6.1.1. Tag forms

````{warning} 
HED-compliant tools should be able to handle tags in **long-form**,
**short-form** or any valid **intermediate-form**.

````
(parenthesized-hed-strings-anchor)=

### 6.1.2. Parentheses

Grouping with parentheses in HED means that the tags are associated.

````{warning} 
HED-compliant tools should be able to handle arbitrary correctly **nested parentheses**
and correctly distinguish differences in grouping.

````

(tag-ordering-anchor)=
### 6.1.3. Tag ordering

Any ordering of HED tags at the same level within a HED string is equivalent.

````{warning} 
HED-compliant tools should not rely on the order that HED tags appear within a string during processing.
````

### 6.1.4. Definitions



````{warning} 
HED-compliant tools should be able to expand, shrink, or remove definitions.
````

Tools may assume that validated HED strings have no duplicates, empty tags, empty groups, or
mismatched parentheses.

In addition to being property formed, validated HED strings will correspond to
terms in the schemas under which they were validated.

Tools may assume that the individual tags within the string have the property units
and are in the property format.


## 6.2 File-level handling

Dataset formats such as [**BIDS**](https://bids.neuroimaging.io/) (Brain Imaging Data Structure)
allow users to provide HED tags in multiple places.
For example, if a study uses local codes to represent different types of events,
The dataset event files often use local codes to identify event markers
and then provide some format of dictionary mapping local codes to annotations. 

The introduction of definitions and temporal scope has added additional complexity 
to validation and processing. Instead of being able to validate the HED string for each event individually,
third generation HED validators must also check consistency across all events in the 
data-recording. This validation requires multiple passes through of the assembled HED tags
associated with the data-recording.

Since *Definition* tags can appear anywhere in the event annotations for a data recording, 
an initial scan must be made to assemble all definitions for a data recording and 
to make sure that the definition names are unique. 

To validate temporal scope, the validator must assure that each *Onset* and *Offset* tag 
is associated with an appropriately defined label. The validator must also check to make 
sure that *Onset* and *Offset* tags are properly matched within the data recording.


Each event that is within the temporal scope of a scoped event, should have the scoped event
information added to the *Event-context* tag group of the intermediate event upon request.
*Delay* tag expansions as insertions of actual events should also be supported. 
*Duration* tag expansion in which offset events should be inserted should also be supported. 
The HED tools should provide this expansion capability as well as a standardized representation
of events in a data recording to enable tools to use a standard API for accessing tag information.


## 6.3. HED support of BIDS

[**BIDS**](https://bids.neuroimaging.io/) (Brain Imaging Data Structure) is a 
widely-adopted specification along with supporting tools for organizing and 
describing brain imaging and behavioral data.
BIDS dataset events are stored in tab-separated tabular files whose names end in `events.tsv`.
HED's use of tabular files and sidecars closely aligns with BIDS and its requirements.
HED has been incorporated into the BIDS standard as the mechanism for annotating
tabular files. 

### 6.3.1. BIDS tabular files

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


The first two columns in a BIDS events file are the `onset` and `duration`, respectively.
The `onset` is the time of the event marker,
while the `duration` represents the duration of some aspect of the event.


### 6.3.2. BIDS sidecars

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

### 6.3.3. HED version in BIDS

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

### 6.3.4. HED in the BIDS validator

HED provides a JavaScript validator in the [**hed-javascript**](https://github.com/hed-standard/hed-javascript) repository, which is available as an installable package via [**npm**](https://www.npmjs.com/). 
The [**BIDS validator**](https://github.com/bids-standard/bids-validator) 
incorporates calls to this package to validate HED tags in BIDS datasets.

### 6.3.5. HED python tools

The [**hedtools**](https://pypi.org/project/hedtools/) package includes
input functions that use [**Pandas**](https://pandas.pydata.org/) data frames to construct internal
representations of HED-annotated event files. 

HED schema developers generally do initial development of the schema using `.mediawiki` format.
The tools to convert schema between `.mediawiki` and `.xml` format are located in the 
`hed.schema` module of the 
[**hedtools**](https://github.com/hed-standard/hed-python/tree/master/hedtools) 
project of the [**hed-python**](https://github.com/hed-standard/hed-python) GitHub repository. 
All conversions are performed by converting the schema to a `HedSchema` object. 
Then modules `wiki2xml.py` and `xml2wiki.py` provide top-level functions to perform these
conversions. 