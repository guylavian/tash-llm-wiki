---
title: "Windows Machine Config Operator prerequisites"
type: reference
domain: openshift
slug: windows-containers-4-22-windows-containers-release-notes-prereqs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/windows-containers-release-notes-prereqs
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Windows Machine Config Operator prerequisites

[id="windows-containers-release-notes-prereqs"]
= Windows Machine Config Operator prerequisites

[role="_abstract"]
You can review the following information for details on the supported platform versions, Windows Server versions, and networking configurations for the Windows Machine Config Operator (WMCO). See the vSphere documentation for any information that is relevant to only that platform.

[id="wmco-prerequisites-supported-install_{context}"]
== WMCO supported installation method

The WMCO fully supports installing Windows nodes into installer-provisioned infrastructure (IPI) clusters. This is the preferred OpenShift Container Platform installation method.

For user-provisioned infrastructure (UPI) clusters, the WMCO supports installing Windows nodes only into a UPI cluster installed with the `platform: none` field set in the `install-config.yaml` file (bare-metal or provider-agnostic) and only for the BYOH (Bring Your Own Host) use case. UPI is not supported for any other platform.

[id="wmco-prerequisites-supported_{context}"]
== WMCO supported platforms and Windows Server versions

The following table lists the Windows Server versions that are supported by WMCO 10.20.0, based on the applicable platform. Windows Server versions not listed are not supported and attempting to use them will cause errors. To prevent these errors, use only an appropriate version for your platform.

[cols="3,7",options="header"]
|===
|Platform
|Supported Windows Server version

|Amazon Web Services (AWS)
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later ^[1]^
* Windows Server 2019, version 1809

|Microsoft Azure
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later
* Windows Server 2019, version 1809

|VMware vSphere
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later

|{gcp-first}
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later

|Nutanix
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later

|Bare metal or provider agnostic
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later

|===
[.small]
. For disconnected clusters, the Windows AMI must have the EC2LaunchV2 agent version 2.0.2107 or later installed. For more information, see the Install the latest version of EC2Launch v2 in the AWS documentation.

== Supported networking

Hybrid networking with OVN-Kubernetes is the only supported networking configuration. See the additional resources below for more information on this functionality. The following tables outline the type of networking configuration and Windows Server versions to use based on your platform. You must specify the network configuration when you install the cluster.

[NOTE]
====
* The WMCO does not support OVN-Kubernetes without hybrid networking or OpenShift SDN.
* Dual NIC is not supported on WMCO-managed Windows instances.
====

.Platform networking support
[cols="2",options="header"]
|===
|Platform
|Supported networking

|Amazon Web Services (AWS)
|Hybrid networking with OVN-Kubernetes

|Microsoft Azure
|Hybrid networking with OVN-Kubernetes

|VMware vSphere
|Hybrid networking with OVN-Kubernetes with a custom VXLAN port

|{gcp-first}
|Hybrid networking with OVN-Kubernetes

|Nutanix
|Hybrid networking with OVN-Kubernetes

|Bare metal or provider agnostic
|Hybrid networking with OVN-Kubernetes
|===

.Hybrid OVN-Kubernetes Windows Server support
[cols="2",options="header"]
|===
|Hybrid networking with OVN-Kubernetes
|Supported Windows Server version

|Default VXLAN port
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later
* Windows Server 2019, version 1809

|Custom VXLAN port
a|* Windows Server 2025, OS Build 10.0.26100 or later
* Windows Server 2022, OS Build 20348.681 or later

|===

[role="_additional-resources"]
.Additional resources
* Hybrid networking
