---
title: "Custom domains for Knative services using the Knative CLI"
type: reference
domain: openshift
slug: serverless-4-22-create-domain-mapping-kn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/create-domain-mapping-kn
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Custom domains for Knative services using the Knative CLI

[id="create-domain-mapping-kn"]
= Custom domains for Knative services using the Knative CLI

You can customize the domain for your Knative service by mapping a custom domain name that you own to a Knative service. You can use the Knative (`kn`) CLI to create a `DomainMapping` custom resource (CR) that maps to an Addressable target CR, such as a Knative service or a Knative route.

// Module included in the following assemblies:
//
// * serverless/security/serverless-custom-domains.adoc
// * serverless/reference/kn-serving-ref.adoc

[id="serverless-create-domain-mapping-kn_{context}"]
= Creating a custom domain mapping by using the Knative CLI

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have created a Knative service or route, and control a custom domain that you want to map to that CR.
+
[NOTE]
====
Your custom domain must point to the DNS of the OpenShift Container Platform cluster.
====
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Map a domain to a CR in the current namespace:
+
[source,terminal]
----
$ kn domain create <domain_mapping_name> --ref <target_name>
----
+
.Example command
[source,terminal]
----
$ kn domain create example-domain-map --ref example-service
----
+
The `--ref` flag specifies an Addressable target CR for domain mapping.
+
If a prefix is not provided when using the `--ref` flag, it is assumed that the target is a Knative service in the current namespace.

* Map a domain to a Knative service in a specified namespace:
+
[source,terminal]
----
$ kn domain create <domain_mapping_name> --ref <ksvc:service_name:service_namespace>
----
+
.Example command
[source,terminal]
----
$ kn domain create example-domain-map --ref ksvc:example-service:example-namespace
----

* Map a domain to a Knative route:
+
[source,terminal]
----
$ kn domain create <domain_mapping_name> --ref <kroute:route_name>
----
+
.Example command
[source,terminal]
----
$ kn domain create example-domain-map --ref kroute:example-route
----
