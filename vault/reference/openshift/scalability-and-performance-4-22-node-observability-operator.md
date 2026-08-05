---
title: "Using the Node Observability Operator"
type: reference
domain: openshift
slug: scalability-and-performance-4-22-node-observability-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/node-observability-operator
version: 4.22
family: scalability_and_performance
documentKind: "Documentation"
---

# Using the Node Observability Operator

[id="using-node-observability-operator"]
= Using the Node Observability Operator

The Node Observability Operator collects and stores CRI-O and Kubelet profiling or metrics from scripts of compute nodes.

With the Node Observability Operator, you can query the profiling data, enabling analysis of performance trends in CRI-O and Kubelet. It supports debugging performance-related issues and executing embedded scripts for network metrics by using the `run` field in the custom resource definition. To enable CRI-O and Kubelet profiling or scripting, you can configure the `type` field in the custom resource definition.

// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

[id="workflow-node-observability-operator_{context}"]
= Workflow of the Node Observability Operator

[role="_abstract"]
The following workflow outlines on how to query the profiling data using the Node Observability Operator:

. Install the Node Observability Operator in the OpenShift Container Platform cluster.
. Create a NodeObservability custom resource to enable the CRI-O profiling on the worker nodes of your choice.
. Run the profiling query to generate the profiling data.

// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

[id="install-node-observability-operator_{context}"]
= Installing the Node Observability Operator

[role="_abstract"]
The Node Observability Operator is not installed in OpenShift Container Platform by default. You can install the Node Observability Operator by using the OpenShift Container Platform CLI or the web console.

// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

[id="install-node-observability-using-cli_{context}"]
= Installing the Node Observability Operator using the CLI

[role="_abstract"]
You can install the Node Observability Operator by using the OpenShift CLI (oc).

.Prerequisites

* You have installed the OpenShift CLI (oc).
* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Confirm that the Node Observability Operator is available by running the following command:
+
[source,terminal]
----
$ oc get packagemanifests -n openshift-marketplace node-observability-operator
----

+
.Example output
[source,terminal]
----
NAME                            CATALOG                AGE
node-observability-operator     Red Hat Operators      9h
----

. Create the `node-observability-operator` namespace by running the following command:
+
[source,terminal]
----
$ oc new-project node-observability-operator
----

. Create an `OperatorGroup` object YAML file:
+
[source,yaml]
----
cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: node-observability-operator
  namespace: node-observability-operator
spec:
  targetNamespaces: []
EOF
----

. Create a `Subscription` object YAML file to subscribe a namespace to an Operator:
+
[source,yaml]
----
cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: node-observability-operator
  namespace: node-observability-operator
spec:
  channel: alpha
  name: node-observability-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
----

.Verification

. View the install plan name by running the following command:
+
[source,terminal]
----
$ oc -n node-observability-operator get sub node-observability-operator -o yaml | yq '.status.installplan.name'
----

+
.Example output
[source,terminal]
----
install-dt54w
----

. Verify the install plan status by running the following command:
+
[source,terminal]
----
$ oc -n node-observability-operator get ip <install_plan_name> -o yaml | yq '.status.phase'
----
+
`<install_plan_name>` is the install plan name that you obtained from the output of the previous command.

+
.Example output
[source,terminal]
----
COMPLETE
----

. Verify that the Node Observability Operator is up and running:
+
[source,terminal]
----
$ oc get deploy -n node-observability-operator
----

+
.Example output
[source,terminal]
----
NAME                                            READY   UP-TO-DATE  AVAILABLE   AGE
node-observability-operator-controller-manager  1/1     1           1           40h
----

// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

[id="install-node-observability-using-web-console_{context}"]
= Installing the Node Observability Operator using the web console

[role="_abstract"]
You can install the Node Observability Operator from the OpenShift Container Platform web console.

