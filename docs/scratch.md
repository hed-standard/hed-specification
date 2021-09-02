# Scratch

`````{list-table} Schema attributes.
:header-rows: 1
:widths: 15, 10, 50

* - Attribute
  - Modifies
  - Description
* - `allowedCharacter`
  - `valueClass`
  - Specifies characters allowed in that value class.
* - `defaultUnits`
  - `unitClass`
  - Specifies the default units to use if substituted placeholder value has no units.  
* - `extensionAllowed`
  - `node`
  -  Indicates unlimited levels of child nodes can be added under this tag. 
`````  

Another try
`````{list-table} Schema attributes.
:header-rows: 1
:widths: 15 10 50

* - Attribute
  - Modifies
  - Description
* - `recommended`
  - `node`
  -  Specifies that the event-level HED string should include this tag.
* - `relatedTag`
  - `node`
  - Specifieds a HED tag value closely related to this HED tag.
* - `requireChild`
  - `node`
  -  Specifies that a child of this node must also be included in the HED tag.
`````  
  
Testing
* - `required`
  -  An attribute of schema nodes indicating that the event-level HED string must include this tag.
* - `SIUnit`
  -  An attribute of units indicating that this unit represents an SI unit and can be modified by 
  multiple and submultiple names.
`````  
  If an SI unit does not also have the `unitSymbol` attribute. Multiples and submultiples with the
  `SIUnitModifier` are used. Otherwise, Multiples and submultiples with the `SIUnitSymbolModifier` are used.
  
  Note that some units such as byte are designated as SI units although they are not part of the standard.
* - `SIUnitModifier`
  - An attribute of unit modifiers that indicates the modifier applies to base units rather than unit symbols.
* - `SIUnitSymbolModifier`
  -  An attribute of unit modifiers that indicates the modifier applies to unit symbols rather than base units.
* - `suggestedTag`
  - An attribute of schema nodes that takes a HED tag value that should probably be included with this HED tag.
* - `tagGroup`
  -  An attribute of schema nodes indicating that the tag can only appear inside a tag group.
* - `takesValue`
  -  An attribute of schema nodes indicating the tag is a placeholder (`#`) that is expected to be replaced
  by a value. This tag will be deprecated.
* - `takesValue`
  -  An attribute of schema nodes indicating the tag is a placeholder (`#`) that is expected to be replaced
  by a value. This tag will be deprecated.      
* - `topLevelTagGroup`
  -  An attribute of schema nodes indicating that this tag (or its descendants) can only appear in
   a top-level tag group.
* - `unique`
  -  An attribute of schema nodes indicating that only one of this tag or its descendants can be used
    in the event-level HED string.
* - `unitClass`
  -  An attribute of schema placeholder (`#`) nodes indicating which unit class this value tag belongs to.
* - `unitPrefix`
  -  An attribute of units indicating that the unit indicator is a prefix (e.g., `$` in the `currency` units).
* - `unitSymbol`
  -  An attribute of units indicating this tag is an abbreviation or symbol representing a type of unit.
  
  Unit symbols represent both the singular and the plural and thus cannot be pluralized.
* - `valueClass`
  -  An attribute of schema placeholder (`#`) nodes indicating which value class this value tag belongs to.        
````{admonition} Notes on rules for allowed characters in the HED schema. 
:class: tip

1. Schema attributes with the `boolProperty`  have a `<name>` node but no `<value>` node in the XML.
Presence indicates true.
2. Schema attributes with the `boolProperty`  have both `<name>` and `<value>` nodes in the XML.
````
`````

An attribute of value classes that takes a value specifying a special character that can be
    included in node names or values of placeholders that have this value class.  
    
    Normally the allowed characters are listed individually as values of the `allowedCharacter`
    attribute. However, the word `letters` designates upper and lower case alphabetic characters. 
    
    The word `digits` indicates the digits 0-9.

  For example, when a placeholder (`#`) of the time unit class is 
  replaced with an actual value and the units are not explicitly listed, 
  they are assumed to be seconds (s) because the time unit class has `defaultUnits=s`.
  
The extensionAllowed  This tag is propagated to child nodes with the exception of nodes with a placeholder (`#`) child.

## 