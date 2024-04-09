# 8. The HED ontology

--------DRAFT DRAFT DRAFT DRAFT DRAFT ------------
## 8.1. Two views of HED

HED (Hierarchical Event Descriptors) has a standard hierarchically-organized vocabulary (the HED standard schema) 
and additional community-specific vocabularies (HED library schemas) that can be used to annotate and analyze experimental data.
The HED vocabularies and the supporting HED ecosystem are designed to support these activities.

A second view of HED --- the HED ontology provides a mapping between HED schemas and classical
ontologies in order to support semantic analysis and reasoning.
The HED ontology structure and its mapping has been made explicit starting with HED standard schema 8.3.0.
The goal is to better leverage links to additional information and examples during annotation, 
and to leverage AI tools during annotation and analysis.

A key idea is that 
### 8.1.1. The annotator's view


![annotator view](_static/images/AnnotatorsView.png)



### 8.1.2. The ontologist's view
![ontologist view](_static/images/OntologyView.png)

## 8.1. Overall ontology structure

HED requires that child tags of tags in the HED schema satisfy the **is-a** relationship.
This requirement is satisfied in HED ontology using subclass relationship.
The HED requirement of orthogonality between tags in different top-level subtrees 
can be captured in the HED ontology by imposing *disjointness* on the top-level trees,
but this is not currently being enforced.



| Schema | Ontology |
| ------ | -------- |
| Header | Class with data properties version, library, withStandard, and merged. |
| Tag    | Classes using subclassing to represent schema structure. |
| Unit classes | Classes |
| Units  | Classes with object property `hasUnitClass` |
| Unit modifiers | Classes |
| Value classes | Classes |
| Attributes | Object, data, or annotation properties defined in structure schema. |
| Properties | Implicitly captured in the domains and ranges of the properties. |


## 8.2. HED global identifiers

### 8.2.1. Schema identifiers

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
 

### 8.2.2. Ontology namespace

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

### 8.2.3. HED IRIs

HED IRIs [(**International Resource Identifiers**)](https://datatracker.ietf.org/doc/html/rfc3987) are mapped
to [**https://purl.org/hed**](https://purl.org/hed).

## 8.3. HED schema to ontology

Starting with HED standard schema 8.3.0.
Each HED element (tag, unit, unit class, unit modifier, or value class) is associated with its
GUID in a HED schema using the `hedId` schema attribute.

The examples in this section use `heds:` to denote the namespace of structural elements,
and `hed:` to represent schema-specific elements.
Both namespaces map to the same PURL.

### 8.3.1. HED Tags

A HED tag is represented in the HED ontology by the `HedTag` class (HED_0000005).

The HED schema hierarchy is captured by subclassing in the HED ontology.
Top-level tag nodes in the HED schema are direct subclasses of `HedTag`.
A descendent of a top-level tag node is a direct subclass of its parent tag node in the HED schema.
The ontology subclass relationship enforces the HED requirement that each tag in the
HED schema must satisfy the **is-a** relationship with its parent in the HED schema.

The examples of this section use the `Action` tag and its child `Communicate`
to illustrate how subclassing is represented in the various HED formats.

#### 8.3.1.1. Mediawiki tag format

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

#### 8.3.1.2. XML tag format

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


#### 8.3.1.3. OWL format for HED classes

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


### 8.3.2. Schema attributes

The purpose of HED schema attributes is to specify characteristics and/or behavior of schema elements.
These attributes map schema elements into values or into other schema elements.


#### 8.3.2.1 Attribute ontology types

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

#### 8.3.2.2. Attribute properties

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

#### 8.3.2.3. Attribute representation

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


#### 8.3.2.4. Mediawiki attribute format

In the MediaWiki format, schema attributes appear in the `Schema Attributes` section of the schema.



````{admonition} **Example** HED MediaWiki representation of a schema attribute.

```text
* extensionAllowed <nowiki>{tagDomain, boolRange}[Users can add unlimited levels of child nodes under this tag. This tag is propagated to child nodes with the exception of the hashtag placeholders.]</nowiki>
```
````

#### 8.3.2.5. XML attribute format


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


#### 8.3.2.6. OWL format for attributes.

The Manchester Owl syntax for schema attributes is similar to that of classes
above in [**#### 8.3.1.3. OWL format for HED classes**](#8313-owl-format-for-hed-classes).
For 


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

### 8.3.4 Other auxiliary sections

The schema-ontology mapping for HED schema units, unit classes, unit modifiers and value classes is
similar to that of HED tags. However, each of these auxiliary items should have an `inHedSchema` (HED_0000102)
restriction to identify which schema it is in.

A conscious decision was made not to subclass `HedUnit`, `HedUnitClass`, `HedUnitModifier` and `ValueClass`
so that library schemas could be more transparently merged.