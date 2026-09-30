[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7869149.svg)](https://doi.org/10.5281/zenodo.7869149) [![Documentation](https://img.shields.io/badge/docs-hedtags.org-blue.svg)](https://www.hedtags.org/hed-specification)

# HED specification

HED (Hierarchical Event Descriptors) is an evolving framework for the description and formal annotation of events and other information in data. The HED ecosystem includes a structured vocabulary (HED schema) together with tools for validation and for using HED annotations in data search, extraction, and analysis.

While HED can be used to annotate any type of data, the current HED community focuses on annotation of events in human neuroimaging and behavioral data such as EEG, MEG, iEEG, fMRI, eye-tracking, motion-capture, EKG, and audiovisual recording.

**Note** This repository is primarily for managing the HED ecosystem specification, including information on the format and rules for HED vocabularies (schemas) as well as rules for how tools should treat HED-annotated data.

## HED specification vs schema

The HED schema represents the allowed vocabulary for use in annotation. The HED specification document specifies how tools should implement and validate various features of HED.

| Specification<br>Version | Release date | Schema<br>versions | Description                                                           |
| ------------------------ | ------------ | ------------------ | --------------------------------------------------------------------- |
| 3.0.0                    | Oct 27, 2022 | ≥ 8.0.0            | - First official release                                              |
| 3.1.0                    | Apr 5, 2023  | ≥ 8.0.0            | - Cleanup and clarification<br>- JSON unit tests keyed to errors.     |
| 3.2.0                    | May 12, 2023 | ≥ 8.2.0            | - Inset tag<br>- Curly braces                                         |
| 3.3.0                    | Jul 5, 2024  | ≥ 8.2.0            | - Lazy partnering of libraries<br>- Specification of ontology format. |

The first official release of the HED specification, HED specification 3.0.0, marked the separation of the versioning of the specification and the schema.

As new features are added to the HED infrastructure, the specification is updated, but the vocabulary represented by the HED schema is usually not affected.

In a similar fashion, many modifications of the HED schema and corresponding vocabulary do not require an update of the HED tools or the HED specification.

Several other aspects of HED annotation are being planned, but their specification has not been fully determined. These aspects are not contained in this specification document, but rather are contained in ancillary working documents which are open for discussion. These ancillary specifications include the HED working document on [spatial annotation](https://docs.google.com/document/u/0/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/edit) and the HED working document on [task annotation](https://docs.google.com/document/u/0/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/edit).

## HED white papers

The following white papers give an overview of HED and how it is used.

> Makeig, S. and K. Robbins (2024).\
> Events in context—The HED framework for the study of brain, experience and behavior.\
> Front. Neuroinform. Vol. 18 Research Topic 15 Years of impact, open neuroscience.\
> [https://doi.org/10.3389/fninf.2024.1292667](https://doi.org/10.3389/fninf.2024.1292667).

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2022).\
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).\
> Neuroinformatics Special Issue Building the NeuroCommons. Neuroinformatics 20, pages463–481. [https://link.springer.com/article/10.1007/s12021-021-09537-4](https://link.springer.com/article/10.1007/s12021-021-09537-4).

> Robbins, K., Truong, D., Appelhoff, S., Delorme, A., & Makeig, S. (2021).\
> Capturing the nature of events and event context using Hierarchical Event Descriptors (HED).\
> NeuroImage Special Issue Practice in MEEG. NeuroImage 245 (2021) 118766.\
> [https://www.sciencedirect.com/science/article/pii/S1053811921010387](https://www.sciencedirect.com/science/article/pii/S1053811921010387).

## Other resources

The JSON tests now have their own GitHub repository [hed-tests](https://github.com/hed-standard/hed-tests) and are no longer housed in this repository.

If you want to annotate your data or want general information about HED, please visit the [**HED resources**](https://www.hedtags.org/hed-resources/) documentation website. If you are a developer of a new HED vocabulary (schema) please see the [Schema developer's guide](https://www.hedtags.org/hed-schemas/developer_guide.html).

The latest version of the HED specification is available at the [**HED specification**](https://www.hedtags.org/hed-specification).

The official library schemas are now housed on the [**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

## Stable links for HED validation

> [**Stable directory link for software requiring a HED schema for validation**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml)

> [**Stable link for the latest version of the HED**](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HEDLatest.xml)

> [**Machine-readable character sets**](https://www.hedtags.org/hed-specification/_static/character_sets.json)

The character sets of section 2.2 of the specification (the names that `allowedCharacter` may use, each as a regular expression usable from Python and JavaScript, plus the default character sets of the standard value classes and the structural characters of HED strings) are published as `docs/source/_static/character_sets.json`. Validators read that file rather than copying the table. The table in `docs/source/02_Terminology.md` is generated from it: edit the JSON, then run `python scripts/generate_character_table.py`; `python scripts/generate_character_table.py --check` (run by CI) fails when the table or the file is off.
