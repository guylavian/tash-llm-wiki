---
title: "Enabling features using feature gates"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cluster-enabling-features
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cluster-enabling-features
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Enabling features using feature gates

[id="nodes-cluster-enabling-features"]
= Enabling features using feature gates

[role="_abstract"]
As an administrator, you can use feature gates to enable features that are not part of the default set of features so that you can use these non-default features in your cluster.

// Module included in the following assemblies:
//
// nodes/clusters/nodes-cluster-enabling-features.adoc

[id="nodes-cluster-enabling-features-about_{context}"]
= Understanding feature gates

[role="_abstract"]
You can use the `FeatureGate` custom resource (CR) to enable specific feature sets so that you can use specific non-default features in your cluster.

A feature set is a collection of OpenShift Container Platform features that are not enabled by default.

You can activate the following feature set by using the `FeatureGate` CR:

* `TechPreviewNoUpgrade`. This feature set is a subset of the current Technology Preview features. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them, while leaving the features disabled on production clusters.
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.
====
+
The following Technology Preview features are enabled by this feature set:
+
--
** `AdditionalStorageConfig`
** `AutomatedEtcdBackup`
** `AWSClusterHostedDNS`
** `AWSClusterHostedDNSInstall`
** `AWSDedicatedHosts`
** `AWSDualStackInstall`
** `AWSEuropeanSovereignCloudInstall`
** `AWSServiceLBNetworkSecurityGroup`
** `AzureClusterHostedDNSInstall`
** `AzureDedicatedHosts`
** `AzureDualStackInstall`
** `AzureMultiDisk`
** `AzureWorkloadIdentity`
** `BootcNodeManagement`
** `BootImageSkewEnforcement`
** `BuildCSIVolumes`
** `CBORServingAndStorage`
** `ClientsPreferCBOR`
** `ClusterAPIInstallIBMCloud`
** `ClusterAPIMachineManagement`
** `ClusterAPIMachineManagementAWS`
** `ClusterAPIMachineManagementAzure`
** `ClusterAPIMachineManagementBareMetal`
** `ClusterAPIMachineManagementGCP`
** `ClusterAPIMachineManagementOpenStack
** `ClusterAPIMachineManagementPowerVS`
** `ClusterAPIMachineManagementVSphere`
** `ClusterMonitoringConfig`
** `ClusterUpdateAcceptRisks`
** `ClusterVersionOperatorConfiguration`
** `ConfigurablePKI`
** `ConsolePluginContentSecurityPolicy`
** `CRDCompatibilityRequirementOperator`
** `CRIOCredentialProviderConfig`
** `DNSNameResolver`
** `DRAPartitionableDevices`
** `DualReplica`
** `DynamicServiceEndpointIBMCloud`
** `EtcdBackendQuota`
** `EventTTL`
//** `EVPN` From Anurag Saxena: EVPN shouldn't be there. It is lifted and to be GA'ed in 4.22.
** `Example`
** `ExternalOIDC`
** `ExternalOIDCWithUIDAndExtraClaimMappings`
** `ExternalOIDCWithUpstreamParity`
** `GatewayAPIWithoutOLM`
** `GCPCustomAPIEndpoints`
** `GCPCustomAPIEndpointsInstall`
** `GCPDualStackInstall`
** `HyperShiftOnlyDynamicResourceAllocation`
** `ImageModeStatusReporting`
** `ImageStreamImportMode`
** `IngressControllerDynamicConfigurationManager`
** `InsightsConfig`
** `InsightsOnDemandDataGather`
** `IrreconcilableMachineConfig`
** `KMSEncryption`
** `KMSv1`
** `MachineAPIMigration`
** `MachineAPIMigrationAWS`
** `MachineAPIMigrationOpenStack`
** `ManagedBootImagesCPMS`
** `MaxUnavailableStatefulSet`
** `MetricsCollectionProfiles`
** `MinimumKubeletVersion`
** `MixedCPUsAllocation`
** `MultiDiskSetup`
** `MutableCSINodeAllocatableCount`
** `MutatingAdmissionPolicy`
** `NewOLM`
** `NewOLMBoxCutterRuntime`
** `NewOLMCatalogdAPIV1Metas`
** `NewOLMConfigAPI`
** `NewOLMOwnSingleNamespace`
** `NewOLMPreflightPermissionChecks`
** `NewOLMWebhookProviderOpenshiftServiceCA`
//From Arti Sood: lgtm for NoOverlayMode
** `NoOverlayMode`
** `NoRegistryClusterInstall`
** `NutanixMultiSubnets`
** `OnPremDNSRecords`
** `OpenShiftPodSecurityAdmission`
** `OSStreams`
** `OVNObservability`
** `RouteExternalCertificate`
** `SELinuxMount`
** `ServiceAccountTokenNodeBinding`
** `SignatureStores`
** `SigstoreImageVerification`
** `SigstoreImageVerificationPKI`
** `StoragePerformantSecurityPolicy`
** `TLSAdherence`
** `UpgradeStatus`
** `UserNamespacesPodSecurityStandards`
** `UserNamespacesSupport`
** `VolumeGroupSnapshot`
** `VSphereConfigurableMaxAllowedBlockVolumesPerNode`
** `VSphereHostVMGroupZonal`
** `VSphereMixedNodeEnv`
** `VSphereMultiDisk`
** `VSphereMultiNetworks`
--

See the _Additional resources_ sections for information on some of these features.

Do not document per Derek Carr: https://github.com/openshift/api/pull/370#issuecomment-510632939
|`CustomNoUpgrade` ^[2]^
|Allows the enabling or disabling of any feature. Turning on this feature set on is not supported, cannot be undone, and prevents upgrades.

[.small]
--
1.
2. If you use the `CustomNoUpgrade` feature set to disable a feature that appears in the web console, you might see that feature, but
no objects are listed. For example, if you disable builds, you can see the *Builds* tab in the web console, but there are no builds present. If you attempt to use commands associated with a disabled feature, such as `oc start-build`, OpenShift Container Platform displays an error.

[NOTE]
====
If you disable a feature that any application in the cluster relies on, the application might not
function properly, depending upon the feature disabled and how the application uses that feature.
====

// Module included in the following assemblies:
//
// * nodes/cluster/nodes-cluster-enabling-features.adoc

[id="nodes-cluster-enabling-features-install_{context}"]
= Enabling feature sets at installation

[role="_abstract"]
You can enable feature sets for all nodes in the cluster by editing the `install-config.yaml` file before you deploy the cluster. This allows you to use non-default features in your cluster.

.Prerequisites

* You have an `install-config.yaml` file.

.Procedure

. Use the `featureSet` parameter to specify the name of the feature set you want to enable, such as `TechPreviewNoUpgrade`:
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.
====
+
.Sample `install-config.yaml` file with an enabled feature set

[source,yaml]
----
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    aws:
      rootVolume:
        iops: 2000
        size: 500
        type: io1
      metadataService:
        authentication: Optional
      type: c5.4xlarge
      zones:
      - us-west-2c
  replicas: 3
featureSet: TechPreviewNoUpgrade
----

. Save the file and reference it when using the installation program to deploy the cluster.

.Verification

// Module included in the following assemblies:
//
// * nodes/clusters/nodes-cluster-enabling-features.adoc

[id="nodes-cluster-enabling-features-console_{context}"]
= Enabling feature sets using the web console

[role="_abstract"]
You can use the OpenShift Container Platform web console to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster.

.Procedure

. In the OpenShift Container Platform web console, switch to the *Administration* -> *Custom Resource Definitions* page.

. On the *Custom Resource Definitions* page, click *FeatureGate*.

. On the *Custom Resource Definition Details* page, click the *Instances* tab.

. Click the *cluster* feature gate, then click the *YAML* tab.

. Edit the *cluster* instance to add specific feature sets:
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.
====

+
.Sample Feature Gate custom resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: FeatureGate
metadata:
  name: cluster <1>
# ...
spec:
  featureSet: TechPreviewNoUpgrade <2>
----
where:
+
--
`metadata.name`:: Specifies the name of the `FeatureGate` CR. You must specify `cluster` for the name.

`spec.featureSet`:: Specifies the feature set that you want to enable:
* `TechPreviewNoUpgrade` enables specific Technology Preview features.
--
+
After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied.

.Verification

// Module included in the following assemblies:
//
// * nodes/cluster/nodes-cluster-enabling-features.adoc

[id="nodes-cluster-enabling-features-cli_{context}"]
= Enabling feature sets using the CLI

[role="_abstract"]
You can use the {oc-first} to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

* Edit the `FeatureGate` CR named `cluster`:
+
[source,terminal]
----
$ oc edit featuregate cluster
----
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters.
====
+
.Sample FeatureGate custom resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: FeatureGate
metadata:
  name: cluster
# ...
spec:
  featureSet: TechPreviewNoUpgrade
----
where:
+
--
`metadata.name`:: Specifies the name of the `FeatureGate` CR. This must be `cluster`.

`spec.featureSet`:: Specifies the feature set that you want to enable:
* `TechPreviewNoUpgrade` enables specific Technology Preview features.
--
+
After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied.

.Verification

[role="_additional-resources"]
[id="additional-resources_nodes-cluster-enabling"]
== Additional resources

* Shared Resources CSI Driver and Build CSI Volumes in OpenShift Builds

* CSI inline ephemeral volumes

* Managing machines with the Cluster API

* Disabling the {insights-operator} gather operations

* Enabling the {insights-operator} gather operations

* Running an {insights-operator} gather operation

* Managing the default storage class

* Pod security admission enforcement
