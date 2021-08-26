# Scope of HED (third generation)

HED (an acronym for Hierarchical Event Descriptors) is an evolving framework that facilitates the description and formal annotation of events identified in time series data, together with tools for validation and for using HED annotations in data search, extraction, and analysis. This specification describes the third generation of HED or HED-3G in its current alpha form. HED-3G specifically refers to HED version 8.0.0-alpha.1 and above.

Third generation HED represents a significant advance in documenting the content and intent of experiments in a format that enables large-scale cross-study analysis of time-series behavioral and neuroimaging data, including but not limited to EEG, MEG, iEEG, eye-tracking, motion-capture, EKG, and audiovisual recording. In principle, third generation HED might be extended or adapted to annotate events in any other type of ordered or time series data. Without adequate documentation of the nature as well as the timing of these events, time series data may have limited value for further analysis beyond the specific analysis goal for which they were acquired. By adequately documenting experiment events using HED-3G, researchers can expand the utility of their data for a broader and longer lasting range of uses. 

Recorded events in behavioral and neuroimaging time series data may be of several types: (1) planned and delivered *sensory stimulation events*, or unplanned *sensory presentations* experienced by the imaged participant(s) or by other agents (e.g., human, animal, real, virtual, storied), (2) participant or other agent *action events* (e.g., time-recorded onsets or other features of body and eye movements, facial expressions), (3) *data feature events* (e.g., emergent data features or phenomena, whether detected online by the recording application or noted post hoc through machine or expert inspection), (4) *control events* (e.g., changes in experiment parameters, task conditions), (5) *procedure events* (e.g., activities that occur during the course of the experiment such as administering a survey or taking a saliva swab), (6) *structural events* (e.g., markers inserted for information about the experiment including metadata that might be useful for analysis), and (7) _measurement events_ (e.g., are markers inserted by external monitoring).

First generation HED attempted to describe events using a strictly hierarchical vocabulary. Difficulties inherent in early approaches led to extension of the formal structure into a second and now third generation. The structure of the HED-3G vocabulary may now be better described as heterarchical collections of terms, each of which may have hierarchical syntax and definition. 

HED-3G is also designed to be modular, thereby remaining compact in its core instantiation but allowing any number of ontological extensions for notating events in fields beyond neuroimaging in which event-related interpretation of time series requires that events be adequately described to support analysis within a common framework. To enable and regulate the extension process, the root HED-3G head schema specified here includes, for the first time, *HED library schema* to extend the HED vocabulary to include terms and concepts of importance to individual user communities -- for example researchers who design and perform experiments to study brain and language, brain and music, or brain dynamics in natural or virtual reality environments. The HED library schema concept may also be used to extend HED annotation to encompass specialized vocabularies used in clinical research and practice. **When the term HED is used in this document, it refers to third generation (HED-3G) unless explicitly stated otherwise.**

This document is a specification document that articulates syntax and processing rules for HED tool developers. The document provides some examples to illustrate these rules, but several separate tutorials and user guides are being developed. All HED-related source and documentation repositories are housed on the HED-standard GitHub site, [https://github.com/hed-standard](https://github.com/hed-standard). A detailed list of HED resources appears in Appendix A. HED development is open-source and community-based. We encourage those interested to contribute to the development process. Users are encouraged to use the _Issues_ mechanism of the `hed-specification` repository on the GitHub `hed-standard` working group website: [https://github.com/hed-standard/hed-specification/issues](https://github.com/hed-standard/hed-specification/issues).


### 2.1. Goals of HED

Event annotation documents the _things happening during data recording_ whether or not they are necessarily relevant to data analysis and interpretation. Commonly recorded events in electrophysiological data collection include the initiation, termination, or other features of **stimulus presentations** and **participant** **actions**. Other events may be **unplanned environmental events** (for example, sudden onset of noise and vibration from construction work unrelated to the experiment, or a laboratory device malfunction), events recording **changes in experiment control** parameters as well as **data feature events** and control **mishap events** that cause operation to fall outside of normal experiment parameters. 

The goals of HED are to provide a standardized annotation system that allows researchers to:

1. *Document* the exact natures of events (sensory, behavioral, environmental, and other) that occur during recorded time series data that may inform data analysis and interpretation.
2. *Describe* in detail the design of the experiment including participant task(s).
3. *Relate* event occurrences both to the experiment design and to participant tasks and experience.
4. *Provide* a basic infrastructure for building and using machine-actionable tools to systematically analyze data associated with recorded events in and across data sets, studies, paradigms, and modalities.

Current systems in neuroimaging experiments do not record events beyond simple numerical (3) or text (Event type Target) labels whose more complete and precise meanings are known only to the experimenter(s). A central goal of HED is to enable building of archives of brain imaging data in a form amenable to new forms of larger scale analysis, both within and across studies. Such event-related analysis requires that the nature(s) of the recorded events be specified in a common language. The HED project seeks to formalize the development of this language, to develop and distribute tools that maximize its ease of use, and to inform new and existing researchers of its purpose and value.


### 2.2. HED design principles

The near decade-long effort to develop effective event annotation for neurophysiological and behavioral data, culminating to date in HED-3G, has revealed the importance of four principals (aka the PASS principles), all of which have roots in other fields:


1. Preserve orthogonality of concepts in specifying vocabularies.
2. Abstract functionality into layers (e.g., more general vs. more specific).
3. Separate implementation from the interface (for flexibility).
4. Separate content from presentation (to maintain a unique, sufficient internal representation, while presenting data to users in forms they can more readily review and understand).

Orthogonality, the notion of keeping independently applicable concepts in separate hierarchies (1 above), has long been recognized as a fundamental principle in reusable software design, distilled in the design rule: *Favor composition over inheritance* (Gamma et al. 1994). *Abstraction of functionality into layers* (2) and *Separation of content from presentation* (4) are well-known principles in user-interface and graphics design that allow tools to maintain a single internal representation of needed information while emphasizing different aspects of the information when presenting it to users. Similarly, making validation code independent of the schema (3) allows redesign of the schema without having to re-implement the annotation validation tools.


### 2.3. HED terminology

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [[RFC2119](https://www.ietf.org/rfc/rfc2119.txt)].

This specification uses a list of terms and abbreviations whose meaning is clarified here. Note: We here hyphenate multi-word terms as they appear in HED strings themselves; in plain text usage they may not need to be hyphenated. Starred variables correspond to actual HED tags.


##### Agent*

A person or thing, living or virtual, that produces (or appears to participants to be ready and capable of producing) specified effects. Agents include the study participants from whom data is collected. Virtual agents may be human or other actors in virtual-reality or augmented-reality paradigms or on-screen in video or cartoon presentations (e.g., an actor interacting with the recorded participant in a social neuroscience experiment, or a dog or robot active in a live action or animated video).

##### Condition-variable*

An aspect of the experiment that is set or manipulated during the experiment to observe an effect or to manage bias. Condition variables are sometimes called independent variables.
