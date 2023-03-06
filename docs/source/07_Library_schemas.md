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
does not become part of the Python language or core libraries. Instead, the module becomes 
part of a library used in conjunction with core modules of the programming language. 

Similar to the design principles imposed on function names and subclass organization in 
software development, HED library schemas must conform to some basic rules:

``````{admonition} Rules for HED library schema design.
:class: tip

1. A library schema must be given a name containing only alphabetic chararacters.
This name must appear in the schema header line in the required format.
2. A library library must use semantic versioning and follow the versioning update rules used by
the HED standard schema.
3. Every term must be unique within the library schema and must conform to the rules for
HED schema terms.
4. Schema terms should be readily understood by most users. The terms should not be ambiguous and
should be meaningful in themselves without reference to their position in the schema hierarchy.
5. If possible, no schema sub-tree should have more than 7 direct subordinate sub-trees.
6. Terms that are used independently of one another should be in different sub-trees (orthogonality).
7. The schema should include the schema attributes, unit classes, unit modifiers, value classes,
and schema properties present in the HED standard schema.

``````

As in Python programming, we anticipate that many HED schema libraries may be defined 
and used, in addition to the standard HED schema. Libraries allow individual research 
communities to annotate details of events in experiments designed to answer questions 
of interest to particular research or clinical communities. Since it would be impossible 
to avoid naming conflicts across schema libraries that may be built in parallel by different
user communities, HED supports schema library namespaces 
(the prefix notation described in the previous section).
Users will be able to add library tags qualified with namespace designators. 
All HED schemas, including library schemas, 
adhere to [**semantic versioning**](https://semver.org/).

In general, library schema developers should include the auxiliary schema classes from
the standard HED schema: the schema attributes, unit classes, unit modifiers,
value classes, and schema properties. The HED tools support these auxiliary
classes but in general would not support special handling of added classes beyond basic
verification. 

If your application requires schema classes that are not available
in the standard HED schema and would like these classes to be supported,
please make a request using the [**HED examples issues**](https://github.com/hed-standard/hed-examples/issues) forum.

A schema should not duplicate tags found in the standard schema.

## 7.1. Defining a schema

A HED library schema is defined in the same way as the standard HED schema 
except that it has an additional attribute name-value pair `library="xxx"` 
in the schema header. 
We will use as a library schema for driving as an illustration.
Syntax details for a library schema are similar to those for the standard HED schema.


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

During annotation tags from different library schemas can
be intermixed with those of the standard schema.
Since the node names within a library must be
unique, annotators can use short form as well as fully expanded tag paths for library schema 
tags as well as those from the standard HED schema.

The schema XML file should be saved as `HED_driving_1.0.0.xml` so that tools can locate them.
The official location of HED standard and library schemas is the
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

## 7.2. Schema namespaces

As part of the HED annotation process, users must associate one or more
HED schemas with their datasets.
If multiple schemas are used, users must define a local prefix for
each additional schema and prefix the tags from each of these
additional schemas by their respective prefix in annotations.
The local names should be strictly alphabetic with no blanks or punctuation.
If a tag prefix is invalid in the version specification,
a schema loading error occurs.



````{admonition} **Example:** Driving library schema example tags.

```
dp:Drive-action/Change-lanes
dp:Drive/Change-lanes
dp:Change-lanes
```
````

A colon (`:`) is used to separate the qualifying local name from the remainder of the tag. 

## 7.3. Library schema layout

In addition to the specification of tags in the main part of a schema, a HED schema has 
sections that specify unit classes, unit modifiers, value classes, schema attributes, 
and properties. The rules for the handling of these sections for a library schema are 
as follows:

### 7.3.1. Required sections

The required sections of a library schema are the same as those for the
standard schema.
These sections are listed in 
[**3.1.2. Schema layout overview**](./03_HED_formats.md#312-schema-layout-overview).
The library schema must include all required 
schema sections even if the content of these sections is empty.

### 7.3.2. Relation to standard HED schema

Any schema attribute, unit class, unit modifier, value class, or property used in the
library schema must be specified in the appropriate section of the library schema
regardless of whether these appear in the standard HED schema. Validators check the library
schema strictly on the basis of its own specification without reference to another 
schema.

### 7.3.3. Schema properties

HED only supports the schema properties listed in
[**A.1.5. Schema properties**](./Appendix_A.md#a15-schema-properties). 
If the library schema uses one of these in the library schema specification, 
then its specification must appear in the *property-specification* section of the library schema.

### 7.3.4. Unit classes

The library schema may define unit classes and units as desired or include unit classes or 
units from the standard HED schema. Similarly, library schema may define unit modifiers or 
reuse unit modifiers from the standard HED schema. HED validation and basic analysis tools 
validate these based strictly on the schema specification and do not use any outside 
information for these.

### 7.3.5. Value classes

The standard value classes listed in [**A.1.3. Value classes**](./Appendix_A.md#(a-13-value-classes)
are the only value classes that should be used in designing library schemas as 
these are the only ones that general tools will support.
If additional value classes are needed, they should be proposed on `hed-schemas` repository
[**issue forum**](https://github.com/hed-standard/hed-schemas/issues).

Library schema may define additional value classes and 
specify their allowed characters, but no additional hard-coded behavior will be 
available in the standard toolset. This does not preclude special-purpose tools 
from incorporating their own behavior.

### 7.3.6. Schema attributes

The standard schema attributes listed in
[**A.1.4. Schema attributes**](./Appendix_A.md#(*allowedCharacter*, *defaultUnits*, *extensionAllowed*,
*recommended*, *relatedTag*, *requireChild*, *required*, *SIUnit*, *SIUnitModifier*,
*SIUnitSymbolModifier*, *suggestedTag*, *tagGroup*, *takesValue*, *topLevelTagGroup*, 
*unique*, *unitClass*, *unitPrefix*, *unitSymbol*, *valueClass*) should have the same
meaning as in the standard HED schema. The hard-coded behavior associated with the schema 
attributes will be the same. Library schema may define additional schema attributes. 
They will be checked for syntax, but no additional hard-coded behavior will be available
in the standard toolset. This does not preclude special-purpose tools from incorporating
their own behavior.

### 7.3.7. Syntax checking

Regardless of whether an entity is in the standard HED schema or a library schema,
HED schema validation tools perform basic syntax checking.

````{admonition} Basic syntax checking for HED schemas.
:class: tip

1. All attributes used in the schema proper must be defined in the schema attribute section of the schema.
2. Undefined attributes cause an error in schema validation.
3. Similar rules apply to unit classes, unit modifiers, value classes, and properties.
4. Actual handling of the semantics by HED tools only occurs for entities appearing in the standard HED schema.
````

## 7.4. Library schemas in BIDS

The most common use case (for 99.9% of the HED users) is to tag events using
a standard HED schemas (preferably the latest one) available in the
`standard_schema/hedxml` directory of the `hed-schemas` repository of the
`hed-standard` organization on GitHub.
The standard schemas are available at:
[**https://github.com/hed-standard/hed-schemas/tree/main/standard_schema**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema).

The **official library schemas** are available at
[**https://github.com/hed-standard/hed-schemas/tree/main/library_schemas**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas).

Standard schemas are referenced by their version number (e.g., `8.0.0`),
while library schema are referenced by a combination of library name
and version number (e.g., `score_1.0.0`).

The following example specifies that version 8.0.0 of the standard HED schema is 
to be used in addition to two library schemas: 
the `score` library version `1.0.0` and the `testlib` library version `1.0.2`. 


````{admonition} **Example:** An example specification with multiple schemas.

```json
{
    "Name": "A wonderful experiment",
    "BIDSVersion": "1.8.0",
    "HEDVersion": ["8.0.0", "sc:score_1.0.0", "ts:testlib_1.0.2"]
}

```
````

Based on the above description tools will download:
1. The standard HED schema:  
[https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.0.0.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.0.0.xml).
2. The HED `score` library schema version 1.0.0:  
[https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_1.0.0.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_0.0.1.xml). 
3. The HED `testlib` library schema version 1.0.2:  
[https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/testlib/hedxml/HED_testlib_1.0.2.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/testlib/hedxml/HED_testlib_1.0.2.xml).

A schema browser is available for each library.
For example the schema browser for the `score` library schema is available at
[https://www.hedtags.org/display_hed_score.html](https://www.hedtags.org/display_hed_score.html).

Given the `HEDVersion` specification from the previous example, annotators
can use any combination of tags from the three indicated schemas.
In this example the standard HED schema version appears without a prefix in the version
specification, so tags from this schema may appear directly in the annotation.

The `sc` and `ts` are local names used to distinguish
tags from the additional schema.
Tags from the `score` library schema are of the form `sc:XXX` where `XXX` 
is a tag from the `score` schema.
Similarly, tags from the `testlib` library schema are of the form `ts:YYY` 
where `YYY` is a tag from the `testlib` schema.

The array specification of the schema versions can have at most one version
appearing without a colon prefix.


### 7.1. Using library schema in BIDS

The following `datset_description.json` of a BIDS dataset
indicates that HED standard schema version 8.1.0 should be used
alone with SCORE library schema 1.0.0.
The tags are....
````{admonition} Illustration of using the namespace prefix for tagging.
:class: tip



```json
{
  "Name": "A great experiment",
  "BIDSVersion": "1.8.0",
  "HEDVersion": ["8.1.0", "sc:score_1.0.0"]
}
```

```text
"Data-feature, sc:Photomyogenic-response, sc:Wicket-spikes"
```
````


Additional information can be found in [**HED schema format**](./03_HED_formats.md#31-hed-schema-format) of Chapter 3 
and [**Appendix A: Schema format details**](Appendix_A.md) for additional information.

Schema developers should also consult the
[**HED schema development guide**](https://www.hed-resources.org/en/latest/HedSchemaDevelopmentGuide.html).

