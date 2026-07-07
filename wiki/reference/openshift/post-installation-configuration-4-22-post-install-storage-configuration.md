---
title: "Postinstallation storage configuration"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-post-install-storage-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/post-install-storage-configuration
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Postinstallation storage configuration

[id="post-install-storage-configuration"]
= Postinstallation storage configuration

After installing OpenShift Container Platform, you can further expand and customize your cluster to your requirements, including storage configuration.

By default, containers operate by using the ephemeral storage or transient local storage. The ephemeral storage has a lifetime limitation. To store the data for a long time, you must configure persistent storage. You can configure storage by using one of the following methods:

Dynamic provisioning:: You can dynamically provision storage on-demand by defining and creating storage classes that control different levels of storage, including storage access.

Static provisioning:: You can use Kubernetes persistent volumes to make existing storage available to a cluster. Static provisioning can support various device configurations and mount options.

[id="post-install-dynamic-provisioning"]
== Dynamic provisioning

Dynamic Provisioning allows you to create storage volumes on-demand, eliminating the need for cluster administrators to pre-provision storage. See Dynamic provisioning.

// include::modules/dynamic-provisioning-gluster-definition.adoc[leveloffset=+2]

// include::modules/dynamic-provisioning-ceph-rbd-definition.adoc[leveloffset=+2]

// Module included in the following assemblies:
//
// * post_installation_configuration/storage-configuration.adoc
// * scalability_and_performance/optimization/optimizing-storage.adoc

[id="recommended-configurable-storage-technology_{context}"]
= Recommended configurable storage technology

[role="_abstract"]
Review the recommended and configurable storage technologies for the given OpenShift Container Platform cluster application.

.Recommended and configurable storage technology
[options="header"]
|===
|Storage type|Block|File|Object

| ROX
| Yes
| Yes
| Yes

| RWX
| No
| Yes
| Yes

| Registry
| Configurable
| Configurable
| Recommended

| Scaled registry
| Not configurable
| Configurable
| Recommended

| Metrics
| Recommended
| Configurable
| Not configurable

| Elasticsearch Logging
| Recommended
| Configurable
| Not supported

| Loki Logging
| Not configurable
| Not configurable
| Recommended

| Apps
| Recommended
| Recommended
| Not configurable

|===

where:

`ROX`:: Specifies `ReadOnlyMany` access mode.

`ROX.Yes`:: Specifies that this access mode

`RWX`:: Specifies `ReadWriteMany` access mode.

`Metrics`:: Specifies Prometheus as the underlying technology used for metrics.

`Metrics.Configurable`:: For metrics, using file storage with the `ReadWriteMany` (RWX) access mode is unreliable. If you use file storage, do not configure the RWX access mode on any persistent volume claims (PVCs) that are configured for use with metrics.

`Elasticsearch Logging.Configurable`:: For logging, review the recommended storage solution in Configuring persistent storage for the log store section. Using NFS storage as a persistent volume or through NAS, such as Gluster, can corrupt the data. Therefore, NFS is not supported for Elasticsearch storage and LokiStack log store in OpenShift Container Platform Logging. You must use one persistent volume type per log store.

`Apps.Not configurable`:: Specifies that object storage is not consumed through PVs or PVCs of OpenShift Container Platform. Apps must integrate with the object storage REST API.

[NOTE]
====
A scaled registry is an {product-registry} where two or more pod replicas are running.
====

[id="post-install-deploy-OCS"]
== Deploy Red Hat OpenShift Data Foundation
// This section is sourced from storage/persistent_storage/persistent-storage-ocs.adoc

{rh-storage-first} is a provider of agnostic persistent storage for OpenShift Container Platform supporting file, block, and object storage, either in-house or in hybrid clouds. As a Red Hat storage solution, {rh-storage-first} is completely integrated with OpenShift Container Platform for deployment, management, and monitoring. For more information, see the {rh-storage-first} documentation.

[IMPORTANT]
====
{rh-storage} on top of Red Hat Hyperconverged Infrastructure (RHHI) for Virtualization, which uses hyperconverged nodes that host virtual machines installed with OpenShift Container Platform, is not a supported configuration. For more information about supported platforms, see the Red Hat OpenShift Data Foundation Supportability and Interoperability Guide.
====

// Module included in the following assemblies:
//
// * post_installation_configuration/storage-configuration.adoc

[options="header",cols="1,1"]
|===

|If you are looking for {rh-storage-first} information about...
|See the following {rh-storage-first} documentation:

|What's new, known issues, notable bug fixes, and Technology Previews
|OpenShift Data Foundation 4.12 Release Notes

|Supported workloads, layouts, hardware and software requirements, sizing and scaling recommendations
|Planning your OpenShift Data Foundation 4.12 deployment

|Instructions on deploying {rh-storage} to use an external Red Hat Ceph Storage cluster
|Deploying OpenShift Data Foundation 4.12 in external mode

|Instructions on deploying {rh-storage} to local storage on bare metal infrastructure
|Deploying OpenShift Data Foundation 4.12 using bare metal infrastructure

|Instructions on deploying {rh-storage} on Red Hat OpenShift Container Platform VMware vSphere clusters
|Deploying OpenShift Data Foundation 4.12 on VMware vSphere

|Instructions on deploying {rh-storage} using Amazon Web Services for local or cloud storage
|Deploying OpenShift Data Foundation 4.12 using Amazon Web Services

|Instructions on deploying and managing {rh-storage} on existing Red Hat OpenShift Container Platform {gcp-full} clusters
|Deploying and managing {rh-storage} 4.12 using {gcp-full}

|Instructions on deploying and managing {rh-storage} on existing Red Hat OpenShift Container Platform Azure clusters
|Deploying and managing OpenShift Data Foundation 4.12 using Microsoft Azure

|Instructions on deploying {rh-storage} to use local storage on {ibm-power-name} infrastructure
|Deploying OpenShift Data Foundation on {ibm-power-name}

|Instructions on deploying {rh-storage} to use local storage on {ibm-z-name} infrastructure
|Deploying OpenShift Data Foundation on {ibm-z-name} infrastructure

|Allocating storage to core services and hosted applications in {rh-storage-first}, including snapshot and clone
|Managing and allocating resources

|Managing storage resources across a hybrid cloud or multicloud environment using the Multicloud Object Gateway (NooBaa)
|Managing hybrid and multicloud resources

|Safely replacing storage devices for {rh-storage-first}
|Replacing devices

|Safely replacing a node in a {rh-storage-first} cluster
|Replacing nodes

|Scaling operations in {rh-storage-first}
|Scaling storage

|Monitoring a {rh-storage-first} 4.12 cluster
|Monitoring Red Hat OpenShift Data Foundation 4.12

|Resolve issues encountered during operations
|Troubleshooting OpenShift Data Foundation 4.12

|Migrating your OpenShift Container Platform cluster from version 3 to version 4
|Migration

|===
