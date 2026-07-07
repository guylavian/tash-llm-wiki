---
title: "Telco hub reference design specification"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-telco-hub-rds
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/telco-hub-rds
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Telco hub reference design specification

[id="telco-hub-ref-design-specs"]
= Telco hub reference design specification

The telco hub reference design specification (RDS) describes the configuration for a hub cluster that deploys and operates fleets of OpenShift Container Platform clusters in a telco environment.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_ran_du_ref_design_specs/telco-ran-du-rds.adoc
// * scalability_and_performance/telco_ref_design_specs/telco-ref-design-specs-overview.adoc
// * scalability_and_performance/telco_ref_design_specs/telco-hubs-rds.adoc

[id="telco-ran-core-ref-design-spec_{context}"]
= Reference design scope

[role="_abstract"]
The telco core, telco RAN and telco hub reference design specifications (RDS) capture the recommended, tested, and supported configurations to get reliable and repeatable performance for clusters running the telco core and telco RAN profiles.

Each RDS includes the released features and supported configurations that are engineered and validated for clusters to run the individual profiles.
The configurations provide a baseline OpenShift Container Platform installation that meets feature and KPI targets.
Each RDS also describes expected variations for each individual configuration.
Validation of each RDS includes many long duration and at-scale tests.

[NOTE]
====
The validated reference configurations are updated for each major Y-stream release of OpenShift Container Platform.
Z-stream patch releases are periodically re-tested against the reference configurations.
====

// Module included in the following assemblies:
// * scalability_and_performance/telco_ran_du_ref_design_specs/telco-ran-du-rds.adoc
// * scalability_and_performance/telco_ref_design_specs/telco-hubs-rds.adoc
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-deviations-from-the-ref-design_{context}"]
= Deviations from the reference design

[role="_abstract"]
Deviating from the validated telco core, telco RAN DU, and telco hub reference design specifications (RDS) can have significant impact beyond the specific component or feature that you change.
Deviations require analysis and engineering in the context of the complete solution.

[IMPORTANT]
====
All deviations from the RDS should be analyzed and documented with clear action tracking information.
Due diligence is expected from partners to understand how to bring deviations into line with the reference design.
This might require partners to provide additional resources to engage with Red Hat to work towards enabling their use case to achieve a best in class outcome with the platform.
This is critical for the supportability of the solution and ensuring alignment across Red Hat and with partners.
====

Deviation from the RDS can have some or all of the following consequences:

* It can take longer to resolve issues.
* There is a risk of missing project service-level agreements (SLAs), project deadlines, end provider performance requirements, and so on.
* Unapproved deviations may require escalation at executive levels.

[NOTE]
====
Red Hat prioritizes the servicing of requests for deviations based on partner engagement priorities.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-architecture-overview_{context}"]
= Hub cluster architecture overview

[role="_abstract"]
Use the features and components running on the management hub cluster to manage many other clusters in a hub-and-spoke topology.
The hub cluster provides a highly available and centralized interface for managing the configuration, lifecycle, and observability of the fleet of deployed clusters.

[NOTE]
====
All management hub functionality can be deployed on a dedicated OpenShift Container Platform cluster or as applications that are co-resident on an existing cluster.
====

Managed cluster lifecycle::
Using a combination of Day 2 Operators, the hub cluster provides the necessary infrastructure to deploy and configure the fleet of clusters by using a GitOps methodology.
Over the lifetime of the deployed clusters, further management of upgrades, scaling the number of clusters, node replacement, and other lifecycle management functions can be declaratively defined and rolled out.
You can control the timing and progression of the rollout across the fleet.

Monitoring::
+
--
The hub cluster provides monitoring and status reporting for the managed clusters through the Observability pillar of the {rh-rhacm} Operator.
This includes aggregated metrics, alerts, and compliance monitoring through the Governance policy framework.
--

The telco management hub reference design specification (RDS) and the associated reference custom resources (CRs) describe the telco engineering and QE validated method for deploying, configuring and managing the lifecycle of telco managed cluster infrastructure.
The reference configuration includes the installation and configuration of the hub cluster components on top of OpenShift Container Platform.

.Hub cluster reference design components
image::telco-hub-cluster-reference-design-components.png[]

.Hub cluster reference design architecture
image::telco-hub-cluster-rds-architecture.png[]

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-telco-management-cluster-use-model_{context}"]
= Telco management hub cluster use model

[role="_abstract"]
The hub cluster provides managed cluster installation, configuration, observability and ongoing lifecycle management for telco application and workload clusters.

[role="_additional-resources"]
.Additional resources
* For more information about core clusters or far edge clusters that host RAN distributed unit (DU) workloads, see the following:
** Telco core RDS
** Telco RAN DU RDS

* For more information about lifecycle management for the fleet of managed clusters see:
** Image-based upgrade for {sno} clusters
** Updating managed clusters with the {cgu-operator-full}
** Upgrading a telco core CNF cluster

* For more information about declarative cluster provisioning with {ztp} see:
** Installing managed clusters with {rh-rhacm} and SiteConfig resources

* For more information about observability metrics and alerts, see:
** Multicluster architecture
** Observability

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-scaling-targets_{context}"]
= Hub cluster scaling target

[role="_abstract"]
The resource requirements for the hub cluster are directly dependent on the number of clusters being managed by the hub, the number of policies used for each managed cluster, and the set of features that are configured in {rh-rhacm-first}.

The hub cluster reference configuration can support up to 3500 managed {sno} clusters under the following conditions:

* 10 {rh-rhacm} configuration policies (comprising 5 Red Hat-provided policies and up to 5 custom configuration policies) with hub-side templating bound to the 3500 clusters and configured with a 10 minute evaluation interval.
* Only the following {rh-rhacm} add-ons are enabled:
** Policy controller
** Observability with the default configuration

* You deploy managed clusters by using {ztp} in batches of up to 500 clusters at a time.

The reference configuration is also validated for deployment and management of a mix of managed cluster topologies.
The specific limits depend on the mix of cluster topologies, enabled {rh-rhacm} features, and so on.
In a mixed topology scenario, the reference hub configuration is validated with a combination of 1200 {sno} clusters, 400 compact clusters (3 nodes combined control plane and compute nodes), and 230 standard clusters (3 control plane and 2 worker nodes).

// Ref Jira ACM-17868 for scale results
A hub cluster conforming to this reference specification can support synchronization of 1000 single node `ClusterInstance` CRs for each ArgoCD application.
You can use multiple applications to achieve the maximum number of clusters supported by a single hub cluster.

[NOTE]
====
Specific dimensioning requirements are highly dependent on the cluster topology and workload.
For more information, see "Storage requirements".
Adjust cluster dimensions for the specific characteristics of your fleet of managed clusters.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-resource-utilization_{context}"]
= Hub cluster resource utilization

[role="_abstract"]
Resource utilization was measured for deploying hub clusters in the following scenario:

* Under reference load managing 3500 {sno} clusters.
* 3-node compact cluster for management hub running on dual socket bare-metal servers.
* Network impairment of 50 ms round-trip latency, 100 Mbps bandwidth limit and 0.02% packet loss.
* Observability was not enabled.
* Only local storage was used.

.Resource utilization values
[options="header"]
|====
|Metric |Peak Measurement
|OpenShift Platform CPU |106 cores (52 cores peak per node)
|OpenShift Platform memory |504 G (168 G peak per node)
//|Persistent storage |<pending data from scale test>
|====

[role="_additional-resources"]
.Additional resources

* Comparison of hub cluster and managed cluster templates

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-cluster-topology_{context}"]
= Hub cluster topology

[role="_abstract"]
In production environments, the OpenShift Container Platform hub cluster must be highly available to maintain high availability of the management functions.

Limits and requirements::
Use a highly available cluster topology for the hub cluster, for example:
* Compact (3 nodes combined control plane and compute nodes)
* Standard (3 control plane nodes + N compute nodes)

Engineering considerations::
* In non-production environments, a {sno} cluster can be used for limited hub cluster functionality.
* Certain capabilities, for example {rh-storage-first}, are not supported on {sno}.
In this configuration, some hub cluster features might not be available.
* The number of optional compute nodes can vary depending on the scale of the specific use case.
* Compute nodes can be added later as required.
* Consult the 4.21 release notes regarding the decrease in the default maximum open files soft limit for containers in this release.

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform architecture
* Postinstallation node tasks

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-networking_{context}"]
= Hub cluster networking

