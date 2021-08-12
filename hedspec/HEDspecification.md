

## **HED Hierarchical Event Descriptors**


##### **Third generation specification(HED-3G)**

##### Available under the CC-BY 4.0 International license.


* TOC {:toc}



## 

## 1. Introduction

This document contains the specification for third generation HED or HED-3G. It is meant for the implementers and users of HED tools. Other tutorials and tagging guides are available to researchers using HED to annotate their data. The information contained in this document is in the process of being finalized for the first official release of HED-3G.  Aspects of HED specification deferred for later releases are delineated in other working documents that will be incorporated into this primary specification document when they are finalized and moved to the implementation phase for HED tools.  These ancillary specifications include [HED working document on spatial annotation](https://docs.google.com/document/u/0/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/edit) and [HED working document on task annotation](https://docs.google.com/document/u/0/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/edit) which are still under development and will not be included in the first release of HED-3G.


## 2. Scope of HED (third generation)

HED (an acronym for ‘Hierarchical Event Descriptors’) is an evolving framework that facilitates the description and formal annotation of events identified in time series data, together with tools for validation and for using HED annotations in data search, extraction, and analysis. This specification describes the third generation of HED or HED-3G in its current alpha form. HED-3G specifically refers to HED version 8.0.0-alpha.1 and above.

Third generation HED represents a significant advance in documenting the content and intent of experiments in a format that enables large-scale cross-study analysis of time-series behavioral and neuroimaging data, including but not limited to EEG, MEG, iEEG, eye-tracking, motion-capture, EKG, and audiovisual recording. In principle, third generation HED might be extended or adapted to annotate events in any other type of ordered or time series data. Without adequate documentation of the nature as well as the timing of these events, time series data may have limited value for further analysis beyond the specific analysis goal for which they were acquired. By adequately documenting experiment events using HED-3G, researchers can expand the utility of their data for a broader and longer lasting range of uses. 

Recorded events in behavioral and neuroimaging time series data may be of several types: (1) planned and delivered _sensory stimulation events_, or unplanned _sensory presentations_ experienced by the imaged participant(s) or by other agents (e.g., human, animal, real, virtual, storied), (2) participant or other agent _action events_ (e.g., time-recorded onsets or other features of body and eye movements, facial expressions), (3) _data feature events_ (e.g., emergent data features or phenomena, whether detected online by the recording application or noted post hoc through machine or expert inspection), (4) _control events_ (e.g., changes in experiment parameters, task conditions), (5) _procedure events_ (e.g., activities that occur during the course of the experiment such as administering a survey or taking a saliva swab), (6) _structural events_ (e.g., markers inserted for information about the experiment including metadata that might be useful for analysis), and (7) _measurement events_ (e.g., are markers inserted by external monitoring).

First generation HED attempted to describe events using a strictly hierarchical vocabulary. Difficulties inherent in early approaches led to extension of the formal structure into a second and now third generation. The structure of the HED-3G vocabulary may now be better described as heterarchical collections of terms, each of which may have hierarchical syntax and definition. 

HED-3G is also designed to be modular, thereby remaining compact in its core instantiation but allowing any number of ontological extensions for notating events in fields _beyond_ neuroimaging in which event-related interpretation of time series requires that events be adequately described to support analysis within a common framework. To enable and regulate the extension process, the root HED-3G head schema specified here includes, for the first time, _HED library schema_ to extend the HED vocabulary to include terms and concepts of importance to individual user communities — for example researchers who design and perform experiments to study brain and language, brain and music, or brain dynamics in natural or virtual reality environments. The HED library schema concept may also be used to extend HED annotation to encompass specialized vocabularies used in clinical research and practice. **When the term HED is used in this document, it refers to third generation (HED-3G) unless explicitly stated otherwise.**

This document is a specification document that articulates syntax and processing rules for HED tool developers. The document provides some examples to illustrate these rules, but several separate tutorials and user guides are in the process of being developed. All HED-related source and documentation repositories are housed on the HED-standard GitHub site, [https://github.com/hed-standard](https://github.com/hed-standard). A detailed list of HED resources appears in Appendix A. HED development is open-source and community-based. We encourage those interested to contribute to the development process. Users are encouraged to use the _Issues_ mechanism of the `hed-specification` repository on the GitHub `hed-standard` working group website: [https://github.com/hed-standard/hed-specification/issues](https://github.com/hed-standard/hed-specification/issues).


### 2.1. Goals of HED

Event annotation documents the _things happening during data recording_ whether or not they are necessarily relevant to data analysis and interpretation. Commonly recorded events in electrophysiological data collection include the initiation, termination, or other features of **stimulus presentations** and **participant** **actions**. Other events may be **unplanned environmental events** (for example, sudden onset of noise and vibration from construction work unrelated to the experiment, or a laboratory device malfunction), events recording **changes in experiment control** parameters as well as **data feature events** and control **mishap events** that cause operation to fall outside of normal experiment parameters. 

The goals of HED are to provide a standardized annotation system that allows researchers to:

1. _Document_ the exact natures of events (sensory, behavioral, environmental, and other) that occur during recorded time series data that may inform data analysis and interpretation.
2. _Describe_ in detail the design of the experiment including participant task(s).
3. _Relate_ event occurrences both to the experiment design and to participant tasks and experience.
4. _Provide_ a basic infrastructure for building and using machine-actionable tools to systematically analyze data associated with recorded events in and across data sets, studies, paradigms, and modalities.

Current systems in neuroimaging experiments do not record events beyond simple numerical (‘3’) or text (‘Event type Target’) labels whose more complete and precise meanings are known only to the experimenter(s). A central goal of HED is to enable building of archives of brain imaging data in a form amenable to new forms of larger scale analysis, both within _and_ _across_ studies. Such event-related analysis requires that the nature(s) of the recorded events be specified in a common language. The HED project seeks to formalize the development of this language, to develop and distribute tools that maximize its ease of use, and to inform new and existing researchers of its purpose and value.


### 2.2. HED design principles

The near decade-long effort to develop effective event annotation for neurophysiological and behavioral data, culminating to date in HED-3G, has revealed the importance of four principals (aka the PASS principles), all of which have roots in other fields:


1. **P**reserve orthogonality of concepts in specifying vocabularies.
2. **A**bstract functionality into layers (e.g., more general vs. more specific).
3. **S**eparate implementation from the interface (for flexibility).
4. **S**eparate content from presentation (to maintain a unique, sufficient internal representation, while presenting data to users in forms they can more readily review and understand).

Orthogonality, the notion of keeping independently applicable concepts in separate hierarchies (1 above), has long been recognized as a fundamental principle in reusable software design, distilled in the design rule: _Favor composition over inheritance_ (Gamma et al. 1994). _Abstraction of functionality into layers_ (2) and _Separation of content from presentation_ (4) are well-known principles in user-interface and graphics design that allow tools to maintain a single internal representation of needed information while emphasizing different aspects of the information when presenting it to users. Similarly, making validation code independent of the schema (3) allows redesign of the schema without having to re-implement the annotation validation tools.


### 2.3. HED terminology

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [[RFC2119](https://www.ietf.org/rfc/rfc2119.txt)].

This specification uses a list of terms and abbreviations whose meaning is clarified here. Note: We here hyphenate multi-word terms as they appear in HED strings themselves; in plain text usage they may not need to be hyphenated. Starred variables correspond to actual HED tags.


##### Agent*

A person or thing, living or virtual, that produces (or appears to participants to be ready and capable of producing) specified effects. Agents include the study participants from whom data is collected. Virtual agents may be human or other actors in virtual-reality or augmented-reality paradigms or on-screen in video or cartoon presentations (e.g., an actor interacting with the recorded participant in a social neuroscience experiment, or a dog or robot active in a live action or animated video).

##### Condition-variable*

An aspect of the experiment that is set or manipulated during the experiment to observe an effect or to manage bias. Condition variables are sometimes called independent variables.

##### Control-variable*

An aspect of the experiment that is fixed throughout the study and usually is explicitly controlled.

##### Dataset

A set of neuroimaging and behavioral data acquired for a purpose of a particular study. A dataset consists of data recordings acquired from one or more subjects, possibly from multiple sessions and sensor modalities. A dataset is often referred to as a study.

##### Event*

_Something that happens during the recording_, or may be perceived by a 
participant as happening, to which a time of occurrence (most typically onset or offset) can be identified. Something expected by a participant to happen at a certain time that _does not_ happen can also be a meaningful recording event. The nature of other events may be known only to the experimenter or to the experiment control application (e.g., undisclosed condition changes in task parameters).

##### Event-context*

Circumstances forming or contributing to the setting in which an event occurs that are relevant to its interpretation, assessment, and consequences.

##### Event-stream*

A named sequence of events such as all of the events that are face stimuli or all of the events that are participant responses.

##### Experimental-participant*

A living agent, particularly a human from whom data is acquired during an experiment, though in some paradigms other human participants may also play roles.

##### Experimental-trial* 
A contiguous data period that is considered a unit used to observe or measure something, typically a data period including an expected event sequence that is repeated many times during the experiment (possibly with variations). Example: a repeating sequence of stimulus presentation, participant response action, and sensory feedback delivery events in a sensory judgment task.

##### HED schema
A formal specification of the vocabulary and rules of a particular version of HED for use in annotation, validation, and analysis. A HED schema is given in XML (_.xml_) format. The top-level versioned HED schema is used for all HED event annotations. Named and versioned HED library schema may be used as well to make use of descriptive terms used by a particular research community. (For example, an experiment on comprehension of connected speech might annotate events using a grammatical vocabulary contained in a linguistics HED schema library.)

##### HED string

A comma-separated list of HED tags and/or tag-groups. 

##### HED tag

A valid path along one branch of a HED vocabulary hierarchy. A valid long-form HED tag is a slash-separated path following the schema tree hierarchy from its root to a term along some branch. Any suffix of a valid long-form HED tag is a valid short-form HED tag. No white space is allowed within terms themselves. For example, the long form of the HED tag specifying an experiment participant is: _Property/Agent-property/Agent-task-role/Experimental-participant_. Valid short-form tags are _Experimental-participant_, _Agent-task-role/Experimental-participant_, and _Agent-property/Agent-task-role/Experimental-participant_. HED tools should treat long-form and short-form tags interchangeably.

##### Indicator-variable*

An aspect of the experiment or task that is measured or calculated for analysis. Indicator variables, sometimes called dependent variables, can be data features that are calculated from measurements rather than aspects that are directly measured. 

##### Parameter*

An experiment-specific item, often a specific behavioral or computer measure, that is useful in documenting the analysis or assisting downstream analysis.

##### Recording*

A continuous recording of data from an instrument in a single session without repositioning the recording sensors.

##### Reference-frame*

A specified set of axes, primary orientation centered at a specified point of origin and having a specified scale. HED reference frames are usually anchored to some physical location or to an object or to another reference-frame that has an anchor.

##### Tag-group

One or more valid, comma-separated HED tags or enclosed in parentheses to indicate that these tags belong together. Tag-groups may contain arbitrary nestings of other tags and tag-groups.

##### Task* 

A set of structured activities performed by the participant that are integrally related to the purpose of the experiment. Tasks often include observations and responses to sensory presentations as well as specified actions in response to presented situations.

##### Temporal scope

The time interval between events marking the beginning and end of something in the experiment. 

##### Time-block*

A contiguous portion of the data recording during which some aspect of the experiment is fixed or noted.


### 2.4. The HED schema

A HED schema is the formal specification of the HED vocabulary and rules for annotating events. A HED schema vocabulary is organized hierarchically so that similar concepts and terms appear close to one another in the organizational hierarchy. A HED schema is used to validate event annotations. Past, present, and future versions of the HED schema adhere to [semantic versioning](https://semver.org/) with version numbers of the form _x.y.z_ representing _major.minor.patch_ versions. Although schema developers work with HED schema in _.mediawiki_ format for ease in editing,  HED tools generally use XML versions of the HED schema. An expandable HTML browser is also available.

HED schema XML filenames use the standardized format _HEDx.y.z.xml_. These standardized names make it easier for tools to locate the appropriate HED schema version in the HED working group [GitHub website](https://github.com/hed-standard). All schema versions are stored in the _hedxml_ directory of the [HED specification repository](https://github.com/hed-standard/hed-specification). Third generation HED begins with schema version _8.0.0_. Thus, the first official release of the third generation HED schema is _HED8.0.0.xml_. Releases are stored in _[hedxml](https://github.com/hed-standard/hed-specification/tree/master/hedxml)_ directory of the  _[hed-specification](https://github.com/hed-standard/hed-specification)_ repository. Deprecated versions of the HED schema are stored in the _[hedxml/deprecated](https://github.com/hed-standard/hed-specification/tree/master/hedxml/deprecated)_ directory of the _[hed-specification](https://github.com/hed-standard/hed-specification)_ repository.

All of the data recordings in a dataset should be annotated using a single version of the standard HED schema. Validation and analysis tools are not expected to handle multiple versions of the standard HED schema when processing a dataset. Datasets may also include annotations from multiple HED library schema extensions in addition to those from the standard schema, as described in **Section 4** of this document. A more detailed discussion of the HED schema format appears in **Appendix B**.


#### 2.4.1. Mediawiki format for HED schemas

HED schema developers can specify a new schema version or revision in _.mediawiki_ format for more convenient editing, display, and reference on GitHub. The following brief example illustrates the format. A full description of the format is given in **Appendix B**.

**Example:** An excerpt of a small portion of a HED schema in _.mediawiki_ format.

````mediawiki
HED version="8.0.0" 

'''Prologue'''
This prologue introduces the schema.

!# start schema
'''Event''' <nowiki>[Something that happens at a given place and time.]</nowiki>
* Sensory-event <nowiki>{suggestedTask=Task-event-role}[Something perceivable by an agent.]</nowiki>
                              . . .
'''Property'''<nowiki>{extensionAllowed}[A characteristic.] </nowiki>
* Informational-property <nowiki>[A quality pertaining to information.]</nowiki>
** Label <nowiki>{requireChild} [A string of 20 or fewer characters.]</nowiki>
*** <nowiki># {takesValue, valueClass=nameClass}</nowiki> 
!# end schema

'''Unit classes''' <nowiki>[Unit classes and units for the nodes.]</nowiki>
                        . . .
'''Unit modifiers''' <nowiki>[Unit multiples and submultiples.]</nowiki>
                       . . .
'''Value classes''' <nowiki>[Rules for the values provided by users.]</nowiki>
                       . . .
'''Schema attributes''' <nowiki>[Allowed node attributes.]</nowiki>
                        . . .
'''Properties''' <nowiki>[Properties of the schema attributes.]</nowiki>
                        . . .
'''Epilogue'''
An optional section that is the place for notes and is ignored in HED processing.

!# end hed
````

Beginning with third generation HED (HED schema versions 8.0.0 and later), **terms in a given schema must be unique within that schema.** This uniqueness rule allows automated expansion of short form HED strings into their full long forms. 

Top level tree root elements are enclosed by triple single quotes. Each child term within the schema must be on a single line that begins with a certain number of asterisks(*) corresponding to the term’s level within the hierarchy. 

Everything after each HED term must be enclosed by `<nowiki></nowiki>` markup elements. Items within these markup elements include a term description and term attributes. Term (node element) descriptions, which are enclosed in square brackets in the mediawiki specification, indicate the meaning of the term or tag they modify. HED schema attributes, which are enclosed with curly braces, provide additional rules about how the tags and its modifying values should be used and handled by tools. Allowed HED schema attributes for HED terms are those schema attributes that do not have the `unitClassProperty`, `unitModifierProperty`, `unitProperty`, or `valueClassProperty`. 

Attributes appear in the schema specification either as `name` attributes or as `name=value` pairs. The presence of a `name` attribute for a schema node element indicates that the attribute is true for that node, while the presence of a `name=value` attribute indicates that the attribute has the specified value for that node. If multiple values of a particular attribute are applicable, they should be specified as separate name-value pairs.

The hashtag character (`#`) is a placeholder for a user-supplied value. Within the HED schema a `#` node indicates that the user must supply a value consistent with the unit classes and value classes of the `#` node if it has any. Unit classes and value classes are specified in curly braces and treated like other schema attributes.  Lines with hashtag (#) placeholders should have everything after the asterisks enclosed by `<nowiki></nowiki>` markup elements. The values of HED tag placeholders cannot stand alone, but must include the parent when used in a HED string.  In the above example, the `#` that is a child of the _Label_ node must include _Label_ when used (e.g., _Label/myLabel_). 


#### 2.4.2. XML format for a HED schema

The HED XML schema format encodes the hierarchical vocabulary as nested `<node>` elements. The HED XML version of the schema is used during validation and analysis. Tools including an online converter are available to convert between _.mediawiki_ and _.xml_ formats. An expandable HTML browser view is also available for easy viewing. The _.xml_ format has changed with the release of HED-3G. This modification of the XML format was done for four reasons:

1. To correctly handle multiple values of schema attributes.
2. To preserve the prologue and epilogue information present in _.mediawiki_ files.
3. To allow schema attributes to be formally specified and validated.
4. To allow an XSD specification of the HED schema for validation of the schema.

The following is a translation of the _.mediawiki_ example from the previous section in the new XML format. A complete specification of the format is given in Appendix B.

**Example:** The XML version of the HED schema segment of the previous example.

````xml
<?xml version="1.0" ?>
<HED version="8.0.0">
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
                    <attribute>
                        <name>requireChild</name>
                    </attribute>
                <node>
                    <name>#</name>
                    <attribute>
                        <name>takesValue</name>
                    </attribute>
                    <attribute>
                        <name>valueClass</name>
                        <value>nameClass</value>
                    </attribute>
                </node></node>
              </node>
        </node>
    </schema>
    <unitClassDefinitions> ...</unitClassDefinitions>
    <unitModifierDefinitions>...</unitModifierDefinitions>
    <valueClassDefinitions>...</valueClassDefinitions>
    <schemaAttributeDefinitions>...</schemaAttributeDefinitions>
    <propertyDefinitions>...</propertyDefinitions>
    <epilogue>This epilogue is a place for notes and is ignored in HED processing.</epilogue>
</HED>
````

Each `<node>` element must have a `<name>` child element corresponding to the HED tag term that it specifies. A `<node>` element may also have a `<description>` child element containing the text that appears in square brackets `[]` in the _.mediawiki_ version. The schema attributes (which appear as `name` values or `name-value` pairs enclosed in curly braces {} in the _.mediawiki_ file) are translated into `<attribute>` child elements of `<node>` in the _.xml_.  These schema attributes are not to be confused with the HED _Attribute_ tag that is part of the HED vocabulary. 

The HED schema also includes a `<unitClassDefinitions>` section that specifies the allowed unit classes and the corresponding allowed unit names. Only the singular version of each unit name is explicitly specified, but the corresponding plurals of the explicitly mentioned singular versions are also allowed (e.g., `feet` is allowed in addition to `foot`). HED uses a `pluralize` function available in both Python and Javascript to check validity.  

The `<unitModifierDefinitions>` section lists the SI unit multiples and submultiples that are allowed to be prepended to units that have the SIUnit schema attribute. 

The `<valueClassDefinitions> `section specifies rules for the values that are substituted for placeholders (`#`). Examples are special characters that are allowed for numeric values or dates. Placeholders that have no `valueClass` attributes, are assumed to follow the rules for HED tag naming described in the next section.

The `<schemaAttributeDefinitions>` section lists the schema attributes that apply to some nodes and definitions in other sections of the schema. The specification of which type of elements an attribute may apply to is specified by the property attributes of these schema attributes. 

The `<schemaAttributeDefinitions>` section lists the schema attributes that apply to some nodes and definitions in other sections of the schema. The specification of which type of elements an attribute may apply to is specified by the property attributes of these schema attributes. 


#### 2.4.3. Allowed characters in the HED schema

The different parts of the HED schema have different rules for the characters that are allowed. Table 2.1 summarizes the rules. UTF-8 characters are not supported. Values that don’t have an associated valueClass attribute are assumed to have `valueClass=nameClass`.

##### Table 2.1. Rules for valid characters in HED schema.

<table>
  <tr>
     <td><strong>Item</strong></td>
     <td><strong>Allowed characters</strong></td>
     <td><strong>Style suggestions and other rules</strong></td>
  </tr>
  <tr>
     <td>Node elements<br>(HED tag names<br><code>valueClass=nameClass</code></td>
     <td>Alphanumeric characters, hyphens, and underbars with no white space.</td>
     <td>The first letter of a term should be capitalized for readability. The remaining characters should be lowercase.</td>
  </tr>
  <tr>
     <td>Descriptions<br><code>valueClass=textClass</code></td>
     <td>Alphanumeric characters, blanks, commas, periods, semicolons, colons, hyphens, underbars, forward slashes, carets (^), and parentheses are allowed.  No square brackets, curly braces, quotes, or other punctuation and symbols are allowed.</td>
     <td>Descriptions should be concise sentences, possibly with clarifying examples.</td>
  </tr>
  <tr>
     <td>Placeholder (<code>#</code>) substitutions by user-defined values.</td>
     <td>The characters allowed depend on the <code>valueClass</code> for the value plus the actual characters in the units and in the unit modifiers if applicable.</td>
   <td><p>If the <code>#</code> has <code>valueClass</code> attributes, the value may have special characters as specified by in the class definition. For example, the colon (:) is specifically allowed for the <code>dateTime</code> unit class.</p><p>Units are separated from the value by at least one blank whether prefix or suffix.</p> </td>
  </tr>
  <tr>
     <td>Library names and nicknames</td>
     <td>A single word containing only alphabetic characters.</td>
     <td>Library nicknames are followed by a single colon when used in a tag string.</td>
  </tr>
</table>


### 2.5. HED vocabulary top-level organization

The HED-3G schema (version 8.0.0 and above) contains eight root trees of HED terms: **_Event_**, **_Agent_**, **_Action_**, **_Item_**, **_Property_**, and **_Relation_**. 

The **_Event_** root tree terms indicate the general category of the event — such as whether it is a sensory event, an agent action, a data feature, or an event indicating experiment control or structure. The HED annotations describing each event may be assembled from a number of sources during processing. The assembled HED string annotating an event should have at least one tag from the _Event_ tree, as many analysis tools use the _Event_ tags as a primary means of segregating, epoching and processing the data. Ideally, tags from the _Event_ subtree should appear at the top level of the HED annotation describing an event to facilitate analysis.

The **_Agent_** root tree terms indicate types of agents (e.g., persons, animals, avatars)  that take an active role or produce a specified effect. An _Agent_ tag should be grouped with property tags that provide information about the agent, such as whether the agent is an experiment participant.

The **_Action_** root tree terms describe actions performed by agents. 

The **_Item_** root tree terms describe things with (actual or virtual) physical existence such as objects, sounds, or language. 

Descriptive elements are organized in the **_Property_** rooted tree, and binary relations are in the **_Relation_** rooted tree. These descriptive elements should always be grouped with the elements they describe using parentheses. 


### 2.6. HED tag syntax and requirements

A **HED tag** is a term in the HED vocabulary identified by a path consisting of the individual node names from some branch of the HED schema hierarchy separated by forward slashes (/). An important requirement of third generation HED is that the node names in the HED schema **must be unique**. As a consequence, the user can specify as much of the path to the root as desired. The full path version is referred to as _long form_ and truncated versions as _short form_. HED tools are available to map between shortened tags and  long form as needed. 

Table 2.2 compares the long forms of several representative tags to various equivalent short-form values. The # placeholder child for _Label_ in the HED schema must be replaced by a string value when the tag is used for annotation. The values that replace these # placeholders cannot be node names.


##### Table 2.2. Valid HED tags described by the excerpt of the previous sections.

<table>
  <tr>
     <td><strong>Long form (full path from node to root)</strong></td>
     <td><strong>Short form(s)</strong></td>
  </tr>
  <tr>
     <td><em>Event/Sensory-event</em></td>
     <td><em>Sensory-event</em></td>
  </tr>
  <tr>
     <td><em>Property/Informational-property/Label/Image1</em></td>
     <td><em>Label/Image1</em><br><em>Informational-property/Label/Image1</em><br></td>
  </tr>
  <tr>
     <td><em>Item/Object/Geometric-object/2D-shape/Triangle</em></td>
     <td><em>Triangle</em><br><em>2D-shape/Triangle</em><br><em>Geometric-object/2D-shape/Triangle</em><br><em>Object/Geometric-object/2D-shape/Triangle</em></td>
  </tr>
</table>

A **HED string** is a comma-separated list of HED tags and/or HED tag groups. A **HED tag group** is a comma-separated list of HED tags and/or tag groups enclosed in parentheses. Tag groups may include other tag groups. Parentheses convey association, since HED strings are _unordered_ lists. The terms in a HED string must be unique, thus, a HED string forms a set.

**Example:** A nested HED tag group indicating that the experiment’s subject pressed a mouse button.

**Short form:**

```
    ((Human-agent, Experiment-participant), (Press, Mouse-button))
```

**Long form:**
```
((Agent/Human-agent,
    Property/Agent-property/Agent-task-role/Experiment-participant),
(Action/Move/Move-body-part/Move-upper-extremity/Press,
 Item/Object/Man-made-object/Device/IO-device/Input-device/Computer-mouse/Mouse-button))
```

The syntax and errors for HED tags and HED strings are summarized in **Appendix C**

**HED # placeholders** cannot have siblings. Thus, tags that have placeholder children cannot be extended even if they inherit an `extensionAllowed` attribute from an ancestor. The parsers treat any child of these tags as a value rather than a tag.  

**HED values** can be strings or numeric values followed by a unit specification. If a `unitClass` is specified as an attribute of the `#` node, then the units specified must be valid units for that `unitClass`. **HED parsers assume that units are separated from values by at least one blank.**


## 3. Annotation using HED tags

This section illustrates the use of HED tags and discusses various tags that are used to document the structure and organization of electrophysiological experiments. The simplest annotations treat each event as happening at a single point in time. The annotation process for such _time-marked_ or _point events_ involves describing what happened during that event. 

Section 3.1 addresses annotation of time-marked events. However, the full power of HED can only be harnessed by downstream analysis tools when the annotations document the context, task, intent and condition variables as well as their relationship to individual events. Further, many important events have extended duration and may elicit different neural responses during their full time-span. These more sophisticated concepts require a tagging process that considers not only description of each event in isolation, but also inter-relationships among events across the data recording. The HED infrastructure and tagging process for these more complex operations are developed in later sections of Chapter 3. 

Most experiments have a limited number of distinct event types, which are often identified in the original experiment by local event codes. The strategy for assigning local codes to individual events depends on the format of the data set. However, in practice, HED tagging usually involves annotating a few event types or codes for an entire study, not tagging individual instances of events in individual data recordings. Discussions of how tags for local event codes are associated with event instances, as well as supporting tools, are deferred to Chapter 5. 


### 3.1. Modeling events as instantaneous occurrences

This section describes HED annotation of time-marked events. A time-marked event is modeled as happening at an instant in time. Generally, a marker is inserted in the data or held in an external event file containing the onset time of some action, relative to the beginning of the data recording. A time-marked event may also point to the end/offset of some happening or to time between the onset and offset (for example, the maximum velocity point in a participant arm movement or the maximum potential peak of an eyeblink artifact). Downstream analyses often look for neurological effects directly following (or preceding) event markers. The addition of HED context, allows information about events that occur over extended periods of time to propagate to intermediate time points. 

This section illustrates basic HED descriptions of four types of events that are often annotated as time-marked events or point events: **stimulus events**, **response events**, **experiment control events**, and **data features**. HED-3G now also allows more sophisticated models of events that have extended duration. The remaining sections of Chapter 3 develop the HED concepts needed to capture these advanced models of events as well as event and task inter-relationships. This specification is meant to provide guidelines for tool-builders. Additional tutorials and user guides provide more specific guidance for annotators.

An typical example of an experiment using time-marked event annotation is simple target detection. In this experiment geometric shapes of different colors are presented on a computer screen at two-second intervals. After every visual shape presentation, the subject is asked to press the left mouse button if the shape is a green triangle or the right mouse button otherwise. After a block of 30 such presentation-response sequences (trials), the control software sounds a buzzer to indicate that the subject can rest for 5 minutes before continuing to the next block of trials. After the experiment is completed, the experiment runs an eyeblink-detection tool on the EEG data and inserts an event marker at the amplitude maximum of each detected blink artifact.


#### 3.1.1. A stimulus event

The target detection experiment described above is an example of a stimulus-response paradigm: perceptually distinct sensory stimuli are presented at precisely recorded times (typically with abrupt onsets) and ensuing and/or preceding precisely-timed changes in the behavioral and physiological data streams are annotated or analyzed. Stimulus onsets (typically) are annotated with the _Sensory-event_ tag. Additional tags indicate task role. Separation of what an event is (as designated by a tag from the _Event_ subtree) from its task role (as indicated by other descriptive tags) is an important design change that distinguishes HED-3G from earlier versions of HED and enables effective annotation in more complex situations.

A stimulus event can be annotated at different levels of detail. When not needed, fine details can generally be ignored, but once annotated can provide valuable information for later, possibly unanticipated analysis purposes. In a series of examples, we will annotate successively more details about the experiment events. Each example shows both the short form and long form. The elements in the long form that correspond to the short form are shown in bold-face. In addition, the long form has a description, which is omitted from the short-form for readability.

**Example:** Version 1 of HED annotation of a green triangle visual stimulus presentation event.

**Short form:** 

```
Sensory-event, Experimental-stimulus, Visual-presentation, (Green, Triangle)
```

**Long form:**
```
Event/Sensory-event,  
Property/task-property/Task-event-role/Experimental-stimulus,
Property/Sensory-property/Visual-presentation,
(Property/Sensory-property/Sensory-attribute/Visual-attribute/Color/CSS-color/Green-color/Green, 
Item/Object/Geometric-object/2D-shape/Triangle),
Property/Informational-property/Description/An experimental stimulus consisting of a green triangle is displayed on the center of the screen.
```

The example HED string above illustrates the most basic form of point event annotation. The annotation indicates that this is a visual sensory event intended to be an experiment stimulus. _Sensory-event_ is in the _Event_ rooted tree and indicates the general class that this event falls into. In general, the annotation for each event should include at least one tag from the _Event_ tree. If there are multiple sensory presentations in the same event, a single _Sensory-event_ tag covers the general category for all presentations in the event. The individual presentations (which may include different modalities) are grouped with their descriptive tags, while the _Sensory-event_ tag applies overall. In this case there is only one, so the grouping is not necessary. 

The _Experimental-stimulus_ is a _Task-property_ tag. Whether a particular sensory event is an experiment stimulus depends on the particular task, hence _Experimental-stimulus_ is a _Task-property_. Sensory events that are extraneous to the task can also occur, so it is important to distinguish those that are related to the intent of the task.

The remaining portion of the annotation describes what the sensory presentation is. The _Green_ and _Triangle_ tags are grouped to indicate specifically that a green triangle is presented. _Visual-presentation_ is a _Sensory-property_ tag from the _Property_ rooted tree. Which senses are impacted by the _Sensory-event_ should always be indicated, even if it appears to be obvious to the reader. The goal is to facilitate machine-actionable analysis.

HED has a number of qualitative relational tags designating spatial features such as _Center-of_, which should always be included if possible. These qualitative terms provide clear search anchors for tools looking for general positional characteristics. Hemispheric and vertical distinctions have particular neurological significance. More detailed size, shape, and position information enhances the annotation. However, actual detailed information requires the specification of a frame of reference, a topic deferred until later in this document.

The order of the tags doesn’t matter; HED strings are unordered lists of HED tags and tag groups. Where the grouping of associated tags needs to be indicated, most commonly in the case of tags with modifiers, the related tags should be put in a tag group enclosed by parentheses (as above).  


#### 3.1.2. Simple specification of task intention

In deciding what additional information should be included, the annotator should consider how to convey the nature and intent of the experiment and the EEG responses that are likely to be elicited. The brief description suggests that green triangles are something “looked for”, within the structure of the task that participants are asked to perform during the experiment.

**Example:** Version 2 of the green triangle presentation conveys more task intent.

**Short form:**
```
Sensory-event, Experimental-stimulus, Visual-presentation,
(Green, Triangle), (Intended-effect, Oddball), (Intended-effect, Target)
```

**Long form:**
```
Event/Sensory-event, 
Property/Task-property/Task-event-role/Experimental-stimulus,
Property/Sensory-property/Sensory-presentation/Visual-presentation,
(Property/Sensory-property/Sensory-attribute/Visual-attribute/Color/CSS-color/Green-color/Green,
Item/Object/Geometric-object/2D-shape/Triangle),
(Property/Task-property/Task-effect-evidence/Intended-effect,
Property/Task-property/Task-stimulus-role/Oddball),
(Property/Task-property/Task-effect-evidence/Intended-effect,
Property/Task-property/Task-stimulus-role/Target),
Property/Informational-property/Description/A green triangle target oddball is presented in the center of the screen with probability 0.1.
```

The _Intended-effect_ tag is a _Task-effect-evidence_ tag that describes the effect expected to be elicited from the participant experiencing the stimulus. This tag indicates, that based on the specification of the task, we can conclude that the subject will be looking for the triangle (_Target_) and that its appearance is unusual (_Oddball_). 

Three other tags in the _Task-effect-evidence_ are _Computational-evidence_, _External-evidence_, and _Behavioral-evidence_. In many experiments, a subject indicates that something occurs by performing an action such as pushing the left mouse button for a green triangle and the right button otherwise. When the left-mouse button is pushed, one may conclude that the participant has behaved as though the green triangle appears. If the button push is tagged with _Behavioral-evidence_, automated tools can check whether the intended effect agrees with subject behavior. An example of _External-evidence_ is annotation by a speech therapist about whether the participant stuttered in a speech experiment. _Computational-evidence_ might be generated from BCI annotation.

Notice that the long form version also includes a _Description_ tag that gives a text description of the event. Users should always include a _Description_ tag in the annotation of each event type. The_ Description_ tag is omitted for readability in the short form examples. As a matter of practice, however, users should start with a detailed text description of each type of event before starting the annotation. This description can serve as a check on the consistency and completeness of the annotation. Generally users annotate using the short form for HED tags and use tools to map the short form into the long form during validation or analysis.

HED-3G has more sophisticated methods of specifying the relationships of events and tasks. These require more advanced tagging mechanisms that are discussed later in this document.


#### 3.1.3. A participant action event

In many experiments, the participant is asked to press (or select and press) a finger button to indicate their perception of or judgment concerning the stimulus. These types of events, as well as participant actions not related to the task, are annotated as _Agent-action_ events. _Agent-action_ events can be annotated with varying levels of detail, as illustrated by the next examples.

**Example:** Version 1 of a HED annotation of a button press in response to a stimulus.

**Short form:**  
```
Agent-action, (Participant-response, (Press, Mouse-button))
```

The _Participant-response_ tag indicates that this event represents a task-related response to a stimulus. The_ Press_ tag is from the _Action_ subtree and is grouped with the _Mouse-button_ to indicate the pressing of a button. In general, _Action_ elements can be considered verbs, while _Items_ and _Agents_ can be considered nouns. These elements form a natural sentence structure: (subject, (verb, direct object)), with the subject and direct object being formed by noun elements. _Attribute_ elements are the adjectives, adverbs, and prepositions that modify and connect these elements.

**Example:** A more detailed HED annotation of a button press in response to a stimulus.

**Short form:**   
```
Agent-action, Participant-response, 
((Human-agent, Experiment-participant), (Press, Mouse-button)),
(Behavioral-evidence, Oddball), (Behavioral-evidence, Target)
```

**Long form:**
```
Event/Agent-action,
Property/Task-property/Task-event-role/Participant-response,
((Agent/Human-agent, 
Property/Agent-property/Agent-task-role/Experiment-participant),
(Action/Move/Move-body-part/Move-upper-extremity/Press,
Item/Object/Man-made-object/Device/IO-Device/Input-device/Computer-mouse/Mouse-button)),
(Property/Task-property/Task-effect-evidence/Behavioral-evidence,
Property/Task-property/Task-stimulus-role/Oddball),
(Property/Task-property/Task-effect-evidence/Behavioral-evidence,
Property/Task-property/Task-stimulus-role/Target),
Property/Informational-property/Description/The subject pushes the left mouse button to indicate the appearance of an oddball target using index finger on the left hand.
```

The _Participant-response_ tag is modified by tags that indicate that the participant is reacting by responding as though the stimulus were an oddball target. Specifically the _Behavioral-evidence_ tag documents that the subject gave a response indicating an oddball target. In other words, the participant pressed the left mouse button indicating an oddball target, which may or may not match the stimulus that was presented. Other details should be annotated, including whether the subject’s left, right, or dominant hand was used to press the mouse button and whether the left mouse button or right mouse button was pressed. (This factor was indicated in the _Description_, but not in the machine-actionable tags.)


#### 3.1.4. An experimental control event

Experiments may have experiment control events written into the event record, often automatically by the presentation or control software. In the illustration provided above, a buzzer sounded by the control software indicates that the subject should rest.

**Example:** A buzzer is sounded to indicate that the subject can rest.

**Short form:**
```
Sensory-event, Instructional, Auditory-presentation,
(Buzz, (Intended-effect, Rest))
```

**Long form:** 
```
Event/Sensory-event, 
Property/Task-property/Task-event-role/Instructional,
Property/Sensory-property/Sensory-presentation/Auditory-presentation,
(Item/Sound/Named-object-sound/Buzz,
(Property/Task-property/Task-effect-evidence/Intended-effect,
Action/Perform/Rest)),
Property/Informational-property/Description/A buzzer sounds indicating a rest period.
```

#### 3.1.5. A data feature event

Another type of tagging documents computed data features and expert annotations that have been inserted post-hoc into the experimental record as events. The _Computed-feature_ and _Observation_ tags designate whether the event came from a computation or from manual evaluation. 

**Example:** HED tag for a computational feature inserted post hoc by the Blinker tool.

**Short form:**  
```
Data-feature, (Computed-feature, Label/Blinker_BlinkMax)
```

**Long form:**
```
Event/Data-feature,
(Property/Data-property/Data-source-type/Computed-feature, 
Property/Informational-property/Label/Blinker_BlinkMax),
Property/Informational-property/Description/Event marking the maximum signal deviation caused by blink inserted by the Blinker tool.
```

As shown by this example, the _Computed-feature_ tag is grouped with a label of the form _toolName_featureName_. In this example, the computed property is just a marker of where a feature was detected. If a value was computed at this point, an additional _Value_ tag would be included.

Clinical evaluations are observational features and many fields have standardized names for these features. Although the HED standard itself does not specify these names, library schema representing terminology in clinical or application subfields may provide the vocabulary. (See Chapter 4 for a discussion of library schema.)

**Example:** Annotator AJM identifies a K-complex in a sleep record.

**Short form:**
```
Data-feature, (Observation, Label/AnnotatorAJM_K-complex)
```

**Long form:**
```
Event/Data-feature,
(Property/Data-property/Data-source-type/Observation,
Property/Informational-property/Label/AnnotatorAJM_K-complex),
Property/Informational-property/Description/K-complex defined by AASM guide.
```

#### 3.1.6. What else should be documented?

Most event annotation focuses on basic identification and description of stimuli and the participant’s direct response to that stimuli. However, for accurate comparisons across studies, much more information is required and should be documented with HED tags rather than just with text descriptions. This is particularly true if this information is relevant to the experimental intent, varied during the experiment, or likely to evoke a neural response. In the example of 3.1.1, the green triangle might be displayed for an extended period (during which other events might occur), and the disappearance of the triangle is likely to elicit a neural response. Exactly how this information should be represented is discussed in Section 3.3 with the introduction of temporal scope and its use with _Onset_ and _Offset_.

Even for a standard setup, aspects such as the screen size, the distance and position of the participant relative to the screen and the stimulus, as well as other details of the environment, should be documented as part of the overall experiment context. These details allow analysis tools to compare and contrast studies or to translate visual stimuli into visual field information. _Event-context_ tags, which are introduced in **Section 3.4**, allow this information to be propagated to recording events in a manner that is convenient for analysis.

Of primary importance and perhaps the most difficult to convey with annotation is how specific stimuli relate to task intent and how the conditions are varied to achieve this intent. **Section 3.5** describes HED mechanisms for annotating this information.


### 3.2. HED definitions and the _Definition_ tag

HED-3G introduces the _Definition_ tag to facilitate tag reuse and to allow implementation of concepts such as _temporal scope_. The _Definition_ tag allows researchers to create a name to represent a group of tags and then use the name in place of these tags when annotating data. These short-cuts make tagging easier and reduce the chance of errors. Often laboratories have a standard setup and event codes with particular meanings. Researchers can define names and reuse them  for multiple experiments. Another important role of definitions is to provide the structure for implementing temporal scope as introduced in **Section 3.3**.

A **HED definition** is a tag group that includes one _Definition_ tag whose required child value names. The definition usually includes an optional tag-group specifying the actual definition information. Table 3.1 summarizes the syntax rules for definitions.

##### Table 3.1. Syntax for HED definitions. Optional items are underlined.

<table>
  <tr>
     <td><strong>Syntax</strong></td>
     <td><strong>Explanation</strong></td>
  </tr>
  <tr>
     <td><p><strong>Short forms:</strong></p>
<p><em>(Definition/XXX, (tag-group))</em></p>
<p><em>(Definition/XXX/#, (tag-group))</em></p>
<p><strong>Long forms:</strong><br>
<em>(Property/Organizational-property/Definition/XXX, (tag-group))</em><br>
<em>(Property/Organizational-property/Definition/XXX/#, (tag-group))</em>
</p></td>
     <td><p><em>XXX</em> is the name of the definition and <em>(tag-group)</em> is the definition’s value.</p>
    <p>If the XXX/# form is used, then the definition’s <em>(tag-group) </em>must contain a single # representing a value to be substituted for when the definition is used.</p>
<p>The <em>tag-group</em> may be omitted if the only purpose of the definition is to define a label to anchor temporal scope. (See Section 3.3.) However, the <em>tag-group</em> is required if the <em>#</em> placeholder is used.</p></td>
  </tr>
  <tr>
   <td>
  </tr>
</table>


**Example:** Create a definition called _PlayMovie_ that represents playing a movie on the screen.

**Short form:** 
```
(Definition/PlayMovie, (Visual-presentation, Movie, Computer-screen))
```

**Long form:** 
```
(Property/Organization-property/Definition/PlayMovie,
(Property/Sensory-property/Sensory-presentation/Visual-presentation, 
Item/Object/Man-made-object/Media/Visualization/Movie,
Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Computerscreen))
```

The placeholder form of the definition is used, for example, to annotate an experimental parameter whose value is selected at random for each occurrence. The annotator can use a single definition name and just substitute the value for each occurrence. 

**Example:** Define _PresentationRate_ to annotate the rate of visual presentation of a stimulus.

**Short form:**
```
(Definition/PresentationRate/#,
(Visual-presentation, Experimental-stimulus, Temporal-rate/# Hz))
```

**Long form:**
```
(Property/Organizational-property/Definition/PresentationRate/#,
(Property/Sensory-property/Sensory-presentation/Visual-presentation, 
Property/Task-property/Task-event-role/Experimental-stimulus,
Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Temporal-rate/#))
```

When a definition name such as _PlayMovie_ or _PresentationRate_ is used in an annotation, the name is prefixed by _Def/_ to indicate that the name represents a defined name. In other words, _Def/PlayMovie_ is shorthand for _(Visual, Movie, Screen)_. Table 3.2 summarizes _Def/_ syntax rules.


##### **Table 3.2.** Syntax for using definitions in annotations with _Def/._

<table>
  <tr>
     <td><strong>Syntax</strong></td>
     <td><strong>Explanation</strong></td>
  </tr>
  <tr>
     <td>
       <p><strong>Short forms:</strong></p>
       <p><em>Def/XXX</em></p>
       <p><em>Def/XXX/#</em></p>
       <p><hr/>
       <p><strong>Long forms:</strong></p>
       <p><em>Property/Organizational-property/Def/XXX</em></p>
       <p><em>Property/Organizational-property/Def/XXX/#</em></p>
     </td>
     <td>
       <p><em>XXX</em> is the name of the definition.</p>
       <p>If the XXX/# form is used, the definition <em>(tag-group) 
          </em> for <em>XXX </em>must contain a single # that 
          represents the value to be substituted for the # 
          placeholder in the <em>Def/XXX/#</em>. In other words, a 
          <em>Def</em> tag cannot include #.</p>
     </td>
  </tr>
</table>

**Example:** Use the _PresentationRate_ definition to annotate a presentation rate of 1.5 Hz.

**Short form:**
```
Def/PresentationRate/1.5 Hz
```

**Long form:**
```
Property/Organizational-property/Def/PresentationRate/1.5 Hz
```

During analysis, tools usually replace _Def/PlayMovie_ with a fully expanded tag string. Tools must retain the association of the expanded tag string with the definition name for identification during searching and substitution. When a definition is expanded, the resulting tag string should include the definition name using the _Def-expand tag_. In other words, the tools should expand the definition as _(Def-expand/PlayMovie, Visual, Movie, Screen)_. The _Def-expand/PlayMovie_ is inserted in the definition tag group as part of the expansion to keep the association with the original definition.

**Usually definitions do not contain tags from the _Event_ subtree.** The standard practice is to use the elements of the _Event_ subtree as top-level tags to designate the general category of an event. This practice makes it easier for search and analysis tools to filter events without extensive parsing. The annotator can use tags such as _Experimental-stimulus_ (Long form: _Property/Task-property/Task-event-role/Experimental-stimulus_) to explain the role of a particular sensory presentation element in the experiment within the definition.

Definitions may appear anywhere in a HED event file or in auxiliary files associating metadata with HED tags such as JSON sidecars in BIDS datasets. Multiple definitions can be defined or used in the same HED string annotation, but definitions cannot be nested. Further, definitions must appear as top-level tag groups. Tools generally make a pass through the event information to extract the definitions prior to other processing. The validation checks made by the HED validator when assembling and processing definitions are summarized in **Appendix C**.

In addition to syntax checks, which occur in early processing passes, HED validators check that names are defined before they are used as definitions. Additional checks for temporal scope are discussed in **Section 3.3**.


### 3.3. Temporal scope

Events are often modeled as instantaneous occurrences that occur at single points in time (i.e., _time-marked_ or _point events_). In reality, many events unfold over extended time periods. The interval between the initiation of an event and its completion is called the **_temporal scope_** of the event. Some events, such as the setup and initiation of the environmental controls for an experiment, may have a temporal scope that spans the entire data recording. Other events, such as the playing of a movie clip or a participant performing an action in response to a sensory presentation, may last for seconds or minutes. Temporal scope captures the effects of these extended events in a machine-actionable manner.


#### 3.3.1. _Onset_/_Offset_ tags to express temporal scope

HED events are assumed to be point events unless they are given an explicit temporal scope (i.e., they are “scoped” events). The most direct HED method of specifying scoped events uses _Onset_ and _Offset_ tags with definitions. Using this method, an event with temporal scope actually corresponds to two point events. The event is initiated by a _(Def/XXX, Onset)_. The end of the event’s temporal scope is marked either by a _(Def/XXX, Offset)_ or by another _(Def/XXX, Onset)_. Table 3.3 summarizes _Onset_ and _Offset_ usage.


##### **Table 3.3.** Syntax for _Onset_ and _Offset_ use with defined names.

<table>
  <tr>
     <td><strong>Syntax</strong></td>
     <td><strong>Explanation</strong></td>
  </tr>
  <tr>
     <td>
        <p><strong>Short forms:</strong> 
        <p><em>(Def/XXX, Onset, (tag-group))</em></p>
        <p><em>(Def/XXX/#, Onset, (tag-group))</em></p>
        <p><em>(Def/XXX, Offset)</em></p>
        <hr></br>
        <p><strong>Long forms:</strong> 
<p>
        <p><em>(Property/Organizational-property/Def/XXX,Property/Data-property/Data-marker/Temporal-marker/Onset, (tag-group)</em>)</p>
        <p><em>(Attribute/Informational/Def/XXX/#, Property/Data-property/Data-marker/Temporal-marker/Onset,(tag-group))</em></p>
        <p><em>(Attribute/Informational/Def/XXX/#, Data-property/Data-marker/Temporal/Offset</em></p>
     </td>
   <td>
       <p><em>XXX</em> is the name of the definition and <em>tag-group</em> is an optional group of tags <strong>in addition</strong> to the tags in the definition.</p>
       <p>The additional <em>tag-group</em> is only in effect for that particular scoped event and <strong>not</strong> for all uses of <em>XXX</em>.</p>
       <p>If the <em>Def/XXX/#</em> form is used, the <em>#</em> must be replaced by an actual value.</p>
       <p>The definition for <em>XXX</em> must have a single # placeholder in its tag-group representing a value.</p>
   </td>
  </tr>
</table>

For example, the _PlayMovie_ definition of the previous section just defines the playing of a movie clip on the screen. The _(tag-group)_ might include tags identifying which clip is playing in this instance. This syntax allows one definition name to be used for the playing of many different clips. 

**Example:** An event sequence representing the playing of a Star Wars clip using _PlayMovie_.

**Short form:** 
```
[event 1] 
Sensory-event, (Def/PlayMovie, Onset, (Label/StarWars, (Media-clip, ID/3284)))
 
         .... [The Star Wars movie clip is playing] ....
    
[event n] 
Sensory-event, (Def/PlayMovie, Offset)
```

**Long form:**
```
[event 1] 
Event/Sensory-event,
(Attribute/Informational/Def/PlayMovie, 
Data-property/Data-marker/Temporal-marker/Onset,
(Attribute/Informational/Label/StarWars,
(Item/Object/Man-made-object/Media/Media-clip, Attribute/Informational/ID/3284)))                                           

        .... [The Star Wars movie clip is playing] ....

[event n]  
Event/Sensory-event,
(Attribute/Informational/Def/PlayMovie,
Data-property/Data-marker/Temporal-marker/Offset)
```

The _PlayMovie_ scoped event type can be reused to annotate the playing of other movie clips. However, scoped events with the same defined name (e.g., _PlayMovie_) cannot be nested. The temporal scope of a _PlayMovie_ event ends with a _PlayMovie_ _Offset_ or with the _Onset_ of another _PlayMovie_ event. 

Because tools need to have the definitions in hand when fully expanding during validation and analysis, tools must gather applicable definitions before final processing. Library functions in Python, Matlab, and JavaScript are being developed to support gathering of definitions and the expansion as described in **Section 5**. 


#### 3.3.2. _Duration_ as an alternative for expressing temporal scope

The _Duration_ tag is an alternative method for specifying an event with temporal scope. The start of the temporal scope is the event in which the _Duration_ tag appears. The end of the temporal scope is implicit and may not coincide with an actual event appearing in the recording. Instead, tools calculate when the scope ends in the data recording. _Duration_ tags do not need a defined label. _Duration_ may be grouped with tags representing the additional information associated with the temporal scope of that event. This grouping usually does not include tags from the _Event_ rooted tree.

**Example:** Use _Duration_ to represent the playing of a 2-second movie clip of Star Wars.

**Short form:**
```
Sensory-event,
(Duration/2 s, Visual-presentation, (Movie, Label/StarWars), Computer-screen)
```
**Long form:**
```
Event/Sensory-event, 
(Property/Data-value/Spatiotemporal-value/Temporal-value/Duration/2 s
Property/Sensory-property/Sensory-presentation/Visual-presentation,
(Item/Object/Man-made-object/Media/Visualization/Movie,
Property/Informational-property/Label/StarWars),
Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Computer-screen,
Property/Informational-property/Description/Play a movie clip for 2 s.)
```

The _Duration_ tag is convenient because its use does not require a _Definition_. The _Duration_ tag has the same effect on event context as the _Onset/Offset_ mechanism (as explained in **Section 3.4**.) However the ending of the temporal scope for events defined with _Duration_ is not marked by an explicit event in the data recording. This has distinct disadvantages for analysis if the offset is expected to elicit a neural response, which is the case for most events involving visual or auditory presentations.


#### 3.3.3. The _Delay_ tag for expressing temporal offsets to current event

The _Delay_ tag is grouped with a set of tags to indicate that the associated _tag-group_ is actually an implicit event that occurs at a time offset from the current event. A typical use case is when the user response time to a stimulus is recorded as a delay time relative to the onset of the corresponding stimulus event. This strategy is convenient for some time-locked analyses. HED tools could be developed to support the expansion of delayed events into actual events in the event stream, provided delays were consistently provided as signed numerical values relative to the anchor onset.

**Example:** A trial consists of the presentation of a cross on the center of the screen. The participant responds with a button press upon seeing the cross. The response time of the button push is recorded relative to the stimulus presentation as part of the stimulus event.

**Short form:**
```
Sensory-event, Experimental-stimulus, Visual-presentation,
(Cross, (Center-of, Computer-screen)),

(Agent-action, Delay/2.83 ms, (Participant-response, (Press, Mouse-button)))
```

**Long form:**
```
Event/Sensory-event, 
Property/Task-property/Task-event-role/Experimental-stimulus,
Property/Sensory-property/Sensory-presentation/Visual-presentation,
(Item/Object/Geometric-object/2D-shape/Cross,
(Relation/Spatial-relation/Center-of,
Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Computer-screen)),

(Event/Agent-action, 
Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/Delay/2.83 ms,
(Property/Task-property/Task-event-role/Participant-response,
(Action/Move/Move-body-part/Move-upper-extremity/Press,
Item/Object/Man-made-object/Device/IO-device/Input-device/Computer-mouse/Mouse-button))),

Property/Informational-property/Description/A cross is displayed 
in the center of the screen and the participant responds by pushing a button.
```

Notice that the _Agent-action_ tag from the _Event_ subtree is included in the _Delay_ tag-group. This allows tools to identify this tag-group as representing a distinct event. For BIDS datasets, such response delays would be in value columns of the `_events.tsv` event files. The HED annotation for the JSON sidecar corresponding to these files would contain a _#_. At HED expansion time, tools replace the _#_ with the column value (2.83) corresponding to each event. 


#### 3.3.4. Validation errors for _Onset_, _Offset_, _Duration_, and _Delay_

Validation of _Onset_ and _Offset_ cannot be completed until all of the annotations for a data recording have been assembled. The applicable validation errors are described in **Appendix C**.


### 3.4. The _Event-stream_ tag

An event stream is a sequence of events in a data recording. The most obvious event stream is the sequence consisting of all of the events in the recording, but there are many other possible streams such as the stream consisting of all sensory events or the stream consisting of all participant response events. 

Event streams can be identified and tagged using the _Event-stream_ tag, allowing annotators to more easily identify subsets of events and interrelationships of events within those event sequences. An event having the tag _Event-stream/XXX_ is part of event stream XXX.  

**Example:** Tag a face event indicating that it is part of the _Face-stream_ event stream. 

**Short form:**
```
Sensory-event, 
Event-stream/Face-stream, Visual-presentation, (Image, Face)
```

**Long form:** 
```    
Event/Sensory-event,
Property/Organizational-property/Event-stream/Face-stream,
Property/Sensory-property/Sensory-presentation/Visual-presentation,  
(Item/Object/Man-made-object/Media/Visualization/Image,
Item/Biological-item/Anatomical-item/Body-part/Head/Face)
```

Using a tag to identify an event stream makes it easier for downstream tools to compute relationships among subsets of events.

### 3.5. The _Event-context_ tag

Event annotations generally focus on describing what happened at the instant an event was initiated. However, the details of the setting in which the event occurs also influence neural responses. For the _PlayMovie_ example of the previous section, events that occur between the _Onset_ and _Offset_ pairs for _PlayMovie_ should inherit the information that a particular movie is playing without requiring the user to explicitly enter those tags for every intervening event. This process should be deferred until analysis time because other events might be added to the event file after the initial annotation of the recording. For example, a user might run a tool to mark blink or other features as events prior to doing other analyses. HED uses the _Event-context_ tag to accomplish the required context mapping.

Table 3.4 summarizes the syntax of the _Event-context_ tag. In normal usage, **this tag is not used directly by annotators**.  Rather, tools insert the _Event-context_ tag at analysis time to handle the implicit context created by enduring or scoped events. However, annotators may use the tag when an event has explicit context information that must be accounted for.

##### **Table 3.4.** Syntax for HED _Event-context_.

<table>
  <tr>
   <td><strong>Syntax</strong></td>
   <td><strong>Explanation</strong></td>
  </tr>
  <tr>
   <td>
      <p><strong>Short form:</strong></p>
      <p><em>(Event-context, other-tags)</em></p>
      <p><hr>
      <p><strong>Long form:</strong></p>
      <p><em>(Property/Organizational-property/Event-context, other-tags)</em></p>
   </td>
   <td> 
      <p>An event can have at most one <em>Event-context</em> 
      tag group.</p> 
      <p>HED-compliant analysis tools should insert the annotations 
      describing each temporally scoped event into the 
      <em>Event-context</em> tag group of the events within its 
      temporal scope during final assembly before analysis of the event.</p> 
      <p>Other task-event relationships may be inserted as tags 
      within the <em>Event-context</em> tag group either at 
      annotation time or analysis time.</p>
   </td>
  </tr>
</table>


### 3.6. Experimental controls, conditions, and responses

Most experiments are conducted by varying certain aspects of the experiment and measuring the resulting responses while carefully controlling other aspects. The intention of the experiment is annotated using the HED _Condition-variable_, _Control-variable_, and _Indicator-variable_ tags. 

The _Condition-variable_ tag is used to mark the independent variables of the experiment — those aspects of an experiment that are explicitly varied in order to observe an effect or to control bias. Contrasts, a term that appears in the neuroscience and statistical literature, are examples of experimental conditions, as are factors in experimental designs.

The _Indicator-variable_ tag is used to mark quantities that are explicitly measured or calculated to evaluate the effect of varying the experimental conditions. Indicator variables often fall into the _Event/Data-feature_ category. Sometimes the values of these data features are explicitly annotated as events. Researchers should provide a sufficiently detailed description of how to compute these data features so that they can be reproduced. 

The _Control-variable_ tag represents an aspect of the experiment that is held constant throughout the experiment, often to remove variability.

Researchers should use _Condition-variable_, _Control-variable_, and _Indicator-variable_ tags to capture the experiment intent and organization in as much detail as possible. Consistent and detailed description allows tools to extract the experiment design from the data in a machine-actionable form. Good tagging processes suggest creating definitions with understandable names to define these aspects of the dataset. This promotes easy searching and extraction for analyses such as regression or other modeling of the experimental design.

To illustrate the use of condition-variables to document experiment design, consider an experiment in which one of the conditions is the rate of presentation of images displayed on the screen. The experiment design compares responses under slow and fast image presentation rate conditions. To avoid unfortunate resonances due to a poor choice of rates, the “slow” and “fast” rate conditions each consist of three possible rates. Selection among the three eligible rates for the given condition is done randomly. 

In analysis, the researcher would typically combine all of the “slow presentation” trials into one group and all “fast presentation” trials into another group even though the exact task condition varies within the group varies according This type of grouping structure is very common in experiment design and can be captured by HED tags in a straightforward manner by defining condition variables for each group and using the # to capture variability within the group.

**Example:** Definitions of condition variables for slow and fast visual presentation rates.

**Short form:**
```
(Definition/SlowPresentation/#,
(Condition-variable/Presentation, Visual-presentation,
Computer-screen, Temporal-rate/#))

(Definition/FastPresentation/#,
(Condition-variable/Presentation, Visual-presentation,
Computer-screen, Temporal-rate/#))        
```

**Long form:**
```
(Property/Informational-property/Definition/SlowPresentation/#,
(Property/Organizational-property/Condition-variable/Presentation,
Property/Sensory-property/Sensory-presentation/Visual-presentation,
Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Computer-screen, 
Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Temporal-rate/#))

(Property/Informational-property/Definition/FastPresentation/#,
(Property/Organizational-property/**Condition-variable/Presentation,
Property/Sensory-property/Sensory-presentation/Visual-presentation, 
Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Computer-screen,
Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Temporal-rate/#))
```

_Organizational_ tags such as _Condition-variable_ are often used in the tag-groups of temporally scoped events. The _Onset_ of such an event represents the start of the _Condition-variable_. The corresponding _Offset_ marks the end of the period during which this condition is in effect. This type of annotation makes it straightforward to extract the experimental design from the events.

**Example:** Annotation of a sensory presentation under the _SlowPresentation_ condition.

**Short form:**
```
Sensory-event, (Def/SlowPresentation/1 Hz, Onset)
```

**Long form:**
```
Event/Sensory-event, 
(Property/Organizational-property/Def/SlowPresentation/1 Hz,
Property/Data-property/Data-marker/Temporal-marker/Onset)
```

During analysis, the _Def_ tags will be replaced with the actual definition’s tag group with an included _Def-expand_ tag giving the definition’s name. Note: expansion is done by tools at analysis time.

**Example:** Show the expanded form of the sensory event of the previous example.

**Short form with expansion:**
```
Sensory-event,
((Def-expand/SlowPresentation, Condition-variable/Presentation,
Visual-presentation, Computer-screen, Temporal-rate/1 Hz), Onset)
```

**Long form with expansion:**
```
Event/Sensory-event,
((Property/Organizational/Def-expand/SlowPresentation,
Property/Organizational/Condition-variable/Presentation,
Property/Sensory-property/Sensory-presentation/Visual-presentation,
Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Computer-screen,
Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Temporal-rate/1 Hz),
Property/Data-property/Data-marker/Temporal-marker/Onset)
```

Properly annotated condition variables and response variables can allow researchers to understand the details of the experiment design and perform analyses such as ANOVA (ANalysis Of VAriance) or regression to extract the dependence of responses on the condition variables. The time-organization of an experiment can be annotated with the Organizational tags _Time-block_ and _Task-trial_ and used for visualizations of experimental layout.

A typical experiment usually consists of a sequence of subject task-related activities interspersed with rest periods and/or off-line activities such as filling in a survey. The _Time-block_ tag is used to mark a contiguous portion of the data recording during which some aspect of the experiment conditions is fixed. _Time-block_ tags can be used to represent temporal organization in a manner similar to the way _Condition-variable_ tags are used to represent factors in an experiment design. 


### 3.7. Using the _Parameter_ tag to annotate specific information

A significant problem with schema design is term accretion. Each type of experiment will have specific terms or concepts that are important for the experiment’s purpose or design but are not widely applicable to other experiments. Schema designers might be tempted to add terms specific to familiar experiments or for annotators to extend the schema tree with terms specific to their experiments during annotation. 

The _Parameter_ tag and its children _Parameter-label_ and _Parameter-value_ are general-purpose tags designed to fill the missing term gap. They can be used to tag important specific concepts in a way that can be used for automated tools without triggering problems of accretion. For example, consider the problem of how to annotate repetition lag between successive presentations of a particular face image. There are several ways to annotate, but annotating with Parameter is a good compromise between machine

**Example:** Annotate the number of times a face image has appeared and the interval since last time this face was shown using _Parameter-value_:

**Short form:**
```
(Parameter-label/Count-of-this-face, Parameter-value/2)
(Parameter-label/Face-count-since-this-face-last-shown, Parameter-value/15)
```

**Example:** Annotate the number of times a face image has appeared and the interval since last time this face was shown using more specific tags for the value _Parameter-value_:

**Short form:**
```
(Parameter-label/Count-of-this-face, Item-count/2)
(Parameter-label/Face-count-since-this-face-last-shown,Item-count-interval/15)
```

**Long form:**
```
(Property/Informational-property/Parameter/Parameter-label/Count-of-this-face,
Property/Data-property/Data-value/Quantitative-value/Item-count/2),
(Property/Informational-property/Parameter/Parameter-label/Face-count-since-this-face-last-shown,
Property/Data-property/Data-value/Quantitative-value/Item-count-interval/15),
```

Using more specific tags as in the second version allows downstream tools to treat the value as numeric integers, facilitating automated processing. The use of _Parameter_ alerts downstream tools that this entity represents something that annotators regard as important to compute or record for analysis. Summary tools can extract all of the experimental parameters and their values, while statistical tools can look for dependencies on these variables. The parameter names are designed to be self-documenting. Parameters are often used for derived values such as response times that are used as indicator variables in the experiment. They are also sometimes used as part of control variable definitions.


## 4. HED library schema

The variety and complexity of events in electrophysiological experiments makes full documentation challenging. As more experiments move out of controlled laboratory environments and into less controlled virtual and real-world settings, the terminology required to adequately describe events has the potential to grow exponentially. In addition, experiments in any given subfield can contribute to pressure to add overly-specific terms and jargon to the schema hierarchy—for example, adding musical terms to tag events in music-based experiments, video markup terms for experiments involving movie viewing, traffic terms for experiments involving virtual driving, and so forth. Clinical fields using neuroimaging also have their own specific vocabularies for describing data features of clinical interest (e.g., _seizure_, _sleep stage IV_). Including these discipline-specific terms quickly makes the base HED schema unwieldy and less usable by the broader user community.

Third generation HED instead introduces the concept of the **HED library schema**. To use a programming analogy, when programmers write a Python module, the resulting code does not become part of the Python language or core library. Instead the module becomes part of a library used in conjunction with core modules of the programming language. 

Similar to the design principles imposed on function names and subclass organization in software development, HED library schemas must conform to some basic rules:

1. Every term must be unique _within_ the library schema and must conform to the rules for HED schema terms.
2. Schema terms should be readily understood by most users. The terms should not be ambiguous and should be meaningful in themselves without reference to their position in the schema hierarchy.
3. If possible, no schema sub-tree should have more than 7 direct subordinate sub-trees.
4. Terms that are used independently of one another should be in different sub-trees (orthogonality).

As in Python programming, we anticipate that many different HED schema libraries may be defined and used, in addition to the base HED schema. Libraries allow individual research communities to annotate details of events in experiments designed to answer questions of interest to particular research or clinical communities. Since it would be impossible to avoid naming conflicts across schema libraries that may be built in parallel by different user communities, HED supports schema library namespaces. Users will be able to add library tags qualified with namespace designators. All HED schemas, including library schemas, adhere to [semantic versioning](https://semver.org/). 


### 4.1. Defining a HED library schema

A HED library schema is defined in the same way as the base HED schema except that it has an additional attribute name-value pair, `library="xxx"` in the schema header. We will use as an illustration a library schema for driving. Syntax details for a library schema are similar to those for the base HED schema. **Appendix B** explains these in more detail.

**Example:** A template of the _.mediawiki_ format of a HED library schema for driving: 

````mediawiki
HED library="driving" version="1.0.0" 
!# start schema 
   [... contents of the HED driving schema ...]
!# end schema
   [... required sections specifying schema attribute definitions ...]
!# end hed
````

The required sections specifying the schema attributes  are _unit-class-specification_, _unit-modifier-specification_, _value-class-specification_, _schema-attribute-specification_, and _property-specification_.

**Example:** A template for the XML version of the HED driving library.

````xml
<?xml version="1.0" ?>
<HED library="driving" version="1.0.0">
    [... contents of the HED_DRIVE schema ... ]
</HED>
````

The schema XML file should be saved as HED_driving_1.0.0.xml to facilitate specification in tools.

### 4.2. Defining a library schema namespace for tagging

As part of the HED annotation process, users must associate a standard HED schema with their datasets. Users may also include tags from an arbitrary number of additional library schemas. For each library schema used to annotate a data recording, the user must associate a local name with the appropriate library schema name and version. Each library must be associated with a distinct local name within a recording’s annotations. The local names should be strictly alphabetic with no blanks or punctuation. 

The user must pass information about the library schema and their associated local names to processing functions. HED uses a standard method of identifying namespace elements by prefixing HED library schema tags with the associated local names. Tags from different library schemas can be intermixed with those of the base schema. Since the node names within a library must be unique, annotators can use short form as well as fully expanded tag paths for library schema tags as well as those from the base-schema.

**Example:** _Action/Drive/Change-lanes_ is a tag from the driving library schema with local name _dp_. The following tags are all possible tags:

```
dp:Action/Drive/Change-lanes
dp:Drive/Change-lanes
dp:Change-lanes
```

A colon (:) is used to separate the qualifying local name from the remainder of the tag. Notice that _Action_ also appears in the standard HED schema. Identical terms may be used in a library schema and the standard HED schema. Use of the same term implies a similar purpose. Library schema developers should try not to reuse terms in the standard schema unless the intention is to convey a close or identical relationship.


### 4.3. Schema attributes and classes in library schemas

In addition to the specification of tags in the main part of a schema, a HED schema has sections that specify unit classes, unit modifiers, value classes, schema attributes, and properties. The rules for the handling of these sections for a library schema are as follows:

1. The required sections of a library schema are: the _schema-specification_, the _unit-class-specification_, the _unit-modifier-specification_, the _value-class-specification_ section, the _schema-attribute-specification_ section, and the _property-specification_. The library schema must include all required schema sections even if the content of these sections is empty.
2. Any schema attribute, unit class, unit modifier, value class, or property used in the library schema must be specified in the appropriate section of the library schema regardless of whether these appear in base schema. Validators check the library schema strictly on the basis of its own specification without reference to another schema.
3. HED only supports the schema properties listed in Table B.2: _boolProperty_, _unitClassProperty_, _unitModifierProperty_, _unitProperty_, and _valueClassProperty_.  If the library schema uses one of these in the library schema specification, then its specification must appear in the _property-specification_ section of the library schema.
4. The library schema may define unit classes and units as desired or include unit classes or units from the base schema. Similarly, library schema may define unit modifiers or reuse unit modifiers from the base schema. HED validation and basic analysis tools validate these based strictly on the schema specification and do not use any outside information for these.
5. The standard value classes (_dateTimeClass*_, _nameClass_, _numericClass*_, _posixPath*_, _textClass_) if used, should have the same meaning as in the base schema. The hard-coded behavior associated with the starred (*) value classes will be the same. Library schema may define additional value classes and specify their allowed characters, but no additional hard-coded behavior will be available in the standard toolset. This does not preclude special-purpose tools from incorporating their own behavior.
6. The standard schema attributes (_allowedCharacter_, _defaultUnits_, _extensionAllowed_, _recommended_, _relatedTag_, <em>requireChild</em>, _required_, _SIUnit_, _SIUnitModifier_, _SIUnitSymbolModifier_, _suggestedTag_, _tagGroup_, _takesValue_, _topLevelTagGroup_, _unique_, _unitClass_, _unitPrefix_, _unitSymbol_, _valueClass_) should have the same meaning as in the base schema. The hard-coded behavior associated with the schema attributes will be the same. Library schema may define additional schema attributes. They will be checked for syntax, but no additional hard-coded behavior will be available in the standard toolset. This does not preclude special-purpose tools from incorporating their own behavior.
7. Regardless of whether a specification is in the base-schema or not, HED tools can perform basic syntax checking:
    1. All attributes used in the schema proper must be defined in the schema attribute section of the schema. Undefined attributes cause an error in schema validation.
    2. Similar rules apply to unit classes, unit modifiers, value classes, and properties.
    3. Actual handling of the semantics of any of these by HED tools only occurs for entities appearing in the base schema.


### 4.4. Using library schema in BIDS datasets 

The most common use case (for 99.9% of the HED users) is to use one of the standard HED schemas available on GitHub in the `hedxml` directory of the `hed-specification` repository ([https://github.com/hed-standard/hed-specification/tree/master/hedxml](https://github.com/hed-standard/hed-specification/tree/master/hedxml)). The HED version is included as the value of the `"HEDVersion"` key in the `dataset_description.json` metadata file located at the top level in a BIDS dataset. HEDTools retrieve the appropriate HED schema directly from GitHub when needed.

**Example:** A portion of the `dataset_description.json` of a dataset using `HED8.0.0.xml` stored on GitHub.

````json
{
   "Name": "A wonderful experiment",
   "BIDSVersion": "1.4.0", 
   "HEDVersion": "8.0.0"
}
````

#### 4.4.1 Proposed changes for HED library schemas handling in BIDS

This section explains the changes that are being proposed in BIDS to accommodate access to HED library schemas. **Appendix A.5.2.3** explains the proposed programmatic interface to support library schemas within the BIDS validator and the accompanying JavaScript HED validator. This section will be updated as the proposals progress though the BIDS review process. All `"fileName"` keys in the following discussion point to the names of files located in the `./code` directory of the dataset tree.

The major change to the BIDS specification is to allow the value associated with the `"HEDVersion"` key in the `dataset_description.json` file to be a dictionary rather than a string expressing the HED version. This proposed change will allow users more flexibility in specifying the base HED schema and will accommodate an arbitrary number of library schemas. The allowed top-level keys in this dictionary are: `"version"`, `"fileName"`, and `"libraries"`. The `"version"` and `"fileName"` keys pertain to the base HED schema, and if both are specified, `"version"` always takes precedence. 

The `"libraries"` key points to a libraries dictionary. The keys of the libraries dictionary are the nicknames used in the dataset to reference the schema. The values  The `"version"` key specifies the HED version number of a schema in the standard library and has the same effect as directly specifying.  `"fileName"`

**Example:** The following example specifies a base HED schema located in the `./code/myLocalSchema.xml` file of the dataset and two library schemas with nicknames `"la"` and `"lb"`.

```json
{
    "Name": "A wonderful experiment",
    "BIDSVersion": "1.4.0",
    "HEDVersion": {
        "fileName": "mylocalSchema.xml",
        "libraries": {
            "la": {
                "libraryName": "libraryA",
                "version": "1.0.2"
            },
            "lb": {
                "fileName": "HED_libraryB_0.5.3.xml"
            }
        }
    }
}
```

The `"la"` library schema is the `./hedxml/HED_libraryA_1.0.2.xml` file found in the [`hed-schema-library`](https://github.com/hed-standard/hed-schema-library) repository on the [`hed-standard`](https://github.com/hed-standard) working group GitHub site. HED tags from this library have the `la:` prefix (e.g., `la:XXX`).  The `"lb"` library schema can be found in the `./code/HED_libraryB_0.5.3.xml` file in the BIDS dataset. Tags from this library are prefixed with `lb:`. NOTE: This specification is preliminary and is waiting the resolution of BIDS formats for specifying external files as outline in [BIDS specification PR #820](https://github.com/bids-standard/bids-specification/pull/820).


## 5. Behavior of HED tools

This section gives an overview of the HED tools. Additional details and links to specific tools are available in **Appendix A**.


### 5.1. Short-form and long-form

Tools that are third-generation HED-compliant must be able to handle both short-form and long-form versions of HED strings. Analysis tools often need to transform all HED tags to long form before processing. To this end, mapping functions are being developed in Python, Matlab, and JavaScript. These libraries also provide mapping from long form to short form. As illustrated in the previous sections, the short form is much more readable and compact. 


### 5.2. Event file format (BIDS)

Dataset events are often represented using spreadsheets either in `.tsv` or Excel format. The rows of each spreadsheet correspond to events, while the columns contain identifying information pertaining to the events.  The first row of each spreadsheet usually contains column names that document what each column represents. Usually one column contains the time of the event. Other columns may contain categorical values, other values, or HED strings. Categorical column values are chosen from a small, explicitly defined subset. Value columns may contain numeric values or other types of values such as file names. HED tools assume that event files are spreadsheets, either in BIDS (`.tsv`) format or Excel format.

The HED tools require that each column of an event file contains items of the same class (categorical or value) and that value columns contain items of the same basic type. Files not satisfying these requirements may need additional processing before being handled by HED tools. BIDS (Brain Imaging Data Structure) datasets do have event files that satisfy these criteria.

BIDS uses tab-separated-value (`.tsv`) format for event files, with a required `onset` column containing the time of the event in seconds. BIDS also requires a `duration` column for event files. 

**Example:** Excerpt from a BIDS event file:

```
onset  duration  trial_type  response_time stim_file
1.2    0.6       go          1.435         images/red_square.jpg
5.6    0.6       stop        1.739         images/blue_square.jpg
```


The `trial_type` column contains categorical values, while the `response_time` and `stim_file` columns contain non-categorical values. In theory `stim_file` could be considered a categorical column if there were just a few possible images, but this would not be common usage. BIDS allows an optional column named `HED` to contain HED strings relevant for the event instance. The above example does not have this column. 

Processing tools read these event files and create their own event representation. The Python version of HEDTools uses the Pandas `DataFrame` for its low-level representations. For MATLAB programs, the dataset events are often held in `struct` arrays.  In EEGLAB, for example, the events for an EEG data recording appear in the `EEG.event` structure array. The time of the event is given in frames in the `EEG.event.latency` field for data that has not been epoched. 


### 5.3. Event dictionary sidecar format (BIDS)

Systems that handle HED annotation should be capable of defining and using metadata dictionaries in JSON format to specify HED tags applicable to the values in different columns of an event file.  BIDS uses JSON dictionaries called sidecars in a particular format. HEDTools assume that dictionaries for event metadata are contained in BIDS-compatible sidecars.

BIDS allows the tagging of both categorical and non-categorical columns in these sidecars as explained in the [HED appendix](https://github.com/bids-standard/bids-specification/blob/master/src/99-appendices/03-hed.md) of the BIDS specification. Internally, EEGLAB and CTAGGER use mapping objects that are stored in the EEG structure. However, these mapping options can be written to or read from BIDS JSON sidecars. 

Each events file spreadsheet column containing categorical values may also have a categorical dictionary that documents the meaning of the data in that column. HED also provides for the HED tagging of non-categorical columns as explained below. The following example shows the JSON sidecar format for annotating the same event file of the previous section. The `"HED"` key for the `"trial_type"` column indexes the categorical dictionary associated with the `trial_type` column in the event file. 

**Example:** JSON sidecar for annotating the columns of an events file.

````json
{
    "trial_type": {
        "LongName": "Event category",
        "Description": "Indicator of type of action that is expected.",
        "Levels": {
            "go": "A red square is displayed to indicate starting",
            "stop": "A blue square is displayed to indicate stopping."
        },
        "HED": {
            "go": "Sensory-event, Visual-presentation, (Square, Red), (Computer-screen, Center-of), Description/A red square is displayed to indicate starting.",
            "stop": "Sensory-event, Visual-presentation, (Square, Blue), (Computer-screen, Center-of), Description/A blue square is displayed to indicate stopping."
        }
    },
    "response_time": {
        "LongName": "Response time after stimulus",
        "Description": "Time from stimulus until subject presses button.",
        "Units": "ms",
        "HED": "(Delay/# ms, Agent-action, Experiment-participant, Press, Mouse-button, Description/Time from stimulus until subject presses button)"
    },
    "stim_file": {
        "LongName": "Stimulus file name",
        "Description": "Relative path of the stimulus image file",
        "HED": "Pathname/#, Description/Relative path of the stimulus image file"
    }
}
````

Non-categorical columns such as `response_time` and `stim_file` have a dictionary “HED” value consisting of a HED string rather than another dictionary. This HED string must have a single # placeholder. The corresponding value in the spreadsheet column replaces the # when the event annotation is assembled.


### 5.4. Levels of validation

Validation of HED annotations is an essential step in using HED for large-scale, reproducible analysis. Third-generation HED encourages a more detailed and useful documentation of events and provides mechanisms for mapping the interrelationships of events and task intent. The additional annotation power also requires more extensive validation to assure consistency across annotations. HED-validators are provided in both Python and JavaScript. There is also a MATLAB wrapper for the Python validator functions.

There are five levels of validation: tag level, string level, dictionary level, event level, and data-recording level. Previous generations of HED only required validation at the first four of these. Since third-generation HED can document relationships across events, it also requires an additional level to validate cross-event relationships. Validation can also be categorized as syntactic or semantic. Syntactic validation, which occurs mainly at the HED tag and HED string levels, tests that the tags are properly formed, independently of the HED schema or purpose of the tags. Semantic validation tests that the tags are used correctly and that they comply with the relevant schema. Syntactic validation is usually done initially during the parsing of the HED strings into HED tags.


#### 5.4.1. HED tag level validation

HED tag level validation checks each individual HED tag against its associated schema. The long-form tag must be in the schema. HED tags that take a value (have a # child in the schema) must have values that only contain appropriate characters. If the HED tag `#` has a _unitClass_ attribute, the units must comply with those of the specified _unitClass_. If the HED tag has additional nodes beyond the leaf node in the schema, the _extensionAllowed_ attribute must be in effect for the leaf node. 


#### 5.4.2. HED string level validation

HED string level validation focuses on the proper formation of HED strings and tag-groups within the HED strings. Syntactic HED string validation includes matching of parentheses and proper delimiting of HED tags by commas. Semantic HED string validation includes verification that HED definitions have the proper form.


#### 5.4.3. HED dictionary level validation

HED dictionary validation assumes that the dictionaries have been written in the JSON format of **Section 5.3**. The validation is similar to HED string evaluation, but the error messages are keyed to dictionary location rather than to line numbers in the event file or spreadsheet. The validator checks that there is exactly one # in the HED string annotation associated with each non-categorical column. The # placeholder should correspond to a # in the HED schema, indicating that the parent tag expects a value. If the placeholder is followed by a units designator, the validator checks that these units are consistent with the unit class of the corresponding # in the schema.  The units are not mandatory.


#### 5.4.4. HED event-level validation

Dataset formats such as BIDS (Brain Imaging Data Structure) allow users to provide HED tags in multiple places. For example, if a study uses local codes to represent different types of events, the dataset specification often allows users to use the local codes when listing the events and then provide some format of dictionary mapping local codes to tags. During event level validation, all of these tags must be assembled into a HED string representing the full HED annotation for that event. 

Several tag attributes are validated at this stage. The expanded event-level HED string annotating an event must include all of the tags with the _required_ attribute and only one copy of each tag with the _unique_ attribute.


#### 5.4.5. HED recording-level validation

The introduction of definitions and temporal scope has added an additional level of complexity to validation. Instead of being able to validate the HED string for each event individually, third generation HED validators must also check consistency across all of the events in the data-recording. This validation requires multiple passes through of the assembled HED tags associated with the data-recording.

Since _Definition_ tags can appear anywhere in the event annotations for a data recording, an initial scan must be made to assemble all of the definitions for a data recording and to make sure that the definition names are unique. 

To validate temporal scope, the validator must assure that each _Onset_ and _Offset_ tag is associated with an appropriately defined label. The validator must also check to make sure that _Onset _and _Offset_ tags are properly matched within the data recording.


### 5.5. Behavior in analysis tools

Third-generation HED analysis tools also require some additional infrastructure. These tools should call the HED libraries to fully expand the tags for a data recording before doing analysis. In addition to converting all HED tags to their long form, the library tools can remove the definitions and replace _def/_ with the full tag expansion with any defined labels. Each event that is within the temporal scope of a scoped event, should have the scoped event information added to the _Event-context_ tag group of the intermediate event upon request. _Delay_ tag expansions as insertions of actual events should also be supported. _Duration_ tag expansion in which offset events should be inserted should also be supported. The HED tools should provide this expansion capability as well as a standardized representation of events in a data recording to enable tools to use a standard API for accessing tag information.


### 5.6. HED-annotated data in BIDS

[BIDS (Brain Imaging Data Structure)](https://bids.neuroimaging.io/is ) is a specification along with supporting tools for organizing and describing brain imaging and behavioral data. BIDS supports HED annotation of events. BIDS events appear in tab-separated value (`_events.tsv`) files in various places in the dataset hierarchy. BIDS event files must have an `onset` column and a `duration` column. The example in **Section 5.2** shows such a BIDS event file. BIDS also recommends data dictionaries in the form of JSON sidecars to document the meaning of the data in the event files. The example in Section 5.2 also includes a JSON data dictionary.  

HED provides a JavaScript validator in the [hed-javascript](https://github.com/hed-standard/hed-javascript) repository, which is available as an installable package via [npm](https://www.npmjs.com/). The [BIDS validator](https://github.com/bids-standard/bids-validator) incorporates calls to this package to validate HED tags in BIDS datasets.

The [hedtools](https://github.com/hed-standard/hed-python/tree/master/hedtools) package includes input functions that use [Pandas](https://pandas.pydata.org/) data frames to construct internal representations of HED-annotated event files. Plans are underway to make this package available on the [PyPI](https://pypi.org/) package index for easy installation.


### 5.7. Mapping old HED tags into third generation HED tags

The HED system is now in its third generation of development. HED was introduced in 2013 to support annotation of events in [HeadIT](https://headit.ucsd.edu/), an early public repository of EEG data hosted by the Swartz Center for Computational Neuroscience, UCSD (Bigdely-Shamlo et al. 2013). HED-1G was partially based on CogPO (Turner and Laird 2012). Event annotation in HED-1G was organized around a single hierarchy whose root was the _Time-Locked Event_. Users could extend the HED-1G hierarchy at its deepest (leaf) nodes.

The second-generation of HED is sometimes referred to as HED-2G. HED-2G has multiple hierarchies with concepts that vary independently in different hierarchies. For example, if red-triangles and green-triangles are terms in a hierarchy, one is also likely to need red-squares and green-squares as well as  other colors.  Separating independent concepts such as shapes and colors into separate hierarchies, eliminates an exponential vocabulary growth due to term duplication in different branches of the hierarchy.  HED-2G also introduced nested parentheses to allow clear grouping of related terms.  A number of datasets have been annotated in HED-2G and released. HED-2G versions are HED 5.0.0 to HED 7.x.x. Third generation HED or HED-3G starts with HED 8.0.0.


## Appendices


## A. Resources in support of third generation HED


### A.1. HED documentation and websites

The following white paper explains the history, development, and motivation for third generation HED: 

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2020, August 1).
> Building FAIR functionality: Annotating events in time series data using Hierarchical Event Descriptors (HED).
> [https://doi.org/10.31219/osf.io/5fg73](https://doi.org/10.31219/osf.io/5fg73)

The following white paper gives a detailed case study in using HED-3G for tagging:

> Robbins, K., Truong, D., Appelhoff, S., Delorme, A., & Makeig, S. (2021, May 7). 
> Capturing the nature of events and event context using Hierarchical Event Descriptors (HED). 
> BioRxiv, 2021.05.06.442841. 
> https://doi.org/10.1101/2021.05.06.442841

A working document with the mapping of HED-3G terms and their descriptions to known ontologies is:

> [https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing](https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing)

Two other working documents hold portions of the HED-3G specification that are under development and will not be finalized for Release 1:

> HED-3G Working Document on Spatial Annotation
> [https://docs.google.com/document/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/view?usp=sharing](https://docs.google.com/document/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/view?usp=sharing)

> HED-3G Working Document on Task Annotation
> [https://docs.google.com/document/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/view?usp=sharing](https://docs.google.com/document/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/view?usp=sharing)

##### Table A.1. List of websites containing code and documentation.

<table>
  <tr>
   <td><strong>Description</strong></td>
   <td><strong>Site</strong></td>
  </tr>
  <tr><td colspan="2"><strong>Information and documentation</strong></td></tr>
  <tr>
   <td>HED organization website</td>
   <td><a href="https://www.hedtags.org">www.hedtags.org</a></td>
  </tr>
  <tr>
   <td>HED organization github</td>
   <td><a href="https://github.com/hed-standard">https://github.com/hed-standard</a></td>
  </tr>
  <tr>
   <td>HED specification repository</td>
   <td><a href="https://github.com/hed-standard/hed-specification">https://github.com/hed-standard/hed-specification</a>
   </td>
  </tr>
  <tr><td colspan="2"><strong>HED Python resources</strong></td></tr>
  <tr>
    <td>Python code repository</td>
    <td><a href="https://github.com/hed-standard/hed-python">https://github.com/hed-standard/hed-python</a></td>
   </tr>
   <tr>
      <td>Python validator and tools</td>
      <td><a href="https://github.com/hed-standard/hed-python/tree/master/hedtools">https://github.com/hed-standard/hed-python/tree/master/hedtools</a></td>
</tr>
 <tr>
    <td>Online tools/Docker deployment</td>
<td><a href="https://github.com/hed-standard/hed-python/tree/master/hedweb">https://github.com/hed-standard/hed-python/tree/master/hedweb</a></td>
</tr>
  <tr>
   <td colspan="2"><strong>HED JavaScript resources</strong></td>
  </tr>
  <tr>
   <td>HED JavaScript code</td>
   <td><a href="https://github.com/hed-standard/hed-javascript">https://github.com/hed-standard/hed-javascript</a></td>
   </tr>
   <tr>
   <td>BIDS validator</td>
   <td><a href="https://github.com/bids-standard/bids-validator"></a>href="https://github.com/bids-standard/bids-validator</td>
  </tr>
  <tr>
   <td colspan="2"><strong>HED Matlab resources</strong></td>
  </tr>
  <tr>
     <td>Matlab source code</td>
     <td><a href="https://github.com/hed-standard/hed-matlab">https://github.com/hed-standard/hed-matlab</a></td>
  </tr>
  <tr>
     <td colspan="2"><strong>CTAGGER resources</strong></td>
  </tr>
   <tr>
     <td>CTAGGER executable jar</td>
     <td><a href="https://github.com/hed-standard/hed-java/raw/master/ctagger.jar">https://github.com/hed-standard/hed-java/raw/master/ctagger.jar</a></td>
    </tr>
   <tr>
     <td>CTAGGER repository</td>
     <td><a href="https://github.com/hed-standard/CTagger">https://github.com/hed-standard/CTagger</a></td>
    </tr>
   <tr>
     <td>Java repository</td>
     <td><a href="https://github.com/hed-standard/hed-java">https://github.com/hed-standard/hed-java</a> </td>
    </tr>
  <tr>
   <td colspan="2"><strong>Online HED tools</strong></td>
  </tr>
  <tr>
     <td>Online website</td>
     <td><a href="https://hedtools.ucsd.edu/hed">https://hedtools.ucsd.edu/hed</a></td>
  </tr>
   <tr>
     <td>Docker deployment</td>
     <td><a href="https://github.com/hed-standard/hed-python/tree/master/webtools/deploy_hed">https://github.com/hed-standard/hed-python/tree/master/webtools/deploy_hed</a></td>
  </tr>
</table>


### A.2. Schema viewers

The HED schema is usually developed in _.mediawiki_ format and converted to XML for use by tools. However, researchers wishing to tag datasets will find both of these views hard to read. For this reason, we provide links to three versions of the schema in Table A.2. The expandable HTML viewer is easier to navigate. Annotators can also use CTAGGER which includes a schema viewer and tagging hints.

##### **Table A.2.** HED web-based schema vocabulary viewers.

<table>
  <tr>
   <td><strong>Viewer</strong></td>
   <td><strong>Link</strong></td>
  </tr>
  <tr>
   <td>Expandable HTML</td>
   <td><a href="https://www.hedtags.org/display_hed.html?version=8.0.0">https://www.hedtags.org/display_hed.html?version=8.0.0</a></td>
   </tr>
  <tr>
   <td>Mediawiki</td>
   <td><a href="https://github.com/hed-standard/hed-specification/blob/master/hedwiki/HED-generation3-schema-8.0.0.mediawiki">https://github.com/hed-standard/hed-specification/blob/master/hedwiki/HED-generation3-schema-8.0.0.mediawiki</a></td>
  </tr>
  <tr>
   <td>XML</td>
   <td><a href="https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0.xml">https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0.xml</a></td>
  </tr>
</table>


### A.3. CTagger for annotating data

The CTagger tool for annotating data provides a graphical user interface (GUI) to assist HED users in the annotation process. CTagger can be run as a standalone application ([https://github.com/hed-standard/hed-java/raw/master/ctagger.jar](https://github.com/hed-standard/hed-java/raw/master/ctagger.jar)) or using the HEDTools plug-in in EEGLAB. The tool is designed to ease the process of constructing HED strings, with features including tag search, an expandable schema-browser view, and free-form formatting. The interchangeability between long-short forms introduced in HED-3G is fully supported. CTagger is also compatible with BIDS, allowing users to import BIDS events.tsv and events.json files to extract the event structure. Once finished tagging, users can export their HED annotation into a json file compatible with BIDS events.json. See [CTagger Github repository](https://github.com/hed-standard/CTagger) for more details, guides, and tutorials.


### A.4. HED web-based services and tools

HED supports a number of web-based tools for HED validation, schema conversion and validation, JSON dictionary validation (as for a BIDS JSON sidecar for events), and validation of a single BIDS event file with supporting JSON sidecar. Additional web-based tools are planned for various analysis and conversion tasks. In addition, a HED web service interface is available for accessing many of the tools programmatically, including from MATLAB and Python programs. Table A.3. summarizes the location of the relevant URLs for online deployments of HED web-based tools and services.

##### Table A.3. URLs for accessing HED web-based tools and services online.

<table>
  <tr>
     <td><strong>URL</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><a href="https://hedtools.ucsd.edu/hed">https://hedtools.ucsd.edu/hed</a></td>
     <td>Main access point for online HED tools.</td>
  </tr>
  <tr>
     <td><a href="https://hedtools.ucsd.edu/hed/services">https://hedtools.ucsd.edu/hed/services</a></td>
     <td>Get the initial access CSRF token.</td>
  </tr>
  <tr>
     <td><a href="https://hedtools.ucsd.edu/hed/services_submit">https://hedtools.ucsd.edu/hed/services_submit</a></td>
     <td>Send the request for the service.</td>
  </tr>
</table>


#### A.4.1. HED web-based tools

The web-based tools are summarized in Table A.3. All of the tools are available from the main access point [https://hedtools.ucsd.edu/hed](https://hedtools.ucsd.edu/hed). The services are implemented in a Docker module and can be deployed locally provided that Docker is installed on the local machine. 

##### Table A.4. Web-based HED tools currently available.

<table>
  <tr>
     <td><strong>Tool</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td>Validate events</td>
     <td><p>Validate a BIDS-style events file with optional JSON sidecar.</p>
<p>The user uploads the two files to validate. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p> <p>The tool first validates the sidecar if present and if the sidecar contains no errors validates the events file in conjunction with the sidecar. If there are errors, the tool returns a downloadable file of error messages.</p></td>
  </tr>
  <tr>
     <td>Validate dictionary</td>
     <td><p>Validate a single BIDS-style events JSON sidecar.</p>
   <p>The user uploads the file. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p> 
  <p>If there are errors, the tool returns a downloadable file of error messages.</p></td>
  </tr>
  <tr>
     <td>Validate spreadsheet</td>
     <td><p>Validate an Excel or tsv file containing HED tags.</p> 
<p>The user uploads an Excel or tsv file and selects a worksheet if the file is an Excel file. The user indicates which columns contain HED tags. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p><p>If there are errors, the tool returns a downloadable file of error messages.</p></td>
  </tr>
  <tr>
    <td>Process string</td>
    <td><p>Validate or convert a HED string.</p>
<p>The user enters or pastes a HED string into a text box. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p><p>The user selects one of three processing options: 1) Validate,  2) Convert from long to short form, or 3) Convert from short to long form.</p> <p>The results appear in the results text box.</p></td>
  </tr>
  <tr>
     <td>Process schema</td>
     <td><p>Validate or check a HED schema.</p>
<p>The user enters the URL of a HED schema or uploads a HED schema file in either <em>.mediawiki</em> or <em>.xml</em> format. The user selects either the validate or convert option and presses the Submit button.</p><p>If the convert option was selected, the tools convert the schema to the other format and make the converted file available for download. If the validate option was selected, button, the tools check the file for compliance errors.</p></td>
  </tr>
</table>

#### A.4.2. HED web services

HED services are accessed by passing a JSON dictionary of parameters in a request to the online server. All requests include a `service` name and additional parameters. Table A.5. summarizes the available web-services and their parameters. The meaning of the different parameters is given in Table A.6.  


##### Table A.5. Summary of available web-services. 

<table>
  <tr>
     <td><strong>Service</strong></td>
     <td><strong>Parameters</strong></td>
     <td><strong>Descriptions</strong></td>
  </tr>
  <tr>
     <td><code>get_services</code></td>
     <td><code>none</code></td>
     <td>Returns a list of available services.</td>
  </tr>
  <tr>
     <td><code>dictionary_to_long</code></td>
     <td><code>json_string</code>,<br>
     <code>[schema_version, hed_schema_string]</code></td>
     <td>Returns either an error file or a JSON file converted to long form depending on whether conversion was successful or not.</td>
  </tr>
  <tr>
     <td><code>dictionary_to_short</code></td>
     <td><code>json_string</code>,<br>
         <code>[schema_version, hed_schema_string]</code></td>
     <td>Returns either an error file or a JSON file converted to long form depending on whether conversion was successful or not.</td>
  </tr>
  <tr>
     <td><code>dictionary_validate</code></td>
     <td><code>json_string</code>,<br><code>[schema_version, hed_schema_string]</code>,<br>
       <code>check_for_warnings</code></td>
     <td>Returns an error file if the JSON file has validation errors.</td>
  </tr>
  <tr>
    <td><code>events_assemble</code></td>
    <td><code>events_string</code>,<br>
        <code>json_string</code>,<br>
        <code>[schema_version, hed_schema_string]</code>,<br>
        <code>check_for_warnings</code>,<br>
        <code>defs_expand</code></td>
    <td>Returns an error file if the JSON file or events file has validation errors otherwise returns a file of assembled events.</td>
  </tr>
  <tr>
     <td><code>events_validate</code></td>
     <td><code>events_string</code>,<br>
         <code>json_string</code>,<br>
<code>[schema_version, hed_schema_string]</code>,<br>
<code>check_for_warnings</code></td>
     <td>Returns an error file if the JSON file or events file has validation errors.</td>
  </tr>
  <tr>
     <td><code>spreadsheet_validate</code></td>
     <td><code>spreadsheet_string</code>,<br>
<code>[schema_version, hed_schema_string]</code>,<br>
<code>check_for_warnings</code></td>
    <td>A tsv spreadsheet of event codes and their tags is sent to be validated. Returns an error file if the spreadsheet has validation errors.</td>
  </tr>
  <tr>
     <td><code>strings_to_long</code></td>
     <td><code>string_list</code>,<br>
<code>[schema_version, hed_schema_string]</code></td>
     <td>Convert a list of strings to long form if valid, otherwise return errors.</td>
  </tr>
  <tr>
     <td><code>strings_to_short</code></td>
     <td><code>string_list</code>,<br>
     <code>[schema_version, hed_schema_string]</code>
   </td>
     <td>Convert a list of strings to short form if valid, otherwise return errors.</td>
  </tr>
  <tr>
    <td><code>strings_validate</code></td>
    <td><code>hed_strings</code>,<br>
     <code>[schema_version, hed_schema_string]</code></td>
    <td><p>Validates a list of hed strings using the specified HED schema and returns a list of the same length as hed strings.</p><p> Each entry in the return list is either empty if the corresponding string has no errors or contains a string with the errors in readable form.</p></td>
  </tr>
</table>

The request is given as in JSON format. The possible keys and their types are described in Table A.6.

##### Table A.6. Top-level JSON parameter dictionary for HED services.

<table>
  <tr>
     <td><strong>Key</strong></td>
     <td><strong>Value</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>check_for_warnings</code></td>
     <td>boolean</td>
     <td>If true, check for warnings when validating.</td>
  </tr>
  <tr>
     <td><code>defs_expand</code></td>
     <td>boolean</td>
     <td>If true assembly expands definitions, replacing <em>def/XXX</em> with <em>def-expand/XXX</em>.</td>
  </tr>
  <tr>
     <td><code>events_string</code></td>
     <td>string</td>
     <td>Events tsv file with header passed as a string.</td>
  </tr>
  <tr>
     <td><code>hed_columns</code></td>
     <td>list of numbers</td>
     <td>A list of column numbers (starting with 1) of columns containing HED strings. If empty, all columns are used.</td>
  </tr>
  <tr>
     <td><code>hed_schema_string</code></td>
     <td>string</td>
     <td>HED schema in XML format as a string.</td>
  </tr>
  <tr>
     <td><code>hed_strings</code></td>
     <td>list of strings</td>
     <td>A list containing HED strings.</td>
  </tr>
  <tr>
     <td><code>json_string</code></td>
     <td>string</td>
     <td>BIDS-style JSON events sidecar as a string.</td>
  </tr>
  <tr>
     <td><code>json_strings</code></td>
     <td>string</td>
     <td>A list of BIDS-style JSON sidecars as strings.</td>
  </tr>
  <tr>
     <td><code>schema_string</code></td>
     <td>string</td>
     <td>A HED schema file as a string.</td>
  </tr>
  <tr>
     <td><code>schema_version</code></td>
     <td>string</td>
     <td>Version of HED to be accessed if relevant.</td>
  </tr>
  <tr>
     <td><code>service</code></td>
     <td>string</td>
     <td>The name of the requested service.</td>
  </tr>
  <tr>
     <td><code>spreadsheet_string</code></td>
     <td>string</td>
     <td>A spreadsheet tsv as a string.</td>
  </tr>
</table>


The web-services always return a JSON dictionary with four keys: `service`, `results`, `error_type`, and `error_msg`. If `error_type` and `error_msg` are not empty, the operation failed, while if these fields are empty, the operation completed. Completed operations always return their results in the `results` dictionary. The field of the `results` dictionary are shown in Table A.7

##### Table A.7. Keys in the `results` dictionary return as part of a HED web service response.

<table>
  <tr>
     <td><strong>Key</strong></td>
     <td><strong>Value</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>command</code></td>
     <td>string</td>
     <td>The command that was executed in response to the service request.</td>
  </tr>
  <tr>
     <td><code>data</code></td>
     <td>string</td>
     <td>The data returned by the service. This could be a list of errors or the processed result depending on what happened.</td>
  </tr>
  <tr>
     <td><code>schema_version</code></td>
     <td>string</td>
     <td>The version of the HED schema used in the processing.</td>
  </tr>
  <tr>
     <td><code>msg_category</code></td>
     <td>string</td>
     <td>One of success, warning, or failure depending on the result of processing the service.</td>
  </tr>
  <tr>
     <td><code>msg</code></td>
     <td>string</td>
     <td>Explanation of the result of service processing.</td>
  </tr>
</table>

The `hedweb/examples/matlab` directory of the `hed-python` repository gives running MATLAB examples of how to call these services in MATLAB.

### A.5. HED validation source code

#### A.5.1. HED validation in python

The python code for validation is in the  `hedtools` project located in the `hed-python` repository [https://github.com/hed-standard/hed-python](https://github.com/hed-standard/hed-python). You can install the tools using `pip` if you have downloaded the `hed-python` repository:

    pip install <hedtools-local-path>

The validation functions are in the `hed.validator` module. The data representations for various items such as dictionaries or event files can be found in the `hed.models` module. The hed_input.py module reads in a spreadsheet and possibly a dictionary and creates a `HedInput` object representing the spreadsheet. The `hed-validator.py` module creates a `HedValidator` object that takes a `HedSchema` object to use in subsequent validation. The `validate_input` method of `HedValidator` validates HED input in various formats and returns a list of issues.

#### A.5.2. HED validation in JavaScript

The JavaScript code for HED validation is in the validation directory of the `hed-javascript` repository located at [https://github.com/hed-standard/hed-javascript](https://github.com/hed-standard/hed-javascript).  

##### A.5.2.1. Installation

You can install the validator using `npm`:

    npm install hed-validator

##### A.5.2.2. Usage

This package contains two sub-packages. `hedValidator.validator` validates HED strings and contains the functions: `buildSchema`, which imports a HED schema and returns a JavaScript Promise object, and `validateHedString`, which validates a single HED string using the returned schema object. `hedValidator.converter` converts HED 3 strings between short and long forms and contains the following functions: `buildSchema`, which behaves similarly to the `buildSchema` function in `hedValidator.validator` except that it does not work with attributes, `convertHedStringToShort`, which converts HED strings from long form to short form, and `convertHedStringToLong`, which converts HED strings from short form to long form.

##### A.5.2.3. Programmatic interface

The programmatic interface to the HED JavaScript `buildSchema` must be modified to accommodate a base HED schema and arbitrary library schemas. Section 4.3.1 outlined the proposed changes in the BIDS specification from the viewpoint of the user.  The BIDS validator will require additional changes to locate the relevant HED schemas from the specification given by `"HEDVersion"` in `dataset_description.json`. The programmatic interface is similar to the JSON specification of section 4.3.1, except that the `"fileName"` key has been replaced by a `"path"` key to emphasize that callers must replace filenames with full paths before calling `buildSchema`. 

**Example:** JSON passed to `buildSchema` to construct the schemas needed for the example in Section 4.3.1. Here the dataset is located in `/data/wonderful`.

````json
{
    "path": "/data/wonderful/code/mylocal.xml",
    "libraries": {
        "la": {
            "libraryName": "libraryA",
            "version": "1.0.2"
        },
        "lb": {
            "libraryName": "libraryB",
            "path": "/data/wonderful/code/HED_libraryB_0.5.3.xml"
        }
    }
}
````

**NOTE:** This interface is proposed and is awaiting resolution of BIDS PR #820 on file passing to BIDS.

#### A.5.3. HED validation in MATLAB

HED validation can be done using the online web-services from MATLAB as shown in the `./examples/matlab` directory of the [hedweb](https://github.com/hed-standard/hed-python/tree/master/webtools) project in the [hed-python](https://github.com/hed-standard/hed-python) repository.


## B. HED schema specification and validation

HED schema developers generally do initial development of the schema using _.mediawiki_ format. The tools to convert schema between _.mediawiki_ and _.xml_ format are located in the `hed.schema` module of the [hedtools](https://github.com/hed-standard/hed-python/tree/master/hedtools) project of the hed-python repository located at  [https://github.com/hed-standard/hed-python](https://github.com/hed-standard/hed-python). All conversions are performed by converting the schema to a HedSchema object and then The modules `wiki2xml.py` and `xml2wiki.py` provide top-level functions to perform these conversions. This appendix presents the rules for HED base and library schema in `.mediawiki` and `.xml` formats.

### B.1. Mediawiki file specification

The rules for creating a valid `.mediawiki` specification of a HED schema are given below. 

#### B.1.1. The layout of the `.mediawiki` file

The overall layout of is `.mediawiki` schema file is:

````mediawiki
header-line: HED . . .
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
!# end hed
epilogue
````

Empty lines and lines containing only blanks are ignored.

#### B.1.2. The _.mediawiki_ _header-line_

The first line of the _.mediawiki_ file should be a _header-line_ that starts with the keyword `HED` followed by a blank-separated list of name-value pairs (Table B.1). 

##### **Table B.1.** Allowed parameters in the HED schema _.mediawiki_ header.

<table>
  <tr>
     <td><strong>Name</strong></td>
     <td><strong>Level</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>library</code></td>
     <td>Optional</td>
     <td>Name of library to be used in <em>.xml</em> file names. The value should consist of alphabetic characters only.</td>
  </tr>
  <tr>
     <td><code>version</code></td>
     <td>Required</td>
     <td>A valid semantic version number of the schema</td>
  </tr>
  <tr>
     <td><code>xmlns:xsi</code></td>
     <td>Optional</td>
     <td><code>xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"</code></td>
  </tr>
  <tr>
      <td><code>xsi:noNamespaceSchemaLocation</code></td>
      <td>Required/Optional</td>
      <td><p>Location of the XSD in effect, for example: <code>"https://github.com/hed-standard/hed-specification/raw/master/hedxml/HED8.0.0-beta.3.xsd"</code></p>
<p>The <code>xsi</code> attribute is required if <code>xmlns:xsi</code> is given.</p></td>
  </tr>
</table>

The `library` and `version` values are used to form the official xml file name and appear as attributes in the `<HED>` root of the `.xml` file`.` The versions of the schema that use XSD validation to verify the format (versions 8.0.0 and above) have `xmlns:xsi` and `xsi:noNamespaceSchemaLocation` attributes.

**Example:** Specify version 8.0.0 of the HED base schema.

The `.mediawiki` file has a header line:

````mediawiki
HED version="8.0.0"
````

The resulting XML root is:

```xml
<HED version="8.0.0">
```

The file name in `hedxml` in `hed-specification` is `HED8.0.0.xml`.

**Example:** Specify version 1.0.2 of the HED library schema `test`.

The `.mediawiki`  has a header line:

```mediawiki
HED library="test" version="1.0.2"
```

The resulting XML root is:

```xml
<HED library="test" version="1.0.2">`
```

The file name in `hedxml` in the hed schema library `test` is `HED_test_1.0.2.xml`.

Unknown _header-line_ attributes are translated as attributes of the `HED` root node of the `.xml` version, but a warning is used when the `.mediawiki` file is validated.

#### B.1.3. The _.mediawiki _specification format

The beginning of the HED specification is marked by the _start-line_:

```mediawiki
!# start schema
```

An arbitrary number of lines of informational text can be placed between the _header-line_ and the _start-line_. Older versions of HED have a CHANGE_LOG as well as information about the syntax and rules. New versions of HED generate a separate change log file for released versions. 

The end of the main HED-specification is marked by the end-line:

```mediawiki
!# end schema
```

The section separator lines (`!# start schema`, `!# end schema`, `!# end hed`) must only appear once in the file and must appear in that order within the file. A section separator is a line starting with !#.

The body of the HED specification consists of two types of lines: top-level node-specification specifications and other node specifications. Each specification is a single line in the `.mediawiki` file. Empty lines or lines containing only blanks are ignored. The basic format for a node-specification is:

```mediawiki
node-name  <nowiki>{attributes}[description]</nowiki>
```

Top-level node names are enclosed in triple single quotes (e.g., `'''Event'''`), while other node names have at least one preceding asterisk (*) followed by a blank and then the name. The number of asterisks indicates the level of the node in the subtree. HED-3G node names can only contain alphanumeric characters, hyphens, and underbars. They cannot contain blanks and must be unique. HED (2G) and earlier versions allow blanks.   Everything after the node name must be contained within `<nowiki></nowiki>` tags. Placeholder nodes have an empty node name, but are followed by a # enclosed in  `<nowiki></nowiki>` tags.

**Example:** Different types of HED node specifications.

**Top-level:**

```mediawiki
'''Property''' <nowiki>{extensionAllowed} [Subtree of properties.]</nowiki>
```

**Normal-level:**

```mediawiki
***** Duration <nowiki>{requireChild} [Time extent of something.]</nowiki>
```

**Placeholder-level:**

```mediawiki
****** <nowiki># {takesValue, unitClass=time,valueClass=numericClass}</nowiki>
```

The _Duration_ tag of this example is at the fifth level below the root of its subtree. The tag: _Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/Duration_ is the long form. The placeholder in the example is the node directly below _Duration_ in the hierarchy.

#### B.1.4. Specification of different schema sections 

After the line marking the end of the schema (`!# end schema`), the `.mediawiki` file contains the unit class specifications, unit modifier specifications, value class specification, the schema attribute specifications, and property specifications. All of these sections are required starting with HED version 8.0.0-beta.3 and must be given in this order.

The unit class specification section starts with `'''Unit classes'''`

**Example:**  Part of the HED unit class specification for time.

```mediawiki
'''Unit classes''' 
* time <nowiki>{defaultUnits=s}</nowiki> 
** second <nowiki>{SIUnit}</nowiki> 
** s <nowiki>{SIUnit, unitSymbol}</nowiki> 
```

**Example:**  Part of the HED unit modifier specification.

```mediawiki
'''Unit modifiers''' 
* deca <nowiki>{SIUnitModifier} [SI unit multiple for 10^1]</nowiki> 
* da <nowiki>{SIUnitSymbolModifier} [SI unit multiple for 10^1]</nowiki>
```

**Example:**  Part of the HED value class specification.

```mediawiki
'''Value classes'''
* posixPath <nowiki>{allowedCharacter=/,allowedCharacter=:}[Posix path specification.]</nowiki> 
```

**Example:**  Part of the HED schema attribute specification.

```mediawiki
'''Schema attributes'''
* allowedCharacter <nowiki>{valueClassProperty}[A schema attribute of value classes specifying a special character that is allowed in expressing the value of a placeholder.]</nowiki>
* defaultUnits <nowiki>{unitClassProperty}[A schema attribute of unit classes specifying the default units for a tag.]</nowiki> 
```

**Example:**  Part of the property specification.

```mediawiki
'''Properties''' 
* valueClassProperty <nowiki>[Indicates that the schema attribute is meant to be applied to value classes.]</nowiki> 
```

### B.2. HED XML format

The XML schema file format has a header, prologue, main schema, definitions, and epilogue sections. The general layout is as follows:

```xml
<?xml version="1.0" ?>
<HED library="test" version="0.0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://github.com/hed-standard/hed-specification/raw/master/hedxml/HED8.0.0-beta.3.xsd">
<prologue>unique optional text blob</prologue>
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

<epilogue>unique optional text blob</epilogue>
</HED>
```

The `<prologue>xxx</prologue>` and `<epilogue>xxx</epilogue>` elements are meant to be treated as opaque as far as schema processing goes. In earlier versions of HED the prologue section contained a Change Log for the schema as well as some basic documentation of syntax. The epilogue section contained additional metadata to be ignored during processing. The following subsections give a more detailed description of the format of these sections.

#### B.2.1. The schema node specification

The schema section of the HED XML document consists of an arbitrary number of `<node></node>` elements enclosed in a single `<schema></schema>` element.

```xml
<schema>
    <node> ... </node>
           ...
    <node> ... </node>
</schema>
```

A `<node>` element contains a required `<name>` child element, an optional `<description>` child element, and an optional number of additional `<attribute>` child elements:

```xml
<node>
    <name>xxx</name>
    <description>yyy</description>
    <attribute> ... </attribute>
    <attribute> ... </attribute>
    <attribute> ... </attribute>   
    <node> ... <node>
</node>
```

The `<name>` element text must conform to the rules for naming HED schema nodes. It corresponds to the _node-name_ in the `mediawiki` specification and must not be empty. A `#` value is used to represent value place-holder elements.

The `<description>` element has the text contained in the square brackets `[]` in the `.mediawiki` node specification. If the `.mediawiki` specification is missing or has an empty `[]`, the `<description>` element is omitted.

The optional `<attribute>` elements are derived from the attribute list contained in curly braces `{}` of the `.mediawiki` specification. An `<attribute>` element has a single non-empty `<name></name>` child element whose text value corresponds to the node-name of attribute in the corresponding `.mediawiki` file. If the attribute does not have the `boolProperty`, then the `<attribute>` element should also have one or more child `<value></value>` elements giving the value(s) of the attribute. 

**Example:** The `requireChild` attribute represents a boolean value. In the `.mediawiki` representation this attribute appears as `{requireChild}` if present and is omitted if absent.

**Old xml if true:**     

```xml
<node requireChild="true"><name>xxx</name></node>
```

**New xml if true:**

```xml
<node>
    <name>xxx</name>
    <attribute>
       <name>requireChild</name>
    </attribute>
</node>
```

**Example:** The `suggestedTag` attribute has a valid HED tag value. In the mediawiki representation this attribute is omitted if absent and appears when present as:

````mediawiki
    {suggestedTag=Sweet,suggestedTag=Gustatory/Salty, suggestedTag=Attribute/Sensory/Gustatory/Sour}
````

The `suggestedTag` attribute is meant to be used by tagging tools to suggest additional tags that a user might want to include. Notice that the `suggestedTag` values are  valid HED tags in any form (short, long, or intermediate).

**Old xml if present:**

```xml
<node suggestedTag="Sweet,Gustatory/Salty Attribute/Sensory/Gustatory/Sour">
    <name>xxx</name>
</node>
```

**New xml if present:**

```xml
<node>
   <name>xxx</name>
   <attribute>
      <name>suggestedTag</name>
    	 <value>Sweet</value>
    	 <value>Gustatory/Salty</value>
    	 <value>Attribute/Sensory/Gustatory/Sour</value>
   </attribute>
</node>
```

#### B.2.2. Unit class and unit modifier definitions

The valid HED-3G unit classes are defined in the `<unitClassDefinitions>` section of the XML schema file, and valid HED-3G unit modifiers are defined in the `<unitModifierDefinitions>` section. These sections follow a format similar to the `<node>` element in the `<schema>` section:

```xml
<unitClassDefinitions>
    <unitClassDefinition> ... </unitClassDefinition>
                          ... 
    <unitClassDefinition> ... </unitClassDefinition>
</unitClassDefinitions>
```

The `<unitClassDefinition>` elements have a required `<name>`, an optional `<description>` and an arbitrary number of additional `<attribute>` child elements. These `<attribute>` elements describe properties of the unit class rather than of individual unit types. In addition, `<unitClassDefinition>` elements may have an arbitrary number of `<unit>` child elements.

```xml
<unitClassDefinition>
    <name>time</name>
    <description>Temporal values except date and time of day.</description>
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

#### B.2.2. Value class definitions and behavior

HED has very strict rules about what characters are allowed in various elements of the HED schema, HED tags and the substitutions made for `#` placeholders. These rules are encoded in the schema using value classes. When a node name or placeholder substitution is given a particular value class, that name or substituted value can only contain the characters allowed for that value class. The allowed characters for a value class are specified in the definition of the value class. The HED validator and other HED tools may hardcode information about behavior of certain value classes (for example the `numericClass` value class). **HED does not allow commas or quotes in any of its values.**


##### Table B.2. Value classes.

<table>
  <tr>
     <td><strong>Class name </strong></td>
     <td><strong>Allowed characters</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>dateTimeClass*</code></td>
     <td><code>digits, T, :, -</code></td>
   <td>Date-times should conform to ISO8601 date-time format YYYY-MM-DDThh:mm:ss. Any variation on the full form is allowed.</td>
  </tr>
  <tr>
     <td><code>nameClass</code></td>
     <td><code>letters, digits, _, -</code></td>
     <td>Value class of node names and labels.</td>
  </tr>
  <tr>
     <td><code>numericClass*</code></td>
     <td><code>digits, ., -, +, E, e</code></td>
     <td>Value must be a valid numerical value.</td>
  </tr>
  <tr>
     <td><code>posixPath*</code></td>
     <td></td>
     <td>Specifies strings conforming to Posix path specification. This is not implemented and currently allows everything except commas.</td>
  </tr>
  <tr>
   <td><code>textClass</code>
   </td>
   <td><code>letters, digits, blank,+, -, :, ;, ., /, (, ),?, *, %, $, @</code>
   </td>
   <td>Value class for text descriptions.
   </td>
  </tr>
</table>


##### * indicates additional syntax checks

Value classes are defined in the `<valueClassDefinitions>` section of the XML schema file. These sections follow a format similar to the `<node>` element in the `<schema>`:

```
    <valueClassDefinitions>
       <valueClassDefinition> ... </valueClassDefinition>
                             ... 
       <valueClassDefinition> ... </valueClassDefinition>
    </valueClassDefinitions>
```

#### B.2.3. Schema attribute definitions and properties

The `<schemaAttributeDefinitions>` section specifies the allowed attributes of the other elements including the `<node>`, `<unitClassDefinition>`, `<unitModifierDefinition>`, and `<valueClassDefinition>` elements. The specifications of individual attributes are given in `<schemaAttributeDefinition>` elements.

```
    <schemaAttributeDefinitions>
       <schemaAttributeDefinition> ... </schemaAttributeDefinition>
                                   ... 
       <schemaAttributeDefinition> ... </schemaAttributeDefinition>
    </schemaAttributeDefinitions>
```

The individual `<schemaAttributeDefinition>` elements have the following format:

```
    <schemaAttributeDefinition>
       <name>allowedCharacter</name>
       <description>An attribute of value classes indicating a special character 
          that is allowed in expressing the value of that placeholder.</description>
       <property>
          <name>valueClassProperty</name>
       </property>
    <schemaAttributeDefinition>
```

The `<property>` elements indicate where various schema attributes apply. Their meanings are hard-coded into the schema processors. Table B.3 lists the names of these properties.


##### Table B.3. HED schema attribute properties.

<table>
  <tr>
   <td><strong>Schema attribute property</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>boolProperty</code>
   </td>
   <td>If a schema attribute has this property, then its values are either true or false. The schema processing translates the attribute into an <code>&lt;attribute></code> element with a <code>&lt;name></code> child but no <code>value</code> child.
   </td>
  </tr>
  <tr>
   <td><code>unitClassProperty</code>
   </td>
   <td>A schema attribute having this property can only apply to an <code>&lt;attribute></code> of <code>&lt;unitClassDefinition> elements.</code>
   </td>
  </tr>
  <tr>
   <td><code>unitModifierProperty</code>
   </td>
   <td>A schema attribute having this property can only apply to an <code>&lt;attribute></code> of <code>&lt;unitModifierDefinition> elements.</code>
   </td>
  </tr>
  <tr>
   <td><code>unitProperty</code>
   </td>
   <td>A schema attribute having this property can only apply to an <code>&lt;attribute></code> of <code>&lt;unit> elements.</code>
   </td>
  </tr>
  <tr>
   <td><code>valueClassProperty</code>
   </td>
   <td>A schema attribute having this property can only apply to an <code>&lt;attribute></code> of <code>&lt;valueClassDefinition> elements.</code>
   </td>
  </tr>
</table>


A given schema attribute can only apply to one type of element (`<node>`, `<unitClassDefinition>`, `<unitModifierDefinition>` or `<unit>`). Attributes that don’t have one of `<unitClassProperty>`, `<unitClassProperty>` or `<unitProperty>` are assumed to apply to `<node>` elements.

Table B.4 gives a list of the supported HED schema attributes. These attributes apply to different parts of the schema as indicated by their properties. 


##### Table B.4. HED schema attributes.

<table>
  <tr>
   <td><strong>Schema attribute</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>allowedCharacter*</code>
   </td>
   <td>A schema attribute of value classes specifying a special character that is allowed in expressing the value of a placeholder. Normally the allowed characters are listed individually. However, the word <code>letters</code> designates upper and lower case alphabetic characters. The word <code>digits</code> indicates the digits 0-9.
   </td>
  </tr>
  <tr>
   <td><code>defaultUnits</code>
   </td>
   <td>A schema attribute of unit classes specifying the default units to use if the placeholder has a unit class but the substituted value has no units. For example, when a <code>#</code> placeholder of the <code>time</code> unit class is replaced with an actual value and the units are not explicitly listed, they are assumed to be seconds (s) because the time unit class has <code>defaultUnits=s</code>.
   </td>
  </tr>
  <tr>
   <td><code>extensionAllowed</code>
   </td>
   <td>A schema attribute indicating that users can add unlimited levels of child nodes under this tag. This tag is propagated to child nodes with the exception of # placeholders.
   </td>
  </tr>
  <tr>
   <td><code>recommended</code>
   </td>
   <td>A schema attribute indicating that the event-level HED string should include this tag.
   </td>
  </tr>
  <tr>
   <td><code>relatedTag*</code>
   </td>
   <td>A schema attribute suggesting HED tags that are closely related to this tag. This attribute is used by tagging tools. Related categorical tags may have this attribute.
   </td>
  </tr>
  <tr>
   <td><code>requireChild</code>
   </td>
   <td>A schema attribute indicating that one of the node elements descendants must be included when using this tag.
   </td>
  </tr>
  <tr>
   <td><code>required</code>
   </td>
   <td>A schema attribute indicating that every event-level HED string should include this tag.
   </td>
  </tr>
  <tr>
   <td><code>SIUnit</code>
   </td>
   <td>A schema attribute indicating that this unit element is an SI unit and can be modified by multiple and submultiple names. Note that some units such as byte are designated as SI units although they are not part of the standard.
   </td>
  </tr>
  <tr>
   <td><code>SIUnitModifier</code>
   </td>
   <td>A schema attribute indicating that this SI unit modifier represents a multiple or submultiple of a base unit rather than a unit symbol.
   </td>
  </tr>
  <tr>
   <td><code>SIUnitSymbolModifier</code>
   </td>
   <td>A schema attribute indicating that this SI unit modifier represents a multiple or submultiple of a unit symbol rather than a base symbol.
   </td>
  </tr>
  <tr>
   <td><code>suggestedTag*</code>
   </td>
   <td>A schema attribute that indicates another tag  that is often associated with this tag. This attribute is used by tagging tools to provide tagging suggestions.
   </td>
  </tr>
  <tr>
   <td><code>tagGroup*</code>
   </td>
   <td>A schema attribute indicating the tag can only appear inside a tag group.
   </td>
  </tr>
  <tr>
   <td><code>takesValue</code>
   </td>
   <td>A schema attribute indicating the tag is a # placeholder that is expected to be replaced with a user-defined value.
   </td>
  </tr>
  <tr>
   <td><code>topLevelTagGroup*</code>
   </td>
   <td>A schema attribute indicating that this tag (or its descendants) can only appear in a top-level tag group.
   </td>
  </tr>
  <tr>
   <td><code>unique</code>
   </td>
   <td>A schema attribute indicating that only one of this tag or its descendants can be used  in the event-level HED string.
   </td>
  </tr>
  <tr>
   <td><code>unitClass</code>
   </td>
   <td>A schema attribute specifying which unit class this value tag belongs to.
   </td>
  </tr>
  <tr>
   <td><code>unitPrefix</code>
   </td>
   <td>A schema attribute applied specifically to <code>unit</code> elements to designate that the unit indicator is a prefix (e.g., <code>$</code> in the<code> currency</code> units).
   </td>
  </tr>
  <tr>
   <td><code>unitSymbol</code>
   </td>
   <td>A schema attribute indicating this tag is an abbreviation or symbol representing a type of unit. Unit symbols represent both the singular and the plural and thus cannot be pluralized.
   </td>
  </tr>
  <tr>
   <td><code>valueClass*</code>
   </td>
   <td>A schema attribute specifying which value class this value tag belongs to.
   </td>
  </tr>
</table>

* indicates an attribute that is new to HED-3G.

In addition to the attributes listed in Table B.4, some schema attributes have been deprecated and are no longer supported in HED-3G, although they are still present in earlier versions of the schema. Table B.5 lists these attributes.


##### Table B.5. Deprecated HED schema attributes.

<table>
  <tr>
   <td><strong>Schema attribute</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>default
   </td>
   <td>Indicates a tag assumed to be present if not explicitly given. This tag was not implemented in existing tools. Only the defaultUnits for the unit class will be implemented going forward.
   </td>
  </tr>
  <tr>
   <td>position
   </td>
   <td>Indicates the order within the overall tag string that this tag should appear during display. This was used to assist annotation tools, which sought to display required and recommend tags before others. The position attribute value should be an integer and the order can start at 0 or 1. Required or recommended tags without this attribute or with negative position will be shown after the others in canonical ordering. Because of the design of the schema vocabulary, this tag is not applicable in HED-3G.
   </td>
  </tr>
  <tr>
   <td>predicateType
   </td>
   <td>This attribute has a value which is one of <code>propertyOf</code>, <code>subclassOf</code>, or <code>passThrough</code>. This tag was added to facilitate mapping to OWL or RDF in earlier versions of the schema where property and subclass types appeared in the same hierarchy. The schema vocabulary redesign of HED-3G eliminated this issue.
   </td>
  </tr>
</table>





#### B.2.5. HED unit classes and unit modifiers

Table B.6 lists the current unit classes for HED-3G.

##### Table B.6. Unit classes for HED-3G.

<table>
  <tr>
   <td><strong>Unit class</strong>
   </td>
   <td><strong>Unit (Bold = SIUnit, * = unitSymbol)</strong>
   </td>
   <td><strong>defaultUnits</strong>
   </td>
  </tr>
  <tr>
   <td>time
   </td>
   <td><strong>second</strong>, <strong>s*,</strong> day, minute, hour
   </td>
   <td><strong>s*</strong>
   </td>
  </tr>
  <tr>
   <td>dateTime
   </td>
   <td>YYYY-MM-DDThh:mm:ss
   </td>
   <td>YYYY-MM-DDThh:mm:ss
   </td>
  </tr>
  <tr>
   <td>clockTime
   </td>
   <td>hour:min, hour:min:sec
   </td>
   <td>hour:min
   </td>
  </tr>
  <tr>
   <td>frequency
   </td>
   <td><strong>hertz</strong>, <strong>Hz*</strong>
   </td>
   <td><strong>Hz*</strong>
   </td>
  </tr>
  <tr>
   <td>angle
   </td>
   <td><strong>radian</strong>, <strong>rad*</strong>, degree
   </td>
   <td><strong>rad*</strong>
   </td>
  </tr>
  <tr>
   <td>physicalLength
   </td>
   <td><strong>metre</strong>, <strong>m*</strong>, foot, mile
   </td>
   <td><strong>m*</strong>
   </td>
  </tr>
  <tr>
   <td>pixels
   </td>
   <td>pixel, px
   </td>
   <td>px*
   </td>
  </tr>
  <tr>
   <td>area
   </td>
   <td><strong>metre^2</strong>, <strong>m^2*</strong>
   </td>
   <td><strong>m^2*</strong>
   </td>
  </tr>
  <tr>
   <td>volume
   </td>
   <td><strong>metre^3</strong>, <strong>m^3*</strong>
   </td>
   <td><strong>m^3*</strong>
   </td>
  </tr>
  <tr>
   <td>speed
   </td>
   <td><strong>m-per-s</strong>*, mph, kph 
   </td>
   <td><strong>m-per-s*</strong>
   </td>
  </tr>
  <tr>
   <td>acceleration
   </td>
   <td><strong>m-per-s^2*</strong>
   </td>
   <td><strong>m-per-s^2*</strong>
   </td>
  </tr>
  <tr>
   <td>jerk
   </td>
   <td><strong>m-per-s^3*</strong>
   </td>
   <td><strong>m-per-s^3*</strong>
   </td>
  </tr>
  <tr>
   <td>intensity
   </td>
   <td>dB
   </td>
   <td>dB
   </td>
  </tr>
  <tr>
   <td>luminousIntensity
   </td>
   <td>candela, cd
   </td>
   <td>cd
   </td>
  </tr>
  <tr>
   <td>memorySize
   </td>
   <td>byte, B
   </td>
   <td>B
   </td>
  </tr>
  <tr>
   <td>currency
   </td>
   <td>dollar, $, point, fraction
   </td>
   <td>$
   </td>
  </tr>
</table>


Table B.7 lists the current unit modifiers for HED-3G.

##### Table B.7. SI unit modifiers for HED-3G. 

<table>
  <tr>
   <td><strong>SI unit modifier</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>deca, da*
   </td>
   <td>SI unit multiple representing 10^1
   </td>
  </tr>
  <tr>
   <td>hecto, h*
   </td>
   <td>SI unit multiple representing 10^2
   </td>
  </tr>
  <tr>
   <td>kilo, k*
   </td>
   <td>SI unit multiple representing 10^3
   </td>
  </tr>
  <tr>
   <td>mega, M*
   </td>
   <td>SI unit multiple representing 10^6
   </td>
  </tr>
  <tr>
   <td>giga, G*
   </td>
   <td>SI unit multiple representing 10^9
   </td>
  </tr>
  <tr>
   <td>tera, T*
   </td>
   <td>SI unit multiple representing 10^12
   </td>
  </tr>
  <tr>
   <td>peta, P*
   </td>
   <td>SI unit multiple representing 10^15
   </td>
  </tr>
  <tr>
   <td>exa, E*
   </td>
   <td>SI unit multiple representing 10^18
   </td>
  </tr>
  <tr>
   <td>zetta, Z*
   </td>
   <td>SI unit multiple representing 10^21
   </td>
  </tr>
  <tr>
   <td>yotta, Y*
   </td>
   <td>SI unit multiple representing 10^24
   </td>
  </tr>
  <tr>
   <td>deci, d*
   </td>
   <td>SI unit submultiple representing 10^−1
   </td>
  </tr>
  <tr>
   <td>centi, c*
   </td>
   <td>SI unit submultiple representing 10^−2
   </td>
  </tr>
  <tr>
   <td>milli, m*
   </td>
   <td>SI unit submultiple representing 10^−3
   </td>
  </tr>
  <tr>
   <td>micro, u*
   </td>
   <td>SI unit submultiple representing 10^−6
   </td>
  </tr>
  <tr>
   <td>nano, n*
   </td>
   <td>SI unit submultiple representing 10^−9
   </td>
  </tr>
  <tr>
   <td>pico, p*
   </td>
   <td>SI unit submultiple representing 10^−12
   </td>
  </tr>
  <tr>
   <td>femto, f*
   </td>
   <td>SI unit submultiple representing 10^−15
   </td>
  </tr>
  <tr>
   <td>atto, a*
   </td>
   <td>SI unit submultiple representing 10^−18
   </td>
  </tr>
  <tr>
   <td>zepto, z*
   </td>
   <td>SI unit submultiple representing 10^−21
   </td>
  </tr>
  <tr>
   <td>yocto, y*
   </td>
   <td>SI unit submultiple representing 10^−24
   </td>
  </tr>
</table>


* indicates an SI unit symbol modifier.


### B.3. HED schema errors

This section is organized by the type of schema format that results in the error. Errors that might be detected regardless of the schema format start with HED_SCHEMA. Errors that are specific to the _.mediawiki_ format start with HED_WIKI.  Errors that occur in the construction of the XML version or that are detected by XML validators when the planned XSD validation is implemented start with HED_XML. All of the schema errors are summarized in **Table B.8**.


#### B.3.1. General schema errors

**HED_SCHEMA_ATTRIBUTE_INVALID**: An attribute that appears in a schema node has not been defined in the  schema attributes section of the schema file.

**HED_SCHEMA_CHARACTER_INVALID**: The specification contains an invalid character.

**HED_SCHEMA_DUPLICATE_NODE**: Node name appears in the schema more than once.

**HED_SCHEMA_HEADER_INVALID**: The schema header has an invalid format, contains invalid characters, or has unrecognized attributes.

**HED_SCHEMA_NODE_NAME_INVALID**: A schema node element name is empty or contains invalid characters.

**HED_SCHEMA_REQUIRED_SECTION_MISSING**: One of the required schema sections (corresponding to the schema, unit classes, unit modifiers, value classes, schema attributes or properties) is missing or in the wrong place.

**HED_SCHEMA_VERSION_INVALID**: The schema version specification in the HED line or element is invalid because the version specification does not have the correct syntax for the schema file format or the schema version does not comply with semantic versioning.


#### B.3.2. HED format-specific schema errors.

**HED_WIKI_DELIMITERS_INVALID**: Line content after node name is not enclosed with `<nowiki></nowiki> `delimiters; or the line has unmatched or multiple `<nowiki></nowiki>`, `[ ]`, or` { }` delimiters.

**HED_WIKI_LINE_START_INVALID**: Start of body line not `'''` or `*`.

**HED_WIKI_SEPARATOR_INVALID**: One of the required wiki section separators is missing or in the wrong place. The required separators are: `!# start schema`, `!# end schema`, and  `!# end hed`.

**HED_XML_SYNTAX_INVALID**: XML syntax or or does not comply with specified XSD.


#### B.3.3. Summary of validation errors for HED schema.

Table B.9 summarizes the errors relevant for HED schema.

##### **Table B.**9**.** Validation errors for HED schema.

<table>
  <tr>
   <td><strong>Error or warning</strong>
   </td>
   <td><strong>Explanation</strong>
   </td>
  </tr>
  <tr>
   <td><code>HED_SCHEMA_ATTRIBUTE_INVALID</code>
   </td>
   <td>Attribute not defined in one of the definition sections: <code>unitClassDefinitions</code>, <code>valueClassDefinitions</code>, <code>schemaAttributeDefinitions</code>.
   </td>
  </tr>
  <tr>
   <td><code>HED_SCHEMA_CHARACTER_INVALID</code>
   </td>
   <td>The specification contains an invalid character.
   </td>
  </tr>
  <tr>
   <td><code>HED_SCHEMA_DUPLICATE_NODE</code>
   </td>
   <td>Node name appears in the schema more than once.
   </td>
  </tr>
  <tr>
   <td><code>HED_SCHEMA_HEADER_INVALID</code>
   </td>
   <td>The schema header has an invalid format, contains invalid characters, or has unrecognized attributes.
   </td>
  </tr>
  <tr>
   <td><code>HED_SCHEMA_NODE_NAME_INVALID</code>
   </td>
   <td>Node element name is empty or contains invalid characters.
   </td>
  </tr>
  <tr>
   <td><code>HED_SCHEMA_REQUIRED_SECTION_MISSING</code>
   </td>
   <td>One of the required schema sections (corresponding to the schema, unit classes, unit modifiers, value classes, schema attributes or properties) is missing or in the wrong place.
   </td>
  </tr>
  <tr>
   <td><code>HED_SCHEMA_VERSION_INVALID</code>
   </td>
   <td>The version is invalid or does not use  semantic versioning.
   </td>
  </tr>
  <tr>
   <td><code>HED_WIKI_DELIMITERS_INVALID</code>
   </td>
   <td>Line content after node name is not enclosed with <code>&lt;nowiki>&lt;/nowiki> </code>delimiters; or the line has unmatched or multiple <code>&lt;nowiki>&lt;/nowiki></code>, <code>[ ]</code>, or<code> { }</code> delimiters.
   </td>
  </tr>
  <tr>
   <td><code>HED_WIKI_LINE_START_INVALID</code>
   </td>
   <td>Start of body line not <code>''' or *.</code>
   </td>
  </tr>
  <tr>
   <td><code>HED_WIKI_SEPARATOR_INVALID</code>
   </td>
   <td>One of the required wiki section separators is missing or in the wrong place. The required separators are: <code>!# start schema</code>, <code>!# end schema</code>, and  <code>!# end hed</code>.
   </td>
  </tr>
  <tr>
   <td>HED_XML_SYNTAX_INVALID
   </td>
   <td>XML syntax or or does not comply with specified XSD.
   </td>
  </tr>
</table>


## C. HED syntax details and validation errors

This appendix specifies the details and requirements for HED tags. It also summarizes the error codes used by the HED validators. 


### C.1. Valid characters

**HED_INVALID_CHARACTER**: HED uses ASCII encoding and does not support UTF-8. The allowed punctuation is limited. Table C.1 lists the allowed characters for various HED elements and explains some associated rules. 

##### Table C.1. Valid characters for various HED elements.

<table>
  <tr>
   <td><strong>HED element</strong>
   </td>
   <td><strong>Allowed characters and rules</strong>
   </td>
  </tr>
  <tr>
   <td>HED node element names
   </td>
   <td>Upper or lower case letters, numbers, hyphens, underbars.
<p>
The `#` is allowed as a placeholder in some situations. 
<p>
No blanks are allowed for HED versions >  8.0.0-alpha.1
<p>
Blanks around comma and parentheses delimiters are not considered to be part of the HED tag, but rather part of the separating delimiters. 
<p>
<strong>Style recommendation:</strong>HED node names should start with a capital letter, with the remainder lower case. Words within the name should be separated by hyphens.
   </td>
  </tr>
  <tr>
   <td>HED labels and definition names
   </td>
   <td>The values substituted for # in the HED tags /Attribute/Informational/Label/# and Attribute/Informational/Definition/# can only contain upper and lower case letters, numbers, hyphens, underbars, or periods.
   </td>
  </tr>
  <tr>
   <td>HED element values
   </td>
   <td>Blanks are allowed as are periods, dollar($), percent(%), caret(^), plus(+), minus(-), underbar(_), and semicolon(;). Values must conform to the underlying unit classes of the placeholder specification. Certain unit classes allow other special characters in their value specification. These special characters are specified in the schema with the <em>allowedCharacter</em> attribute. Examples of this are the forward slash in the <em>fileType</em> unit class and the colon in the dateTime unit class.
   </td>
  </tr>
  <tr>
   <td>Library nicknames
   </td>
   <td>Can only be a single word containing alphabetic characters. The name must be followed by a single colon and then the remainder of the tag. 
   </td>
  </tr>
</table>


Note: The **tilde syntax is no longer supported** for any version of HED and will generate a HED_INVALID_CHARACTER error.  Annotators should replace the syntax _(A ~ B ~ C)_ with _(A, (B,C))_.


### C.2. HED validation errors 

**HED_CHARACTER_INVALID**: String contains an invalid character. HED uses ANSI encoding and does not support UTF-8. Different parts of a HED string have different rules for acceptable characters as outlined in the specification (Section C.1).

**HED_COMMA_MISSING**: HED tag groups must be separated from other HED tags and tag groups with commas. Commas missing between two HED tags are generally detected as invalid HED tags, rather than as missing commas.

**HED_DEF_UNMATCHED**: A _Def_ tag cannot be correctly matched to a definition because the definition is missing or defined multiple times.

**HED_DEF_INVALID**: A _Def_ tag is incorrectly used, usually because of a mismatch between its _Definition_ placeholder and _Def_’s value.  This error is detected if the _Definition_ has a placeholder, but the _Def_ is used without a value, or the _Definition_ does not have a placeholder, but the _Def_ is used with a value.

**HED_DEFINITION_INVALID**: The _Definition_ syntax is incorrect or the _Definition_ contains other _Def_ or _Definition _tags.  Potential syntax errors include invalid definition names or a definition value that is not a single valid tag-group. Definitions that include a # placeholder must have exactly two # characters: one after the definition name and one in the definition body. Definitions that have too many # placeholders, not enough placeholders, or placeholders in the incorrect positions also generate this error.

**HED_GENERIC_ERROR**: The expression raised an error that did not fall into other categories.

**HED_GENERIC_WARNING**: The expression raised a warning that did not fall into other categories.

**HED_LIBRARY_UNMATCHED**: A tag that starts with **_name:_** is interpreted as a library schema nickname name. The association of **_name_** with an actual HED library schema must be passed to the validator when the string containing the tag is validated.

**HED_NODE_NAME_EMPTY**:** **A HED string cannot start or end with a slash, nor can a tag have consecutive slashes as all of these imply an empty tag node name within a HED tag.

**HED_ONSET_OFFSET_ERROR**: An _Onset_ or _Offset_ tag appears without being grouped with a defined name (using _Def_) with a tag-group containing a _Def-expand_. An _Offset_ tag appears before an _Offset_ tag of the same name.

**HED_PARENTHESES_MISMATCH**: The number of opening and closing parentheses in a HED string must be equal. 

**HED_PLACEHOLDER_INVALID**: A JSON sidecar with HED annotations cannot have a placeholder (`#`) in the tag dictionary for a categorical column and must have exactly one placeholder in the tag string for a value column. 

**HED_REQUIRED_TAG_MISSING**: A tag has the required attribute but is not present in the assembled event string.

**HED_SIDECAR_KEY_MISSING**: (WARNING) The annotation for a categorical value in the events file is missing, although its column has a HED dictionary in the JSON sidecar.

**HED_STYLE_WARNING**: (WARNING) A tag, tag extension, or label does not follow HED naming conventions. Tag names should start with a capital letter with the remainder lower case. Blanks are not allowed for HED-3G labels or tag extensions. Use hyphens instead.

**HED_TAG_EMPTY**: A HED string cannot have multiple consecutive commas (ignoring white space) without intervening non-empty HED tags. A HED string cannot begin or end with a comma, which also implies an empty HED tag. A tag group cannot be empty, so empty parentheses are not allowed.

**HED_TAG_EXTENDED**: (WARNING) Issued to warn annotators that this tag represents an extension of the HED schema. Often such tags were really spelling errors and not meant to extend the schema.

**HED_TAG_GROUP_ERROR:** A tag has `tagGroup` or `topLevelTagGroup` attribute but is not in an appropriate tag group or a `topLevelTagGroup` tag appears in the same tag group as other tags with the `topLevelTagGroup` attribute.

**HED_TAG_INVALID**: The tag is not valid in this schema, has incorrect format, or is used as a tag extension or placeholder value while appearing elsewhere in the schema. Note: an existing HED node cannot be used as a value or extension.

**HED_TAG_NOT_UNIQUE**: This event-level HED string has multiple occurrences of a tag with the _unique_ schema attribute.

**HED_TAG_REPEATED**: HED tags or tag-group cannot be repeated in grouping. _(A, (A, B))_ is not considered to be a duplicate, while  _(A, (B, C), A)_ and _(A, (B, C), (C, B))_ are repeated. HED strings are not ordered, so _(B, C)_ is considered to be equivalent to _(B, C)_.

**HED_TAG_REQUIRES_CHILD**: A HED tag requires an additional ending node because its current ending node has the _requireChild_ schema attribute.

**HED_TILDES_UNSUPPORTED**: The tilde notation is no longer supported. Replace _(A ~ B ~ C)_ with _(A, (B, C))_. Replace _(A ~ B)_ with _(A, B)_.

**HED_UNITS_DEFAULT_USED**: (WARNING) A HED tag value is missing units so the default units are used.

**HED_UNITS_INVALID**: The HED tag has a value with units that are invalid or not of the correct unit class for the tag. A typical mistake is to use unit modifiers with units that are not SI units.

**HED_VALUE_INVALID**: The value substituted for a placeholder (`#`) is not valid or compatible with the specified value class.

**HED_VALUE_IS_NODE**: An existing HED node name cannot be used as a value or extension. This is true for all HED schemas regardless of version.

**HED_VERSION_WARNING**: (WARNING) The HED version number or HED schema was not provided or was invalid, so the latest version is used.


### C.3. Summary of HED validation errors

Table C.2 Lists the validation errors checked for by the validator.


##### Table C.2. Summary of HED validator errors and warnings.


<table>
  <tr>
   <td><strong>Error or warning</strong>
   </td>
   <td><strong>Explanation</strong>
   </td>
  </tr>
  <tr>
   <td>HED_CHARACTER_INVALID
   </td>
   <td>String contains an invalid character.
   </td>
  </tr>
  <tr>
   <td>HED_COMMA_MISSING
   </td>
   <td>Comma missing, usually separating tag groups.
   </td>
  </tr>
  <tr>
   <td>HED_DEF_UNMATCHED
   </td>
   <td>A <em>Def</em> tag cannot be matched to definition.
   </td>
  </tr>
  <tr>
   <td>HED_DEF_INVALID
   </td>
   <td>A <em>Def</em>’s value is incorrect or does not match its <em>Definition</em> #. 
   </td>
  </tr>
  <tr>
   <td>HED_DEFINITION_INVALID
   </td>
   <td>A <em>Definition</em>’s syntax is invalid or definitions are nested.
   </td>
  </tr>
  <tr>
   <td>HED_GENERIC_ERROR
   </td>
   <td>HED expression raised an uncategorized error.
   </td>
  </tr>
  <tr>
   <td>HED_GENERIC_WARNING
   </td>
   <td>HED expression raised an uncategorized warning.
   </td>
  </tr>
  <tr>
   <td>HED_LIBRARY_UNMATCHED
   </td>
   <td>A tag starting with <em>name:</em> does not have an associated library.
   </td>
  </tr>
  <tr>
   <td>HED_NODE_NAME_EMPTY
   </td>
   <td>Extra slashes at beginning, end, or within a tag imply empty node names.
   </td>
  </tr>
  <tr>
   <td>HED_ONSET_OFFSET_ERROR
   </td>
   <td>Unnamed or unmatched <em>Onset</em> or <em>Offset</em> tag.
   </td>
  </tr>
  <tr>
   <td>HED_PARENTHESES_MISMATCH
   </td>
   <td>HED string has mismatched parentheses.
   </td>
  </tr>
  <tr>
   <td>HED_PLACEHOLDER_INVALID
   </td>
   <td>A # is missing or appears in a place that it should not. 
   </td>
  </tr>
  <tr>
   <td>HED_REQUIRED_TAG_MISSING
   </td>
   <td>Event annotation missing a required tag.
   </td>
  </tr>
  <tr>
   <td>HED_SIDECAR_KEY_MISSING*
   </td>
   <td>A categorical value is missing HED tags.
   </td>
  </tr>
  <tr>
   <td>HED_STYLE_WARNING*
   </td>
   <td>Extension or label does not follow HED naming conventions.
   </td>
  </tr>
  <tr>
   <td>HED_TAG_EMPTY
   </td>
   <td>Extra commas or empty parentheses indicate empty tags.
   </td>
  </tr>
  <tr>
   <td>HED_TAG_EXTENDED*
   </td>
   <td>HED tag represents an extension from the schema.
   </td>
  </tr>
  <tr>
   <td>HED_TAG_GROUP_ERROR
   </td>
   <td>A tag has <code><em>tagGroup</em></code> or <code><em>topLevelTagGroup</em></code> attribute but is not in an appropriate tag group or a <em>topLevelTagGroup</em> tag appears in the same tag group as other tags with the <em>topLevelTagGroup</em> attribute.
   </td>
  </tr>
  <tr>
   <td>HED_TAG_INVALID
   </td>
   <td>HED tag has incorrect format, does not exist in schema, or is a tag extension that appears elsewhere in the schema.
   </td>
  </tr>
  <tr>
   <td>HED_TAG_NOT_UNIQUE
   </td>
   <td>HED tag with <em>unique</em> attribute appears more than once.
   </td>
  </tr>
  <tr>
   <td>HED_TAG_REPEATED
   </td>
   <td>Tags cannot be repeated in the same tag group or level.
   </td>
  </tr>
  <tr>
   <td>HED_TAG_REQUIRES_CHILD
   </td>
   <td>HED tag requires an additional ending node.
   </td>
  </tr>
  <tr>
   <td>HED_TILDES_UNSUPPORTED
   </td>
   <td>Replace (a ~ b ~ c) with (a, (b, c)).
   </td>
  </tr>
  <tr>
   <td>HED_UNITS_DEFAULT_USED*
   </td>
   <td>HED tag value has a unit class but no units are specified. Default units are used if available.
   </td>
  </tr>
  <tr>
   <td>HED_UNITS_INVALID
   </td>
   <td>HED tag value has incorrect or invalid units.
   </td>
  </tr>
  <tr>
   <td>HED_VALUE_INVALID
   </td>
   <td>The value substituted for a placeholder is invalid.
   </td>
  </tr>
  <tr>
   <td>HED_VERSION_WARNING*
   </td>
   <td>The HED version is not provided, so the latest is used.
   </td>
  </tr>
</table>


* Indicates a warning
