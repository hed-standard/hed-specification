# 7. Library schema

The variety and complexity of events in electrophysiological experiments makes full 
documentation challenging. As more experiments move out of controlled laboratory environments
and into less controlled virtual and real-world settings, the terminology required to adequately
describe events has the potential to grow exponentially.  

In addition, experiments in any given subfield can contribute to pressure to add 
overly-specific terms and jargon to the schema hierarchy—for example, adding musical 
terms to tag events in music-based experiments, video markup terms for experiments 
involving movie viewing, traffic terms for experiments involving
virtual driving, and so forth. 

Clinical fields using neuroimaging also have their own specific
vocabularies for describing data features of clinical interest (e.g., seizure, sleep stage IV).
Including these discipline-specific terms quickly makes the standard HED schema unwieldy and less
usable by the broader user community.

Third generation HED instead introduces the concept of the **HED library schema**. 
To use a programming analogy, when programmers write a Python module, the resulting code 
does not become part of the Python language or core library. Instead, the module becomes 
part of a library used in conjunction with core modules of the programming language. 

Similar to the design principles imposed on function names and subclass organization in 
software development, HED library schemas must conform to some basic rules:

``````{admonition} Rules for HED library schema design.
:class: tip

1. Every term must be unique within the library schema and must conform to the rules for
HED schema terms.
2. Schema terms should be readily understood by most users. The terms should not be ambiguous and
should be meaningful in themselves without reference to their position in the schema hierarchy.
3. If possible, no schema sub-tree should have more than 7 direct subordinate sub-trees.
4. Terms that are used independently of one another should be in different sub-trees (orthogonality).

``````