[role="_abstract"]
The reference hub cluster is designed to operate in a disconnected networking environment where direct access to the internet is not possible.
As with all OpenShift Container Platform clusters, the hub cluster requires access to an image registry hosting all OpenShift and Day 2 {olm-first} images.

The hub cluster supports dual-stack networking support for IPv6 and IPv4 networks.
IPv6 is typical in edge or far-edge network segments, while IPv4 is more prevalent for use with legacy equipment in the data center.

Limits and requirements::
+
--
* Regardless of the installation method, you must configure the following network types for the hub cluster:
** `clusterNetwork`
** `serviceNetwork`
** `machineNetwork`

* You must configure the following IP addresses for the hub cluster:
** `apiVIP`
** `ingressVIP`

[NOTE]
====
For the above networking configurations, some values are required, or can be auto-assigned, depending on the chosen architecture and DHCP configuration.
====

* You must use the default OpenShift Container Platform network provider OVN-Kubernetes.
* Networking between the managed cluster and hub cluster must meet the networking requirements in the {rh-rhacm-first} documentation, for example:
** Hub cluster access to managed cluster API service, Ironic Python agent, and baseboard management controller (BMC) port.
** Managed cluster access to hub cluster API service, ingress IP and control plane node IP addresses.
** Managed cluster BMC access to hub cluster control plane node IP addresses.
* An image registry must be accessible throughout the lifetime of the hub cluster.
** All required container images must be mirrored to the disconnected registry.
All OpenShift Container Platform releases and OLM Operator release images needed in your deployment must be mirrored to the registry.
You can see example mirroring configuration in the `imageset-config.yaml` resource. You must update this example YAML to include your required versions.
For deploying clusters, you can only use `ClusterImageSet` CRs that reference mirrored versions.
** The hub cluster must be configured to use a disconnected registry.
** The hub cluster cannot host its own image registry.
For example, the registry must be available in a scenario where a power failure affects all cluster nodes.
--
Engineering considerations::
* When deploying a hub cluster, ensure you define appropriately sized CIDR range definitions.

[role="_additional-resources"]
.Additional resources

* Installing a cluster in a disconnected environment
* Using Operator Lifecycle Manager on restricted networks
* Configuring the hub cluster to use a disconnected mirror registry
* CIDR range definitions
* Installing OpenShift Container Platform
* Networking in OpenShift Container Platform
* Networking in {rh-rhacm}
* Network configuration in {rh-rhacm}

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-memory-and-cpu-requirements_{context}"]
= Hub cluster memory and CPU requirements

[role="_abstract"]
The memory and CPU requirements of the hub cluster vary depending on the configuration of the hub cluster, the number of resources on the cluster, and the number of managed clusters.

Limits and requirements::
* Ensure that the hub cluster meets the underlying memory and CPU requirements for OpenShift Container Platform and {rh-rhacm-first}.

Engineering considerations::
+
--
* Before deploying a telco hub cluster, ensure that your cluster host meets cluster requirements.

For more information about scaling the number of managed clusters, see "Hub cluster scaling target".
--

[role="_additional-resources"]
.Additional resources

* Scaling your OpenShift Container Platform cluster and tuning performance in production environments
* Sizing your cluster

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-storage-requirements_{context}"]
= Hub cluster storage requirements

[role="_abstract"]
The total amount of storage required by the management hub cluster is dependant on the storage requirements for each of the applications deployed on the cluster.
The main components that require storage through highly available `PersistentVolume` resources are described in the following sections.

[NOTE]
====
The storage required for the underlying OpenShift Container Platform installation is separate to these requirements.
====

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-assisted-service_{context}"]
= Assisted Service

[role="_abstract"]
The Assisted Service is deployed with the multicluster engine and {rh-rhacm-first}.

[NOTE]
====
The following numbers are estimates.
Tune the values for more accurate results.
Add an engineering margin, for example +20%, to the results to account for potential estimation inaccuracies.
====

.Assisted Service storage requirements
[cols="1,2", options="header"]
|====
|Persistent volume resource
|Size (GB)

|`imageStorage`^[1]^
|30

|`filesystemStorage`^[2]^
|709

|`dataBaseStorage`^[3]^
|0.7
|====

[1][2] For more information, refer to the multicluster engine Operator documentation About enabling central infrastructure management.

[3] The `databaseStorage` value is an empirical estimate based on cluster topology, number of installation events, hardware profile, and configuration complexity. Based on empirical testing, estimate approximately 200 KB per host.

[role="_additional-resources"]
.Additional resources

* Enabling central infrastructure management in disconnected environments

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-acm-observability_{context}"]
= {rh-rhacm} Observability

[role="_abstract"]
Cluster Observability is provided by the multicluster engine and {rh-rhacm-first}.

* Observability storage needs several `PV` resources and an S3 compatible bucket storage for long-term retention of the metrics.
* Storage requirements calculation is complex and dependent on the specific workloads and characteristics of managed clusters.
Requirements for `PV` resources and the S3 bucket depend on many aspects including data retention, the number of managed clusters, managed cluster workloads, and so on.
* Estimate the required storage for observability by using the observability sizing calculator in the {rh-rhacm} capacity planning repository.
See the Red Hat Knowledgebase article Calculating storage need for MultiClusterHub Observability on telco environments for an explanation of using the calculator to estimate observability storage requirements.
The below table uses inputs derived from the telco RAN DU RDS and the hub cluster RDS as representative values.
[NOTE]
====
The following numbers are estimates.
Tune the values for more accurate results.
Add an engineering margin, for example +20%, to the results to account for potential estimation inaccuracies.

Storage resources depend on the number of replicas for each component.
You can configure the sizing for the Observability stack in the `MultiClusterObservability` custom resource.
The number of replicas scales with the sizing configuration.
The sizing values in this specification use the default size.
====

.Cluster requirements
[cols="42%,42%,16%",options="header"]
|====
|Capacity planner input
|Data source
|Example value

|Number of control plane nodes
|Hub cluster RDS (scale) and telco RAN DU RDS (topology)
|3500

|Number of additional worker nodes
|Hub cluster RDS (scale) and telco RAN DU RDS (topology)
|0

|Days for storage of data
|Hub cluster RDS
|15

|Total number of pods per cluster
|Telco RAN DU RDS
|120

|Number of namespaces (excluding OpenShift Container Platform)
|Telco RAN DU RDS
|4

|Number of metric samples per hour
|Default value
|12

|Number of hours of retention in receiver persistent volume (PV)
|Default value
|24
|====

With these input values, the sizing calculator as described in the Red Hat Knowledgebase article Calculating storage need for MultiClusterHub Observability on telco environments indicates the following storage needs:

.Storage requirements
[options="header"]
|====
2+|`alertmanager` PV 2+|`thanos receive` PV 2+|`thanos compact` PV

|*Per replica* |*Total* |*Per replica* |*Total* 2+|*Total*

|10 GiB |30 GiB |10 GiB |30 GiB 2+|100 GiB
|====

.Storage requirements
[options="header"]
|====
|`thanos rule` PV 2+|`thanos store` PV 2+|Object bucket^[1]^

|*Per replica* |*Total* |*Per replica* |*Total* |*Total*

|30 GiB |90 GiB |100 GiB |300 GiB |310 GiB
|====

[1] This value assumes downsampling is enabled. You cannot configure the object bucket size in the `MultiClusterObservability` CR. Ensure this storage capacity is available in your environment.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-storage-considerations_{context}"]
= Storage considerations

[role="_abstract"]
Limits and requirements::
+
--
* Minimum OpenShift Container Platform and {rh-rhacm-first} limits apply
* High availability should be provided through a storage backend.
The hub cluster reference configuration provides storage through {rh-storage-first}.
* Object bucket storage is provided through {rh-storage}.
--

Engineering considerations::
* Use SSD or NVMe disks with low latency and high throughput for etcd storage.
* You must use clean storage disks with {rh-storage}, including before a re-install procedure. See "ODF disks cleaning procedure" for further information.
* The storage solution for telco hub clusters is {rh-storage}.
** Local Storage Operator supports the storage class used by {rh-storage} to provide block, file, and object storage as needed by other components on the hub cluster.
* The Local Storage Operator `LocalVolume` configuration includes setting `forceWipeDevicesAndDestroyAllData: true` to support the reinstallation of hub cluster nodes where {rh-storage} has previously been used.

[role="_additional-resources"]
.Additional resources

* ODF disks cleaning procedure
* Persistent storage overview
* {rh-storage} architecture
* Persistent storage using local volumes
* Recommended etcd practices

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-git-repository_{context}"]
= Git repository

