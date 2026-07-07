---
title: "Differences between {product-title} 3 and 4"
type: reference
domain: openshift
slug: migrating-from-ocp-3-to-4-4-22-planning-migration-3-4
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/migrating_from_ocp_3_to_4/planning-migration-3-4
version: 4.22
family: migrating_from_ocp_3_to_4
documentKind: "Documentation"
---

# Differences between {product-title} 3 and 4

[id="planning-migration-3-4"]
= Differences between OpenShift Container Platform 3 and 4

OpenShift Container Platform  introduces architectural changes and enhancements/ The procedures that you used to manage your OpenShift Container Platform 3 cluster might not apply to OpenShift Container Platform 4.

For information on configuring your OpenShift Container Platform 4 cluster, review the appropriate sections of the OpenShift Container Platform documentation. For information on new features and other notable technical changes, review the OpenShift Container Platform  release notes.

It is not possible to upgrade your existing OpenShift Container Platform 3 cluster to OpenShift Container Platform 4. You must start with a new OpenShift Container Platform 4 installation. Tools are available to assist in migrating your control plane settings and application workloads.

[id="migration-differences-architecture"]
== Architecture

With OpenShift Container Platform 3, administrators individually deployed {op-system-base-full} hosts, and then installed OpenShift Container Platform on top of these hosts to form a cluster. Administrators were responsible for properly configuring these hosts and performing updates.

OpenShift Container Platform 4 represents a significant change in the way that OpenShift Container Platform clusters are deployed and managed. OpenShift Container Platform 4 includes new technologies and functionality, such as Operators, machine sets, and {op-system-first}, which are core to the operation of the cluster. This technology shift enables clusters to self-manage some functions previously performed by administrators. This also ensures platform stability and consistency, and simplifies installation and scaling.

Beginning with OpenShift Container Platform 4.13, {op-system} now uses {op-system-base-full} 9.2 packages. This enhancement enables the latest fixes and features as well as the latest hardware support and driver updates. For more information about how this upgrade to RHEL 9.2 might affect your options configuration and services as well as driver and container support, see the RHCOS now uses RHEL 9.2 in the _OpenShift Container Platform 4.13 release notes_.

For more information, see OpenShift Container Platform architecture.

=== Immutable infrastructure

OpenShift Container Platform 4 uses {op-system-first}, which is designed to run containerized applications, and provides efficient installation, Operator-based management, and simplified upgrades. {op-system} is an immutable container host, rather than a customizable operating system like {op-system-base}. {op-system} enables OpenShift Container Platform 4 to manage and automate the deployment of the underlying container host. {op-system} is a part of OpenShift Container Platform, which means that everything runs inside a container and is deployed using OpenShift Container Platform.

In OpenShift Container Platform 4, control plane nodes must run {op-system}, ensuring that full-stack automation is maintained for the control plane. This makes rolling out updates and upgrades a much easier process than in OpenShift Container Platform 3.

For more information, see {op-system-first}.

=== Operators

Operators are a method of packaging, deploying, and managing a Kubernetes application. Operators ease the operational complexity of running another piece of software. They watch over your environment and use the current state to make decisions in real time. Advanced Operators are designed to upgrade and react to failures automatically.

For more information, see Understanding Operators.

[id="migration-differences-install"]
== Installation and upgrade

=== Installation process

To install OpenShift Container Platform 3.11, you prepared your {op-system-base-full} hosts, set all of the configuration values your cluster needed, and then ran an Ansible playbook to install and set up your cluster.

In OpenShift Container Platform , you use the OpenShift installation program to create a minimum set of resources required for a cluster. After the cluster is running, you use Operators to further configure your cluster and to install new services. After first boot, {op-system-first} systems are managed by the Machine Config Operator (MCO) that runs in the OpenShift Container Platform cluster.

For more information, see Installation process.

=== Infrastructure options

In OpenShift Container Platform 3.11, you installed your cluster on infrastructure that you prepared and maintained. In addition to providing your own infrastructure, OpenShift Container Platform 4 offers an option to deploy a cluster on infrastructure that the OpenShift Container Platform installation program provisions and the cluster maintains.

