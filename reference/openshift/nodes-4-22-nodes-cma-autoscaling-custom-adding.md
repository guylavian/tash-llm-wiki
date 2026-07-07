---
title: "Understanding how to add custom metrics autoscalers"
type: reference
domain: openshift
slug: nodes-4-22-nodes-cma-autoscaling-custom-adding
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-cma-autoscaling-custom-adding
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Understanding how to add custom metrics autoscalers

[id="nodes-cma-autoscaling-custom-adding"]
= Understanding how to add custom metrics autoscalers

To add a custom metrics autoscaler, create a `ScaledObject` custom resource for a deployment, stateful set, or custom resource. Create a `ScaledJob` custom resource for a job.

You can create only one scaled object for each workload that you want to scale. Also, you cannot use a scaled object and the horizontal pod autoscaler (HPA) on the same workload.

// If you want to scale based on a custom trigger and CPU/Memory, you can create multiple triggers in the scaled object or scaled job.

// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-adding.adoc

[id="nodes-cma-autoscaling-custom-creating-workload_{context}"]
= Adding a custom metrics autoscaler to a workload

You can create a custom metrics autoscaler for a workload that is created by a `Deployment`, `StatefulSet`, or `custom resource` object.

.Prerequisites

* The Custom Metrics Autoscaler Operator must be installed.

* If you use a custom metrics autoscaler for scaling based on CPU or memory:

** Your cluster administrator must have properly configured cluster metrics. You can use the `oc describe PodMetrics <pod-name>` command to determine if metrics are configured. If metrics are configured, the output appears similar to the following, with CPU and Memory displayed under Usage.
+
[source,terminal]
----
$ oc describe PodMetrics openshift-kube-scheduler-ip-10-0-135-131.ec2.internal
----
+
.Example output
[source,yaml,options="nowrap"]
----
Name:         openshift-kube-scheduler-ip-10-0-135-131.ec2.internal
Namespace:    openshift-kube-scheduler
Labels:       <none>
Annotations:  <none>
API Version:  metrics.k8s.io/v1beta1
Containers:
  Name:  wait-for-host-port
  Usage:
    Memory:  0
  Name:      scheduler
  Usage:
    Cpu:     8m
    Memory:  45440Ki
Kind:        PodMetrics
Metadata:
  Creation Timestamp:  2019-05-23T18:47:56Z
  Self Link:           /apis/metrics.k8s.io/v1beta1/namespaces/openshift-kube-scheduler/pods/openshift-kube-scheduler-ip-10-0-135-131.ec2.internal
Timestamp:             2019-05-23T18:47:56Z
Window:                1m0s
Events:                <none>
----

** The pods associated with the object you want to scale must include specified memory and CPU limits. For example:
+
.Example pod spec
[source,yaml]
----
apiVersion: v1
kind: Pod
# ...
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      limits:
        memory: "128Mi"
        cpu: "500m"
# ...
----

.Procedure

. Create a YAML file similar to the following. Only the name `<2>`, object name `<4>`, and object kind `<5>` are required:
+
.Example scaled object
[source,yaml,options="nowrap"]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  annotations:
    autoscaling.keda.sh/paused-replicas: "0" <1>
  name: scaledobject <2>
  namespace: my-namespace
spec:
  scaleTargetRef:
    apiVersion: apps/v1 <3>
    name: example-deployment <4>
    kind: Deployment <5>
    envSourceContainerName: .spec.template.spec.containers[0] <6>
  cooldownPeriod:  200 <7>
  maxReplicaCount: 100 <8>
  minReplicaCount: 0 <9>
  metricsServer: <10>
    auditConfig:
      logFormat: "json"
      logOutputVolumeClaim: "persistentVolumeClaimName"
      policy:
        rules:
        - level: Metadata
        omitStages: "RequestReceived"
        omitManagedFields: false
      lifetime:
        maxAge: "2"
        maxBackup: "1"
        maxSize: "50"
  fallback: <11>
    failureThreshold: 3
    replicas: 6
    behavior: static <12>
  pollingInterval: 30 <13>
  advanced:
    restoreToOriginalReplicaCount: false <14>
    horizontalPodAutoscalerConfig:
      name: keda-hpa-scale-down <15>
      behavior: <16>
        scaleDown:
          stabilizationWindowSeconds: 300
          policies:
          - type: Percent
            value: 100
            periodSeconds: 15
  triggers:
  - type: prometheus <17>
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: basic
    authenticationRef: <18>
      name: prom-triggerauthentication
      kind: TriggerAuthentication