[role="_abstract"]
The telco management hub cluster supports a GitOps-driven methodology for installing and managing the configuration of OpenShift clusters for various telco applications.
This methodology requires an accessible Git repository that serves as the authoritative source of truth for cluster definitions and configuration artifacts.

Red Hat does not offer a commercially supported Git server.
An existing Git server provided in the production environment can be used.
Gitea and Gogs are examples of self-hosted Git servers that you can use.

The Git repository is typically provided in the production network external to the hub cluster.
In a large-scale deployment, multiple hub clusters can use the same Git repository for maintaining the definitions of managed clusters. Using this approach, you can easily review the state of the complete network.
As the source of truth for cluster definitions, the Git repository should be highly available and recoverable in disaster scenarios.

[NOTE]
====
For disaster recovery and multi-hub considerations, run the Git repository separately from the hub cluster.
====

Limits and requirements::
* A Git repository is required to support the {ztp} functions of the hub cluster, including installation, configuration, and lifecycle management of the managed clusters.
* The Git repository must be accessible from the management cluster.

Engineering considerations::
* The Git repository is used by the GitOps Operator to ensure continuous deployment and a single source of truth for the applied configuration.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-hub-cluster-openshift-deployment_{context}"]
= OpenShift Container Platform installation on the hub cluster

[role="_abstract"]
Description::
+
--
The reference method for installing OpenShift Container Platform for the hub cluster is through the Agent-based Installer.

Agent-based Installer provides installation capabilities without additional centralized infrastructure.
The Agent-based Installer creates an ISO image, which you mount to the server to be installed.
When you boot the server, OpenShift Container Platform is installed alongside optionally supplied extra manifests, such as {gitops-title} custom resources.

[NOTE]
====
You can also install OpenShift Container Platform in the hub cluster by using other installation methods.
====

If hub cluster functions are being applied to an existing OpenShift Container Platform cluster, the Agent-based Installer installation is not required.
The remaining steps to install Day 2 Operators and configure the cluster for these functions remains the same.
When OpenShift Container Platform installation is complete, the set of additional Operators and their configuration must be installed on the hub cluster.

The reference configuration includes all of these custom resources (CRs), which you can apply manually, for example:

[source,terminal]
----
$ oc apply -f <reference_cr>
----

You can also add the reference configuration to the Git repository and apply it using ArgoCD.

[NOTE]
====
If you apply the CRs manually, ensure you apply the CRs in the order of their dependencies.
For example, apply namespaces before Operators and apply Operators before configurations.
====
--

Limits and requirements::
* Agent-based Installer requires an accessible image repository containing all required OpenShift Container Platform and Day 2 Operator images.
* Agent-based Installer builds ISO images based on a specific OpenShift releases and specific cluster details.
Installation of a second hub requires a separate ISO image to be built.

Engineering considerations::
* Agent-based Installer provides a baseline OpenShift Container Platform installation.
You apply Day 2 Operators and other configuration CRs after the cluster is installed.
* The reference configuration supports Agent-based Installer installation in a disconnected environment.
* A limited set of additional manifests can be supplied at installation time.

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform installation overview
* Installing a cluster with customizations
* Preparing to install with the Agent-based Installer

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-hub-cluster-day-2-operators_{context}"]
= Day 2 Operators in the hub cluster

[role="_abstract"]
The management hub cluster relies on a set of Day 2 Operators to provide critical management services and infrastructure.
Use Operator versions that match the set of managed cluster versions in your fleet.

Install Day 2 Operators using {olm-first} and `Subscription` custom resources (CRs).
`Subscription` CRs identify the specific Day 2 Operator to install, the catalog in which the Operator is found, and the appropriate version channel for the Operator.
By default {olm} installs and attempt to keep Operators updated with the latest z-stream version available in the channel.
By default all Subscriptions are set with an `installPlanApproval: Automatic` value.
In this mode, {olm} automatically installs new Operator versions when they are available in the catalog and channel.

[NOTE]
====
Setting `installPlanApproval` to automatic exposes the risk of the Operator being updated outside of defined maintenance windows if the catalog index is updated to include newer Operator versions.
In a disconnected environment where you are building and maintaining a curated set of Operators and versions in the catalog, and if you follow a strategy of creating a new catalog index for updated versions, the risk of the Operators being inadvertently updated is largely removed.
However, if you want to further close this risk, the `Subscription` CRs can be set to `installPlanApproval: Manual` which prevents Operators from being updated without explicit administrator approval.
====

Limits and requirements::
* When upgrading a telco hub cluster, the versions of OpenShift Container Platform and Operators must meet the requirements of all relevant compatibility matrixes.

[role="_additional-resources"]
.Additional resources

* Red Hat Advanced Cluster Management for Kubernetes 2.11 Support Matrix
* OpenShift Operator lifecycles

* For more information about telco hub cluster update requirements, see:
** Recommended hub cluster specifications and managed cluster limits for {ztp}.
** Red Hat Advanced Cluster Management for Kubernetes 2.11 Support Matrix
** OpenShift Operator Life Cycles

* For more information about updating the hub cluster, see:
** Introduction to OpenShift updates
** Upgrading your hub cluster
** Updating {ztp}

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-observability_{context}"]
= Observability

[role="_abstract"]
The {rh-rhacm-first} multicluster engine Observability component provides centralized aggregation and visualization of metrics and alerts for all managed clusters.
To balance performance and data analysis, the monitoring service maintains a subset list of aggregated metrics that are collected at a downsampled interval.
The metrics can be accessed on the hub through a set of different preconfigured dashboards.

Observability installation::
The primary custom resource (CR) to enable and configure the observability service is the `MulticlusterObservability` CR, which defines the following settings:

* Configurable retention settings.
* Storage for the different components: `thanos receive`, `thanos compact`, `thanos rule`, `thanos store` sharding, `alertmanager`.
* The `metadata.annotations.mco-disable-alerting="true"` annotation that enables tuning for the monitoring configuration on managed clusters.
+
[NOTE]
====
Without this setting the Observability component attempts to configure the managed cluster monitoring configuration.
With this value set you can merge your desired configuration with the necessary Observability configuration of alert forwarding into the managed cluster monitoring `ConfigMap` object.
When the Observability service is enabled {rh-rhacm} will deploy to each managed cluster a workload to push metrics and alerts generated by local Monitoring to the hub cluster.
The metrics and alerts to be forwarded from the managed cluster to the hub, are defined by a `ConfigMap` CR in the `open-cluster-management-addon-observability` namespace.
You can also specify custom metrics. For more information, see Adding custom metrics.
====

Alertmananger configuration::
+
--
* The hub cluster provides an Observability Alertmanager that can be configured to push alerts to external systems, for example, email.
The Alertmanager is enabled by default.
* You must configure alert forwarding.
* When the Alertmanager is enabled but not configured, the hub Alertmanager does not forward alerts externally.
* When Observability is enabled, the managed clusters can be configured to send alerts to any endpoint including the hub Alertmanager.
* When a managed cluster is configured to forward alerts to external sources, alerts are not routed through the hub cluster Alertmanager.
* Alert state is available as a metric.
* When observability is enabled, the managed cluster alert states are included in the subset of metrics forwarded to the hub cluster and are available through Observability dashboards.
--

Limits and requirements::
* Observability requires persistent object storage for long-term metrics.
For more information, see "Storage requirements".

Engineering considerations::
* Forwarding of metrics is a subset of the full metric data.
It includes only the metrics defined in the `observability-metrics-allowlist` config map and any custom metrics added by the user.
* Metrics are forwarded at a downsampled rate.
Metrics are forwarded by taking the latest datapoint at a 5 minute interval (or as defined by the `MultiClusterObservability` CR configuration).
* A network outage may lead to a loss of metrics forwarded to the hub cluster during that interval.
This can be mitigated if metrics are also forwarded directly from managed clusters to an external metrics collector in the providers network.
Full resolution metrics are available on the managed cluster.
* In addition to default metrics dashboards on the hub, users may define custom dashboards.
* The reference configuration is sized based on 15 days of metrics storage by the hub cluster for 3500 {sno} clusters.
If longer retention or other managed cluster topology or sizing is required, the storage calculations must be updated and sufficient storage capacity be maintained.
For more information about calculating new values, see "Storage requirements".

[role="_additional-resources"]
.Additional resources

* For more information about observability, see:
** Exporting metrics to external endpoints
** Enabling the Observability service

* For more information about custom metrics, see Adding custom metrics

