# A.Schema format

HED schema developers generally do initial development of the schema using `.mediawiki` format. The tools to convert schema between `.mediawiki` and `.xml` format are located in the `hed.schema` module of the [hedtools](https://github.com/hed-standard/hed-python/tree/master/hedtools) project of the hed-python repository located at  [https://github.com/hed-standard/hed-python](https://github.com/hed-standard/hed-python). All conversions are performed by converting the schema to a HedSchema object and then The modules `wiki2xml.py` and `xml2wiki.py` provide top-level functions to perform these conversions. This appendix presents the rules for HED base and library schema in `.mediawiki` and `.xml` formats.

## A.1. Mediawiki file format

The rules for creating a valid `.mediawiki` specification of a HED schema are given below. 

### A.1.1. Overall file layout

The overall layout of is `.mediawiki` schema file is:

```mediawiki
header-line: HED . . .
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

Empty lines and lines containing only blanks are ignored.

### A.1.2. The *header-line*

The first line of the `.mediawiki` file should be a _header-line_ that starts with the keyword `HED` followed by a blank-separated list of name-value pairs (Table A.1). 

#### **Table A.1.** Allowed parameters in the HED schema `.mediawiki` header.

<table>
  <tr>
     <td><strong>Name</strong></td>
     <td><strong>Level</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>library</code></td>
     <td>Optional</td>
     <td>Name of library to be used in <em>.xml</em> file names. The value should consist of alphabetic characters only.</td>
  </tr>
  <tr>
     <td><code>version</code></td>
     <td>Required</td>
     <td>A valid semantic version number of the schema</td>
  </tr>
  <tr>
     <td><code>xmlns:xsi</code></td>
     <td>Optional</td>
     <td><code>xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"</code></td>
  </tr>
  <tr>
      <td><code>xsi:noNamespaceSchemaLocation</code></td>
      <td>Required/Optional</td>
      <td><p>Location of the XSD in effect, for example: <code>"https://github.com/hed-standard/hed-specification/raw/master/hedxml/HED8.0.0-beta.3.xsd"</code></p>
<p>The <code>xsi</code> attribute is required if <code>xmlns:xsi</code> is given.</p></td>
  </tr>
</table>

The `library` and `version` values are used to form the official xml file name and appear as attributes in the `<HED>` root of the `.xml` file`.` The versions of the schema that use XSD validation to verify the format (versions 8.0.0 and above) have `xmlns:xsi` and `xsi:noNamespaceSchemaLocation` attributes.

**Example:** Specify version 8.0.0 of the HED base schema.

The `.mediawiki` file has a header line:

```mediawiki
HED version="8.0.0"
```

The resulting XML root is:

```xml
<HED version="8.0.0">
```

The file name in `hedxml` in `hed-specification` is `HED8.0.0.xml`.

**Example:** Specify version 1.0.2 of the HED library schema `test`.

The `.mediawiki`  has a header line:

```mediawiki
HED library="test" version="1.0.2"
```

The resulting XML root is:

```xml
<HED library="test" version="1.0.2">
```

The file name in `hedxml` in the hed schema library `test` is `HED_test_1.0.2.xml`.

Unknown _header-line_ attributes are translated as attributes of the `HED` root node of the `.xml` version, but a warning is used when the `.mediawiki` file is validated.

### A.1.3. Schema section

The beginning of the HED specification is marked by the *start-line*:

```mediawiki
!# start schema
```

An arbitrary number of lines of informational text can be placed between the *header-line* and the *start-line*. Older versions of HED have a CHANGE_LOG as well as information about the syntax and rules. New versions of HED generate a separate change log file for released versions. 

The end of the main HED-specification is marked by the end-line:

```mediawiki
!# end schema
```

The section separator lines (`!# start schema`, `!# end schema`, `!# end hed`) must only appear once in the file and must appear in that order within the file. A section separator is a line starting with !#.

The body of the HED specification consists of two types of lines: top-level node-specification specifications and other node specifications. Each specification is a single line in the `.mediawiki` file. Empty lines or lines containing only blanks are ignored. The basic format for a node-specification is:

```mediawiki
node-name  <nowiki>{attributes}[description]</nowiki>
```

Top-level node names are enclosed in triple single quotes (e.g., `'''Event'''`), while other node names have at least one preceding asterisk (*) followed by a blank and then the name. The number of asterisks indicates the level of the node in the subtree. HED-3G node names can only contain alphanumeric characters, hyphens, and underbars. They cannot contain blanks and must be unique. HED (2G) and earlier versions allow blanks.   Everything after the node name must be contained within `<nowiki></nowiki>` tags. Placeholder nodes have an empty node name, but are followed by a # enclosed in  `<nowiki></nowiki>` tags.

**Example:** Different types of HED node specifications.

**Top-level:**

```mediawiki
'''Property''' <nowiki>{extensionAllowed} [Subtree of properties.]</nowiki>
```

**Normal-level:**

```mediawiki
***** Duration <nowiki>{requireChild} [Time extent of something.]</nowiki>
```

**Placeholder-level:**

```mediawiki
****** <nowiki># {takesValue, unitClass=time,valueClass=numericClass}</nowiki>
```

The *Duration* tag of this example is at the fifth level below the root of its subtree. The tag: *Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/Duration* is the long form. The placeholder in the example is the node directly below *Duration* in the hierarchy.

### A.1.4. Other sections

After the line marking the end of the schema (`!# end schema`), the `.mediawiki` file contains the unit class specifications, unit modifier specifications, value class specification, the schema attribute specifications, and property specifications. All of these sections are required starting with HED version 8.0.0-beta.3 and must be given in this order.

The unit class specification section starts with `'''Unit classes'''`

**Example:**  Part of the HED unit class specification for time.

```mediawiki
'''Unit classes''' 
* time <nowiki>{defaultUnits=s}</nowiki> 
** second <nowiki>{SIUnit}</nowiki> 
** s <nowiki>{SIUnit, unitSymbol}</nowiki> 
```

**Example:**  Part of the HED unit modifier specification.

```mediawiki
'''Unit modifiers''' 
* deca <nowiki>{SIUnitModifier} [SI unit multiple for 10^1]</nowiki> 
* da <nowiki>{SIUnitSymbolModifier} [SI unit multiple for 10^1]</nowiki>
```

**Example:**  Part of the HED value class specification.

```mediawiki
'''Value classes'''
* posixPath <nowiki>{allowedCharacter=/,allowedCharacter=:}[Posix path specification.]</nowiki> 
```

**Example:**  Part of the HED schema attribute specification.

```mediawiki
'''Schema attributes'''
* allowedCharacter <nowiki>{valueClassProperty}[A schema attribute of value classes specifying a special character that is allowed in expressing the value of a placeholder.]</nowiki>
* defaultUnits <nowiki>{unitClassProperty}[A schema attribute of unit classes specifying the default units for a tag.]</nowiki> 
```

**Example:**  Part of the property specification.

```mediawiki
'''Properties''' 
* valueClassProperty <nowiki>[Indicates that the schema attribute is meant to be applied to value classes.]</nowiki> 
```

## A.2. XML file format

The XML schema file format has a header, prologue, main schema, definitions, and epilogue sections. The general layout is as follows:

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

The `<prologue>xxx</prologue>` and `<epilogue>xxx</epilogue>` elements are meant to be treated as opaque as far as schema processing goes. In earlier versions of HED the prologue section contained a Change Log for the schema as well as some basic documentation of syntax. The epilogue section contained additional metadata to be ignored during processing. The following subsections give a more detailed description of the format of these sections.

### A.2.1. The schema section

The schema section of the HED XML document consists of an arbitrary number of `<node></node>` elements enclosed in a single `<schema></schema>` element.

```xml
<schema>
    <node> ... </node>
           ...
    <node> ... </node>
</schema>
```

A `<node>` element contains a required `<name>` child element, an optional `<description>` child element, and an optional number of additional `<attribute>` child elements:

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

The `<name>` element text must conform to the rules for naming HED schema nodes. It corresponds to the _node-name_ in the `mediawiki` specification and must not be empty. A `#` value is used to represent value place-holder elements.

The `<description>` element has the text contained in the square brackets `[]` in the `.mediawiki` node specification. If the `.mediawiki` specification is missing or has an empty `[]`, the `<description>` element is omitted.

The optional `<attribute>` elements are derived from the attribute list contained in curly braces `{}` of the `.mediawiki` specification. An `<attribute>` element has a single non-empty `<name></name>` child element whose text value corresponds to the node-name of attribute in the corresponding `.mediawiki` file. If the attribute does not have the `boolProperty`, then the `<attribute>` element should also have one or more child `<value></value>` elements giving the value(s) of the attribute. 

**Example:** The `requireChild` attribute represents a boolean value. In the `.mediawiki` representation this attribute appears as `{requireChild}` if present and is omitted if absent.

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

**Example:** The `suggestedTag` attribute has a valid HED tag value. In the mediawiki representation this attribute is omitted if absent and appears when present as:

```mediawiki
{suggestedTag=Sweet,suggestedTag=Gustatory-attribute/Salty, suggestedTag=Property/Sensory-property/Gustatory-attribute/Gustatory-attribute/Sour}
```

The `suggestedTag` attribute is meant to be used by tagging tools to suggest additional tags that a user might want to include. Notice that the `suggestedTag` values are  valid HED tags in any form (short, long, or intermediate).

**Old xml if present:**

```xml
<node suggestedTag="Sweet,Gustatory-attribute/Salty Property/Sensory-property/Sensory-attribute/Gustatory-attribute/Sour">
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
    	 <value>Property/Sensory-property/Sensory-attribute/Gustatory-attribute/Sour</value>
   </attribute>
</node>
```

### A.2.2. Unit classes

The valid HED-3G unit classes are defined in the `<unitClassDefinitions>` section of the XML schema file, and valid HED-3G unit modifiers are defined in the `<unitModifierDefinitions>` section. These sections follow a format similar to the `<node>` element in the `<schema>` section:

```xml
<unitClassDefinitions>
    <unitClassDefinition> ... </unitClassDefinition>
                          ... 
    <unitClassDefinition> ... </unitClassDefinition>
</unitClassDefinitions>
```

The `<unitClassDefinition>` elements have a required `<name>`, an optional `<description>` and an arbitrary number of additional `<attribute>` child elements. These `<attribute>` elements describe properties of the unit class rather than of individual unit types. In addition, `<unitClassDefinition>` elements may have an arbitrary number of `<unit>` child elements.

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

### A.2.2. Value classes

HED has very strict rules about what characters are allowed in various elements of the HED schema, HED tags and the substitutions made for `#` placeholders. These rules are encoded in the schema using value classes. When a node name or placeholder substitution is given a particular value class, that name or substituted value can only contain the characters allowed for that value class. The allowed characters for a value class are specified in the definition of the value class. The HED validator and other HED tools may hardcode information about behavior of certain value classes (for example the `numericClass` value class). **HED does not allow commas or quotes in any of its values.**


#### **Table B.2.** Value classes.

<table>
  <tr>
     <td><strong>Class name </strong></td>
     <td><strong>Allowed characters</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>dateTimeClass</code>*</td>
     <td><code>digits</code>, <code>T</code>, <code>:</code>, <code>-</code></td>
   <td>Date-times should conform to ISO8601 date-time format YYYY-MM-DDThh:mm:ss. Any variation on the full form is allowed.</td>
  </tr>
  <tr>
     <td><code>nameClass</code></td>
     <td><code>letters</code>, <code>digits</code>, <code>_</code>, <code>-</code></td>
     <td>Value class of node names and labels.</td>
  </tr>
  <tr>
     <td><code>numericClass</code>*</td>
     <td><code>digits</code>, <code>.</code>, <code>-</code>, <code>+</code>, <code>E</code>, <code>e</code></td>
     <td>Value must be a valid numerical value.</td>
  </tr>
  <tr>
     <td><code>posixPath</code>*</td>
     <td></td>
     <td>Specifies strings conforming to Posix path specification. This is not implemented and currently allows everything except commas.</td>
  </tr>
  <tr>
   <td><code>textClass</code>
   </td>
   <td><code>letters</code>, <code>digits</code>, <code>blank</code>, <code>+</code>, <code>-</code>, <code>:</code>, <code>;</code>, <code>.</code>, <code>/</code>, <code>(</code>, <code>)</code>, <code>?</code>, <code>*</code>, <code>%</code>, <code>$</code>, <code>@</code>
   </td>
   <td>Value class for text descriptions.
   </td>
  </tr>
</table>

* indicates additional syntax checks

Value classes are defined in the `<valueClassDefinitions>` section of the XML schema file. These sections follow a format similar to the `<node>` element in the `<schema>`:

```xml
<valueClassDefinitions>
    <valueClassDefinition> ... </valueClassDefinition>
                             ... 
    <valueClassDefinition> ... </valueClassDefinition>
</valueClassDefinitions>
```

### A.2.3. Schema attributes

The `<schemaAttributeDefinitions>` section specifies the allowed attributes of the other elements including the `<node>`, `<unitClassDefinition>`, `<unitModifierDefinition>`, and `<valueClassDefinition>` elements. The specifications of individual attributes are given in `<schemaAttributeDefinition>` elements.

```xml
<schemaAttributeDefinitions>
    <schemaAttributeDefinition> ...</schemaAttributeDefinition>
                                   ... 
    <schemaAttributeDefinition> ... </schemaAttributeDefinition>
</schemaAttributeDefinitions>
```

The individual `<schemaAttributeDefinition>` elements have the following format:

```xml
<schemaAttributeDefinition>
    <name>allowedCharacter</name>
    <description>An attribute of value classes indicating a special character that is allowed in expressing the value of that placeholder.</description>
    <property>
        <name>valueClassProperty</name>
    </property>
</schemaAttributeDefinition>
```

The `<property>` elements indicate where various schema attributes apply. Their meanings are hard-coded into the schema processors. Table A.3 lists the names of these properties.


#### **Table A.3.** Schema properties.

<table>
  <tr>
     <td><strong>Schema attribute property</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>boolProperty</code></td>
     <td><p>If a schema attribute has this property, then its values are either true or false.</p> <p>The schema processing translates the attribute into an <code>attribute</code> element with a <code>&lt;name></code> child but no <code>value</code> child.</p></td>
  </tr>
  <tr>
     <td><code>unitClassProperty</code>
     <td>A schema attribute having this property can only apply to an <code>attribute</code> of <code>unitClassDefinition</code> elements.</td>
  </tr>
  <tr>
     <td><code>unitModifierProperty</code></td>
     <td>A schema attribute having this property can only apply to an <code>attribute</code> of <code>unitModifierDefinition</code> elements.</td>
  </tr>
  <tr>
     <td><code>unitProperty</code></td>
     <td>A schema attribute having this property can only apply to an <code>attribute</code> of <code>unit</code> elements.</td>
  </tr>
  <tr>
     <td><code>valueClassProperty</code></td>
     <td>A schema attribute having this property can only apply to an <code>attribute</code> of <code>valueClassDefinition</code> elements.</td>
  </tr>
</table>


A given schema attribute can only apply to one type of element (`node`, `unitClassDefinition`, `unitModifierDefinition` or `unit`). Attributes that don’t have one of `unitClassProperty`, `unitClassProperty` or `unitProperty` are assumed to apply to `node` elements.

Table A.4 gives a list of the supported HED schema attributes. These attributes apply to different parts of the schema as indicated by their properties. 


#### **Table A.4. Schema attributes.

<table>
  <tr>
     <td><strong>Schema attribute</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>allowedCharacter</code>*</td>
     <td><p>A schema attribute of value classes specifying a special character that is allowed in expressing the value of a placeholder.</p> <p>Normally the allowed characters are listed individually. However, the word <code>letters</code> designates upper and lower case alphabetic characters.</p><p>The word <code>digits</code> indicates the digits 0-9.</p></td>
  </tr>
  <tr>
     <td><code>defaultUnits</code></td>
     <td><p>A schema attribute of unit classes specifying the default units to use if the placeholder has a unit class but the substituted value has no units.</p> <p>For example, when a <code>#</code> placeholder of the <code>time</code> unit class is replaced with an actual value and the units are not explicitly listed, they are assumed to be seconds (s) because the time unit class has <code>defaultUnits=s</code>.</p></td>
  </tr>
  <tr>
     <td><code>extensionAllowed</code></td>
     <td>A schema attribute indicating that users can add unlimited levels of child nodes under this tag. This tag is propagated to child nodes with the exception of # placeholders</td>
  </tr>
  <tr>
     <td><code>recommended</code></td>
     <td>A schema attribute indicating that the event-level HED string should include this tag.</td>
  </tr>
  <tr>
     <td><code>relatedTag</code>*</td>
     <td>A schema attribute suggesting HED tags that are closely related to this tag. This attribute is used by tagging tools. Related categorical tags may have this attribute.</td>
  </tr>
  <tr>
     <td><code>requireChild</code></td>
     <td>A schema attribute indicating that one of the node elements descendants must be included when using this tag.</td>
  </tr>
  <tr>
     <td><code>required</code></td>
     <td>A schema attribute indicating that every event-level HED string should include this tag.</td>
  </tr>
  <tr>
     <td><code>SIUnit</code></td>
     <td><p>A schema attribute indicating that this unit element is an SI unit and can be modified by multiple and submultiple names.</p><p>Note that some units such as byte are designated as SI units although they are not part of the standard.<p></td>
  </tr>
  <tr>
     <td><code>SIUnitModifier</code></td>
     <td>A schema attribute indicating that this SI unit modifier represents a multiple or submultiple of a base unit rather than a unit symbol.</td>
  </tr>
  <tr>
     <td><code>SIUnitSymbolModifier</code></td>
     <td>A schema attribute indicating that this SI unit modifier represents a multiple or submultiple of a unit symbol rather than a base symbol.</td>
  </tr>
  <tr>
     <td><code>suggestedTag</code>*</td>
     <td>A schema attribute that indicates another tag  that is often associated with this tag. This attribute is used by tagging tools to provide tagging suggestions.</td>
  </tr>
  <tr>
     <td><code>tagGroup</code>*</td>
     <td>A schema attribute indicating the tag can only appear inside a tag group.</td>
  </tr>
  <tr>
     <td><code>takesValue</code></td>
     <td>A schema attribute indicating the tag is a <em>#</em>> placeholder that is expected to be replaced with a user-defined value.</td>
  </tr>
  <tr>
     <td><code>topLevelTagGroup</code>*</td>
     <td>A schema attribute indicating that this tag (or its descendants) can only appear in a top-level tag group.</td>
  </tr>
  <tr>
     <td><code>unique</code></td>
     <td>A schema attribute indicating that only one of this tag or its descendants can be used  in the event-level HED string.</td>
  </tr>
  <tr>
     <td><code>unitClass</code></td>
     <td>A schema attribute specifying which unit class this value tag belongs to.</td>
  </tr>
  <tr>
     <td><code>unitPrefix</code></td>
     <td>A schema attribute applied specifically to <code>unit</code> elements to designate that the unit indicator is a prefix (e.g., <code>$</code> in the<code> currency</code> units).</td>
  </tr>
  <tr>
     <td><code>unitSymbol</code></td>
     <td>A schema attribute indicating this tag is an abbreviation or symbol representing a type of unit. Unit symbols represent both the singular and the plural and thus cannot be pluralized.</td>
  </tr>
  <tr>
     <td><code>valueClass</code>*</td>
     <td>A schema attribute specifying which value class this value tag belongs to.</td>
  </tr>
</table>

  _*_ indicates an attribute that is new to HED-3G.

In addition to the attributes listed in Table B.4, some schema attributes have been deprecated and are no longer supported in HED-3G, although they are still present in earlier versions of the schema. Table A.5 lists these attributes.


#### Table A.5. Deprecated HED schema attributes.

<table>
  <tr>
     <td><strong>Schema attribute</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>default</code></td>
     <td><p>Indicates a tag assumed to be present if not explicitly given.</p><p>Note: This tag was not implemented in existing tools. Only the defaultUnits for the unit class will be implemented going forward.</p></td>
  </tr>
  <tr>
     <td><code>position</code></td>
     <td><p>Indicates the order within the overall tag string that this tag should appear during display.</p> <p>This attribute was used to assist annotation tools, which sought to display required and recommend tags before others. The position attribute value should be an integer and the order can start at 0 or 1. Required or recommended tags without this attribute or with negative position will be shown after the others in canonical ordering.</p><p>Because of the design of the schema vocabulary, this tag is not applicable in HED-3G.</p></td>
  </tr>
  <tr>
     <td><code>predicateType</code></td>
     <td><p>This attribute has a value which is one of <code>propertyOf</code>, <code>subclassOf</code>, or <code>passThrough</code>.</p><p>This tag was added to facilitate mapping to OWL or RDF in earlier versions of the schema where property and subclass types appeared in the same hierarchy. The schema vocabulary redesign of HED-3G eliminated this issue.</p></td>
  </tr>
</table>



### A.2.5. HED unit classes and unit modifiers

Table A.6 lists the current unit classes for HED.

#### *Table A.6.* Unit classes for HED.

<table>
  <tr>
   <td><strong>Unit class</strong></td>
   <td><strong>Unit (Bold = SIUnit, * = unitSymbol)</strong></td>
   <td><strong>defaultUnits</strong></td>
  </tr>
  <tr>
     <td><code>accelerationUnits</code></td>
     <td><strong>m-per-s^2*</strong></td>
     <td>m-per-s^2*</td>
  </tr>
  <tr>
     <td><code>angleUnits</code></td>
     <td><strong>radian</strong>, <strong>rad*</strong>, degree</td>
     <td>rad</td>
  </tr>
  <tr>
     <td><code>areaUnits</code></td>
     <td><strong>metre^2</strong>, <strong>m^2*</strong></td>
     <td>m^2*</td>
  </tr>
  <tr>
     <td><code>currencyUnits</code></td>
     <td>dollar, $, point</td>
     <td>$</td>
  </tr>
  <tr>
     <td><code>frequencyUnits</code></td>
     <td><strong>hertz</strong>, <strong>Hz*</strong></td>
     <td>Hz</td>
  </tr>
  <tr>
     <td><code>intensityUnits</code></td>
     <td>dB, candela, cd</td>
     <td>dB</td>
  </tr>
  <tr>
     <td><code>jerkUnits</code></td>
     <td><strong>m-per-s^3*</strong></td>
     <td>m-per-s^3*</td>
  </tr>
  <tr>
     <td><code>memorySizeUnits</code></td>
     <td>byte, B</td>
     <td>B</td>
  </tr>
  <tr>
     <td><code>physicalLength</code></td>
     <td><strong>metre</strong>, <strong>m*</strong>, inch, foot, mile</td>
     <td>m*</td>
  </tr>
  <tr>
     <td><code>speedUnits</code></td>
     <td><strong>m-per-s</strong>*, mph, kph</td>
     <td>m-per-s*</td>
  </tr>
  <tr>
     <td><code>timeUnits</code></td>
     <td><strong>second</strong>, <strong>s*,</strong> day, minute, hour</td>
     <td>s*</td>
  </tr>
  <tr>
     <td><code>volumeUnits</code></td>
     <td><strong>metre^3</strong>, <strong>m^3*</strong></td>
     <td>m^3*</td>
  </tr>
  <tr>
     <td><code>weightUnits</code></td>
     <td><strong>gram</strong>, <strong>g*</strong>, pound, lb</td>
     <td>m^3*</td>
  </tr>

</table>


Table A.7 lists the current unit modifiers for HED-3G.

#### *Table A.7.* SI unit modifiers. 

<table>
  <tr>
     <td><strong>SI unit modifier</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td>deca, da*</td>
     <td>SI unit multiple representing 10^1</td>
  </tr>
  <tr>
     <td>hecto, h*</td>
     <td>SI unit multiple representing 10^2</td>
  </tr>
  <tr>
     <td>kilo, k*</td>
     <td>SI unit multiple representing 10^3</td>
  </tr>
  <tr>
     <td>mega, M*</td>
     <td>SI unit multiple representing 10^6</td>
  </tr>
  <tr>
     <td>giga, G*</td>
     <td>SI unit multiple representing 10^9</td>
  </tr>
  <tr>
     <td>tera, T*</td>
     <td>SI unit multiple representing 10^12</td>
  </tr>
  <tr>
     <td>peta, P*</td>
     <td>SI unit multiple representing 10^15</td>
  </tr>
  <tr>
     <td>exa, E*</td>
     <td>SI unit multiple representing 10^18</td>
  </tr>
  <tr>
     <td>zetta, Z*</td>
     <td>SI unit multiple representing 10^21</td>
  </tr>
  <tr>
     <td>yotta, Y*</td>
     <td>SI unit multiple representing 10^24</td>
  </tr>
  <tr>
     <td>deci, d*</td>
     <td>SI unit submultiple representing 10^−1</td>
  </tr>
  <tr>
     <td>centi, c*</td>
     <td>SI unit submultiple representing 10^−2</td>
  </tr>
  <tr>
     <td>milli, m*</td>
     <td>SI unit submultiple representing 10^−3</td>
  </tr>
  <tr>
     <td>micro, u*</td>
     <td>SI unit submultiple representing 10^−6</td>
  </tr>
  <tr>
     <td>nano, n*</td>
     <td>SI unit submultiple representing 10^−9</td>
  </tr>
  <tr>
     <td>pico, p*</td>
     <td>SI unit submultiple representing 10^−12</td>
  </tr>
  <tr>
     <td>femto, f*</td>
     <td>SI unit submultiple representing 10^−15</td>
  </tr>
  <tr>
     <td>atto, a*</td>
     <td>SI unit submultiple representing 10^−18</td>
  </tr>
  <tr>
     <td>zepto, z*</td>
     <td>SI unit submultiple representing 10^−21</td>
  </tr>
  <tr>
     <td>yocto, y*</td>
     <td>SI unit submultiple representing 10^−24</td>
  </tr>
</table>

 _*_ indicates an SI unit symbol modifier.


## A.3. HED schema errors

This section is organized by the type of schema format that results in the error. Errors that might be detected regardless of the schema format start with HED_SCHEMA. Errors that are specific to the `.mediawiki` format start with HED_WIKI.  Errors that occur in the construction of the XML version or that are detected by XML validators when the planned XSD validation is implemented start with HED_XML. All of the schema errors are summarized in **Table B.8**.


### A.3.1. General schema errors

**HED_SCHEMA_ATTRIBUTE_INVALID**: An attribute that appears in a schema node has not been defined in the  schema attributes section of the schema file.

**HED_SCHEMA_CHARACTER_INVALID**: The specification contains an invalid character.

**HED_SCHEMA_DUPLICATE_NODE**: Node name appears in the schema more than once.

**HED_SCHEMA_HEADER_INVALID**: The schema header has an invalid format, contains invalid characters, or has unrecognized attributes.

**HED_SCHEMA_NODE_NAME_INVALID**: A schema node element name is empty or contains invalid characters.

**HED_SCHEMA_REQUIRED_SECTION_MISSING**: One of the required schema sections (corresponding to the schema, unit classes, unit modifiers, value classes, schema attributes or properties) is missing or in the wrong place.

**HED_SCHEMA_VERSION_INVALID**: The schema version specification in the HED line or element is invalid because the version specification does not have the correct syntax for the schema file format or the schema version does not comply with semantic versioning.


### A.3.2. HED format-specific schema errors.

**HED_WIKI_DELIMITERS_INVALID**: Line content after node name is not enclosed with `<nowiki></nowiki> `delimiters; or the line has unmatched or multiple `<nowiki></nowiki>`, `[ ]`, or` { }` delimiters.

**HED_WIKI_LINE_START_INVALID**: Start of body line not `'''` or `*`.

**HED_WIKI_SEPARATOR_INVALID**: One of the required wiki section separators is missing or in the wrong place. The required separators are: `!# start schema`, `!# end schema`, and  `!# end hed`.

**HED_XML_SYNTAX_INVALID**: XML syntax or or does not comply with specified XSD.


### A.3.3. Summary of validation errors for HED schema.

Table A.9 summarizes the errors relevant for HED schema.

#### **Table A.9.** Validation errors for HED schema.

<table>
  <tr>
     <td><strong>Error or warning</strong></td>
     <td><strong>Explanation</strong></td>
  </tr>
  <tr>
     <td><code>HED_SCHEMA_ATTRIBUTE_INVALID</code></td>
     <td>Attribute not defined in one of the definition sections: <code>unitClassDefinitions</code>, <code>valueClassDefinitions</code>, <code>schemaAttributeDefinitions</code></td>
  </tr>
  <tr>
     <td><code>HED_SCHEMA_CHARACTER_INVALID</code></td>
     <td>The specification contains an invalid character.</td>
  </tr>
  <tr>
     <td><code>HED_SCHEMA_DUPLICATE_NODE</code></td>
     <td>Node name appears in the schema more than once.</td>
  </tr>
  <tr>
     <td><code>HED_SCHEMA_HEADER_INVALID</code></td>
     <td>The schema header has an invalid format, contains invalid characters, or has unrecognized attributes.</td>
  </tr>
  <tr>
     <td><code>HED_SCHEMA_NODE_NAME_INVALID</code></td>
     <td>Node element name is empty or contains invalid characters</td>
  </tr>
  <tr>
     <td><code>HED_SCHEMA_REQUIRED_SECTION_MISSING</code></td>
     <td>One of the required schema sections (corresponding to the schema, unit classes, unit modifiers, value classes, schema attributes or properties) is missing or in the wrong place.</td>
  </tr>
  <tr>
     <td><code>HED_SCHEMA_VERSION_INVALID</code></td>
     <td>The version is invalid or does not use  semantic versioning</td>
  </tr>
  <tr>
     <td><code>HED_WIKI_DELIMITERS_INVALID</code></td>
     <td>Line content after node name is not enclosed with <code>&lt;nowiki>&lt;/nowiki> </code>delimiters; or the line has unmatched or multiple <code>&lt;nowiki>&lt;/nowiki></code>, <code>[ ]</code>, or<code> { }</code> delimiters.</td>
  </tr>
  <tr>
     <td><code>HED_WIKI_LINE_START_INVALID</code></td>
     <td>Start of body line not <code>''' or *.</code></td>
  </tr>
  <tr>
     <td><code>HED_WIKI_SEPARATOR_INVALID</code></td>
     <td>One of the required wiki section separators is missing or in the wrong place. The required separators are: <code>!# start schema</code>, <code>!# end schema</code>, and  <code>!# end hed</code>.</td>
  </tr>
  <tr>
     <td><code>HED_XML_SYNTAX_INVALID</code></td>
     <td>XML syntax or or does not comply with specified XSD.</td>
  </tr>
</table>

