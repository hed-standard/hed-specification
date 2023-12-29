# 6. Infrastructure and tools

The HED infrastructure includes libraries written in Python, Matlab,
and JavaScript that support the use of HED in validation and/or applications.
This section describes the expected behavior of the HED infrastructure and
its integration into other systems such as [**BIDS**](https://bids.neuroimaging.io/).

In general, tools should either explicitly call HED validation to assure that the input
tag strings are valid or should make explicit that they assume the HED has already been validated.
Most tools will use the later approach. 

See [**3.2. Annotation formats**](./03_HED_formats.md#32-annotation-formats)
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

In addition to being property formed, validated HED strings will correspond to
terms in the schemas under which they were validated.

Tools should not distinguish between variations in case for the same tag term.
Only units must have their cases preserved.

Tools may assume that the individual tags within validated HED strings have 
values of the proper form and that the units, if provided, are consistent with
any unit classes

**Note**:  At this time it is not required that terms with specified unit classes
always have associated units.  However, it is implicitly assumed that if
the units are omitted in this case, the value has the default units.

See [**3.2.2. Tag forms**](./03_HED_formats.md#322-tag-forms) for more information
on tag forms.

### 6.1.2. Parentheses and commas

Tools may assume that validated HED strings have no duplicates, empty tags,
empty groups (parentheses enclosing only whitespace), or mismatched parentheses.

Grouping with parentheses in HED indicates that the tags are associated.
Where possible, parentheses should be preserved.

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

HED definitions should only appear in sidecars in dummy entries
or in an accompanying definition list.
Actual `Definition` groups should not appear in the `HED` column of event files.


## 6.2. File-level handling

Dataset formats such as [**BIDS**](https://bids.neuroimaging.io/) (Brain Imaging Data Structure)
allow users to provide HED tags in multiple places.
For example, BIDS dataset event files often use local codes to identify event markers
in tabular (`events.tsv`) files
and then provide dictionaries called JSON sidecars to map local codes to annotations. 

The introduction of definitions and temporal scope for HED versions >= 8.0.0
has added additional complexity to validation and processing.
Instead of being able to validate the HED string for each event individually,
HED validators must now also check consistency across all events in the data-recording.

Tools should make explicit whether they support temporal scope.
Tools that support temporal scope should be able to add scoped event
information to the `Event-context` tag group of the intermediate events upon request.

Tools should make explicit whether they support insertion of actual events
for `Delay` tag expansions and for the offsets of `Duration` tags.
This information will allow analysts to call HED tools that support these operations
to appropriately modify event files as a preamble to processing
if the tool does not support these tags.

## 6.3. HED support of BIDS

[**BIDS**](https://bids.neuroimaging.io/) (Brain Imaging Data Structure) is a 
widely-adopted specification and supporting tools for organizing and 
describing brain imaging and behavioral data.

### 6.3.1. BIDS tabular files

HED has been incorporated into the BIDS standard as the mechanism for annotating
BIDS tabular files, which are tab-separated value files whose first line has the column names.
A BIDS tabular file has extension `.tsv` and can be optionally accompanied by a 
similarly named `.json` file (i.e., a sidecar) containing metadata for the file.

The most common types of BIDS tabular files are shown in the following table.

(tabular-types-anchor)=
| Ends with            | Time? | A row represents                                   |
|----------------------|-------|----------------------------------------------------| 
| `_events.tsv`        | Yes   | Markers on the timeline of another file.           | 
| `_participants.tsv`  | No    | Metadata about one dataset subject.                |
| `_scans.tsv`         | No    | Metadata about one dataset recording.              | 
| `_beh.tsv`           | No    | A measurement not associated with an `onset`. |  
| `_samples.tsv `      | No    | Properties of a particular sample (e.g., tissue).  |
| `phenotype/xxx_.tsv` | No    | A measurement from a particular participant.       |  

HED treats tabular files such as (e.g., `_events.tsv` files) whose first column has 
the name `onset` as expressing markers on a timeline.
These timeline files allow `Onset`, `Inset`, and `Offset` tags in their
annotations and receive additional [**file-level processing**](./03_HED_formats.md#32104-file-level-processing) to assure that these tags are properly
matched. 

**Tabular files that do not represent timelines are not permitted to use
`Onset`, `Inset`, and `Offset` tags in their annotations.**
See [**ONSET_OFFSET_INSET_ERROR**](./Appendix_B.md#onset_offset_inset_error)
for additional information.

The following shows an excerpt from a BIDS event file:

````{admonition} **Example:** Excerpt from a BIDS _events.tsv file.

```
onset  duration  trial_type  response_time  HED
1.2    0.6       go          1.435          Label/Starting-point, Quiet 
5.6    0.6       stop        1.739          n/a
```
````

The first two columns in a BIDS event file are required to be `onset` and `duration`, respectively.
The `onset` is the time in seconds of an event marker relative to the start of its corresponding
data recording, 
while the `duration` represents the duration in seconds of some aspect of the event.
The remaining columns in this event file are optional.

BIDS reserves an optional column named `HED` to contain HED strings relevant for the instance
represented by that row.
In the above example, the first row `HED` column contains `Label/Starting-point, Quiet`,
meaning that the event that starts at time 1.2 has these particular annotations
in addition to annotations contributed by any relevant sidecars.
The `HED` column in the second row contains `n/a`, indicating that entry should be ignored.
In this case only annotations from applicable sidecars are applied.

HED annotations can also be associated with entries in other columns of the event file
through an associated JSON sidecar as described in the next section.


### 6.3.2. BIDS timeseries

BIDS also includes another type of file with extension `.tsv` that represents 
continuous timeseries data. 
For example, the motion capture `_motion.tsv` files give samples from
channels of a motion capture apparatus,
while physiological data files
 `_physio.tsv` and `_stim.tsv` represent continuous 
physiological recordings such as cardiac and respiratory signals. 
These tabular files do not have column headers,
but rather use other files to define the column names.
**BIDS currently does not support HED in these types of files.**


### 6.3.3. BIDS sidecars

BIDS also recommends data dictionaries in the form of JSON sidecars to document
the meaning of the data in the event files.
HEDTools supports BIDS dataset format, where event metadata is contained 
in compatibly-named sidecars.
See the [**example sidecar**](./03_HED_formats.md#3291-sidecar-entries) in Chapter 3
for an explanation of the different sidecar entries.

### 6.3.4. Annotation assembly

HED tools are available to assemble the annotations associated with each row in
a tabular file using its `HED` column and the sidecar information associated
with other columns of the events file.

For example, the annotations for the first row of the 
[**example event file**](./06_Infrastructure_and_tools.md#631-bids-tabular-files)
above can be assembled using the
[**example sidecar**](./03_HED_formats.md#3291-sidecar-entries) in Chapter 3
to give the following annotation:

````{admonition} Example assembled HED annotation for one event marker.

> `Sensory-event`, `Visual-presentation`, (`Square`, `Blue`), 
> (`Delay/1.435 ms`, `Agent-action`, (`Experiment-participant`, (`Press`, `Mouse-button`))),
> `Label/Starting-point`, `Quiet` 

````
The process is to look up the appropriate row annotation for each column in the sidecar and append these with an annotation in the `HED` column if available.

### 6.3.5. HED version in BIDS

The HED version is included as the value of the `"HEDVersion"` key in the 
`dataset_description.json` metadata file located at the top level in a BIDS dataset. 
HEDTools retrieve the appropriate HED schema directly from GitHub 
or from locally cached versions when needed. 

The following example `dataset_description.json` specifies that HED version 8.0.0 is
used for a dataset called "A wonderful experiment". 

````{admonition} **Example:** BIDS dataset description using HED version 8.0.0.

```json
{
   "Name": "A wonderful experiment",
   "BIDSVersion": "1.4.0", 
   "HEDVersion": "8.0.0"
}
```
````

It is possible to include library schema in the HED version specification of the
`dataset_description.json` file as shown by the following example:

````{admonition} **Example:** BIDS dataset description using HED version 8.1.0 and score library 1.0.0.
```json

{
  "Name": "A great experiment",
  "BIDSVersion": "1.7.0",
  "HEDVersion": ["8.1.0", "sc:score_1.0.0"]
}
```
````

The version specification indicates that tags from the `score` library must be prefixed with `sc:` 
namespace identifier in dataset HED annotations.

The prefix notation (such as the `sc:` prefix for the `score` library in the previous example is required when more than one schema is used in the annotation.
However, namespace prefixes can be used with the standard schema as well as library schemas
as illustrated by the following example.

````{admonition} **Example:** Prefixed standard schema in BIDS dataset description version specification.

```json

{
  "Name": "A great experiment",
  "BIDSVersion": "1.7.0",
  "HEDVersion": ["st:8.1.0", "score_1.0.0"]
}
```
````

For this specification tags from the standard schema must be prefixed
by `st:`, while tags from the `score` library are unprefixed.
The `sc:` and `st:` namespace prefixes are arbitrary (usually short) alphabetic strings
chosen by the annotation and are specific to each dataset based on its
version specification.



````{warning} 
HED-compliant tools must be able to handle multiple schemas and prefixed
tags.
````


### 6.3.6. HED in the BIDS validator

HED provides a JavaScript validator in the [**hed-javascript**](https://github.com/hed-standard/hed-javascript) repository, which is available as an installable package via [**npm**](https://www.npmjs.com/). 
The [**BIDS validator**](https://github.com/bids-standard/bids-validator) 
incorporates calls to this package to validate HED tags in BIDS datasets.

### 6.3.7. HED python tools

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