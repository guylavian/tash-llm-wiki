---
title: "Specifying remote pipelines and tasks using resolvers"
type: reference
domain: openshift
slug: cicd-4-22-remote-pipelines-tasks-resolvers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/remote-pipelines-tasks-resolvers
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Specifying remote pipelines and tasks using resolvers

[id="remote-pipelines-tasks-resolvers"]
= Specifying remote pipelines and tasks using resolvers

Pipelines and tasks are reusable blocks for your CI/CD processes. You can reuse pipelines or tasks that you previously developed, or that were developed by others, without having to copy and paste their definitions. These pipelines or tasks can be available from several types of sources, from other namespaces on your cluster to public catalogs.

In a pipeline run resource, you can specify a pipeline from an existing source. In a pipeline resource or a task run resource, you can specify a task from an existing source.

In these cases, the _resolvers_ in {pipelines-title} retrieve the pipeline or task definition from the specified source at run time.

The following resolvers are available in a default installaton of {pipelines-title}:

Hub resolver:: Retrieves a task or pipeline from the Pipelines Catalog available on {artifact-hub} or {tekton-hub}.
Bundles resolver:: Retrieves a task or pipeline from a Tekton bundle, which is an OCI image available from any OCI repository, such as an OpenShift container repository.
Cluster resolver:: Retrieves a task or pipeline that is already created on the same OpenShift Container Platform cluster in a specific namespace.
Git resolver:: Retrieves a task or pipeline binding from a Git repository. You must specify the repository, the branch, and the path.

[id="resolver-hub_{context}"]
== Specifying a remote pipeline or task from a Tekton catalog
You can use the hub resolver to specify a remote pipeline or task that is defined either in a public Tekton catalog of {artifact-hub} or in an instance of {tekton-hub}.

[IMPORTANT]
====
The {artifact-hub} project is not supported with {pipelines-title}. Only the configuration of {artifact-hub} is supported.
====

// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-hub-config_{context}"]
= Configuring the hub resolver

You can change the default hub for pulling a resource, and the default catalog settings, by configuring the hub resolver.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
. In the `TektonConfig` custom resource, edit the `pipeline.hub-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    hub-resolver-config:
      default-tekton-hub-catalog: Tekton # <1>
      default-artifact-hub-task-catalog: tekton-catalog-tasks # <2>
      default-artifact-hub-pipeline-catalog: tekton-catalog-pipelines # <3>
      defailt-kind: pipeline # <4>
      default-type: tekton # <5>
      tekton-hub-api: "https://my-custom-tekton-hub.example.com" # <6>
      artifact-hub-api: "https://my-custom-artifact-hub.example.com" # <7>
----
<1> The default {tekton-hub} catalog for pulling a resource.
<2> The default {artifact-hub} catalog for pulling a task resource.
<3> The default {artifact-hub} catalog for pulling a pipeline resource.
<4> The default object kind for references.
<5> The default hub for pulling a resource, either `artifact` for {artifact-hub} or `tekton` for {tekton-hub}.
<6> The {tekton-hub} API used, if the `default-type` option is set to `tekton`.
<7> Optional: The {artifact-hub} API used, if the `default-type` option is set to `artifact`.
+
[IMPORTANT]
====
If you set the `default-type` option to `tekton`, you must configure your own instance of the {tekton-hub} by setting the `tekton-hub-api` value.

If you set the `default-type` option to `artifact` then the resolver uses the public hub API at https://artifacthub.io/ by default. You can configure your own {artifact-hub} API by setting the `artifact-hub-api` value.
====
// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-hub-specify_{context}"]
= Specifying a remote pipeline or task using the hub resolver

When creating a pipeline run, you can specify a remote pipeline from {artifact-hub} or {tekton-hub}. When creating a pipeline or a task run, you can specify a remote task from {artifact-hub} or {tekton-hub}.

.Procedure

* To specify a remote pipeline or task from {artifact-hub} or {tekton-hub}, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: hub
  params:
  - name: catalog
    value: <catalog>
  - name: type
    value: <catalog_type>
  - name: kind
    value: [pipeline|task]
  - name: name
    value: <resource_name>
  - name: version
    value: <resource_version>
# ...
----
+
.Supported parameters for the hub resolver
|===
| Parameter | Description | Example value

| `catalog`
| The catalog for pulling the resource.
| Default:  `tekton-catalog-tasks` (for the `task` kind);  `tekton-catalog-pipelines` (for the `pipeline` kind).

| `type`
| The type of the catalog for pulling the resource. Either `artifact` for {artifact-hub} or `tekton` for {tekton-hub}.
| Default:  `artifact`

| `kind`
| Either `task` or `pipeline`.
| Default: `task`

| `name`
| The name of the task or pipeline to fetch from the hub.
| `golang-build`

| `version`
| The version of the task or pipeline to fetch from the hub. You must use quotes (`"`) around the number.
| `"0.5.0"`
|===
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from a catalog:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: hub-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: hub
    params:
    - name: catalog
      value: tekton-catalog-pipelines
    - name: type
      value: artifact
    - name: kind
      value: pipeline
    - name: name
      value: example-pipeline
    - name: version
      value: "0.1"
    - name: sample-pipeline-parameter
      value: test
