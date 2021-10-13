## Proposed modifications for HED schema

This is a record of proposed changes/corrections to the HED schema for future release. As suggestions reach consensus they will be moved to this document. 

### Proposed changes/corrections (requiring more development/discussion)

#### Add Body between Anatomical-item and Body-part
Then we can annotate right hand as (Hand, (Right-side-of, Body)).
Should the recommended way to annotate right hand be:
(Hand, (Right-side-of, Body))
(Hand, (Right-side-of, Human-agent))
(Hand, (Right-side-of, (Human-agent, Torso)))

#### Add value class --- not sure what class this should be needs discussion (See issue #324)
- Item/Object/Man-made-object/Device/IO-device/Input-device/Keyboard/Keyboard-key/#
- Item/Object/Man-made-object/Device/IO-device/Input-device/Keypad/Keypad-key/#
- Property/Informational-property/Metadata/Pathname/#
- Property/Informational-property/Metadata/CogAtlas/# (What are these?)

### Placeholders clearly missing value class or other specification.

##### Add numericClass attribute (* indicates should consider unit class too)
- *Property/Agent-property/Agent-trait/Age/#*
- *Property/Data-property/Data-resolution/Printer-resolution/#*
- *Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Sampling-rate/#*
- *Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Refresh-rate/#*
- *Property/Data-property/Data-value/Spatiotemporal-value/Spatial-value/Angle/#*

### Review of attributes
- *takesValue* appears to now be redundant, as it is only used with #, which is assumed to take a value.
- Do we need a *topLevel* attribute?

### Agreed upon changes/corrections
- *Action/Perceive* should be *Action/Sensory-attend*.
- *Action/Perceive/See* should be *Action/Sensory-attend/Look*.
- *Action/Perceive/Hear* should be *Action/Sensory-attend/Listen*.


### Typos/corrections
This section lists typos or other errors that should be fixed.

- Correct the word between in `**** Fraction <nowiki>[A numerical value betwee 0 and 1.]</nowiki>`
- Rename `labelClass` to `nameClass` in `Property/Informational-property/Parameter/Parameter-label/#'
- Rename `labelClass` to `nameClass` in `Property/Sensory-property/Sensory-attribute/auditory-attribute/Timbre/#'

### Suggested additions
This section suggests listed additions to the HED tags

- Add `Distracted` to `Agent-emotional-state`.  (Source Monique Denissen.  Re: Often experiments are designed with
  distractions and surveys may assess the participant's degree of distration.)
- Add Arrow to 2D-shape. (Source Monique Denissen.  Re:  Arrow is a common 2D-shape used in experiments.
- Needed some way of tagging that the participant is finished --- like an OK or Done.  (Source Monique Denissen)
