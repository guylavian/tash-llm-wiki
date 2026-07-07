---
title: "Pod security authentication and authorization with SCC"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-authentication
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-authentication
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Pod security authentication and authorization with SCC

[id="authentication-with-microshift"]
= Pod security authentication and authorization with SCC

[role="_abstract"]
Pod security admission is an implementation of the Kubernetes pod security standards. Use security content constraints (SCC) for pod security admission to restrict pod behavior.

// Module included in the following assemblies:
//
// * microshift_running_apps/microshift-authentication.adoc

[id="microshift-security-context-constraints_{context}"]

= Security context constraint synchronization with pod security standards

[role="_abstract"]
{microshift-short} includes Kubernetes pod security admission (PSA) and a controller that applies PSA labels to namespaces based on the security context constraint (SCC) permissions of service accounts in that namespace.

[IMPORTANT]
====
Namespaces that are defined as part of the node payload have pod security admission synchronization disabled permanently. You can enable pod security admission synchronization on other namespaces as necessary. If an Operator is installed in a user-created `openshift-*` namespace, synchronization is turned on by default after a cluster service version (CSV) is created in the namespace.
====

The controller examines `ServiceAccount` object permissions to use security context constraints in each namespace. Security context constraints (SCCs) are mapped to pod security profiles based on their field values; the controller uses these translated profiles. Pod security admission `warn` and `audit` labels are set to the most privileged pod security profile found in the namespace to prevent warnings and audit logging as pods are created.

Namespace labeling is based on consideration of namespace-local service account privileges.

Applying pods directly might use the SCC privileges of the user who runs the pod. However, user privileges are not considered during automatic labeling.

[role="_additional-resources"]
.Additional resources
* Kubernetes pod security

* Kubernetes pod security admission

// Module included in the following assemblies:
//
// * microshift_running_apps/microshift-authentication.adoc

[id="microshift-viewing-security-context_{context}"]
= Viewing security context constraints in a namespace

[role="_abstract"]
You can view and check the security context constraints (SCC) permissions in a given namespace using the OpenShift CLI (`oc`).

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

.Procedure

* To view the security context constraints in your namespace, run the following command:
+
[source,terminal]
----
$ oc get --show-labels namespace <namespace>
----

// Module included in the following assemblies:
//
// * microshift_running_apps/microshift-authentication.adoc

[id="microshift-security-context-constraints-opting_{context}"]
= Controlling pod security admission synchronization

[role="_abstract"]
You can enable automatic pod security admission synchronization for most namespaces.

System defaults are not enforced when the `security.openshift.io/scc.podSecurityLabelSync` field is empty or set to `false`. You must set the label to `true` for synchronization to occur. You can use the `--overwrite` flag to reverse the effects of the pod security label synchronization in a namespace.

[IMPORTANT]
====
Namespaces that are defined as part of the node payload have pod security admission synchronization disabled permanently. These namespaces include:

* `default`
* `kube-node-lease`
* `kube-system`
* `kube-public`
* `openshift`
* All system-created namespaces that are prefixed with `openshift-`, except for `openshift-operators`
By default, all namespaces that have an `openshift-` prefix are not synchronized. You can enable synchronization for any user-created [x-]`openshift-*` namespaces. You cannot enable synchronization for any system-created [x-]`openshift-*` namespaces, except for `openshift-operators`.

If an Operator is installed in a user-created `openshift-*` namespace, synchronization is turned on by default after a node service version (CSV) is created in the namespace. The synchronized label inherits the permissions of the service accounts in the namespace.
====

.Procedure

* To enable pod security admission label synchronization in a namespace, set the value of the `security.openshift.io/scc.podSecurityLabelSync` label to `true` by running the following command:
+
[source,terminal]
----
$ oc label namespace <namespace> security.openshift.io/scc.podSecurityLabelSync=true
----
