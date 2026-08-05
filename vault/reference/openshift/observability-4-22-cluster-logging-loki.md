---
title: "Configuring the LokiStack log store"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-loki
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-loki
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring the LokiStack log store

[id="cluster-logging-loki"]
= Configuring the LokiStack log store

In {logging} documentation, _LokiStack_ refers to the {logging} supported combination of Loki and web proxy with OpenShift Container Platform authentication integration. LokiStack's proxy uses OpenShift Container Platform authentication to enforce multi-tenancy. _Loki_ refers to the log store as either the individual component or an external store.

// Module included in the following assemblies:

//  * cluster-logging-loki.adoc
//  * network_observability/installing-operators.adoc

[id="logging-creating-new-group-cluster-admin-user-role_{context}"]
= Creating a new group for the cluster-admin user role

Use the following procedure to create a new group for users with `cluster-admin` permissions.

.Procedure

. Enter the following command to create a new group:
+
[source,terminal]
----
$ oc adm groups new cluster-admin
----
. Enter the following command to add the desired user to the `cluster-admin` group:
+
[source,terminal]
----
$ oc adm groups add-users cluster-admin <username>
----
. Enter the following command to add `cluster-admin` user role to the group:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-group cluster-admin cluster-admin
----

// Module included in the following assemblies:
//
// * logging/cluster-logging-loki.adoc

[id="logging-loki-restart-hardening_{context}"]
= LokiStack behavior during cluster restarts

In logging version 5.8 and newer versions, when an OpenShift Container Platform cluster is restarted, LokiStack ingestion and the query path continue to operate within the available CPU and memory resources available for the node. This means that there is no downtime for the LokiStack during OpenShift Container Platform cluster updates. This behavior is achieved by using `PodDisruptionBudget` resources. The {loki-op} provisions `PodDisruptionBudget` resources for Loki, which determine the minimum number of pods that must be available per component to ensure normal operations under certain conditions.

[role="_additional-resources"]
.Additional resources
* Pod disruption budgets Kubernetes documentation

// Module included in the following assemblies:
//
// * logging/cluster-logging-loki.adoc

[id="logging-loki-reliability-hardening_{context}"]
= Configuring Loki to tolerate node failure

In the {logging} 5.8 and later versions, the {loki-op} supports setting pod anti-affinity rules to request that pods of the same component are scheduled on different available nodes in the cluster.

The Operator sets default, preferred `podAntiAffinity` rules for all Loki components, which includes the `compactor`, `distributor`, `gateway`, `indexGateway`, `ingester`, `querier`, `queryFrontend`, and `ruler` components.

You can override the preferred `podAntiAffinity` settings for Loki components by configuring required settings in the `requiredDuringSchedulingIgnoredDuringExecution` field:

.Example user settings for the ingester component
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
# ...
  template:
    ingester:
      podAntiAffinity:
      # ...
        requiredDuringSchedulingIgnoredDuringExecution: <1>
        - labelSelector:
            matchLabels: <2>
              app.kubernetes.io/component: ingester
          topologyKey: kubernetes.io/hostname
# ...
----
<1> The stanza to define a required rule.
<2> The key-value pair (label) that must be matched to apply the rule.

[role="_additional-resources"]
.Additional resources
* `PodAntiAffinity` v1 core Kubernetes documentation
* Assigning Pods to Nodes Kubernetes documentation
* Placing pods relative to other pods using affinity and anti-affinity rules

// Module included in the following assemblies:
//
// * logging/cluster-logging-loki.adoc

[id="logging-loki-zone-aware-rep_{context}"]
= Zone aware data replication

In the {logging} 5.8 and later versions, the {loki-op} offers support for zone-aware data replication through pod topology spread constraints. Enabling this feature enhances reliability and safeguards against log loss in the event of a single zone failure. When configuring the deployment size as `1x.extra.small`, `1x.small`, or `1x.medium,` the `replication.factor` field is automatically set to 2.

To ensure proper replication, you need to have at least as many availability zones as the replication factor specifies. While it is possible to have more availability zones than the replication factor, having fewer zones can lead to write failures. Each zone should host an equal number of instances for optimal operation.

