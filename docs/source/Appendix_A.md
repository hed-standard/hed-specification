(appendix-a-schema-format-details-anchor)=
# A. Schema format details

This appendix augments the discussion of HED schema formats presented
in [**Chapter 3: HED formats**](./03_HED_formats.md) of the HED specification.
The appendix presents additional details on the rules with examples
for standard HED schema and HED library schema in `.mediawiki` and `.xml` formats.

## A.1. Auxiliary schema  sections

This section gives information about how the various auxiliary sections of the HED 
schema are used to specify the behavior of the schema elements.

### A.1.1. Unit classes and units

Unit classes allow annotators to express the units of values in a consistent way. 
The plurals of the various units are not explicitly listed, but are allowed as HED
tools uses standard pluralize functions to expand the list of allowed units.

Units corresponding to unit symbols (i.e., have a `unitSymbol` attribute)
represent abbreviated versions of units and cannot be pluralized. 

Elements with the `SIUnit` modifier may be prefixed with a multiple or a sub-multiple modifier.
If the SI unit does not also have the `unitSymbol` attribute, then multiples and sub-multiples
with the `SIUnitModifier` attribute are used for the expansion.

On the other hand, units with both `SIUnit` and `SIUnitModifier` attributes are expanded using
multiples and sub-multiples having the `SIUnitSymbolModifier` attribute.
  
Note that some units such as byte are designated as SI units, although they are not 
part of the SI standard.
However, they follow the same rules for unit modifiers as do SI units.


`````{list-table} Unit classes and units in HED 8.0.0 (* indicates unit symbol).
:widths: 20 10 40
:header-rows: 1

* - Unit class
  - Default units
  - Units
* - accelerationUnits
  - m-per-s^2 
  - m-per-s^2*
* - angleUnits
  - rad 
  - radian, rad*, degree
* - areaUnits
  - m^2 
  - metre^2, m^2*
* - currencyUnits
  - $ 
  - dollar, $, point
* - frequencyUnits
  - Hz 
  - hertz, Hz*
* - intensityUnits
  - dB 
  - dB, candela, cd*
* - jerkUnits
  - m-per-s^3 
  - m-per-s^3*  
* - memorySizeUnits
  - B 
  - byte, B 
* - physicalLength
  - m 
  - metre, m*, inch, foot, mile   
* - speedUnits
  - m-per-s 
  - m-per-s*, mph, kph     
* - timeUnits
  - s 
  - second, s*, day, minute, hour
* - volumeUnits
  - m^3 
  - metre^3, m^3*  
* - weightUnits
  - g 
  - gram, g*, pound, lb   
``````

### A.1.2. Unit modifiers

A unit modifier can be applied to SI base units to indicate a multiple or sub-multiple of the unit.
Unit symbols are modified by unit symbol modifiers, whereas
SI units that are not unit symbols are modified by unit modifiers.

`````{list-table} SI unit modifiers
:widths: 20 20 50
:header-rows: 1

* - Modifier
  - Symbol modifier
  - Description
* - deca
  - da
  - Multiple representing 10^1
* - hecto
  - h
  - Multiple representing 10^2
* - kilo
  - k
  - Multiple representing 10^3
* - mega
  - M
  - Multiple representing 10^6
* - giga
  - G
  - Multiple representing 10^9
* - tera
  - T
  - Multiple representing 10^12
* - peta
  - P
  - Multiple representing 10^15
* - exa
  - E	
  - Multiple representing 10^18
* - zetta
  - Z
  - Multiple representing 10^21
* - yotta
  - Y
  - Multiple representing 10^24
* - deci
  - d
  - Submultiple representing 10^−1
* - centi
  - c
  - Submultiple representing 10^−2
* - milli
  - m
  - Submultiple representing 10^−3
* - micro
  - u
  - Submultiple representing 10^−6
* - nano
  - n
  - Submultiple representing 10^−9
* - pico
  - p
  - Submultiple representing 10^−12
* - femto
  - f
  - Submultiple representing 10^−15
* - atto
  - a
  - Submultiple representing 10^−18