.Prerequisites

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.
. In the Administrator's navigation panel, select *Ecosystem* -> *Software Catalog*.
. In the *All items* field, enter *Node Observability Operator* and select the *Node Observability Operator* tile.
. Click *Install*.
. On the *Install Operator* page, configure the following settings:
.. In the *Update channel* area, click *alpha*.
.. In the *Installation mode* area, click *A specific namespace on the cluster*.
.. From the *Installed Namespace* list, select *node-observability-operator* from the list.
.. In the *Update approval* area, select *Automatic*.
.. Click *Install*.

.Verification
. In the Administrator's navigation panel, expand *Ecosystem* -> *Installed Operators*.
. Verify that the Node Observability Operator is listed in the Operators list.

// Module included in the following assemblies:
//
// * scalability_and_performance/node-observability-operator.adoc

[id="requesting-crio-kubelet-profiling-using-noo_{context}"]
= Requesting CRI-O and Kubelet profiling data using the Node Observability Operator

[role="_abstract"]
Creating a Node Observability custom resource to collect CRI-O and Kubelet profiling data.

// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

[id="creating-node-observability-custom-resource_{context}"]
= Creating the Node Observability custom resource

[role="_abstract"]
You must create and run the `NodeObservability` custom resource (CR) before you run the profiling query. When you run the `NodeObservability` CR, it creates the necessary machine config and machine config pool CRs to enable the CRI-O profiling on the worker nodes matching the `nodeSelector`.

[IMPORTANT]
====
If CRI-O profiling is not enabled on the worker nodes, the `NodeObservabilityMachineConfig` resource gets created. Worker nodes matching the `nodeSelector` specified in `NodeObservability` CR restarts. This might take 10 or more minutes to complete.
====

[NOTE]
====
Kubelet profiling is enabled by default.
====

The CRI-O unix socket of the node is mounted on the agent pod, which allows the agent to communicate with CRI-O to run the pprof request. Similarly, the `kubelet-serving-ca` certificate chain is mounted on the agent pod, which allows secure communication between the agent and node's kubelet endpoint.

.Prerequisites
* You have installed the Node Observability Operator.
* You have installed the OpenShift CLI (oc).
* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Log in to the OpenShift Container Platform CLI by running the following command:
+
[source,terminal]
----
$ oc login -u kubeadmin https://<HOSTNAME>:6443
----

. Switch back to the `node-observability-operator` namespace by running the following command:
+
[source,terminal]
----
$ oc project node-observability-operator
----

. Create a CR file named `nodeobservability.yaml` that contains the following text:
+
[source,yaml]
----
    apiVersion: nodeobservability.olm.openshift.io/v1alpha2
    kind: NodeObservability
    metadata:
      name: cluster
    spec:
      nodeSelector:
        kubernetes.io/hostname: <node_hostname>
      type: crio-kubelet
----
+
where:
+
`cluster`:: You must specify the name as `cluster` because there should be only one `NodeObservability` CR per cluster.
`<node_hostname>`:: Specify the nodes on which the Node Observability agent must be deployed.

. Run the `NodeObservability` CR:
+
[source,terminal]
----
oc apply -f nodeobservability.yaml
----

+
.Example output
[source,terminal]
----
nodeobservability.olm.openshift.io/cluster created
----

. Review the status of the `NodeObservability` CR by running the following command:
+
[source,terminal]
----
$ oc get nob/cluster -o yaml | yq '.status.conditions'
----

+
.Example output
[source,terminal]
----
conditions:
  conditions:
  - lastTransitionTime: "2022-07-05T07:33:54Z"
    message: 'DaemonSet node-observability-ds ready: true NodeObservabilityMachineConfig
      ready: true'
    reason: Ready
    status: "True"
    type: Ready
----

+
`NodeObservability` CR run is completed when the reason is `Ready` and the status is `True`.

// Module included in the following assemblies:
//
// * scalability_and_performance/understanding-node-observability-operator.adoc

[id="running-profiling-query_{context}"]
= Running the profiling query

[role="_abstract"]
To run the profiling query, you must create a `NodeObservabilityRun` resource. The profiling query is a blocking operation that fetches CRI-O and Kubelet profiling data for a duration of 30 seconds. After the profiling query is complete, you must retrieve the profiling data inside the container file system `/run/node-observability` directory. The lifetime of data is bound to the agent pod through the `emptyDir` volume, so you can access the profiling data while the agent pod is in the `running` status.

