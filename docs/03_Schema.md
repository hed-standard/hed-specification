# 3. The HED schema

A HED schema is the formal specification of the HED vocabulary and rules for annotating events. A HED schema vocabulary is organized hierarchically so that similar concepts and terms appear close to one another in the organizational hierarchy. A HED schema is used to validate event annotations. Past, present, and future versions of the HED schema adhere to [semantic versioning](https://semver.org/) with version numbers of the form *x.y.z* representing *major.minor.patch* versions. Although schema developers work with HED schema in `.mediawiki` format for ease in editing,  HED tools generally use XML versions of the HED schema. An expandable HTML browser is also available.

HED schema XML filenames use the standardized format `HEDx.y.z.xml`. These standardized names make it easier for tools to locate the appropriate HED schema version in the HED working group [GitHub website](https://github.com/hed-standard). All schema versions are stored in the `hedxml` directory of the [HED specification repository](https://github.com/hed-standard/hed-specification). 

Third generation HED begins with schema version 8.0.0. Thus, the file containing the first official release of the third generation HED schema is `HED8.0.0.xml`. Releases are stored in [`hedxml`](https://github.com/hed-standard/hed-specification/tree/master/hedxml) directory of the [`hed-specification`](https://github.com/hed-standard/hed-specification) repository. Deprecated versions of the HED schema are stored in the [`hedxml/deprecated`](https://github.com/hed-standard/hed-specification/tree/master/hedxml/deprecated) directory of the [`hed-specification`](https://github.com/hed-standard/hed-specification) repository.


All data recordings in a dataset should be annotated using a single version of the standard HED schema. Validation and analysis tools are not expected to handle multiple versions of the standard HED schema when processing a dataset. Datasets may also include annotations from multiple HED library schema extensions in addition to those from the standard schema, as described in [Section 6](06_Library_schema.md#6-hed-library-schema) of this document. A more detailed discussion of the HED schema format appears in [Appendix A](Appendix_A.md#a-schema-format).


## 3.1. Mediawiki schema format

HED schema developers can specify a new schema version or revision in `.mediawiki` format for more convenient editing, display, and reference on GitHub. The following brief example illustrates the format. A full description of the format is given in [Appendix A](Appendix_A.md#a-schema-format).

````{admonition} Example: Excerpt of a HED schema (.mediawiki).

```moin
HED version="8.0.0" 

'''Prologue'''
This prologue introduces the schema.

!# start schema
'''Event''' <nowiki>[Something that happens at a given place and time.]</nowiki>
* Sensory-event <nowiki>{suggestedTask=Task-event-role}[Something perceivable by an agent.]</nowiki>
                              . . .
'''Property'''<nowiki>{extensionAllowed}[A characteristic.] </nowiki>
* Informational-property <nowiki>[A quality pertaining to information.]</nowiki>
** Label <nowiki>{requireChild} [A string of 20 or fewer characters.]</nowiki>
*** <nowiki># {takesValue, valueClass=nameClass}</nowiki> 
!# end schema

'''Unit classes''' <nowiki>[Unit classes and units for the nodes.]</nowiki>
                        . . .
'''Unit modifiers''' <nowiki>[Unit multiples and submultiples.]</nowiki>
                       . . .
'''Value classes''' <nowiki>[Rules for the values provided by users.]</nowiki>
                       . . .
'''Schema attributes''' <nowiki>[Allowed node attributes.]</nowiki>
                        . . .
'''Properties''' <nowiki>[Properties of the schema attributes.]</nowiki>
                        . . .
'''Epilogue'''
An optional section that is the place for notes and is ignored in HED processing.

!# end hed
```

````

Beginning with third generation HED (HED schema versions 8.0.0 and later), **terms in a given schema must be unique within that schema.** This uniqueness rule allows automated expansion of short form HED strings into their full long forms. 

Top level tree root elements are enclosed by triple single quotes. Each child term within the schema must be on a single line that begins with a certain number of asterisks(*) corresponding to the term’s level within the hierarchy. 

Everything after each HED term must be enclosed by `<nowiki></nowiki>` markup elements. Items within these markup elements include a term description and term attributes. Term (node element) descriptions, which are enclosed in square brackets in the mediawiki specification, indicate the meaning of the term or tag they modify. HED schema attributes, which are enclosed with curly braces, provide additional rules about how the tags and its modifying values should be used and handled by tools. Allowed HED schema attributes for HED terms are those schema attributes that do not have the `unitClassProperty`, `unitModifierProperty`, `unitProperty`, or `valueClassProperty`. 

Attributes appear in the schema specification either as `name` attributes or as `name=value` pairs. The presence of a `name` attribute for a schema node element indicates that the attribute is true for that node, while the presence of a `name=value` attribute indicates that the attribute has the specified value for that node. If multiple values of a particular attribute are applicable, they should be specified as separate name-value pairs.

The hashtag character (`#`) is a placeholder for a user-supplied value. Within the HED schema a `#` node indicates that the user must supply a value consistent with the unit classes and value classes of the `#` node if it has any. Unit classes and value classes are specified in curly braces and treated like other schema attributes.  Lines with hashtag (#) placeholders should have everything after the asterisks enclosed by `<nowiki></nowiki>` markup elements. The values of HED tag placeholders cannot stand alone, but must include the parent when used in a HED string.  In the above example, the `#` that is a child of the *Label* node must include *Label* when used (e.g., *Label/myLabel*). 


## 3.2. XML schema format

The HED XML schema format encodes the hierarchical vocabulary as nested `<node>` elements. The HED XML version of the schema is used during validation and analysis. Tools including an online converter are available to convert between `.mediawiki` and `.xml` formats. An expandable HTML browser view is also available for easy viewing. The `.xml` format has changed with the release of HED-3G. This modification of the XML format was done for four reasons:

1. To correctly handle multiple values of schema attributes.
2. To preserve the prologue and epilogue information present in `.mediawiki` files.
3. To allow schema attributes to be formally specified and validated.
4. To allow an XSD specification of the HED schema for validation of the schema.

The following is a translation of the `.mediawiki` example from the previous section in the new XML format. A complete specification of the format is given in Appendix B.

````{admonition} Example: XML version of previous example.

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
                    <attribute>
                        <name>requireChild</name>
                    </attribute>
                <node>
                    <name>#</name>
                    <attribute>
                        <name>takesValue</name>
                    </attribute>
                    <attribute>
                        <name>valueClass</name>
                        <value>nameClass</value>
                    </attribute>
                </node></node>
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

Each `<node>` element must have a `<name>` child element corresponding to the HED tag term that it specifies. A `<node>` element may also have a `<description>` child element containing the text that appears in square brackets `[]` in the `.mediawiki` version. The schema attributes (which appear as `name` values or `name-value` pairs enclosed in curly braces {} in the `.mediawiki` file) are translated into `<attribute>` child elements of `<node>` in the `.xml`.  These schema attributes are not to be confused with the HED *Attribute* tag that is part of the HED vocabulary. 

The HED schema also includes a `<unitClassDefinitions>` section that specifies the allowed unit classes and the corresponding allowed unit names. Only the singular version of each unit name is explicitly specified, but the corresponding plurals of the explicitly mentioned singular versions are also allowed (e.g., `feet` is allowed in addition to `foot`). HED uses a `pluralize` function available in both Python and Javascript to check validity.  

The `<unitModifierDefinitions>` section lists the SI unit multiples and submultiples that are allowed to be prepended to units that have the SIUnit schema attribute. 

The `<valueClassDefinitions> `section specifies rules for the values that are substituted for placeholders (`#`). Examples are special characters that are allowed for numeric values or dates. Placeholders that have no `valueClass` attributes, are assumed to follow the rules for HED tag naming described in the next section.

The `<schemaAttributeDefinitions>` section lists the schema attributes that apply to some nodes and definitions in other sections of the schema. The specification of which type of elements an attribute may apply to is specified by the property attributes of these schema attributes. 

The `<schemaAttributeDefinitions>` section lists the schema attributes that apply to some nodes and definitions in other sections of the schema. The specification of which type of elements an attribute may apply to is specified by the property attributes of these schema attributes. 


## 3.3. Allowed schema characters

The different parts of the HED schema have different rules for the characters that are allowed. Table 3.1 summarizes the rules. UTF-8 characters are not supported. Values that don’t have an associated valueClass attribute are assumed to have `valueClass=nameClass`.

### Table 3.1. Rules for valid schema characters.

<table>
  <tr>
     <td><strong>Item</strong></td>
     <td><strong>Allowed characters</strong></td>
     <td><strong>Style suggestions and other rules</strong></td>
  </tr>
  <tr>
     <td>Node elements<br>(HED tag names<br><code>valueClass=nameClass</code></td>
     <td>Alphanumeric characters, hyphens, and underbars with no white space.</td>
     <td>The first letter of a term should be capitalized for readability. The remaining characters should be lowercase.</td>
  </tr>
  <tr>
     <td>Descriptions<br><code>valueClass=textClass</code></td>
     <td>Alphanumeric characters, blanks, commas, periods, semicolons, colons, hyphens, underbars, forward slashes, carets (^), and parentheses are allowed.  No square brackets, curly braces, quotes, or other punctuation and symbols are allowed.</td>
     <td>Descriptions should be concise sentences, possibly with clarifying examples.</td>
  </tr>
  <tr>
     <td>Placeholder (<code>#</code>) substitutions by user-defined values.</td>
     <td>The characters allowed depend on the <code>valueClass</code> for the value plus the actual characters in the units and in the unit modifiers if applicable.</td>
   <td><p>If the <code>#</code> has <code>valueClass</code> attributes, the value may have special characters as specified by in the class definition. For example, the colon (:) is specifically allowed for the <code>dateTime</code> unit class.</p><p>Units are separated from the value by at least one blank whether prefix or suffix.</p> </td>
  </tr>
  <tr>
     <td>Library names and nicknames</td>
     <td>A single word containing only alphabetic characters.</td>
     <td>Library nicknames are followed by a single colon when used in a tag string.</td>
  </tr>
</table>


## 3.4. Vocabulary organization

The HED-3G schema (version 8.0.0 and above) contains six root trees of HED terms: *Event*, *Agent*, *Action*, *Item*, *Property*, and *Relation*. 

The *Event* root tree terms indicate the general category of the event, such as whether it is a sensory event, an agent action, a data feature, or an event indicating experiment control or structure. The HED annotations describing each event may be assembled from a number of sources during processing. The assembled HED string annotating an event should have at least one tag from the *Event* tree, as many analysis tools use the *Event* tags as a primary means of segregating, epoching and processing the data. Ideally, tags from the *Event* subtree should appear at the top level of the HED annotation describing an event to facilitate analysis.

The *Agent* root tree terms indicate types of agents (e.g., persons, animals, avatars)  that take an active role or produce a specified effect. An *Agent* tag should be grouped with property tags that provide information about the agent, such as whether the agent is an experiment participant.

The *Action* root tree terms describe actions performed by agents. 

The *Item* root tree terms describe things with (actual or virtual) physical existence such as objects, sounds, or language. 

Descriptive elements are organized in the *Property* rooted tree, and binary relations are in the *Relation* rooted tree. These descriptive elements should always be grouped with the elements they describe using parentheses. 


## 3.5. Tag syntax

A **HED tag** is a term in the HED vocabulary identified by a path consisting of the individual node names from some branch of the HED schema hierarchy separated by forward slashes (/). An important requirement of third generation HED is that the node names in the HED schema **must be unique**. As a consequence, the user can specify as much of the path to the root as desired. The full path version is referred to as **long form** and truncated versions as **short form**. HED tools are available to map between shortened tags and long form as needed. 

Table 3.2 compares the long forms of several representative tags to various equivalent short-form values. The # placeholder child for *Label* in the HED schema must be replaced by a string value when the tag is used for annotation. The values that replace these # placeholders cannot be node names.


### Table 3.2. Long versus short form.

<table>
  <tr>
     <td><strong>Long form (full path from node to root)</strong></td>
     <td><strong>Short form(s)</strong></td>
  </tr>
  <tr>
     <td><em>Event/Sensory-event</em></td>
     <td><em>Sensory-event</em></td>
  </tr>
  <tr>
     <td><em>Property/Informational-property/Label/Image1</em></td>
     <td><em>Label/Image1</em><br><em>Informational-property/Label/Image1</em><br></td>
  </tr>
  <tr>
     <td><em>Item/Object/Geometric-object/2D-shape/Triangle</em></td>
     <td><em>Triangle</em><br><em>2D-shape/Triangle</em><br><em>Geometric-object/2D-shape/Triangle</em><br><em>Object/Geometric-object/2D-shape/Triangle</em></td>
  </tr>
</table>

A **HED string** is a comma-separated list of HED tags and/or HED tag groups. A **HED tag group** is a comma-separated list of HED tags and/or tag groups enclosed in parentheses. Tag groups may include other tag groups. Parentheses convey association, since HED strings are _unordered_ lists. The terms in a HED string must be unique, thus, a HED string forms a set.

**Example:** A nested HED tag group indicating that the experiment’s subject pressed a mouse button.

**Short form:**

```
    ((Human-agent, Experiment-participant), (Press, Mouse-button))
```

**Long form:**
```
((Agent/Human-agent,
    Property/Agent-property/Agent-task-role/Experiment-participant),
(Action/Move/Move-body-part/Move-upper-extremity/Press,
 Item/Object/Man-made-object/Device/IO-device/Input-device/Computer-mouse/Mouse-button))
```

The syntax and errors for HED tags and HED strings are summarized in **Appendix C**

**HED # placeholders** cannot have siblings. Thus, tags that have placeholder children cannot be extended even if they inherit an `extensionAllowed` attribute from an ancestor. The parsers treat any child of these tags as a value rather than a tag.  

**HED values** can be strings or numeric values followed by a unit specification. If a `unitClass` is specified as an attribute of the `#` node, then the units specified must be valid units for that `unitClass`. **HED parsers assume that units are separated from values by at least one blank.**