* - zepto
  - z
  - Submultiple representing 10^−21
* - yocto
  - y
  - Submultiple representing 10^−24
``````

### A.1.3. Value classes

HED has very strict rules about what characters are allowed in various elements of the HED
schema, HED tags, and the substitutions made for `#` placeholders.
These rules are encoded in the schema using value classes.
When a node name extension or placeholder substitution is given a particular value class,
that name or substituted value can only contain the characters allowed for by that value class.

```{Warning}
**Note**: However, that a placeholder `#` specification may include multiple value classes.

Tools check the value in question against the union of an element's `valueClass` allowed
characters and any additional characters allowed by a particular unit type.

```

The allowed characters for a value class are specified in the definition of each value class.
The HED validator and other HED tools may hardcode information about 
behavior of certain value classes (for example the `numericClass` value class). 

(value-class-character-table-anchor)=
`````{list-table} Allowed characters for value classes.
:widths: 20 50
:header-rows: 1

* - Value class
  - Allowed characters
* - dateTimeClass
  - `digits`  `T`  `:`  `-` 
* - nameClass
  - `alphanumeric`  `-`  `_`
* - numericClass
  - `digits`  `.`  `-`  `+`  `E`  `e` 
* - posixPath
  -  As yet unspecified
* - textClass
  - `alphanumeric`  `blank`  `+`  `-`  `:`  `;`  `.`  `/`  `(`  `)`  `?`  ` *`  `%`  ` $`  `@`  `^`  `_`
``````

````{admonition} Notes on rules for allowed characters in the HED schema. 
:class: tip

1. Commas or single quotes are not allowed in any values.
2. Date-times should conform to ISO8601 date-time format YYYY-MM-DDThh:mm:ss.
3. Any variation on the full form of ISO8601 date-time is allowed.
4. The `nameClass` is for schema nodes and labels.
5. Values of `numericClass` must equivalent to a valid floating point value.
6. Scientific notation is supported with the `numericClass`.
7. The text class is for descriptions, mainly for use with the *Description* tag or schema element descriptions.
8. The posix path class is yet unspecified and currently allows any characters except commas.

````


### A.1.4. Schema attributes

As mentioned in the previous section schema attributes can only apply to one
type of element in the schema as indicated by their property values. 
Tools hardcode processing based on the schema attribute name. Only the schema 
attributes listed in the following table can be handled by current HED tools.


`````{list-table} Schema attributes (* indicates attribute has a value).
:widths: 20 15 45
:header-rows: 1

* - Attribute
  - Target
  - Description
* - allowedCharacter*
  - valueClass
  - Specifies a character used in values of this class.
* - defaultUnits*
  - unitClass
  - Specifies units to use if placeholder value has no units.   
* - extensionAllowed
  - node
  - A tag can have unlimited levels of child nodes added.
* - recommended
  - node
  - Event-level HED strings should include this tag.
* - relatedTag*
  - node
  - A HED tag closely related to this HED tag.
* - requireChild
  - node    
  - A child of this node must be included in the HED tag.
* - required
  - node      
  - Event-level HED string must include this tag.
* - SIUnit
  - unit   
  - This unit represents an SI unit and can be modified.
* - SIUnitModifier
  - unitModifier   
  - Modifier applies to base units.
* - SIUnitSymbolModifier
  - unitModifier    
  - Modifier applies to unit symbols.
* - suggestedTag*
  - node   
  - Tag could be included with this HED tag.
* - tagGroup
  - node   
  - Tag can only appear inside a tag group.
* - takesValue
  - node #   
  - Placeholder (#)should be replaced by a value.
* - topLevelTagGroup
  - node        
  - Tag (or its descendants) can be in a top-level tag group.
* - unique
  - node        
  - Tag or its descendants can only occur once in <br/>
    an event-level HED string.
* - unitClass*
  - node #        
  - Unit class this replacement value belongs to.
* - unitPrefix
  - unit        
  - Unit is a prefix (e.g., $ in the currency units).
* - unitSymbol
  - unit        
  - Tag is an abbreviation representing a unit.
* - valueClass*
  - node #        
  - Type of value this is.        
``````

The `allowedCharacter` attribute should appear separately for each individual character to be allowed.
However, the following group designations are allowed as a value for this attribute:
- `letters` designates upper and lower case alphabetic characters.
- `blank` indicates a space is an allowed character.
- `digits` indicates the digits 0-9 may be used in the value.
- `alphanumeric` indicates `letter` and `digits`

If placeholder (`#`) has a `unitClass`, but the replacement value for the placeholder
does not have units, tools may assume the value of `defaultUnits` if the unit class has them.
For example, the `timeUnits` has the attribute `defaultUnits=s` in HED versions >=8.0.0.
Tools may assume that tag `Duration/3` is  equivalent to `Duration/3 s` because `Duration` has
`defaultUnits` of `s`.

