---
title: "Postinstallation configuration overview"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-index
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/index
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Postinstallation configuration overview

[id="post-install-configuration-overview"]
= Postinstallation configuration overview

After installing OpenShift Container Platform, a cluster administrator can configure and customize the following components:

* Machine
* Bare metal
* Cluster
* Node
* Network
* Storage
* Users
* Alerts and notifications

[id="post-install-tasks"]
== Postinstallation configuration tasks

You can perform the postinstallation configuration tasks to configure your environment to meet your needs.

The following lists details these configurations:

* Configure operating system features: The Machine Config Operator (MCO) manages `MachineConfig` objects. By using the MCO, you can configure nodes and custom resources.

* Configure cluster features. You can modify the following features of an OpenShift Container Platform cluster:

** Image registry
** Networking configuration
** Image build behavior
** Identity provider
** The etcd configuration
** Machine set creation to handle the workloads
** Cloud provider credential management

* Configuring a private cluster: By default, the installation program provisions OpenShift Container Platform by using a publicly accessible DNS and endpoints. To make your cluster accessible only from within an internal network, configure the following components to make them private:

** DNS
** Ingress Controller
** API server

* Perform node operations: By default, OpenShift Container Platform uses {op-system-first} compute machines. You can perform the following node operations:

** Add and remove compute machines.
** Add and remove taints and tolerations.
** Configure the maximum number of pods per node.
** Enable Device Manager.

* Configure users: Users can authenticate themselves to the API by using OAuth access tokens. You can configure OAuth to perform the following tasks:

** Specify an identity provider.
** Use role-based access control to define and grant permissions to users.
** Install an Operator from the software catalog.

* Configuring alert notifications: By default, firing alerts are displayed on the Alerting UI of the web console. You can also configure OpenShift Container Platform to send alert notifications to external systems.
