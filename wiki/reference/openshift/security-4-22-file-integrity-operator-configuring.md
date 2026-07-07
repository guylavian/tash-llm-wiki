---
title: "Configuring the Custom File Integrity Operator"
type: reference
domain: openshift
slug: security-4-22-file-integrity-operator-configuring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security/file-integrity-operator-configuring
version: 4.22
family: security
documentKind: "Documentation"
---

# Configuring the Custom File Integrity Operator

[id="configuring-file-integrity-operator"]
= Configuring the Custom File Integrity Operator

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="viewing-file-integrity-object-attributes_{context}"]
= Viewing FileIntegrity object attributes

As with any Kubernetes custom resources (CRs), you can run `oc explain fileintegrity`, and then look at the individual attributes using:

[source,terminal]
----
$ oc explain fileintegrity.spec
----

[source,terminal]
----
$ oc explain fileintegrity.spec.config
----

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="important-file-integrity-object-attributes_{context}"]
= Important attributes

.Important `spec` and `spec.config` attributes

[%header,cols=2*]
|===
|Attribute
|Description

|`spec.nodeSelector`
|A map of key-values pairs that must match with node's labels in order for the
AIDE pods to be schedulable on that node. The typical use is to set only a
single key-value pair where `node-role.kubernetes.io/worker: ""` schedules AIDE on
all worker nodes, `node.openshift.io/os_id: "rhcos"` schedules on all
{op-system-first} nodes.

|`spec.debug`
|A boolean attribute. If set to `true`, the daemon running in the AIDE deamon set's
pods would output extra information.

|`spec.tolerations`
|Specify tolerations to schedule on nodes with custom taints. When not specified,
a default toleration is applied, which allows tolerations to run on control plane nodes.

|`spec.config.gracePeriod`
|The number of seconds to pause in between AIDE integrity checks. Frequent AIDE
checks on a node can be resource intensive, so it can be useful to specify a
longer interval. Defaults to `900`, or 15 minutes.

|`maxBackups`
|The maximum number of AIDE database and log backups leftover from the `re-init` process to keep on a node. Older backups beyond this number are automatically pruned by the daemon.

|`spec.config.name`
| Name of a configMap that contains custom AIDE configuration. If omitted, a default configuration is created.

|`spec.config.namespace`
|Namespace of a configMap that contains custom AIDE configuration. If unset, the FIO generates a default configuration suitable for {op-system} systems.

|`spec.config.key`
|Key that contains actual AIDE configuration in a config map specified by `name` and `namespace`. The default value is `aide.conf`.

|`spec.config.initialDelay`
|The number of seconds to wait before starting the first AIDE integrity check. Default is set to 0. This attribute is optional.
|===

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="file-integrity-examine-default-config_{context}"]
= Examine the default configuration

The default File Integrity Operator configuration is stored in a config map with
the same name as the `FileIntegrity` CR.

.Procedure

* To examine the default config, run:
+
[source,terminal]
----
$ oc describe cm/worker-fileintegrity
----

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="file-integrity-understanding-default-config_{context}"]
= Understanding the default File Integrity Operator configuration

Below is an excerpt from the `aide.conf` key of the config map:

[source,bash]
----
@@define DBDIR /hostroot/etc/kubernetes
@@define LOGDIR /hostroot/etc/kubernetes
database=file:@@{DBDIR}/aide.db.gz
database_out=file:@@{DBDIR}/aide.db.gz
gzip_dbout=yes
verbose=5
report_url=file:@@{LOGDIR}/aide.log
report_url=stdout
PERMS = p+u+g+acl+selinux+xattrs
CONTENT_EX = sha512+ftype+p+u+g+n+acl+selinux+xattrs

/hostroot/boot/    	CONTENT_EX
/hostroot/root/\..* PERMS
/hostroot/root/   CONTENT_EX
----

The default configuration for a `FileIntegrity` instance provides coverage for
files under the following directories:

* `/root`
* `/boot`
* `/usr`
* `/etc`

The following directories are not covered:

* `/var`
* `/opt`
* Some OpenShift Container Platform-specific excludes under `/etc/`

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="file-integrity-operator-supplying-custom-aide-config_{context}"]
= Supplying a custom AIDE configuration

Any entries that configure AIDE internal behavior such as `DBDIR`, `LOGDIR`,
`database`, and `database_out` are overwritten by the Operator. The Operator
would add a prefix to `/hostroot/` before all paths to be watched for integrity
changes. This makes reusing existing AIDE configs that might often not be
tailored for a containerized environment and start from the root directory
easier.

[NOTE]
====
`/hostroot` is the directory where the pods running AIDE mount the host's
file system. Changing the configuration triggers a reinitializing of the database.
====

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="file-integrity-operator-defining-custom-config_{context}"]
= Defining a custom File Integrity Operator configuration

This example focuses on defining a custom configuration for a scanner that runs
on the control plane nodes based on the default configuration provided for the
`worker-fileintegrity` CR. This workflow might be useful if you are planning
to deploy a custom software running as a daemon set and storing its data under
`/opt/mydaemon` on the control plane nodes.

.Procedure

. Make a copy of the default configuration.

. Edit the default configuration with the files that must be watched or excluded.

. Store the edited contents in a new config map.

. Point the `FileIntegrity` object to the new config map through the attributes in
`spec.config`.

. Extract the default configuration:
+
[source,terminal]
----
$ oc extract cm/worker-fileintegrity --keys=aide.conf
----
+
This creates a file named `aide.conf` that you can edit. To illustrate how the
Operator post-processes the paths, this example adds an exclude directory
without the prefix:
+
[source,terminal]
----
$ vim aide.conf
----
+
.Example output
[source,terminal]
----
/hostroot/etc/kubernetes/static-pod-resources
!/hostroot/etc/kubernetes/aide.*
!/hostroot/etc/kubernetes/manifests
!/hostroot/etc/docker/certs.d
!/hostroot/etc/selinux/targeted
!/hostroot/etc/openvswitch/conf.db
----
+
Exclude a path specific to control plane nodes:
+
[source,terminal]
----
!/opt/mydaemon/
----
+
Store the other content in `/etc`:
+
[source,terminal]
----
/hostroot/etc/	CONTENT_EX
----

. Create a config map based on this file:
+
[source,terminal]
----
$ oc create cm master-aide-conf --from-file=aide.conf
----

. Define a `FileIntegrity` CR manifest that references the config map:
+
[source,yaml]
----
apiVersion: fileintegrity.openshift.io/v1alpha1
kind: FileIntegrity
metadata:
  name: master-fileintegrity
  namespace: openshift-file-integrity
spec:
  nodeSelector:
      node-role.kubernetes.io/master: ""
  config:
      name: master-aide-conf
      namespace: openshift-file-integrity
----
+
The Operator processes the provided config map file and stores the result in a
config map with the same name as the `FileIntegrity` object:
+
[source,terminal]
----
$ oc describe cm/master-fileintegrity | grep /opt/mydaemon
----
+
.Example output
[source,terminal]
----
!/hostroot/opt/mydaemon
----

// Module included in the following assemblies:
//
// * security/file_integrity_operator/file-integrity-operator-configuring.adoc

[id="file-integrity-operator-changing-custom-config_{context}"]
= Changing the custom File Integrity configuration

To change the File Integrity configuration, never change the generated
config map. Instead, change the config map that is linked to the `FileIntegrity`
object through the `spec.name`, `namespace`, and `key` attributes.
