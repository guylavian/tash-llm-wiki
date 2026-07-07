---
title: "Running jobs with quota limits"
type: reference
domain: openshift
slug: ai-workloads-4-22-running-kueue-jobs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/running-kueue-jobs
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Running jobs with quota limits

[id="running-kueue-jobs"]
= Running jobs with quota limits

You can run Kubernetes jobs with {kueue-name} enabled to manage resource allocation within defined quota limits. This can help to ensure predictable resource availability, cluster stability, and optimized performance.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/running-kueue-jobs.adoc

[id="identifying-local-queues_{context}"]
= Identifying available local queues

Before you can submit a job to a queue, you must find the name of the local queue.

.Prerequisites

.Procedure

* Run the following command to list available local queues in your namespace:
+
[source,terminal]
----
$ oc -n <namespace> get localqueues
----
+
.Example output
[source,terminal]
----
NAME         CLUSTERQUEUE    PENDING WORKLOADS
user-queue   cluster-queue   3
----

// Module included in the following assemblies:
//
// * ai_workloads/kueue/running-kueue-jobs.adoc

[id="defining-running-jobs_{context}"]
= Defining a job to run with {kueue-name}

When you are defining a job to run with {kueue-name}, ensure that it meets the following criteria:

* Specify the local queue to submit the job to, by using the `kueue.x-k8s.io/queue-name` label.
* Include the resource requests for each job pod.

{kueue-name} suspends the job, and then starts it when resources are available. {kueue-name} creates a corresponding workload, represented as a `Workload` object with a name that matches the job.

.Prerequisites

* You have identified the name of the local queue that you want to submit jobs to.

.Procedure

. Create a `Job` object.
+
.Example job
[source,yaml]
----
apiVersion: batch/v1
kind: Job # <1>
metadata:
  generateName: sample-job- # <2>
  namespace: my-namespace
  labels:
    kueue.x-k8s.io/queue-name: user-queue # <3>
spec:
  parallelism: 3
  completions: 3
  template:
    spec:
      containers:
      - name: dummy-job
        image: registry.k8s.io/e2e-test-images/agnhost:2.53
        args: ["entrypoint-tester", "hello", "world"]
        resources: # <4>
          requests:
            cpu: 1
            memory: "200Mi"
      restartPolicy: Never
----
<1> Defines the resource type as a `Job` object, which represents a batch computation task.
<2> Provides a prefix for generating a unique name for the job.
<3> Identifies the queue to send the job to.
<4> Defines the resource requests for each pod.

. Run the job by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

.Verification

* Verify that pods are running for the job you have created, by running the following command and observing the output:
+
[source,terminal]
----
$ oc get job <job-name>
----
+
.Example output
[source,terminal]
----
NAME               STATUS      COMPLETIONS   DURATION   AGE
sample-job-sk42x   Suspended   0/1                      2m12s
----

* Verify that a workload has been created in your namespace for the job, by running the following command and observing the output:
+
[source,terminal]
----
$ oc -n <namespace> get workloads
----
+
.Example output
[source,terminal]
----
NAME                         QUEUE          RESERVED IN   ADMITTED   FINISHED   AGE
job-sample-job-sk42x-77c03   user-queue                                         3m8s
----
