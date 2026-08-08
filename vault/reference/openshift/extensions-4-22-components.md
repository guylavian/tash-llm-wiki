---
title: "{olmv1} components overview"
type: reference
domain: openshift
slug: extensions-4-22-components
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/components
version: 4.22
family: extensions
documentKind: "Documentation"
---

# {olmv1} components overview

[id="olm-components"]
= {olmv1} components overview

{olmv1-first} comprises the following component projects:

Operator Controller:: Operator Controller is the central component of {olmv1} that extends Kubernetes with an API through which users can install and manage the lifecycle of Operators and extensions. It consumes information from catalogd.

Catalogd:: Catalogd is a Kubernetes extension that unpacks file-based catalog (FBC) content packaged and shipped in container images for consumption by on-cluster clients. As a component of the {olmv1} microservices architecture, catalogd hosts metadata for Kubernetes extensions packaged by the authors of the extensions, and as a result helps users discover installable content.
