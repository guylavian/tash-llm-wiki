---
title: "Troubleshooting builds"
type: reference
domain: openshift
slug: cicd-4-22-troubleshooting-builds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/troubleshooting-builds
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Troubleshooting builds

[id="troubleshooting-builds_{context}"]
= Troubleshooting builds

Use the following to troubleshoot build issues.

// Module included in the following assemblies:
//
// * builds/troubleshooting-builds.adoc

[id="builds-troubleshooting-access-resources_{context}"]
= Resolving denial for access to resources

If your request for access to resources is denied:

Issue::
A build fails with:

[source,terminal]
----
requested access to the resource is denied
----

Resolution::
You have exceeded one of the image quotas set on your project. Check your current quota and verify the limits applied and storage in use:

[source,terminal]
----
$ oc describe quota
----

// Module included in the following assemblies:
//
// *builds/troubleshooting-builds.adoc

[id="builds-troubleshooting-service-certificate-generation_{context}"]
= Service certificate generation failure

If your request for access to resources is denied:

Issue::
If a service certificate generation fails with (service's `service.beta.openshift.io/serving-cert-generation-error` annotation contains):

.Example output
[source,terminal]
----
secret/ssl-key references serviceUID 62ad25ca-d703-11e6-9d6f-0e9c0057b608, which does not match 77b6dd80-d716-11e6-9d6f-0e9c0057b60
----

Resolution::
The service that generated the certificate no longer exists, or has a different `serviceUID`. You must force certificates regeneration by removing the old secret, and clearing the following annotations on the service: `service.beta.openshift.io/serving-cert-generation-error` and `service.beta.openshift.io/serving-cert-generation-error-num`. To clear the annotations, enter the following commands:
+
[source,terminal]
----
$ oc delete secret <secret_name>
----
+
[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-
----
+
[source,terminal]
----
$ oc annotate service <service_name> service.beta.openshift.io/serving-cert-generation-error-num-
----
+
[NOTE]
====
The command removing an annotation has a `-` after the annotation name to be
removed.
====
