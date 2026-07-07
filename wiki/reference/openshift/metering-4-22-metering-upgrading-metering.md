---
title: "Upgrading metering"
type: reference
domain: openshift
slug: metering-4-22-metering-upgrading-metering
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metering/metering-upgrading-metering
version: 4.22
family: metering
documentKind: "Documentation"
---

# Upgrading metering

[id="upgrading-metering"]
= Upgrading metering

// When including this file, ensure that {FeatureName} is set immediately before
// the include. Otherwise it will result in an incorrect replacement.

[IMPORTANT]
====
[subs="attributes+"]
{FeatureName} is a deprecated feature. Deprecated functionality is still included in OpenShift Container Platform and continues to be supported; however, it will be removed in a future release of this product and is not recommended for new deployments.

For the most recent list of major functionality that has been deprecated or removed within OpenShift Container Platform, refer to the _Deprecated and removed features_ section of the OpenShift Container Platform release notes.
====
// Undefine {FeatureName} attribute, so that any mistakes are easily spotted

You can upgrade metering to  by updating the Metering Operator subscription.

== Prerequisites

*  The cluster is updated to .
*  The Metering Operator is installed from the software catalog.
+
[NOTE]
====
You must upgrade the Metering Operator to  manually. Metering does not upgrade automatically if you selected the "Automatic" *Approval Strategy* in a previous installation.
====
*  The MeteringConfig custom resource is configured.
*  The metering stack is installed.
*  Ensure that metering status is healthy by checking that all pods are ready.

[IMPORTANT]
====
Potential data loss can occur if you modify your metering storage configuration after installing or upgrading metering.
====

.Procedure

.  Click *Ecosystem* -> *Installed Operators* from the web console.

.  Select the `openshift-metering` project.

.  Click *Metering Operator*.

.  Click *Subscription* -> *Channel*.

.  In the *Change Subscription Update Channel* window, select ** and click *Save*.
+
[NOTE]
====
Wait several seconds to allow the subscription to update before proceeding to the next step.
====
.  Click *Ecosystem* -> *Installed Operators*.
+
The Metering Operator is shown as 4.9. For example:
+
----
Metering
4.9.0-202107012112.p0 provided by Red Hat, Inc
----

.Verification
You can verify the metering upgrade by performing any of the following checks:

*  Check the Metering Operator cluster service version (CSV) for the new metering version. This can be done through either the web console or CLI.
+
--
.Procedure (UI)
  .  Navigate to *Ecosystem* -> *Installed Operators* in the metering namespace.
  .  Click *Metering Operator*.
  .  Click *Subscription* for *Subscription Details*.
  .  Check the *Installed Version* for the upgraded metering version. The *Starting Version* shows the metering version prior to upgrading.

.Procedure (CLI)
*  Check the Metering Operator CSV:
+
[source,terminal]
----
$ oc get csv | grep metering
----
+
.Example output for metering upgrade from 4.8 to 4.9
[source,terminal]
----
NAME                                        DISPLAY                  VERSION                 REPLACES                                 PHASE
metering-operator.4.9.0-202107012112.p0     Metering                 4.9.0-202107012112.p0   metering-operator.4.8.0-202007012112.p0  Succeeded
----
--

*  Check that all required pods in the `openshift-metering` namespace are created. This can be done through either the web console or CLI.
+
--
[NOTE]
====
Many pods rely on other components to function before they themselves can be considered ready. Some pods may restart if other pods take too long to start. This is to be expected during the Metering Operator upgrade.
====

.Procedure (UI)
*  Navigate to *Workloads* -> *Pods* in the metering namespace and verify that pods are being created. This can take several minutes after upgrading the metering stack.

.Procedure (CLI)
*  Check that all required pods in the `openshift-metering` namespace are created:
+
[source,terminal]
----
$ oc -n openshift-metering get pods
----
.Example output
[source,terminal]
+
----
NAME                                  READY   STATUS    RESTARTS   AGE
hive-metastore-0                      2/2     Running   0          3m28s
hive-server-0                         3/3     Running   0          3m28s
metering-operator-68dd64cfb6-2k7d9    2/2     Running   0          5m17s
presto-coordinator-0                  2/2     Running   0          3m9s
reporting-operator-5588964bf8-x2tkn   2/2     Running   0          2m40s
----
--

*  Verify that the `ReportDataSource` resources are importing new data, indicated by a valid timestamp in the `NEWEST METRIC` column. This might take several minutes. Filter out the "-raw" `ReportDataSource` resources, which do not import data:
+
[source,terminal]
----
$ oc get reportdatasources -n openshift-metering | grep -v raw
----
+
Timestamps in the `NEWEST METRIC` column indicate that `ReportDataSource` resources are beginning to import new data.
+
.Example output
[source,terminal]
----
NAME                                         EARLIEST METRIC        NEWEST METRIC          IMPORT START           IMPORT END             LAST IMPORT TIME       AGE
node-allocatable-cpu-cores                   2021-07-01T21:10:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:56:44Z   23h
node-allocatable-memory-bytes                2021-07-01T21:10:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:52:07Z   23h
node-capacity-cpu-cores                      2021-07-01T21:10:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:56:52Z   23h
node-capacity-memory-bytes                   2021-07-01T21:10:00Z   2021-07-02T19:57:00Z   2021-07-01T19:10:00Z   2021-07-02T19:57:00Z   2021-07-02T19:57:03Z   23h
persistentvolumeclaim-capacity-bytes         2021-07-01T21:09:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:56:46Z   23h
persistentvolumeclaim-phase                  2021-07-01T21:10:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:52:36Z   23h
persistentvolumeclaim-request-bytes          2021-07-01T21:10:00Z   2021-07-02T19:57:00Z   2021-07-01T19:10:00Z   2021-07-02T19:57:00Z   2021-07-02T19:57:03Z   23h
persistentvolumeclaim-usage-bytes            2021-07-01T21:09:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:52:02Z   23h
pod-limit-cpu-cores                          2021-07-01T21:10:00Z   2021-07-02T19:57:00Z   2021-07-01T19:10:00Z   2021-07-02T19:57:00Z   2021-07-02T19:57:02Z   23h
pod-limit-memory-bytes                       2021-07-01T21:10:00Z   2021-07-02T19:58:00Z   2021-07-01T19:11:00Z   2021-07-02T19:58:00Z   2021-07-02T19:59:06Z   23h
pod-persistentvolumeclaim-request-info       2021-07-01T21:10:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:52:07Z   23h
pod-request-cpu-cores                        2021-07-01T21:10:00Z   2021-07-02T19:58:00Z   2021-07-01T19:11:00Z   2021-07-02T19:58:00Z   2021-07-02T19:58:57Z   23h
pod-request-memory-bytes                     2021-07-01T21:10:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:55:32Z   23h
pod-usage-cpu-cores                          2021-07-01T21:09:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:54:55Z   23h
pod-usage-memory-bytes                       2021-07-01T21:08:00Z   2021-07-02T19:52:00Z   2021-07-01T19:11:00Z   2021-07-02T19:52:00Z   2021-07-02T19:55:00Z   23h
report-ns-pvc-usage                                                                                                                                             5h36m
report-ns-pvc-usage-hourly
----

After all pods are ready and you have verified that new data is being imported, metering continues to collect data and report on your cluster. Review a previously scheduled report or create a run-once metering report to confirm the metering upgrade.
