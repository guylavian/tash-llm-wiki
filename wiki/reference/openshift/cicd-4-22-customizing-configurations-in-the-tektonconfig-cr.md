---
title: "Customizing configurations in the TektonConfig custom resource"
type: reference
domain: openshift
slug: cicd-4-22-customizing-configurations-in-the-tektonconfig-cr
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/customizing-configurations-in-the-tektonconfig-cr
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Customizing configurations in the TektonConfig custom resource

[id="customizing-configurations-in-the-tektonconfig-cr"]
= Customizing configurations in the TektonConfig custom resource

In {pipelines-title}, you can customize the following configurations by using the `TektonConfig` custom resource (CR):

* Configuring the {pipelines-title} control plane
* Changing the default service account
* Disabling the service monitor
* Configuring pipeline resolvers
* Disabling cluster tasks and pipeline templates
* Disabling the integration of {tekton-hub}
* Disabling the automatic creation of RBAC resources
* Pruning of task runs and pipeline runs

[id="prerequisites_customizing-configurations-in-the-tektonconfig-cr"]
== Prerequisites

* You have installed the {pipelines-title} Operator.

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-configuring-pipelines-control-plane_{context}"]
= Configuring the {pipelines-title} control plane

You can customize the {pipelines-shortname} control plane by editing the configuration fields in the `TektonConfig` custom resource (CR). The {pipelines-title} Operator automatically adds the configuration fields with their default values so that you can use the {pipelines-shortname} control plane.

.Procedure

. In the *Administrator* perspective of the web console, navigate to *Administration* → *CustomResourceDefinitions*.

. Use the *Search by name* box to search for the `tektonconfigs.operator.tekton.dev` custom resource definition (CRD). Click *TektonConfig* to see the CRD details page.

. Click the *Instances* tab.

. Click the *config* instance to see the `TektonConfig` CR details.

. Click the *YAML* tab.

. Edit the `TektonConfig` YAML file based on your requirements.
+
.Example of `TektonConfig` CR with default values
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    running-in-environment-with-injected-sidecars: true
    metrics.taskrun.duration-type: histogram
    metrics.pipelinerun.duration-type: histogram
    await-sidecar-readiness: true
    params:
      - name: enableMetrics
        value: 'true'
    default-service-account: pipeline
    require-git-ssh-secret-known-hosts: false
    enable-tekton-oci-bundles: false
    metrics.taskrun.level: task
    metrics.pipelinerun.level: pipeline
    enable-api-fields: stable
    enable-provenance-in-status: false
    enable-custom-tasks: true
    disable-creds-init: false
    disable-affinity-assistant: true
----

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-modifiable-fields-with-default-values_{context}"]
= Modifiable fields with default values

The following list includes all modifiable fields with their default values in the `TektonConfig` CR:

* `running-in-environment-with-injected-sidecars` (default: `true`): Set this field to `false` if pipelines run in a cluster that does not use injected sidecars, such as Istio. Setting it to `false` decreases the time a pipeline takes for a task run to start.
+
[NOTE]
====
For clusters that use injected sidecars, setting this field to `false` can lead to an unexpected behavior.
====

* `await-sidecar-readiness` (default: `true`): Set this field to `false` to stop {pipelines-shortname} from waiting for `TaskRun` sidecar containers to run before it begins to operate. This allows tasks to be run in environments that do not support the `downwardAPI` volume type.

* `default-service-account` (default: `pipeline`): This field contains the default service account name to use for the `TaskRun` and `PipelineRun` resources, if none is specified.

* `require-git-ssh-secret-known-hosts` (default: `false`): Setting this field to `true` requires that any Git SSH secret must include the `known_hosts` field.

** For more information about configuring Git SSH secrets, see  _Configuring SSH authentication for Git_ in the _Additional resources_ section.

* `enable-tekton-oci-bundles` (default: `false`): Set this field to `true` to enable the use of an experimental alpha feature named Tekton OCI bundle.

* `enable-api-fields` (default: `stable`): Setting this field determines which features are enabled. Acceptable value is `stable`, `beta`, or `alpha`.
+
[NOTE]
====
{pipelines-title} does not support the `alpha` value.
====

* `enable-provenance-in-status` (default: `false`): Set this field to `true` to enable populating the `provenance` field in `TaskRun` and `PipelineRun` statuses. The `provenance` field contains metadata about resources used in the task run and pipeline run, such as the source from where a remote task or pipeline definition was fetched.

* `enable-custom-tasks` (default: `true`): Set this field to `false` to disable the use of custom tasks in pipelines.

* `disable-creds-init` (default: `false`): Set this field to `true` to prevent {pipelines-shortname} from scanning attached service accounts and injecting any credentials into your steps.

* `disable-affinity-assistant` (default: `true`): Set this field to `false` to enable affinity assistant for each `TaskRun` resource sharing a persistent volume claim workspace.

.Metrics options
You can modify the default values of the following metrics fields in the `TektonConfig` CR:

* `metrics.taskrun.duration-type` and `metrics.pipelinerun.duration-type` (default: `histogram`): Setting these fields determines the duration type for a task or pipeline run. Acceptable value is `gauge` or `histogram`.

