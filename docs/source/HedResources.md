# HED resources


## HED publications

Explanation of the history, development, and motivation for third generation HED: 

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2021).  
> Building FAIR functionality: Annotating events in time series data using Hierarchical Event Descriptors (HED).  
> Neuroinformatics Special Issue Building the NeuroCommons. Neuroinformatics https://doi.org/10.1007/s12021-021-09537-4.  
> [https://link.springer.com/article/10.1007/s12021-021-09537-4](https://link.springer.com/article/10.1007/s12021-021-09537-4).

Detailed case study in using HED-3G for tagging:

> Robbins, K., Truong, D., Appelhoff, S., Delorme, A., & Makeig, S. (2021, May 7).   
> Capturing the nature of events and event context using Hierarchical Event Descriptors (HED).  
> NeuroImage Special Issue Practice in MEEG. NeuroImage  245  (2021)  118766.  
> [https://www.sciencedirect.com/science/article/pii/S1053811921010387](https://www.sciencedirect.com/science/article/pii/S1053811921010387).

## HED schema viewers

The HED schema is usually developed in `.mediawiki` format and converted to XML for use by tools.
However, researchers wishing to tag datasets will find both of these views hard to read. 
For this reason, we provide links to three versions of the schema. The expandable
HTML viewer is easier to navigate. Annotators can also use CTAGGER, which includes a schema viewer
and tagging hints.

`````{list-table} HED web-based schema vocabulary viewers.
:header-rows: 1
:widths: 20 50

* - **Viewer**
  - **Link**
* - **standard HED schema**
  -
* - Expandable HTML	
  - [https://www.hedtags.org/display_hed.html](https://www.hedtags.org/display_hed.html)
* - Expandable prerelease HTML	
  - [https://www.hedtags.org/display_hed_prelease.html](https://www.hedtags.org/display_hed_prelease.html)
* - Mediawiki	
  - [https://github.com/hed-standard/hed-specification/blob/master/hedwiki/HED8.0.0.mediawiki](https://github.com/hed-standard/hed-specification/blob/master/hedwiki/HED8.0.0.mediawiki)
* - XML	
  - [https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0.xml](https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0.xml)
* - **Score library schemas**
  - 
* - Expandable HTML
  - [https://www.hedtags.org/display_hed_score.html](https://www.hedtags.org/display_hed_score.html)
* - Expandable prelease HTML
  - [https://www.hedtags.org/display_hed_score_prerelease.html](https://www.hedtags.org/display_hed_score_prerelease.html)
* - Mediawiki	
  - [https://github.com/hed-standard/hed-schema-library/blob/main/library_schemas/score/hedwiki/HED_score_0.0.1.mediawiki](https://github.com/hed-standard/hed-schema-library/blob/main/library_schemas/score/hedwiki/HED_score_0.0.1.mediawiki)
* - XML	
  - [https://github.com/hed-standard/hed-schema-library/blob/main/library_schemas/score/hedxml/HED_score_0.0.1.xml](https://github.com/hed-standard/hed-schema-library/blob/main/library_schemas/score/hedxml/HED_score_0.0.1.xml)
`````  

## HED websites

The following is a summary of the HED-related websites:


`````{list-table}
:header-rows: 1
:widths: 20 50

* - Description
  - Site
* - HED organization website
  - [https://www.hedtags.org](https://www.hedtags.org)
* - HED specification
  - [https://hed-specification.readthedocs.io/en/latest/index.html](https://hed-specification.readthedocs.io/en/latest/index.html)
* - HED examples and tutorials
  - [https://hed-examples.readthedocs.io/en/latest/index.html](https://hed-examples.readthedocs.io/en/latest/index.html)
* - CTAGGER executable jar
  - [https://github.com/hed-standard/hed-java/raw/master/ctagger.jar](https://github.com/hed-standard/hed-java/raw/master/ctagger.jar)
* - **Repositories**
  -
* - HED organization
  - [https://github.com/hed-standard](https://github.com/hed-standard)
* - HED specification
  - [https://github.com/hed-standard/hed-specification](https://github.com/hed-standard/hed-specification)
* - HED examples and datasets
  - [https://github.com/hed-standard/hed-examples](https://github.com/hed-standard/hed-examples)
* - HED Python tools
  - [https://github.com/hed-standard/hed-python](https://github.com/hed-standard/hed-python)
* - HED Javascript code
  - [https://github.com/hed-standard/hed-javascript](https://github.com/hed-standard/hed-javacript)
* - HED Matlab code and EEGLAB support
  - [https://github.com/hed-standard/hed-matlab](https://github.com/hed-standard/hed-matlab)
* - HED web deployment
  - [https://github.com/hed-standard/hed-web](https://github.com/hed-standard/hed-web)
* - HED-2G support
  - [https://github.com/hed-standard/hed2-python](https://github.com/hed-standard/hed2-python)
* - CTAGGER resources
  - [https://github.com/hed-standard/CTagger](https://github.com/hed-standard/CTagger)
* - **Online tools**
  -
* - HED tools
  - [https://hedtools.ucsd.edu/hed](https://hedtools.ucsd.edu/hed)
* - HED-2G support
  - [https://hedtools.ucsd.edu/hed2](https://hedtools.ucsd.edu/hed2)
`````


## HED working documents

Mapping of HED terms and their descriptions to known ontologies is:

> HED-3G Working Document on Ontology mapping
> [https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing](https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing)

Two other working documents hold portions of the HED-3G specification that are under development 
and will not be finalized for Release 1:

> HED-3G Working Document on Spatial Annotation
> [https://docs.google.com/document/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/view?usp=sharing](https://docs.google.com/document/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/view?usp=sharing)

> HED-3G Working Document on Task Annotation
> [https://docs.google.com/document/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/view?usp=sharing](https://docs.google.com/document/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/view?usp=sharing)
