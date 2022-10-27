# Hierarchical Event Descriptors (HED)
### HED schema version 8.1.0 was released 5/23/2022.

**Note** This repository is primarily for managing the HED vocabulary. If you just 
want to annotate your data, please visit the [**HED examples**](https://readthedocs.org/projects/hed-examples/) documentation website. 

The full HED specification is available at the
[**HED specification**](https://hed-specification.readthedocs.io/en/latest/index.html) website. 

## What is HED?
HED is an evolving framework for the description and formal annotation of events 
identified in time series data. The HED ecosystem includes a structured vocabulary (HED schema)
together with tools for validation and for using HED annotations in data search, 
extraction, and analysis. While HED can be used to annotate any type of event, 
the current HED community focuses on annotation of events in human 
electrophysiological and behavioral data such as EEG, MEG, iEEG, eye-tracking, 
motion-capture, EKG, and audiovisual recording.
 

## Viewing the HED schema
The HED schema vocabulary can be viewed at:

> [**Expandable html view of the HED schema**](http://www.hedtags.org/display_hed.html) 

## HED white papers

The following white papers give an overview of HED and how it is used.

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2021).  
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).   
> Neuroinformatics Special Issue Building the NeuroCommons. Neuroinformatics https://doi.org/10.1007/s12021-021-09537-4.  
> [https://link.springer.com/article/10.1007/s12021-021-09537-4](https://link.springer.com/article/10.1007/s12021-021-09537-4).

> Robbins, K., Truong, D., Appelhoff, S., Delorme, A., & Makeig, S. (2021).  
> Capturing the nature of events and event context using Hierarchical Event Descriptors (HED).  
> NeuroImage Special Issue Practice in MEEG. NeuroImage 245 (2021) 118766.  
> [https://www.sciencedirect.com/science/article/pii/S1053811921010387](https://www.sciencedirect.com/science/article/pii/S1053811921010387).

## HED generations and schema versions 
The HED system has gone through two major restructurings since the original system
(HED-1G) was introduced. The following table shows the correspondence between 
HED schema version number and the design generation.

| schema version | release date | HED generation |
| --- | --- | --- |
| 1.0 | 2011-01-01 | HED-1G |
| 4.0.0 | 2016-02-25 | HED-2G |
| 8.0.0 | 2021-08-07 | HED-3G |


HED-1G introduced the basic ideas of annotation using path strings and is
still in use in the [HEADIT archive](https://headit.ucsd.edu). 

A major redesign of HED, HED-2G released in 2016 (4.0.0 <= schema version < 8.0.0), 
orthogonalized the vocabulary terms and introduced parentheses for grouping modifiers
with the terms they modify, resulting in much improved annotation. 

The second majoring restructuring, HED-3G (7.x.x < schema version), 
has resulted in a dramatic improvement in capabilities, including the 
introduction of annotations of condition variables and experimental 
design within the data as well as the ability to handle event context 
and events with temporal extent.

## HED semantic versioning

Starting with version 8.0.0, HED has adopted the following rules for
changing the semantic version *major.minor.patch*. These rules are
based on the assumption that the short form will not require retagging
for patch-level or minor-version changes. A validation error might occur
during for patch-level or minor-version changes for changes or
corrections in tag values or units.

| Change                          | Semantic-level | 
| ---------------------------------- | -------------- |
| Major addition to HED functionality     | Major  |
| Unit or unit class removed from node.   | Minor  |
| Tag deprecated in the schema.           | Minor  |
| New tag added to the schema.            | Minor  |
| New attribute added to schema.          | Minor  |
| New unit class or unit added to schema. | Minor  |
| New value class added to schema         | Minor |
| New unit class or value class added to node.   | Minor  |
| Node moved in schema without change in meaning. | Minor |
| Revision of description field in schema.        | Patch   |
| Correction of suggestedTag or relatedTag.       | Patch  |
| Correction of wiki syntax such as closing tags. | Patch |

**Note:** It is an official policy that once in a schema, a node will not be removed.
If a node becomes out-of-date, a `deprecated` tag will be added as an attribute.
Suggested replacement tags should be included in the node description.
A suggested replacement should be added to the tag_patch table.

##  HED specification versus the HED schema

The HED schema represents the allowed vocabulary for use in annotation.
The HED specification document specifies how tools should implement 
and validate various features of HED.

| HED spec version  | Specification release date | Applicable schema versions |
| ----------------- | -------------------------- | -------------------------- |
|   HEDSpec 3.0.0           |     Oct 27, 2022           |  <= HED 8.0.0                  |

The first official release of the HED specification, HEDSpec 3.0.0, marked the separation of
the versioning of the specification and the schema.
As new features are added to HED, the specification is updated,
but the vocabulary represented by the HED schema is usually not affected.

## HED revision process

As modifications to the HED schema are proposed, they are entered into the
[PROPOSED](PROPOSED.md) document for discussion.
Approved changes and corrections are first made in a working version of the
schema that is located in the [prelease directory](https://github.com/hed-standard/hed-specification/tree/master/prelease) and can be viewed
using the following viewer:

> [**Expandable html view of the prerelease HED schema**](https://www.hedtags.org/display_hed_prelease.html) 

Upon final review, the new HED schema is released and moved to the
[hedxml directory](https://github.com/hed-standard/hed-specification/tree/master/hedxml).

## HED schema details
_HED schema_ is the structured vocabulary from which HED annotations base on. HED annotations consist of comma-separated path strings,
selected from the schema. In the newest versions of HED,
all individual nodes in the vocabulary are unique, so users can annotate
by simply giving the last node in the path string rather than the entire path
string: *Red* instead of *Attribute/Sensory/Sensory-property/Visual/Color/CSS-color/Red-color/Red*.

This repository contains the HED schema specification, where discussions on schema terms and syntax are held via Github issue mechanism and where HED-supporting tools can find machine-readable format of the schema. The HED schema is available in MediaWiki and XML. 

The MediaWiki markdown format, stored in 
[`hedwiki`](https://github.com/hed-standard/hed-specification/tree/master/hedwiki),
allows vocabulary developers to view and edit the vocabulary tree using a 
human-readable markdown language available in Wikis and on GitHub repositories. 
In addition, an expandable non-editable 
[HTML viewer](http://www.hedtags.org/display_hed.html)  is available
to help users explore the vocabulary.

All analysis and validation tools operate on an XML translation of the vocabulary 
markdown document, stored in [`hedxml`](https://github.com/hed-standard/hed-specification/tree/master/hedxml). 


## Further documentation

The documentation on this page refers specifically to the HED vocabulary and supporting tools. Additional documentation is available on:

> [**HED organization website**](https://www.hedtags.org)

All of the HED software is open-source and organized into various repositories on the HED standards organization website:

> [**HED organization github repository**](https://github.com/hed-standard)


## Tools to help with HED annotations
The GUI tool [_CTagger_](https://github.com/hed-standard/CTagger) is available to help users with the annotation process. CTagger can be used as a standalone application or can be called from EEGLAB via the [hedtools plug-in](https://github.com/hed-standard/hed-matlab) to annotate an EEGLAB dataset/STUDY directly. Please refer to the linked repositories for more documentation on how to start HED-tagging using CTagger.

## Web-based HED tools

The current web-based HED tools include an online validator of spreadsheets (Excel or tsv)
containing HED tags. Schema tools are available for converting HED schema specifications between `.mediawiki` and
`.xml` formats. 
Also available is a tool for checking for duplicate nodes in schema and for converting
HED annotations between short and long forms.  

The current web-based HED tools are located at [https://hedtags.ucsd.edu/hed](https://hedtags.ucsd.edu/hed).  

The tools can be run locally using the `runserver.py` function the hedweb module
of the [hed-python](https://github.com/hed-standard/hed-python) repository of 
[hed-standard](https://github.com/hed-standard).

## Stable links for HED validation

> [**Stable directory link for software requiring a HED schema for validation**](https://github.com/hed-standard/hed-specification/tree/master/hedxml)

> [**Stable link for the latest version of the HED**](https://raw.githubusercontent.com/hed-standard/hed-specification/master/hedxml/HEDLatest.xml)


## HED-3G library schema

HED-3G supports library schema, which are specialized vocabularies used in conjunction with the
base vocabulary to support annotation of specialized datasets. Communities may develop and submit
library schema.  HED library schema are hosted on the repository: 
[https://github.com/hed-standard/hed-schema-library](https://github.com/hed-standard/hed-schema-library)

### HED-3G document mapping to defined terms in existing ontologies

The following working document describes the origin of the descriptions associated with individual nodes in the HED-3G hierarchy. Many terms appear in the NCIT ontology (National Cancer Institute Thesaurus OBO edition).

> [**Google doc with mapping of HED-3G term descriptions to existing ontology terms**](https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing) 
