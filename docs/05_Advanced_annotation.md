# 5. Advanced tagging concepts

## 5.1. HED definitions

HED-3G introduces the *Definition* tag to facilitate tag reuse and to allow implementation of concepts such as **temporal scope**. The *Definition* tag allows researchers to create a name to represent a group of tags and then use the name in place of these tags when annotating data. These short-cuts make tagging easier and reduce the chance of errors. Often laboratories have a standard setup and event codes with particular meanings. Researchers can define names and reuse them  for multiple experiments. Another important role of definitions is to provide the structure for implementing temporal scope as introduced in **Section 3.3**.

A **HED definition** is a tag group that includes one *Definition* tag whose required child value names. The definition usually includes an optional tag-group specifying the actual definition information. Table 3.1 summarizes the syntax rules for definitions.

### **Table 5.1.** Syntax for *Definition*. Optional items are underlined.

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

**Example:** Define *PresentationRate* to annotate the rate of visual presentation of a stimulus.

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

## 5.2. Using definitions

When a definition name such as *PlayMovie* or *PresentationRate* is used in an annotation, the name is prefixed by *Def/* to indicate that the name represents a defined name. In other words, *Def/PlayMovie* is shorthand for *(Visual, Movie, Screen)*. Table 5.2 summarizes _Def/_ syntax rules.


### **Table 5.2.** Syntax for *Def/*.

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

During analysis, tools usually replace *Def/PlayMovie* with a fully expanded tag string. Tools must retain the association of the expanded tag string with the definition name for identification during searching and substitution. When a definition is expanded, the resulting tag string should include the definition name using the *Def-expand* tag. In other words, the tools should expand the definition as *(Def-expand/PlayMovie, Visual, Movie, Screen)*. The *Def-expand/PlayMovie* is inserted in the definition tag group as part of the expansion to keep the association with the original definition.

**Usually definitions do not contain tags from the *Event* subtree.** The standard practice is to use the elements of the *Event* subtree as top-level tags to designate the general category of an event. This practice makes it easier for search and analysis tools to filter events without extensive parsing. The annotator can use tags such as *Experimental-stimulus* (Long form: *Property/Task-property/Task-event-role/Experimental-stimulus*) to explain the role of a particular sensory presentation element in the experiment within the definition.

Definitions may appear anywhere in a HED event file or in auxiliary files associating metadata with HED tags such as JSON sidecars in BIDS datasets. Multiple definitions can be defined or used in the same HED string annotation, but definitions cannot be nested. Further, definitions must appear as top-level tag groups. Tools generally make a pass through the event information to extract the definitions prior to other processing. The validation checks made by the HED validator when assembling and processing definitions are summarized in **Appendix C**.

In addition to syntax checks, which occur in early processing passes, HED validators check that names are defined before they are used as definitions. Additional checks for temporal scope are discussed in **Section 3.3**.


## 5.3. Temporal scope

Events are often modeled as instantaneous occurrences that occur at single points in time (i.e., time-marked or point events). In reality, many events unfold over extended time periods. The interval between the initiation of an event and its completion is called the **temporal scope** of the event. Some events, such as the setup and initiation of the environmental controls for an experiment, may have a temporal scope that spans the entire data recording. Other events, such as the playing of a movie clip or a participant performing an action in response to a sensory presentation, may last for seconds or minutes. Temporal scope captures the effects of these extended events in a machine-actionable manner.


### 5.3.1. *Onset* and *Offset* tags 

HED events are assumed to be point events unless they are given an explicit temporal scope (i.e., they are “scoped” events). The most direct HED method of specifying scoped events uses *Onset* and *Offset* tags with definitions. Using this method, an event with temporal scope actually corresponds to two point events. The event is initiated by a *(Def/XXX, Onset)*. The end of the event’s temporal scope is marked either by a *(Def/XXX, Offset)* or by another *(Def/XXX, Onset)*. Table 5.3 summarizes *Onset* and *Offset* usage.


#### **Table 5.3.** *Onset* and *Offset*  syntax.

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

For example, the *PlayMovie* definition of the previous section just defines the playing of a movie clip on the screen. The *(tag-group)* might include tags identifying which clip is playing in this instance. This syntax allows one definition name to be used for the playing of many different clips. 

**Example:** An event sequence representing the playing of a Star Wars clip using *PlayMovie*.

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

The *PlayMovie* scoped event type can be reused to annotate the playing of other movie clips. However, scoped events with the same defined name (e.g., *PlayMovie*) cannot be nested. The temporal scope of a *PlayMovie* event ends with a *PlayMovie* offset or with the onset of another *PlayMovie* event. 

Because tools need to have the definitions in hand when fully expanding during validation and analysis, tools must gather applicable definitions before final processing. Library functions in Python, Matlab, and JavaScript are being developed to support gathering of definitions and the expansion as described in **Section 5**. 


### 5.3.2. *Duration* 

The *Duration* tag is an alternative method for specifying an event with temporal scope. The start of the temporal scope is the event in which the *Duration* tag appears. The end of the temporal scope is implicit and may not coincide with an actual event appearing in the recording. Instead, tools calculate when the scope ends in the data recording. *Duration* tags do not need a defined label. *Duration* may be grouped with tags representing the additional information associated with the temporal scope of that event. This grouping usually does not include tags from the *Event* rooted tree.

**Example:** Use *Duration* to represent the playing of a 2-second movie clip of Star Wars.

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

The *Duration* tag is convenient because its use does not require a *Definition*. The *Duration* tag has the same effect on event context as the onset/offset mechanism (as explained in **Section 3.4**.) However the ending of the temporal scope for events defined with *Duration* is not marked by an explicit event in the data recording. This has distinct disadvantages for analysis if the offset is expected to elicit a neural response, which is the case for most events involving visual or auditory presentations.


### 5.3.3. Temporal offsets with *Delay*

The *Delay* tag is grouped with a set of tags to indicate that the associated tag-group is actually an implicit event that occurs at a time offset from the current event. A typical use case is when the user response time to a stimulus is recorded as a delay time relative to the onset of the corresponding stimulus event. This strategy is convenient for some time-locked analyses. HED tools could be developed to support the expansion of delayed events into actual events in the event stream, provided delays were consistently provided as signed numerical values relative to the anchor onset.

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

Notice that the *Agent-action* tag from the *Event* subtree is included in the *Delay* tag-group. This allows tools to identify this tag-group as representing a distinct event. For BIDS datasets, such response delays would be in value columns of the `_events.tsv` event files. The HED annotation for the JSON sidecar corresponding to these files would contain a *#*. At HED expansion time, tools replace the *#* with the column value (2.83) corresponding to each event. 


## 5.4. The *Event-stream* tag

An event stream is a sequence of events in a data recording. The most obvious event stream is the sequence consisting of all of the events in the recording, but there are many other possible streams such as the stream consisting of all sensory events or the stream consisting of all participant response events. 

Event streams can be identified and tagged using the *Event-stream* tag, allowing annotators to more easily identify subsets of events and interrelationships of events within those event sequences. An event having the tag *Event-stream/XXX* is part of event stream XXX.  

**Example:** Tag a face event indicating that it is part of the *Face-stream* event stream. 

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

## 5.5. The *Event-context* tag

Event annotations generally focus on describing what happened at the instant an event was initiated. However, the details of the setting in which the event occurs also influence neural responses. For the *PlayMovie* example of the previous section, events that occur between the *Onset* and *Offset* pairs for *PlayMovie* should inherit the information that a particular movie is playing without requiring the user to explicitly enter those tags for every intervening event. This process should be deferred until analysis time because other events might be added to the event file after the initial annotation of the recording. For example, a user might run a tool to mark blink or other features as events prior to doing other analyses. HED uses the *Event-context* tag to accomplish the required context mapping.

Table 5.4 summarizes the syntax of the *Event-context* tag. In normal usage, **this tag is not used directly by annotators**.  Rather, tools insert the *Event-context* tag at analysis time to handle the implicit context created by enduring or scoped events. However, annotators may use the tag when an event has explicit context information that must be accounted for.

### **Table 5.4.** Syntax for HED *Event-context*.

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


## 5.6. Experimental design

Most experiments are conducted by varying certain aspects of the experiment and measuring the resulting responses while carefully controlling other aspects. The intention of the experiment is annotated using the HED *Condition-variable*, *Control-variable*, and *Indicator-variable* tags. 

The *Condition-variable* tag is used to mark the independent variables of the experiment -- those aspects of an experiment that are explicitly varied in order to observe an effect or to control bias. Contrasts, a term that appears in the neuroscience and statistical literature, are examples of experimental conditions, as are factors in experimental designs.

The *Indicator-variable* tag is used to mark quantities that are explicitly measured or calculated to evaluate the effect of varying the experimental conditions. Indicator variables often fall into the *Event/Data-feature* category. Sometimes the values of these data features are explicitly annotated as events. Researchers should provide a sufficiently detailed description of how to compute these data features so that they can be reproduced. 

The *Control-variable* tag represents an aspect of the experiment that is held constant throughout the experiment, often to remove variability.

Researchers should use *Condition-variable*, *Control-variable*, and *Indicator-variable* tags to capture the experiment intent and organization in as much detail as possible. Consistent and detailed description allows tools to extract the experiment design from the data in a machine-actionable form. Good tagging processes suggest creating definitions with understandable names to define these aspects of the dataset. This promotes easy searching and extraction for analyses such as regression or other modeling of the experimental design.

To illustrate the use of condition-variables to document experiment design, consider an experiment in which one of the conditions is the rate of presentation of images displayed on the screen. The experiment design compares responses under slow and fast image presentation rate conditions. To avoid unfortunate resonances due to a poor choice of rates, the “slow” and “fast” rate conditions each consist of three possible rates. Selection among the three eligible rates for the given condition is done randomly. 

In analysis, the researcher would typically combine all of the “slow presentation” trials into one group and all “fast presentation” trials into another group even though the exact task condition varies within the group varies according This type of grouping structure is very common in experiment design and can be captured by HED tags in a straightforward manner by defining condition variables for each group and using the *#* to capture variability within the group.

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

*Organizational* tags such as *Condition-variable* are often used in the tag-groups of temporally scoped events. The *Onset* of such an event represents the start of the *Condition-variable*. The corresponding *Offset* marks the end of the period during which this condition is in effect. This type of annotation makes it straightforward to extract the experimental design from the events.

**Example:** Annotation of a sensory presentation under the *SlowPresentation* condition.

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

During analysis, the *Def* tags will be replaced with the actual definition’s tag group with an included *Def-expand* tag giving the definition’s name. Note: expansion is done by tools at analysis time.

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

Properly annotated condition variables and response variables can allow researchers to understand the details of the experiment design and perform analyses such as ANOVA (ANalysis Of VAriance) or regression to extract the dependence of responses on the condition variables. The time-organization of an experiment can be annotated with the Organizational tags *Time-block* and *Task-trial* and used for visualizations of experimental layout.

A typical experiment usually consists of a sequence of subject task-related activities interspersed with rest periods and/or off-line activities such as filling in a survey. The *Time-block* tag is used to mark a contiguous portion of the data recording during which some aspect of the experiment conditions is fixed. *Time-block* tags can be used to represent temporal organization in a manner similar to the way *Condition-variable* tags are used to represent factors in an experiment design. 


## 5.7. Specialized annotation

A significant problem with schema design is term accretion. Each type of experiment will have specific terms or concepts that are important for the experiment’s purpose or design but are not widely applicable to other experiments. Schema designers might be tempted to add terms specific to familiar experiments or for annotators to extend the schema tree with terms specific to their experiments during annotation. 

The *Parameter* tag and its children *Parameter-label* and *Parameter-value* are general-purpose tags designed to fill the missing term gap. They can be used to tag important specific concepts in a way that can be used for automated tools without triggering problems of accretion. For example, consider the problem of how to annotate repetition lag between successive presentations of a particular face image. There are several ways to annotate, but annotating with *Parameter* is a good compromise between machine

**Example:** Annotate the number of times a face image has appeared and the interval since last time this face was shown using *Parameter-value*:

**Short form:**
```
(Parameter-label/Count-of-this-face, Parameter-value/2)
(Parameter-label/Face-count-since-this-face-last-shown, Parameter-value/15)
```

**Example:** Annotate the number of times a face image has appeared and the interval since last time this face was shown using more specific tags for the value *Parameter-value*:

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

Using more specific tags as in the second version allows downstream tools to treat the value as numeric integers, facilitating automated processing. The use of *Parameter* alerts downstream tools that this entity represents something that annotators regard as important to compute or record for analysis. Summary tools can extract all of the experimental parameters and their values, while statistical tools can look for dependencies on these variables. The parameter names are designed to be self-documenting. Parameters are often used for derived values such as response times that are used as indicator variables in the experiment. They are also sometimes used as part of control variable definitions.

