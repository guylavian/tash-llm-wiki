---
title: "Troubleshooting OVN-Kubernetes"
type: reference
domain: openshift
slug: networking-4-22-ovn-kubernetes-troubleshooting-sources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/ovn-kubernetes-troubleshooting-sources
version: 4.22
family: networking
documentKind: "Documentation"
---

# Troubleshooting OVN-Kubernetes

[id="ovn-kubernetes-troubleshooting-sources"]
= Troubleshooting OVN-Kubernetes

[role="_abstract"]
To troubleshoot OVN-Kubernetes in OpenShift Container Platform, you can use built-in health checks, alerting, logs, and connectivity checks. Follow these sections to examine your cluster before opening a support case.

OVN-Kubernetes has many sources of built-in health checks and logs. Follow the instructions in these sections to examine your cluster. If a support case is necessary, collect additional information through a `must-gather` as described in the Additional resources section. Only use the `-- gather_network_logs` option when instructed by support.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-readiness-probes_{context}"]
= Monitoring OVN-Kubernetes health by using readiness probes

[role="_abstract"]
To monitor OVN-Kubernetes component health in OpenShift Container Platform, you can review readiness probe configuration and status for `ovnkube-control-plane` and `ovnkube-node` pods.

.Prerequisites

* Access to the OpenShift CLI (`oc`).
* You have access to the cluster with `cluster-admin` privileges.
* You have installed `jq`.

.Procedure

. Review the details of the `ovnkube-node` readiness probe by running the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node \
-o json | jq '.items[0].spec.containers[] | .name,.readinessProbe'
----
+
The readiness probe for the northbound and southbound database containers in the `ovnkube-node` pod checks for the health of the databases and the `ovnkube-controller` container.

+
The `ovnkube-controller` container in the `ovnkube-node` pod has a readiness probe to verify the presence of the OVN-Kubernetes CNI configuration file, the absence of which would indicate that the pod is not running or is not ready to accept requests to configure pods.

. Show all events including the probe failures, for the namespace by using the following command:
+
[source,terminal]
----
$ oc get events -n openshift-ovn-kubernetes
----

. Show the events for just a specific pod:
+
[source,terminal]
----
$ oc describe pod ovnkube-node-9lqfk -n openshift-ovn-kubernetes
----

. Show the messages and statuses from the cluster network operator:
+
[source,terminal]
----
$ oc get co/network -o json | jq '.status.conditions[]'
----

. Show the `ready` status of each container in `ovnkube-node` pods by running the following script:
+
[source,terminal]
----
$ for p in $(oc get pods --selector app=ovnkube-node -n openshift-ovn-kubernetes \
-o jsonpath='{range.items[*]}{" "}{.metadata.name}'); do echo === $p ===;  \
oc get pods -n openshift-ovn-kubernetes $p -o json | jq '.status.containerStatuses[] | .name, .ready'; \
done
----
+
[NOTE]
====
The expectation is all container statuses are reporting as `true`. Failure of a readiness probe sets the status to `false`.
====

[role="_additional-resources"]
.Additional resources

* Monitoring application health by using health checks

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-alerts-console_{context}"]
= Viewing OVN-Kubernetes alerts in the console

[role="_abstract"]
To view OVN-Kubernetes alerts in the OpenShift Container Platform web console, you can open *Observe* -> *Alerting* to inspect rules, alerts, and silences.

The Alerting UI provides detailed information about alerts and their governing alerting rules and silences.

.Prerequisites

* You have access to the cluster as a developer or as a user with view permissions for the project that you are viewing metrics for.

.Procedure

. In the *Administrator* perspective, select *Observe* -> *Alerting*. The three main pages in the Alerting UI in this perspective are the *Alerts*, *Silences*, and *Alerting Rules* pages.

. View the rules for OVN-Kubernetes alerts by selecting *Observe* -> *Alerting* -> *Alerting Rules*.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-alerts-cli_{context}"]
= Viewing OVN-Kubernetes alerts in the CLI