.Example LokiStack CR with zone replication enabled
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
 name: logging-loki
 namespace: openshift-logging
spec:
 replicationFactor: 2 # <1>
 replication:
   factor: 2 # <2>
   zones:
   -  maxSkew: 1 # <3>
      topologyKey: topology.kubernetes.io/zone # <4>
----
<1> Deprecated field, values entered are overwritten by `replication.factor`.
<2> This value is automatically set when deployment size is selected at setup.
<3> The maximum difference in number of pods between any two topology domains. The default is 1, and you cannot specify a value of 0.
<4> Defines zones in the form of a topology key that corresponds to a node label.

// Module included in the following assemblies:
//
// * logging/cluster-logging-loki.adoc

[id="logging-loki-zone-fail-recovery_{context}"]
= Recovering Loki pods from failed zones

In OpenShift Container Platform a zone failure happens when specific availability zone resources become inaccessible. Availability zones are isolated areas within a cloud provider's data center, aimed at enhancing redundancy and fault tolerance. If your OpenShift Container Platform cluster is not configured to handle this, a zone failure can lead to service or data loss.

Loki pods are part of a StatefulSet, and they come with Persistent Volume Claims (PVCs) provisioned by a `StorageClass` object. Each Loki pod and its PVCs reside in the same zone. When a zone failure occurs in a cluster, the StatefulSet controller automatically attempts to recover the affected pods in the failed zone.

[WARNING]
====
The following procedure will delete the PVCs in the failed zone, and all data contained therein.  To avoid complete data loss the replication factor field of the `LokiStack` CR should always be set to a value greater than 1 to ensure that Loki is replicating.
====

.Prerequisites
* Logging version 5.8 or later.
* Verify your `LokiStack` CR has a replication factor greater than 1.
* Zone failure detected by the control plane, and nodes in the failed zone are marked by cloud provider integration.

The StatefulSet controller automatically attempts to reschedule pods in a failed zone. Because the associated PVCs are also in the failed zone, automatic rescheduling to a different zone does not work. You must manually delete the PVCs in the failed zone to allow successful re-creation of the stateful Loki Pod and its provisioned PVC in the new zone.

.Procedure
. List the pods in `Pending` status by running the following command:
+
[source,terminal]
----
oc get pods --field-selector status.phase==Pending -n openshift-logging
----
+
.Example `oc get pods` output
[source,terminal]
----
NAME                           READY   STATUS    RESTARTS   AGE # <1>
logging-loki-index-gateway-1   0/1     Pending   0          17m
logging-loki-ingester-1        0/1     Pending   0          16m
logging-loki-ruler-1           0/1     Pending   0          16m
----
<1> These pods are in `Pending` status because their corresponding PVCs are in the failed zone.

. List the PVCs in `Pending` status by running the following command:
+
[source,terminal]
----
oc get pvc -o=json -n openshift-logging | jq '.items[] | select(.status.phase == "Pending") | .metadata.name' -r
----
+
.Example `oc get pvc` output
[source,terminal]
----
storage-logging-loki-index-gateway-1
storage-logging-loki-ingester-1
wal-logging-loki-ingester-1
storage-logging-loki-ruler-1
wal-logging-loki-ruler-1
----

. Delete the PVC(s) for a pod by running the following command:
+
[source,terminal]
----
oc delete pvc __<pvc_name>__  -n openshift-logging
----
+
. Then delete the pod(s) by running the following command:
+
[source,terminal]
----
oc delete pod __<pod_name>__  -n openshift-logging
----

Once these objects have been successfully deleted, they should automatically be rescheduled in an available zone.

[id="logging-loki-zone-fail-term-state_{context}"]
== Troubleshooting PVC in a terminating state

The PVCs might hang in the terminating state without being deleted, if PVC metadata finalizers are set to `kubernetes.io/pv-protection`. Removing the finalizers should allow the PVCs to delete successfully.

. Remove the finalizer for each PVC by running the command below, then retry deletion.
+
[source,terminal]
----
oc patch pvc __<pvc_name>__ -p '{"metadata":{"finalizers":null}}' -n openshift-logging
----

