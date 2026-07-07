---
title: "Patching existing ingress objects"
type: reference
domain: openshift
slug: networking-4-22-configuring-ingress-cluster-patch-fields
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-ingress-cluster-patch-fields
version: 4.22
family: networking
documentKind: "Documentation"
---

# Patching existing ingress objects

[id="configuring-ingress-cluster-patch-fields"]
= Patching existing ingress objects

[role="_abstract"]
You can update or modify the following fields of existing `Ingress` objects without recreating the objects or disrupting services to these objects:

* Specifications
* Host
* Path
* Backend services
* SSL/TLS settings
* Annotations

// Example: Patching ingress objects with an ingressClassName
// Module included in the following assemblies:
//
// * networking/configuring_ingress_cluster_traffic/configuring-ingress-cluster-patch-fields.adoc

[id="nw-patch-fields-example_{context}"]
= Patching Ingress objects to resolve an ingressWithoutClassName alert

[role="_abstract"]
To prevent certain routing issues, you must define define the `ingressClassName` field for each `Ingress` object.

[NOTE]
====
Approximately 24 hours after you create an `Ingress` object, the Ingress Controller sends you an `ingressWithoutClassName` alert to remind you to set the `ingressClassName` field.
====

The procedure demonstrates patching the `Ingress` objects with a completed `ingressClassName` field to ensure proper routing and functionality.

.Procedure

. List all `IngressClass` objects:
+
[source,terminal]
----
$ oc get ingressclass
----

. List all `Ingress` objects in all namespaces:
+
[source,terminal]
----
$ oc get ingress -A
----

. Patch the `Ingress` object by running the following command. This command patches the `Ingress` object to include the desired ingress class name.
+
[source,terminal]
----
$ oc patch ingress/<ingress_name> --type=merge --patch '{"spec":{"ingressClassName":"openshift-default"}}'
----
* `<ingress_name>`: Replace `<ingress_name>` with the name of the `Ingress` object.
