---
title: "Updating Logging"
type: reference
domain: openshift
slug: observability-4-22-cluster-logging-upgrading
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/cluster-logging-upgrading
version: 4.22
family: observability
documentKind: "Documentation"
---

# Updating Logging

[id="cluster-logging-upgrading"]
= Updating Logging

There are two types of {logging} updates: minor release updates (5.y.z) and major release updates (5.y).

[id="cluster-logging-upgrading-minor"]
== Minor release updates

If you installed the {logging} Operators using the *Automatic* update approval option, your Operators receive minor version updates automatically. You do not need to complete any manual update steps.

If you installed the {logging} Operators using the *Manual* update approval option, you must manually approve minor version updates. For more information, see Manually approving a pending Operator update.

[id="cluster-logging-upgrading-major"]
== Major release updates

For major version updates you must complete some manual steps.

For major release version compatibility and support information, see OpenShift Operator Life Cycles.

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-upgrading.adoc

[id="logging-operator-upgrading-all-ns_{context}"]
= Upgrading the {clo} to watch all namespaces

In logging 5.7 and older versions, the {clo} only watches the `openshift-logging` namespace.
If you want the {clo} to watch all namespaces on your cluster, you must redeploy the Operator. You can complete the following procedure to redeploy the Operator without deleting your logging components.

.Prerequisites

* You have installed the {oc-first}.
* You have administrator permissions.

.Procedure

. Delete the subscription by running the following command:
+
[source,terminal]
----
$ oc -n openshift-logging delete subscription <subscription>
----

. Delete the Operator group by running the following command:
+
[source,terminal]
----
$ oc -n openshift-logging delete operatorgroup <operator_group_name>
----

. Delete the cluster service version (CSV) by running the following command:
+
[source,terminal]
----
$ oc delete clusterserviceversion cluster-logging.<version>
----

. Redeploy the {clo} by following the "Installing Logging" documentation.

.Verification

* Check that the `targetNamespaces` field in the `OperatorGroup` resource is not present or is set to an empty string.
+
To do this, run the following command and inspect the output:
+
[source,terminal]
----
$ oc get operatorgroup <operator_group_name> -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-logging-f52cn
  namespace: openshift-logging
spec:
  upgradeStrategy: Default
status:
  namespaces:
  - ""
# ...
----

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-upgrading.adoc

[id="logging-upgrading-clo_{context}"]
= Updating the {clo}

To update the {clo} to a new major release version, you must modify the update channel for the Operator subscription.

.Prerequisites

* You have installed the {clo}.
* You have administrator permissions.
* You have access to the OpenShift Container Platform web console and are viewing the *Administrator* perspective.

.Procedure

. Navigate to *Ecosystem* -> *Installed Operators*.

. Select the *openshift-logging* project.

. Click the *Red Hat OpenShift Logging* Operator.

. Click *Subscription*. In the *Subscription details* section, click the *Update channel* link. This link text might be *stable* or *stable-5.9*, depending on your current update channel.

. In the *Change Subscription Update Channel* window, select the latest major version update channel, *stable-5.9*, and click *Save*. Note the `cluster-logging.v5.9.<z>` version.

. Wait for a few seconds, and then go to *Ecosystem* -> *Installed Operators* to verify that the {clo} version matches the latest `cluster-logging.v5.9.<z>` version.

. On the *Ecosystem* -> *Installed Operators* page, wait for the *Status* field to report *Succeeded*.

. Check if the `LokiStack` custom resource contains the `v13` schema version and add it if it is missing. For correctly adding the `v13` schema version, see "Upgrading the LokiStack storage schema".

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-upgrading.adoc

[id="logging-upgrading-loki_{context}"]
= Updating the {loki-op}

To update the {loki-op} to a new major release version, you must modify the update channel for the Operator subscription.

.Prerequisites

* You have installed the {loki-op}.
* You have administrator permissions.
* You have access to the OpenShift Container Platform web console and are viewing the *Administrator* perspective.

.Procedure

. Navigate to *Ecosystem* -> *Installed Operators*.

. Select the *openshift-operators-redhat* project.

. Click the *{loki-op}*.

. Click *Subscription*. In the *Subscription details* section, click the *Update channel* link. This link text might be *stable* or *stable-5.y*, depending on your current update channel.

. In the *Change Subscription Update Channel* window, select the latest major version update channel, *stable-5.y*, and click *Save*. Note the `loki-operator.v5.y.z` version.

. Wait for a few seconds, then click *Ecosystem* -> *Installed Operators*. Verify that the {loki-op} version matches the latest `loki-operator.v5.y.z` version.

