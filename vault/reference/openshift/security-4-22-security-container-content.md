---
title: "Securing container content"
type: reference
domain: openshift
slug: security-4-22-security-container-content
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/security-container-content
version: 4.22
family: security
documentKind: "Documentation"
---

# Securing container content

[id="security-container-content"]
= Securing container content

To ensure the security of the content inside your containers
you need to start with trusted base images, such as Red Hat
Universal Base Images, and add trusted software. To check the
ongoing security of your container images, there are both
Red Hat and third-party tools for scanning images.

// Security inside the container
// Module included in the following assemblies:
//
// * security/container_security/security-container-content.adoc

[id="security-container-content-inside_{context}"]
= Securing inside the container

Applications and infrastructures are composed of readily available components,
many of which are open source packages such as, the Linux operating system,
JBoss Web Server, PostgreSQL, and Node.js.

Containerized versions of these packages are also available. However, you need
to know where the packages originally came from, what versions are used, who built them, and whether
there is any malicious code inside them.

Some questions to answer include:

* Will what is inside the containers compromise your infrastructure?
* Are there known vulnerabilities in the application layer?
* Are the runtime and operating system layers current?

By building your containers from Red Hat
Universal Base Images (UBI) you are
assured of a foundation for your container images that consists of
the same RPM-packaged software that is included in Red Hat Enterprise Linux.
No subscriptions are required to either use or redistribute UBI images.

To assure ongoing security of the containers themselves, security
scanning features, used directly from {op-system-base} or added to OpenShift Container Platform,
can alert you when
an image you are using has vulnerabilities. OpenSCAP image scanning is
available in {op-system-base} and the
{rhq-cso} can be added
to check container images used in OpenShift Container Platform.

// Red Hat Universal Base Images
// Module included in the following assemblies:
//
// * security/container_security/security-container-content.adoc

[id="security-container-content-universal_{context}"]
= Creating redistributable images with UBI

To create containerized applications, you typically start with a trusted base
image that offers the components that are usually provided by the operating system.
These include the libraries, utilities, and other features the application
expects to see in the operating system's file system.

Red{nbsp}Hat Universal Base Images (UBI) were created to encourage anyone building their
own containers to start with one that is made entirely from Red{nbsp}Hat Enterprise
Linux rpm packages and other content. These UBI images are updated regularly
to keep up with security patches and free to use and redistribute with
container images built to include your own software.

Search the
Red Hat Ecosystem Catalog
to both find and check the health of different UBI images.
As someone creating secure container images, you might
be interested in these two general types of UBI images:

* **UBI**: There are standard UBI images for RHEL 7, 8, and 9 (`ubi7/ubi`,
`ubi8/ubi`, and `ubi9/ubi`), as well as minimal images based on those systems (`ubi7/ubi-minimal`, `ubi8/ubi-mimimal`, and ubi9/ubi-minimal). All of these images are preconfigured to point to free
repositories of {op-system-base} software that you can add to the container images you build,
using standard `yum` and `dnf` commands.
+
[NOTE]
====
Red{nbsp}Hat encourages people to use these images on other distributions,
such as Fedora and Ubuntu.
====

* **Red{nbsp}Hat Software Collections**: Search the Red{nbsp}Hat Ecosystem Catalog
for `rhscl/` to find images created to use as base images for specific types
of applications. For example, there are Apache httpd ([x-]`rhscl/httpd-*`),
Python ([x-]`rhscl/python-*`), Ruby ([x-]`rhscl/ruby-*`), Node.js
([x-]`rhscl/nodejs-*`) and Perl ([x-]`rhscl/perl-*`) rhscl images.

Keep in mind that while UBI images are freely available and redistributable,
Red{nbsp}Hat support for these images is only available through Red{nbsp}Hat
product subscriptions.

See
Using Red{nbsp}Hat Universal Base Images
in the Red Hat Enterprise Linux documentation for information on how to use and build on
standard, minimal and init UBI images.

// Container content scanning
// Module included in the following assemblies:
//
// * security/container_security/security-container-content.adoc

[id="security-container-content-scanning_{context}"]
= Security scanning in {op-system-base}

