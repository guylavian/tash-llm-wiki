---
title: "Understanding and managing pod security admission"
type: reference
domain: openshift
slug: authentication-4-22-understanding-and-managing-pod-security-admission
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/understanding-and-managing-pod-security-admission
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Understanding and managing pod security admission

[id="understanding-and-managing-pod-security-admission"]
= Understanding and managing pod security admission

Pod security admission is an implementation of the Kubernetes pod security standards. Use pod security admission to restrict the behavior of pods.

// About pod security admission
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc
// * operators/operator_sdk/osdk-complying-with-psa.adoc

[id="security-context-constraints-psa-about_{context}"]
= About pod security admission

OpenShift Container Platform includes Kubernetes pod security admission. Pods that do not comply with the pod security admission defined globally or at the namespace level are not admitted to the cluster and cannot run.

Globally, the `privileged` profile is enforced, and the `restricted` profile is used for warnings and audits.

You can also configure the pod security admission settings at the namespace level.

[id="psa-modes_{context}"]
== Pod security admission modes

You can configure the following pod security admission modes for a namespace:

.Pod security admission modes
[cols="1,2,3a",options="header"]
|===
|Mode
|Label
|Description

|`enforce`
|`pod-security.kubernetes.io/enforce`
|Rejects a pod from admission if it does not comply with the set profile

|`audit`
|`pod-security.kubernetes.io/audit`
|Logs audit events if a pod does not comply with the set profile

|`warn`
|`pod-security.kubernetes.io/warn`
|Displays warnings if a pod does not comply with the set profile
|===

[id="psa-profiles_{context}"]
== Pod security admission profiles

You can set each of the pod security admission modes to one of the following profiles:

.Pod security admission profiles
[cols="1,3a",options="header"]
|===
|Profile
|Description

|`privileged`
|Least restrictive policy; allows for known privilege escalation

|`baseline`
|Minimally restrictive policy; prevents known privilege escalations

|`restricted`
|Most restrictive policy; follows current pod hardening best practices
|===

[id="psa-privileged-namespaces_{context}"]
== Privileged namespaces

The following system namespaces are always set to the `privileged` pod security admission profile:

* `default`
* `kube-public`
* `kube-system`

You cannot change the pod security profile for these privileged namespaces.

.Example privileged namespace configuration

