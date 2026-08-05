---
title: "Managing workloads with the {js-operator}"
type: reference
domain: openshift
slug: ai-workloads-4-22-managing-jobset
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/ai_workloads/managing-jobset
version: 4.22
family: ai_workloads
documentKind: "Documentation"
---

# Managing workloads with the {js-operator}

[id="js-managing"]
= Managing workloads with the {js-operator}

[role="_abstract"]
Use the {js-operator} on OpenShift Container Platform to manage and run large-scale, coordinated workloads like high-performance computing (HPC) and AI training. Features like multi-template job support and stable networking can help you recover quickly and use resources efficiently.

// Deploying a jobset
// Module included in the following assemblies:
//
// * ai_workloads/jobset_operator/managing-jobset.adoc

[id="js-config_{context}"]
= Deploying a JobSet

[role="_abstract"]
You can use the {js-operator} to deploy a JobSet to manage and run large-scale, coordinated workloads.

.Prerequisites

* You have installed the {js-operator}.
* You have a cluster with available NVIDIA GPUs.

.Procedure

. Create a new project by running the following command:
+
[source,terminal]
----
$ oc new-project <my_namespace>
----

. Create a file named `jobset.yaml`:
+
[source,yaml]
----
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: pytorch
spec:
  replicatedJobs:
  - name: workers
    template:
      spec:
        parallelism: 3
        completions: 3
        backoffLimit: 0
        template:
          spec:
            imagePullSecrets:
              - name: my-registry-secret
            initContainers:
              - name: prepare
                image: docker.io/alpine/git:v2.52.0
                args: ['clone', 'https://github.com/pytorch/examples']
                volumeMounts:
                  - name: workdir
                    mountPath: /git
            containers:
              - name: pytorch
                image: docker.io/pytorch/pytorch:2.10.0-cuda13.0-cudnn9-runtime
                resources:
                  limits:
                    nvidia.com/gpu: "1"
                  requests:
                    nvidia.com/gpu: "1"
                ports:
                - containerPort: 4321
                env:
                - name: MASTER_ADDR
                  value: "pytorch-workers-0-0.pytorch"
                - name: MASTER_PORT
                  value: "4321"
                - name: RANK
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.annotations['batch.kubernetes.io/job-completion-index']
                - name: PYTHONUNBUFFERED
                  value: "0"
                command:
                - /bin/sh
                - -c
                - |
                  cd examples/distributed/ddp-tutorial-series
                  torchrun --nproc_per_node=1 --nnodes=3 --rdzv_id=100 --rdzv_backend=c10d --rdzv_endpoint=$MASTER_ADDR:$MASTER_PORT multinode.py 1000 100
                volumeMounts:
                  - name: workdir
                    mountPath: /workspace
            volumes:
              - name: workdir
                emptyDir: {}
----
+
where:
+
--
`spec.replicatedJobs.template.spec.parallelism`:: Specifies the number of pods running at the same time.
`spec.replicatedJobs.template.spec.completions`:: Specifies the total number of pods that must finish successfully for the job to be marked complete.
--

. Apply the JobSet configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f jobset.yaml
----

.Verification

* Verify that pods were started by running the following command:
+
[source,terminal]
----
$ oc get pods -n <my_namespace>
----
+
.Example output
[source,terminal]
----
NAME                        READY   STATUS    RESTARTS   AGE
pytorch-workers-0-0-2lzwt   1/1     Running   0          2m17s
pytorch-workers-0-1-g2lrv   1/1     Running   0          2m17s
pytorch-workers-0-2-dpljq   1/1     Running   0          2m17s
----

// Designating a coordinator
// Module included in the following assemblies:
//
// * ai_workloads/jobset_operator/managing-jobset.adoc

[id="js-coordinator_{context}"]
= Specifying a JobSet coordinator

[role="_abstract"]
To manage communication between JobSet pods, you can assign a specific JobSet coordinator pod. This ensures that your distributed workloads can reference a stable network endpoint as a central point of coordination for task synchronization and data exchange.

.Prerequisites

* You have installed the {js-operator}.

.Procedure

. Create a new namespace by running the following command.
+
[source,terminal]
----
$ oc new-project <new_namespace>
----

