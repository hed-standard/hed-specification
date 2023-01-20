(3-hed-formats-anchor)=
# 3. HED formats

This chapter describes the requirements and formats for HED schema and HED annotations.

## 3.1. HED schema format

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
[**A. Schema format details**](./Appendix_A.md)

### 3.1.1 Official schema releases

The HED ecosystem supports a standard base schema and additional discipline-specific
library schemas.
(See the [**expandable schema viewer**](https://www.hedtags.org/display_hed.html)
to explore existing schemas.)

Releases of the HED standard schema are stored in
[**standard_schema/hedxml**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml) 
directory of the [**hed-schemas**](https://github.com/hed-standard/hed-schemas) repository.

Releases of a HED library schema are stored in a subdirectory of
[**library_schemas**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas)
whose name is the library name.

### 3.1.2 Schema layout overview

Schemas can be specified in either `.mediawiki` or `.xml` format.
[**Online tools**](https://hedtools.ucsd.edu/hed/schema) 
provide an easy way for users to validate schema and convert between formats.

HED schema developers usually use `.mediawiki` format for more convenient editing,
display, and viewing on GitHub.
However, tools assume that the schema is in `.xml` format for processing.

Regardless of the format, a valid HED schema has the following sections in this order:

````{Admonition} Sections of a HED schema (in the required order):
| Section   | Mediawiki format | XML format  |
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

See appendix [**A. Schema format details**](./Appendix_A.md) for additional details.

#### 3.1.2.1 The header

The schema header line specifies the version.
If the schema is a library schema rather than the standard schema, the library name must be included.
This may optionally be followed by an XSD namespace specification.

Library names must contain only alphabetic characters and should be short and descriptive.
A schema's library name or lack there of is used to locate the schema in the
HED schema repository located in the
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

Library names should be lowercase.

#### 3.1.2.2 The prologue

The prologue should contain a concise introduction to the schema and its purpose.
Together with the epilogue section, 
the contents are used by tools to provide information about the schema to the users.

#### 3.1.2.3 The schema section

The schema section contains the actual vocabulary contents of the schema.
Each element in this section corresponds to a *node* or *tag term* element.

A node element specifies the tag term name,
its attributes, and an informative description of the tag term's meaning.
The location of the element within the section specifies its relationship to other tag terms in the schema.


#### 3.1.2.4 Unit classes and units

The unit class definition section specifies the allowed unit classes and the 
associated units that can be used with tags that take values and have the unit class as an attribute value.

Only the singular version of each unit is explicitly specified,
but the corresponding plurals of the explicitly mentioned 
singular version are also allowed (e.g., `feet` is allowed in addition to `foot`). 
HED uses a `pluralize` function available in both Python and Javascript to check validity.

See appendix [**A.1.1. Unit classes and units**](./Appendix_A.md#a11-unit-classes-and-units)
for additional details and a listing.

#### 3.1.2.5 Unit modifiers

The unit modifier definition section lists the SI unit multiples and submultiples 
that are allowed to be prepended to units that have the `SIUnit` schema attribute.

**Unit modifiers are case-sensitive.**

See appendix [**A.1.2. Unit modifiers**](./Appendix_A.md#a12-unit-modifiers)
for additional details and a listing of values for the standard schema.

#### 3.1.2.6 Value classes

The value class definition section specifies rules for the values that are substituted 
for placeholders (`#`). Examples are special characters that are allowed for numeric values 
or dates. Placeholders that have no `valueClass` attributes, are assumed to take `textClass` values.

See appendix [**A.1.3. Value classes**](./Appendix_A.md#a13-value-classes)
for additional details and a listing of values for the standard schema.

#### 3.1.2.7 Schema attributes

The schema attribute definition section lists the schema attributes that may be applied to
schema elements in other sections of the schema.

The specification of which type of elements a schema attribute may apply
to is specified by its schema properties.

See appendices [**A.1.4. Schema attributes**](./Appendix_A.md#a14-schema-attributes)
and [**A.1.5. Schema properties**](./Appendix_A.md#a15-schema-properties)
for additional details and a listing for the standard schema.

#### 3.1.2.8 Schema properties

The schema properties definition section lists the allowed properties of the schema attributes.
These properties help tools validate certain requirements directly based
on the HED schema rather than on hard-coded implementation. 

See [**A.1.5. Schema properties**](./Appendix_A.md#a15-schema-properties) for additional details
and a listing for the standard schema.

#### 3.1.2.9 The epilogue

The epilogue should give license information, acknowledgments, and references.


### 3.1.3. Naming conventions

The different parts of the HED schema have different rules 
for the characters and the names that are allowed. UTF-8 characters are not supported.


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
2. Schema node names consisting of multiple words may not contain blanks and should be hyphenated.
3. Schema descriptions should be concise sentences, possibly with clarifying examples.
4. Schema descriptions may include characters allowed by `textClass` as well as commas.
They may not contain square brackets, curly braces, quotes, or other characters.
````

#### 3.1.3.2 Epilogue and prologue
The epilogue and prologue section text must conform to the rules for
[`textClass`](./Appendix_A.md#a13-value-classes) and may not contain commas.

#### 3.1.3.3 Naming in other blocks

The names of elements corresponding to schema attributes, schema properties, 
unit classes, and value classes should start with a lower case letter,
with the remainder in camel case.

Units and unit modifiers follow the naming conventions of the units they represent.

Case is preserved for unit modifiers, as uppercase and lowercase versions often have distinct meanings.


### 3.1.4 Mediawiki schema format

[**Mediawiki**](https://www.mediawiki.org/wiki/Cheatsheet) is a markdown-like format that was
selected as the HED schema editing format because of its flexibility
and ability to represent nested or hierarchical relationships.

The format is line-oriented, so each schema entry should be on a single line.

The schema must follow the layout described in the previous section.
All sections are required, although they may be empty.

Top nodes in the schema are enclosed by pairs of three single quotes (`'''`).
The levels of other nodes is designated by the number of asterisks (`*`) at the beginning of the defining line.
Each term is separated from its level-indicating asterisks by a single space.

Descriptions, which are enclosed in square brackets (`[ ]`),
indicate the meaning of the item they modify.
The descriptions are displayed to users by schema browsers and other tools,
so every effort should be made to make them informative and clear.

Attributes are enclosed with curly braces (`{ }`). These attributes provide
additional rules about how the item and modifying values should be used and handled by tools.
If an attribute or property is referenced in the schema,
it must be defined in the appropriate definition section of the schema,
or schema processing tools will generate an error.

Allowed HED node attributes include unit class and value class values as well as
HED schema attributes that do not have one of the following modifiers:
`unitClassProperty`, `unitModifierProperty`, `unitProperty`, or `valueClassProperty`. 

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
* Sensory-event <nowiki>{suggestedTag=Task-event-role}[Something perceivable by an agent.]</nowiki>
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
[**A.2 Mediawiki file format**](./Appendix_A.md#a2-mediawiki-file-format)

### 3.1.5 XML schema format

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

## 3.2 HED annotation format

**HED annotations** are comma-separated strings of HED tags 
drawn from a HED schema vocabulary. 
HED validators and other tools use the information encoded in the relevant schema when 
performing validation and other processing of HED annotations.

Users must provide the version of the HED schema they are using when creating an annotation.

### 3.2.1 Vocabulary organization

HED (Hierarchical Event Descriptors) are nodes (tag terms) organized hierarchically under their
respective root or **top nodes**.
In HED versions >= 8.0.0 these top nodes are:
`Event`, `Agent`, `Action`, `Item`, `Property`, and `Relation`. 

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
grouped in a triple *(A, (Action, B))* which is interpreted as *A* does *Action* on *B*. 
If the action does not have a target, it should be annotated *(A, (Action))*, meaning
*A* does *Action*.

The `Item` subtree tags represent things with (actual or virtual) physical existence
such as objects, sounds, or language. 

Descriptive tags are organized in the `Property` subtree. These descriptive
tags should always be grouped with the tags they describe using parentheses. 

Binary relations are in the `Relation` subtree. Like items from the `Action` subtree,
these should be annotated using *(A, (Relation, B))*.


### 3.2.2 Tag syntax

A **HED tag** is a term in the HED vocabulary identified by a path consisting of the 
individual node names from some branch of the HED schema hierarchy
separated by forward slashes (/). 

Valid HED tags do not have leading or trailing forward slashes ('/').
A HED tag path many also not have consecutive forward slashes.

An important requirement of third generation HED (versions >= 8.0.0)
is that the node names in the HED schema **must be unique**. 
As a consequence, the user may specify as much of the path to the root as desired
when using the tag in annotation.

The full path version is referred to as **long form**,
and the version with only the final tag element
(excluding placeholder) is called **short form**.

Any **intermediate form** of the tag path is also allowed as illustrated by this example:


````{Admonition} Different allowed forms of HED tags with and without values. 
| Short-form |  Intermediate form(s) | Long-form |
| -----------|  ------------------ |--------- |
| *Cough*  |  *Move/Breathe/Cough*<br/> *Breathe/Cough* | *Action/Move/Breathe/Cough* |
| *Weight/3 lbs* | *Data-property/Data-value/Physical-value/Weight/3 lbs*<br/> *Data-value/Physical-value/Weight/3 lbs*<br/> *Physical-value/Weight/3 lbs* | *Property/Data-property/Data-value/Physical-value/Weight/3 lbs* | 
````

HED tools are available to map between shortened and long forms as needed. 

### 3.2.3. Tag case-sensitivity

Although by convention tag terms start with a capital letter with the remainder being lower case,
tag processing is case-insensitive.
Validators and other tools must treat tags containing the same characters,
but different variations in capitalization as equivalent.

The only exception to the case-insensitive processing rule is that the correct case of units
should be preserved, both during schema processing and during annotation processing.
This rule is required because SI distinguishes units that have different case.

### 3.2.4. Tags that take values

A HED tag that takes a value corresponds to a schema node whose unique child is a `#` leaf node.
The actual schema `takesValue` attribute appears on the `#` placeholder 
rather than on the tag itself.

These tags may appear with or without a value. 
When used with a value, the tag term is followed by a slash,
followed by a value and possibly a blank, followed by units.

Neither a placeholder nor its direct parent tag  may not be extended in any other way.
Thus, tags that have placeholder children cannot be extended even
if they inherit an `extensionAllowed` attribute from an ancestor.
The parsers treat any child of these tags as a value substituted for the
placeholder rather than as a tag extension.

**HED values** may be strings or numeric values followed by an optional unit specification. 
If a `unitClass` is specified as an attribute of the `#` node, then the units specified 
must be valid units for that `unitClass`.

**HED parsers assume that units are separated from values by a single blank.**

The characters that may be used in the value that replaces the `#` placeholder must be
in the union of the values allowed by the `valueClass` attributes of the`#` node.
If units are given, they may place additional restrictions on the allowed values.

Additional checks may be made on the substituted values depending on the `valueClass`

| valueClass  | Additional value checks |
| ----------- | ----------------------- |
| numericClass | Must be a valid floating point number. |
| dateTimeClass | Must be a valid ISO8601 value. |

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

### 3.2.5. Tag extensions
A tag extension, in contrast to a value, is a tag that users add
as a child of an existing schema node as a more specific term for an item already in the schema.
For example, a user might want to use `Helicopter` instead of the more general term `Aircraft`.
Since `Aircraft` inherits the `extensionAllowed` attribute,
users may use extended tags such as `Aircraft/Helicopter` in their annotation.
The requirements for such an extension are:

````{warning} **Requirements for tag extensions by users:**

1. Unlike values, an extension term must not already be a node in the schema.
2. The extension term must only have alphanumeric, hyphen, or underbar characters so that it
conforms to the rules for a *nameClass* value.
3. The parent of the tag extension must always be included with the extended tag in annotation.
4. The extension term must satisfy the "is-a" relationship with its parent node.

**Note:** The is-a relationship is not checked by validators.
It is needed so that term search works correctly.

```` 

Users should not use tag extension unless necessary for their application,
as this breaks the commonality among annotations across datasets.
Please open an [**issue**](https://github.com/hed-standard/hed-examples/issues)
proposing that the new term be added to the schema in question,
if you think the term would be useful to other users.

### 3.2.6. Tag prefixes

Users may select tags from multiple schemas, but additional schema must be included in the
HED version specification.
Terms from only one schema can appear in the annotation without a namespace prefix followed by a colon.
Users are free to use any alphabetic prefix and associate it with a specific
schema in the HED version specification.
Tags from the associated schema must be prefixed with this name (followed by a colon)
when used in annotation.

### 3.2.7. Strings and groups

A **HED string** is an unordered, comma-separated list of HED tags and/or HED tag groups.
The terms in a HED string must be unique, thus, a HED string forms a set.

A **HED tag group** is a comma-separated list of HED tags and/or tag groups enclosed in
parentheses. Tag groups may include other tag groups. 

Any ordering of HED tags and HED tag groups at the same level within a HED string is equivalent.
Valid HED strings may have parentheses nested to arbitrary levels (nested groups).

A HED tag corresponding to a schema node with the `tagGroup` attribute,
must appear inside parentheses (e.g., must be in HED tag group).

Duplicated tags at the same level in a tag-group or at the top level are not allowed.
For example, (`Red`, `Red`, `Blue`) is an invalid HED string.

Empty parentheses and multiple commas with no intervening tags represent empty tags and are invalid,
as are HED strings with leading or trailing commas.

A HED tag corresponding to a schema node with the `topLevelTagGroup` attribute 
must appear within a single level of parentheses.
This attribute is usually associated with tags that have special meanings in HED such
as `Definition` and `Onset`.

Parentheses are meaningful and convey association.
If *A* and *B* represent HED tags, the HED string *(A, B)* is not equivalent to
the HED string *A, B* and the distinction should be preserved if relevant.
*(A, B)* means that HED tag *A* and HED tag *B* are associated with each other,
whereas *A, B* means that *A* and *B* are each annotating some larger construct.

Specific rules of association will be encoded in a future version of the HED specification.

The validation errors for HED tags and HED strings are summarized in
[**Appendix B: HED errors**](Appendix_B.md#b-hed-errors).


### 3.2.8. Special tags

#### 3.2.8.1. The `Definition` tag

HED definitions are special HED tag groups that consist of a `Definition` tag and a tag group
defining the concept.

The `Definition` tag must be extended with a value representing the definition name and may
be additionally extended by a `#` placeholder.

Multiple definitions with the same definition name are not allowed.
This issue may not be detected until all available locations for definitions are scanned.
Thus, definitions are usually detected and removed during early stages of processing.

If the definition name includes the `#` placeholder extension, then the defining tags must
include exactly one tag that takes a value along with its `#` placeholder.
A value must be substituted for the `#` placeholder when final event annotation assembly
occurs. **Each distinct substituted value represents a distinct definition.**

A definition is incorporated into annotations using the tag `Def/xxx` where `xxx` is the definition's name.
Alternatively, the annotator may use an expanded form `(Def-expand/xxx, yyy)` where `xxx` is the
definition's name and `yyy` represents the definition's tags, not including the inner groups enclosing
parentheses.
The two usages are equivalent, and tools should be able to transform between the two representations.
Note, however, that transforming from the `Def` to the `Def-expand` form requires the definition,
while transforming from the `Def-expand` to `Def` form does not.

The `Definition` tag groups may appear anywhere that HED annotations can be used,
including in sidecars, in the HED column of tabular files, or in HED-specified columns of tag spreadsheets.

`Definition` tag groups are not part of any annotation and should be removed and processed
separately before other annotations are processed.

Each definition is independent and stands alone.
It can be validated independently of any other definitions or HED annotations.

The `Definition` tag corresponds to a schema node with the `topLevelTagGroup` attribute,
assuring that definitions cannot be nested.

See [**Definition syntax**](./05_Advanced_annotation.md#51-definition-syntax) and
[**Using definitions**](./05_Advanced_annotation.md#52-using-definitions) for more details
and examples.

#### 3.2.8.2. `Onset` and `Offset` tags

The `Onset` and `Offset` tags are used to represent the temporal extent
of events that have non-zero duration.
These tags correspond to schema nodes with the `topLevelTagGroup` attribute.
An `Onset` tag group and a `Offset` tag group associated with the same definition name
cannot appear in the assembled annotation for a single time-point.


In annotations, the `Onset` tag group includes the `Onset` tag, a `Def` or `Def-expand` group,
and optionally an additional tag group. No other items are allowed.

A tag group with an `Onset` represents the start of an event that extends over time.
Only one `Def` or `Def-expand` group may be included in the `Onset` group at the top level.
The name of the corresponding definition identifies the event that was initiated.

In annotations, the `Offset` tag group includes the `Offset` tag and a `Def` or `Def-expand` group.
No other items are allowed.
A tag group with an `Offset` represents the end of an event that was previously initiated by an `Onset` group.
The definition name associated with the top-level `Def` or `Def-expand` group identifies the
event that ended.

As a consequence of the `topLevelTagGroup` and format requirements,
`Onset` and `Offset` may not appear in the same tag group.
Further, a HED definition cannot include `Onset` or `Offset` tags.

In addition to the top-level `Def` or `Def-expand` group that identifies the event,
`Def` or `Def-expand` groups may appear in the optional tag group within an `Onset` group.
The definition names corresponding to these should not be used elsewhere to identify events.

See [**Onsets and Offsets**](./05_Advanced_annotation.md#531-onsets-and-offsets)
in Chapter 5 for examples of usage and additional details.

#### 3.2.8.3. The `Event-context` tag

The `Event-context` tag corresponds to a schema node with both the `topLevelTagGroup` and `unique` attributes.
This implies that there can be only one `Event-context` group in each assembled event-level string.
The `Event-context` group contains information about what other events are ongoing at the time point
associated with the event marker for which the annotation is included.

In general, the `Event-context` group is not included in annotations, but is generated by tools during
downstream event processing. 

### 3.2.9. Sidecars

A sidecar is a dictionary that can be used to associate tabular file columns
and their values with HED annotations. 


The rows of tabular event files represent time markers on the experimental timeline,
and the assembled events for the row represent the annotations of what happened at that time marker.
A sidecar containing annotations associated with the columns of such an event file
allows HED tools to assemble HED annotations for each row in a tabular file.

The rows of tabular files representing other types of information
can also be annotated in the same way.

HED sidecar validation assumes that the dictionary is saved in JSON format and complies with the
[**BIDS sidecar**](https://bids-specification.readthedocs.io/en/stable/appendices/hed.html) format.


#### 3.2.9.1. HED sidecar entries

In order to support HED, a sidecar must have `"HED"` as a key in one or more second-level dictionaries.
A BIDS sidecar is dictionary with many possible types of entries, three of which are relevant to HED.
These entries all have `"HED"` as a key in one or more second-level dictionaries.

````{Admonition} Three types of JSON sidecar entries of interest to HED tools 
- **Categorical entries**: are associated with a particular event file column and provide
individual annotations for each column value. 
The dictionary is not required to provide annotations for every possible
value in the column, although tools may choose to issue a warning if appropriate.
The dictionary may also include annotations for values that do not appear in the associated event file column.  
<p></p>

- **Value entries**: are associated with a particular event file column and provide
an annotation that applies to any entry in the column.
The HED annotation must contain a single `#` placeholder,
and each individual column value is substituted for the `#` in the annotation
when the annotation for the entire row is assembled.

<p></p>
 
- **Dummy entries**: are similar in format to categorical entries,
but are not associated with any event file columns.
Rather these annotations are mainly used to gather HED definitions.

````

While HED definitions are allowed anywhere,
the recommended style is to separate them into dummy categorical sidecar entries for readability.

The sidecar does not have to provide a HED-relevant entry for every event file column.
Columns with no corresponding sidecar entry are skipped during assembly of the HED annotation
for an event file row.

For compatibility with [**BIDS**](https://bids.neuroimaging.io/),
tabular file column entries containing `n/a` are ignored.
The sidecar is not permitted to provide an annotation for `n/a`.

The following example illustrates the three types of JSON sidecar entries that are relevant to HED.
Entries without a `"HED"` key in the second level entry dictionaries are ignored.

(example-sidecar-anchor)=
````{Admonition} Examples of the three types of sidecar annotation entries relevant to HED
:class: tip
```json
{
   "trial_type": {
      "LongName": "Event category",
      "Description": "Indicator of type of action that is expected",
      "HED": {
          "go": "Sensory-event, Visual-presentation, (Square, Blue)",
          "stop": "Sensory-event, Visual-presentation, (Square, Red)"
       }
   },
   "response_time": {
       "LongName": "Response time after stimulus",
       "Description": "Time from stimulus presentation until subject presses button",
       "HED": "(Delay/# ms, Agent-action, (Experiment-participant, (Press, Mouse-button)))"
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

In the example, the `trial_type` key references a **categorical** entry.
Categorical entries have keys corresponding to the event file column names.
The value of a categorical entry is a dictionary which has a `HED` key.
In the above example, the keys of this second dictionary are the values (`go` and `stop`) that
appear in the `trial_type` column of the event file.
The values are the HED annotations associated with those values.
Thus, the `"Sensory-event, Visual-presentation, (Square, Blue)"` is the HED annotation
associated with a `go` value in the `trial_type` column of the associated event file.

The `response_time` key references a **value annotation**.
Value entries have keys, one of which is `HED`.
Associated with the `HED` key is a HED annotation value.
There must be exactly one `#` placeholder in the annotation.
The actual value in the `response_time` column is substituted for the
`#` when the annotation is needed.

The `dummy_defs` is an example of a **dummy annotation**.
The value of this entry is a dictionary with a `HED` key
pointing to a dictionary.
A dummy annotation is similar in form to a **categorical annotation**,
but its keys do not correspond to any event file column names.
Rather it is used as a container to organize HED definitions.

In the example,
`Definition/Cue1` is a definition that does not use a placeholder (`#`) modifier in its name,
while `Definition/Image/#` is a definition whose name `Image` is modified by a placeholder value.
Notice that `Image` is both a definition name and an actual tag in the schema in this example.
This is permitted.

#### 3.2.9.2. Sidecar validation

As with other entities definitions should be removed from sidecars and validated separately,
although validation error messages for such definitions should be associated with
the locations of the definitions in the sidecars.

HED categorical sidecar entries contain HED strings and should be validated in the same way.

HED value sidecar entries must contain exactly one `#` placeholder in the HED string annotation associated 
with the entry. The `#` placeholder should correspond to a `#` in the HED schema,
indicating that the parent tag (also included in the annotation) expects a value. 

If the placeholder is followed by a unit designator, the validator checks that 
these units are consistent with the unit class of the
corresponding `#` in the schema.  The units are not mandatory.

### 3.2.10. Tabular files

A tabular file is a text file in which each line represents a row in a table.
The column entries in a given row are separated by tabs.
Further, the first line of the file must contain a tab-separated list of
column names, which should be unique.
This definition of tabular file conforms to that used by [**BIDS**](https://bids.neuroimaging.io/).

Generally each row in a tabular file represents an item and the columns values provide properties of that item.
The most common HED-annotated tabular file represents event markers in an experiment.
In this case each row in the file represents a time at which something happened.

Another common HED-annotated tabular file represents experiment participants.
In this case each row in the file represents a participant, and the columns provide
characteristics or other information about the participant identified in that row.

In any case, the general strategy for validation or other processing is:
1. Process the individual components of the HED annotation (tag and string level processing).
2. Assemble the component annotations for a row (event or row level processing).
3. Check consistency and relationships among the row annotations (file-level processing).

#### 3.2.10.1. Tabular annotations

HED annotations in tabular files can occur both in a `HED` column within the file and
in an associated JSON sidecar.

The HED strings that appear in a `HED` column must be valid HED strings.

Definitions applicable to a tabular file may appear anywhere in the `HED` column
or an associated sidecar, not necessarily before it is used in a particular entry.
Thus, validation and other processing must gather definitions from the `HED` column
and associated sidecars before any other processing can occur.

#### 3.2.10.2. Event-level processing

After individual HED tags and HED strings in the `HED` column and sidecars are validated or otherwise processed,
the HED strings associated with each row of the tabular file must be assembled to provide an overall
annotation for the row.
We refer to this as *event-level* or *row* processing.

````{Admonition} General procedure for event-level (row) processing. 

1. Start with an empty list.
2. For each categorical column, the column value for the row is looked up in the sidecar.
If an annotation for that column value is available it is concatenated to the list. 
3. For each value column, if a column an associated value entry in the sidecar,
the row value is substituted for `#` placeholder in the annotation and the result concatenated to the list.
4. If a `HED` column exists the annotation for that row, it is concatenated to the list.
5. Finally, all the entries of the list are joined using a comma (`,`) separator.

In all cases `n/a` row values are skipped.
````

For an example, see [**How HED works in BIDS**](https://www.hed-resources.org/en/latest/BidsAnnotationQuickstart.html#how-hed-works-in-bids) tutorial.

If the HED schema used for processing contains a schema node that has the `required` attribute, then
the assembled HED annotations for each row must include that tag.
Currently, HED schema versions >= 8.0.0 do not contain any nodes with the `required`
attribute, and this attribute may be deprecated in future versions of the schema.

If the HED schema used for processing contains a schema node that has the `unique` attribute,
then the assembled HED annotations for each row must contain no more than one occurrence of that tag.
Currently, only `Event-context` has the `unique` attribute for HED schema versions >= 8.0.0.

#### 3.2.10.3 File-level processing

HED versions >= 8.0.0 allow annotation of relationships among rows in a tabular file.
Hence, processing generally requires that annotations for all the rows be assembled
so that consistency can be checked.

To validate temporal scope, the validator must assure that each `Onset` and `Offset` tag 
is associated with an appropriately defined identifier corresponding to a definition name.
The validator must also check to make sure that `Onset` and `Offset` tags are
properly matched within the data recording.
In particular every `Offset` tag group must correspond to a preceding `Onset` tag group.
