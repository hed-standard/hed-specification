# 7. Library schemas

A HED library schema contains the vocabulary terms needed for annotation in a specialized area. An example of such a library is the [HED SCORE schema](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/README.md) for annotation of EEG by clinical neurologists. All officially released HED schemas, whether standard or library, are hosted on the [hed-standard/hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository and can be viewed using the [hed-schema-browser](https://www.hedtags.org/hed-schema-browser). Library schemas were introduced in HED specification version `3.2.0`.

## 7.1. Why library schemas?

The variety and complexity of events in electrophysiological experiments make full documentation challenging. As more experiments move out of controlled laboratory environments and into less controlled virtual and real-world settings, the terminology required to adequately describe events and other experimental metadata has the potential to grow exponentially.

In addition, experiments in any given subfield can create pressures to add overly-specific terms and jargon to the schema hierarchy - for example, adding musical terms to tag events in music-based experiments, video markup terms for experiments involving movie viewing, traffic terms for experiments involving virtual driving, and so forth.

Clinical fields using neuroimaging also have their own specific vocabularies for describing data features of clinical interest (e.g., seizure, sleep stage IV). Including these discipline-specific terms quickly makes the standard HED schema unwieldy and less usable by the broader user community.

Third generation HED addressed the problem of vocabulary bloat by introducing **HED library schemas** to organize discipline-specific terminology. To use a programming analogy, when programmers write a Python module, the resulting code does not become part of the Python language or core libraries. Instead, the module becomes part of a library used in conjunction with core modules of the programming language.

## 7.2. Unpartnered library schemas

HED library schemas were originally designed as standalone vocabularies. These **unpartnered library schemas** were self-contained schemas with all the needed schema attributes and properties. In practice however, these "standalone" schemas almost always required tags from the standard schema, and library schemas either had to duplicate items from the standard schema or use namespaces so that each schema could be used independently in an annotation without conflicts. See [3.1.1. Schema versions](./03_HED_formats.md#311-schema-versions) and [3.1.2 Version combinations](./03_HED_formats.md#312-version-combinations) for more detailed explanations of namespaces and merge groups.

Using tags from schemas in different namespaces for annotation proved to be inconvenient. Tags from schemas in different namespaces must have different prefixes when used in annotation. In the following example `score_1.0.0` is in the default namespace and `8.4.0` is in the `ts:` namespace:

````{admonition} A version specification of the score library version 1.0.0 with standard schema version 8.4.0.
```text
["score_1.0.0", "ts:8.4.0"]
```
````

Annotations using this version specification must prefix every tag from the standard schema with `ts:` (e.g., `ts:Sensory-event`). Partnered library schemas were introduced to avoid the namespace complication for annotators in most practical use cases.

## 7.3. Partnered library schemas

A **partnered library schema** is tied to a specific version of the HED standard schema and designed to be used with its partner as a unified vocabulary in a single namespace. A given library schema version is either **partnered** or **unpartnered** depending on whether its header has the `withStandard="x.y.z"` attribute. Here `x.y.z` corresponds to the semantic version of a standard schema >= `8.2.0`. Unpartnered library schemas do not have a `withStandard` attribute. The filenames for library schemas are the same regardless of partnership.

### 7.3.1. Partnered file formats

HED schema files (including library schema files) can be represented in one of 4 equivalent formats: MediaWiki, TSV, XML, and JSON. The hed-python tools read each of these formats into a common object format and can then convert to any other equivalent formats.

**MediaWiki** format has one line per tag, is relatively easy to read, and clearly displays the hierarchy structure for human readers. Many developers work in this format after the tag vocabulary has been established.

**TSV** is a multi-file format (13 TSV files for schema versions >= `8.4.0`) that represents each type of element in a spreadsheet. Developers often use TSV format in the initial development of a library vocabulary, because they only need to focus on the `_Tags.tsv` spreadsheet which contains the library tags. Most of the other TSV files will be empty or fixed after the initial setup.

**XML** is hard to read, so humans almost never use this format directly, but instead, convert XML to MediaWiki or TSV. XML is easily parsed by tools and is the standard format for tools in the HED ecosystem.

**JSON** is a flattened format that is useful for AI agents, as its tags are in a top-level dictionary.

### 7.3.2. Schema filenames

The canonical filenames for the standard schemas are `HEDx.y.z.mediawiki`, `HEDx.y.z.xml`, and `HEDx.y.z.json` for the MediaWiki, XML, and JSON formats, respectively. The `x.y.z` represents the semantic version (e.g., `8.4.0`). The filenames for TSV format are of the form `HEDx.y.z_www.tsv`, where `www` designates the spreadsheet type (e.g., `HED8.4.0_Tags.tsv`).

Library schemas have the form `HED_libname_x.y.z.mediawiki`, `HED_libname_x.y.z.xml`, and `HED_libname_x.y.z.json` for the MediaWiki, XML, and JSON formats, respectively. The `x.y.z` represents the semantic version (e.g., `1.1.0`) and `libname` is the name of the library in lower case (e.g., `HED_lang_1.1.0.mediawiki` is version `1.1.0` of the language library schema `lang`). The TSV format for library schemas follows the `HED_libname_x.y.z_www.tsv` pattern.

```{admonition} Library schema filenames don't show partnership.
---
class: warning
---
Whether a schema file represents a partnered or unpartnered schema can ONLY be determined by the schema header not by the filename. If the `withStandard` attribute is present in the schema header, it is partnered. If the `withStandard` is absent it is unpartnered.
```

The following example shows the header for the `.mediawiki` form of a partnered library schema.

````{admonition} MediaWiki header for TESTLIB library 2.0.0 partnered with 8.4.0 (merged).
```html
HED library="testlib" version="2.0.0" withStandard="8.4.0"
```
````

```{admonition} Library schema filenames don't show merge status.
---
class: warning
---
Whether a schema library file has been stored in merged or unmerged form can ONLY be determined by the schema header:

If the `unmerged="true"` attribute is present in the schema header, it is unmerged. If absent, it is merged.
```

### 7.3.3. Merged vs unmerged

There are several significant differences between merged and unmerged partnered library schema formats:

- An unmerged schema has the `unmerged="true"` attribute in its header line. The merged version does not have an `unmerged` attribute in its header.

- An unmerged schema **must** have prologue and epilogue sections that appropriately explain the purpose of the library schema. The contents of these prologue and epilogue sections become the prologue and epilogue, respectively, in the merged schema. The prologue and epilogue of the standard schema are omitted in the merged schema.

- With the exception of the prologue and epilogue sections, the merged form of library schema `xxx` has the `inLibrary=xxx` attribute on every schema element that is in the library. Here `xxx` is the name of the library. The unmerged form has no `inLibrary` attributes. The `inLibrary` attribute is added or removed automatically when a schema file is written depending on whether the output is being written in merged or unmerged format.

- The schema properties section of an unmerged library schema should always be empty except for its section header. The properties section of a merged schema will have only the standard schema properties.

- An unmerged schema should only include content in the auxiliary sections (unit classes, units, unit modifiers, value classes, and schema attributes) and the extra sections (Sources, Prefixes, and External annotations) that it explicitly extends. Otherwise, the section is present and empty except for its section header in that format. A tool writing the schema includes every section; see [3.1.4.10. Sources, prefixes, and external annotations](./03_HED_formats.md#31410-sources-prefixes-and-external-annotations) for the cases where a reader must accept a file that omits the extra sections. The merged version will have all of the section values from both the library schema and its partner.

- In an unmerged schema, nodes with the `rooted=XXX` schema attribute must be top-level tags, and `XXX` must correspond to a node in the standard schema. In the merged schema, nodes with the `rooted=XXX` schema attribute are placed directly under the standard schema node `XXX`.

The following excerpt from an unmerged TESTLIB library schema in MediaWiki format shows a library schema node (`Data-mode`) rooted to `Statistical-value` in the standard schema.

````{admonition} Example of a rooted node in an unmerged schema in MediaWiki format.
```html
                      . . .
'''Data-mode''' <nowiki>{rooted=Statistical-value}[A value that occurs most often in data.]</nowiki>
* <nowiki># {takesValue, valueClass=numericClass}</nowiki>
                      . . .
```
````

In MediaWiki format, the number of asterisks (\*) indicates how deep in the hierarchy that node is. The single `*` in front of the `#` indicates that this element is directly below its top-level ancestor (`'''Data-mode'''`). However, `Data-mode` has the `rooted=Statistical-value` attribute. In the unified tree representation provided by the merged schema, `Data-mode` will be one level below the `Statistical-value` tag of the standard schema, which is three levels below its top-level ancestor (`'''Property'''`):

````{admonition} When a library is merged with the standard schema, the indentation levels are adjusted.
```html
                      . . .
*** Statistical-value <nowiki>{extensionAllowed}[A value based on or employing the principles of statistics.]</nowiki>
                       . . .
**** Data-minimum <nowiki>[The smallest possible quantity.]</nowiki>
***** <nowiki># {takesValue, valueClass=numericClass}</nowiki>
**** Data-mode <nowiki>{inLibrary=testlib, rooted=Statistical-value}[A value that occurs most often in data.]</nowiki>
***** <nowiki># {takesValue, valueClass=numericClass, inLibrary=testlib}</nowiki>
**** Probability <nowiki> [A measure of the expectation of the occurrence of a particular event.]</nowiki>
***** <nowiki># {takesValue, valueClass=numericClass}</nowiki>
                      . . .
```
````

Similar differences occur between the merged and unmerged versions in other file formats.

### 7.3.4. Partnered attributes

To support partnered library schema the following items were introduced in HED standard schema `8.2.0`:

| Name           | Type              | Role                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `withStandard` | Header attribute  | <ul><li>Indicates that this is a partnered library schema.</li><li>Its value is the version of its standard schema partner.</li></ul>                                                                                                                                                                                                                                                                      |
| `unmerged`     | Header attribute  | <ul><li>Its presence indicates that this schema contains only library information.</li><li>Its value is either "true" or "false" (case-insensitive).</li><li>If "false", the attribute should be omitted.</li></ul>                                                                                                                                                                                        |
| `inLibrary`    | Element attribute | <ul><li>Indicates that this element is in the library schema.</li><li>Its value is the library name in lowercase.</li><li>The attribute appears only in merged schemas.</li><li>An element contributed by more than one library in a merge group carries one `inLibrary` value per contributing library, and the attribute is excluded from element compatibility comparisons.</li></ul>                   |
| `rooted=XXX`   | Node attribute    | <ul><li>Indicates that this library schema node is to appear directly under<br/> standard schema node `XXX` in the merged schema.</li><li>A node with the `rooted` attribute must be<br/>a top-level node in the unmerged schema.</li></ul>                                                                                                                                                                |
| `reserved`     | Node attribute    | <ul><li>Indicates that this node has special meaning or function.</li><li>**Can only appear in standard schemas or unpartnered library schemas.**</li><li>Its use in an unmerged partnered library schema is a [SCHEMA_LIBRARY_INVALID](./Appendix_B.md#schema_library_invalid) error.</li><li>In merged partnered library schemas it cannot appear in an element with the `inLibrary` attribute</li></ul> |

### 7.3.5. Motivation for partners

Partnered library schemas are the strongly preferred format for HED libraries for consistency and elimination of redundancy. This section explains why partnered library schemas are preferred.

#### 7.3.5.1. Auxiliary consistency

An unpartnered library schema must duplicate the [auxiliary schema sections](./Appendix_A.md#a1-auxiliary-schema-sections) appearing in standard schemas, introducing the possibility of inconsistency in usage or definition between the library schema and standard schemas. A partnered library schema automatically inherits its standard partner's auxiliary sections, assuring consistent handling by tools and preventing the introduction of inconsistently handled attributes.

Although unpartnered library schemas may add additional items to the auxiliary sections, HED tools only guarantee support of standard schema auxiliary items requiring special handling. **Thus, addition of items in the auxiliary sections of a library schema is discouraged.**

#### 7.3.5.2. Reserved tags handling

Several tags in the standard schema have the `reserved` attribute: each has a specified meaning in the HED ecosystem that individual schemas, library schemas included, cannot redefine. The nine structural reserved tags (`Definition`, `Def`, `Def-expand`, `Onset`, `Offset`, `Inset`, `Delay`, `Duration`, and `Event-context`) implement definitions and events of temporal extent; see [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags) for their rules. By partnering with a standard schema, a library schema is assured of having HED support for key features such as events of temporal extent and definitions.

#### 7.3.5.3. Annotation conciseness

The most common use case for library schemas in annotation requires tags from both a standard schema and a library schema, thus requiring a namespace prefix (e.g., `xx:`) on the tags from one of the schemas when unpartnered library schemas are used.

Because a partnered library schema is merged with a standard schema to form a single, unified schema, users can annotate data without the `xx:` namespace prefix. The `xx:` is still needed when multiple incompatible library schemas are used together. See [7.3.6 Lazy partnering](./07_Library_schemas.md#736-lazy-partnering) for more information on compatibility.

#### 7.3.5.4. Library searches

The subtrees appearing in the library schemas are often elaborations of a particular term in the standard schema. However, if the library schema terms are not in the appropriate standard schema hierarchy, HED search cannot be leveraged to find these elaborations by searching for a more general standard schema term.

#### 7.3.5.5. Suggested tags

Unpartnered library schemas cannot use the `suggestedTag` or `relatedTag` attributes to suggest using particular tags from the standard schema, since the values of the tags must be in the schemas themselves. However, partnered library schemas can refer to tags in the standard schema using the `suggestedTag` or `relatedTag` attributes.

### 7.3.6. Lazy partnering

HED allows multiple partnered schemas from a merge group to be loaded into a namespace (unified vocabulary tree), provided that the schemas are compatible. We refer to this process as **lazy partnering**. Lazy partnering became available with standard schema `8.4.0`. The rules for lazy partnering were codified in HED specification `4.0.0`.

In the following example, all the library schemas are partnered with standard schema `8.4.0`. Library schemas `liba_1.0.0` and `libc_4.3.2` are merged in the default namespace, and library schemas `ac:libb_2.8.1` and `ac:exam_2.3.2` are merged in the `ac` namespace. The schema `sc:test_1.3.2` stays the same, and listing `8.4.0` adds nothing, since it is already the partner of `liba_1.0.0` and `libc_4.3.2`. If there are any conflicts during the merging process, an error is raised.

````{admonition} Example: Merging of multiple schemas.

```
     ['liba_1.0.0', 'ac:libb_2.8.1', 'libc_4.3.2', '8.4.0', 'sc:test_1.3.2', 'ac:exam_2.3.2']
```
````

The full set of rules governing merge groups and partnered combination is given in the rule table of [3.1.2.4. Partnered combinations](./03_HED_formats.md#3124-partnered-combinations). The subsections below give worked examples of version specifications that load and version specifications that fail, organized by the row groups of that table.

If an incompatible list of schemas is given, a [SCHEMA_LOAD_FAILED](./Appendix_B.md#schema_load_failed) error is generated.

```{admonition} Avoid new auxiliary section entries in library schemas.
---
class: warning
---
Auxiliary sections have information for HED tools, and new entries may require modification to
schema validation and analysis tools.

With the possible (and rare) exception of new `unitClasses` and `units`, partnered library schemas
usually have empty auxiliary sections except for the `prologue` and `epilogue`. The empty sections
are still written in every format; they are not removed from the file.

While new value class and schema attribute definitions are allowed in library schemas, this is strongly discouraged. If a new entry is needed, contact the HED Working Group (hed.maintainers@gmail.com) to see if the
entry might be added to the standard schema instead.
```

#### 7.3.6.1. Test schema examples

The worked examples in the following subsections use four test-only library schemas: **testconflict**, **testclash**, **testminimal**, and **testaux**. These schemas are maintained in the [hed-tests](https://github.com/hed-standard/hed-tests) repository (under `json_test_data/test_schemas/`) and are not released HED schemas. Their contents are fully controlled, so each example exercises exactly one rule of the rule table in [3.1.2.4. Partnered combinations](./03_HED_formats.md#3124-partnered-combinations). Each example mirrors a test case in that repository's `json_test_data/validation_test_data/SCHEMA_LOAD_FAILED.json`, keeping the specification and the validator test suites in sync.

| Schema versions                                                  | Standard schema partner (`withStandard`) |
| ---------------------------------------------------------------- | ---------------------------------------- |
| `testconflict_1.0.0`, `testconflict_1.1.0`, `testconflict_1.1.2` | None (unpartnered)                       |
| `testconflict_2.0.0`, `testconflict_2.1.0`, `testconflict_2.1.1` | `8.5.0`                                  |
| `testclash_1.0.0` through `testclash_19.0.0`                     | `8.5.0`                                  |
| `testminimal_1.0.0`                                              | None (unpartnered)                       |
| `testminimal_2.0.0`                                              | `8.4.0`                                  |
| `testminimal_2.1.0`                                              | `8.5.0`                                  |
| `testaux_1.0.0`                                                  | `8.5.0`                                  |

The examples rely on the following facts about these libraries:

- `testconflict_2.1.0` is `testconflict_2.0.0` plus one added tag. `testconflict_2.1.1` differs from `testconflict_2.1.0` only in one revised tag description (a patch-level change).
- `testconflict_2.0.0` declares the top-level tags `Shared-item`, `Attribute-item` (with `suggestedTag=Object-one`), `Description-item`, `Anchor-item` (with child `Nested-item`), `Placeholder-item` (with a `#` child), and `Rooted-tag` (with `rooted=Event`), whose children are `Rooted-one` (with child `Deep-one`) and `Rooted-two`.
- Each `testclash` version declares its own `Clash-tag` subtree plus at most one probe element also declared by another test library, identical except for at most one controlled difference. Versions `1.0.0` through `12.0.0` probe tag elements declared by `testconflict_2.0.0`; the differences are tabulated in [7.3.6.5. Element compatibility examples](#7365-element-compatibility-examples). Versions `13.0.0` through `19.0.0` probe auxiliary elements declared by `testaux_1.0.0`; the differences are tabulated in [7.3.6.6. Auxiliary element examples](#7366-auxiliary-element-examples).
- `testminimal` declares only its own `Mini-tag` subtree, which is disjoint from the vocabularies of the other libraries.
- `testaux_1.0.0` declares one auxiliary element of each type - the unit class `auxUnits` (with units `auxunit` and `bigauxunit`), the unit modifier `auxMod`, the value class `auxClass`, and the schema attribute `auxAttribute` - plus the tags `Aux-measure` (which takes a value with `auxUnits` units) and `Aux-value` (which takes a value of the `auxClass` value class). Its vocabulary is disjoint from the other libraries and from the standard schema.

#### 7.3.6.2. Merge group examples

| Version specification                                            | Loads | Explanation                                                                                                                                             |
| ---------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `['testconflict_2.1.0', 'testclash_1.0.0', 'testminimal_2.1.0']` | Yes   | All three libraries are partnered with `8.5.0`, and their elements are either disjoint or identical, so they merge into a single unprefixed vocabulary. |
| `['8.4.0', 'sc:testconflict_2.1.0', 'ts:testminimal_1.0.0']`     | Yes   | Three merge groups (unprefixed, `sc:`, `ts:`) resolve independently; the standard schema partners of different groups do not have to agree.             |
| `['8.5.0', 'sc:8.4.0']`                                          | Yes   | A standard schema in its own namespace forms its own merge group, so the two standard versions do not conflict.                                         |
| `['testconflict_2.0.0', 'testconflict_2.0.0']`                   | No    | Duplicate schemas (the same name, whatever the version) cannot appear in the same merge group; an exact duplicate fails like two different versions.    |
| `['testconflict_2.0.0', 'testconflict_2.1.0']`                   | No    | Different versions of the same schema cannot appear in the same merge group, even though these two share the `8.5.0` partner and have no conflicts.     |
| `['8.5.0', 'sc:testconflict_2.0.0', 'sc:testminimal_2.0.0']`     | No    | The rules apply inside each namespace: the `sc` namespace has conflicting partners (`8.5.0` versus `8.4.0`), even though the default namespace is fine. |

#### 7.3.6.3. Standard partner examples

| Version specification                         | Loads | Explanation                                                                                                                                                                       |
| --------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `['testconflict_2.0.0']`                      | Yes   | A partnered library schema automatically includes its standard schema partner (`8.5.0`), so standard schema tags such as `Red` validate without the standard schema being listed. |
| `['8.5.0', 'testconflict_2.0.0']`             | Yes   | A standard schema matching the group partner is allowed and adds nothing to the merged result.                                                                                    |
| `['8.4.0', 'testconflict_2.0.0']`             | No    | A standard schema in a merge group must match the group partner; `testconflict_2.0.0` is partnered with `8.5.0`, not `8.4.0`.                                                     |
| `['testconflict_2.0.0', 'testminimal_2.0.0']` | No    | Partnered library schemas in a merge group must have the same partner; here the partners are `8.5.0` and `8.4.0`.                                                                 |
| `['8.4.0', '8.5.0']`                          | No    | Two bare standard schema versions give the unprefixed group two conflicting partners.                                                                                             |

#### 7.3.6.4. Unpartnered examples

| Version specification                                        | Loads | Explanation                                                                                                           |
| ------------------------------------------------------------ | ----- | --------------------------------------------------------------------------------------------------------------------- |
| `['8.4.0', 'sc:testconflict_2.1.0', 'ts:testminimal_1.0.0']` | Yes   | The unpartnered `testminimal_1.0.0` is alone in its own `ts` namespace, which is where an unpartnered schema must be. |
| `['8.5.0', 'testconflict_1.1.0']`                            | No    | The unpartnered `testconflict_1.1.0` cannot share the unprefixed merge group with another schema.                     |
| `['ts:testconflict_1.1.2', 'ts:testminimal_1.0.0']`          | No    | Two unpartnered library schemas cannot share a namespace; each needs its own.                                         |

#### 7.3.6.5. Element compatibility examples

Each example in this subsection loads `testconflict_2.0.0` together with one of the `testclash` versions `1.0.0` through `12.0.0`, each of which carries at most one probe element shared with `testconflict_2.0.0`, so each pair isolates a single element compatibility rule:

| Version specification                        | Probe element        | Difference from `testconflict_2.0.0`                                                                                                                                                                                                                                  | Loads |
| -------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `['testconflict_2.0.0', 'testclash_1.0.0']`  | `Shared-item`        | None: an identical copy. Identical shared elements are compatible, and the merged vocabulary keeps a single copy.                                                                                                                                                     | Yes   |
| `['testconflict_2.0.0', 'testclash_2.0.0']`  | `Attribute-item`     | The `suggestedTag` value is `Clash-one` instead of `Object-one`: the attribute values differ.                                                                                                                                                                         | No    |
| `['testconflict_2.0.0', 'testclash_3.0.0']`  | `Description-item`   | The description text differs.                                                                                                                                                                                                                                         | No    |
| `['testconflict_2.0.0', 'testclash_4.0.0']`  | `Nested-item`        | Declared at the top level instead of as a child of `Anchor-item`: the ancestor paths differ.                                                                                                                                                                          | No    |
| `['testconflict_2.0.0', 'testclash_5.0.0']`  | `Placeholder-item`   | Has no `#` child, while `testconflict`'s has one.                                                                                                                                                                                                                     | No    |
| `['testconflict_2.0.0', 'testclash_6.0.0']`  | `Rooted-tag`         | Declared as an ordinary top-level tag instead of with `rooted=Event`: the merged ancestor paths differ (`Rooted-tag` versus `Event/Rooted-tag`).                                                                                                                      | No    |
| `['testconflict_2.0.0', 'testclash_7.0.0']`  | `Rooted-tag`         | Declared with `rooted=Item` instead of `rooted=Event`: the same tag is anchored at different standard schema nodes.                                                                                                                                                   | No    |
| `['testconflict_2.0.0', 'testclash_8.0.0']`  | `Rooted-tag` subtree | `Rooted-tag` and its child `Rooted-one` are identical; `testclash` adds its own child `Rooted-three`. A shared element may have different non-`#` children, so the merged `Rooted-tag` has children `Rooted-one` (with `Deep-one`), `Rooted-two`, and `Rooted-three`. | Yes   |
| `['testconflict_2.0.0', 'testclash_9.0.0']`  | `Rooted-tag` subtree | The shared child `Rooted-one` carries a different description. The compatibility rules apply to shared children, so the changed shared child fails the merge even though the non-shared sibling `Rooted-three` would be allowed.                                      | No    |
| `['testconflict_2.0.0', 'testclash_10.0.0']` | `Rooted-tag`         | Identical, but its only child is `testclash`'s own `Rooted-four`: a shared element's children may be entirely disjoint.                                                                                                                                               | Yes   |
| `['testconflict_2.0.0', 'testclash_11.0.0']` | `Rooted-tag` subtree | The chain `Rooted-tag`/`Rooted-one` is identical; below it `testclash` declares `Deep-two` where `testconflict` declares `Deep-one`. The differing grandchildren are not shared, so the merged `Rooted-one` carries both.                                             | Yes   |
| `['testconflict_2.0.0', 'testclash_12.0.0']` | `Rooted-tag` subtree | The shared grandchild `Deep-one` carries a different description. Compatibility applies at every depth of a shared hierarchy.                                                                                                                                         | No    |

Two versions of one library are never compared element by element, because different versions of the same schema cannot appear in the same merge group: `['testconflict_2.1.0', 'testconflict_2.1.1']` fails to load on that rule alone. To use two versions together, give one its own namespace, for example `['testconflict_2.1.0', 'alt:testconflict_2.1.1']` (namespace names must be alphabetic, so a name such as `v2` is not allowed).

Any failing pair in this subsection can still be used together by giving one schema its own namespace. For example, `['testconflict_2.0.0', 'cl:testclash_2.0.0']` loads because the two `Attribute-item` declarations are in different merge groups and are never compared.

#### 7.3.6.6. Auxiliary element examples

The element compatibility rules apply to auxiliary elements (unit classes, units, unit modifiers, value classes, and schema attributes) exactly as they do to tags. The first example pairs `testconflict_2.0.0`, which declares no auxiliary elements, with `testaux_1.0.0` to show direct merging; each remaining example loads `testaux_1.0.0` together with one of the `testclash` versions `13.0.0` through `19.0.0`, so each pair isolates a single rule:

| Version specification                     | Probe element                   | Difference from `testaux_1.0.0`                                                                                                                                                        | Loads |
| ----------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `['testconflict_2.0.0', 'testaux_1.0.0']` | all auxiliary elements          | None shared: every `testaux` auxiliary element is new to the merge group. New unit classes with their units, unit modifiers, value classes, and schema attributes are merged directly. | Yes   |
| `['testaux_1.0.0', 'testclash_13.0.0']`   | all auxiliary elements          | None: identical copies. Identical shared auxiliary elements are compatible, and the merged vocabulary keeps a single copy of each.                                                     | Yes   |
| `['testaux_1.0.0', 'testclash_14.0.0']`   | unit `auxunit`                  | The `conversionFactor` value differs: the attribute values of a shared unit differ.                                                                                                    | No    |
| `['testaux_1.0.0', 'testclash_15.0.0']`   | unit class `auxUnits`           | The shared units are identical; `testclash` adds its own unit `smallauxunit`. New units under an existing unit class are merged if there are no conflicts.                             | Yes   |
| `['testaux_1.0.0', 'testclash_16.0.0']`   | value class `auxClass`          | The `allowedCharacter` value is `digits` instead of `letters`: the attribute values of a shared value class differ.                                                                    | No    |
| `['testaux_1.0.0', 'testclash_17.0.0']`   | schema attribute `auxAttribute` | Declared without `boolRange`: for schema attribute elements the properties are the attribute values that are compared.                                                                 | No    |
| `['testaux_1.0.0', 'testclash_18.0.0']`   | schema attribute `auxAttribute` | The description text differs.                                                                                                                                                          | No    |
| `['testaux_1.0.0', 'testclash_19.0.0']`   | unit modifier `auxMod`          | The `conversionFactor` value differs: the attribute values of a shared unit modifier differ.                                                                                           | No    |

## 7.4. Library schema design

Most library schema developers work with unmerged MediaWiki or unmerged TSV format. Developers should always validate the schema before converting to XML. Only validated versions of the schema should be uploaded to the GitHub [hed-schemas](https://github.com/hed-standard/hed-schemas) repository. The [online HEDtools](https://hedtools.org/hed/schemas) provide easy access to tools for schema validation, conversion, and comparison. More information about the development process is contained in the HED [Schema developers guide](https://www.hedtags.org/hed-schemas/developer_guide.html).

Developers of partnered library schemas should release new versions whenever HED updates its standard schema. This ensures that the partnered library schema benefits from the latest updates to HED features and tools.

If the update can be done without conflict, this update may be initiated as part of the release mechanism by the maintainers of the HED repositories.

### 7.4.1. General design rules

This section summarizes the general design rules for all library schema.

```{admonition} General design rules for HED library schema.
---
class: tip
---
1. **Follow naming conventions**:<br/>
A library schema must be given a name containing only lowercase alphabetic characters.
This name must appear in the schema header line in the required format.
<br>&nbsp;</br>
2. **Use semantic versioning**:<br/>
A library schema must use semantic versioning and follow the versioning update rules used by
the HED standard schema as specified in [3.1.3. Version updates](./03_HED_formats.md#313-version-updates).
<br>&nbsp;</br>
3. **Tag uniqueness**:<br/>
Every term must be unique within the library schema and must
conform to the rules for HED schema terms.
<br>&nbsp;</br>
4. **Have a meaningful prologue**:<br/>
The schema should include a prologue section giving an overview, purpose and scope
of the library schema.
<br>&nbsp;</br>
5. **Have a meaningful epilogue**:<br/>
The schema should include an epilogue section containing reference, citation, and license information.
<br>&nbsp;</br>
6. **Be understandable**:<br/>
Schema terms should be readily understood by most users. The terms should not be ambiguous and
should be meaningful in themselves without reference to their position in the schema hierarchy.
<br>&nbsp;</br>
7. **Be well-organized**:<br/>
If possible, no schema sub-tree should have more than 7 direct subordinate sub-trees.
<br>&nbsp;</br>
8. **Maintain subtree orthogonality**:<br/>
Terms that are used independently of one another should be in different sub-trees (orthogonality).
<br>&nbsp;</br>
9. **Enforce is-a relationship between child nodes and their parents**:<br/>
Every node in a HED hierarchy must be a subclass of its parent node.
This is required for HED search generalizability.

```

Rules 1 through 5 are enforced by validators, while rules 6 through 9 are the responsibility of the schema designers and review committees.

In general, library schema developers should avoid adding schema terms that duplicate those found in the latest HED standard schema at the time of release. For partnered library schemas this is a strict requirement: the unmerged library schema cannot contain a tag that appears in its standard schema partner ([SCHEMA_LIBRARY_INVALID](./Appendix_B.md#schema_library_invalid)); the merged form necessarily contains all of its partner's tags. Library schema developers should also try to avoid overlap of terms found in other schema libraries.

All HED schemas, including library schemas, must use [semantic versions](https://semver.org/) and adhere to the rules specified in [3.1.3. Version updates](./03_HED_formats.md#313-version-updates).

If your application requires schema classes that are not available in the standard HED schema and would like these classes to be supported, please make a request using the [issues](https://github.com/hed-standard/hed-schemas/issues) forum of the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository.

### 7.4.2. Unpartnered design rules

Normally, a new library schema should be partnered with the latest version of the standard schema. Unpartnered schema creation should be avoided except in rare cases. Unpartnered schemas should copy the `Properties` section of the most recent standard schema, since these properties define the structure of the schema itself. An unpartnered schema must also include the auxiliary sections from the standard HED schema (schema attributes, unit classes, unit modifiers, and value classes) that are needed to support the behavior of its tags; otherwise the schema cannot be validated and used by the tools of the HED ecosystem. No changes should be made to the copied items: HED tools support the auxiliary classes of the standard schema, but in general do not support special handling of added classes beyond basic verification.

### 7.4.3. Partnered design rules

Partnered library schemas are now the recommended format for the reasons listed in [Motivation for partners](./07_Library_schemas.md#735-motivation-for-partners). The following design rules are specifically meant for partnered library schemas. Developers usually work on their library schemas in either unmerged MediaWiki or unmerged TSV format because these formats are concise and easy to edit. The [HED online tools](https://hedtools.org/hed) provide online tools for converting from one schema format to all formats in merged or unmerged forms.

```{admonition} Design rules specific to partnered HED library schemas.
---
class: tip
---
1. **Check for overlap**:<br/>
The terms in the partnered library schema must not duplicate terms present in its partnered
standard schema.
<br>&nbsp;</br>
2. **Use the latest released version of the standard schema**:<br/>
A partnered library schema should always use the latest version of the HED schema
available at the time of its release. While in development a partnered library schema may be partnered with a prerelease version of the standard schema.
<br>&nbsp;</br>
3. **The auxiliary sections of the unmerged partnered library schema are usually empty**:<br/>
The auxiliary sections of an unmerged partnered library schema (e.g., schema attributes, unit classes, unit modifiers, and value classes) should be empty
unless a new item is added to a section, in which case only that item should appear.
<br>&nbsp;</br>
4. **Seek reviews early in the process**:<br/>
Any additions to the auxiliary sections must be reviewed by the HED Working Group to
determine what requirements the additions would impose on downstream tools.

```

It is recognized that HED standard and library schemas will both evolve and that additions or tag reorganizations may cause conflicts. These conflicts must be resolved as they occur. In general the standard schema takes precedence over any library schema in resolving these conflicts.

## 7.5. Library schemas in BIDS

By far the most common use case is to tag events using a standard HED schema (preferably the latest one) available in the `standard_schema/hedxml` directory of the `hed-schemas` repository of the `hed-standard` organization on GitHub. The standard schemas are available at: [https://github.com/hed-standard/hed-schemas/tree/main/standard_schema](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema).

The **official library schemas** are available at [https://github.com/hed-standard/hed-schemas/tree/main/library_schemas](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas).

Standard schemas are referenced by their version number (e.g., `8.1.0`), while library schema are referenced by a combination of library name and version number (e.g., `score_1.0.0`).

For BIDS datasets, the versions of the HED schema are specified by the `HEDVersion` field of the BIDS `dataset_description.json` file. The schema versions in this section's examples are historical: SCORE `1.0.0` (unpartnered) and SCORE `1.1.0` (partnered) are used to illustrate the difference partnering makes for annotators. The following example specifies that version `8.1.0` of the standard HED schema is to be used in addition to `score` library schema version `1.0.0`.

````{admonition} Illustration of using the namespace prefix for tagging.
---
class: tip
---
The `dataset_description.json` file contains:

```json
{
  "Name": "A great experiment",
  "BIDSVersion": "1.8.0",
  "HEDVersion": ["8.1.0", "sc:score_1.0.0"]
}
```

A typical annotation is:

```text
"Data-feature, sc:Photomyogenic-response, sc:Wicket-spikes"
```
````

Based on the above description tools will download:

1. The standard HED schema:\
   [https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.1.0.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.1.0.xml).
2. The HED `score` library schema version `1.0.0`:\
   [https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_1.0.0.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_1.0.0.xml).

In the dataset annotations for the above example, tags drawn from the score schema would be prefixed with `sc:`, where `sc` is the namespace name chosen to distinguish tags from the additional schema.

SCORE version `1.0.0` is not partnered, so the HED version specification had to include both the library and standard schema versions. In contrast, SCORE version `1.1.0` is partnered with HED standard schema `8.2.0`, so no namespace prefixes are needed as shown in the following example:

````{admonition} **Example:** An example specification of HED version for a partnered schema.
---
class: tip
---
The `dataset_description.json` file contains:

```json
{
  "Name": "A great experiment",
  "BIDSVersion": "1.8.0",
  "HEDVersion": "score_1.1.0"
}
```

A typical annotation is:

```text
"Data-feature, Photomyogenic-response, Wicket-spikes"
```
````
