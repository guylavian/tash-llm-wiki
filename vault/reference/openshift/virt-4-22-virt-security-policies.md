---
title: "Security policies"
type: reference
domain: openshift
slug: virt-4-22-virt-security-policies
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-security-policies
version: 4.22
family: virt
documentKind: "Documentation"
---

# Security policies

[id="virt-security-policies"]
= Security policies

[role="_abstract"]
{VirtProductName} provides built-in security features and authorization policies to protect virtual machine workloads and ensure secure cluster operations across your environment.

*Key points*

* {VirtProductName} adheres to the `restricted` Kubernetes pod security standards profile, which aims to enforce the current best practices for pod security.
* Virtual machine (VM) workloads run as unprivileged pods.
* Security context constraints (SCCs) are defined for the `kubevirt-controller` service account. For more information about SSCs, see "Additional resources".
* TLS certificates for {VirtProductName} components are renewed and rotated automatically.

// Module included in the following assemblies:
//
// * virt/virt-security-policies.adoc

[id="virt-about-workload-security_{context}"]
= About workload security

[role="_abstract"]
By default, virtual machine (VM) workloads do not run with root privileges in {VirtProductName}, and there are no supported {VirtProductName} features that require root privileges.

For each VM, a `virt-launcher` pod runs an instance of `libvirt` in _session mode_ to manage the VM process. In session mode, the `libvirt` daemon runs as a non-root user account and only permits connections from clients that are running under the same user identifier (UID). Therefore, VMs run as unprivileged pods, adhering to the security principle of least privilege.

// Module included in the following assemblies:
//
// * virt/about_virt/virt-security-policies.adoc

[id="virt-automatic-certificates-renewal_{context}"]
= TLS certificates

[role="_abstract"]
TLS certificates for {VirtProductName} components are renewed and rotated automatically. You are not required to refresh them manually.

== Automatic renewal schedules

TLS certificates are automatically deleted and replaced according to the following schedule:

* KubeVirt certificates are renewed daily.

* Containerized Data Importer controller (CDI)
 certificates are renewed every 15 days.
* MAC pool certificates are renewed every year.
Automatic TLS certificate rotation does not disrupt any operations. For example, the following operations continue to function without any disruption:

* Migrations

* Image uploads

* VNC and console connections

// Module included in the following assemblies:
//
// * virt/about_virt/virt-security-policies.adoc

[id="virt-security-policies-auth_{context}"]
= Authorization

[role="_abstract"]
{VirtProductName} uses role-based access control (RBAC) to define permissions for human users and service accounts. The permissions defined for service accounts control the actions that {VirtProductName} components can perform.

You can also use RBAC roles to manage user access to virtualization features. For example, an administrator can create an RBAC role that provides the permissions required to launch a virtual machine. The administrator can then restrict access by binding the role to specific users.

// Module included in the following assemblies:
//
// * virt/about_virt/virt-security-policies.adoc

[id="default-cluster-roles-for-virt_{context}"]
= Default cluster roles for {VirtProductName}

[role="_abstract"]
By using cluster role aggregation, {VirtProductName} extends the default OpenShift Container Platform cluster roles to include permissions for accessing virtualization objects. Roles unique to {VirtProductName} are not aggregated with OpenShift Container Platform roles.

.{VirtProductName} cluster roles
[cols="1,1,4",options="header"]
|===
|Default cluster role
|{VirtProductName} cluster role
|{VirtProductName} cluster role description

.^| `view`
.^|`kubevirt.io:view`
| A user that can view all {VirtProductName} resources in the cluster but cannot create, delete, modify, or access them. For example, the user can see that a virtual machine (VM) is running but cannot shut it down or gain access to its console.

.^| `edit`
.^|`kubevirt.io:edit`
| A user that can modify all {VirtProductName} resources in the cluster. For example, the user can create VMs, access VM consoles, and delete VMs.

.^| `admin`
.^|`kubevirt.io:admin`
| A user that has full permissions to all {VirtProductName} resources, including the ability to delete collections of resources. The user can also view and modify the {VirtProductName} runtime configuration, which is located in the `HyperConverged` custom resource in the `openshift-cnv` namespace.

.^| `N/A`
.^|`kubevirt.io:migrate`
| A user that can create, delete, and update VM live migration requests, which are represented by namespaced `VirtualMachineInstanceMigration` (VMIM) objects. This role is specific to {VirtProductName}.
|===

