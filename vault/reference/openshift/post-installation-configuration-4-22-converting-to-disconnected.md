---
title: "Converting a connected cluster to a disconnected cluster"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-converting-to-disconnected
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/converting-to-disconnected
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Converting a connected cluster to a disconnected cluster

[id="converting-to-disconnected"]
= Converting a connected cluster to a disconnected cluster

There might be some scenarios where you need to convert your OpenShift Container Platform cluster from a connected cluster to a disconnected cluster.

A disconnected cluster, also known as a restricted cluster, does not have an active connection to the internet. As such, you must mirror the contents of your registries and installation media. You can create this mirror registry on a host that can access both the internet and your closed network, or copy images to a device that you can move across network boundaries.

For information on how to convert your cluster, see the Converting a connected cluster to a disconnected cluster procedure in the Disconnected environments section.