[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
    pod-security.kubernetes.io/audit: privileged
    pod-security.kubernetes.io/warn: privileged
  name: "<mig_namespace>"
# ...
----

// Understanding pod security admission coexistence
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

[id="security-context-constraints-psa-coexistence_{context}"]
= Pod security admission and security context constraints

Pod security admission standards and security context constraints are reconciled and enforced by two independent controllers. The two controllers work independently using the following processes to enforce security policies:

. The security context constraint controller may mutate some security context fields per the pod's assigned SCC. For example, if the seccomp profile is empty or not set and if the pod's assigned SCC enforces `seccompProfiles` field to be `runtime/default`, the controller sets the default type to `RuntimeDefault`.

. The security context constraint controller validates the pod's security context against the matching SCC.

. The pod security admission controller validates the pod's security context against the pod security standard assigned to the namespace.

// About pod security admission synchronization
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc
// * operators/operator_sdk/osdk-complying-with-psa.adoc

[id="security-context-constraints-psa-synchronization_{context}"]
= About pod security admission synchronization

In addition to the global pod security admission control configuration, a controller applies pod security admission control `warn` and `audit` labels to namespaces according to the SCC permissions of the service accounts that are in a given namespace.

The controller examines `ServiceAccount` object permissions to use security context constraints in each namespace. Security context constraints (SCCs) are mapped to pod security profiles based on their field values; the controller uses these translated profiles. Pod security admission `warn` and `audit` labels are set to the most privileged pod security profile in the namespace to prevent displaying warnings and logging audit events when pods are created.

Namespace labeling is based on consideration of namespace-local service account privileges.

Applying pods directly might use the SCC privileges of the user who runs the pod. However, user privileges are not considered during automatic labeling.

// Pod security admission synchronization namespace exclusions
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc
// * operators/operator_sdk/osdk-complying-with-psa.adoc

[id="security-context-constraints-psa-sync-exclusions_{context}"]
= Pod security admission synchronization namespace exclusions

Pod security admission synchronization is permanently disabled on most system-created namespaces. Synchronization is also initially disabled on user-created `openshift-*` prefixed namespaces, but you can enable synchronization on them later.

Pod security admission synchronization is permanently disabled on system-created namespaces and `openshift-*` prefixed namespaces.

[IMPORTANT]
====
If a pod security admission label (`pod-security.kubernetes.io/<mode>`) is manually modified from the automatically labeled value on a label-synchronized namespace, synchronization is disabled for that label.

If necessary, you can enable synchronization again by using one of the following methods:

* By removing the modified pod security admission label from the namespace
* By setting the `security.openshift.io/scc.podSecurityLabelSync` label to `true`
+
If you force synchronization by adding this label, then any modified pod security admission labels will be overwritten.
====

== Permanently disabled namespaces

Namespaces that are defined as part of the cluster payload have pod security admission synchronization disabled permanently. The following namespaces are permanently disabled:

* `default`
* `kube-node-lease`
* `kube-system`
* `kube-public`
* `openshift`
* All system-created namespaces that are prefixed with `openshift-`
, except for `openshift-operators`

== Initially disabled namespaces

By default, all namespaces that have an `openshift-` prefix have pod security admission synchronization disabled initially. You can enable synchronization for user-created [x-]`openshift-*` namespaces and for the `openshift-operators` namespace.

[NOTE]
====
You cannot enable synchronization for any system-created [x-]`openshift-*` namespaces, except for `openshift-operators`.
====

If an Operator is installed in a user-created `openshift-*` namespace, synchronization is enabled automatically after a cluster service version (CSV) is created in the namespace. The synchronized label is derived from the permissions of the service accounts in the namespace.

// Controlling pod security admission synchronization
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

[id="security-context-constraints-psa-opting_{context}"]
= Controlling pod security admission synchronization

You can enable or disable automatic pod security admission synchronization for most namespaces.

[IMPORTANT]
====
You cannot enable pod security admission synchronization on
some
system-created namespaces. For more information, see _Pod security admission synchronization namespace exclusions_.
====

.Procedure

* For each namespace that you want to configure, set a value for the `security.openshift.io/scc.podSecurityLabelSync` label:
+
--
** To disable pod security admission label synchronization in a namespace, set the value of the `security.openshift.io/scc.podSecurityLabelSync` label to `false`.
+
Run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace> security.openshift.io/scc.podSecurityLabelSync=false
----

** To enable pod security admission label synchronization in a namespace, set the value of the `security.openshift.io/scc.podSecurityLabelSync` label to `true`.
+
Run the following command:
+
[source,terminal]
----
$ oc label namespace <namespace> security.openshift.io/scc.podSecurityLabelSync=true
----
--
+
[NOTE]
====
Use the `--overwrite` flag to overwrite the value if this label is already set on the namespace.
====

.Additional resources

* Pod security admission synchronization namespace exclusions

// Configuring pod security admission for a namespace
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

[id="security-context-constraints-psa-label_{context}"]
=  Configuring pod security admission for a namespace

You can configure the pod security admission settings at the namespace level. For each of the pod security admission modes on the namespace, you can set which pod security admission profile to use.

.Procedure

* For each pod security admission mode that you want to set on a namespace, run the following command:

+
[source,terminal]
----
$ oc label namespace <namespace> \                <1>
    pod-security.kubernetes.io/<mode>=<profile> \ <2>
    --overwrite
----
<1> Set `<namespace>` to the namespace to configure.
<2> Set `<mode>` to `enforce`, `warn`, or `audit`. Set `<profile>` to `restricted`, `baseline`, or `privileged`.

// About pod security admission alerts
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

[id="security-context-constraints-psa-rectifying_{context}"]
= About pod security admission alerts

A `PodSecurityViolation` alert is triggered when the Kubernetes API server reports that there is a pod denial on the audit level of the pod security admission controller. This alert persists for one day.

View the Kubernetes API server audit logs to investigate alerts that were triggered. As an example, a workload is likely to fail admission if global enforcement is set to the `restricted` pod security level.

For assistance in identifying pod security admission violation audit events, see Audit annotations in the Kubernetes documentation.

// OSD and ROSA dedicated-admin users cannot use the must-gather tool.
// Identifying pod security violations
// Module included in the following assemblies:
//
// * authentication/understanding-and-managing-pod-security-admission.adoc

[id="security-context-constraints-psa-alert-eval_{context}"]
= Identifying pod security violations

The `PodSecurityViolation` alert does not provide details on which workloads are causing pod security violations. You can identify the affected workloads by reviewing the Kubernetes API server audit logs. This procedure uses the `must-gather` tool to gather the audit logs and then searches for the `pod-security.kubernetes.io/audit-violations` annotation.

.Prerequisites

* You have installed `jq`.
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. To gather the audit logs, enter the following command:
+
[source,terminal]
----
$ oc adm must-gather -- /usr/bin/gather_audit_logs
----

. To output the affected workload details, enter the following command:
+
[source,terminal]
----
$ zgrep -h pod-security.kubernetes.io/audit-violations must-gather.local.<archive_id>/<image_digest_id>/audit_logs/kube-apiserver/*log.gz \
  | jq -r 'select((.annotations["pod-security.kubernetes.io/audit-violations"] != null) and (.objectRef.resource=="pods")) | .objectRef.namespace + " " + .objectRef.name' \
  | sort | uniq -c
----
+
Replace `<archive_id>` and `<image_digest_id>` with the actual path names.
+
.Example output
[source,text]
----
1 test-namespace my-pod
----

[role="_additional-resources"]
[id="additional-resources_managing-pod-security-admission"]
== Additional resources

// Module not included in the HCP distro
* Viewing audit logs
* Managing security context constraints