. Create a YAML file called `jobset-coordinator.yaml`:
+
.Example YAML file
[source,yaml]
----
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: coordinator
spec:
  coordinator:
    replicatedJob: driver
    jobIndex: 0
    podIndex: 0
  replicatedJobs:
  - name: workers
    template:
      spec:
        parallelism: <pods_running_number>
        completions: <pods_finish_number>
        backoffLimit: 0
        template:
          spec:
            containers:
            - name: worker
              env:
                - name: COORDINATOR_ENDPOINT
                  valueFrom:
                    fieldRef:
                      fieldPath: metadata.labels['jobset.sigs.k8s.io/coordinator']
              image: quay.io/nginx/nginx-unprivileged:1.29-alpine
              command: [ "/bin/sh", "-c" ]
              args:
                - |
                  while ! curl -s "${COORDINATOR_ENDPOINT}:8080" | grep Welcome; do
                    sleep 3
                  done
                  sleep 100
  - name: driver
    template:
      spec:
        parallelism: <pods_running_number>
        completions: <pods_finish_number>
        backoffLimit: 0
        template:
          spec:
            containers:
            - name: driver
              image: quay.io/nginx/nginx-unprivileged:1.29-alpine
            ports:
              - containerPort: 8080
                protocol: TCP
----
+
where:
+
--
`<pods_running_number>`:: Specifies the number of pods running at the same time.
`<pods_finish_number>`:: Specifies the total number of pods that must finish successfully for the job to be marked complete.
--

. Apply the `jobset-coordinator.yaml` file by running the following command:
+
[source,terminal]
----
$ oc apply -f jobset-coordinator.yaml
----

.Verification

* Verify that pods were created by running the following command:
+
[source,terminal]
----
$ oc get pods -n <new_namespace>
----
+
.Example output
[source,terminal]
----
NAME                            READY   STATUS              RESTARTS   AGE
coordinator-driver-0-0-svgk7    1/1     Running             0          67s
coordinator-workers-0-0-57jvg   1/1     Running             0          67s
coordinator-workers-0-1-mghvx   1/1     Running             0          67s
coordinator-workers-0-2-7cnvv   1/1     Running             0          67s
----

// Failure Policy Configurations
// Module included in the following assemblies:
//
// * ai_workloads/jobset_operator/managing-jobset.adoc

[id="js-failure-policy_{context}"]
= Failure policy configuration for {js-operator}

[role="_abstract"]
To control workload behavior in response to child job failures, you can configure a JobSet failure policy. This enables you to define specific actions, such as restarting or failing the entire JobSet, based on the failure reason or the specific replicated job affected.

[id="jobset-failure-policy-actions_{context}"]
== Failure policy actions

These actions are available when a job failure matches a defined rule.

[cols="1,3"]
|===
| Action | Description

| `FailJobSet`
| Marks the entire JobSet as failed immediately.

| `RestartJobSet`
| Restarts the JobSet by recreating all child jobs. This action counts toward the `maxRestarts` limit. This is the default action if no rules match.

| `RestartJobSetAndIgnoreMaxRestarts`
| Restarts the JobSet without counting toward the `maxRestarts` limit.
|===

[id="jobset-rule-attributes_{context}"]
== Rule-targeting attributes

Use the following attributes to define failure rules.

[cols="1,3"]
|===
| Attribute | Description

| `targetReplicatedJobs`
| Specifies which replicated jobs trigger the rule.

| `onJobFailureReasons`
| Triggers the rule based on the specific job failure reason. Valid values include `BackoffLimitExceeded`, `DeadlineExceeded`, and `PodFailurePolicy`.
|===

[id="jobset-rule-config-example_{context}"]
== Configuration example

This configuration marks the JobSet as failed if the `leader` job fails.