[role="_abstract"]
To view OVN-Kubernetes alerts from the command line in OpenShift Container Platform, you can query the `Alertmanager` API for active alerts and related rules.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.
* The OpenShift CLI (`oc`) installed.
* You have installed `jq`.

.Procedure

. View active or firing alerts by running the following commands.

.. Set the alert manager route environment variable by running the following command:
+
[source,terminal]
----
$ ALERT_MANAGER=$(oc get route alertmanager-main -n openshift-monitoring \
-o jsonpath='{@.spec.host}')
----

.. Issue a `curl` request to the alert manager route API by running the following command, replacing `$ALERT_MANAGER` with the URL of your `Alertmanager` instance:
+
[source,terminal]
----
$ curl -s -k -H "Authorization: Bearer $(oc create token prometheus-k8s -n openshift-monitoring)" https://$ALERT_MANAGER/api/v1/alerts | jq '.data[] | "\(.labels.severity) \(.labels.alertname) \(.labels.pod) \(.labels.container) \(.labels.endpoint) \(.labels.instance)"'
----

. View alerting rules by running the following command:
+
[source,terminal]
----
$ oc -n openshift-monitoring exec -c prometheus prometheus-k8s-0 -- curl -s 'http://localhost:9090/api/v1/rules' | jq '.data.groups[].rules[] | select(((.name|contains("ovn")) or (.name|contains("OVN")) or (.name|contains("Ovn")) or (.name|contains("North")) or (.name|contains("South"))) and .type=="alerting")'
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-logs-cli_{context}"]
= Viewing the OVN-Kubernetes logs using the CLI

[role="_abstract"]
To view OVN-Kubernetes pod logs in OpenShift Container Platform, you can use the {oc-first} to examine logs from containers in the `openshift-ovn-kubernetes` namespace.

.Prerequisites

* Access to the cluster as a user with the `cluster-admin` role.
* Access to the OpenShift CLI (`oc`).
* You have installed `jq`.

.Procedure

. View the log for a specific pod:
+
[source,terminal]
----
$ oc logs -f <pod_name> -c <container_name> -n <namespace>
----
+
--
where:

`-f`:: Optional: Specifies that the output follows what is being written into the logs.
`<pod_name>`:: Specifies the name of the pod.
`<container_name>`:: Optional: Specifies the name of a container. When a pod has more than one container, you must specify the container name.
`<namespace>`:: Specify the namespace the pod is running in.
--
+
For example:
+
[source,terminal]
----
$ oc logs ovnkube-node-5dx44 -n openshift-ovn-kubernetes
----
+
[source,terminal]
----
$ oc logs -f ovnkube-node-5dx44 -c ovnkube-controller -n openshift-ovn-kubernetes
----
+
The contents of log files are printed out.

. Examine the most recent entries in all the containers in the `ovnkube-node` pods:
+
[source,terminal]
----
$ for p in $(oc get pods --selector app=ovnkube-node -n openshift-ovn-kubernetes \
-o jsonpath='{range.items[*]}{" "}{.metadata.name}'); \
do echo === $p ===; for container in $(oc get pods -n openshift-ovn-kubernetes $p \
-o json | jq -r '.status.containerStatuses[] | .name');do echo ---$container---; \
oc logs -c $container $p -n openshift-ovn-kubernetes --tail=5; done; done
----

. View the last 5 lines of every log in every container in an `ovnkube-node` pod using the following command:
+
[source,terminal]
----
$ oc logs -l app=ovnkube-node -n openshift-ovn-kubernetes --all-containers --tail 5
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-logs-console_{context}"]
= Viewing the OVN-Kubernetes logs using the web console

[role="_abstract"]
To view OVN-Kubernetes pod logs in the OpenShift Container Platform web console, you can open pod logs for each container in the `openshift-ovn-kubernetes` project.

