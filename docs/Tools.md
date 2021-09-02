# Tools and services

## 1. CTagger for annotation

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

## 2. Web-based tools

The web-based tools are summarized in this section. All tools are available from the main
access point [https://hedtools.ucsd.edu/hed](https://hedtools.ucsd.edu/hed). The services are
implemented in a Docker module and can be deployed locally provided that Docker is installed on.

Event files are BIDS style tab-separated value files. The first line is always a header line
giving the names of the columns, which are used as keys to metadata in accompanying JSON
sidecars. The online tools for BIDS events file are designed to help users debug their
HED annotations for BIDS datasets before using the BIDS validator.

``````{admonition} Web tools for BIDS-style events.tsv files

**Assemble events:** Assemble HED annotation of a BIDS-style events file.  
 - Upload the event file and an optional JSON sidecar file.  
 - Specify the HED version.  
 - Select the `Assemble` processing option and whether to expand definitions.  
 - Click the `Process` button.  
 - The tool assembles a new two-column event file.  
 - If there are errors, a downloadable file of error messages is returned.  
 - If no errors, the new event file is returned.  

**Validate events:** Validate a BIDS-style events file with optional JSON sidecar.
 - Upload the event file and an optional JSON sidecar file.  
 - Specify the HED version.  
 - Select the `Validate` processing option.  
 - Click the `Process` button.  
 - The tool first validates the sidecar if present.   
 - If the sidecar contains no errors, the tool validates the events file with the sidecar.  
 - If there are any errors, the tool returns a downloadable file of error messages.  

`````{admonition} Notes:
:class: tip
1. If the HED version number is given, the tool downloads a standard version from GitHub.
Otherwise, the user must upload a local HED schema. 
1. The `Assemble` creates a two-column event file. The first column is the event onset
time and the second column is the full event-level HED annotation.
`````
``````

HED schema tools are designed to assist HED schema developers and library schema developers
in making sure that the schema has the correct form and to provide easy conversion between
schema formats.

``````{admonition} Web tools for HED schema files.
**Convert schema:** Convert a HED schema between XML and MEDIAWIKI format.  
 - Upload a HED schema file or gives a URL pointing to a schema file.  
 - Select the `Convert` option.  
 - Press the `Process` button.  
 - The tool returns a downloadable converted file (XML input is converted to MEDIAWIKI and vice versa).  
 - Errors are reported as message at the bottom of the screen.  

**Validate schema:** Validate a HED schema between XML and MEDIAWIKI format.  
 - Upload a HED schema file or gives a URL pointing to a schema file.  
 - Selects the `Validate` option.  
 - Press the `Process` button.  
 - The tool returns a downloadable file of error messages if the schema is invalid.  
``````

BIDS JSON sidecars have file names ending in `_events.json`. These JSON files contain metadata
and HED tags applicable to associated events files.

``````{admonition} Web tools for BIDS style JSON sidecar.
**Convert to long:** Convert the HED tags in a BIDS-style events JSON sidecar to long form.
 - Upload the JSON sidecar file.  
 - Specify the HED version of HED.  
 - Select the `Convert to long` option.  
 - Press the `Process` button.  
 - The tool first validates the sidecar and returns an error file if errors.   
 - Otherwise, the tool returns a JSON sidecar with the HED tags converted to full-paths.  


**Convert to short:** Convert the HED tags in a BIDS-style events JSON sidecar to short form.  
 - Upload the JSON sidecar file.  
 - Specify the HED version.  
 - Select the `Convert to short` option.  
 - Press the `Process` button.  
 - The tool first validates the sidecar and returns an error file if errors.    
 - Otherwise, the tool returns a JSON sidecar with the HED tags converted to short-form.  
 
**Validate sidecar:** Validate a single BIDS-style events JSON sidecar.  
 - Upload the JSON sidecar file.   
 - Specify the HED version.  
 - Select the `Validate` option.  
 - Press the `Process` button.  
 - The tool validates the sidecar and returns an error file if there are errors.  
 
`````{admonition} Notes:
:class: tip
1. If the HED version number is given, the tool downloads a standard version from GitHub.
Otherwise, the user must upload a local HED schema. 
`````
``````

Spreadsheets (either in Excel or tab-separated-value format) are convenient for organizing tags.

``````{admonition} Web tools for spreadsheets of HED tags.
**Convert to long:** Convert the HED tags in tag spreadsheet to long form.  
 - Upload the spreadsheet file, indicating whether the first row is a header.   
 - Select a worksheet if the spreadsheet is an Excel file with multiple worksheets.   
 - Specify the HED version.  
 - Select the columns containing HED tags or are prefix columns.   
 - Select the `Convert to long` option.   
 - Press the `Process` button.  
 - The tool first validates the spreadsheet and returns an error file if errors.  
 - Otherwise, the tool returns a spreadsheet with the HED tags converted to full-paths.   

**Convert to short:** Convert the HED tags in a spreadsheet to short form.  
 - Upload the spreadsheet file, indicating whether the first row is a header.   
 - Select a worksheet if the spreadsheet is an Excel file with multiple worksheets.    
 - Specify the HED version.   
 - Select the columns containing HED tags or are prefix columns.  
 - Select the `Convert to short` option.   
 _ Press the `Process` button.   
 - The tool first validates the spreadsheet and returns an error file if errors.  
 - Otherwise, the tool returns a spreadsheet with the HED tags converted to short-form.  
 
**Validate:** Validate  the HED tags in a spreadsheet.  
 - Upload the spreadsheet file, indicating whether the first row is a header.  
 - Selects a worksheet if the spreadsheet is an Excel file with multiple worksheets.  
 - Specify the HED version.   
 - Select the columns containing HED tags or are prefix columns.  
 - Select the `Validate` option.  
 - Press the `Process` button.  
 - The tool validates the spreadsheet and returns an error file if the spreadsheet is invalid.  
 
`````{admonition} Notes:
:class: tip
1. If the HED version number is given, the tool downloads a standard version from GitHub.
Otherwise, the user must upload a local HED schema. 
`````
``````

Online validation of HED strings.

``````{admonition} Web tools for processing strings
**Convert to long:** Convert a HED string to long form.  
 - Paste a string into the input text box.  
 - Specify the HED version.  
 - Select the `Convert to long` option.  
 - Press the `Process` button.  
 - The tool first validates the string and returns errors in the lower text box if any.  
 - Otherwise the tool returns the full path version of the strings in the lower text box.  

**Convert to short:** Convert a HED tag string to short form.  
 - Paste a string into the input text box.  
 - Specify the HED version.  
 - Selects the `Convert to short` option.  
 - Press the `Process` button.  
 - The tool first validates the string and returns errors in the lower text box if any.  
 - Otherwise the tool returns the short-form versions of the tag strings in the lower text box.  
 
**Validate:** Validate a HED string.  
 - Paste a string into the input text box.  
 - Specify the HED version.  
 - Select the `Validate` option and presses the `Process` button.  
 - The tool validates the string and returns any error messages in the lower text box.  
`````{admonition} Notes:
:class: tip
1. If the HED version number is given, the tool downloads a standard version from GitHub.
Otherwise, the user must upload a local HED schema. 
`````
``````


## 3. Web-based services

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

HED services are accessed by passing a JSON dictionary of parameters in a request to the online
server. All requests include a `service` name and additional parameters. The parameters are explained
in a subsequent table.  Parameter values listed in square brackets (e,g, [`a`, `b`]) indicate that only
one of `a` or `b` should be provided.

`````{list-table} Summary of HED ReST services
:header-rows: 1
:widths: 15 20 45

* - Service
  - Parameters	
  - Descriptions
* - get_services
  - none
  - Returns a list of available services.
* - events_assemble  
  - events_string,   
    json_string,   
    [schema_version,    
    schema_string],   
    check_for_warnings,     
    defs_expand  
  - Returns an error file or a file of assembled events.
* - events_validate  
  - events_string,   
    json_string,  
    [schema_version,   
    schema_string],  
    check_for_warnings   
  - Returns an error file if errors.  
* - sidecar_to_long  
  - json_string,   
    [schema_version,   
    schema_string]   
  - Returns either an error file or converted file.  
* - sidecar_to_short 
  - json_string,   
    [schema_version,     
    hed_schema_string]  
  - Returns either an error file or a long form JSON file.   
* - sidecar_validate  
  - json_string,   
    [schema_version,   
    schema_string],  
    check_for_warnings 
  - Returns an error file if errors.  
* - spreadsheet_validate 
  - spreadsheet_string,   
    [schema_version,   
    schema_string],   
    check_for_warnings  
  - Returns an error file if errors.
* - strings_to_long  
  - string_list,    
    [schema_version,   
    schema_string]  
  - Returns errors or a list of strings to long form.
* - strings_to_short 
  - string_list,   
    [schema_version,   
    schema_string]  
  - Convert errors or a list of short-form strings.
* - strings_validate  
  - hed_strings,   
    [schema_version,   
    schema_string]	  
  - Validates a list of hed strings and returns a list of errors.
``````

The following table gives an explanation of the parameters used for various services.


`````{list-table} Parameters for web services.
:header-rows: 1
:widths: 20 20 40

* - Key value
  - Type
  - Description
* - check_for_warnings
  - boolean
  - If true, check for warnings when validating.
* - defs_expand
  - boolean
  - If true assembly replaces *def/XXX* with *def-expand/XXX*.
* - events_string
  - string
  - Events tsv file with header passed as a string.
* - hed_columns
  - list of numbers
  - A list of HED string column numbers (starting with 1).
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
``````

The web-services always return a JSON dictionary with four keys: `service`, 
`results`, `error_type`, and `error_msg`. If `error_type` and `error_msg` 
are not empty, the operation failed, while if these fields are empty, 
the operation completed. Completed operations always return their results 
in the `results` dictionary. Keys in the `results` dictionary return 
as part of a HED web service response.

`````{list-table} The results dictionary.
:header-rows: 1
:widths: 20 10 50

* - Key
  - Type
  - Description
* - command
  - string
  - Command executed in response to the service request.
* - data
  - string
  - A list of errors or the processed result.
* - schema_version
  - string
  - The version of the HED schema used in the processing.
* - msg_category
  - string
  - One of success, warning, or failure depending on the result.
* - msg
  - string
  - Explanation of the result of service processing.

``````
  
The [`hedweb/examples/matlab`](https://github.com/hed-standard/hed-python/tree/master/webtools/examples/matlab)
directory of the hed-python repository gives running MATLAB examples of how to call these services in MATLAB.

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

### 5.2 Package organization

This package contains two sub-packages.  

`hedValidator.validator` validates HED strings and contains the functions:  

> `buildSchema` imports a HED schema and returns a JavaScript Promise object.  
> `validateHedString` validates a single HED string using the returned schema object.  

`hedValidator.converter` converts HED strings between short and long forms 
and contains the following functions:  

>`buildSchema` behaves similarly to the `buildSchema` function in `hedValidator.validator` 
except that it does not work with attributes.  

> `convertHedStringToShort` converts HED strings from long form to short form.  

> `convertHedStringToLong` converts HED strings from short form to long form.  

### 5.3 Programmatic interface

The programmatic interface to the HED JavaScript `buildSchema` must be modified to accommodate
a base HED schema and arbitrary library schemas.  The BIDS validator will require
additional changes to locate the relevant HED schemas from the specification given by
`"HEDVersion"` in `dataset_description.json`. 

The programmatic interface is similar to the JSON specification of the proposed 
BIDS implementation except that the `"fileName"` key has been replaced by a `"path"`
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