* For more information about forwarding alerts to other external systems, see Forwarding alerts

* For more information about CPU and memory requirements see: Observability pod capacity requests

* For more information about custom dashboards, see Using Grafana dashboards

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-managed-clusters-lifecycle-management_{context}"]
= Managed cluster lifecycle management

[role="_abstract"]
To provision and manage sites at the far edge of the network, use {ztp} in a hub-and-spoke architecture, where a single hub cluster manages many managed clusters.

Lifecycle management for spoke clusters can be divided into two different stages: cluster deployment, including OpenShift Container Platform installation, and cluster configuration.

[role="_additional-resources"]
.Additional resources

* Challenges of the network far edge

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-managed-cluster-deployment_{context}"]
= Managed cluster deployment

[role="_abstract"]
Description::
As of {rh-rhacm-first} 2.12, using the SiteConfig Operator is the recommended method for deploying managed clusters.
The SiteConfig Operator introduces a unified ClusterInstance API that decouples the parameters that define the cluster from the manner in which it is deployed.
The SiteConfig Operator uses a set of cluster templates that are instantiated using the data from a `ClusterInstance` custom resource (CR) to dynamically generate installation manifests.
Following the GitOps methodology, the `ClusterInstance` CR is sourced from a Git repository through ArgoCD.
The `ClusterInstance` CR can be used to initiate cluster installation by using either Assisted Installer, or the image-based installation available in multicluster engine.

Limits and requirements::
* The `SiteConfig` ArgoCD plugin which handles `SiteConfig` CRs is removed from OpenShift Container Platform 4.21.
From this release, use `ClusterInstance` CRs to define managed cluster deployments.
* An HTTP server hosting the root filesystem and RHCOS live ISO images is required for cluster deployment.
These images are release specific.
ISO images for each OpenShift Container Platform release to be deployed must be reachable by the hub cluster and each deployed spoke cluster.
Only include ISO images which exist on the HTTP server in the `AgentServiceConfig` CR.
* A container registry hosting all OpenShift Container Platform and day-2 OLM operator images must be reachable from all deployed spoke clusters.
The hub configuration includes Kustomize overlays which you can use to provide the TLS certificates and credentials for a disconnected container registry.

Engineering considerations::
* You must create a `Secret` CR with the login information for the cluster baseboard management controller (BMC).
This `Secret` CR is then referenced in the `SiteConfig` CR.
Integration with a secret store, such as Vault, can be used to manage the secrets.
* Besides offering deployment method isolation and unification of Git and non-Git workflows, the SiteConfig Operator provides better scalability, greater flexibility with the use of custom templates, and an enhanced troubleshooting experience.

[role="_additional-resources"]
.Additional resources

* SiteConfig
* ClusterInstance
* Creating the managed bare-metal host secrets

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-managed-cluster-updates-and-upgrades_{context}"]
= Managed cluster updates

[role="_abstract"]
Description::
+
--
You can upgrade versions of OpenShift Container Platform, Day 2 Operators, and managed cluster configurations, by declaring the required version in the `Policy` custom resources (CRs) that target the clusters to be upgraded.

Policy controllers periodically check for policy compliance.
If the result is negative, a violation report is created.
If the policy remediation action is set to `enforce` the violations are remediated according to the updated policy.
If the policy remediation action is set to `inform`, the process ends with a non-compliant status report and responsibility to initiate the upgrade is left to the user to perform during an appropriate maintenance window.

The {cgu-operator-first} extends {rh-rhacm-first} with features to manage the rollout of upgrades or configuration throughout the lifecycle of the fleet of clusters.
It operates in progressive, limited size batches of clusters.
When upgrades to OpenShift Container Platform or the Day 2 Operators are required, {cgu-operator} progressively rolls out the updates by stepping through the set of policies and switching them to an "enforce" policy to push the configuration to the managed cluster.

The custom resource (CR) that {cgu-operator} uses to build the remediation plan is the `ClusterGroupUpgrade` CR.

You can use image-based upgrade (IBU) with the Lifecycle Agent as an alternative upgrade path for the {sno} cluster platform version.
IBU uses an OCI image generated from a dedicated seed cluster to install {sno} on the target cluster.

{cgu-operator} uses the `ImageBasedGroupUpgrade` CR to roll out image-based upgrades to a set of identified clusters.
--

Limits and requirements::
* You can perform direct upgrades for {sno} clusters using image-based upgrade for OpenShift Container Platform `<4.y>` to `<4.y+2>`, and `<4.y.z>` to `<4.y.z+n>`.
* Image-based upgrade uses custom images that are specific to the hardware platform that the clusters are running on.
Different hardware platforms require separate seed images.

Engineering considerations::
* In edge deployments, you can minimize the disruption to managed clusters by managing the timing and rollout of changes.
Set all policies to `inform` to monitor compliance without triggering automatic enforcement.
Similarly, configure Day 2 Operator subscriptions to manual to prevent updates from occurring outside of scheduled maintenance windows.
* The recommended upgrade aproach for {sno} clusters is the image-based upgrade.
* For multi-node cluster upgrades, consider the following `MachineConfigPool` CR configurations to reduce upgrade times:

** Pause configuration deployments to nodes during a maintenance window by setting the `paused` field to `true`.
** Adjust the `maxUnavailable` field to control how many nodes in the pool can be updated simultaneously.
The `MaxUnavailable` field defines the percentage of nodes in the pool that can be simultaneously unavailable during a `MachineConfig` object update.
Set `maxUnavailable` to the maximum tolerable value.
This reduces the number of reboots in a cluster during upgrades which results in shorter upgrade times.
** Resume configuration deployments by setting the `paused` field to `false`. The configuration changes are applied in a single reboot.
* During cluster installation, you can pause `MachineConfigPool` CRs by setting the `paused` field to `true` and setting `maxUnavailable` to 100% to improve installation times.

[role="_additional-resources"]
.Additional resources

* Configuration policy YAML structure
* About the ClusterGroupUpgrade CR
* Understanding the image-based upgrade for {sno} clusters
* Performing an image-based upgrade for {sno} clusters using {ztp}

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-hub-disaster-recovery_{context}"]
= Hub cluster disaster recovery

[role="_abstract"]
Note that loss of the hub cluster does not typically create a service outage on the managed clusters.
Functions provided by the hub cluster will be lost, such as observability, configuration, lifecycle management updates being driven through the hub cluster, and so on.

Limits and requirements::

* Backup,restore and disaster recovery are offered by the cluster backup and restore Operator, which depends on the {oadp-first} Operator.

Engineering considerations::

* You can extend the cluster backup and restore operator to third party resources of the hub cluster based on your configuration.
* The cluster backup and restore operator is not enabled by default in {rh-rhacm-first}.
The reference configuration enables this feature.

[role="_additional-resources"]
.Additional resources

*  Business continuity

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-hub-components_{context}"]
= Hub cluster components

[role="_abstract"]

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-red-hat-advanced-cluster-management-rhacm_{context}"]
= {rh-rhacm-first}

[role="_abstract"]
New in this release::

* No reference design updates in this release.

Description::
+
--
{rh-rhacm-first} provides multicluster engine installation and ongoing lifecycle management functionality for deployed clusters.
You can manage cluster configuration and upgrades declaratively by applying `Policy` custom resources (CRs) to clusters during maintenance windows.

{rh-rhacm} provides functionality such as the following:

* Zero touch provisioning (ZTP) and ongoing scaling of clusters using the multicluster engine component in {rh-rhacm}.
* Configuration, upgrades, and cluster status through the {rh-rhacm} policy controller.
* During managed cluster installation, {rh-rhacm} can apply labels to individual nodes as configured through the `ClusterInstance` CR.
* The {cgu-operator-full} component of {rh-rhacm} provides phased rollout of configuration changes to managed clusters.
* The {rh-rhacm} multicluster engine Observability component provides selective monitoring, dashboards, alerts, and metrics.
The recommended method for {sno} cluster installation is the image-based installation method in multicluster engine, which uses the `ClusterInstance` CR for cluster definition.

The recommended method for {sno} upgrade is the image-based upgrade method.

[NOTE]
====
The {rh-rhacm} multicluster engine Observability component brings you a centralized view of the health and status of all the managed clusters.
By default, every managed cluster is enabled to send metrics and alerts, created by their {cmo-first}, back to Observability.
For more information, see "Observability".
====
--

Limits and requirements::

