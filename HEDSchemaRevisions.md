(hed-schema-revisions-anchor)=
## HED schema revisions

As modifications to the HED schema are proposed, they are entered into the
[PROPOSED](PROPOSED.md) document for discussion.
Approved changes and corrections are first made in a working version of the
schema that is located in the [prelease directory](https://github.com/hed-standard/hed-specification/tree/master/prelease) and can be viewed
using the following viewer:

> [**Expandable html view of the prerelease HED schema**](https://www.hedtags.org/display_hed_prelease.html) 

Upon final review, the new HED schema is released and moved to the
[hedxml directory](https://github.com/hed-standard/hed-specification/tree/master/hedxml).

### HED schema details
_HED schema_ is the structured vocabulary from which HED annotations base on. HED annotations consist of comma-separated path strings,
selected from the schema. In the newest versions of HED,
all individual nodes in the vocabulary are unique, so users can annotate
by simply giving the last node in the path string rather than the entire path
string: *Red* instead of *Attribute/Sensory/Sensory-property/Visual/Color/CSS-color/Red-color/Red*.

This repository contains the HED schema specification, where discussions on schema terms and syntax are held via Github issue mechanism and where HED-supporting tools can find machine-readable format of the schema. The HED schema is available in MediaWiki and XML. 

The MediaWiki markdown format, stored in 
[`hedwiki`](https://github.com/hed-standard/hed-specification/tree/master/hedwiki),
allows vocabulary developers to view and edit the vocabulary tree using a 
human-readable markdown language available in Wikis and on GitHub repositories. 
In addition, an expandable non-editable 
[HTML viewer](http://www.hedtags.org/display_hed.html)  is available
to help users explore the vocabulary.

All analysis and validation tools operate on an XML translation of the vocabulary 
markdown document, stored in [`hedxml`](https://github.com/hed-standard/hed-specification/tree/master/hedxml). 


### Further documentation

The documentation on this page refers specifically to the HED vocabulary and supporting tools. Additional documentation is available on:

> [**HED organization website**](https://www.hedtags.org)

All of the HED software is open-source and organized into various repositories on the HED standards organization website:

> [**HED organization github repository**](https://github.com/hed-standard)
