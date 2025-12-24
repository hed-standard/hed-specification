HED specification
=================

.. sidebar:: Quick links  

   * `HED homepage <https://www.hedtags.org/>`_

   * `HED resources <https://www.hedtags.org/hed-resources/>`_

   * `HED schema browser <https://www.hedtags.org/hed-schema-browser/>`_

   * `HED online tools <https://hedtools.org/hed>`_


Welcome to the official specification for Hierarchical Event Descriptors (HED), a system for annotating events and experimental structure using controlled vocabularies.

About HED
---------

HED (Hierarchical Event Descriptors) is a system for annotating events and experimental structure using controlled vocabularies. The HED ecosystem includes:

- **Vocabularies** - Standardized terms organized in hierarchical schemas
- **Annotation tools** - Software for creating and validating HED annotations
- **Analysis tools** - Methods for searching and analyzing HED-annotated data
- **Community schemas** - Domain-specific extensions to the base vocabulary

Specification contents
----------------------

1. Introduction
~~~~~~~~~~~~~~~
:doc:`Introduction to HED <01_Introduction>` - Overview of the HED system and its applications.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- HED system overview
- Integration with neuroimaging standards
- Schema vocabulary
- Getting started

2. Terminology
~~~~~~~~~~~~~~
:doc:`Terminology <02_Terminology>` - Key concepts and definitions used throughout the specification.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- Character sets and restrictions
- HED vocabulary terminology
- Schema version naming
- Tag specification

3. HED formats
~~~~~~~~~~~~~~
:doc:`HED formats <03_HED_formats>` - Schema and annotation format specifications.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- Schema format
- HED string format
- Sidecar format
- Assembly and validation

4. Basic annotation
~~~~~~~~~~~~~~~~~~~
:doc:`Basic annotation <04_Basic_annotation>` - Fundamental annotation techniques and best practices.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- Annotation principles
- Basic event markup
- Event context
- Temporal relationships

5. Advanced annotation
~~~~~~~~~~~~~~~~~~~~~~
:doc:`Advanced annotation <05_Advanced_annotation>` - Complex annotation patterns and advanced features.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- Definitions
- Temporal scope
- Event structure
- Advanced examples

6. Infrastructure and tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
:doc:`Infrastructure and tools <06_Infrastructure_and_tools>` - HED ecosystem tools and services.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- HED tools overview
- Validation services
- Web-based tools
- Programming interfaces

7. Library schemas
~~~~~~~~~~~~~~~~~~
:doc:`Library schemas <07_Library_schemas>` - Domain-specific schema extensions.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- Library schema concept
- Creating library schemas
- Using library schemas
- BIDS integration

8. HED ontology
~~~~~~~~~~~~~~~
:doc:`HED ontology <08_HED_ontology>` - Ontological framework and mappings.

.. contents:: Chapter contents
   :local:
   :depth: 2

**Topics:**

- Ontological foundations
- Semantic relationships
- External ontology mappings
- Interoperability

Appendices
~~~~~~~~~~
* :doc:`Appendix A <Appendix_A>` - Additional schema information
* :doc:`Appendix B <Appendix_B>` - Error codes and validation rules

.. toctree::
   :hidden:
   :maxdepth: 3

   01_Introduction
   02_Terminology
   03_HED_formats
   04_Basic_annotation
   05_Advanced_annotation
   06_Infrastructure_and_tools
   07_Library_schemas
   08_HED_ontology
   Appendix_A
   Appendix_B
