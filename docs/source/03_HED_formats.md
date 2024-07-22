(3-hed-formats-anchor)=
# 3. HED formats

This chapter describes the requirements and formats for HED schema and HED annotations.

## 3.1. Schema formats

A **HED schema** is a formal specification of a HED vocabulary and annotation format rules.
A HED schema vocabulary is organized hierarchically so that similar concepts and terms appear
close to one another in the organizational hierarchy.

HED schema nodes **must** satisfy an "is-a" relationship with their parent nodes in the schema.
That is, if node *A* is an ancestor of node *B* in the schema,
then *B* is a type of *A*.
This relationship is fundamental to HED and permits search generality.
Searches for *A* are able to also return instances of *B*.

A key requirement for third generation HED (versions >=8.0.0) is that all node names (tag terms) in 
the HED schema (except for `#` placeholders) **must be unique**.

Additional details about HED schema format can be found in appendix
[**A. Schema format details**](./Appendix_A.md).
[**7. Library schemas**](./07_Library_schemas.md#7-library-schemas)
discusses the additional requirements and restrictions on library schemas.

[**B.2. Schema validation errors**](./Appendix_B.md#b2-schema-validation-errors)
gives the errors
Library specific schema issues usually generate  [**SCHEMA_LIBRARY_INVALID**](./Appendix_B.md#schema_library_invalid) errors.


### 3.1.1. Official schema releases

The HED ecosystem supports a standard base schema and additional discipline-specific
library schemas.
(See the [**expandable schema viewer**](https://www.hedtags.org/display_hed.html)
to explore existing schemas.)

Releases of the HED standard base schema are stored in
[**standard_schema/hedxml**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml) 
directory of the [**hed-schemas**](https://github.com/hed-standard/hed-schemas) repository.

Releases of a HED library schemas are stored in a subdirectory of
[**library_schemas**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas)
whose name is the library name.

### 3.1.2. Schema layout overview

Schemas can be specified in either `.mediawiki` or `.xml` format.
The HED schema [**online tools**](https://hedtools.org/hed/schemas) 
provide an easy way for users to validate schema and convert between formats.

HED schema developers usually use `.mediawiki` format for more convenient editing,
display, and viewing on GitHub.
However, the stable links provided for tools to access and download the HED schema
are to the XML versions.
Both formats must be available and synchronized in the 
[**hed/standard/hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

Regardless of the format, a valid HED schema must have the following sections in this order:

````{Admonition} Required sections of a HED schema (in the required order):
| Section   | MediaWiki format | XML format  |
|------- | --------- | ---------- |
| Header line  | `HED version="8.0.0"` | `<HED version="8.0.0">` |
| Prologue | `'''Prologue'''`  | `<prologue> ... </prologue>` |
| Schema start   | `!# start schema`  | `<schema>` ... |
| Schema end  | `!# end schema` | `</schema>` |
| Unit classes | `'''Unit classes'''` | `<unitClassDefinitions>` ... `</unitClassDefinitions>` |
| Unit modifiers | `'''Unit modifiers'''`  | `<unitModifierDefinitions>` ... `</unitModifierDefinitions>`  |
| Value classes | `'''Value classes'''`  | `<valueClassDefinitions>` ... `<valueClassDefinitions>` |
| Schema attributes | `'''Schema attributes'''`  | `<schemaAttributeDefinitions>` ... `</schemaAttributeDefinitions>`    |
| Properties | `'''Properties'''`  | `<propertyDefinitions>` ... `</propertyDefinitions>`  |
| Epilogue  | `'''Epilogue'''` | `<epilogue>` ... `</epilogue>` |
| Ending line | `!# end hed` | `</HED>` |
````

The sections in the `.xml` version must always be terminated by closing `</  >` tokens,
whereas the sections of the `.mediawiki` version, which is line-oriented,
are terminated when the next section begins (`#!`) or a top tag (`'''`) is encountered.

The actual HED tag specifications (referred to in the discussion as nodes or tag terms)
appear in the `schema` section,
while the remaining sections specify additional information and behavior.
These additional sections are required, but are allowed to be empty.

If any of the required sections of the schema are missing or out of order,
a [**SCHEMA_SECTION_MISSING**](./Appendix_B.md#schema_section_missing) error occurs.

Each of the schema sections has "schema attributes", which are the attributes that may be assigned
to elements in a given section.
If a schema attribute is applied improperly to an element in a given section,
the [**SCHEMA_ATTRIBUTE_INVALID**](./Appendix_B.md#schema_attribute_invalid) error occurs.

See [**Appendix A. Schema format details**](./Appendix_A.md) for additional details.

#### 3.1.2.1. The header

The schema header line MUST specify the `version` attribute whose value MUST be a valid semantic version.
See [**SCHEMA_VERSION_INVALID**](./Appendix_B.md#schema_version_invalid).

A schema may optionally contain `library`, `withStandard`, and `unmerged` attributes for library schemas.
A schema's library name or lack there of is used to locate the schema in the
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

The header may optionally contain an XSD namespace specification.
If the schema contains any additional unrecognized attributes, 
[**SCHEMA_HEADER_INVALID**](./Appendix_B.md#schema_header_invalid) error occurs.

See [**A.2.2. MediaWiki header**](./Appendix_A.md#a22-mediawiki-header)
and [**A.3.2. XML header**](./Appendix_A.md#a32-xml-header) for more
detailed information on the MediaWiki and XML header formats, respectively.

#### 3.1.2.2. The prologue

The prologue should contain a concise introduction to the schema and its purpose.
Together with [**the epilogue**](./03_HED_formats.md#3129-the-epilogue) section, 
the contents are used by tools to provide information about the schema to the users.

The prologue may contain `text` characters or `newline`.
If other characters appear, a [**SCHEMA_CHARACTER_INVALID**](./Appendix_B.md#schema_character_invalid) error occurs.


#### 3.1.2.3. The schema section

The schema section contains the actual vocabulary contents of the schema.
Each element in this section is a *node* element, which we will also call a *tag term*.
The location of the node element within the section specifies its relationship to other tag terms in the schema.

A node element specifies a name,
node attributes, and an informative description of the tag term's meaning.
A node name may only contain valid `name` characters 
(`alphanumeric`, `hyphen`, `underscore`, `period`, and `nonascii`).

This also applies to tag extensions.
Substitutions for the `#` placeholder that have value classes are governed by
the rules of that value class.
If other characters appear, a [**SCHEMA_CHARACTER_INVALID**](./Appendix_B.md#schema_character_invalid) error occurs.

Each schema node element must be unique or a
[**SCHEMA_DUPLICATE_NODE**](./Appendix_B.md#schema_duplicate_node) error is generated.


#### 3.1.2.4. Unit classes and units

The unit classes are attributes that modify the `#` schema placeholder nodes.
The unit class definition section specifies the allowed unit classes for the schema
as well as the associated units that can be used with tags that take values.

Only the singular version of each unit is explicitly specified,
but the corresponding plurals of the explicitly mentioned 
singular version are also allowed (e.g., `feet` is allowed in addition to `foot`). 
HED uses a `pluralize` function available in both Python and Javascript to check validity.

Units may be in one of four forms as designated by their unit type attributes: 

| Unit type | Unit type attributes |
| --------- | ---------- |
| SI unit   | only `SIUnit`     |
| SI unit symbol | both `SIUnit` and  `unitSymbol` |
| unit that is not an SI unit | no unit type attribute   |
| unit symbol is not an SI unit | only `unitSymbol` |

Most units appear after the value in annotations. However, certain units such as `$`
appear before their corresponding values.
These units have the `unitPrefix` attribute.

If a unit class, `SIUnit`, or `unitPrefix` attribute appears in a 
section other than the unit class definition section of the schema,
a [**SCHEMA_ATTRIBUTE_INVALID**](./Appendix_B.md#schema_attribute_invalid) error occurs.
See appendix [**A.1.1. Unit classes and units**](./Appendix_A.md#a11-unit-classes-and-units)
for additional details and a listing.

**Units names are case-insensitive and should not contain blanks.
Unit symbols MUST maintain their case.**
Unit class names are case-insensitive, but MUST contain only valid `name` characters.
If other characters appear, a [**SCHEMA_CHARACTER_INVALID**](./Appendix_B.md#schema_character_invalid) error occurs.

#### 3.1.2.5. Unit modifiers

The unit modifier definition section lists the SI unit multiples and submultiples 
that are allowed to be prepended to units that have the `SIUnit` schema attribute.

Unit modifiers can only be used with SI units and SI unit symbols.
SI unit modifiers used with ordinary SI units have the `SIUnitModifier` attribute,
while unit modifiers used with SI unit symbols have the `SIUnitSymbolModifier` attribute.

If a `SIUnitModifier`, or `SIUNitSymbolModifier` attribute appears in a 
section other than unit modifier section of the schema,
a [**SCHEMA_ATTRIBUTE_INVALID**](./Appendix_B.md#schema_attribute_invalid) error occurs.

**Unit modifiers are case-sensitive.**

See appendix [**A.1.2. Unit modifiers**](./Appendix_A.md#a12-unit-modifiers)
for additional details and a listing of values for the standard schema.

#### 3.1.2.6. Value classes

The value class definition section specifies rules for
the values that are substituted for placeholders (`#`). 
Examples are special characters that are allowed for numeric values 
or dates. Placeholders that have no `valueClass` attributes, are assumed to take `textClass` values.

See appendix [**A.1.3. Value classes**](./Appendix_A.md#a13-value-classes)
for additional details and a listing of values for the standard schema.

Value class names are insensitive, but must contain only valid `name` characters.

#### 3.1.2.7. Schema attributes

The schema attribute definition section lists the schema attributes that may be applied to
schema elements in other sections of the schema (except for the properties section).

The specification of which type of schema elements a particular schema attribute may apply
to is specified by its schema properties. 
If a schema attribute appears in a section contradicted by its properties,
a [**SCHEMA_ATTRIBUTE_INVALID**](./Appendix_B.md#schema_attribute_invalid) error occurs.

See appendices [**A.1.4. Schema attributes**](./Appendix_A.md#a14-schema-attributes)
and [**A.1.5. Schema properties**](./Appendix_A.md#a15-schema-properties)
for additional details and a listing for the standard schema.

#### 3.1.2.8. Schema properties

The schema properties section lists the allowed properties of the schema attributes.
These properties help tools validate certain requirements directly based
on the HED schema rather than on a hard-coded implementation. 

There are two types of properties: **form type** and **section type** properties.
The `boolProperty` is a form type property indicating that a schema attribute
does not take a value.
Rather, its presence indicates true and absence indicate false.

The *section* type properties indicate the sections in which a schema attribute may appear.
The section properties include `unitClassProperty`, `unitModifierProperty`, 
`unitProperty`, and `valueClassProperty`.
Schema attributes without any section properties are assumed to apply to node elements.

A schema attribute may have multiple section properties, 
indicating that the attribute may appear as an attribute in multiple sections of the schema.
 
See [**A.1.4 Schema attributes**](./Appendix_A.md#a14-schema-attributes) and 
[**A.1.5. Schema properties**](./Appendix_A.md#a15-schema-properties) 
for information and a listing of schema attributes and their respective properties. 

#### 3.1.2.9. The epilogue

The epilogue should give license information, acknowledgments, and references.

The epilogue may contain `text` characters or `newline`.
If other characters appear, a [**SCHEMA_CHARACTER_INVALID**](./Appendix_B.md#schema_character_invalid) error occurs.


### 3.1.3. Naming conventions

The different parts of the HED schema have different rules 
for the characters and the names that are allowed. 



#### 3.1.3.1. Node elements

Schema designers and users that extend HED schema or develop library
schema will be mainly concerned with nodes (tag terms) found in the schema section.
The names of these elements must conform to the rules for
[`nameClass`](./Appendix_A.md#a13-value-classes).

Other conventions and requirements for the contents of schema node elements
are as follows:   


````{admonition} Naming conventions for nodes (tag terms) in HED schema. 
:class: tip
1. By convention, the first letter of a schema node (tag term) should be capitalized with the remainder lower case. 
2. Schema node names consisting of multiple words should not not contain blanks and should be hyphenated.
3. Schema descriptions should be concise sentences, possibly with clarifying examples.
4. Schema descriptions may include only `text` characters but should not contain `newline` or
square brackets or braces.
````

#### 3.1.3.2. Epilogue and prologue
The epilogue and prologue section text must conform to the rules for
[`text`](./Appendix_A.md#a13-value-classes) value.
The section text may have new lines, which are preserved.

#### 3.1.3.3. Naming in other blocks

The names of elements corresponding to schema attributes, schema properties, 
unit classes, and value classes should start with a lower case letter,
with the remainder in camel case.

Units and unit modifiers follow the naming conventions of the units they represent.

Case is preserved for unit modifiers, as uppercase and lowercase versions often have distinct meanings. The case for unit symbols is also maintained.


### 3.1.4. MediaWiki schema format

[**MediaWiki**](https://www.mediawiki.org/wiki/Cheatsheet) is a markdown-like format that was
selected as the HED schema editing format because of its flexibility
and ability to represent nested or hierarchical relationships.

The format is line-oriented, so each schema entry should be on a single line.

The schema must follow the layout described in the previous section.
All sections are required, although they may be empty.

Top nodes in the schema are enclosed by pairs of three single quotes (`'''`).
The levels of other nodes are designated by the number of asterisks (`*`) at the beginning of the respective defining lines.
Each term is separated from its level-indicating asterisks by a single space.

Descriptions, which are enclosed in square brackets (`[ ]`),
indicate the meaning of the item they modify.
The descriptions are displayed to users by schema browsers and other tools,
so every effort should be made to make them informative and clear.

Attributes are enclosed with curly braces (`{ }`).
These attributes provide additional rules about how the item and 
modifying values should be used and handled by tools.

If an attribute or property is referenced in the schema,
it must be defined in the appropriate definition section of the schema,
or schema processing tools will generate a [**SCHEMA_ATTRIBUTE_INVALID**](./Appendix_B.md#schema_attribute_invalid) error.

Allowed HED node attributes include unit class and value class values as well as
HED schema attributes that do not have one of the following modifiers:
`unitClassProperty`, `unitModifierProperty`, `unitProperty`, or `valueClassProperty`.
Note: schema attributes having the `elementProperty` may apply anywhere in the
schema, including the schema header,
schema attributes having the `nodeProperty` may only apply to node elements.

HED schema attributes that have the `boolProperty` appear with just their name
in the schema element they are modifying.
The presence of such an attribute indicates that it is true or present.

HED schema attributes that do not have the `boolProperty` are specified in the form of a
`name=value` pair.
If multiple values of a particular attribute are applicable,
they should be specified as name-value pairs separated by commas within the curly braces.

The following example shows a simple HED schema in `.mediawiki` format.

````{admonition} **Example:** Example HED schema in .mediawiki format.

```tid
HED version="8.0.0" 

'''Prologue'''
This prologue introduces the schema.

!# start schema
'''Event''' <nowiki>[Something that happens at a given place and time.]</nowiki>
* Sensory-event <nowiki>{suggestedTag=Task-event-role,suggestedTag=Sensory-presentation}[Something perceivable by an agent.]</nowiki>
                              . . .
'''Property'''<nowiki>{extensionAllowed}[A characteristic.] </nowiki>
* Informational-property <nowiki>[A quality pertaining to information.]</nowiki>
** Label <nowiki>[A string of 20 or fewer characters.]</nowiki>
*** <nowiki># {takesValue}</nowiki> 
!# end schema

'''Unit classes''' <nowiki>[Unit classes and units for the nodes.]</nowiki>
                        . . .
'''Unit modifiers''' <nowiki>[Unit multiples and submultiples.]</nowiki>
                       . . .
'''Value classes''' <nowiki>[Rules for the values provided by users.]</nowiki>
                       . . .
'''Schema attributes''' <nowiki>[Allowed node attributes.]</nowiki>
* extensionAllowed <nowiki>{boolProperty}[Attribute indicating that users can add child nodes.]</nowiki>
* suggestedTag <nowiki>[Attribute indicating another tag that is often associated with this tag.]</nowiki>
* takesValue <nowiki>{boolProperty}[Attribute indicating a placeholder to be replaced by a user-defined value.] </nowiki> 
                        . . .
'''Properties''' <nowiki>[Properties of the schema attributes.]</nowiki>
* boolProperty <nowiki>[Indicates a schema attribute represents a boolean.]</nowiki>
                        . . .
'''Epilogue'''
An optional section that is the place for notes and is ignored in HED processing.

!# end hed
```

````


In the above example, `Property` in the `schema` section is a top node because it appears
enclosed by three single quotes, while `Informational-property` is a first-level node
because its defining line begins with a single asterisk (`*`).

`Sensory-event` in the `schema` section has a `suggestedTag` attribute (shown in curly braces).
Similarly, `Property` has an `extensionAllowed` attribute, and the `#` placeholder has a `takesValue` attribute.
The `schema attributes` section must include definitions of `suggestedTag,`
`extensionAllowed` and `takesValue` or the schema will not validate.

The definition of the `takesValue` attribute has `boolProperty`,
so a definition of `boolProperty` must be included in the `Properties` section 
or the schema will not validate.

Everything after each HED node (tag term) must be enclosed by `<nowiki></nowiki>` markup elements.
The contents within these markup elements include the description and attributes.

Within the HED schema a `#` node indicates that the user must supply a value
consistent with the unit and value class attributes of the `#` node during annotation.
Lines with hashtag (`#`) placeholders should have
everything after the asterisks, including the `#` placeholder, enclosed by `<nowiki></nowiki>` markup elements.


Additional details and rules can be found in appendix
[**A.2 MediaWiki file format**](./Appendix_A.md#a2-mediawiki-file-format)

### 3.1.5. XML schema format

The `.xml` format directly mirrors the order and information in the `.mediawiki` version of the schema.

The `<node>` elements of the schema represent the HED tags (tag terms),
with remaining schema elements specifying additional information and properties.

Each `<node>` element must have a `<name>` child element corresponding to the HED tag term 
that it specifies.

A `<node>` element should also have a `<description>` child element whose content 
corresponds to the text that appears in square brackets (`[ ]`) in the `.mediawiki` version. 

The schema attributes, which appear as `name` values or `name-value` pairs enclosed in 
curly braces (`{ }`) in the `.mediawiki` file, are translated into `<attribute>` child elements
of `<node>` in the `.xml`. These `<attribute>` elements always have a `<name>` element child
and also have a `<value>` element if the corresponding schema attribute does not have `boolProperty`.

The following is a translation of the `.mediawiki` example from the previous section in the HEDXML format.

````{admonition} **Example:** XML version of the example schema in the previous section.

```xml
<?xml version="1.0" ?>
<HED version="8.0.0">
    <prologue>This prologue introduces the schema.</prologue>
    <schema>
        <node>
           <name>Event</name>
           <description>Something that happens at a given place and time.</description>
           <node>
               <name>Sensory-event</name>
               <description>Something perceivable by an agent.</description>
               <attribute>
                   <name>suggestedTag</name>
                   <value>Task-event-role</value>
               </attribute>
           </node>
        </node>
                         . . .
        <node>
            <name>Property</name>
            <description>A characteristic of some entity.</description>
            <attribute>
                <name>extensionAllowed</name>
            </attribute>
            <node>
                <name>Informational-property</name>
                <description>A quality pertaining to information.</description>
                <node>
                    <name>Label</name>
                    <description>A string of less than 20.</description>
                    <node>
                        <name>#</name>
                        <attribute>
                            <name>takesValue</name>
                        </attribute>
                    </node>
                </node>
            </node>
        </node>
    </schema>
    <unitClassDefinitions></unitClassDefinitions>
    <unitModifierDefinitions></unitModifierDefinitions>
    <valueClassDefinitions></valueClassDefinitions>
    <schemaAttributeDefinitions>
        <schemaAttributeDefinition>
            <name>extensionAllowed</name>
            <description>Attribute indicating that users can add child nodes.</description>
            <property>
                <name>boolProperty</name>
            </property>
        </schemaAttributeDefinition>
        <schemaAttributeDefinition>
            <name>suggestedTag</name>
            <description>Attribute indicating another tag that is often associated with this tag.</description>
        </schemaAttributeDefinition>
        <schemaAttributeDefinition>
            <name>takesValue</name>
            <description>Attribute indicating a placeholder to be replaced by a user-defined value.</description>
            <property>
                <name>boolProperty</name>
            </property>
        </schemaAttributeDefinition>
    </schemaAttributeDefinitions>
    <propertyDefinitions>
        <propertyDefinition>
             <name>boolProperty</name>
             <description>Attribute indicating a placeholder to be replaced by a user-defined value.</description>
        </propertyDefinition>
    </propertyDefinitions>
    <epilogue>This epilogue is a place for notes and is ignored in HED processing.</epilogue>
</HED>
```
````


Additional details and rules can be found in appendix
[**A.3 XML file format**](./Appendix_A.md#a3-xml-file-format)

## 3.2. Annotation formats

**HED annotations** are comma-separated strings of HED tags 
drawn from a HED schema vocabulary. 
HED validators and other tools use the information encoded in the relevant schema when 
performing validation and other processing of HED annotations.

Users must provide the version of the HED schema they are using when creating an annotation.

### 3.2.1. Vocabulary organization

HED (Hierarchical Event Descriptors) are nodes (tag terms) organized hierarchically under their
respective root or **top nodes**.
In HED versions >= 8.0.0 these top nodes are:
`Event`, `Agent`, `Action`, `Item`, `Property`, and `Relation`.
Each top node and its subtree represent distinct **is-a** relationships
for the vocabulary schema.

The `Event` subtree tags indicate the general event category, such as whether it 
is a sensory event, an agent action, a data feature, or an event indicating experiment control or structure.

The HED annotations describing each event may be assembled from a 
number of sources during processing and the annotations associated with a single event
marker may represent multiple events.

Many analysis tools use the `Event` tags as a primary means of 
segregating, epoching, and processing the data.
Ideally, tags from the `Event` subtree should appear at the top level of the
HED annotation describing an event to facilitate analysis.

The `Agent` subtree tags indicate the types of agents (e.g., persons, animals, avatars)
that take an active role or produce a specified effect. An `Agent` tag should be 
grouped with property tags that provide information about the agent, such as 
whether the agent is an experiment participant.

The `Action` subtree tags indicate actions performed by agents. Generally these are
grouped in a triple (`A`, (`Action`, `B`)) which is interpreted as `A` does `Action` on `B`. 
If the action does not have a target, it should be annotated (`A`, (`Action`)), meaning
`A` does `Action`.

The `Item` subtree tags represent things with (actual or virtual) physical existence
such as objects, sounds, or language. 

Descriptive tags are organized in the `Property` subtree. These descriptive
tags should always be grouped with the tags they describe using parentheses. 

Binary relations are in the `Relation` subtree. Like items from the `Action` subtree,
these should be annotated using (`A`, (`Relation`, `B`)).


### 3.2.2. Tag forms

A **HED tag** is a term in the HED vocabulary identified by a path consisting of the 
individual node names from some branch of the HED schema hierarchy
separated by forward slashes (`/`).

Valid HED tags do not have leading or trailing forward slashes (`/`).
A HED tag path may also not have consecutive forward slashes.

An important requirement of third generation HED (versions >= 8.0.0)
is that the node names in the HED schema **must be unique**. 
As a consequence, the user may specify as much of the path to the root as desired
when using the tag in annotation.

The full path version is referred to as **long form**,
and the version with only the final tag element
(excluding placeholder) is called **short form**.

Any **intermediate form** of the tag path is also allowed as illustrated by this example:


````{Admonition} Examples of allowed forms of HED tags with and without values. 
| Short-form |  Intermediate form(s) | Long-form |
| -----------|  ------------------ |--------- |
| *Cough*  |  *Move/Breathe/Cough*<br/> *Breathe/Cough* | *Action/Move/Breathe/Cough* |
| *Weight/3 lbs* | *Data-property/Data-value/Physical-value/Weight/3 lbs*<br/> *Data-value/Physical-value/Weight/3 lbs*<br/> *Physical-value/Weight/3 lbs* | *Property/Data-property/Data-value/Physical-value/Weight/3 lbs* | 
````

HED tools are available to map between shortened and long forms as needed. 
The tag must be associated with a schema and must correspond to a path in the schema
(excluding any extension or value).

See [**TAG_INVALID**](./Appendix_B.md#tag_invalid) for errors involving
forward slashes (`/`), extra white-space, and other types of tag syntax errors.

### 3.2.3. Tag case-sensitivity

Although by convention tag terms start with a capital letter with the remainder being lower case,
tag processing is case-insensitive.
This convention makes annotation strings more readable and is recommended
for tag extensions.
Validators and other tools must treat tags containing the same characters,
but different variations in capitalization as equivalent.

The only exception to the case-insensitive processing rule is that the correct case of unit symbols
or unit modifiers should be preserved, both during schema processing and during annotation processing.
This rule is required because SI distinguishes symbols and unit modifiers
that differ in case.

### 3.2.4. Tags that take values

A HED tag that takes a value corresponds to a schema node whose unique child is a `#` leaf node.
The actual schema `takesValue` attribute appears on the `#` placeholder 
rather than on the tag itself.

These tags may appear with or without a value. 
When used with a value, the tag term is followed by a slash,
followed by a value.

A placeholder or its direct parent tag  may not be extended in any other way.
Thus, tags that have placeholder children cannot be extended even
if they inherit an `extensionAllowed` attribute from an ancestor.
The parsers treat any child of these tags as a value substituted for the
placeholder rather than as a tag extension.

If a `unitClass` is specified as an attribute of the `#` node, then the units specified 
must be valid units for that `unitClass`.

The characters that may be used in the value that replaces the `#` placeholder must be
in the union of the values allowed by the `valueClass` attributes of the`#` node.
If units are given, they may place additional restrictions on the allowed values.

Units with the `unitPrefix` attribute, such as `$`, appear before the value. Units without the `unitPrefix` attribute appear after the value.
**HED parsers assume that units are separated from values by a single blank regardless of the position of the units.**

Some unit classes have the `defaultUnits` attribute specifying the units
that downstream analysis tools should assume if units are omitted.

Additional checks may be made on the substituted values depending on the `valueClass`.
For example `numericClass` values must be valid floating point numbers and `dateTimeClass` 
values must be valid ISO8601 values conforming to the 
[**BIDS data-time requirements**](https://bids-specification.readthedocs.io/en/stable/glossary.html#datetime-formats).

The values of HED tag placeholders cannot stand alone,
but must include the parent when used in a HED string. 
For example, the `Label` node in the HED schema has the `#` child.
Thus, the value `myLabel` meant to
substitute for the `#` child of the `Label` node must include `Label` term when used in a HED tag
(e.g., `Label/myLabel` not `myLabel`).

The values substituted for `#` may themselves be schema node names provided they conform with any
value class requirements associated with that `#`.
Thus, `Label/Item` is a valid HED tag event though `Item`, itself, is a valid top tag.
It is the `Label` tag with its value `Item` and is unrelated to the `Item` HED tag.
However, `Data-maximum/Item` is not valid because
the `#` child of `Data-maximum` has a `valueClass=numericClass` attribute
and the `Item` value is not numeric.

Certain unit classes allow other special characters in their value specification. 
These special characters are specified in the schema with the `allowedCharacter` attribute. 
An example of this is the colon in the `dateTimeClass` value class.

See [**VALUE_INVALID**](./Appendix_B.md#value_invalid) and
[**UNITS_INVALID**](./Appendix_B.md#units_invalid) for information
on the specific validation errors associated with tags that take values.

### 3.2.5. Tag extensions
A tag extension, in contrast to a value, is a tag that users add
as a child of an existing schema node as a more specific term for an item already in the schema.
For example, a user might want to use `Helicopter` instead of the more general term `Aircraft`.
Since `Aircraft` inherits the `extensionAllowed` attribute,
users may use extended tags such as `Aircraft/Helicopter` in their annotation.
The requirements for such an extension are:

````{warning} **Requirements for tag extensions by users:**

1. Unlike values, an extension term must not already be a node in the schema.
2. The extension term contain only `name` characters. Blanks should be avoided.
3. The parent of the tag extension must always be included with the extended tag in annotation.
4. The extension term must satisfy the "is-a" relationship with its parent node.
5. The `#` placeholder cannot be used as an extension -- in particular it cannot be used as a placeholder in definitions or as value annotations in sidecars.

**Note:** The is-a relationship is not checked by validators.
It is needed so that term search works correctly.

```` 

Tag extensions should follow the same naming conventions as
those for schema nodes. 
See [**3.1.3. Naming conventions**](#313-naming-conventions) for more information about HED naming conventions.
A [**STYLE_WARNING**](Appendix_B.md#style_warning) is
issued for extension tags that do not follow the HED naming convention.

Users should not use tag extension unless necessary for their application,
as this breaks the commonality among annotations across datasets.
Please open an [**issue**](https://github.com/hed-standard/hed-examples/issues)
proposing that the new term be added to the schema in question,
if you think the term would be useful to other users.

See [**TAG_EXTENSION_INVALID**](./Appendix_B.md#tag_extension_invalid) 
for information on the specific validation errors associated invalid tag extensions.

**Note:** User tag extensions are sometimes accidental and due to misspelling,
particularly when a long or intermediate form of the tag is used.
For this reason the [**TAG_EXTENDED**](./Appendix_B.md#tag_extended)
warning is issued for extended tags during validation.

### 3.2.6. Tag namespace prefixes

Users may select tags from multiple schemas, 
but additional schemas must be included in the HED version specification.

Users are free to use any alphabetic prefix and associate it with a specific
schema in the HED version specification.
Tags from the associated schema must be prefixed with this namespace designator (including the colon)
when used in annotation.

Terms from only one schema can appear in the annotation without a namespace prefix followed by a colon.

See [**TAG_NAMESPACE_PREFIX_INVALID**](./Appendix_B.md#tag_namespace_prefix_invalid) 
for information on the specific validation errors associated with missing schemas.

See [**7.5. Library schema in BIDS**](./07_Library_schemas.md#75-library-schemas-in-bids) for an example of how the
namespace prefix notation is used in BIDS.


### 3.2.7. Strings and groups

A **HED string** is an unordered, comma-separated list of HED tags and/or HED tag groups.

A **HED tag group** is an unordered,
comma-separated list of HED tags and/or tag groups enclosed in parentheses. 
Tag groups may include other tag groups.

The validation errors for HED tags and HED strings are summarized in
[**Appendix B: HED errors**](Appendix_B.md#b-hed-errors).

#### 3.2.7.1. Parenthesis and order

Any ordering of HED tags and HED tag groups at the same level within a HED string is equivalent.
Valid HED strings may have parentheses nested to arbitrary levels (nested groups).
The parentheses must be properly nested and matched.

Parentheses are meaningful and convey association.
If `A` and `B` represent HED expressions, (`A`, `B`) is not equivalent to
the HED string `A`, `B`. 
The distinction should be preserved if possible.
(`A`, `B`) means that HED tag `A` and HED tag `B` are associated with each other,
whereas `A`, `B` means that `A` and `B` are each annotating some larger construct.

Specific rules of association will be encoded in a future version of the HED specification.

See [**PARENTHESES_MISMATCH**](./Appendix_B.md#parentheses_mismatch)
for validation errors result from improper use of parentheses.


#### 3.2.7.2. Tag group attributes

A HED tag corresponding to a schema node with the `tagGroup` attribute
must appear inside parentheses (e.g., must be in HED tag group).

A HED tag corresponding to a schema node with the `topLevelTagGroup` must appear
in an unnested HED group in an assembled HED annotation.
Only one tag with the `topLevelTagGroup` attribute may appear in the same
top-level group.
The `topLevelTagGroup` attribute is usually associated with tags
that have special meanings in HED such as `Definition` and `Onset`.

See [**TAG_GROUP_ERROR**](./Appendix_B.md#tag_group_error) for
information on the group errors detected based on schema attributes.

#### 3.2.7.3. Empty tags and groups

Empty parentheses and multiple commas with no intervening tags represent empty tags and are invalid,
as are HED strings with leading or trailing commas.
Hence, if `A` and `B` are any HED expressions,  
(`A`, ((`B`))) is valid but (`A`, ()) is not.

See [**TAG_EMPTY**](./Appendix_B.md#tag_empty) for
information on the validation errors due to empty tags or groups.
Some of these errors may be reported as 
[**COMMA_MISSING*](./Appendix_B.md#comma_missing)


#### 3.2.7.4. Repeated expressions

Duplicated tag expressions at the same level in a 
HED tag group or HED string are not allowed.
For example, the expressions (`Red`, `Blue`, `Red`) and
(`Red`, `Blue`), (`Red`, `Blue`) have duplicated tag expressions at the same
level and are hence invalid.

See [**TAG_EXPRESSION_REPEATED**](./Appendix_B.md#tag_expression_repeated) for
more details on validation errors due to repeated tag expressions.


### 3.2.8. Special tags

#### 3.2.8.1. The `Definition` tag

A HED definition is a tag group consist of a `Definition` tag that takes
a value representing the definition's name and a tag group defining the concept.
Each definition is independent and stands alone.
The definition must contain a non-empty tag group.

The `Definition` tag corresponds to a schema node with the `topLevelTagGroup` attribute,
assuring that definitions cannot be nested. 

HED definitions may not contain any `Def` or `Def-expand` tags and must contain
exactly one `Definition` tag.
Multiple definitions with the same definition name are not allowed.

The `Definition` tag must be extended with a 
value representing the definition name and may
be additionally extended by a `#` placeholder.
If the definition name includes the `#` placeholder extension, 
then the defining tags must
include exactly one tag that takes a value along with its `#` placeholder.

Definitions with the same name are considered duplicate definitions regardless of 
whether one has a placeholder and another does not.
**However, each distinct substituted value represents a distinct definition name for
purposes of `Onset`/`Offset` processing.**

See [**DEFINITION_INVALID**](./Appendix_B.md#definition_invalid) for
a listing of situations in which a definition may be invalid.

See also [**Chapter 5.1 Creating definitions**](./05_Advanced_annotation.md#51-creating-definitions) 
for more details and examples.

#### 3.2.8.2. `Def` and `Def-expand` tags

A definition is incorporated into annotations using the tag 
`Def/xxx` where `xxx` is the definition's name.

Alternatively, the annotator may use an expanded form `(Def-expand/xxx, yyy)` 
where `xxx` is the definition's name and `yyy` is a tag group containing
the definitions contents.

The two usages are equivalent, and tools should be able to transform between the two representations.
Note, however, that transforming from a `Def` tag to a `Def-expand` group requires the definition,
while transforming from a `Def-expand` group to `Def` tag does not.

For definitions that include a placeholder, a value must be substituted for 
the `#` placeholder in `Def` tag and `Def-expand` group when final
annotation assembly occurs. 

See [**DEF_INVALID**](./Appendix_B.md#def_invalid) and
[**DEF_EXPAND_INVALID**](./Appendix_B.md#def_expand_invalid)
for details on the types of errors that occur with `Def` and `Def-expand`.

See also [**Using definitions**](./05_Advanced_annotation.md#52-using-definitions)
for more details and examples.

#### 3.2.8.3. `Onset`, `Offset`, and `Inset`

The `Onset` and `Offset` tags are used to represent the temporal extent
of events that have non-zero duration.

Each of these tags must appear in a top level tag group with a
`Def` tag or `Def-expand` group anchor.

A tag group with an `Onset` represents the start of an event that extends over time.
A tag group with an `Offset` represents the end of an event that was previously initiated by an `Onset` group.
A given event of temporal extent is also terminated by the appearance of another
`Onset` group with the same `Def` tag or `Def-expand` group anchor.

The `Onset` tag group may only contain its `Def` tag or `Def-expand` group anchor and
at most one additional inner tag group in addition to the `Onset` tag.

The `Offset` tag group may only contain its `Def` tag or `Def-expand` group anchor in
addition to the `Offset` tag.

These requirements imply that `Onset` and `Offset` must be the only tags
in their tag group with the `topLevelTagGroup` attribute.
`Onset` and `Offset` tags correspond to schema nodes with the `topLevelTagGroup` attribute.
This implies, for example, that HED definition's contents may not include 
`Onset` or `Offset` tags. 

An `Inset` tag designates an intermediate time point in an event of temporal extent. 
Like `Onset` and `Offset`, the `Inset` tag has the  `topLevelTagGroup` attribute
and must be anchored by a `Def` or `Def-expand`.
The anchor must be the same name as that of an ongoing `Onset`.
In addition to its anchor, the `Inset` tag group may contain a single additional
tag group with additional information about that marked point.
An event of temporal extent may contain several of these intermediate points.

See [**TEMPORAL_TAG_ERROR**](./Appendix_B.md#temporal_tag_error) and 
 [**TAG_GROUP_ERROR**](./Appendix_B.md#tag_group_error) and
for a listing of specific errors associated with onsets, and offsets, and insets.

[**Chapter 5.3.1 Using Onset and Offset**](./05_Advanced_annotation.md#531-using-onset-and-offset)
in Chapter 5 gives examples of usage and additional details.


#### 3.2.8.4. The `Event-context` tag

The `Event-context` tag corresponds to a schema node with both the `topLevelTagGroup` and `unique` attributes.
This implies that there can be only one `Event-context` group in each assembled event-level HED string.
The `Event-context` group contains information about what other events are ongoing at the time point
associated with the event marker for which the annotation is included.

In general, the `Event-context` group is not included in annotations, but is generated by tools during
downstream event processing. 

See [**TAG_GROUP_ERROR**](./Appendix_B.md#tag_group_error) and
[**TAG_NOT_UNIQUE**](./Appendix_B.md#tag_not_unique) for additional information
on validation errors related to `Event-context`.

Additional details and examples for `Event-context` can be found in
[**5.5. Event contexts**](./05_Advanced_annotation.md#55-event-contexts).

### 3.2.9. Sidecars

JSON sidecars are an integral part of the [**BIDS**](https://bids.neuroimaging.io/)
(Brain Imaging Data Structure) neuroimaging standard and are used to associate
metadata with data files.

The JSON sidecars that are relevant to HED are associated with tabular data files.
For example, the rows of tabular event files represent time markers on the experimental timeline,
and the assembled HED annotations for each row describe what happened at that time marker.
A sidecar containing annotations associated with the columns of such an event file
allows HED tools to assemble HED annotations for each row of the file.

In addition to sidecars, HED annotations can also be given in the `HED` column of tabular files.
At validation or analysis time the HED information from both the `HED` column of a tabular file
and its associated sidecar are assembled to provide the annotation.

HED validators assume that the annotation dictionary is saved in JSON format and 
that they comply with the
[**BIDS sidecar**](https://bids-specification.readthedocs.io/en/stable/appendices/hed.html) format.

#### 3.2.9.1. Sidecar entries

A BIDS sidecar is a JSON dictionary with several types of entries, three of which are relevant to HED:


````{Admonition} Three types of JSON sidecar HED-related entries. 
**Categorical entries**
- The top-level JSON key corresponds to a column name in the event file.
- The value associated with the HED key is a dictionary of HED annotations.
- The keys of the annotation dictionary are the unique column values.
- The entry is not required to have annotations for every possible unique column value.
- Tools may choose to issue a warning if a column value does not have an annotation.
- The annotation dictionary may include annotations for values that do not appear in a particular event file.  


**Value entries**:
- The top-level JSON key corresponds to a column name in the event file.
- The value associated with the HED key is a HED string.  
- The entry's annotation is applicable to all values in its associated event file column.  
- The HED annotation must contain a single `#` placeholder.  
- Each row's column value is substituted for the `#` in the annotation
when the row annotation is assembled.

**Dummy entries**:
- The top-level JSON key must not correspond to a column name in the event file.
- The value associated with the HED key is a dictionary of HED annotations.
- The keys are dummy entries.
- Used to gather HED definitions.

````

The other types of sidecar entries include categorical and value
entries with no `"HED"` key, as well as arbitrary entries
whose keys do not correspond to column names in an associated tabular file.

When annotations are assembled, sidecar entries with no `"HED"` key are ignored
as are entries in the corresponding tabular data file that have `n/a` or blank values.

See [**3.2.9.4. A sidecar example**](./03_HED_formats.md/#3294-a-sidecar-example)
for an elaborated example of these different types of entries and
[**3.2.10.2 Event-level processing**](./03_HED_formats.md/#32103-event-level-processing)
for an example of how the resulting HED annotations are assembled.

#### 3.2.9.2. Sidecar validation

All HED-related entries in a JSON sidecar must 
have `"HED"` as a key in a second-level dictionary.
`"HED"` cannot appear as a sidecar key that is not at the second level.
Further, a sidecar is not permitted to provide a HED annotation for `n/a`.
Both of these generate a [**SIDECAR_INVALID**](./Appendix_B.md#sidecar_invalid) error.

HED definitions are required to be separated into dummy sidecar column entries
and cannot appear in sidecar entries containing tags other than definitions.
A HED definition appearing in a categorical or value sidecar entry 
generates a [**DEFINITION_INVALID**](./Appendix_B.md#definition_invalid) error.

The sidecar does not have to provide a HED-relevant entry for every event file column.
Columns with no corresponding sidecar entry are skipped during assembly of the 
HED annotation for an event file row.
However, if a value is encountered in a tabular file column that is
annotated as a categorical column but does not have a HED annotation,
a [**SIDECAR_KEY_MISSING**](./Appendix_B.md#sidecar_key_missing) warning is generated.

HED value sidecar entries must contain exactly one `#` placeholder in 
the HED string annotation associated with the entry.
The `#` placeholder should correspond to a `#` in the HED schema,
indicating that the parent tag (also included in the annotation) expects a value.
These issues generate a [**PLACEHOLDER_INVALID**](./Appendix_B.md#placeholder_invalid) error.

If the placeholder is followed by a unit designator, the validator checks that 
these units are consistent with the unit class of the
corresponding `#` in the schema.  The units are not mandatory.

#### 3.2.9.3. Sidecar curly braces

The curly brace notation is new with HED specification version 3.2.0 and is 
supported by all versions of the HED schema &ge; 8.0.0.
The notation was introduced to
facilitate proper nesting of HED tags associated with different event file
columns when the complete HED annotation for an event marker is assembled.

When a column name appears in curly braces within a HED annotation in
a JSON sidecar, the corresponding HED annotation for that row is substituted
for the curly braces and their contents when the HED annotation is assembled.


``````{admonition} Rules for curly braces notation in sidecars.
:class: tip

1. The item within the curly braces must either be the word `HED` or
the name of another HED-annotated column within the sidecar.
2. The HED annotation for the column in curly braces directly replaces the curly braces and their contents in the target annotation.
3. During assembly of a HED annotation for an event, if the 'n/a' value appears in a curly brace column,
the curly brace expression including the curly braces as well as any extra parentheses or commas are removed. 
4. A sidecar column name cannot both appear in a curly braces and have
an annotation that uses curly braces (to prevent circular references).
5. The curly braces cannot be used within a `Definition`.
6. Curly braces can not appear in the HED column of a tabular file.
7. Curly braces can not be nested. 
8. A pair of curly braces must appear syntactically as a tag and not as the substitution for a place holder.

``````

If curly braces appear in the HED column of a tabular file,
a [**CHARACTER_INVALID**](./Appendix_B.md#character_invalid) error is generated. 

If curly braces appear in a `Definition`,
a [**DEFINITION_INVALID**](./Appendix_B.md#definition_invalid) error is generated. 

If the curly brace notation is used improperly in a sidecar or elsewhere, a
[**SIDECAR_BRACES_INVALID**](./Appendix_B.md#sidecar_braces_invalid) is generated.


#### 3.2.9.4. A sidecar example

The following example illustrates the different types of JSON sidecar entries.

(example-sidecar-anchor)=
````{Admonition} Different types of sidecar annotation entries that might appear in 
:class: tip
```json
{
   "event_type": {
      "LongName": "Event category",
      "Description": "Indicator of type of event.",
      "Levels": {
          "show": "Show a face to a participant.",
          "press": "Participant presses key to indicate symmetry."
       },
      "HED": {
          "show": "Sensory-event, Visual-presentation, {stim_file}",
          "press": "Agent-action, (Experiment-participant, (Press, {key}))"
       }
   },
   "stim_file": {
       "LongName": "Stimulus image file",
       "Description": "Time from stimulus presentation until subject presses button",
       "HED": "(Image, Face, Pathname/#)"
   },
   "key":   {
       "LongName": "Indicates which key is pressed.",
       "Description": "Indicator of participant evaluation.",
       "HED": {
          "left-arrow": "((Leftward, Arrow), Keypad-key)",
          "right-arrow": "((Rightward, Arrow), Keypad-key)"
       }
   },
   "symmetry":   {
       "LongName": "Indicates symmetrical or asymmetrical.",
       "Description": "Indicates the participant's judgement of symmetry.",
       "HED": {
          "symmetric": "(Judge, Asymmetrical)",
          "asymmetric": "(Judge, Symmetrical)"
       }
   },

   "dummy_defs": {
        "HED": {
            "MyDef1": "(Definition/Cue1, (Buzz))",
            "MyDef2": "(Definition/Image/#, (Image, Face, Label/#))"
        }
   }
}
```
````

In the example, `"event_type"` is the name of a column that is annotated using the
**categorical** strategy.
Its top-level dictionary has `"LongName"`, `"Description"`, `"Levels"`, and `"HED"` keys.

The value of `"Levels"` is a dictionary with the unique values in the `"event_type"` 
column keyed to full text descriptions of these unique values.

The value of `"HED"` is a dictionary with the unique values in `"event_type"`
keyed to the corresponding HED annotations of these unique values.
In the above example, the unique values are `"show"` and `"press"`.
The HED annotation for `show` is `"Sensory-event, Visual-presentation, {stim_file}"`.

Notice use of curly braces in the notation. Here `"stim_file"` must
correspond to another HED-annotated column in the sidecar.
The `"stim_file"` column is an example of a value column.
Its top level dictionary keys are `"LongName"`, `"Description"`, and `"HED"`.
and its annotation entry:
`"(Image, Face, Pathname/#)"`.
This annotation has a single `#`. 
The filename in the `stim_file` column replaces this `#` when the HED annotation for a
line in an associated `events.tsv` file is assembled.

Since `"stim_file` and `"key"` appear within curly braces in annotations
for `"event_type"`, their HED annotations can not use curly braces.


The `"dummy_defs"` is an example of a **dummy annotation**.
The value of this entry is a dictionary with a `"HED"` key
pointing to a dictionary.
A dummy annotation is similar in form to a **categorical annotation**,
but its keys do not correspond to any event file column values.
Rather it is used as a container to organize HED definitions.

In the example,
`Definition/Cue1` is a definition that does not use a placeholder (`#`) modifier in its name,
while `Definition/Image/#` is a definition whose name `Image` is modified by a placeholder value.
Notice that `Image` is both a definition name and an actual tag in the schema in this example.
This is permitted.


### 3.2.10. Tabular files

A tabular (`.tsv`) file is a text file in which each line represents a row in a table.
The column entries in a given row are separated by tabs. 
The first line of the file must contain a tab-separated list of
column names, which should be unique.
This description of tabular files conforms to that used by [**BIDS**](https://bids.neuroimaging.io/).

#### 3.2.10.1 Tabular types

Generally each row in a tabular file represents an item and the columns values provide properties of that item.
The most common HED-annotated tabular files represent event markers in an experiment (e.g., BIDS `events.tsv` files).
In this case each row represents a time at which something happened.

Another common HED-annotated tabular file represents experiment participants
(e.g., BIDS `participants.tsv`).
Each row in the file represents a participant, and the columns provide
characteristics or other information about the participant identified in that row.

The `events.tsv` files are tabular files representing markers on a timeline.
This type of tabular file must have `onset` as the first column,
and HED tools use the time values in this column to resolve `Onset`, `Offset` and `Inset`.
In contrast, the `participants.tsv` file, which contains information about the
experimental participants, is representative of a non time-marker file.
Non time-marker files cannot use the `Onset`, `Offset`, or `Inset` tags as these
tags are reserved for annotations of time processes and cannot be resolved if there is no time.

In any case, the general strategy for validation or other processing is:
1. Process the individual components of the HED annotation (tag-level and string-level processing).
2. Assemble the component annotations for a row (event-level or row-level processing).
3. Check consistency and relationships among the row annotations (file-level processing).

See [**BIDS tabular files**](06_Infrastructure_and_tools.md#631-bids-tabular-files) for
more examples.

#### 3.2.10.2. Tabular annotations

HED annotations in tabular files can occur both in a `HED` column within the file and
in an associated JSON sidecar.

The HED strings that appear in a `HED` column must be valid HED strings.
If the first column is not called `onset`, the assembled annotation for
the tabular file cannot contain any of the tags `Onset`, `Offset`, or `Inset`.

Definitions many not appear in the `HED` column of a tabular file or
in any entry of a JSON sidecar that contains items other than definitions.

See [**DEFINITION_INVALID**](./Appendix_B.md#definition_invalid)
and [**TEMPORAL_TAG_ERROR**](./Appendix_B.md#temporal_tag_error) for information.


#### 3.2.10.3. Event-level processing

After individual HED tags and HED strings in the `HED` column of tabular files and 
in the associated sidecars are validated or otherwise processed,
the HED strings associated with each row of the tabular file must be assembled to provide an overall
annotation for the row.
We refer to this as *event-level* or *row* processing.

If the HED schema used for processing contains a schema node that has the `required` attribute, then
the assembled HED annotations for each row must include that tag.
Currently, HED schema versions &ge; 8.0.0 do not contain any nodes with the `required`
attribute, and this attribute may be deprecated in future versions of the schema.

If the HED schema used for processing contains a schema node that has the `unique` attribute,
then the assembled HED annotations for each row must contain no more than one occurrence of that tag.
Currently, only `Event-context` has the `unique` attribute for HED schema versions &ge; 8.0.0.

See [**REQUIRED_TAG_MISSING**](./Appendix_B.md#required_tag_missing)
and [**TAG_NOT_UNIQUE**](./Appendix_B.md#tag_not_unique) for information
on the validation errors that may occur with tags that have the `required` or `unique`
schema attributes, respectively.

````{Admonition} General procedure for event-level (row) assembly. 

1. Create an empty result list.
2. Create an assembly list of columns that contain HED annotations 
and whose names do not appear in the curly braces of other HED annotations.
3. For each the column in the assembly list look up the annotation in the sidecar, replacing all curly braces and place holder values appropriately.
Append to the result list.
4. If a `HED` column annotation exists for that row and `HED` did not appear
in curly braces in the sidecar, concatenate the annotation to the result list.
5. Finally, join all the entries of the result list using a comma (`,`) separator.

In all cases `n/a` column values are skipped.
````

To illustrate the assembly process, consider the following excerpt from an event file:


````{Admonition} General procedure for event-level (row) assembly. 

| onset | duration | event_type | stim_file | key | symmetry | HED |
| ----- | -------- | ---------- | --------- | --- | -------- | --- |
| 3.42  | n/a   | show  |   h234.bmp  |  n/a |  n/a | "(Recording, Label/Setup)" |
| 3.86  | n/a    | press  |  n/a  |  left-arrow  |  asymmetric | n/a |
| 7.42  | n/a    | show  |   h734.bmp  |  n/a |   n/a | n/a |
````

Using the [**example sidecar**](example-sidecar-anchor) 
results in the following assembled HED annotation for the first row of the event file:

````{Admonition} A result for event-level (row) assembly of the sample file.
:class: tip

```shell
"Sensory-event, Visual-presentation, (Image, Face, Pathname/h234.bmp), (Recording, Label/Setup)"
```
````

The specific annotation `(Image, Face, Pathname/h234.bmp)` has been substituted for
`{stim_file}` and the annotation for in the `HED` column of the `events.tsv` file
has been included. The entries with `n/a` have been ignored.

For more examples of event assembly, see [**How HED works in BIDS**](https://www.hed-resources.org/en/latest/BidsAnnotationQuickstart.html#how-hed-works-in-bids) tutorial.


#### 3.2.10.4. File-level processing

HED versions >= 8.0.0 allow annotation of relationships among rows in a tabular file.
Hence, processing generally requires that annotations for all the rows be assembled
so that consistency can be checked.

To validate temporal scope, the validator must assure that each `Onset` and `Offset` tag 
is associated with an appropriately defined identifier corresponding to a definition name.
The validator must also check to make sure that `Onset` and `Offset` tags are
properly matched within the data recording.
In particular every `Offset` tag group must correspond to a preceding `Onset` tag group.

See [**TEMPORAL_TAG_ERROR**](./Appendix_B.md#temporal_tag_error) for details on the
type of errors that are generated due to `Onset` and `Offset` errors.


## 3.3. Semantic versioning

HED schema use the following rules for
changing the  *major.minor.patch* semantic version.
These rules are based on the assumption that the [**HED tag**](https://hed-specification.readthedocs.io/en/latest/02_Terminology.html#hed-tag) 
short form will not require data annotators to retag their data for patch-level or minor-version changes of the schema.
That is, a dataset tagged using schema version *X.Y.Z* will also validate for *X.Y+.Z+*. 
However, the reverse is not necessarily true.
In addition, validation errors might occur
during for patch-level or minor-version changes for changes or
corrections in tag values or units. 

Here is a summary of the types of changes that correspond to different
levels of changes in the semantic version:

| Change                          | Semantic-level | 
| ---------------------------------- | -------------- |
| Major addition to HED functionality     | Major  |
| Tag deleted from schema.                | Major  |
| Unit or unit class removed from node.   | Major  |
| New tag added to the schema.            | Minor  |
| New attribute added to schema.          | Minor  |
| New unit class or unit added to schema. | Minor  |
| New unit class added to node.           | Minor  |
| Node moved in schema without change in meaning. | Minor |
| Revision of description field in schema.        | Patch   |
| Correction of suggestedTag or relatedTag.       | Patch  |
| Correction of wiki syntax such as closing tags. | Patch |

**Note:** It is an official policy that once in a schema, a node will not be removed.
If a node becomes out-of-date, a `deprecated` attribute will be added to the tag in the schema.
Suggested replacement tags should be included in the node description.
A suggested replacement should be added to the tag patch table.
