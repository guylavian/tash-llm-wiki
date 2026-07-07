---
title: "About remote health monitoring"
type: reference
domain: openshift
slug: support-4-22-about-remote-health-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/about-remote-health-monitoring
version: 4.22
family: support
documentKind: "Documentation"
---

# About remote health monitoring

[id="about-remote-health-monitoring"]
= About remote health monitoring

[role="_abstract"]
OpenShift Container Platform collects telemetry and configuration data about your cluster and reports it to Red{nbsp}Hat by using the Telemeter Client and the {insights-operator}. The data that is provided to Red{nbsp}Hat enables the benefits outlined in this document.

A cluster that reports data to Red Hat through Telemetry and the {insights-operator} is considered a _connected cluster_.

*Telemetry* is the term that Red Hat uses to describe the information being sent to Red Hat by the OpenShift Container Platform Telemeter Client. Lightweight attributes are sent from connected clusters to Red Hat to enable subscription management automation, monitor the health of clusters, assist with support, and improve customer experience.

The *{insights-operator}* gathers OpenShift Container Platform configuration data and sends it to Red{nbsp}Hat. The data is used to produce insights about potential issues that a cluster might be exposed to. These insights are communicated to cluster administrators on {cluster-manager-url}.

More information is provided in this document about these two processes.

== Telemetry and {insights-operator} benefits

Telemetry and the {insights-operator} enable the following benefits for end-users:

* *Enhanced identification and resolution of issues*. Events that might seem normal to an end-user can be observed by Red Hat from a broader perspective across a fleet of clusters. Some issues can be more rapidly identified from this point of view and resolved without an end-user needing to open a support case or file a Jira issue.

* *Advanced release management*. OpenShift Container Platform offers the `candidate`, `fast`, and `stable` release channels, which enable you to choose an update strategy. The graduation of a release from `fast` to `stable` is dependent on the success rate of updates and on the events seen during upgrades. With the information provided by connected clusters, Red Hat can improve the quality of releases to `stable` channels and react more rapidly to issues found in the `fast` channels.

* *Targeted prioritization of new features and functionality*. The data collected provides insights about which areas of OpenShift Container Platform are used most. With this information, Red Hat can focus on developing the new features and functionality that have the greatest impact for our customers.

* *A streamlined support experience*. You can provide a cluster ID for a connected cluster when creating a support ticket on the Red Hat Customer Portal. This enables Red Hat to deliver a streamlined support experience that is specific to your cluster, by using the connected information. This document provides more information about that enhanced support experience.

* *Predictive analytics*. The insights displayed for your cluster on {cluster-manager-url} are enabled by the information collected from connected clusters. Red Hat is investing in applying deep learning, machine learning, and artificial intelligence automation to help identify issues that OpenShift Container Platform clusters are exposed to.

On OpenShift Container Platform, remote health reporting is always enabled. You cannot opt out of it.

OpenShift Container Platform may be installed without a pull secret received at console.redhat.com. In this case default imagestreams will not be imported and telemetry data will not be sent.

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

[id="telemetry-about-telemetry_{context}"]
= About Telemetry

[role="_abstract"]
Telemetry sends a carefully chosen subset of the cluster monitoring metrics to Red Hat. The Telemeter Client fetches the metrics values every four minutes and thirty seconds and uploads the data to Red Hat. These metrics are described in this document.

This stream of data is used by Red Hat to monitor the clusters in real-time and to react as necessary to problems that impact our customers. It also allows Red Hat to roll out OpenShift Container Platform upgrades to customers to minimize service impact and continuously improve the upgrade experience.

This debugging information is available to Red Hat Support and Engineering teams with the same restrictions as accessing data reported through support cases. All connected cluster information is used by Red Hat to help make OpenShift Container Platform better and more intuitive to use.

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform update documentation
* OpenShift Container Platform upgrade documentation
* OpenShift Container Platform upgrade documentation
* OpenShift Container Platform upgrade documentation

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

[id="what-information-is-collected_{context}"]
= Information collected by Telemetry

[role="_abstract"]
The following information is collected by Telemetry:

[id="system-information_{context}"]
== System information

* Version information, including the OpenShift Container Platform cluster version and installed update details that are used to determine update version availability
* Update information, including the number of updates available per cluster, the channel and image repository used for an update, update progress information, and the number of errors that occur in an update
* The unique random identifier that is generated during an installation
* Configuration details that help Red Hat Support to provide beneficial support for customers, including node configuration at the cloud infrastructure level, hostnames, IP addresses, Kubernetes pod names, namespaces, and services
* The OpenShift Container Platform framework components installed in a cluster and their condition and status
* Events for all namespaces listed as "related objects" for a degraded Operator
* Information about degraded software
* Information about the validity of certificates
* The name of the provider platform that OpenShift Container Platform is deployed on and the data center location

[id="sizing-information_{context}"]
== Sizing Information

* Sizing information about clusters, machine types, and machines, including the number of CPU cores and the amount of RAM used for each
* The number of running virtual machine instances in a cluster
* The number of etcd members and the number of objects stored in the etcd cluster
* Number of application builds by build strategy type

[id="usage-information_{context}"]
== Usage information

* Usage information about components, features, and extensions
* Usage details about Technology Previews and unsupported configurations

Telemetry does not collect identifying information such as usernames or passwords. Red Hat does not intend to collect personal information. If Red Hat discovers that personal information has been inadvertently received, Red Hat will delete such information. To the extent that any telemetry data constitutes personal data, please refer to the Red Hat Privacy Statement for more information about Red Hat's privacy practices.

// Module is not in OCP
// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

[id="telemetry-user-telemetry_{context}"]
= User Telemetry

