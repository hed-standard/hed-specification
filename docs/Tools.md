# Tools and services

## 1. CTagger for annotating data

The CTagger tool for annotating data provides a graphical user interface (GUI) to assist HED users 
in the annotation process. CTagger can be run as a standalone application 
([https://github.com/hed-standard/hed-java/raw/master/ctagger.jar](https://github.com/hed-standard/hed-java/raw/master/ctagger.jar)) or using the HEDTools plug-in in EEGLAB. 

The tool is designed to ease the process of constructing HED strings, with features including tag search, 
an expandable schema-browser view, and free-form formatting. The interchangeability between long-short 
forms introduced in HED-3G is fully supported. CTagger is also compatible with BIDS, allowing users to 
import BIDS `events.tsv` and `events.json` files to extract the event structure. Once finished tagging, 
users can export their HED annotation into a json file compatible with BIDS events.json. 
See [CTagger GitHub repository](https://github.com/hed-standard/CTagger) for more details, 
guides, and tutorials.


## 2. Web-based services

HED supports a number of web-based tools for HED validation, schema conversion and validation, 
JSON dictionary validation (as for a BIDS JSON sidecar for events), and validation of a single
BIDS event file with supporting JSON sidecar. 

Additional web-based tools are planned for various analysis and conversion tasks. 
In addition, a HED web service interface is available for accessing many of the 
tools programmatically, including from MATLAB and Python programs. 
The following table summarizes the location of the relevant URLs for online deployments of HED 
web-based tools and services.

`````{list-table} URLs for HED online services.
:header-rows: 1
:widths: 20 50

* - Service
  - URL
* - Online HED tools
  - [https://hedtools.ucsd.edu/hed](https://hedtools.ucsd.edu/hed)
* - CSRF token access
  - [https://hedtools.ucsd.edu/hed/services](https://hedtools.ucsd.edu/hed/services)  
* - Service request
  - [https://hedtools.ucsd.edu/hed/services_submit](https://hedtools.ucsd.edu/hed/services_submit)
`````


### 2.1. Web-based tools

The web-based tools are summarized in Table A.3. All tools are available from the main
access point [https://hedtools.ucsd.edu/hed](https://hedtools.ucsd.edu/hed). The services are
implemented in a Docker module and can be deployed locally provided that Docker is installed on
the local machine.

HED services are accessed by passing a JSON dictionary of parameters in a request to the online server. All requests include a service name and additional parameters. Table 8.5. summarizes the available web-services and their parameters. The meaning of the different parameters is given in Table 8.6.

`````{list-table} Top-level JSON parameter dictionary for HED services.
:header-rows: 1
:widths: 20 20 40

* - Service	Parameters	Descriptions
* - get_services
  - none
  - Returns a list of available services.
* - dictionary_to_long
  - json_string,
  [schema_version, hed_schema_string]
  - Returns either an error file or a JSON file converted to long form depending
  on whether conversion was successful or not.
* - dictionary_to_short
  - json_string,
  [schema_version, hed_schema_string]
  - Returns either an error file or a JSON file converted to long form 
  depending on whether conversion was successful or not.
* - dictionary_validate
  - json_string,
  [schema_version, hed_schema_string],
  check_for_warnings
  - Returns an error file if the JSON file has validation errors.
* - events_assemble	events_string,
  - json_string,
  [schema_version, hed_schema_string],
  check_for_warnings,
  defs_expand
  - Returns an error file if the JSON file or events file has 
  validation errors otherwise returns a file of assembled events.
* - events_validate
  - events_string,
  json_string,
  [schema_version, hed_schema_string],
  check_for_warnings
  - Returns an error file if the JSON file or events file has validation errors.
* - spreadsheet_validate
  - spreadsheet_string,
  [schema_version, hed_schema_string],
  check_for_warnings
  - A tsv spreadsheet of event codes and their tags is sent to be validated. 
  Returns an error file if the spreadsheet has validation errors.
* - strings_to_long
  - string_list,
  [schema_version, hed_schema_string]
  - Convert a list of strings to long form if valid, otherwise return errors.
* - strings_to_short
  - string_list,
  [schema_version, hed_schema_string]
  - Convert a list of strings to short form if valid, otherwise return errors.
* - strings_validate
  - hed_strings,
  [schema_version, hed_schema_string]	
  - Validates a list of hed strings using the specified HED schema 
  and returns a list of the same length as hed strings.
`````

Each entry in the return list is either empty if the corresponding string has no errors or contains a string with the errors in readable form.

`````{list-table} Top-level JSON parameter dictionary for HED services.
:header-rows: 1
:widths: 20 10 50

* - Key	value
  - Type
  - Description
* - check_for_warnings
  - boolean
  - If true, check for warnings when validating.
* - defs_expand
  - boolean
  - If true assembly expands definitions, replacing def/XXX with def-expand/XXX.
* - events_string
  - string
  - Events tsv file with header passed as a string.
* - hed_columns
  - list of numbers
  - A list of column numbers (starting with 1) of columns containing HED strings. If empty, all columns are used.
* - hed_schema_string
  - string
  - HED schema in XML format as a string.
* - hed_strings
  - list of strings
  - A list containing HED strings.
* - json_string
  - string
  - BIDS-style JSON events sidecar as a string.
* - json_strings
  - string
  - A list of BIDS-style JSON sidecars as strings.
* - schema_string
  - string
  - A HED schema file as a string.
* - schema_version
  - string
  - Version of HED to be accessed if relevant.
* - service
  - string
  - The name of the requested service.
* - spreadsheet_string
  - string
  - A spreadsheet tsv as a string.
`````

The web-services always return a JSON dictionary with four keys: `service`, `results`, 
`error_type`, and `error_msg`. If `error_type` and `error_msg` are not empty, the operation failed,
while if these fields are empty, the operation completed. Completed operations always 
return their results in the `results` dictionary. The field of the `results` dictionary are shown in Table 8.7

Keys in the `results` dictionary return as part of a HED web service response.

`````{list-table} The results dictionary.
:header-rows: 1
:widths: 20 10 50

* - Key
  - Type
  - Description
* - `command`
  - string
  - The command that was executed in response to the service request.
* - `data`
  - string
  - The data returned by the service. This could be a list of errors or the processed 
  result depending on what happened.
* - `schema_version`
  - string
  - The version of the HED schema used in the processing.
* - `msg_category`
  - string
  - One of success, warning, or failure depending on the result of processing the service.
* - `msg`
  - string
  - Explanation of the result of service processing.

`````

The [`hedweb/examples/matlab`](https://github.com/hed-standard/hed-python/tree/master/webtools/examples/matlab)
directory of the hed-python repository gives running MATLAB examples of how to call these services in MATLAB.




### **Table A.4.** Web-based HED tools.

``````{admonition} Summary of HED web-based tools.
**Validate events:** Validate a BIDS-style events file with optional JSON sidecar.
 ~ The user uploads the two files to validate. 
 ~ The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.
 ~ The tool first validates the sidecar if present and if the sidecar contains no errors validates the events file in conjunction with the sidecar.
 ~ If there are errors, the tool returns a downloadable file of error messages.

**Validate sidecar:** Validate a single BIDS-style events JSON sidecar.
 ~ The user uploads the JSON sidecar file.  
 ~ The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.
 ~ The tool first validates the sidecar if present and if the sidecar contains no errors validates the events file in conjunction with the sidecar.
 ~ If there are errors, the tool returns a downloadable file of error messages.

``````

Here is the leftovers for testing.
<table>
  <tr>
     <td>Validate spreadsheet</td>
     <td><p>Validate an Excel or tsv file containing HED tags.</p> 
<p>The user uploads an Excel or tsv file and selects a worksheet if the file is an Excel file. The user indicates which columns contain HED tags. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p><p>If there are errors, the tool returns a downloadable file of error messages.</p></td>
  </tr>
  <tr>
    <td>Process string</td>
    <td><p>Validate or convert a HED string.</p>
<p>The user enters or pastes a HED string into a text box. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p><p>The user selects one of three processing options: 1) Validate,  2) Convert from long to short form, or 3) Convert from short to long form.</p> <p>The results appear in the results text box.</p></td>
  </tr>
  <tr>
     <td>Process schema</td>
     <td><p>Validate or check a HED schema.</p>
<p>The user enters the URL of a HED schema or uploads a HED schema file in either <em>.mediawiki</em> or <em>.xml</em> format. The user selects either the validate or convert option and presses the Submit button.</p><p>If the convert option was selected, the tools convert the schema to the other format and make the converted file available for download. If the validate option was selected, button, the tools check the file for compliance errors.</p></td>
  </tr>
</table>

### 8.4.2. HED web services

HED services are accessed by passing a JSON dictionary of parameters in a request to the online
server. All requests include a `service` name and additional parameters. Table 8.5. summarizes
the available web-services and their parameters. The meaning of the different parameters is 
given in Table 8.6.  


### *Table 8.5.* Summary of available web-services. 

<table>
  <tr>
     <td><strong>Service</strong></td>
     <td><strong>Parameters</strong></td>
     <td><strong>Descriptions</strong></td>
  </tr>
  <tr>
     <td><code>get_services</code></td>
     <td><code>none</code></td>
     <td>Returns a list of available services.</td>
  </tr>
  <tr>
     <td><code>dictionary_to_long</code></td>
     <td><code>json_string</code>,<br>
     <code>[schema_version, hed_schema_string]</code></td>
     <td>Returns either an error file or a JSON file converted to long form depending on whether conversion was successful or not.</td>
  </tr>
  <tr>
     <td><code>dictionary_to_short</code></td>
     <td><code>json_string</code>,<br>
         <code>[schema_version, hed_schema_string]</code></td>
     <td>Returns either an error file or a JSON file converted to long form depending on whether conversion was successful or not.</td>
  </tr>
  <tr>
     <td><code>dictionary_validate</code></td>
     <td><code>json_string</code>,<br><code>[schema_version, hed_schema_string]</code>,<br>
       <code>check_for_warnings</code></td>
     <td>Returns an error file if the JSON file has validation errors.</td>
  </tr>
  <tr>
    <td><code>events_assemble</code></td>
    <td><code>events_string</code>,<br>
        <code>json_string</code>,<br>
        <code>[schema_version, hed_schema_string]</code>,<br>
        <code>check_for_warnings</code>,<br>
        <code>defs_expand</code></td>
    <td>Returns an error file if the JSON file or events file has validation errors otherwise returns a file of assembled events.</td>
  </tr>
  <tr>
     <td><code>events_validate</code></td>
     <td><code>events_string</code>,<br>
         <code>json_string</code>,<br>
<code>[schema_version, hed_schema_string]</code>,<br>
<code>check_for_warnings</code></td>
     <td>Returns an error file if the JSON file or events file has validation errors.</td>
  </tr>
  <tr>
     <td><code>spreadsheet_validate</code></td>
     <td><code>spreadsheet_string</code>,<br>
<code>[schema_version, hed_schema_string]</code>,<br>
<code>check_for_warnings</code></td>
    <td>A tsv spreadsheet of event codes and their tags is sent to be validated. Returns an error file if the spreadsheet has validation errors.</td>
  </tr>
  <tr>
     <td><code>strings_to_long</code></td>
     <td><code>string_list</code>,<br>
<code>[schema_version, hed_schema_string]</code></td>
     <td>Convert a list of strings to long form if valid, otherwise return errors.</td>
  </tr>
  <tr>
     <td><code>strings_to_short</code></td>
     <td><code>string_list</code>,<br>
     <code>[schema_version, hed_schema_string]</code>
   </td>
     <td>Convert a list of strings to short form if valid, otherwise return errors.</td>
  </tr>
  <tr>
    <td><code>strings_validate</code></td>
    <td><code>hed_strings</code>,<br>
     <code>[schema_version, hed_schema_string]</code></td>
    <td><p>Validates a list of hed strings using the specified HED schema and returns a list of the same length as hed strings.</p><p> Each entry in the return list is either empty if the corresponding string has no errors or contains a string with the errors in readable form.</p></td>
  </tr>
</table>

The request is given as in JSON format. The possible keys and their types are described in 
Table 8.6.

### *Table 8.6.* Top-level JSON parameter dictionary for HED services.

<table>
  <tr>
     <td><strong>Key</strong></td>
     <td><strong>Value</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>check_for_warnings</code></td>
     <td>boolean</td>
     <td>If true, check for warnings when validating.</td>
  </tr>
  <tr>
     <td><code>defs_expand</code></td>
     <td>boolean</td>
     <td>If true assembly expands definitions, replacing <em>def/XXX</em> with <em>def-expand/XXX</em>.</td>
  </tr>
  <tr>
     <td><code>events_string</code></td>
     <td>string</td>
     <td>Events tsv file with header passed as a string.</td>
  </tr>
  <tr>
     <td><code>hed_columns</code></td>
     <td>list of numbers</td>
     <td>A list of column numbers (starting with 1) of columns containing HED strings. If empty, all columns are used.</td>
  </tr>
  <tr>
     <td><code>hed_schema_string</code></td>
     <td>string</td>
     <td>HED schema in XML format as a string.</td>
  </tr>
  <tr>
     <td><code>hed_strings</code></td>
     <td>list of strings</td>
     <td>A list containing HED strings.</td>
  </tr>
  <tr>
     <td><code>json_string</code></td>
     <td>string</td>
     <td>BIDS-style JSON events sidecar as a string.</td>
  </tr>
  <tr>
     <td><code>json_strings</code></td>
     <td>string</td>
     <td>A list of BIDS-style JSON sidecars as strings.</td>
  </tr>
  <tr>
     <td><code>schema_string</code></td>
     <td>string</td>
     <td>A HED schema file as a string.</td>
  </tr>
  <tr>
     <td><code>schema_version</code></td>
     <td>string</td>
     <td>Version of HED to be accessed if relevant.</td>
  </tr>
  <tr>
     <td><code>service</code></td>
     <td>string</td>
     <td>The name of the requested service.</td>
  </tr>
  <tr>
     <td><code>spreadsheet_string</code></td>
     <td>string</td>
     <td>A spreadsheet tsv as a string.</td>
  </tr>
</table>


The web-services always return a JSON dictionary with four keys: `service`, `results`, 
`error_type`, and `error_msg`. If `error_type` and `error_msg` are not empty, the operation
failed, while if these fields are empty, the operation completed. Completed operations always
return their results in the `results` dictionary. The field of the `results` dictionary are 
shown in Table 8.7

### *Table 8.7.* Keys in the `results` dictionary return as part of a HED web service response.

<table>
  <tr>
     <td><strong>Key</strong></td>
     <td><strong>Value</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><code>command</code></td>
     <td>string</td>
     <td>The command that was executed in response to the service request.</td>
  </tr>
  <tr>
     <td><code>data</code></td>
     <td>string</td>
     <td>The data returned by the service. This could be a list of errors or the processed result depending on what happened.</td>
  </tr>
  <tr>
     <td><code>schema_version</code></td>
     <td>string</td>
     <td>The version of the HED schema used in the processing.</td>
  </tr>
  <tr>
     <td><code>msg_category</code></td>
     <td>string</td>
     <td>One of success, warning, or failure depending on the result of processing the service.</td>
  </tr>
  <tr>
     <td><code>msg</code></td>
     <td>string</td>
     <td>Explanation of the result of service processing.</td>
  </tr>
</table>

The `hedweb/examples/matlab` directory of the `hed-python` repository gives running MATLAB 
examples of how to call these services in MATLAB.

## 4. Python tools

The python code for validation is in the  `hedtools` project located in the `hed-python` 
repository [https://github.com/hed-standard/hed-python](https://github.com/hed-standard/hed-python). You can install the tools using `pip` if you have downloaded 
the `hed-python` repository:

    pip install <hedtools-local-path>

The validation functions are in the `hed.validator` module. The data representations for 
various items such as dictionaries or event files can be found in the `hed.models` module. 
The `hed_input.py` module reads in a spreadsheet and possibly a dictionary and creates a 
`HedInput` object representing the spreadsheet. The `hed-validator.py` module creates a
`HedValidator` object that takes a `HedSchema` object to use in subsequent validation. 
The `validate_input` method of `HedValidator` validates HED input in various formats and
returns a list of issues.

## 5. JavaScript tools 

The JavaScript code for HED validation is in the validation directory of the 
`hed-javascript` repository located at [https://github.com/hed-standard/hed-javascript](https://github.com/hed-standard/hed-javascript).

### 5.1 Installation

You can install the validator using `npm`:

    npm install hed-validator

This package contains two sub-packages. `hedValidator.validator` validates HED strings and
contains the functions: `buildSchema`, which imports a HED schema and returns a JavaScript
Promise object, and `validateHedString`, which validates a single HED string using the returned
schema object. `hedValidator.converter` converts HED 3 strings between short and long forms 
and contains the following functions: `buildSchema`, which behaves similarly to the 
`buildSchema` function in `hedValidator.validator` except that it does not work with attributes,
`convertHedStringToShort`, which converts HED strings from long form to short form, 
and `convertHedStringToLong`, which converts HED strings from short form to long form.

### 5.3 Programmatic interface

The programmatic interface to the HED JavaScript `buildSchema` must be modified to accommodate
a base HED schema and arbitrary library schemas.  The BIDS validator will require
additional changes to locate the relevant HED schemas from the specification given by
`"HEDVersion"` in `dataset_description.json`. The programmatic interface is similar to the JSON 
specification of the proposed BIDS implementation except that the `"fileName"` key has been replaced by a `"path"`
key to emphasize that callers must replace filenames with full paths before calling 
`buildSchema`. 

````{admonition} **Example:** JSON passed to buildSchema.

```json
{
    "path": "/data/wonderful/code/mylocal.xml",
    "libraries": {
        "la": {
            "libraryName": "libraryA",
            "version": "1.0.2"
        },
        "lb": {
            "libraryName": "libraryB",
            "path": "/data/wonderful/code/HED_libraryB_0.5.3.xml"
        }
    }
}
```
````

**NOTE:** This interface is proposed and is awaiting resolution of BIDS PR #820 on file passing to BIDS.

## 6. MATLAB tools

HED validation can be done using the online web-services from MATLAB as shown in the
`./examples/matlab` directory of the
[hedweb](https://github.com/hed-standard/hed-python/tree/master/webtools) project in the
[hed-python](https://github.com/hed-standard/hed-python) repository.
