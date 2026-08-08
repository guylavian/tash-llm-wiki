---
title: "{VirtProductName} runbooks"
type: reference
domain: openshift
slug: virt-4-22-virt-runbooks
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-runbooks
version: 4.22
family: virt
documentKind: "Documentation"
---

# {VirtProductName} runbooks

[id="virt-runbooks"]
= {VirtProductName} runbooks

[role="_abstract"]
To diagnose and resolve {VirtProductName} alerts, you can use the {VirtProductName} Operator runbooks. These guides help ensure you can effectively troubleshoot cluster issues and restore system health.

[NOTE]
====
Runbooks for the {VirtProductName} Operator are maintained in the openshift/runbooks Git repository, and you can view them on GitHub.
====

[id="virt-runbooks-supported-table"]
[cols="1m,1"]
.Runbooks for {VirtProductName} alerts
|===
| Alert | GitHub link

| CDIDataImportCronOutdated
| Runbook

| CDIDataVolumeUnusualRestartCount
| Runbook

| CDIDefaultStorageClassDegraded
| Runbook

| CDIMultipleDefaultVirtStorageClasses
| Runbook

| CDINoDefaultStorageClass
| Runbook

| CDINotReady
| Runbook

| CDIOperatorDown
| Runbook

| CDIStorageProfilesIncomplete
| Runbook

| CnaoDown
| Runbook

| CnaoNMstateMigration
| Runbook

| DeprecatedMachineType
| Runbook

| GuestFilesystemAlmostOutOfSpace
| Runbook

| GuestVCPUQueueHighCritical
| Runbook

| GuestVCPUQueueHighWarning
| Runbook

| HAControlPlaneDown
| Runbook

| HCOGoldenImageWithNoArchitectureAnnotation
| Runbook

| HCOGoldenImageWithNoSupportedArchitecture
| Runbook

| HCOInstallationIncomplete
| Runbook

| HCOMisconfiguredDescheduler
| Runbook

| HCOMultiArchGoldenImagesDisabled
| Runbook

| HCOOperatorConditionsUnhealthy
| Runbook

| HighNodeCPUFrequency
| Runbook

| HPPNotReady
| Runbook

| HPPOperatorDown
| Runbook

| HPPSharingPoolPathWithOS
| Runbook

| HighCPUWorkload
| Runbook

| KubemacpoolDown
| Runbook

| KubeVirtCRModified
| Runbook

| KubeVirtDeprecatedAPIRequested
| Runbook

| KubeVirtVMGuestMemoryAvailableLow
| Runbook

| KubeVirtVMGuestMemoryPressure
| Runbook

| KubeVirtNoAvailableNodesToRunVMs
| Runbook

| KubeVirtVMIExcessiveMigrations
| Runbook

| LowKVMNodesCount
| Runbook

| LowReadyVirtControllersCount
| Runbook

| LowReadyVirtOperatorsCount
| Runbook

| LowVirtAPICount
| Runbook

| LowVirtControllersCount
| Runbook

| LowVirtOperatorCount
| Runbook

| NetworkAddonsConfigNotReady
| Runbook

| NoLeadingVirtOperator
| Runbook

| NoReadyVirtController
| Runbook

| NoReadyVirtOperator
| Runbook

| NodeNetworkInterfaceDown
| Runbook

| OrphanedVirtualMachineInstances
| Runbook

| OutdatedVirtualMachineInstanceWorkloads
| Runbook

| PersistentVolumeFillingUp
| Runbook

| SSPCommonTemplatesModificationReverted
| Runbook

| SSPDown
| Runbook

| SSPFailingToReconcile
| Runbook

| SSPHighRateRejectedVms
| Runbook

| SSPTemplateValidatorDown
| Runbook

| UnsupportedHCOModification
| Runbook

| VirtAPIDown
| Runbook

| VirtApiRESTErrorsBurst
| Runbook

| VirtControllerDown
| Runbook

| VirtControllerRESTErrorsBurst
| Runbook

| VirtHandlerDaemonSetRolloutFailing
| Runbook

| VirtHandlerRESTErrorsBurst
| Runbook

| VirtLauncherPodsStuckFailed
| Runbook

| VirtOperatorDown
| Runbook

| VirtOperatorRESTErrorsBurst
| Runbook

| VirtualMachineInstanceHasEphemeralHotplugVolume
| Runbook

| VirtualMachineStuckInUnhealthyState
| Runbook

| VirtualMachineStuckOnNode
| Runbook

| VMCannotBeEvicted
| Runbook

| VMStorageClassWarning
| Runbook
|===

[id="virt-runbooks-deprecated"]
== Runbooks for deprecated alerts

Deprecated alerts no longer report actual issues and you can safely ignore them.

.Runbooks for deprecated {VirtProductName} alerts
[id="virt-runbooks-deprecated-table"]
[cols="2m,1,1"]
|===
| Alert | GitHub link | Notes

| DuplicateWaspAgentDSDetected
| Runbook
| -

| KubeMacPoolDuplicateMacsFound
| Runbook
| -

| KubeVirtComponentExceedsRequestedCPU
| Runbook
| -

| KubeVirtComponentExceedsRequestedMemory
| Runbook
| -

| KubevirtVmHighMemoryUsage
| Runbook
| -

| OperatorConditionsUnhealthy
| Runbook
| -

| SingleStackIPv6Unsupported
| Runbook
| -

| SSPOperatorDown
| Runbook
| -

| VirtApiRESTErrorsHigh
| Runbook
| -

| VirtControllerRESTErrorsHigh
| Runbook
| -

| VirtHandlerRESTErrorsHigh
| Runbook
| -

| VirtOperatorRESTErrorsHigh
| Runbook
| -

| VirtualMachineCRCErrors
| Runbook
| Renamed to `VMStorageClassWarning`.
|===
