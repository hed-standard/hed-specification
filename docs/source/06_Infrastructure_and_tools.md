# 6. Infrastructure and tools

The HED infrastructure includes functions written in Python, Matlab,
and JavaScript that support the use of HED in applications.
This section describes the expected behavior of the HED infrastructure and
its integration into other systems such as [**BIDS**](https://bids.neuroimaging.io/).

This section also specifies how HED-compliant tools should handle various aspects of HED.
In general, tools should either explicitly call HED validation to assure that the input
tag strings are valid or should make explicit that they assume the HED has already been validated.
Most tools will use the later approach. 

See [**3.2. HED annotation format**](./03_HED_formats.md#32-hed-annotation-format)
for more detailed specifications of HED formats. 

See [**4. Basic annotation**](./04_Basic_annotation.md) and 
[**5. Advanced annotation**](./05_Advanced_annotation.md) for examples and usage.

## 6.1. Basic tag handling

HED-compliant tools should be able to a handle HED string in its equivalent forms
and using various valid syntax as described in this section.

### 6.1.1. Tag forms

````{warning} 
HED-compliant tools should be able to handle tags in **long-form**,
**short-form** or any valid **intermediate-form**.

````

Tools may assume that validated HED tags do not have leading, trailing, or
consecutive forward slashes in their names.

Tools should not distinguish between variations in case for the same tag term.
Only units must have their cases preserved.


### 6.1.2. Parentheses and commas

Tools may assume that validated HED strings have no duplicates, empty tags,
empty groups (parentheses enclosing only whitespace), or mismatched parentheses.

Grouping with parentheses in HED means that the tags are associated.

````{warning} 
HED-compliant tools should be able to handle arbitrary correctly **nested parentheses**
and correctly distinguish differences in grouping.

````

(tag-ordering-anchor)=
### 6.1.3. Tag ordering

Any ordering of HED tags and HED tag groups at the same level within a HED tag group is equivalent.

Any ordering of top-level HED tags and HED tag groups in a HED string is equivalent.

````{warning} 
HED-compliant tools should not rely on the order that HED tags appear within a string or group during processing.
````

### 6.1.4. Definitions



````{warning} 
HED-compliant tools should be able to expand, shrink, or remove definitions.
````



In addition to being property formed, validated HED strings will correspond to
terms in the schemas under which they were validated.

Tools may assume that the individual tags within the string have the property units
and are in the proper format.


## 6.2 File-level handling

Dataset formats such as [**BIDS**](https://bids.neuroimaging.io/) (Brain Imaging Data Structure)
allow users to provide HED tags in multiple places.
For example, BIDS dataset event files often use local codes to identify event markers
in tabular (`events.tsv`) files,
and then provide dictionaries called JSON sidecars to map local codes to annotations. 

The introduction of definitions and temporal scope for HED versions >= 8.0.0
has added additional complexity to validation and processing.
Instead of being able to validate the HED string for each event individually,
HED validators must now also check consistency across all events in the data-recording. 
This validation requires multiple passes through of the assembled HED tags
associated with the data-recording.

Since `Definition` tags can appear anywhere in the event annotations for a data recording, 
an initial scan must be made to assemble all definitions for a data recording and 
to make sure that the definition names are unique. 

Tools may assume that validated datasets have all of their definitions.
However, tools should be sure to extract all embedded HED definitions before processing.
Tools should also make sure that all needed definitions are available for processing.

Tools should make explicit whether they support temporal scope.
Tools that support temporal scope should be able to add scoped event
information added to the `Event-context` tag group of the intermediate events upon request.

Tools should make explicit whether they support insertion of actual events
for `Delay` tag expansions and for the offsets of `Duration` tags.
This information will allow analysts to call HED tools that support these operations
as a preamble to processing.

## 6.3. HED support of BIDS

[**BIDS**](https://bids.neuroimaging.io/) (Brain Imaging Data Structure) is a 
widely-adopted specification along with supporting tools for organizing and 
describing brain imaging and behavioral data.
BIDS dataset events are stored in tab-separated tabular files whose names end in `events.tsv`.
HED's use of tabular files and sidecars closely aligns with BIDS and its requirements.
HED has been incorporated into the BIDS standard as the mechanism for annotating
tabular files. 

### 6.3.1. BIDS tabular files

BIDS supports HED annotation of events. BIDS events appear in tab-separated value (`events.tsv`)
files in various places in the dataset hierarchy. BIDS event files must have an `onset` column
and a `duration` column. The following shows an excerpt from a BIDS event file:

````{admonition} **Example:** Excerpt from a BIDS event file.

```
onset  duration  trial_type  response_time  HED
1.2    0.6       go          1.435          Label/Starting-point, Quiet 
5.6    0.6       stop        1.739          n/a
```
````


The first two columns in a BIDS events file are required to be `onset` and `duration`, respectively.
The `onset` is the time of the event marker,
while the `duration` represents the duration of some aspect of the event.

The `trial_type` column contains categorical values, while the `response_time` and `stim_file`
columns contain non-categorical values. In theory `stim_file` could be considered a categorical 
column if there were just a few possible images, but this would not be common usage. 
BIDS allows an optional column named `HED` to contain HED strings relevant for the event instance.
In the above example, the first row `HED` column contains `Label/Starting-point, Quiet`,
while the second row contains `n/a`, indicating that entry should be ignored.

Processing tools read these event files and create their own event representation. 
The Python version of HEDTools uses the Pandas `DataFrame` for its low-level representations. 
For MATLAB programs, the dataset events are often held in `struct` arrays.

In EEGLAB, for example, the events for an EEG data recording appear in the `EEG.event` 
structure array. The time of the event is given in frames in the `EEG.event.latency` 
field for data that has not been epoched. 


### 6.3.2. BIDS sidecars

BIDS also recommends data dictionaries in the form of JSON sidecars to document
the meaning of the data in the event files.
HEDTools supports BIDS dataset format, where event metadata is contained 
in compatibly-named sidecars.
See the [**example sidecar**](./03_HED_formats.md#3291-hed-sidecar-entries) in Chapter 3
for an explanation of the different sidecar entries.

### 6.3.3. Annotation assembly

HED tools are available to assemble the annotations associated with each row in
a tabular file using its `HED` column and associated sidecar information.

For example, the annotations for the first row of the 
[**example event file**](./06_Infrastructure_and_tools.md#631-bids-tabular-files)
above can be assembled using the
[**example sidecar**](./03_HED_formats.md#3291-hed-sidecar-entries) in Chapter 3
to give the following annotation:

````{admonition} Example assembled HED annotation for one event marker.

> `Sensory-event`, `Visual-presentation`, (`Square`, `Blue`), 
> (`Delay/1.435 ms`, `Agent-action`, (`Experiment-participant`, (`Press`, `Mouse-button`))),
> `Label/Starting-point`, `Quiet` 

````
The process is to look up the appropriate row annotation for each column in the sidecar and append these with an annotation in the `HED` column if available.

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

It is possible to include library schema in the version as shown by the
following example:

```json

{
  "Name": "A great experiment",
  "BIDSVersion": "1.7.0",
  "HEDVersion": ["8.1.0", "sc:score_0.0.1"]
}
```

which shows that annotations use HED standard schema version 8.1.0
and `score` library schema version 0.0.1.
Tags from the `score` library must be prefixed with `sc:` for this version
specification.

The following version specification is also valid:

```json

{
  "Name": "A great experiment",
  "BIDSVersion": "1.7.0",
  "HEDVersion": ["st:8.1.0", "score_0.0.1"]
}
```
For this specification tags from the standard schema must be prefixed
by `st:`, while tags from the `score` library are unprefixed.
The `sc:` and `st:` prefixes are arbitrary (usually short) alphabetic strings
chosen by the annotation and are specific to each dataset based on its
version specification.



````{warning} 
HED-compliant tools must be able to handle multiple schemas and prefixed
tags.
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
The tools to convert schema between `.mediawiki` and `.xml` format are located 
in the `hed.schema` module of the 
[**hedtools**](https://github.com/hed-standard/hed-python/tree/master/hedtools) 
project of the [**hed-python**](https://github.com/hed-standard/hed-python) GitHub repository. 
All conversions are performed by converting the schema to a `HedSchema` object. 
Then modules `wiki2xml.py` and `xml2wiki.py` provide top-level functions to perform these
conversions. 