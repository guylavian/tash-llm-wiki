---
title: "Creating CI/CD solutions for applications using {pipelines-shortname}"
type: reference
domain: openshift
slug: cicd-4-22-creating-applications-with-cicd-pipelines
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/creating-applications-with-cicd-pipelines
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Creating CI/CD solutions for applications using {pipelines-shortname}

[id="creating-applications-with-cicd-pipelines"]
= Creating CI/CD solutions for applications using {pipelines-shortname}

With {pipelines-title}, you can create a customized CI/CD solution to build, test, and deploy your application.

To create a full-fledged, self-serving CI/CD pipeline for an application, perform the following tasks:

* Create custom tasks, or install existing reusable tasks.
* Create and define the delivery pipeline for your application.
* Provide a storage volume or filesystem that is attached to a workspace for the pipeline execution, using one of the following approaches:
** Specify a volume claim template that creates a persistent volume claim
** Specify a persistent volume claim
* Create a `PipelineRun` object to instantiate and invoke the pipeline.
* Add triggers to capture events in the source repository.

This section uses the `pipelines-tutorial` example to demonstrate the preceding tasks. The example uses a simple application which consists of:

* A front-end interface, `pipelines-vote-ui`, with the source code in the `pipelines-vote-ui` Git repository.
* A back-end interface, `pipelines-vote-api`, with the source code in the `pipelines-vote-api`  Git repository.
* The `apply-manifests` and `update-deployment` tasks in the `pipelines-tutorial` Git repository.

== Prerequisites

* You have access to an OpenShift Container Platform cluster.
* You have installed {pipelines-shortname} using the {pipelines-title} Operator listed in the software catalog. After it is installed, it is applicable to the entire cluster.
* You have installed {pipelines-shortname} CLI.
* You have forked the front-end `pipelines-vote-ui` and back-end `pipelines-vote-api` Git repositories using your GitHub ID, and have administrator access to these repositories.
* Optional: You have cloned the `pipelines-tutorial` Git repository.

// This module is included in the following assembly:
//
// *openshift_pipelines/creating-cicd-solutions-using-openshift-pipelines.adoc

[id="creating-project-and-checking-pipeline-service-account_{context}"]
= Creating a project and checking your pipeline service account

[discrete]
.Procedure

. Log in to your OpenShift Container Platform cluster:
+
----
$ oc login -u <login> -p <password> https://openshift.example.com:6443
----

. Create a project for the sample application. For this example workflow, create the `pipelines-tutorial` project:
+
----
$ oc new-project pipelines-tutorial
----
+
[NOTE]
====
If you create a project with a different name, be sure to update the resource URLs used in the example with your project name.
====
. View the `pipeline` service account:
+
{pipelines-title} Operator adds and configures a service account named `pipeline` that has sufficient permissions to build and push an image. This service account is used by the `PipelineRun` object.
+
----
$ oc get serviceaccount pipeline
----

// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="creating-pipeline-tasks_{context}"]
= Creating pipeline tasks

[discrete]
.Procedure

. Install the `apply-manifests` and `update-deployment` task resources from the `pipelines-tutorial` repository, which contains a list of reusable tasks for pipelines:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/01_pipeline/01_apply_manifest_task.yaml
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/01_pipeline/02_update_deployment_task.yaml
----

. Use the `tkn task list` command to list the tasks you created:
+
[source,terminal]
----
$ tkn task list
----
+
The output verifies that the `apply-manifests` and `update-deployment` task resources were created:
+
[source,terminal]
----
NAME                DESCRIPTION   AGE
apply-manifests                   1 minute ago
update-deployment                 48 seconds ago
----

. Use the `tkn clustertasks list` command to list the Operator-installed additional cluster tasks such as `buildah` and `s2i-python`:
+
[NOTE]
====
To use the `buildah` cluster task in a restricted environment, you must ensure that the Dockerfile uses an internal image stream as the base image.
====
+
[source,terminal]
----
$ tkn clustertasks list
----
+
The output lists the Operator-installed `ClusterTask` resources:
+
[source,terminal]
----
NAME                       DESCRIPTION   AGE
buildah                                  1 day ago
git-clone                                1 day ago
s2i-python                               1 day ago
tkn                                      1 day ago
----

[IMPORTANT]
====
In {pipelines-title} 1.10, cluster task functionality is deprecated and is planned to be removed in a future release.
====