----
<1> Optional: Specifies that the Custom Metrics Autoscaler Operator is to scale the replicas to the specified value and stop autoscaling, as described in the "Pausing the custom metrics autoscaler for a workload" section.
<2> Specifies a name for this custom metrics autoscaler.
<3> Optional: Specifies the API version of the target resource. The default is `apps/v1`.
<4> Specifies the name of the object that you want to scale.
<5> Specifies the `kind` as `Deployment`, `StatefulSet` or `CustomResource`.
<6> Optional: Specifies the name of the container in the target resource, from which the custom metrics autoscaler gets environment variables holding secrets and so forth. The default is `.spec.template.spec.containers[0]`.
<7> Optional. Specifies the period in seconds to wait after the last trigger is reported before scaling the deployment back to `0` if the `minReplicaCount` is set to `0`. The default is `300`.
<8> Optional: Specifies the maximum number of replicas when scaling up. The default is `100`.
<9> Optional: Specifies the minimum number of replicas when scaling down.
<10> Optional: Specifies the parameters for audit logs. as described in the "Configuring audit logging" section.
<11> Optional: Specifies the number of replicas to fall back to if a scaler fails to get metrics from the source for the number of times defined by the `failureThreshold` parameter. For more information on fallback behavior, see the KEDA documentation.
<12> Optional: Specifies the replica count to be used if a fallback occurs. Enter one of the following options or omit the parameter:
* Enter `static` to use the number of replicas specified by the `fallback.replicas` parameter. This is the default.
* Enter `currentReplicas` to maintain the current number of replicas.
* Enter `currentReplicasIfHigher` to maintain the current number of replicas, if that number is higher than the `fallback.replicas` parameter. If the current number of replicas is lower than the `fallback.replicas` parameter, use the `fallback.replicas` value.
* Enter `currentReplicasIfLower` to maintain the current number of replicas, if that number is lower than the `fallback.replicas` parameter. If the current number of replicas is higher than the `fallback.replicas` parameter, use the `fallback.replicas` value.
<13> Optional: Specifies the interval in seconds to check each trigger on. The default is `30`.
<14> Optional: Specifies whether to scale back the target resource to the original replica count after the scaled object is deleted. The default is `false`, which keeps the replica count as it is when the scaled object is deleted.
<15> Optional: Specifies a name for the horizontal pod autoscaler. The default is `keda-hpa-{scaled-object-name}`.
<16> Optional: Specifies a scaling policy to use to control the rate to scale pods up or down, as described in the "Scaling policies" section.
<17> Specifies the trigger to use as the basis for scaling, as described in the "Understanding the custom metrics autoscaler triggers" section. This example uses OpenShift Container Platform monitoring.
<18> Optional: Specifies a trigger authentication or a cluster trigger authentication. For more information, see _Understanding the custom metrics autoscaler trigger authentication_ in the _Additional resources_ section.
* Enter `TriggerAuthentication` to use a trigger authentication. This is the default.
* Enter `ClusterTriggerAuthentication` to use a cluster trigger authentication.

. Create the custom metrics autoscaler by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

.Verification

* View the command output to verify that the custom metrics autoscaler was created:
+
[source,terminal]
----
$ oc get scaledobject <scaled_object_name>
----
+
.Example output
[source,terminal]
----
NAME            SCALETARGETKIND      SCALETARGETNAME        MIN   MAX   TRIGGERS     AUTHENTICATION               READY   ACTIVE   FALLBACK   AGE
scaledobject    apps/v1.Deployment   example-deployment     0     50    prometheus   prom-triggerauthentication   True    True     True       17s
----
+
Note the following fields in the output:
+
--
* `TRIGGERS`: Indicates the trigger, or scaler, that is being used.
* `AUTHENTICATION`: Indicates the name of any trigger authentication being used.
* `READY`: Indicates whether the scaled object is ready to start scaling:
** If `True`, the scaled object is ready.
** If `False`, the scaled object is not ready because of a problem in one or more of the objects you created.
* `ACTIVE`: Indicates whether scaling is taking place:
** If `True`, scaling is taking place.
** If `False`, scaling is not taking place because there are no metrics or there is a problem in one or more of the objects you created.
* `FALLBACK`: Indicates whether the custom metrics autoscaler is able to get metrics from the source
** If `False`, the custom metrics autoscaler is getting metrics.
** If `True`, the custom metrics autoscaler is getting metrics because there are no metrics or there is a problem in one or more of the objects you created.
--

//Scaling by using a scaled job is a Technology Preview feature. TP not supported in ROSA/OSD
// Module included in the following assemblies:
//
// * nodes/cma/nodes-cma-autoscaling-custom-adding.adoc

[id="nodes-cma-autoscaling-custom-creating-job_{context}"]
= Adding a custom metrics autoscaler to a job

You can create a custom metrics autoscaler for any `Job` object.

.Prerequisites

* The Custom Metrics Autoscaler Operator must be installed.

.Procedure

