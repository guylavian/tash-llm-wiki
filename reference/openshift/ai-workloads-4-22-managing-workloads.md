---
title: "Managing jobs and workloads"
type: reference
domain: openshift
slug: ai-workloads-4-22-managing-workloads
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/managing-workloads
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Managing jobs and workloads

[id="managing-workloads"]
= Managing jobs and workloads

{kueue-name} does not directly manipulate jobs that are created by users. Instead, Kueue manages `Workload` objects that represent the resource requirements of a job. {kueue-name} automatically creates a workload for each job, and syncs any decisions and statuses between the two objects.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/install-kueue.adoc
// * ai_workloads/kueue/install-disconnected.adoc

[id="label-namespaces_{context}"]
= Labeling namespaces to allow {kueue-name} to manage jobs

The {kueue-name} Operator uses an opt-in webhook mechanism to ensure that policies are only enforced for the jobs and namespaces that it is expected to target.

You must label the namespaces where you want {kueue-name} to manage jobs with the `kueue.openshift.io/managed=true` label.

.Prerequisites

* You have cluster administrator permissions.
* The {kueue-name} Operator is installed on your cluster, and you have created a `Kueue` custom resource (CR).
* You have installed the {oc-first}.

.Procedure

* Add the `kueue.openshift.io/managed=true` label to a namespace by running the following command:
+
[source,terminal]
----
$ oc label namespace <namespace> kueue.openshift.io/managed=true
----

When you add this label, you instruct the {kueue-name} Operator that the namespace is managed by its webhook admission controllers. As a result, any {kueue-name} resources within that namespace are properly validated and mutated.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/managing-workloads.adoc

[id="configuring-labelpolicy_{context}"]
= Configuring label policies for jobs

The `spec.config.workloadManagement.labelPolicy` spec in the `Kueue` custom resource (CR) is an optional field that controls how {kueue-name} decides whether to manage or ignore different jobs. The allowed values are `QueueName`, `None` and empty (`""`).

If the `labelPolicy` setting is omitted or empty (`""`), the default policy is that {kueue-name} manages jobs that have a `kueue.x-k8s.io/queue-name` label, and ignores jobs that do not have the `kueue.x-k8s.io/queue-name` label. This is the same workflow as if the `labelPolicy` is set to `QueueName`.

If the `labelPolicy` setting is set to `None`, jobs are managed by {kueue-name} even if they do not have the `kueue.x-k8s.io/queue-name` label.

.Example `workloadManagement` spec configuration
[source,yaml]
----
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  labels:
    app.kubernetes.io/name: kueue-operator
    app.kubernetes.io/managed-by: kustomize
  name: cluster
  namespace: openshift-kueue-operator
spec:
  config:
    workloadManagement:
      labelPolicy: QueueName
# ...
----

.Example user-created `Job` object containing the `kueue.x-k8s.io/queue-name` label
[source,yaml]
----
apiVersion: batch/v1
kind: Job
metadata:
  generateName: sample-job-
  namespace: my-namespace
  labels:
    kueue.x-k8s.io/queue-name: user-queue
spec:
# ...
----
