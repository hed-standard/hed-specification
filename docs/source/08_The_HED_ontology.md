# 8. The HED ontology

--------DRAFT DRAFT DRAFT DRAFT DRAFT ------------




Range assignments
| HED ID |  Type |
| ------ | ----- | 
| 00000xx | Class entities defining the structure of a HED schema  |
| 0001xx | ObjectProperty entities common to all HED schemas.|
| xxx02xx | DataProperty entities common to all HED schemas. |  
| 00101xx-00102xx | Standard schema DataProperty and ObjectProperty entities representing<br/>schema attributes in the standard schema. |
| 00102xx | HedValueClass definitions in the standard schema. |
| 00103xx | HedUnitClass definitions in the standard schema. |
| 00104xx | HedUnitModifier definitions in the standard schema. |
| 00105xx | HedUnitClass definitions in the standard schema. |
| 00106xx-00107xx  | HedUnit definitions in the standard schema. |
 


````{admonition} **Example:** An example specification of HED version for a partnered schema.
:class: tip

The `dataset_description.json` file contains:

```json
{
  "Name": "A great experiment",
  "BIDSVersion": "1.8.0",
  "HEDVersion": "score_1.1.0"
}
```

A typical annotation is:

```text
"Data-feature, Photomyogenic-response, Wicket-spikes"
```
````