The `extensionAllowed` tag indicates that descendents of this node may be extended by annotators.
However, any tag that has a placeholder (`#`) child cannot be extended,
regardless of `extensionAllowed` since its single child is always interpreted as a user-supplied value. 

Tags with the `required` or `unique` attributes cannot appear in definitions.

In addition to the attributes listed above, some schema attributes have been deprecated
and are no longer supported in HED, although they are still present in earlier versions of 
the schema. The following table lists these.

`````{list-table} Schema attributes deprecated for versions >=8.0.0 (* indicates attribute has a value).
:widths: 20 15 45
:header-rows: 1

* - Schema attribute
  - Target
  - Description
* - default
  - node #
  - Indicates a default value used if no value is provided.
* - position*
  - node    
  - Indicates where this tag should appear during display.
* - predicateType
  - node   
  - Indicates the relationship of the node to its parent. 
``````

The `default` attribute was not implemented in existing tools. 
The attribute is not used in HED-3G. Only the `defaultUnits` for the unit class 
will be implemented going forward. 

The `position` attribute was used to assist annotation tools, which sought to 
display required and recommend tags before others. The position attribute value
is an integer and the order can start at 0 or 1. Required or recommended 
tags without this attribute or with negative position were to be shown after the 
others in canonical ordering. 
The tagging strategy of HED versions >= 8.0.0 using decomposition
and definitions does not permit this type of ordering.
The `position` attribute is not used for HED versions >= 8.0.0.

The `predicateType` attribute was introduced in HED-2G to facilitate mapping to OWL or RDF. 
It was needed because the HED-2G schema had a mixture of children
that were properties and subclasses.
The possible values of `predicateType` were `propertyOf`, `subclassOf`, or `passThrough` 
to indicate which role each child node had with respect to its parent.
In HED versions >= 8.0.0, the parent-child relationship MUST be `subclassOf` to allow search generality.
The attribute is ignored by tools.


### A.1.5. Schema properties

The `property` elements apply to schema attribute elements to indicate how and where these attributes
apply to other elements in the schema. 
Their meanings are hard-coded into the schema processors.
The following is a list of schema attribute properties. 

`````{list-table} Summary of schema attribute properties for HED Version >= 8.0.0.
:widths: 20 50
:header-rows: 1

* - Property
  - Description
* - boolProperty
  - A schema attribute's value is either true or false.<br/>Presence indicates true, absence false. 
* - unitClassProperty
  - A schema attribute only applies to unit classes.
* - unitModifierProperty
  - A schema attribute only applies to unit modifiers.
* - unitProperty
  - A schema attribute only applies to units.
* - valueClassProperty
  - A schema attribute only applies to value classes.
``````

A given schema attribute can only apply to one type of schema element as
controlled by  `unitClassProperty`, `unitModifierProperty`, `unitModifierProperty`, `unitProperty`, and `valueClassProperty`.
A schema attribute that doesn't have one of these properties only applies to node elements in the schema section.

The `boolProperty` controls how a given schema attribute is applied to other
schema elements as described here:

````{admonition} Format for schema properties in the schema. 
:class: tip

- **Schema attributes with the `boolProperty`:**
  - In `.xml`, appear as a `<name>` element with the property, but no 
