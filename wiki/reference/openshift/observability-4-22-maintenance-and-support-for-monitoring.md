---
title: "Maintenance and support for monitoring"
type: reference
domain: openshift
slug: observability-4-22-maintenance-and-support-for-monitoring
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/maintenance-and-support-for-monitoring
version: 4.22
family: observability
documentKind: "Documentation"
---

# Maintenance and support for monitoring

[id="maintenance-and-support-for-monitoring"]
= Maintenance and support for monitoring

[role="_abstract"]
Not all configuration options for the monitoring stack are exposed. To configure OpenShift Container Platform monitoring, configure the {cmo-first} using the options described in the "Config map reference for the {cmo-full}" linked in the _Additional resources_ section. *Do not use other configurations, as they are unsupported.*

Configuration paradigms might change across Prometheus releases, and such cases can only be handled gracefully if all configuration possibilities are controlled. If you use unsupported configurations, your changes will disappear because the {cmo-short} automatically reconciles any differences and resets any unsupported changes back to the originally defined state by default and by design.

[IMPORTANT]
====
Installing another Prometheus instance is not supported by the Red Hat Site Reliability Engineers (SRE).
====

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="support-considerations_{context}"]
= Support considerations for monitoring

[role="_abstract"]
The OpenShift Container Platform monitoring has configuration limitations. Understanding them is essential for avoiding automated configuration resets.

[NOTE]
====
Backward compatibility for metrics, recording rules, or alerting rules is not guaranteed.
====

The following modifications are explicitly not supported:

* *Creating additional `ServiceMonitor`, `PodMonitor`, and `PrometheusRule` objects in the `openshift-&#42;` and `kube-&#42;` projects.*
* *Modifying any resources or objects deployed in the `openshift-monitoring` or `openshift-user-workload-monitoring` projects.* The resources created by the OpenShift Container Platform monitoring stack are not meant to be used by any other resources, as there are no guarantees about their backward compatibility.
+
[NOTE]
====
The Alertmanager configuration is deployed as the `alertmanager-main` secret resource in the `openshift-monitoring` namespace. If you have enabled a separate Alertmanager instance for user-defined alert routing, an Alertmanager configuration is also deployed as the `alertmanager-user-workload` secret resource in the `openshift-user-workload-monitoring` namespace. To configure additional routes for any instance of Alertmanager, you need to decode, modify, and then encode that secret. This procedure is a supported exception to the preceding statement.
====
+
* *Modifying resources of the stack.* The OpenShift Container Platform monitoring stack ensures its resources are always in the state it expects them to be. If they are modified, the stack will reset them.
* *Deploying user-defined workloads to `openshift-&#42;`, and `kube-&#42;` projects.* These projects are reserved for Red{nbsp}Hat provided components and they should not be used for user-defined workloads.
* *Enabling symptom based monitoring by using the `Probe` custom resource definition (CRD) in Prometheus Operator.*
* *Manually deploying monitoring resources into namespaces that have the `openshift.io/cluster-monitoring: "true"` label.*
* *Adding the `openshift.io/cluster-monitoring: "true"` label to namespaces.* This label is reserved only for the namespaces with core OpenShift Container Platform components and Red{nbsp}Hat certified components.

* *Installing custom Prometheus instances on OpenShift Container Platform.* A custom instance is a Prometheus custom resource (CR) managed by the Prometheus Operator.
* *Modifying the default platform monitoring components.* You should not modify any of the components defined in the `cluster-monitoring-config` config map. Red{nbsp}Hat SRE uses these components to monitor the core cluster components and Kubernetes services.

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="support-policy-for-monitoring-operators_{context}"]
= Support policy for monitoring Operators

[role="_abstract"]
Monitoring Operators ensure that OpenShift Container Platform monitoring resources function as designed and tested. If Cluster Version Operator (CVO) control of an Operator is overridden, the Operator does not respond to configuration changes, reconcile the intended state of cluster objects, or receive updates.

While overriding CVO control for an Operator can be helpful during debugging, this is  unsupported and the cluster administrator assumes full control of the individual component configurations and upgrades.

*Overriding the Cluster Version Operator*

The `spec.overrides` parameter can be added to the configuration for the CVO to allow administrators to provide a list of overrides to the behavior of the CVO for a component. Setting the `spec.overrides[].unmanaged` parameter to `true` for a component blocks cluster upgrades and alerts the administrator after a CVO override has been set:

[source,terminal]
----
Disabling ownership via cluster version overrides prevents upgrades. Please remove overrides before continuing.
----

[WARNING]
====
Setting a CVO override puts the entire cluster in an unsupported state and prevents the monitoring stack from being reconciled to its intended state. This impacts the reliability features built into Operators and prevents updates from being received. Reported issues must be reproduced after removing any overrides for support to proceed.
====

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="support-version-matrix-for-monitoring-components_{context}"]
= Support version matrix for monitoring components

[role="_abstract"]
The following matrix contains information about versions of monitoring components for OpenShift Container Platform 4.12 and later releases:

.OpenShift Container Platform and component versions
|===
|OpenShift Container Platform |Prometheus Operator |Prometheus  |Metrics Server |Alertmanager |kube-state-metrics agent |monitoring-plugin |node-exporter agent |Thanos

|4.20 |0.85.0 |3.5.0 |0.8.0 |0.28.1 |2.16.0 |1.0.0 |1.9.1 |0.39.2

|4.19 |0.81.0 |3.2.1 |0.7.2 |0.28.1 |2.15.0 |1.0.0 |1.9.1 |0.37.2

|4.18 |0.78.1 |2.55.1 |0.7.2 |0.27.0 |2.13.0 |1.0.0 |1.8.2 |0.36.1

|4.17 |0.75.2 |2.53.1 |0.7.1 |0.27.0 |2.13.0 |1.0.0 |1.8.2 |0.35.1

|4.16 |0.73.2 |2.52.0 |0.7.1 |0.26.0 |2.12.0 |1.0.0 |1.8.0 |0.35.0

|4.15 |0.70.0 |2.48.0 |0.6.4 |0.26.0 |2.10.1 |1.0.0 |1.7.0 |0.32.5

|4.14 |0.67.1 |2.46.0 |N/A |0.25.0 |2.9.2 |1.0.0 |1.6.1 |0.30.2

|4.13 |0.63.0 |2.42.0 |N/A |0.25.0 |2.8.1 |N/A |1.5.0 |0.30.2

|4.12 |0.60.1 |2.39.1 |N/A |0.24.0 |2.6.0 |N/A |1.4.0 |0.28.1
|===

[NOTE]
====
The openshift-state-metrics agent and Telemeter Client are OpenShift-specific components. Therefore, their versions correspond with the versions of OpenShift Container Platform.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Config map reference for the {cmo-full}
