# 8. The HED ontology

--------DRAFT DRAFT DRAFT DRAFT DRAFT ------------

The HED schema representation was developed to facilitate complex annotation of experimental data.
The Hierarchical Event Descript system also has an underlying ontological structure, 
which has been made explicit starting with HED standard schema 8.3.0 in order to
leverage links to additional external and external knowledge sources
during both annotation and analysis.


## 8.1 Assignment of global identifiers

All HED standard and library schema entities are mapped to the `HED_xxxxxxx` namespace
using the range assignments described in the following table.

| HED ID |  Type |
| ------ | ----- | 
| HED_00000xx | `Class` entities defining the structure of a HED schema  |
| HED_00001xx | `ObjectProperty` entities common to all HED schemas.|
| HED_00003xx | `DataProperty` entities common to all HED schemas. |  
| HED_00005xx | `AnnotationProperty` entities common to all HED schemas. |
| HED_00101xx-HED_00102xx | Standard schema `DataProperty` and `ObjectProperty` entities<br/>representing schema attributes in the standard schema. |
| HED_00103xx | `HedValueClass` definitions in the standard schema. |
| HED_00104xx | `HedUnitModifier` definitions in the standard schema. |
| HED_00105xx | `HedUnitClass` definitions in the standard schema. |
| HED_00106xx-HED_00107xx  | `HedUnit` definitions in the standard schema. |
| HED_00120xx-HED_0029999  | `HedTag` entities in the standard schema. |
| HED_0032000-HED_0039999  | `HedTag` entities in the score schema. |
| HED_0042000-HED_0049999  | `HedTag` entities in the lang schema. |

 

## 8.2 HED schema to ontology

### 8.2.1 HED Tags

A HED tag is represented in the HED ontology by the `HedTag` class (HED_0000016).

The HED schema hierarchy is captured by subclassing in the HED ontology.
A HED node that is a direct subclass of `HedTag` is a top-level tag in the HED schema.
A descendent of a top-level tag is a direct subclass of its parent tag in the HED schema.
The ontology subclass relationship enforces the HED requirement that each tag in the
HED schema must satisfy the **is-a** relationship with its parent in the HED schema.

The HED requirement of orthogonality between tags in different top-level subtrees 
can be captured by imposing *disjointness* on the top-level trees,
but this is not currently being enforced.

````{admonition} **Example** Ontology subclass relationships capture HED schema structure.

`Event` is a subclass of `HedTag`, so it is a top-level tag in the HED schema. 

`Sensory-event` is a subclass of `Event`.

````
