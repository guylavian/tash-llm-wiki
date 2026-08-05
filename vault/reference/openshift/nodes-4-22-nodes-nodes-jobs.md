---
title: "Running tasks in pods using jobs"
type: reference
domain: openshift
slug: nodes-4-22-nodes-nodes-jobs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-nodes-jobs
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Running tasks in pods using jobs

[id="nodes-nodes-jobs"]
= Running tasks in pods using jobs

A _job_ executes a task in your OpenShift Container Platform cluster.

A job tracks the overall progress of a task and updates its status with information
about active, succeeded, and failed pods. Deleting a job will clean up any pod
replicas it created. Jobs are part of the Kubernetes API, which can be managed
with `oc` commands like other object types.

.Sample Job specification

[source,yaml]
----
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  parallelism: 1    <1>
  completions: 1    <2>
  activeDeadlineSeconds: 1800 <3>
  backoffLimit: 6   <4>
  ttlSecondsAfterFinished: 100 <5>
  template:         <6>
    metadata:
      name: pi
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: OnFailure    <7>
#...
----
<1> The pod replicas a job should run in parallel.
<2> Successful pod completions are needed to mark a job completed.
<3> The maximum duration the job can run.
<4> The number of retries for a job.
<5> The period of time in seconds after which the job should be automatically deleted upon completion.
<6> The template for the pod the controller creates.
<7> The restart policy of the pod.

.Additional resources

* Jobs (Kubernetes documentation)

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-jobs.adoc

[id="nodes-nodes-jobs-about_{context}"]
= Understanding jobs and cron jobs

A job tracks the overall progress of a task and updates its status with information
about active, succeeded, and failed pods. Deleting a job cleans up any pods it created.
Jobs are part of the Kubernetes API, which can be managed
with `oc` commands like other object types.

There are two possible resource types that allow creating run-once objects in OpenShift Container Platform:

Job::
A regular job is a run-once object that creates a task and ensures the job finishes.
+
There are three main types of task suitable to run as a job:
+
* Non-parallel jobs:
** A job that starts only one pod, unless the pod fails.
** The job is complete as soon as its pod terminates successfully.
+
* Parallel jobs with a fixed completion count:
** a job that starts multiple pods.
** The job represents the overall task and is complete when there is one successful pod for each value in the range `1` to the `completions` value.
+
* Parallel jobs with a work queue:
** A job with multiple parallel worker processes in a given pod.
** OpenShift Container Platform coordinates pods to determine what each should work on or use an external queue service.
** Each pod is independently capable of determining whether or not all peer pods are complete and that the entire job is done.
** When any pod from the job terminates with success, no new pods are created.
** When at least one pod has terminated with success and all pods are terminated, the job is successfully completed.
** When any pod has exited with success, no other pod should be doing any work for this task or writing any output. Pods should all be in the process of exiting.
+
For more information about how to make use of the different types of job, see Job Patterns in the Kubernetes documentation.

Cron job::

A job can be scheduled to run multiple times, using a cron job.
+
A _cron job_ builds on a regular job by allowing you to specify
how the job should be run. Cron jobs are part of the
Kubernetes API, which
can be managed with `oc` commands like other object types.
+
Cron jobs are useful for creating periodic and recurring tasks, like running backups or sending emails.
Cron jobs can also schedule individual tasks for a specific time, such as if you want to schedule a job for a low activity period. A cron job creates a `Job` object based on the timezone configured on the control plane node that runs the cronjob controller.
+
[WARNING]
====
A cron job creates a `Job` object approximately once per execution time of its
schedule, but there are circumstances in which it fails to create a job or
two jobs might be created. Therefore, jobs must be idempotent and you must
configure history limits.
====

[id="jobs-create_{context}"]
== Understanding how to create jobs

Both resource types require a job configuration that consists of the following key parts:

- A pod template, which describes the pod that OpenShift Container Platform creates.
- The `parallelism` parameter, which specifies how many pods running in parallel at any point in time should execute a job.
** For non-parallel jobs, leave unset. When unset, defaults to `1`.
- The `completions` parameter, specifying how many successful pod completions are needed to finish a job.
** For non-parallel jobs, leave unset. When unset, defaults to `1`.
** For parallel jobs with a fixed completion count, specify a value.
** For parallel jobs with a work queue, leave unset. When unset defaults to the `parallelism` value.

[id="jobs-set-max_{context}"]
== Understanding how to set a maximum duration for jobs

When defining a job, you can define its maximum duration by setting
the `activeDeadlineSeconds` field. It is specified in seconds and is not
set by default. When not set, there is no maximum duration enforced.

The maximum duration is counted from the time when a first pod gets scheduled in
the system, and defines how long a job can be active. It tracks overall time of
an execution. After reaching the specified timeout, the job is terminated by OpenShift Container Platform.

