## Changes to HED that were proposed and accepted.


### Changes for version 8.1.0

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
