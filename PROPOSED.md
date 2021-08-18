##Proposed modifications for HED schema

This is a record of proposed changes/corrections to the HED schema for future release. As suggestions reach consensus they will be moved to this document. 

### Proposed changes/corrections

##### Add value class --- not sure what class this should be needs discussion (See issue #)
Item/Object/Man-made-object/Device/IO-device/Input-device/Keyboard/Keyboard-key/#
Item/Object/Man-made-object/Device/IO-device/Input-device/Keypad/Keypad-key/#
Property/Informational-property/Metadata/Pathname/#
Property/Informational-property/Metadata/CogAtlas/# (What are these?)

#### Placeholders missing value class or other specification.

##### Add numericClass attribute (* indicates should consider unit class too)
Property/Agent-property/Agent-trait/Age/#
*Property/Data-property/Data-resolution/Printer-resolution/#
*Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Sampling-rate/#
*Property/Data-property/Data-value/Spatiotemporal-value/Rate-of-change/Refresh-rate/#
*Property/Data-property/Data-value/Spatiotemporal-value/Spatial-value/Angle/#

### Typos/corrections
This section lists typos or other errors that should be fixed.

- Extra line
- Correct the word between in `**** Fraction <nowiki>[A numerical value betwee 0 and 1.]</nowiki>`
- Rename `labelClass` to `nameClass` in `Property/Informational-property/Parameter/Parameter-label/#'