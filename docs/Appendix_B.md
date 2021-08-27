# B. HED validation errors

This appendix specifies the details and requirements for HED tags. It also summarizes the error codes used by the HED validators. 


## B.1. Valid characters

**HED_INVALID_CHARACTER**: HED uses ASCII encoding and does not support UTF-8. The allowed punctuation is limited. Table B.1 lists the allowed characters for various HED elements and explains some associated rules. 

### **Table B.1.** Valid characters.

<table>
  <tr>
     <td><strong>HED element</strong></td>
     <td><strong>Allowed characters and rules</strong></td>
  </tr>
  <tr>
     <td>HED node element names</td>
     <td>
        <p>Upper or lower case letters, numbers, hyphens, underbars.</p>
        <p>The `#` is allowed as a placeholder in some situations.</p>
        <p>No blanks are allowed for HED versions >  8.0.0-alpha.1</p>
        <p>Blanks around comma and parentheses delimiters are not considered to be part of the HED tag, but rather part of the separating delimiters.</p>
<p><strong>Style recommendation:</strong> HED node names should start with a capital letter, with the remainder lower case. Words within the name should be separated by hyphens.</p></td>
  </tr>
  <tr>
     <td>HED labels and definition names</td>
     <td>The values substituted for # in the HED tags /Attribute/Informational/Label/# and Attribute/Informational/Definition/# can only contain upper and lower case letters, numbers, hyphens, underbars, or periods.
   </td>
  </tr>
  <tr>
     <td>HED element values</td>
     <td><p>Blanks are allowed as are periods, dollar($), percent(%), caret(^), plus(+), minus(-), underbar(_), and semicolon(;). Values must conform to the underlying unit classes of the placeholder specification.</p> <p>Certain unit classes allow other special characters in their value specification. These special characters are specified in the schema with the <em>allowedCharacter</em> attribute. Examples of this are the forward slash in the <em>fileType</em> unit class and the colon in the dateTime unit class.</p></td>
  </tr>
  <tr>
      <td>Library nicknames</td>
      <td>Can only be a single word containing alphabetic characters. The name must be followed by a single colon and then the remainder of the tag.</td>
  </tr>
</table>


Note: The **tilde syntax is no longer supported** for any version of HED and will generate a HED_INVALID_CHARACTER error.  Annotators should replace the syntax *(A ~ B ~ C)* with *(A, (B,C))*.


## B.2. HED validation errors 

**HED_CHARACTER_INVALID**: String contains an invalid character. HED uses ANSI encoding and does not support UTF-8. Different parts of a HED string have different rules for acceptable characters as outlined in the specification (Section C.1).

**HED_COMMA_MISSING**: HED tag groups must be separated from other HED tags and tag groups with commas. Commas missing between two HED tags are generally detected as invalid HED tags, rather than as missing commas.

**HED_DEF_UNMATCHED**: A *Def* tag cannot be correctly matched to a definition because the definition is missing or defined multiple times.

**HED_DEF_INVALID**: A _Def_ tag is incorrectly used, usually because of a mismatch between its *Definition* placeholder and *Def* tag value.  This error is detected if the *Definition* has a placeholder, but the *Def* is used without a value, or the *Definition* does not have a placeholder, but the *Def* is used with a value.

**HED_DEFINITION_INVALID**: The *Definition* syntax is incorrect or the *Definition* contains other *Def* or *Definition* tags.  Potential syntax errors include invalid definition names or a definition value that is not a single valid tag-group. Definitions that include a *#* placeholder must have exactly two *#* characters: one after the definition name and one in the definition body. Definitions that have too many *#* placeholders, not enough placeholders, or placeholders in the incorrect positions also generate this error.

**HED_GENERIC_ERROR**: The expression raised an error that did not fall into other categories.

**HED_GENERIC_WARNING**: The expression raised a warning that did not fall into other categories.

**HED_LIBRARY_UNMATCHED**: A tag that starts with *name:* is interpreted as a library schema nickname name. The association of *name* with an actual HED library schema must be passed to the validator when the string containing the tag is validated.

**HED_NODE_NAME_EMPTY**: A HED string cannot start or end with a slash, nor can a tag have consecutive slashes as all of these imply an empty tag node name within a HED tag.

**HED_ONSET_OFFSET_ERROR**: An *Onset* or *Offset* tag appears without being grouped with a defined name (using *Def*) with a tag-group containing a *Def-expand*. An *Offset* tag appears before an *Offset* tag of the same name.