.Example of a YAML file to mark the job set failed if the leader fails
[source,yaml]
----
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: failjobset-action-example
spec:
  failurePolicy:
    maxRestarts: 3
    rules:
      - action: FailJobSet
        targetReplicatedJobs:
        - leader
  replicatedJobs:
  - name: leader
    replicas: 1
    template:
      spec:
        backoffLimit: 0
        completions: 2
        parallelism: 2
        template:
          spec:
            containers:
            - name: leader
              image: docker.io/bash:latest
              command:
              - bash
              - -xc
              - |
                echo "JOB_COMPLETION_INDEX=$JOB_COMPLETION_INDEX"
                if [[ "$JOB_COMPLETION_INDEX" == "0" ]]; then
                  for i in $(seq 10 -1 1)
                  do
                    echo "Sleeping in $i"
                    sleep 1
                  done
                  exit 1
                fi
                for i in $(seq 1 1000)
                do
                  echo "$i"
                  sleep 1
                done
  - name: workers
    replicas: 1
    template:
      spec:
        backoffLimit: 0
        completions: 2
        parallelism: 2
        template:
          spec:
            containers:
            - name: worker
              image: docker.io/bash:latest
              command:
              - bash
              - -xc
              - |
                sleep 1000

----

[NOTE]
====
The `InPlaceRestart` alpha feature is not currently supported on the {js-operator}.
====

// Configuring volume claim policies for {js-operator}
// Module included in the following assemblies:
//
// * ai_workloads/jobset_operator/managing-jobset.adoc

[id="js-volume-claim-policies_{context}"]
= Configuring volume claim policies for {js-operator}

[role="_abstract"]
You can configure a JobSet to automatically create and manage shared persistent volume claims (PVCs) across multiple replicated jobs. This is useful for workloads that require shared access to datasets, models, or checkpoints.

.Prerequisites

* You have the {js-operator} installed in your cluster.
* You have set a default storage class or chosen a storage class for your workload.

.Procedure

. Define the volume templates in the `spec.volumeClaimPolicies` section of your JobSet YAML file.
+
[source,yaml]
----
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: <job_name>
spec:
  volumeClaimPolicies:
    - templates:
        - metadata:
            name: <persistent_volume_claim_name_prefix>
          spec:
            accessModes: ["ReadWriteOnce"]
            storageClassName: mystorageclass
            resources:
              requests:
                storage: 1Gi
      retentionPolicy:
        whenDeleted: Retain
----
+
where:
+
--
`<job_name>`:: Specifies your unique identifier for your jobs within your namespace.
`<persistent_volume_claim_name>`:: Specifies the name for the PVC. The name used here will also be used as the `volumeMounts` name. A volume will be automatically added to the pod that will mount a PVC created with a name in the format of `<persistent_volume_claim_name>-<job_name>`.
`<deletion_retention_policy>`:: Specifies the deletion retention policy. Optionally, you can keep data after the JobSet is deleted by setting this value to `Retain`.
--

. In your `replicatedJobs` configuration, add a `volumeMount` that matches the template name you defined.
+
[source,yaml]
----
apiVersion: jobset.x-k8s.io/v1alpha2
kind: JobSet
metadata:
  name: <job_name>
spec:
  replicatedJobs:
  - name: workers
    template:
      spec:
        parallelism: 2
        completions: 2
        backoffLimit: 0
        template:
          spec:
            imagePullSecrets:
              - name: my-registry-secret
            initContainers:
              - name: prepare
                image: docker.io/alpine/git:v2.52.0
                args: ['clone', 'https://github.com/pytorch/examples']
                volumeMounts:
                  - name: <persistent_volume_claim_name>
                    mountPath: /git/checkpoint
#...
----

. Apply the JobSet configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f <jobset_yaml>
----

.Verification

* Verify that the PVCs were created using the naming convention `<claim_name>-<jobset_name>`:
+
[source,terminal]
----
$ oc get pvc
----
+
.Example output
[source,terminal]
----
NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
pvc-1       Bound    pvc-385996a0-70af-4791-aa8e-9e6459e6b123   3Gi        RWO            file-storage   3d
pvc-2       Bound    pvc-8aeddd4d-aad5-4039-8d04-640a71c9a72d   12Gi       RWO            file-storage   3d
pvc-3       Bound    pvc-0050144d-940c-4c4e-a23a-2a660a5490eb   12Gi       RWO            file-storage   3d
----

[role="_additional-resources"]
[id="js-managing_additional-resources"]
== Additional resources

* JobSet documentation (Kubernetes)

* Failure Policy (Kubernetes)