`<value>` in an `<attribute>` section of the schema element.
  - In `.mediawiki`, the attribute has the {`name`} in the element's specification line.
  - In either case, presence of the property indicates true and absence indicates false.
<p></p>  

- **Schema attributes without the `boolProperty`:**
  - In `.xml`, appear with both `<name>` and `<value>` in the `<attribute> section of a schema element.
  - In `.mediawiki`, the schema element has the {`name`=`value`} in the element's specification line.
  - These schema attributes may appear multiple times in an element with different values if appropriate.

````



## A.2. Mediawiki file format

The rules for creating a valid `.mediawiki` specification of a HED schema are given below. 
The format is line-oriented, meaning that all information about an individual entity should be on a 
single line. Empty lines and lines containing only blanks are ignored.

### A.2.1. Overall file layout

````{admonition} Overall layout of a HED MEDIAWIKI schema file.

```moin
header-line
prologue
             . . .
!# start schema
schema-specification
!# end schema
unit-class-specification
unit-modifier-specification
value-class-specification
schema-attribute-specification
property-specification
!# end hed
epilogue
```
````

### A.2.2. The *header-line*

The first line of the `.mediawiki` file should be a _header-line_ that starts with the 
keyword `HED` followed by a blank-separated list of name-value pairs.

````{eval-rst}
.. list-table:: Allowed HED schema header parameters
   :header-rows: 1
   :widths: 15 15 50

   * - Name
     - Level
     - Description
   * - library
     - optional
     - Name of library used in XML file names.  
     
       The value should only have alphabetic characters.
   * - version
     - required
     - A valid semantic version number of the schema.  
   * - xmlns
     - optional
     - xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance".
   * - xsi
     - optional
     - xsi:noNamespaceSchemaLocation points to an XSD file.

````

The following example gives a sample *header-line* for standard schema version 8.0.0 in `.mediawiki` format.

````{admonition} **Example:** Sample *header-line* for version 8.0.0 in .mediawiki format.

```moin
HED version="8.0.0"
```
````

The schema `.mediawiki` file specified in this example is named `HED8.0.0.mediawiki` and can be found in the 
[**standard_schema/hedwiki**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedwiki)
directory of the [**hed-schemas**](https://github.com/hed-standard/hedschemas) GitHub repository.

The versions of the schema that use XSD validation to verify the format (versions 8.0.0 and above) have `xmlns:xsi` and `xsi:noNamespaceSchemaLocation` attributes.
The `xsi` attribute is required if `xmlns:xsi` is given.
The [**XSD file**](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/hedxml/HED8.0.0.xsd)
allows validators to check the format of the `.xml` using standard XML validators.

The following example shows a sample *header-line* for `testlib` library schema version 1.0.2 in `.mediawiki` format.

````{admonition} **Example:** Sample *header-line* for testlib library version 1.0.2 in .mediawiki format.

```moin
HED library="testlib" version="1.0.2"
```
````

The `library` and `version` values are used to form the official file name `HED_testlib_1.0.2.mediawiki`.
The file is found in [**library_schemas/testlib/hedwiki**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/testlib/hedwiki)
directory of the [**hed-schemas**](https://github.com/hed-standard/hedschemas) GitHub repository.

A warning is generated when unknown header-line attributes are translated as attributes of the `HED` line
when the `.mediawiki` file is validated.

### A.2.3. The prologue and epilogue

The prologue is an optional paragraph of text appearing after the *header-line*.
The prologue is used by tools for help and display purposes.
The prologue can only contain characters allowed by the 
[`textClass`](./Appendix_A.md#a13-value-classes).

Early versions of HED use the prologue section to record a CHANGE_LOG as well as information about 
the syntax and rules. HED versions >= 8.0.0 include a separate change log file for released 
versions.

Similar to the prologue section, the epilogue is an optional paragraph of text
conforming to the rules of [`textClass`](./Appendix_A.md#a13-value-classes).
However, the epilogue appears directly before the ending line of the schema.

### A.2.4. Schema sections

The beginning of the actual specification of the HED vocabulary is marked by the *start-line*:

```moin
!# start schema
```


The end of the main HED-specification is marked by the *end-line*:

```moin
!# end schema
```

A section separator is a line starting with `!#`. 
The section separator lines (`!# start schema`, `!# end schema`, `!# end hed`) must only 
appear once in the file and must appear in that order within the file. 

