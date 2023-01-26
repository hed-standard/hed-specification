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

**a.**  The string contains a UTF-8 character.  
(HED uses ANSI encoding and does not support UTF-8.) 
**b.**  An extension or a value substituted for a `#` is not allowed by its value or unit class.  

Different parts of a HED string have different rules for acceptable characters as outlined in
[**3.2.4 Tags that take values**](03_HED_formats.md#324-tags-that-take-values)
[**3.2.5: Tag extensions**](03_HED_formats.md#325-tag-extensions).

### COMMA_MISSING

HED tag groups and tags must be separated with commas.  

**a.**  Two tag groups are not separated by commas: *(A, B)(C, D)*.  
**b.**  A tag and a tag group are not separated by commas: *A,(B,D)*.  

**Note:** Commas missing between two HED tags are generally detected as invalid HED tags,
rather than as missing commas.

### DEF_EXPAND_INVALID

**a.**  A `Def-expand` tag's name does not correspond to a definition.  
**b.**  A `Def-expand` is missing an expected placeholder value or has an unexpected placeholder value.  
**c.**  A `Def-expand` has a placeholder value of incorrect format or units for definition.   
**d.**  The tags within a `Def-expand` do not match the corresponding definition.  


### DEF_INVALID

**a.**  A `Def` tag's name does not correspond to a definition.   
**b.**  A `Def` tag is missing an expected placeholder value or has an unexpected placeholder value.    
**c.**  A `Def` has a placeholder value of incorrect format or units for definition.  


### DEFINITION_INVALID
A **definition** is a tag group containing a `Definition` tag and a single tag group with
the definition's contents.  

**a.**  A definition does not appear in a tag group at the top level in an annotation.   
**b.**  A definition's enclosing tag group is missing the inner tag group (.i.e., the definition's contents).    
**c.**  A definition's enclosing tag group contains more than a `Definition` tag and an inner group.    
**d.**  A definition's inner tag group contains `Definition`, `Def` or `Def-expand` tags.    
**e.**  A definition that includes a placeholder (`#`) does not have exactly two `#` characters.    
**f.**  A definition's two placeholders (`#`) but one or more of them are in incorrect positions.  
**g.**  Definitions of the same name appear with and without a `#`.  
**h.**  Multiple `Definition` tags with same name are encountered.  


### NODE_NAME_EMPTY

**a.**  An empty tag was detected in a HED string.  
**b.**  A tag has one or more forward slashes (`\`) at beginning or end (ignoring whitespace).  
**c.**  A tag contains consecutive forward slashes (ignoring whitespace).  

### ONSET_OFFSET_ERROR

Note: For the purpose of `Onset`/`Offset` matching, `Def` or `Def-expand` tags with
different placeholder substitutions are considered to be different.

**a.**  An `Onset` or `Offset` tag does not appear in a tag group.  
**b.**  An `Onset` or `Offset` tag appears in a nested tag group (not a top-level tag group).   
**c.**  An `Onset` or `Offset` tag appears without being grouped with a definition name
and a `Def-expand` tag group or a `Def`.  
**d.**  An `Onset` appears in a tag group with more than a single `Def` or `Def-expand` and
at most one additional tag group.  
**e.**  An `Offset` tag appears before an `Onset` tag associated with the same definition.  
**f.**  An `Offset` tag associated with a given definition appears after a previous `Offset` tag
without the appearance of an intervening `Onset` of the same name.   
**g.**  An `Onset` tag group either lacks an internal tag group or has more than one internal
tag group.  

**Note:** if the `Onset` tag group's definition is in expanded form, 
the `Def-expand` will be an additional internal tag group.

### PARENTHESES_MISMATCH

**a.**  A HED string does not have the same number of open and closed parentheses.  
**b.**  The open and closed parentheses are not correctly nested in the HED string.  

### PLACEHOLDER_INVALID

**a.**  A `#` appears in a place that it should not (such as in the `HED` column of an event file outside a definition).  
**b.**  A JSON sidecar has a placeholder (`#`) in the HED dictionary for a categorical column.  
**c.**  A JSON sidecar does not have exactly one placeholder (`#`) in each HED string representing a value column.  
**d.**  A placeholder (`#`) is used in JSON sidecar or definition, but its parent in the schema does not have a placeholder child.  


### REQUIRED_TAG_MISSING

**a.**  An event-level annotation does not have a tag corresponding to a node with the `required`
schema attribute.  

**Note:**
An assembled event string must all tags that have the *required* schema attribute.

### SIDECAR_KEY_MISSING*
(WARNING) 

**a.**  A value in a categorical column does not have an expected entry in a sidecar.    

**Note:** This warning is only triggered if the categorical column in which the value
appears does have HED annotations, but a particular column value does not have
an annotation.

### STYLE_WARNING*

(WARNING) 
**a.**  An extension or label does not follow HED naming conventions.  


### TAG_EMPTY

**a.**  A HED string has extra commas or parentheses separated by only white space, indicating empty tags.  
**b.**  A HED string begins or ends with a comma (ignoring white space), indicating an empty string.  
**c.**  A tag group is empty (i.e., empty parentheses are not allowed).  

### TAG_EXTENDED*
(WARNING) 

**a.**  A tag represents an extension from the schema.    

**Note:** Often such extensions are really spelling errors and not meant to extend the schema.

**Note:** Annotators are discouraged from extending the schema unless absolutely necessary.
If an extension tag is needed, annotators should consider posting an 
[**issue**](https://github.com/hed-standard/hed-schemas/issues)
explaining the tag extension so that an addition to the respective schema might be
considered.

### TAG_GROUP_ERROR

**a.**  A tag has `tagGroup` or `topLevelTagGroup` attribute,
but is not enclosed in parentheses.
**b.**  A tag with the `topLevelTagGroup` does not appear at a HED tag group at the top level
in an assembled HED annotation.

### TAG_INVALID

**a.**  The tag is not valid in the schema it associated with.  


### TAG_NOT_UNIQUE

**a.**  A tag appears multiple times at the same level in a HED group or HED string.  
**b.**  A tag with `unique` attribute appears more than once in an event-level HED string.  

### TAG_PREFIX_UNMATCHED

**a.**  A tag starting with *name:* does not have an associated schema.  
**b.**  A tag starting with *name:* is interpreted as a schema nickname name, but no
corresponding library schema has been defined.  


### TAG_REPEATED

**a.**  A tag is repeated in the same tag group or level.  

Note: HED strings are not ordered, so *(B, C)* is equivalent to *(B, C)*:
**a.**  *(A, (A, B))* is not a duplicate.  
**b.**  *(A, (B, C), A)* and *(A, (B, C), (C, B))* are duplicates.  

### TAG_REQUIRES_CHILD 
 
**a.**  A tag has the `requireChild` schema attribute but does not have a child.  

### TILDES_UNSUPPORTED

The tilde notation is not supported in HED versions >= 8.0.0 supported.  

**a.**  The **tilde syntax is no longer supported** for any version of HED.  
   Annotators should replace the syntax *(A ~ B ~ C)* with *(A, (B, C))*.  
**b.**  The tilde (`~`) is considered an invalid character in all versions of the schema.  


### UNITS_DEFAULT_USED*
(WARNING) 

**a.**  A HED tag value is missing units although the `#` placeholder has a unit class.  
If the corresponding unit class has default units, those are assumed. 

### UNITS_INVALID

ED tag value has incorrect or invalid units.  
**a.**  A tag has a value with units that are invalid or not of the 
correct unit class for the tag.  
**b.**  A unit modifiers is with units that are not SI units.  

### VALUE_INVALID

**a.**  The value substituted for a placeholder (`#`) is not valid.  
**b.**  A tag value is incompatible with the specified value class.  
**c.**  A tag value with no value class is assumed to be a text and may contain invalid characters.  

### VERSION_DEPRECATED*
(WARNING) 

**a.**  The HED schema version being used as been deprecated.   

It is strongly recommended that a current schema version be used as these deprecated 
versions may not be supported in the future. Deprecated versions can be found in the
[**standard_schema/hedxml/deprecated**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml/deprecated) subdirectory
or the corresponding subdirectory for individual library schemas in
the [**hed-standard/hed-schemas**](https://github.com/hed-standard/hed-schemas)
GitHub repository.

### VERSION_WARNING*
(WARNING) 

**a.**  The schema version was not provided or was invalid, so the latest version is used.  


## B.2. Schema validation errors

This section is organized by the type of schema format that results in the error. 
Errors that might be detected regardless of the schema format start with HED_SCHEMA. 
Errors that are specific to the `.mediawiki` format start with HED_WIKI.  Errors that 
occur in the construction of the XML version or that are detected by XML validators 
when the planned XSD validation is implemented start with HED_XML.


### B.2.1. General validation errors

#### LIBRARY_NAME_INVALID

**a.**  The specified library name is not alphabetic or lowercase.  

#### SCHEMA_ATTRIBUTE_INVALID

**a.**  An attribute is used in the schema, but is not defined in the appropriate schema section.  
**b.**  A schema attribute is defined in the wrong section (e.g., a unit definition does appear
under an appropriate unit class).  

**Note:** 
- A `unitClass` attribute must be defined in the `unitClassDefinitions` section of the schema.  
- A `valueClass` attributes must be defined in the `valueClassDefinitions` section of the schema.  
- A `schemaAttribute` must be defined in the `schemaAttributeDefinitions` section of the schema.  

#### SCHEMA_CHARACTER_INVALID

**a.**  The specification contains an invalid character.  

#### SCHEMA_DUPLICATE_NODE

**a.**  A schema node name appears in the schema more than once.  

#### SCHEMA_HEADER_INVALID

**a.**  The schema header has invalid characters or format.  
**b.**  The schema header has unrecognized attributes.  

#### SCHEMA_NODE_NAME_INVALID

**a.**  Schema node name is empty or contains invalid characters.  

#### SCHEMA_SECTION_MISSING

**a.**  A required schema section is missing.   
**b.**  The required sections (corresponding to the schema, unit classes, unit modifiers, value classes,
schema attributes, and properties) are not in the correct order and hence not detected.  

**Note:** Required schema sections may be empty, but still be given.

#### SCHEMA_VERSION_INVALID

**a.**  The schema version in the HED line or element is invalid.  
**b.**  A HED version specification does not have the correct syntax for the schema file format.  
**c.**  A HED schema version does not comply with semantic versioning.  


### B.2.2. Mediawiki format errors

#### WIKI_DELIMITERS_INVALID

**a.**  Delimiters used in the wiki are invalid.    
**b.**  Schema line content after node name is not enclosed with `<nowiki></nowiki>` delimiters.  
**c.**  A line has unmatched or multiple `<nowiki></nowiki>`, `[ ]`, or `{ }` delimiters.  

#### WIKI_LINE_START_INVALID

**a.**  Start of body line not `'''` or `*`.   

#### WIKI_SEPARATOR_INVALID

**a.**  Required wiki section separator is missing or misplaced.   
**b.**  A required schema separator is missing. (The required separators are: `!# start schema`, `!# end schema`, and  `!# end hed`.)  

### B.2.3. XML format errors

#### XML_SYNTAX_INVALID

**a.**  XML syntax or does not comply with specified XSD.  

### B.2.4 Schema loading errors

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