[role="_additional-resources"]
.Additional resources

* Managing non-versioned and versioned cluster tasks

// This module is included in the following assembly:
//
//  *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="assembling-a-pipeline_{context}"]
= Assembling a pipeline

A pipeline represents a CI/CD flow and is defined by the tasks to be executed. It is designed to be generic and reusable in multiple applications and environments.

A pipeline specifies how the tasks interact with each other and their order of execution using the `from` and `runAfter` parameters. It uses the `workspaces` field to specify one or more volumes that each task in the pipeline requires during execution.

In this section, you will create a pipeline that takes the source code of the application from GitHub, and then builds and deploys it on OpenShift Container Platform.

The pipeline performs the following tasks for the back-end application `pipelines-vote-api` and front-end application `pipelines-vote-ui`:

* Clones the source code of the application from the Git repository by referring to the `git-url` and `git-revision` parameters.
* Builds the container image using the `buildah` cluster task.
* Pushes the image to the {product-registry} by referring to the `image` parameter.
* Deploys the new image on OpenShift Container Platform by using the `apply-manifests` and `update-deployment` tasks.

[discrete]
.Procedure

. Copy the contents of the following sample pipeline YAML file and save it:
+
[source,yaml,subs="attributes+"]
----
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: build-and-deploy
spec:
  workspaces:
  - name: shared-workspace
  params:
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
  tasks:
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
  - name: build-image
    taskRef:
      name: buildah
      kind: ClusterTask
    params:
    - name: IMAGE
      value: $(params.IMAGE)
    workspaces:
    - name: source
      workspace: shared-workspace
    runAfter:
    - fetch-repository
  - name: apply-manifests
    taskRef:
      name: apply-manifests
    workspaces:
    - name: source
      workspace: shared-workspace
    runAfter:
    - build-image
  - name: update-deployment
    taskRef:
      name: update-deployment
    params:
    - name: deployment
      value: $(params.deployment-name)
    - name: IMAGE
      value: $(params.IMAGE)
    runAfter:
    - apply-manifests
----
+
The pipeline definition abstracts away the specifics of the Git source repository and image registries. These details are added as `params` when a pipeline is triggered and executed.

. Create the pipeline:
+
----
$ oc create -f <pipeline-yaml-file-name.yaml>
----
+
Alternatively, you can also execute the YAML file directly from the Git repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/01_pipeline/04_pipeline.yaml
----

. Use the `tkn pipeline list` command to verify that the pipeline is added to the application:
+
----
$ tkn pipeline list
----
+
The output verifies that the `build-and-deploy` pipeline was created:
+
----
NAME               AGE            LAST RUN   STARTED   DURATION   STATUS
build-and-deploy   1 minute ago   ---        ---       ---        ---
----

// Module included in the following assemblies:
//
// pipelines/creating-applications-with-cicd-pipelines

[id="op-mirroring-images-to-run-pipelines-in-restricted-environment_{context}"]
=  Mirroring images to run pipelines in a restricted environment

To run {pipelines-shortname} in a disconnected cluster or a cluster provisioned in a restricted environment, ensure that either the Samples Operator is configured for a restricted network, or a cluster administrator has created a cluster with a mirrored registry.

The following procedure uses the `pipelines-tutorial` example to create a pipeline for an application in a restricted environment using a cluster with a mirrored registry. To ensure that the `pipelines-tutorial` example works in a restricted environment, you must mirror the respective builder images from the mirror registry for the front-end interface, `pipelines-vote-ui`; back-end interface, `pipelines-vote-api`; and the `cli`.

.Procedure

. Mirror the builder image from the mirror registry for the front-end interface, `pipelines-vote-ui`.
.. Verify that the required images tag is not imported:
+
[source,terminal]
----
$ oc describe imagestream python -n openshift
----
+
.Example output
[source,terminal]
----
Name:			python
Namespace:		openshift
[...]

3.8-ubi9 (latest)
  tagged from registry.redhat.io/ubi9/python-38:latest
    prefer registry pullthrough when referencing this tag

  Build and run Python 3.8 applications on UBI 8. For more information about using this builder image, including OpenShift considerations, see https://github.com/sclorg/s2i-python-container/blob/master/3.8/README.md.
  Tags: builder, python
  Supports: python:3.8, python
  Example Repo: https://github.com/sclorg/django-ex.git