The body of the HED specification is located between the `!# start schema` and `!# end schema`
section separators.
Each specification is a single line in the `.mediawiki` file.

The three types of lines in the main specification section
are **top-nodes**, **normal-nodes**, and **placeholders**, respectively.

Empty lines or lines containing only blanks are ignored.

The basic format for a node-specification is:

```moin
node-name  <nowiki>{attributes}[description]</nowiki>
```

Top node names are enclosed in triple single quotes (e.g., `'''Event'''`), while other types of 
node have at least one preceding asterisk (*) followed by a blank and then the name.

The number of asterisks indicates the level of the node in the subtree.
The attributes are in curly braces ('{ }') and the description is in square brackets (`[ ]`).

HED versions >= 8.0.0 node names can only contain alphanumeric characters, hyphens, and under-bars
(i.e., they must be of type [`nameClass`](./Appendix_A.md#a13-value-classes).
They cannot contain blanks and must be unique.

HED versions < 8.0.0 allow blanks.

For top nodes and normal nodes, everything after the node name must be contained within `<nowiki></nowiki>` tags.
The `#` is included within the `<nowiki></nowiki>` tags in placeholder nodes (`#`).

````{admonition} **Example:** Different types of HED node specifications in .mediawiki format.

**Top node:**

```moin
'''Property''' <nowiki>{extensionAllowed} [Subtree of properties.]</nowiki>
```

**Normal node:**

```moin
***** Duration <nowiki>{requireChild} [Time extent of something.]</nowiki>
```

**Placeholder node:**

```moin
****** <nowiki># {takesValue, unitClass=time,valueClass=numericClass}</nowiki>
```
````

The *Duration* tag of this example is at the fifth level below the root (top node) of its subtree. 
The tag: *Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/Duration* 
is the long form. The placeholder in the example is the node directly below *Duration* 
in the hierarchy.

### A.2.5. Auxiliary sections

After the line marking the end of the schema (`!# end schema`), the `.mediawiki` file contains 
the unit class definitions, unit modifier definitions, value class definitions, 
the schema attribute definitions, and property definitions. All of these sections are
required starting with HED version 8.0.0 and must be given in this order.

#### A.2.5.1. Unit classes and units

Unit classes specify the types of units allowed to be used with a value that substituted for
a `#` placeholder.

The unit class specification section starts with `'''Unit classes'''` and 
lists the type of unit (unit class) at the first level and the specific units at the second level.

````{admonition} **Example:** Part of the HED unit class for time in .mediawiki format.

```moin
'''Unit classes''' 
* time <nowiki>{defaultUnits=s}</nowiki> 
** second <nowiki>{SIUnit}</nowiki> 
** s <nowiki>{SIUnit, unitSymbol}</nowiki> 
```
````

#### A.2.5.2. Unit modifiers

The SI units can be modified by SI (International System Units) sub-multiples 
and multiples. All unit modifiers are at level 1 of the `.mediawiki` file.


````{admonition} **Example:** Part of the HED unit modifier in .mediawiki format.

```moin
'''Unit modifiers''' 
* deca <nowiki>{SIUnitModifier} [SI unit multiple for 10^1]</nowiki> 
* da <nowiki>{SIUnitSymbolModifier} [SI unit multiple for 10^1]</nowiki>
```
````

A unit must have the `SIUnit` attribute in order to be used with modifiers.
If the unit has both the `SIUnit` and `unitSymbol` attributes,
then it can be used with `SIUnitSymbolModifier` modifiers.
If the unit has only the `SIUnit` attribute,
then it can be used with the `SIUnitModifer`.

For example the unit `second` is an `SIUnit` but not a symbol,
so `second`, `seconds`, `decasecond` and `decaseconds` are all valid units.

The unit `s` is both a `SIUnit` and a `unitSymbol`, so `s` and `das` are valid units.
Note that pluralization does not apply to unit symbols.


#### A.2.5.3. Value classes

Value classes give rules about what kind of value is allowed to be substituted
for `#` placeholder tags.

````{admonition} **Example:** Part of the HED value class for posix paths in .mediawiki format.

```moin
'''Value classes'''
* posixPath <nowiki>{allowedCharacter=/,allowedCharacter=:}[Posix path specification.]</nowiki> 
```
````

The `posixPath` is completely specified.

#### A.2.5.4. Schema attributes

The schema attributes specify other characteristics about how particular tags may be used in 
annotation. These attributes allow validators and other tools to process tag strings based
on the HED schema specification, thus avoiding hard-coding particular behavior.

````{admonition} **Example:** HED schema attributes allowedChaaracter and defaultUnits in .mediawiki format.

```moin
'''Schema attributes'''
* allowedCharacter <nowiki>{valueClassProperty}[Attribute of value classes specifying a special character that is allowed in expressing the value of a placeholder.]</nowiki>
* defaultUnits <nowiki>{unitClassProperty}[Attribute of unit classes specifying the default units for a tag.]</nowiki> 
```
````
In the above example, the schema attributes, themselves have attributes referred to as
*schema properties*. These schema properties are listed in the `Properties` section of the schema.
The example indicates that `allowedCharacter` is associated with value classes,
while `defaultUnits` is associated with unit classes.

#### A.2.5.5. Schema properties

Properties apply only to schema attributes.
The following example defines the `valueClassProperty` in `.mediawiki` format.

````{admonition} **Example:** HED schema property valueClassProperty in .mediawiki format.

```moin
'''Properties''' 
* valueClassProperty <nowiki>[Attribute is meant to be applied to value classes.]</nowiki> 
```
````

## A.3. XML file format

This section describes details of the XML schema format.

### A.3.1. Overall file layout

The XML schema file format has a header, prologue, main schema, definitions, and epilogue
sections. The general layout is as follows:

````{admonition} XML layout of the HED schema.
```xml
<?xml version="1.0" ?>
<HED library="test" version="0.0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://github.com/hed-standard/hed-specification/raw/master/hedxml/HED8.0.0-beta.3.xsd">
<prologue>unique optional text blob</prologue>
<schema>
         ...  schema specification  ... 
</schema>
<unitClassDefinitions>
   <unitClassDefinition> ... </unitClassDefinition>
                         ...
   <unitClassDefinition> ... </unitClassDefinition>
</unitClassDefinitions>
<unitModifierDefinitions>
   <unitModifierDefinition> ... </unitModifierDefinition>
                                ...
   <unitModifierDefinition> ... </unitModifierDefinition>
</unitModifierDefinitions>
    
<valueClassDefinitions>
    <valueClassDefinition> ... </valueClassDefinition>
                           ... 
    <valueClassDefinition> ... </valueClassDefinition>
</valueClassDefinitions>

<schemaAttributeDefinitions> 
   <schemaAttributeDefinition> ... </schemaAttributeDefinition>
                               ... 
   <schemaAttributeDefinition> ... </schemaAttributeDefinition>
</schemaAttributeDefinitions>

<propertyDefinitions>
    <propertyDefinition> ... </propertyDefinition>
                             ... 
    <propertyDefinition> ... </propertyDefinition>
</propertyDefinitions>

<epilogue>unique optional text blob</epilogue>
</HED>
```
````

### A.3.2. The header

The `HED` node is the root node of the XML schema.

````{admonition} **Example:** Header for Version 8.0.0 of the standard HED XML schema.

```xml
<HED version="8.0.0">
```
````

The file name corresponding to this example is `HED8.0.0.xml`.
The file is found in [**standard_schema/hedxml**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml)
directory of the [**hed-schemas**](https://github.com/hed-standard/hedschemas) GitHub repository.

The resulting XML header is:

````{admonition} **Example:** Version 1.0.2 of HED testlib library schema in .xml format.
```xml
<HED library="testlib" version="1.0.2">
```
````


The `library` and `version` values are used to form the official xml `HED_test_1.0.2.xml`.
The file is found in [**library_schemas/testlib/hedxml**](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/testlib/hedxml)
directory of the [**hed-schemas**](https://github.com/hed-standard/hedschemas) GitHub repository.

Unknown header-line attributes are translated as attributes of the `HED` root node of the 
`.xml` version, but a warning is used when the `.mediawiki` file is validated.

### A.3.3. The prologue and epilogue

The `<prologue>xxx</prologue>` and `<epilogue>xxx</epilogue>` elements are meant to be treated
as opaque as far as schema processing goes.

HED versions < 8.0.0 contained a Change Log for the HED schema in the prologue section
as well as some basic documentation of syntax. 
The epilogue section contained additional metadata to be ignored during processing. 


### A.3.4. The schema section

The schema section of the HED XML document consists of an arbitrary number of `<node></node>` 
elements enclosed in a single `<schema></schema>` element.

````{admonition} Top-level XML layout of the HED schema.
```xml
<schema>
    <node> ... </node>
           ...
    <node> ... </node>
</schema>
```
````

A `<node>` element contains a required `<name>` child element, an optional `<description>` 
child element, and an optional number of additional `<attribute>` child elements:

````{admonition} XML layout HED node element.
```xml
<node>
    <name>xxx</name>
    <description>yyy</description>
    <attribute> ... </attribute>
    <attribute> ... </attribute>
    <attribute> ... </attribute>   
    <node> ... <node>
</node>
```
````

The `<name>` element text must conform to the rules for naming HED schema nodes. 
It corresponds to the _node-name_ in the `mediawiki` specification and must not be empty. 
A `#` value is used to represent value place-holder elements.

The `<description>` element has the text contained in the square brackets `[]` in the 
`.mediawiki` node specification. If the `.mediawiki` specification is missing or has an 
empty `[]`, the `<description>` element is omitted.

The optional `<attribute>` elements are derived from the attribute list contained in curly 
braces `{}` of the `.mediawiki` specification. An `<attribute>` element has a single non-empty
`<name></name>` child element whose text value corresponds to the node-name of attribute in the
corresponding `.mediawiki` file. If the attribute does not have the `boolProperty`, 
then the `<attribute>` element should also have one or more child `<value></value>` elements
giving the value(s) of the attribute. **Example:** The `requireChild` attribute represents a boolean value. In the `.mediawiki` representation this attribute appears as `{requireChild}` if present and is omitted if absent.

````{admonition} The requireChild attribute represents a boolean value.

**Old xml if true:**     

```xml
<node requireChild="true"><name>xxx</name></node>
```

**New xml if true:**

```xml
<node>
    <name>xxx</name>
    <attribute>
       <name>requireChild</name>
    </attribute>
</node>
```
````

The `suggestedTag` attribute has a valid HED tag value. In the mediawiki representation 
this attribute is omitted if absent and appears when present as shown in this example.

````{admonition} The suggestedTag attribute has a valid HED tag value.

```moin
{suggestedTag=Sweet,suggestedTag=Gustatory-attribute/Salty}
```
````

The `suggestedTag` attribute is meant to be used by tagging tools to suggest additional tags
that a user might want to include. Notice that the `suggestedTag` values are  valid HED tags
in any form (short, long, or intermediate).

````{admonition} The suggestedTag old format.

**Old xml if present:**

```xml
<node suggestedTag="Sweet,Gustatory-attribute/Salty">
    <name>xxx</name>
</node>
```

**New xml if present:**

```xml
<node>
   <name>xxx</name>
   <attribute>
      <name>suggestedTag</name>
    	 <value>Sweet</value>
    	 <value>Gustatory-attribute/Salty</value>
   </attribute>
</node>
```
````

### A.3.5. Auxiliary sections

The auxiliary sections define various aspects of behavior of various types of elements in the schema.

#### A.3.5.1. Unit classes

The valid HED-3G unit classes are defined in the `<unitClassDefinitions>` section of the XML
schema file, and valid HED-3G unit modifiers are defined in the `<unitModifierDefinitions>` 
section. These sections follow a format similar to the `<node>` element in the `<schema>` 
section:

````{admonition} XML layout of the unit class definitions.
```xml
<unitClassDefinitions>
    <unitClassDefinition> ... </unitClassDefinition>
                          ... 
    <unitClassDefinition> ... </unitClassDefinition>
</unitClassDefinitions>
```
````

The `<unitClassDefinition>` elements have a required `<name>`, an optional `<description>` 
and an arbitrary number of additional `<attribute>` child elements. These `<attribute>` elements 
describe properties of the unit class rather than of individual unit types. In addition,
`<unitClassDefinition>` elements may have an arbitrary number of `<unit>` child elements.

````{admonition} XML layout of the unit class definitions.
```xml
<unitClassDefinition>
    <name>time</name>
    <description>Temporal values except date and time of day.</description>
    <attribute>
       <name>defaultUnits</name>
       <value>s</value>
    </attribute>
    <unit>
       <name>second</name>
       <description>SI unit second.</description>
       <attribute>
          <name>SIUnit</name>
       </attribute>
    </unit>
    <unit>
       <name>s</name>
       <description>SI unit second in abbreviated form.</description>
       <attribute>
          <name>SIUnit</name>
       </attribute>
       <attribute>
          <name>unitSymbol</name>
       </attribute>
    </unit>  
</unitClassDefinition>
```
````

#### A.3.5.2. Unit modifiers

The following shows the layout of an example unit modifier

````{admonition} XML layout of the unit modifier definition
```xml

<unitModifierDefinitions>
    <unitModifierDefinition>
        <name>deca</name>
        <description>SI unit multiple representing 10^1.</description>
        <attribute>
           <name>SIUnitModifier</name>
        </attribute>
        <attribute>
           <name>conversionFactor</name>
           <value>10.0</value>
        </attribute>
    </unitModifierDefinition>
                . . .
</unitModifierDefinitions>  
```
````


#### A.3.5.3 Value classes

Value classes are defined in the `<valueClassDefinitions>` section of the XML schema file. 
These sections follow a format similar to the `<node>` element in the `<schema>`:

````{admonition} XML layout of the unit class definitions.
```xml
<valueClassDefinitions>
    <valueClassDefinition> ... </valueClassDefinition>
                             ... 
    <valueClassDefinition> ... </valueClassDefinition>
</valueClassDefinitions>
```
````

#### A.3.5.4. Schema attributes

The `<schemaAttributeDefinitions>` section specifies the allowed attributes of the other elements
including the `<node>`, `<unitClassDefinition>`, `<unitModifierDefinition>`, and
`<valueClassDefinition>` elements. The specifications of individual attributes are given in
`<schemaAttributeDefinition>` elements.

````{admonition} XML layout of the schema attribute definitions.
```xml
<schemaAttributeDefinitions>
    <schemaAttributeDefinition> ...</schemaAttributeDefinition>
                                   ... 
    <schemaAttributeDefinition> ... </schemaAttributeDefinition>
</schemaAttributeDefinitions>
```
````

The individual `<schemaAttributeDefinition>` elements have the following format:

````{admonition} XML layout of the schema attribute definitions.
```xml
<schemaAttributeDefinition>
    <name>allowedCharacter</name>
    <description>An attribute of value classes indicating a special character that is allowed in expressing the value of that placeholder.</description>
    <property>
        <name>valueClassProperty</name>
    </property>
    . . .
</schemaAttributeDefinition>
```
````

#### A.3.5.5. Schema properties

The following is an example of the layout of the `valueClassProperty` in `.xml` format.

````{admonition} XML layout of the schema property definitions.
```xml

  <propertyDefinitions>
                  . . .
      <propertyDefinition>
         <name>valueClassProperty</name>
         <description>Indicates that the schema attribute is meant to be applied to value classes.</description>
      </propertyDefinition>
   </propertyDefinitions>