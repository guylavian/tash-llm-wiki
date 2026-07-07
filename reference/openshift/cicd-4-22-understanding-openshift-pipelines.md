---
title: "Understanding {pipelines-shortname}"
type: reference
domain: openshift
slug: cicd-4-22-understanding-openshift-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/understanding-openshift-pipelines
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Understanding {pipelines-shortname}

[id="understanding-openshift-pipelines"]
= Understanding {pipelines-shortname}

{pipelines-title} is a cloud-native, continuous integration and continuous delivery (CI/CD) solution based on Kubernetes resources. It uses Tekton building blocks to automate deployments across multiple platforms by abstracting away the underlying implementation details. Tekton introduces a number of standard custom resource definitions (CRDs) for defining CI/CD pipelines that are portable across Kubernetes distributions.

[id="op-key-features"]
== Key features

* {pipelines-title} is a serverless CI/CD system that runs pipelines with all the required dependencies in isolated containers.
* {pipelines-title} are designed for decentralized teams that work on microservice-based architecture.
* {pipelines-title} use standard CI/CD pipeline definitions that are easy to extend and integrate with the existing Kubernetes tools, enabling you to scale on-demand.
* You can use {pipelines-title} to build images with Kubernetes tools such as Source-to-Image (S2I), Buildah, Buildpacks, and Kaniko that are portable across any Kubernetes platform.
* You can use the OpenShift Container Platform web console *Developer* perspective to create Tekton resources, view logs of pipeline runs, and manage pipelines in your OpenShift Container Platform namespaces.

[id="op-detailed-concepts"]
== {pipelines-shortname} Concepts
This guide provides a detailed view of the various pipeline concepts.

//About tasks
// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="about-tasks_{context}"]
= Tasks

`Task` resources are the building blocks of a pipeline and consist of sequentially executed steps. It is essentially a function of inputs and outputs. A task can run individually or as a part of the pipeline. Tasks are reusable and can be used in multiple pipelines.

_Steps_ are a series of commands that are sequentially executed by the task and achieve a specific goal, such as building an image. Every task runs as a pod, and each step runs as a container within that pod. Because steps run within the same pod, they can access the same volumes for caching files, config maps, and secrets.

The following example shows the `apply-manifests` task.

[source,yaml]
----
apiVersion: tekton.dev/v1beta1 <1>
kind: Task <2>
metadata:
  name: apply-manifests <3>
spec: <4>
  workspaces:
  - name: source
  params:
    - name: manifest_dir
      description: The directory in source that contains yaml manifests
      type: string
      default: "k8s"
  steps:
    - name: apply
      image: image-registry.openshift-image-registry.svc:5000/openshift/cli:latest
      workingDir: /workspace/source
      command: ["/bin/bash", "-c"]
      args:
        - |-
          echo Applying manifests in $(params.manifest_dir) directory
          oc apply -f $(params.manifest_dir)
          echo -----------------------------------
----
<1> The task API version, `v1beta1`.
<2> The type of Kubernetes object, `Task`.
<3> The unique name of this task.
<4> The list of parameters and steps in the task and the workspace used by the task.

This task starts the pod and runs a container inside that pod using the specified image to run the specified commands.

[NOTE]
====
Starting with {pipelines-shortname} 1.6, the following defaults from the step YAML file are removed:

* The `HOME` environment variable does not default to the `/tekton/home` directory
* The `workingDir` field does not default to the `/workspace` directory

Instead, the container for the step defines the `HOME` environment variable and the `workingDir` field. However, you can override the default values by specifying the custom values in the YAML file for the step.

As a temporary measure, to maintain backward compatibility with the older {pipelines-shortname} versions, you can set the following fields in the `TektonConfig` custom resource definition to `false`:
```
spec:
  pipeline:
    disable-working-directory-overwrite: false
    disable-home-env-overwrite: false
```
====
//About when expression
// This module is included in the following assembly:
//
// *openshift_pipelines/understanding-openshift-pipelines.adoc

[id="about-whenexpression_{context}"]
= When expression

