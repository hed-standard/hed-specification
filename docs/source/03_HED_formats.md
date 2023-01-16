(3-hed-formats-anchor)=
# 3. HED formats

This chapter describes the requirements and formats that HED schema and HED annotations
must adhere to.

## 3.1 HED schema format

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

Additional details about HED schema format can be found in
[**Appendix A. Schema format details**](./Appendix_A.md)

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

### 3.1.2. Schema naming

The different parts of the HED schema have different rules 
for the characters and names that are allowed. UTF-8 characters are not supported.
Schema designers and users that extend HED schema must use node (tag term) names 
that conform to the rules for 
[**nameClass**](./Appendix_A.md#a-3-3-value-classes) as explained below.

````{admonition} Rules for naming nodes (tag terms) in HED schema. 
:class: tip
1. By convention, the first letter of a schema node (tag term) should be capitalized with the remainder lower case. 
2. Schema node names consisting of multiple words cannot contain blanks and should be hyphenated.
3. Schema descriptions should be concise sentences, possibly with clarifying examples.
4. Schema descriptions cannot contain square brackets, curly braces, quotes, or punctuation 
or other characters not specifically allowed by `textClass` with the addition of commas.
````



### 3.1.3 Schema layout overview

Schemas can be specified in either `.mediawiki` or `.xml` format.
[**Online schema validation and conversion tools**](https://hedtools.ucsd.edu/hed/schema)
provide an easy way for users to convert between formats.

HED schema developers usually use `.mediawiki` format for more convenient editing,
display, and reference on GitHub.
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
whereas most of the sections of the `.mediawiki` version, which is line-oriented,
are terminated when the next section begins (`#!`) or a top tag (`'''`) is encountered.

The actual HED tag specifications (referred to in the discussion as nodes or tag terms)
appear in the `schema` section,
while the remaining sections specify additional information and behavior.
These additional sections are required, but are allowed to be empty.

#### 3.1.3.1 The header

The schema header line contains specifies the version and the library name,
if the schema is a library schema rather than the standard schema.

Library names must contain only alphabetic characters and are usually short and descriptive.
A schema's library name or lack there of is used to locate the schema in the
HED schema repository located in GitHub in the
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) repository.

#### 3.1.3.2 Unit classes

The unit class definition section specifies the allowed 
unit classes and the corresponding allowed unit names.
Only the singular version of each unit name is explicitly specified,
but the corresponding plurals of the explicitly mentioned 
singular versions are also allowed (e.g., `feet` is allowed in addition to `foot`). 
HED uses a `pluralize` function available in both Python and Javascript to check validity.  


#### 3.1.3.3 Unit modifiers

The unit modifier definition section lists the SI unit multiples and submultiples 
that are allowed to be prepended to units that have the `SIUnit` schema attribute. 

#### 3.1.3.4 Value classes

The value class definition section specifies rules for the values that are substituted 
for placeholders (`#`). Examples are special characters that are allowed for numeric values 
or dates. Placeholders that have no `valueClass` attributes, are assumed to be of text class.

#### 3.1.3.5 Schema attributes

The schema attribute definition section lists the schema attributes that may be applied to
schema elements in other sections of the schema.
The specification of which type of elements an attribute may apply
to is specified by the property attributes of these schema attributes. 

#### 3.1.3.6 Schema properties

The schema properties definition section lists properties of the schema attributes, themselves.
These properties help tools validate certain requirements directly based
on the HED schema rather than on hard-coded implementation. 


### 3.1.4 Mediawiki schema format

[**Mediawiki**](https://www.mediawiki.org/wiki/Cheatsheet) is a markdown-like format that was
selected as the schema editing format because of its flexibility
and ability to represent nested or hierarchical relationships.

The format is line-oriented, so each schema entry should be on a single line.

The schema must follow the layout described in the previous section.
All sections are required, although they may be empty.

If an attribute or property is referenced in the schema,
it must be defined in the appropriate definition section of the schema,
or schema processing tools will generate an error.

The following example shows a simple HED schema in `.mediawiki` format.

````{admonition} **Example:** Example HED schema in .mediawiki format.

```tid
HED version="8.0.0" 

'''Prologue'''
This prologue introduces the schema.

!# start schema
'''Event''' <nowiki>[Something that happens at a given place and time.]</nowiki>
* Sensory-event <nowiki>[Something perceivable by an agent.]</nowiki>
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
* extensionAllowed <nowiki>{boolProperty}[A schema attribute indicating that users can add unlimited levels of child nodes under this tag. This tag is propagated to child nodes with the exception of the hashtag placeholders.]</nowiki>
* takesValue <nowiki>{boolProperty}[A schema attribute indicating the tag is a hashtag placeholder that is expected to be replaced with a user-defined value.] </nowiki> 
                        . . .
'''Properties''' <nowiki>[Properties of the schema attributes.]</nowiki>
* boolProperty <nowiki>[Indicates that the schema attribute represents something that is either true or false and does not have a value. Attributes without this value are assumed to have string values.]</nowiki>
                        . . .
'''Epilogue'''
An optional section that is the place for notes and is ignored in HED processing.

!# end hed
```

````

Top nodes in the schema are designated by three single quotes (`'''`).
The level of other nodes is reported by the number of asterisks (`*`) at the beginning of the line.
Each term is separated from its level-indicating asterisks by a single space.

In the above example, `Property` in the `schema` section is a top node because it appears
enclosed by three single quotes, while `Informational-property` is a first-level node
because its defining line begins with a single asterisk (`*`).

In the above example, the top-level `Property` term (node) has an `extensionAllowed` schema attribute.
This implies that the `schema attributes` section must include a definition of the
`extensionAllowed` attribute or the schema will not validate.

The `#` node, which is a child of `Label`,
is a third-level node that has the `takesValue` schema attribute,
The `#` is a placeholder, and an actual value must be substituted when an annotation is assembled.

The definition of the `takesValue` attribute has `boolProperty`,
so a definition of `boolProperty` must be included in the `Properties` section 
or the schema will not validate.

Everything after each HED node (tag term) must be enclosed by `<nowiki></nowiki>` markup elements.
The contents within these markup elements include a description and attributes.

Descriptions, which are enclosed in square brackets (`[ ]`)
indicate the meaning of the item they modify.
The descriptions are displayed to users by schema browsers and other tools,
so every effort should be made to make them informative and clear.

Attributes are enclosed with curly braces (`{ }`). These attributes provide
additional rules about how the item and modifying values should be used and handled by tools.
Allowed HED node attributes include unit class and value class values as well as
HED schema attributes that do not have the `unitClassProperty`, `unitModifierProperty`,
`unitProperty`, or `valueClassProperty`. 

HED schema attributes that have the `boolProperty` appear in the schema element they
are modifying just with their name.
The presence of such an attribute indicates that it is true or present.

HED schema attributes that do not have the `boolProperty` are specified in the form of a
`name=value` pair.
If multiple values of a particular attribute are applicable,
they should be specified as name-value pairs separated by commas within the square brackets.

The hashtag character (`#`) is a placeholder for a user-supplied value. Within the HED schema a
`#` node indicates that the user must supply a value consistent with the unit classes and value
classes of the `#` node if it has any during annotation.
Lines with hashtag (`#`) placeholders should have
everything after the asterisks enclosed by `<nowiki></nowiki>` markup elements.

Additional details and rules can be found in 
[**Appendix A. Mediawiki file format**](./Appendix_A.md#a-1-mediawiki-file-format)

### 3.1.5 XML schema format

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
    <unitClassDefinitions> ...</unitClassDefinitions>
    <unitModifierDefinitions>...</unitModifierDefinitions>
    <valueClassDefinitions>...</valueClassDefinitions>
    <schemaAttributeDefinitions>...</schemaAttributeDefinitions>
    <propertyDefinitions>...</propertyDefinitions>
    <epilogue>This epilogue is a place for notes and is ignored in HED processing.</epilogue>
</HED>
```
````

The `<node>` elements of the schema represent the HED tags,
with remaining schema elements specifying additional information and properties.

Each `<node>` element must have a `<name>` child element corresponding to the HED tag term 
that it specifies.

A `<node>` element may also have a `<description>` child element containing
the text that appears in square brackets (`[ ]`) in the `.mediawiki` version. 

The schema attributes (which appear as `name` values or `name-value` pairs enclosed in 
curly braces {} in the `.mediawiki` file) are translated into `<attribute>` child elements
of `<node>` in the `.xml`. 

Additional details and rules can be found in 
[**Appendix A. XML file format**](./Appendix_A.md#a-2-xml-file-format)

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
*Event*, *Agent*, *Action*, *Item*, *Property*, and *Relation*. 

The *Event* root tree terms indicate the general category of the event, such as whether it 
is a sensory event, an agent action, a data feature, or an event indicating experiment 
control or structure. The HED annotations describing each event may be assembled from a 
number of sources during processing. 

Many analysis tools use the *Event* tags as a primary means of 
segregating, epoching, and processing the data.
Ideally, tags from the *Event* subtree should appear at the top level of the
HED annotation describing an event to facilitate analysis.

The *Agent* root tree terms indicate types of agents (e.g., persons, animals, avatars)
that take an active role or produce a specified effect. An *Agent* tag should be 
grouped with property tags that provide information about the agent, such as 
whether the agent is an experiment participant.

The *Action* root tree terms describe actions performed by agents. Generally these are
grouped in a triple *(A, (Action, B))* which is interpreted as *A* does *Action* on *B*. 
If the action does not have a target, it should be annotated *(A, (Action))*, meaning
*A* does *Action*.

The *Item* root tree terms describe things with (actual or virtual) physical existence
such as objects, sounds, or language. 

Descriptive elements are organized in the *Property* rooted tree. These descriptive
elements should always be grouped with the elements they describe using parentheses. 

Binary relations are in the *Relation* rooted tree. Like items from the *Action*
sub-tree, these should be annotated using *(A, (Relation, B))*.


### 3.2.2 Tag syntax

A **HED tag** is a term in the HED vocabulary identified by a path consisting of the 
individual node names from some branch of the HED schema hierarchy separated by forward 
slashes (/). 

An important requirement of third generation HED is that the node names in 
the HED schema **must be unique**. 
As a consequence, the user can specify as much of the path to the root as desired. 

The full path version is referred to as **long form** and truncated versions as 
**short form**. HED tools are available to map between shortened tags and long form as needed. 
Any **intermediate form** of the tag path is also allowed as illustrated by this example:

The following illustrates some variations possible for HED tags with and without values.

````{Admonition} Different allowed forms of HED tags with and without values. 
| Short-form |  Intermediate form(s) | Long-form |
| -----------|  ------------------ |--------- |
| *Cough*  |  *Move/Breathe/Cough*<br/> *Breathe/Cough* | *Action/Move/Breathe/Cough* |
| *Weight/3 lbs* | *Data-property/Data-value/Physical-value/Weight/3 lbs*<br/> *Data-value/Physical-value/Weight/3 lbs*<br/> *Physical-value/Weight/3 lbs* | *Property/Data-property/Data-value/Physical-value/Weight/3 lbs* | 
````


### 3.2.3. Tags that take values

A HED tag that takes a value corresponds to a schema node whose unique child is a `#` leaf node.
These tags may appear with or without a value. 
If given with a value, the tag term is followed by a slash,
followed by a value and possibly a blank followed by units.

Neither a placeholder nor its direct parent tag  may not be extended in any other way.
Thus, tags that have placeholder children cannot be extended even
if they inherit an `extensionAllowed` attribute from an ancestor.
The parsers treat any child of these tags as a value substituted for the
placeholder rather than a tag.

**HED values** can be strings or numeric values followed by a unit specification. 
If a `unitClass` is specified as an attribute of the `#` node, then the units specified 
must be valid units for that `unitClass`. 
**HED parsers assume that units are separated from values by at least one blank.**

The characters that may be used in the value that replaces the `#` placeholder must be
in the union of the values allowed by the `valueClass` attributes of the`#` node.

Additional checks may be made on the substituted values depending on the *valueClass*

| valueClass  | Additional value checks |
| ----------- | ----------------------- |
| numericClass | Must be a valid floating point number. |
| dateTimeClass | must be a valid ISO8601 value. |

The values of HED tag placeholders cannot stand alone, but must include the parent when used in a HED string. 
For example, the *Label* node in the HED schema has the `#` child. Thus, the value *myLabel* meant to
substitute for the `#` child of the *Label* node must include *Label* when used in a HED tag
(e.g., *Label/myLabel* not *myLabel*).

The values substituted for `#` may themselves be schema node names provided they conform with any
value class requirements associated with that `#`.
Thus, *Label/Item* is a valid HED tag.
It is the *Label* tag with its value *Item* and is unrelated to the *Item* HED tag.
However, *Data-maximum/Item* is not valid because
the `#` child of *Data-maximum* has a *valueClass=numericClass* attribute
and the *Item* value is not numeric.

Certain unit classes allow other special characters in their value specification. 
These special characters are specified in the schema with the `allowedCharacter` attribute. 
An example of this is the colon in the `dateTimeClass` unit class.

#### 3.2.4. Tag extensions
A tag extension, in contrast to a value, is a tag that users add
after a leaf node as a more specific term for an item already in the schema.

For example, a user might want to use *Helicopter* instead of the more general term *Aircraft*.
Since *Aircraft* inherits the *extensionAllowed* attribute,
users may use extended tags such as *Aircraft/Helicopter* in their annotation.
The requirements such an extension are:

````{warning} **Requirements for tag extensions by users:**

1. The extension term must not already be a node in the schema.
2. The extension term must only have alphanumeric, hyphen, or underbar characters so that it
conforms to the rules for a *nameClass* value.
3. The parent of the tag extension must always be included with the extended tag in annotation.
4. The extension term must satisfy the "is-a" relationship with its parent node.

Notes: The is-a relationship is not checked by validators.
It is needed so that term search works correctly.

```` 

Users should not use tag extension unless necessary for their application,
as this breaks the commonality among annotations across datasets.
Please open an [**issue**](https://github.com/hed-standard/hed-examples/issues)
proposing that the new term be added to the schema in question,
if you think the term would be useful to other users.

### 3.2.5. Tag prefixes

Users may select tags from multiple schemas, but these must be specified in the
HED version specification.



### 3.2.6. HED strings and groups

A **HED string** is a comma-separated list of HED tags and/or HED tag groups.

A **HED tag group** is a comma-separated list of HED tags and/or tag groups enclosed in
parentheses. Tag groups may include other tag groups. 

Parentheses convey association, since HED strings are unordered lists. 

The terms in a HED string must be unique, thus, a HED string forms a set.

````{admonition} **Example:** Nested HED tag group indicated press.

**Short form:**  
> *((Human-agent, Experiment-participant), (Press, Mouse-button))*

**Long form:**
> *((Agent/<strong>Human-agent</strong>,*  
>    *Property/Agent-property/Agent-task-role/<strong>Experiment-participant</strong>),*  
> *(Action/Move/Move-body-part/Move-upper-extremity/<strong>Press</strong>,*  
> *Item/Object/Man-made-object/Device/IO-device/Input-device/Computer-mouse/<strong>Mouse-button</strong>))*  

````

Any ordering of HED tags at the same level within a HED string is equivalent.

The validation errors for HED tags and HED strings are summarized in
[Appendix B: HED errors](Appendix_B.md#b-hed-errors).


### 3.2.5 Parenthesized HED strings

Valid HED tags may have parentheses nested to arbitrary levels.
Parentheses are meaningful.

If *A* and *B* represent HED tags, the HED string *(A, B)* is not equivalent to
the HED string *A, B* and the distinction should be preserved if relevant.
*(A, B)* means that HED tag *A* and HED tag *B* are associated with each other,
whereas *A, B* means that *A* and *B* are each annotating some larger construct.

Specific rules of association will be encoded in a future version of the HED specification.
