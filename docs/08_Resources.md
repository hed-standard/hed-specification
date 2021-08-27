# 8. Resources


### 8.1. Documentation

The following white paper explains the history, development, and motivation for third generation HED: 

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2020, August 1).
> Building FAIR functionality: Annotating events in time series data using Hierarchical Event Descriptors (HED).
> [https://doi.org/10.31219/osf.io/5fg73](https://doi.org/10.31219/osf.io/5fg73)

The following white paper gives a detailed case study in using HED-3G for tagging:

> Robbins, K., Truong, D., Appelhoff, S., Delorme, A., & Makeig, S. (2021, May 7). 
> Capturing the nature of events and event context using Hierarchical Event Descriptors (HED). 
> BioRxiv, 2021.05.06.442841. 
> [https://doi.org/10.1101/2021.05.06.442841](https://doi.org/10.1101/2021.05.06.442841)

A working document with the mapping of HED terms and their descriptions to known ontologies is:

> [https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing](https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing)

Two other working documents hold portions of the HED-3G specification that are under development and will not be finalized for Release 1:

> HED-3G Working Document on Spatial Annotation
> [https://docs.google.com/document/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/view?usp=sharing](https://docs.google.com/document/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/view?usp=sharing)

> HED-3G Working Document on Task Annotation
> [https://docs.google.com/document/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/view?usp=sharing](https://docs.google.com/document/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/view?usp=sharing)

### **Table A.1**. List of websites containing code and documentation.

<table>
  <tr>
   <td><strong>Description</strong></td>
   <td><strong>Site</strong></td>
  </tr>
  <tr><td colspan="2"><strong>Information and documentation</strong></td></tr>
  <tr>
   <td>HED organization website</td>
   <td><a href="https://www.hedtags.org">www.hedtags.org</a></td>
  </tr>
  <tr>
   <td>HED organization github</td>
   <td><a href="https://github.com/hed-standard">https://github.com/hed-standard</a></td>
  </tr>
  <tr>
   <td>HED specification repository</td>
   <td><a href="https://github.com/hed-standard/hed-specification">https://github.com/hed-standard/hed-specification</a>
   </td>
  </tr>
  <tr><td colspan="2"><strong>HED Python resources</strong></td></tr>
  <tr>
    <td>Python code repository</td>
    <td><a href="https://github.com/hed-standard/hed-python">https://github.com/hed-standard/hed-python</a></td>
   </tr>
   <tr>
      <td>Python validator and tools</td>
      <td><a href="https://github.com/hed-standard/hed-python/tree/master/hedtools">https://github.com/hed-standard/hed-python/tree/master/hedtools</a></td>
</tr>
 <tr>
    <td>Online tools/Docker deployment</td>
<td><a href="https://github.com/hed-standard/hed-python/tree/master/hedweb">https://github.com/hed-standard/hed-python/tree/master/hedweb</a></td>
</tr>
  <tr>
   <td colspan="2"><strong>HED JavaScript resources</strong></td>
  </tr>
  <tr>
   <td>HED JavaScript code</td>
   <td><a href="https://github.com/hed-standard/hed-javascript">https://github.com/hed-standard/hed-javascript</a></td>
   </tr>
   <tr>
   <td>BIDS validator</td>
   <td><a href="https://github.com/bids-standard/bids-validator"></a>href="https://github.com/bids-standard/bids-validator</td>
  </tr>
  <tr>
   <td colspan="2"><strong>HED Matlab resources</strong></td>
  </tr>
  <tr>
     <td>Matlab source code</td>
     <td><a href="https://github.com/hed-standard/hed-matlab">https://github.com/hed-standard/hed-matlab</a></td>
  </tr>
  <tr>
     <td colspan="2"><strong>CTAGGER resources</strong></td>
  </tr>
   <tr>
     <td>CTAGGER executable jar</td>
     <td><a href="https://github.com/hed-standard/hed-java/raw/master/ctagger.jar">https://github.com/hed-standard/hed-java/raw/master/ctagger.jar</a></td>
    </tr>
   <tr>
     <td>CTAGGER repository</td>
     <td><a href="https://github.com/hed-standard/CTagger">https://github.com/hed-standard/CTagger</a></td>
    </tr>
   <tr>
     <td>Java repository</td>
     <td><a href="https://github.com/hed-standard/hed-java">https://github.com/hed-standard/hed-java</a> </td>
    </tr>
  <tr>
   <td colspan="2"><strong>Online HED tools</strong></td>
  </tr>
  <tr>
     <td>Online website</td>
     <td><a href="https://hedtools.ucsd.edu/hed">https://hedtools.ucsd.edu/hed</a></td>
  </tr>
   <tr>
     <td>Docker deployment</td>
     <td><a href="https://github.com/hed-standard/hed-python/tree/master/webtools/deploy_hed">https://github.com/hed-standard/hed-python/tree/master/webtools/deploy_hed</a></td>
  </tr>
</table>


## 8.2. Schema viewers

The HED schema is usually developed in `.mediawiki` format and converted to XML for use by tools. However, researchers wishing to tag datasets will find both of these views hard to read. For this reason, we provide links to three versions of the schema in Table 8.2. The expandable HTML viewer is easier to navigate. Annotators can also use CTAGGER which includes a schema viewer and tagging hints.

### **Table A.2.** HED web-based schema vocabulary viewers.

<table>
  <tr>
   <td><strong>Viewer</strong></td>
   <td><strong>Link</strong></td>
  </tr>
  <tr>
   <td>Expandable HTML</td>
   <td><a href="https://www.hedtags.org/display_hed.html?version=8.0.0">https://www.hedtags.org/display_hed.html?version=8.0.0</a></td>
   </tr>
  <tr>
   <td>Mediawiki</td>
   <td><a href="https://github.com/hed-standard/hed-specification/blob/master/hedwiki/HED-generation3-schema-8.0.0.mediawiki">https://github.com/hed-standard/hed-specification/blob/master/hedwiki/HED-generation3-schema-8.0.0.mediawiki</a></td>
  </tr>
  <tr>
   <td>XML</td>
   <td><a href="https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0.xml">https://github.com/hed-standard/hed-specification/blob/master/hedxml/HED8.0.0.xml</a></td>
  </tr>
</table>


## 8.3. CTagger for annotating data

The CTagger tool for annotating data provides a graphical user interface (GUI) to assist HED users in the annotation process. CTagger can be run as a standalone application ([https://github.com/hed-standard/hed-java/raw/master/ctagger.jar](https://github.com/hed-standard/hed-java/raw/master/ctagger.jar)) or using the HEDTools plug-in in EEGLAB. The tool is designed to ease the process of constructing HED strings, with features including tag search, an expandable schema-browser view, and free-form formatting. The interchangeability between long-short forms introduced in HED-3G is fully supported. CTagger is also compatible with BIDS, allowing users to import BIDS events.tsv and events.json files to extract the event structure. Once finished tagging, users can export their HED annotation into a json file compatible with BIDS events.json. See [CTagger Github repository](https://github.com/hed-standard/CTagger) for more details, guides, and tutorials.


## 8.4. Web-based services

HED supports a number of web-based tools for HED validation, schema conversion and validation, JSON dictionary validation (as for a BIDS JSON sidecar for events), and validation of a single BIDS event file with supporting JSON sidecar. Additional web-based tools are planned for various analysis and conversion tasks. In addition, a HED web service interface is available for accessing many of the tools programmatically, including from MATLAB and Python programs. Table A.3. summarizes the location of the relevant URLs for online deployments of HED web-based tools and services.

### **Table A.3.** URLs for services online.

<table>
  <tr>
     <td><strong>URL</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td><a href="https://hedtools.ucsd.edu/hed">https://hedtools.ucsd.edu/hed</a></td>
     <td>Main access point for online HED tools.</td>
  </tr>
  <tr>
     <td><a href="https://hedtools.ucsd.edu/hed/services">https://hedtools.ucsd.edu/hed/services</a></td>
     <td>Get the initial access CSRF token.</td>
  </tr>
  <tr>
     <td><a href="https://hedtools.ucsd.edu/hed/services_submit">https://hedtools.ucsd.edu/hed/services_submit</a></td>
     <td>Send the request for the service.</td>
  </tr>
</table>


### 8.4.1. Web-based tools

The web-based tools are summarized in Table A.3. All of the tools are available from the main access point [https://hedtools.ucsd.edu/hed](https://hedtools.ucsd.edu/hed). The services are implemented in a Docker module and can be deployed locally provided that Docker is installed on the local machine. 

### **Table A.4.** Web-based HED tools.

<table>
  <tr>
     <td><strong>Tool</strong></td>
     <td><strong>Description</strong></td>
  </tr>
  <tr>
     <td>Validate events</td>
     <td><p>Validate a BIDS-style events file with optional JSON sidecar.</p>
<p>The user uploads the two files to validate. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p> <p>The tool first validates the sidecar if present and if the sidecar contains no errors validates the events file in conjunction with the sidecar. If there are errors, the tool returns a downloadable file of error messages.</p></td>
  </tr>
  <tr>
     <td>Validate dictionary</td>
     <td><p>Validate a single BIDS-style events JSON sidecar.</p>
   <p>The user uploads the file. The user also specifies which version of HED to validate against either by selecting a standard version from Github or uploading a local HED schema.</p> 
  <p>If there are errors, the tool returns a downloadable file of error messages.</p></td>
  </tr>
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

HED services are accessed by passing a JSON dictionary of parameters in a request to the online server. All requests include a `service` name and additional parameters. Table 8.5. summarizes the available web-services and their parameters. The meaning of the different parameters is given in Table 8.6.  


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

The request is given as in JSON format. The possible keys and their types are described in Table 8.6.

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


The web-services always return a JSON dictionary with four keys: `service`, `results`, `error_type`, and `error_msg`. If `error_type` and `error_msg` are not empty, the operation failed, while if these fields are empty, the operation completed. Completed operations always return their results in the `results` dictionary. The field of the `results` dictionary are shown in Table 8.7

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

The `hedweb/examples/matlab` directory of the `hed-python` repository gives running MATLAB examples of how to call these services in MATLAB.

## 8.5. HED validation source code

### 8.5.1. HED validation in python

The python code for validation is in the  `hedtools` project located in the `hed-python` repository [https://github.com/hed-standard/hed-python](https://github.com/hed-standard/hed-python). You can install the tools using `pip` if you have downloaded the `hed-python` repository:

    pip install <hedtools-local-path>

The validation functions are in the `hed.validator` module. The data representations for various items such as dictionaries or event files can be found in the `hed.models` module. The hed_input.py module reads in a spreadsheet and possibly a dictionary and creates a `HedInput` object representing the spreadsheet. The `hed-validator.py` module creates a `HedValidator` object that takes a `HedSchema` object to use in subsequent validation. The `validate_input` method of `HedValidator` validates HED input in various formats and returns a list of issues.

### 8.5.2. JavaScript validation 

The JavaScript code for HED validation is in the validation directory of the `hed-javascript` repository located at [https://github.com/hed-standard/hed-javascript](https://github.com/hed-standard/hed-javascript).  

#### 8.5.2.1. Installation

You can install the validator using `npm`:

    npm install hed-validator

#### 8.5.2.2. Usage

This package contains two sub-packages. `hedValidator.validator` validates HED strings and contains the functions: `buildSchema`, which imports a HED schema and returns a JavaScript Promise object, and `validateHedString`, which validates a single HED string using the returned schema object. `hedValidator.converter` converts HED 3 strings between short and long forms and contains the following functions: `buildSchema`, which behaves similarly to the `buildSchema` function in `hedValidator.validator` except that it does not work with attributes, `convertHedStringToShort`, which converts HED strings from long form to short form, and `convertHedStringToLong`, which converts HED strings from short form to long form.

#### 8.5.2.3. Programmatic interface

The programmatic interface to the HED JavaScript `buildSchema` must be modified to accommodate a base HED schema and arbitrary library schemas. Section 4.3.1 outlined the proposed changes in the BIDS specification from the viewpoint of the user.  The BIDS validator will require additional changes to locate the relevant HED schemas from the specification given by `"HEDVersion"` in `dataset_description.json`. The programmatic interface is similar to the JSON specification of section 4.3.1, except that the `"fileName"` key has been replaced by a `"path"` key to emphasize that callers must replace filenames with full paths before calling `buildSchema`. 

**Example:** JSON passed to `buildSchema` to construct the schemas needed for the example in Section 4.3.1. Here the dataset is located in `/data/wonderful`.

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

**NOTE:** This interface is proposed and is awaiting resolution of BIDS PR #820 on file passing to BIDS.

### 8.5.3. HED validation in MATLAB

HED validation can be done using the online web-services from MATLAB as shown in the `./examples/matlab` directory of the [hedweb](https://github.com/hed-standard/hed-python/tree/master/webtools) project in the [hed-python](https://github.com/hed-standard/hed-python) repository.
