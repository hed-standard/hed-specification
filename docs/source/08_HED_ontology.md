# 8. The HED ontology

--------DRAFT DRAFT DRAFT DRAFT DRAFT ------------

The HED (Hierarchical Event Descriptors) schema representation was developed to facilitate complex annotation of experimental data.

HED has a standard vocabulary (the HED standard schema) and additional community-specific vocabularies
(HED library schemas) which can be used in conjunction with each other.
HED is an annotation system --- with rules as described in this document for how
annotations can be combined to convey meaning for experimental data.

The HED system also has an underlying ontological structure, 
which has been made explicit starting with HED standard schema 8.3.0 in order to
leverage links to additional information and examples as well as external knowledge sources
during both annotation and analysis.

HED requires that child tags of tags in the HED schema satisfy the **is-a** relationship.
This requirement is satisfied in HED ontology using subclass relationship.
The HED requirement of orthogonality between tags in different top-level subtrees 
can be captured in the HED ontology by imposing *disjointness* on the top-level trees,
but this is not currently being enforced.


## 8.1. HED global identifiers

### 8.1.1. Schema identifiers

The HED tags in each HED schema are unique, 
so a HED tag is uniquely identified by its name (label) and schema version.
If the tag is from a library schema, the library name is part of the version. 
The rules for updating HED version numbers are specified in 
[**HED semantic versioning**](https://github.com/hed-standard/hed-schemas/blob/main/README.md#hed-semantic-versioning).

Starting with HED schema version 8.2.0 (released April 28, 2023),
HED library schemas are strongly recommended to be 
[**partnered with a standard schema**](./07_Library_schemas.md#72-partnered-schemas).
Partnered schemas are joined with a specific version of the standard schema
and are treated as a single integrated vocabulary for annotation.
Partnered schemas MUST not have name conflicts with their standard schema partner.

[**Lazy partnering**](./07_Library_schemas.md#726-lazy-partnering), 
introduced with HED schema version 8.3.0, allows any number of library schemas to be loaded
into a single integrated vocabulary provided they are partnered with the same version of the standard schema
and there are no name conflicts.
If there are conflicts, user-selected namespace prefixes must be used
in the version specification and in annotations.
 

### 8.1.2. Ontology namespace

The HED ontology uses GUIDs (Global Universal Identifiers) of the form HED_xxxxxxx for all elements of HED 
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

### 8.1.3. HED IRIs

HED IRIs [(**International Resource Identifiers**)](https://datatracker.ietf.org/doc/html/rfc3987) are mapped
to [**https://purl.org/hed**](https://purl.org/hed).

## 8.2. HED schema to ontology

Starting with HED standard schema 8.3.0.
Each HED element (tag, unit, unit class, unit modifier, or value class) is associated with its
GUID in a HED schema using the `hedId` schema attribute.

The examples in this section use `heds:` to denote the namespace of structural elements,
and `hed`: to represent schema-specific elements.
Both namespaces map to the same PURL.

### 8.2.1. HED Tags

A HED tag is represented in the HED ontology by the `HedTag` class (HED_0000016).

The HED schema hierarchy is captured by subclassing in the HED ontology.
A HED node that is a direct subclass of `HedTag` is a top-level tag node in the HED schema.
A descendent of a top-level tag node is a direct subclass of its parent tag node in the HED schema.
The ontology subclass relationship enforces the HED requirement that each tag in the
HED schema must satisfy the **is-a** relationship with its parent in the HED schema.

The examples of this section use the `Action` tag and its child `Communicate`
to illustrate how subclassing is represented in the various HED formats.

#### 8.2.1.1. Mediawiki tag format

The **MediaWiki** representation of a HED tag uses asterisks to mark parentage relationships.
The parent of a tag prefixed by *X* number of asterisks is the first tag
above it with *X-1* asterisks.
Top level tags are enclosed by three quotes and have no parent within the schema.
Each top-level tag is the root of a HED tree of tags that are orthogonal.

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

#### 8.2.1.2. XML tag format

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
`Communicate` tag is a subclass (is-a) of `Action` because
its &lt;node&gt; &lt;/node&gt; definition is nested with the  &lt;node&gt; &lt;/node&gt; definition of `Action`.


#### 8.2.1.3. OWL format

We use the [**OWL Manchester syntax**](https://www.w3.org/TR/owl2-manchester-syntax/)
for the examples in this specification document because of readability.
The HED ontology is also distributed in OWL/RDF format.


````{admonition} **Example** HED Manchester OWL syntax.

```yaml
Class: hed:HED_0012016
    Annotations: 
        dc:description "Do something.,
        heds:hedId "HED_0012016",
        rdfs:label "Action"   
    EquivalentTo: 
        heds:HED_0000016
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


### 8.2.2. Schema attributes

Schema attributes are mappings of schema elements into values or into other schema elements.
How a given HED schema attribute is mapped into its corresponding HED ontology is
determined by the domain, the range, and whether the attribute is inherited.
The mapping strategy is summarized in the following table.

| Ontology | Domain | Range | Inherited? |
| -------- | ------ | ----- | ----------- |
| AnnotationProperty | HED element | string, numeric, boolean | No |  
| ObjectProperty | HED element | string, numeric, boolean | Yes | 
| DataProperty | HED element | HED element | Yes | 

A HED element refers to a HED tag, unit, unit class, or value class element.
The schema attributes themselves are also considered HED elements.




* hedId <nowiki>{annotationProperty, elementDomain, stringRange}[The unique identifier of this element in the HED namespace.]</nowiki>
Example:
<schemaAttributeDefinition>
   <name>hedId</name>
   <description>The unique identifier of this element in the HED namespace.</description>
   <property>
      <name>annotationProperty</name>
      <name>elementDomain</name>
      <name>stringRange</name>
   </property>
</schemaAttributeDefinition>

#### 8.2.3.1. Schema attribute properties

The auxiliary schema attribute `Properties` section of the HED schema defines
notation for designating where a schema attribute for designating 
the domain, range and inheritance properties of a schema object.

All items in the schema `Properties` auxiliary schema section are indicator variables:
presence indicates `true` and absence indicates `false`.

The presence of the `annotationProperty` in a schema attribute definition
indicates that this schema attribute is not inherited by its children.
Since inheritance is only relevant to HED tags,
this property only appears in schema attributes applicable to HED tags.

````{admonition} **Example** The annotation property.

**MediaWiki definition:**
```
* hedId <nowiki>{annotationProperty, elementDomain, stringRange}[The unique identifier of this element in the HED namespace.]</nowiki>
```

**XML definition:**

```
<schemaAttributeDefinition>
   <name>hedId</name>
   <description>The unique identifier of this element in the HED namespace.</description>
   <property>
      <name>annotationProperty</name>
      <name>elementDomain</name>
      <name>stringRange</name>
   </property>
</schemaAttributeDefinition>
```


````
wapplies indicates that this schema attribute is not inherited by its children and is <nowiki>[This schema attribute is inherited by child nodes. This property only applies to schema attributes for nodes.]</nowiki>


The attribute properties section of a HED schema is an auxiliary schema section
of a HED schema that specifies how schema attributes should behave.
#### 8.2.2.1 Attribute domains
Property names ending in `Domain` specify what types of schema elements
an attribute is allowed to be associated with.


The `annotationProperty` applies in a schema attribute definition indicates that this
schema attribute is not inherited by its children and is <nowiki>[This schema attribute is inherited by child nodes. This property only applies to schema attributes for nodes.]</nowiki>


#### Th
* boolRange <nowiki>[This schema attribute's value can be true or false. This property was formerly named boolProperty.]</nowiki>
* elementDomain <nowiki>[This schema attribute can apply to any type of element (tag term, unit class, etc). This property was formerly named elementProperty.]</nowiki>
* tagDomain <nowiki>[This schema attribute can apply to node (tag-term) elements. This was added so attributes could apply to multiple types of elements. This property was formerly named nodeProperty.]</nowiki>
* tagRange <nowiki>[This schema attribute's value can be a node. This property was formerly named nodeProperty.]</nowiki>
* numericRange <nowiki>[This schema attribute's value can be numeric.]</nowiki>
* stringRange <nowiki>[This schema attribute's value can be a string.]</nowiki>
* unitClassDomain <nowiki>[This schema attribute can apply to unit classes. This property was formerly named unitClassProperty.]</nowiki>
* unitClassRange <nowiki>[This schema attribute's value can be a unit class.]</nowiki>
* unitModifierDomain <nowiki>[This schema attribute can apply to unit modifiers. This property was formerly named unitModifierProperty.]</nowiki>
* unitDomain <nowiki>[This schema attribute can apply to units. This property was formerly named unitProperty.]</nowiki>
* unitRange <nowiki>[This schema attribute's value can be units.]</nowiki>
* valueClassDomain <nowiki>[This schema attribute can apply to value classes. This property was formerly named valueClassProperty.]</nowiki>
* valueClassRange <nowiki>[This schema attribute's value can be a value class.]</nowiki>