[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7869149.svg)](https://doi.org/10.5281/zenodo.7869149)
[![Documentation](https://img.shields.io/badge/docs-hedtags.org-blue.svg)](https://www.hedtags.org/hed-specification)


# HED specification

**Note** This repository is primarily for managing the HED ecosystem specification,
including information on the format and rules for HED vocabularies (schemas)
as well as rules for how tools should treat HED-annotated data.

If you want to annotate your data, please visit the [**HED resources**](https://www.hedtags.org/hed-resources/) documentation website. 
If you are a developer of a new HED vocabulary (schema) please see the
[Schema developer's guide](https://www.hedtags.org/hed-resources/HedSchemaDevelopersGuide.html).

The latest version of the HED specification is available at the
[**HED specification**](https://www.hedtags.org/hed-specification).

The official library schemas are now housed on the
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

The most current officially released version of the HED specification can be found at [**HED specification (PDF)**](<https://raw.githubusercontent.com/hed-standard/hed-specification/main/hedspec/HEDSpecification_3_3_0.pdf>`)

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


> Makeig, S. and K. Robbins (2024).      
> Events in context—The HED framework for the study of brain, experience and behavior.    
> Front. Neuroinform. Vol. 18 Research Topic 15 Years of impact, open neuroscience.  
> [https://doi.org/10.3389/fninf.2024.1292667]( https://doi.org/10.3389/fninf.2024.1292667).

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2022).  
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).   
> Neuroinformatics Special Issue Building the NeuroCommons. Neuroinformatics 20, pages463–481.
> [https://link.springer.com/article/10.1007/s12021-021-09537-4](https://link.springer.com/article/10.1007/s12021-021-09537-4).

> Robbins, K., Truong, D., Appelhoff, S., Delorme, A., & Makeig, S. (2021).  
> Capturing the nature of events and event context using Hierarchical Event Descriptors (HED).  
> NeuroImage Special Issue Practice in MEEG. NeuroImage 245 (2021) 118766.  
> [https://www.sciencedirect.com/science/article/pii/S1053811921010387](https://www.sciencedirect.com/science/article/pii/S1053811921010387).


##  HED specification versus the HED schema

The HED schema represents the allowed vocabulary for use in annotation.
The HED specification document specifies how tools should implement 
and validate various features of HED.

| Specification<br>Version  | Release date | Schema<br>versions | Description |
| ---------- | ---------------- | -------------- | --------------  |
|   3.0.0    |    Oct 27, 2022   |  &ge; 8.0.0  | - First official release  |
| 3.1.0  | Apr 5, 2023 |  &ge; 8.0.0  | - Cleanup and clarification<br>- JSON unit tests keyed to errors. |

The first official release of the HED specification, HED Specification 3.0.0, 
marked the separation of the versioning of the specification and the schema.

As new features are added to the HED infrastructure, the specification is updated,
but the vocabulary represented by the HED schema is usually not affected.

In a similar fashion, many modifications of the HED schema and corresponding vocabulary
do not require an update of the HED tools or the HED specification.

Several other aspects of HED annotation are being planned, but their specification has 
not been fully determined. These aspects are not contained in this specification document, 
but rather are contained in ancillary working documents which are open for discussion. 
These ancillary specifications include the HED working document on 
[spatial annotation](https://docs.google.com/document/u/0/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/edit) 
and the HED working document on 
[task annotation](https://docs.google.com/document/u/0/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/edit).



## Stable links for HED validation

> [**Stable directory link for software requiring a HED schema for validation**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml)

> [**Stable link for the latest version of the HED**](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HEDLatest.xml)