// Module included in the following assemblies:
//
// * virt/about_virt/virt-security-policies.adoc

[id="virt-storage-rbac-roles_{context}"]
= RBAC roles for storage features in {VirtProductName}

[role="_abstract"]
The following permissions are granted to the Containerized Data Importer (CDI), including the `cdi-operator` and `cdi-controller` service accounts.

[id="cluster-wide-rbac-roles-cdi"]
== Cluster-wide RBAC roles

.Aggregated cluster roles for the `cdi.kubevirt.io` API group
[cols="1,2,1",options="header"]
|===
| CDI cluster role
| Resources
| Verbs

.2+.^| `cdi.kubevirt.io:admin`
.^| `datavolumes`, `uploadtokenrequests`
.^| `*` (all)

.^| `datavolumes/source`
.^| `create`

.2+.^| `cdi.kubevirt.io:edit`
.^| `datavolumes`, `uploadtokenrequests`
.^| `*`

.^| `datavolumes/source`
.^| `create`

.2+.^| `cdi.kubevirt.io:view`
.^| `cdiconfigs`, `dataimportcrons`, `datasources`, `datavolumes`, `objecttransfers`, `storageprofiles`, `volumeimportsources`, `volumeuploadsources`, `volumeclonesources`
.^| `get`, `list`, `watch`

.^| `datavolumes/source`
.^| `create`

.^| `cdi.kubevirt.io:config-reader`
.^| `cdiconfigs`, `storageprofiles`
.^| `get`, `list`, `watch`
|===

.Cluster-wide roles for the `cdi-operator` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `rbac.authorization.k8s.io`
.^| `clusterrolebindings`, `clusterroles`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `security.openshift.io`
.^| `securitycontextconstraints`
.^| `get`, `list`, `watch`, `update`, `create`

.^| `apiextensions.k8s.io`
.^| `customresourcedefinitions`, `customresourcedefinitions/status`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `cdi.kubevirt.io`
.^| `*`
.^| `*`

.^| `upload.cdi.kubevirt.io`
.^| `*`
.^| `*`

.^| `admissionregistration.k8s.io`
.^| `validatingwebhookconfigurations`, `mutatingwebhookconfigurations`
.^| `create`, `list`, `watch`

.^| `admissionregistration.k8s.io`
.^| `validatingwebhookconfigurations`

Allow list: `cdi-api-dataimportcron-validate, cdi-api-populator-validate, cdi-api-datavolume-validate, cdi-api-validate, objecttransfer-api-validate`
.^| `get`, `update`, `delete`

.^| `admissionregistration.k8s.io`
.^| `mutatingwebhookconfigurations`

Allow list: `cdi-api-datavolume-mutate`
.^| `get`, `update`, `delete`

.^| `apiregistration.k8s.io`
.^| `apiservices`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`
|===

.Cluster-wide roles for the `cdi-controller` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `""` (core)
.^| `events`
.^| `create`, `patch`

.^| `""` (core)
.^| `persistentvolumeclaims`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`, `deletecollection`, `patch`

.^| `""` (core)
.^| `persistentvolumes`
.^| `get`, `list`, `watch`, `update`

.^| `""` (core)
.^| `persistentvolumeclaims/finalizers`, `pods/finalizers`
.^| `update`

.^| `""` (core)
.^| `pods`, `services`
.^| `get`, `list`, `watch`, `create`, `delete`

.^| `""` (core)
.^| `configmaps`
.^| `get`, `create`

.^| `storage.k8s.io`
.^| `storageclasses`, `csidrivers`
.^| `get`, `list`, `watch`

.^| `config.openshift.io`
.^| `proxies`
.^| `get`, `list`, `watch`

.^| `cdi.kubevirt.io`
.^| `*`
.^| `*`

.^| `snapshot.storage.k8s.io`
.^| `volumesnapshots`, `volumesnapshotclasses`, `volumesnapshotcontents`
.^| `get`, `list`, `watch`, `create`, `delete`

.^| `snapshot.storage.k8s.io`
.^| `volumesnapshots`
.^| `update`, `deletecollection`

.^| `apiextensions.k8s.io`
.^| `customresourcedefinitions`
.^| `get`, `list`, `watch`