When expressions guard task execution by setting criteria for the execution of tasks within a pipeline. They contain a list of components that allows a task to run only when certain criteria are met. When expressions are also supported in the final set of tasks that are specified using the `finally` field in the pipeline YAML file.

The key components of a when expression are as follows:

* `input`: Specifies static inputs or variables such as a parameter, task result, and execution status. You must enter a valid input. If you do not enter a valid input, its value defaults to an empty string.
* `operator`: Specifies the relationship of an input to a set of `values`. Enter `in` or `notin` as your operator values.
* `values`: Specifies an array of string values. Enter a non-empty array of static values or variables such as parameters, results, and a bound state of a workspace.

The declared when expressions are evaluated before the task is run. If the value of a when expression is `True`, the task is run. If the value of a when expression is `False`, the task is skipped.

You can use the when expressions in various use cases. For example, whether:

* The result of a previous task is as expected.
* A file in a Git repository has changed in the previous commits.
* An image exists in the registry.
* An optional workspace is available.

The following example shows the when expressions for a pipeline run. The pipeline run will execute the `create-file` task only if the following criteria are met: the `path` parameter is `README.md`,  and the `echo-file-exists` task executed only if the `exists` result from the `check-file` task is `yes`.

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun <1>
metadata:
  generateName: guarded-pr-
spec:
  serviceAccountName: 'pipeline'
  pipelineSpec:
    params:
      - name: path
        type: string
        description: The path of the file to be created
    workspaces:
      - name: source
        description: |
          This workspace is shared among all the pipeline tasks to read/write common resources
    tasks:
      - name: create-file <2>
        when:
          - input: "$(params.path)"
            operator: in
            values: ["README.md"]
        workspaces:
          - name: source
            workspace: source
        taskSpec:
          workspaces:
            - name: source
              description: The workspace to create the readme file in
          steps:
            - name: write-new-stuff
              image: ubuntu
              script: 'touch $(workspaces.source.path)/README.md'
      - name: check-file
        params:
          - name: path
            value: "$(params.path)"
        workspaces:
          - name: source
            workspace: source
        runAfter:
          - create-file
        taskSpec:
          params:
            - name: path
          workspaces:
            - name: source
              description: The workspace to check for the file
          results:
            - name: exists
              description: indicates whether the file exists or is missing
          steps:
            - name: check-file
              image: alpine
              script: |
                if test -f $(workspaces.source.path)/$(params.path); then
                  printf yes | tee /tekton/results/exists
                else
                  printf no | tee /tekton/results/exists
                fi
      - name: echo-file-exists
        when: <3>
          - input: "$(tasks.check-file.results.exists)"
            operator: in
            values: ["yes"]
        taskSpec:
          steps:
            - name: echo
              image: ubuntu
              script: 'echo file exists'
...
      - name: task-should-be-skipped-1
        when: <4>
          - input: "$(params.path)"
            operator: notin
            values: ["README.md"]
        taskSpec:
          steps:
            - name: echo
              image: ubuntu
              script: exit 1
...
    finally:
      - name: finally-task-should-be-executed
        when: <5>
          - input: "$(tasks.echo-file-exists.status)"
            operator: in
            values: ["Succeeded"]
          - input: "$(tasks.status)"
            operator: in
            values: ["Succeeded"]
          - input: "$(tasks.check-file.results.exists)"
            operator: in
            values: ["yes"]
          - input: "$(params.path)"
            operator: in
            values: ["README.md"]
        taskSpec:
          steps:
            - name: echo
              image: ubuntu
              script: 'echo finally done'
  params:
    - name: path
      value: README.md
  workspaces:
    - name: source
      volumeClaimTemplate:
        spec:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 16Mi
----
<1> Specifies the type of Kubernetes object. In this example, `PipelineRun`.
<2> Task `create-file` used in the pipeline.
<3> `when` expression that specifies to execute the `echo-file-exists` task only if the `exists` result from the `check-file` task is `yes`.
<4> `when` expression that specifies to skip the `task-should-be-skipped-1` task only if the `path` parameter is `README.md`.
<5> `when` expression that specifies to execute the `finally-task-should-be-executed` task only if the execution status of the `echo-file-exists` task and the task status is `Succeeded`, the `exists` result from the `check-file` task is `yes`, and the `path` parameter is `README.md`.