[IMPORTANT]
====
You can request only one profiling query at any point of time.
====

.Prerequisites
* You have installed the Node Observability Operator.
* You have created the `NodeObservability` custom resource (CR).
* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create a `NodeObservabilityRun` resource file named `nodeobservabilityrun.yaml` that contains the following text:
+
[source,yaml]
----
apiVersion: nodeobservability.olm.openshift.io/v1alpha2
kind: NodeObservabilityRun
metadata:
  name: nodeobservabilityrun
spec:
  nodeObservabilityRef:
    name: cluster
----

. Trigger the profiling query by running the `NodeObservabilityRun` resource:
+
[source,terminal]
----
$ oc apply -f nodeobservabilityrun.yaml
----

. Review the status of the `NodeObservabilityRun` by running the following command:
+
[source,terminal]
----
$ oc get nodeobservabilityrun nodeobservabilityrun -o yaml  | yq '.status.conditions'
----

+
.Example output
[source,terminal]
----
conditions:
- lastTransitionTime: "2022-07-07T14:57:34Z"
  message: Ready to start profiling
  reason: Ready
  status: "True"
  type: Ready
- lastTransitionTime: "2022-07-07T14:58:10Z"
  message: Profiling query done
  reason: Finished
  status: "True"
  type: Finished
----

+
The profiling query is complete once the status is `True` and type is `Finished`.

. Retrieve the profiling data from the container's `/run/node-observability` path by running the following bash script:
+
[source,bash]
----
for a in $(oc get nodeobservabilityrun nodeobservabilityrun -o yaml | yq .status.agents[].name); do
  echo "agent ${a}"
  mkdir -p "/tmp/${a}"
  for p in $(oc exec "${a}" -c node-observability-agent -- bash -c "ls /run/node-observability/*.pprof"); do
    f="$(basename ${p})"
    echo "copying ${f} to /tmp/${a}/${f}"
    oc exec "${a}" -c node-observability-agent -- cat "${p}" > "/tmp/${a}/${f}"
  done
done
----

// Module included in the following assemblies:
//
// * scalability_and_performance/node-observability-operator.adoc

[id="node-observability-operator-scripting_{context}"]
= Node Observability Operator scripting

[role="_abstract"]
Scripting allows you to run pre-configured bash scripts, using the current Node Observability Operator and Node Observability Agent.

These scripts monitor key metrics like CPU load, memory pressure, and worker node issues. They also collect sar reports and custom performance metrics.

// Module included in the following assemblies:
//
// * scalability_and_performance/node-observability-operator.adoc

[id="node-observability-scripting-cr_{context}"]
= Creating the Node Observability custom resource for scripting

[role="_abstract"]
You must create and run the `NodeObservability` custom resource (CR) before you run the scripting. When you run the `NodeObservability` CR, it enables the agent in scripting mode on the compute nodes matching the `nodeSelector` label.

.Prerequisites
* You have installed the Node Observability Operator.
* You have installed the {oc-first}.
* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Log in to the OpenShift Container Platform cluster by running the following command:
+
[source,terminal]
----
$ oc login -u kubeadmin https://<host_name>:6443
----

. Switch to the `node-observability-operator` namespace by running the following command:
+
[source,terminal]
----
$ oc project node-observability-operator
----

. Create a file named `nodeobservability.yaml` that contains the following content:
+
[source,yaml]
----
    apiVersion: nodeobservability.olm.openshift.io/v1alpha2
    kind: NodeObservability
    metadata:
      name: cluster
    spec:
      nodeSelector:
        kubernetes.io/hostname: <node_hostname>
      type: scripting
----
+
where:
+
`cluster`:: You must specify the name as `cluster` because there should be only one `NodeObservability` CR per cluster.
`<node_hostname>`:: Specify the nodes on which the Node Observability agent must be deployed.
`scripting`:: To deploy the agent in scripting mode, you must set the type to `scripting`.

. Create the `NodeObservability` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f nodeobservability.yaml
----

