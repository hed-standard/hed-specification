# hed-specification
Hierarchical Event Descriptor (HED) specification

### HED notes
The current version of HED is maintained in the wiki associated with
https://github.com/hed-standard/hed-specification
 
The latest and selected past XML versions of the HED schema are generated
from this wiki and stored in the hedxml directory of this repository. 

The stable link for software requiring the HED schema for validation is
https://github.com/hed-standard/hed-specification/tree/master/hedxml

The stable link for the latest version of the HED schema is
https://raw.githubusercontent.com/hed-standard/hed-specification/master/hedxml/HEDLatest.xml

### HED restructuring
HED is undergoing a major reorganization on the HED-restructure branch.

#### Versioning during restructuring

We will use a variation of semantic versioning to facilitate incremental testing and implementation. Versions will be of the form vreX.Y.Z

* X: MAJOR (requires validator or CTAGGER code to be modified) 
* Y: MINOR (requires data tagged under previous version to be retagged, but validator does not change needs additions to remap file) 
* PATCH (does not require data tagged under previous version to be retagged nor does it require validator code to be modified) 

#### HEDremap.tsv
This file two-column, tab-separated file lists the replacement for tags in HED2 with the tags in HED3 if they need to be changed. The purpose of this file is to facilitate retagging datasets that have already been tag.  Use -- in column two to indicate a tag that should simply be deleted.  If a series of changes need to be made for a given tag, then use a -- in column 1 to indicate this line is a continuation.  

**Example 1:**  
Event/ID/3	(Event, Attribute/ID/3)
