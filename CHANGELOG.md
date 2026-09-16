# CHANGELOG for HED specification

## Changes for HED specification 4.0.0

This is a breaking change:

- The PDF versions of the schema (formerly stored in `hedspec`) has been removed. HED specifications will just undergo the GITHUB releases.
- The versions of the standard HED schema that were stored in `hedxml` for backwards compatibility has been removed.
- The `tests` directory containing the JSON tests that HED validators must pass has been moved to the GitHub `hed-standard/hed-tests` repository.
- Tools that write schema files include the Sources, Prefixes, and External annotations sections in every format, empty when the schema has no entries. Tools that read schema files require these sections in standard schemas with versions >= `8.5.0` and in library schemas partnered with those standard schemas; for compatibility they accept their omission from older standard schemas and from unpartnered library schemas and treat an omitted section as empty.
- Units: all unit strings (names, symbols, and SI modifiers) are case-sensitive; unit names may be pluralized, symbols never. A value with units is the number, one blank, and the unit.
- Units: a compound unit (`m-per-s`, `m-per-s^2`, `m^3`, `mol-per-L`) with `SIUnit` takes one SI modifier on each component, with the conversion factor computed component-wise; a modifier no longer applies to the whole string.
- Units: `conversionFactor` is the factor by which a value in the unit is multiplied to obtain default units; a unit without one has no defined conversion. A unit class in a standard schema >= `8.5.0` (or a partnered library) may not list a unit derivable from another unit of the class by an SI modifier (SCHEMA_DUPLICATE_NODE); `defaultUnits` may be such a derived form.
- Units: a `#` placeholder has at most one unit class and, when it has one, `valueClass=numericClass` (SCHEMA_ATTRIBUTE_VALUE_INVALID otherwise; the value-class rule is checked for standard schemas >= `8.5.0` and partnered libraries). A schema MAY define the empty pseudo unit class `anyUnits`; a placeholder with `unitClass=anyUnits` accepts a unit from any unit class, a listed unit winning over a derived form, and a string derived by two classes and listed by none is SCHEMA_DUPLICATE_NODE. HED `8.5.0` introduces `anyUnits` and `Quantity`. The `unitPrefix` attribute and `$` are deprecated as of HED `8.5.0`.
- `hedId` values are assigned only at release and never reused; retired identifiers are recorded under `retired_ids` in hed-schemas `library_data.json`.
- The `annotation` schema attribute has one grammar: `prefix:id value`, where `prefix:id` is a row of the External annotations section and `prefix` a row of the Prefixes section. A link to a term in an external ontology is written with a SKOS mapping property (`skos:exactMatch ncit:C25499`) rather than as a bare term. A `dc:source` value must name a row of the Sources section, by the row's `source` name or by a URL under the row's `link`; Appendix A.1.6 no longer says that sources do not affect validation. A violation of either rule is the new SCHEMA_ANNOTATION_INVALID warning (Appendix B), with reasons a-d. The rules apply to standard schemas with versions >= `8.5.0` and to library schemas partnered with them.

## Changes for HED specification 3.2.0

- The `Inset` tag was introduced to mark intermediate points in events of temporal extent.
- Partnered schemas were introduced using the `withStandard` schema header attribute and the `rooted` schema attribute.
- The curly brace annotation for sidecars was introduced.

## Changes for HED specification 3.1.1

This release is added additional minor corrections and clarifications in the specification document and does not include any enhancements from version 3.0.0.

## Changes for HED specification 3.1.0

This release is focused on corrections and clarifications in the specification document and does not include any enhancements.

- \[**Clarification**\] The inner tag group in a definition cannot be empty.
- \[**Clarification**\] The additional tags within an `Onset` or `Offset` group must be enclosed in parentheses. Consequently, only one definition can anchor an event of temporal extent.
- \[**Correction/Clarification**\] The initial specification said that definitions could be given anywhere. Our examples only put them in dummy entries in the sidecars. Allowing definitions to be anywhere turned out to be burdensome for downstream analysis tools. We have now restricted definitions so that they can only appear in dummy entries of sidecars.
- \[**Clarification**\] Chapter 3.2 was rewritten so that full specification details of tag syntax were given and keyed to error codes in Appendix B.
- \[**Clarification**\] Error codes of Appendix B were modified to have more consistent form, and some additional codes were added to account for requirements of the specification.
- \[**Improvement**\] Each error code in Appendix B was given its own markdown section so that error messages in the validators could use the error code as a link into the specification for more information about the cause of errors.
- \[**Improvement**\] A standardized set of validation test data keyed to the error codes was added to the specification repository in the [**tests**](https://github.com/hed-standard/hed-specification/tree/main/tests) directory. This test data will be validated by both the Python and JavaScript validators in addition to their internal tests as part of the GitHub actions.
- \[**Clarification**\] All chapters of the specification were edited for clarity and correctness.

## Initial release 3.0.0 Oct. 27, 2022.

The specification version was set to 3.0.0 to designate the specification for HED-3G corresponding to HED standard schema versions >= 8.0.0
