---
title: "Catalogd"
type: reference
domain: openshift
slug: extensions-4-22-catalogd
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/catalogd
version: 4.22
family: extensions
documentKind: "Documentation"
---

# Catalogd

[id="catalogd"]
= Catalogd

{olmv1-first} uses the catalogd component and its resources to manage Operator and extension catalogs.

// Module included in the following assemblies:
//
// * operators/olm_v1/olmv1-installing-an-operator-from-a-catalog.adoc
// * operators/olm_v1/arch/olmv1-catalogd.adoc
// * extensions/arch/olmv1-catalogd.adoc

[id="olmv1-about-catalogs_{context}"]
= About catalogs in {olmv1}

You can discover installable content by querying a catalog for Kubernetes extensions, such as Operators and controllers, by using the catalogd component. Catalogd is a Kubernetes extension that unpacks catalog content for on-cluster clients and is part of the {olmv1-first} suite of microservices. Currently, catalogd unpacks catalog content that is packaged and distributed as container images.

[role="_additional-resources"]
.Additional resources
* File-based catalogs
* Adding a catalog to a cluster
* Red Hat-provided catalogs