For {op-system-base-full} systems, OpenSCAP scanning is available
from the `openscap-utils` package. In {op-system-base}, you can use the `openscap-podman`
command to scan images for vulnerabilities. See
Scanning containers and container images for vulnerabilities in the Red Hat Enterprise Linux documentation.

OpenShift Container Platform enables you to leverage {op-system-base} scanners with your CI/CD process.
For example, you can integrate static code analysis tools that test for security
flaws in your source code and software composition analysis tools that identify
open source libraries to provide metadata on those libraries such as
known vulnerabilities.

[id="quay-security-scan_{context}"]
== Scanning OpenShift images

For the container images that are running in OpenShift Container Platform
and are pulled from {quay} registries, you can use an Operator to list the
vulnerabilities of those images. The
{rhq-cso}
can be added to OpenShift Container Platform to provide vulnerability reporting
for images added to selected namespaces.

Container image scanning for {quay} is performed by the
Clair.
In {quay}, Clair can search for and report vulnerabilities in
images built from {op-system-base}, CentOS, Oracle, Alpine, Debian, and Ubuntu
operating system software.

// Integrating external scanning tools with OpenShift
// Module included in the following assemblies:
//
// * security/container_security/security-container-content.adoc

[id="security-container-content-external-scanning_{context}"]
= Integrating external scanning

OpenShift Container Platform makes use of object annotations
to extend functionality. External tools, such as vulnerability scanners, can
annotate image objects with metadata to summarize results and control pod
execution. This section describes the recognized format of this annotation so it
can be reliably used in consoles to display useful data to users.

[id="security-image-metadata_{context}"]
== Image metadata

There are different types of image quality data, including package
vulnerabilities and open source software (OSS) license compliance. Additionally,
there may be more than one provider of this metadata. To that end, the following
annotation format has been reserved:

----
quality.images.openshift.io/<qualityType>.<providerId>: {}
----

.Annotation key format
[option="header"]
|===
|Component |Description |Acceptable values

|`qualityType`
|Metadata type
|`vulnerability` +
`license` +
`operations` +
`policy`

|`providerId`
|Provider ID string
|`openscap` +
`redhatcatalog` +
`redhatinsights` +
`blackduck` +
`jfrog`
|===

[id="security-example-annotation-keys_{context}"]
=== Example annotation keys

----
quality.images.openshift.io/vulnerability.blackduck: {}
quality.images.openshift.io/vulnerability.jfrog: {}
quality.images.openshift.io/license.blackduck: {}
quality.images.openshift.io/vulnerability.openscap: {}
----

The value of the image quality annotation is structured data that must adhere to
the following format:

.Annotation value format
[option="header"]
|===
|Field |Required? |Description |Type

|`name`
|Yes
|Provider display name
|String

|`timestamp`
|Yes
|Scan timestamp
|String

|`description`
|No
|Short description
|String
|`reference`
|Yes
|URL of information source or more details. Required so user may validate the data.
|String

|`scannerVersion`
|No
|Scanner version
|String

|`compliant`
|No
|Compliance pass or fail
|Boolean

|`summary`
|No
|Summary of issues found
|List (see table below)
|===

The `summary` field must adhere to the following format:

.Summary field value format
[option="header"]
|===
|Field |Description |Type

|`label`
|Display label for component (for example, "critical," "important," "moderate,"
"low," or "health")
|String

|`data`
|Data for this component (for example, count of vulnerabilities found or score)
|String

|`severityIndex`
|Component index allowing for ordering and assigning graphical
representation. The value is range `0..3` where `0` = low.
|Integer

|`reference`
|URL of information source or more details. Optional.
|String
|===

[id="security-example-annotation-values_{context}"]
=== Example annotation values

This example shows an OpenSCAP annotation for an image with
vulnerability summary data and a compliance boolean:

