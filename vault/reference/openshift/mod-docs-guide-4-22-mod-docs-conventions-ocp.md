---
title: "Modular docs OpenShift conventions"
type: reference
domain: openshift
slug: mod-docs-guide-4-22-mod-docs-conventions-ocp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/mod_docs_guide/mod-docs-conventions-ocp
version: 4.22
family: mod_docs_guide
documentKind: "Documentation"
---

# Modular docs OpenShift conventions

// Base the file name and the ID on the assembly title. For example:
// * file name: my-assembly-a.adoc
// * ID: [id="my-assembly-a"]
// * Title: = My assembly A

// Choose a context that is not too long and encapsulates what this assembly or
// module is about. Context MUST be unique across the docs set.

[id="mod-docs-ocp-references"]
= Modular docs OpenShift conventions

Before you contribute to the OpenShift docs repo, review the following modular docs conventions.

// Module included in the following assemblies:
//
// * mod_docs_guide/mod-docs-conventions-ocp.adoc

// Base the file name and the ID on the module title. For example:
// * file name: my-reference-a.adoc
// * ID: [id="my-reference-a"]
// * Title: = My reference A

[id="mod-docs-ocp-conventions_{context}"]
= Modular docs OpenShift conventions

These Modular Docs conventions for OpenShift docs build on top of the CCS
modular docs guidelines.

These guidelines and conventions should be read along with the:

* General CCS
modular docs guidelines.
* AsciiDoc markup conventions
* OpenShift Contribution Guide
* OpenShift Documentation Guidelines

IMPORTANT: If some convention is duplicated, the convention in this guide
supersedes all others.

[id="ocp-ccs-conventions_{context}"]
== OpenShift CCS conventions

* All assemblies must define a context that is unique.
+
Add this context at the top of the page, just before the first anchor id.
+
Example:
+
----
----

* All assemblies must include the `_attributes/common-attributes.adoc` file near the
context statement. This file contains the standard attributes for the collection.
+
`include::_attributes/common-attributes.adoc[leveloffset=+1]`

* All anchor ids must follow the format:
+
----
[id="<anchor-name-with-dashes>_{context}"]
----
+
Anchor name is _connected_ to the `&#123;context&#125;` using a dash.
+
Example:
+
----
[id="creating-your-first-content_{context}"]
----

* All modules anchor ids must have the `&#123;context&#125;` variable.
+
This is just reiterating the format described in the previous bullet point.

* A comment section must be present at the top of each module and assembly, as
shown in the modular docs templates.
+
The modules comment section must list which assemblies this module has been
included in, while the assemblies comment section must include other assemblies
that it itself is included in, if any.
+
Example comment section in an assembly:
+
----
// This assembly is included in the following assemblies:
//
// NONE
----
+
Example comment section in a module:
+
----
// Module included in the following assemblies:
//
// mod_docs_guide/mod-docs-conventions-ocp.adoc
----

* All modules must go in the modules directory which is present in the top level
of the openshift-docs repository. These modules must follow the file naming
conventions specified in the
modular docs guidelines.

* All assemblies must go in the relevant guide/book. If you cannot find a relevant
 guide/book, reach out to a member of the OpenShift CCS team. So guides/books contain assemblies, which
 contain modules.

* modules and images folders are symlinked to the top level folder from each book/guide folder.

* In your assemblies, when you are linking to the content in other books, you must
use the relative path starting like so:
+
----
architecture overview.
----
+
[IMPORTANT]
====
You must not include xrefs in modules or create an xref to a module. You can
only use xrefs to link from one assembly to another.
====

* All modules in assemblies must be included using the following format (replace 'ilude' with 'include'):
+
`ilude::modules/<file_name_of_module>.adoc[]`
+
_OR_
+
`ilude::modules/<file_name_of_module>.adoc[leveloffset=+<offset_by>]`
+
if it requires a leveloffset.
+
Example:
+
`include::modules/creating-your-first-content.adoc[leveloffset=+1]`

NOTE: There is no `..` at the starting of the path.

* If your assembly is in a subfolder of a guide/book directory, you must add a
statement to the assembly's metadata to use `relfileprefix`.
+
This adjusts all the xref links in your modules to start from the root
directory.
+
At the top of the assembly (in the metadata section), add the following line:
+
----
----
+
NOTE: There is a space between the second : and the ../.

+
The only difference in including a module in the _install_config/index.adoc_
assembly and _install_config/install/planning.adoc_ assembly is the addition of
the `:relfileprefix: ../` attribute at the top of the
_install_config/install/planning.adoc_ assembly. The actual inclusion of
module remains the same as described in the previous bullet.

+
NOTE: This strategy is in place so that links resolve correctly on both
docs.openshift.com and portal docs.

* Do not use 3rd level folders even though AsciiBinder permits it. If you need
to, work out a better way to organize your content.
