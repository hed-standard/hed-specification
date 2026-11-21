# 2. HED terminology

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this specification are to be interpreted as described in \[[RFC2119](https://www.ietf.org/rfc/rfc2119.txt)\].

This specification uses a list of terms and abbreviations whose meaning is clarified here. Note: We here hyphenate multi-word terms as they appear in HED strings themselves; in plain text usage they may not need to be hyphenated. Starred variables [\*] correspond to actual HED tags.

## 2.1. Definitions

### Agent [\*]

A person or thing, living or virtual, that produces (or appears to participants to be ready and capable of producing) specified effects. Agents include the study participants from whom data is collected. Virtual agents may be human or other actors in virtual-reality or augmented-reality paradigms or on-screen in video or cartoon presentations (e.g., an actor interacting with the recorded participant in a social neuroscience experiment, or a dog or robot active in a live action or animated video).

### Anchor

The [definition](#definition-) that an `Onset`, `Offset`, or `Inset` group refers to, written in the group as a `Def` tag or as the equivalent `Def-expand` group. The anchor identifies the event process that the group starts, ends, or marks.

### Assembled annotation

The [HED string](#hed-string) for one row of a [table](#table), formed by combining the row's entry in the `HED` column with the [sidecar](#sidecar) annotations of the row's other columns.

### Condition-variable [\*]

An aspect of the experiment that is set or manipulated during the experiment to observe an effect or to manage bias. Condition variables are sometimes called independent variables.

### Control-variable [\*]

An aspect of the experiment that is fixed throughout the study and usually is explicitly controlled.

### Dataset

A set of neuroimaging and behavioral data acquired for a purpose of a particular study. A dataset consists of data recordings acquired from one or more subjects, possibly from multiple sessions and sensor modalities. A dataset is often referred to as a study.

### Definition [\*]

A name given to a group of tags, so that an annotation can refer to the whole group with a `Def` tag. A definition is written as a [tag group](#tag-group) that contains a `Definition` tag.

### Event [\*]

Something that happens during the recording or that may be perceived by a participant as happening, to which a time of occurrence (most typically onset or offset) can be identified. Something expected by a participant to happen at a certain time that does not happen can also be a meaningful recording event. The nature of other events may be known only to the experimenter or to the experiment control application (e.g., undisclosed condition changes in task parameters).

### Event-context [\*]

In general, context is the set of circumstances or background information that helps explain or gives meaning to what is happening at a specific point in time. In HED, the event context specifically means something ongoing that started at another point in time (such as the display of an image that started earlier but continues to be displayed at this time).

### Event marker

A time point relative to the experimental timeline that can be associated with an annotation. Often such a marker indicates a transition point for some underlying event process.

### Event-stream [\*]

A named sequence of events such as all the events that are face stimuli or all of the events that are participant responses.

### Experiment-participant [\*]

A living agent, particularly a human from whom data is acquired during an experiment, though in some paradigms other human participants may also play roles.

### Experimental-trial [\*]

A contiguous data period that is considered a unit used to observe or measure something, typically a data period including an expected event sequence that is repeated many times during the experiment (possibly with variations). Example: a repeating sequence of stimulus presentation, participant response action, and sensory feedback delivery events in a sensory judgment task.

### HED entity

An item of a HED schema that is assigned a [hedId](#hedid) and so has a counterpart in the [HED ontology](#hed-ontology). The HED entities of a schema are its [schema elements](#schema-element), its [schema attributes](#schema-attribute), its [schema properties](#schema-property), and its three [structural elements](#structural-element). The rows of the sources, prefixes, and external annotations sections are not HED entities: they have no `hedId`.

### HED ontology

The representation of the HED schemas as an ontology, which supports semantic analysis and reasoning and links HED terms to the terms of other ontologies. Every [HED entity](#hed-entity) has a counterpart in the HED ontology, identified by its [hedId](#hedid): a [schema element](#schema-element) is a class, and a [schema attribute](#schema-attribute) or a [schema property](#schema-property) is a property.

### HED schema

A formal specification of the vocabulary and rules of a particular version of HED for use in annotation, validation, and analysis. A HED schema is given in one of four formats: MediaWiki, XML, JSON, or TSV. The top-level versioned HED schema is used for all HED event annotations. Named and versioned HED library schema may be used as well to make use of descriptive terms used by a particular research community. (For example, an experiment on comprehension of connected speech might annotate events using a grammatical vocabulary contained in a linguistics HED schema library.)

### HED string

A comma-separated list of HED tags and/or tag-groups.

### HED tag

A valid path along one branch of a HED vocabulary hierarchy. A valid long-form HED tag is a slash-separated path following the schema tree hierarchy from its root to a term along some branch. The short form of a tag is the last schema node of its path alone; a path that starts at a node between the root and the last node is an intermediate form. A value or an extension that follows the last schema node is kept in every form: `Weight/3 lbs` is a short form. No white space is allowed within terms themselves. For example, the long form of the HED tag specifying an experiment participant is: `Property/Agent-property/Agent-task-role/Experiment-participant`. The short form is `Experiment-participant`; the intermediate forms are `Agent-task-role/Experiment-participant` and `Agent-property/Agent-task-role/Experiment-participant`. HED tools should treat the long, intermediate, and short forms of a tag interchangeably.

### hedId

The permanent identifier of a [HED entity](#hed-entity): the prefix `HED_` followed by seven digits, as `HED_0012016` for the tag `Action`. The identifier stays the same when the entity is renamed or moved within the schema, and it identifies the entity in the [HED ontology](#hed-ontology). Schema elements, schema attributes, and schema properties carry it as the value of the `hedId` [schema attribute](#schema-attribute).

### Indicator-variable [\*]

An aspect of the experiment or task that is measured or calculated for analysis. Indicator variables, sometimes called dependent variables, can be data features that are calculated from measurements rather than aspects that are directly measured.

### Library schema

A [HED schema](#hed-schema) that holds the vocabulary of a particular research community, identified by a library name and a version (for example, `score_2.1.0`). A library schema is either a [partnered library schema](#partnered-library-schema) or an unpartnered one.

### Merge group

The set of schemas that a version specification lists in the same namespace. The namespace is the name; the merge group is the set of schemas listed under it. The schemas of a merge group are combined into one vocabulary.

### Namespace

A named partition of the vocabulary used when several schemas are combined. The schemas listed in a version specification with the same namespace name form one merge group; those listed with no namespace name form the merge group of the default namespace. Every unpartnered library schema must be alone in its own namespace.

### Namespace prefix

The namespace name followed by a colon (e.g., `sc:`), placed before a schema version in a version specification and before every tag drawn from that namespace in an annotation. Tags in the default namespace carry no prefix.

### Node

An entry of the schema section of a HED schema. A node is either a tag, which has a name, schema attributes, and a description and is placed under a parent node or at the top level, or a `#` placeholder, which has no name and stands for the value of its parent tag. A placeholder is not a tag: it defines no term, and its schema attributes (`takesValue`, `valueClass`, `unitClass`) describe the value that its parent tag takes. Nodes are the [schema elements](#schema-element) of the tag kind; each node, including a placeholder, is assigned a `hedId`. Earlier versions of this specification, and the descriptions in released schemas, also call a node a tag term.

### Parameter [\*]

An experiment-specific item, often a specific behavioral or computer measure, that is useful in documenting the analysis or assisting downstream analysis.

### Partnered library schema

A [library schema](#library-schema) whose header has the `withStandard` attribute, which names the version of the [standard schema](#standard-schema) that it is used with to form one vocabulary. A library schema without the attribute is *unpartnered* and is self-contained.

### Placeholder

The `#` character. In a schema it is the child [node](#node) of a tag that takes a value; in a [definition](#definition-) or a [sidecar](#sidecar) annotation it marks where a value is substituted. The *value* is the text that takes the place of the placeholder, as `3 s` in `Duration/3 s`.

### Recording [\*]

A continuous recording of data from an instrument in a single session without repositioning the recording sensors.

### Reserved tag

A tag with a specified meaning in the HED ecosystem that individual HED schemas cannot redefine. Standard schemas mark these tags with the `reserved` attribute. Some reserved tags determine the structure of an annotation. These tags and their validation rules are defined in the file [`docs/source/_static/reserved_tags.json`](https://github.com/hed-standard/hed-specification/blob/main/docs/source/_static/reserved_tags.json) of the specification repository, and all HED validators should use this file to handle them. Other reserved tags are defined for specific uses by downstream tools.

### Schema attribute

A named characteristic that may be assigned to the [schema elements](#schema-element) of a HED schema, such as `takesValue` or `conversionFactor`. Schema attributes are defined in the schema attributes section. A schema attribute that has the `elementDomain` property may also be assigned to a schema attribute, and `hedId` to a schema property. A schema attribute is a [HED entity](#hed-entity) but not a schema element: in the [HED ontology](#hed-ontology) it is a property, not a class.

### Schema element

A named item of the vocabulary that a HED schema defines, of one of five kinds: tag, unit class, unit, unit modifier, or value class. The `#` placeholder of a tag that takes a value is a schema element of the tag kind, although it has no name and is not itself a tag (see [Node](#node)). Schema elements are the items to which [schema attributes](#schema-attribute) are assigned; in the [HED ontology](#hed-ontology) each is a class under `HedElement`. Schema attributes, schema properties, and structural elements are [HED entities](#hed-entity) but not schema elements. The descriptions in released schemas sometimes use the word element for any HED entity.

### Schema property

A named characteristic of a [schema attribute](#schema-attribute): the kinds of schema element it may be assigned to, the kind of value it takes, and whether its value is inherited. Schema properties are defined in the schema properties section. A schema property is a [HED entity](#hed-entity) but not a schema element. The TSV format stores the schema properties in the file `AttributeProperty`.

### Schema section

One of the blocks of a HED schema file. The header, the prologue, and the epilogue are the three [structural elements](#structural-element). The *schema section* holds the nodes: the tags and their `#` placeholders. The *auxiliary sections* hold the other schema elements (unit classes with their units, unit modifiers, and value classes) and the definitions of the schema attributes and the schema properties. The *extra sections* (sources, prefixes, and external annotations) hold rows that are not HED entities: they have no [hedId](#hedid).

### Sidecar

A JSON structure, stored in a file or held in memory, that associates HED annotations with the columns of a [table](#table) and may hold [definitions](#definition-).

### Standard schema

The [HED schema](#hed-schema) that holds the base vocabulary of HED, identified by a version alone (for example, `8.5.0`). A [library schema](#library-schema) holds additional vocabulary.

### Structural element

One of the three parts of a HED schema that describe the schema itself and hold none of its vocabulary: the header, which gives the version of the schema and, for a library schema, its library name; the prologue, which introduces the schema and its purpose; and the epilogue, which gives license information, acknowledgments, and references. Each is one of the [schema sections](#schema-section) and is a [HED entity](#hed-entity). A structural element is not a [schema element](#schema-element): it defines no term, and no [schema attribute](#schema-attribute) is assigned to it.

### Table

An arrangement of rows and columns that carries HED annotations in a `HED` column, in an associated sidecar, or in both. A table may be stored as a tabular (`.tsv`) file, as a spreadsheet, or in a container such as an NWB table. A table that has an `onset` column or its equivalent, such as the NWB `timestamp` column, is a *timeline table*, such as the contents of a BIDS `events.tsv` file; any other table is a *descriptor table*, such as the contents of a BIDS `participants.tsv` file.

### Tag extension

A term that a user adds as a child of an existing schema [node](#node), as a more specific term for an item already in the schema, as `Helicopter` in `Aircraft/Helicopter`. A tag extension is not a [value](#placeholder).

### Tag-group

One or more valid, comma-separated HED tags enclosed in parentheses to indicate that these tags belong together. Tag-groups may contain arbitrary nestings of other tags and tag-groups.

### Task [\*]

A set of structured activities performed by the participant that are integrally related to the purpose of the experiment. Tasks often include observations and responses to sensory presentations as well as specified actions in response to presented situations.

### Temporal scope

The time interval between the start and end of an event process. Often the start time is annotated with the `Onset` tag, and the end time is annotated with the `Offset` tag. Since in practical terms the time is measured in discrete samples, the temporal scope includes the start time sample but does not include the end time sample.

### Time-block [\*]

A contiguous portion of the data recording during which some aspect of the experiment is fixed or noted.

### Top-level tag group

A [tag group](#tag-group) that is not nested inside another tag group.

### Version specification

The schema version, or the list of schema versions, that names the HED schemas used for a set of annotations, as `8.5.0` or `['8.4.0', 'sc:score_2.1.0']`. A version in the list may be preceded by a [namespace prefix](#namespace-prefix).

## 2.2. Character sets and restrictions

The types of characters referred to in this specification are:

<!-- character-sets:begin -->

| Name            | Description                                                                       |
| --------------- | --------------------------------------------------------------------------------- |
| `alphanumeric`  | `letters` and/or `digits`                                                         |
| `ampersand`     | ASCII code 38                                                                     |
| `ascii`         | utf-8 codes 0 to 127 (single byte)                                                |
| `asterisk`      | ASCII code 42                                                                     |
| `at-sign`       | ASCII code 64                                                                     |
| `backslash`     | ASCII code 92                                                                     |
| `blank`         | ASCII code 32                                                                     |
| `caret`         | ASCII code 94                                                                     |
| `colon`         | ASCII code 58                                                                     |
| `comma`         | ASCII code 44                                                                     |
| `digits`        | 0-9                                                                               |
| `dollar`        | ASCII code 36                                                                     |
| `double-quote`  | ASCII code 34                                                                     |
| `equals`        | ASCII code 61                                                                     |
| `exclamation`   | ASCII code 33                                                                     |
| `forward-slash` | ASCII code 47                                                                     |
| `greater-than`  | ASCII code 62                                                                     |
| `hyphen`        | ASCII code 45                                                                     |
| `left-paren`    | ASCII code 40                                                                     |
| `less-than`     | ASCII code 60                                                                     |
| `letters`       | `lowercase` and/or `uppercase`                                                    |
| `lowercase`     | ASCII characters a-z                                                              |
| `name`          | `alphanumeric`, `hyphen`, `underscore`, `nonascii`                                |
| `newline`       | ASCII code 10 (linefeed)                                                          |
| `nonascii`      | utf-8 codes 160 and above (multi-byte)                                            |
| `number-sign`   | ASCII code 35                                                                     |
| `percent-sign`  | ASCII code 37                                                                     |
| `period`        | ASCII code 46                                                                     |
| `plus`          | ASCII code 43                                                                     |
| `printable`     | ASCII codes 32 to 126                                                             |
| `question-mark` | ASCII code 63                                                                     |
| `right-paren`   | ASCII code 41                                                                     |
| `semicolon`     | ASCII code 59                                                                     |
| `single-quote`  | ASCII code 39                                                                     |
| `slash`         | Alias of `forward-slash`.                                                         |
| `tab`           | ASCII code 09                                                                     |
| `text`          | `printable` and/or `nonascii` excluding comma, square brackets, and curly braces. |
| `tilde`         | ASCII code 126                                                                    |
| `underscore`    | ASCII code 95                                                                     |
| `uppercase`     | ASCII characters A-Z                                                              |
| `value-text`    | `text` excluding left and right parentheses, number sign, and tilde.              |
| `vertical-bar`  | ASCII code 124                                                                    |

<!-- character-sets:end -->

`text` together with the comma is the character set of the prologue, the epilogue, and the element descriptions of a schema. `value-text` is the textClass character set: the characters a value may contain without changing the structure of the HED string it is substituted into.

A schema names these sets in its `allowedCharacter` attributes (see [A.1.4.1. allowedCharacter](./Appendix_A.md#a141-allowedcharacter)). An `allowedCharacter` name is a name from this table, an alias listed in it, or a single character, which names itself: `allowedCharacter=T` allows `T`. The characters that no HED string may contain (listed in [Appendix B](./Appendix_B.md#character_invalid)) are excluded from every value whatever its value class allows.

The table is generated from the machine-readable file [`character_sets.json`](_static/character_sets.json), published with this specification at `https://www.hedtags.org/hed-specification/_static/character_sets.json`. The file gives each set as a regular expression usable from Python and JavaScript, the default character sets of the standard value classes by schema version, and the structural characters of HED strings. Validators are expected to read that file rather than transcribe this table. [A.7. Character sets file](./Appendix_A.md#a7-character-sets-file) defines the file and its fields, including its `specification_version` and `file_version`.
