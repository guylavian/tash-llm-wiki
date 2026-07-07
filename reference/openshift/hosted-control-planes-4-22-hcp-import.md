---
title: "Manually importing a hosted cluster"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-import
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-import
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Manually importing a hosted cluster

[id="hcp-import"]
= Manually importing a hosted cluster

Hosted clusters are automatically imported into {mce-short} after the hosted control plane becomes available.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-import.adoc

[id="hcp-import-limitations_{context}"]
= Limitations of managing imported hosted clusters

Hosted clusters are automatically imported into the local {mce}, unlike a standalone OpenShift Container Platform or third party clusters. Hosted clusters run some of their agents in the _hosted mode_ so that the agents do not use the resources of your cluster.

If you choose to automatically import hosted clusters, you can update node pools and the control plane in hosted clusters by using the `HostedCluster` resource on the management cluster. To update node pools and a control plane, see "Updating node pools in a hosted cluster" and "Updating a control plane in a hosted cluster".

You can import hosted clusters into a location other than the local {mce-short} by using the {rh-rhacm-first}. For more information, see "Discovering {mce} hosted clusters in {rh-rhacm-title}".

In this topology, you must update your hosted clusters by using the command-line interface or the console of the local {mce} where the cluster is hosted. You cannot update the hosted clusters through the {rh-rhacm} hub cluster.

[role="_additional-resources_{context}"]
== Additional resources

* Updating node pools in a hosted cluster
* Updating a control plane in a hosted cluster
* Discovering {mce} hosted clusters in {rh-rhacm-title}

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-import.adoc

[id="hcp-import-manual_{context}"]
= Manually importing hosted clusters

If you want to import hosted clusters manually, complete the following steps.

.Procedure

. In the console, click *Infrastructure* -> *Clusters* and select the hosted cluster that you want to import.

. Click *Import hosted cluster*.

+
[NOTE]
====
For your _discovered_ hosted cluster, you can also import from the console, but the cluster must be in an upgradable state. Import on your cluster is disabled if the hosted cluster is not in an upgradable state because the hosted control plane is not available. Click *Import* to begin the process. The status is `Importing` while the cluster receives updates and then changes to `Ready`.
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-import.adoc

[id="hcp-import-manual-aws_{context}"]
= Manually importing a hosted cluster on {aws-short}

You can also import a hosted cluster on {aws-first} with the command-line interface.

.Procedure

. Create your `ManagedCluster` resource by using the following sample YAML file:
+
[source,yaml]
----
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  annotations:
    import.open-cluster-management.io/hosting-cluster-name: local-cluster
    import.open-cluster-management.io/klusterlet-deploy-mode: Hosted
    open-cluster-management/created-via: hypershift
  labels:
    cloud: auto-detect
    cluster.open-cluster-management.io/clusterset: default
    name: <hosted_cluster_name> <1>
    vendor: OpenShift
  name: <hosted_cluster_name>
spec:
  hubAcceptsClient: true
  leaseDurationSeconds: 60
----
+
<1> Replace `<hosted_cluster_name>` with the name of your hosted cluster.

. Run the following command to apply the resource:
+
[source,terminal]
----
$ oc apply -f <file_name> <1>
----
+
<1> Replace `<file_name>` with the YAML file name you created in the previous step.

. If you have {rh-rhacm-title} installed, create your `KlusterletAddonConfig` resource by using the following sample YAML file. If you have installed {mce-short} only, skip this step:
+
[source,yaml]
----
apiVersion: agent.open-cluster-management.io/v1
kind: KlusterletAddonConfig
metadata:
  name: <hosted_cluster_name> <1>
  namespace: <hosted_cluster_namespace> <2>
spec:
  clusterName: <hosted_cluster_name>
  clusterNamespace: <hosted_cluster_namespace>
  clusterLabels:
    cloud: auto-detect
    vendor: auto-detect
  applicationManager:
    enabled: true
  certPolicyController:
    enabled: true
  iamPolicyController:
    enabled: true
  policyController:
    enabled: true
  searchCollector:
    enabled: false
----
+
<1> Replace `<hosted_cluster_name>` with the name of your hosted cluster.
<2> Replace `<hosted_cluster_namespace>` with the name of your hosted cluster namespace.

. Run the following command to apply the resource:
+
[source,terminal]
----
$ oc apply -f <file_name> <1>
----
+
<1> Replace `<file_name>` with the YAML file name you created in the previous step.

. After the import process is complete, your hosted cluster becomes visible in the console. You can also check the status of your hosted cluster by running the following command:
+
[source,terminal]
----
$ oc get managedcluster <hosted_cluster_name>
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-import.adoc

[id="hcp-import-disable_{context}"]
= Disabling the automatic import of hosted clusters into {mce-short}

Hosted clusters are automatically imported into {mce-short} after the control plane becomes available. If needed, you can disable the automatic import of hosted clusters.

Any hosted clusters that were previously imported are not affected, even if you disable automatic import. When you upgrade to {mce-short} 2.5 and automatic import is enabled, all hosted clusters that are not imported are automatically imported if their control planes are available.

[NOTE]
====
If Red{nbsp}Hat Advanced Cluster Management is installed, all Red{nbsp}Hat Advanced Cluster Management add-ons are also enabled.
====

When automatic import is disabled, only newly created hosted clusters are not automatically imported. Hosted clusters that were already imported are not affected. You can still manually import clusters by using the console or by creating the `ManagedCluster` and `KlusterletAddonConfig` custom resources.

.Procedure

To disable the automatic import of hosted clusters, complete the following steps:

. On the hub cluster, open the `hypershift-addon-deploy-config` specification that is in the `AddonDeploymentConfig` resource in the namespace where {mce-short} is installed by entering the following command:
+
[source,terminal]
----
$ oc edit addondeploymentconfig hypershift-addon-deploy-config \
  -n multicluster-engine
----

. In the `spec.customizedVariables` section, add the `autoImportDisabled` variable with value of `"true"`, as shown in the following example:
+
[source,yaml]
----
apiVersion: addon.open-cluster-management.io/v1alpha1
kind: AddOnDeploymentConfig
metadata:
  name: hypershift-addon-deploy-config
  namespace: multicluster-engine
spec:
  customizedVariables:
   - name: hcMaxNumber
     value: "80"
  - name: hcThresholdNumber
    value: "60"
  - name: autoImportDisabled
    value: "true"
----

. To re-enable automatic import, set the value of the `autoImportDisabled` variable to `"false"` or remove the variable from the `AddonDeploymentConfig` resource.