* For more information about limits on number of clusters managed by a single hub cluster, see "Telco management hub cluster use model".
* The number of managed clusters that can be effectively managed by the hub depends on various factors, including:
** Resource availability at each managed cluster
** Policy complexity and cluster size
** Network utilization
** Workload demands and distribution
* The hub and managed clusters must maintain sufficient bidirectional connectivity.
  Refer to the {rh-rhacm} Hub Network Configuration for further details.

Engineering considerations::
* You can configure the cluster backup and restore Operator to include third-party resources.
* The use of {rh-rhacm} hub side templating when defining configuration through policy is strongly recommended.
This feature reduces the number of policies needed to manage the fleet by enabling for each cluster or for each group. For example, regional or hardware type content to be templated in a policy and substituted on cluster or group basis.
* Managed clusters typically have some number of configuration values which are specific to an individual cluster.
These should be managed using {rh-rhacm} policy hub side templating with values pulled from `ConfigMap` CRs based on the cluster name.

[role="_additional-resources"]
.Additional resources

* * Hub Network Configuration
* Multi Cluster Engine
* Governance
* {cgu-operator-full}
* MultiClusterHub Observability
* Business continuity
* Performance and scalability
* Network configuration

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-topology-aware-lifecycle-manager-talm_{context}"]
= {cgu-operator-full}

[role="_abstract"]
New in this release::

* No reference design updates in this release.

Description::
+
--
{cgu-operator} is an Operator that runs only on the hub cluster for managing how changes like cluster upgrades, Operator upgrades, and cluster configuration are rolled out to the network. {cgu-operator} supports the following features:

* Progressive rollout of policy updates to fleets of clusters in user configurable batches.
* Per-cluster actions add `ztp-done` labels or other user-configurable labels following configuration changes to managed clusters.
* {cgu-operator} supports optional pre-caching of OpenShift Container Platform, {olm} Operator, and additional images to {sno} clusters before initiating an upgrade. The pre-caching feature is not applicable when using the recommended image-based upgrade method for upgrading {sno} clusters.
** Specifying optional pre-caching configurations with `PreCachingConfig` CRs.

** Configurable image filtering to exclude unused content.

** Storage validation before and after pre-caching, using defined space requirement parameters.
--

Limits and requirements::

* {cgu-operator} supports concurrent cluster upgrades in batches of 500.
* Pre-caching is limited to {sno} cluster topology.

Engineering considerations::

* The `PreCachingConfig` custom resource (CR) is optional. You do not need to create it if you want to pre-cache platform-related images only, such as OpenShift Container Platform and {olm}.
* {cgu-operator} supports the use of hub-side templating with Red Hat Advanced Cluster Management policies.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-gitops-operator-and-ztp-plugins_{context}"]
= GitOps Operator and {ztp}

[role="_abstract"]
New in this release::
* No reference design updates in this release

Description::
GitOps Operator and {ztp} provide a GitOps-based infrastructure for managing cluster deployment and configuration.
Cluster definitions and configurations are maintained as a declarative state in Git.
You can apply `ClusterInstance` custom resources (CRs) to the hub cluster where the `SiteConfig` Operator renders them as installation CRs.
In earlier releases, a {ztp} plugin supported the generation of installation CRs from `SiteConfig` CRs.
This plugin is now deprecated.
A separate {ztp} plugin is available to enable automatic wrapping of configuration CRs into policies based on the `PolicyGenerator` or the `PolicyGenTemplate` CRs.
+
You can deploy and manage multiple versions of OpenShift Container Platform on managed clusters by using the baseline reference configuration CRs.
You can use custom CRs alongside the baseline CRs.
To maintain multiple per-version policies simultaneously, use Git to manage the versions of the source and policy CRs by using the `PolicyGenerator` or the `PolicyGenTemplate` CRs.

Limits and requirements::
* To ensure consistent and complete cleanup of managed clusters and their associated resources during cluster or node deletion, you must configure ArgoCD to use background deletion mode.

Engineering considerations::
* To avoid confusion or unintentional overwrite when updating content, use unique and distinguishable names for custom CRs in the `source-crs` directory and extra manifests.
* Keep reference source CRs in a separate directory from custom CRs.
This facilitates easy update of reference CRs as required.
* To help with multiple versions, keep all source CRs and policy creation CRs in versioned Git repositories to ensure consistent generation of policies for each OpenShift Container Platform version.

[role="_additional-resources"]
.Additional resources

* ClusterInstance CR
* PolicyGenTemplate CRs
* {ztp} version independence

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-local-storage-operator_{context}"]
= Local Storage Operator

[role="_abstract"]
New in this release::
* No reference design updates in this release

Description::
You can create persistent volumes that can be used as `PVC` resources by applications with the Local Storage Operator.
The number and type of `PV` resources that you create depends on your requirements.

Engineering considerations::
* Create backing storage for `PV` CRs before creating the persistent volume.
This can be a partition, a local volume, LVM volume, or full disk.
* Refer to the device listing in `LocalVolume` CRs by the hardware path used to access each device to ensure correct allocation of disks and partitions, for example, `/dev/disk/by-path/<id>`.
Logical names (for example, `/dev/sda`) are not guaranteed to be consistent across node reboots.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-openshift-data-foundation_{context}"]
= {rh-storage-first}

[role="_abstract"]
New in this release::
* No reference design updates in this release

Description::
{rh-storage-first} provides file, block, and object storage services to the hub cluster.

Limits and requirements::
* {odf-first} in internal mode requires the Local Storage Operator to define a storage class which will provide the necessary underlying storage.
* When doing the planning for a telco management cluster, consider the {odf-short} infrastructure and networking requirements.
* Dual stack support is limited.
{odf-short} IPv4 is supported on dual-stack clusters.

Engineering considerations::
* Address capacity warnings promptly as recovery can be difficult in case of storage capacity exhaustion, see Capacity planning.

[role="_additional-resources"]
.Additional resources

* Support OpenShift dual stack with {rh-storage} using IPv4
* Infrastructure requirements
* Network requirements
* Storage cluster deployment approaches

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-logging_{context}"]
= Logging

[role="_abstract"]
New in this release::
* No reference design updates in this release

Description::
Use the Cluster Logging Operator to collect and ship logs off the node for remote archival and analysis.
The reference configuration uses Kafka to ship audit and infrastructure logs to a remote archive.

Limits and requirements::
* The reference configuration does not include local log storage.
* The reference configuration does not include aggregation of managed cluster logs at the hub cluster.

Engineering considerations::
* The impact of cluster CPU use is based on the number or size of logs generated and the amount of log filtering configured.
* The reference configuration does not include shipping of application logs.
The inclusion of application logs in the configuration requires you to evaluate the application logging rate and have sufficient additional CPU resources allocated to the reserved set.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-oadp-operator_{context}"]
= {oadp-full}

[role="_abstract"]
New in this release::
* No reference design updates in this release

Description::
+
--
The {oadp-first} Operator is automatically installed and managed by {rh-rhacm-first} when the backup feature is enabled.

The {oadp-short} Operator facilitates the backup and restore of workloads in OpenShift Container Platform clusters.
Based on the upstream open source project Velero, it allows you to backup and restore all Kubernetes resources for a given project, including persistent volumes.

While it is not mandatory to have it on the hub cluster, it is highly recommended for cluster backup, disaster recovery and high availability architecture for the hub cluster.
The {oadp-short} Operator must be enabled to use the disaster recovery solutions for {rh-rhacm}.
The reference configuration enables backup (OADP) through the `MultiClusterHub` custom resource (CR) provided by the {rh-rhacm} Operator.
--

Limits and requirements::

* Only one version of {oadp-short} can be installed on a cluster.
The version installed by {rh-rhacm} must be used for {rh-rhacm} disaster recovery features.
Engineering considerations::

* No engineering consideration updates in this release.

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-cert-manager-operator_{context}"]
= cert-manager Operator

New in this release::
* No reference design updates in this release.

Description::
+
--
The cert-manager Operator for OpenShift Container Platform manages the lifecycle of TLS certificates for cluster components and workloads.
The cert-manager Operator automates certificate issuance, renewal, and rotation, eliminating manual certificate management.
The reference configuration includes the cert-manager Operator to optionally manage certificates for the API server and ingress controller endpoints.

You can use {rh-rhacm} `CertificatePolicy` resources to monitor certificate health across all managed clusters.
--

Limits and requirements::

* The reference configuration includes only the ACME DNS01 challenge type for platform certificate issuance.

Engineering considerations::

* Use {rh-rhacm} `CertificatePolicy` resources on the hub cluster to monitor certificate expiration and compliance across managed clusters.
* Optionally, configure a `PrometheusRule` on the hub cluster to generate alerts based on policy compliance status.

