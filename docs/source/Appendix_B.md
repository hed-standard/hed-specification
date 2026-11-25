# B. HED errors

This appendix summarizes the error codes used by HED validators and other tools.

A code marked with a star (`*`) is a warning. A warning reports something that an annotator or a schema developer should look at; it does not make the annotation or the schema invalid, and a tool MAY let the user suppress warnings. Every other code is an error.

HED-compliant tools may assume that it if a HED annotation has been properly validated, it will comply with the rules of the HED specification. Annotators and analysts are mainly concerned with HED validation errors relating to incorrectly annotated events. See [B.1: HED validation errors](#b1-hed-validation-errors) for a listing of errors keyed to the HED specification.

HED-compliant tools assume that the HED schemas available on the [hed-standard/hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository are error-free, and that schema errors can only occur due to failure to locate or read a HED schema.

HED schema developers are mainly concerned with errors and inconsistencies in the schema itself. Schemas under development should be validated at all stages of development. See [B.2: Schema validation errors](#b2-schema-validation-errors) for a listing of errors keyed to the HED specification. Rules that a validator applies differently to an earlier schema version are listed in [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).

## B.1. HED validation errors

### CHARACTER_INVALID

**a.** A HED string cannot contain the following characters:

- Character code \<= 31 (hex 0x1f).
- 127 (hex 0x7f) \<= character code \<= 159 (hex 0x9f).
- Left or right square brackets (`[`, `]`).
- Tilde (`~`) character. Replace: the syntax (`A` ~ `B` ~ `C`) with (`A`, (`B`, `C`)).
- Double quotes (`"`).

**b.** Curly braces (`{`, `}`) appear in a HED string that is not a sidecar annotation, such as a cell in the `HED` column of a table. Curly braces indicate a column reference in a sidecar and are not HED.

**Notes:**

1. Different parts of a HED string have different rules for acceptable characters. For example tag names must satisfy the rules for the HED name class. The values used after tag names depend on the value classes of the tag and the unit classes of the tag.
2. A textClass value containing a parenthesis, number sign, or tilde is CHARACTER_INVALID under the value class. For earlier schema versions see [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).
3. The character sets named here and in [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions) are published as [`character_sets.json`](_static/character_sets.json). A validator reporting this error names the character, its position, and the set it failed.

**See also:**

- [A.1. Auxiliary and extra schema sections](./Appendix_A.md#a1-auxiliary-and-extra-schema-sections) for a discussion of the HED name and unit class rules.
- [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions) for a discussion of the restrictions on characters.
- [3.2.4. Tags that take values](03_HED_formats.md#324-tags-that-take-values) and [3.2.5. Tag extensions](03_HED_formats.md#325-tag-extensions) for an explanation of the rules for tag values and extensions.

### COMMA_MISSING

HED tag groups and tags must be separated with commas. In the following `A`, `B`, `C`, and `D` represent HED expressions.

**a.** Two tag groups are not separated by commas: (`A`, `B`)(`C`, `D`).\
**b.** A tag and a tag group are not separated by commas: `A`(`B`,`D`).

**Note:** Commas missing between two HED tags are generally detected as invalid HED tags, rather than as missing commas.

See [3.2.7.3. Empty tags and groups](./03_HED_formats.md#3273-empty-tags-and-groups) for an explanation of the rules for empty tags.

See also [TAG_EMPTY](./Appendix_B.md#tag_empty).

### DEF_EXPAND_INVALID

**a.** A `Def-expand` tag's name does not correspond to a definition.\
**b.** A `Def-expand` is missing an expected placeholder value or has an unexpected placeholder value.\
**c.** A `Def-expand` has a placeholder value of incorrect format or units for definition.\
**d.** The tags within a `Def-expand` do not match the corresponding definition.\
**e.** A `Def-expand` tag group of a definition that has contents is missing its inner tag group.\
**f.** A `Def-expand` tag group has extra tags or groups.

See [3.2.8.2. The Def and Def-expand tags](./03_HED_formats.md#3282-def-and-def-expand-tags) for an explanation of the rules for `Def-expand` and [5.2. Using definition](./05_Advanced_annotation.md#52-using-definitions) for more details and examples.

### DEF_INVALID

**a.** A `Def` tag's name does not correspond to a definition.\
**b.** A `Def` tag is missing an expected placeholder value or has an unexpected placeholder value.\
**c.** A `Def` has a placeholder value of incorrect format or units for definition.

See [3.2.8.2. The Def and Def-expand tags](./03_HED_formats.md#3282-def-and-def-expand-tags) for an explanation of the rules for `Def` and [5.2. Using definition](./05_Advanced_annotation.md#52-using-definitions) for more details and examples.

### DEFINITION_INVALID

A **definition** is a tag group containing a `Definition` tag and at most one inner tag group, which holds the definition's contents. A definition without a placeholder may omit the inner group, for example when it serves only as an anchor.

**a.** A `Definition` tag does not appear in a tag group at the top level in an annotation.\
**b.** No longer used: an empty inner group in a definition is [TAG_EMPTY](#tag_empty) (c) from specification `4.0.0`.\
**c.** A definition's enclosing tag group contains more than a `Definition` tag and an inner group.\
**d.** A definition's contents contain, at any level, a structural reserved tag (`Definition`, `Def`, `Def-expand`, `Onset`, `Offset`, `Inset`, `Delay`, `Duration`, `Event-context`), in every schema version.\
**e.** A definition uses curly braces.\
**f.** A definition that includes a placeholder (`#`) does not have exactly two `#` characters.\
**g.** A definition has placeholders (`#`) in incorrect positions.\
**h.** Definitions of the same name appear with and without a `#`.\
**i.** Two definitions with the same name have different contents. Identical definitions of one name (the same placeholder form and the same contents in any order, under the case rule of [3.2.3. Tag case-sensitivity](./03_HED_formats.md#323-tag-case-sensitivity)) are allowed and treated as one definition.\
**j.** A tag with the `unique` attribute appears in a definition.\
**k.** A definition appears in an unexpected place such as a table or a sidecar dictionary that contains non-definition entries.\
**l.** The value of a `Definition` tag has a part after the name other than a single `#` (`Definition/MyDef/3`, `Definition/MyDef/#/#`).

See [3.2.8.1. The Definition tag](./03_HED_formats.md#3281-the-definition-tag) for an explanation of the rules for definitions. See also [5.1. Creating definitions](./05_Advanced_annotation.md#51-creating-definitions) and [5.2. Using definitions](./05_Advanced_annotation.md#52-using-definitions) for more details and examples of definition syntax.

### ELEMENT_DEPRECATED\*

(WARNING)

A schema element has been deprecated and should not be used. When an element is updated, its description is updated to include the reason for deprecation and a suggested path for updating usage.

**a.** A tag has been deprecated and an alternative method of tagging should be used. See tag description for how to replace.\
**b.** A unit or unit modifier has been deprecated and an alternative should be used.

See [3.2. Annotation rules](./03_HED_formats.md#32-annotation-rules) for the rule and [A.1.4.5. deprecatedFrom](./Appendix_A.md#a145-deprecatedfrom) for additional information about the `deprecatedFrom` schema attribute.

### ONSETS_UNORDERED\*

(WARNING)

**a.** The rows of a timeline table are not in time order: the time of a row is earlier than the time of a row above it. Rows whose `onset` value is `n/a` are not considered. The warning is reported once for the table.

See [3.2.10.4. Table-level processing](./03_HED_formats.md#32104-table-level-processing) for the rule.

### PARENTHESES_MISMATCH

**a.** A HED string does not have the same number of open and closed parentheses.\
**b.** The open and closed parentheses are not correctly nested in the HED string.

See [3.2.7.1. Parentheses and order](./03_HED_formats.md#3271-parenthesis-and-order) for the rules for parentheses in HED.

### PLACEHOLDER_INVALID

**a.** A `#` appears in a place that it should not (such as in the `HED` column of a table).\
**b.** A JSON sidecar has a placeholder (`#`) in the HED dictionary for a categorical column.\
**c.** A JSON sidecar does not have exactly one placeholder (`#`) in each HED string representing a value column.\
**d.** A placeholder (`#`) is used in JSON sidecar or definition, but its parent in the schema does not have a placeholder child, or its parent is a user extension (`Item/Blech/#`).\
**e.** Multiple placeholders (`#`) appear in a HED string (e.g., `"Label/#, Parameter-value/#"`).\
**f.** A placeholder (`#`) is not the whole value of its tag, or of the second part of a `Definition`, `Def` or `Def-expand` value (e.g., `"Label/x#"`, `"Label/#x"`, `"Def/MyDef/x#"`).

**Notes:** A `#` directly after a reserved tag that takes no value (`Onset/#`) is an error in every context, which a validator may report either as PLACEHOLDER_INVALID (reason **a** or **d**) or as [TAG_EXTENSION_INVALID](#tag_extension_invalid) (reason **c**), depending on which check finds it first. Units after the placeholder (`"Frequency/# Hz"`) are not part of its value. A validator may report a `#` with other characters in the value (reason **f**) as [VALUE_INVALID](#value_invalid) or [CHARACTER_INVALID](#character_invalid) instead, depending on which check finds it first. Reason **f** is stated in this form from specification `4.0.0`.

See [3.2.4. Tags that take values](./03_HED_formats.md#324-tags-that-take-values) and [3.2.9.1. Sidecar entries](./03_HED_formats.md#3291-sidecar-entries) for information on the use of placeholders in HED.

### REQUIRED_TAG_MISSING

**a.** An event-level annotation does not have a tag corresponding to a node with the `required` schema attribute. Only standard schemas < `8.3.0` and the unpartnered library schema SCORE `1.0.0` define this attribute; see [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).

### SCHEMA_LOAD_FAILED

**a.** Different standard schema partner versions in a merge group.\
**b.** Schema elements (tag, unit class, unit, unit modifier, or value class) or schema attributes of two library schemas in the same merge group have the same name but have conflicting attributes, description, parents, or placeholder (`#`) children.\
**c.** The same schema (a library schema with the same library name, or the standard schema) is listed more than once in a merge group, in the same or in different versions.\
**d.** A schema with a specified name and version cannot be found.\
**e.** Rows of the `Sources`, `Prefixes`, or `External annotations` section of two library schemas in the same merge group have the same key but different contents.\
**f.** A schema file cannot be parsed in its format, and no code of [B.2.2. MediaWiki format errors](#b22-mediawiki-format-errors) or [B.2.3. XML format errors](#b23-xml-format-errors) applies. No code is specific to the JSON or TSV format.\
**g.** A version specification names a standard schema version earlier than `8.0.0` (see [3.1.1. Schema versions](./03_HED_formats.md#311-schema-versions)).\
**h.** A namespace name in a version specification is not made of ASCII letters only (see [3.1.1. Schema versions](./03_HED_formats.md#311-schema-versions)).

**Note:** Depending on the validator, a missing file or a file that cannot be parsed may be reported through a file error exception (e.g., a `HedFileError` exception in the Python tools) rather than as `SCHEMA_LOAD_FAILED`.

**Note:** Partnered library schemas never define schema properties: the `Properties` section of an unmerged partnered library schema is empty and that of a merged partnered library schema is the `Properties` section of its standard schema partner, so conflicts with the standard partner are detected when the schema itself is validated. See reason **j** and **k** of [SCHEMA_LIBRARY_INVALID](#schema_library_invalid).

A version specification that violates any rule of the rule table in [3.1.2.4. Partnered combinations](./03_HED_formats.md#3124-partnered-combinations) is this error, including an unpartnered library schema that shares its namespace with another schema.

See [3.1.2.4. Partnered combinations](./03_HED_formats.md#3124-partnered-combinations) for the rule table and [7.3.6. Lazy partnering](./07_Library_schemas.md#736-lazy-partnering) for a description of the merging process.

### SIDECAR_BRACES_INVALID

**a.** A name appearing in curly braces in a sidecar HED annotation is not the word `HED` or the name of a HED-annotated column in the sidecar.\
**b.** A column name entry in a sidecar has a HED annotation with curly braces, but this name also appears in curly braces in another HED annotation.\
**c.** The curly braces in a sidecar are nested or unmatched.\
**d.** The curly braces appear as the substitution for a placeholder in another tag.

See [3.2.9. Sidecars](./03_HED_formats.md#329-sidecars) for information on the requirements for using sidecars.

### SIDECAR_INVALID

**a.** The `"HED"` key is not a second-level dictionary key.\
**b.** An annotation entry is provided for `n/a`.\
**c.** No longer used: a sidecar that refers in curly braces to a column with no HED is [SIDECAR_BRACES_INVALID](#sidecar_braces_invalid) (a) from specification `4.0.0`.\
**d.** A top-level sidecar key begins or ends with whitespace (blank, tab, line feed, or carriage return), whether or not its entry has a `"HED"` key.\
**e.** In a categorical entry, a column value listed as a key under `"HED"` begins or ends with whitespace (blank, tab, line feed, or carriage return), such as `"go "` in `{"trial": {"HED": {"go ": "Sensory-event"}}}`.\
**f.** An annotation in a categorical entry is empty or consists only of blanks. A column value that has no HED annotation is given the annotation `n/a`.

For (e) only the keys under `"HED"` in a categorical entry are checked: the column values that the entry annotates. The top-level key (`trial`, the column name) is (d), and the keys of other dictionaries in the entry, such as a BIDS `Levels` dictionary, are not checked. A column value is matched to these keys exactly, so a key with whitespace could only match a column value with whitespace, which is itself TABULAR_INVALID (d), and could never annotate a row. Both (d) and (e) are stated from specification `4.0.0`.

See [3.2.9. Sidecars](./03_HED_formats.md#329-sidecars) for a general explanation of sidecar requirements.

### SIDECAR_KEY_MISSING\*

(WARNING)

**a.** A value in a categorical column does not have an expected entry in a sidecar.\
**b.** A \{ref} in a sidecar does not correspond to a column in the associated table.

**Note:** This warning is only triggered if the categorical column in which the value appears does have HED annotations.

See [3.2.9. Sidecars](./03_HED_formats.md#329-sidecars) for a general explanation of sidecar requirements.

### TABULAR_INVALID

**a.** A column name appears more than once in the first line (the column names) of a tabular file.\
**b.** A column name in the first line of a tabular file begins or ends with whitespace (blank, tab, line feed, or carriage return).\
**c.** A column name in the first line of a tabular file is blank (the empty string).\
**d.** A value in a column with categorical or value HED annotations begins or ends with whitespace (blank, tab, line feed, or carriage return).\
**e.** A line other than the first of a tabular file is empty (has no characters before its line terminator).\
**f.** A line other than the first of a tabular file has a different number of tab-separated cells than the first line.

For (a) the error names each repeated column, and the repeated columns are not renamed, merged, or dropped: assembling the row annotations of such a file would combine the annotations of the repeated columns into one row and report the result as TAG_EXPRESSION_REPEATED, or lose one of them. For (a) names are compared exactly as written, so two names that differ only in leading or trailing whitespace (`trial` and `trial `) are not a repeat; the name with the whitespace is (b). For (b) the error is reported once for each column name with leading or trailing whitespace; a name that is both padded and repeated (`trial ` twice) is reported under (b) only. For (c) the error is reported once for each blank name, by its column position; several blank names are reported under (c) only, not as a repeat under (a), and a name made only of whitespace is (b), not (c). Reasons (a), (b), (c), (e), and (f) are reported before any row annotation is assembled. When (e) or (f) is found, the rows of the file are then not validated: no row is checked for (d) or for any other error.

For (d) the error is reported once for each distinct value with leading or trailing whitespace in each such column, at the first row that holds it, column by column before the values are checked against their annotations (VALUE_INVALID, UNITS_INVALID, SIDECAR_KEY_MISSING) and before any row annotation is assembled. A value made only of whitespace, and `n/a` with whitespace before or after it, are (d); an empty value and `n/a` are missing values. Values are compared and substituted exactly as written, so (d) is the error for `go ` in a column whose annotation has the key `go`, not SIDECAR_KEY_MISSING. The `HED` column and columns without HED annotations are not checked. Reason (d) is stated from specification `4.0.0`.

For (e) and (f) every offending line is reported, by its line number in the file, counting from 1 with the column-name line as line 1. For (f) the error also gives the number of tab-separated cells in the line and the number expected (the number of cells in the first line). An empty line is reported under (e) only, not also under (f). A single line ending at the end of the file is not an empty line; two line endings at the end of the file make an empty last line, which is (e). An empty first line is a blank column name, which is (c), not (e). A line made only of tabs that has as many cells as the first line is a row of missing values and is not an error. A line made only of blanks is (f) unless the table has one column; in a table with one column it is a value made only of whitespace, which is (d) if the column has categorical or value HED annotations. Reasons (e) and (f) are stated from specification `4.0.0`, as BIDS also requires (BIDS TSV_EMPTY_LINE and TSV_EQUAL_ROWS).

Reasons (a), (b), and (c) apply to the column names of every HED-annotated table whose columns have names, however the table stores them (the header row of a `.tsv` file or spreadsheet, or the column names an NWB table stores with its columns), as 3.2.10 states, including a spreadsheet whose columns a tool refers to by number, and they apply to the names under which the columns are assembled: in NWB the `TimestampVectorData` column named `timestamp` counts as `onset`, so a table that also has a column named `onset` is (a). Other `TimestampVectorData` columns keep their own names. Reasons (e) and (f) apply only to text tabular files (`.tsv`), not to spreadsheets or NWB tables.

See [3.2.10. Tabular files and structures](./03_HED_formats.md#3210-tabular-files-and-structures) for the requirements on tabular files.

### TAG_EMPTY

**a.** A HED string has extra commas or parentheses separated by only white space, indicating empty tags.\
**b.** A HED string begins or ends with a comma (ignoring white space), indicating an empty string.\
**c.** A tag group is empty (i.e., empty parentheses are not allowed).

**Note:** Some of these errors MAY instead be reported as [COMMA_MISSING](#comma_missing).

See [3.2.7.3. Empty tags and groups](./03_HED_formats.md#3273-empty-tags-and-groups) for the rules on empty tags and groups.

### TAG_EXPRESSION_REPEATED

**a.** A tag is repeated in the same tag group or level.

Suppose `A`, `B`, and `C` represent HED expressions. HED strings are not ordered, so (`B`, `C`) is equivalent to (`C`, `B`). Thus, (`A`, (`A`, `B`)) is not a duplicate, but (`A`, (`B`, `C`), `A`) and (`A`, (`B`, `C`), (`C`, `B`)) are duplicates.

**Note:** In a table, a repetition can also come from the assembly of a row's annotation rather than from any single annotation, for example two columns whose annotations contain the same tag. In a sidecar, a repetition can also come from a substitution of a curly-brace reference, including the removal of a reference whose column is `n/a` or blank, so `(Red, {HED}), (Red)` is this error (rule 10 of [3.2.9.3. Sidecar curly braces](./03_HED_formats.md#3293-sidecar-curly-braces)). A column name that appears twice in the first line of the file is [TABULAR_INVALID](#tabular_invalid), not this error.

See [3.2.7.4. Repeated expressions](./03_HED_formats.md#3274-repeated-expressions) for additional information on the rules for duplication.

### TAG_EXTENDED\*

(WARNING)

**a.** A tag represents an extension from the schema.

**Note:** Often such extensions are really spelling errors and not meant to extend the schema.

**Note:** Annotators are discouraged from extending the schema unless absolutely necessary. If an extension tag is needed, annotators should consider posting an [issue](https://github.com/hed-standard/hed-schemas/issues) explaining the tag extension so that an addition to the respective schema might be considered.

See [3.2.5 Tag extensions](./03_HED_formats.md#325-tag-extensions) for additional information on the tag extension rules.

### TAG_EXTENSION_INVALID

**a.** A tag extension term is already in the schema.\
**b.** A tag extension term does not comply with rules for schema nodes, or contains no letter (`Item/Blech/3`).\
**c.** A tag has extension, but an extension is not allowed. This includes an extension of a reserved tag (`Onset/Blah`), although reserved tags inherit `extensionAllowed`; a `#` after a reserved tag that takes no value (`Onset/#`) may be reported here or as [PLACEHOLDER_INVALID](#placeholder_invalid); see [3.2.5 Tag extensions](./03_HED_formats.md#325-tag-extensions).

See [3.2.5 Tag extensions](./03_HED_formats.md#325-tag-extensions) for additional information on the tag extension rules.

### TAG_GROUP_ERROR

**a.** A tag has `tagGroup` or `topLevelTagGroup` attribute, but is not enclosed in parentheses.\
**b.** A tag with the `topLevelTagGroup` does not appear at a HED tag group at the top level in an assembled HED annotation.\
**c.** Multiple tags with the `topLevelTagGroup` attribute appear in the same top-level tag group. Note: a single `Delay` may be in the same group as a single `Duration`, `Onset`, `Offset`, or `Inset`.\
**d.** An `Event-context` group contains a tag other than `Event-context` that is not inside a tag group.\
**e.** An `Event-context` group contains a curly brace column reference (`{column}`).

**Note:** For the structural reserved tags of [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags), a violation of a group rule is reported with the tag's own code ([DEFINITION_INVALID](#definition_invalid), [TEMPORAL_TAG_ERROR](#temporal_tag_error)). A tag that is not in a group (a), not in a top-level group (b), or in a group with a tag not allowed beside it (c) MAY instead be reported as TAG_GROUP_ERROR. For example, `(Onset, Def/MyDef, Red)` MAY be reported as TAG_GROUP_ERROR.

See [3.2.7.2. Tag group attributes](./03_HED_formats.md#3272-tag-group-attributes) for additional information on the rules for group errors due to schema attributes.

**See also:** [TEMPORAL_TAG_ERROR](#temporal_tag_error) for errors involving `Onset`, `Offset`, `Inset`, `Duration` and `Delay`.

### TAG_INVALID

**a.** The tag is not valid in the schema it is associated with.\
**b.** The tag has extra internal whitespace, including directly before or after a forward slash of the tag path or the slash that begins a value (`Event/ Sensory-event`, `Label/ abc`, `Label/ #`); see [3.2.2. Tag forms](./03_HED_formats.md#322-tag-forms). Blanks inside a value, after its first character, including blanks next to a slash inside the value (`Description/left / right`), are judged by the rules for the value ([VALUE_INVALID](#value_invalid), [CHARACTER_INVALID](#character_invalid)), not by this reason.\
**c.** The tag has a leading, trailing, or consecutive forward slashes.\
**d.** A tag or tag extension contains a non `name` character.

See [3.2.2. Tag forms](./03_HED_formats.md#322-tag-forms) for a discussion of tag forms and their relationship to the HED schema.

### TAG_NAMESPACE_PREFIX_INVALID

**a.** A namespace prefix has invalid characters.\
**b.** A tag has a namespace prefix that is not defined: no schema in the HED version specification is associated with that namespace.

See [3.2.6. Tag namespace prefixes](./03_HED_formats.md#326-tag-namespace-prefixes) and [7. Library schema](./07_Library_schemas.md) for additional information on using multiple schemas in annotation.

### TAG_NOT_UNIQUE

**a.** A tag with `unique` attribute appears more than once in an event-level HED string.

See [3.2.10.3. Event-level processing](./03_HED_formats.md#32103-event-level-processing) for additional information on the `unique` tag.

### TAG_REQUIRES_CHILD

**a.** A tag has the `requireChild` schema attribute but does not have a child.\
**b.** A structural reserved tag whose `requireValue` is true in `reserved_tags.json` (see [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags)) has no value.

See [A.1.4.11. requireChild](./Appendix_A.md#a1411-requirechild) for an explanation of the `requireChild` attribute.

### TEMPORAL_TAG_ERROR

Note: For the purpose of `Onset`/`Offset` matching, `Def` or `Def-expand` tags with different placeholder substitutions are considered to be different.

**a.** An `Offset`, `Onset`, `Inset`, `Duration`, or `Delay` tag does not appear in a tag group.\
**b.** An `Offset`, `Onset`, `Inset`, `Duration`, or `Delay` tag appears in a nested tag group (not a top-level tag group).\
**c.** An `Onset`, `Offset` or `Inset` tag is not grouped with exactly one `Def` tag or `Def-expand` group.\
**d.** An `Onset`, `Inset`, or `Offset` group contains too many inner tag groups (more than the Max groups of [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags)).\
**e.** An `Offset` group contains top-level tags besides its anchor and an optional `Delay` tag.\
**f.** An `Offset` tag appears before an `Onset` tag associated with the same definition.\
**g.** An `Offset` tag associated with a given definition appears after a previous `Offset` tag without the appearance of an intervening `Onset` of the same name.\
**h.** An `Onset` or an `Inset` tag group has tags besides the anchor `Def` tag or `Def-expand` group and an optional `Delay` tag that are not in a tag group.\
**i.** An `Onset`, `Offset`, or `Inset` group occurs at the same time as another `Onset`, `Offset`, or `Inset` group with the same anchor.\
**j.** An `Inset` tag is not grouped with a `Def` tag or a `Def-expand` group corresponding to an ongoing `Onset`.\
**k.** An `Onset`, `Inset`, `Offset`, or `Delay` tag appears in an annotation for a table without an `onset` or equivalent column.\
**l.** A `Duration` or `Delay` tag group contains extra tags or groups, or is missing the required group. A `Delay` group that does not contain `Onset`, `Offset`, or `Inset` MUST have exactly one inner group, so `(Delay/2 s)` alone is an error.\
**m.** An `Offset`, `Onset`, `Inset`, `Duration`, or `Delay` tag appears with other top-level tags, except that a `Delay` MAY be paired with a `Duration`, `Onset`, `Offset`, or `Inset`.\
**n.** In a timeline table (a table with an `onset` or equivalent column), a `Duration` or `Delay` tag has a value that cannot be converted to the default units of its unit class (non-numeric value, invalid units, or units with no `conversionFactor`, such as `month` or `year`), so the delayed onset (`Delay`) or the end time (`Duration`) cannot be placed on the table's timeline. A `Duration` tag in a descriptor table MAY use any valid unit of its unit class. For earlier schema versions see [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).\
**o.** An `Onset`, `Offset`, `Inset`, or `Delay` tag appears in a row of a timeline table whose `onset` value is `n/a`. A `Duration` tag MAY appear in such a row.

**See also:** [TAG_GROUP_ERROR](#tag_group_error).

See [3.2.8.3 Onset, Offset, and Inset](./03_HED_formats.md#3283-onset-offset-and-inset) for a specification of the required behavior of the `Onset`, `Offset`, and `Inset` tags.

[5.3.1. Using Onset and Offset](./05_Advanced_annotation.md#531-using-onset-and-offset) in Chapter 5 gives examples of usage and additional details.

### UNITS_INVALID

**a.** A tag has a value with units that are invalid or not of the correct unit class for the tag.\
**b.** A unit modifier is applied to units that are not SI units.\
**c.** A component of a compound unit (`m-per-s`, `m^3`) is not a schema unit symbol, differs in case from it, or carries more than one SI unit modifier (`kmm-per-s`, `m-per-sec`, `m-per-S`).

See [3.2.4 Tags that take values](./03_HED_formats.md#324-tags-that-take-values) for more information.

### VALUE_INVALID

**a.** The value substituted for a placeholder (`#`) is not valid.\
**b.** A tag value is incompatible with the specified value class.\
**c.** A tag value with no value class is assumed to be textClass and contains invalid characters.\
**d.** The units are not separated from the value by a single blank. More than one blank (`Duration/3  ms`) MAY instead be reported as [UNITS_INVALID](#units_invalid).\
**e.** A value in a table column annotated by a sidecar value entry is invalid, in any row whose value is not `n/a` or blank, including rows whose assembled annotation does not use the column. Depending on the order of validation, such a value MAY instead be reported as [UNITS_INVALID](#units_invalid) or [CHARACTER_INVALID](#character_invalid).

See [3.2.4 Tags that take values](./03_HED_formats.md) for more information.

(b-2-schema-validation-errors)=

## B.2. Schema validation errors

This section is organized by the type of schema format that results in the error. Errors that might be detected regardless of the schema format start with `SCHEMA_`. Errors that are specific to the `.mediawiki` format start with `WIKI_`. Errors that occur in the construction of the XML version or that are detected by XML validators when the planned XSD validation is implemented start with `XML_`.

### B.2.1. General validation errors

#### SCHEMA_ANNOTATION_INVALID\*

(WARNING)

**a.** An `annotation` value uses a prefix that is not a row of the Prefixes section.\
**b.** The `prefix:id` of an `annotation` value is not a row of the External annotations section. A bare external term such as `glotto:afro1255` falls here; write `skos:exactMatch glotto:afro1255`.\
**c.** A `dc:source` value names no row of the Sources section: it neither begins with a row's `source` name nor contains a URL under a row's `link`.\
**d.** A value in prefix notation (`prefix:term`) has a prefix that is not a row of the Prefixes section, or the value of a SKOS mapping property (`skos:exactMatch`, `skos:closeMatch`) is not in prefix notation at all (`skos:exactMatch C25499`, `skos:exactMatch https://example.org/C25499`).

The Prefixes, External annotations, and Sources rows of a partnered library's standard schema count as the library's own. For earlier schema versions see [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).

See [A.1.4.2. annotation](./Appendix_A.md#a142-annotation) for the form of an `annotation` value and [A.1.6. Schema sources](./Appendix_A.md#a16-schema-sources) for what a `dc:source` value must name.

#### SCHEMA_ATTRIBUTE_INVALID

**a.** An attribute is used in the schema, but is not defined in the schema attribute section.\
**b.** A schema attribute is applied to the incorrect type (e.g., the `SIUnit` attribute, whose domain is units, appears on a tag).\
**c.** A schema attribute is used in an invalid way\
**d.** The pseudo unit class `anyUnits` lists a unit or has `defaultUnits`.\
**e.** A schema property is used in the schema, but is not defined in the schema properties section.

| Attribute        | Invalid Usage Location                                    |
| ---------------- | --------------------------------------------------------- |
| `deprecatedFrom` | See [SCHEMA_DEPRECATION_ERROR](#schema_deprecation_error) |
| `rooted`         | See [SCHEMA_LIBRARY_INVALID](#schema_library_invalid)     |
| `takesValue`     | Used on a non-placeholder(#) node.                        |
| `unitClass`      | Used on a non-placeholder(#) node.                        |
| `valueClass`     | Used on a non-placeholder(#) node.                        |

**Notes:**

- A `tag` or a `#` placeholder (the nodes of the schema) can have schema attributes that have the `tagDomain` or the `elementDomain` property or have no domain property.
- A `unitClass` element can only have schema attributes that have the `unitClassDomain` or the `elementDomain` property.
- A `unitModifier` element can only have schema attributes that have the `unitModifierDomain` or the `elementDomain` property.
- A `unit` element can only have schema attributes that have the `unitDomain` or the `elementDomain` property.
- A `valueClass` element can only have schema attributes that have the `valueClassDomain` or the `elementDomain` property.
- A schema attribute can only have schema attributes that have the `elementDomain` property.
- A schema property can only have the `hedId` attribute.

#### SCHEMA_ATTRIBUTE_VALUE_INVALID

**a.** A non-boolean schema attribute has an invalid value or usage as indicated by the following table.

| Attribute          | Invalid Attribute Value                                                                                                         |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `allowedCharacter` | Not a character set name or alias of [2.2](./02_Terminology.md#22-character-sets-and-restrictions), and not a single character. |
| `conversionFactor` | Not a positive numeric value.                                                                                                   |
| `defaultUnits`     | Not a unit, or a derived form of a unit, of this unit class.                                                                    |
| `deprecatedFrom`   | See [SCHEMA_DEPRECATION_ERROR](#schema_deprecation_error)                                                                       |
| `inLibrary`        | The value of an inLibrary attribute is for the wrong library.                                                                   |
| `relatedTag`       | Not an existing tag.                                                                                                            |
| `rooted`           | See [SCHEMA_LIBRARY_INVALID](#schema_library_invalid)                                                                           |
| `suggestedTag`     | Not an existing tag.                                                                                                            |
| `unitClass`        | Not an existing unit class, more than one, or `valueClass` not `numericClass`.                                                  |
| `valueClass`       | Not an existing value class.                                                                                                    |

For earlier schema versions, where the `valueClass` condition in the `unitClass` row is not checked, see [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).

#### SCHEMA_CHARACTER_INVALID

**a.** A non-placeholder schema node contains non-`name` characters.\
**b.** The name of a schema element other than a tag (unit class, unit, unit modifier, or value class), of a schema attribute, or of a schema property contains a character that is neither a `name` character nor, for a unit or unit modifier, one that it declares with `allowedCharacter`.\
**c.** A unit name or unit symbol contains a blank.\
**d.** The prologue or epilogue contains a character other than `text`, the comma, or newline.\
**e.** The description of a schema element, schema attribute, or schema property contains a character other than `text` or the comma.

The deprecated unit `degree Celsius` is the one exception to **b** and **c** (see [3.1.4.4. Unit classes and units](./03_HED_formats.md#3144-unit-classes-and-units)).

See [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions) for definitions of the different types of characters.

Note: tag extensions may contain `nonascii` characters.

#### SCHEMA_DEPRECATION_ERROR

**a.** The value of `deprecatedFrom` is not a previously released HED schema version.\
**b.** A deprecated tag is used as a `suggestedTag` or a `relatedTag` in a non-deprecated tag.\
**c.** A child tag of a deprecated tag does not have the `deprecatedFrom` attribute.\
**d.** A deprecated attribute is used on a non-deprecated element.\
**e.** No longer used: a schema property cannot be deprecated (specification `4.0.0`).\
**f.** A deprecated unit class has non-deprecated units.\
**g.** A tag has deprecated unit or value classes.\
**h.** A unit class has a deprecated default unit.

#### SCHEMA_DUPLICATE_NODE

**a.** A schema node name appears in the schema more than once.\
**b.** A unit class lists a unit that is an SI unit modifier applied to another unit of the same class (`uV` beside `V`). For earlier schema versions see [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).\
**c.** A unit string is derived by two unit classes (an SI unit modifier applied to a unit of each, or a plural) and listed by neither, so it would be ambiguous on a placeholder with `unitClass=anyUnits`. A string listed in one class and derived in another is not an error: the listed unit wins. See [3.1.4.4. Unit classes and units](./03_HED_formats.md#3144-unit-classes-and-units).

#### SCHEMA_HEADER_INVALID

**a.** The schema header has invalid characters or format.\
**b.** The schema header has unrecognized attributes.

#### SCHEMA_LIBRARY_INVALID

Library schema errors are specific to library schema. Library schema may also raise any of the other schema errors.\
**a.** The specified library name is not alphabetic or lowercase.\
**b.** The `withStandard` attribute is used in a header that does not also have the `library` attribute.\
**c.** The `withStandard` attribute value does not correspond to a valid standard schema version, or names a version earlier than `8.2.0` (see [3.1.2.1. Partnered vs unpartnered](./03_HED_formats.md#3121-partnered-vs-unpartnered)).\
**d.** The `rooted` attribute appears in a schema whose header does not have both the `library` and `withStandard` attributes.\
**e.** In an unmerged schema, a node with the `rooted` attribute is not at the top level; in a merged schema, a node with `rooted=XXX` is not a direct child of `XXX`.\
**f.** A node with the `rooted` attribute does not correspond to a node in its partnered standard schema.\
**g.** A partnered library schema with the `unmerged="true"` header attribute has an `inLibrary` attribute on some schema element or schema attribute or in a row of the extra sections.\
**h.** A partnered library schema with the `unmerged="true"` header attribute has a row of the extra sections (`Sources`, `Prefixes`, or `External annotations`) with the same key as a row of its standard schema partner.\
**i.** A partnered library schema with the `unmerged="true"` header attribute has a schema element (tag, unit, unit class, unit modifier, or value class) or a schema attribute with the same name as one of its standard schema partner. Naming an existing unit class solely to add new units under it is not a duplication.\
**j.** A partnered library schema with the `unmerged="true"` header attribute has a non-empty `Properties` section.\
**k.** A merged partnered library schema has a `Properties` section that differs from that of its standard schema partner.\
**l.** A library schema uses the `reserved` attribute on one of its own elements (in a merged partnered library schema, an element with the `inLibrary` attribute).\
**m.** A library schema defines, among its own elements (in a merged partnered library schema, those with the `inLibrary` attribute), a tag whose name is a reserved tag of a standard schema; the partner's reserved tags carried into a merged file are not affected. For an unmerged partnered library schema this is also reason i.\
**n.** A partnered library schema places a node under a reserved tag with the `rooted` attribute.

#### SCHEMA_MISSING_EXTRA\*

(WARNING)

**a.** A row of the Sources, Prefixes, or External annotations section has an empty value in a required column.

See [A.1.6. Schema sources](./Appendix_A.md#a16-schema-sources), [A.1.7. Schema prefixes](./Appendix_A.md#a17-schema-prefixes), and [A.1.8. External annotations](./Appendix_A.md#a18-external-annotations) for the columns of each section.

#### SCHEMA_RESERVED_INVALID

**a.** A standard schema does not define a tag that `reserved_tags.json` names, or defines it without the attributes the rules rely on: `reserved` and `topLevelTagGroup` for every row; `reserved` on `Def` and `Def-expand`; and `reserved` on the ten organizational reserved tags. For earlier schema versions see [B.3. Differences for earlier schema versions](#b3-differences-for-earlier-schema-versions).\
**b.** A reserved tag has a child node other than `#`.

See [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags) for the tags and [A.6. Reserved tags file](./Appendix_A.md#a6-reserved-tags-file) for the file.

#### SCHEMA_SECTION_MISSING

**a.** A required schema section is missing.\
**b.** The schema sections (corresponding to the prologue, schema, unit classes, unit modifiers, value classes, schema attributes, properties, epilogue, sources, prefixes, and external annotations) are not in the correct order and hence not detected.

**Note:** The sources, prefixes, and external annotations sections are required in every schema; a schema without them can still be loaded (see [3.1.4.10. Sources, prefixes, and external annotations](./03_HED_formats.md#31410-sources-prefixes-and-external-annotations)).

#### SCHEMA_VERSION_INVALID

**a.** The schema version in the HED line or element is invalid.\
**b.** A HED version specification does not have the correct syntax for the schema file format.\
**c.** A HED schema version does not comply with semantic versioning.

### B.2.2. MediaWiki format errors

#### WIKI_DELIMITERS_INVALID

**a.** Delimiters used in the wiki are invalid.\
**b.** Schema line content after node name is not enclosed with `<nowiki></nowiki>` delimiters.\
**c.** A line has unmatched or multiple `<nowiki></nowiki>`, `[ ]`, or `{ }` delimiters.\
**d.** Attributes section of a node is malformed(e.g., hanging `=` character).\
**e.** A comma-separated piece of a row of the Sources, Prefixes, or External annotations section that comes before the `description` pair is not a `name=value` pair. A comma in a value other than `description` has this effect.

See [A.2.5.7. Schema sources](./Appendix_A.md#a257-schema-sources) for how a row of these sections is split.

#### WIKI_LINE_START_INVALID

**a.** Start of body line not `'''` or `*`.

#### WIKI_SEPARATOR_INVALID

**a.** A malformed section separator is present\
**b.** A duplicate section separator is present.

### B.2.3. XML format errors

#### XML_SYNTAX_INVALID

**a.** XML syntax or does not comply with specified XSD.

### B.2.4. Schema loading errors

Schema loading errors can occur because the file is inaccessible or cannot be parsed in its format (MediaWiki, XML, JSON, or TSV); see reason **f** of [SCHEMA_LOAD_FAILED](#schema_load_failed). Schema loading errors are handled in different ways by the Python and JavaScript tools.

Python tools generally raise a `HedFileError` exception when a failure to load the schema occurs. The calling programs are responsible for deciding how to handle such a failure. The exception carries a code that says what failed. The code is `SCHEMA_LOAD_FAILED` when the schemas of a version specification cannot be combined; for a file that is missing or cannot be parsed it is a code of the Python tools that is not listed in this appendix.

JavaScript tools in contrast are mainly used for validation of HED annotations in data. These tools are mainly called by the [BIDS](https://bids.neuroimaging.io/) validator. If a **BIDS dataset uses HED**, it must provide a HED version specification in the `dataset_description.json` file. If the HED JavaScript validator cannot load a valid HED schema based on this specification it reports a `SCHEMA_LOAD_FAILED` issue.

## B.3. Differences for earlier schema versions

The rules of this specification are stated for the latest released standard schema, `8.5.0`, and the library schemas partnered with it. This section lists every rule that a validator applies differently to an earlier schema version. A rule not listed here applies unchanged to all schema versions >= `8.0.0`.

This paragraph covers the released unpartnered library schema, SCORE `1.0.0`; a new unpartnered library schema is not supported ([7.4.2. Unpartnered design rules](./07_Library_schemas.md#742-unpartnered-design-rules)). An unpartnered library schema has no standard schema version, so the entries below are applied to it as follows, whatever its own version. The entries on value class characters, on the `required` schema attribute, and on the names of the schema properties apply to it as they apply to a standard schema < `8.3.0`. The entries on the unit class of a placeholder, on derived units, and on the form of an `annotation` value do not apply to it: SCHEMA_ATTRIBUTE_VALUE_INVALID (a), SCHEMA_DUPLICATE_NODE (b), and SCHEMA_ANNOTATION_INVALID are reported for an unpartnered library schema as they are for standard schema `8.5.0`. The other entries concern reserved tags, which an unpartnered library schema does not have, and TSV files written for earlier standard schemas. SCORE `1.0.0` has the auxiliary sections of standard schema `8.1.0` and no TSV files.

**Annotation validation**

- Standard schemas < `8.3.0`: standard schemas mark the reserved tags with the `reserved` attribute only from `8.2.0` (the nine structural tags) and `8.3.0` (all nineteen); `8.0.0` and `8.1.0` carry no such attribute. The term reserved tag and the rules of 3.2.8 apply by tag name in every standard schema version, whether or not the schema marks the tag. See [Reserved tag](./02_Terminology.md#reserved-tag) and [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags).
- Standard schemas < `8.5.0` and library schemas partnered with them: the `allowedCharacter` names a standard value class declares do not define its characters, because these declarations predate the named sets; validators use the defaults recorded for each standard value class in the `value_class_defaults` section of [`character_sets.json`](_static/character_sets.json) (see [A.7.3. Names and value class defaults](./Appendix_A.md#a73-names-and-value-class-defaults)). `dateTimeClass` allows `digits`, `T`, `hyphen`, `colon`, `period`, `Z`, and `plus`, although these versions declare only the first four. `nameClass` allows `letters`, `digits`, `hyphen`, and `underscore`, and `nonascii` from standard schema `8.3.0`, although the released `8.3.0` and `8.4.0` rows omit it. `textClass` values use the `text` character set, not `value-text`; the `8.0.0` to `8.2.0` schemas enumerate `letters`, `digits`, `blank`, `+`, `-`, `:`, `;`, `.`, `/`, `(`, `)`, `?`, `*`, `%`, `$`, `@` (no underscore), and validators have always applied `text` there and still do. A textClass value containing a parenthesis, number sign, or tilde is therefore not CHARACTER_INVALID under the value class, but the substituted string is still parsed as HED, so tools report the structural error instead (PARENTHESES_MISMATCH, PLACEHOLDER_INVALID, or CHARACTER_INVALID for the tilde). See [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions), [A.1.3. Value classes](./Appendix_A.md#a13-value-classes), and [A.1.4.1. allowedCharacter](./Appendix_A.md#a141-allowedcharacter).
- Standard schemas < `8.3.0`: `Delay` and `Duration` do not carry the `requireChild` schema attribute (before `8.3.0`) or the `topLevelTagGroup` schema attribute (before `8.2.0`). The `requireValue`, `tagGroup`, and `topLevelTagGroup` fields of [`reserved_tags.json`](https://github.com/hed-standard/hed-specification/blob/main/docs/source/_static/reserved_tags.json) supply what these schemas lack, so the rules of 3.2.8 apply to every standard schema version >= `8.0.0`. A `Delay` or `Duration` tag with no value is TAG_REQUIRES_CHILD (b). See [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags) and [A.6.2. Tag fields](./Appendix_A.md#a62-tag-fields).
- Standard schema `8.0.0`, whose `timeUnits` units carry no `conversionFactor`: in a timeline table, a `Duration` or `Delay` value with no unit, or in the default unit written as its symbol `s` or as its name `second` or `seconds`, is taken as is; a value in a modified form (`ms`) or in any other unit is an error, TEMPORAL_TAG_ERROR (n). See [3.2.8.4. Duration and Delay](./03_HED_formats.md#3284-duration-and-delay).
- Standard schemas < `8.3.0`: these schemas define the `required` schema attribute. The assembled annotation of each row must include every tag whose schema node has it (REQUIRED_TAG_MISSING), and such a tag MUST NOT appear in the contents of a definition (DEFINITION_INVALID j). No released schema puts the attribute on a tag.

**Schema validation**

- Standard schemas < `8.5.0` and library schemas partnered with them: a unit class on a placeholder whose value class is not `numericClass`, or that has no value class, is not an error (`8.3.0` and earlier have `Sampling-rate/#` with a unit class and no value class), so the `valueClass` condition of the `unitClass` row of SCHEMA_ATTRIBUTE_VALUE_INVALID (a) is not checked. See [3.1.4.4. Unit classes and units](./03_HED_formats.md#3144-unit-classes-and-units) and [A.1.4.22. unitClass](./Appendix_A.md#a1422-unitclass).
- Standard schemas < `8.5.0` and library schemas partnered with them: a unit class may list a unit that can be formed by applying an SI unit modifier to another unit of the same class that has the `SIUnit` attribute; these schemas remain valid (`8.3.0` and `8.4.0` list `uV`), and SCHEMA_DUPLICATE_NODE (b) is not reported. See [3.1.4.4. Unit classes and units](./03_HED_formats.md#3144-unit-classes-and-units).
- Standard schemas < `8.3.0`: the schema properties had other names: `boolProperty` for `boolRange`, and `elementProperty`, `nodeProperty`, `unitClassProperty`, `unitModifierProperty`, `unitProperty`, and `valueClassProperty` for `elementDomain`, `tagDomain`, `unitClassDomain`, `unitModifierDomain`, `unitDomain`, and `valueClassDomain`. No error code applies. See [3.1.4.8. Schema properties](./03_HED_formats.md#3148-schema-properties) and [A.1.5. Schema properties](./Appendix_A.md#a15-schema-properties) for the mapping.
- Standard schemas < `8.5.0` and library schemas partnered with them: an `annotation` value is not required to have the form `prefix:id value`. Earlier schemas wrote a bare term such as `ncit:C25499`; files partnered with standard schemas before `8.5.0` keep that form, and tools do not check it, so SCHEMA_ANNOTATION_INVALID is not reported. See [A.1.4.2. annotation](./Appendix_A.md#a142-annotation).
- Standard schemas < `8.3.0`: SCHEMA_RESERVED_INVALID (a) requires less. `Inset` must exist only from `8.2.0`; the `reserved` attribute on every row of `tags` and on `Def` and `Def-expand`, and the `topLevelTagGroup` attribute on `Delay` and `Duration`, are required only from `8.2.0`; `reserved` on the ten organizational reserved tags is required only from `8.3.0`. See [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags) and [A.6. Reserved tags file](./Appendix_A.md#a6-reserved-tags-file).

**Schema file formats**

- Standard schemas < `8.5.0` and library schemas partnered with them: the TSV files of these schemas were written with other header rows than those of [A.5.2. TSV header formats](./Appendix_A.md#a52-tsv-header-formats). A tool that reads the TSV format accepts them, and no tool writes them. For standard schema `8.4.0` and its partnered libraries, the `DataProperty`, `ObjectProperty`, and `AnnotationProperty` files have the columns `omn:Domain` and `omn:Range` after `Type`, and the `Sources`, `Prefixes`, and `AnnotationPropertyExternal` files have no `Attributes` column. For standard schema `8.3.0` and its partnered libraries, in addition, the `Tag` file has `rdfs:label` before `Level` and ends with an `omn:EquivalentTo` column (followed by an `Annotations` column in `lang_1.0.0`); the `Unit` file has `hasUnitClass` after `omn:SubClassOf` and ends with `omn:EquivalentTo`; the `UnitClass`, `UnitModifier`, and `ValueClass` files end with `omn:EquivalentTo`; and there are no `Sources`, `Prefixes`, or `AnnotationPropertyExternal` files. Standard schemas < `8.3.0` have no TSV files. No error code applies.