[...]
----

.. Mirror the supported image tag to the private registry:
+
[source,terminal]
----
$ oc image mirror registry.redhat.io/ubi9/python-39:latest <mirror-registry>:<port>/ubi9/python-39
----

.. Import the image:
+
[source,terminal]
----
$ oc tag <mirror-registry>:<port>/ubi9/python-39 python:latest --scheduled -n openshift
----
+
You must periodically re-import the image. The `--scheduled` flag enables automatic re-import of the image.

.. Verify that the images with the given tag have been imported:
+
[source,terminal]
----
$ oc describe imagestream python -n openshift
----
+
.Example output
[source,terminal]
----
Name:			python
Namespace:		openshift
[...]

latest
  updates automatically from registry  <mirror-registry>:<port>/ubi9/python-39

  *  <mirror-registry>:<port>/ubi9/python-39@sha256:3ee...

[...]
----

. Mirror the builder image from the mirror registry for the back-end interface, `pipelines-vote-api`.
.. Verify that the required images tag is not imported:
+
[source,terminal]
----
$ oc describe imagestream golang -n openshift
----
+
.Example output
[source,terminal]
----
Name:			golang
Namespace:		openshift
[...]

1.14.7-ubi8 (latest)
  tagged from registry.redhat.io/ubi8/go-toolset:1.14.7
    prefer registry pullthrough when referencing this tag

  Build and run Go applications on UBI 8. For more information about using this builder image, including OpenShift considerations, see https://github.com/sclorg/golang-container/blob/master/README.md.
  Tags: builder, golang, go
  Supports: golang
  Example Repo: https://github.com/sclorg/golang-ex.git

[...]
----

.. Mirror the supported image tag to the private registry:
+
[source,terminal]
----
$ oc image mirror registry.redhat.io/ubi9/go-toolset:latest <mirror-registry>:<port>/ubi9/go-toolset
----

.. Import the image:
+
[source,terminal]
----
$ oc tag <mirror-registry>:<port>/ubi9/go-toolset golang:latest --scheduled -n openshift
----
+
You must periodically re-import the image. The `--scheduled` flag enables automatic re-import of the image.

.. Verify that the images with the given tag have been imported:
+
[source,terminal]
----
$ oc describe imagestream golang -n openshift
----
+
.Example output
[source,terminal]
----
Name:			golang
Namespace:		openshift
[...]

latest
  updates automatically from registry <mirror-registry>:<port>/ubi9/go-toolset

  * <mirror-registry>:<port>/ubi9/go-toolset@sha256:59a74d581df3a2bd63ab55f7ac106677694bf612a1fe9e7e3e1487f55c421b37

[...]
----

. Mirror the builder image from the mirror registry for the `cli`.
.. Verify that the required images tag is not imported:
+
[source,terminal]
----
$ oc describe imagestream cli -n openshift
----
+
.Example output
[source,terminal]
----
Name:                   cli
Namespace:              openshift
[...]

latest
  updates automatically from registry quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551

  * quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551

[...]
----

.. Mirror the supported image tag to the private registry:
+
[source,terminal]
----
$ oc image mirror quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551 <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev:latest
----

.. Import the image:
+
[source,terminal]
----
$ oc tag <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev cli:latest --scheduled -n openshift
----
+
You must periodically re-import the image. The `--scheduled` flag enables automatic re-import of the image.

.. Verify that the images with the given tag have been imported:
+
[source,terminal]
----
$ oc describe imagestream cli -n openshift
----
+
.Example output
[source,terminal]
----
Name:                   cli
Namespace:              openshift
[...]

latest
  updates automatically from registry <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev

  * <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551

[...]
----

[role="_additional-resources"]
.Additional resources

* Configuring Samples Operator for a restricted cluster

* Creating a cluster with a mirrored registry

// This module is included in the following assembly:
//
// // *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="running-a-pipeline_{context}"]
= Running a pipeline

A `PipelineRun` resource starts a pipeline and ties it to the Git and image resources that should be used for the specific invocation. It automatically creates and starts the `TaskRun` resources for each task in the pipeline.

[discrete]
.Procedure