// Module included in the following assemblies:
//
// * scalability-and-performance/telco-hub-rds.adoc

[id="telco-hub-rds-container_{context}"]
= Extracting the telco hub reference design configuration CRs

[role="_abstract"]
You can extract the complete set of custom resources (CRs) for the telco hub profile from the `openshift-telco-hub-rds-rhel9` container image.
The container image has both the required CRs, and the optional CRs, for the telco hub profile.

.Prerequisites

* You have installed `podman`.

.Procedure

. Log on to the container image registry with your credentials by running the following command:
+
[source,terminal]
----
$ podman login registry.redhat.io
----

. Extract the content from the `openshift-telco-hub-rds-rhel9` container image by running the following commands:
+
[source,terminal]
----
$ mkdir -p ./out
----
+
[source,terminal]
----
$ podman run -it registry.redhat.io/openshift4/openshift-telco-hub-rds-rhel9:v4.22 | base64 -d | tar xv -C out
----

.Verification

* The `out` directory has the following directory structure. You can view the telco hub CRs in the `out/telco-hub-rds/` directory by running the following command:
+
[source,terminal]
----
$ tree -L 4 out/telco-hub-rds/
----
+
.Example output
[source,text]
----
out/telco-hub-rds/
├── configuration
│   ├── example-overlays-config
│   │   ├── acm
│   │   │   ├── acmMirrorRegistryCM-patch.yaml
│   │   │   ├── kustomization.yaml
│   │   │   ├── options-agentserviceconfig-patch.yaml
│   │   │   └── storage-mco-patch.yaml
│   │   ├── gitops
│   │   │   ├── argocd-tls-certs-cm-patch.yaml
│   │   │   ├── init-argocd-app.yaml
│   │   │   └── kustomization.yaml
│   │   ├── logging
│   │   │   ├── cluster-log-forwarder-patch.yaml
│   │   │   ├── kustomization.yaml
│   │   │   └── README.md
│   │   ├── lso
│   │   │   ├── kustomization.yaml
│   │   │   └── local-storage-disks-patch.yaml
│   │   ├── odf
│   │   │   ├── kustomization.yaml
│   │   │   └── options-storage-cluster.yaml
│   │   └── registry
│   │       ├── catalog-source-image-patch.yaml
│   │       ├── idms-operator-mirrors-patch.yaml
│   │       ├── idms-release-mirrors-patch.yaml
│   │       ├── itms-generic-mirrors-patch.yaml
│   │       ├── itms-release-mirrors-patch.yaml
│   │       ├── kustomization.yaml
│   │       └── registry-ca-patch.yaml
│   ├── kustomization.yaml
│   ├── README.md
│   └── reference-crs
│       ├── kustomization.yaml
│       ├── optional
│       │   ├── logging
│       │   ├── lso
│       │   └── odf-internal
│       └── required
│           ├── acm
│           ├── gitops
│           ├── registry
│           └── talm
├── install
│   ├── mirror-registry
│   │   ├── imageset-config.yaml
│   │   └── README.md
│   └── openshift
│       ├── agent-config.yaml
│       └── install-config.yaml
└── scripts
    └── check_current_versions.sh
----

// Module included in the following assemblies:
//
// * scalability_and_performance/telco-hub-rds.adoc

[id="using-cluster-compare-telco_hub_{context}"]
= Comparing a cluster with the {rds} reference configuration

After you deploy a {rds} cluster, you can use the `cluster-compare` plugin to assess the cluster's compliance with the {rds} reference design specifications (RDS). The `cluster-compare` plugin is an OpenShift CLI (`oc`) plugin. The plugin uses a {rds} reference configuration to validate the cluster with the {rds} custom resources (CRs).

The plugin-specific reference configuration for {rds} is packaged in a container image with the {rds} CRs.

For further information about the `cluster-compare` plugin, see "Understanding the cluster-compare plugin".

The following example shows how to compare the configuration of a cluster to the {rds} reference configuration by using `must-gather` data.

[NOTE]
====
When comparing a cluster to the {rds} reference configuration by using `must-gather` data, you must use the `--all-images` flag when generating the `must-gather` data. You must also collect cluster-scoped resource information, as well as Operator and registry configurations. Without this data, the plugin might report false positives.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

* You have credentials to access the `registry.redhat.io` container image registry.

* You installed the `cluster-compare` plugin.

* You extracted the {rds} reference configuration from the `openshift-telco-hub-rds-rhel9` container image.

.Procedure

. Collect data about your cluster by running the `must-gather` command with the `--all-images` flag:
+
[source,terminal]
----
$ oc adm must-gather --all-images
----
+
* The `--all-images` flag ensures that the `must-gather` command collects all the data required by the {rds} reference configuration.

. Collect cluster-scoped resource information by running the following command:
+
[source,terminal]
----
$ oc adm inspect clusterroles,clusterrolebindings,namespaces,nodes --dest-dir=./cluster-scoped
----

. Collect Operator and registry configurations by running the following command:
+
[source,terminal]
----
$ oc adm inspect imagedigestmirrorset,imagetagmirrorset,catalogsource,clusterserviceversion,customresourcedefinition,operatorhub --dest-dir=./cluster-config
----

. Compare the collected data to a reference configuration by running the following command:
+
[source,terminal]
----
$ oc cluster-compare -r <path_to_reference_config>/metadata.yaml -f "must-gather*/*/cluster-scoped-resources","must-gather*/*/namespaces","cluster-scoped","cluster-config" -R
----
+
** `-r` specifies a path to the `metadata.yaml` file of the reference configuration. You can specify a local directory or a URI.
** `-f` specifies the path to the `must-gather` data directory. You can specify a local directory or a URI. This example restricts the comparison to the relevant cluster configuration directories in the `must-gather` data, and also the `cluster-config` and `cluster-scoped` directories you created.
** `-R` searches the target directories recursively.
+
.Example output
[source,terminal]
----
W0309 13:08:01.564387   29400 compare.go:476] Reference Contains Templates With Types (kind) Not Supported By Cluster: AgentServiceConfig, AppProject, Application, Certificate, ClusterIssuer, ClusterLogForwarder, LocalVolume, ManagedClusterSetBinding, MultiClusterEngine, MultiClusterHub, MultiClusterObservability, ObjectBucketClaim, Placement, PlacementBinding, Policy, StorageCluster
...

**********************************

Cluster CR: operator.openshift.io/v1_IngressController_openshift-ingress-operator_default
Reference File: optional/cert-manager/ingressControllerConfig.yaml
Diff Output: diff -u -N /tmp/MERGED-3542158379/operator-openshift-io-v1_ingresscontroller_openshift-ingress-operator_default /tmp/LIVE-285048405/operator-openshift-io-v1_ingresscontroller_openshift-ingress-operator_default
--- /tmp/MERGED-3542158379/operator-openshift-io-v1_ingresscontroller_openshift-ingress-operator_default	2026-03-09 13:09:32.985703558 +0000
+++ /tmp/LIVE-285048405/operator-openshift-io-v1_ingresscontroller_openshift-ingress-operator_default	2026-03-09 13:09:32.985703558 +0000
@@ -4,5 +4,17 @@
   name: default
   namespace: openshift-ingress-operator
 spec:
-  defaultCertificate:
-    name: ingress-wildcard-cert
+  clientTLS:
+    clientCA:
+      name: ""
+    clientCertificatePolicy: ""
+  closedClientConnectionPolicy: Continue
+  httpCompression: {}
+  httpEmptyRequestsPolicy: Respond
+  httpErrorCodePages:
+    name: ""
+  idleConnectionTerminationPolicy: Immediate
+  replicas: 2
+  tuningOptions:
+    reloadInterval: 0s
+  unsupportedConfigOverrides: null

**********************************

Summary
CRs with diffs: 5/5
CRs in reference missing from the cluster: 43
optional-cert-manager:
  cert-manager-apiserver:
    Missing CRs:
    - optional/cert-manager/apiServerCertificate.yaml
  cert-manager-ingress:
    Missing CRs:
    - optional/cert-manager/ingressCertificate.yaml

...

No CRs are unmatched to reference CRs
Metadata Hash: 6297bc738df2373467cc6f5acc3a6aa23f3c3d0b0ce2ac23887d7914a6241d92
No patched CRs

