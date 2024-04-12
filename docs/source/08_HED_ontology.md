# 8. The HED ontology

--------DRAFT DRAFT DRAFT DRAFT DRAFT ------------

## 8.1. HED views and representations

### 8.1.1. The annotator's view

HED (Hierarchical Event Descriptors) has a standard hierarchically-organized vocabulary (the HED standard schema) 
and additional community-specific vocabularies (HED library schemas) that can be used to annotate and analyze experimental data.
The HED vocabularies and the supporting HED ecosystem are designed to support these activities.

The data annotator's natural view is top-down -- identifying a general category and
then filling out the details with more specific tags in that category or grouping with descriptive tags
from other categories. As illustrated in the following diagram, the HED schema hierarchy is organized in a top-down 
manner to support this work-flow.

![annotator view](_static/images/AnnotatorsView.png)

In the diagram, top-level tags `S1`, `S4`, and `L6` represent general categories
and are roots of subtrees organized so that child nodes are more specific terms.
HED supports "search generality", so searches may specify an exact match or matches any term in a particular subtree.
In the latter case a search for `Event` may also match `Sensory-event` or `Agent-action` or any other descendent of
`Event`.

The [**HED schema viewer**](https://www.hedtags.org/display_hed.html),
allows users to focus on top-level categories or expand the hierarchy view to any specified level of detail.

### 8.1.2. The ontologist's view

A second view of HED --- the HED ontology --- provides a mapping between HED schemas and classical
ontologies in order to support semantic analysis and reasoning. 

The following diagram shows the ontology view of HED. 
The nodes of the HED schema are embedded in the ontology,
but the view is "term-centric" or "bottom-up" with links from the given term to its
parent class (yellow arrows) and as well links between the given term and other terms (gray arrows).

![ontologist view](_static/images/OntologyView.png)

The ontology represents a complex network of interrelationships among the terms in the HED 
hierarchy and terms in other ontologies. 
The HED ontology and its mapping has been made explicit starting with HED standard schema 8.3.0.
The goal is to include links to additional information including provenance and examples during annotation 
and to leverage AI tools during annotation and analysis.

### 8.1.3. HED information space

The HED schema is embedded in a larger information space that includes
additional information such as sources, provenance, and links to other ontologies.
This HED information space is illustrated schematically in the following diagram.

![hed information space](_static/images/HedInformationSpace.png)

The embedding is anchored by the `hedId` schema attribute introduced with HED standard schema 8.3.0.
The `hedId` values are of the form `HED_xxxxxxx` and resolve to IRIs (International Resource Identifiers) 
of the form *https://purl.org/hed/HED_xxxxxxx*.

The extended information space is completely represented by the HED ontology in OWL format.
In this document we use OWL Manchester format (`.omn`) for readability.  

### 8.1.4. HED representations

The HED vocabularies have 4 different formats as shown in the following table:

| Format | Content | Uses | Editing |
| ------ | ------- | ---- | ------- |
| Mediawiki | Schema | Schema development<br/>Schema updating | Manual editing<br/>Updated from spreadsheet |  
| XML | Schema | Annotation tools<br/>Validation tools<br/>Analysis tools | Generated from MediaWiki |
| Spreadsheet | Complete | Schema development<br/>Schema updating<br/>Ontology updating | Manual editing<br/>Updated from MediaWiki<br/>Updated from OWL |
| OWL | Complete | Ontology updating<br/>Semantic validation<br/>Documentation generation<br/>Semantic tools | Manual editing<br/>Updated from spreadsheet |

The HED schema, which contains the core HED vocabulary and captures the "annotator's view" of HED,
is completely represented in either the HED MediaWiki and HED XML formats.
The HED schema is used for annotation, validation, searching, and most analyses.
Tools access the HED schema in its XML format, but schema developers create
and update the schema in MediaWiki format, which is easier to read and displays as formatted
MarkDown on GitHub.

#### 8.1.4.1. Spreadsheet <--> Mediawiki

The HED schema also has a HED spreadsheet representation 
(with columns containing a tag's name, parent, attributes, and description).
The mapping between the HED MediaWiki format and the HED spreadsheet is illustrated in the following example:

![hed mediawiki to spreadsheet](_static/images/HEDSpreadsheetMediawiki.png)

Note: The information about a single tag in the MediaWiki file must be on a single line,
but the above diagram has formatted the information so that it will fit within image boundaries.

The mapping of the spreadsheet row and column values to a line in the MediaWiki is further explained in the
following table:

| Spreadsheet<br/>column | Row value | MediaWiki format |
| ----------- |:------------------:| ------- |
| **hedId**  | *xxx* | {hedId=*xxx*, ... other attributes in comma separated list} |
| **level**  | 0 | This row corresponds to a top-level HED tag. Example:  `'''tag'''`.  |  
| **Level**  | *n* | For level *n* > 0, *n* asterisks appear in front of `tag`.<br/>Example: `* tag` when *n* = 1. Example: `** tag` when *n*=2. |
| **rdfs:label**  | *yyy* | The tag's unique name is *yyy*. |
| **Parent** | *zzz* | The tag's parent tag in the HED hierarchy is *zzz*. |
| **Attributes** | *uuu*, *vvv*, ... | List appearing in curly braces: {hedId=*xxx*, *uuu*, *vvv*, ...} |
| **dc:description** | *www* | The contents of the square braces: [*www*]. |

HED schema developers can develop in either HED MediaWiki or HED spreadsheet (tab-separated-value) file format and
can use tools to update the representations.
Users may NOT assign or modify the `hedId` in the MediaWiki file.
If adding a new tag to the MediaWiki file, schema developers should omit the `hedId`. 
Tools will assign and validate the `hedId` during the update process.

#### 8.1.4.2. Spreadsheet <--> Ontology

HED spreadsheets have been expanded to include additional columns to capture all the information 
contained in the HED ontology as illustrated in the following example.

![hed representations](_static/images/HedRepresentations.png)

The mapping of the spreadsheet row and column values to a line in the MediaWiki is further explained in the
following table:


| Spreadsheet<br/>column | Row value | Ontology format |
| ----------- |:------------------:| ------- |
| **hedId**  | *xxx* | `Class: hed:xxx` |
| **Level**  | *n* | Redundant information -- can be recovered using class hierarchy. |
| **rdfs:label**  | *yyy* | `rdfs:label yyy` in the `Annotations` section |
| **Parent** | *zzz* | The tag is either a `SubClassOf` or `EquivalentTo` *zzz*<br/>but *zzz* is identified by **hedId* rather name. |
| **Attributes** | *uuu*, *vvv*, ... | If non-empty, then these appear as restrictions<br/> in the `EquivalentTo`. |
| **dc:description** | *www* | `dc:description www` in the `Annotations` section. |
|**EquivalentTo** |    | A combination of the information in **Parent** and **Attributes** |

In this table `hed:` is the abbreviation for HED's IRI (International Resource Identifier)
as explained in [**8.3 HED global identifiers](./#83-global-identifiers)

HED tags are always represented by classes in the HED ontology. 
A tag class IRI (International Resource Identifier) is its `hedId`.
HED tag names also uniquely identify HED tags. 
The `hedId` values are managed by tools and not allowed to be modified by users.

The value in the `rdfs:label` column, which corresponds to the HED tag name in the MediaWiki,
maps to `rdfs:label` in the `Annotation` section for the tag class in the ontology.
The `rdfs:` prefix indicates that `label` is a term from the 
[**RDF Schema**](https://en.wikipedia.org/wiki/RDF_Schema) (i.e., the Resource Description Framework Schema).
For ease in editing, the spreadsheet uses an item's `rdfs:label` column value when referring to the item
rather than its `hedId`, but the Ontology representation always uses the `hedId`.

A top-level (level 0) tag such as `Event` is a subclass of `HedTag`, 
while any tag lower in the HED schema hierarchy is a subclass of its parent tag (class).

The value in the  `dc:description` which corresponds to the tag's description 
maps to the `dc:description` in the `Annotation` for the tag class in the ontology.
The `dc:` prefix indicates that `description` is a term from the Dublin Core ontology.

If a HED tag has no attributes, its parent class in the HED hierarchy is given using `SubClassOf` in the ontology.
However, if a tag has attributes, the class must be declared using restrictions with `EquivalentTo`.

Users may add additional columns to the spreadsheet with qualified column names of the form `yyy:xxx`.
`yyy` is a shortcut ref to a particular ontology, while `yyy` is a property in that ontology.
These items are added automatically to the `Annotations:` section of the HED ontology.

## 8.2. HED schema to ontology

Each HED element (tag, unit, unit class, unit modifier, or value class) is associated with its
GUID in a HED schema using the `hedId` schema attribute.

The examples in this section use `heds:` to denote the namespace of structural elements,
and `hed:` to represent schema-specific elements.
Both namespaces map to the same PURL (Persistent Uniform Resource Locator).

## 8.2.1. Overall ontology structure

HED requires that child tags of tags in the HED schema satisfy the **is-a** relationship.
This requirement is satisfied in HED ontology using subclass relationship.
The HED requirement of orthogonality between tags in different top-level subtrees 
can be captured in the HED ontology by imposing *disjointness* on the top-level trees,
but this is not currently being enforced.


| Schema | Ontology |
| ------ | -------- |
| Header | Class with `DataProperty` values for `version`, `library`, `withStandard`, and `merged`. |
| Tag    | Class using subclassing to represent schema structure.<br/>The parent class appears either in `SubClassOf` or `EquivalentTo`. |
| Unit class | Class inheriting from `StandardUnitClass` (`HED_0010006`)<br/>if defined in the standard schema. |
| Unit  | Class inheriting from `StandardUnit` (`HED_0010007`)<br/>if defined in the standard schema.<br/>The class must have `hasUnitClass` some unit class. |
| Unit modifier | Class in inheriting from `StandardUnitModifier` (`HED_0010008`)<br/>if defined in the standard schema. |
| Value class | Classes |
| Attribute | `ObjectProperty`, `DataProperty`, or `AnnotationProperty` depending on range and inheritability.<br>Attributes are defined in the structure ontology. |
| Property | Implicitly captured in the domains and ranges of the attributes. |


### 8.2.2. HED Tags

A HED tag is represented in the HED ontology by the `HedTag` class (HED_0000005).

The HED schema hierarchy is captured by subclassing in the HED ontology.
Top-level tag nodes in the HED schema are direct subclasses of `HedTag`.
A descendent of a top-level tag node is a direct subclass of its parent tag node in the HED schema.
The ontology subclass relationship enforces the HED requirement that each tag in the
HED schema must satisfy the **is-a** relationship with its parent in the HED schema.

The examples of this section use the `Action` tag and its child `Communicate`
to illustrate how subclassing is represented in the various HED formats.

#### 8.2.2.1. Mediawiki tag format

The **MediaWiki** representation of a HED tag uses asterisks to mark parentage relationships.
The parent of a tag prefixed by *X* number of asterisks is the first tag
above it with *X-1* asterisks.
Top level tags are enclosed by three quotes and have no parent within the schema (i.e., *X* = 0).
Each top-level tag is the root of a tree of tags that are orthogonal to tags in other trees.

For the example, the `Action` tag is a top-level tag (enclosed in a set of three quotes).
The `Communicate` tag is a child (subclass) of `Action`.


````{admonition} **Example** HED MediaWiki representation of subclasses.

```text
'''Action''' <nowiki>{extensionAllowed, hedId=HED_0012016}[Do something.]</nowiki>
* Communicate <nowiki>{hedId=HED_0012017}[Action conveying knowledge of or about something.]</nowiki>
```

````
The tag's schema attributes are enclosed in curly braces, 
and the tag's description is enclosed in square brackets.

#### 8.2.2.2. XML tag format

The **XML** representation of a HED tag uses nesting to indicate hierarchical relationships in the HED schema. 
For HED tags (nodes) the nesting indicates subclassing.
For other schema elements such as unit classes and units,
nesting indicates organizational grouping rather than subclasses.

````{admonition} **Example** HED MediaWiki representation of subclasses.

```xml
<node>
   <name>Action</name>
   <description>Do something.</description>
   <attribute>
      <name>extensionAllowed</name>
   </attribute>
   <attribute>
      <name>hedId</name>
      <value>HED_0012016</value>
   </attribute>
   <node>
      <name>Communicate</name>
      <description>Action conveying knowledge of or information about something.</description>
      <attribute>
         <name>hedId</name>
         <value>HED_0012017</value>
      </attribute>  
   </node>
</node>
```
````
`Communicate` tag is a subclass (**is-a**) of `Action` because
its `<node></node>` definition is nested within the  `<node></node>` definition of `Action`.


#### 8.2.2.3. OWL format for HED classes

We use the [**OWL Manchester syntax**](https://www.w3.org/TR/owl2-manchester-syntax/)
for the examples in this specification document because of readability.
The HED ontology is also distributed in OWL/RDF format.

The following example illustrates the syntax for the HED mapping.
HED schema elements (tags, unit classes, unit modifiers, units, and value classes) are mapped to OWL classes. 
Every element has a unique `hedId`, which is represented as an OWL `AnnotationProperty`.
The `rdfs:label` annotation value is the name of the element as it appears in the HED schema.
The `dc:description` annotation value is the description of the element as it appears in square brackets
in the MediaWiki version of the schema.


````{admonition} **Example** HED Manchester OWL syntax.

```yaml
Class: hed:HED_0012016
    Annotations: 
        dc:description "Do something.,
        heds:hedId "HED_0012016",
        rdfs:label "Action"   
    EquivalentTo: 
        heds:HED_0000005
        and (heds:HED_0000102 some hed:HED_0010004)
        and (heds:HED_0000307 value "true")
    
Class: hed:HED_0012017
    Annotations: 
        dc:description "Action conveying knowledge of or information about something.",
        heds:hedId "HED_0012017",
        rdfs:label "Communicate"   
    SubClassOf: 
        hed:HED_0012016
```
````

The `Action`  (HED_0012016) class is a top level schema tag and therefore a subclass of `HedTag` (HED_0000005).
The parentage relationship is represented by `EquivalentTo` rather than `SubClassOf`
because `Action` has the `extensionAllowed` (HED_0000307) data property.
and the `inHedSchema` (HED_0000102) object property.
Here `HED_0010004` is the `HedStandardSchema` class, which has
 `version` (HED_0000307) data property value 8.3.0.
The `HedStandardSchema` class has been declared elsewhere in the ontology.

The `Communicate` HED tag (HED_0012017) is a direct child of `Action` as indicated by the `SubClassOf` entry.
Since `Communicate` is a subclass of `Action`, it inherits the `inHedSchema` association
with the correct version of the standard schema.


### 8.2.3. Schema attributes

The purpose of HED schema attributes is to specify characteristics and/or behavior of schema elements.
These attributes map schema elements into values or into other schema elements.


#### 8.2.3.1. Attribute ontology types

A given HED schema attribute's representation in the HED ontology is
determined by its domain, its range, and whether the attribute is inherited.
The mapping strategy is summarized in the following table.

| Ontology | Domain | Range | Inherited? |
| -------- | ------ | ----- | ----------- |
| `AnnotationProperty` | HED entity | string, numeric, boolean | No |  
| `DataProperty` | HED entity | string, numeric, boolean | Yes | 
| `ObjectProperty` | HED entity | HED element | Yes | 

`DataProperty` and `ObjectProperty` entities are inherited by subclasses, and reasoners can check their consistency.
`AnnotationProperty` entities are not inherited by subclasses, and reasoners ignore them.

#### 8.2.3.2. Attribute properties

Schema attribute properties appear in the `Properties` section of a HED schema.
They determine how schema attributes behave as described in the following table.

| Attribute name |   Description |  
| -------------- | -------------- |
| `annotationProperty` | The value is not inherited by child nodes. |
| `boolRange` | The value can be true or false. This property was formerly named `boolProperty`. |
| `elementDomain` | The attribute can apply to any type of element (tag, unit, unit class, unit class, or value class). This property was formerly named `elementProperty`. |
| `tagDomain` | The attribute can apply to node (tag-term) elements. This property was formerly named `nodeProperty`. |
| `tagRange` | The value can be a node (tag). |
| `numericRange` | The value can be numeric. |
| `stringRange` | The value can be a string. |
| `unitClassDomain` | The attribute can apply to unit classes. This property was formerly named `unitClassProperty`. |
| `unitClassRange` | The value can be a unit class. |
| `unitModifierDomain` | The attribute can apply to unit modifiers. This property was formerly named `unitModifierProperty`. |
| `unitDomain` | The attribute can apply to units. This property was formerly named `unitProperty`. |
| `unitRange` | The value can be units. |
| `valueClassDomain` | The attribute can apply to value classes. This property was formerly named `valueClassProperty`. |
| `valueClassRange` | The value can be a value class. |

#### 8.2.3.3. Attribute representation

The following table lists schema attributes with their types (A=`AnnotationProperty`, D=`DataProperty`, 
and O=`ObjectProperty`), domains and ranges.

| Attribute | Type |  Domain  |  Range |  Handling
| --------- | ---------- | ---------  | ---------- | ------|
| `allowedCharacter`  | D | `unitDomain`<br/>`unitModifierDomain`<br/>`valueClassDomain` | string  |    |
| `conversionFactor` | D | `unitDomain`<br/>`unitModifierDomain` | `numericRange` |    |
| `defaultUnits`  | O | `unitClassDomain` | `unitRange` |    |
|  `deprecatedFrom` | D | `elementDomain` | `stringRange`   |    |
| `extensionAllowed`  |  | `tagDomain` | `boolRange` |   |
| `hedId` | A | `elementDomain` | `stringRange` | Tools: Assign and verify. |
| `inLibrary` | D | `elementDomain` | `stringRange` |    |
| `relatedTag` | O | `tagDomain` | `tagRange` |    |
| `requireChild`  | A | `tagDomain` | `boolRange` | Tools: Verify.  |
| `reserved`  | D  | `tagDomain` | `boolRange` |   |
| `rooted`  | A | `tagDomain` | `tagRange` | Tools: make tag subclass of tag in range. |
| `SIUnit`  | D | `unitDomain` | `boolRange` |   |
| `SIUnitModifier` | D | `unitModifierDomain` | `boolRange` |   |   |
| `SIUnitSymbolModifier` | D | `SIUnitSymbolModifier` |  `boolRange` |   | 
| `suggestedTag` | O | `tagDomain` | `tagRange` |   |
| `tagGroup`  | D | `tagDomain` | `boolRange` |   |
| `takesValue` | A | `tagDomain` | `boolRange` | Only placeholders |
| `topLevelTagGroup` | D | `tagDomain` | `boolRange`  |    | 
| `unique` | D |`tagDomain`  | `boolRange`  |    |
| `unitClass` | O | `tagDomain` | `unitRange`  |   |
| `unitPrefix` | D | `unitDomain` | `boolRange`  |  |
| `unitSymbol` | D |`unitDomain` |  `boolRange`  |   |
| `valueClass` | O | `tagDomain` | `valueClassRange`  |   |


#### 8.2.3.4. Mediawiki attribute format

In the MediaWiki format, schema attributes appear in the `Schema Attributes` section of the schema.


````{admonition} **Example** HED MediaWiki representation of a schema attribute.

```text
* extensionAllowed <nowiki>{tagDomain, boolRange}[Users can add unlimited levels of child nodes under this tag. This tag is propagated to child nodes with the exception of the hashtag placeholders.]</nowiki>
```
````

#### 8.2.3.5. XML attribute format


Schema attribute definitions are nexted in the `<schemaAttributeDefinitions>` section of the schema's XML file.
The format of an individual schema attribute is shown here.
````{admonition} **Example** HED XML representation of a schema attribute.

```xml
<schemaAttributeDefinition>
   <name>extensionAllowed</name>
   <description>Users can add unlimited levels of child nodes under this tag. This tag is propagated to child 
                nodes with the exception of the hashtag placeholders.
  </description>
   <property>
       <name>tagDomain</name>
   </property>
   <property>
       <name>boolRange</name>
   </property>
</schemaAttributeDefinition>
```
````

#### 8.2.3.6. OWL format for attributes.

The Manchester Owl syntax for schema attributes is similar to that of classes above.


````{admonition} **Example** HED Manchester OWL syntax for extensionAllowed.

```yaml
DataProperty: heds:HED_0000307
    Annotations: 
        dc:description "A schema attribute indicating that users can add unlimited levels of child nodes under this tag. This tag is propagated to child nodes with the exception of the hashtag placeholders.",
        rdfs:label "extensionAllowed" 
    Domain: 
        heds:HED_0000005  
    Range: 
        xsd:boolean

```
````
Unlike `DataProperty` and `ObjectProperty` attributes, `AnnotationProperty` attributes 
are not inherited and do not use domain and range specifications.
These must be handled individual by tools as flagged by the HED schema `annotationProperty` property.
In the OWL representation, information about the handling should be provided in an `rdfs:comment` field.


````{admonition} **Example** HED Manchester OWL syntax for rooted.

```yaml
AnnotationProperty: heds:HED_0000502
    Annotations: 
        dc:description "This top-level library schema node should have a parent which is the indicated node in the partnered standard schema.",
        rdfs:comment "Maps a HedTag into a HedTag name as a string.",
        rdfs:label "rooted"
```
````    

### 8.2.4 Other auxiliary sections

The schema-ontology mapping for HED schema units, unit classes, unit modifiers and value classes is
similar to that of HED tags. However, each of these auxiliary items should have an `inHedSchema` (HED_0000102)
restriction to identify which schema it is in.

A conscious decision was made not to subclass `HedUnit`, `HedUnitClass`, `HedUnitModifier` and `ValueClass`
so that library schemas could be more transparently merged.

## 8.3. HED global identifiers

### 8.3.1. Schema identifiers

The HED tags in each HED schema are unique, 
so a HED tag is uniquely identified by its name (label) and schema version.
If the tag is from a library schema, the library name is part of the version. 
The rules for updating HED version numbers are specified in 
[**HED semantic versioning**](https://github.com/hed-standard/hed-schemas/blob/main/README.md#hed-semantic-versioning).

Starting with HED schema version 8.2.0 (released April 28, 2023),
HED library schemas are strongly recommended to be 
[**partnered with a standard schema**](./07_Library_schemas.md#73-partnered-schemas).
Partnered schemas are joined with a specific version of the standard schema
and are treated as a single integrated vocabulary for annotation and analysis.
Partnered schemas MUST not have name conflicts with their standard schema partner.

[**Lazy partnering**](./07_Library_schemas.md#736-lazy-partnering), 
introduced with HED schema version 8.3.0, allows any number of library schemas to be loaded
into a single integrated vocabulary provided they are partnered with the same version of the standard schema
and there are no name conflicts.
If there are conflicts, user-selected namespace prefixes must be used
in the version specification and in annotations to resolve the conflicts.
 

### 8.3.2. Ontology namespace

The HED ontology uses GUIDs (Global Universal Identifiers) of the form HED_xxxxxxx for all entities of HED 
schemas.

All HED standard and library schema entities are mapped to the `HED_xxxxxxx` namespace
using the range assignments described in the following table.

| HED ID |  Type |
| ------ | ----- | 
| HED_0000001-HED_0000099 | `Class` entities defining the structure of a HED schema  |
| HED_0000100-HED_0000299 | `ObjectProperty` entities common to all HED schemas.|
| HED_0000300-HED-0000499 | `DataProperty` entities common to all HED schemas. |  
| HED_0000500- | `AnnotationProperty` entities common to all HED schemas. |
| HED_0010001-HED_0010099  | `Class` structure of standard schema. |
| HED_0011300-HED_0011399 | `HedValueClass` definitions in the standard schema. |
| HED_0011400-HED_0011499 | `HedUnitModifier` definitions in the standard schema. |
| HED_0011500-HED_0011599 | `HedUnitClass` definitions in the standard schema. |
| HED_0011600-            | `HedUnit` definitions in the standard schema. |
| HED_0012000-HED_0029999  | `HedTag` entities in the standard schema. |
| HED_0032000-HED_0039999  | `HedTag` entities in the score schema. |
| HED_0042000-HED_0049999  | `HedTag` entities in the lang schema. |

### 8.3.3. HED IRIs

HED IRIs [(**International Resource Identifiers**)](https://datatracker.ietf.org/doc/html/rfc3987) are mapped
to [**https://purl.org/hed**](https://purl.org/hed).