. On the *Ecosystem* -> *Installed Operators* page, wait for the *Status* field to report *Succeeded*.

. Check if the `LokiStack` custom resource contains the `v13` schema version and add it if it is missing. For correctly adding the `v13` schema version, see "Upgrading the LokiStack storage schema".

// Module included in the following assemblies:
//
// * observability/logging/cluster-logging-upgrading.adoc

[id="logging-upgrading-loki-schema_{context}"]
= Upgrading the LokiStack storage schema

If you are using the {clo} with the {loki-op}, the {clo} 5.9 or later supports the `v13` schema version in the `LokiStack` custom resource. Upgrading to the `v13` schema version is recommended because it is the schema version to be supported going forward.

.Procedure

* Add the `v13` schema version in the `LokiStack` custom resource as follows:
+
[source,yaml]
----
apiVersion: loki.grafana.com/v1
kind: LokiStack
# ...
spec:
# ...
  storage:
    schemas:
    # ...
      version: v12 # <1>
    - effectiveDate: "<yyyy>-<mm>-<future_dd>" # <2>
      version: v13
# ...
----
<1> Do not delete. Data persists in its original schema version. Keep the previous schema versions to avoid data loss.
<2> Set a future date that has not yet started in the Coordinated Universal Time (UTC) time zone.
+
[TIP]
====
To edit the `LokiStack` custom resource, you can run the `oc edit` command:

[source,terminal]
----
$ oc edit lokistack <name> -n openshift-logging
----
====

.Verification

* On or after the specified `effectiveDate` date, check that there is no *LokistackSchemaUpgradesRequired* alert in the web console in *Administrator* -> *Observe* -> *Alerting*.

// Module file include in the following assemblies:
//
// * observability/logging/cluster-logging-upgrading.adoc

[id="cluster-logging-upgrading-elasticsearch_{context}"]
= Updating the {es-op}

To update the {es-op} to the current version, you must modify the subscription.

.Prerequisites

* If you are using Elasticsearch as the default log store, and Kibana as the UI, update the {es-op} before you update the {clo}.
+
[IMPORTANT]
====
If you update the Operators in the wrong order, Kibana does not update and the Kibana custom resource (CR) is not created. To fix this issue, delete the {clo} pod. When the {clo} pod redeploys, it creates the Kibana CR and Kibana becomes available again.
====

* The Logging status is healthy:
** All pods have a `ready` status.
** The Elasticsearch cluster is healthy.

* Your Elasticsearch and Kibana data is backed up.
* You have administrator permissions.
* You have installed the {oc-first} for the verification steps.

.Procedure

. In the OpenShift Container Platform web console, click *Ecosystem* -> *Installed Operators*.
. In the {hybrid-console}, click *Ecosystem* -> *Installed Operators*.

. Select the *openshift-operators-redhat* project.

. Click *OpenShift Elasticsearch Operator*.

. Click *Subscription* -> *Channel*.

. In the *Change Subscription Update Channel* window, select *stable-5.y* and click *Save*. Note the `elasticsearch-operator.v5.y.z` version.

. Wait for a few seconds, then click *Ecosystem* -> *Installed Operators*. Verify that the {es-op} version matches the latest `elasticsearch-operator.v5.y.z` version.

. On the *Ecosystem* -> *Installed Operators* page, wait for the *Status* field to report *Succeeded*.

.Verification

. Verify that all Elasticsearch pods have a *Ready* status by entering the following command and observing the output:
+
[source,terminal]
----
$ oc get pod -n openshift-logging --selector component=elasticsearch
----
+
.Example output
[source,terminal]
----
NAME                                            READY   STATUS    RESTARTS   AGE
elasticsearch-cdm-1pbrl44l-1-55b7546f4c-mshhk   2/2     Running   0          31m
elasticsearch-cdm-1pbrl44l-2-5c6d87589f-gx5hk   2/2     Running   0          30m
elasticsearch-cdm-1pbrl44l-3-88df5d47-m45jc     2/2     Running   0          29m
----

. Verify that the Elasticsearch cluster status is `green` by entering the following command and observing the output:
+
[source,terminal]
----
$ oc exec -n openshift-logging -c elasticsearch elasticsearch-cdm-1pbrl44l-1-55b7546f4c-mshhk -- health
----
+
.Example output
[source,json]
----
{
  "cluster_name" : "elasticsearch",
  "status" : "green",
}
----