[role="_abstract"]
Red Hat collects anonymized user data from your browser. This anonymized data includes what pages, features, and resource types that the user of all clusters with enabled telemetry uses.

Other considerations:

* User events are grouped as a SHA-1 hash.
* User's IP address is saved as `0.0.0.0`.
* User names and IP addresses are never saved as separate values.

[role="_additional-resources"]
.Additional resources

* Showing data collected by Telemetry
* Upstream cluster-monitoring-operator source code

* Remote health reporting

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

[id="insights-operator-about_{context}"]
= About the {insights-operator}

[role="_abstract"]
The {insights-operator} periodically gathers configuration and component failure status and, by default, reports that data every two hours to Red{nbsp}Hat. This information enables Red{nbsp}Hat to assess configuration and deeper failure data than is reported through Telemetry.

Users of OpenShift Container Platform can display the report of each cluster in the {insights-advisor-url} service on {hybrid-console}. If any issues have been identified, {red-hat-lightspeed} provides further details and, if available, steps on how to solve a problem.

The {insights-operator} does not collect identifying information, such as user names, passwords, or certificates. See {red-hat-lightspeed} Data & Application Security for information about {red-hat-lightspeed} data collection and controls.

Red Hat uses all connected cluster information to:

* Identify potential cluster issues and provide a solution and preventive actions in the {insights-advisor-url} service on {hybrid-console}
* Improve OpenShift Container Platform by providing aggregated and critical information to product and support teams
* Make OpenShift Container Platform more intuitive

[role="_additional-resources"]
.Additional resources

* Remote health reporting

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

[id="insights-operator-what-information-is-collected_{context}"]
= Information collected by the {insights-operator}

[role="_abstract"]
The following information is collected by the {insights-operator}:

* General information about your cluster and its components to identify issues that are specific to your OpenShift Container Platform version and environment.
* Configuration files, such as the image registry configuration, of your cluster to determine incorrect settings and issues that are specific to parameters you set.
* Errors that occur in the cluster components.
* Progress information of running updates, and the status of any component upgrades.
* Details of the platform that OpenShift Container Platform is deployed on and the region that the cluster is located in
* Cluster workload information transformed into discreet Secure Hash Algorithm (SHA) values, which allows Red{nbsp}Hat to assess workloads for security and version vulnerabilities without disclosing sensitive details.
* Workload information about the operating system and runtime environment, including runtime kinds, names, and version. This data gives Red{nbsp}Hat a better understanding of how you use OpenShift Container Platform containers so that we can proactively help you make investment decisions to drive optimal utilization.

* If an Operator reports an issue, information is collected about core OpenShift Container Platform pods in the `openshift-&#42;` and `kube-&#42;` projects. This includes state, resource, security context, volume information, and more.

[role="_additional-resources"]
.Additional resources

* Showing data collected by the {insights-operator}
* What data is being collected by the {insights-operator} in OpenShift?

* Enabling features using feature gates
* {insights-operator} upstream project

// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

[id="understanding-telemetry-and-insights-operator-data-flow_{context}"]
= Understanding Telemetry and {insights-operator} data flow

[role="_abstract"]
The Telemeter Client collects selected time series data from the Prometheus API. The time series data is uploaded to api.openshift.com every four minutes and thirty seconds for processing.

The {insights-operator} gathers selected data from the Kubernetes API and the Prometheus API into an archive. The archive is uploaded to {cluster-manager-url} every two hours for processing. The {insights-operator} also downloads the latest {red-hat-lightspeed} analysis from {cluster-manager-url}. This is used to populate the *{red-hat-lightspeed} status* pop-up that is included in the *Overview* page in the OpenShift Container Platform web console.

All of the communication with Red Hat occurs over encrypted channels by using Transport Layer Security (TLS) and mutual certificate authentication. All of the data is encrypted in transit and at rest.

Access to the systems that handle customer data is controlled through multi-factor authentication and strict authorization controls. Access is granted on a need-to-know basis and is limited to required operations.

== Telemetry and {insights-operator} data flow

image:telmetry-and-insights-operator-data-flow.png[Telemetry and {insights-operator} data flow]

// TODO: Add the first xref to ROSA HCP when the monitoring book is migrated.
[role="_additional-resources"]
.Additional resources

* About OpenShift Container Platform monitoring

* About OpenShift Container Platform monitoring
* Configuring your firewall

[id="additional-details-about-how-remote-health-monitoring-data-is-used"]
== Additional details about how remote health monitoring data is used

The information collected to enable remote health monitoring is detailed in Information collected by Telemetry and Information collected by the {insights-operator}.

As further described in the preceding sections of this document, Red Hat collects data about your use of the Red Hat Product(s) for purposes such as providing support and upgrades, optimizing performance or configuration, minimizing service impacts, identifying and remediating threats, troubleshooting, improving the offerings and user experience, responding to issues, and for billing purposes if applicable.

== Collection safeguards

Red Hat employs technical and organizational measures designed to protect the telemetry and configuration data.

== Sharing

Red{nbsp}Hat might share the data collected through Telemetry and the {insights-operator} internally within Red Hat to improve your user experience. Red{nbsp}Hat might share telemetry and configuration data with its business partners in an aggregated form that does not identify customers to help the partners better understand their markets and their customers' use of Red{nbsp}Hat offerings or to ensure the successful integration of products jointly supported by those partners.

== Third parties

Red Hat may engage certain third parties to assist in the collection, analysis, and storage of the Telemetry and configuration data.

== User control / enabling and disabling telemetry and configuration data collection

You may disable OpenShift Container Platform Telemetry and the {insights-operator} by following the instructions in Remote health reporting.