. Start the pipeline for the back-end application:
+
[source,yaml,subs="attributes+"]
----
$ tkn pipeline start build-and-deploy \
    -w name=shared-workspace,volumeClaimTemplateFile=https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/01_pipeline/03_persistent_volume_claim.yaml \
    -p deployment-name=pipelines-vote-api \
    -p git-url=https://github.com/openshift/pipelines-vote-api.git \
    -p IMAGE='image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/pipelines-vote-api' \
    --use-param-defaults
----
+
The previous command uses a volume claim template, which creates a persistent volume claim for the pipeline execution.

. To track the progress of the pipeline run, enter the following command::
+
[source,yaml]
----
$ tkn pipelinerun logs <pipelinerun_id> -f
----
+
The <pipelinerun_id> in the above command is the ID for the `PipelineRun` that was returned in the output of the previous command.

. Start the pipeline for the front-end application:
+
[source,yaml,subs="attributes+"]
----
$ tkn pipeline start build-and-deploy \
    -w name=shared-workspace,volumeClaimTemplateFile=https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/01_pipeline/03_persistent_volume_claim.yaml \
    -p deployment-name=pipelines-vote-ui \
    -p git-url=https://github.com/openshift/pipelines-vote-ui.git \
    -p IMAGE='image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/pipelines-vote-ui' \
    --use-param-defaults
----

. To track the progress of the pipeline run, enter the following command:
+
[source,yaml]
----
$ tkn pipelinerun logs <pipelinerun_id> -f
----
+
The <pipelinerun_id> in the above command is the ID for the `PipelineRun` that was returned in the output of the previous command.

. After a few minutes, use `tkn pipelinerun list` command to verify that the pipeline ran successfully by listing all the pipeline runs:
+
[source,yaml]
----
$ tkn pipelinerun list
----
+
The output lists the pipeline runs:
+
[source,yaml]
----

 NAME                         STARTED      DURATION     STATUS
 build-and-deploy-run-xy7rw   1 hour ago   2 minutes    Succeeded
 build-and-deploy-run-z2rz8   1 hour ago   19 minutes   Succeeded
----

. Get the application route:
+
[source,yaml]
----
$ oc get route pipelines-vote-ui --template='http://{{.spec.host}}'
----
Note the output of the previous command. You can access the application using this route.

. To rerun the last pipeline run, using the pipeline resources and service account of the previous pipeline, run:
+
[source,yaml]
----
$ tkn pipeline start build-and-deploy --last
----

[role="_additional-resources"]
.Additional resources

* Authenticating pipelines using git secret

// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="adding-triggers_{context}"]
= Adding triggers to a pipeline

Triggers enable pipelines to respond to external GitHub events, such as push events and pull requests. After you assemble and start a pipeline for the application, add the `TriggerBinding`, `TriggerTemplate`, `Trigger`, and `EventListener` resources to capture the GitHub events.

[discrete]
.Procedure
. Copy the content of the following sample `TriggerBinding` YAML file and save it:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: TriggerBinding
metadata:
  name: vote-app
spec:
  params:
  - name: git-repo-url
    value: $(body.repository.url)
  - name: git-repo-name
    value: $(body.repository.name)
  - name: git-revision
    value: $(body.head_commit.id)
----

. Create the `TriggerBinding` resource:
+
[source,terminal]
----
$ oc create -f <triggerbinding-yaml-file-name.yaml>
----
+
Alternatively, you can create the `TriggerBinding` resource directly from the `pipelines-tutorial` Git repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/03_triggers/01_binding.yaml
----

. Copy the content of the following sample `TriggerTemplate` YAML file and save it:
+
[source,yaml,subs="attributes+"]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: TriggerTemplate
metadata:
  name: vote-app
spec:
  params:
  - name: git-repo-url
    description: The git repository url
  - name: git-revision
    description: The git revision
    default: {pipelines-ver}
  - name: git-repo-name
    description: The name of the deployment to be created / patched

  resourcetemplates:
  - apiVersion: tekton.dev/v1beta1
    kind: PipelineRun
    metadata:
      generateName: build-deploy-$(tt.params.git-repo-name)-
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
The template specifies a volume claim template to create a persistent volume claim for defining the storage volume for the workspace. Therefore, you do not need to create a persistent volume claim to provide data storage.