[id="jobs-set-backoff_{context}"]
== Understanding how to set a job back off policy for pod failure

A job can be considered failed, after a set amount of retries due to a
logical error in configuration or other similar reasons. Failed pods associated with the job are recreated by the controller with
an exponential back off delay (`10s`, `20s`, `40s` …) capped at six minutes. The
limit is reset if no new failed pods appear between controller checks.

Use the `spec.backoffLimit` parameter to set the number of retries for a job.

[id="jobs-artifacts_{context}"]
== Understanding how to configure a cron job to remove artifacts

Cron jobs can leave behind artifact resources such as jobs or pods.  As a user it is important
to configure history limits so that old jobs and their pods are properly cleaned.  There are two fields within cron job's spec responsible for that:

* `.spec.successfulJobsHistoryLimit`. The number of successful finished jobs to retain (defaults to 3).

* `.spec.failedJobsHistoryLimit`. The number of failed finished jobs to retain (defaults to 1).

[TIP]
====
* Delete cron jobs that you no longer need:
+
[source,terminal]
----
$ oc delete cronjob/<cron_job_name>
----
+
Doing this prevents them from generating unnecessary artifacts.

* You can suspend further executions by setting the `spec.suspend` to true.  All subsequent executions are suspended until you reset to `false`.
====

[id="jobs-ttl_{context}"]
== Understanding how to automatically remove completed jobs

You can specify that OpenShift Container Platform should delete jobs when they are finished, either `Complete` or `Failed`, in order to limit the number of objects in your cluster.

By default, for jobs that are not associated with a cron job or other controlling object, OpenShift Container Platform does not delete the job or its related pods when the job is finished. If you keep these artifacts in your cluster, you can view the status of finished jobs or view job logs for errors, warnings, or other diagnostic output.

However, having too many of these objects in the cluster can lead to etcd issues, latency issues, performance degradation, and other problems.

You can configure a time-to-live (TTL) duration for jobs without a controlling object by setting the `ttlSecondsAfterFinished` parameter in the job spec. When set, OpenShift Container Platform deletes the jobs and any related pods immediately after the job is finished or after a specified period of time in seconds.

[id="jobs-limits_{context}"]
== Known limitations

The job specification restart policy only applies to the _pods_, and not the _job controller_. However, the job controller is hard-coded to keep retrying jobs to completion.

As such, `restartPolicy: Never` or `--restart=Never` results in the same behavior as `restartPolicy: OnFailure` or `--restart=OnFailure`. That is, when a job fails it is restarted automatically until it succeeds (or is manually discarded). The policy only sets which subsystem performs the restart.

With the `Never` policy, the _job controller_ performs the restart. With each attempt, the job controller increments the number of failures in the job status and create new pods. This means that with each failed attempt, the number of pods increases.

With the `OnFailure` policy, _kubelet_ performs the restart. Each attempt does not increment the number of failures in the job status. In addition, kubelet will retry failed jobs starting pods on the same nodes.

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-jobs.adoc

[id="nodes-nodes-jobs-creating_{context}"]
= Creating jobs

You create a job in OpenShift Container Platform by creating a job object.

.Procedure

To create a job:

. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  parallelism: 1    <1>
  completions: 1    <2>
  activeDeadlineSeconds: 1800 <3>
  backoffLimit: 6   <4>
  ttlSecondsAfterFinished: 100 <5>
  template:         <6>
    metadata:
      name: pi
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: OnFailure    <7>
#...
----
<1> Optional: Specify how many pod replicas a job should run in parallel; defaults to `1`.
* For non-parallel jobs, leave unset. When unset, defaults to `1`.
<2> Optional: Specify how many successful pod completions are needed to mark a job completed.
* For non-parallel jobs, leave unset. When unset, defaults to `1`.
* For parallel jobs with a fixed completion count, specify the number of completions.
* For parallel jobs with a work queue, leave unset. When unset defaults to the `parallelism` value.
<3> Optional: Specify the maximum duration the job can run.
<4> Optional: Specify the number of retries for a job. This field defaults to six.
<5> Optional: Specify the period of time in seconds after which the job should be automatically deleted upon completion. If set to '0', the job is immediately deleted after completion. If this field is not included, the job is not automatically deleted.
<6> Specify the template for the pod the controller creates.
<7> Specify the restart policy of the pod:
* `Never`. Do not restart the job.
* `OnFailure`. Restart the job only if it fails.
* `Always`. Always restart the job.
+
For details on how OpenShift Container Platform uses restart policy with failed containers, see
the Example States in the Kubernetes documentation.

. Create the job:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

[NOTE]
====
You can also create and launch a job from a single command using `oc create job`. The following command creates and launches a job similar to the one specified in the previous example:

