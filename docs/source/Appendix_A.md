(appendix-a-schema-format-details-anchor)=

# A. Schema format details

This appendix augments the discussion of HED schema formats presented in [Chapter 3: HED formats](./03_HED_formats.md) of the HED specification. The appendix presents additional details on the rules with examples for standard HED schema and HED library schema in `.mediawiki`, `.xml`, `.json`, and `.tsv` formats.

## A.1. Auxiliary schema sections

This section gives information about how the various auxiliary sections of the HED schema are used to specify the behavior of the schema elements.

### A.1.1. Unit classes and units

Unit classes allow annotators to express the units of values in a consistent way. The plurals of the unit names are not explicitly listed, but are allowed (`feet`, `inches`, `seconds`; `hertz` is its own plural), as HED tools use standard pluralize functions to expand the list of allowed units. A `#` placeholder has at most one unit class. The pseudo unit class `anyUnits` lists no units; a placeholder with `unitClass=anyUnits` accepts a unit from any unit class of the schema, and the value converts to the default units of that unit's class when the unit has a `conversionFactor` (see [A.1.4.3. conversionFactor](#a143-conversionfactor)); a value without a unit is valid and has no default unit. See [3.1.4.4. Unit classes and units](./03_HED_formats.md#3144-unit-classes-and-units).

Units corresponding to unit symbols (i.e., have a `unitSymbol` attribute) represent abbreviated versions of units and cannot be pluralized (`mss` and `Hzs` are invalid).

Elements with the `SIUnit` modifier may be prefixed with a multiple or a sub-multiple modifier. If the SI unit does not also have the `unitSymbol` attribute, then multiples and sub-multiples with the `SIUnitModifier` attribute are used for the expansion.

On the other hand, units with both `SIUnit` and `unitSymbol` attributes are expanded using multiples and sub-multiples having the `SIUnitSymbolModifier` attribute.

Note that some units such as byte are designated as SI units, although they are not part of the SI standard. However, they follow the same rules for unit modifiers as do SI units.

```{list-table} Unit classes and units in HED 8.5.0 (* indicates unit symbol; a default unit such as mA that is not listed is a derived form).
---
widths: 20 10 40
header-rows: 1
---
* - Unit class
  - Default units
  - Units
* - accelerationUnits
  - m-per-s^2
  - m-per-s^2*
* - angleUnits
  - radian
  - radian, rad*, degree
* - anyUnits
  - (none)
  - (none: accepts any unit of any unit class)
* - areaUnits
  - m^2
  - m^2*
* - chargeUnits
  - C
  - coulomb, C*
* - concentrationUnits
  - mol-per-L
  - molar, mol-per-L*
* - currencyUnits
  - dollar
  - dollar, $* (deprecated), euro, point
* - currentUnits
  - mA
  - ampere, A*
* - electricPotentialUnits
  - uV
  - V*, volt
* - energyUnits
  - J
  - joule, J*, calorie
* - forceUnits
  - N
  - newton, N*
* - frequencyUnits
  - Hz
  - hertz, Hz*
* - intensityUnits
  - dB
  - dB*, candela, cd*
* - jerkUnits
  - m-per-s^3
  - m-per-s^3*
* - magneticFieldUnits
  - T
  - tesla, T*
* - memorySizeUnits
  - B
  - byte, B*
* - physicalLengthUnits
  - m
  - foot, inch, meter, metre, m*, mile
* - powerUnits
  - mW
  - watt, W*
* - pressureUnits
  - Pa
  - pascal, Pa*, mmHg*
* - resistanceUnits
  - kOhm
  - ohm, Ohm*
* - speedUnits
  - m-per-s
  - m-per-s*, mph*, kph*
* - temperatureUnits
  - degree-Celsius
  - degree-Celsius, degree Celsius (deprecated), oC*
* - timeUnits
  - s
  - second, s*, day, week, month, minute, hour, year
* - volumeUnits
  - m^3
  - m^3*, liter, litre, L*
* - weightUnits
  - g
  - g*, gram, pound, lb
```

The deprecated `degree Celsius` (`deprecatedFrom=8.2.0`) contains a blank and so predates the rule that unit names contain none; it cannot be written in an annotation. Use `degree-Celsius` or `oC`.

### A.1.2. Unit modifiers

A unit modifier can be applied to SI base units to indicate a multiple or sub-multiple of the unit. Unit symbols are modified by unit symbol modifiers, whereas SI units that are not unit symbols are modified by unit modifiers.

```{list-table} SI unit modifiers
---
widths: 20 20 50
header-rows: 1
---
* - Modifier
  - Symbol modifier
  - Description
* - deca
  - da
  - Multiple representing 10 to power 1
* - hecto
  - h
  - Multiple representing 10 to power 2
* - kilo
  - k
  - Multiple representing 10 to power 3
* - mega
  - M
  - Multiple representing 10 to power 6
* - giga
  - G
  - Multiple representing 10 to power 9
* - tera
  - T
  - Multiple representing 10 to power 12
* - peta
  - P
  - Multiple representing 10 to power 15
* - exa
  - E
  - Multiple representing 10 to power 18
* - zetta
  - Z
  - Multiple representing 10 to power 21
* - yotta
  - Y
  - Multiple representing 10 to power 24
* - deci
  - d
  - Submultiple representing 10 to power -1
* - centi
  - c
  - Submultiple representing 10 to power -2
* - milli
  - m
  - Submultiple representing 10 to power -3
* - micro
  - u
  - Submultiple representing 10 to power -6
* - nano
  - n
  - Submultiple representing 10 to power -9
* - pico
  - p
  - Submultiple representing 10 to power -12
* - femto
  - f
  - Submultiple representing 10 to power -15
* - atto
  - a
  - Submultiple representing 10 to power -18
* - zepto
  - z
  - Submultiple representing 10 to power -21
* - yocto
  - y
  - Submultiple representing 10 to power -24
```

### A.1.3. Value classes

HED has very strict rules about what characters are allowed in various elements of the HED schema, HED tags, and the substitutions made for `#` placeholders. These rules are encoded in the schema using value classes. When a node name extension or placeholder substitution is given a particular value class, that name or substituted value can only contain the characters allowed for by that value class.

```{Warning}
**Note**: A placeholder `#` specification without a unit class may include multiple value class attributes.

Tools check the value in question against the union of an element's `valueClass` allowed
characters and any additional characters allowed by a particular unit type.

```

The allowed characters for a value class are specified in the definition of each value class. The HED validator and other HED tools may hardcode information about behavior of certain value classes (for example the `numericClass` value class).

(value-class-character-table-anchor)=

```{list-table} Allowed characters for value classes.
---
widths: 20 50
header-rows: 1
---
* - Value class
  - Allowed characters
* - dateTimeClass
  - `digits`, `T`, `hyphen`, `colon`, `period`, `Z`, `plus`
* - nameClass
  - `letters`, `digits`, `hyphen`, `underscore`, `nonascii`
* - numericClass
  - `digits`, `E`, `e`, `plus`, `hyphen`, `period`
* - posixPath
  - `digits`, `letters`, `slash`, `colon`
* - textClass
  - `value-text`. See [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions).
