---
title: "Running {gitops-shortname} control plane workloads on infrastructure nodes"
type: reference
domain: openshift
slug: cicd-4-22-run-gitops-control-plane-workload-on-infra-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/run-gitops-control-plane-workload-on-infra-nodes
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Running {gitops-shortname} control plane workloads on infrastructure nodes

[id="run-gitops-control-plane-workload-on-infra-nodes"]
= Running {gitops-shortname} control plane workloads on infrastructure nodes

You can use infrastructure nodes to prevent additional billing cost against subscription counts.

You can use the OpenShift Container Platform to run certain workloads on infrastructure nodes installed by the {gitops-title} Operator. This comprises the workloads that are installed by the {gitops-title} Operator by default in the `openshift-gitops` namespace, including the default Argo CD instance in that namespace.

[NOTE]
====
Any other Argo CD instances installed to user namespaces are not eligible to run on infrastructure nodes.
====

// Module included in the following assembly:
//
// * gitops/run-gitops-control-plane-workload-on-infra-node.adoc

[id="add-infra-nodes_{context}"]
= Moving {gitops-shortname} workloads to infrastructure nodes

You can move the default workloads installed by the {gitops-title} to the infrastructure nodes. The workloads that can be moved are:

* `kam deployment`
* `cluster deployment` (backend service)
* `openshift-gitops-applicationset-controller deployment`
* `openshift-gitops-dex-server deployment`
* `openshift-gitops-redis deployment`
* `openshift-gitops-redis-ha-haproxy deployment`
* `openshift-gitops-repo-sever deployment`
* `openshift-gitops-server deployment`
* `openshift-gitops-application-controller statefulset`
* `openshift-gitops-redis-server statefulset`

.Procedure

. Label existing nodes as infrastructure by running the following command:
+
[source,terminal]
----
$ oc label node <node-name> node-role.kubernetes.io/infra=
----
. Edit the `GitOpsService` custom resource (CR) to add the infrastructure node selector:
+
[source,terminal]
----
$ oc edit gitopsservice -n openshift-gitops
----
. In the `GitOpsService` CR file, add `runOnInfra` field to the `spec` section and set it to `true`. This field moves the workloads in `openshift-gitops` namespace to the infrastructure nodes:
+
[source,yaml]
----
apiVersion: pipelines.openshift.io/v1alpha1
kind: GitopsService
metadata:
  name: cluster
spec:
  runOnInfra: true
----
. Optional: Apply taints and isolate the workloads on infrastructure nodes and prevent other workloads from scheduling on these nodes.
+
[source,terminal]
----
$ oc adm taint nodes -l node-role.kubernetes.io/infra
infra=reserved:NoSchedule infra=reserved:NoExecute
----
+
. Optional: If you apply taints to the nodes, you can add tolerations in the `GitOpsService` CR:
+
[source,yaml]
----
spec:
  runOnInfra: true
  tolerations:
  - effect: NoSchedule
    key: infra
    value: reserved
  - effect: NoExecute
    key: infra
    value: reserved
----

To verify that the workloads are scheduled on infrastructure nodes in the {gitops-title} namespace, click any of the pod names and ensure that the *Node selector* and *Tolerations* have been added.

[NOTE]
====
Any manually added *Node selectors* and *Tolerations* in the default Argo CD CR will be overwritten by the toggle and the tolerations in the `GitOpsService` CR.
====

[role="_additional-resources"]
[id="additional-resources_run-gitops-control-plane-workload-on-infra-nodes"]
== Additional resources
* To learn more about taints and tolerations, see Controlling pod placement using node taints.
* For more information on infrastructure machine sets, see Creating infrastructure machine sets.
