## Proposed modifications for HED schema

This is a record of proposed changes/corrections to the HED schema for future release. As suggestions reach consensus they will be moved to this document. 


### Changes included in version 8.1.0

<hr/>

#### Add Body between Anatomical-item and Body-part
Then we can annotate right hand as `(Hand, (Right-side-of, Body))`.  

Should the recommended way to annotate right hand be:
(Hand, (Right-side-of, Body))  
(Hand, (Right-side-of, Human-agent))  
(Hand, (Right-side-of, (Human-agent, Torso)))  

**Response**:  Added `Item/Object/Anatomical-item/Body` at the same level as `Body-part` instead of moving `Body-part` under `Body` because `Body-part` is not a `Body` so that would violate the "is-a".

<hr/>


#### Add numericClass attribute (* indicates should consider unit class too)  
- `Property/Agent-property/Agent-trait/Age/#`  
- `Property/Data-property/Data-resolution/Printer-resolution/#`  
- `Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Sampling-rate/#`  
- `Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Refresh-rate/#`  
- `Property/Data-property/Data-value/Spatiotemporal-value/Spatial-value/Angle/#`  

**Response**: Added to version 8.1.0.


<hr/>

#### Addition of a conversionFactor

Proposed (@MichaelJachan) add schema attribute `conversionFactor` which takes a value
(i.e. does not have `boolProperty`). This attribute is associated with unit classes 
that are not SIUnits and gives the multiplicative conversion factor between the
specified units and the default units.  (Suggest adding to version 8.1. @VisLab).

**Response**: Added in version 8.10.

<hr/>

#### unitClasses and Units
- Add *euro* as a currency unit.

**Response**: Added but did not provide conversion factor to dollars.

<hr/>

#### Weights and volumes

- Add `weightUnits` and reorganize `volumeUnits`.  
- Deal with grams  

**Response**: Added `weightUnits` and simplified `volumeUnits` but did not resolve the difference between mass and weight.

<hr/>

#### Typos/corrections
This section lists typos or other errors that should be fixed.  

- Correct the word between in `**** Fraction <nowiki>[A numerical value betwee 0 and 1.]</nowiki>`  
- Rename `labelClass` to `nameClass` in `Property/Informational-property/Parameter/Parameter-label/#`  
- Rename `labelClass` to `nameClass` in `Property/Sensory-property/Sensory-attribute/auditory-attribute/Timbre/#`  
- The description of `topLevelTagGroup` schema attribute to mention that only one tag with the `topLevelTagGroup` attribute can appear in the same tag group.

**Response**: These have been fixed in 8.1.0.

<hr/>

#### Suggested additions
This section suggests listed additions to the HED tags.

- Add tag `Data-property/Data-marker/Data-break-marker`.

**Response**:  Added `Data-property/Data-marker/Data-break-marker`.

- Add `Distracted` to `Agent-emotional-state` since some experiments are designed with
distractions and surveys may assess the participant's degree of distraction.
(source @monique2208).
 
**Response**: Added to `Agent-cognitive-state` rather than `Agent-emotional-state` as
`Property/Agent-property/Agent-cognitive-state/Distracted`.

- Add Arrow to 2D-shape since arrow is a common 2D-shape used in experiments
(source @monique2208).
 
**Response**: Added `Item\Object\Man-made-object\Geometric-object\2D-shape\Arrow`.

- Need a way to tag that the participant is finished --- like an OK or Done
(Source @monique2208).

**Response**:  Added `Property/Task-property/Task-action-type/Done-indication` and `Property/Task-property/Task-action-type/Ready-indication`.

- Add `Sound-volume/#` to allow specification of a numerical value. Loudness can be
grouped with qualitative attributes such as `High` (@ Scott Makeig).

**Response**: Added `Property/Sensory-property/Sensory-attribute/Auditory-attribute/Sound-volume`. 

----------------------------------------------------------------------------------------

### Proposed changes deferred for later versions

<hr/>

#### Add Action-imperative

Need an `Action-imperative` tag to capture that a stimulus directs a specific action (source @smakeig).

**Response**: This is an important update, but we need to defer putting it in until a later
version for the following reasons.  

- We must work out how this tag relates to the existing `Intended-effect`. 
- The tag will clearly need to be part of a parenthesized group and not standing on its own in
an annotation. We need to finish working out the rules for parentheses and how groups are to
be used in searching before putting this in. 
- The issue this tag would address is part of the larger problem of how to best incorporate
task and event relationships into HED. We need to have a clearer handle on how to best address
this.

<hr/>

#### Schema attributes
- *takesValue* appears to now be redundant, as it is only used with #, which is assumed to take a value.  
- Do we need a *topLevel* attribute?  

**Response**: Need to keep these for backward compatibility. May need in the future.

<hr/>

#### Add additional data types

Consider adding other times of numerical features such as `Absmax`, `First-derivative-max`  (Source @smakeig).

**Response**: We're going to have to add many of these.
Let's defer until we have a better handle on the needs of the derivatives requirements.


#### Add value class --- not sure what class this should be needs discussion (See issue #324)

- `Item/Object/Man-made-object/Device/IO-device/Input-device/Keyboard/Keyboard-key/#`  
- `Item/Object/Man-made-object/Device/IO-device/Input-device/Keypad/Keypad-key/#`  
- `Property/Informational-property/Metadata/Pathname/#`  
- `Property/Informational-property/Metadata/CogAtlas/#` (What are these?)  

**Response**:  Defer to a later version when we fully implement value classes.

<hr/>

#### Other proposed changes:
- `Action/Perceive* should be *Action/Sensory-attend`.  
- `Action/Perceive/See* should be *Action/Sensory-attend/Look`.  
- `Action/Perceive/Hear* should be *Action/Sensory-attend/Listen`.  
 
**Response**: These changes cannot be made until a major version (e.g. 9.0.0). Not clear how they should be made. This needs more discussion and is deferred for additional discussion.

<hr/>

#### Placeholders clearly missing value class or other specification.

**Response**: Detailed work on value classes will be deferred until the next version.

<hr/>


#### Topics for future discussion

- Alternative syntax for library tags.  
- Spatial specification tags.  Should these be in a spatial library?  
- Formulation of task and event linkage.  