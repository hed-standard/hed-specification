# 5. Advanced annotation

## 5.1. Creating definitions

HED version 8.0.0 introduced the `Definition` tag to facilitate tag reuse and 
to allow implementation of concepts such as **temporal scope**. 
The `Definition` tag allows researchers to create a name to represent a group of tags and 
then use the name in place of these tags when annotating data. 
These short-cuts make tagging easier and reduce the chance of errors. 
Often laboratories have a standard setup and event codes with particular meanings.
Researchers can define names and reuse them for multiple experiments. 

Another important role of definitions is to provide the structure for 
implementing temporal scope as introduced in [**Chapter 5.3: Temporal Scope**](05_Advanced_annotation.md#53-temporal-scope).

A **HED definition** is a tag group that includes one `Definition` tag whose required 
child value is the definition's name.
The definition tag group also includes an internal tag-group 
specifying the definition's content. 
The following summarizes the syntax of HED definitions.

``````{admonition} Syntax summary for HED definitions.

**Short forms:** 
 ~ *(Definition/xxx, (definition-content))*
 ~ *(Definition/xxx/#, (definition-content))*
 
**Long forms:**  
 ~ *(Property/Organizational-property/<strong>Definition/xxx</strong>, (definition-content))*
 ~ *(Property/Organizational-property/<strong>Definition/xxx/#</strong>, (definition-content))*
 
````{admonition} Notes:
:class: tip
1. *xxx* is the name of the definition, and *(definition-content)* is a tag group
containing the tags representing the definition’s contents.
2. If the *xxx/#* form is used, then the *(definition-content)* MUST contain a single `#` 
representing a value to be substituted for when the definition is used.

````

``````

The following example defines the *PlayMovie* term. 

````{admonition} **Example:** *PlayMovie* defines the playing a movie on a computer screen.

**Short form:** <br/> 
> *(Definition/PlayMovie, (Visual-presentation, Movie, Computer-screen))* 

**Long form:** <br/>
> *(Property/Organization-property/<strong>Definition/PlayMovie</strong>,*  
> *(Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*  
> *Item/Object/Man-made-object/Media/Visualization/<strong>Movie</strong>,*  
> *Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/<strong>Computer-screen</strong>))*  

````

The next example gives a definition that uses a placeholder representing a presentation
rate, for example, to annotate events in which a presentation rate is varied
at random. Usually the specific value substituted for the `#` will come from 
one of the columns in the `events.tsv` file.

````{admonition} **Example:** Use definition with placeholder to annotate a variable presentation rate.

**Short form:**  
> *(Definition/PresentationRate/#,*  
> *(Visual-presentation, Experimental-stimulus, Temporal-rate/# Hz))*  

**Long form:**  
> *(Property/Organizational-property/<strong>Definition/PresentationRate/#</strong>,*  
> *(Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*  
> *Property/Task-property/Task-event-role/<strong>Experimental-stimulus</strong>,*  
> *Data-property/Data-value/Spatiotemporal-value/Rate-of-change/<strong>Temporal-rate/# Hz</strong>))*  

````


Definitions may only appear in dummy entries of JSON sidecars and as external dictionaries.
Definitions cannot be nested. 
Further, definitions must appear as top-level tag groups. 

The validation checks made by the HED validator when assembling and processing definitions 
are summarized in [**Appendix B: HED errors**](Appendix_B.md#b-hed-errors).
In addition to syntax checks, which occur in early processing passes,
HED validators check that the definition names have unique definitions. 
Additional checks for temporal scope are discussed in 
[Chapter 5.2: Using definitions](05_Advanced_annotation.md#52-using-definitions) and
[Chapter 5.3: Temporal scope](05_Advanced_annotation.md#53-temporal-scope).


## 5.2. Using definitions

This section describes how to use definitions to assist in annotation.

### 5.2.1. The *Def* tag

When a definition name such as `PlayMovie` or `PresentationRate` is used in an annotation, 
the name is prefixed by the `Def` tag to indicate that the name represents a defined name. 
In other words, `Def/PlayMovie` is shorthand for 
`(Visual-presentation, Movie, Computer-screen)`.

The following summarizes `Def` tag syntax rules.

``````{admonition} Syntax summary for the <code>Def</code> tag:
**Short forms:** 
 ~ *Def/xxx*
 ~ *Def/xxx/yyy*
 
**Long forms:**
 ~ *Property/Organizational-property/<strong>Def/xxx</strong>* 
 ~ *Property/Organizational-property/<strong>Def/xxx/yyy</strong>*

````{admonition} Notes:
:class: tip
1. *xxx* is the name of the definition.
2. *yyy* is the value that is substituted for the definition's placeholder if it has one.
2. If the *xxx/yyy* form is used, then the corresponding definition’s tag-group MUST contain a single `#` 
representing a value to be substituted for when the definition is used.
````
``````

The following example shows how `Def` is used in annotation.

````{admonition} **Example:** Use *PresentationRate* to annotate a presentation rate of 1.5 Hz.

**Short form:**  
 ~ *Def/PresentationRate/1.5 Hz*

**Long form:**  
 ~ *Property/Organizational-property/<strong>Def/PresentationRate/1.5 Hz</strong>*

````

### 5.2.2. The *Def-expand* tag

The `Def-expand` tag provides an alternative to `Def` tag in annotations.
Unlike the `Def` tag, a `Def-expand` tag must be in a tag group that includes 
an inner tag group with the definition's contents.
If the definition includes a placeholder, that must be replaced with these
contents by the appropriate value.

The following summarizes `Def-expand` tag syntax rules.

``````{admonition} Syntax summary for the <code>Def-expand</code> tag:
**Short forms:** 
 ~ *(Def-expand/xxx, (definition-contents))*
 ~ *(Def-expand/xxx/yyy, (definition-contents))*
 
**Long forms:**
 ~ *(Property/Organizational-property/<strong>Def-expand/xxx</strong>, (definition-contents))* 
 ~ *(Property/Organizational-property/<strong>Def-expand/xxx/yyy</strong>, (definition-contents))*

````{admonition} Notes:
:class: tip
1. *xxx* is the name of the definition.
2. *yyy* is the replacement value for the `#` placeholder.
3. If the *xxx/yyy* form is used in the definition, then the replacement value (*yyy* above)
must replace placeholders both in the definition's name and its contents. 
````
``````

The following example shows how `Def-expand` is used in an annotation.

````{admonition} **Example:** Use *PresentationRate* to annotate a presentation rate of 1.5 Hz.

**Short form:**  
> *(Def-expand/PresentationRate/1.5 Hz,*  
> *(Visual-presentation, Experimental-stimulus, Temporal-rate/1.5 Hz))*  

**Long form:**  
> *(Property/Organizational-property/<strong>Def-expand/PresentationRate/1.5 Hz</strong>,*  
> *(Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*  
> *Property/Task-property/Task-event-role/<strong>Experimental-stimulus</strong>,*  
> *Data-property/Data-value/Spatiotemporal-value/Rate-of-change/<strong>Temporal-rate/1.5 Hz</strong>))*  

````
During analysis, tools may replace `Def/PlayMovie` with a fully expanded tag string. 
Tools sometimes need to retain the association of the expanded tag string with the definition
name for identification during searching and substitution. 



## 5.3. Temporal scope

Events are often modeled as instantaneous occurrences that occur at single points in time 
(i.e., time-marked or point events). 
In reality, many events unfold over extended time periods. 
The interval between the initiation of an event and its completion is called
the **temporal scope** of the event. 
HED events are assumed to be point events unless they are given an explicit temporal scope 
(i.e., they are “scoped” events). 

Some events, such as the setup and initiation of the environmental controls 
for an experiment, may have a temporal scope that spans the entire data recording. 
Other events, such as the playing of a movie clip or a participant performing an action in 
response to a sensory presentation, may last for seconds or minutes. 
Temporal scope captures the effects of these extended events in a machine-actionable manner.
HED has two distinct mechanisms for expressing temporal scope: `Onset`/`Offset` and `Duration`/`Delay`.
Tools can transform between one representation and the other.
However, transform from the `Duration`/`Delay` representation to the `Onset`/`Offset`
representation may require the addition of additional rows (time markers) in the events file.

The mechanisms are summarized in the following table and discussed in more detail 
in the following sections. 



| Tag  | Meaning  | Usage  |
| ---- | ----------- |  ------- |
| `Onset` |  Marks start of event |  Used with a `Def` tag or `Def-exand` group anchor. <br/>The corresponding end is marked using<br/> `Onset` or `Offset` with same anchor. |  
| `Offset` | Marks end of event | Used with a `Def` tag or `Def-exand` group anchor. <br/> Must be preceded by an `Onset` <br/> anchored by the same definition. |
| `Inset`   | Marks event intermediate pt | New in standard schema 8.2.0. <br/> Used with a `Def` tag or `Def-exand` group anchor.<br/> Must be within the event markers<br/>for an `Onset` marked-event with the same anchor. | 
| `Duration ` | Marks end of an event.  | Doesn't use a definition anchor.<br/>Starts at the current event marker unless `Delay`.<br/>If `Delay` included, start = current marker + delay. <br/>The offset = start + duration. |
| `Delay` | Marks delayed onset. | Doesn't use a definition anchor.<br/>If no `Duration`, treated as point event.<br/>Commonly for delayed response times. |
| `Event-context` |  Context of ongoing events. | Should only be inserted by tools.<br/>Each unique event marker can have <br/>only one `Event-context` group.|

All of these tags must appear in a `topLevelTagGroup`, which implies that they can't be nested.
`Delay` and `Duration` will not be fully supported until HED standard schema version 8.2.0.

The `Inset` tag will also not be included until HED standard schema version 8.2.0,
but is listed here for completeness.  

### 5.3.1. Using `Onset` and `Offset`

The most direct HED method of specifying scoped events combines 
`Onset` and `Offset` tags with defined names. 
Using this method, an event with temporal scope actually corresponds to two point events. 

The initiation event is tagged by a `(Def/xxx, Onset)` where `xxx` is a defined name.
The end of the event’s temporal scope is marked either by a `(Def/xxx, Offset)` or by 
another `(Def/xxx, Onset)`. The `Def/xxx` is said to **anchor** the `Onset` 
(and similarly for `Offset`). 
By anchor, we mean that tools use the anchor to determine
where each event of temporal extent begins and ends. 
A `Def-expand` tag group can also anchor the `Onset` and `Offset` groups.

The `Onset` tag group may contain an additional internal tag group in addition to the
anchor `Def` tag. This internal tag group usually contains annotations specific 
to this instance of the event. As with all HED tags and groups, order does not matter.

Event initiations identified by definitions with placeholders are handled similarly.
Suppose the initiation event is tagged by a `(Def/xxx/yyy, Onset)` where `xxx`
is a defined name and `yyy` is the value substituted for the `#` placeholder. 
The end of this event's temporal scope is marked either by `(Def/xxx/yyy, Offset)` or by 
another `(Def/xxx/yyy, Onset)`. 
An intervening `(Def/xxx/zzz, Onset)`, where `yyy` and `zzz`
are different, is treated as a completely distinct temporal event.

The following table summarizes `Onset` and `Offset` usage. 
**Note**: A `Def-expand/xxx` tag group can be used
interchangeably with the `Def/xxx`. 


``````{admonition} **Syntax summary for <code>Onset</code> and <code>Offset</code>.**
**Short forms:**
 ~ *(Def/xxx, Onset, (tag-group))*
 ~ *(Def/xxx/yyy, Onset, (tag-group))*
 ~ *(Def/xxx, Offset)*
 ~ *(Def/xxx/yyy, Offset)*
 
**Long forms:**  
 ~ *(Property/Organizational-property/<strong>Def/xxx</strong>,*  
   *Property/Data-property/Data-marker/Temporal-marker/<strong>Onset</strong>, <strong>(tag-group)</strong>)*
 ~ *(Property/Organizational-property/<strong>Def/xxx/#</strong>,*  
   *Property/Data-property/Data-marker/Temporal-marker/<strong>Onset</strong>, <strong>(tag-group)</strong>)*
 ~ *(Property/Organizational-property/<strong>Def/xxx</strong>,*
   *Property/Data-property/Data-marker/Temporal-marker/<strong>Offset</strong>)*
 ~ *(Property/Organizational-property/<strong>Def/xxx/#</strong>,*
   *Property/Data-property/Data-marker/Temporal-marker/<strong>Offset</strong>)*

````{admonition} Notes:
:class: tip
1. *xxx* is the name of the definition anchoring the scoped event.
2. *yyy* is the value substituted for a definition's placeholder if it has one.
3. The *(tag-group)*, which is optional, contains tags specific to that temporal event.
This tag group is not the tag group specifying the contents of the definition.
4. The additional <em>tag-group</em> is only in effect for that particular scoped event
 and not for all events anchored by *Def/xxx*.
5. If the *Def/xxx/#* form is used, the `#` must be replaced by an actual value.
6. The entire definition identifier *Def/xxx/#*, including the value substituted for the `#`,
is used as the anchor for temporal scope.
````
``````

For example, the `PlayMovie` definition of the previous section just defines the playing of a
movie clip on the screen. 
The *(tag-group)* might include tags identifying which clip is playing in this instance. 
This syntax allows one definition name to be used to represent the
playing of different clips. 

````{admonition} **Example:** The playing of a Star Wars clip using *PlayMovie*.

**Short form:**  
> [event 1]  
> *Sensory-event, (Def/PlayMovie, Onset, (Label/StarWars, (Media-clip, ID/3284)))*  
 
>         .... [The Star Wars movie clip is playing] ....
  
> [event n]  
> *Sensory-event, (Def/PlayMovie, Offset)*

**Long form:**  
> [event 1]  
> *Event/<strong>Sensory-event</strong>,*  
> *(Property/Organizational-property/<strong>Def/PlayMovie</strong>,*  
> *Data-property/Data-marker/Temporal-marker/<strong>Onset</strong>,*  
> *(Property/Informational-property/<strong>Label/StarWars</strong>,*  
> *(Item/Object/Man-made-object/Media/<strong>Media-clip</strong>,*  
> *Property/Informational-property/<strong>ID/3284</strong>)))*  
            
>         .... [The Star Wars movie clip is playing] ....

> [event n]  
> *Event/<strong>Sensory-event</strong>,*  
> *(Property/Organizational-property/<strong>Def/PlayMovie</strong>,*  
> *Data-property/Data-marker/Temporal-marker/<strong>Offset</strong>)*  
````

The `PlayMovie` scoped event type can be reused to annotate the playing of other movie clips.
However, scoped events with the same defined name (e.g., `PlayMovie`) cannot be nested. 
The temporal scope of a `PlayMovie` event ends with a `PlayMovie` offset or with the 
onset of another `PlayMovie` event. 

In the previous example, the `Def/PlayMovie` "anchors" the temporal scope,
and the appearance of another `Def/PlayMovie` indicates the previous movie has ceased.
The `Label` tag identifies the particular movie but does not affect the `Onset`/`Offset`
determination. 

If you want to have interleaved movies playing, use definitions with 
placeholder values as shown in the next example. The example assumes a definition 
`Definition/MyPlayMovie/#` exists.

````{admonition} **Example:** The interleaved playing of Star Wars and Forrest Gump.

**Short form:**  
> [event 1]  
> *Sensory-event, (Def/MyPlayMovie/StarWars, Onset, (Media-clip, ID/3284))*  
 
>         .... [The Star Wars movie clip is playing] ....
  
> [event n1]
> *Sensory-event, (Def/MyPlayMovie/ForrestGump, Onset, (Media-clip, ID/5291))*  
 
>         .... [Both Star Wars and Forrest Gump are playing] ....

> [event n2]    
> *Sensory-event, (Def/MyPlayMovie/StarWars, Offset)*

>         .... [Just Forrest Gump is playing] ....

> [event n3]    
> *Sensory-event, (Def/MyPlayMovie/ForrestGump, Offset)*   
````

Because tools need to have the definitions in hand when fully expanding during validation 
and analysis, tools must gather applicable definitions before final processing. 
Library functions in Python, Matlab, and JavaScript are available to support 
gathering of definitions and the expansion.
These definitions may be given in JSON sidecars or provided externally.

### 5.3.2. Using `Inset`

The `Inset` tag group marks an intermediate point in an event of temporal extent
defined by `Onset` and `Offset`.
Like the `Offset`, the `Inset` tag is anchored by a `Def` tag or `Def-expand` tag group
that is the anchor of its enclosing `Onset`.

The `Inset` tag group may contain an additional internal tag group in addition to the
anchor `Def` tag. This internal tag group usually contains annotations specific 
to this instance of the event. As with all HED tags and groups, order does not matter.

The following table summarizes `Inset` usage. 
**Note**: A `Def-expand/xxx` tag group can be used
interchangeably with the `Def/xxx`. 


``````{admonition} **Syntax summary for <code>Inset</code>.**
**Short forms:**
 ~ *(Def/xxx, Inset, (tag-group))*
 ~ *(Def/xxx/yyy, Inset, (tag-group))*
 
**Long forms:**  
 ~ *(Property/Organizational-property/<strong>Def/xxx</strong>,*  
   *Property/Data-property/Data-marker/Temporal-marker/<strong>Inset</strong>, <strong>(tag-group)</strong>)*
 ~ *(Property/Organizational-property/<strong>Def/xxx/#</strong>,*  
   *Property/Data-property/Data-marker/Temporal-marker/<strong>Inset</strong>, <strong>(tag-group)</strong>)*

````{admonition} Notes:
:class: tip
1. *xxx* is the name of the definition anchoring the scoped event.
2. *yyy* is the value substituted for a definition's placeholder if it has one.
3. The *(tag-group)*, which is optional, contains information specific to that intermediate.
point in the ongoing event. This tag group is not the tag group specifying the contents of the definition..
4. The additional <em>tag-group</em> is only in effect at that particular point.
5. If the *Def/xxx/#* form is used, the `#` must be replaced by an actual value that is
the same as the value used for its `Onset`.
````
``````


### 5.3.3. Using `Duration`

The `Duration` tag is an alternative method for specifying an event with temporal scope. 
The start of the temporal scope is the event in which the `Duration` tag appears. 
The end of the temporal scope is implicit and may not coincide with an actual event 
appearing in the recording. 
Instead, tools calculate when the scope ends (i.e., the event offset) by
adding the value of the duration to the onset of the event marker associated
with that `Duration` tag. As with all HED tags and groups, order does not matter.

The following table summaries the syntax for `Duration`.

``````{admonition} **Syntax summary for <code>Duration</code>.**
**Short forms:**
 ~ *(Duration/xxx, (tag-group))*
 ~ *(Duration/xxx, Delay/yyy, (tag-group))*
 
**Long forms:**  
 ~ *(Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Duration/xxx</strong>,*  
   *(tag-group)*
 ~ *(Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Duration/xxx</strong>,*
 *(Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Delay/yyy</strong>,*    
   *(tag-group))*

````{admonition} Notes:
:class: tip
1. *xxx* is a time value for the duration.
2. *yyy* is a time value for the delay if given.
2. The *(tag-group)* contains the additional tags specific to the temporal event whose duration is specified.

````
``````

`Duration` tags do not use a definition anchor. 
`Duration` should be grouped with tags representing additional information associated 
with the temporal scope of that event. 

The `Duration` tag must appear in a top level tag
group that may include an additional `Delay` tag.
If the `Duration` appears with `Delay`, the end of the temporal event is the onset of the current event plus the delay value plus the duration value.

Several events with temporal-scopes defined by `Duration` tag groups 
may appear in the annotations associated with the same event marker.

````{admonition} **Example:** Use the <code>Duration</code> tag to annotate the playing of a 2-s movie clip of Star Wars.

**Short form:**    
> *(Duration/2 s, (Sensory-event, Visual-presentation, (Movie, Label/StarWars)))*  

**Long form:**    
> *(Property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Duration/2 s</strong>,*  
> *(Event/<strong>Sensory-event</strong>,*  
> *Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*  
> *(Item/Object/Man-made-object/Media/Visualization/<strong>Movie</strong>,*  
> *Property/Informational-property/<strong>Label/StarWars</strong>)))* 

````

The `Duration` tag has the same effect on event context as the 
`Onset`/`Offset` mechanism explained in 
[**5.5. Event contexts**](./05_Advanced_annotation.md#55-event-contexts)

The `Duration` tag is convenient because its use does not require a definition. 
However, the ending time point of events whose temporal scope is defined 
with `Duration` is not marked by an explicit event in the data recording. 
This has distinct disadvantages for analysis if the offset is expected to elicit a
neural response, which is the case for many events involving visual or auditory presentations.
The use of the `Duration` tag will not be fully supported by validators until HED
standard schema version 8.2.0. 

### 5.3.4. Using `Delay`

The `Delay` tag is grouped with an inner tag group to indicate that the associated tag-group is
actually an implicit event that occurs at a time offset from the current event. 
`Delay` tags do not use a definition anchor. 

If the tag group containing the `Delay` also contains a `Duration` tag,
then the tag group represents an event with temporal extent.
Otherwise, it is considered a point event. 
As with all HED tags and groups, order does not matter.

The following table summarizes the syntax for `Delay`.

``````{admonition} **Syntax summary for <code>Delay</code>.**
**Short forms:**
 ~ *(Delay/xxx, (tag-group))*
 ~ *(Delay/xxx, Duration/yyy, (tag-group))*
 
**Long forms:**  
 ~ *(Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Delay/xxx</strong>,*  
   *(tag-group)*
 ~ *(Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Duration/xxx</strong>,*
 *(Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Delay/yyy</strong>,*    
   *(tag-group))*

````{admonition} Notes:
:class: tip
1. *xxx* is a time value for the duration.
2. *yyy* is a time value for the delay if given.
2. The *(tag-group)* contains the additional tags specific to the temporal event whose duration is specified.

````
``````


A typical use case for `Delay` is when a secondary stimulus appears offset from
the first. A typical use case for `Delay` combined with `Duration` is the encoding
of a participant response, where the reaction time is measured relative to
a secondary stimulus (such as a 'go').



In the following example, a trial consists of the presentation of a cross in the 
center of the screen. The participant responds with a button press upon seeing the cross. 
The response time of the button push is recorded relative to the stimulus presentation 
as part of the stimulus event.

````{admonition} **Example:** Use the delay mechanism for a participant response.

**Short form:**  
> *(Sensory-event, (Experimental-stimulus, Visual-presentation, Cross))*  
> *(Delay/2.83 ms, (Agent-action, Participant-response, (Press, Mouse-button)))*  

**Long form:**    
> *(Event/<strong>Sensory-event</strong>,*  
> *Property/Task-property/Task-event-role/<strong>Experimental-stimulus</strong>,*  
> *Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*  
> *(Item/Object/Geometric-object/2D-shape/<strong>Cross</strong>)),*   
> (*Property/Data-property/Data-value/Spatiotemporal-value/Temporal-value/<strong>Delay/2.83 ms</strong>,* 
> *(Event/<strong>Agent-action</strong>,*   
> *(Property/Task-property/Task-event-role/<strong>Participant-response</strong>,*  
> *(Action/Move/Move-body-part/Move-upper-extremity/<strong>Press</strong>/,*  
> *Item/Object/Man-made-object/Device/IO-device/Input-device/Computer-mouse/<strong>Mouse-button</strong>))),*  

````

Notice that the `Agent-action` tag from the `Event` subtree is 
included in the `Delay` tag-group.
This allows tools to identify this tag group as a distinct event. 
For BIDS datasets, such response delays would be recorded in a column of the `events.tsv` 
event files. The HED annotation for the JSON sidecar corresponding to these files would 
contain a `#`. At HED expansion time, tools replace the `#` with the column value (2.83)
corresponding to each event. 

The `Delay` tag can also be used in the same top level tag group as the `Duration` tag to
define an event with temporal extent. 
HED tools are being developed to support the expansion of delayed events to have their
own event markers without the delay tag.
However, use of the `Delay` tag will not be fully supported by validators until HED
standard schema version 8.2.0.

## 5.4. Event streams

An event stream is a sequence of events in a data recording. 
The most obvious event stream is the sequence consisting of all the events in the recording,
but there are many other possible streams such as the stream consisting o
f all sensory events or the stream consisting of all participant response events. 

Event streams can be identified and tagged using the `Event-stream` tag, allowing annotators
to more easily identify subsets of events and interrelationships of events within those event
sequences. 

An event having the tag `Event-stream/xxx` indicates that event or marker is part of event stream `xxx`.  

````{admonition} **Example:** Tag a face event as part of the *Face-stream* event stream.

**Short form:**  
> *Sensory-event, Event-stream/Face-stream, Visual-presentation, (Image, Face)*

**Long form:**   
> *Event/<strong>Sensory-event</strong>,*  
> *Property/Organizational-property/<strong>Event-stream/Face-stream</strong>,*  
> *Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*    
> *(Item/Object/Man-made-object/Media/Visualization/<strong>Image</strong>,*  
> *Item/Biological-item/Anatomical-item/Body-part/Head/<strong>Face</strong>)*  

````

Using a tag to identify an event stream makes it easier for downstream tools to compute
relationships among subsets of events.

**Note:** Event streams are still under development.

## 5.5. Event contexts

Event annotations generally focus on describing what happened at the instant an event was
initiated. However, the details of the setting in which the event occurs also influence neural
responses. For the `PlayMovie` example of the previous section, 
events that occur between the `Onset` and `Offset` pairs for `PlayMovie` should
inherit the information that a particular movie is playing without requiring 
the user to explicitly enter those tags for every intervening event.

The process of event context mapping should be deferred until analysis time because other 
events might be added to the event file after the initial annotation of the recording. 
For example, a user might run a tool to mark blink or other features as events prior 
to doing other analyses. 
HED uses the `Event-context` tag to accomplish the required context mapping.


In normal usage, **the `Event-context` tag is not used directly by annotators**.
Rather, tools insert the `Event-context` tag at analysis time to
handle the implicit context created by enduring or scoped events. 
However, annotators may use the tag when an event has explicit context information 
that must be accounted for. 
Tools are available to insert the appropriate `Event-context` at analysis time.
The `Event-context` has the `unique` attribute, 
implying that only one `Event-context` tag group may appear in the assembled
HED annotation corresponding to each time-marker value.

``````{admonition} **Syntax summary for *Event-context*.**

**Short form:**
 ~ *(Event-context, other-tag-groups)*  
 
**Long form:**
 ~ *(Property/Organizational-property/<strong>Event-context</strong>, other-tag-groups)*
 
````{admonition} Notes:
:class: tip
1. The `Event-context` may only appear in a top-level tag group of an assembled HED string.
2. An event can have at most one `Event-context` tag group in its assembled HED annotation.
3. HED-compliant analysis tools should insert the annotations describing each temporally 
scoped event into the `Event-context` tag group of the events within its 
temporal scope during final assembly before analysis of the event.
4. Each of these internal annotations should be in a group, indicating that they represent a distinct event process.
````
``````

## 5.6. Experimental design

Most experiments are conducted by varying certain aspects of the experiment and measuring the
resulting responses while carefully controlling other aspects.
The intention of the experiment is annotated using the HED `Condition-variable`, 
`Control-variable`, and `Indicator-variable` tags. 

The `Condition-variable` tag is used to mark the independent variables of the experiment
-- those aspects of an experiment that are explicitly varied in order to observe an effect
or to control bias. 
Contrasts, a term that appears in the neuroscience and statistical literature, 
are examples of experimental conditions as are factors in experimental designs.

The `Indicator-variable` tag is used to mark quantities that are explicitly measured or
calculated to evaluate the effect of varying the experimental conditions. 
Indicator variables often fall into the `Event/Data-feature` category. 
Sometimes the values of these data features are explicitly annotated as events. 
Researchers should provide a sufficiently detailed
description of how to compute these data features so that they can be reproduced. 

The `Control-variable` tag represents an aspect of the experiment that is held constant
throughout the experiment, often to remove variability.

Researchers should use `Condition-variable`, `Control-variable`, 
and `Indicator-variable` tags to capture the experiment intent and 
organization in as much detail as possible. 
Consistent and detailed description allows tools to extract the experiment design 
from the data in a machine-actionable form. 
Good tagging processes suggest creating definitions with understandable
names to define these aspects of the dataset. 
This promotes easy searching and extraction for
analyses such as regression or other modeling of the experimental design.

To illustrate the use of condition-variables to document experiment design, 
consider an experiment in which one of the conditions is the rate of 
presentation of images displayed on the screen. 
The experiment design compares responses under slow and fast image presentation rate conditions. 
To avoid unfortunate resonances due to a poor choice of rates, the “slow” and “fast”
rate conditions each consist of three possible rates. Selection among the three eligible rates
for the given condition is done randomly. 

In analysis, the researcher would typically combine the “slow presentation” trials into
one group and the “fast presentation” trials into another group even though the exact task
condition varies within the group varies according This type of grouping structure is very 
common in experiment design and can be captured by HED tags in a straightforward manner by
defining condition variables for each group and using the `#` to capture variability within 
the group.

````{admonition} **Example:** Condition variables for slow and fast visual presentation rates.

**Short form:**  
> *(Definition/SlowPresentation/#,*   
> *(Condition-variable/Presentation, Visual-presentation, Computer-screen, Temporal-rate/#))*  
>  
> *(Definition/FastPresentation/#,*  
> *(Condition-variable/Presentation, Visual-presentation, Computer-screen, Temporal-rate/#))*          

**Long form:**  
> *(Property/Informational-property/<strong>Definition/SlowPresentation/#</strong>,*  
> *(Property/Organizational-property/<strong>Condition-variable/Presentation</strong>,*  
> *Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*  
> *Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/<strong>Computer-screen</strong>,*   
> *Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/<strong>Temporal-rate/#</strong>))*  
>  
> *(Property/Informational-property/<strong>Definition/FastPresentation/#</strong>,*  
> *(Property/Organizational-property/<strong>Condition-variable/Presentation</strong>,*  
> *Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*   
> *Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/<strong>Computer-screen</strong>,*  
> *Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/<strong>Temporal-rate/#</strong>))*  

````

`Organizational-property` tags such as `Condition-variable` are often 
used in the tag-groups of temporally scoped events. 
The `Onset` of such an event represents the start of the`Condition-variable`. 
The corresponding `Offset` marks the end of the period during which this condition is in effect. 
This type of annotation makes it straightforward to extract
the experimental design from the events.

````{admonition} **Example:** Annotation using *SlowPresentation* condition.

**Short form:**  
> *Sensory-event, (Def/SlowPresentation/1 Hz, Onset)*  

**Long form:**  
> *Event/<strong>Sensory-event</strong>,*   
> *(Property/Organizational-property/<strong>Def/SlowPresentation/1 Hz</strong>,*  
> *Property/Data-property/Data-marker/Temporal-marker/<strong>Onset</strong>)*  
````

During analysis, the `Def` tags may be replaced with the actual definition’s tag group 
with an included `Def-expand` tag giving the definition’s name. 
Note: expansion is done by tools at analysis time.

````{admonition} **Example:** Expanded form of the previous example.

**Short form with expansion:**  
> *Sensory-event,*  
> *((Def-expand/SlowPresentation, Condition-variable/Presentation,*  
> *Visual-presentation, Computer-screen, Temporal-rate/1 Hz), Onset)*  

**Long form with expansion:**  
Event/<strong>Sensory-event</strong>,*  
> *((Property/Organizational/<strong>Def-expand/SlowPresentation</strong>,*  
> *Property/Organizational/<strong>Condition-variable/Presentation</strong>,*  
> *Property/Sensory-property/Sensory-presentation/<strong>Visual-presentation</strong>,*  
> *Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/<strong>Computer-screen</strong>,*  
> *Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/<strong>Temporal-rate/1 Hz</strong>),*  
> *Property/Data-property/Data-marker/Temporal-marker/<strong>Onset</strong>)*  
````

Properly annotated condition variables and response variables can allow researchers to 
understand the details of the experiment design and perform analyses such as 
ANOVA (ANalysis Of VAriance) or regression to extract the dependence of responses on the
condition variables. 
The time-organization of an experiment can be annotated with the
Organizational tags `Time-block` and `Task-trial` and used for 
visualizations of experimental layout.

A typical experiment usually consists of a sequence of subject task-related activities
interspersed with rest periods and/or off-line activities such as filling in a survey.
The `Time-block` tag is used to mark a contiguous portion of the data recording during 
which some aspect of the experiment conditions is fixed. 
`Time-block` tags can be used to represent temporal organization 
in a manner similar to the way `Condition-variable` 
tags are used to represent factors in an experiment design. 

## 5.7. Specialized annotation


### 5.7.1. Parameter tags

The `Parameter` tag and its children `Parameter-label` and `Parameter-value` 
are general-purpose tags designed to fill the missing term gap. 
They can be used to tag important specific concepts
in a way that can be used for automated tools without triggering problems of accretion. 
For example, consider the problem of how to annotate repetition lag between successive
presentations of a particular face image. 
There are several ways to annotate, but annotating with `Parameter` is a good compromise between clarity and machine-actionability.

````{admonition} **Example:** Annotate face repetition and interval using *Parameter-value*.

**Short form:**  
> *(Parameter-label/Count-of-this-face, Parameter-value/2)*  
> *(Parameter-label/Face-count-since-this-face-last-shown, Parameter-value/15)*  
````

Annotate the number of times a face image has appeared and the interval since last time this 
face was shown using more specific tags for the value `Parameter-value`:

````{admonition} **Example:** Annotate the number of times a face image has appeared.

**Short form:**  
> *(Parameter-label/Count-of-this-face, Item-count/2),*  
> *(Parameter-label/Face-count-since-this-face-last-shown,Item-count-interval/15),*  

**Long form:**  
> *(Property/Informational-property/Parameter/<strong>Parameter-label/Count-of-this-face</strong>,*  
> *Property/Data-property/Data-value/Quantitative-value/<strong>Item-count/2</strong>),*  
> *(Property/Informational-property/Parameter/<strong>Parameter-label/Face-count-since-this-face-last-shown</strong>*  
> *Property/Data-property/Data-value/Quantitative-value/<strong>Item-count-interval/15</strong>)*  

````

Using more specific tags as in the second version allows downstream tools to treat the value
as numeric integers, facilitating automated processing. The use of *Parameter* alerts 
downstream tools that this entity represents something that annotators regard as important to
compute or record for analysis. Summary tools can extract the experimental parameters 
and their values, while statistical tools can look for dependencies on these variables. The
parameter names are designed to be self-documenting. Parameters are often used for derived 
values such as response times that are used as indicator variables in the experiment. 
They are also sometimes used as part of control variable definitions.

**Note:** Parameters and related annotations are still under development.