# B. HED errors

This appendix summarizes the error codes used by HED validators and other tools.

HED-compliant tools may assume that it if a HED annotation has been properly validated,
it will comply with the rules of the HED specification.
Annotators and analysts are mainly concerned with 
HED validation errors relating to incorrectly annotated events.
See [**B.1: HED validation errors**](#b1-hed-validation-errors) 
for a listing of errors keyed to the HED specification.

HED-compliant tools assume that the HED schemas available on the 
[**hed-standard/hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository
are error-free, and that schema errors can only occur due to failure to locate or read a HED schema.

HED schema developers are mainly concerned with errors and inconsistencies in the schema itself.
Schemas under development should be validated at all stages of development.
See [**B.2: Schema validation errors**](#b2-schema-validation-errors) for a listing
of errors keyed to the HED specification.


## B.1. HED validation errors 

### CHARACTER_INVALID

A HED string contains an invalid character.

**a.**  The HED string contains a UTF-8 character.  
**b.** Curly braces appear in a HED string not in a sidecar.


**Notes:**  
- HED uses ANSI encoding and does not support UTF-8.  
- Different parts of a HED string have different rules for acceptable characters.
 
See 
[**3.2.4 Tags that take values**](03_HED_formats.md#324-tags-that-take-values) and
[**3.2.5: Tag extensions**](03_HED_formats.md#325-tag-extensions) for
an explanation of the rules for tag values and extensions.

### COMMA_MISSING

HED tag groups and tags must be separated with commas. 
In the following `A`, `B`, `C`, and `D` represent HED expressions.

**a.**  Two tag groups are not separated by commas: (`A`, `B`)(`C`, `D`).  
**b.**  A tag and a tag group are not separated by commas: `A`(`B`,`D`).  

**Note:** Commas missing between two HED tags are generally detected as invalid HED tags,
rather than as missing commas.

See [**3.2.7.3. Empty tags and groups**](./03_HED_formats.md#3273-empty-tags-and-groups)
for an explanation of the rules for empty tags.

See also [**TAG_EMPTY**](./Appendix_B.md#tag_empty).


### DEF_EXPAND_INVALID

**a.**  A `Def-expand` tag's name does not correspond to a definition.  
**b.**  A `Def-expand` is missing an expected placeholder value or has an unexpected placeholder value.  
**c.**  A `Def-expand` has a placeholder value of incorrect format or units for definition.   
**d.**  The tags within a `Def-expand` do not match the corresponding definition.  
**e.**  A `Def-expand` tag group is missing its inner tag group.  
**f.**  A `Def-expand` tag group has extra tags or groups.


See [**3.2.8.2. The Def and Def-expand tags**](./03_HED_formats.md#3282-def-and-def-expand-tags)
for an explanation of the rules for `Def-expand` and 
[**5.2. Using definition**](./05_Advanced_annotation.md#52-using-definitions) 
for more details and examples.


### DEF_INVALID

**a.**  A `Def` tag's name does not correspond to a definition.   
**b.**  A `Def` tag is missing an expected placeholder value or has an unexpected placeholder value.    
**c.**  A `Def` has a placeholder value of incorrect format or units for definition.  

See [**3.2.8.2. The Def and Def-expand tags**](./03_HED_formats.md#3282-def-and-def-expand-tags)
for an explanation of the rules for `Def` and 
[**5.2. Using definition**](./05_Advanced_annotation.md#52-using-definitions) 
for more details and examples.


### DEFINITION_INVALID
A **definition** is a tag group containing a `Definition` tag and a single tag group with
the definition's contents.  

**a.**  A `Definition` tag does not appear in a tag group at the top level in an annotation.   
**b.**  A definition's enclosing tag group is missing the inner tag group (.i.e., the definition's contents).    
**c.**  A definition's enclosing tag group contains more than a `Definition` tag and an inner group.    
**d.**  A definition's inner tag group contains `Definition`, `Def` or `Def-expand` tags.  
**e.** A definition uses curly braces.  
**f.**  A definition that includes a placeholder (`#`) does not have exactly two `#` characters.   
**g.**  A definition has placeholders (`#`) in incorrect positions.  
**h.**  Definitions of the same name appear with and without a `#`.  
**i.**  Multiple `Definition` tags with same name are encountered.  
**j.**  A tag with a `required` or `unique` attribute appears in a definition.  
**k.**  A definition appears in an unexpected place such as an events file or in a sidecar dictionary that
contains non-definition entries.  

See [**3.2.8.1. The Definition tag**](./03_HED_formats.md#3281-the-definition-tag)
for an explanation of the rules for definitions.
See also [**5.1. Creating definitions**](./05_Advanced_annotation.md#51-creating-definitions) 
and [**5.2. Using definitions**](./05_Advanced_annotation.md#52-using-definitions)
for more details and examples of definition syntax.

### ELEMENT_DEPRECATED*
A schema element has been deprecated and should not be used. When an element is updated,
its description is updated to include the reason for deprecation and a suggested path for updating usage.  

**a.** A tag has been deprecated and an alternative method of tagging should be used.  
**b.** A unit, unit class, value class has been deprecated and an alternative should be used.  

See [**A.1.4. Schema attributes**](./Appendix_A.md#a14-schema-attributes) for additional information
about the `deprecatedFrom` schema attribute.

### NODE_NAME_EMPTY

**a.**  A tag has one or more forward slashes (`/`) at beginning or end (ignoring whitespace).  
**b.**  A tag contains consecutive forward slashes (ignoring whitespace).  

See [**3.2.3 Tag forms**](./03_HED_formats.md#322-tag-forms) for more information.

### ONSET_OFFSET_INSET_ERROR

Note: For the purpose of `Onset`/`Offset` matching, `Def` or `Def-expand` tags with
different placeholder substitutions are considered to be different.

**a.**  An `Onset` or `Offset` tag does not appear in a tag group.  
**b.**  An `Onset` or `Offset` tag appears in a nested tag group (not a top-level tag group).   
**c.**  An `Onset` or `Offset` tag is not grouped with exactly one `Def` tag or `Def-expand` group.   
**d.** An `Onset` or an `Inset` tag group contains more than one additional tag group.   
**e.** An `Offset` appears with one or more tags or additional tag groups.   
**f.**  An `Offset` tag appears before an `Onset` tag associated with the same definition.     
**g.**  An `Offset` tag associated with a given definition appears after a previous `Offset` tag.
without the appearance of an intervening `Onset` of the same name.   
**h.**  An `Onset` or an `Inset` tag group with has tags besides the anchor `Def` tag or `Def-expand` group
that are not in a tag group.  
**i.** An `Onset` or  `Offset` with a given `Def` tag or `Def-expand` group anchor
appears in an event marker with the same time as with another `Onset`, `Inset`, or `Offset`
that uses the same anchor.  
**j.** An `Inset` tag is not grouped with a `Def` tag or a `Def-expand` group corresponding to an ongoing `Onset`.  
**k.** An `Onset`, `Inset`, or `Offset` tag appears in an annotation for a non-time tabular file.   

**Note:** if the `Onset` tag group's definition is in expanded form, 
the `Def-expand` will be an additional internal tag group.

See [**3.2.8.3 Onset, Offset, and Inset**](./03_HED_formats.md#3283-onset-offset-and-inset)
for a specification of the required behavior of the `Onset`, `Offset`, and `Inset` tags.

[**5.3.1. Using Onset and Offset**](./05_Advanced_annotation.md#531-using-onset-and-offset)
in Chapter 5 gives examples of usage and additional details.

### PARENTHESES_MISMATCH

**a.**  A HED string does not have the same number of open and closed parentheses.  
**b.**  The open and closed parentheses are not correctly nested in the HED string.  

See [**3.2.7.1. Parentheses and order**](./03_HED_formats.md#3271-parenthesis-and-order)
for the rules for parentheses in HED.

### PLACEHOLDER_INVALID

**a.**  A `#` appears in a place that it should not (such as in the `HED` column of an events file).  
**b.**  A JSON sidecar has a placeholder (`#`) in the HED dictionary for a categorical column.  
**c.**  A JSON sidecar does not have exactly one placeholder (`#`) in each HED string representing a value column.  
**d.**  A placeholder (`#`) is used in JSON sidecar or definition, but its parent in the schema does not have a placeholder child.  

See [**3.2.4. Tags that take values**](./03_HED_formats.md#324-tags-that-take-values)
and [**3.2.9.1. Sidecar entries**](./03_HED_formats.md#3291-sidecar-entries) for
information on the use of placeholders in HED.

### REQUIRED_TAG_MISSING

**a.**  An event-level annotation does not have a tag corresponding to a node with the `required`
schema attribute.  


**Note:**
An assembled event string must include all tags having the *required* schema attribute.

See [**3.2.10.2. Event-level processing**](./03_HED_formats.md#32103-event-level-processing) for
additional information on the `required` tag.

### SIDECAR_BRACES_INVALID

**a.**  A name appearing in curly braces in a sidecar HED annotation is not the word `HED` or the name of a HED-annotated column in the sidecar.  
**b.**  A column name entry in a sidecar has a HED annotation with curly braces, but this name also appears in curly braces in another HED annotation.  
**c.** The curly braces in a sidecar are nested or unmatched.  
**d.** The curly braces appear as the substitution for a placeholder in another tag.

See [**3.2.9. Sidecars**](./03_HED_formats.md#329-sidecars) for information
on the requirements for using sidecars.

### SIDECAR_INVALID

**a.**  The `"HED"` key is not a second-level dictionary key.  
**b.**  An annotation entry is provided for `n/a`.  

See [**3.2.9. Sidecars**](./03_HED_formats.md#329-sidecars) for a
general explanation of sidecar requirements.

### SIDECAR_KEY_MISSING*
(WARNING) 

**a.**  A value in a categorical column does not have an expected entry in a sidecar.    

**Note:** This warning is only triggered if the categorical column in which the value
appears does have HED annotations.

See [**3.2.9. Sidecars**](./03_HED_formats.md#329-sidecars) for a
general explanation of sidecar requirements.

### STYLE_WARNING*

(WARNING) 
**a.**  An extension or label does not follow HED naming conventions.  

See [**3.1.3. Naming conventions**](./03_HED_formats.md#313-naming-conventions)
for an explanation of HED naming conventions.

### TAG_EMPTY

**a.**  A HED string has extra commas or parentheses separated by only white space, indicating empty tags.  
**b.**  A HED string begins or ends with a comma (ignoring white space), indicating an empty string.  
**c.**  A tag group is empty (i.e., empty parentheses are not allowed).  

See [**3.2.7.3. Empty tags and groups**](./03_HED_formats.md#3273-empty-tags-and-groups)
for the rules on empty tags and groups. 

### TAG_EXPRESSION_REPEATED

**a.**  A tag is repeated in the same tag group or level.  

Suppose `A`, `B`, and `C` represent HED expressions.
HED strings are not ordered, so (`B`, `C`) is equivalent to (`B`, `C`).
Thus, (`A`, (`A`, `B`)) is not a duplicate, but 
(`A`, (`B`, `C`), `A`) and (`A`, (`B`, `C`), (`C`, `B`)) are duplicates.  

See [**3.2.7.4. Repeated expressions**](./03_HED_formats.md#3274-repeated-expressions)
for additional information on the rules for duplication.

### TAG_EXTENDED*
(WARNING) 

**a.**  A tag represents an extension from the schema.    

**Note:** Often such extensions are really spelling errors and not meant to extend the schema.

**Note:** Annotators are discouraged from extending the schema unless absolutely necessary.
If an extension tag is needed, annotators should consider posting an 
[**issue**](https://github.com/hed-standard/hed-schemas/issues)
explaining the tag extension so that an addition to the respective schema might be
considered.

See [**3.2.5 Tag extensions**](./03_HED_formats.md#325-tag-extensions)
for additional information on the tag extension rules.

### TAG_EXTENSION_INVALID 

**a.**  A tag extension term is already in the schema.   
**b.**  A tag extension term does not comply with rules for schema nodes.
**c.**  A tag has extension, but an extension is not allowed.

See [**3.2.5 Tag extensions**](./03_HED_formats.md#325-tag-extensions)
for additional information on the tag extension rules.

### TAG_GROUP_ERROR

**a.**  A tag has `tagGroup` or `topLevelTagGroup` attribute, but is not enclosed in parentheses.   
**b.**  A tag with the `topLevelTagGroup` does not appear at a HED tag group at the top level in an assembled HED annotation. 
**c.**  Multiple tags with the `topLevelTagGroup` attribute appear in the same top-level tag group.

See [**3.2.7.2. Tag group attributes**](./03_HED_formats.md#3272-tag-group-attributes)
for additional information on the rules for group errors due to schema attributes.

### TAG_INVALID

**a.**  The tag is not valid in the schema it is associated with.  

See [**3.2.2. Tag forms**](./03_HED_formats.md#322-tag-forms) for a discussion
of tag forms and their relationship to the HED schema.

### TAG_NAMESPACE_PREFIX_INVALID

**a.**  A tag starting with *name:* does not have an associated schema.  
**b.**  A tag prefix has invalid characters.

See [**3.2.6. Tag namespace prefixes**](./03_HED_formats.md#326-tag-namespace-prefixes) and
[**7. Library schema**](./07_Library_schemas.md) for additional information
on using multiple schemas in annotation.

### TAG_NOT_UNIQUE
 
**a.**  A tag with `unique` attribute appears more than once in an event-level HED string. 

See [**3.2.10.2. Event-level processing**](./03_HED_formats.md#32103-event-level-processing) for
additional information on the `unique` tag.

### TAG_REQUIRES_CHILD 
 
**a.**  A tag has the `requireChild` schema attribute but does not have a child.  

See [**3.2.4. Tags that take values**](03_HED_formats.md#324-tags-that-take-values)
for an explanation of the `requireChild` attribute.

### TILDES_UNSUPPORTED

The tilde notation is not supported.  

**a.**  The **tilde syntax is no longer supported** for any version of HED.  
   Annotators should replace the syntax (`A` ~ `B` ~ `C`) with (`A`, (`B`, `C`)).  
**b.**  The tilde (`~`) is considered an invalid character in all versions of the schema.  

### UNITS_INVALID
 
**a.**  A tag has a value with units that are invalid or not of the 
correct unit class for the tag.  
**b.**  A unit modifier is applied to units that are not SI units.

### UNITS_MISSING*
(WARNING)
 
**a.**  A tag that takes value and has a unit class does not have units.

See [**3.2.4 Tags that take values**](./03_HED_formats.md#324-tags-that-take-values)
for more information.

### VALUE_INVALID

**a.**  The value substituted for a placeholder (`#`) is not valid.  
**b.**  A tag value is incompatible with the specified value class.  
**c.**  A tag value with no value class is assumed to be a text and contains invalid characters.
**d.** The units are not separated from the value by a single blank.

See [**3.2.4 Tags that take values**](./03_HED_formats.md) for more information.

### VERSION_DEPRECATED*
(WARNING) 

**a.**  The HED schema version being used as been deprecated.   

It is strongly recommended that a current schema version be used as these deprecated 
versions may not be supported in the future. Deprecated versions can be found in the
[**standard_schema/hedxml/deprecated**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml/deprecated) subdirectory
or the corresponding subdirectory for individual library schemas in
the [**hed-standard/hed-schemas**](https://github.com/hed-standard/hed-schemas)
GitHub repository.

**Note:** Support for versions of the schema less than 8.0.0 is being phased out.
If you are using a deprecated version, you may need to switch to an earlier version
of the HED validators.

## B.2. Schema validation errors

This section is organized by the type of schema format that results in the error. 
Errors that might be detected regardless of the schema format start with HED_SCHEMA. 
Errors that are specific to the `.mediawiki` format start with HED_WIKI.  Errors that 
occur in the construction of the XML version or that are detected by XML validators 
when the planned XSD validation is implemented start with HED_XML.


### B.2.1. General validation errors


#### SCHEMA_ATTRIBUTE_INVALID

**a.**  An attribute is used in the schema, but is not defined in the schema attribute section.  
**b.**  A schema attribute is applied to the incorrect type (e.g., an element with the unit definition does appear
under an appropriate unit class).  
**c.** A schema attribute is used in an invalid way

| Attribute          | Invalid Usage Location                                                                                         |
|--------------------|----------------------------------------------------------------------------------------------------------------|
| `deprecatedFrom`   | An element with a `deprecatedFrom` attribute has a child node that does not have a `deprecatedFrom` attribute. |
| `rooted`          | See [SCHEMA_LIBRARY_INVALID](#schema_library_invalid)                                                          |
| `takesValue`       | Used on a non-placeholder(#) node.                                                                             |
| `unitClass`        | Used on a non-placeholder(#) node.                                                                             |
| `valueClass`       | Used on a non-placeholder(#) node.                                                                             |

**Notes:** 
- A `tag` (referred to as a node element in the schema) can have schema attributes that have the `nodeClassProperty` or the `elementProperty` or have no type property designator. 
- A `unitClass` element can only have schema attributes that have the `unitClassProperty` or the `elementProperty`.  
- A `unitModifier` element can only have schema attributes that have the `unitModifierProperty` or the `elementProperty`.  
- A `unit` element can only have schema attributes that have the `unitProperty` or the `elementProperty`.  
- A `valueClass` element can only have schema attributes that have the `valueClassProperty` or the `elementProperty`.  

#### SCHEMA_ATTRIBUTE_VALUE_INVALID

**a.** A non-boolean schema attribute has an invalid value or usage as indicated by the following table.

| Attribute       | Invalid Attribute Value                                                            |
|-----------------|------------------------------------------------------------------------------------|
| `allowedCharacter` | Not a single character or one of:<br>`letters`, `blank`, `digits`, `alphanumeric`. |
| `conversionFactor` | Not a positive numeric value.                                                      |
| `defaultUnits`    | Not a valid unit in this unit class.                                               |
| `deprecatedFrom`  | Does not correspond to a valid schema version.                                     |
| `inLibrary`       | The value of an inLibrary attribute is for the wrong library.                      |
| `relatedTag`      | Not an existing tag.                                                               |
| `rooted`          | See [SCHEMA_LIBRARY_INVALID](#schema_library_invalid)                              |
| `suggestedTag`    | Not an existing tag.                                                               |
| `unitClass`       | Not an existing unit class.                                                        |
| `valueClass`      | Not an existing value class.                                                       |

#### SCHEMA_CHARACTER_INVALID

**a.**  The specification contains an invalid character for the section in which it appears.  

#### SCHEMA_DEPRECATION_ERROR  

**a.** The value of `deprecatedFrom` is not a previously released HED schema version.  
**b.** A deprecated tag is used as a `suggestedTag` or a `relatedTag` in a non-deprecated tag.  
**c.** A child tag of a deprecated tag does not have the `deprecatedFrom` attribute.  
**d.** A deprecated attribute, unit, unit modifier or value class is used in a non-deprecated tag.  
**e.** A deprecated unit class has non-deprecated units.  


#### SCHEMA_DUPLICATE_NODE

**a.**  A schema node name appears in the schema more than once.  

#### SCHEMA_HEADER_INVALID

**a.**  The schema header has invalid characters or format.  
**b.**  The schema header has unrecognized attributes.

#### SCHEMA_LIBRARY_INVALID

Library schema errors are specific to library schema. Library schema may also raise any of the other schema errors.  
**a.**  The specified library name is not alphabetic or lowercase.  
**b.**  The `withStandard` attribute is used in a header that does not also have the `library` attribute.   
**c.**  The `withStandard` attribute value does not correspond to a valid standard schema version.  
**d.**  The `rooted` attribute appears in a schema whose header does not have `unmerged="true"` as well as appropriate `library` and `withStandard` header values.  
**e.**  A node with the `rooted` attribute is not at the top level.  
**f.**  A node with the `rooted` attribute does not correspond to a node in its partnered standard schema.  
**g.**  A library schema with the `unmerged="true"` header attribute has an `inLibrary` attribute in some element.  
**h.**  A library schema with the `unmerged="true"` duplicates special section items found in its partnered standard schema.

#### SCHEMA_SECTION_MISSING

**a.**  A required schema section is missing.   
**b.**  The required sections (corresponding to the prologue, schema, unit classes, unit modifiers, value classes,
schema attributes, properties and epilogue) are not in the correct order and hence not detected.  

**Note:** Required schema sections may be empty, but still be given.

#### SCHEMA_VERSION_INVALID

**a.**  The schema version in the HED line or element is invalid.  
**b.**  A HED version specification does not have the correct syntax for the schema file format.  
**c.**  A HED schema version does not comply with semantic versioning.  

### B.2.3. Mediawiki format errors

#### WIKI_DELIMITERS_INVALID

**a.**  Delimiters used in the wiki are invalid.    
**b.**  Schema line content after node name is not enclosed with `<nowiki></nowiki>` delimiters.  
**c.**  A line has unmatched or multiple `<nowiki></nowiki>`, `[ ]`, or `{ }` delimiters.  
**d.**  Attributes section of a node is malformed(e.g., hanging `=` character).

#### WIKI_LINE_START_INVALID

**a.**  Start of body line not `'''` or `*`.   

#### WIKI_SEPARATOR_INVALID

**a.**  A malformed section separator is present   
**b.**  A duplicate section separator is present.  

### B.2.4. XML format errors

#### XML_SYNTAX_INVALID

**a.**  XML syntax or does not comply with specified XSD.  

### B.2.5 Schema loading errors

Schema loading errors can occur because the file is inaccessible or is not proper XML.
Schema loading errors are handled in different ways by the Python and JavaScript tools.

Python tools generally raise a `HedFileError` exception when a failure to load the 
schema occurs. The calling programs are responsible for deciding how to handle such a
failure.

JavaScript tools in contrast are mainly used for validation in HED validation BIDS and
are mainly called by the [BIDS](https://bids.neuroimaging.io/) validator. 
Usually BIDS datasets provide a HED version number to designate the version of HED 
to be used, and the HED JavaScript validator is 
responsible for locating and loading schema. 

BIDS validator users do not always have
unrestricted access to the Internet during the validation process. The HED JavaScript
tools have a fallback of the loading of the specified schema fails. The validator loads
an internal copy of the most recent version of the HED schema and loads it. However, it
also reports a `SCHEMA_LOAD_FAILED` issue to alert the user that the schema used
for validation may not be the one designated in the dataset. However, validation will 
continue with the fallback schema.

If the fallback schema stored with the HED validator fails to load, 
the `SCHEMA_LOAD_FAILED` issue will also be reported and no additional
HED validation will occur.
