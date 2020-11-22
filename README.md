# Hierarchical Event Descriptors (HED)
HED is an evolving framework for the description and formal annotation of events identified in time series data. The HED ecosystem includes a structured vocabulary together with tools for validation and for using HED annotations in data search, extraction, and analysis. While HED can be used to annotate any type of event, the current HED community focuses on annotation of events in human electrophysiological and behavioral data such as EEG, MEG, iEEG, eye-tracking, motion-capture, EKG, and audiovisual recording.

## HED annotation
HED annotations consist of comma-separated path strings. The path strings are selected from a tree-structured vocabulary. The vocabulary is available in several formats. The MediaWiki markdown format allows vocabulary developers to view and edit the vocabulary tree using a markdown language available in Wikis and on github repositories. All analysis and validation tools operate on an XML translation of the vocabulary markdown document. In addition, an expandable HTML viewer is available to help users explore the vocabulary.

The current version of HED (referred to as HED2 or HED-generation2) has semantic version numbers less than or equal to 7.x.x. The next generation HED (referred to as HED3 or HED-generation3) has semantic version numbers greater than or equal to 7.x.x. HED-generation3 represents a dramatic improvement in HED's capability for capturing complex temporal relationships among events and the relationships of events to the task. HED-generation3 is under alpha release (HEDv8.0.0-alpha.1) and is open for community input and discussion.

## Viewing the HED vocabulary

### HED-generation3 vocabulary views
The latest version of the redesigned HED vocabulary is 8.0.0-alpha.1. This is a prerelease version pending community comments:

> [**Expandable html view of HEDv8.0.0-alpha.1**](http://www.hedtags.org/display_hed_restruct.html?version=reduced) 

> [**Readable mediawiki view of HEDv8.0.0-alpha.1**](https://github.com/hed-standard/hed-specification/blob/master/HED-generation3-schema.mediawiki) 

> [**XML view of HEDv8.0.0-alpha.1**](https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0-alpha.1.xml)  

### HED-generation2 vocabulary views

The latest version is of HED-generation2 is 7.1.2:
> [**Expandable html view of HEDv7.1.2**](http://www.hedtags.org/display_hed.html?version=7.1.2)  

> [**Readable mediawiki view of HEDv7.1.2**](https://github.com/VisLab/hed-specification/blob/master/HED-generation2-schema.mediawiki)

> [**XML view of HEDv7.1.2**](https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED7.1.2.xml)  

## Documentation of the vocabulary

The documentation on this page refers specifically to the HED vocabulary and supporting tools. Additional documentataion is available on:

> [**HED organization website**](http://hedtags.org)

All of the HED software is open-source and organized into various repositories on the HED standards organization website:

> [**HED organization github repository**](http://github.com/hed-standard)

### HED-generation3 white paper
The following white paper gives the history of HED development and the goals for HED-generation3

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2020, August 1).  
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).  
> https://doi.org/10.31219/osf.io/5fg73

### HED-generation3 specification document

>[**Google doc with mapping of HED generation3 specification**](https://docs.google.com/document/d/1icp4fJyCqngSfYy1kPe7FJ-bqA8_Ei67oqn5--0vrDo/edit?usp=sharing)

### Mapping of HED-generation2 tags into HED-generation3 tags

> [**Google doc with mapping of HED 7.1.1 into the restructured version**](https://docs.google.com/document/d/1MKjJzpxyZULXVRenFhiIvJ_-BpaEqHp3-bMvKxkcoL0/edit?usp=sharing) 


## Online tools

> [**HED-generation2 online spreadsheet validator**](http://visual.cs.utsa.edu/hed) 

> [**HED-generation3 online spreadsheet validator**](http://visual.cs.utsa.edu/hed3) 

> [**HED schema format converter**](http://visual.cs.utsa.edu/hedschema) 

## For HED validation

> [**Stable directory link for software requiring a HED schema for validation**](https://github.com/hed-standard/hed-specification/tree/master/hedxml)

> [**Stable  link for the latest version of the HED-generation2 schema**](https://raw.githubusercontent.com/hed-standard/hed-specification/master/hedxml/HEDLatest.xml)