* `metrics.taskrun.level` (default: `task`): This field determines the level of the task run metrics. Acceptable value is `taskrun`, `task`, or `namespace`.

* `metrics.pipelinerun.level` (default: `pipeline`): This field determines the level of the pipeline run metrics. Acceptable value is `pipelinerun`, `pipeline`, or `namespace`.

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-optional-configuration-fields_{context}"]
= Optional configuration fields

The following fields do not have a default value, and are considered only if you configure them. By default, the Operator does not add and configure these fields in the `TektonConfig` custom resource (CR).

* `default-timeout-minutes`: This field sets the default timeout for the `TaskRun` and `PipelineRun` resources, if none is specified when creating them. If a task run or pipeline run takes more time than the set number of minutes for its execution, then the task run or pipeline run is timed out and cancelled. For example, `default-timeout-minutes: 60` sets 60 minutes as default.

* `default-managed-by-label-value`: This field contains the default value given to the `app.kubernetes.io/managed-by` label that is applied to all `TaskRun` pods, if none is specified. For example, `default-managed-by-label-value: tekton-pipelines`.

* `default-pod-template`: This field sets the default `TaskRun` and `PipelineRun` pod templates, if none is specified.

* `default-cloud-events-sink`: This field sets the default `CloudEvents` sink that is used for the `TaskRun` and `PipelineRun` resources, if none is specified.

* `default-task-run-workspace-binding`: This field contains the default workspace configuration for the workspaces that a `Task` resource declares, but a `TaskRun` resource does not explicitly declare.

* `default-affinity-assistant-pod-template`: This field sets the default `PipelineRun` pod template that is used for affinity assistant pods, if none is specified.

* `default-max-matrix-combinations-count`: This field contains the default maximum number of combinations generated from a matrix, if none is specified.

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-changing-default-service-account_{context}"]
= Changing the default service account for {pipelines-shortname}

You can change the default service account for {pipelines-shortname} by editing the `default-service-account` field in the `.spec.pipeline` and `.spec.trigger` specifications. The default service account name is `pipeline`.

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    default-service-account: pipeline
  trigger:
    default-service-account: pipeline
    enable-api-fields: stable
----

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-disabling-the-service-monitor_{context}"]
= Disabling the service monitor

You can disable the service monitor, which is part of {pipelines-shortname}, to expose the telemetry data. To disable the service monitor, set the `enableMetrics` parameter to `false` in the `.spec.pipeline` specification of the `TektonConfig` custom resource (CR):

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    params:
       - name: enableMetrics
         value: 'false'
----

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-configuring-pipeline-resolvers_{context}"]
= Configuring pipeline resolvers

You can configure pipeline resolvers in the `TektonConfig` custom resource (CR). You can enable or disable these pipeline resolvers:

* `enable-bundles-resolver`
* `enable-cluster-resolver`
* `enable-git-resolver`
* `enable-hub-resolver`

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    enable-bundles-resolver: true
    enable-cluster-resolver: true
    enable-git-resolver: true
    enable-hub-resolver: true
----

You can also provide resolver specific configurations in the `TektonConfig` CR. For example, define the following fields in the `map[string]string` format to set configurations for each pipeline resolver:

.Example
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  pipeline:
    bundles-resolver-config:
      default-service-account: pipelines
    cluster-resolver-config:
      default-namespace: test
    git-resolver-config:
      server-url: localhost.com
    hub-resolver-config:
      default-tekton-hub-catalog: tekton
----

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-disabling-cluster-tasks-and-pipeline-templates_{context}"]
= Disabling cluster tasks and pipeline templates

By default, the `TektonAddon` custom resource (CR) installs `clusterTasks` and `pipelineTemplates` resources along with {pipelines-shortname} on the cluster.

You can disable installation of the `clusterTasks` and `pipelineTemplates` resources by setting the parameter value to `false` in the `.spec.addon` specification. In addition, you can disable the `communityClusterTasks` parameter.

.Example

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  addon:
    params:
      - name: clusterTasks
        value: 'false'
      - name: pipelineTemplates
        value: 'false'
      - name: communityClusterTasks
        value: 'true'
----

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-disabling-the-integretion-of-tekton-hub_{context}"]
= Disabling the integration of {tekton-hub}

You can disable the integration of {tekton-hub} in the web console *Developer* perspective by setting the `enable-devconsole-integration` parameter to `false` in the `TektonConfig` custom resource (CR).

.Example of disabling {tekton-hub}

