---
title: "Troubleshooting networking"
type: reference
domain: openshift
slug: support-4-22-rosa-troubleshooting-networking
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/rosa-troubleshooting-networking
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting networking

[id="rosa-troubleshooting-networking"]
= Troubleshooting networking

[role="_abstract"]
Troubleshoot networking errors by completing the following instructions.

// Module included in the following assemblies:
//
// * support/rosa-troubleshooting-deployments.adoc
[id="rosa-troubleshooting-general-deployment-failure_{context}"]
= Connectivity issues on clusters with private network load balancers

[role="_abstract"]
OpenShift Container Platform clusters created with version  deploy AWS Network Load Balancers (NLB) by default for the `default` ingress controller. In the case of a private NLB, the NLB client IP address preservation might drop connections where the source and destination are the same host. See the AWS documentation about how to Troubleshoot your Network Load Balancer. This IP address preservation means that customer workloads co-located on the same node with the router pods might not be able to send traffic to the private NLB fronting the ingress controller router.

.Procedure

* To mitigate this impact, reschedule your workloads onto nodes separate from those where the router pods run. Or, rely on the internal pod and service networks for accessing other workloads co-located within the same cluster.
