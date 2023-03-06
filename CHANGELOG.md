# CHANGELOG for HED specification

## Changes for HED specification 3.1.0
This release is focused on corrections and clarifications in the specification document
and does not include any enhancements.

* [**Clarification**] The inner tag group in a definition cannot be empty.
* [**Clarification**] The additional tags within an `Onset` or `Offset` group must be
enclosed in parentheses. Consequently, only one definition can anchor an event of temporal extent.
* [**Correction/Clarification**] The initial specification said that definitions could be
given anywhere. Our examples only put them in dummy entries in the sidecars.
Allowing definitions to be anywhere turned out to be burdensome for downstream analysis
tools. We have now restricted definitions so that they can only appear in dummy entries of sidecars.
* [**Clarification**] Chapter 3.2 was rewritten so that full specification details of tag
syntax were given and keyed to error codes in Appendix B.
* [**Clarification**] Error codes of Appendix B were modified to have more consistent form,
and some additional codes were added to account for requirements of the specification.
* [**Improvement**] Each error code in Appendix B was given its own markdown section so that
error messages in the validators could use the error code as a link into the specification
for more information about the cause of errors.
* [**Improvement**] A standardized set of validation test data keyed to the error codes 
was added to the specification repository in the 
[**error_tests**](https://github.com/hed-standard/hed-specification/tree/master/docs/source/_static/data/error_tests) directory. This test data will be validated by both the Python 
and JavaScript validators in addition to their internal tests as part of the GitHub actions.
* [**Clarification**] All chapters of the specification were edited for clarity and correctness.

## Initial release 3.0.0 Oct. 27, 2022.

The specification version was set to 3.0.0 to designate the specification for HED-3G
corresponding to HED standard schema versions >= 8.0.0