. Verify that the Elasticsearch cron jobs are created by entering the following commands and observing the output:
+
[source,terminal]
----
$ oc project openshift-logging
----
+
[source,terminal]
----
$ oc get cronjob
----
+
.Example output
[source,terminal]
----
NAME                     SCHEDULE       SUSPEND   ACTIVE   LAST SCHEDULE   AGE
elasticsearch-im-app     */15 * * * *   False     0        <none>          56s
elasticsearch-im-audit   */15 * * * *   False     0        <none>          56s
elasticsearch-im-infra   */15 * * * *   False     0        <none>          56s
----

. Verify that the log store is updated to the correct version and the indices are `green` by entering the following command and observing the output:
+
[source,terminal]
----
$ oc exec -c elasticsearch <any_es_pod_in_the_cluster> -- indices
----
+
Verify that the output includes the `app-00000x`, `infra-00000x`, `audit-00000x`, `.security` indices:
+
.Sample output with indices in a green status
[%collapsible]
====
[source,terminal]
----
Tue Jun 30 14:30:54 UTC 2020
health status index                                                                 uuid                   pri rep docs.count docs.deleted store.size pri.store.size
green  open   infra-000008                                                          bnBvUFEXTWi92z3zWAzieQ   3 1       222195            0        289            144
green  open   infra-000004                                                          rtDSzoqsSl6saisSK7Au1Q   3 1       226717            0        297            148
green  open   infra-000012                                                          RSf_kUwDSR2xEuKRZMPqZQ   3 1       227623            0        295            147
green  open   .kibana_7                                                             1SJdCqlZTPWlIAaOUd78yg   1 1            4            0          0              0
green  open   infra-000010                                                          iXwL3bnqTuGEABbUDa6OVw   3 1       248368            0        317            158
green  open   infra-000009                                                          YN9EsULWSNaxWeeNvOs0RA   3 1       258799            0        337            168
green  open   infra-000014                                                          YP0U6R7FQ_GVQVQZ6Yh9Ig   3 1       223788            0        292            146
green  open   infra-000015                                                          JRBbAbEmSMqK5X40df9HbQ   3 1       224371            0        291            145
green  open   .orphaned.2020.06.30                                                  n_xQC2dWQzConkvQqei3YA   3 1            9            0          0              0
green  open   infra-000007                                                          llkkAVSzSOmosWTSAJM_hg   3 1       228584            0        296            148
green  open   infra-000005                                                          d9BoGQdiQASsS3BBFm2iRA   3 1       227987            0        297            148
green  open   infra-000003                                                          1-goREK1QUKlQPAIVkWVaQ   3 1       226719            0        295            147
green  open   .security                                                             zeT65uOuRTKZMjg_bbUc1g   1 1            5            0          0              0
green  open   .kibana-377444158_kubeadmin                                           wvMhDwJkR-mRZQO84K0gUQ   3 1            1            0          0              0
green  open   infra-000006                                                          5H-KBSXGQKiO7hdapDE23g   3 1       226676            0        295            147
green  open   infra-000001                                                          eH53BQ-bSxSWR5xYZB6lVg   3 1       341800            0        443            220
green  open   .kibana-6                                                             RVp7TemSSemGJcsSUmuf3A   1 1            4            0          0              0
green  open   infra-000011                                                          J7XWBauWSTe0jnzX02fU6A   3 1       226100            0        293            146
green  open   app-000001                                                            axSAFfONQDmKwatkjPXdtw   3 1       103186            0        126             57
green  open   infra-000016                                                          m9c1iRLtStWSF1GopaRyCg   3 1        13685            0         19              9
green  open   infra-000002                                                          Hz6WvINtTvKcQzw-ewmbYg   3 1       228994            0        296            148
green  open   infra-000013                                                          KR9mMFUpQl-jraYtanyIGw   3 1       228166            0        298            148
green  open   audit-000001                                                          eERqLdLmQOiQDFES1LBATQ   3 1            0            0          0              0
----
====

. Verify that the log visualizer is updated to the correct version by entering the following command and observing the output:
+
[source,terminal]
----
$ oc get kibana kibana -o json
----
+
Verify that the output includes a Kibana pod with the `ready` status:
+
.Sample output with a ready Kibana pod
[%collapsible]
====
[source,json]
----
[
{
"clusterCondition": {
"kibana-5fdd766ffd-nb2jj": [
{
"lastTransitionTime": "2020-06-30T14:11:07Z",
"reason": "ContainerCreating",
"status": "True",
"type": ""
},
{
"lastTransitionTime": "2020-06-30T14:11:07Z",
"reason": "ContainerCreating",
"status": "True",
"type": ""
}
]
},
"deployment": "kibana",
"pods": {
"failed": [],
"notReady": []
"ready": []
},
"replicaSets": [
"kibana-5fdd766ffd"
],
"replicas": 1
}
]
----
====
