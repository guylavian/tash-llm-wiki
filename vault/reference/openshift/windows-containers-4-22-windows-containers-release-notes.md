---
title: "{productwinc} release notes"
type: reference
domain: openshift
slug: windows-containers-4-22-windows-containers-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/windows-containers-release-notes
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# {productwinc} release notes

[id="windows-containers-release-notes"]
= {productwinc} release notes

[role="_abstract"]
You can review the release notes to learn about the changes introduced through each release of the {productwinc} and the Windows Machine Config Operator (WMCO).

// Module included in the following assemblies:
//
// * windows_containers/wmco_rn/windows-containers-release-notes.adoc

[id="windows-containers-release-notes-10-22-0_{context}"]
= Release notes for Red Hat Windows Machine Config Operator 10.22.0

Issued: 20 May 2026

[role="_abstract"]
You can review the following release notes to learn about the new features and bug fixes in the Windows Machine Config Operator (WMCO) version 10.22.0.

The components of the WMCO version 10.22.0 were released in RHBA-2026:19710.

[id="wmco-10-22-0-new-features_{context}"]
== New features and improvements

Windows Server 2025 support::
The WMCO now supports Windows Server 2025, OS Build 10.0.26100 or later for all supported platforms.

Kubernetes upgrade::
The WMCO now uses Kubernetes version 1.35.

[id="wmco-10-22-0-bug-fixes_{context}"]
== Bug fixes

* Before this update, if you enabled the `ClusterAPIMachineManagement` feature gate by enabling the `TechPreviewNoUpgrade` feature set, OpenShift Container Platform provisioned the `openshift-cluster-api` namespace. However, the WMCO was not adding the `windows-user-data` secret to that namespace, which is required by Cluster API compute machine sets. Because of the missing secret, CAPI-provisioned Windows machines would not bootstrap, remaining stuck in the `Pending` phase, and never joining the cluster. With this release, the OpenShift Container Platform now detects whether the `openshift-cluster-api` namespace exists and mirrors the `windows-user-data` secret into that namespace. CAPI-provisioned Windows machines successfully receive the bootstrap secret, are no longer getting stuck in `Pending` state, and join the cluster as expected. (OCPBUGS-38401)
