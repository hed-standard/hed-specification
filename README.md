# Hierarchical Event Descriptors (HED)
HED is an evolving framework that facilitates the description and formal annotation of events identified in time series data, together with tools for validation and for using HED annotations in data search, extraction, and analysis. While HED can be used to annotate any type of event, the current HED community is focusing on annotation of event in human electrophysiological and behavioral data such as EEG, MEG, iEEG, eye-tracking, motion-capture, EKG, and audiovisual recording.

## HED annotation
HED annotations consist of comma-separated path strings. The path strings are selected from a tree-structured vocabulary. The vocabulary is available in several formats. The MediaWiki markdown format allows vocabulary developers to view and edit the vocabulary tree using a markdown language available in Wiki's and github repositories. All analysis and validation tools operate on an XML translation of the vocabulary markdown document. In addition, an expandable HTML viewer is available to help users explore the vocabulary.

The current version of HED (referred to as HED2 or HED-generation2) has semantic version numbers less than or equal to 7.x.x. The next generation HED (referred to as HED3 or HED-generation3) has semantic version numbers greater than or equal to 7.x.x. HED-generation3 represents a dramatic improvement in HED's capability to capture complex temporal relationships among events and the relationship of events to the task. HED-generation3 is under alpha release (HEDv8.0.0-alpha.1) and is open for community input and discussion.

## Viewing the HED vocabulary

### HED-generation3 vocabulary views
The latest version of the redesigned HED vocabulary is 8.0.0-alpha.1. This is a prerelease version pending community comments:

> [**Expandable html view HEDv8.0.0-alpha.1**](http://www.hedtags.org/display_hed_restruct.html?version=reduced) 

> [**Readable mediawiki view HEDv8.0.0-alpha.1**](https://github.com/hed-standard/hed-specification/blob/master/HED-generation3-schema.mediawiki) 

[**XML view HEDv8.0.0-alpha.1**](https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0-alpha.1.xml)  

### HED-generation2 vocabulary views

The latest version is of HED-generation2 is 7.1.2:
> [**Expandable html view (7.1.2)**](http://www.hedtags.org/display_hed.html?version=7.1.2)  

> [**Readable mediawiki view (7.1.2)**](https://github.com/VisLab/hed-specification/blob/master/HED-generation2-schema.mediawiki)

> [**XML view (7.1.2)**](https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED7.1.2.xml)  

## Documentation of the vocabulary

The documentation on this page refers specifically to the HED vocabulary and supporting tools.

### HED-generation3 white paper
The following white paper gives the history of HED development and the goals for HED-generation3

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2020, August 1).  
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).  
> https://doi.org/10.31219/osf.io/5fg73

### HED-generation3 specification document:

>[**Google doc with mapping of HED generation3 specification**](https://docs.google.com/document/d/1icp4fJyCqngSfYy1kPe7FJ-bqA8_Ei67oqn5--0vrDo/edit?usp=sharing)

### Mapping of HED-generation2 tags into HED-generation3 tags:

> [**Google doc with mapping of HED 7.1.1 into the restructured version**](https://docs.google.com/document/d/1MKjJzpxyZULXVRenFhiIvJ_-BpaEqHp3-bMvKxkcoL0/edit?usp=sharing) 


## Online tools

> [**HED-generation2 online spreadsheet validator**](http://visual.cs.utsa.edu/hed) 

> [**HED-generation3 online spreadsheet validator**](http://visual.cs.utsa.edu/hed3) 

> [**HED schema format converter**](http://visual.cs.utsa.edu/hedschema) 

## For HED validation

> [**Stable directory link for software requiring a HED schema for validation**](https://github.com/hed-standard/hed-specification/tree/master/hedxml)

> [**Stable  link for the latest version of the HED-generation2 schema is**](https://raw.githubusercontent.com/hed-standard/hed-specification/master/hedxml/HEDLatest.xml)


## Temporary notes:

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

