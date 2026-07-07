---
title: "Introduction to {hcp} in a disconnected environment"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-deploy-dc
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-deploy-dc
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Introduction to {hcp} in a disconnected environment

[id="hcp-deploy-dc"]
= Introduction to {hcp} in a disconnected environment

[role="_abstract"]
In the context of {hcp}, a disconnected environment is an OpenShift Container Platform deployment that is not connected to the internet and that uses {hcp} as a base. You can deploy {hcp} in a disconnected environment on bare metal or {VirtProductName}.

{hcp-capital} in disconnected environments function differently than in standalone OpenShift Container Platform:

* The control plane is in the management cluster. The control plane is where the pods of the hosted control plane are run and managed by the Control Plane Operator.
* The data plane is in the workers of the hosted cluster. The data plane is where the workloads and other pods run, all managed by the HostedClusterConfig Operator.

Depending on where the pods are running, they are affected by the `ImageDigestMirrorSet` (IDMS) or `ImageContentSourcePolicy` (ICSP) that is created in the management cluster or by the `ImageContentSource` that is set in the `spec` field of the manifest for the hosted cluster. The `spec` field is translated into an IDMS object on the hosted cluster.

You can deploy {hcp} in a disconnected environment on IPv4, IPv6, and dual-stack networks. IPv4 is one of the simplest network configurations to deploy {hcp} in a disconnected environment. IPv4 ranges require fewer external components than IPv6 or dual-stack setups. For {hcp} on {VirtProductName} in a disconnected environment, use either an IPv4 or a dual-stack network.