[source,terminal]
----
$ oc create job pi --image=perl -- perl -Mbignum=bpi -wle 'print bpi(2000)'
----
====

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-jobs.adoc

[id="nodes-nodes-jobs-creating-cron_{context}"]
= Creating cron jobs

You create a cron job in OpenShift Container Platform by creating a job object.

.Procedure

To create a cron job:

. Create a YAML file similar to the following:
+
[source,yaml]
----
apiVersion: batch/v1
kind: CronJob
metadata:
  name: pi
spec:
  schedule: "*/1 * * * *"          <1>
  timeZone: Etc/UTC                <2>
  concurrencyPolicy: "Replace"     <3>
  startingDeadlineSeconds: 200     <4>
  suspend: true                    <5>
  successfulJobsHistoryLimit: 3    <6>
  failedJobsHistoryLimit: 1        <7>
  jobTemplate:                     <8>
    spec:
      template:
        metadata:
          labels:                  <9>
            parent: "cronjobpi"
        spec:
          containers:
          - name: pi
            image: perl
            command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
          restartPolicy: OnFailure <10>
#...
----
+
<1> Schedule for the job specified in cron format. In this example, the job will run every minute.
<2> An optional time zone for the schedule. See List of tz database time zones for valid options. If not specified, the Kubernetes controller manager interprets the schedule relative to its local time zone.
<3> An optional concurrency policy, specifying how to treat concurrent jobs within a cron job. Only one of the following concurrent policies may be specified. If not specified, this defaults to allowing concurrent executions.
* `Allow` allows cron jobs to run concurrently.
* `Forbid` forbids concurrent runs, skipping the next run if the previous has not
finished yet.
* `Replace` cancels the currently running job and replaces
it with a new one.
<4> An optional deadline (in seconds) for starting the job if it misses its
scheduled time for any reason. Missed jobs executions will be counted as failed
ones. If not specified, there is no deadline.
<5> An optional flag allowing the suspension of a cron job. If set to `true`,
all subsequent executions will be suspended.
<6> The number of successful finished jobs to retain (defaults to 3).
<7> The number of failed finished jobs to retain (defaults to 1).
<8> Job template. This is similar to the job example.
<9> Sets a label for jobs spawned by this cron job.
<10> The restart policy of the pod. This does not apply to the job controller.
[source,yaml]
----
apiVersion: batch/v1
kind: CronJob
metadata:
  name: pi
spec:
  schedule: "*/1 * * * *"          <1>
  concurrencyPolicy: "Replace"     <2>
  startingDeadlineSeconds: 200     <3>
  suspend: true                    <4>
  successfulJobsHistoryLimit: 3    <5>
  failedJobsHistoryLimit: 1        <6>
  jobTemplate:                     <7>
    spec:
      template:
        metadata:
          labels:                  <8>
            parent: "cronjobpi"
        spec:
          containers:
          - name: pi
            image: perl
            command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
          restartPolicy: OnFailure <9>
----
+
<1> Schedule for the job specified in cron format. In this example, the job will run every minute.
<2> An optional concurrency policy, specifying how to treat concurrent jobs within a cron job. Only one of the following concurrent policies may be specified. If not specified, this defaults to allowing concurrent executions.
* `Allow` allows cron jobs to run concurrently.
* `Forbid` forbids concurrent runs, skipping the next run if the previous has not
finished yet.
* `Replace` cancels the currently running job and replaces
it with a new one.
<3> An optional deadline (in seconds) for starting the job if it misses its
scheduled time for any reason. Missed jobs executions will be counted as failed
ones. If not specified, there is no deadline.
<4> An optional flag allowing the suspension of a cron job. If set to `true`,
all subsequent executions will be suspended.
<5> The number of successful finished jobs to retain (defaults to 3).
<6> The number of failed finished jobs to retain (defaults to 1).
<7> Job template. This is similar to the job example.
<8> Sets a label for jobs spawned by this cron job.
<9> The restart policy of the pod. This does not apply to the job controller.
+
[NOTE]
====
The `.spec.successfulJobsHistoryLimit` and `.spec.failedJobsHistoryLimit` fields are optional.
These fields specify how many completed and failed jobs should be kept.  By default, they are
set to `3` and `1` respectively.  Setting a limit to `0` corresponds to keeping none of the corresponding
kind of jobs after they finish.
====

. Create the cron job:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

[NOTE]
====
You can also create and launch a cron job from a single command using `oc create cronjob`. The following command creates and launches a cron job similar to the one specified in the previous example:

[source,terminal]
----
$ oc create cronjob pi --image=perl --schedule='*/1 * * * *' -- perl -Mbignum=bpi -wle 'print bpi(2000)'
----

With `oc create cronjob`, the `--schedule` option accepts schedules in cron format.
====
