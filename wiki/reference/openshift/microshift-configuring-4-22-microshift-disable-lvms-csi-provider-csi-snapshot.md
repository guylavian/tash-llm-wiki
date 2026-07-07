---
title: "Disabling the LVMS CSI provider or CSI snapshot"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-disable-lvms-csi-provider-csi-snapshot
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-disable-lvms-csi-provider-csi-snapshot
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Disabling the LVMS CSI provider or CSI snapshot

[id="microshift-disable-lvms-csi-provider-csi-snapshot"]
= Disabling the LVMS CSI provider or CSI snapshot

[role="_abstract"]
To reduce use of runtime resources such as RAM, CPU, and storage in {microshift-short}, you can disable the built-in LVMS CSI provider or CSI snapshot. Configure the storage section in the configuration file before you install or run the product.

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc
// * microshift_configuring/microshift-disable-lvms-csi-provider-csi-snapshot.adoc

[id="microshift-disabling-lvms-csi-snapshot_{context}"]
= Disabling deployments that run CSI snapshot implementations

[role="_abstract"]
To prevent the installation of CSI implementation pods, disable the deployments that run CSI snapshot implementations. This configuration conserves system resources by ensuring that snapshot components are not deployed when they are not required.

[IMPORTANT]
====
Use the procedure if you are defining the configuration file before installing and running {microshift-short}. If {microshift-short} is already started, the CSI snapshot implementation will be running. You must manually remove the implementation by following the uninstallation instructions.
====

[NOTE]
====
{microshift-short} does not delete CSI snapshot implementation pods. You must configure {microshift-short} to disable installation of the CSI snapshot implementation pods during the startup process.
====

.Procedure

. Disable installation of the CSI snapshot controller by entering the `optionalCsiComponents` value under the `storage` section of the {microshift-short} configuration file in `/etc/microshift/config.yaml`:
+
[source,yaml]
----
# ...
  storage: {}
# ...
----
+
where:
+
`storage`:: Specifies the storage details. You can choose to not define `optionalCsiComponents`. If you do specify the `optionalCsiComponents` field, valid values include: an empty value (`[]`) or a single empty string element (`[""]`), `snapshot-controller`, or `none`. A value of `none` is mutually exclusive with all other values.
+
[NOTE]
====
If the `optionalCsiComponents` value is empty or null, {microshift-short} defaults to deploying `snapshot-controller`.
====

. After the `optionalCsiComponents` field is specified with a supported value in the `config.yaml`, start {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----
+
[NOTE]
====
{microshift-short} does not redeploy the disabled components after a restart.
====

// Module included in the following assemblies:
//
// * microshift_storage/microshift-storage-plugin-overview.adoc
// * microshift_configuring/microshift-disable-lvms-csi-provider-csi-snapshot.adoc

[id="microshift-disabling-lvms-csi-driver_{context}"]
= Disabling deployments that run the CSI driver implementations

[role="_abstract"]
You can disable installation of the CSI implementation pods. {microshift-short} does not delete CSI driver implementation pods. You must configure {microshift-short} to disable installation of the CSI driver implementation pods during the startup process.

[IMPORTANT]
====
This procedure is for defining the configuration file before installing and running {microshift-short}. If {microshift-short} is already started, then the CSI driver implementation is running. You must manually remove it by following the uninstallation instructions.
====

.Procedure

. Disable installation of the CSI driver by entering the `driver` value under the `storage` section of the {microshift-short} configuration file in `/etc/microshift/config.yaml`:
+
[source,yaml]
----
# ...
  storage
   driver:
   - "none"
# ...
----
+
where:
+
`storage.driver.none`:: Specifies the driver to disable. Valid values are `none` or `lvms`.
+
[NOTE]
====
By default, the `driver` value is empty or null and LVMS is deployed.
====

. Start {microshift-short} after the `driver` field is specified with a supported value in the `/etc/microshift/config.yaml` file by running the following command:
+
[source,terminal]
----
$ sudo systemctl enable --now microshift
----
+
[NOTE]
====
{microshift-short} does not redeploy the disabled components after a restart operation.
====
