---
title: "Setting compute resource quota for {pipelines-shortname}"
type: reference
domain: openshift
slug: cicd-4-22-setting-compute-resource-quota-for-openshift-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/setting-compute-resource-quota-for-openshift-pipelines
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Setting compute resource quota for {pipelines-shortname}

[id="setting-compute-resource-quota-for-openshift-pipelines"]
= Setting compute resource quota for {pipelines-shortname}

A `ResourceQuota` object in {pipelines-title} controls the total resource consumption per namespace. You can use it to limit the quantity of objects created in a namespace, based on the type of the object. In addition, you can specify a compute resource quota to restrict the total amount of compute resources consumed in a namespace.

However, you might want to limit the amount of compute resources consumed by pods resulting from a pipeline run, rather than setting quotas for the entire namespace. Currently, {pipelines-title} does not enable you to directly specify the compute resource quota for a pipeline.

// This module is included in the following assembly:
//
// */cicd/pipelines/setting-compute-resource-quota-for-openshift-pipelines.adoc

[id="alternative-approaches-compute-resource-quota-pipelines_{context}"]
= Alternative approaches for limiting compute resource consumption in {pipelines-shortname}

To attain some degree of control over the usage of compute resources by a pipeline, consider the following alternative approaches:

* Set resource requests and limits for each step in a task.
+
.Example: Set resource requests and limits for each step in a task.
+
[source,yaml]
----
...
spec:
  steps:
    - name: step-with-limts
      resources:
        requests:
          memory: 1Gi
          cpu: 500m
        limits:
          memory: 2Gi
          cpu: 800m
...
----

* Set resource limits by specifying values for the `LimitRange` object. For more information on `LimitRange`, refer to Restrict resource consumption with limit ranges.

* Reduce pipeline resource consumption.

* Set and manage resource quotas per project.

* Ideally, the compute resource quota for a pipeline should be same as the total amount of compute resources consumed by the concurrently running pods in a pipeline run. However, the pods running the tasks consume compute resources based on the use case. For example, a Maven build task might require different compute resources for different applications that it builds. As a result, you cannot predetermine the compute resource quotas for tasks in a generic pipeline. For greater predictability and control over usage of compute resources, use customized pipelines for different applications.

[NOTE]
====
When using {pipelines-title} in a namespace configured with a `ResourceQuota` object, the pods resulting from task runs and pipeline runs might fail with an error, such as: `failed quota: <quota name> must specify cpu, memory`.

To avoid this error, do any one of the following:

* (Recommended) Specify a limit range for the namespace.
* Explicitly define requests and limits for all containers.

For more information, refer to the issue and the resolution.
====

If your use case is not addressed by these approaches, you can implement a workaround by using a resource quota for a priority class.

// This module is included in the following assembly:
//
// */cicd/pipelines/setting-compute-resource-quota-for-openshift-pipelines.adoc

[id="specifying-pipelines-resource-quota-using-priority-class_{context}"]
= Specifying pipelines resource quota using priority class

A `PriorityClass` object maps priority class names to the integer values that indicates their relative priorities. Higher values increase the priority of a class. After you create a priority class, you can create pods that specify the priority class name in their specifications. In addition, you can control a pod's consumption of system resources based on the pod's priority.

Specifying resource quota for a pipeline is similar to setting a resource quota for the subset of pods created by a pipeline run. The following steps provide an example of the workaround by specifying resource quota based on priority class.

.Procedure

. Create a priority class for a pipeline.
+
.Example: Priority class for a pipeline
[source,yaml]
----
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: pipeline1-pc
value: 1000000
description: "Priority class for pipeline1"
----

. Create a resource quota for a pipeline.
+
.Example: Resource quota for a pipeline
[source,yaml]
----
apiVersion: v1
kind: ResourceQuota
metadata:
  name: pipeline1-rq
spec:
  hard:
    cpu: "1000"
    memory: 200Gi
    pods: "10"
  scopeSelector:
    matchExpressions:
    - operator : In
      scopeName: PriorityClass
      values: ["pipeline1-pc"]
----

. Verify the resource quota usage for the pipeline.
+
.Example: Verify resource quota usage for the pipeline
[source,terminal]
----
$ oc describe quota
----
+
.Sample output
----
Name:       pipeline1-rq
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     1k
memory      0     200Gi
pods        0     10
----
+
Because pods are not running, the quota is unused.

. Create the pipelines and tasks.
+
.Example: YAML for the pipeline
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: maven-build
spec:
  workspaces:
  - name: local-maven-repo
  resources:
  - name: app-git
    type: git
  tasks:
  - name: build
    taskRef:
      name: mvn
    resources:
      inputs:
      - name: source
        resource: app-git
    params:
    - name: GOALS
      value: ["package"]
    workspaces:
    - name: maven-repo
      workspace: local-maven-repo
  - name: int-test
    taskRef:
      name: mvn
    runAfter: ["build"]
    resources:
      inputs:
      - name: source
        resource: app-git
    params:
    - name: GOALS
      value: ["verify"]
    workspaces:
    - name: maven-repo
      workspace: local-maven-repo
  - name: gen-report
    taskRef:
      name: mvn
    runAfter: ["build"]
    resources:
      inputs:
      - name: source
        resource: app-git
    params:
    - name: GOALS
      value: ["site"]
    workspaces:
    - name: maven-repo
      workspace: local-maven-repo
----
+
.Example: YAML for a task in the pipeline
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: mvn
spec:
  workspaces:
  - name: maven-repo
  resources:
    inputs:
    - name: source
      type: git
  params:
  - name: GOALS
    description: The Maven goals to run
    type: array
    default: ["package"]
  steps:
    - name: mvn
      image: gcr.io/cloud-builders/mvn
      workingDir: /workspace/source
      command: ["/usr/bin/mvn"]
      args:
        - -Dmaven.repo.local=$(workspaces.maven-repo.path)
        - "$(params.GOALS)"
----

. Create and start the pipeline run.
+
.Example: YAML for a pipeline run
[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  generateName: petclinic-run-
spec:
  pipelineRef:
    name: maven-build
  podTemplate:
    priorityClassName: pipeline1-pc
  workspaces:
  - name: local-maven-repo
    emptyDir: {}
  resources:
  - name: app-git
    resourceSpec:
      type: git
      params:
        - name: url
          value: https://github.com/spring-projects/spring-petclinic
----
+
[NOTE]
====
The pipeline run might fail with an error: `failed quota: <quota name> must specify cpu, memory`.

To avoid this error, set a limit range for the namespace, where the defaults from the `LimitRange` object apply to pods created during the build process.

For more information about setting limit ranges, refer to _Restrict resource consumption with limit ranges_ in the _Additional resources_ section.
====

. After the pods are created, verify the resource quota usage for the pipeline run.
+
.Example: Verify resource quota usage for the pipeline
[source,terminal]
----
$ oc describe quota
----
+
.Sample output
----
Name:       pipeline1-rq
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         500m  1k
memory      10Gi  200Gi
pods        1     10
----
+
The output indicates that you can manage the combined resource quota for all concurrent running pods belonging to a priority class, by specifying the resource quota per priority class.

[role="_additional-resources"]
[id="additional-resources_setting-compute-resource-quota-for-pipelines"]
== Additional resources

* Restrict resource consumption with limit ranges
* Resource quotas in Kubernetes
* Limit ranges in Kubernetes
* Resource requests and limits in Kubernetes
