# 7. Library schemas

## 7.1. Why library schemas?

The variety and complexity of events in electrophysiological experiments make full 
documentation challenging. As more experiments move out of controlled laboratory environments
and into less controlled virtual and real-world settings, the terminology required to adequately
describe events has the potential to grow exponentially.  

In addition, experiments in any given subfield can create pressures to add 
overly-specific terms and jargon to the schema hierarchy—for example, adding musical 
terms to tag events in music-based experiments, video markup terms for experiments 
involving movie viewing, traffic terms for experiments involving
virtual driving, and so forth. 

Clinical fields using neuroimaging also have their own specific
vocabularies for describing data features of clinical interest (e.g., seizure, sleep stage IV).
Including these discipline-specific terms quickly makes the standard HED schema unwieldy and less
usable by the broader user community.

Third generation HED addressed the problem of vocabulary bloat by introducing
**HED library schemas** to organize discipline-specific terminology. 
To use a programming analogy, when programmers write a Python module, 
the resulting code does not become part of the Python language or core libraries. 
Instead, the module becomes part of a library used in conjunction with
core modules of the programming language.

A HED library schema contains the specialized vocabulary terms needed
for event annotation in a specialized area.
An example of such a library is the [**HED SCORE schema**](https://hed-schemas.readthedocs.io/en/latest/hed_score_schema.html) for annotation of EEG by clinicians.

## 7.2. Partnered schemas

HED library schemas were originally assumed to be **standalone** vocabularies,
complete with all the needed schema attributes and properties.
These standalone library schemas were usually used in conjunction with the 
HED standard schema, and the tags from the two different vocabularies
were distinguished by prefixing the tags from one of the vocabularies with `xx:`.
Here `xx:` is called the **namespace** for that schema within the annotation
and is chosen by the annotator.

**Partnered library schemas** were introduced in HED specification version 3.2.0
and are supported by HED standard schema versions &ge; 8.2.0. 

A partnered library schema version is tied to a specific version of the HED standard schema
as specified in its header.
A given library schema version is either **partnered** or **standalone**.

### 7.2.1. Partnered files

The XML file corresponding to a partnered library schema is a single, unified schema
containing the information from both the library and its standard schema partner
and validated as an integrated whole. 

This XML merged schema file is downloaded and used by tools. 
Downstream tools see a single schema and can process it with no special handling.
The following example shows the XML header for merged TESTLIB library version 2.0.0.

````{admonition} XML header for TESTLIB library 2.0.0 partnered with 8.2.0 (merged).
```xml
<?xml version="1.0" ?>
<HED library="testlib" version="2.0.0" withStandard="8.2.0">

```
````
The canonical filename for this `.xml` file is `HED_testlib_2.0.0.xml`.
This file is always stored in the libraries `hedxml` directory in the
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.
For the above example, the directory is [**library_schemas/testlib/hedxml**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/testlib/hedxml).


As with any HED schema, schema builders develop and maintain their schema in
MediaWiki mark-down format and use tools to convert to XML.
The schema developer's version is unmerged, 
containing only the information specific to the library schema.
The following example shows the header for the `.mediawiki` developer's version
of a partnered library schema.

````{admonition} Mediawiki header for TESTLIB library 2.0.0 partnered with 8.2.0 (unmerged).
```html
HED library="testlib" version="2.0.0" withStandard="8.2.0" unmerged="true"
```
````

The canonical filename for this `.mediawiki` file is 
`HED_testlib_2.0.0_unmerged.mediawiki`.

Tools also support an alternative form of the `.mediawiki` library schema
containing all the information in the merged schema (a mirror to the XML),
which may be useful for debugging, but is usually not explicitly created.

The following table summarizes the different partnered library schema formats
and their uses. File names and link examples are specifically for the TESTLIB
library. For other libraries, substitute the library name for the word *testlib*.

| Format | Merged<br/>status | Canonical filename | Handling |
| ------ | ------------- | ------------------ | -------- |
| XML    |   merged    |  `HED_testlib_2.0.0.xml` | Stored in library [**hedxml**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/testlib/hedxml).<br/>Used by tools. |
| XML    |   unmerged    |  `HED_testlib_2.0.0_unmerged.xml` | Can be generated but is never<br/> stored on [**hed-schemas**](https://github.com/hed-standard/hed-schemas).<br/>Not used, but available for completeness. |
| MediaWiki    |   merged    |  `HED_testlib_2.0.0.mediawiki` | Usually not stored in [**hedwiki**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/testlib/hedwiki).<br/>Possibly used during<br/>schema development. |
| MediaWiki   |   unmerged    |  `HED_testlib_2.0.0_unmerged.mediawiki` | Working format for developers<br/>Should be stored in [**hedwiki**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/testlib/hedwiki). |

### 7.2.2. Partnered formats

There are four significant differences between merged and unmerged MediaWiki formats:
1. The unmerged version has the `unmerged="true"` attribute in its header line.
<br/>&nbsp;<br/>
2. The unmerged version should only include the auxiliary sections (e.g., unit classes,
unit modifiers, value classes, schema attributes, and schema properties)
that it explicitly extends.
<br/>&nbsp;<br/>
3. In the unmerged schema, nodes with the `rooted=XXX` schema attribute must be top-level tags,
and `XXX` must correspond to a node in the standard schema. In the merged schema, nodes with the `rooted=XXX` schema attribute are placed directly
under the standard schema node `XXX`.
<br/>&nbsp;<br/>
4. Nodes in the unmerged version cannot have the `inLibrary` attribute.
In contrast, nodes from the library schema are given the `inLibrary==YYY`
attribute during the merging process. Here `YYY` is the library schema name.

The following excerpt from an unmerged TESTLIB library schema in MediaWiki format shows a library schema node (`Data-mode`) rooted to `Statistical-value` in the
standard schema. 

````{admonition} Example of a rooted node in an unmerged schema in MediaWiki format.
```html
                      . . .
'''Data-mode''' <nowiki>{rooted=Statistical-value}[A value that occurs most often in data.]</nowiki>   
* <nowiki># {takesValue, valueClass=numericClass}</nowiki> 
                      . . .
```
````
Notice that the indentation asterisks (*) indicate that the node's children are at the first level.
In the merged schema, these are adjusted accordingly as shown in the following:

````{admonition} When merged with the standard schema, the indentation levels are adjusted.
```html 
                      . . .
*** Statistical-value <nowiki>{extensionAllowed}[A value based on or employing the principles of statistics.]</nowiki>              
                       . . .
**** Data-minimum <nowiki>[The smallest possible quantity.]</nowiki>
***** <nowiki># {takesValue, valueClass=numericClass}</nowiki>
**** Data-mode''' <nowiki>{inLibrary=testlib, rooted}[A value that occurs most often in data.]</nowiki>   
***** <nowiki># {takesValue, valueClass=numericClass, inLibrary=testlib}</nowiki> 
**** Probability <nowiki> [A measure of the expectation of the occurrence of a particular event.]</nowiki>
***** <nowiki># {takesValue, valueClass=numericClass}</nowiki>
                      . . .
```
````


Similar differences occur between the merged and unmerged XML formats, 
but only the merged XML format is useful.

### 7.2.3. Auxiliary sections

The unmerged version of a partnered library schema **must** have
prologue and epilogue sections that appropriately explain the
purpose of the library schema.
The contents of these prologue and 
epilogue sections become the prologue and epilogue, respectively,
in the merged schema.

All the other auxiliary sections of the corresponding partner standard schema
are inherited by the merged schema.
Most unmerged partnered library schemas will not contain any additional
auxiliary sections.

**Auxiliary section items that do not appear in a standard schema
are unlikely to be supported by the HED infrastructure if
they require special handling.**
Thus, adding items to the auxiliary library schema sections is discouraged.

Library schema developers who need to add an item, such as
a unit class to an auxiliary section,
should first contact the HED Working Group to determine whether
this item could be appropriately added to the standard schema.
If a new item must be added, only that item and its corresponding
auxiliary section should appear in the unmerged schema.

Library schema additions of units, unit classes, unit modifiers, value classes,
and schema attributes are permitted, though not encouraged.
**Library schemas cannot add information to the property definitions
section of the schema.**

### 7.2.4. Partnered attributes

To support partnered library schema the following items were introduced in
HED standard schema 8.2.0:

| Name | Type  | Role |
| --------- | ----- | ---- |
| `withStandard` | Header attribute | <ul><li>Indicates that this is a partnered library schema.</li><li>Its value is the version of its standard schema partner.</li></ul> |
| `unmerged` | Header attribute | <ul><li>Indicates that this schema contains only library information.</li><li>Its value is either "true" or "false.</li><li>If "false", the attribute should be omitted.</li></ul> |
| `inLibrary` | Element attribute | <ul><li>Indicates that this element is in the library schema.</li><li>Its value is the library name in lowercase.</li><li>The  attribute appears only in merged schemas.</li></ul> |
| `rooted=XXX` | Node attribute | <ul><li>Indicates that this node is to appear directly under<br/> standard schema node `XXX` in the merged schema.</li><li>A node with the `rooted` attribute must be<br/>a top-level node in the unmerged schema.</li></ul> |
| `reserved` | Node attribute | <ul><li>Indicates that this node has special meaning or function.</li><li>**Can only appear in standard schemas.**</li></ul>. |


### 7.2.5. Motivation for partners
Starting with HED specification version 3.2.0 and HED standard schema version 8.2.0, 
**partnered library schemas** have become the recommended form for library schemas.
This section describes the motivation for this preference.

#### 7.2.5.1. Auxiliary consistency

A standalone library schema must duplicate the 
[**auxiliary schema sections**](https://hed-specification.readthedocs.io/en/latest/Appendix_A.html#a-1-auxiliary-schema-sections) appearing in standard schemas,
introducing the possibility of inconsistency in usage or definition
between the library schema and standard schemas.

Partnered library schema automatically inherit the partner standard schema's auxiliary attributes,
this assuring consistent handling by tools and preventing the introduction of inconsistently
handled attributes.

Although standalone library schemas may add additional items to the auxiliary sections,
HED tools only guarantee support of standard schema auxiliary items requiring special handling.
**Thus, addition of items in the auxiliary sections of a library schema is discouraged.**


#### 7.2.5.2. Reserved tag handling

Several tags in the standard schema such as `Definition`, `Onset`, and `Offset` 
define the structure of events and the data.
By partnering with a standard schema, a library schema is assured of having
HED support for key features such as events of temporal extent and definitions.

Developers of partnered library schemas should release new versions 
whenever HED updates its standard schema.
This ensures that the partnered library schema benefits from the latest updates to HED features and tools.

If the update can be done without conflict,
this update may be initiated as part of the release mechanism 
by the maintainers of the HED repositories.

#### 7.2.5.3. Annotation conciseness

The most common use case for library schemas in annotation requires tags from both
a standard schema and a library schema, thus requiring that a `xx:` be assigned to tags from
one of the schemas when standalone library schemas are used.

Because a partnered library schema is merged with a standard schema to form a single, unified schema,
users can annotate data without the `xx:` namespace designator.
The `xx:` is still needed if more than one library schema is used.

#### 7.2.5.4. Library searches

The subtrees appearing in the library schemas are often elaborations of a particular term
in the standard schema. 
However, if the library schema terms are not in appropriate standard schema hierarchy,
HED search can not be leveraged to find these elaborations by searching for a more 
general standard schema term.

#### 7.2.5.5. Suggested tags

Standalone library schemas cannot use the `suggestedTag` or `relatedTag` attributes to 
suggest using particular tags from the standard schema,
since the values of the tags must be in the schemas themselves.
However, with partnered library schemas, validation is only performed on
the merged versions of the schema, so tags from the standard schema can be used
as `suggestTag` or `relatedTag` values.

#### 7.2.5.6 Loading multiple partnered schemas

HED allows multiple partnered schemas to be loaded and used without prefixes provided that
there are no conflicts. We refer to this process as **lazy merging**. Conflicting schemas
can always be used together if all but one have an associated prefix.
A merge is attempted for all non-prefixed schemas and for each group of schemas with the
same prefix.  

In the following example, all the library schemas are partnered with '8.2.0'.
Library schemas `liba_1.0.0` and `libc_4.3.2` are merged with no prefix, and 
library schemas `ac:libb_2.8.1` and `ac:exam_2.3.2` are merged with prefix `ac:`. 
The schema `sc:test_1.3.2` stays the same and schema `8.2.0` has no effect,
since it is already included as a partner of `liba_1.0.0` and
`libc_4.3.2`. If there are any conflicts during the merging process, an error is raised.


````{admonition} Example: Merging of multiple schemas.

```
     ['liba_1.0.0', 'ac:libb_2.8.1', 'libc_4.3.2', '8.2.0', sc:test_1.3.2', 'ac:exam_2.3.2']
```
```` 


````{admonition} Rules for lazy merging of partnered schemas A and B. 
:class: tip
1. Partnered library schemas MUST be partnered with the same standard schema in order to merge.
2. Partnered library schemes with the same prefix are merged into one schema.
3. Partnered library schemas with no prefix are merged into one schema.
4. The schema versions are given in a list and merged successively.
5. Including a standard schema separately has no effect if it is a partner of another schema in the same
merge group.  
6. The prefixes of the resulting merge groups must be unique. Only one merge group has no prefix. 
7. If any tags match in two schemas being merged, even if identical, the load fails.
8. The prologue and epilogue sections of the schema are ignored since merge groups are never saved.
9. Partnered library schemas can only specify new unit classes or units, not value classes, schema attributes,
or properties.
10. New library schema unit classes and their accompanying units are merged directly. 
11. New library schema units under an existing unit class are merged if there is no conflict in the units.
````

If an incompatible list of schemas is given, a [**SCHEMA_LOAD_FAILED**](./Appendix_B.md#b25-schema-loading-errors)
error is generated.

````{admonition} Avoid new auxiliary section entries in library schemas.
:class: warning
**Note:** With the possible (and rare) exception of new `unitClasses` and `units`, partnered library schemas 
should not have auxiliary sections except for the `prologue` and `epilogue`.  

Auxilliary sections have information for HED tools, and new entries may require modification to
schema validation tools.  

If a new entry is needed, contact the HED Working Group (hed.maintainers@gmail.com) to see if the
entry might be added to the standard schema instead.
````

## 7.3. Library schema design

Library schema should be developed and maintained in MediaWiki format for readability.
Developers should always validate the schema before converting to XML.
Only validated versions of the schema should be uploaded to the GitHub
[**hed-schemas**](https://github.com/) repository.
More information about the development process is contained in the
[**HED schema developers guide**](https://www.hed-resources.org/en/latest/HedSchemaDevelopersGuide.html).


### 7.3.1. General design rules

This section summarizes the general design rules for all library schema.

``````{admonition} General design rules for HED library schema.
:class: tip

1. **Follow naming conventions**:<br/>
A library schema must be given a name containing only alphabetic chararacters.
This name must appear in the schema header line in the required format.
<br>&nbsp;</br>
2. **Use semantic versioning**:<br/>
A library library must use semantic versioning and follow the versioning update rules used by
the HED standard schema as specified in [**Semantic versioning**](./03_HED_formats.md#33-semantic-versioning).
<br>&nbsp;</br>
3. **Tag uniqueness**:<br/>
Every term must be unique within the library schema and must 
conform to the rules for HED schema terms.
<br>&nbsp;</br>
4. **Have a meaningful prologue**:<br/>
The schema should include a prologue section giving an overview, purpose and scope
of the library schema.
<br>&nbsp;</br>
5. **Have a meaningful epilogue**:<br/>
The schema should include an epilogue section containing reference, citation, and license information.
<br>&nbsp;</br>
6. **Be understandable**:<br/>
Schema terms should be readily understood by most users. The terms should not be ambiguous and
should be meaningful in themselves without reference to their position in the schema hierarchy.
<br>&nbsp;</br>
7. **Be well-organized**:<br/>
If possible, no schema sub-tree should have more than 7 direct subordinate sub-trees.
<br>&nbsp;</br>
8. **Maintain subtree orthogonality**:<br/>
Terms that are used independently of one another should be in different sub-trees (orthogonality).
<br>&nbsp;</br>
9. **Enforce is-a relationship between child nodes and their parents**:<br/>
Every node in a HED hierarchy must be a subclass of its parent node.
This is required for HED search generalizability.

``````
Rules 1 through 5 are enforced by validators, while rules 6 through 9 are
the responsibility of the schema designers and review committees.

In general, library schema developers should avoid adding schema terms that
duplicate those found in the latest HED standard schema at the time of release.
Library schema developers should also try to avoid overlap of terms found
in other schema libraries.

All HED schemas, including library schemas, must use [**semantic versions**](https://semver.org/) and
adhere to the rules specified [**3.3 Semantic versioning**](./03_HED_formats.md/#33-semantic-versioning).

Standalone library schema developers must include the auxiliary schema classes from
the standard HED schema including the schema attributes, unit classes, unit modifiers,
value classes, and schema properties.
No changes should be made to these sections since HED tools support the special auxiliary
classes from the standard schema,
but in general do not support special handling of added classes beyond basic verification. 

If your application requires schema classes that are not available
in the standard HED schema and would like these classes to be supported,
please make a request using the [**issues**](https://github.com/hed-standard/hed-schemas/issues) 
forum of the [**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.


### 7.3.2. Standalone design rules

The following design rules are specifically meant for standalone library schemas.

``````{admonition} Design rules specific to standalone HED library schemas.
:class: tip

1. **Avoid tag duplication**:<br/>
The terms in the library schema should not overlap terms present in the latest
version of the HED schema at the time of its release.
<br>&nbsp;</br>
2. **Do not modify the special auxiliary sections**:<br/>
The standalone library schema should exactly duplicate of special auxiliary sections 
of the HED standard schema that was the latest version when this schema version was released.
The special sections include:  schema attributes, unit classes, 
unit modifiers, value classes, and schema properties.
<br>&nbsp;</br>
3. **Avoid adding special auxiliary items**:<br/>
A library schema may not modify any of the items in the special sections
of the HED standard schema.
<br>&nbsp;</br>
4. **Obtain the appropriate reviews early**:<br/>
Any additions to the special sections must be reviewed by the HED Working Group to
determine what requirements the additions would impose on downstream tools.
This should be done as early in the process as possible.

``````

Standalone library schemas are no longer recommended because of the difficulty
in enforcing conflict rules with HED standard schemas.

### 7.3.3. Partnered design rules

Partnered library schemas are now the recommended format for the reasons
listed in [**Motivation for partners**](./07_Library_schemas.md#725-motivation-for-partners).
The following design rules are specifically meant for partnered library schemas.

``````{admonition} Design rules specific to partnered HED library schemas.
:class: tip

1. **Check for overlap**:<br/>
The terms in the partnered library schema must not overlap with terms present in its partnered
standard schema.
<br>&nbsp;</br>
2. **Use the latest released version of the standard schema**:<br/>
A partnered library schema should always use the latest version of the HED schema
available at the time of its release.
<br>&nbsp;</br>
3. **Do not put any auxiliary sections**:<br/>
A partnered library schema should not contain the special auxiliary sections (e.g., schema attributes, unit classes, unit modifiers, value classes, and schema properties),
unless a new item is added to the section, in which only that item should appear.
<br>&nbsp;</br>
4. **Seek reviews early in the process**:<br/>
Any additions to the special sections must be reviewed by the HED Working Group to
determine what requirements the additions would impose on downstream tools.

``````
It is recognized that HED standard and library schemas will both evolve and
that additions or tag reorganizations may cause conflicts.
These conflicts must be resolved as they occur.
In general the standard schema takes precedence over any library schema in
resolving these conflicts.

### 7.3.4. Schema namespaces

As part of the HED annotation process, users must associate one or more
HED schemas with their datasets.
Since it would be impossible to avoid naming conflicts across schema libraries built in parallel by different user communities, 
HED supports schema library namespaces to facilitate the use of multiple schemas in
annotating a datasets.

If multiple schemas are used, users must define a local namespace for
each additional schema and prefix the tags from each of these
additional schemas by their respective namespace in annotations.
The local names should be strictly alphabetic with no blanks or punctuation.
If a tag namespace prefix is invalid in the version specification,
a schema loading error occurs.



````{admonition} **Example:** Driving library schema example tags.

```
dp:Drive-action/Change-lanes
dp:Drive/Change-lanes
dp:Change-lanes
```
````

A colon (`:`) is used to separate the qualifying local name from the remainder of the tag. 

The introduction of partnered library schemas has greatly reduced the need for namespaces,
since the most common use case is a library schema used with a standard schema.

## 7.4. Library schemas in BIDS

The most common use case (for 99.9% of the HED users) is to tag events using
a standard HED schema (preferably the latest one) available in the
`standard_schema/hedxml` directory of the `hed-schemas` repository of the
`hed-standard` organization on GitHub.
The standard schemas are available at:
[**https://github.com/hed-standard/hed-schemas/tree/main/standard_schema**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema).

The **official library schemas** are available at
[**https://github.com/hed-standard/hed-schemas/tree/main/library_schemas**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas).

Standard schemas are referenced by their version number (e.g., `8.1.0`),
while library schema are referenced by a combination of library name
and version number (e.g., `score_1.0.0`).

For BIDS datasets, the versions of the HED schema are specified by
the `HEDVersion` field of the BIDS `dataset_description.json` file.
The following example specifies that version 8.1.0 of the standard HED schema is 
to be used in addition to `score` library schema version `1.0.0`.

````{admonition} Illustration of using the namespace prefix for tagging.
:class: tip

The `dataset_description.json` file contains:

```json
{
  "Name": "A great experiment",
  "BIDSVersion": "1.8.0",
  "HEDVersion": ["8.1.0", "sc:score_1.0.0"]
}
```

A typical annotation is:

```text
"Data-feature, sc:Photomyogenic-response, sc:Wicket-spikes"
```
````



Based on the above description tools will download:
1. The standard HED schema:  
[https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.1.0.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.1.0.xml).
2. The HED `score` library schema version 1.0.0:  
[https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_1.0.0.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_1.0.0.xml). 

In the dataset annotations for the above example, tags drawn from the score schema would
be prefixed with `sc:`, where `sc` is a local name used to distinguish
tags from the additional schema.

The array specification of the schema versions in BIDS can have at most one version
appearing without a colon prefix.

SCORE version 1.0.0 is not partnered, so the HED version specification had to include
both the library and standard schema versions.
In contrast, SCORE version 1.1.0 is partnered with HED standard schema 8.2.0,
so no namespace prefixes are needed as shown in the following example:

````{admonition} **Example:** An example specification of HED version for a partnered schema.
:class: tip

The `dataset_description.json` file contains:

```json
{
  "Name": "A great experiment",
  "BIDSVersion": "1.8.0",
  "HEDVersion": "score_1.1.0"
}
```

A typical annotation is:

```text
"Data-feature, Photomyogenic-response, Wicket-spikes"
```
````
