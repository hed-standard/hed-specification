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

Circumstances forming or contributing to the setting in which an event occurs that are relevant to its interpretation, assessment, and consequences.

### Event marker

A time point relative to the experimental timeline that can be associated with an annotation. Often such a marker indicates a transition point for some underlying event process.

### Event-stream [\*]

A named sequence of events such as all the events that are face stimuli or all of the events that are participant responses.

### Experiment-participant [\*]

A living agent, particularly a human from whom data is acquired during an experiment, though in some paradigms other human participants may also play roles.

### Experimental-trial [\*]

A contiguous data period that is considered a unit used to observe or measure something, typically a data period including an expected event sequence that is repeated many times during the experiment (possibly with variations). Example: a repeating sequence of stimulus presentation, participant response action, and sensory feedback delivery events in a sensory judgment task.

### HED schema [\*]

A formal specification of the vocabulary and rules of a particular version of HED for use in annotation, validation, and analysis. A HED schema is given in XML (`.xml`) format. The top-level versioned HED schema is used for all HED event annotations. Named and versioned HED library schema may be used as well to make use of descriptive terms used by a particular research community. (For example, an experiment on comprehension of connected speech might annotate events using a grammatical vocabulary contained in a linguistics HED schema library.)

### HED string

A comma-separated list of HED tags and/or tag-groups.

### HED tag

A valid path along one branch of a HED vocabulary hierarchy. A valid long-form HED tag is a slash-separated path following the schema tree hierarchy from its root to a term along some branch. Any suffix of a valid long-form HED tag is a valid short-form HED tag. No white space is allowed within terms themselves. For example, the long form of the HED tag specifying an experiment participant is: `Property/Agent-property/Agent-task-role/Experiment-participant`. Valid short-form tags are `Experiment-participant`, `Agent-task-role/Experiment-participant`, and `Agent-property/Agent-task-role/Experiment-participant`. HED tools should treat long-form and short-form tags interchangeably.

### Indicator-variable [\*]

An aspect of the experiment or task that is measured or calculated for analysis. Indicator variables, sometimes called dependent variables, can be data features that are calculated from measurements rather than aspects that are directly measured.

### Namespace

A named partition of the vocabulary used when several schemas are combined. Schemas listed in a version specification with the same namespace name form one merge group; those listed with no namespace form the default merge group. Every unpartnered library schema must be alone in its own namespace. See [3.1.2. Version combinations](./03_HED_formats.md#312-version-combinations).

### Namespace prefix

The namespace name followed by a colon (e.g., `sc:`), placed before a schema version in a version specification and before every tag drawn from that namespace in an annotation. Tags in the default namespace carry no prefix. See [3.2.6. Tag namespace prefixes](./03_HED_formats.md#326-tag-namespace-prefixes).

### Parameter [\*]

An experiment-specific item, often a specific behavioral or computer measure, that is useful in documenting the analysis or assisting downstream analysis.

### Recording [\*]

A continuous recording of data from an instrument in a single session without repositioning the recording sensors.

### Schema element

A named item of a HED schema that is assigned a `hedId` in the HED ontology: a tag, unit, unit class, unit modifier, value class, schema attribute, or schema attribute property, together with the structural elements (header, prologue, and epilogue). All schema elements except the structural elements participate in merging and are subject to the element compatibility rules of [3.1.2.4. Partnered combinations](./03_HED_formats.md#3124-partnered-combinations); differences in prologues and epilogues are not merge conflicts.

### Schema section

One of the ordered blocks of a HED schema file (see [3.1.4. Schema layout overview](./03_HED_formats.md#314-schema-layout-overview)). The *schema section* holds the tags. The *auxiliary sections* (unit classes, unit modifiers, value classes, schema attributes, and properties) hold the other schema elements. The *extra sections* (Sources, Prefixes, and External annotations) hold rows that are not schema elements: they have no `hedId` and are not merged when the schema is loaded.

### Tag-group

One or more valid, comma-separated HED tags enclosed in parentheses to indicate that these tags belong together. Tag-groups may contain arbitrary nestings of other tags and tag-groups.

### Task [\*]

A set of structured activities performed by the participant that are integrally related to the purpose of the experiment. Tasks often include observations and responses to sensory presentations as well as specified actions in response to presented situations.

### Temporal scope

The time interval between the start and end of an event process. Often the start time is annotated with the `Onset` tag, and the end time is annotated with the `Offset` tag. Since in practical terms the time is measured in discrete samples, the temporal scope includes the start time sample but does not include the end time sample.

### Time-block [\*]

A contiguous portion of the data recording during which some aspect of the experiment is fixed or noted.

## 2.2. Character sets and restrictions

Starting with HED standard schema versions `8.3.0` and above, HED will allow UTF-8 characters in various settings. The types of characters referred to in this specification are:

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
| `dollar`        | ASCII code 36                                                                     |
| `digits`        | 0-9                                                                               |
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
| `name`          | `alphanumeric`, `hyphen`, `period`, `underscore`, `nonascii`                      |
| `newline`       | ASCII code 10 (linefeed)                                                          |
| `nonascii`      | utf-8 codes >= 160 (multi-byte)                                                   |
| `number-sign`   | ASCII code 35                                                                     |
| `numeric`       | digits, period, hyphen, plus, caret, E, e                                         |
| `percent-sign`  | ASCII code 37                                                                     |
| `period`        | ASCII code 46                                                                     |
| `plus`          | ASCII code 43                                                                     |
| `printable`     | ASCII 32 \<= code < 127                                                           |
| `question-mark` | ASCII code 63                                                                     |
| `right-paren`   | ASCII code 41                                                                     |
| `semicolon`     | ASCII code 59                                                                     |
| `single-quote`  | ASCII code 39                                                                     |
| `tab`           | ASCII code 09                                                                     |
| `text`          | `printable` and/or `nonascii` excluding comma, square brackets, and curly braces. |
| `tilde`         | ASCII code 126                                                                    |
| `underscore`    | ASCII code 95                                                                     |
| `uppercase`     | ASCII characters A-Z                                                              |
| `value-text`    | `text` excluding left and right parentheses, number sign, and tilde.              |
| `vertical-bar`  | ASCII code 124                                                                    |

`text` is the character set of the prologue, epilogue, and element descriptions of a schema, and of textClass values in standard schemas before `8.5.0`. `value-text` is the textClass character set from standard schema `8.5.0`: the characters a value may contain without changing the structure of the HED string it is substituted into.