The *Pipeline Run details* page of the OpenShift Container Platform web console shows the status of the tasks and when expressions as follows:

* All the criteria are met: Tasks and the when expression symbol, which is represented by a diamond shape are green.
* Any one of the criteria are not met: Task is skipped. Skipped tasks and the when expression symbol are grey.
* None of the criteria are met: Task is skipped. Skipped tasks and the when expression symbol are grey.
* Task run fails: Failed tasks and the when expression symbol are red.

//About final tasks
// This module is included in the following assembly:
//
// *openshift_pipelines/understanding-openshift-pipelines.adoc

[id="about-finally_tasks_{context}"]
= Finally tasks

The `finally` tasks are the final set of tasks specified using the `finally` field in the pipeline YAML file. A `finally` task always executes the tasks within the pipeline, irrespective of whether the pipeline runs are executed successfully. The `finally` tasks are executed in parallel after all the pipeline tasks are run, before the corresponding pipeline exits.

You can configure a `finally` task to consume the results of any task within the same pipeline. This approach does not change the order in which this final task is run. It is executed in parallel with other final tasks after all the non-final tasks are executed.

The following example shows a code snippet of the `clone-cleanup-workspace` pipeline. This code clones the repository into a shared workspace and cleans up the workspace. After executing the pipeline tasks, the `cleanup` task specified in the `finally` section of the pipeline YAML file cleans up the workspace.

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: clone-cleanup-workspace <1>
spec:
  workspaces:
    - name: git-source <2>
  tasks:
    - name: clone-app-repo <3>
      taskRef:
        name: git-clone-from-catalog
      params:
        - name: url
          value: https://github.com/tektoncd/community.git
        - name: subdirectory
          value: application
      workspaces:
        - name: output
          workspace: git-source
  finally:
    - name: cleanup <4>
      taskRef: <5>
        name: cleanup-workspace
      workspaces: <6>
        - name: source
          workspace: git-source
    - name: check-git-commit
      params: <7>
        - name: commit
          value: $(tasks.clone-app-repo.results.commit)
      taskSpec: <8>
        params:
          - name: commit
        steps:
          - name: check-commit-initialized
            image: alpine
            script: |
              if [[ ! $(params.commit) ]]; then
                exit 1
              fi
----
<1> Unique name of the pipeline.
<2> The shared workspace where the git repository is cloned.
<3> The task to clone the application repository to the shared workspace.
<4> The task to clean-up the shared workspace.
<5> A reference to the task that is to be executed in the task run.
<6> A shared storage volume that a task in a pipeline needs at runtime to receive input or provide output.
<7> A list of parameters required for a task. If a parameter does not have an implicit default value, you must explicitly set its value.
<8> Embedded task definition.
//About task run
// Ths module is included in the following assembly:
//
// *openshift_pipelines/op-creating-applications-with-cicd-pipelines.adoc

[id="about-taskrun_{context}"]
= TaskRun

A `TaskRun` instantiates a task for execution with specific inputs, outputs, and execution parameters on a cluster. It can be invoked on its own or as part of a pipeline run for each task in a pipeline.

A task consists of one or more steps that execute container images, and each container image performs a specific piece of build work. A task run executes the steps in a task in the specified order, until all steps execute successfully or a failure occurs. A `TaskRun` is automatically created by a `PipelineRun` for each task in a pipeline.

The following example shows a task run that runs the `apply-manifests` task with the relevant input parameters:
[source,yaml]
----
apiVersion: tekton.dev/v1beta1 <1>
kind: TaskRun <2>
metadata:
  name: apply-manifests-taskrun <3>
spec: <4>
  serviceAccountName: pipeline
  taskRef: <5>
    kind: Task
    name: apply-manifests
  workspaces: <6>
  - name: source
    persistentVolumeClaim:
      claimName: source-pvc