.Prerequisites
* Access to the OpenShift CLI (`oc`).

.Procedure

. In the OpenShift Container Platform console, navigate to *Workloads* -> *Pods* or navigate to the pod through the resource you want to investigate.

. Select the `openshift-ovn-kubernetes` project from the drop-down menu.

. Click the name of the pod you want to investigate.

. Click *Logs*. By default for the `ovnkube-master` the logs associated with the `northd` container are displayed.

. Use the down-down menu to select logs for each container in turn.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-change-log-levels_{context}"]
= Changing the OVN-Kubernetes log levels

[role="_abstract"]
To debug OVN-Kubernetes in OpenShift Container Platform, you can raise log levels by applying an `env-overrides` `ConfigMap` and restarting affected pods.

The default log level for OVN-Kubernetes is 4. To debug OVN-Kubernetes, set the log level to 5. Follow this procedure to increase the log level of the OVN-Kubernetes to help you debug an issue.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Run the following command to get detailed information for all pods in the OVN-Kubernetes project:
+
[source,terminal]
----
$ oc get po -o wide -n openshift-ovn-kubernetes
----
+
.Example output
[source,terminal]
----
NAME                                     READY   STATUS    RESTARTS       AGE    IP           NODE                                       NOMINATED NODE   READINESS GATES
ovnkube-control-plane-65497d4548-9ptdr   2/2     Running   2 (128m ago)   147m   10.0.0.3     ci-ln-3njdr9b-72292-5nwkp-master-0         <none>           <none>
ovnkube-control-plane-65497d4548-j6zfk   2/2     Running   0              147m   10.0.0.5     ci-ln-3njdr9b-72292-5nwkp-master-2         <none>           <none>
ovnkube-node-5dx44                       8/8     Running   0              146m   10.0.0.3     ci-ln-3njdr9b-72292-5nwkp-master-0         <none>           <none>
ovnkube-node-dpfn4                       8/8     Running   0              146m   10.0.0.4     ci-ln-3njdr9b-72292-5nwkp-master-1         <none>           <none>
ovnkube-node-kwc9l                       8/8     Running   0              134m   10.0.128.2   ci-ln-3njdr9b-72292-5nwkp-worker-a-2fjcj   <none>           <none>
ovnkube-node-mcrhl                       8/8     Running   0              134m   10.0.128.4   ci-ln-3njdr9b-72292-5nwkp-worker-c-v9x5v   <none>           <none>
ovnkube-node-nsct4                       8/8     Running   0              146m   10.0.0.5     ci-ln-3njdr9b-72292-5nwkp-master-2         <none>           <none>
ovnkube-node-zrj9f                       8/8     Running   0              134m   10.0.128.3   ci-ln-3njdr9b-72292-5nwkp-worker-b-v78h7   <none>           <none>
----

. Create a `ConfigMap` file similar to the following example and use a filename such as `env-overrides.yaml`:
+
[source,yaml]
.Example `ConfigMap` file
----
kind: ConfigMap
apiVersion: v1
metadata:
  name: env-overrides
  namespace: openshift-ovn-kubernetes
data:
  ci-ln-3njdr9b-72292-5nwkp-master-0: |
    # This sets the log level for the ovn-kubernetes node process:
    OVN_KUBE_LOG_LEVEL=5
    # You might also/instead want to enable debug logging for ovn-controller:
    OVN_LOG_LEVEL=dbg
  ci-ln-3njdr9b-72292-5nwkp-master-2: |
    # This sets the log level for the ovn-kubernetes node process:
    OVN_KUBE_LOG_LEVEL=5
    # You might also/instead want to enable debug logging for ovn-controller:
    OVN_LOG_LEVEL=dbg
  _master: |
    # This sets the log level for the ovn-kubernetes master process as well as the ovn-dbchecker:
    OVN_KUBE_LOG_LEVEL=5
    # You might also/instead want to enable debug logging for northd, nbdb and sbdb on all masters:
    OVN_LOG_LEVEL=dbg