[role="_additional-resources"]
.Additional resources
* Topology spread constraints Kubernetes documentation
* Kubernetes storage documentation.

* Controlling pod placement by using pod topology spread constraints

// Module included in the following assemblies:
//
// * observability/network_observability/installing-operators.adoc
// * logging/cluster-logging-loki.adoc

[id="logging-loki-log-access_{context}"]
= Fine grained access for Loki logs

In {logging} 5.8 and later, the {clo} does not grant all users access to logs by default. As an administrator, you must configure your users' access unless the Operator was upgraded and prior configurations are in place. Depending on your configuration and need, you can configure fine grain access to logs using the following:

* Cluster wide policies
* Namespace scoped policies
* Creation of custom admin groups

As an administrator, you need to create the role bindings and cluster role bindings appropriate for your deployment. The {clo} provides the following cluster roles:

* `cluster-logging-application-view` grants permission to read application logs.
* `cluster-logging-infrastructure-view` grants permission to read infrastructure logs.
* `cluster-logging-audit-view` grants permission to read audit logs.

If you have upgraded from a prior version, an additional cluster role `logging-application-logs-reader` and associated cluster role binding `logging-all-authenticated-application-logs-reader` provide backward compatibility, allowing any authenticated user read access in their namespaces.

[NOTE]
====
Users with access by namespace must provide a namespace when querying application logs.
====

== Cluster wide access
Cluster role binding resources reference cluster roles, and set permissions cluster wide.

.Example ClusterRoleBinding
[source,yaml]
----
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: logging-all-application-logs-reader
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-logging-application-view # <1>
subjects: # <2>
- kind: Group
  name: system:authenticated
  apiGroup: rbac.authorization.k8s.io
----
<1> Additional `ClusterRoles` are `cluster-logging-infrastructure-view`, and `cluster-logging-audit-view`.
<2> Specifies the users or groups this object applies to.

== Namespaced access

`RoleBinding` resources can be used with `ClusterRole` objects to define the namespace a user or group has access to logs for.

.Example RoleBinding
[source,yaml]
----
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: allow-read-logs
  namespace: log-test-0 # <1>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-logging-application-view
subjects:
- kind: User
  apiGroup: rbac.authorization.k8s.io
  name: testuser-0
----
<1> Specifies the namespace this `RoleBinding` applies to.

// tag::CustomAdmin[]
== Custom admin group access

// tag::LokiMode[]
If you have a large deployment with several users who require broader permissions, you can create a custom group using the `adminGroup` field. Users who are members of any group specified in the `adminGroups` field of the `LokiStack` CR are considered administrators.
// end::LokiMode[]

// tag::NetObservMode[]
If you need to see cluster-wide logs without necessarily being an administrator, or if you already have any group defined that you want to use here, you can specify a custom group using the `adminGroup` field. Users who are members of any group specified in the `adminGroups` field of the `LokiStack` custom resource (CR) have the same read access to logs as administrators.
// end::NetObservMode[]

// tag::LokiMode[]
Administrator users have access to all application logs in all namespaces, if they also get assigned the `cluster-logging-application-view` role.
// end::LokiMode[]

// tag::NetObservMode[]
Administrator users have access to all network logs across the cluster.
// end::NetObservMode[]

.Example LokiStack CR
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
# tag::LokiMode[]
  name: logging-loki
  namespace: openshift-logging
# end::LokiMode[]
# tag::NetObservMode[]
  name: loki
  namespace: netobserv
# end::NetObservMode[]
spec:
  tenants:
# tag::LokiMode[]
    mode: openshift-logging # <1>
# end::LokiMode[]
# tag::NetObservMode[]
    mode: openshift-network # <1>
# end::NetObservMode[]
    openshift:
      adminGroups: # <2>
      - cluster-admin
      - custom-admin-group # <3>
----
<1> Custom admin groups are only available in this mode.
<2> Entering an empty list `[]` value for this field disables admin groups.
<3> Overrides the default groups (`system:cluster-admins`, `cluster-admin`, `dedicated-admin`)
// end::CustomAdmin[]

[role="_additional-resources"]
.Additional resources