. Create the `TriggerTemplate` resource:
+
[source,terminal]
----
$ oc create -f <triggertemplate-yaml-file-name.yaml>
----
+
Alternatively, you can create the `TriggerTemplate` resource directly from the `pipelines-tutorial` Git repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/03_triggers/02_template.yaml
----

. Copy the contents of the following sample `Trigger` YAML file and save it:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: Trigger
metadata:
  name: vote-trigger
spec:
  serviceAccountName: pipeline
  bindings:
    - ref: vote-app
  template:
    ref: vote-app
----

. Create the `Trigger` resource:
+
[source,terminal]
----
$ oc create -f <trigger-yaml-file-name.yaml>
----
+
Alternatively, you can create the `Trigger` resource directly from the `pipelines-tutorial` Git repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/03_triggers/03_trigger.yaml
----

. Copy the contents of the following sample `EventListener` YAML file and save it:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: vote-app
spec:
  serviceAccountName: pipeline
  triggers:
    - triggerRef: vote-trigger
----
+

Alternatively, if you have not defined a trigger custom resource, add the binding and template spec to the `EventListener` YAML file, instead of referring to the name of the trigger:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: vote-app
spec:
  serviceAccountName: pipeline
  triggers:
  - bindings:
    - ref: vote-app
    template:
      ref: vote-app
----

. Create the `EventListener` resource by performing the following steps:
+
* To create an `EventListener` resource using a secure HTTPS connection:
+
.. Add a label to enable the secure HTTPS connection to the `Eventlistener` resource:
+
[source,terminal]
----
$ oc label namespace <ns-name> operator.tekton.dev/enable-annotation=enabled
----
.. Create the `EventListener` resource:
+
[source,terminal]
----
$ oc create -f <eventlistener-yaml-file-name.yaml>
----
+
Alternatively, you can create the `EvenListener` resource directly from the `pipelines-tutorial` Git repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/03_triggers/04_event_listener.yaml
----
.. Create a route with the re-encrypt TLS termination:
+
[source,terminal]
----
$ oc create route reencrypt --service=<svc-name> --cert=tls.crt --key=tls.key --ca-cert=ca.crt --hostname=<hostname>
----
+
Alternatively, you can create a re-encrypt TLS termination YAML file to create a secured route.
+
.Example Re-encrypt TLS Termination YAML of the Secured Route
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: route-passthrough-secured <1>
spec:
  host: <hostname>
  to:
    kind: Service
    name: frontend <1>
  tls:
    termination: reencrypt         <2>
    key: [as in edge termination]
    certificate: [as in edge termination]
    caCertificate: [as in edge termination]
    destinationCACertificate: |-   <3>
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
----
+
<1> The name of the object, which is limited to 63 characters.
<2> The `*termination*` field is set to `reencrypt`. This is the only required `tls` field.
<3> Required for re-encryption. `*destinationCACertificate*` specifies a CA certificate to validate the endpoint certificate, securing the connection from the router to the destination pods. If the service is using a service signing certificate, or the administrator has specified a default CA certificate for the router and the service has a certificate signed by that CA, this field can be omitted.
+
See `oc create route reencrypt --help` for more options.
+
* To create an `EventListener` resource using an insecure HTTP connection:
+
.. Create the `EventListener` resource.
.. Expose the `EventListener` service as an OpenShift Container Platform route to make it publicly accessible:
+
[source,terminal]
----
$ oc expose svc el-vote-app
----

// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="configuring-eventlisteners-to-serve-multiple-namespaces_{context}"]
= Configuring event listeners to serve multiple namespaces

[NOTE]
====
You can skip this section if you want to create a basic CI/CD pipeline. However, if your deployment strategy involves multiple namespaces, you can configure event listeners to serve multiple namespaces.
====

To increase reusability of `EvenListener` objects, cluster administrators can configure and deploy them as multi-tenant event listeners that serve multiple namespaces.

