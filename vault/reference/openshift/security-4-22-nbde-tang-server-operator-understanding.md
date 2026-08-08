---
title: "Understanding the NBDE Tang Server Operator"
type: reference
domain: openshift
slug: security-4-22-nbde-tang-server-operator-understanding
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/nbde-tang-server-operator-understanding
version: 4.22
family: security
documentKind: "Documentation"
---

# Understanding the NBDE Tang Server Operator

[id="understanding-nbde-tang-server-operator"]
= Understanding the NBDE Tang Server Operator

You can use the NBDE Tang Server Operator to automate the deployment of a Tang server in an OpenShift Container Platform cluster that requires Network Bound Disk Encryption (NBDE) internally, leveraging the tools that OpenShift Container Platform provides to achieve this automation.

The NBDE Tang Server Operator simplifies the installation process and uses native features provided by the OpenShift Container Platform environment, such as multi-replica deployment, scaling, traffic load balancing, and so on. The Operator also provides automation of certain operations that are error-prone when you perform them manually, for example:

* server deployment and configuration
* key rotation
* hidden keys deletion

The NBDE Tang Server Operator is implemented using the Operator SDK and allows the deployment of one or more Tang servers in OpenShift through custom resource definitions (CRDs).

[id="understanding-nbde-tang-server-operator_additional-resources"]
[role="_additional-resources"]
== Additional resources
* Tang-Operator: Providing NBDE in OpenShift
* Tang Server Operator
* Configuring automated unlocking of encrypted volumes using policy-based decryption