.^| `scheduling.k8s.io`
.^| `priorityclasses`
.^| `get`, `list`, `watch`

.^| `image.openshift.io`
.^| `imagestreams`
.^| `get`, `list`, `watch`

.^| `""` (core)
.^| `secrets`
.^| `create`

.^| `kubevirt.io`
.^| `virtualmachines/finalizers`
.^| `update`
|===

[id="namespaced-rbac-roles-cdi"]
== Namespaced RBAC roles

.Namespaced roles for the `cdi-operator` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `rbac.authorization.k8s.io`
.^| `rolebindings`, `roles`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `""` (core)
.^| `serviceaccounts`, `configmaps`, `events`, `secrets`, `services`
.^| `get`, `list`, `watch`, `create`, `update`, `patch`, `delete`

.^| `apps`
.^| `deployments`, `deployments/finalizers`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `route.openshift.io`
.^| `routes`, `routes/custom-host`
.^| `get`, `list`, `watch`, `create`, `update`

.^| `config.openshift.io`
.^| `proxies`
.^| `get`, `list`, `watch`

.^| `monitoring.coreos.com`
.^| `servicemonitors`, `prometheusrules`
.^| `get`, `list`, `watch`, `create`, `delete`, `update`, `patch`

.^| `coordination.k8s.io`
.^| `leases`
.^| `get`, `create`, `update`
|===

.Namespaced roles for the `cdi-controller` service account
[cols="1,1,2",options="header"]
|===
| API group
| Resources
| Verbs

.^| `""` (core)
.^| `configmaps`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `""` (core)
.^| `secrets`
.^| `get`, `list`, `watch`

.^| `batch`
.^| `cronjobs`
.^| `get`, `list`, `watch`, `create`, `update`, `delete`

.^| `batch`
.^| `jobs`
.^| `create`, `delete`, `list`, `watch`

.^| `coordination.k8s.io`
.^| `leases`
.^| `get`, `create`, `update`

.^| `networking.k8s.io`
.^| `ingresses`
.^| `get`, `list`, `watch`

.^| `route.openshift.io`
.^| `routes`
.^| `get`, `list`, `watch`
|===

// Module included in the following assemblies:
//
// * virt/virt-security-policies.adoc

[id="virt-additional-scc-for-kubevirt-controller_{context}"]
= Additional SCCs and permissions for the kubevirt-controller service account

[role="_abstract"]
Security context constraints (SCCs) control permissions for pods. These permissions include actions that a pod, a collection of containers, can perform and what resources it can access. You can use SCCs to define a set of conditions that a pod must run with to be accepted into the system.

The `virt-controller` is a cluster controller that creates the `virt-launcher` pods for virtual machines in the cluster.

[NOTE]
====
By default, `virt-launcher` pods run with the `default` service account in the namespace. If your compliance controls require a unique service account, assign one to the VM. The setting applies to the `VirtualMachineInstance` object and the `virt-launcher` pod.
====

The `kubevirt-controller` service account is granted additional SCCs and Linux capabilities so that it can create `virt-launcher` pods with the appropriate permissions. These extended permissions allow virtual machines to use {VirtProductName} features that are beyond the scope of typical pods.

The `kubevirt-controller` service account is granted the following SCCs:

`scc.AllowHostDirVolumePlugin = true`::
This allows virtual machines to use the hostpath volume plugin.

`scc.AllowPrivilegedContainer = false`::
This ensures the `virt-launcher` pod is not run as a privileged container.

`scc.AllowedCapabilities = []corev1.Capability{"SYS_NICE", "NET_BIND_SERVICE"}`::

* `SYS_NICE` allows setting the CPU affinity.
* `NET_BIND_SERVICE` allows DHCP and Slirp operations.

== Viewing the SCC and RBAC definitions for the kubevirt-controller

You can view the `SecurityContextConstraints` definition for the `kubevirt-controller` by using the `oc` tool:

[source,terminal]
----
$ oc get scc kubevirt-controller -o yaml
----

You can view the RBAC definition for the `kubevirt-controller` clusterrole by using the `oc` tool:

[source,terminal]
----
$ oc get clusterrole kubevirt-controller -o yaml
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Pod Security Standards
* About Security context constraints
* Using RBAC to define and apply permissions
* Managing security context constraints
* Creating a cluster role
* Cluster role binding commands
* Enabling user permissions to clone data volumes across namespaces