As in Python programming, we anticipate that many HED schema libraries may be defined 
and used, in addition to the standard HED schema. Libraries allow individual research 
communities to annotate details of events in experiments designed to answer questions 
of interest to particular research or clinical communities. Since it would be impossible 
to avoid naming conflicts across schema libraries that may be built in parallel by different
user communities, HED supports schema library namespaces. Users will be able to add library 
tags qualified with namespace designators. All HED schemas, including library schemas, 
adhere to [semantic versioning](https://semver.org/). 


## 7.1. Defining a schema

A HED library schema is defined in the same way as the standard HED schema except that it has an
additional attribute name-value pair, `library="xxx"` in the schema header. We will use as an
illustration a library schema for driving. Syntax details for a library schema are similar to
those for the standard HED schema. (See [Appendix A: Schema format](Appendix_A.md#a-schema-format)
for more details).

````{admonition} **Example:** Driving library schema (MEDIAWIKI template).

```moin
HED library="driving" version="1.0.0" 
!# start schema 
   [... contents of the HED driving schema ...]
!# end schema
   [... required sections specifying schema attribute definitions ...]
!# end hed
```
````

The required sections specifying the schema attributes  are *unit-class-specification*, 
*unit-modifier-specification*, *value-class-specification*, *schema-attribute-specification*,
and *property-specification*.

````{admonition} **Example:** Driving library schema (XML template).

```xml
<?xml version="1.0" ?>
<HED library="driving" version="1.0.0">
    [... contents of the HED_DRIVE schema ... ]
</HED>
```
````

The schema XML file should be saved as `HED_driving_1.0.0.xml` to facilitate 
specification in tools.

## 7.2. Schema namespaces

As part of the HED annotation process, users must associate a standard HED schema with their
datasets.
Users may also include tags from an arbitrary number of additional library schemas.
For each library schema used to annotate a data recording,
the user must associate a local 
name with the appropriate library schema name and version.
Each library must be associated with a distinct local name within a recording annotations.
The local names should be strictly alphanumeric with no blanks or punctuation. 

The user must pass information about the library schema and their associated local names to 
processing functions. HED uses a standard method of identifying namespace elements by prefixing
HED library schema tags with the associated local names. Tags from different library schemas can
be intermixed with those of the standard schema. Since the node names within a library must be
unique, annotators can use short form as well as fully expanded tag paths for library schema 
tags as well as those from the standard HED schema.

````{admonition} **Example:** Driving library schema example tags.

```
dp:Action/Drive/Change-lanes
dp:Drive/Change-lanes
dp:Change-lanes
```
````

A colon (`:`) is used to separate the qualifying local name from the remainder of the tag. 
Notice that *Action* also appears in the standard HED schema. Identical terms may be used 
in a library schema and the standard HED schema. Use of the same term implies a similar 
purpose. Library schema developers should try not to reuse terms in the standard schema 
unless the intention is to convey a close or identical relationship.


## 7.3. Attributes and classes

In addition to the specification of tags in the main part of a schema, a HED schema has 
sections that specify unit classes, unit modifiers, value classes, schema attributes, 
and properties. The rules for the handling of these sections for a library schema are 
as follows:

### 7.3.1. Required sections

The required sections of a library schema are: the *schema-specification*, 
the *unit-class-specification*, the *unit-modifier-specification*, 
the *value-class-specification* section, the *schema-attribute-specification* section, 
and the *property-specification*. The library schema must include all required 
schema sections even if the content of these sections is empty.

### 7.3.2. Relation to standard HED schema

Any schema attribute, unit class, unit modifier, value class, or property used in the
library schema must be specified in the appropriate section of the library schema
regardless of whether these appear in the standard HEd schema. Validators check the library
schema strictly on the basis of its own specification without reference to another 
schema.

### 7.3.3. Schema properties

HED only supports the schema properties listed in Table B.2: *boolProperty*, 
*unitClassProperty*, *unitModifierProperty*, *unitProperty*, and *valueClassProperty*.  
If the library schema uses one of these in the library schema specification, 
then its specification must appear in the *property-specification* section of the library schema.

### 7.3.4. Unit classes

The library schema may define unit classes and units as desired or include unit classes or 
units from the standard HED schema. Similarly, library schema may define unit modifiers or 
reuse unit modifiers from the standard HED schema. HED validation and basic analysis tools 
validate these based strictly on the schema specification and do not use any outside 
information for these.

### 7.3.5. Value classes

The standard value classes (*dateTimeClass[*]*, *nameClass*, *numericClass[*]*, 
*posixPath[*]*, *textClass[*]*) if used, should have the same meaning as in the 
standard HED schema. The hard-coded behavior associated with the starred ([*]) value 
classes will be the same. Library schema may define additional value classes and 
specify their allowed characters, but no additional hard-coded behavior will be 
available in the standard toolset. This does not preclude special-purpose tools 
from incorporating their own behavior.

### 7.3.6. Schema attributes

The standard schema attributes (*allowedCharacter*, *defaultUnits*, *extensionAllowed*,
*recommended*, *relatedTag*, *requireChild*, *required*, *SIUnit*, *SIUnitModifier*,
*SIUnitSymbolModifier*, *suggestedTag*, *tagGroup*, *takesValue*, *topLevelTagGroup*, 
*unique*, *unitClass*, *unitPrefix*, *unitSymbol*, *valueClass*) should have the same
meaning as in the standard HED schema. The hard-coded behavior associated with the schema 
attributes will be the same. Library schema may define additional schema attributes. 
They will be checked for syntax, but no additional hard-coded behavior will be available
in the standard toolset. This does not preclude special-purpose tools from incorporating
their own behavior.

### 7.3.7. Syntax checking

Regardless of whether a specification is in the standard HED schema or not, HED tools can perform basic syntax checking.

````{admonition} Basic syntax checking for library schema.
:class: tip

1. All attributes used in the schema proper must be defined in the schema attribute section of the schema.
2. Undefined attributes cause an error in schema validation.
3. Similar rules apply to unit classes, unit modifiers, value classes, and properties.
4. Actual handling of the semantics by HED tools only occurs for entities appearing in the standard HED schema.
````

## 7.4. library schemas in BIDS

The most common use case (for 99.9% of the HED users) is to tag events using
one of the standard HED schemas (preferably the latest one) available in the
`hedxml` directory of the `hed-specification` repository of the
`hed-standard` organization on GitHub.
The standard schemas are available at:
[https://github.com/hed-standard/hed-specification/tree/master/hedxml](https://github.com/hed-standard/hed-specification/tree/master/hedxml).

This section explains the changes that are being proposed in BIDS to accommodate
access to HED library schemas in addition to the standard HED schemas.
This section will be updated as the proposals progress though the 
BIDS review process.
The initial proposal only supports **official standard schemas** available at 
[https://github.com/hed-standard/hed-specification/tree/master/hedxml](https://github.com/hed-standard/hed-specification/tree/master/hedxml) 
and **official library schemas** available at
[https://github.com/hed-standard/hed-schema-library/tree/main/library_schemas](https://github.com/hed-standard/hed-schema-library/tree/main/library_schemas).

Standard schemas are referenced by their version number (e.g., `8.0.0`),
while library schema are referenced by a combination of library name
and version number (e.g., `score_0.0.1`).

The major change proposed to the BIDS specification is to allow the value
associated with the `"HEDVersion"` key in the `dataset_description.json` 
file to be an array rather than a string expressing the HED version. 
This proposed change will allow users more flexibility in specifying the 
standard HED schema and will accommodate an arbitrary number of library schemas.
The different cases are illustrated in the following two examples.


````{admonition} **Example:** Using just the standard HED schema in BIDS.

```json
{
    "Name": "A wonderful experiment",
    "BIDSVersion": "1.6.0",
    "HEDVersion":  "8.0.0"
}

```
````


The following example specifies that version 8.0.0 of the standard HED schema is 
to be used in addition to two library schemas: 
the `score` library version `0.0.1` and the `testlib` library version `1.0.2`. 


````{admonition} **Example:** Proposed specification of library schema in BIDS.

```json
{
    "Name": "A wonderful experiment",
    "BIDSVersion": "1.6.0",
    "HEDVersion": ["8.0.0", "sc:score_0.0.1", "ts:testlib_1.0.2"]
}

```
````


Based on the above description tools will download:
1. The standard HED schema:  
[https://github.com/hed-standard/hed-specification/tree/master/hedxml/HED8.0.0.xml](https://github.com/hed-standard/hed-specification/tree/master/hedxml/HED8.0.0.xml).
2. The HED `score` library schema version 0.0.1:  
[https://github.com/hed-standard/hed-schema-library/tree/main/library_schemas/score/hedxml/HED_score_0.0.1.xml](https://github.com/hed-standard/hed-schema-library/tree/main/library_schemas/score/hedxml/HED_score_0.0.1.xml). 
3. The HED `testlib` library schema version 1.0.2:  
[https://github.com/hed-standard/hed-schema-library/tree/main/library_schemas/testlib/hedxml/HED_testlib_1.0.2.xml](https://github.com/hed-standard/hed-schema-library/blob/main/library_schemas/testlib/hedxml/HED_testlib_1.0.2.xml).

A list of available library schemas is available through the
schema browser available for each library.
For example the schema browser for the `score` library schema is available at
[https://www.hedtags.org/display_hed_score.html](https://www.hedtags.org/display_hed_score.html).

Given the `HEDVersion` specification from the previous example, annotators
can use any combination of tags from the three indicated schemas.
Tags from the `score` library schema are of the form `sc:XXX` where `XXX` 
is a tag from the `score` schema.
Similarly, tags from the `test` library schema are of the form `la:YYY` 
where `YYY` is a tag from the `test` schema.
The `sc` and `la` are local names used to distinguish
tags from library schemas and those of the standard HED schema.
The standard HED schema tags don't have a colon prefix.

For some applications, the annotator will only want to use particular
library schema. The following example specifies that only the `score`
library will be used. No prefixes are required in this case.

```{admonition} **Example:** Proposed specification of library schema in BIDS.

```json
{
    "Name": "A wonderful experiment",
    "BIDSVersion": "1.6.0",
    "HEDVersion": "score_0.0.1"
}

```
````