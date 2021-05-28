# Hierarchical Event Descriptors (HED)
HED is an evolving framework for the description and formal annotation of events identified in time series data. The HED ecosystem includes a structured vocabulary together with tools for validation and for using HED annotations in data search, extraction, and analysis. While HED can be used to annotate any type of event, the current HED community focuses on annotation of events in human electrophysiological and behavioral data such as EEG, MEG, iEEG, eye-tracking, motion-capture, EKG, and audiovisual recording.

## HED annotation
HED annotations consist of comma-separated path strings. The path strings are selected from a tree-structured vocabulary. The vocabulary is available in several formats. The MediaWiki markdown format allows vocabulary developers to view and edit the vocabulary tree using a markdown language available in Wikis and on github repositories. All analysis and validation tools operate on an XML translation of the vocabulary markdown document. In addition, an expandable HTML viewer is available to help users explore the vocabulary.

The current version of HED (referred to as HED-2G or HED-2nd generation) has semantic version numbers less than or equal to 7.x.x. The next generation HED (referred to as HED-3G or HED-3rd generation) has semantic version numbers greater than or equal to 7.x.x. HED-3G represents a dramatic improvement in HED's capability for capturing complex temporal relationships among events and the relationships of events to the task. HED-3G is under alpha release (HED8.0.0-alpha.2) and is open for community input and discussion.  The current version of the HED-3G specification can be viewed in the [HED Hierarchical Event Descriptors working 3G specification](https://docs.google.com/document/d/1icp4fJyCqngSfYy1kPe7FJ-bqA8_Ei67oqn5--0vrDo/edit?usp=sharing).

## Viewing the HED vocabulary

### HED-3G vocabulary views
The latest version of the redesigned HED vocabulary is 8.0.0-alpha.1. This is a prerelease version pending community comments:

> [**Expandable html view of HED8.0.0-alpha.2**](http://www.hedtags.org/display_hed.html?version=8.0.0-alpha.2) 

> [**Readable mediawiki view of HED8.0.0-alpha.2**](https://github.com/hed-standard/hed-specification/blob/master/HED-generation3-schema-8.0.0-alpha.2.mediawiki) 

> [**XML view of HED8.0.0-alpha.2**](https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0-alpha.2.xml)  

> [**XML view of HED8.0.0-alpha.3**] (https://github.com/hed-standard/hed-specification/blob/master/hedxml-test/HED8.0.0-alpha.3.xml)  Under development

### HED-2G vocabulary views

The latest version is of HED-2G is 7.2.0:
> [**Expandable html view of HED7.2.0**](http://www.hedtags.org/display_hed.html?version=7.2.0)  

> [**Readable mediawiki view of HED7.2.0**](https://github.com/hed-standard/hed-specification/blob/master/HED-generation2-schema-7.2.0.mediawiki)

> [**XML view of HED7.2.0**](https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED7.2.0.xml)  

## Documentation of the vocabulary

The documentation on this page refers specifically to the HED vocabulary and supporting tools. Additional documentataion is available on:

> [**HED organization website**](https://www.hedtags.org)

All of the HED software is open-source and organized into various repositories on the HED standards organization website:

> [**HED organization github repository**](https://github.com/hed-standard)

### HED-3G white papers
The following white paper gives the history of HED development and the goals for HED-3G

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2020, August 1).  
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).  
> https://doi.org/10.31219/osf.io/5fg73

> Robbins, K., Truong, D., Appelhoff, S., Delorme, A., & Makeig, S. (2021, May 7). 
> Capturing the nature of events and event context using Hierarchical Event Descriptors (HED). 
> BioRxiv, 2021.05.06.442841. 
> https://doi.org/10.1101/2021.05.06.442841


### HED-3G specification document

>[**Google doc with current version of the HED-3G specification**](https://docs.google.com/document/d/1icp4fJyCqngSfYy1kPe7FJ-bqA8_Ei67oqn5--0vrDo/edit?usp=sharing)

### Mapping of HED-2G tags into HED-3G tags

> [**Google doc with mapping of HED 7.1.2 into HED 8.0.0-alpha.1**](https://docs.google.com/document/d/1MKjJzpxyZULXVRenFhiIvJ_-BpaEqHp3-bMvKxkcoL0/edit?usp=sharing) 


## Web-based HED tools

The current web-based HED tools include an online validator of spreadsheets (Excel or tsv)
containing HED tags. Schema tools are available for converting HED schema specifications between `.mediawiki` and
`.xml` formats. Also available is a tool for checking for duplicate nodes in schema.  

The current web-based HED tools are located at [https://hedtags.ucsd.edu/hed](https://hedtags.ucsd.edu/hed).  

The tools can be run locally using the `runserver.py` function the hedweb module
of the [hed-python](https://github.com/hed-standard/hed-python) repository of 
[hed-standard](https://github.com/hed-standard).

## Stable links for HED validation

> [**Stable directory link for software requiring a HED schema for validation**](https://github.com/hed-standard/hed-specification/tree/master/hedxml)

> [**Stable  link for the latest version of the HED-generation2 schema**](https://raw.githubusercontent.com/hed-standard/hed-specification/master/hedxml/HEDLatest.xml)

## HED-3G library schema

HED-3G supports library schema, which are specialized vocabularies used in conjunction with the
base vocabulary to support annotation of specialized datasets. Communities may develop and submit
library schema.  HED library schema are hosted on the repository 
[https://github.com/hed-standard/hed-schema-library](https://github.com/hed-standard/hed-schema-library)
