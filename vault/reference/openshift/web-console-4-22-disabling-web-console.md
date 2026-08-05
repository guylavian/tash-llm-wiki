---
title: "Disabling the web console in {product-title}"
type: reference
domain: openshift
slug: web-console-4-22-disabling-web-console
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/disabling-web-console
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Disabling the web console in {product-title}

[id="disabling-web-console"]
= Disabling the web console in OpenShift Container Platform

[role="_abstract"]
You can disable the OpenShift Container Platform web console.

== Prerequisites

* Deploy
an OpenShift Container Platform
a {rosa-short}
a {rosa-classic-short}
cluster.

// Module included in the following assemblies:
//
// * web_console/disabling-web-console.adoc

[id="web-console-disable_{context}"]
= Disabling the web console

[role="_abstract"]
You can disable the web console by editing the `consoles.operator.openshift.io` resource.

.Procedure
* Edit the `consoles.operator.openshift.io` resource:
+
[source,terminal]
----
$ oc edit consoles.operator.openshift.io cluster
----
+
The following example displays the parameters from this resource that you can
modify:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  managementState: Removed
----
+
--
where:

`spec.managementState.Removed`:: Set the `managementState` parameter value to `Removed` to disable the web console. The other valid values for this parameter are `Managed`, which enables the console under the cluster's control, and `Unmanaged`, which means that you are taking control of web console management.
--
