# HED specification

**Note** This repository is primarily for managing the HED ecosystem specification,
including information on the format and rules for HED vocabularies (schemas)
as well as rules for how tools should treat HED-annotated data.

If you just 
want to annotate your data, please visit the [**HED examples**](https://readthedocs.org/projects/hed-examples/) documentation website. 
If you are a schema developer

The full HED specification is available at the
[**HED specification**](https://hed-specification.readthedocs.io/en/latest/index.html) website or as a PDF document at  

## About HED
HED (Hierarchical Event Descriptors) is an evolving framework for the description and 
formal annotation of events and other information in data.
The HED ecosystem includes a structured vocabulary (HED schema)
together with tools for validation and for using HED annotations in data search, 
extraction, and analysis.

While HED can be used to annotate any type of data, 
the current HED community focuses on annotation of events in human 
neuroimaging and behavioral data such as EEG, MEG, iEEG, fMRI, eye-tracking, 
motion-capture, EKG, and audiovisual recording.
 

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


##  HED specification versus the HED schema

The HED schema represents the allowed vocabulary for use in annotation.
The HED specification document specifies how tools should implement 
and validate various features of HED.

| HED specification version  | Release date | HED schema versions |
| ----------------- | -------------------------- | -------------------------- |
|   HED Specification 3.0.0           |     Oct 27, 2022           |  >= HED 8.0.0                  |

The first official release of the HED specification, HED Specification 3.0.0, 
marked the separation of the versioning of the specification and the schema.

As new features are added to the HED infrastructure, the specification is updated,
but the vocabulary represented by the HED schema is usually not affected.

In a similar fashion, many modifications of the HED schema and corresponding vocabulary
do not require an update of the HED tools or the HED specification.

## Stable links for HED validation

> [**Stable directory link for software requiring a HED schema for validation**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml)

> [**Stable link for the latest version of the HED**](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HEDLatest.xml)