----
+
* `Cluster CR` shows the CR with a difference from the corresponding template.
* `Reference File` shows the template file that the tool uses in its comparison with the cluster CR. The output in Linux diff format shows the difference between the template and the cluster CR.
* `CRs with diffs` shows the number of CRs in the comparison with differences from the corresponding templates.
* `CRs in reference missing from the cluster` shows the number of CRs represented in the reference configuration, but missing from the live cluster.
* `Missing CRs` shows the list of CRs represented in the reference configuration, but missing from the live cluster.
* `No CRs are unmatched to reference CRs` indicates that all CRs in the cluster matched to a corresponding template in the reference configuration.
* `Metadata Hash` shows the metadata hash that identifies the reference configuration.
* `No patched CRs` indicates that there are no patched CRs in the cluster.

// Module included in the following assemblies:
//
// * scalability-and-performance/telco-hub-rds.adoc

[id="hub-cluster-ref-config-crs_{context}"]
= Hub cluster reference configuration CRs

[role="_abstract"]
The following sections briefly describe each custom resource (CR) for the telco management hub reference configuration in 4.21.

// Module included in the following assemblies:
//
// * scalability-and-performance/telco-hub-rds.adoc

[id="advanced-cluster-management-crs_{context}"]
= {rh-rhacm-first} CRs

[role="_abstract"]
The following custom resources (CRs) configure {rh-rhacm-first} for the telco hub cluster.

.{rh-rhacm} CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
{rh-rhacm},`acmAgentServiceConfig.yaml`,Creates a policy to manage copying data from an object bucket claim into a secret for Observability to connect to Thanos.,No
{rh-rhacm},`acmMCE.yaml`,Defines the MultiCluster Engine configuration required by ACM.,No
{rh-rhacm},`acmMCH.yaml`,"Configures a `MultiClusterHub` CR with high availability, enabling various components and specifying installation settings.",No
{rh-rhacm},`acmMirrorRegistryCM.yaml`,Defines the SSL certificates and mirror registry configuration for various Red Hat and OpenShift Container Platform registries used by the `multicluster-engine` in the `multicluster-engine` namespace.,No
{rh-rhacm},`acmNS.yaml`,Defines the `open-cluster-management` namespace with a label to enable cluster monitoring.,No
{rh-rhacm},`acmOperGroup.yaml`,"Defines an OperatorGroup for the `open-cluster-management` namespace, targeting the same namespace.",No
{rh-rhacm},`acmPerfSearch.yaml`,Configures search for Open Cluster Management by defining various parameters and API settings.,No
{rh-rhacm},`acmProvisioning.yaml`,Configures a provisioning resource in the metal3.io/v1alpha1 API version to watch all namespaces.,No
{rh-rhacm},`acmSubscription.yaml`,Subscribes to the {rh-rhacm} Operator using automatic install plan approval.,No
{rh-rhacm},`observabilityMCO.yaml`,Configures `MultiClusterObservability` for managing observability and alerting across multiple clusters.,No
{rh-rhacm},`observabilityNS.yaml`,Creates an `open-cluster-management-observability` namespace.,No
{rh-rhacm},`observabilityOBC.yaml`,Creates an `ObjectBucketClaim` CR in the `open-cluster-management-observability` namespace.,No
{rh-rhacm},`observabilitySecret.yaml`,Creates a Secret CR in the `open-cluster-management-observability` namespace for storing Docker configuration details.,No
{rh-rhacm},`observabilityRoutePolicy.yaml`,Policy to propagate {rh-rhacm} observability route to the managed cluster.,No
{rh-rhacm},`pullSecretMCSB.yaml`,Creates a `ManagedClusterSetBinding` CR for the pull secret policy.,No
{rh-rhacm},`pullSecretPlacementBinding.yaml`,Creates the `PlacementBinding` CR needed for the pull secret policy.,No
{rh-rhacm},`pullSecretPlacement.yaml`,Creates the `Placement` CR against local cluster needed for the pull secret policy.,No
{rh-rhacm},`pullSecretPolicy.yaml`,Creates a policy to copy the global pull secret into observability namespaces.,No
{rh-rhacm},`thanosSecretPlacementBinding.yaml`,Creates the `PlacementBinding` CR needed for the thanos secret policy.,No
{rh-rhacm},`thanosSecretPlacement.yaml`,Creates the `Placement` CR against local cluster needed for the thanos secret policy.,No
{rh-rhacm},`thanosSecretPolicy.yaml`,Creates a policy to copy data from an object bucket claim into a secret for observability to connect to Thanos.,No
{cgu-operator},`talmSubscription.yaml`,Creates a `Subscription` CR for {cgu-operator}.,No
|====

// Module included in the following assemblies:
//
// *

[id="storage-crs_{context}"]
= Storage reference CRs

[role="_abstract"]
The following custom resources (CRs) configure storage for the telco hub cluster.

.Storage CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
Local Storage Operator,`lsoLocalVolume.yaml`,Defines a `LocalVolume` CR specifying local storage configuration and node selection criteria.,Yes
Local Storage Operator,`lsoNS.yaml`,Defines the `openshift-local-storage` namespace.,Yes
Local Storage Operator,`lsoOperatorGroup.yaml`,Defines an `OperatorGroup` for the `openshift-local-storage` namespace.,Yes
Local Storage Operator,`lsoSubscription.yaml`,Defines a `Subscription` CR for the Local Storage Operator.,Yes
{rh-storage},`odfNS.yaml`,Defines the `openshift-storage namespace` with specific annotations and labels for workload management and cluster monitoring.,Yes
{rh-storage},`odfOperatorGroup.yaml`,Defines an `OperatorGroup` for the `openshift-storage` namespace.,Yes
{rh-storage},`odfReady.yaml`,Defines a resource to verify readiness of the ODF deployment.,Yes
{rh-storage},`odfSubscription.yaml`,"Configures an OpenShift Container Platform subscription to the {rh-storage-first} Operator, specifying installation details such as the Operator's name, namespace, channel, and approval strategy.",Yes
{rh-storage},`storageCluster.yaml`,"Defines a `StorageCluster` CR with specific resource requests and limits, storage device sets, and annotations for Argo CD synchronization.",No
|====

// Module included in the following assemblies:
//
// * scalability-and-performance/telco-hub-rds.adoc

[id="gitops-ztp-crs_{context}"]
= {ztp-first} reference CRs

[role="_abstract"]
The following custom resources (CRs) configure {ztp-first} for the telco hub cluster.

.{ztp} CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
GitOps Operator,`argocd-ssh-known-hosts-cm.yaml`,Defines a `ConfigMap` CR to store SSH known hosts used by ArgoCD in a disconnected environment.,No
GitOps Operator,`addPluginsMCSB.yaml`,Defines the `ManagedClusterSetBinding` CR for policy used to patch GitOps operator.,No
GitOps Operator,`addPluginsPolicyNS.yaml`,Namespace for GitOps plugin policy.,No
GitOps Operator,`addPluginsPolicyPlacementBinding.yaml`,Defines the `PlacementBinding` CR for the GitOps plugin policy.,No
GitOps Operator,`addPluginsPolicyPlacement.yaml`,Defines the `Placement` CR against local cluster for the GitOps plugin policy.,No
GitOps Operator,`addPluginsPolicy.yaml`,Defines a policy to add ArgoCD custom plugins to the GitOps controller.,No
GitOps Operator,`argocd-application.yaml`,Defines the ArgoCD Application for GitOps management.,No
GitOps Operator,`argocd-tls-certs-cm.yaml`,Defines a `ConfigMap` CR for ArgoCD TLS certificate management.,No
GitOps Operator,`clusterrole.yaml`,Defines the `ClusterRole` CR that grants permissions to the GitOps Operator.,No
GitOps Operator,`clusterrolebinding.yaml`,Binds the `ClusterRole` CR to the ArgoCD controller `ServiceAccount` CR.,No
GitOps Operator,`gitopsNS.yaml`,Defines an `openshift-gitops-operator` namespace with a label for cluster monitoring.,No
GitOps Operator,`gitopsOperatorGroup.yaml`,Defines an OperatorGroup in the `openshift-gitops-operator` namespace with a default upgrade strategy.,No
GitOps Operator,`gitopsSubscription.yaml`,"Defines a subscription for the OpenShift Container Platform GitOps Operator, specifying automatic install plan approval and source details.",No
GitOps Operator,`ztp-repo.yaml`,Defines the Git repository for ZTP manifests and configurations.,No
GitOps applications,`app-project.yaml`,Defines an ArgoCD `AppProject` CR specifying resource whitelists and destination rules for cluster and namespace resources.,No
GitOps applications,`clusters-app.yaml`,Defines a namespace and an ArgoCD application for managing the deployment of cluster configurations from the specified Git repository.,No
GitOps applications,`gitops-cluster-rolebinding.yaml`,Defines a `ClusterRoleBinding` CR that grants the `cluster-admin` role to the openshift-gitops-argocd-application-controller service account in the `openshift-gitops` namespace.,No
GitOps applications,`gitops-policy-rolebinding.yaml`,Binds the `cluster-manager-admin` cluster role to the ArgoCD application controller `ServiceAccount` CR.,No
GitOps applications,`kustomization.yaml`,"Defines a Kustomization configuration for the {ztp} application installations, listing various YAML resources to be included.",No
GitOps applications,`policies-app-project.yaml`,"Defines an Argo CD AppProject resource, specifying cluster and namespace resource whitelists and destinations.",No
GitOps applications,`policies-app.yaml`,Defines the ArgoCD `Application` CR for policy management.,No
GitOps applications,`extra-manifests-policy.yaml`,Defines policy to manage extra configuration manifests provided during Day 0 installation.,No
|====