[discrete]
.Procedure
. Configure cluster-wide fetch permission for the event listener.
.. Set a service account name to be used in the `ClusterRoleBinding` and `EventListener` objects. For example, `el-sa`.
+
.Example `ServiceAccount.yaml`
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: el-sa
---
----
.. In the `rules` section of the `ClusterRole.yaml` file, set appropriate permissions for every event listener deployment to function cluster-wide.
+
.Example `ClusterRole.yaml`
[source,yaml]
----
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: el-sel-clusterrole
rules:
- apiGroups: ["triggers.tekton.dev"]
  resources: ["eventlisteners", "clustertriggerbindings", "clusterinterceptors", "triggerbindings", "triggertemplates", "triggers"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["configmaps", "secrets"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["serviceaccounts"]
  verbs: ["impersonate"]
...
----
.. Configure cluster role binding with the appropriate service account name and cluster role name.
+
.Example `ClusterRoleBinding.yaml`
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: el-mul-clusterrolebinding
subjects:
- kind: ServiceAccount
  name: el-sa
  namespace: default
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: el-sel-clusterrole
...
----

. In the `spec` parameter of the event listener, add the service account name, for example `el-sa`. Fill the `namespaceSelector` parameter with names of namespaces where event listener is intended to serve.
+
.Example `EventListener.yaml`
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: namespace-selector-listener
spec:
  serviceAccountName: el-sa
  namespaceSelector:
    matchNames:
    - default
    - foo
...
----

. Create a service account with the necessary permissions, for example `foo-trigger-sa`. Use it for role binding the triggers.
+
.Example `ServiceAccount.yaml`
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: foo-trigger-sa
  namespace: foo
...
----
+
.Example `RoleBinding.yaml`
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: triggercr-rolebinding
  namespace: foo
subjects:
- kind: ServiceAccount
  name: foo-trigger-sa
  namespace: foo
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: tekton-triggers-eventlistener-roles
...
----

. Create a trigger with the appropriate trigger template, trigger binding, and service account name.
+
.Example `Trigger.yaml`
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: Trigger
metadata:
  name: trigger
  namespace: foo
spec:
  serviceAccountName: foo-trigger-sa
  interceptors:
    - ref:
        name: "github"
      params:
        - name: "secretRef"
          value:
            secretName: github-secret
            secretKey: secretToken
        - name: "eventTypes"
          value: ["push"]
  bindings:
    - ref: vote-app
  template:
    ref: vote-app
...
----

// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="creating-webhooks_{context}"]
= Creating webhooks

_Webhooks_ are HTTP POST messages that are received by the event listeners whenever a configured event occurs in your repository. The event payload is then mapped to trigger bindings, and processed by trigger templates. The trigger templates eventually start one or more pipeline runs, leading to the creation and deployment of Kubernetes resources.

In this section, you will configure a webhook URL on your forked Git repositories `pipelines-vote-ui` and `pipelines-vote-api`. This URL points to the publicly accessible `EventListener` service route.

[NOTE]
====
Adding webhooks requires administrative privileges to the repository. If you do not have administrative access to your repository, contact your system administrator for adding webhooks.
====

[discrete]
.Procedure

. Get the webhook URL:
+
* For a secure HTTPS connection:
+
----
$ echo "URL: $(oc  get route el-vote-app --template='https://{{.spec.host}}')"
----
+
* For an HTTP (insecure) connection:
+
----
$ echo "URL: $(oc  get route el-vote-app --template='http://{{.spec.host}}')"
----
+
Note the URL obtained in the output.

. Configure webhooks manually on the front-end repository:

.. Open the front-end Git repository `pipelines-vote-ui` in your browser.
.. Click *Settings* -> *Webhooks* -> *Add Webhook*
.. On the *Webhooks/Add Webhook* page:
+
... Enter the webhook URL from step 1 in *Payload URL* field
... Select *application/json* for the *Content type*
... Specify the secret in the *Secret* field
... Ensure that the *Just the push event* is selected
... Select *Active*
... Click *Add Webhook*

. Repeat step 2 for the back-end repository `pipelines-vote-api`.

// This module is included in the following assembly:
//
// *openshift_pipelines/creating-applications-with-cicd-pipelines.adoc

[id="triggering-a-pipeline_{context}"]
= Triggering a pipeline run

Whenever a `push` event occurs in the Git repository, the configured webhook sends an event payload to the publicly exposed `EventListener` service route. The `EventListener` service of the application processes the payload, and passes it to the relevant `TriggerBinding` and `TriggerTemplate` resource pairs. The `TriggerBinding` resource extracts the parameters, and the `TriggerTemplate` resource uses these parameters and specifies the way the resources must be created. This may rebuild and redeploy the application.

In this section, you push an empty commit to the front-end `pipelines-vote-ui` repository, which then triggers the pipeline run.

[discrete]
.Procedure

. From the terminal, clone your forked Git repository `pipelines-vote-ui`:
+
[source,terminal,subs="attributes+"]
----
$ git clone git@github.com:<your GitHub ID>/pipelines-vote-ui.git -b {pipelines-ver}
----
. Push an empty commit:
+
[source,terminal,subs="attributes+"]
----
$ git commit -m "empty-commit" --allow-empty && git push origin {pipelines-ver}
----
. Check if the pipeline run was triggered:
+
----
$ tkn pipelinerun list
----
+
Notice that a new pipeline run was initiated.

// This module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

[id="enabling-monitoring-of-event-listeners-for-triggers-for-user-defined-projects_{context}"]
= Enabling monitoring of event listeners for Triggers for user-defined projects

As a cluster administrator, to gather event listener metrics for the `Triggers` service in a user-defined project and display them in the OpenShift Container Platform web console, you can create a service monitor for each event listener. On receiving an HTTP request, event listeners for the `Triggers` service return three metrics -- `eventlistener_http_duration_seconds`, `eventlistener_event_count`, and `eventlistener_triggered_resources`.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console.
* You have installed the {pipelines-title} Operator.
* You have enabled monitoring for user-defined projects.

.Procedure

. For each event listener, create a service monitor. For example, to view the metrics for the `github-listener` event listener in the `test` namespace, create the following service monitor:
+
[source,yaml]
----
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app.kubernetes.io/managed-by: EventListener
    app.kubernetes.io/part-of: Triggers
    eventlistener: github-listener
  annotations:
    networkoperator.openshift.io/ignore-errors: ""
  name: el-monitor
  namespace: test
spec:
  endpoints:
    - interval: 10s
      port: http-metrics
  jobLabel: name
  namespaceSelector:
    matchNames:
      - test
  selector:
    matchLabels:
      app.kubernetes.io/managed-by: EventListener
      app.kubernetes.io/part-of: Triggers
      eventlistener: github-listener
...
----
. Test the service monitor by sending a request to the event listener. For example, push an empty commit:
+
[source,terminal]
----
$ git commit -m "empty-commit" --allow-empty && git push origin main
----
. On the OpenShift Container Platform web console, navigate to **Administrator** -> **Observe** -> **Metrics**.
. To view a metric, search by its name. For example, to view the details of the `eventlistener_http_resources` metric for the `github-listener` event listener, search using the `eventlistener_http_resources` keyword.

[role="_additional-resources"]
.Additional resources

* Enabling monitoring for user-defined projects

// Ths module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

[id="op-configuring-pull-request-capabilities-in-GitHub-interceptor_{context}"]
= Configuring pull request capabilities in GitHub Interceptor

With GitHub Interceptor, you can create logic that validates and filters GitHub webhooks. For example, you can validate the webhook’s origin and filter incoming events based on specified criteria. When you use GitHub Interceptor to filter event data, you can specify the event types that Interceptor can accept in a field.
In {pipelines-title}, you can use the following capabilities of GitHub Interceptor:

* Filter pull request events based on the files that have been changed
* Validate pull requests based on configured GitHub owners

// This module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

[id="op-filtering-pull-requests-using-GitHub-interceptor_{context}"]
= Filtering pull requests using GitHub Interceptor

You can filter GitHub events based on the files that have been changed for push and pull events. This helps you to execute a pipeline for only relevant changes in your Git repository.
GitHub Interceptor adds a comma delimited list of all files that have been changed and uses the CEL Interceptor to filter incoming events based on the changed files. The list of changed files is added to the `changed_files` property of the event payload in the top-level  `extensions` field.

.Prerequisites
* You have installed the {pipelines-title} Operator.

.Procedure
. Perform one of the following steps:
* For a public GitHub repository, set the value of the `addChangedFiles` parameter to `true` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-add-changed-files-pr-listener
spec:
  triggers:
    - name: github-listener
      interceptors:
        - ref:
            name: "github"
            kind: ClusterInterceptor
            apiVersion: triggers.tekton.dev
          params:
          - name: "secretRef"
            value:
              secretName: github-secret
              secretKey: secretToken
          - name: "eventTypes"
            value: ["pull_request", "push"]
          - name: "addChangedFiles"
            value:
              enabled: true
        - ref:
            name: cel
          params:
          - name: filter
            value: extensions.changed_files.matches('controllers/')
...
----

* For a private GitHub repository, set the value of the `addChangedFiles` parameter to `true` and provide the access token details, `secretName` and `secretKey` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-add-changed-files-pr-listener
spec:
  triggers:
    - name: github-listener
      interceptors:
        - ref:
            name: "github"
            kind: ClusterInterceptor
            apiVersion: triggers.tekton.dev
          params:
          - name: "secretRef"
            value:
              secretName: github-secret
              secretKey: secretToken
          - name: "eventTypes"
            value: ["pull_request", "push"]
          - name: "addChangedFiles"
            value:
              enabled: true
              personalAccessToken:
                secretName: github-pat
                secretKey: token
        - ref:
            name: cel
          params:
          - name: filter
            value: extensions.changed_files.matches('controllers/')
...
----

. Save the configuration file.

// This module is included in the following assembly:
//
// *cicd/pipelines/creating-applications-with-cicd-pipelines.adoc

[id="op-validating-pull-requests-using-GitHub-interceptors_{context}"]
= Validating pull requests using GitHub Interceptors

You can use GitHub Interceptor to validate the processing of pull requests based on the GitHub owners configured for a repository. This validation helps you to prevent unnecessary execution of a `PipelineRun` or `TaskRun` object.
GitHub Interceptor processes a pull request only if the user name is listed as an owner or if a configurable comment is issued by an owner of the repository. For example, when you comment `/ok-to-test` on a pull request as an owner, a `PipelineRun` or `TaskRun` is triggered.

[NOTE]
====
Owners are configured in an `OWNERS` file at the root of the repository.
====

.Prerequisites
* You have installed the {pipelines-title} Operator.

.Procedure
. Create a secret string value.
. Configure the GitHub webhook with that value.
. Create a Kubernetes secret named `secretRef` that contains your secret value.
. Pass the Kubernetes secret as a reference to your GitHub Interceptor.
. Create an `owners` file and add the list of approvers into the `approvers` section.
. Perform one of the following steps:
* For a public GitHub repository, set the value of the `githubOwners` parameter to `true` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-owners-listener
spec:
  triggers:
    - name: github-listener
      interceptors:
        - ref:
            name: "github"
            kind: ClusterInterceptor
            apiVersion: triggers.tekton.dev
          params:
            - name: "secretRef"
              value:
                secretName: github-secret
                secretKey: secretToken
            - name: "eventTypes"
              value: ["pull_request", "issue_comment"]
            - name: "githubOwners"
              value:
                enabled: true
                checkType: none
...
----

* For a private GitHub repository, set the value of the `githubOwners` parameter to `true` and provide the access token details, `secretName` and `secretKey` in the YAML configuration file shown below:
+
[source,yaml]
----
apiVersion: triggers.tekton.dev/v1beta1
kind: EventListener
metadata:
  name: github-owners-listener
spec:
  triggers:
    - name: github-listener
      interceptors:
        - ref:
            name: "github"
            kind: ClusterInterceptor
            apiVersion: triggers.tekton.dev
          params:
            - name: "secretRef"
              value:
                secretName: github-secret
                secretKey: secretToken
            - name: "eventTypes"
              value: ["pull_request", "issue_comment"]
            - name: "githubOwners"
              value:
                enabled: true
                personalAccessToken:
                  secretName: github-token
                  secretKey: secretToken
                checkType: all
...
----
+
[NOTE]
====
The `checkType` parameter is used to specify the GitHub owners who need authentication. You can set its value to `orgMembers`, `repoMembers`, or `all`.
====

. Save the configuration file.

[role="_additional-resources"]
[id="pipeline-addtl-resources"]
== Additional resources

* To include {pac} along with the application source code in the same repository, see Using {pac}.
* For more details on pipelines in the *Developer* perspective, see the working with pipelines in the web console section.
* To learn more about Security Context Constraints (SCCs), see the Managing Security Context Constraints section.
* For more examples of reusable tasks, see the OpenShift Catalog repository. Additionally, you can also see the Tekton Catalog in the Tekton project.
* To install and deploy a custom instance of Tekton Hub for reusable tasks and pipelines, see Using {tekton-hub} with {pipelines-title}.
* For more details on re-encrypt TLS termination, see Re-encryption Termination.
* For more details on secured routes, see the Securing routes section.