----
+
where::
`ci-ln-3njdr9b-72292-5nwkp-master-0:`:: Specifies the name of the node you want to set the debug log level on.
`_master:`:: Specifies `_master` to set the log levels of `ovnkube-master` components.

. Apply the `ConfigMap` file by using the following command:
+
[source,terminal]
----
$ oc apply -n openshift-ovn-kubernetes -f env-overrides.yaml
----
+
.Example output
[source,terminal]
----
configmap/env-overrides.yaml created
----

. Restart the `ovnkube` pods to apply the new log level by using the following commands:
+
[source,terminal]
----
$ oc delete pod -n openshift-ovn-kubernetes \
--field-selector spec.nodeName=ci-ln-3njdr9b-72292-5nwkp-master-0 -l app=ovnkube-node
----
+
[source,terminal]
----
$ oc delete pod -n openshift-ovn-kubernetes \
--field-selector spec.nodeName=ci-ln-3njdr9b-72292-5nwkp-master-2 -l app=ovnkube-node
----
+
[source,terminal]
----
$ oc delete pod -n openshift-ovn-kubernetes -l app=ovnkube-node
----

. To verify that the `ConfigMap`file has been applied to all nodes for a specific pod, run the following command:
+
[source,terminal]
----
$ oc logs -n openshift-ovn-kubernetes --all-containers --prefix ovnkube-node-<xxxx> | grep -E -m 10 '(Logging config:|vconsole|DBG)'
----
+
where:
`<XXXX>`:: Specifies the random sequence of letters for a pod from the previous step.
+
.Example output
[source,terminal]
----
[pod/ovnkube-node-2cpjc/sbdb] + exec /usr/share/ovn/scripts/ovn-ctl --no-monitor '--ovn-sb-log=-vconsole:info -vfile:off -vPATTERN:console:%D{%Y-%m-%dT%H:%M:%S.###Z}|%05N|%c%T|%p|%m' run_sb_ovsdb
[pod/ovnkube-node-2cpjc/ovnkube-controller] I1012 14:39:59.984506   35767 config.go:2247] Logging config: {File: CNIFile:/var/log/ovn-kubernetes/ovn-k8s-cni-overlay.log LibovsdbFile:/var/log/ovnkube/libovsdb.log Level:5 LogFileMaxSize:100 LogFileMaxBackups:5 LogFileMaxAge:0 ACLLoggingRateLimit:20}
[pod/ovnkube-node-2cpjc/northd] + exec ovn-northd --no-chdir -vconsole:info -vfile:off '-vPATTERN:console:%D{%Y-%m-%dT%H:%M:%S.###Z}|%05N|%c%T|%p|%m' --pidfile /var/run/ovn/ovn-northd.pid --n-threads=1
[pod/ovnkube-node-2cpjc/nbdb] + exec /usr/share/ovn/scripts/ovn-ctl --no-monitor '--ovn-nb-log=-vconsole:info -vfile:off -vPATTERN:console:%D{%Y-%m-%dT%H:%M:%S.###Z}|%05N|%c%T|%p|%m' run_nb_ovsdb
[pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.552Z|00002|hmap|DBG|lib/shash.c:114: 1 bucket with 6+ nodes, including 1 bucket with 6 nodes (32 nodes total across 32 buckets)
[pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00003|hmap|DBG|lib/shash.c:114: 1 bucket with 6+ nodes, including 1 bucket with 6 nodes (64 nodes total across 64 buckets)
[pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00004|hmap|DBG|lib/shash.c:114: 1 bucket with 6+ nodes, including 1 bucket with 7 nodes (32 nodes total across 32 buckets)
[pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00005|reconnect|DBG|unix:/var/run/openvswitch/db.sock: entering BACKOFF
[pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00007|reconnect|DBG|unix:/var/run/openvswitch/db.sock: entering CONNECTING
[pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00008|ovsdb_cs|DBG|unix:/var/run/openvswitch/db.sock: SERVER_SCHEMA_REQUESTED -> SERVER_SCHEMA_REQUESTED at lib/ovsdb-cs.c:423
----

. Optional: Check the `ConfigMap` file has been applied by running the following command:
+
[source,terminal]
----
for f in $(oc -n openshift-ovn-kubernetes get po -l 'app=ovnkube-node' --no-headers -o custom-columns=N:.metadata.name) ; do echo "---- $f ----" ; oc -n openshift-ovn-kubernetes exec -c ovnkube-controller $f --  pgrep -a -f  init-ovnkube-controller | grep -P -o '^.*loglevel\s+\d' ; done
----
+
.Example output
[source,terminal]
----
---- ovnkube-node-2dt57 ----
60981 /usr/bin/ovnkube --init-ovnkube-controller xpst8-worker-c-vmh5n.c.openshift-qe.internal --init-node xpst8-worker-c-vmh5n.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
---- ovnkube-node-4zznh ----
178034 /usr/bin/ovnkube --init-ovnkube-controller xpst8-master-2.c.openshift-qe.internal --init-node xpst8-master-2.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
---- ovnkube-node-548sx ----
77499 /usr/bin/ovnkube --init-ovnkube-controller xpst8-worker-a-fjtnb.c.openshift-qe.internal --init-node xpst8-worker-a-fjtnb.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
---- ovnkube-node-6btrf ----
73781 /usr/bin/ovnkube --init-ovnkube-controller xpst8-worker-b-p8rww.c.openshift-qe.internal --init-node xpst8-worker-b-p8rww.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
---- ovnkube-node-fkc9r ----
130707 /usr/bin/ovnkube --init-ovnkube-controller xpst8-master-0.c.openshift-qe.internal --init-node xpst8-master-0.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 5
---- ovnkube-node-tk9l4 ----
181328 /usr/bin/ovnkube --init-ovnkube-controller xpst8-master-1.c.openshift-qe.internal --init-node xpst8-master-1.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-pod-connectivity-checks_{context}"]
= Checking the OVN-Kubernetes pod network connectivity

[role="_abstract"]
To verify pod network connectivity in OpenShift Container Platform, you can inspect `PodNetworkConnectivityCheck` resources in the `openshift-network-diagnostics` namespace.

The connectivity check controller, in OpenShift Container Platform 4.10 and later, orchestrates connection verification checks in your cluster. These include Kubernetes API, OpenShift API and individual nodes. The results for the connection tests are stored in `PodNetworkConnectivity` objects in the `openshift-network-diagnostics` namespace. Connection tests are performed every minute in parallel.

.Prerequisites

* You have access to the {oc-first}.
* You are logged in to the cluster with the `cluster-admin` role.
* You have installed `jq`.

.Procedure

. To list the current `PodNetworkConnectivityCheck` objects, enter the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics
----

. View the most recent success for each connection object by using the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
-o json | jq '.items[]| .spec.targetEndpoint,.status.successes[0]'
----

. View the most recent failures for each connection object by using the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
-o json | jq '.items[]| .spec.targetEndpoint,.status.failures[0]'
----

. View the most recent outages for each connection object by using the following command:
+
[source,terminal]
----
$ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
-o json | jq '.items[]| .spec.targetEndpoint,.status.outages[0]'
----
+
The connectivity check controller also logs metrics from these checks into Prometheus.

. View all the metrics by running the following command:
+
[source,terminal]
----
$ oc exec prometheus-k8s-0 -n openshift-monitoring -- \
promtool query instant  http://localhost:9090 \
'{component="openshift-network-diagnostics"}'
----

. View the latency between the source pod and the openshift api service for the last 5 minutes:
+
[source,terminal]
----
$ oc exec prometheus-k8s-0 -n openshift-monitoring -- \
promtool query instant  http://localhost:9090 \
'{component="openshift-network-diagnostics"}'
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="nw-ovn-kubernetes-observability_{context}"]
= Checking OVN-Kubernetes network traffic with OVS sampling using the CLI

[role="_abstract"]
To trace OVN-Kubernetes network traffic with OVS sampling in OpenShift Container Platform, you can enable the `OVNObservability` feature gate and run `ovnkube-observ` from an `ovnkube-node` pod.

OVN-Kubernetes network traffic can be viewed with OVS sampling via the CLI for the following network APIs:

* `NetworkPolicy`
* `AdminNetworkPolicy`
* `BaselineNetworkPolicy`
* `UserDefinedNetwork` isolation
* `EgressFirewall`
* Multicast ACLs.

Scripts for these networking events are found in the `/usr/bin/ovnkube-observ` path of each OVN-Kubernetes node.

Although both the Network Observability Operator and checking OVN-Kubernetes network traffic with OVS sampling are good for debuggability, the Network Observability Operator is intended for observing network events. Alternatively, checking OVN-Kubernetes network traffic with OVS sampling using the CLI is intended to help with packet tracing; it can also be used while the Network Observability Operator is installed, however that is not a requirement.

Administrators can add the `--add-ovs-collect` option to view network traffic across the node, or pass in additional flags to filter result for specific pods. Additional flags can be found in the "OVN-Kubernetes network traffic with OVS sampling flags" section.

Use the following procedure to view OVN-Kubernetes network traffic using the CLI.

.Prerequisites

* You are logged in to the cluster as a user with `cluster-admin` privileges.
* You have created a source pod and a destination pod and ran traffic between them.
* You have created at least one of the following network APIs: `NetworkPolicy`, `AdminNetworkPolicy`, `BaselineNetworkPolicy`, `UserDefinedNetwork` isolation, multicast, or egress firewalls.

.Procedure

. To enable the `OVNObservability` with OVS sampling feature, enable `TechPreviewNoUpgrade` feature set in the `FeatureGate` CR named `cluster` by entering the following command:
+
[source,terminal]
----
$ oc patch --type=merge --patch '{"spec": {"featureSet": "TechPreviewNoUpgrade"}}' featuregate/cluster
----
+
.Example output
[source,terminal]
----
featuregate.config.openshift.io/cluster patched
----

. Confirm that the `OVNObservability` feature is enabled by entering the following command:
+
[source,terminal]
----
$ oc get featuregate cluster -o yaml
----
+
.Example output
[source,yaml]
----
  featureGates:
# ...
    enabled:
    - name: OVNObservability
----

. Obtain a list of the pods inside of the namespace in which you have created one of the relevant network APIs by entering the following command. Note the `NODE` name of the pods, as they are used in the following step.
+
[source,terminal]
----
$ oc get pods -n <namespace> -o wide
----
+
.Example output
[source,terminal]
----
NAME              READY   STATUS    RESTARTS   AGE     IP            NODE                                       NOMINATED NODE   READINESS GATES
destination-pod   1/1     Running   0          53s     10.131.0.23   ci-ln-1gqp7b2-72292-bb9dv-worker-a-gtmpc   <none>           <none>
source-pod        1/1     Running   0          56s     10.131.0.22   ci-ln-1gqp7b2-72292-bb9dv-worker-a-gtmpc   <none>           <none>
----

. Obtain a list of OVN-Kubernetes pods and locate the pod that shares the same `NODE` as the pods from the previous step by entering the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ovn-kubernetes -o wide
----
+
.Example output
[source,terminal]
----
NAME
...                             READY   STATUS    RESTARTS      AGE   IP           NODE                                       NOMINATED NODE
ovnkube-node-jzn5b              8/8     Running   1 (34m ago)   37m   10.0.128.2   ci-ln-1gqp7b2-72292-bb9dv-worker-a-gtmpc   <none>
...
----

. Open a bash shell inside of the `ovnkube-node` pod by entering the following command:
+
[source,terminal]
----
$ oc exec -it <pod_name> -n openshift-ovn-kubernetes -- bash
----

. While inside of the `ovnkube-node` pod, you can run the `ovnkube-observ -add-ovs-collector` script to show network events using the OVS collector. For example:
+
[source,terminal]
----
# /usr/bin/ovnkube-observ -add-ovs-collector
----
+
.Example output
[source,terminal]
----
...
2024/12/02 19:41:41.327584 OVN-K message: Allowed by default allow from local node policy, direction ingress
2024/12/02 19:41:41.327593 src=10.131.0.2, dst=10.131.0.6

2024/12/02 19:41:41.327692 OVN-K message: Allowed by default allow from local node policy, direction ingress
2024/12/02 19:41:41.327715 src=10.131.0.6, dst=10.131.0.2
...
----

. You can filter the content by type, such as source pods, by entering the following command with the `-filter-src-ip` flag and your pod's IP address. For example:
+
[source,terminal]
----
# /usr/bin/ovnkube-observ -add-ovs-collector -filter-src-ip <pod_ip_address>
----
+
.Example output
[source,terminal]
----
...
Found group packets, id 14
2024/12/10 16:27:12.456473 OVN-K message: Allowed by admin network policy allow-egress-group1, direction Egress
2024/12/10 16:27:12.456570 src=10.131.0.22, dst=10.131.0.23

2024/12/10 16:27:14.484421 OVN-K message: Allowed by admin network policy allow-egress-group1, direction Egress
2024/12/10 16:27:14.484428 src=10.131.0.22, dst=10.131.0.23

2024/12/10 16:27:12.457222 OVN-K message: Allowed by network policy test:allow-ingress-from-specific-pod, direction Ingress
2024/12/10 16:27:12.457228 src=10.131.0.22, dst=10.131.0.23

2024/12/10 16:27:12.457288 OVN-K message: Allowed by network policy test:allow-ingress-from-specific-pod, direction Ingress
2024/12/10 16:27:12.457299 src=10.131.0.22, dst=10.131.0.23
...
----
+
For a full list of flags that can be passed in with `/usr/bin/ovnkube-observ`, see "OVN-Kubernetes network traffic with OVS sampling flags".

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/ovn-kubernetes-troubleshooting-sources.adoc

[id="observability-ovs-sampling-flags_{context}"]
= OVN-Kubernetes network traffic with OVS sampling flags

[role="_abstract"]
To filter OVN-Kubernetes traffic samples from `ovnkube-observ`, you can pass command line flags that limit output and collector options.

After you have opened a bash shell inside of the `ovnkube-node` pod, the following flags are available and can be appended using the following syntax:

.Command syntax
[source,terminal]
----
# /usr/bin/ovnkube-observ <flag>
----

[options="header",cols="1,3"]
|===
| Flag | Description

| `-h` | Returns a complete list flags that can be used with the `usr/bin/ovnkube-observ` command.
`
|`-add-ovs-collector` | Add OVS collector to enable sampling. Use with caution. Make sure no one else is using observability.

|`-enable-enrichment` | Enrich samples with NBDB data. Defaults to `true`.

|`-filter-dst-ip` | Filter only packets to a given destination IP.

|`-filter-src-ip` | Filters only packets from a given source IP.

|`-log-cookie` | Print raw sample cookie with psample group_id.

|`-output-file` | Output file to write the samples to.

|`-print-full-packet` | Print full received packet. When false, only source and destination IPs are printed with every sample.

|===

[role="_additional-resources"]
[id="additional-resources_ovn-kubernetes-sources-of-troubleshooting-information"]
== Additional resources

* Gathering data about your cluster for Red Hat Support
* Implementation of connection health checks
* Verifying network connectivity for an endpoint