. Create a YAML file similar to the following:
+
[source,yaml,options="nowrap"]
----
kind: ScaledJob
apiVersion: keda.sh/v1alpha1
metadata:
  name: scaledjob
  namespace: my-namespace
spec:
  failedJobsHistoryLimit: 5
  jobTargetRef:
    activeDeadlineSeconds: 600 <1>
    backoffLimit: 6 <2>
    parallelism: 1 <3>
    completions: 1 <4>
    template:  <5>
      metadata:
        name: pi
      spec:
        containers:
        - name: pi
          image: perl
          command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
  maxReplicaCount: 100 <6>
  pollingInterval: 30 <7>
  successfulJobsHistoryLimit: 5 <8>
  failedJobsHistoryLimit: 5 <9>
  envSourceContainerName: <10>
  rolloutStrategy: gradual <11>
  scalingStrategy: <12>
    strategy: "custom"
    customScalingQueueLengthDeduction: 1
    customScalingRunningJobPercentage: "0.5"
    pendingPodConditions:
      - "Ready"
      - "PodScheduled"
      - "AnyOtherCustomPodCondition"
    multipleScalersCalculation : "max"
  triggers:
  - type: prometheus <13>
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9092
      namespace: kedatest
      metricName: http_requests_total
      threshold: '5'
      query: sum(rate(http_requests_total{job="test-app"}[1m]))
      authModes: "bearer"
    authenticationRef: <14>
      name: prom-cluster-triggerauthentication
----
<1> Specifies the maximum duration the job can run.
<2> Specifies the number of retries for a job. The default is `6`.
<3> Optional: Specifies how many pod replicas a job should run in parallel; defaults to `1`.
* For non-parallel jobs, leave unset. When unset, the default is `1`.
<4> Optional: Specifies how many successful pod completions are needed to mark a job completed.
* For non-parallel jobs, leave unset. When unset,  the default is `1`.
* For parallel jobs with a fixed completion count, specify the number of completions.
* For parallel jobs with a work queue, leave unset. When unset the default is the value of the `parallelism` parameter.
<5> Specifies the template for the pod the controller creates.
<6> Optional: Specifies the maximum number of replicas when scaling up. The default is `100`.
<7> Optional: Specifies the interval in seconds to check each trigger on. The default is `30`.
<8> Optional: Specifies the number of successful finished jobs should be kept. The default is `100`.
<9> Optional: Specifies how many failed jobs should be kept. The default is `100`.
<10> Optional: Specifies the name of the container in the target resource, from which the custom autoscaler gets environment variables holding secrets and so forth. The default is `.spec.template.spec.containers[0]`.
<11> Optional: Specifies whether existing jobs are terminated whenever a scaled job is being updated:
+
--
* `default`: The autoscaler terminates an existing job if its associated scaled job is updated. The autoscaler recreates the job with the latest specs.
* `gradual`: The autoscaler does not terminate an existing job if its associated scaled job is updated. The autoscaler creates new jobs with the latest specs.
--
+
<12> Optional: Specifies a scaling strategy: `default`, `custom`, or `accurate`. The default is `default`. For more information, see the link in the "Additional resources" section that follows.
<13> Specifies the trigger to use as the basis for scaling, as described in the "Understanding the custom metrics autoscaler triggers" section.
<14> Optional: Specifies a trigger authentication or a cluster trigger authentication. For more information, see _Understanding the custom metrics autoscaler trigger authentication_ in the _Additional resources_ section.
* Enter `TriggerAuthentication` to use a trigger authentication. This is the default.
* Enter `ClusterTriggerAuthentication` to use a cluster trigger authentication.

. Create the custom metrics autoscaler by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

.Verification

* View the command output to verify that the custom metrics autoscaler was created:
+
[source,terminal]
----
$ oc get scaledjob <scaled_job_name>
----
+
.Example output
[source,terminal]
----
NAME        MAX   TRIGGERS     AUTHENTICATION              READY   ACTIVE    AGE
scaledjob   100   prometheus   prom-triggerauthentication  True    True      8s
----
+
Note the following fields in the output:
+
--
* `TRIGGERS`: Indicates the trigger, or scaler, that is being used.
* `AUTHENTICATION`: Indicates the name of any trigger authentication being used.
* `READY`: Indicates whether the scaled object is ready to start scaling:
** If `True`, the scaled object is ready.
** If `False`, the scaled object is not ready because of a problem in one or more of the objects you created.
* `ACTIVE`: Indicates whether scaling is taking place:
** If `True`, scaling is taking place.
** If `False`, scaling is not taking place because there are no metrics or there is a problem in one or more of the objects you created.
--

[role="_additional-resources"]
[id="nodes-cma-autoscaling-custom-adding-additional-resources"]
== Additional resources

* Understanding custom metrics autoscaler trigger authentications