[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  hub:
    params:
      - name: enable-devconsole-integration
        value: false
----

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-disabling-automatic-creation-of-rbac-resources_{context}"]
= Disabling the automatic creation of RBAC resources

The default installation of the {pipelines-title} Operator creates multiple role-based access control (RBAC) resources for all namespaces in the cluster, except the namespaces matching the `^(openshift|kube)-*` regular expression pattern. Among these RBAC resources, the `pipelines-scc-rolebinding` security context constraint (SCC) role binding resource is a potential security issue, because the associated `pipelines-scc` SCC has the `RunAsAny` privilege.

To disable the automatic creation of cluster-wide RBAC resources after the {pipelines-title} Operator is installed, cluster administrators can set the `createRbacResource` parameter to `false` in the cluster-level `TektonConfig` custom resource (CR).

.Example `TektonConfig` CR
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  params:
  - name: createRbacResource
    value: "false"
...
----

[WARNING]
====
As a cluster administrator or an user with appropriate privileges, when you disable the automatic creation of RBAC resources for all namespaces, the default `ClusterTask` resource does not work. For the `ClusterTask` resource to function, you must create the RBAC resources manually for each intended namespace.
====

// This module is included in the following assembly:
//
// *openshift_pipelines/customizing-configurations-in-the-tektonconfig-cr.adoc

[id="op-automatic-pruning-taskrun-pipelinerun_{context}"]
= Automatic pruning of task runs and pipeline runs

Stale `TaskRun` and `PipelineRun` objects and their executed instances occupy physical resources that can be used for active runs. For optimal utilization of these resources, {pipelines-title} provides a pruner component that automatically removes unused objects and their instances in various namespaces.

[NOTE]
====
You can configure the pruner for your entire installation by using the `TektonConfig` custom resource and modify configuration for a namespace by using namespace annotations. However, you cannot selectively auto-prune an individual task run or pipeline run in a namespace.
====

// This module is included in the following assembly:
//
// cicd/pipelines/automatic-pruning-taskrun-pipelinerun.adoc

[id="default-pruner-configuration_{context}"]
= Configuring the pruner

You can use the `TektonConfig` custom resource to configure periodic pruning of resources associated with pipeline runs and task runs.

The following example corresponds to the default configuration:

.Example of the pruner configuration
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
# ...
spec:
  pruner:
    resources:
      - taskrun
      - pipelinerun
    keep: 100
    prune-per-resource: false
    schedule: "* 8 * * *"
# ...
----

.Supported parameters for pruner configuration
|===
| Parameter | Description

|`schedule`
|The Cron schedule for running the pruner process. The default schedule runs the process at 08:00 every day. For more information about the Cron schedule syntax, see Cron schedule syntax in the Kubernetes documentation.

|`resources`
|The resource types to which the pruner applies. The available resource types are `taskrun` and `pipelinerun`

|`keep`
|The number of most recent resources of every type to keep.

|`prune-per-resource`
|If set to `false`, the value for the `keep` parameter denotes the total number of task runs or pipeline runs. For example, if `keep` is set to `100`, then the pruner keeps 100 most recent task runs and 100 most recent pipeline runs and removes all other resources.

If set to `true`, the value for the `keep` parameter is calculated separately for pipeline runs referencing each pipeline and for task runs referencing each task. For example, if `keep` is set to `100`, then the pruner keeps 100 most recent pipeline runs for `Pipeline1`, 100 most recent pipeline runs for `Pipeline2`, 100 most recent task runs for `Task1`, and so on, and removes all other resources.

|`keep-since`
|The maximum time for which to keep resources, in minutes. For example, to retain resources which were created not more than five days ago, set `keep-since` to `7200`.
|===

[NOTE]
====
The `keep` and `keep-since` parameters are mutually exclusive. Use only one of them in your configuration.
====

// This module is included in the following assembly:
//
// cicd/pipelines/automatic-pruning-taskrun-pipelinerun.adoc

[id="annotations-for-automatic-pruning-taskruns-pipelineruns_{context}"]
= Annotations for automatically pruning task runs and pipeline runs

To modify the configuration for automatic pruning of task runs and pipeline runs in a namespace, you can set annotations in the namespace.

The following namespace annotations have the same meanings as the corresponding keys in the `TektonConfig` custom resource:

* `operator.tekton.dev/prune.schedule`
* `operator.tekton.dev/prune.resources`
* `operator.tekton.dev/prune.keep`
* `operator.tekton.dev/prune.prune-per-resource`
* `operator.tekton.dev/prune.keep-since`

[NOTE]
====
The `operator.tekton.dev/prune.resources` annotation accepts a comma-separated list. To prune both task runs and pipeline runs, set this annotation to `"taskrun, pipelinerun"`.
====

The following additional namespace annotations are available:

* `operator.tekton.dev/prune.skip`: When set to `true`, the namespace for which the annotation is configured is not pruned.
* `operator.tekton.dev/prune.strategy`: Set the value of this annotation to either `keep` or `keep-since`.

For example, the following annotations retain all task runs and pipeline runs created in the last five days and delete the older resources:

.Example of auto-pruning annotations
[source,yaml]
----
kind: Namespace
apiVersion: v1
# ...
spec:
  annotations:
    operator.tekton.dev/prune.resources: "taskrun, pipelinerun"
    operator.tekton.dev/prune.keep-since: 7200
# ...
----

[role="_additional-resources"]
[id="additional-resources_customizing-configurations-in-the-tektonconfig-cr"]
== Additional resources

* Configuring SSH authentication for Git
* Managing non-versioned and versioned cluster tasks
* Pruning objects to reclaim resources
* Creating pipeline templates in the Administrator perspective
