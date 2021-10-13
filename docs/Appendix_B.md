# B. HED errors

This appendix summarizes the error codes used by the HED validators and other tools

## B.1. HED validation errors 

**HED_CHARACTER_INVALID**: HED string contains an invalid character.  
 ~ HED uses ANSI encoding and does not support UTF-8. 
 ~ Different parts of a HED string have different rules for acceptable characters as outlined in
[Chapter 3.3: Valid characters](03_Schema.md#33-allowed-characters).

**HED_COMMA_MISSING**: HED tag groups and tags must be separated with commas.  
 ~ Commas missing between two HED tags are generally detected as invalid HED tags,
rather than as missing commas.

**HED_DEF_UNMATCHED**: A HED *Def/* label cannot be matched to definition name.  
 ~ A *Def* tag label cannot be correctly matched to a definition name because the 
definition is missing or defined multiple times.

**HED_DEF_VALUE_INVALID**: A *Def/* label value is missing or has incorrect format or value.  
~ A *Def/* tag value is a schema node name.
~ A *Def/* tag value does not meet the requirements associated with the placeholder in
its definition tag group.
~ A *Def/* tag has a value, but its corresponding *Definition* does not have a placeholder.
~ A *Def/* tag does not have a value, but its corresponding *Definition* has a value.

**HED_DEFINITION_INVALID**: The *Definition* syntax is incorrect or nested.  
 ~ A definition name is invalid or already appears as a schema node triggers this error.
 ~ A definition is that not in a top-level tag group is invalid.
 ~ A definition's enclosing tag group cannot contain another *Definition/* tag.
 ~ A definition cannot another *Definition/* or any *Def/* or *Def-expand/* tags.
 ~ Definitions that include a  placeholder (`#`) must have exactly two `#` characters:
one after the definition name and one in the definition body. 
 ~ Definitions with  placeholders (`#`) in incorrect positions are invalid.

**HED_GENERIC_ERROR:** A HED expression raised an uncategorized error.  

**HED_GENERIC_WARNING:** A HED expression raised an uncategorized warning.  

**HED_LIBRARY_UNMATCHED:** A tag starting with *name:* does not have an associated library.  
 ~ A tag that starts with *name:* is interpreted as a library schema nickname name.
 ~ The association of *name* with an actual HED library schema must be passed 
to the validator when the string containing the tag is validated.

**HED_NODE_NAME_EMPTY:** An empty tag was detected in a HED string.  
 ~ Extra slashes at beginning, end, or within a tag imply empty node names. 
 ~ A HED string cannot start or end with a slash.
 ~ A HED tag cannot contain consecutive slashes as all of these imply a term name within a HED tag.

**HED_ONSET_OFFSET_ERROR:** An *Onset* or *Offset* tag is used incorrectly.  
 ~ An *Onset* or *Offset* tag that appears without being grouped with a defined name
(using *Def/* or *Def-expand/*) triggers this error. 
 ~ *Onset* or *Offset* must be in top-level tag groups.
 ~ Only one *Onset* or *Offset* can appear in the same tag group.
 ~ An *Offset* tag cannot appear before an *Onset* tag of the same name. 
 ~ An *Offset* tag of a given name cannot appear after a previous *Offset* tag until
an intervening *Onset* of the same name has appeared. 

**HED_PARENTHESES_MISMATCH:** A HED string has unmatched open and closed parentheses.  
 ~ A HED string must have the same number of open and closed parentheses.
 ~ Open and closed parentheses must be correctly nested.  

**HED_PLACEHOLDER_INVALID:** A `#` is missing or appears in a place that it should not.  
 ~ A JSON sidecar cannot have a placeholder (`#`) the HED dictionary for a categorical column.
 ~ A JSON sidecar must have exactly one placeholder (`#`) in each HED string representing a value column.
 ~ A placeholder (`#`) cannot be used unless its parent in the schema has placeholder child.

**HED_REQUIRED_TAG_MISSING:** An event-level annotation missing a required tag.  
 ~ An assembled event string must contain all tags that have the *required* schema attribute.

**HED_SIDECAR_KEY_MISSING:** (WARNING) A categorical value is missing HED tags in sidecar.  
 ~ The events file column has a HED dictionary in the JSON sidecar, but this categorical
value does not have a key in the sidecar dictionary.

**HED_STYLE_WARNING:** (WARNING) An extension or label does not follow HED naming conventions.   
~ Tag names should start with a capital letter with the remainder lower case. 
~ Blanks are not allowed for HED-3G labels or tag extensions. Use hyphens (not under bars) instead.

**HED_TAG_EMPTY:** Extra commas or empty parentheses indicate empty tags.  
 ~ A HED string cannot have multiple consecutive commas (ignoring white space).
 ~ A HED string cannot begin or end with a comma, which also implies an empty HED tag. 
 ~ A tag group cannot be empty, so empty parentheses are not allowed.

**HED_TAG_EXTENDED:** (WARNING) HED tag represents an extension from the schema.  
 ~ Issued to warn annotators that this tag represents an extension of the HED schema. Often such tags were really spelling errors and not meant to extend the schema.

**HED_TAG_GROUP_ERROR:** A tag does not have its required tag group behavior.  
 ~ A tag has `tagGroup` or `topLevelTagGroup` attribute but is not in an appropriate tag group.
 ~ A tag with the `topLevelTagGroup` attribute appears in same tag group as other tags with the `topLevelTagGroup` attribute.

**HED_TAG_INVALID:** The tag is not valid in this schema.  
 ~ The tag has incorrect format for compliance with this schema. 
 ~ The tag is used as a tag extension or placeholder value while appearing elsewhere in the schema.

**HED_TAG_NOT_UNIQUE:** A HED tag with *unique* attribute appears more than once in an event-level HED string.  

**HED_TAG_REPEATED:** HED tags cannot be repeated in the same tag group or level.  
 ~ HED strings are not ordered, so *(B, C)* is considered to be equivalent to *(B, C)*.
 ~  *(A, (A, B))* is not considered to be a duplicate.
 ~  *(A, (B, C), A)* and *(A, (B, C), (C, B))* are repeated. 

**HED_TAG_REQUIRES_CHILD:** A HED tag requires an additional ending node.   
 ~ The tag has the *requireChild* schema attribute.

**HED_TILDES_UNSUPPORTED:** The tilde notation is no longer supported.   
 ~ The **tilde syntax is no longer supported** for any version of HED.
   Annotators should replace the syntax *(A ~ B ~ C)* with *(A, (B, C))*.  
 ~ The tilde (`~`) is considered an invalid character in all versions of the schema.

**HED_UNITS_DEFAULT_USED:** (WARNING) A HED tag value is missing units.   
 ~ If the corresponding unit class has default units, those are assumed. 

**HED_UNITS_INVALID:** HED tag value has incorrect or invalid units.  
 ~ The HED tag has a value with units that are invalid or not of the 
correct unit class for the tag. 
 ~ A typical mistake is to use unit modifiers with units that are not SI units.  

**HED_VALUE_INVALID:** The value substituted for a placeholder (`#`) is not valid.  
 ~ The value may be incompatible with the specified value class.
 ~ Values with no value class may contain invalid characters.
 ~ The value is a schema node name.

**HED_VERSION_DEPRECATED:** (WARNING) The HED version is deprecated.  
 ~ It is strongly recommended that a current version be used as these deprecated 
versions may not be supported in the future.
 ~ Deprecated versions can be found in
[https://github.com/hed-standard/hed-specification/tree/master/hedxml/deprecated](https://github.com/hed-standard/hed-specification/tree/master/hedxml/deprecated).

**HED_VERSION_WARNING:** (WARNING) The HED version number or HED schema was not provided or was invalid, so the latest version is used.


## B.2. HED schema errors

This section is organized by the type of schema format that results in the error. 
Errors that might be detected regardless of the schema format start with HED_SCHEMA. 
Errors that are specific to the `.mediawiki` format start with HED_WIKI.  Errors that 
occur in the construction of the XML version or that are detected by XML validators 
when the planned XSD validation is implemented start with HED_XML.


### B.2.1. General schema errors

**HED_SCHEMA_ATTRIBUTE_INVALID:** An attribute not defined in the appropriate schema section.    
 ~ The `unitClass` attribute must be defined in the `unitClassDefinitions` section of the schema.
 ~ A `unitClass` attribute has an invalid suffix because it is not a plural or unit modifier.
 ~ A `valueClass` attribute must be defined in the `valueClassDefinitions` section of the schema.
 ~ Other attributes should be defined in the `schemaAttributeDefinitions` section.

**HED_SCHEMA_CHARACTER_INVALID:** The specification contains an invalid character.  

**HED_SCHEMA_DUPLICATE_NODE:** A schema node name appears in the schema more than once.  

**HED_SCHEMA_HEADER_INVALID:** The schema header is invalid.  
 ~ Invalid characters or format in the header can trigger this.
 ~ Unrecognized header attributes can also cause this error.

**HED_SCHEMA_NODE_NAME_INVALID:** Schema node name is empty or contains invalid characters.  

**HED_SCHEMA_REQUIRED_SECTION_MISSING:** A required schema section is missing.   
 ~ The required sections (corresponding to the schema, unit classes, unit modifiers, value classes, schema attributes, and properties) must be included in this order even if their content is empty.

**HED_SCHEMA_VERSION_INVALID:** The schema version in the HED line or element is invalid.  
 ~ Version specification does not have the correct syntax for the schema file format or the schema version does not comply with semantic versioning.


### B.2.2. HED format-specific schema errors.

**HED_WIKI_DELIMITERS_INVALID:** Delimiters used in the wiki are invalid.    
 ~ Line content after node name is not enclosed with `<nowiki></nowiki>` delimiters.
 ~ A line has unmatched or multiple `<nowiki></nowiki>`, `[ ]`, or `{ }` delimiters.

**HED_WIKI_LINE_START_INVALID:** Start of body line not `'''` or `*`.  

**HED_WIKI_SEPARATOR_INVALID:** Required wiki section separator is missing or misplaced.  
 ~ The required separators are: `!# start schema`, `!# end schema`, and  `!# end hed`.

**HED_XML_SYNTAX_INVALID:** XML syntax or does not comply with specified XSD.  