**HED_PARENTHESES_MISMATCH**: The number of opening and closing parentheses in a HED string must be equal. 

**HED_PLACEHOLDER_INVALID**: A JSON sidecar with HED annotations cannot have a placeholder (*#*) in the tag dictionary for a categorical column and must have exactly one placeholder in the tag string for a value column. 

**HED_REQUIRED_TAG_MISSING**: A tag has the required attribute but is not present in the assembled event string.

**HED_SIDECAR_KEY_MISSING**: (WARNING) The annotation for a categorical value in the events file is missing, although its column has a HED dictionary in the JSON sidecar.

**HED_STYLE_WARNING**: (WARNING) A tag, tag extension, or label does not follow HED naming conventions. Tag names should start with a capital letter with the remainder lower case. Blanks are not allowed for HED-3G labels or tag extensions. Use hyphens instead.

**HED_TAG_EMPTY**: A HED string cannot have multiple consecutive commas (ignoring white space) without intervening non-empty HED tags. A HED string cannot begin or end with a comma, which also implies an empty HED tag. A tag group cannot be empty, so empty parentheses are not allowed.

**HED_TAG_EXTENDED**: (WARNING) Issued to warn annotators that this tag represents an extension of the HED schema. Often such tags were really spelling errors and not meant to extend the schema.

**HED_TAG_GROUP_ERROR:** A tag has `tagGroup` or `topLevelTagGroup` attribute but is not in an appropriate tag group or a `topLevelTagGroup` tag appears in the same tag group as other tags with the `topLevelTagGroup` attribute.

**HED_TAG_INVALID**: The tag is not valid in this schema, has incorrect format, or is used as a tag extension or placeholder value while appearing elsewhere in the schema. Note: an existing HED node cannot be used as a value or extension.

**HED_TAG_NOT_UNIQUE**: This event-level HED string has multiple occurrences of a tag with the *unique* schema attribute.

**HED_TAG_REPEATED**: HED tags or tag-group cannot be repeated in grouping. *(A, (A, B))* is not considered to be a duplicate, while  *(A, (B, C), A)* and *(A, (B, C), (C, B))* are repeated. HED strings are not ordered, so *(B, C)* is considered to be equivalent to *(B, C)*.

**HED_TAG_REQUIRES_CHILD**: A HED tag requires an additional ending node because its current ending node has the *requireChild* schema attribute.

**HED_TILDES_UNSUPPORTED**: The tilde notation is no longer supported. Replace *(A ~ B ~ C)* with *(A, (B, C))*. Replace *(A ~ B)* with *(A, B)*.

**HED_UNITS_DEFAULT_USED**: (WARNING) A HED tag value is missing units so the default units are used.

**HED_UNITS_INVALID**: The HED tag has a value with units that are invalid or not of the correct unit class for the tag. A typical mistake is to use unit modifiers with units that are not SI units.

**HED_VALUE_INVALID**: The value substituted for a placeholder (*#*) is not valid or compatible with the specified value class.

**HED_VALUE_IS_NODE**: An existing HED node name cannot be used as a value or extension. This is true for all HED schemas regardless of version.

**HED_VERSION_DEPRECATED**: (WARNING) The HED version is deprecated. It is strongly recommended that a current version be used as these deprecated versions may not be supported in the future.

**HED_VERSION_WARNING**: (WARNING) The HED version number or HED schema was not provided or was invalid, so the latest version is used.


## B.3. Summary of HED validation errors

Table C.2 Lists the validation errors checked for by the validator.


### **Table B.2.** Validation errors and warnings.

<table>
  <tr>
     <td><strong>Error or warning</strong></td>
     <td><strong>Explanation</strong></td>
  </tr>
  <tr>
     <td><code>HED_CHARACTER_INVALID</code></td>
     <td><code>String contains an invalid character.</code></td>
  </tr>
  <tr>
     <td><code>HED_COMMA_MISSING</code></td>
     <td>Comma missing, usually separating tag groups.</td>
  </tr>
  <tr>
      <td><code>HED_DEF_UNMATCHED</code></td>
      <td>A <em>Def</em> tag cannot be matched to definition.</td>
  </tr>
  <tr>
      <td><code>HED_DEF_INVALID</code></td>
      <td>A <em>Def</em>’s value is incorrect or does not match its <em>Definition</em>.</td>
  </tr>
  <tr>
     <td><code>HED_DEFINITION_INVALID</code></td>
     <td>A <em>Definition</em>’s syntax is invalid or definitions are nested.</td>
  </tr>
  <tr>
     <td><code>HED_GENERIC_ERROR</code></td>
     <td>HED expression raised an uncategorized error.</td>
  </tr>
  <tr>
     <td><code>HED_GENERIC_WARNING</code>*</td>
     <td>HED expression raised an uncategorized warning.</td>
  </tr>
  <tr>
     <td><code>HED_LIBRARY_UNMATCHED</code></td>
     <td>A tag starting with <em>name:</em> does not have an associated library.</td>
  </tr>
  <tr>
     <td><code>HED_NODE_NAME_EMPTY</code></td>
     <td>Extra slashes at beginning, end, or within a tag imply empty node names.</td>
  </tr>
  <tr>
     <td><code>HED_ONSET_OFFSET_ERROR</code></td>
     <td>Unnamed or unmatched <em>Onset</em> or <em>Offset</em> tag.</td>
  </tr>
  <tr>
     <td><code>HED_PARENTHESES_MISMATCH</code></td>
     <td>HED string has mismatched parentheses.</td>
  </tr>
  <tr>
     <td><code>HED_PLACEHOLDER_INVALID</code></td>
     <td>A <em>#</em> is missing or appears in a place that it should not.</td>
  </tr>
  <tr>
     <td><code>HED_REQUIRED_TAG_MISSING</code></td>
     <td>Event annotation missing a required tag.</td>
  </tr>
  <tr>
     <td><code>HED_SIDECAR_KEY_MISSING</code>*</td>
     <td>A categorical value is missing HED tags.</td>
  </tr>
  <tr>
     <td><code>HED_STYLE_WARNING</code>*</td>
     <td>Extension or label does not follow HED naming conventions.</td>
  </tr>
  <tr>
      <td><code>HED_TAG_EMPTY</code></td>
      <td>Extra commas or empty parentheses indicate empty tags.</td>
  </tr>
  <tr>
      <td><code>HED_TAG_EXTENDED</code>*</td>
      <td>HED tag represents an extension from the schema.</td>
  </tr>
  <tr>
      <td><code>HED_TAG_GROUP_ERROR</code></td>
      <td>A tag has <code><em>tagGroup</em></code> or <code><em>topLevelTagGroup</em></code> attribute but is not in an appropriate tag group or a <em>topLevelTagGroup</em> tag appears in the same tag group as other tags with the <em>topLevelTagGroup</em> attribute.</td>
  </tr>
  <tr>
     <td><code>HED_TAG_INVALID</code></td>
     <td>HED tag has incorrect format, does not exist in schema, or is a tag extension that appears elsewhere in the schema.</td>
  </tr>
  <tr>
     <td><code>HED_TAG_NOT_UNIQUE</code></td>
     <td>HED tag with <em>unique</em> attribute appears more than once.</td>
  </tr>
  <tr>
     <td><code>HED_TAG_REPEATED</code></td>
     <td>Tags cannot be repeated in the same tag group or level.</td>
  </tr>
  <tr>
     <td><code>HED_TAG_REQUIRES_CHILD</code></td>
     <td>HED tag requires an additional ending node.</td>
  </tr>
  <tr>
     <td><code>HED_TILDES_UNSUPPORTED</code></td>
     <td>Replace <em>(a ~ b ~ c)</em> with <em>(a, (b, c))</em>.</td>
  </tr>
  <tr>
     <td><code>HED_UNITS_DEFAULT_USED</code>*</td>
     <td>HED tag value has a unit class but no units are specified. Default units are used if available.</td>
  </tr>
  <tr>
     <td><code>HED_UNITS_INVALID</code></td>
     <td>HED tag value has incorrect or invalid units.</td>
  </tr>
  <tr>
     <td><code>HED_VALUE_INVALID</code></td>
     <td>The value substituted for a placeholder is invalid.</td>
  </tr>
  <tr>
     <td><code>HED_VERSION_DEPRECATED</code>*</td>
     <td>The HED version used has been deprecated and may not be supported in the future.</td>
  <tr>
     <td><code>HED_VERSION_WARNING</code>*</td>
     <td>The HED version is not provided, so the latest is used.</td>
  </tr>
</table>

_*_ Indicates a warning