For more information, see OpenShift Container Platform installation overview.

=== Upgrading your cluster

In OpenShift Container Platform 3.11, you upgraded your cluster by running Ansible playbooks. In OpenShift Container Platform , the cluster manages its own updates, including updates to {op-system-first} on cluster nodes. You can easily upgrade your cluster by using the web console or by using the `oc adm upgrade` command from the OpenShift CLI and the Operators will automatically upgrade themselves. If your OpenShift Container Platform  cluster has {op-system-base} worker machines, then you will still need to run an Ansible playbook to upgrade those worker machines.

For more information, see Updating clusters.

[id="migration-considerations"]
== Migration considerations

Review the changes and other considerations that might affect your transition from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.

[id="migration-preparing-storage"]
=== Storage considerations

Review the following storage changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform .

==== Local volume persistent storage

Local storage is only supported by using the Local Storage Operator in OpenShift Container Platform . It is not supported to use the local provisioner method from OpenShift Container Platform 3.11.

For more information, see Persistent storage using local volumes.

==== FlexVolume persistent storage

The FlexVolume plugin location changed from OpenShift Container Platform 3.11. The new location in OpenShift Container Platform  is `/etc/kubernetes/kubelet-plugins/volume/exec`. Attachable FlexVolume plugins are no longer supported.

For more information, see Persistent storage using FlexVolume.

==== Container Storage Interface (CSI) persistent storage

Persistent storage using the Container Storage Interface (CSI) was Technology Preview in OpenShift Container Platform 3.11. OpenShift Container Platform  includes with several CSI drivers. You can also install your own driver.

For more information, see Persistent storage using the Container Storage Interface (CSI).

==== Red Hat OpenShift Data Foundation

OpenShift Container Storage 3, which is available for use with OpenShift Container Platform 3.11, uses Red Hat Gluster Storage as the backing storage.

{rh-storage-first} 4, which is available for use with OpenShift Container Platform 4, uses Red Hat Ceph Storage as the backing storage.

For more information, see Persistent storage using Red Hat OpenShift Data Foundation and the interoperability matrix article.

==== Unsupported persistent storage options

Support for the following persistent storage options from OpenShift Container Platform 3.11 has changed in OpenShift Container Platform :

* GlusterFS is no longer supported.
* CephFS as a standalone product is no longer supported.
* Ceph RBD as a standalone product is no longer supported.

If you used one of these in OpenShift Container Platform 3.11, you must choose a different persistent storage option for full support in OpenShift Container Platform .

For more information, see Understanding persistent storage.

==== Migration of in-tree volumes to CSI drivers

OpenShift Container Platform 4 is migrating in-tree volume plugins to their Container Storage Interface (CSI) counterparts. In OpenShift Container Platform , CSI drivers are the new default for the following in-tree volume types:

* Amazon Web Services (AWS) Elastic Block Storage (EBS)
* Azure Disk
* Azure File
* {gcp-full} Persistent Disk (GCP PD)
* OpenStack Cinder
* VMware vSphere
+
[NOTE]
====
As of OpenShift Container Platform 4.13, VMware vSphere is not available by default. However, you can opt into VMware vSphere.
====

All aspects of volume lifecycle, such as creation, deletion, mounting, and unmounting, is handled by the CSI driver.

For more information, see CSI automatic migration.

[id="migration-preparing-networking"]
=== Networking considerations

Review the following networking changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform .

==== Network isolation mode

The default network isolation mode for OpenShift Container Platform 3.11 was `ovs-subnet`, though users frequently switched to use `ovn-multitenant`. The default network isolation mode for OpenShift Container Platform  is controlled by a network policy.

If your OpenShift Container Platform 3.11 cluster used the `ovs-subnet` or `ovs-multitenant` mode, it is recommended to switch to a network policy for your OpenShift Container Platform  cluster. Network policies are supported upstream, are more flexible, and they provide the functionality that `ovs-multitenant` does. If you want to maintain the `ovs-multitenant` behavior while using a network policy in OpenShift Container Platform , follow the steps to configure multitenant isolation using network policy.