----
<1> The task run API version `v1beta1`.
<2> Specifies the type of Kubernetes object. In this example, `TaskRun`.
<3> Unique name to identify this task run.
<4> Definition of the task run. For this task run, the task and the required workspace are specified.
<5> Name of the task reference used for this task run. This task run executes the `apply-manifests` task.
<6> Workspace used by the task run.
//About pipelines
// Ths module is included in the following assembly:
//
// *openshift_pipelines/op-creating-applications-with-cicd-pipelines.adoc

[id="about-pipelines_{context}"]
= Pipelines

A `Pipeline` is a collection of `Task` resources arranged in a specific order of execution. They are executed to construct complex workflows that automate the build, deployment and delivery of applications. You can define a CI/CD workflow for your application using pipelines containing one or more tasks.

A `Pipeline` resource definition consists of a number of fields or attributes, which together enable the pipeline to accomplish a specific goal. Each `Pipeline` resource definition must contain at least one `Task` resource, which ingests specific inputs and produces specific outputs. The pipeline definition can also optionally include _Conditions_, _Workspaces_, _Parameters_, or _Resources_ depending on the application requirements.

The following example shows the `build-and-deploy` pipeline, which builds an application image from a Git repository using the `buildah` `ClusterTask` resource:

[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1 <1>
kind: Pipeline <2>
metadata:
  name: build-and-deploy <3>
spec: <4>
  workspaces: <5>
  - name: shared-workspace
  params: <6>
  - name: deployment-name
    type: string
    description: name of the deployment to be patched
  - name: git-url
    type: string
    description: url of the git repo for the code of deployment
  - name: git-revision
    type: string
    description: revision to be used from repo of the code for deployment
    default: "{pipelines-ver}"
  - name: IMAGE
    type: string
    description: image to be built from the code
  tasks: <7>
  - name: fetch-repository
    taskRef:
      name: git-clone
      kind: ClusterTask
    workspaces:
    - name: output
      workspace: shared-workspace
    params:
    - name: url
      value: $(params.git-url)
    - name: subdirectory
      value: ""
    - name: deleteExisting
      value: "true"
    - name: revision
      value: $(params.git-revision)
  - name: build-image <8>
    taskRef:
      name: buildah
      kind: ClusterTask
    params:
    - name: TLSVERIFY
      value: "false"
    - name: IMAGE
      value: $(params.IMAGE)
    workspaces:
    - name: source
      workspace: shared-workspace
    runAfter:
    - fetch-repository
  - name: apply-manifests <9>
    taskRef:
      name: apply-manifests
    workspaces:
    - name: source
      workspace: shared-workspace
    runAfter: <10>
    - build-image
  - name: update-deployment
    taskRef:
      name: update-deployment
    workspaces:
    - name: source
      workspace: shared-workspace
    params:
    - name: deployment
      value: $(params.deployment-name)
    - name: IMAGE
      value: $(params.IMAGE)
    runAfter:
    - apply-manifests
----
<1> Pipeline API version `v1beta1`.
<2> Specifies the type of Kubernetes object. In this example, `Pipeline`.
<3> Unique name of this pipeline.
<4> Specifies the definition and structure of the pipeline.
<5> Workspaces used across all the tasks in the pipeline.
<6> Parameters used across all the tasks in the pipeline.
<7> Specifies the list of tasks used in the pipeline.
<8> Task `build-image`, which uses the `buildah` `ClusterTask` to build application images from a given Git repository.
<9> Task `apply-manifests`, which uses a user-defined task with the same name.
<10> Specifies the sequence in which tasks are run in a pipeline. In this example, the `apply-manifests` task is run only after the `build-image` task is completed.

[NOTE]
====
The {pipelines-title} Operator installs the Buildah cluster task and creates the `pipeline` service account with sufficient permission to build and push an image. The Buildah cluster task can fail when associated with a different service account with insufficient permissions.
====
//About pipeline run
// This module is included in the following assembly:
//
// *openshift_pipelines/op-creating-applications-with-cicd-pipelines.adoc

[id="about-pipelinerun_{context}"]
= PipelineRun

A `PipelineRun` is a type of resource that binds a pipeline, workspaces, credentials, and a set of parameter values specific to a scenario to run the CI/CD workflow.

A `PipelineRun` is the running instance of a pipeline. It instantiates a pipeline for execution with specific inputs, outputs, and execution parameters on a cluster. It also creates a task run for each task in the pipeline run.

The pipeline runs the tasks sequentially until they are complete or a task fails. The `status` field tracks and the progress of each task run and stores it for monitoring and auditing purposes.

The following example runs the `build-and-deploy` pipeline with relevant resources and parameters:
[source,yaml]
----
apiVersion: tekton.dev/v1beta1 <1>
kind: PipelineRun <2>
metadata:
  name: build-deploy-api-pipelinerun <3>
spec:
  pipelineRef:
    name: build-and-deploy <4>
  params: <5>
  - name: deployment-name
    value: vote-api
  - name: git-url
    value: https://github.com/openshift-pipelines/vote-api.git
  - name: IMAGE
    value: image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/vote-api
  workspaces: <6>
  - name: shared-workspace
    volumeClaimTemplate:
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 500Mi
----
<1> Pipeline run API version `v1beta1`.
<2> The type of Kubernetes object. In this example, `PipelineRun`.
<3> Unique name to identify this pipeline run.
<4> Name of the pipeline to be run. In this example, `build-and-deploy`.
<5> The list of parameters required to run the pipeline.
<6> Workspace used by the pipeline run.

[role="_additional-resources"]
.Additional resources

* Authenticating pipelines using git secret
//About workspace
// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="about-workspaces_{context}"]
= Workspaces

[NOTE]
====
It is recommended that you use workspaces instead of the `PipelineResource` CRs in {pipelines-title}, as `PipelineResource` CRs are difficult to debug, limited in scope, and make tasks less reusable.
====

Workspaces declare shared storage volumes that a task in a pipeline needs at runtime to receive input or provide output. Instead of specifying the actual location of the volumes, workspaces enable you to declare the filesystem or parts of the filesystem that would be required at runtime. A task or pipeline declares the workspace and you must provide the specific location details of the volume. It is then mounted into that workspace in a task run or a pipeline run. This separation of volume declaration from runtime storage volumes makes the tasks reusable, flexible, and independent of the user environment.

With workspaces, you can:

* Store task inputs and outputs
* Share data among tasks
* Use it as a mount point for credentials held in secrets
* Use it as a mount point for configurations held in config maps
* Use it as a mount point for common tools shared by an organization
* Create a cache of build artifacts that speed up jobs

You can specify workspaces in the `TaskRun` or `PipelineRun` using:

* A read-only config map or secret
* An existing persistent volume claim shared with other tasks
* A persistent volume claim from a provided volume claim template
* An `emptyDir` that is discarded when the task run completes

The following example shows a code snippet of the `build-and-deploy` pipeline, which declares a `shared-workspace` workspace for the `build-image` and `apply-manifests` tasks as defined in the pipeline.

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: build-and-deploy
spec:
  workspaces: <1>
  - name: shared-workspace
  params:
...
  tasks: <2>
  - name: build-image
    taskRef:
      name: buildah
      kind: ClusterTask
    params:
    - name: TLSVERIFY
      value: "false"
    - name: IMAGE
      value: $(params.IMAGE)
    workspaces: <3>
    - name: source <4>
      workspace: shared-workspace <5>
    runAfter:
    - fetch-repository
  - name: apply-manifests
    taskRef:
      name: apply-manifests
    workspaces: <6>
    - name: source
      workspace: shared-workspace
    runAfter:
      - build-image
...
----
<1> List of workspaces shared between the tasks defined in the pipeline. A pipeline can define as many workspaces as required. In this example, only one workspace named `shared-workspace` is declared.
<2> Definition of tasks used in the pipeline. This snippet defines two tasks, `build-image` and `apply-manifests`, which share a common workspace.
<3> List of workspaces used in the `build-image` task. A task definition can include as many workspaces as it requires. However, it is recommended that a task uses at most one writable workspace.
<4> Name that uniquely identifies the workspace used in the task. This task uses one workspace named `source`.
<5> Name of the pipeline workspace used by the task. Note that the workspace `source` in turn uses the pipeline workspace named `shared-workspace`.
<6> List of workspaces used in the `apply-manifests` task. Note that this task shares the `source` workspace with the `build-image` task.

Workspaces help tasks share data, and allow you to specify one or more volumes that each task in the pipeline requires during execution. You can create a persistent volume claim or provide a volume claim template that creates a persistent volume claim for you.

The following code snippet of the `build-deploy-api-pipelinerun` pipeline run uses a volume claim template to create a persistent volume claim for defining the storage volume for the `shared-workspace` workspace used in the `build-and-deploy` pipeline.

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: build-deploy-api-pipelinerun
spec:
  pipelineRef:
    name: build-and-deploy
  params:
...

  workspaces: <1>
  - name: shared-workspace <2>
    volumeClaimTemplate: <3>
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 500Mi
----
<1> Specifies the list of pipeline workspaces for which volume binding will be provided in the pipeline run.
<2> The name of the workspace in the pipeline for which the volume is being provided.
<3> Specifies a volume claim template that creates a persistent volume claim to define the storage volume for the workspace.
//About triggers
// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="about-triggers_{context}"]
= Triggers

Use _Triggers_ in conjunction with pipelines to create a full-fledged CI/CD system where Kubernetes resources define the entire CI/CD execution. Triggers capture the external events, such as a Git pull request, and process them to extract key pieces of information. Mapping this event data to a set of predefined parameters triggers a series of tasks that can then create and deploy Kubernetes resources and instantiate the pipeline.

For example, you define a CI/CD workflow using {pipelines-title} for your application. The pipeline must start for any new changes to take effect in the application repository. Triggers automate this process by capturing and processing any change event and by triggering a pipeline run that deploys the new image with the latest changes.

Triggers consist of the following main resources that work together to form a reusable, decoupled, and self-sustaining CI/CD system:

--
* The `TriggerBinding` resource extracts the fields from an event payload and stores them as parameters.
+
The following example shows a code snippet of the `TriggerBinding` resource, which extracts the Git repository information from the received event payload:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1 <1>
kind: TriggerBinding <2>
metadata:
  name: vote-app <3>
spec:
  params: <4>
  - name: git-repo-url
    value: $(body.repository.url)
  - name: git-repo-name
    value: $(body.repository.name)
  - name: git-revision
    value: $(body.head_commit.id)
----
+
<1> The API version of the `TriggerBinding` resource. In this example, `v1beta1`.
<2> Specifies the type of Kubernetes object. In this example, `TriggerBinding`.
<3> Unique name to identify the `TriggerBinding` resource.
<4> List of parameters which will be extracted from the received event payload and passed to the `TriggerTemplate` resource. In this example, the Git repository URL, name, and revision are extracted from the body of the event payload.

* The `TriggerTemplate` resource acts as a standard for the way resources must be created. It specifies the way parameterized data from the `TriggerBinding` resource should be used.
A trigger template receives input from the trigger binding, and then performs a series of actions that results in creation of new pipeline resources, and initiation of a new pipeline run.
+
The following example shows a code snippet of a `TriggerTemplate` resource, which creates a pipeline run using the Git repository information received from the `TriggerBinding` resource you just created:
+
[source,yaml,subs="attributes+"]
----
apiVersion: triggers.tekton.dev/v1beta1 <1>
kind: TriggerTemplate <2>
metadata:
  name: vote-app <3>
spec:
  params: <4>
  - name: git-repo-url
    description: The git repository url
  - name: git-revision
    description: The git revision
    default: {pipelines-ver}
  - name: git-repo-name
    description: The name of the deployment to be created / patched

  resourcetemplates: <5>
  - apiVersion: tekton.dev/v1beta1
    kind: PipelineRun
    metadata:
      name: build-deploy-$(tt.params.git-repo-name)-$(uid)
    spec:
      serviceAccountName: pipeline
      pipelineRef:
        name: build-and-deploy
      params:
      - name: deployment-name
        value: $(tt.params.git-repo-name)
      - name: git-url
        value: $(tt.params.git-repo-url)
      - name: git-revision
        value: $(tt.params.git-revision)
      - name: IMAGE
        value: image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/$(tt.params.git-repo-name)
      workspaces:
      - name: shared-workspace
        volumeClaimTemplate:
         spec:
          accessModes:
           - ReadWriteOnce
          resources:
            requests:
              storage: 500Mi
----
+
<1> The API version of the `TriggerTemplate` resource. In this example, `v1beta1`.
<2> Specifies the type of Kubernetes object. In this example, `TriggerTemplate`.
<3> Unique name to identify the `TriggerTemplate` resource.
<4> Parameters supplied by the `TriggerBinding` resource.
<5> List of templates that specify the way resources must be created using the parameters received through the `TriggerBinding` or `EventListener` resources.

* The `Trigger` resource combines the `TriggerBinding` and `TriggerTemplate` resources, and optionally, the `interceptors` event processor.
+
Interceptors process all the events for a specific platform that runs before the `TriggerBinding` resource.  You can use interceptors to filter the payload, verify events, define and test trigger conditions, and implement other useful processing. Interceptors use secret for event verification. Once the event data passes through an interceptor, it then goes to the trigger before you pass the payload data to the trigger binding. You can also use an interceptor to modify the behavior of the associated trigger referenced in the `EventListener` specification.
//image::op-triggers.png[]
+
The following example shows a code snippet of a `Trigger` resource, named `vote-trigger` that connects the `TriggerBinding` and `TriggerTemplate` resources, and the `interceptors` event processor.
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1 <1>
kind: Trigger <2>
metadata:
  name: vote-trigger <3>
spec:
  serviceAccountName: pipeline <4>
  interceptors:
    - ref:
        name: "github" <5>
      params: <6>
        - name: "secretRef"
          value:
            secretName: github-secret
            secretKey: secretToken
        - name: "eventTypes"
          value: ["push"]
  bindings:
    - ref: vote-app <7>
  template: <8>
     ref: vote-app
---
apiVersion: v1
kind: Secret <9>
metadata:
  name: github-secret
type: Opaque
stringData:
  secretToken: "1234567"
----
+
<1> The API version of the `Trigger` resource. In this example, `v1beta1`.
<2> Specifies the type of Kubernetes object. In this example, `Trigger`.
<3> Unique name to identify the `Trigger` resource.
<4> Service account name to be used.
<5> Interceptor name to be referenced. In this example, `github`.
<6> Desired parameters to be specified.
<7> Name of the `TriggerBinding` resource to be connected to the `TriggerTemplate` resource.
<8> Name of the `TriggerTemplate` resource to be connected to the `TriggerBinding` resource.
<9> Secret to be used to verify events.

* The `EventListener` resource provides an endpoint, or an event sink, that listens for incoming HTTP-based events with a JSON payload. It  extracts event parameters from each `TriggerBinding` resource, and then processes this data to create Kubernetes resources as specified by the corresponding `TriggerTemplate` resource. The `EventListener` resource also performs lightweight event processing or basic filtering on the payload using event `interceptors`, which identify the type of payload and optionally modify it. Currently, pipeline triggers support five types of interceptors: _Webhook Interceptors_, _GitHub Interceptors_, _GitLab Interceptors_, _Bitbucket Interceptors_, and _Common Expression Language (CEL) Interceptors_.
+
The following example shows an `EventListener` resource, which references the `Trigger` resource named `vote-trigger`.
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1 <1>
kind: EventListener <2>
metadata:
  name: vote-app <3>
spec:
  serviceAccountName: pipeline <4>
  triggers:
    - triggerRef: vote-trigger <5>
----
+
<1> The API version of the `EventListener` resource. In this example, `v1beta1`.
<2> Specifies the type of Kubernetes object. In this example, `EventListener`.
<3> Unique name to identify the `EventListener` resource.
<4> Service account name to be used.
<5> Name of the `Trigger` resource referenced by the `EventListener` resource.
--

[role="_additional-resources"]
== Additional resources

* For information on installing {pipelines-shortname}, see Installing {pipelines-shortname}.
* For more details on creating custom CI/CD solutions, see Creating CI/CD solutions for applications using {pipelines-shortname}.
* For more details on re-encrypt TLS termination, see Re-encryption Termination.
* For more details on secured routes, see the Securing routes section.
