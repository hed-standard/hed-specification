# hed-specification
Hierarchical Event Descriptor (HED) specification. 

### HED notes
This branch (HED-restructure) is the development branch of HED (a.k.a. HED-Phase 3). If you are tagging a dataset with
the current version of HED (a.k.a. HED-Phase 2) you want the Master branch. Human-readable versions of the HED schema
are presented in `.mediawiki` format. The machine-readable versions are in `.xml`. There is also a `.html` expandable view which
makes it easier to see what the tags are. You can read a white paper on the development of HED-Phase 3 at:

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2020, August 1). 
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).
> https://doi.org/10.31219/osf.io/5fg73

### HED if you are tagging data (latest release of HED)
The current version (latest release) of HED is HED 7.0.5 can be found on the Master branch of this repository. However,
the version in the process of being released is HED 7.1.1. Here are the views of HED 7.1.1 in different forms:

> [**Expandable html view (7.1.1)**](http://www.hedtags.org/display_hed.html?version=7.1.1)  

> [**Readable mediawiki view (7.1.1)**](https://github.com/VisLab/hed-specification/blob/master/HED-schema.mediawiki)

> [**XML view (7.1.1)**](https://github.com/VisLab/hed-specification/blob/master/hedxml/HED7.1.1.xml)  

### HED if you are a HED schema developer
The HED schema developers are working on the HED-restructure branch of the repository and the working version of the HED-phase 3 schema is 
the reduced schema. Here are the views of the HED restructuring in progress:

> [**Readable mediawiki view**](https://github.com/hed-standard/hed-specification/blob/HED-restructure/HED-schema-reduced.mediawiki) 

> [**Expandable html view reduced schema**](http://www.hedtags.org/display_hed_restruct.html?version=reduced) 

> [**Google doc with mapping of HED 7.1.1 into the restructured version**](https://docs.google.com/document/d/1MKjJzpxyZULXVRenFhiIvJ_-BpaEqHp3-bMvKxkcoL0/edit?usp=sharing) 


### For HED validation
The stable link for software requiring the HED schema for validation is
https://github.com/hed-standard/hed-specification/tree/master/hedxml

The stable link for the latest version of the HED schema is
https://raw.githubusercontent.com/hed-standard/hed-specification/master/hedxml/HEDLatest.xml


#### Versioning during restructuring
HED is undergoing a major reorganization on the HED-restructure branch.
We use a variation of semantic versioning during restructuring to facilitate incremental testing and implementation. Versions will be of the form vreX.Y.Z

* X: MAJOR (requires validator or CTAGGER code to be modified) 
* Y: MINOR (requires data tagged under previous version to be retagged, but validator does not change needs additions to remap file) 
* PATCH (does not require data tagged under previous version to be retagged nor does it require validator code to be modified) 

#### General procedure for releases

Tags and releases are not part of the ordinary github commit process.  We are doing these releases so that developers of the validators and converters can develop new code without disturbing the existing infrastructure. These will later be merged when the restructuring process is complete.


##### Versioning of the developing infrastructure
The auto-changelog and other things assume adherence to semantic versioning.  We have two distinct development branches that are in process:  
   1.  HEDVx.y.z-restruct is being developed on the HED-restructure branch and consists of restructuring the HED schema without modifying the validators and parsers.
   2.  HEDVx.y.z.-devunit is being developed to better handle SI units as well as multiples and submultiples so that it will be compatible with BIDS.

The procedures described below are only for the transition well HED is being restructured.  The current version of HED as supported by BIDS and the online HED validator has not changed and is in the master branch of this repository.

##### Merge process
Update process:  
   1.  Fork the HED-restructure branch of the hed-standard/hed-specification repository to your github account.  
   2.  To avoid confusion, I have been renaming this repository hed-specification-working in my account.  
   3.  Clone this repository locally to make your changes and then push to your working repository.
   4.  When you are done, do a pull request for hed-specification-working to the actual repository on hed-standard.  Be sure to indicate whether this is a change that is patch level, minor, or major. Make sure that Nima, Dung, and Kay are reviewers of the pull request.
   5.  When all reviewers have approved, the request is merged.  

##### Adding annotated tags to define the version
After a fork has been merged, Kay will create a new release so that we can control testing.  This is the process:  
    1. Clone hed-standard/hed-specification (HED-restructure) locally.
    2. Add an annotated tag with the new version that is associated with the merge commit:: 
```
git tag -a v1.2.1-restruct   fe03asg  -m "Release v1.1.0-restruct removes IDs from non Attribute subtrees"
```
The `fe03asg` is the leading part of the hash string for the commit that we are going to associate a new version number with. Now we have to push the tag to github since the tags are stored separately from the respository:

```
git push origin --tags
```

##### Create the new release on github
Once this is done, Kay will create a release associated with this tag on github.  This is done through the GUI on github.

##### Generate the changelog:
At this point, we will generate a final change log for this release using auto-changelog.  This is an npm module.

  1.  Clone the HED-restructure branch of the hed-standard/hed-specification repository to your local machine.  
  2.  In the top level directory of the repository, execute the following:  
```
auto-changelog --commit-limit false --sort-commits date-desc
```

  3.  Edit the CHANGELOG.md that is created to make sure everything is in order.  
  4.  Commit locally and push to the HED-restructure branch of hed-standard/hed-specification.
  

**NOTE:** The only time we should be directly pushing to hed-standard/hed-specification is during the version/CHANGELOG process.   

Eventually we might look into continuous integration.

