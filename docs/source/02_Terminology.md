# 2. HED terminology

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this specification are to be interpreted as described in \[[RFC2119](https://www.ietf.org/rfc/rfc2119.txt)\].

This specification uses a list of terms and abbreviations whose meaning is clarified here. Note: We here hyphenate multi-word terms as they appear in HED strings themselves; in plain text usage they may not need to be hyphenated. Starred variables [\*] correspond to actual HED tags.

## 2.1. Definitions

### Agent [\*]

A person or thing, living or virtual, that produces (or appears to participants to be ready and capable of producing) specified effects. Agents include the study participants from whom data is collected. Virtual agents may be human or other actors in virtual-reality or augmented-reality paradigms or on-screen in video or cartoon presentations (e.g., an actor interacting with the recorded participant in a social neuroscience experiment, or a dog or robot active in a live action or animated video).

### Condition-variable [\*]

An aspect of the experiment that is set or manipulated during the experiment to observe an effect or to manage bias. Condition variables are sometimes called independent variables.

### Control-variable [\*]

An aspect of the experiment that is fixed throughout the study and usually is explicitly controlled.

### Dataset

A set of neuroimaging and behavioral data acquired for a purpose of a particular study. A dataset consists of data recordings acquired from one or more subjects, possibly from multiple sessions and sensor modalities. A dataset is often referred to as a study.

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

An item of a HED schema that is assigned a `hedId` and so has a counterpart in the HED ontology. The HED entities of a schema are its [schema elements](#schema-element), its [schema attributes](#schema-attribute), its [schema properties](#schema-property), and its three [structural elements](#structural-element). The rows of the sources, prefixes, and external annotations sections are not HED entities: they have no `hedId`. See [8.2. HED schema to ontology](./08_HED_ontology.md#82-hed-schema-to-ontology).

### HED schema

A formal specification of the vocabulary and rules of a particular version of HED for use in annotation, validation, and analysis. A HED schema is given in one of four formats: MediaWiki, XML, JSON, or TSV (see [3.1. Schema rules](./03_HED_formats.md#31-schema-rules)). The top-level versioned HED schema is used for all HED event annotations. Named and versioned HED library schema may be used as well to make use of descriptive terms used by a particular research community. (For example, an experiment on comprehension of connected speech might annotate events using a grammatical vocabulary contained in a linguistics HED schema library.)

### HED string

A comma-separated list of HED tags and/or tag-groups.

### HED tag

A valid path along one branch of a HED vocabulary hierarchy. A valid long-form HED tag is a slash-separated path following the schema tree hierarchy from its root to a term along some branch. The short form of a tag is the last schema node of its path alone; a path that starts at a node between the root and the last node is an intermediate form. A value or an extension that follows the last schema node is kept in every form: `Weight/3 lbs` is a short form. No white space is allowed within terms themselves. For example, the long form of the HED tag specifying an experiment participant is: `Property/Agent-property/Agent-task-role/Experiment-participant`. The short form is `Experiment-participant`; the intermediate forms are `Agent-task-role/Experiment-participant` and `Agent-property/Agent-task-role/Experiment-participant`. HED tools should treat the long, intermediate, and short forms of a tag interchangeably.

### Indicator-variable [\*]

An aspect of the experiment or task that is measured or calculated for analysis. Indicator variables, sometimes called dependent variables, can be data features that are calculated from measurements rather than aspects that are directly measured.

### Merge group

The set of schemas that a version specification lists in the same namespace. The namespace is the name; the merge group is the set of schemas listed under it. The schemas of a merge group are combined into one vocabulary under the rules of [3.1.2.4. Partnered combinations](./03_HED_formats.md#3124-partnered-combinations). See [3.1.2.3. Merge groups](./03_HED_formats.md#3123-merge-groups).

### Namespace

A named partition of the vocabulary used when several schemas are combined. The schemas listed in a version specification with the same namespace name form one merge group; those listed with no namespace name form the merge group of the default namespace. Every unpartnered library schema must be alone in its own namespace. See [3.1.2. Version combinations](./03_HED_formats.md#312-version-combinations).

### Namespace prefix

The namespace name followed by a colon (e.g., `sc:`), placed before a schema version in a version specification and before every tag drawn from that namespace in an annotation. Tags in the default namespace carry no prefix. See [3.2.6. Tag namespace prefixes](./03_HED_formats.md#326-tag-namespace-prefixes).

### Node

An entry of the schema section of a HED schema. A node is either a tag, which has a name, schema attributes, and a description and is placed under a parent node or at the top level, or a `#` placeholder, which has no name and stands for the value of its parent tag. A placeholder is not a tag: it defines no term, and its schema attributes (`takesValue`, `valueClass`, `unitClass`) describe the value that its parent tag takes. Nodes are the [schema elements](#schema-element) of the tag kind; each node, including a placeholder, is assigned a `hedId`. Earlier versions of this specification, and the descriptions in released schemas, also call a node a tag term.

### Parameter [\*]

An experiment-specific item, often a specific behavioral or computer measure, that is useful in documenting the analysis or assisting downstream analysis.

### Recording [\*]

A continuous recording of data from an instrument in a single session without repositioning the recording sensors.

### Reserved tag

A tag with a specified meaning in the HED ecosystem that individual HED schemas cannot redefine. Standard schemas mark these tags with the `reserved` attribute. Some reserved tags determine the structure of an annotation and carry the validation rules of [3.2.8. Reserved tags](./03_HED_formats.md#328-reserved-tags). Other reserved tags are defined for specific uses by downstream tools.

### Schema attribute

A named characteristic that may be assigned to the [schema elements](#schema-element) of a HED schema, such as `takesValue` or `conversionFactor`. Schema attributes are defined in the schema attributes section (see [3.1.4.7. Schema attributes](./03_HED_formats.md#3147-schema-attributes)). A schema attribute that has the `elementDomain` property may also be assigned to a schema attribute, and `hedId` to a schema property (see [3.1.4.8. Schema properties](./03_HED_formats.md#3148-schema-properties)). A schema attribute is a [HED entity](#hed-entity) but not a schema element: in the HED ontology it is a property, not a class.

### Schema element

A named item of the vocabulary that a HED schema defines, of one of five kinds: tag, unit class, unit, unit modifier, or value class. The `#` placeholder of a tag that takes a value is a schema element of the tag kind, although it has no name and is not itself a tag (see [Node](#node)). Schema elements are the items to which [schema attributes](#schema-attribute) are assigned; in the HED ontology each is a class under `HedElement`. Schema attributes, schema properties, and structural elements are [HED entities](#hed-entity) but not schema elements. The descriptions in released schemas sometimes use the word element for any HED entity.

### Schema property

A named characteristic of a [schema attribute](#schema-attribute): the kinds of schema element it may be assigned to, the kind of value it takes, and whether its value is inherited. Schema properties are defined in the schema properties section (see [3.1.4.8. Schema properties](./03_HED_formats.md#3148-schema-properties)). A schema property is a [HED entity](#hed-entity) but not a schema element. The TSV format stores the schema properties in the file `AttributeProperty`.

### Schema section

One of the blocks of a HED schema file (see [3.1.4. Schema layout overview](./03_HED_formats.md#314-schema-layout-overview)). The header, the prologue, and the epilogue each hold one [structural element](#structural-element). The *schema section* holds the nodes: the tags and their `#` placeholders. The *auxiliary sections* hold the other schema elements (unit classes with their units, unit modifiers, and value classes) and the definitions of the schema attributes and the schema properties. The *extra sections* (sources, prefixes, and external annotations) hold rows that are not HED entities: they have no `hedId`. [3.1.4.10. Sources, prefixes, and external annotations](./03_HED_formats.md#31410-sources-prefixes-and-external-annotations) says how the rows of a library schema are combined with those of its standard schema partner.

### Structural element

The header, the prologue, or the epilogue of a HED schema. Each is a [HED entity](#hed-entity) (`HedStructure` in the HED ontology) and is also one of the [schema sections](#schema-section). A structural element is not a [schema element](#schema-element): it is not assigned schema attributes and takes no part in merging (see [3.1.2.4. Partnered combinations](./03_HED_formats.md#3124-partnered-combinations)).

### Table

An arrangement of rows and columns that carries HED annotations in a `HED` column, in an associated sidecar, or in both. A table may be stored as a tabular (`.tsv`) file, as a spreadsheet, or in a container such as an NWB table (see [3.2.10. Tabular files and structures](./03_HED_formats.md#3210-tabular-files-and-structures)). A table that has an `onset` column or its equivalent is a *timeline table*, such as the contents of a BIDS `events.tsv` file; any other table is a *descriptor table*, such as the contents of a BIDS `participants.tsv` file (see [3.3.4. Timeline versus descriptor tables](./03_HED_formats.md#334-timeline-versus-descriptor-tables)).

### Tag-group

One or more valid, comma-separated HED tags enclosed in parentheses to indicate that these tags belong together. Tag-groups may contain arbitrary nestings of other tags and tag-groups.

### Task [\*]

A set of structured activities performed by the participant that are integrally related to the purpose of the experiment. Tasks often include observations and responses to sensory presentations as well as specified actions in response to presented situations.

### Temporal scope

The time interval between the start and end of an event process. Often the start time is annotated with the `Onset` tag, and the end time is annotated with the `Offset` tag. Since in practical terms the time is measured in discrete samples, the temporal scope includes the start time sample but does not include the end time sample.

### Time-block [\*]

A contiguous portion of the data recording during which some aspect of the experiment is fixed or noted.

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
| `numeric`       | digits, period, hyphen, plus, caret, E, e                                         |
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