----

The following example pipeline that references a remote task from a catalog:

[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-with-cluster-task-reference-demo
spec:
  tasks:
  - name: "cluster-task-reference-demo"
    taskRef:
      resolver: hub
      params:
      - name: catalog
        value: tekton-catalog-tasks
      - name: type
        value: artifact
      - name: kind
        value: task
      - name: name
        value: example-task
      - name: version
        value: "0.6"
      - name: sample-task-parameter
        value: test
----

The following example task run that references a remote task from a catalog:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: cluster-task-reference-demo
spec:
  taskRef:
    resolver: hub
    params:
    - name: catalog
      value: tekton-catalog-tasks
    - name: type
      value: artifact
    - name: kind
      value: task
    - name: name
      value: example-task
    - name: version
      value: "0.6"
    - name: sample-task-parameter
      value: test
----

[id="resolver-bundles_{context}"]
== Specifying a remote pipeline or task from a Tekton bundle

You can use the bundles resolver to specify a remote pipeline or task from a Tekton bundle. A Tekton bundle is an OCI image available from any OCI repository, such as an OpenShift container repository.

// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-bundles-config_{context}"]
= Configuring the bundles resolver

You can change the default service account name and the default kind for pulling resources from a Tekton bundle by configuring the bundles resolver.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
+
. In the `TektonConfig` custom resource, edit the `pipeline.bundles-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    bundles-resolver-config:
      default-service-account: pipelines # <1>
      default-kind: task # <2>
----
<1> The default service account name to use for bundle requests.
<2> The default layer kind in the bundle image.
// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-bundles-specify_{context}"]
= Specifying a remote pipeline or task using the bundles resolver

When creating a pipeline run, you can specify a remote pipeline from a Tekton bundle. When creating a pipeline or a task run, you can specify a remote task from a Tekton bundle.

.Procedure

* To specify a remote pipeline or task from a Tekton bundle, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: bundles
  params:
  - name: bundle
    value: <fully_qualified_image_name>
  - name: name
    value: <resource_name>
  - name: kind
    value: [pipeline|task]
# ...
----
+
.Supported parameters for the bundles resolver
|===
| Parameter | Description | Example value

| `serviceAccount`
| The name of the service account to use when constructing registry credentials.
| `default`

| `bundle`
| The bundle URL pointing at the image to fetch.
| `gcr.io/tekton-releases/catalog/upstream/golang-build:0.1`

| `name`
| The name of the resource to pull out of the bundle.
| `golang-build`

| `kind`
| The kind of the resource to pull out of the bundle.
| `task`
|===
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from a Tekton bundle:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: bundle-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: bundles
    params:
    - name: bundle
      value: registry.example.com:5000/simple/pipeline:latest
    - name: name
      value: hello-pipeline
    - name: kind
      value: pipeline
    - name: sample-pipeline-parameter
      value: test
  params:
  - name: username
    value: "pipelines"
----

The following example pipeline references a remote task from a Tekton bundle:

[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-with-bundle-task-reference-demo
spec:
  tasks:
  - name: "bundle-task-demo"
    taskRef:
      resolver: bundles
      params:
      - name: bundle
        value: registry.example.com:5000/advanced/task:latest
      - name: name
        value: hello-world
      - name: kind
        value: task
      - name: sample-task-parameter
        value: test
----

The following example task run references a remote task from a Tekton bundle:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: bundle-task-reference-demo
spec:
  taskRef:
    resolver: bundles
    params:
    - name: bundle
      value: registry.example.com:5000/simple/new_task:latest
    - name: name
      value: hello-world
    - name: kind
      value: task
    - name: sample-task-parameter
      value: test
----

[id="resolver-cluster_{context}"]
== Specifying a remote pipeline or task from the same cluster

You can use the cluster resolver to specify a remote pipeline or task that is defined in a namespace on the OpenShift Container Platform cluster where {pipelines-title} is running.

// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-cluster-config_{context}"]
= Configuring the cluster resolver

You can change the default kind and namespace for the cluster resolver, or limit the namespaces that the cluster resolver can use.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
+
. In the `TektonConfig` custom resource, edit the `pipeline.cluster-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    cluster-resolver-config:
      default-kind: pipeline # <1>
      default-namespace: namespace1 # <2>
      allowed-namespaces: namespace1, namespace2 # <3>
      blocked-namespaces: namespace3, namespace4 # <4>
----
<1> The default resource kind to fetch, if not specified in parameters.
<2> The default namespace for fetching resources, if not specified in parameters.
<3> A comma-separated list of namespaces that the resolver is allowed to access. If this key is not defined, all namespaces are allowed.
<4> An optional comma-separated list of namespaces which the resolver is blocked from accessing. If this key is not defined, all namespaces are allowed.
// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-cluster-specify_{context}"]
= Specifying a remote pipeline or task using the cluster resolver

When creating a pipeline run, you can specify a remote pipeline from the same cluster. When creating a pipeline or a task run, you can specify a remote task from the same cluster.

.Procedure

* To specify a remote pipeline or task from the same cluster, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: cluster
  params:
  - name: name
    value: <name>
  - name: namespace
    value: <namespace>
  - name: kind
    value: [pipeline|task]
# ...
----
+
.Supported parameters for the cluster resolver
|===
| Parameter | Description | Example value

| `name`
| The name of the resource to fetch.
| `some-pipeline`

| `namespace`
| The namespace in the cluster containing the resource.
| `other-namespace`

| `kind`
| The kind of the resource to fetch.
| `pipeline`

|===
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from the same cluster:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: cluster-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: cluster
    params:
    - name: name
      value: some-pipeline
    - name: namespace
      value: test-namespace
    - name: kind
      value: pipeline
    - name: sample-pipeline-parameter
      value: test
----

The following example pipeline references a remote task from the same cluster:

[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-with-cluster-task-reference-demo
spec:
  tasks:
  - name: "cluster-task-reference-demo"
    taskRef:
      resolver: cluster
      params:
      - name: name
        value: some-task
      - name: namespace
        value: test-namespace
      - name: kind
        value: task
      - name: sample-task-parameter
        value: test
----

The following example task run references a remote task from the same cluster:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: cluster-task-reference-demo
spec:
  taskRef:
    resolver: cluster
    params:
    - name: name
      value: some-task
    - name: namespace
      value: test-namespace
    - name: kind
      value: task
    - name: sample-task-parameter
      value: test
----

[id="resolver-git_{context}"]
== Specifying a remote pipeline or task from a Git repository

You can use the Git resolver to specify a remote pipeline or task from a Git repostory. The repository must contain a YAML file that defines the pipeline or task. The Git resolver can access a repository either by cloning it anonymously or else by using the authenticated SCM API.

// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-git-config-anon_{context}"]
= Configuring the Git resolver for anonymous Git cloning

If you want to use anonymous Git cloning, you can configure the default Git revision, fetch timeout, and default repository URL for pulling remote pipelines and tasks from a Git repository.

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----
. In the `TektonConfig` custom resource, edit the `pipeline.git-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    git-resolver-config:
      default-revision: main # <1>
      fetch-timeout: 1m # <2>
      default-url: https://github.com/tektoncd/catalog.git # <3>
----
<1> The default Git revision to use if none is specified.
<2> The maximum time any single Git clone resolution may take, for example, `1m`, `2s`, `700ms`. {pipelines-title} also enforces a global maximum timeout of 1 minute on all resolution requests.
<3> The default Git repository URL for anonymous cloning if none is specified.
// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-git-config-scm_{context}"]
= Configuring the Git resolver for the authenticated SCM API

For the authenticated SCM API, you must set the configuration for the authenticated Git connection.

You can use Git repository providers that are supported by the `go-scm` library. Not all `go-scm` implementations have been tested with the Git resolver, but the following providers are known to work:

* `github.com` and GitHub Enterprise
* `gitlab.com` and self-hosted Gitlab
* Gitea
* BitBucket Server
* BitBucket Cloud

[NOTE]
====
* You can configure only one Git connection using the authenticated SCM API for your cluster. This connection becomes available to all users of the cluster. All users of the cluster can access the repository using the security token that you configure for the connection.

* If you configure the Git resolver to use the authenticated SCM API, you can also use anonymous Git clone references to retrieve pipelines and tasks.
====

.Procedure

. To edit the `TektonConfig` custom resource, enter the following command:
+
[source,terminal]
----
$ oc edit TektonConfig config
----

. In the `TektonConfig` custom resource, edit the `pipeline.git-resolver-config` spec:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    git-resolver-config:
      default-revision: main # <1>
      fetch-timeout: 1m # <2>
      scm-type: github # <3>
      server-url: api.internal-github.com # <4>
      api-token-secret-name: github-auth-secret # <5>
      api-token-secret-key: github-auth-key # <6>
      api-token-secret-namespace: github-auth-namespace # <7>
      default-org: tektoncd # <8>
----
<1> The default Git revision to use if none is specified.
<2> The maximum time any single Git clone resolution may take, for example, `1m`, `2s`, `700ms`. {pipelines-title} also enforces a global maximum timeout of 1 minute on all resolution requests.
<3> The SCM provider type.
<4> The base URL for use with the authenticated SCM API. This setting is not required if you are using `github.com`, `gitlab.com`, or BitBucket Cloud.
<5> The name of the secret that contains the SCM provider API token.
<6> The key within the token secret that contains the token.
<7> The namespace containing the token secret, if not `default`.
<8> Optional: The default organization for the repository, when using the authenticated API. This organization is used if you do not specify an organization in the resolver parameters.

[NOTE]
====
The `scm-type`, `api-token-secret-name`, and `api-token-secret-key` settings are required to use the authenticated SCM API.
====
// This module is included in the following assembly:
//
// // *openshift_pipelines/remote-pipelines-tasks-resolvers.adoc

[id="resolver-git-specify_{context}"]
= Specifying a remote pipeline or task using the Git resolver

When creating a pipeline run, you can specify a remote pipeline from a Git repository. When creating a pipeline or a task run, you can specify a remote task from a Git repository.

.Prerequisites

* If you want to use the authenticated SCM API, you must configure the authenticated Git connection for the Git resolver.

.Procedure

. To specify a remote pipeline or task from a Git repository, use the following reference format in the `pipelineRef` or `taskRef` spec:
+
[source,yaml]
----
# ...
  resolver: git
  params:
  - name: url
    value: <git_repository_url>
  - name: revision
    value: <branch_name>
  - name: pathInRepo
    value: <path_in_repository>
# ...
----
+
.Supported parameters for the Git resolver
|===
| Parameter | Description | Example value

| `url`
| The URL of the repository, when using anonymous cloning.
| `+https://github.com/tektoncd/catalog.git+`

| `repo`
| The repository name, when using the authenticated SCM API.
| `test-infra`

| `org`
| The organization for the repository, when using the authenticated SCM API.
| `tektoncd`

| `revision`
| The Git revision in the repository. You can specify a branch name, a tag  name, or a commit SHA hash.
| `aeb957601cf41c012be462827053a21a420befca` +
`main` +
`v0.38.2`

| `pathInRepo`
| The path name of the YAML file in the repository.
| `task/golang-build/0.3/golang-build.yaml`
|===
+
[NOTE]
====
To clone and fetch the repository anonymously, use the `url` parameter. To use the authenticated SCM API, use the `repo` parameter. Do not specify the `url` parameter and the `repo` parameter together.
====
+
If the pipeline or task requires additional parameters, provide these parameters in `params`.

The following example pipeline run references a remote pipeline from a Git repository:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: PipelineRun
metadata:
  name: git-pipeline-reference-demo
spec:
  pipelineRef:
    resolver: git
    params:
    - name: url
      value: https://github.com/tektoncd/catalog.git
    - name: revision
      value: main
    - name: pathInRepo
      value: pipeline/simple/0.1/simple.yaml
    - name: sample-pipeline-parameter
      value: test
  params:
  - name: name
    value: "testPipelineRun"
----

The following example pipeline references a remote task from a Git repository:

[source,yaml]
----
apiVersion: tekton.dev/v1
kind: Pipeline
metadata:
  name: pipeline-with-git-task-reference-demo
spec:
  tasks:
  - name: "git-task-reference-demo"
    taskRef:
      resolver: git
      params:
      - name: url
        value: https://github.com/tektoncd/catalog.git
      - name: revision
        value: main
      - name: pathInRepo
        value: task/git-clone/0.6/git-clone.yaml
      - name: sample-task-parameter
        value: test
----

The following example task run references a remote task from a Git repository:

[source,yaml]
----
apiVersion: tekton.dev/v1beta1
kind: TaskRun
metadata:
  name: git-task-reference-demo
spec:
  taskRef:
    resolver: git
    params:
    - name: url
      value: https://github.com/tektoncd/catalog.git
    - name: revision
      value: main
    - name: pathInRepo
      value: task/git-clone/0.6/git-clone.yaml
    - name: sample-task-parameter
      value: test
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Using Tekton Hub with {pipelines-shortname}
