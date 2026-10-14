# 3. HED formats

A **HED schema** is a formal specification of a standardized HED vocabulary including its properties and constraints.

Each HED schema vocabulary is organized hierarchically so that similar concepts and terms appear close to one another in the hierarchy.

The individual vocabulary terms (the HED schema nodes) **must** satisfy an "is-a" relationship with their parent nodes in the schema. That is, if node *A* is an ancestor of node *B* in the schema, then *B* is a type of *A*. This relationship is fundamental to HED and permits search generality. Searches for *A* are able to also return instances of *B*. All of the nodes of a HED schema must be unique.

A **HED annotation** is a string consisting of comma-separated (and possibly parenthesized) terms from a HED schema. HED annotations provide a standardized language for describing virtually anything. HED's primary application is to describe what happens during an experiment (the experimental events). HED annotations must be associated with one or more specific HED schema versions.

This chapter describes the requirements and formats for HED schemas and HED annotations.

Additional details about HED schema formats can be found in appendix [A. Schema format details](./Appendix_A.md). [7. Library schemas](./07_Library_schemas.md#7-library-schemas) discusses the additional requirements and restrictions on library schemas. [B.2. Schema validation errors](./Appendix_B.md#b2-schema-validation-errors) describes the schema errors.

The HED ecosystem supports a standard base schema and additional discipline-specific library schemas. (See the [expandable schema viewer](https://www.hedtags.org/hed-schema-browser) to explore existing schemas.) Releases of the HED standard base schema are stored in the [standard_schema/hedxml](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml) directory of the [hed-standard/hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository. Releases of HED library schemas are stored in a subdirectory of [library_schemas](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas) in the [hed-standard/hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

Additional rules for HED annotations can be found in [4. Basic annotation](./04_Basic_annotation.md) and [5. Advanced annotation](./05_Advanced_annotation.md). The [Making HED meaningful](https://www.hedtags.org/hed-resources/HedAnnotationSemantics.html) tutorial explains the semantics of HED and rules for making meaningful, standardized, and complete annotations. [B.1. HED validation errors](./Appendix_B.md#b1-hed-validation-errors) gives a complete list of HED annotation validation errors.

## 3.1. Schema rules

### 3.1.1. Schema versions

A HED standard schema version is a string representing a valid [semantic version](https://semver.org/) (e.g., `8.4.0` specifies standard schema version `8.4.0`). HED library schemas have their semantic version appended to `"XXX_"`. Here `"XXX"` is the name of the library (e.g., `lang_1.2.0` represents version `1.2.0` of the `lang` HED library schema).

A schema version specification may be preceded by a **namespace prefix**: an alphabetic namespace name followed by a colon (`:`). An example of a schema version specification using a namespace prefix is `"ts:8.4.0"` or `"mystuff:lang_1.2.0"`. The namespace name can be any alphabetic string. If the schema version specification has a namespace prefix, then all tags drawn from that schema must appear in any corresponding annotation with that namespace prefix prepended (e.g., `"ts:Sensory-event"` for the `"Sensory-event"` tag in schema `"ts:8.4.0"`). Namespace designations allow annotators to use tags from incompatible HED schemas to annotate a dataset.

### 3.1.2. Version combinations

#### 3.1.2.1. Partnered vs unpartnered

HED library schemas are of two types: **partnered** and **unpartnered**. A partnered library schema, which has a `withStandard` attribute in its header, is designed to be used with a specific version of the HED standard schema to form a single unified vocabulary. For example, the score library schema version `2.1.0` is partnered with standard schema version `8.4.0` and has the header (in XML format):

```xml
<HED version="2.1.0" library="score" withStandard="8.4.0">
```

Without the `withStandard` attribute in the header, a schema is considered unpartnered and must be completely self-contained. All current versions of the supported HED library schemas are partnered. The only time a new unpartnered schema would be developed is to support a new type of application where the standard HED schema tags are not relevant.

#### 3.1.2.2. Merged vs unmerged

A partnered library schema can be saved in two equivalent forms: *merged* or *unmerged*. The example in [3.1.2.1 Partnered vs unpartnered](#3121-partnered-vs-unpartnered) shows a schema that has been stored in merged form as a single vocabulary with all of its standard schema partner elements included in the schema file. Because these merged schema files are very large, an alternative, equivalent unmerged file format is also allowed. When stored in unmerged form the schema header includes the *unmerged* attribute as shown here for the XML format:

```xml
<HED version="2.1.0" library="score" withStandard="8.4.0" unmerged="True">
```

The value of the `unmerged` attribute is case-insensitive (`true` and `True` are equivalent). HED schema loaders are **required** to automatically load the HED standard schema partner when loading an unmerged partnered library schema. Elements from a merged library schema always have the `inLibrary` schema attribute to distinguish these elements from standard schema elements. These `inLibrary` attributes are removed when a library schema is saved in unmerged form.

#### 3.1.2.3. Merge groups

HED has adopted a strategy that allows multiple compatible library schemas to be combined into a single build-your-own unified vocabulary. The rules for combining compatible partnered library schemas were introduced in HED specification version `4.0.0`. If the library schemas are incompatible, they can still be used together by placing them in different namespaces. We refer to library schemas in the same namespace as a **merge group**.

Merge groups (i.e., namespaces) are defined in the schema version specification not in the schema itself. The schemas listed in the default namespace (no prefix) form one merge group, and each unique prefix in the version specification designates a distinct merge group. For example the following [BIDS](https://bids.neuroimaging.io/index.html) version specification:

```json
"HEDVersion": ["lang_1.1.0", "score_2.1.0", "bc:testlib_4.0.0"]
```

indicates for this particular BIDS dataset HED tags from the lang and score HED library schemas can be used without prefix, but tags from testlib must have the `bc:` prefix prepended. The user-selected prefix `bc:` is a namespace designator. This dataset uses two namespaces (default and `bc:`).

#### 3.1.2.4. Partnered combinations

Combination of different schemas into a single vocabulary can proceed provided there are no conflicts as governed by the following rules. A specification that violates any of these rules generates a [SCHEMA_LOAD_FAILED](./Appendix_B.md#schema_load_failed) error.

| Topic                 | Rule                                                                                                                                                                                                                                         |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge groups          | Schemas listed in the same namespace form a single merge group.                                                                                                                                                                              |
| Merge groups          | Each merge group is resolved independently; the standard schema partners of different merge groups do not have to agree.                                                                                                                     |
| Merge groups          | Schemas in a merge group can be combined in any order. Whether or not the load fails is independent of order, but what element first generates a conflict depends on the order.                                                              |
| Merge groups          | Duplicate schemas (same name regardless of version) cannot appear in the same merge group.                                                                                                                                                   |
| Standard partner      | All partnered library schemas in a merge group must have the same standard schema partner (the same `withStandard` version).                                                                                                                 |
| Standard partner      | A standard schema in a merge group is allowed if its version is the same as the group partner; it adds nothing to the merged result.                                                                                                         |
| Standard partner      | A standard schema in a merge group raises an error if its version differs from the group partner.                                                                                                                                            |
| Unpartnered schemas   | An unpartnered library schema must be alone in its own namespace.                                                                                                                                                                            |
| Element compatibility | An element (tag, unit class, unit, unit modifier, value class, or schema attribute) appearing in more than one schema of a merge group must have the same attribute values, the same description, and the same ancestor path in each schema. |
| Element compatibility | For schema attribute elements, the properties are the attribute values that are compared: two schema attributes with the same name must have the same properties.                                                                            |
| Element compatibility | An element appearing in more than one schema of a merge group must either have a `#` child in all of its appearances, or in none of them. When the `#` is present, it must have the same attributes in all schemas.                          |
| Element compatibility | A shared element can have different non-`#` children, but the compatibility rules apply to shared children in the same way.                                                                                                                  |
| Element compatibility | The `inLibrary` bookkeeping attribute is excluded from the comparison of attribute values: an element contributed by different library schemas necessarily carries a different `inLibrary` value in each library's merged schema.            |
| Element compatibility | An element contributed by more than one library schema of a merge group carries one `inLibrary` value for each contributing library in the merged result.                                                                                    |
| Auxiliary sections    | New library schema unit classes and their accompanying units are merged directly.                                                                                                                                                            |
| Auxiliary sections    | New library schema units under an existing unit class are merged if there are no conflicts.                                                                                                                                                  |
| Auxiliary sections    | New library schema value classes are merged if there are no conflicts.                                                                                                                                                                       |
| Prologue and epilogue | Differences in the prologues and epilogues of the schemas in a merge group are not conflicts, since merge groups are never saved.                                                                                                            |

See [7.3.6. Lazy partnering](./07_Library_schemas.md#736-lazy-partnering) for a description of the merging process and examples.

### 3.1.3. Version updates

HED schemas are versioned using the semantic versioning system and use these rules for changing the *major.minor.patch* semantic version. These rules are based on the assumption that annotators using the [HED tag](https://hed-specification.readthedocs.io/en/latest/02_Terminology.html#hed-tag) short form will not have to retag their data for patch-level or minor-version changes of the schema. That is, a dataset tagged using schema version *X.Y.Z* will also validate for *X.Y+.Z+*. In addition, validation errors might occur for patch-level or minor-version changes for changes or corrections in tag values or units.

Here is a summary of the types of changes that correspond to different levels of changes in the semantic version:

| Change                                          | Semantic-level |
| ----------------------------------------------- | -------------- |
| Major addition to HED functionality             | Major          |
| Tag deleted from schema.                        | Major          |
| Unit or unit class removed from node.           | Major          |
| Listed unit removed but still derivable (uV).   | Patch          |
| Node attribute value changed                    | Minor          |
| Inherited attribute change                      | Minor          |
| New property added to or removed from schema    | Minor          |
| New value class added to schema                 | Minor          |
| New unit modifier added to schema               | Minor          |
| New tag added to the schema.                    | Minor          |
| New attribute added to schema.                  | Minor          |
| New unit class or unit added to schema.         | Minor          |
| New unit class added to node.                   | Minor          |
| New value class added to node.                  | Minor          |
| Node moved in schema without change in meaning. | Minor          |
| Standard schema partner version changed.        | Minor          |
| Revision of description field in schema.        | Patch          |
| Correction of suggestedTag or relatedTag.       | Patch          |

**Note:** It is an official policy that once in a schema, a node will not be removed without a major schema version change. The one exception is a listed unit that stays valid because it is derived from another unit of its class by an SI unit modifier (`uV` is `u` + `V`, so HED `8.5.0` no longer lists it): removing such a listing changes the validity of no annotation and is a patch-level change; the unit's `hedId` is retired, not reused (see [8.3.1. Schema namespaces versus the ontology namespace](./08_HED_ontology.md#831-schema-namespaces-versus-the-ontology-namespace)). If a node becomes out-of-date, a `deprecated` attribute will be added to the tag in the schema. Suggested replacement tags should be included in the node description. A suggested replacement should be added to the tag patch table.

### 3.1.4. Schema layout overview

Schemas can be specified in any of four equivalent formats: MediaWiki, TSV, XML, or JSON. The examples in this section primarily use MediaWiki or XML formats for illustration, but appendix [A. Schema format details](./Appendix_A.md) provides details about all four formats. The HED schema [online tools](https://hedtools.org/hed/schemas) provide an easy way for users to validate schema and convert between formats.

HED schema developers usually use `.mediawiki` format for more convenient editing, display, and viewing on GitHub. However, the stable links provided for tools to access and download the HED schema are to the XML versions. TSV format is sometimes used early in schema development and JSON format is used primarily by AIs. All formats must be available and synchronized in the [hed-standard/hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

Regardless of the format, the sections of a valid HED schema must appear in the following order. All sections are required except the three after the epilogue, whose status is described below the table.

```{Admonition} Sections of a HED schema (in the required order):
| Section   | MediaWiki format | XML format  |
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
| Sources | `'''Sources'''` | `<schemaSources>` ... `</schemaSources>` |
| Prefixes | `'''Prefixes'''` | `<schemaPrefixes>` ... `</schemaPrefixes>` |
| External annotations | `'''External annotations'''` | `<externalAnnotations>` ... `</externalAnnotations>` |
| Ending line | `!# end hed` | `</HED>` |
```

The three extra sections after the epilogue were introduced with HED schema `8.4.0`. A tool that writes a schema file includes them, like the other sections, even when they are empty. A tool that reads a schema file accepts their omission only under the compatibility conditions given in [3.1.4.10. Sources, prefixes, and external annotations](#31410-sources-prefixes-and-external-annotations). The sections must appear in the order shown.

The sections in the `.xml` version must always be terminated by closing `</  >` tokens, whereas the sections of the `.mediawiki` version, which is line-oriented, are terminated when the next section begins (`#!`) or a top tag (`'''`) is encountered.

The actual HED tag specifications (referred to in the discussion as nodes or tag terms) appear in the `schema` section, while the remaining sections specify additional information and behavior. These additional sections are required, but are allowed to be empty.

If any of the required sections of the schema are missing or out of order, a [SCHEMA_SECTION_MISSING](./Appendix_B.md#schema_section_missing) error occurs.

Each of the schema sections has "schema attributes", which are the attributes that may be assigned to elements in a given section. If a schema attribute is applied improperly to an element in a given section, the [SCHEMA_ATTRIBUTE_INVALID](./Appendix_B.md#schema_attribute_invalid) error occurs.

See [Appendix A.s](./Appendix_A.md) for additional details on format.

#### 3.1.4.1. The header

The schema header line MUST specify the `version` attribute whose value MUST be a valid semantic version. See [SCHEMA_VERSION_INVALID](./Appendix_B.md#schema_version_invalid).

A schema may optionally contain `library`, `withStandard`, and `unmerged` attributes for library schemas. A schema's library name or lack there of is used to locate the schema in the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

The header may optionally contain an XSD namespace specification. If the schema contains any additional unrecognized attributes, [SCHEMA_HEADER_INVALID](./Appendix_B.md#schema_header_invalid) error occurs.

See [A.2.2. MediaWiki header](./Appendix_A.md#a22-mediawiki-header) and [A.3.2. XML header](./Appendix_A.md#a32-xml-header) for more detailed information on the MediaWiki and XML header formats, respectively.

#### 3.1.4.2. The prologue

The prologue should contain a concise introduction to the schema and its purpose. Together with [the epilogue](#3149-the-epilogue) section, the contents are used by tools to provide information about the schema to the users.

The prologue may contain `text` characters or `newline`. If other characters appear, a [SCHEMA_CHARACTER_INVALID](./Appendix_B.md#schema_character_invalid) error occurs.

#### 3.1.4.3. The schema section

The schema section contains the actual vocabulary contents of the schema. Each element in this section is a *node* element, which we will also call a *tag term*. The location of the node element within the section specifies its relationship to other tag terms in the schema.

A node element specifies a name, node attributes, and an informative description of the tag term's meaning. A node name may only contain valid `name` characters (`alphanumeric`, `hyphen`, `underscore`, and `nonascii`; see [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions)).

This also applies to tag extensions. Substitutions for the `#` placeholder that have value classes are governed by the rules of that value class. If other characters appear, a [SCHEMA_CHARACTER_INVALID](./Appendix_B.md#schema_character_invalid) error occurs.

Each schema node element must be unique or a [SCHEMA_DUPLICATE_NODE](./Appendix_B.md#schema_duplicate_node) error is generated.

#### 3.1.4.4. Unit classes and units

A unit class is an attribute of a `#` schema placeholder node. A placeholder MUST NOT have more than one unit class (specification `4.0.0`); a `unitClass` attribute listing several unit classes is a [SCHEMA_ATTRIBUTE_VALUE_INVALID](./Appendix_B.md#schema_attribute_value_invalid) error. A placeholder with a unit class MUST also have `valueClass=numericClass`, because a value with units is a number to be converted; in standard schemas with versions >= `8.5.0` and library schemas partnered with them, a unit class on a placeholder with any other value class, or with none, is likewise a SCHEMA_ATTRIBUTE_VALUE_INVALID error (`8.3.0` and earlier have `Sampling-rate/#` with a unit class and no value class). A schema MAY define the pseudo unit class `anyUnits`, which lists no units and has no `defaultUnits`; a placeholder with `unitClass=anyUnits` accepts a unit from any unit class of the schema, listed or derived, and, when that unit has a `conversionFactor`, its value converts to the default units of the class that unit belongs to; otherwise conversion is undefined, as for any unit without a factor (HED `8.5.0` introduces `anyUnits` and the tag `Quantity` that uses it). A value on such a placeholder MAY be written without a unit: it is then valid as a plain number with no default unit and no conversion; unlike `Delay` and `Duration`, nothing requires a unit on it. When a unit string resolves in more than one unit class, the class that lists it outright wins over a class that only derives it (`dB` is the decibel of `intensityUnits`, not `d` + `B` of `memorySizeUnits`); a string that two classes derive and none lists is a [SCHEMA_DUPLICATE_NODE](./Appendix_B.md#schema_duplicate_node) error, and `anyUnits` with units or `defaultUnits` is a [SCHEMA_ATTRIBUTE_INVALID](./Appendix_B.md#schema_attribute_invalid) error. The unit class definition section specifies the allowed unit classes for the schema as well as the associated units that can be used with tags that take values.

Only the singular version of each unit name is explicitly specified, but the corresponding plurals are also allowed (e.g., `feet` in addition to `foot`, `inches` in addition to `inch`; `hertz` is its own plural). Only unit names may be pluralized; unit symbols never are (`mss` and `Hzs` are invalid). HED uses a `pluralize` function available in both Python and Javascript to check validity.

Units may be in one of four forms as designated by their unit type attributes:

| Unit type                     | Unit type attributes           |
| ----------------------------- | ------------------------------ |
| SI unit                       | only `SIUnit`                  |
| SI unit symbol                | both `SIUnit` and `unitSymbol` |
| unit that is not an SI unit   | no unit type attribute         |
| unit symbol is not an SI unit | only `unitSymbol`              |

Units appear after the value in annotations. A unit with the `unitPrefix` attribute appears before its value instead; the only such unit, `$`, and the `unitPrefix` attribute itself are deprecated as of HED `8.5.0` (`$` carries `deprecatedFrom=8.4.0`) and will be removed in a future major version. Currency values are written with the unit name, as in `5 dollars`.

If a unit class, `SIUnit`, or `unitPrefix` attribute appears in a section other than the unit class definition section of the schema, a [SCHEMA_ATTRIBUTE_INVALID](./Appendix_B.md#schema_attribute_invalid) error occurs. See appendix [A.1.1. Unit classes and units](./Appendix_A.md#a11-unit-classes-and-units) for additional details and a listing.

**Unit names and unit symbols are case-sensitive and MUST NOT contain blanks. A unit in an annotation MUST be a unit listed in the schema, the plural of a listed unit name, or a form derived from a listed unit that has the `SIUnit` attribute by prepending an SI unit modifier (for a compound unit, one modifier per component; see [3.1.4.5. Unit modifiers](#3145-unit-modifiers)), with the case of the unit and of the modifier exactly as listed. Only unit names may be pluralized (`feet`, `milliseconds`); unit symbols never may. `Feet`, `Milliseconds`, and `MS` are invalid.** The deprecated unit `degree Celsius`, listed since before this rule, is the one legacy exception: it cannot be written in an annotation, because a blank separates the value from its unit, and it remains listed only so that older schemas load. Before specification version `4.0.0`, unit names were case-insensitive. Unit class names are case-insensitive, but MUST contain only valid `name` characters. If other characters appear, a [SCHEMA_CHARACTER_INVALID](./Appendix_B.md#schema_character_invalid) error occurs.

A unit class MUST NOT list a unit that can be formed by applying an SI unit modifier to another unit of the same class that has the `SIUnit` attribute; such a unit is derived, not listed. For example, `uV` is `u` + `V` and is not listed once `V` has `SIUnit`. This rule applies to standard schemas with versions >= `8.5.0` and to library schemas partnered with them; earlier standard schemas (`8.2.0` through `8.4.0` list `uV`) remain valid. A violation is a [SCHEMA_DUPLICATE_NODE](./Appendix_B.md#schema_duplicate_node) error. See appendix [A.1.1. Unit classes and units](./Appendix_A.md#a11-unit-classes-and-units) for the units of HED `8.5.0`.

#### 3.1.4.5. Unit modifiers

The unit modifier definition section lists the SI unit multiples and submultiples that are allowed to be prepended to units that have the `SIUnit` schema attribute.

Unit modifiers can only be used with SI units and SI unit symbols. SI unit modifiers used with ordinary SI units have the `SIUnitModifier` attribute, while unit modifiers used with SI unit symbols have the `SIUnitSymbolModifier` attribute.

A **compound unit** is a unit whose name contains `-per-` or a `^` exponent, such as `m-per-s`, `m-per-s^2`, `m^2`, `m^3`, and `mol-per-L`. Its components are unit symbols, and a compound unit that has the `SIUnit` attribute takes one SI unit symbol modifier on each component independently, never on the string as a whole. The grammar is:

```text
unit      := component ("-per-" component)*
component := [modifier] base ["^" digits]
```

Here `base` is a component of the listed unit and `modifier` is an `SIUnitSymbolModifier`. Thus `cm-per-us`, `mm-per-s^2`, and `mm^3` are valid forms of `m-per-s`, `m-per-s^2`, and `m^3`, while `kmm-per-s` (two modifiers on one component), `m-per-sec` (not a symbol), and `m-per-S` (wrong case) are not. An exponent applies to the prefixed component, so `mm^3` is a cubic millimeter. The conversion factor of a compound form is the listed `conversionFactor` multiplied, for each component, by the modifier's `conversionFactor` raised to that component's exponent, negative for components after `-per-`: `cm-per-us` = 1.0 x 0.01 x (1e-6)^-1 = 10000 `m-per-s`, and `mm^3` = (0.001)^3 = 1e-9 `m^3`. A compound form that breaks these rules is a [UNITS_INVALID](./Appendix_B.md#units_invalid) error. Before specification version `4.0.0`, tools applied the modifier to the whole compound unit string.

If a `SIUnitModifier`, or `SIUNitSymbolModifier` attribute appears in a section other than unit modifier section of the schema, a [SCHEMA_ATTRIBUTE_INVALID](./Appendix_B.md#schema_attribute_invalid) error occurs.

**Unit modifiers are case-sensitive.**

See appendix [A.1.2. Unit modifiers](./Appendix_A.md#a12-unit-modifiers) for additional details and a listing of values for the standard schema.

#### 3.1.4.6. Value classes

The value class definition section specifies rules for the values that are substituted for placeholders (`#`). Examples are special characters that are allowed for numeric values or dates. Placeholders that have no `valueClass` attributes, are assumed to take `textClass` values.

See appendix [A.1.3. Value classes](./Appendix_A.md#a13-value-classes) for additional details and a listing of values for the standard schema.

Value class names are insensitive, but must contain only valid `name` characters.

#### 3.1.4.7. Schema attributes

The schema attribute definition section lists the schema attributes that may be applied to schema elements in other sections of the schema (except for the properties section).

The specification of which type of schema elements a particular schema attribute may apply to is specified by its schema properties. If a schema attribute appears in a section contradicted by its properties, a [SCHEMA_ATTRIBUTE_INVALID](./Appendix_B.md#schema_attribute_invalid) error occurs.

See appendices [A.1.4. Schema attributes](./Appendix_A.md#a14-schema-attributes) and [A.1.5. Schema properties](./Appendix_A.md#a15-schema-properties) for additional details and a listing for the standard schema.

#### 3.1.4.8. Schema properties

The schema properties section lists the allowed properties of the schema attributes. These properties help tools validate certain requirements directly based on the HED schema rather than on a hard-coded implementation.

There are two main types of properties: **domain** properties and **range** properties. Property names ending in `Domain` indicate the types of schema element a schema attribute may apply to. The domain properties are `elementDomain`, `tagDomain`, `unitClassDomain`, `unitModifierDomain`, `unitDomain`, and `valueClassDomain`. Schema attributes without any domain property are assumed to apply to node (tag-term) elements.

Property names ending in `Range` indicate the type of value a schema attribute may have. The range properties are `boolRange`, `numericRange`, `stringRange`, `tagRange`, `unitClassRange`, `unitRange`, and `valueClassRange`. A schema attribute with the `boolRange` property does not take a value: its presence indicates true, and its absence indicates false. The remaining property, `annotationProperty`, marks a schema attribute whose value is not inherited by child nodes.

A schema attribute may have multiple domain properties, indicating that the attribute may appear in multiple sections of the schema, and multiple range properties, indicating that its values may be of several types. Before HED standard schema version `8.3.0` these properties had other names (`boolProperty`, `elementProperty`, `nodeProperty`, `unitClassProperty`, `unitModifierProperty`, `unitProperty`, and `valueClassProperty`); see [A.1.5. Schema properties](./Appendix_A.md#a15-schema-properties) for the mapping.

See [A.1.4 Schema attributes](./Appendix_A.md#a14-schema-attributes) and [A.1.5. Schema properties](./Appendix_A.md#a15-schema-properties) for information and a listing of schema attributes and their respective properties.

#### 3.1.4.9. The epilogue

The epilogue should give license information, acknowledgments, and references.

The epilogue may contain `text` characters or `newline`. If other characters appear, a [SCHEMA_CHARACTER_INVALID](./Appendix_B.md#schema_character_invalid) error occurs.

#### 3.1.4.10. Sources, prefixes, and external annotations

The Sources, Prefixes, and External annotations sections (the *extra sections* of [Chapter 2: Terminology](./02_Terminology.md#schema-section)) were introduced in HED schema `8.4.0`. The rules in this section were codified in HED specification `4.0.0`; they apply to standard schemas with versions >= `8.5.0` and to library schemas partnered with those standard schemas.

A tool that writes a schema file, in any format, includes all three extra sections, whether the schema is a standard schema or a library schema and whether a library schema is in merged or unmerged form. A section for which the schema has no entries is written empty: the section header alone in MediaWiki, an element with no children in XML, an empty array in JSON, and a header-only file in TSV. In an unmerged partnered library schema the extra sections are empty unless the library adds rows of its own. The sections must appear in the order Sources, Prefixes, External annotations, immediately after the epilogue.

A tool that reads a schema file requires all three sections in a standard schema with version >= `8.5.0` and in a library schema partnered with such a standard schema; if one is missing, a [SCHEMA_SECTION_MISSING](./Appendix_B.md#schema_section_missing) error occurs. For compatibility with files written before this rule, a reader accepts the omission of any of the three sections from a standard schema with version < `8.5.0` or from an unpartnered library schema and treats each omitted section as an empty section.

Each of these sections is a table of rows with fixed columns:

- **Sources** records the external resources consulted in developing the schema. Columns: `source` (a short name), `link` (a URL), and `description`. A `dc:source` annotation must name one of these rows (see [A.1.6. Schema sources](./Appendix_A.md#a16-schema-sources)).
- **Prefixes** defines the namespace prefixes used in `annotation` attribute values. Columns: `prefix` (including the trailing colon), `namespace` (the IRI of the namespace), and `description`.
- **External annotations** lists the properties from external ontologies that may be attached to schema elements. Columns: `prefix` (which must be defined in the Prefixes section), `id` (the local identifier), `iri` (the full IRI of the property), and `description`.

These are the column names used by the MediaWiki and TSV formats. The XML and JSON formats serialize the first column of each section (`source` or `prefix`) as `name`; the other column names are identical in every format.

A section may have no rows at all. Each row that is present must give a non-empty value in each column; if a row has an empty value in any column, a [SCHEMA_MISSING_EXTRA](./Appendix_B.md#schema_missing_extra) warning is issued.

See [A.1.6. Schema sources](./Appendix_A.md#a16-schema-sources), [A.1.7. Schema prefixes](./Appendix_A.md#a17-schema-prefixes), and [A.1.8. External annotations](./Appendix_A.md#a18-external-annotations) for further discussion, and the per-format sections of Appendix A for the representation of these sections in each file format.

### 3.1.5. Naming conventions

The different parts of the HED schema have different rules for the characters and the names that are allowed.

#### 3.1.5.1. Node elements

Schema designers and users that extend HED schema or develop library schema will be mainly concerned with nodes (tag terms) found in the schema section. The names of these elements must conform to the rules for [`nameClass`](./Appendix_A.md#a13-value-classes).

Other conventions and requirements for the contents of schema node elements are as follows:

```{admonition} Naming conventions for nodes (tag terms) in HED schema.
---
class: tip
---
1. By convention, the first letter of a schema node (tag term) should be capitalized with the remainder lower case.
2. Schema node names consisting of multiple words should not not contain blanks and should be hyphenated.
3. Schema descriptions should be concise sentences, possibly with clarifying examples.
4. Schema descriptions may include only `text` characters but should not contain `newline` or
square brackets or braces.
```

#### 3.1.5.2. Epilogue and prologue

The epilogue and prologue section text must conform to the rules for [`text`](./Appendix_A.md#a13-value-classes) value. The section text may have new lines, which are preserved.

#### 3.1.5.3. Naming in other blocks

The names of elements corresponding to schema attributes, schema properties, unit classes, and value classes should start with a lower case letter, with the remainder in camel case.

Units and unit modifiers follow the naming conventions of the units they represent.

Case is preserved for unit modifiers, as uppercase and lowercase versions often have distinct meanings. The case for unit symbols is also maintained.

### 3.1.6. MediaWiki schema format

[MediaWiki](https://www.mediawiki.org/wiki/Cheatsheet) is a markdown-like format that was selected as the HED schema editing format because of its flexibility and ability to represent nested or hierarchical relationships.

The format is line-oriented, so each schema entry should be on a single line.

The schema must follow the layout described in the previous section. All sections are required, although they may be empty.

Top nodes in the schema are enclosed by pairs of three single quotes (`'''`). The levels of other nodes are designated by the number of asterisks (`*`) at the beginning of the respective defining lines. Each term is separated from its level-indicating asterisks by a single space.

Descriptions, which are enclosed in square brackets (`[ ]`), indicate the meaning of the item they modify. The descriptions are displayed to users by schema browsers and other tools, so every effort should be made to make them informative and clear.

Attributes are enclosed with curly braces (`{ }`). These attributes provide additional rules about how the item and modifying values should be used and handled by tools.

If an attribute or property is referenced in the schema, it must be defined in the appropriate definition section of the schema, or schema processing tools will generate a [SCHEMA_ATTRIBUTE_INVALID](./Appendix_B.md#schema_attribute_invalid) error.

Allowed HED node attributes include unit class and value class values as well as HED schema attributes that have the `tagDomain` or the `elementDomain` property or no domain property. Note: schema attributes having the `elementDomain` property may apply anywhere in the schema, including the schema header.

HED schema attributes that have the `boolRange` property appear with just their name in the schema element they are modifying. The presence of such an attribute indicates that it is true or present.

HED schema attributes that do not have the `boolRange` property are specified in the form of a `name=value` pair. If multiple values of a particular attribute are applicable, they should be specified as name-value pairs separated by commas within the curly braces.

The following example shows a simple HED schema in `.mediawiki` format.

````{admonition} **Example:** Example HED schema in .mediawiki format.

```tid
HED version="8.4.0"

'''Prologue'''
This prologue introduces the schema.

!# start schema
'''Event''' <nowiki>[Something that happens at a given place and time.]</nowiki>
* Sensory-event <nowiki>{suggestedTag=Task-event-role,suggestedTag=Sensory-presentation}[Something perceivable by an agent.]</nowiki>
                              . . .
'''Property'''<nowiki>{extensionAllowed}[A characteristic.]</nowiki>
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
* extensionAllowed <nowiki>{boolRange}[Attribute indicating that users can add child nodes.]</nowiki>
* suggestedTag <nowiki>[Attribute indicating another tag that is often associated with this tag.]</nowiki>
* takesValue <nowiki>{boolRange}[Attribute indicating a placeholder to be replaced by a user-defined value.] </nowiki>
                        . . .
'''Properties''' <nowiki>[Properties of the schema attributes.]</nowiki>
* boolRange <nowiki>[Indicates that a schema attribute's value can be true or false.]</nowiki>
                        . . .
'''Epilogue'''
An optional section that is the place for notes and is ignored in HED processing.

!# end hed
```

````

In the above example, `Property` in the `schema` section is a top node because it appears enclosed by three single quotes, while `Informational-property` is a first-level node because its defining line begins with a single asterisk (`*`).

`Sensory-event` in the `schema` section has a `suggestedTag` attribute (shown in curly braces). Similarly, `Property` has an `extensionAllowed` attribute, and the `#` placeholder has a `takesValue` attribute. The `schema attributes` section must include definitions of `suggestedTag,` `extensionAllowed` and `takesValue` or the schema will not validate.

The definition of the `takesValue` attribute has `boolRange`, so a definition of `boolRange` must be included in the `Properties` section or the schema will not validate.

Everything after each HED node (tag term) must be enclosed by `<nowiki></nowiki>` markup elements. The contents within these markup elements include the description and attributes.

Within the HED schema a `#` node indicates that the user must supply a value consistent with the unit and value class attributes of the `#` node during annotation. Lines with hashtag (`#`) placeholders should have everything after the asterisks, including the `#` placeholder, enclosed by `<nowiki></nowiki>` markup elements.

Additional details and rules can be found in appendix [A.2 MediaWiki file format](./Appendix_A.md#a2-mediawiki-file-format)

### 3.1.7. XML schema format

The `.xml` format directly mirrors the order and information in the `.mediawiki` version of the schema.

The `<node>` elements of the schema represent the HED tags (tag terms), with remaining schema elements specifying additional information and properties.

Each `<node>` element must have a `<name>` child element corresponding to the HED tag term that it specifies.

A `<node>` element should also have a `<description>` child element whose content corresponds to the text that appears in square brackets (`[ ]`) in the `.mediawiki` version.

The schema attributes, which appear as `name` values or `name-value` pairs enclosed in curly braces (`{ }`) in the `.mediawiki` file, are translated into `<attribute>` child elements of `<node>` in the `.xml`. These `<attribute>` elements always have a `<name>` element child and also have a `<value>` element if the corresponding schema attribute does not have the `boolRange` property.

The following is a translation of the `.mediawiki` example from the previous section in the HEDXML format.

````{admonition} **Example:** XML version of the example schema in the previous section.

```xml
<?xml version="1.0" ?>
<HED version="8.4.0">
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
                <name>boolRange</name>
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
                <name>boolRange</name>
            </property>
        </schemaAttributeDefinition>
    </schemaAttributeDefinitions>
    <propertyDefinitions>
        <propertyDefinition>
             <name>boolRange</name>
             <description>Indicates that a schema attribute's value can be true or false.</description>
        </propertyDefinition>
    </propertyDefinitions>
    <epilogue>This epilogue is a place for notes and is ignored in HED processing.</epilogue>
</HED>
```
````

Additional details and rules can be found in appendix [A.3 XML file format](./Appendix_A.md#a3-xml-file-format)

## 3.2. Annotation rules

**HED annotations** are comma-separated strings of HED tags drawn from a HED schema vocabulary. HED validators and other tools use the information encoded in the relevant schema when performing validation and other processing of HED annotations.

Users must provide the version of the HED schema they are using when creating an annotation.

### 3.2.1. Vocabulary organization

HED (Hierarchical Event Descriptors) are nodes (tag terms) organized hierarchically under their respective root or **top nodes**. In HED standard schema versions >= `8.0.0` these top nodes are: `Event`, `Agent`, `Action`, `Item`, `Property`, and `Relation`. Each top node and its subtrees represent distinct **is-a** relationships for the vocabulary schema.

The `Event` subtree tags indicate the general event category, such as whether it is a sensory event, an agent action, a data feature, or an event indicating experiment control or structure.

The HED annotations describing each event may be assembled from a number of sources during processing and the annotations associated with a single event marker may represent multiple events.

Many analysis tools use the `Event` tags as a primary means of segregating, epoching, and processing the data. Ideally, tags from the `Event` subtree should appear at the top level of the HED annotation describing an event to facilitate analysis.

The `Agent` subtree tags indicate the types of agents (e.g., persons, animals, avatars) that take an active role or produce a specified effect. An `Agent` tag should be grouped with property tags that provide information about the agent, such as whether the agent is an experiment participant.

The `Action` subtree tags indicate actions performed by agents. Generally these are grouped in a triple (`A`, (`Action`, `B`)) which is interpreted as `A` does `Action` on `B`. If the action does not have a target, it should be annotated (`A`, (`Action`)), meaning `A` does `Action`.

The `Item` subtree tags represent things with (actual or virtual) physical existence such as objects, sounds, or language.

Descriptive tags are organized in the `Property` subtree. These descriptive tags should always be grouped with the tags they describe using parentheses.

Binary relations are in the `Relation` subtree. Like items from the `Action` subtree, these should be annotated using (`A`, (`Relation`, `B`)).

### 3.2.2. Tag forms

A **HED tag** is a term in the HED vocabulary identified by a path consisting of the individual node names from some branch of the HED schema hierarchy separated by forward slashes (`/`).

Valid HED tags do not have leading or trailing forward slashes (`/`). A HED tag path may also not have consecutive forward slashes.

An important requirement of third generation HED (versions >= `8.0.0`) is that the node names in the HED schema **must be unique**. As a consequence, the user may specify as much of the path to the root as desired when using the tag in annotation.

The full path version is referred to as **long form**, and the version with only the final tag element (excluding placeholder) is called **short form**.

Any **intermediate form** of the tag path is also allowed as illustrated by this example:

```{Admonition} Examples of allowed forms of HED tags with and without values.
| Short-form |  Intermediate form(s) | Long-form |
| -----------|  ------------------ |--------- |
| *Cough*  |  *Move/Breathe/Cough*<br/> *Breathe/Cough* | *Action/Move/Breathe/Cough* |
| *Weight/3 lbs* | *Data-property/Data-value/Physical-value/Weight/3 lbs*<br/> *Data-value/Physical-value/Weight/3 lbs*<br/> *Physical-value/Weight/3 lbs* | *Property/Data-property/Data-value/Physical-value/Weight/3 lbs* |
```

HED tools are available to map between shortened and long forms as needed. The tag must be associated with a schema and must correspond to a path in the schema (excluding any extension or value).

See [TAG_INVALID](./Appendix_B.md#tag_invalid) for errors involving forward slashes (`/`), extra white-space, and other types of tag syntax errors.

### 3.2.3. Tag case-sensitivity

Although by convention tag terms start with a capital letter with the remainder being lower case, tag processing is case-insensitive. This convention makes annotation strings more readable and is recommended for tag extensions. Validators and other tools must treat tags containing the same characters, but different variations in capitalization as equivalent.

The only exception to the case-insensitive processing rule is that units (unit names as well as unit symbols) and unit modifiers MUST be matched with their case preserved, both during schema processing and during annotation processing. SI distinguishes symbols and unit modifiers that differ in case (`m` and `M`), and a unit name, with or without a modifier, must have the case listed in the schema, optionally pluralized. See [3.1.4.4. Unit classes and units](#3144-unit-classes-and-units).

### 3.2.4. Tags that take values

A HED tag that takes a value corresponds to a schema node whose unique child is a `#` leaf node. The actual schema `takesValue` attribute appears on the `#` placeholder rather than on the tag itself.

These tags may appear with or without a value. When used with a value, the tag term is followed by a slash, followed by a value.

A placeholder or its direct parent tag may not be extended in any other way. Thus, tags that have placeholder children cannot be extended even if they inherit an `extensionAllowed` attribute from an ancestor. The parsers treat any child of these tags as a value substituted for the placeholder rather than as a tag extension.

If a `unitClass` is specified as an attribute of the `#` node, then the units specified must be valid units for that `unitClass`. A `#` node has at most one unit class (see [3.1.4.4. Unit classes and units](#3144-unit-classes-and-units)), so a unit string is checked against exactly one unit class, unless that class is `anyUnits`, in which case it is checked against every unit class of the schema and a listed unit wins over a derived form.

The characters that may be used in the value that replaces the `#` placeholder must be in the union of the values allowed by the `valueClass` attributes of the`#` node. If units are given, they may place additional restrictions on the allowed values.

Units appear after the value. Units with the deprecated `unitPrefix` attribute (`$`) appear before the value. **HED parsers assume that units are separated from values by a single blank regardless of the position of the units.** A value with units is the number, one blank, and the unit: `Duration/3 ms` is valid, while `Duration/3ms` (no blank), `Duration/3  ms` (two blanks), and `Duration/ms` (no value) are [VALUE_INVALID](./Appendix_B.md#value_invalid) errors.

Some unit classes have the `defaultUnits` attribute specifying the units that downstream analysis tools should assume if units are omitted.

Additional checks are made on the substituted values depending on the `valueClass`: `numericClass` values must be valid floating point numbers and `dateTimeClass` values must have the [BIDS Datetime format](https://bids-specification.readthedocs.io/en/stable/glossary.html#datetime-formats), RFC 3339 with an optional offset. The whole-value rules are the `value_class_words` entries of [`character_sets.json`](_static/character_sets.json); see [A.1.3. Value classes](./Appendix_A.md#a13-value-classes).

The values of HED tag placeholders cannot stand alone, but must include the parent when used in a HED string. For example, the `Label` node in the HED schema has the `#` child. Thus, the value `myLabel` meant to substitute for the `#` child of the `Label` node must include `Label` term when used in a HED tag (e.g., `Label/myLabel` not `myLabel`).

The values substituted for `#` may themselves be schema node names provided they conform with any value class requirements associated with that `#`. Thus, `Label/Item` is a valid HED tag event though `Item`, itself, is a valid top tag. It is the `Label` tag with its value `Item` and is unrelated to the `Item` HED tag. However, `Data-maximum/Item` is not valid because the `#` child of `Data-maximum` has a `valueClass=numericClass` attribute and the `Item` value is not numeric.

Certain unit classes allow other special characters in their value specification. These special characters are specified in the schema with the `allowedCharacter` attribute. An example of this is the colon in the `dateTimeClass` value class.

See [VALUE_INVALID](./Appendix_B.md#value_invalid) and [UNITS_INVALID](./Appendix_B.md#units_invalid) for information on the specific validation errors associated with tags that take values.

### 3.2.5. Tag extensions

A tag extension, in contrast to a value, is a tag that users add as a child of an existing schema node as a more specific term for an item already in the schema. For example, a user might want to use `Helicopter` instead of the more general term `Aircraft`. Since `Aircraft` inherits the `extensionAllowed` attribute, users may use extended tags such as `Aircraft/Helicopter` in their annotation. The requirements for such an extension are:

```{warning} **Requirements for tag extensions by users:**

1. Unlike values, an extension term must not already be a node in the schema.
2. The extension term contain only `name` characters. Blanks should be avoided.
3. The parent of the tag extension must always be included with the extended tag in annotation.
4. The extension term must satisfy the "is-a" relationship with its parent node.
5. The `#` placeholder cannot be used as an extension -- in particular it cannot be used as a placeholder in definitions or as value annotations in sidecars.

**Note:** The is-a relationship is not checked by validators.
It is needed so that term search works correctly.

```

A reserved tag (see [3.2.8. Reserved tags](#328-reserved-tags)) MUST NOT be extended, although it inherits `extensionAllowed` from `Property`: `Onset/Blah`, `Event-context/Blah` and `Onset/#` are [TAG_EXTENSION_INVALID](./Appendix_B.md#tag_extension_invalid) errors. This rule is stated from specification `4.0.0`; validators apply it for all standard schema versions >= `8.0.0`.

Tag extensions should follow the same naming conventions as those for schema nodes. See [3.1.5. Naming conventions](#315-naming-conventions) for more information about HED naming conventions. A [STYLE_WARNING](./Appendix_B.md#style_warning) is issued for extension tags that do not follow the HED naming convention.

Users should not use tag extension unless necessary for their application, as this breaks the commonality among annotations across datasets. Please open an [issue](https://github.com/hed-standard/hed-examples/issues) proposing that the new term be added to the schema in question, if you think the term would be useful to other users.

See [TAG_EXTENSION_INVALID](./Appendix_B.md#tag_extension_invalid) for information on the specific validation errors associated with missing schemas.

**Note:** User tag extensions are sometimes accidental and due to misspelling, particularly when a long or intermediate form of the tag is used. For this reason the [TAG_EXTENDED](./Appendix_B.md#tag_extended) warning is issued for extended tags during validation.

### 3.2.6. Tag namespace prefixes

Users may select tags from multiple schemas, but additional schemas must be included in the HED version specification.

Users are free to choose any alphabetic namespace name and associate it with a specific schema in the HED version specification. The namespace prefix is that name followed by a colon (e.g., `sc:`), and tags from the associated schema must carry this prefix when used in annotation. The namespace name and its prefix are chosen per dataset and are not part of any schema; they are an import mechanism, like `import pandas as pd` in Python, and the same schema may be given a different prefix in another dataset.

Terms from only one schema can appear in the annotation without a namespace prefix.

See [TAG_NAMESPACE_PREFIX_INVALID](./Appendix_B.md#tag_namespace_prefix_invalid) for information on the specific validation errors associated with missing schemas.

See [7.5. Library schema in BIDS](./07_Library_schemas.md#75-library-schemas-in-bids) for an example of how the namespace prefix notation is used in BIDS.

### 3.2.7. Strings and groups

A **HED string** is an unordered, comma-separated list of HED tags and/or HED tag groups.

A **HED tag group** is an unordered, comma-separated list of HED tags and/or tag groups enclosed in parentheses. Tag groups may include other tag groups.

The validation errors for HED tags and HED strings are summarized in [Appendix B: HED errors](Appendix_B.md#b-hed-errors).

#### 3.2.7.1. Parenthesis and order

Any ordering of HED tags and HED tag groups at the same level within a HED string is equivalent. Valid HED strings may have parentheses nested to arbitrary levels (nested groups). The parentheses must be properly nested and matched.

Parentheses are meaningful and convey association. If `A` and `B` represent HED expressions, (`A`, `B`) is not equivalent to the HED string `A`, `B`. The distinction should be preserved if possible. (`A`, `B`) means that HED tag `A` and HED tag `B` are associated with each other, whereas `A`, `B` means that `A` and `B` are each annotating some larger construct.

Specific rules of association will be encoded in a future version of the HED specification.

See [PARENTHESES_MISMATCH](./Appendix_B.md#parentheses_mismatch) for validation errors result from improper use of parentheses.

#### 3.2.7.2. Tag group attributes

A HED tag corresponding to a schema node with the `tagGroup` attribute must appear inside parentheses (e.g., must be in HED tag group).

A HED tag corresponding to a schema node with the `topLevelTagGroup` must appear in an unnested HED group in an assembled HED annotation. Only one tag with the `topLevelTagGroup` attribute may appear in the same top-level group. The `topLevelTagGroup` attribute is usually associated with tags that have special meanings in HED such as `Definition` and `Onset`.

See [TAG_GROUP_ERROR](./Appendix_B.md#tag_group_error) for information on the group errors detected based on schema attributes.

#### 3.2.7.3. Empty tags and groups

Empty parentheses and multiple commas with no intervening tags represent empty tags and are invalid, as are HED strings with leading or trailing commas. Hence, if `A` and `B` are any HED expressions,\
(`A`, ((`B`))) is valid but (`A`, ()) is not.

See [TAG_EMPTY](./Appendix_B.md#tag_empty) for information on the validation errors due to empty tags or groups. Some of these errors may be reported as [COMMA_MISSING\*](./Appendix_B.md#comma_missing)

#### 3.2.7.4. Repeated expressions

Duplicated tag expressions at the same level in a HED tag group or HED string are not allowed. For example, the expressions (`Red`, `Blue`, `Red`) and (`Red`, `Blue`), (`Red`, `Blue`) have duplicated tag expressions at the same level and are hence invalid.

See [TAG_EXPRESSION_REPEATED](./Appendix_B.md#tag_expression_repeated) for more details on validation errors due to repeated tag expressions.

### 3.2.8. Reserved tags

A **reserved tag** is a tag with the `reserved` schema attribute (see [Chapter 2](./02_Terminology.md#reserved-tag)). Nine of the tags with reserved attributes are *structural*: `Definition`, `Def`, `Def-expand`, `Onset`, `Offset`, `Inset`, `Delay`, `Duration`, and `Event-context`. These tags determine the structure of an annotation and carry the validation rules of this section.

The other reserved tags (including `Collection`, `Condition-variable`, `Task`, `Control-variable`, `Indicator-variable`, `Experimental-trial`, `Experimental-intertrial`, `Time-block`, `Recording` and `Event-stream`) carry no rules beyond their schema attributes. However, these tags are expected to be used by downstream analysis tools in specific ways. `Condition-variable` and `Task` already have defined behaviors, and the other reserved tags are expected to have specific defined behaviors in the future. The `reserved` attribute indicates that these tags have an assigned meaning and are not to be used or modified for other purposes.

The table below gives, for each structural reserved tag other than `Def` and `Def-expand`, the rules for the top-level tag group that contains it. `Def` and `Def-expand` are not rows of the table: they appear in these groups as the anchor. The parts of such a group are named using the example `(Onset, Def/MyDef, Delay/2 s, (Red, Circle))`:

- the **reserved tag**: `Onset`;
- the **anchor**: `Def/MyDef`, the definition the group refers to, written either as a `Def` tag or as the equivalent `Def-expand` group (see [3.2.8.2](#3282-def-and-def-expand-tags));
- **other top-level tags**: `Delay/2 s`;
- **inner groups**: `(Red, Circle)`.

In the table, **Value** says whether the tag requires a value, **Anchor** whether the group requires an anchor, **Others** lists the other top-level tags allowed, and **Min** and **Max** bound the number of inner groups; **Secondary**, **Timeline**, and **{ }** are explained by rules 3, 4, and 5 below. The table is generated from [`reserved_tags.json`](https://www.hedtags.org/hed-specification/_static/reserved_tags.json), which the HED validators also load; [Appendix A.6](./Appendix_A.md#a6-reserved-tags-file) defines the file and the field behind each column.

<!-- reserved-tags:begin -->

Every tag in the following table MUST NOT be extended and MUST appear in a top-level tag group.

| Tag             | Schemas    | Value | Anchor | Others                                 | Min | Max      | Secondary                              | Timeline | { } |
| --------------- | ---------- | ----- | ------ | -------------------------------------- | --- | -------- | -------------------------------------- | -------- | --- |
| `Definition`    | all        | yes   | no     | none                                   | 0   | 1        | none                                   | no       | no  |
| `Delay`         | >= `8.2.0` | yes   | no     | `Duration`, `Onset`, `Offset`, `Inset` | 1   | 1        | `Duration`, `Onset`, `Offset`, `Inset` | yes      | yes |
| `Duration`      | >= `8.2.0` | yes   | no     | `Delay`                                | 1   | 1        | none                                   | no       | yes |
| `Event-context` | all        | no    | no     | none                                   | 0   | no limit | none                                   | no       | no  |
| `Inset`         | >= `8.2.0` | no    | yes    | `Delay`                                | 0   | 1        | none                                   | yes      | yes |
| `Offset`        | all        | no    | yes    | `Delay`                                | 0   | 0        | none                                   | yes      | yes |
| `Onset`         | all        | no    | yes    | `Delay`                                | 0   | 1        | none                                   | yes      | yes |

A violation of a rule in this table is reported as [DEFINITION_INVALID](./Appendix_B.md#definition_invalid) for `Definition`, [TAG_GROUP_ERROR](./Appendix_B.md#tag_group_error) for `Event-context`, and [TEMPORAL_TAG_ERROR](./Appendix_B.md#temporal_tag_error) for `Delay`, `Duration`, `Inset`, `Offset`, and `Onset`.

Tags whose value has two parts:

| Tag          | Value                  | After the name                                                                                                                                                 |
| ------------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Definition` | `name` or `name/#`     | only `#`, present exactly when the definition's contents hold one `#`                                                                                          |
| `Def`        | `name` or `name/value` | the value of the definition's placeholder, checked against that placeholder tag's value class and units; present exactly when the definition has a placeholder |
| `Def-expand` | `name` or `name/value` | the value of the definition's placeholder, checked against that placeholder tag's value class and units; present exactly when the definition has a placeholder |

<!-- reserved-tags:end -->

The following rules complete the table:

1. `Delay` and `Duration` follow these rules only in standard schemas >= `8.2.0`, the first in which they have the `reserved` and `topLevelTagGroup` attributes. In `8.0.0` and `8.1.0` they are ordinary value tags: they may appear anywhere a tag may and are not mapped onto the timeline.
2. A tag whose row says "no" under **Anchor** MUST NOT have a `Def` tag or `Def-expand` group at the top level of its group: `(Duration/3 s, Def/MyDef)` is an error. Except in a definition (see [3.2.8.1](#3281-the-definition-tag)), one may appear inside an inner group: `(Duration/3 s, (Def/MyDef))` is valid.
3. `Delay` is the only tag of the table that may share a group with another one, and in such a group it is secondary, as its **Secondary** column lists. When `Delay` shares a group with `Onset`, `Offset`, `Inset`, or `Duration`, the row of that tag gives the rules for the group and `Delay` is one of its allowed other top-level tags: `(Onset, Def/MyDef, Delay/2 s)` is valid with no inner group, as `(Onset, Def/MyDef)` is. The `Delay` row applies only when `Delay` is the only tag of the table in its group, so `(Delay/2 s, (Red))` is valid and `(Delay/2 s)` alone is an error.
4. A tag marked "yes" under **Timeline** MUST NOT appear in a table without an `onset` column (or equivalent such as a `TimestampVectorData` column in NWB).
5. A group whose tag is marked "no" under **{ }** (e.g.,`Definition`, `Event-context`) MUST NOT contain a sidecar column reference (`{column}`). A column reference MAY appear in other groups, and the rules of the table are checked on the assembled annotation (see [3.2.9.3](#3293-sidecar-curly-braces), rule 9).
6. A violation is reported with the code named after the table. A tag that is outside a group, outside a top-level group, or next to a top-level tag its row does not allow MAY instead be reported as [TAG_GROUP_ERROR](./Appendix_B.md#tag_group_error).

These rules are stated from specification `4.0.0`; validators apply them for all standard schema versions >= `8.0.0`, except as rule 1 says. The subsections below expand on the information.

#### 3.2.8.1. The `Definition` tag

A definition gives a name to a group of tags, so that annotations can refer to the whole group with a `Def` tag. Definitions are useful for lab-specific concepts and are the anchors of `Onset`, `Offset`, and `Inset` groups. Each definition is independent and stands alone.

A definition is a tag group `(Definition/name, (contents))` or `(Definition/name/#, (contents))`; a definition with a placeholder MUST have the inner group. Definitions appear only where definitions are allowed, such as the definition entries of a sidecar or definitions supplied separately to a tool, and MUST NOT appear in the annotations of a tabular file.

`Definition`, `Def`, and `Def-expand` are the only tags that permit values with two parts, `name` or `name/value`, an exception to the rule that the value of a `nameClass` tag contains no `/`. The name MUST be a `nameClass` value. After a `Definition` name only `#` MAY follow, and when it does, the contents MUST contain exactly one tag with a `#` placeholder: `Definition/MyDef/3` is an error.

The contents of a definition MUST NOT contain, at any level, a structural reserved tag (`Definition`, `Def`, `Def-expand`, `Onset`, `Offset`, `Inset`, `Delay`, `Duration`, `Event-context`) or a tag with the `required` or `unique` attribute.

A definition name MAY be defined more than once only when every definition of that name is identical: the same placeholder form and the same contents, without regard to case or order.

See [DEFINITION_INVALID](./Appendix_B.md#definition_invalid) for the errors and [5.1. Creating definitions](./05_Advanced_annotation.md#51-creating-definitions) for examples.

#### 3.2.8.2. `Def` and `Def-expand` tags

A definition is used in an annotation as the tag `Def/name`, or `Def/name/value` when the definition has a placeholder. The equivalent expanded forms are the groups `(Def-expand/name, (contents))` and `(Def-expand/name/value, (contents))`, whose inner group holds the definition's contents with the value substituted for the placeholder. The value MUST be present in the assembled annotation exactly when the definition has a placeholder, and it is checked as the value of the definition's placeholder tag, with that tag's value class and units: `Def/MyDef/3 Hz`. In a sidecar, the value may itself be a `#` placeholder that is filled in during assembly.

Annotators SHOULD avoid writing `Def-expand` groups: the expanded form is generally created by tools that need the actual tags of a definition's contents during processing. Tools SHOULD be able to transform between the two forms; transforming a `Def` tag into a `Def-expand` group requires the definition, while the reverse does not.

The two forms are equivalent. A `Def-expand` group stands wherever its `Def` tag would stand, and every rule about the place of a `Def` tag, such as rule 2, applies to it unchanged: `(Duration/3 s, (Def-expand/MyDef, (Red)))` is an error, as `(Duration/3 s, Def/MyDef)` is. The inner group of a `Def-expand` group MUST match the definition's contents, with the value substituted, and is never counted as an inner group of the group that contains it.

See [DEF_INVALID](./Appendix_B.md#def_invalid) and [DEF_EXPAND_INVALID](./Appendix_B.md#def_expand_invalid) for the errors and [5.2. Using definitions](./05_Advanced_annotation.md#52-using-definitions) for examples.

#### 3.2.8.3. `Onset`, `Offset`, and `Inset`

Many events are not instantaneous but unfold over time as event processes. An `Onset` group marks the start of such a process, identified by its anchor; an `Offset` group with the same anchor marks its end. A later `Onset` group with the same anchor also ends the process and starts a new one. The inner group of an `Onset` holds the tags that are specific to that instance of the event, not to every instance. An `Inset` group marks an intermediate time point of an ongoing process, and its inner group describes that point; a process may have several.

An `Offset` or `Inset` group MUST have the same anchor as an `Onset` that is ongoing at its time: an `Offset` before the corresponding `Onset`, or after an `Offset` with no `Onset` of that anchor in between, is an error. An `Onset` or `Offset` group MUST NOT occur at the same time as another `Onset`, `Offset`, or `Inset` group with the same anchor. Anchors with different placeholder values are different anchors.

See [TEMPORAL_TAG_ERROR](./Appendix_B.md#temporal_tag_error) for the errors and [5.3.1. Using Onset and Offset](./05_Advanced_annotation.md#531-using-onset-and-offset) for examples.

#### 3.2.8.4. `Duration` and `Delay`

A `Duration` group represents an event that begins at the time of the row's event marker and lasts for the given time; the other tags of the group describe the event. A `Delay` group represents an event that begins at the row's time plus the given delay; if the group also contains `Duration`, the event lasts for that time, otherwise it is a point event. A `Delay` in an `Onset`, `Offset`, or `Inset` group places that marker at the row's time plus the delay (rule 3). The start or end time computed this way need not coincide with any event marker in the file; tools compute it during analysis and may insert markers.

The value of `Duration` and `Delay` is a number with a unit of the `timeUnits` unit class (in a sidecar, a `#` placeholder for such a value). In a timeline table (see [3.3.4. Timeline versus descriptor tables](#334-timeline-versus-descriptor-tables)) the value is placed on the timeline represented by the table, so it MUST use a unit with a `conversionFactor` in the schema; `month` and `year` have none. In a descriptor table, `Duration` MAY use any unit of its unit class.

See [TEMPORAL_TAG_ERROR](./Appendix_B.md#temporal_tag_error) for the errors, and [5.3.3. Using Duration](./05_Advanced_annotation.md#533-using-duration) and [5.3.4. Using Delay](./05_Advanced_annotation.md#534-using-delay) for examples.

#### 3.2.8.5. The `Event-context` tag

An `Event-context` group records the event processes that are ongoing at the time of an event marker, for example an image displayed from its `Onset` until its `Offset`. Each inner group holds the tags of one ongoing process. The group is generated by tools during event processing, with every definition and column reference already expanded, and is generally not written by annotators. Because `Event-context` has the `unique` attribute, an assembled annotation contains at most one `Event-context` group.

See [TAG_GROUP_ERROR](./Appendix_B.md#tag_group_error) and [TAG_NOT_UNIQUE](./Appendix_B.md#tag_not_unique) for the errors and [5.5. Event contexts](./05_Advanced_annotation.md#55-event-contexts) for examples.

### 3.2.9. Sidecars

JSON sidecars are an integral part of the [BIDS](https://bids.neuroimaging.io/) (Brain Imaging Data Structure) neuroimaging standard and are used to associate metadata with data files.

The JSON sidecars that are relevant to HED are associated with tabular data files. For example, the rows of tabular event files represent time markers on the experimental timeline, and the assembled HED annotations for each row describe what happened at that time marker. A sidecar containing annotations associated with the columns of such an event file allows HED tools to assemble HED annotations for each row of the file.

In addition to sidecars, HED annotations can also be given in the `HED` column of tabular files. At validation or analysis time the HED information from both the `HED` column of a tabular file and its associated sidecar are assembled to provide the annotation.

HED validators assume that the annotation dictionary is saved in JSON format and that they comply with the [BIDS sidecar](https://bids-specification.readthedocs.io/en/stable/appendices/hed.html) format.

#### 3.2.9.1. Sidecar entries

A BIDS sidecar is a JSON dictionary with several types of entries, three of which are relevant to HED:

```{Admonition} Three types of JSON sidecar HED-related entries.
**Categorical entries**
- The top-level JSON key corresponds to a column name in the event file.
- The value associated with the HED key is a dictionary of HED annotations.
- The keys of the annotation dictionary are the unique column values.
- The entry is not required to have annotations for every possible unique column value.
- Tools may choose to issue a warning if a column value does not have an annotation.
- The annotation dictionary may include annotations for values that do not appear in a particular event file.


**Value entries**:
- The top-level JSON key corresponds to a column name in the event file.
- The value associated with the HED key is a HED string.
- The entry's annotation is applicable to all values in its associated event file column.
- The HED annotation must contain a single `#` placeholder.
- Each row's column value is substituted for the `#` in the annotation
when the row annotation is assembled.

**Dummy entries**:
- The top-level JSON key must not correspond to a column name in the event file.
- The value associated with the HED key is a dictionary of HED annotations.
- The keys are dummy entries.
- Used to gather HED definitions.

```

The other types of sidecar entries include categorical and value entries with no `"HED"` key, as well as arbitrary entries whose keys do not correspond to column names in an associated tabular file.

When annotations are assembled, sidecar entries with no `"HED"` key are ignored as are entries in the corresponding tabular data file that have `n/a` or blank values.

See [3.2.9.4. A sidecar example](./03_HED_formats.md#3294-a-sidecar-example) for an elaborated example of these different types of entries and [3.2.10.3. Event-level processing](./03_HED_formats.md#32103-event-level-processing) for an example of how the resulting HED annotations are assembled.

#### 3.2.9.2. Sidecar validation

All HED-related entries in a JSON sidecar must have `"HED"` as a key in a second-level dictionary. `"HED"` cannot appear as a sidecar key that is not at the second level. Further, a sidecar is not permitted to provide a HED annotation for `n/a`. Both of these generate a [SIDECAR_INVALID](./Appendix_B.md#sidecar_invalid) error.

HED definitions are required to be separated into dummy sidecar column entries and cannot appear in sidecar entries containing tags other than definitions. A HED definition appearing in a categorical or value sidecar entry generates a [DEFINITION_INVALID](./Appendix_B.md#definition_invalid) error.

The sidecar does not have to provide a HED-relevant entry for every event file column. Columns with no corresponding sidecar entry are skipped during assembly of the HED annotation for an event file row. However, if a value is encountered in a tabular file column that is annotated as a categorical column but does not have a HED annotation, a [SIDECAR_KEY_MISSING](./Appendix_B.md#sidecar_key_missing) warning is generated.

HED value sidecar entries must contain exactly one `#` placeholder in the HED string annotation associated with the entry. The `#` placeholder should correspond to a `#` in the HED schema, indicating that the parent tag (also included in the annotation) expects a value. These issues generate a [PLACEHOLDER_INVALID](./Appendix_B.md#placeholder_invalid) error.

If the placeholder is followed by a unit designator, the validator checks that these units are consistent with the unit class of the corresponding `#` in the schema. The units are not mandatory.

#### 3.2.9.3. Sidecar curly braces

The curly brace notation is new with HED specification version `3.2.0` and is supported by all versions of the HED schema >= `8.0.0`. The notation was introduced to facilitate proper nesting of HED tags associated with different event file columns when the complete HED annotation for an event marker is assembled.

When a column name appears in curly braces within a HED annotation in a JSON sidecar, the corresponding HED annotation for that row is substituted for the curly braces and their contents when the HED annotation is assembled.

If a column is used in curly braces in a HED annotation, then that column must have a HED annotation or a [SIDECAR_INVALID](./Appendix_B.md#sidecar_invalid) error is generated.

```{admonition} Rules for curly braces notation in sidecars.
---
class: tip
---
1. The item within the curly braces must either be the word `HED` or
the name of another HED-annotated column within the sidecar.
2. The HED annotation for the column in curly braces directly replaces the curly braces and their contents in the target annotation.
3. During assembly of a HED annotation for an event, if the 'n/a' value appears in a curly brace column,
the curly brace expression including the curly braces as well as any extra parentheses or commas are removed.
A value other than `n/a` or blank in a curly brace column is validated in every row, whether or not the row's template substitutes it.
4. A sidecar column name cannot both appear in a curly braces and have
an annotation that uses curly braces (to prevent circular references).
5. The curly braces cannot be used within a `Definition` or an `Event-context` group.
6. Curly braces can not appear in the HED column of a tabular file.
7. Curly braces can not be nested.
8. A pair of curly braces must appear syntactically as a tag and not as the substitution for a place holder.
9. The group rules of a structural reserved tag (its anchor, the number of inner groups, and the tags allowed beside it, see [3.2.8](#328-reserved-tags)) are checked on the assembled annotation. A sidecar entry such as `(Duration/#, {stim_desc})` is valid when every substitution of `{stim_desc}` supplies the required inner group.

```

If curly braces appear in the HED column of a tabular file, a [CHARACTER_INVALID](./Appendix_B.md#character_invalid) error is generated.

If curly braces appear in a `Definition`, a [DEFINITION_INVALID](./Appendix_B.md#definition_invalid) error is generated.

If the curly brace notation is used improperly in a sidecar or elsewhere, a [SIDECAR_BRACES_INVALID](./Appendix_B.md#sidecar_braces_invalid) is generated.

#### 3.2.9.4. A sidecar example

The following example illustrates the different types of JSON sidecar entries.

(example-sidecar-anchor)=

````{Admonition} Different types of sidecar annotation entries that might appear in
---
class: tip
---
```json
{
   "event_type": {
      "LongName": "Event category",
      "Description": "Indicator of type of event.",
      "Levels": {
          "show": "Show a face to a participant.",
          "press": "Participant presses key to indicate symmetry."
       },
      "HED": {
          "show": "Sensory-event, Visual-presentation, {stim_file}",
          "press": "Agent-action, (Experiment-participant, (Press, {key}))"
       }
   },
   "stim_file": {
       "LongName": "Stimulus image file",
       "Description": "Time from stimulus presentation until subject presses button",
       "HED": "(Image, Face, Pathname/#)"
   },
   "key":   {
       "LongName": "Indicates which key is pressed.",
       "Description": "Indicator of participant evaluation.",
       "HED": {
          "left-arrow": "((Leftward, Arrow), Keypad-key)",
          "right-arrow": "((Rightward, Arrow), Keypad-key)"
       }
   },
   "symmetry":   {
       "LongName": "Indicates symmetrical or asymmetrical.",
       "Description": "Indicates the participant's judgement of symmetry.",
       "HED": {
          "symmetric": "(Judge, Asymmetrical)",
          "asymmetric": "(Judge, Symmetrical)"
       }
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

In the example, `"event_type"` is the name of a column that is annotated using the **categorical** strategy. Its top-level dictionary has `"LongName"`, `"Description"`, `"Levels"`, and `"HED"` keys.

The value of `"Levels"` is a dictionary with the unique values in the `"event_type"` column keyed to full text descriptions of these unique values.

The value of `"HED"` is a dictionary with the unique values in `"event_type"` keyed to the corresponding HED annotations of these unique values. In the above example, the unique values are `"show"` and `"press"`. The HED annotation for `show` is `"Sensory-event, Visual-presentation, {stim_file}"`.

Notice use of curly braces in the notation. Here `"stim_file"` must correspond to another HED-annotated column in the sidecar. The `"stim_file"` column is an example of a value column. Its top level dictionary keys are `"LongName"`, `"Description"`, and `"HED"`. and its annotation entry: `"(Image, Face, Pathname/#)"`. This annotation has a single `#`. The filename in the `stim_file` column replaces this `#` when the HED annotation for a line in an associated `events.tsv` file is assembled.

Since `"stim_file` and `"key"` appear within curly braces in annotations for `"event_type"`, their HED annotations can not use curly braces.

The `"dummy_defs"` is an example of a **dummy annotation**. The value of this entry is a dictionary with a `"HED"` key pointing to a dictionary. A dummy annotation is similar in form to a **categorical annotation**, but its keys do not correspond to any event file column values. Rather it is used as a container to organize HED definitions.

In the example, `Definition/Cue1` is a definition that does not use a placeholder (`#`) modifier in its name, while `Definition/Image/#` is a definition whose name `Image` is modified by a placeholder value. Notice that `Image` is both a definition name and an actual tag in the schema in this example. This is permitted.

### 3.2.10. Tabular files

A tabular (`.tsv`) file is a text file in which each line represents a row in a table. The column entries in a given row are separated by tabs. The first line of the file must contain a tab-separated list of column names, which should be unique. This description of tabular files conforms to that used by [BIDS](https://bids.neuroimaging.io/).

#### 3.2.10.1 Tabular types

Generally each row in a table represents an item and the columns values provide properties of that item. The most common HED-annotated tables represent event markers in an experiment. For example, each BIDS `events.tsv` file contains a table whose rows represent markers on the experimental timeline. The columns contain additional information pertaining to that time marker.

Another common HED-annotated table contains metadata. For example, in the BIDS `participants.tsv` each row represents a participant, and the columns provide characteristics or other information about the participant identified in that row.

In any case, the general strategy for validation or other processing is:

1. Process the individual components of the HED annotation (tag-level and string-level processing).
2. Assemble the component annotations for a row (event-level or row-level processing).
3. Check consistency and relationships among the row annotations (table-level processing).

See [BIDS tabular files](06_Infrastructure_and_tools.md#631-bids-tabular-files) for more examples.

#### 3.2.10.2. Table annotations

BIDS HED annotations for a table can occur both in a column called `HED` within the table and in an associated JSON sidecar.

The values in a table column that a sidecar value entry annotates must also be valid: for every row whose value is not `n/a` or blank, the string obtained by substituting the value for the `#` in the column's annotation must be a valid HED string ([VALUE_INVALID](./Appendix_B.md#value_invalid), [UNITS_INVALID](./Appendix_B.md#units_invalid), or [CHARACTER_INVALID](./Appendix_B.md#character_invalid) as applicable). This check is made column by column before row assembly and does not depend on whether the row's assembled annotation uses the column, in particular when the column appears in curly braces only in templates the row does not select.

The HED strings that appear in a `HED` column must be valid HED strings. If the first column is not called `onset`, the assembled annotation for the tabular file cannot contain any of the tags `Onset`, `Offset`, or `Inset`.

Definitions many not appear in the `HED` column of a tabular file or in any entry of a JSON sidecar that contains items other than definitions.

See [DEFINITION_INVALID](./Appendix_B.md#definition_invalid) and [TEMPORAL_TAG_ERROR](./Appendix_B.md#temporal_tag_error) for information.

#### 3.2.10.3. Event-level processing

After individual HED tags and HED strings in the `HED` column of tabular files and in the associated sidecars are validated or otherwise processed, the HED strings associated with each row of the tabular file must be assembled to provide an overall annotation for the row. We refer to this as *event-level* or *row* processing.

If the HED schema used for processing contains a schema node that has the `required` attribute, then the assembled HED annotations for each row must include that tag. Currently, HED schema versions >= `8.0.0` do not contain any nodes with the `required` attribute, and this attribute may be deprecated in future versions of the schema.

If the HED schema used for processing contains a schema node that has the `unique` attribute, then the assembled HED annotations for each row must contain no more than one occurrence of that tag. Currently, only `Event-context` has the `unique` attribute for HED schema versions >= `8.0.0`.

See [REQUIRED_TAG_MISSING](./Appendix_B.md#required_tag_missing) and [TAG_NOT_UNIQUE](./Appendix_B.md#tag_not_unique) for information on the validation errors that may occur with tags that have the `required` or `unique` schema attributes, respectively.

```{Admonition} General procedure for event-level (row) assembly.

1. Create an empty result list.
2. Create an assembly list of columns that contain HED annotations
and whose names do not appear in the curly braces of other HED annotations.
3. For each the column in the assembly list look up the annotation in the sidecar, replacing all curly braces and place holder values appropriately.
Append to the result list.
4. If a `HED` column annotation exists for that row and `HED` did not appear
in curly braces in the sidecar, concatenate the annotation to the result list.
5. Finally, join all the entries of the result list using a comma (`,`) separator.

In all cases `n/a` column values are skipped.
```

To illustrate the assembly process, consider the following excerpt from an event file:

```{Admonition} General procedure for event-level (row) assembly.

| onset | duration | event_type | stim_file | key | symmetry | HED |
| ----- | -------- | ---------- | --------- | --- | -------- | --- |
| 3.42  | n/a   | show  |   h234.bmp  |  n/a |  n/a | "(Recording, Label/Setup)" |
| 3.86  | n/a    | press  |  n/a  |  left-arrow  |  asymmetric | n/a |
| 7.42  | n/a    | show  |   h734.bmp  |  n/a |   n/a | n/a |
```

Using the [example sidecar](example-sidecar-anchor) results in the following assembled HED annotation for the first row of the event file:

````{Admonition} A result for event-level (row) assembly of the sample file.
---
class: tip
---
```shell
"Sensory-event, Visual-presentation, (Image, Face, Pathname/h234.bmp), (Recording, Label/Setup)"
```
````

The specific annotation `(Image, Face, Pathname/h234.bmp)` has been substituted for `{stim_file}` and the annotation for in the `HED` column of the `events.tsv` file has been included. The entries with `n/a` have been ignored.

For more examples of event assembly, see [How HED works in BIDS](https://www.hedtags.org/hed-resources/BidsAnnotationQuickstart.html#how-hed-works-in-bids) tutorial.

#### 3.2.10.4. Table-level processing

HED versions >= `8.0.0` allow annotation of relationships among rows in a table. Hence, processing generally requires that annotations for all the rows be assembled so that consistency can be checked.

To validate temporal scope, the validator must assure that each `Onset` and `Offset` tag is associated with an appropriately defined identifier corresponding to a definition name. The validator must also check to make sure that `Onset` and `Offset` tags are properly matched within the data recording. In particular every `Offset` tag group must correspond to a preceding `Onset` tag group.

See [TEMPORAL_TAG_ERROR](./Appendix_B.md#temporal_tag_error) for details on the type of errors that are generated due to `Onset` and `Offset` errors.

## 3.3. Annotation semantics

HED annotations describe events and entities using tags drawn from a HED schema vocabulary. The semantic interpretation of these annotations depends on their structure and context.

### 3.3.1. The reversibility principle

**A well-formed HED annotation SHOULD be translatable back into a coherent English description.**

This reversibility principle serves as the fundamental semantic validation test. If a HED string cannot be converted back into a meaningful English sentence, the annotation likely has structural problems, usually related to incorrect grouping.

For example, the HED string:

> `Experimental-stimulus, Sensory-event, (Visual-presentation, (Red, Circle))`

translates to: "An experimental stimulus sensory event consisting of a visual presentation of a red circle."

In contrast, the ungrouped version:

> `Experimental-stimulus, Sensory-event, Visual-presentation, Red, Circle`

is ambiguous: "An experimental stimulus sensory event with visual presentation; something red; something circular."

The grouping `(Red, Circle)` makes it clear that both properties describe the same object. The outer grouping indicates that the red circle is something to be seen.

### 3.3.2. Semantic grouping

**Parentheses group tags that describe the same entity, relationship, or concept.**

Tags within a group are semantically bound and work together to describe one thing. Tags outside the group describe different aspects or entities.

#### 3.3.2.1. Basic grouping rules

The following rules govern how tags should be grouped:

1. **Object properties** - Tags describing properties of an object MUST be grouped together.

   - Example: `(Red, Circle)` indicates a single red circular object.

2. **Agent-action-object** - Agent-action-object triples require nested grouping.

   - Pattern: `((Agent-tags), (Action-tag, (Object-tags)))`
   - Example: `((Experiment-participant), (Press, Mouse-button))`

3. **Directional relationships** - Tags from the `Relation/` subtree require specific nesting.

   - Pattern: `(A, (Relation-tag, C))` means "A has the relationship to C"
   - Example: `((Red, Circle), (To-left-of, (Green, Square)))`

4. **Independent facts** - Tags describing independent separate events should be grouped separately.

   - Pattern: `(Event-type1, Task-event-role1, and Sensory-modality1, (...)), (Event-type2, Task-event-role2, and Sensory-modality2, (...))`.
   - Example: `(Experimental-stimulus, Sensory-event, Visual-presentation, (Red, Circle)), (Sensory-event)` not `(Experimental-stimulus, Sensory-event, Red, Circle)`

5. **Structural reserved tags** - Structural reserved tags have special rules for grouping and location in an annotation.

   - Tags: `Definition`, `Def`, `Def-expand`, `Onset`, `Inset`, `Offset`, `Delay`, `Duration`, `Event-context`
   - See: [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags) for details of the specification.
   - See: [5. Advanced Annotation](./05_Advanced_annotation.md) for example usage.

See [TAG_GROUP_ERROR](./Appendix_B.md#tag_group_error) for validation errors related to grouping.

#### 3.3.2.2. Event structure

Every event annotation SHOULD include both an `Event` tag and a `Task-event-role` tag:

- **Event tags** (from `Event/`) classify the nature of what happened:

  - `Sensory-event`, `Agent-action`, `Data-feature`, `Experiment-control`, `Experiment-procedure`, `Experiment-structure`, or `Measurement-event`

- **Task-event-role tags** (from `Task-event-role/`) classify the event's role in the task:

  - `Experimental-stimulus`, `Cue`, `Participant-response`, `Feedback`, `Instructional`, etc.

These tags typically appear at the top level or grouped together in a top-level group.

For `Sensory-event` types, a `Sensory-modality` tag (e.g., `Visual-presentation`, `Auditory-presentation`) SHOULD appear with the `Sensory-event` tag.

### 3.3.3. Assembly semantics

When annotations are assembled from multiple sources (sidecar columns, HED column), the semantic interpretation depends on the assembly method.

#### 3.3.3.1. Concatenation assembly

When columns are NOT referenced in curly braces, their annotations are concatenated with commas at the top level. Tags at the same level are independent.

#### 3.3.3.2. Curly brace assembly

When curly braces `{column_name}` appear in a sidecar annotation, the referenced column's annotation REPLACES the curly braces, allowing explicit control over grouping structure.

Rules for curly brace usage:

1. The item within curly braces MUST be either `HED` or a HED-annotated column name.
2. The substituted annotation directly replaces the curly braces and their contents.
3. If an `n/a` value appears in a curly brace column, the entire curly brace expression is removed.
4. A column name MUST NOT both appear in curly braces and use curly braces in its own annotation.
5. Curly braces MUST NOT appear in `Definition` tags or in the `HED` column of tabular files.

See [SIDECAR_BRACES_INVALID](./Appendix_B.md#sidecar_braces_invalid) for curly brace errors.

### 3.3.4. Timeline versus descriptor tables

A table with an `onset` (or equivalent) column is a **timeline table**: each row describes what happened at the time in its `onset` column. Currently the only timeline tables in BIDS are in `*_events.tsv` files. In NWB, dynamic tables with a `TimestampVectorData` type are considered to be timeline tables.

A table without an `onset` or equivalent column is a **descriptor table**: each row describes the properties of an entity, such as a participant, session, or sample. An example of a descriptor table in BIDS is the table contained in the `participants.tsv` file.

- In a timeline table, each assembled annotation SHOULD include at least one `Event` tag. The temporal tags `Onset`, `Offset`, `Inset`, `Duration`, and `Delay` MAY be used.
- In a descriptor table, annotations describe characteristics of the entity and MUST NOT include `Event` tags. `Onset`, `Offset`, `Inset`, and `Delay` MUST NOT be used (rule 4 of [3.2.8](#328-reserved-tags)); `Duration` MAY be used with any unit of its unit class ([3.2.8.4](#3284-duration-and-delay)).

See [TEMPORAL_TAG_ERROR](./Appendix_B.md#temporal_tag_error) for validation errors when temporal tags appear in descriptor tables.
