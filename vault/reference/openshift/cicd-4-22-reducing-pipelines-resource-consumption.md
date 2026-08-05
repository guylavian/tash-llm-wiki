---
title: "Reducing resource consumption of {pipelines-shortname}"
type: reference
domain: openshift
slug: cicd-4-22-reducing-pipelines-resource-consumption
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/reducing-pipelines-resource-consumption
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Reducing resource consumption of {pipelines-shortname}

[id="reducing-pipelines-resource-consumption"]
= Reducing resource consumption of {pipelines-shortname}

If you use clusters in multi-tenant environments you must control the consumption of CPU, memory, and storage resources for each project and Kubernetes object. This helps prevent any one application from consuming too many resources and affecting other applications.

To define the final resource limits that are set on the resulting pods, {pipelines-title} use resource quota limits and limit ranges of the project in which they are executed.

To restrict resource consumption in your project, you can:

* Set and manage resource quotas to limit the aggregate resource consumption.
* Use limit ranges to restrict resource consumption for specific objects, such as pods, images, image streams, and persistent volume claims.

// Module included in the following assemblies:
//
// */openshift_pipelines/uninstalling-pipelines.adoc

[id='op-understanding-pipelines-resource-consumption_{context}']
= Understanding resource consumption in pipelines

Each task consists of a number of required steps to be executed in a particular order defined in the `steps` field of the `Task` resource. Every task runs as a pod, and each step runs as a container within that pod.

Steps are executed one at a time. The pod that executes the task only requests enough resources to run a single container image (step) in the task at a time, and thus does not store resources for all the steps in the task.

The `Resources` field in the `steps` spec specifies the limits for resource consumption.
By default, the resource requests for the CPU, memory, and ephemeral storage are set to `BestEffort` (zero) values or to the minimums set through limit ranges in that project.

.Example configuration of resource requests and limits for a step
[source,yaml]
----
spec:
  steps:
  - name: <step_name>
    resources:
      requests:
        memory: 2Gi
        cpu: 600m
      limits:
        memory: 4Gi
        cpu: 900m
----

When the `LimitRange` parameter and the minimum values for container resource requests are specified in the project in which the pipeline and task runs are executed, {pipelines-title} looks at all the `LimitRange` values in the project and uses the minimum values instead of zero.

.Example configuration of limit range parameters at a project level
[source,yaml]
----
apiVersion: v1
kind: LimitRange
metadata:
  name: <limit_container_resource>
spec:
  limits:
  - max:
      cpu: "600m"
      memory: "2Gi"
    min:
      cpu: "200m"
      memory: "100Mi"
    default:
      cpu: "500m"
      memory: "800Mi"
    defaultRequest:
      cpu: "100m"
      memory: "100Mi"
    type: Container
...
----

// Module included in the following assemblies:
//
// */openshift_pipelines/uninstalling-pipelines.adoc

[id='op-mitigating-extra-pipeline-resource-consumption_{context}']
= Mitigating extra resource consumption in pipelines

When you have resource limits set on the containers in your pod, OpenShift Container Platform sums up the resource limits requested as all containers run simultaneously.

To consume the minimum amount of resources needed to execute one step at a time in the invoked task, {pipelines-title} requests the maximum CPU, memory, and ephemeral storage as specified in the step that requires the most amount of resources. This ensures that the resource requirements of all the steps are met. Requests other than the maximum values are set to zero.

However, this behavior can lead to higher resource usage than required. If you use resource quotas, this could also lead to unschedulable pods.

For example, consider a task with two steps that uses scripts, and that does not define any resource limits and requests. The resulting pod has two init containers (one for entrypoint copy, the other for writing scripts) and two containers, one for each step.

OpenShift Container Platform uses the limit range set up for the project to compute required resource requests and limits.
For this example, set the following limit range in the project:

[source,yaml]
----
apiVersion: v1
kind: LimitRange
metadata:
  name: mem-min-max-demo-lr
spec:
  limits:
  - max:
      memory: 1Gi
    min:
      memory: 500Mi
    type: Container
----

In this scenario, each init container uses a request memory of 1Gi (the max limit of the limit range), and each container uses a request memory of 500Mi. Thus, the total memory request for the pod is 2Gi.

If the same limit range is used with a task of ten steps, the final memory request is 5Gi, which is higher than what each step actually needs, that is 500Mi (since each step runs after the other).

Thus, to reduce resource consumption of resources, you can:

* Reduce the number of steps in a given task by grouping different steps into one bigger step, using the script feature, and the same image. This reduces the minimum  requested resource.
* Distribute steps that are relatively independent of each other and can run on their own to multiple tasks instead of a single task. This lowers the number of steps in each task, making the request for each task smaller, and the scheduler can then run them when the resources are available.

[role="_additional-resources"]
[id="additional-resources_reducing-pipelines-resource-consumption"]
== Additional resources

* Setting compute resource quota for {pipelines-shortname}
* Resource quotas per project
* Restricting resource consumption using limit ranges
* Resource requests and limits in Kubernetes
