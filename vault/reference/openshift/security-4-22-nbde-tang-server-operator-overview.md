---
title: "NBDE Tang Server Operator overview"
type: reference
domain: openshift
slug: security-4-22-nbde-tang-server-operator-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/nbde-tang-server-operator-overview
version: 4.22
family: security
documentKind: "Documentation"
---

# NBDE Tang Server Operator overview

[id="nbde-tang-server-operator-overview"]
= NBDE Tang Server Operator overview

Network-bound Disk Encryption (NBDE) provides an automated unlocking of LUKS-encrypted volumes using one or more dedicated network-binding servers. The client side of NBDE is called the Clevis decryption policy framework and the server side is represented by Tang.

The NBDE Tang Server Operator allows the automation of deployments of one or several Tang servers in the OpenShift Container Platform (OCP) environment.
