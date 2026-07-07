---
title: "Windows Machine Config Operator known limitations"
type: reference
domain: openshift
slug: windows-containers-4-22-windows-containers-release-notes-limitations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/windows-containers-release-notes-limitations
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Windows Machine Config Operator known limitations

[id="windows-containers-release-notes-limitations"]
= Windows Machine Config Operator known limitations

Note the following limitations when working with Windows nodes managed by the WMCO (Windows nodes):

* The following OpenShift Container Platform features are not supported on Windows nodes:
// ** Red Hat OpenShift Developer CLI (odo)
** Image builds
** OpenShift Pipelines
** OpenShift Service Mesh
** OpenShift monitoring of user-defined projects
** {ServerlessProductName}
** Horizontal Pod Autoscaling
** Vertical Pod Autoscaling
** Hosted Control Planes

* The following Red Hat features are not supported on Windows nodes:
** {red-hat-lightspeed} cost management
** Red Hat OpenShift Local

* Dual NIC is not supported on WMCO-managed Windows instances.

* Windows nodes do not support workloads created by using deployment configs. You can use a deployment or other method to deploy workloads.

* {productwinc} does not support adding Windows nodes to a cluster through a trunk port. The only supported networking configuration for adding Windows nodes is through an access port that carries traffic for the VLAN.

* {productwinc} does not support any Windows operating system language other than English (United States).

* Due to a limitation within the Windows operating system, `clusterNetwork` CIDR addresses of class E, such as `240.0.0.0`, are not compatible with Windows nodes.

* Kubernetes has identified the following node feature limitations :
** Huge pages are not supported for Windows containers.
** Privileged containers are not supported for Windows containers.

* Kubernetes has identified several API compatibility issues.
