---
title: "Gang scheduling"
type: reference
domain: openshift
slug: ai-workloads-4-22-gangscheduling
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/gangscheduling
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Gang scheduling

[id="gangscheduling"]
= Gang scheduling

Gang scheduling ensures that a group or _gang_ of related jobs only start when all required resources are available. {kueue-name} enables gang scheduling by suspending jobs until the OpenShift Container Platform cluster can guarantee the capacity to start and execute all of the related jobs in the gang together. This is also known as _all-or-nothing_ scheduling.

Gang scheduling is important if you are working with expensive, limited resources, such as GPUs. Gang scheduling can prevent jobs from claiming but not using GPUs, which can improve GPU utilization and can reduce running costs. Gang scheduling can also help to prevent issues like resource segmentation and deadlocking.

// Module included in the following assemblies:
//
// * ai_workloads/kueue/gangscheduling.adoc

[id="configuring-gangscheduling_{context}"]
= Configuring gang scheduling

As a cluster administrator, you can configure gang scheduling by modifying the `gangScheduling` spec in the `Kueue` custom resource (CR).

.Example `Kueue` CR with gang scheduling configured
[source,yaml]
----
apiVersion: kueue.openshift.io/v1
kind: Kueue
metadata:
  name: cluster
  labels:
    app.kubernetes.io/managed-by: kustomize
    app.kubernetes.io/name: kueue-operator
  namespace: openshift-kueue-operator
spec:
  config:
    gangScheduling:
      policy: ByWorkload # <1>
      byWorkload:
        admission: Parallel # <2>
# ...
----
<1> You can set the `policy` value to enable or disable gang scheduling. The possible values are `ByWorkload`, `None`, or empty (`""`).
+
`ByWorkload`:: When the `policy` value is set to `ByWorkload`, each job is processed and considered for admission as a single unit. If the job does not become ready within the specified time, the entire job is evicted and retried at a later time.
+
`None`:: When the `policy` value is set to `None`, gang scheduling is disabled.
+
Empty (`""`):: When the `policy` value is empty or set to `""`, the {kueue-name} Operator determines settings for gang scheduling. Currently, gang scheduling is disabled by default.
<2> If the `policy` value is set to `ByWorkload`, you must configure job admission settings. The possible values for the `admission` spec are `Parallel`, `Sequential`, or empty (`""`).
+
`Parallel`:: When the `admission` value is set to `Parallel`, pods from any job can be admitted at any time. This can cause a deadlock, where jobs are in contention for cluster capacity. When a deadlock occurs, the successful scheduling of pods from another job can prevent the scheduling of pods from the current job.
+
`Sequential`:: When the `admission` value is set to `Sequential`, only pods from the currently processing job are admitted. After all of the pods from the current job have been admitted and are ready, {kueue-name} processes the next job. Sequential processing can slow down admission when the cluster has sufficient capacity for multiple jobs, but provides a higher likelihood that all of the pods for a job are scheduled together successfully.
+
Empty (`""`):: When the `admission` value is empty or set to `""`, the {kueue-name} Operator determines job admission settings. Currently, the `admission` value is set to `Parallel` by default.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Creating a Kueue custom resource

// use case - deep learning
One classic example is in deep learning workloads. Deep learning frameworks (Tensorflow, PyTorch etc) require all the workers to be running during the training process.

In this scenario, when you deploy training workloads, all the components should be scheduled and deployed to ensure the training works as expected.

Gang Scheduling is a critical feature for Deep Learning workloads to enable all-or-nothing scheduling capability, as most DL frameworks requires all workers to be running to start training process. Gang Scheduling avoids resource inefficiency and scheduling deadlock sometimes.
