---
title: "Installing a cluster on vSphere using the Agent-based Installer"
type: reference
domain: openshift
slug: installing-4-22-installing-vsphere-agent-based-installer
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-vsphere-agent-based-installer
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on vSphere using the Agent-based Installer

[id="installing-vsphere-agent-based-installer"]
= Installing a cluster on vSphere using the Agent-based Installer

The Agent-based installation method provides the flexibility to boot your on-premise servers in any way that you choose. It combines the ease of use of the Assisted Installation service with the ability to run offline, including in air-gapped environments.

Agent-based installation is a subcommand of the OpenShift Container Platform installer. It generates a bootable ISO image containing all of the information required to deploy an OpenShift Container Platform cluster with an available release image.

For more information about installing a cluster using the Agent-based Installer, see Preparing to install with the Agent-based Installer.

[IMPORTANT]
====
Your vSphere account must include privileges for reading and creating the resources required to install an OpenShift Container Platform cluster.
For more information about privileges, see vCenter requirements.
====