For more information, see About network policy.

==== OVN-Kubernetes as the default networking plugin in Red Hat OpenShift Networking

In OpenShift Container Platform 3.11, OpenShift SDN was the default networking plugin in Red Hat OpenShift Networking. In OpenShift Container Platform , OVN-Kubernetes is now the default networking plugin.

For more information on the removal of the OpenShift SDN network plugin and why it has been removed see OpenShiftSDN CNI removal in OCP 4.17.

For information on OVN-Kubernetes features that are similar to features in the OpenShift SDN plugin see:

* Configuring an egress IP address

* Configuring an egress firewall for a project

* Enabling multicast for a project

* Deploying an egress router pod in redirect mode

* Configuring multitenant isolation with network policy

[WARNING]
====
You should install OpenShift Container Platform 4 with the OVN-Kubernetes network plugin because it is not possible to upgrade a cluster to OpenShift Container Platform 4.17 or later if it is using the OpenShift SDN network plugin.
====

[id="migration-preparing-logging"]
=== Logging considerations

Review the following logging changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform .

==== Deploying OpenShift Logging

OpenShift Container Platform 4 provides a simple deployment mechanism for OpenShift Logging, by using a Cluster Logging custom resource.

==== Aggregated logging data

You cannot transition your aggregate logging data from OpenShift Container Platform 3.11 into your new OpenShift Container Platform 4 cluster.

==== Unsupported logging configurations

Some logging configurations that were available in OpenShift Container Platform 3.11 are no longer supported in OpenShift Container Platform .

[id="migration-preparing-security"]
=== Security considerations

Review the following security changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform .

==== Unauthenticated access to discovery endpoints

In OpenShift Container Platform 3.11, an unauthenticated user could access the discovery endpoints (for example, [x-]`/api/*` and [x-]`/apis/*`). For security reasons, unauthenticated access to the discovery endpoints is no longer allowed in OpenShift Container Platform . If you do need to allow unauthenticated access, you can configure the RBAC settings as necessary; however, be sure to consider the security implications as this can expose internal cluster components to the external network.

// TODO: Anything to xref to, or additional details?

==== Identity providers

Configuration for identity providers has changed for OpenShift Container Platform 4, including the following notable changes:

* The request header identity provider in OpenShift Container Platform  requires mutual TLS, where in OpenShift Container Platform 3.11 it did not.
* The configuration of the OpenID Connect identity provider was simplified in OpenShift Container Platform . It now obtains data, which previously had to specified in OpenShift Container Platform 3.11, from the provider's `/.well-known/openid-configuration` endpoint.

For more information, see Understanding identity provider configuration.

==== OAuth token storage format

Newly created OAuth HTTP bearer tokens no longer match the names of their OAuth access token objects. The object names are now a hash of the bearer token and are no longer sensitive. This reduces the risk of leaking sensitive information.

==== Default security context constraints

The `restricted` security context constraints (SCC) in OpenShift Container Platform 4 can no longer be accessed by any authenticated user as the `restricted` SCC in OpenShift Container Platform 3.11. The broad authenticated access is now granted to the `restricted-v2` SCC, which is more restrictive than the old `restricted` SCC. The `restricted` SCC still exists; users that want to use it must be specifically given permissions to do it.

For more information, see Managing security context constraints.

[id="migration-preparing-monitoring"]
=== Monitoring considerations

Review the following monitoring changes when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform . You cannot migrate Hawkular configurations and metrics to Prometheus.

==== Alert for monitoring infrastructure availability

The default alert that triggers to ensure the availability of the monitoring structure was called `DeadMansSwitch` in OpenShift Container Platform 3.11. This was renamed to `Watchdog` in OpenShift Container Platform 4. If you had PagerDuty integration set up with this alert in OpenShift Container Platform 3.11, you must set up the PagerDuty integration for the `Watchdog` alert in OpenShift Container Platform 4.

For more information, see Configuring alert routing for default platform alerts.