* Using RBAC to define and apply permissions

// Module included in the following assemblies:
//
// * observability/logging/log_storage/cluster-logging-loki.adoc

[id="logging-loki-retention_{context}"]
= Enabling stream-based retention with Loki

With Logging version 5.6 and higher, you can configure retention policies based on log streams. Rules for these may be set globally, per tenant, or both. If you configure both, tenant rules apply before global rules.

[NOTE]
====
Although logging version 5.9 and higher supports schema v12, v13 is recommended.
====

. To enable stream-based retention, create a `LokiStack` CR:
+
.Example global stream-based retention for AWS
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
  limits:
   global: <1>
      retention: <2>
        days: 20
        streams:
        - days: 4
          priority: 1
          selector: '{kubernetes_namespace_name=~"test.+"}' <3>
        - days: 1
          priority: 1
          selector: '{log_type="infrastructure"}'
  managementState: Managed
  replicationFactor: 1
  size: 1x.small
  storage:
    schemas:
    - effectiveDate: "2020-10-11"
      version: v11
    secret:
      name: logging-loki-s3
      type: aws
  storageClassName: gp3-csi
  tenants:
    mode: openshift-logging
----
<1> Sets retention policy for all log streams. *Note: This field does not impact the retention period for stored logs in object storage.*
<2> Retention is enabled in the cluster when this block is added to the CR.
<3> Contains the LogQL query used to define the log stream.spec:
  limits:

.Example per-tenant stream-based retention for AWS
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
  limits:
    global:
      retention:
        days: 20
    tenants: <1>
      application:
        retention:
          days: 1
          streams:
            - days: 4
              selector: '{kubernetes_namespace_name=~"test.+"}' <2>
      infrastructure:
        retention:
          days: 5
          streams:
            - days: 1
              selector: '{kubernetes_namespace_name=~"openshift-cluster.+"}'
  managementState: Managed
  replicationFactor: 1
  size: 1x.small
  storage:
    schemas:
    - effectiveDate: "2020-10-11"
      version: v11
    secret:
      name: logging-loki-s3
      type: aws
  storageClassName: gp3-csi
  tenants:
    mode: openshift-logging
----
<1> Sets retention policy by tenant. Valid tenant types are `application`, `audit`, and `infrastructure`.
<2> Contains the LogQL query used to define the log stream.

2 Apply the `LokiStack` CR:

[source,terminal]
----
$ oc apply -f <filename>.yaml
----

[NOTE]
====
This is not for managing the retention for stored logs. Global retention periods for stored logs to a supported maximum of 30 days is configured with your object storage.
====
// Module is included in the following assemblies:
// * logging/cluster-logging-loki.adoc
// * observability/logging/log_collection_forwarding/log-forwarding.adoc
// * observability/logging/troubleshooting/log-forwarding-troubleshooting.adoc

[id="loki-rate-limit-errors_{context}"]
= Troubleshooting Loki rate limit errors

If the Log Forwarder API forwards a large block of messages that exceeds the rate limit to Loki, Loki generates rate limit (`429`) errors.

These errors can occur during normal operation. For example, when adding the {logging} to a cluster that already has some logs, rate limit errors might occur while the {logging} tries to ingest all of the existing log entries. In this case, if the rate of addition of new logs is less than the total rate limit, the historical data is eventually ingested, and the rate limit errors are resolved without requiring user intervention.

In cases where the rate limit errors continue to occur, you can fix the issue by modifying the `LokiStack` custom resource (CR).

[IMPORTANT]
====
The `LokiStack` CR is not available on Grafana-hosted Loki. This topic does not apply to Grafana-hosted Loki servers.
====

.Conditions

* The Log Forwarder API is configured to forward logs to Loki.

* Your system sends a block of messages that is larger than 2 MB to Loki. For example:
+
[source,text]
----
"values":[["1630410392689800468","{\"kind\":\"Event\",\"apiVersion\":\
.......
......
......
......
\"received_at\":\"2021-08-31T11:46:32.800278+00:00\",\"version\":\"1.7.4 1.6.0\"}},\"@timestamp\":\"2021-08-31T11:46:32.799692+00:00\",\"viaq_index_name\":\"audit-write\",\"viaq_msg_id\":\"MzFjYjJkZjItNjY0MC00YWU4LWIwMTEtNGNmM2E5ZmViMGU4\",\"log_type\":\"audit\"}"]]}]}
----

