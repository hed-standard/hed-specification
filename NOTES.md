
## Maintenance notes:

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