```

See [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions) for the definitions of the character sets. The same values, with the earlier ones for older standard schemas, are the `value_class_defaults` section of [`character_sets.json`](_static/character_sets.json).

````{admonition} Notes on rules for allowed characters in the HED schema.
---
class: tip
---
1. Commas are not allowed in any values with the exception of
term descriptions, the prologue, and the epilogue in the HED schema and tsv column values
declared to be of type "list". The latter must be handled specially by tools.
2. A `dateTimeClass` value has the BIDS `Datetime` format, RFC 3339 with an optional offset:
"YYYY-MM-DDThh:mm:ss[.ffffff][Z|+hh:mm|-hh:mm]", with one to six fractional digits, hour 00-23, and seconds 00-60.
The regular expression, also the `value_class_words.dateTimeClass` entry of [`character_sets.json`](_static/character_sets.json), is:
```text
^[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])T(?:2[0-3]|[01][0-9]):[0-5][0-9]:(?:[0-5][0-9]|60)(?:\.[0-9]{1,6})?(?:Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$
```
3. The date must also exist in the Gregorian calendar (HED specification `4.0.0`): `2026-02-31` and `2027-02-29` are invalid, `2028-02-29` is valid.
The BIDS specification requires validators to reject such dates; HED validators check the calendar after the expression, for every schema version.
Other ISO 8601 forms (a date without a time, a space instead of `T`, lowercase `t` or `z`, `+hhmm`, basic format, week dates) are not valid.
NWB's `isodatetime` type accepts every value of this format.
4. The `nameClass` is for schema nodes.
5. Values of `numericClass` must be equivalent to a valid floating point value.
6. Scientific notation is supported with the `numericClass`.
7. The `textClass` is for descriptions, mainly for use with the `Description` tag. Its values use the `value-text` character set, so parentheses, the number sign, and the tilde may not appear in a value; they are structural characters of HED strings.
8. The `posixPath` class allows digits, letters, forward slash, and colon characters for POSIX path specifications.

````

### A.1.4. Schema attributes

The type of schema element that a schema attribute may apply to is indicated by its schema type property values. Tools hardcode processing based on the schema attribute name. Only the schema attributes listed in the following table can be handled by current HED tools.

```{list-table} Schema attributes.
---
widths: 21 15 12 40
header-rows: 1
---
* - Attribute
  - Domain
  - Range
  - Description
* - [`allowedCharacter`](#a141-allowedcharacter)
  - unit<br/>unit modifier<br/>value class
  - string
  - Specifies a character used in values of this class.
* - [`annotation`](#a142-annotation)
  - element
  - string
  - Annotation link to an item in another ontology.
* - [`conversionFactor`](#a143-conversionfactor)
  - unit<br/>unit modifier
  - numeric
  - Multiplicative factor to multiply by to convert to default units.
* - [`defaultUnits`](#a144-defaultunits)
  - unit class
  - unit
  - Specifies units to use if placeholder value has no units.
* - [`deprecatedFrom`](#a145-deprecatedfrom)
  - element
  - string
  - The latest schema version in which the element was not deprecated.
* - [`extensionAllowed`](#a146-extensionallowed)
  - node
  - boolean
  - Users can add unlimited levels of child nodes under this tag (`Item/Blech/Blech1/Blech2`). This tag is propagated to child nodes with the exception of the hashtag placeholders.
* - [`hedId`](#a147-hedid)
  - element
  - string
  - The unique identifier of this element in the HED namespace.
* - [`inLibrary`](#a148-inlibrary)
  - element
  - string
  - This schema element is from the named library schema, not the standard schema. (Added/removed by tools.)
* - [`isPartOf`](#a149-ispartof)
  - node
  - node
  - This tag is part of the indicated tag.
* - [`relatedTag`](#a1410-relatedtag)
  - node
  - node
  - A HED tag closely related to this HED tag.
* - [`requireChild`](#a1411-requirechild)
  - node
  - boolean
  - A child of this node must be included in the HED tag.
* - [`reserved`](#a1412-reserved)
  - node
  - boolean
  - This tag has special meaning and requires special handling by tools.
* - [`rooted`](#a1413-rooted)
  - node
  - node
  - A top-level library schema node should appear under this standard schema node when merged.
* - [`SIUnit`](#a1414-siunit)
  - unit
  - boolean
  - This unit represents an SI unit and can be modified.
* - [`SIUnitModifier`](#a1415-siunitmodifier)
  - unitModifier
  - boolean
  - Modifier applies to base units.
* - [`SIUnitSymbolModifier`](#a1416-siunitsymbolmodifier)
  - unitModifier
  - boolean
  - Modifier applies to unit symbols.
* - [`suggestedTag`](#a1417-suggestedtag)
  - node
  - node
  - Tag could be included with this HED tag.
* - [`tagGroup`](#a1418-taggroup)
  - node
  - boolean
  - Tag can only appear inside a tag group.
* - [`takesValue`](#a1419-takesvalue)
  - node
  - boolean
  - Placeholder (#) should be replaced by a value.
* - [`topLevelTagGroup`](#a1420-topleveltaggroup)
  - node
  - boolean
  - Tag (or its descendants) can be in a top-level tag group.
* - [`unique`](#a1421-unique)
  - node
  - boolean
  - Tag or its descendants can only occur once in an event-level HED string.
* - [`unitClass`](#a1422-unitclass)
  - node
  - unit class
  - The unit class that the value of a placeholder node can belong to.
* - [`unitPrefix`](#a1423-unitprefix)
  - unit
  - boolean
  - Unit is a prefix (e.g., $ in the currency units).
* - [`unitSymbol`](#a1424-unitsymbol)
  - unit
  - boolean
  - An abbreviation representing a unit.
* - [`valueClass`](#a1425-valueclass)
  - node
  - value class
  - Type of value taken on by the value of a placeholder node.
```

#### A.1.4.1. allowedCharacter

The `allowedCharacter` attribute specifies individual characters or character groups that are allowed in the values of a value class, or in the name of a unit or unit modifier that declares it (see [3.1.4. Schema layout overview](./03_HED_formats.md#314-schema-layout-overview)). This attribute determines what characters can be used when values are substituted for placeholders or when units are specified. Each allowed character should have a separate `allowedCharacter` attribute entry in the schema. The following group designations are allowed as shorthand values:

- `letters` designates upper and lower case alphabetic characters (A-Z, a-z).
- `blank` indicates a space character is allowed.
- `digits` indicates the digits 0-9 may be used in the value.
- `alphanumeric` indicates both `letters` and `digits`.

A name is a row of the table in [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions), an alias listed there (`slash` for `forward-slash`), or a single character, which names itself. Any other name is a schema error. The names a value class declares define the characters its values may contain.

For example, the `numericClass` value class includes `allowedCharacter` entries for `digits`, `E`, `e`, `+`, `-`, and `.` to support scientific notation and signed decimal numbers. The union of all `allowedCharacter` values for a value class defines the complete set of permissible characters.

#### A.1.4.2. annotation

The `annotation` attribute attaches a property from an external ontology or vocabulary to a HED schema element. The value has the form `prefix:id value` (HED specification `4.0.0`): `prefix:id` names a row of the External annotations section ([A.1.8. External annotations](#a18-external-annotations)), whose `prefix` is a row of the Prefixes section ([A.1.7. Schema prefixes](#a17-schema-prefixes)), and `value` is that property's value. For example, `rdfs:comment Should have this tag in every event process.` attaches a comment, and `dc:source Wikipedia` cites a source ([A.1.6. Schema sources](#a16-schema-sources) says what a `dc:source` value must name). A link from a schema element to a term in an external ontology uses a SKOS mapping property whose value is the external term in prefix notation: `skos:exactMatch ncit:C25499` states a high degree of confidence that the element and NCI Thesaurus term C25499 can be used interchangeably across a wide range of information retrieval applications, and `skos:closeMatch` that they are similar enough to be used interchangeably in some information retrieval applications. The value of a mapping property must be in prefix notation, and the prefix of the term (`ncit:`) must be a row of the Prefixes section; the term itself is not checked. An element may carry several `annotation` attributes. A value that breaks these rules is reported as a warning.

#### A.1.4.3. conversionFactor

The `conversionFactor` attribute of a unit is the factor by which a value expressed in that unit is multiplied to convert it to the default units of its unit class; the `conversionFactor` of a unit modifier is the factor the modifier contributes. This attribute was added to enable automatic unit conversion in tools and analyses. The attribute value must be a positive numeric value. For example, `minute` has `conversionFactor=60` because 2 minutes x 60 = 120 seconds, the default unit of `timeUnits`. A modifier's factor multiplies the unit's factor: `Duration/300 ms` converts as 300 x 0.001 (`m`) x 1.0 (`s`) = 0.3 s. For compound units the modifier factors are raised to the component exponents; see [3.1.4.5. Unit modifiers](./03_HED_formats.md#3145-unit-modifiers). When a unit has no `conversionFactor` (in HED `8.5.0`: `month`, `year`, `euro`, `point`, `candela`, `cd`), conversion to default units is undefined, and tools MUST NOT treat such a value as already being in default units. The exception for standard schema `8.0.0`, whose units carry no `conversionFactor`, is in [B.3. Differences for earlier schema versions](./Appendix_B.md#b3-differences-for-earlier-schema-versions). This attribute is particularly useful for units within the same physical dimension but with different scales (e.g., meters, feet, inches).

#### A.1.4.4. defaultUnits

The `defaultUnits` attribute specifies which unit should be assumed when a value is provided without explicit units for a placeholder that has a `unitClass` attribute. This attribute is applied to unit classes rather than individual tags. For example, the `timeUnits` class has the attribute `defaultUnits=s` (seconds). When a user provides a tag like `Duration/3` without units, tools interpret this as `Duration/3 s` because the `Duration` tag's `#` placeholder has `unitClass=timeUnits`, which has `defaultUnits=s`. This feature improves annotation convenience while maintaining unambiguous interpretation. The `defaultUnits` attribute does not affect the validation of annotation values, but may be used by downstream tools; the attribute value itself is checked during schema validation as described next. The value MAY be a derived form of a listed unit rather than a listed unit: HED `8.5.0` has `defaultUnits=mA` for `currentUnits`, which lists only `ampere` and `A`, and likewise `uV`, `mW`, and `kOhm`; tools resolve such a value with the same modifier rules as annotation units. A value that is neither a listed unit nor a derived form of one is an error, and a deprecated unit MUST NOT be the `defaultUnits` of a non-deprecated unit class.

#### A.1.4.5. deprecatedFrom

The `deprecatedFrom` attribute indicates that a schema element is deprecated (no longer recommended for use). Its value is the last released schema version in which the element was not deprecated; the element is deprecated in every later version. For example, `$` carries `deprecatedFrom=8.4.0` in HED `8.5.0`, and `degree Celsius` carries `deprecatedFrom=8.2.0` from `8.3.0` on. The attribute value must be a released semantic schema version that is earlier than the current schema version. Since `deprecatedFrom` can be applied to a schema element of any kind, to a schema attribute, and to a schema property, it provides a comprehensive deprecation mechanism. Deprecated elements remain in the schema for backward compatibility but are subject to strict usage rules:

- Deprecated tags cannot appear as values in `suggestedTag` or `relatedTag` attributes of non-deprecated tags.
- Deprecated schema attributes, units, unit modifiers, or value classes cannot be applied to non-deprecated elements.
- Child tags of deprecated tags must themselves be deprecated unless they are moved to a non-deprecated parent.

A validator issues a warning when an annotation uses a deprecated element (see [3.2. Annotation rules](./03_HED_formats.md#32-annotation-rules)).

#### A.1.4.6. extensionAllowed

The `extensionAllowed` attribute indicates that annotators may add unlimited levels of child nodes (extensions) under this tag without validation errors. This attribute enables domain-specific customization and extension of the HED vocabulary beyond the terms explicitly defined in the schema. When a tag has `extensionAllowed`, validators will accept any child path extensions provided they follow HED naming conventions. The attribute is typically propagated to child nodes in the schema, allowing extensions at any level of the subtree. However, nodes that have a placeholder (`#`) child cannot be extended, regardless of the `extensionAllowed` attribute, since the `#` placeholder indicates the node takes a user-supplied value rather than extended taxonomy terms. For example, if `Property` has `extensionAllowed`, then `Property/My-custom-property` is valid even though `My-custom-property` is not in the schema. An extension may have several levels: `Item/Blech/Blech1/Blech2` extends `Item` by three terms, each subject to the rules of [3.2.5. Tag extensions](./03_HED_formats.md#325-tag-extensions).

#### A.1.4.7. hedId

The `hedId` attribute provides a unique identifier for each HED entity in the HED namespace. This identifier remains stable across schema versions and is used to track entities when names change or entities are restructured. The `hedId` format follows a structured pattern (e.g., `HED_0012001`) that categorizes entities by kind. These identifiers are essential for maintaining references to HED entities in ontologies, linked data representations, and cross-version mappings. Tools use `hedId` values to maintain consistency when schemas evolve.

A `hedId` value is the prefix `HED_` followed by a 7 digit integer. The standard schema occupies an ID range [0010000, 0039999]. Each library schema is assigned its own range of 20000 identifiers when the library is officially created. The assignment list is kept in the [library_data.json](https://raw.githubusercontent.com/hed-standard/hed-schemas/refs/heads/main/library_data.json) file in the [hed-standard/hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository. The base ontology has its own ID range. Identifiers are assigned when a schema is released, after Working Group review; new entities in a prerelease carry none. Identifiers are never reused: an identifier whose entity is removed from a released schema, or one that a prerelease carried and the release withdrew, is recorded under `retired_ids` in the same `library_data.json` file (see [8.3.1. Schema namespaces versus the ontology namespace](./08_HED_ontology.md#831-schema-namespaces-versus-the-ontology-namespace)). For more information, see the section [8.3.2 Ontology Namespace](./08_HED_ontology.md#832-ontology-namespace).

#### A.1.4.8. inLibrary

The `inLibrary` attribute indicates that a schema element or schema attribute originates from a named library schema rather than the standard schema. The attribute value is the library name in lowercase (e.g., `inLibrary=mouse`). This attribute is automatically added by tools during the schema merging process when a partnered library schema is merged with a standard schema. In unmerged library schemas, nodes cannot have the `inLibrary` attribute. The attribute helps tools and validators track the provenance of schema elements when multiple schemas are combined and ensures proper validation against the original library schema definitions. Users should not manually add this attribute to the schema as it is managed automatically by tools. Because `inLibrary` is bookkeeping, it is excluded from the element compatibility comparisons of [3.1.2.4](./03_HED_formats.md#3124-partnered-combinations): an element contributed by more than one library schema of a merge group carries a different `inLibrary` value in each library's merged schema, and the merged result retains one `inLibrary` value for each contributing library. The attribute also marks the rows that a library contributes to the Sources, Prefixes, and External annotations sections of a merged schema (see [3.1.2.2. Merged vs unmerged](./03_HED_formats.md#3122-merged-vs-unmerged)).

#### A.1.4.9. isPartOf

The `isPartOf` attribute indicates a hierarchical or compositional relationship where the current tag is semantically considered part of another tag. This attribute helps define ontological relationships beyond the structural hierarchy of the schema tree. The value of `isPartOf` must be a valid node in the schema. This relationship can be used by tools for semantic reasoning and for identifying related concepts that may not share a direct parent-child relationship in the schema tree structure.

#### A.1.4.10. relatedTag

The `relatedTag` attribute specifies a HED tag that is closely related to the current tag. The value must be an existing valid tag in the schema. This attribute helps tagging tools provide context and suggestions to users by identifying semantically related concepts. For example, tags describing related sensory modalities or complementary experimental conditions might reference each other. A tag cannot have `relatedTag` values that reference deprecated tags. The relationship is informational and does not impose validation constraints on annotations.

#### A.1.4.11. requireChild

The `requireChild` attribute indicates that a tag must have at least one child tag when used in an annotation. This attribute enforces structural requirements to ensure annotations are sufficiently specific. For example, a general category tag with `requireChild` cannot be used alone; users must select a more specific descendant. If a tag with the `requireChild` attribute appears without a child in an annotation, an error is generated. This attribute helps maintain annotation quality by preventing overly generic tags from being used when more specific information is required. The `requireChild` attribute is also used for certain tags with placeholder children, such as `Delay`, which are not meaningful without a value.

#### A.1.4.12. reserved

The `reserved` attribute indicates that a tag has a specified meaning in the HED ecosystem and cannot be redefined by individual HED schemas. The nine structural reserved tags (`Definition`, `Def`, `Def-expand`, `Onset`, `Offset`, `Inset`, `Delay`, `Duration`, and `Event-context`) determine the structure of an annotation; their validation rules are given in [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags) and in the machine-readable file `reserved_tags.json` that validators load. The other reserved tags carry no validation rule beyond their schema attributes and are defined for specific uses by downstream tools: `Condition-variable` and `Task` already have defined behavior, and the other reserved tags are expected to have defined behavior in the future. See the [Reserved tag](./02_Terminology.md#reserved-tag) entry in Chapter 2. The attribute can only appear in standard schemas: a library schema MUST NOT carry it on its own elements (those with `inLibrary` in a merged partnered library schema), MUST NOT define a tag with a reserved name, and MUST NOT root a node under a reserved tag. A reserved tag has no child node other than `#`, and a standard schema MUST define the tags that `reserved_tags.json` names.

#### A.1.4.13. rooted

The `rooted` attribute specifies where a library schema node should be placed in the standard schema hierarchy during the merging process. The attribute value (e.g., `rooted=Statistical-value`) must be a valid node name in the partnered standard schema. In an unmerged library schema, nodes with the `rooted` attribute must be top-level tags. During merging, these nodes are relocated to appear directly under the specified standard schema node, allowing library-specific terms to be integrated into the appropriate standard schema hierarchy. This mechanism enables library schemas to extend standard schema branches logically while maintaining separate development and versioning.

#### A.1.4.14. SIUnit

The `SIUnit` attribute indicates that a unit is an International System of Units (SI) unit and can be modified with SI unit prefixes (multiples and sub-multiples). Units with this attribute can be combined with modifiers like `kilo`, `mega`, `milli`, `micro`, etc. If a unit has the `SIUnit` attribute but not the `unitSymbol` attribute, it is modified using `SIUnitModifier` modifiers (e.g., `second` can become `kilosecond`, `millisecond`). If a unit has both `SIUnit` and `unitSymbol` attributes, it is modified using `SIUnitSymbolModifier` modifiers instead (e.g., `s` becomes `ks`, `ms`). A compound unit such as `m-per-s^2` with `SIUnit` takes one modifier on each component; see [3.1.4.5. Unit modifiers](./03_HED_formats.md#3145-unit-modifiers). The attribute enables consistent expression of scaled measurements.

#### A.1.4.15. SIUnitModifier

The `SIUnitModifier` attribute identifies a unit modifier that can be applied to SI base units (those with the `SIUnit` attribute but not the `unitSymbol` attribute). These modifiers represent powers of 10 for scaling units and include prefixes like `kilo` (10^3), `mega` (10^6), `milli` (10^-3), and `micro` (10^-6). For example, the modifier `kilo` with `SIUnitModifier` can be applied to `second` to create `kilosecond`. These modifiers can be pluralized following standard English rules, so both `kiloseconds` and `kilosecond` are valid. SI unit modifiers must only appear in the unit modifier section of the schema.

#### A.1.4.16. SIUnitSymbolModifier

The `SIUnitSymbolModifier` attribute identifies a unit modifier that can be applied to SI unit symbols (units with both `SIUnit` and `unitSymbol` attributes). These are single-letter or abbreviated prefix symbols such as `k` (kilo), `M` (mega), `m` (milli), and `u` (micro). For example, the modifier `k` can be applied to the unit symbol `s` to create `ks` (kiloseconds). Like all unit modifiers, symbol modifiers are case-sensitive (`M` for mega vs. `m` for milli). A unit symbol with a modifier cannot be pluralized. Unit symbol modifiers must only appear in the unit modifier section of the schema.

#### A.1.4.17. suggestedTag

The `suggestedTag` attribute specifies one or more HED tags that tagging tools might suggest to users when the current tag is used. The attribute values must be valid existing tags in the schema (or in the merged schema for partnered library schemas). This attribute is intended to help annotators by prompting them to consider related tags that often co-occur or provide complementary information. For example, a sensory event tag might suggest task-related tags. Suggested tags are informational hints for tools and do not impose validation requirements. A tag cannot use deprecated tags as `suggestedTag` values.

#### A.1.4.18. tagGroup

The `tagGroup` attribute indicates that a tag must appear within a tag group (enclosed in parentheses) and cannot be used as a standalone tag. This attribute enforces structural requirements for tags that only make sense in association with other tags. For example, temporal offset tags or relational tags might require grouping to establish their context. If a tag with the `tagGroup` attribute appears outside parentheses, an error is generated. This attribute ensures proper semantic grouping and prevents tags from being used in isolation when their meaning depends on association.

#### A.1.4.19. takesValue

The `takesValue` attribute indicates that a node represents a placeholder (`#`) that must be replaced by a user-defined value during annotation. This attribute can only be applied to `#` placeholder nodes. The value that replaces the placeholder must conform to any `valueClass` restrictions (e.g., `numericClass`, `textClass`, `dateTimeClass`) and, if a `unitClass` is specified, may include valid units from that class. Tags with `takesValue` provide a mechanism for annotators to specify measurements, labels, identifiers, and other variable information. The actual schema node that is the parent of the `#` placeholder is said to "take a value."

#### A.1.4.20. topLevelTagGroup

The `topLevelTagGroup` attribute indicates that a tag must appear in a top-level tag group (not nested within other groups) in an assembled HED annotation. Only one tag with the `topLevelTagGroup` attribute may appear in the same top-level group, except that `Delay` may share a group with `Onset`, `Offset`, `Inset`, or `Duration` (see [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags)). This attribute is typically associated with tags that have special structural meaning, such as `Definition`, `Onset`, `Offset`, `Inset`, and `Event-context`. The restriction to top-level groups ensures these structural elements are properly positioned for tool processing and prevents nested definitions or temporal event structures.

#### A.1.4.21. unique

The `unique` attribute indicates that a tag or its descendants can appear only once in a HED string. This constraint is checked after all definitions are expanded and column-based annotations are assembled into a complete event annotation. If a tag with the `unique` attribute appears multiple times, an error is generated. `Event-context` is the only tag that has the `unique` attribute.

#### A.1.4.22. unitClass

The `unitClass` attribute specifies which unit class the value of a placeholder (`#`) node can belong to. The attribute value must be exactly one valid unit class defined in the schema (e.g., `timeUnits`, `physicalLengthUnits`, `frequencyUnits`); a placeholder MUST NOT have more than one unit class, and a placeholder with a unit class MUST have `valueClass=numericClass` (specification `4.0.0`). The value MAY be the pseudo unit class `anyUnits`, which makes the placeholder accept a unit from any unit class of the schema. When a `unitClass` is specified, the value substituted for the placeholder may include units from that class, and validators will check that any units provided are valid members of the specified unit class. If the replacement value has no units and the unit class has `defaultUnits` defined, tools may assume those default units. The `unitClass` attribute can only be applied to `#` placeholder nodes.

#### A.1.4.23. unitPrefix

The `unitPrefix` attribute indicates that a unit appears before its corresponding value rather than after it in annotations. Most units in HED appear after their values (e.g., `3 s`, `5 meters`), but certain units like currency symbols conventionally precede values (e.g., `$ 50`). Units with the `unitPrefix` attribute follow this reversed ordering convention. HED parsers recognize these prefix units and handle them appropriately during validation and processing. Even though prefix units appear before values, they are still separated from the value by a single space. The `unitPrefix` attribute and the only unit that carries it, `$`, are deprecated and MUST NOT be used in new schemas; currency is written with the unit name, as in `5 dollars`. Prefix units will be removed in a future major version.

#### A.1.4.24. unitSymbol

The `unitSymbol` attribute indicates that a unit represents an abbreviated symbolic form rather than a full unit name. Unit symbols are typically single letters or short abbreviations (e.g., `s` for second, `m` for meter, `Hz` for hertz) and follow international conventions. Unit symbols are case-sensitive and cannot be pluralized. When a unit has both the `SIUnit` and `unitSymbol` attributes, it can only be modified with `SIUnitSymbolModifier` modifiers (not `SIUnitModifier` modifiers). Unit symbols without the `SIUnit` attribute remain unmodifiable by SI prefixes.

#### A.1.4.25. valueClass

The `valueClass` attribute specifies the type of value that can be substituted for a placeholder (`#`) node. The attribute value must be a valid value class defined in the schema (e.g., `numericClass`, `textClass`, `nameClass`, `dateTimeClass`, `posixPath`). Each value class defines a set of allowed characters and format requirements. Multiple `valueClass` attributes may be applied to a placeholder that has no unit class (see [3.1.4.4. Unit classes and units](./03_HED_formats.md#3144-unit-classes-and-units)), and tools validate the substituted value against the union of allowed characters from all specified value classes. If no `valueClass` is specified, the placeholder is assumed to take `textClass` values. The `valueClass` attribute can only be applied to `#` placeholder nodes.

#### A.1.4.x. Deprecated attributes

In addition to the attributes listed above, some schema attributes have been deprecated and are no longer supported in HED. The following table lists these.

```{list-table} Schema attributes deprecated.
---
widths: 20 15 45
header-rows: 1
---
* - Schema attribute
  - Target
  - Description
* - `default`
  - node
  - A default value used if no value is provided.
* - `position`
  - node
  - Indicates where this tag should appear during display.
* - `predicateType`
  - node
  - Indicates the relationship of the node to its parent.
* - `recommended`
  - node
  - Event-level HED strings should include this tag.
* - `required`
  - node
  - Event-level HED string must include this tag.
```

The `default` attribute was not implemented in existing tools. Only the `defaultUnits` for the unit class will be implemented going forward.

The `position` attribute was used to assist annotation tools, which sought to display required and recommended tags before others. The position attribute value is an integer and the order can start at 0 or 1. Required or recommended tags without this attribute or with negative position were to be shown after the others in canonical ordering. The tagging strategy of HED using decomposition and definitions does not permit this type of ordering. The `position` attribute is not used.

The `predicateType` attribute was introduced in HED-2G to facilitate mapping to OWL or RDF. It was needed because the HED-2G schema had a mixture of children that were properties and subclasses. The possible values of `predicateType` were `propertyOf`, `subclassOf`, or `passThrough` to indicate which role each child node had with respect to its parent. The parent-child relationship MUST be `subclassOf` to allow search generality. The attribute is ignored by tools.

### A.1.5. Schema properties

**The schema properties are qualifiers on the domains and ranges of schema attributes.** A property's presence implies the attribute has this property, while its absence implies it does not. Processing of `property` elements is hard-coded into the schema processors. The following is a list of the schema properties.

```{list-table} Summary of schema properties.
---
widths: 20 50
header-rows: 1
---
* - Property
  - Description
* - `annotationProperty`
  - This schema attribute is NOT inherited.<br/>Replaces `isInheritedProperty`.
* - `boolRange`
  - This schema attribute's value can be true or false.<br/>This property was formerly named `boolProperty`.
* - `elementDomain`
  - This schema attribute can apply to any type<br/>of element (tag term, unit class, etc).<br/>This property was formerly named `elementProperty`.
* - `isInheritedProperty`
  - **Deprecated** in favor of `annotationProperty`.<br/>This schema attribute is inherited by child nodes.<br/>This property only applies to schema attributes for nodes.
* - `tagDomain`
  - This schema attribute can apply to node (tag-term) elements.<br/>This was added so attributes could apply to multiple types of elements.<br/>This property was formerly named `nodeProperty`.
* - `tagRange`
  - This schema attribute's value can be a node.
* - `numericRange`
  - This schema attribute's value can be numeric.
* - `stringRange`
  - This schema attribute's value can be a string.
* - `unitClassDomain`
  - This schema attribute can apply to unit classes.<br/>This property was formerly named `unitClassProperty`.
* - `unitClassRange`
  - This schema attribute's value can be a unit class.
* - `unitModifierDomain`
  - This schema attribute can apply to unit modifiers.<br/>This property was formerly named `unitModifierProperty`.
* - `unitDomain`
  - This schema attribute can apply to units.<br/>This property was formerly named `unitProperty`.
* - `unitRange`
  - This schema attribute's value can be units.
* - `valueClassDomain`
  - This schema attribute can apply to value classes.<br/>This property was formerly named `valueClassProperty`.
* - `valueClassRange`
  - This schema attribute's value can be a value class.
```

Property names ending in `Range` designate the type of value a schema attribute has.

Property names ending in `Domain` indicate the type of schema element that a schema attribute applies to.

```{admonition} Format for schema attributes with schema property values.
---
class: tip
---
**Attributes with boolean range** (`boolRange`):
  - In `.xml` the attribute appears as a `<name>` element with the property's name but no
`<value>` in an `<attribute>` section of the schema element.
  - In `.mediawiki`, the attribute name appears in curly braces in the element's specification line.
  - In either case presence of the property indicates true, and absence indicates false.
<p></p>

**Schema without a boolean range**:
  - In `.xml`, the attribute appears with both `<name>` and `<value>` in an `<attribute>` section of the schema element.
  - In `.mediawiki`, the schema element has the `{name =value}` in the element's specification line.
  - These schema attributes may appear multiple times in an element with different values if appropriate.

```

See [property example](#a255-schema-properties) for an example in MediaWiki format.

### A.1.6. Schema sources

The schema sources section provides references to external resources used during schema development or that provide background information for schema terms. Each schema source entry includes a name, a link (URL), and a description of how the source was used or its relevance to the schema.

Schema sources serve as documentation and attribution for the intellectual sources that informed the schema design. For example, the HED standard schema typically includes Wikipedia as a source, since many term descriptions and conceptual definitions are informed by or adapted from Wikipedia definitions. Other sources might include published ontologies, scientific literature, or technical standards documents.

Schema sources are the targets of `dc:source` annotations ([A.1.4.2. annotation](#a142-annotation)). The value of a `dc:source` annotation names a source when it begins with a row's `source` name, or contains a URL that begins with a row's `link` (compared without the scheme and without a trailing slash); any other text, such as "Adapted from", is free. A `dc:source` value that names no row is reported as a warning. The rows of a partnered library's standard schema count as the library's own. Each source has three required components (an empty component is reported as a warning):

- **`source`**: A short identifier for the source (e.g., "Wikipedia", "NCIT")
- **`link`**: A URL pointing to the source resource
- **`description`**: A brief explanation of how the source was used or its relevance

The section is required in every schema (see [3.1.4.10. Sources, prefixes, and external annotations](./03_HED_formats.md#31410-sources-prefixes-and-external-annotations)). The names that each file format gives these components are in [A.2.5.7. Schema sources](#a257-schema-sources) (MediaWiki), [A.3.5.7. Schema sources](#a357-schema-sources) (XML), [A.4.5.6. Schema sources](#a456-schema-sources) (JSON), and [A.5.11.1. Sources file](#a5111-sources-file) (TSV).

### A.1.7. Schema prefixes

The schema prefixes section defines the prefixes used for linking HED schema elements to external ontologies and controlled vocabularies. These prefixes are not the namespace prefixes of tags (see [Namespace prefix](./02_Terminology.md#namespace-prefix)). Each prefix entry associates a short prefix string (e.g., `dc:`, `ncit:`, `owl:`) with its full namespace IRI and provides a description of the ontology or vocabulary it represents.

Schema prefixes are essential for the `annotation` schema attribute, which uses prefix notation to create links between HED elements and external ontology terms. For example, the annotation `skos:exactMatch ncit:C25499` uses the `skos:` prefix for the mapping property and the `ncit:` prefix to reference term C25499 in the NCI Thesaurus. Without the prefix definition, tools cannot resolve these references to their full IRIs.

Each prefix entry has three required components (an empty component is reported as a warning):

- **`prefix`**: The prefix string including the colon separator (e.g., `dc:`, `foaf:`, `rdfs:`)
- **`namespace`**: The full IRI or URL for the ontology namespace
- **`description`**: A brief description of the ontology or vocabulary, often including standard references

Common prefixes in HED schemas include Dublin Core (`dc:`), RDF Schema (`rdfs:`), OWL (`owl:`), Friend-of-a-Friend (`foaf:`), and domain-specific ontologies like NCI Thesaurus (`ncit:`) and the Gene Ontology (`obogo:`). The schema prefixes enable HED to participate in the broader linked data ecosystem and support semantic web applications.

The section is required in every schema (see [3.1.4.10. Sources, prefixes, and external annotations](./03_HED_formats.md#31410-sources-prefixes-and-external-annotations)). The prefixes are used in `annotation` attribute values. A library schema may add rows of its own to this section; [3.1.2.2. Merged vs unmerged](./03_HED_formats.md#3122-merged-vs-unmerged) says how they are combined with the rows of its standard schema partner.

### A.1.8. External annotations

The external annotations section defines specific annotation properties that can be used to attach metadata to HED schema elements. Each external annotation entry specifies a property from an external ontology or vocabulary that is recognized for schema documentation and integration purposes.

External annotations extend beyond the HED schema's internal structure to enable rich metadata using standard ontology properties. For example, Dublin Core properties like `dc:creator`, `dc:contributor`, and `dc:date` can be used to document authorship and provenance. Properties from the PROV ontology (`prov:`) support detailed provenance tracking. The Friend-of-a-Friend vocabulary (`foaf:`) enables linking to personal and organizational homepages.

Each external annotation entry has four required components (an empty component is reported as a warning):

- **`prefix`**: The prefix identifying the ontology (must match a defined schema prefix)
- **`id`**: The local identifier for the property within its namespace
- **`iri`**: The full internationalized resource identifier for the property
- **`description`**: A clear explanation of the property's meaning and intended use

External annotations serve multiple purposes:

1. **Documentation**: Properties like `dc:description` and `dc:title` provide standardized ways to document schema elements
2. **Provenance**: Properties like `dc:creator`, `dc:contributor`, and `dc:date` track authorship and version history
3. **Cross-references**: The SKOS mapping properties `skos:exactMatch` and `skos:closeMatch` link a schema element to a term in an external ontology, and properties like `obogo:has_dbxref` enable systematic cross-referencing with external databases
4. **Licensing**: Properties like `terms:license` formally declare usage rights

The external annotations section works in conjunction with the schema prefixes section. Each annotation must use a prefix that is defined in the schema prefixes section. Tools can use external annotations to generate rich metadata, export schemas to RDF/OWL formats, and integrate HED with broader ontology frameworks.

The section is required in every schema (see [3.1.4.10. Sources, prefixes, and external annotations](./03_HED_formats.md#31410-sources-prefixes-and-external-annotations)).

## A.2. MediaWiki file format

[MediaWiki](https://www.mediawiki.org/wiki/Cheatsheet) is a markdown-like format that was selected as the HED schema editing format because of its flexibility and ability to represent nested or hierarchical relationships. The rules for creating a valid `.mediawiki` specification of a HED schema are given below. The format is line-oriented, meaning that all information about an individual entity should be on a single line. Empty lines and lines containing only blanks are ignored.

### A.2.1. Overall file layout

````{admonition} Overall layout of a HED MEDIAWIKI schema file.

```moin
header
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
epilogue
sources
prefixes
external-annotations
!# end hed
```
````

Every section in this layout is present in every file. A section with no entries consists of its section header alone. For example, the end of an unmerged library schema that adds no sources, prefixes, or external annotations of its own is:

````{admonition} Empty extra sections at the end of a MEDIAWIKI schema file.

```moin
'''Epilogue'''
             . . .
'''Sources'''
'''Prefixes'''
'''External annotations'''
!# end hed
```
````

The format has no closing markers: a section ends where the next section separator (`!#`) or the next section header in triple single quotes (`'''`) begins.

The following example shows a small but complete HED schema in `.mediawiki` format.

````{admonition} **Example:** Example HED schema in .mediawiki format.

```moin
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
This epilogue is a place for notes and is ignored in HED processing.

'''Sources'''
'''Prefixes'''
'''External annotations'''
!# end hed
```

````

In the above example, `Property` in the `schema` section is a top node because it appears enclosed by three single quotes, while `Informational-property` is a first-level node because its defining line begins with a single asterisk (`*`).

`Sensory-event` in the `schema` section has a `suggestedTag` attribute (shown in curly braces). Similarly, `Property` has an `extensionAllowed` attribute, and the `#` placeholder has a `takesValue` attribute. The `schema attributes` section must include definitions of `suggestedTag`, `extensionAllowed` and `takesValue` or the schema will not validate.

The definition of the `takesValue` attribute has `boolRange`, so a definition of `boolRange` must be included in the `Properties` section or the schema will not validate.

### A.2.2. MediaWiki header

The first line of the `.mediawiki` file should be a _header_ that starts with the keyword `HED` followed by a blank-separated list of name-value pairs.

```{eval-rst}
.. list-table:: Allowed HED schema header parameters
   :header-rows: 1
   :widths: 15 15 50

   * - Name
     - Level
     - Description
   * - library
     - optional
     - |
       | Name of library used in XML filenames.
       | The value should only have lowercase alphabetic characters.
   * - version
     - required
     - A valid semantic version number of the schema.
   * - xmlns
     - optional
     - xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance".
   * - xsi
     - optional
     - xsi:noNamespaceSchemaLocation points to an XSD file.
   * - withStandard
     - optional
     - |
       | The version of the standard schema partner
       | if this is a partnered library schema.
   * - unmerged
     - optional
     - |
       | If true, this is an unmerged partnered library schema.
       | If omitted, assumed false.
```

The following example gives a sample *header* for standard schema version `8.0.0` in `.mediawiki` format.

````{admonition} **Example:** Sample *header* for version 8.0.0 in .mediawiki format.

```moin
HED version="8.0.0"
```
````

The schema `.mediawiki` file specified in this example is named `HED8.0.0.mediawiki` and can be found in the [standard_schema/hedwiki](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedwiki) directory of the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

The versions of the schema that use XSD validation to verify the format have `xmlns:xsi` and `xsi:noNamespaceSchemaLocation` attributes. The `xsi` attribute is required if `xmlns:xsi` is given. The [XSD file](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/hedxml/HED8.4.0.xsd) allows validators to check the format of the `.xml` using standard XML validators; `HED8.4.0.xsd` is the latest. It declares `version` as the only attribute of the header, so it applies to standard schemas. The released library schemas do not reference an XSD file.

The following example shows a sample *header* for the unpartnered `score` library schema version `1.0.0` in `.mediawiki` format. Almost all library schemas going forward will be partnered; SCORE `1.0.0` is historical, but it is the only unpartnered library schema that has been released.

````{admonition} **Example:** Sample *header* for score library version 1.0.0 in .mediawiki format.

```moin
HED library="score" version="1.0.0"
```
````

The `library` and `version` values are used to form the official filename `HED_score_1.0.0.mediawiki`. The file is found in [library_schemas/score/hedwiki](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/score/hedwiki) directory of the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

An unknown header attribute is ignored when the schema is loaded and is an error in schema validation (see [3.1.4.1. The header](./03_HED_formats.md#3141-the-header)).

### A.2.3. MediaWiki prologue and epilogue

The prologue is a paragraph of text appearing after the *header*; the section is always present and may be empty. The prologue is used by tools for help and display purposes.

The epilogue is described in [Section A.2.5.6](#a256-epilogue) as part of the auxiliary sections that appear after the main schema specification.

Both the prologue and epilogue may contain new lines and commas in addition to the characters of the `text` character set ([2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions)).

### A.2.4. MediaWiki schema section

The beginning of the actual specification of the HED vocabulary is marked by the *start-line*:

```moin
!# start schema
```

The end of the main HED-specification is marked by the *end-line*:

```moin
!# end schema
```

A section separator is a line starting with `!#`. The section separator lines (`!# start schema`, `!# end schema`, `!# end hed`) must only appear once in the file and must appear in that order within the file.

The body of the HED specification is located between the `!# start schema` and `!# end schema` section separators. Each specification is a single line in the `.mediawiki` file.

The three types of lines in the main specification section are **top-nodes**, **normal-nodes**, and **placeholders**, respectively.

Empty lines or lines containing only blanks are ignored.

The basic format for a node-specification is:

```moin
node-name  <nowiki>{attributes}[description]</nowiki>
```

Top node names are enclosed in triple single quotes (e.g., `'''Event'''`), while other types of nodes have at least one preceding asterisk (\*) followed by a blank and then the name.

The number of asterisks indicates the level of the node in the subtree. The attributes are in curly braces (`{ }`) and the description is in square brackets (`[ ]`).

A schema attribute that has the `boolRange` property appears as its name alone; its presence indicates that it is true. Any other schema attribute is written as a `name=value` pair. An attribute that has several values is written as several `name=value` pairs. The entries within the curly braces are separated by commas.

The characters allowed in a node name are given in [3.1.4.3. The schema section](./03_HED_formats.md#3143-the-schema-section). Node names cannot contain blanks and must be unique.

For top nodes and normal nodes, everything after the node name must be contained within `<nowiki></nowiki>` tags. The `#` is included within the `<nowiki></nowiki>` tags in placeholder nodes.

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
****** <nowiki># {takesValue, valueClass=numericClass, unitClass=timeUnits}</nowiki>
```
````

The `Duration` tag of this example is at the fifth level below the root (top node) of its subtree. The tag: `Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/Duration` is the long form. The placeholder in the example is the node directly below `Duration` in the hierarchy.

In an unmerged partnered library schema, a node with the `rooted` attribute is a top node; in the merged schema it is placed directly under the standard schema node that the attribute names, so the number of asterisks of the node and of its descendants changes. The following excerpt from the unmerged MOUSE library schema `1.0.0` shows a library schema node (`Fore-limb-part`) rooted to `Body-part` in the standard schema.

````{admonition} Example of a rooted node in an unmerged schema in MediaWiki format.
```moin
                      . . .
'''Fore-limb-part''' <nowiki>{rooted=Body-part, hedId=HED_0102006} [A part of the fore-limb.]</nowiki>
* Manus <nowiki>{hedId=HED_0102007} [The distal segment of the fore-limb, homologous to the hand.]</nowiki>
                      . . .
```
````

The single `*` in front of `Manus` indicates that this element is directly below its top-level ancestor (`'''Fore-limb-part'''`). In the merged schema, `Fore-limb-part` is one level below the `Body-part` tag of the standard schema, which is three levels below its top-level ancestor (`'''Item'''`):

````{admonition} When a library is merged with the standard schema, the indentation levels are adjusted.
```moin
                      . . .
*** Body-part <nowiki>{hedId=HED_0012175} [Any part of an organism.]</nowiki>
**** Fore-limb <nowiki>{rooted=Body-part, hedId=HED_0102005, inLibrary=mouse} [Either of the front pair of limbs in a quadruped.]</nowiki>
**** Fore-limb-part <nowiki>{rooted=Body-part, hedId=HED_0102006, inLibrary=mouse} [A part of the fore-limb.]</nowiki>
***** Manus <nowiki>{hedId=HED_0102007, inLibrary=mouse} [The distal segment of the fore-limb, homologous to the hand.]</nowiki>
                      . . .
**** Head-part <nowiki>{hedId=HED_0013200} [A part of the head.]</nowiki>
                      . . .
```
````

### A.2.5. MediaWiki auxiliary sections

After the line marking the end of the schema (`!# end schema`), the `.mediawiki` file contains the unit class definitions, unit modifier definitions, value class definitions, schema attribute definitions, property definitions, epilogue, schema sources, schema prefixes, and external annotations sections, in that order. Every section is present; a section with no entries consists of its header alone.

#### A.2.5.1. Unit classes and units

Unit classes specify the types of units allowed to be used with a value substituted for a `#` placeholder.

The unit class specification section starts with `'''Unit classes'''` and lists the types of units (the unit classes) at the first level and the specific units corresponding to those unit classes at the second level.

````{admonition} **Example:** Part of the HED unit class for time in .mediawiki format.

```moin
'''Unit classes'''
* timeUnits <nowiki>{defaultUnits=s}</nowiki>
** second <nowiki>{SIUnit}</nowiki>
** s <nowiki>{SIUnit, unitSymbol}</nowiki>
```
````

#### A.2.5.2. Unit modifiers

The SI units can be modified by SI (International System Units) sub-multiples and multiples. All unit modifiers are at level 1 of the `.mediawiki` file.

````{admonition} **Example:** Part of the HED unit modifier in .mediawiki format.

```moin
'''Unit modifiers'''
* deca <nowiki>{SIUnitModifier, conversionFactor=10.0} [SI unit multiple representing 10^1.]</nowiki>
* da <nowiki>{SIUnitSymbolModifier, conversionFactor=10.0} [SI unit multiple representing 10^1.]</nowiki>
```
````

A unit must have the `SIUnit` attribute in order to be used with modifiers. If the unit has both the `SIUnit` and `unitSymbol` attributes, then it only can be used with `SIUnitSymbolModifier` modifiers. If the unit has only the `SIUnit` attribute, then it only can be used with the `SIUnitModifier`.

For example the unit `second` is an `SIUnit` but not a symbol, so `second`, `seconds`, `decasecond` and `decaseconds` are all valid units.

The unit `s` is both a `SIUnit` and a `unitSymbol`, so `s` and `das` are valid units. Note that rules about pluralization do not apply to unit symbols.

#### A.2.5.3. Value classes

Value classes give rules about what kind of value is allowed to be substituted for `#` placeholder tags.

````{admonition} **Example:** Part of the HED value class for date-time in .mediawiki format.

```moin
'''Value classes'''
* dateTimeClass <nowiki>{allowedCharacter=digits, allowedCharacter=T, allowedCharacter=hyphen, allowedCharacter=colon, allowedCharacter=period, allowedCharacter=Z, allowedCharacter=plus} [Date-times conform to the BIDS Datetime format, RFC 3339 with an optional offset: YYYY-MM-DDThh:mm:ss (year, month, day, hour (24h), minute, second), an optional fraction of one to six digits, and an optional Z for UTC or a +hh:mm or -hh:mm offset.]</nowiki>
```
````

#### A.2.5.4. Schema attributes

The schema attributes specify other characteristics about how particular tags may be used in annotation. These attributes allow validators and other tools to process tag strings based on the HED schema specification, thus avoiding hard-coding particular behavior.

````{admonition} **Example:** HED schema attributes allowedCharacter and extensionAllowed in .mediawiki format.

```moin
'''Schema attributes'''
* allowedCharacter <nowiki>{unitDomain, unitModifierDomain, valueClassDomain, stringRange} [A special character that is allowed in expressing the value of a placeholder of a specified value class.]</nowiki>
* extensionAllowed <nowiki>{tagDomain, boolRange}[This tag may be extended by user-defined terms.]</nowiki>
```
````

The schema attributes, themselves, have attributes referred to as *schema properties*. These schema properties are listed in the `Properties` section of the schema. The example indicates that `allowedCharacter` is associated with units, unit modifiers, and value classes (via `unitDomain`, `unitModifierDomain`, and `valueClassDomain`), while `extensionAllowed` applies to tags (via `tagDomain`).

#### A.2.5.5. Schema properties

Properties apply only to schema attributes. The following example defines the `valueClassDomain` property in `.mediawiki` format.

````{admonition} **Example:** HED schema property valueClassDomain in .mediawiki format.

```moin
'''Properties'''
* valueClassDomain <nowiki>{hedId=HED_0010713} [This schema attribute can apply to value classes. This property was formerly named valueClassProperty.]</nowiki>
```
````

See [Schema properties](#a15-schema-properties) for a list of available schema properties.

#### A.2.5.6. Epilogue

The epilogue section is marked by `'''Epilogue'''` and contains a text block with information about the schema license, attribution, and other metadata. The epilogue text appears on lines following the header without any special formatting markers. The epilogue may contain new lines, commas, and the characters of the `text` character set, which includes non-ASCII characters.

````{admonition} **Example:** HED schema epilogue in .mediawiki format.

```moin
'''Epilogue'''
This schema is released under the Creative Commons Attribution 4.0 International and is a product of the HED Working Group. The DOI for the latest version of the HED standard schema is 10.5281/zenodo.7876037.
```
````

#### A.2.5.7. Schema sources

The schema sources section is marked by `'''Sources'''` and lists external resources used during schema development. Each source is specified on a single line at level 1 (one asterisk) with comma-separated name-value pairs in `<nowiki>` tags. The section is present in every MediaWiki file; when the schema has no sources, it consists of the `'''Sources'''` header alone.

````{admonition} **Example:** HED schema source in .mediawiki format.

```moin
'''Sources'''
* <nowiki>source=Wikipedia,link=https://en.wikipedia.org,description=General definitions of concepts.</nowiki>
```
````

Each source entry has three required components:

- `source`: A short name for the source
- `link`: A URL pointing to the source
- `description`: A brief explanation of the source's relevance

In a merged library schema, a row contributed by the library begins with the attribute block `{inLibrary=xxx}`, with `xxx` the library name, followed by a blank and the name-value pairs (see [3.1.2.2. Merged vs unmerged](./03_HED_formats.md#3122-merged-vs-unmerged)). The rows of the standard schema partner have no attribute block.

````{admonition} **Example:** Source contributed by the lang library in a merged .mediawiki schema.

```moin
* <nowiki>{inLibrary=lang} source=GOLD,link=http://purl.org/linguistics/gold,description=General Ontology for Linguistic Description.</nowiki>
```
````

#### A.2.5.8. Schema prefixes

The schema prefixes section is marked by `'''Prefixes'''` and defines prefixes for ontology integration. Each prefix is specified on a single line at level 1 with comma-separated name-value pairs in `<nowiki>` tags. The section is present in every MediaWiki file; when the schema has no prefixes, it consists of the `'''Prefixes'''` header alone.

````{admonition} **Example:** HED schema prefixes in .mediawiki format.

```moin
'''Prefixes'''
* <nowiki>prefix=dc:,namespace=http://purl.org/dc/elements/1.1/#,description=The Dublin Core elements</nowiki>
* <nowiki>prefix=ncit:,namespace=http://purl.obolibrary.org/obo/ncit.owl,description=NCI Thesaurus OBO Edition</nowiki>
```
````

Each prefix entry has three required components:

- `prefix`: The prefix string including the colon (e.g., `dc:`)
- `namespace`: The full IRI for the ontology namespace
- `description`: A description of the ontology or vocabulary

A row contributed by a library is marked in a merged schema as in [A.2.5.7. Schema sources](#a257-schema-sources).

#### A.2.5.9. External annotations

The external annotations section is marked by `'''External annotations'''` and defines annotation properties from external ontologies. Each annotation is specified on a single line at level 1 with comma-separated name-value pairs in `<nowiki>` tags. The section is present in every MediaWiki file; when the schema has no external annotations, it consists of the `'''External annotations'''` header alone.

````{admonition} **Example:** HED external annotations in .mediawiki format.

```moin
'''External annotations'''
* <nowiki>prefix=dc:,id=creator,iri=http://purl.org/dc/elements/1.1/creator,description=An entity primarily responsible for making the resource.</nowiki>
* <nowiki>prefix=dc:,id=contributor,iri=http://purl.org/dc/elements/1.1/contributor,description=An entity responsible for making contributions to the resource.</nowiki>
```
````

Each external annotation entry has four required components:

- `prefix`: The ontology designator prefix (must be defined in the prefixes section)
- `id`: The local identifier for the property
- `iri`: The full IRI for the property
- `description`: An explanation of the property's meaning

A row contributed by a library is marked in a merged schema as in [A.2.5.7. Schema sources](#a257-schema-sources).

## A.3. XML file format

This section describes details of the XML schema format. The `.xml` format directly mirrors the order and information in the `.mediawiki` version of the schema.

### A.3.1. XML file layout

The XML schema file format has a header, prologue, main schema, definitions, and epilogue sections. The general layout is as follows:

````{admonition} XML layout of the HED schema.
```xml
<?xml version="1.0" ?>
<HED xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="8.5.0" xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/hed-standard/hed-schemas/refs/heads/main/standard_schema/hedxml/HED8.4.0.xsd">
<prologue>text of the prologue</prologue>
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

<epilogue>text of the epilogue</epilogue>

<schemaSources>
   <schemaSource> ... </schemaSource>
                  ...
   <schemaSource> ... </schemaSource>
</schemaSources>

<schemaPrefixes>
   <schemaPrefix> ... </schemaPrefix>
                  ...
   <schemaPrefix> ... </schemaPrefix>
</schemaPrefixes>

<externalAnnotations>
   <externalAnnotation> ... </externalAnnotation>
                        ...
   <externalAnnotation> ... </externalAnnotation>
</externalAnnotations>
</HED>
```
````

Every element in this layout is present in every file. A section with no entries is an element with no children, written either as a self-closing element or as an empty start-end pair; the two forms are equivalent in XML and tools accept both. For example, the end of an unmerged library schema that adds no sources, prefixes, or external annotations of its own is:

````{admonition} Empty extra sections at the end of an XML schema file.
```xml
<epilogue>text of the epilogue</epilogue>
<schemaSources/>
<schemaPrefixes/>
<externalAnnotations/>
</HED>
```
````

The following is the example schema of [A.2.1. Overall file layout](#a21-overall-file-layout) in XML format.

````{admonition} **Example:** XML version of the example schema of A.2.1.

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
                   <value>Sensory-presentation</value>
               </attribute>
           </node>
        </node>
                         . . .
        <node>
            <name>Property</name>
            <description>A characteristic.</description>
            <attribute>
                <name>extensionAllowed</name>
            </attribute>
            <node>
                <name>Informational-property</name>
                <description>A quality pertaining to information.</description>
                <node>
                    <name>Label</name>
                    <description>A string of 20 or fewer characters.</description>
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
    <schemaSources/>
    <schemaPrefixes/>
    <externalAnnotations/>
</HED>
```
````

### A.3.2. XML header

The `HED` node is the root node of the XML schema.

````{admonition} **Example:** Header for Version 8.0.0 of the standard HED XML schema.

```xml
<HED version="8.0.0">
```
````

The filename corresponding to this example is `HED8.0.0.xml`. The file is found in the [standard_schema/hedxml](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml) directory of the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

Library schemas must include the `library` attribute with the library name in their header line as shown in the following example.

````{admonition} **Example:** Version 1.0.0 of HED score library schema in .xml format.
```xml
<HED library="score" version="1.0.0">
```
````

The `library` and `version` values are used to form the official xml filename `HED_score_1.0.0.xml`. The file is found in [library_schemas/score/hedxml](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/score/hedxml) directory of the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

Unknown header attributes are treated as in the MediaWiki format ([A.2.2. MediaWiki header](#a22-mediawiki-header)).

Library schemas may also be partnered as is `HED_mouse_1.0.0.xml`.

````{admonition} **Example:** Partnered library schema mouse version 1.0.0 in .xml format.
```xml
<HED version="1.0.0" library="mouse" withStandard="8.5.0">
```
````

### A.3.3. XML prologue and epilogue

The `<prologue>...</prologue>` and `<epilogue>...</epilogue>` elements are meant to be treated as opaque as far as schema processing goes.

### A.3.4. XML schema section

The schema section of the HED XML document consists of an arbitrary number of `<node></node>` elements enclosed in a single `<schema></schema>` element.

````{admonition} Top-level XML layout of the HED schema.
```xml
<schema>
    <node> ... </node>
           ...
    <node> ... </node>
</schema>
```
````

A `<node>` element contains a required `<name>` child element, an optional `<description>` child element, and an optional number of additional `<attribute>` child elements:

````{admonition} XML layout HED node element.
```xml
<node>
    <name>xxx</name>
    <description>yyy</description>
    <attribute> ... </attribute>
    <attribute> ... </attribute>
    <attribute> ... </attribute>
    <node> ... </node>
</node>
```
````

The `<name>` element text must conform to the rules for naming HED schema nodes. It corresponds to the _node-name_ in the `mediawiki` specification and must not be empty. A `#` value is used to represent value place-holder elements.

The `<description>` element has the text contained in the square brackets `[ ]` in the `.mediawiki` node specification. If the `.mediawiki` description is missing or has an empty `[ ]`, the `<description>` element is omitted.

The optional `<attribute>` elements are derived from the attribute list contained in curly braces `{ }` of the `.mediawiki` specification. An `<attribute>` element has a single non-empty `<name></name>` child element whose text value corresponds to the node-name of attribute in the corresponding `.mediawiki` file. If the attribute does not have the `boolRange` property, then the `<attribute>` element should also have one or more child `<value></value>` elements giving the value(s) of the attribute.

**Example:** The `requireChild` attribute has the `boolRange` property. In the `.mediawiki` representation it appears as `{requireChild}` if present and is omitted if absent.

````{admonition} XML layout of an attribute that has the boolRange property.

```xml
<node>
    <name>xxx</name>
    <attribute>
       <name>requireChild</name>
    </attribute>
</node>
```
````

**Example:** The `suggestedTag` is a schema attribute that has a value. The attribute is meant to be used by tagging tools to suggest additional tags that a user might want to include. Notice that the `suggestedTag` values are valid HED tags in any form (short, long, or intermediate).

````{admonition} XML layout of an attribute that has values.

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

### A.3.5. XML auxiliary sections

The auxiliary sections define various aspects of behavior of various types of elements in the schema.

#### A.3.5.1. Unit classes

The unit classes are defined in the `<unitClassDefinitions>` section of the XML schema file, and the unit modifiers are defined in the `<unitModifierDefinitions>` section. These sections follow a format similar to the `<node>` element in the `<schema>` section.

The `<unitClassDefinition>` elements have a required `<name>`, an optional `<description>`, and an arbitrary number of additional `<attribute>` child elements. These `<attribute>` elements describe properties of the unit class rather than of individual unit types. In addition, `<unitClassDefinition>` elements may have an arbitrary number of `<unit>` child elements as shown in the following example.

````{admonition} Example XML layout of the unit class definitions.
```xml
<unitClassDefinition>
    <name>timeUnits</name>
    <description>Units of time, for example durations, delays, and intervals between events.</description>
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

Unit modifiers are defined in the `<unitModifierDefinitions>` section of the XML schema file. The following shows the layout of an example unit modifier definitions:

````{admonition} Example XML layout of the unit modifier definition
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

#### A.3.5.3. Value classes

Value classes are defined in the `<valueClassDefinitions>` section of the XML schema file. These sections follow a format similar to the `<node>` element in the `<schema>`:

````{admonition} Example XML layout of the value class definitions.
```xml
<valueClassDefinitions>
   <valueClassDefinition>
       <name>dateTimeClass</name>
       <description>Date-times conform to the BIDS Datetime format, RFC 3339 with an optional offset: YYYY-MM-DDThh:mm:ss (year, month, day, hour (24h), minute, second), an optional fraction of one to six digits, and an optional Z for UTC or a +hh:mm or -hh:mm offset.</description>
       <attribute>
           <name>allowedCharacter</name>
           <value>digits</value>
           <value>T</value>
           <value>hyphen</value>
           <value>colon</value>
           <value>period</value>
           <value>Z</value>
           <value>plus</value>
       </attribute>
   </valueClassDefinition>
</valueClassDefinitions>
```
````

#### A.3.5.4. Schema attributes

The `<schemaAttributeDefinitions>` section specifies the allowed attributes of the other elements including the `<node>`, `<unitClassDefinition>`, `<unitModifierDefinition>`, and `<valueClassDefinition>` elements. The specifications of individual attributes are given in `<schemaAttributeDefinition>` elements.

````{admonition} Example XML layout of the schema attribute definitions.
```xml
<schemaAttributeDefinitions>
    <schemaAttributeDefinition>
        <name>allowedCharacter</name>
        <description>A special character that is allowed in expressing the value of a placeholder of a specified value class.</description>
        <property>
            <name>unitDomain</name>
        </property>
        <property>
            <name>unitModifierDomain</name>
        </property>
        <property>
            <name>valueClassDomain</name>
        </property>
        <property>
            <name>stringRange</name>
        </property>
        <property>
            <name>hedId</name>
            <value>HED_0010304</value>
        </property>
    </schemaAttributeDefinition>
    <schemaAttributeDefinition>
        <name>takesValue</name>
        <description>This tag is a hashtag placeholder that is expected to be replaced with a user-defined value.</description>
        <property>
            <name>tagDomain</name>
        </property>
        <property>
            <name>boolRange</name>
        </property>
        <property>
            <name>hedId</name>
            <value>HED_0010503</value>
        </property>
        <property>
            <name>annotationProperty</name>
        </property>
    </schemaAttributeDefinition>
    . . .
</schemaAttributeDefinitions>
```
````

#### A.3.5.5. Schema properties

The following is an example of the layout of the `valueClassDomain` in `.xml` format.

````{admonition} Example XML layout of the schema property definitions.
```xml

  <propertyDefinitions>
                  . . .
      <propertyDefinition>
         <name>valueClassDomain</name>
         <description>This schema attribute can apply to value classes. This property was formerly named valueClassProperty.</description>
         <property>
            <name>hedId</name>
            <value>HED_0010713</value>
         </property>
      </propertyDefinition>
   </propertyDefinitions>
```
````

See [Schema properties](#a15-schema-properties) for a list of available schema properties.

#### A.3.5.6. Epilogue

The `<epilogue>` element contains text providing information about the schema license, attribution, and other metadata. It appears as a single child element of the root `<HED>` element. The element is always present and may be empty.

````{admonition} **Example:** XML layout of the epilogue section.
```xml
<epilogue>This schema is released under the Creative Commons Attribution 4.0 International and is a product of the HED Working Group. The DOI for the latest version of the HED standard schema is 10.5281/zenodo.7876037.</epilogue>
```
````

#### A.3.5.7. Schema sources

The `<schemaSources>` element contains zero or more `<schemaSource>` child elements, each documenting an external resource used during schema development. The element is present in every XML file and has no children when the schema has no sources.

````{admonition} **Example:** XML layout of the schema sources section.
```xml
<schemaSources>
   <schemaSource>
      <name>Wikipedia</name>
      <link>https://en.wikipedia.org</link>
      <description>General definitions of concepts.</description>
   </schemaSource>
</schemaSources>
```
````

Each `<schemaSource>` element has three required child elements:

- `<name>`: A short identifier for the source (the `source` column of the MediaWiki and TSV formats)
- `<link>`: A URL pointing to the source resource
- `<description>`: A brief explanation of the source's relevance

In a merged library schema, a `<schemaSource>` element contributed by the library has one more child, an `<attribute>` element for `inLibrary` in the form used for the attributes of a `<node>` (see [3.1.2.2. Merged vs unmerged](./03_HED_formats.md#3122-merged-vs-unmerged)). The elements of the standard schema partner do not have it.

````{admonition} **Example:** XML source contributed by the lang library in a merged schema.
```xml
<schemaSource>
   <name>GOLD</name>
   <link>http://purl.org/linguistics/gold</link>
   <description>General Ontology for Linguistic Description.</description>
   <attribute>
      <name>inLibrary</name>
      <value>lang</value>
   </attribute>
</schemaSource>
```
````

#### A.3.5.8. Schema prefixes

The `<schemaPrefixes>` element contains zero or more `<schemaPrefix>` child elements, each defining a namespace prefix for ontology integration. The element is present in every XML file and has no children when the schema has no prefixes.

````{admonition} **Example:** XML layout of the schema prefixes section.
```xml
<schemaPrefixes>
   <schemaPrefix>
      <name>dc:</name>
      <namespace>http://purl.org/dc/elements/1.1/#</namespace>
      <description>The Dublin Core elements</description>
   </schemaPrefix>
   <schemaPrefix>
      <name>ncit:</name>
      <namespace>http://purl.obolibrary.org/obo/ncit.owl</namespace>
      <description>NCI Thesaurus OBO Edition</description>
   </schemaPrefix>
</schemaPrefixes>
```
````

Each `<schemaPrefix>` element has three required child elements:

- `<name>`: The prefix string including the colon (e.g., `dc:`) (the `prefix` column of the MediaWiki and TSV formats)
- `<namespace>`: The full IRI for the ontology namespace
- `<description>`: A description of the ontology or vocabulary

A row contributed by a library is marked in a merged schema as in [A.3.5.7. Schema sources](#a357-schema-sources).

#### A.3.5.9. External annotations

The `<externalAnnotations>` element contains zero or more `<externalAnnotation>` child elements, each defining an annotation property from an external ontology. The element is present in every XML file and has no children when the schema has no external annotations.

````{admonition} **Example:** XML layout of the external annotations section.
```xml
<externalAnnotations>
   <externalAnnotation>
      <name>dc:</name>
      <id>creator</id>
      <iri>http://purl.org/dc/elements/1.1/creator</iri>
      <description>An entity primarily responsible for making the resource.</description>
   </externalAnnotation>
   <externalAnnotation>
      <name>dc:</name>
      <id>contributor</id>
      <iri>http://purl.org/dc/elements/1.1/contributor</iri>
      <description>An entity responsible for making contributions to the resource.</description>
   </externalAnnotation>
</externalAnnotations>
```
````

Each `<externalAnnotation>` element has four required child elements:

- `<name>`: The ontology designator prefix (must be defined in the prefixes section) (the `prefix` column of the MediaWiki and TSV formats)
- `<id>`: The local identifier for the property
- `<iri>`: The full IRI for the property
- `<description>`: An explanation of the property's meaning

A row contributed by a library is marked in a merged schema as in [A.3.5.7. Schema sources](#a357-schema-sources).

## A.4. JSON file format

This section describes details of the JSON schema format.

### A.4.1. JSON file layout

The JSON schema file format is a nested structure representing the schema in JavaScript Object Notation. The general layout follows the standard JSON format with objects and arrays:

````{admonition} JSON layout of the HED schema.
```json
{
  "version": "8.5.0",
  "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
  "xsi:noNamespaceSchemaLocation": "...",
  "prologue": "text of the prologue",
  "tags": {
    "tag-name": {
      "short_form": "...",
      "long_form": "...",
      "description": "...",
      "parent": "...",
      "children": [...],
      "attributes": {...},
      "explicitAttributes": {...}
    },
    ...
  },
  "units": {...},
  "unit_classes": {...},
  "unit_modifiers": {...},
  "value_classes": {...},
  "schema_attributes": {...},
  "properties": {...},
  "epilogue": "text of the epilogue",
  "sources": [...],
  "prefixes": [...],
  "external_annotations": [...]
}
```
````

Every key in this layout is present in every file. A section with no entries is an empty object (`{}`) for `units`, `unit_classes`, `unit_modifiers`, `value_classes`, `schema_attributes`, and `properties`, and an empty array (`[]`) for `sources`, `prefixes`, and `external_annotations`. For example, an unmerged library schema that adds no sources, prefixes, or external annotations of its own ends with:

````{admonition} Empty extra sections at the end of a JSON schema file.
```json
  "sources": [],
  "prefixes": [],
  "external_annotations": []
```
````

### A.4.2. JSON header

The top-level JSON object contains metadata attributes including the schema version and XML schema location information.

````{admonition} Example JSON header for version 8.5.0 of the standard HED schema.
```json
{
  "version": "8.5.0",
  "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
  "xsi:noNamespaceSchemaLocation": "https://raw.githubusercontent.com/hed-standard/hed-schemas/refs/heads/main/standard_schema/hedxml/HED8.4.0.xsd"
}
```
````

Library schemas include a `library` field with the library name:

````{admonition} Example JSON header for a library schema.
```json
{
  "library": "score",
  "version": "1.0.0"
}
```
````

Partnered library schemas also include `withStandard` and optionally `unmerged` fields:

````{admonition} Example JSON header for partnered library schema.
```json
{
  "library": "mouse",
  "version": "1.0.0",
  "withStandard": "8.5.0",
  "unmerged": "True"
}
```
````

### A.4.3. JSON prologue and epilogue

The `prologue` and `epilogue` fields are always present and contain text, possibly empty, that provides documentation about the schema but is not processed during validation.

### A.4.4. JSON tags section

The `tags` section is an object where each key is a tag name and the value is an object containing:

- `short_form`: The tag name without ancestors
- `long_form`: The full path of the tag
- `description`: Human-readable description
- `parent`: The parent tag name (or null for top-level tags)
- `children`: Array of child tag names
- `attributes`: All attributes including inherited ones
- `explicitAttributes`: Only attributes explicitly assigned to this tag

````{admonition} Example JSON tag element.
```json
"Agent-action": {
  "short_form": "Agent-action",
  "long_form": "Event/Agent-action",
  "description": "Any action engaged in by an agent.",
  "parent": "Event",
  "children": [],
  "attributes": {
    "suggestedTag": ["Task-event-role", "Agent", "Task-property"],
    "hedId": "HED_0012003"
  },
  "explicitAttributes": {
    "suggestedTag": ["Task-event-role", "Agent"],
    "hedId": "HED_0012003"
  }
}
```
````

### A.4.5. JSON auxiliary sections

#### A.4.5.1. Unit classes

The `unit_classes` section defines unit classes as objects where each key is a unit class name:

````{admonition} Example JSON layout of unit classes.
```json
"unit_classes": {
  "timeUnits": {
    "description": "Units of time, for example durations, delays, and intervals between events.",
    "hedId": "HED_0011513",
    "units": ["second", "s", "day", "week", "month", "minute", "hour", "year"],
    "default_units": "s"
  }
}
```
````

The `units` array of a unit class lists the names of its units. The units themselves are the entries of the top-level `units` object, keyed by unit name; each entry gives the unit's `description`, its `hedId`, and its attributes:

````{admonition} Example JSON layout of units.
```json
"units": {
  "second": {
    "description": null,
    "SIUnit": true,
    "conversionFactor": "1.0",
    "hedId": "HED_0011633"
  },
  "s": {
    "description": null,
    "SIUnit": true,
    "unitSymbol": true,
    "conversionFactor": "1.0",
    "hedId": "HED_0011634"
  }
}
```
````

#### A.4.5.2. Unit modifiers

The `unit_modifiers` section defines unit modifiers with their properties:

````{admonition} Example JSON layout of unit modifiers.
```json
"unit_modifiers": {
  "deca": {
    "description": "SI unit multiple representing 10^1.",
    "hedId": "HED_0011400",
    "conversionFactor": "10.0",
    "SIUnitModifier": true
  },
  "da": {
    "description": "SI unit multiple representing 10^1.",
    "hedId": "HED_0011401",
    "conversionFactor": "10.0",
    "SIUnitSymbolModifier": true
  }
}
```
````

#### A.4.5.3. Value classes

The `value_classes` section defines value classes with their allowed characters:

````{admonition} Example JSON layout of value classes.
```json
"value_classes": {
  "dateTimeClass": {
    "description": "Date-times conform to the BIDS Datetime format, RFC 3339 with an optional offset: YYYY-MM-DDThh:mm:ss (year, month, day, hour (24h), minute, second), an optional fraction of one to six digits, and an optional Z for UTC or a +hh:mm or -hh:mm offset.",
    "hedId": "HED_0011301",
    "allowed_characters": ["digits", "T", "hyphen", "colon", "period", "Z", "plus"]
  },
  "numericClass": {
    "description": "Value must be a valid numerical value.",
    "hedId": "HED_0011303",
    "allowed_characters": ["digits", "E", "e", "plus", "hyphen", "period"]
  }
}
```
````

#### A.4.5.4. Schema attributes

The `schema_attributes` section defines the allowed schema attributes with their domain and range properties:

````{admonition} Example JSON layout of schema attributes.
```json
"schema_attributes": {
  "suggestedTag": {
    "description": "A tag that is often associated with this tag.",
    "hedId": "HED_0010106",
    "tagDomain": true,
    "tagRange": true
  },
  "takesValue": {
    "description": "This tag is a hashtag placeholder...",
    "hedId": "HED_0010503",
    "tagDomain": true,
    "boolRange": true,
    "annotationProperty": true
  }
}
```
````

#### A.4.5.5. Schema properties

The `properties` section defines the schema properties in JSON format:

````{admonition} Example JSON layout of schema properties.
```json
"properties": {
  "tagDomain": {
    "description": "This schema attribute can apply to node (tag-term) elements. This was added so attributes could apply to multiple types of elements. This property was formerly named nodeProperty.",
    "hedId": "HED_0010704"
  },
  "boolRange": {
    "description": "This schema attribute's value can be true or false. This property was formerly named boolProperty.",
    "hedId": "HED_0010702"
  },
  "valueClassDomain": {
    "description": "This schema attribute can apply to value classes. This property was formerly named valueClassProperty.",
    "hedId": "HED_0010713"
  }
}
```
````

See [Schema properties](#a15-schema-properties) for a list of available schema properties.

#### A.4.5.6. Schema sources

The `sources` section defines external resources used during schema development as an array of objects. The array is present in every JSON file and is empty when the schema has no sources:

````{admonition} Example JSON layout of schema sources.
```json
"sources": [
  {
    "name": "Wikipedia",
    "link": "https://en.wikipedia.org",
    "description": "General definitions of concepts."
  }
]
```
````

Each source object has three required properties:

- `name`: A short identifier for the source (the `source` column of the MediaWiki and TSV formats)
- `link`: A URL pointing to the source resource
- `description`: A brief explanation of the source's relevance

In a merged library schema, a source object contributed by the library has one more property, `inLibrary`, whose value is the library name (see [3.1.2.2. Merged vs unmerged](./03_HED_formats.md#3122-merged-vs-unmerged)). The objects of the standard schema partner do not have it.

````{admonition} Example JSON source contributed by the lang library in a merged schema.
```json
{
  "name": "GOLD",
  "link": "http://purl.org/linguistics/gold",
  "description": "General Ontology for Linguistic Description.",
  "inLibrary": "lang"
}
```
````

#### A.4.5.7. Schema prefixes

The `prefixes` section defines prefixes for ontology integration as an array of objects. The array is present in every JSON file and is empty when the schema has no prefixes:

````{admonition} Example JSON layout of schema prefixes.
```json
"prefixes": [
  {
    "name": "dc:",
    "namespace": "http://purl.org/dc/elements/1.1/#",
    "description": "The Dublin Core elements"
  },
  {
    "name": "ncit:",
    "namespace": "http://purl.obolibrary.org/obo/ncit.owl",
    "description": "NCI Thesaurus OBO Edition"
  }
]
```
````

Each prefix object has three required properties:

- `name`: The prefix string including the colon (e.g., `dc:`) (the `prefix` column of the MediaWiki and TSV formats)
- `namespace`: The full IRI for the ontology namespace
- `description`: A description of the ontology or vocabulary

A row contributed by a library is marked in a merged schema as in [A.4.5.6. Schema sources](#a456-schema-sources).

#### A.4.5.8. External annotations

The `external_annotations` section defines annotation properties from external ontologies as an array of objects. The array is present in every JSON file and is empty when the schema has no external annotations:

````{admonition} Example JSON layout of external annotations.
```json
"external_annotations": [
  {
    "name": "dc:",
    "id": "creator",
    "iri": "http://purl.org/dc/elements/1.1/creator",
    "description": "An entity primarily responsible for making the resource."
  },
  {
    "name": "dc:",
    "id": "contributor",
    "iri": "http://purl.org/dc/elements/1.1/contributor",
    "description": "An entity responsible for making contributions to the resource."
  }
]
```
````

Each external annotation object has four required properties:

- `name`: The ontology designator prefix (must be defined in the prefixes section) (the `prefix` column of the MediaWiki and TSV formats)
- `id`: The local identifier for the property
- `iri`: The full IRI for the property
- `description`: An explanation of the property's meaning

A row contributed by a library is marked in a merged schema as in [A.4.5.6. Schema sources](#a456-schema-sources).

## A.5. TSV file format

This section describes details of the TSV (Tab-Separated Values) schema format. Unlike other HED schema formats that use a single file, the TSV format represents a schema as a collection of separate TSV files organized in a directory structure. This format is designed to facilitate ontology mapping and interoperability with semantic web technologies.

### A.5.1. TSV file organization

The TSV schema format consists of multiple files, each representing a different aspect of the schema:

````{admonition} TSV file organization for HED schema.
```text
HED8.5.0/
|-- HED8.5.0_Structure.tsv
|-- HED8.5.0_Tag.tsv
|-- HED8.5.0_UnitClass.tsv
|-- HED8.5.0_Unit.tsv
|-- HED8.5.0_UnitModifier.tsv
|-- HED8.5.0_ValueClass.tsv
|-- HED8.5.0_DataProperty.tsv
|-- HED8.5.0_ObjectProperty.tsv
|-- HED8.5.0_AnnotationProperty.tsv
|-- HED8.5.0_AnnotationPropertyExternal.tsv
|-- HED8.5.0_AttributeProperty.tsv
|-- HED8.5.0_Prefixes.tsv
`-- HED8.5.0_Sources.tsv
```
````

The twelve sections of a schema (see [3.1.4. Schema layout overview](./03_HED_formats.md#314-schema-layout-overview)) are stored in these files as follows:

| Section              | TSV files                                              |
| -------------------- | ------------------------------------------------------ |
| Header               | `Structure`                                            |
| Prologue             | `Structure`                                            |
| Schema               | `Tag`                                                  |
| Unit classes         | `UnitClass`, `Unit`                                    |
| Unit modifiers       | `UnitModifier`                                         |
| Value classes        | `ValueClass`                                           |
| Schema attributes    | `DataProperty`, `ObjectProperty`, `AnnotationProperty` |
| Schema properties    | `AttributeProperty`                                    |
| Epilogue             | `Structure`                                            |
| Sources              | `Sources`                                              |
| Prefixes             | `Prefixes`                                             |
| External annotations | `AnnotationPropertyExternal`                           |

Every file in this layout is written for every schema. The file for a section with no entries contains only its header row. For example, the Sources file of an unmerged library schema that adds no sources of its own is the single line `source	link	Attributes	description`.

### A.5.2. TSV header formats

Each TSV file begins with a header row of column names. The header row of each file is:

| File                         | Header row                                                                              |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| `Structure`                  | `hedId`, `rdfs:label`, `Attributes`, `omn:SubClassOf`, `dc:description`                 |
| `Tag`                        | `hedId`, `Level`, `rdfs:label`, `omn:SubClassOf`, `Attributes`, `dc:description`        |
| `UnitClass`                  | `hedId`, `rdfs:label`, `omn:SubClassOf`, `Attributes`, `dc:description`                 |
| `Unit`                       | `hedId`, `rdfs:label`, `omn:SubClassOf`, `Attributes`, `dc:description`, `hasUnitClass` |
| `UnitModifier`               | `hedId`, `rdfs:label`, `omn:SubClassOf`, `Attributes`, `dc:description`                 |
| `ValueClass`                 | `hedId`, `rdfs:label`, `omn:SubClassOf`, `Attributes`, `dc:description`                 |
| `DataProperty`               | `hedId`, `rdfs:label`, `Type`, `Properties`, `dc:description`                           |
| `ObjectProperty`             | `hedId`, `rdfs:label`, `Type`, `Properties`, `dc:description`                           |
| `AnnotationProperty`         | `hedId`, `rdfs:label`, `Type`, `Properties`, `dc:description`                           |
| `AttributeProperty`          | `hedId`, `rdfs:label`, `Type`, `dc:description`                                         |
| `Sources`                    | `source`, `link`, `Attributes`, `description`                                           |
| `Prefixes`                   | `prefix`, `namespace`, `Attributes`, `description`                                      |
| `AnnotationPropertyExternal` | `prefix`, `id`, `iri`, `Attributes`, `description`                                      |

Columns are identified by name. `rdfs:label` is the name of the element, `omn:SubClassOf` its parent, `dc:description` its description, and `Level` the depth of a tag in the hierarchy. An `Attributes` cell is a comma-separated list of attribute assignments. A `Properties` cell is a comma-separated list of the schema properties of a schema attribute, together with any schema attribute other than `hedId` that is assigned to it: the cell for `unitPrefix` in HED `8.5.0` is `deprecatedFrom=8.4.0, unitDomain, boolRange` (see [A.5.12. TSV format conventions](#a512-tsv-format-conventions)). The `AttributeProperty` file has neither column: of the two schema attributes that may be assigned to a schema property, it records `hedId` and has no place for `deprecatedFrom`, so the deprecation of a schema property cannot be recorded in the TSV format (see [3.1.4.8. Schema properties](./03_HED_formats.md#3148-schema-properties)).

A tool that writes a schema in TSV format MUST write these columns, in this order, whatever the version of the schema. A file MAY also have columns that are not in this table, holding annotation properties for the HED ontology such as `dc:comment` (see [8.1.4.3. TSV format](./08_HED_ontology.md#8143-tsv-format)); such columns are not part of the schema. A tool that reads a schema in TSV format MUST also accept the header rows that earlier schema versions were written with, which are listed in [B.3. Differences for earlier schema versions](./Appendix_B.md#b3-differences-for-earlier-schema-versions). This is stated from specification `4.0.0`.

### A.5.3. TSV structure file

The Structure file contains metadata about the schema including header, prologue, and epilogue:

````{admonition} Example TSV Structure file layout.
```text
hedId	rdfs:label	Attributes	omn:SubClassOf	dc:description
HED_0010010	StandardHeader	version="8.5.0", xmlns:xsi="..."	HedHeader
HED_0010011	StandardPrologue		HedPrologue	The HED standard schema is...
HED_0010012	StandardEpilogue		HedEpilogue	This schema is released under...
```
````

### A.5.4. TSV tag file

The Tag file contains all HED tags with their hierarchy and attributes:

````{admonition} Example TSV Tag file layout.
```text
hedId	Level	rdfs:label	omn:SubClassOf	Attributes	dc:description
HED_0012001	0	Event	HedTag	suggestedTag=Task-property, annotation=skos:exactMatch ncit:C25499	Something that happens...
HED_0012002	1	Sensory-event	Event	suggestedTag=Task-event-role	Something perceivable...
```
````

The `Level` column indicates the depth in the hierarchy (0 for top-level tags, 1 for children, etc.).

### A.5.5. TSV unit class file

The UnitClass file defines all unit classes:

````{admonition} Example TSV UnitClass file layout.
```text
hedId	rdfs:label	omn:SubClassOf	Attributes	dc:description
HED_0011513	timeUnits	StandardUnitClass	defaultUnits=s
HED_0011510	physicalLengthUnits	StandardUnitClass	defaultUnits=m
```
````

### A.5.6. TSV unit file

The Unit file contains all units with their attributes and unit class associations:

````{admonition} Example TSV Unit file layout.
```text
hedId	rdfs:label	omn:SubClassOf	Attributes	dc:description	hasUnitClass
HED_0011633	second	StandardUnit	SIUnit, conversionFactor=1.0		timeUnits
HED_0011634	s	StandardUnit	SIUnit, unitSymbol, conversionFactor=1.0		timeUnits
HED_0011635	day	StandardUnit	conversionFactor=86400		timeUnits
```
````

The `hasUnitClass` column indicates which unit class the unit belongs to.

### A.5.7. TSV unit modifier file

The UnitModifier file defines unit modifiers (SI prefixes):

````{admonition} Example TSV UnitModifier file layout.
```text
hedId	rdfs:label	omn:SubClassOf	Attributes	dc:description
HED_0011424	milli	StandardUnitModifier	SIUnitModifier, conversionFactor=0.001	SI unit submultiple...
HED_0011425	m	StandardUnitModifier	SIUnitSymbolModifier, conversionFactor=0.001	SI unit submultiple...
```
````

### A.5.8. TSV value class file

The ValueClass file defines value classes and their allowed characters:

````{admonition} Example TSV ValueClass file layout.
```text
hedId	rdfs:label	omn:SubClassOf	Attributes	dc:description
HED_0011301	dateTimeClass	StandardValueClass	allowedCharacter=digits, allowedCharacter=T, allowedCharacter=hyphen, allowedCharacter=colon, allowedCharacter=period, allowedCharacter=Z, allowedCharacter=plus	Date-times conform to the BIDS Datetime format, RFC 3339 with an optional offset: YYYY-MM-DDThh:mm:ss (year, month, day, hour (24h), minute, second), an optional fraction of one to six digits, and an optional Z for UTC or a +hh:mm or -hh:mm offset.
HED_0011303	numericClass	StandardValueClass	allowedCharacter=digits, allowedCharacter=E, allowedCharacter=e, allowedCharacter=plus, allowedCharacter=hyphen, allowedCharacter=period	Value must be a valid numerical value.
```
````

### A.5.9. TSV property files

The schema attributes are stored in three files, one for each kind of ontology property:

#### A.5.9.1. DataProperty file

Defines the schema attributes that are data properties (their values are strings, numbers, or booleans):

````{admonition} Example TSV DataProperty file layout.
```text
hedId	rdfs:label	Type	Properties	dc:description
HED_0010304	allowedCharacter	DataProperty	unitDomain, unitModifierDomain, valueClassDomain, stringRange	A special character...
HED_0010305	conversionFactor	DataProperty	unitDomain, unitModifierDomain, numericRange	The factor to multiply...
```
````

#### A.5.9.2. ObjectProperty file

Defines the schema attributes that are object properties (their values are other schema elements):

````{admonition} Example TSV ObjectProperty file layout.
```text
hedId	rdfs:label	Type	Properties	dc:description
HED_0010104	defaultUnits	ObjectProperty	unitClassDomain, unitRange	The default units...
HED_0010105	relatedTag	ObjectProperty	tagDomain, tagRange	A HED tag closely related...
```
````

#### A.5.9.3. AnnotationProperty file

Defines the schema attributes that are annotation properties (they are not inherited and do not participate in reasoning):

````{admonition} Example TSV AnnotationProperty file layout.
```text
hedId	rdfs:label	Type	Properties	dc:description
HED_0010500	hedId	AnnotationProperty	elementDomain, stringRange	The unique identifier...
HED_0010501	requireChild	AnnotationProperty	tagDomain, boolRange	This tag must have...
```
````

### A.5.10. TSV attribute property file

The AttributeProperty file defines the schema properties:

````{admonition} Example TSV AttributeProperty file layout.
```text
hedId	rdfs:label	Type	dc:description
HED_0010704	tagDomain	AnnotationProperty	This schema attribute can apply to node (tag-term) elements. This was added so attributes could apply to multiple types of elements. This property was formerly named nodeProperty.
HED_0010702	boolRange	AnnotationProperty	This schema attribute's value can be true or false. This property was formerly named boolProperty.
HED_0010713	valueClassDomain	AnnotationProperty	This schema attribute can apply to value classes. This property was formerly named valueClassProperty.
```
````

### A.5.11. TSV sources, prefixes, and annotations

The TSV format includes separate files for schema sources, schema prefixes, and external annotation properties.

#### A.5.11.1. Sources file

Defines external resources used during schema development. The file is present in every TSV schema directory and contains only the header row when the schema has no sources:

````{admonition} Example TSV Sources file layout.
```text
source	link	Attributes	description
Wikipedia	https://en.wikipedia.org		General definitions of concepts.
```
````

Each row has three required columns:

- `source`: A short name for the source
- `link`: A URL pointing to the source
- `description`: A brief explanation of the source's relevance

The file also has an `Attributes` column, between `link` and `description`. Its cell is empty except in a merged library schema, where a row contributed by the library has `inLibrary=xxx`, with `xxx` the library name (see [3.1.2.2. Merged vs unmerged](./03_HED_formats.md#3122-merged-vs-unmerged)). In the merged `lang` library schema `1.2.0`, for example, the `GOLD` row of the Sources file has `inLibrary=lang` and the two rows of the standard schema have an empty cell.

#### A.5.11.2. Prefixes file

Defines the prefixes used for external ontology references. The file is present in every TSV schema directory and contains only the header row when the schema has no prefixes:

````{admonition} Example TSV Prefixes file layout.
```text
prefix	namespace	Attributes	description
dc:	http://purl.org/dc/elements/1.1/#		The Dublin Core elements
ncit:	http://purl.obolibrary.org/obo/ncit.owl		NCI Thesaurus OBO Edition
```
````

Each row has three required columns:

- `prefix`: The prefix string including the colon (e.g., `dc:`)
- `namespace`: The full IRI or URL for the ontology namespace
- `description`: A description of the ontology or vocabulary

The file also has an `Attributes` column, between `namespace` and `description`, used as in the [Sources file](#a5111-sources-file).

#### A.5.11.3. External annotations file

Defines external annotation properties that can be used. The file is present in every TSV schema directory and contains only the header row when the schema has no external annotations:

````{admonition} Example TSV AnnotationPropertyExternal file layout.
```text
prefix	id	iri	Attributes	description
dc:	creator	http://purl.org/dc/elements/1.1/creator		An entity primarily responsible for making the resource.
dc:	contributor	http://purl.org/dc/elements/1.1/contributor		An entity responsible for making contributions to the resource.
```
````

Each row has four required columns:

- `prefix`: The ontology designator prefix (must be defined in the Prefixes file)
- `id`: The local identifier for the property
- `iri`: The full IRI for the property
- `description`: An explanation of the property's meaning

The file also has an `Attributes` column, between `iri` and `description`, used as in the [Sources file](#a5111-sources-file).

### A.5.12. TSV format conventions

1. **Delimiters**: Fields are separated by tab characters (`\t`).
2. **Multiple values**: When a column contains multiple values (e.g., multiple attributes), they are separated by commas.
3. **Attribute format**: Attributes are specified as `name=value` for valued attributes or just `name` for boolean attributes.
4. **Encoding**: Files use UTF-8 encoding.
5. **Hierarchy**: Tag hierarchy is expressed through the `Level` column in the Tag file and through the `omn:SubClassOf` column in the files that have one.
6. **Identifiers**: Each element has a unique `hedId` that persists across schema versions.

See [Schema properties](#a15-schema-properties) for a list of available schema properties.

## A.6. Reserved tags file

The validation rules of the structural reserved tags are published as the JSON file [`reserved_tags.json`](https://www.hedtags.org/hed-specification/_static/reserved_tags.json) (`docs/source/_static/reserved_tags.json` in the specification repository). HED validators load this file unchanged rather than transcribing its rules. The tables of [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags) are generated from it, and that section states what each column requires of an annotation. The file is introduced in specification `4.0.0`. A standard schema is checked against the file: every row of `tags` MUST exist as a tag, with the `topLevelTagGroup` attribute and `reserved`; `Def` and `Def-expand` MUST exist and carry `reserved`.

### A.6.1. File layout

The file is a JSON object with six keys:

- `title` and `description`: text for human readers.
- `specificationVersion` and `fileVersion`: the version of this specification that the file belongs to and the version of the file's layout, defined below.
- `tags`: an object with one entry per structural reserved tag that defines a top-level tag group (`Definition`, `Delay`, `Duration`, `Event-context`, `Inset`, `Offset`, `Onset`). Each entry is keyed by the tag name and holds the fields of [A.6.2](#a62-tag-fields). `Def` and `Def-expand` have no entry: they are the anchor that these groups refer to.
- `valueForms`: an object with one entry for each tag whose value has two parts, described in [A.6.3](#a63-value-forms).

The two version fields have the same meaning in this file and in the character sets file of [A.7](#a7-character-sets-file). Each file spells them in the case of its own keys: camel case here, snake case (`specification_version`, `file_version`) in the character sets file.

- The specification version (`specificationVersion` here, `specification_version` in the character sets file) is a string `X.Y.Z`, the version of this specification that the file belongs to. It equals the specification version and changes with every specification release, even when nothing else in the file changes.
- The file version (`fileVersion` here, `file_version` in the character sets file) is a string `X.Y.Z`, the version of the file's layout, independent of the specification version. The major number changes when a validator must be updated to apply the file: a key is removed or renamed, the meaning of a key changes, or a key is added that carries a validation rule. The minor number changes when a key is added that carries no validation rule, such as descriptive text or tests. The patch number changes when only values change, other than the specification version.

A validator MUST NOT apply a file whose file version major number it does not support, and it accepts any minor and patch number under a major number it supports. Both fields are introduced in specification `4.0.0`, in which the file version of each file is `1.0.0`.

### A.6.2. Tag fields

Each entry of `tags` has the fields below. The **Column** is the heading of the corresponding column in the first table of 3.2.8; fields that have the same value in every entry are stated in the sentences around that table instead.

| Field                    | Type               | Column        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                   | string             | Tag           | The tag name; equal to the entry's key.                                                                                                                                                                                                                                                                                                                                                                           |
| `noExtension`            | boolean            | -             | The tag MUST NOT be extended, although it inherits `extensionAllowed` ([3.2.5](./03_HED_formats.md#325-tag-extensions)).                                                                                                                                                                                                                                                                                          |
| `requireValue`           | boolean            | Value         | The tag MUST have a value.                                                                                                                                                                                                                                                                                                                                                                                        |
| `tagGroup`               | boolean            | -             | The same as the schema attribute of that name: the tag MUST be in a tag group.                                                                                                                                                                                                                                                                                                                                    |
| `topLevelTagGroup`       | boolean            | -             | The same as the schema attribute of that name: the tag MUST be in a top-level tag group.                                                                                                                                                                                                                                                                                                                          |
| `requiresDef`            | boolean            | Anchor        | `true`: the group MUST contain exactly one anchor, a `Def` tag or `Def-expand` group. `false`: no anchor at the top level of the group.                                                                                                                                                                                                                                                                           |
| `otherAllowedNonDefTags` | array of tag names | Other tags    | The only tags, besides the tag itself and its anchor, allowed at the top level of the group.                                                                                                                                                                                                                                                                                                                      |
| `minNonDefSubgroups`     | integer            | Min groups    | The minimum number of inner groups in the group, not counting a `Def-expand` anchor group.                                                                                                                                                                                                                                                                                                                        |
| `maxNonDefSubgroups`     | integer or `null`  | Max groups    | The maximum number of inner groups, not counting a `Def-expand` anchor group; `null` means no limit.                                                                                                                                                                                                                                                                                                              |
| `secondaryWith`          | array of tag names | -             | Optional. In a group that also holds one of these tags, that tag's entry gives the group rules (`requiresDef`, `otherAllowedNonDefTags`, `minNonDefSubgroups`, `maxNonDefSubgroups`, `allowSpliceInGroup`), and this entry's group rules apply only when its tag is the only one of `tags` in the group; its other fields apply wherever the tag appears (see the paragraph on `Delay` after the table of 3.2.8). |
| `requiresTimeline`       | boolean            | Timeline only | The tag MUST NOT appear in a table without an `onset` or equivalent column, such as the NWB `TimestampVectorData` column named `timestamp`.                                                                                                                                                                                                                                                                       |
| `allowSpliceInGroup`     | boolean            | { } allowed   | `true`: a sidecar column reference (`{column}`) MAY appear in the group, and the rules are checked after substitution. `false`: it MUST NOT.                                                                                                                                                                                                                                                                      |
| `ERROR_CODE`             | string             | -             | The error code reported by default when a rule of the entry is violated; a heading of [Appendix B](./Appendix_B.md), which gives the violations reported under another code.                                                                                                                                                                                                                                      |

### A.6.3. Value forms

Each entry of `valueForms` is keyed by a tag name (`Definition`, `Def`, `Def-expand`) and has one field, `secondPart`, which gives what may follow the name in the tag's two-part value:

- `placeholder`: only `#` (used by `Definition`).
- `placeholderValue`: the value substituted for the definition's placeholder, checked against the placeholder tag's value class and units (used by `Def` and `Def-expand`).

The second table of 3.2.8 is generated from these entries. See [3.2.8.1](./03_HED_formats.md#3281-the-definition-tag) and [3.2.8.2](./03_HED_formats.md#3282-def-and-def-expand-tags) for the rules.

## A.7. Character sets file

The character sets of [2.2 Character sets and restrictions](./02_Terminology.md#22-character-sets-and-restrictions) are published as the JSON file [`character_sets.json`](https://www.hedtags.org/hed-specification/_static/character_sets.json) (`docs/source/_static/character_sets.json` in the specification repository). HED validators load this file unchanged rather than transcribing its sets. The table of 2.2 is generated from it. The file is introduced in specification `4.0.0`. Every regular expression in the file uses only syntax that Python `re` and JavaScript `RegExp` share, with ASCII digit classes (`[0-9]`, never a Unicode-aware shorthand).

### A.7.1. File layout

The file is a JSON object with eleven keys:

- `title` and `description`: text for human readers.
- `specification_version` and `file_version`: the version of this specification that the file belongs to and the version of the file's layout, as defined in [A.6.1](#a61-file-layout).
- `sets`: an object with one entry per named character set, keyed by the set name, holding the fields of [A.7.2](#a72-set-entries). These are the rows of the table in 2.2.
- `aliases`: an object whose keys are alternative names and whose values are keys of `sets` (`slash` for `forward-slash`). An alias is not itself a key of `sets`.
- `literal_names`: how a single character names itself as an `allowedCharacter` name; fields in [A.7.3](#a73-names-and-value-class-defaults).
- `declaration_wins_from`: the standard schema version from which a value class's own `allowedCharacter` declaration defines its characters; fields in [A.7.3](#a73-names-and-value-class-defaults).
- `value_class_defaults`: the characters of the standard value classes in the standard schemas before that version, described in [A.7.3](#a73-names-and-value-class-defaults).
- `value_class_words`: whole-value regular expressions of value classes, described in [A.7.4](#a74-value-class-words).
- `hed_string`: the characters that no HED string may contain, the characters that structure a HED string, and the characters of a tag, described in [A.7.5](#a75-hed-string-characters).

### A.7.2. Set entries

Each entry of `sets` has the fields below.

| Field         | Type                           | Meaning                                                                                                                                                                                                                  |
| ------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `regex`       | string                         | A regular expression that matches exactly one character of the set (one UTF-16 code unit in JavaScript). A validator anchors it at both ends, `^(?:regex)$`, when it tests a single character.                           |
| `description` | string                         | The description shown in the table of 2.2.                                                                                                                                                                               |
| `excludes`    | array of one-character strings | Optional. Characters that a set this one is built from includes and this one leaves out; `regex` matches none of them.                                                                                                   |
| `tests`       | object                         | Optional. Its `valid` array lists characters that `regex` MUST match and its `invalid` array characters that `regex` MUST NOT match; both are checked in Python and JavaScript by `scripts/generate_character_table.py`. |

### A.7.3. Names and value class defaults

A name in an `allowedCharacter` declaration resolves to a key of `sets`, an alias in `aliases`, or a single character, which names itself (see [A.1.4.1. allowedCharacter](#a141-allowedcharacter)). The objects that state these rules have the fields below.

| Field              | Object                          | Type           | Meaning                                                                                                                                                                          |
| ------------------ | ------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rule`             | `literal_names`                 | string         | The rule that any single character is an `allowedCharacter` name for itself.                                                                                                     |
| `regex_for`        | `literal_names`                 | string         | The regular expression of such a name: the character, regex-escaped.                                                                                                             |
| `standard_version` | `declaration_wins_from`         | string `X.Y.Z` | The first standard schema version (`8.5.0`) from which, and in library schemas partnered with it or later, the names a value class declares define the characters of its values. |
| `rule`             | `declaration_wins_from`         | string         | The text of that rule and of the reason earlier standard schemas use `value_class_defaults`.                                                                                     |
| `from`             | entry of `value_class_defaults` | string `X.Y.Z` | The first standard schema version to which the entry applies.                                                                                                                    |
| `sets`             | entry of `value_class_defaults` | array of names | The names, each resolved as above, whose union is the characters of the value class.                                                                                             |

`value_class_defaults` is keyed by standard value class (`dateTimeClass`, `nameClass`, `numericClass`, `posixPath`, `textClass`). Each value is an array of entries in increasing order of `from`. For a standard schema version before `declaration_wins_from.standard_version`, a validator applies the last entry whose `from` is less than or equal to that version. The last entry of each class is the table of [A.1.3. Value classes](#a13-value-classes); the earlier entries are described in [B.3. Differences for earlier schema versions](./Appendix_B.md#b3-differences-for-earlier-schema-versions).

### A.7.4. Value class words

`value_class_words` is keyed by value class (`dateTimeClass`, `numericClass`). Its entries check a whole value, after the value's characters have been checked against its value class.

| Field         | Type   | Meaning                                                                                                                                     |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `regex`       | string | A regular expression, anchored with `^` and `$`, that a whole value of the class MUST match.                                                |
| `description` | string | The format in words, including any check that follows the expression (for `dateTimeClass`, that the date exists in the Gregorian calendar). |
| `tests`       | object | Optional. Its `valid` array lists values that `regex` MUST match and its `invalid` array values that `regex` MUST NOT match.                |

### A.7.5. HED string characters

`hed_string` has three keys, `forbidden`, `structural`, and `tag_chars`, each an object. Their fields are below.

| Field                 | Object       | Type                                 | Meaning                                                                                                            |
| --------------------- | ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `forbidden`           | `hed_string` | object                               | The characters that no HED string may contain anywhere, whatever the value class.                                  |
| `characters`          | `forbidden`  | array of one-character strings       | The forbidden characters outside `code_ranges`.                                                                    |
| `code_ranges`         | `forbidden`  | array of `[low, high]` integer pairs | Inclusive ranges of forbidden code points.                                                                         |
| `regex`               | `forbidden`  | string                               | A regular expression that matches any single forbidden character: the union of `characters` and `code_ranges`.     |
| `description`         | `forbidden`  | string                               | Text for human readers.                                                                                            |
| `structural`          | `hed_string` | object                               | The characters that give a HED string its structure; a value may contain one only where its value class allows it. |
| `comma`               | `structural` | one-character string                 | Separates tags and tag groups.                                                                                     |
| `group_open`          | `structural` | one-character string                 | Opens a tag group.                                                                                                 |
| `group_close`         | `structural` | one-character string                 | Closes a tag group.                                                                                                |
| `column_open`         | `structural` | one-character string                 | Opens a sidecar column reference.                                                                                  |
| `column_close`        | `structural` | one-character string                 | Closes a sidecar column reference.                                                                                 |
| `placeholder`         | `structural` | one-character string                 | The placeholder that a value replaces.                                                                             |
| `path_separator`      | `structural` | one-character string                 | Separates the nodes of a tag path.                                                                                 |
| `namespace_separator` | `structural` | one-character string                 | Separates a namespace prefix from a tag.                                                                           |
| `description`         | `structural` | string                               | Text for human readers.                                                                                            |
| `tag_chars`           | `hed_string` | object                               | The characters of a schema node name and of a tag extension.                                                       |
| `sets`                | `tag_chars`  | array of names                       | The names, resolved as in [A.7.3](#a73-names-and-value-class-defaults), whose union is those characters.           |
| `description`         | `tag_chars`  | string                               | Text for human readers.                                                                                            |