// Module included in the following assemblies:
//
// *

[id="logging-crs_{context}"]
= Logging reference CRs

[role="_abstract"]
The following custom resources (CRs) configure logging for the telco hub cluster.

.Logging CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
Cluster Logging Operator,`clusterLogForwarder.yaml`,Defines the `ClusterLogForwarder` CR to send logs to configured outputs.,Yes
Cluster Logging Operator,`clusterLogNS.yaml`,Configures a namespace for the Cluster Logging Operator.,Yes
Cluster Logging Operator,`clusterLogOperGroup.yaml`,Configures an Operator group for the Cluster Logging Operator.,Yes
Cluster Logging Operator,`clusterLogServiceAccount.yaml`,Defines the `ServiceAccount` CR used by Cluster Logging Operator components.,Yes
Cluster Logging Operator,`clusterLogServiceAccountAuditBinding.yaml`,Binds the Cluster Logging `ServiceAccount` CR to audit log roles.,Yes
Cluster Logging Operator,`clusterLogServiceAccountInfrastructureBinding.yaml`,Binds the Cluster Logging `ServiceAccount` CR to infrastructure log roles.,Yes
Cluster Logging Operator,`clusterLogSubscription.yaml`,Defines a subscription for installing and managing the Cluster Logging Operator.,Yes
|====

// Module included in the following assemblies:
//
// * scalability-and-performance/telco-hub-rds.adoc

[id="container-registry-crs_{context}"]
= Container registry reference CRs

[role="_abstract"]
The following custom resources (CRs) configure the container registry for the telco hub cluster.

.Container registry CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
Registry,`catalog-source.yaml`,Defines a `CatalogSource` CR for mirrored Operator catalogs.,No
Registry,`idms-operator.yaml`,Defines an image digest `MirrorSet` Operator CR for mirrored Operator images.,No
Registry,`idms-release.yaml`,Defines an image digest `MirrorSet` CR for OpenShift Container Platform release images.,No
Registry,`image-config.yaml`,Defines an image configuration CR to manage image registries and policies.,No
Registry,`itms-generic.yaml`,Defines an image tag `MirrorSet` CR for mirrored images in a disconnected registry.,No
Registry,`itms-release.yaml`,Defines an image tag `MirrorSet` CR for OpenShift Container Platform release images.,No
Registry,`kustomization.yaml`,Defines a `Kustomization` manifest for registry-related CRs.,No
Registry,`operator-hub.yaml`,Configures the `OperatorHub` CR for offline catalog sources.,No
Registry,`registry-ca.yaml`,Defines a `ConfigMap` CR containing registry CA certificates.,No
|====

// Module included in the following assemblies:
//
// *

[id="image-mirroring-crs_{context}"]
= Image mirroring reference CRs

[role="_abstract"]
The following custom resources (CRs) configure image mirroring for the telco hub cluster.

.Image mirroring CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
Mirroring configuration CRs,`imageset-config.yaml`,"Defines an `ImageSetConfiguration` CR for mirroring OpenShift Container Platform channels and Operator packages, specifying versions and target catalogs.",No
|====

// Module included in the following assemblies:
//
// *

[id="installation-crs_{context}"]
= Installation reference CRs

[role="_abstract"]
The following custom resources (CRs) configure the installation for the telco hub cluster.

.Installation CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
Agent-based install,`agent-config.yaml`,"Configures the Agent-based installer, specifying network and device settings for the hosts to be installed.",No
Agent-based install,`install-config.yaml`,"Configures the hub cluster installation for networking, control plane, compute nodes, mirror registries, and so on.",No
|====

// Module included in the following assemblies:
//
// *

[id="security-crs_{context}"]
= Security reference CRs

.Security CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
Cert-Manager,`certManagerNS.yaml`,Defines the cert-manager-operator namespace.,Yes
Cert-Manager,`certManagerOperatorgroup.yaml`,Defines the OperatorGroup for cert-manager.,Yes
Cert-Manager,`certManagerSubscription.yaml`,Installs the OpenShift cert-manager operator.,Yes
Cert-Manager,`certManagerClusterIssuer.yaml`,Configures an ACME ClusterIssuer using Let's Encrypt with DNS-01 challenge.,Yes
Cert-Manager,`apiServerCertificate.yaml`,Creates a certificate for the API Server endpoint.,Yes
Cert-Manager,`ingressCertificate.yaml`,Creates a wildcard certificate for the Ingress/Router.,Yes
Cert-Manager,`apiServerConfig.yaml`,Configures OpenShift to use the cert-manager generated API Server certificate.,Yes
Cert-Manager,`ingressControllerConfig.yaml`,Configures OpenShift to use the cert-manager generated Ingress certificate.,Yes
Cert-Manager,`certManagerCertificatePolicy.yaml`,Defines CertificatePolicy for monitoring certificate expiration and compliance across managed clusters.,Yes
Cert-Manager,`certManagerCertificatePolicyPlacement.yaml`,Defines Placement for CertificatePolicy targeting clusters with the common label.,Yes
Cert-Manager,`certManagerCertificatePolicyPlacementBinding.yaml`,Binds the CertificatePolicy to the Placement for policy distribution.,Yes
|====

// Module included in the following assemblies:
//
// *

[id="backup-recovery-crs_{context}"]
= Backup Recovery reference CRs

.Backup Recovery CRs
[cols="4*", options="header", format=csv]
|====
Component,Reference CR,Description,Optional
OADP,`backupSchedule.yaml`,Defines a `BackupSchedule` CR.,Yes
OADP,`dataProtectionApplication.yaml`,Defines the data protection application with backup storage and configuration parameters.,Yes
OADP,`objectBucketClaim.yaml`,Defines the object bucket used by backup.,Yes
OADP,`policy-backup.yaml`,Defines a policy to ensure `BareMetalHost` CRs are correctly annotated for backup.,Yes
OADP,`restore.yaml`,Example `Restore` CR.,Yes
|====

// Module included in the following assemblies:
//
// * scalability_and_performance/telco_core_ref_design_specs/telco-core-rds.adoc

[id="telco-hub-software-stack_{context}"]
= Telco hub reference configuration software specifications

[role="_abstract"]
The following y-stream versions were used in validation of the telco hub solution for OpenShift Container Platform clusters.

[width="100%",cols="62%,38%",options="header",]
|====
|Hub Cluster Component
|Software Version (y-stream)

|OpenShift Container Platform
|4.22

|{rh-rhacm-first}
|2.17

|Local Storage Operator
|4.22

|cert-manager Operator
|1.19

|{odf-first}
|4.21

|{gitops-title}
|1.20

|{ztp-first} plugins
|4.22

|{mce-short} PolicyGenerator plugin
|2.17

|{cgu-operator-first}
|4.22

|Cluster Logging Operator
|6.5

|{oadp-first}
|The version aligned with the {rh-rhacm} release.
|====
* {odf-short} will be updated to 4.22 when the aligned {odf-short} version is released.
* Cluster Logging Operator will be updated to 6.6 when the aligned Cluster Logging Operator version is released.
* The cert-manager Operator and {gitops-title} Operator are platform agnostic operators.
The support lifecycle for these operators is independent from the support lifecycle for OpenShift Container Platform.
You might need to update to a newer minor version of these operators at the end of an operator lifecycle, or when planning to update the OpenShift Container Platform cluster to continue support.
For support lifecycle details for platform agnostic operators, see OpenShift Operator Life Cycles.