* After you enter `oc logs -n openshift-logging -l component=collector`, the collector logs in your cluster show a line containing one of the following error messages:
+
[source,text]
----
429 Too Many Requests Ingestion rate limit exceeded
----
+
.Example Vector error message
[source,text]
----
2023-08-25T16:08:49.301780Z  WARN sink{component_kind="sink" component_id=default_loki_infra component_type=loki component_name=default_loki_infra}: vector::sinks::util::retries: Retrying after error. error=Server responded with an error: 429 Too Many Requests internal_log_rate_limit=true
----
+
.Example Fluentd error message
[source,text]
----
2023-08-30 14:52:15 +0000 [warn]: [default_loki_infra] failed to flush the buffer. retry_times=2 next_retry_time=2023-08-30 14:52:19 +0000 chunk="604251225bf5378ed1567231a1c03b8b" error_class=Fluent::Plugin::LokiOutput::LogPostError error="429 Too Many Requests Ingestion rate limit exceeded for user infrastructure (limit: 4194304 bytes/sec) while attempting to ingest '4082' lines totaling '7820025' bytes, reduce log volume or contact your Loki administrator to see if the limit can be increased\n"
----
+
The error is also visible on the receiving end. For example, in the LokiStack ingester pod:
+
.Example Loki ingester error message
[source,text]
----
level=warn ts=2023-08-30T14:57:34.155592243Z caller=grpc_logging.go:43 duration=1.434942ms method=/logproto.Pusher/Push err="rpc error: code = Code(429) desc = entry with timestamp 2023-08-30 14:57:32.012778399 +0000 UTC ignored, reason: 'Per stream rate limit exceeded (limit: 3MB/sec) while attempting to ingest for stream
----

.Procedure

* Update the `ingestionBurstSize` and `ingestionRate` fields in the `LokiStack` CR:
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
  limits:
    global:
      ingestion:
        ingestionBurstSize: 16 # <1>
        ingestionRate: 8 # <2>
# ...
----
<1> The `ingestionBurstSize` field defines the maximum local rate-limited sample size per distributor replica in MB. This value is a hard limit. Set this value to at least the maximum logs size expected in a single push request. Single requests that are larger than the `ingestionBurstSize` value are not permitted.
<2> The `ingestionRate` field is a soft limit on the maximum amount of ingested samples per second in MB. Rate limit errors occur if the rate of logs exceeds the limit, but the collector retries sending the logs. As long as the total average is lower than the limit, the system recovers and errors are resolved without user intervention.
// Module included in the following assemblies:
//
// * logging/cluster-logging-loki.adoc

[id="logging-loki-memberlist-ip_{context}"]
= Configuring Loki to tolerate memberlist creation failure

In an OpenShift cluster, administrators generally use a non-private IP network range. As a result, the LokiStack memberlist configuration fails because, by default, it only uses private IP networks.

As an administrator, you can select the pod network for the memberlist configuration. You can modify the LokiStack CR to use the `podIP` in the `hashRing` spec. To configure the LokiStack CR, use the following command:

[source,terminal]
----
$ oc patch LokiStack logging-loki -n openshift-logging  --type=merge -p '{"spec": {"hashRing":{"memberlist":{"instanceAddrType":"podIP","type": "memberlist"}}}}'
----

.Example LokiStack to include `podIP`
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: logging-loki
  namespace: openshift-logging
spec:
# ...
  hashRing:
    type: memberlist
    memberlist:
      instanceAddrType: podIP
# ...
----

[role="_additional-resources"]
[id="additional-resources_cluster-logging-loki"]
== Additional resources
* Loki components documentation
* Loki Query Language (LogQL) documentation
* Grafana Dashboard documentation
* Loki Object Storage documentation
* {loki-op} `IngestionLimitSpec` documentation
* Loki Storage Schema documentation