+
.Example output
[source,terminal]
----
nodeobservability.olm.openshift.io/cluster created
----

. Review the status of the `NodeObservability` CR by running the following command:
+
[source,terminal]
----
$ oc get nob/cluster -o yaml | yq '.status.conditions'
----

+
.Example output
[source,terminal]
----
conditions:
  conditions:
  - lastTransitionTime: "2022-07-05T07:33:54Z"
    message: 'DaemonSet node-observability-ds ready: true NodeObservabilityScripting
      ready: true'
    reason: Ready
    status: "True"
    type: Ready
----

+
The `NodeObservability` CR run is completed when the `reason` is `Ready` and `status` is `"True"`.

// Module included in the following assemblies:
//
// * scalability_and_performance/node-observability-operator.adoc

[id="node-observability-scripting_{context}"]
= Configuring Node Observability Operator scripting

[role="_abstract"]
You can configure the Node Observability Operator to run pre-configured scripts for collecting metrics data from compute nodes.

.Prerequisites

* You have installed the Node Observability Operator.
* You have created the `NodeObservability` custom resource (CR).
* You have access to the cluster with `cluster-admin` privileges.

.Procedure

. Create a file named `nodeobservabilityrun-script.yaml` that contains the following content:
+
[source,yaml]
----
apiVersion: nodeobservability.olm.openshift.io/v1alpha2
kind: NodeObservabilityRun
metadata:
  name: nodeobservabilityrun-script
  namespace: node-observability-operator
spec:
  nodeObservabilityRef:
    name: cluster
    type: scripting
----
+
[IMPORTANT]
====
You can request only the following scripts:

* `metrics.sh`
* `network-metrics.sh` (uses `monitor.sh`)
====

. Trigger the scripting by creating the `NodeObservabilityRun` resource with the following command:
+
[source,terminal]
----
$ oc apply -f nodeobservabilityrun-script.yaml
----

. Review the status of the `NodeObservabilityRun` scripting by running the following command:
+
[source,terminal]
----
$ oc get nodeobservabilityrun nodeobservabilityrun-script -o yaml  | yq '.status.conditions'
----

+
.Example output
[source,terminal]
----
Status:
  Agents:
    Ip:    10.128.2.252
    Name:  node-observability-agent-n2fpm
    Port:  8443
    Ip:    10.131.0.186
    Name:  node-observability-agent-wcc8p
    Port:  8443
  Conditions:
    Conditions:
      Last Transition Time:  2023-12-19T15:10:51Z
      Message:               Ready to start profiling
      Reason:                Ready
      Status:                True
      Type:                  Ready
      Last Transition Time:  2023-12-19T15:11:01Z
      Message:               Profiling query done
      Reason:                Finished
      Status:                True
      Type:                  Finished
  Finished Timestamp:        2023-12-19T15:11:01Z
  Start Timestamp:           2023-12-19T15:10:51Z
----

+
The scripting is complete once `Status` is `True` and `Type` is `Finished`.

. Retrieve the scripting data from the root path of the container by running the following bash script:
+
[source,bash]
----
#!/bin/bash

RUN=$(oc get nodeobservabilityrun --no-headers | awk '{print $1}')

for a in $(oc get nodeobservabilityruns.nodeobservability.olm.openshift.io/${RUN} -o json | jq .status.agents[].name); do
  echo "agent ${a}"
  agent=$(echo ${a} | tr -d "\"\'\`")
  base_dir=$(oc exec "${agent}" -c node-observability-agent -- bash -c "ls -t | grep node-observability-agent" | head -1)
  echo "${base_dir}"
  mkdir -p "/tmp/${agent}"
  for p in $(oc exec "${agent}" -c node-observability-agent -- bash -c "ls ${base_dir}"); do
    f="/${base_dir}/${p}"
    echo "copying ${f} to /tmp/${agent}/${p}"
    oc exec "${agent}" -c node-observability-agent -- cat ${f} > "/tmp/${agent}/${p}"
  done
done
----

[role="_additional-resources"]
[id="additional-resources_node-observability-operator"]
== Additional resources

* Collecting worker metrics using the Node Observability Operator
