## Proposed modifications for future releases of the HED schema

This is a record of proposed changes/corrections to the HED schema for future release. As suggestions reach consensus they will be incorporated into the prerelease version. 


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