---
title: "Viewing an egress firewall for a project"
type: reference
domain: openshift
slug: networking-4-22-viewing-egress-firewall-ovn
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/viewing-egress-firewall-ovn
version: 4.22
family: networking
documentKind: "Documentation"
---

# Viewing an egress firewall for a project

[id="viewing-egress-firewall-ovn"]
= Viewing an egress firewall for a project

[role="_abstract"]
As a cluster administrator, you can list the names of any existing egress firewalls and view the traffic rules for a specific egress firewall.

// Module included in the following assemblies:
//
// * networking/network_security/configuring-egress-firewall-ovn.adoc

[id="nw-egress-firewall-view_{context}"]
= Viewing an EgressFirewall custom resource (CR)

[role="_abstract"]
You can view an `EgressFirewall` CR in your cluster.

.Prerequisites

* A cluster using the OVN-Kubernetes network plugin.
* Install the OpenShift Command-line Interface (CLI), commonly known as `oc`.
* You must log in to the cluster.

.Procedure

. Optional: To view the names of the `EgressFirewall` CR defined in your cluster,
enter the following command:
+
[source,terminal,subs="attributes"]
----
$ oc get egressfirewall --all-namespaces
----

. To inspect a policy, enter the following command. Replace `<policy_name>` with the name of the policy to inspect.
+
[source,terminal,subs="attributes+"]
----
$ oc describe egressfirewall <policy_name>
----
+
[source,terminal]
.Example output
----
Name:		default
Namespace:	project1
Created:	20 minutes ago
Labels:		<none>
Annotations:	<none>
Rule:		Allow to 1.2.3.0/24
Rule:		Allow to www.example.com
Rule:		Deny to 0.0.0.0/0
----
