---
title: "Security"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-troubleshooting-security
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/troubleshooting-security
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Security

[id="troubleshooting-security"]
= Security

Implementing a robust cluster security profile is important for building resilient environments.

// Module included in the following assemblies:
//
// * edge_computing/day_2_core_cnf_clusters/troubleshooting/troubleshooting-security.adoc
[id="troubleshooting-security-authentication_{context}"]
= Authentication

[role="_abstract"]
Determine which identity providers are in your cluster.
For more information about supported identity providers, see "Supported identity providers" in _Authentication and authorization_.

After you know which providers are configured, you can inspect the `openshift-authentication` namespace to determine if there are potential issues.

.Procedure

. Check the events in the `openshift-authentication` namespace by running the following command:
+
[source,terminal]
----
$ oc get events -n openshift-authentication --sort-by='.metadata.creationTimestamp'
----

. Check the pods in the `openshift-authentication` namespace by running the following command:
+
[source,terminal]
----
$ oc get pod -n openshift-authentication
----

. Optional: If you need more information, check the logs of one of the running pods by running the following command:
+
[source,terminal]
----
$ oc logs -n openshift-authentication <pod_name>
----

[role="_additional-resources"]
.Additional resources

* Supported identity providers