.OpenSCAP annotation
[source,json]
----
{
  "name": "OpenSCAP",
  "description": "OpenSCAP vulnerability score",
  "timestamp": "2016-09-08T05:04:46Z",
  "reference": "https://www.open-scap.org/930492",
  "compliant": true,
  "scannerVersion": "1.2",
  "summary": [
    { "label": "critical", "data": "4", "severityIndex": 3, "reference": null },
    { "label": "important", "data": "12", "severityIndex": 2, "reference": null },
    { "label": "moderate", "data": "8", "severityIndex": 1, "reference": null },
    { "label": "low", "data": "26", "severityIndex": 0, "reference": null }
  ]
}
----

This example shows the
Container images section of the Red Hat Ecosystem Catalog
annotation for an image with health index data
with an external URL for additional details:

.Red Hat Ecosystem Catalog annotation
[source,json]
----
{
  "name": "Red Hat Ecosystem Catalog",
  "description": "Container health index",
  "timestamp": "2016-09-08T05:04:46Z",
  "reference": "https://access.redhat.com/errata/RHBA-2016:1566",
  "compliant": null,
  "scannerVersion": "1.2",
  "summary": [
    { "label": "Health index", "data": "B", "severityIndex": 1, "reference": null }
  ]
}
----

[id="security-annotating-image-objects_{context}"]
== Annotating image objects

While image stream objects
are what an end user of OpenShift Container Platform operates against,
image objects are annotated with
security metadata. Image objects are cluster-scoped, pointing to a single image
that may be referenced by many image streams and tags.

[id="security-example-annotate-CLI_{context}"]
=== Example annotate CLI command

Replace `<image>` with an image digest, for example
`sha256:401e359e0f45bfdcf004e258b72e253fd07fba8cc5c6f2ed4f4608fb119ecc2`:

[source,terminal]
----
$ oc annotate image <image> \
    quality.images.openshift.io/vulnerability.redhatcatalog='{ \
    "name": "Red Hat Ecosystem Catalog", \
    "description": "Container health index", \
    "timestamp": "2020-06-01T05:04:46Z", \
    "compliant": null, \
    "scannerVersion": "1.2", \
    "reference": "https://access.redhat.com/errata/RHBA-2020:2347", \
    "summary": "[ \
      { "label": "Health index", "data": "B", "severityIndex": 1, "reference": null } ]" }'
----

[id="controlling-pod-execution_{context}"]
== Controlling pod execution

Use the `images.openshift.io/deny-execution` image policy
to programmatically control if an image can be run.

[id="security-controlling-pod-execution-example-annotation_{context}"]
=== Example annotation

[source,yaml]
----
annotations:
  images.openshift.io/deny-execution: true
----

[id="security-integration-reference_{context}"]
== Integration reference

In most cases, external tools such as vulnerability scanners develop a
script or plugin that watches for image updates, performs scanning, and
annotates the associated image object with the results. Typically this
automation calls the OpenShift Container Platform  REST APIs to write the annotation. See
OpenShift Container Platform REST APIs for general
information on the REST APIs.

[id="security-integration-reference-example-api-call_{context}"]
=== Example REST API call

The following example call using `curl` overrides the value of the
annotation. Be sure to replace the values for `<token>`, `<openshift_server>`,
`<image_id>`, and `<image_annotation>`.

.Patch API call
[source,terminal]
----
$ curl -X PATCH \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/merge-patch+json" \
  https://<openshift_server>:6443/apis/image.openshift.io/v1/images/<image_id> \
  --data '{ <image_annotation> }'
----

The following is an example of `PATCH` payload data:

.Patch call data
[source,terminal]
----
{
"metadata": {
  "annotations": {
    "quality.images.openshift.io/vulnerability.redhatcatalog":
       "{ 'name': 'Red Hat Ecosystem Catalog', 'description': 'Container health index', 'timestamp': '2020-06-01T05:04:46Z', 'compliant': null, 'reference': 'https://access.redhat.com/errata/RHBA-2020:2347', 'summary': [{'label': 'Health index', 'data': '4', 'severityIndex': 1, 'reference': null}] }"
    }
  }
}
----

[NOTE]
====
Due to the complexity of this API call and challenges with escaping characters,
an API developer tool such as Postman may
assist in creating API calls.
====

[role="_additional-resources"]
.Additional resources
* Image stream objects
// * OpenShift Container Platform  REST APIs
