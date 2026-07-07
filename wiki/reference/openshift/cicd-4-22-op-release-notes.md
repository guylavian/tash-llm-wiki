---
title: "{pipelines-title} release notes"
type: reference
domain: openshift
slug: cicd-4-22-op-release-notes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/op-release-notes
version: 4.22
family: cicd
documentKind: "Documentation"
---

# {pipelines-title} release notes

//OpenShift Pipelines Release Notes
[id="op-release-notes"]
= {pipelines-title} release notes

{pipelines-title} is a cloud-native CI/CD experience based on the Tekton project which provides:

* Standard Kubernetes-native pipeline definitions (CRDs).
* Serverless pipelines with no CI server management overhead.
* Extensibility to build images using any Kubernetes tool, such as S2I, Buildah, JIB, and Kaniko.
* Portability across any Kubernetes distribution.
* Powerful CLI for interacting with pipelines.
* Integrated user experience with the *Developer* perspective of the OpenShift Container Platform web console.

For an overview of {pipelines-title}, see Understanding {pipelines-shortname}.

[id="compatibility-support-matrix_{context}"]
= Compatibility and support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

In the table, features are marked with the following statuses:

[horizontal]
TP:: Technology Preview
GA:: General Availability

// Writer, see http://dashboard.apps.cicd.ospqa.com/releases/componentmatrix/

.Compatibility and support matrix
[options="header"]
|===

| {pipelines-title} Version 7+| Component Version | OpenShift Version | Support Status

| Operator | Pipelines | Triggers | CLI | Chains | Hub | {pac} | Results | |
|1.11 | 0.47.x | 0.24.x | 0.31.x | 0.16.x (GA) | 1.13.x (TP) | 0.19.x (GA) | 0.6.x (TP) | 4.12, 4.13, 4.14 (planned)  | GA

|1.10 | 0.44.x | 0.23.x | 0.30.x | 0.15.x (TP) | 1.12.x (TP) | 0.17.x (GA) | NA | 4.10, 4.11, 4.12, 4.13  | GA

|1.9 | 0.41.x | 0.22.x | 0.28.x | 0.13.x (TP) | 1.11.x (TP) | 0.15.x (GA) | NA | 4.10, 4.11, 4.12, 4.13  | GA

|1.8 | 0.37.x | 0.20.x | 0.24.x | 0.9.0 (TP) | 1.8.x (TP) | 0.10.x (TP) | NA | 4.10, 4.11, 4.12 | GA

|1.7 | 0.33.x | 0.19.x | 0.23.x | 0.8.0 (TP) | 1.7.0 (TP) | 0.5.x (TP) | NA | 4.9, 4.10, 4.11 | GA

|1.6 | 0.28.x | 0.16.x | 0.21.x | NA | NA | NA | NA | 4.9 | GA

|1.5 | 0.24.x | 0.14.x (TP) | 0.19.x | NA | NA | NA | NA |4.8 | GA

|1.4 | 0.22.x | 0.12.x (TP) | 0.17.x | NA | NA | NA | NA | 4.7 | GA

|===

For questions and feedback, you can send an email to the product team at pipelines-interest@redhat.com.

// Modules included, most to least recent
// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc
[id="op-release-notes-1-11_{context}"]
= Release notes for {pipelines-title} General Availability 1.11

With this update, {pipelines-title} General Availability (GA) 1.11 is available on OpenShift Container Platform 4.12 and later versions.

[id="new-features-1-11_{context}"]
== New features

In addition to fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.11:

[NOTE]
====
Before upgrading to the {pipelines-title} Operator 1.11, ensure that you have at least installed the OpenShift Container Platform 4.12.19 or 4.13.1 version on your cluster.
====

[id="pipelines-new-features-1-11_{context}"]
=== Pipelines

* With this update, you can use {pipelines-title} on the OpenShift Container Platform cluster that runs on ARM hardware. You have support for the `ClusterTask` resources where images are available and the Tekton CLI tool on ARM hardware.

* This update adds support for results, object parameters, array results, and indexing into an array when you set the `enable-api-fields` feature flag to `beta` value in the `TektonConfig` CR.

* With this update, propagated parameters are now part of a stable feature. This feature enables interpolating parameters in embedded specifications to reduce verbosity in Tekton resources.

* With this update, propagated workspaces are now part of a stable feature. You can enable the propagated workspaces feature by setting the `enable-api-fields` feature flag to `alpha` or `beta` value.

* With this update, the `TaskRun` object fetches and displays the init container failure message to users when a pod fails to run.

* With this update, you can replace parameters, results, and the context of a pipeline task while configuring a matrix as per the following guidelines:
** Replace an array with an `array` parameter or a string with a `string`, `array`, or `object` parameter in the `matrix.params` configuration.
** Replace a string with a `string`, `array`, or `object` parameter in the `matrix.include` configuration.
** Replace the context of a pipeline task with another context in the `matrix.include` configuration.

* With this update, the `TaskRun` resource validation process also validates the `matrix.include` parameters. The validation checks whether all parameters have values and match the specified type, and object parameters have all the keys required.

* This update adds a new `default-resolver-type` field in the `default-configs` config map. You can set the value of this field to configure a default resolver.

* With this update, you can define and use a `PipelineRun` context variable in the `pipelineRun.workspaces.subPath` configuration.

* With this update, the `ClusterResolver`, `BundleResolver`, `HubResolver`, and `GitResolver` features are now available by default.

[id="triggers-new-features-1-11_{context}"]
=== Triggers

* With this update, Tekton Triggers support the `Affinity` and `TopologySpreadConstraints` values in the `EventListener` specification. You can use these values to configure Kubernetes and custom resources for an `EventListener` object.
* This update adds a Slack interceptor that allows you to extract fields by using a slash command in Slack. The extracted fields are sent in the form data section of an HTTP request.

[id="operator-new-features-1-11_{context}"]
=== Operator

* With this update, you can configure pruning for each `PipelineRun` or `TaskRun` resource by setting a `prune-per-resource` boolean field in the `TektonConfig` CR. You can also configure pruning for each `PipelineRun` or `TaskRun` resource in a  namespace by adding the `operator.tekton.dev/prune.prune-per-resource=true` annotation to that namespace.

* With this update, if there are any changes in the OpenShift Container Platform cluster-wide proxy, Operator Lifecycle Manager (OLM) recreates the {pipelines-title} Operator.
* With this update, you can disable the pruner feature by setting the value of the `config.pruner.disabled` field to `true` in the `TektonConfig` CR.

[id="chains-new-features-1-11_{context}"]
=== {tekton-chains}

* With this update, {tekton-chains} is now generally available for use.

* With this update, you can use the skopeo tool with {tekton-chains} to generate keys, which are used in the `cosign` signing scheme.

* When you upgrade to the {pipelines-title} Operator 1.11, the previous {tekton-chains} configuration will be overwritten and you must set it again in the `TektonConfig` CR.

[id="tekton-hub-new-features-1-11_{context}"]
=== {tekton-hub}

* This update adds a new `resource/<catalog_name>/<kind>/<resource_name>/raw` endpoint and a new `resourceURLPath` field in the `resource` API response. This update helps you to obtain the latest raw YAML file of the resource.

[id="tekton-results-new-features-1-11_{context}"]
=== Tekton Results

* This update adds Tekton Results to the Tekton Operator as an optional component.

[id="pac-new-features-1-11_{context}"]
=== {pac}

* With this update, {pac} allows you to expand a custom parameter within your `PipelineRun` resource by using the `params` field. You can specify a value for the custom parameter inside the template of the `Repository` CR. The specified value replaces the custom parameter in your pipeline run. Also, you can define a custom parameter and use its expansion only when specified conditions are compatible with a Common Expression Language (CEL) filter.

* With this update, you can either rerun a specific pipeline or all pipelines by clicking the *Re-run all checks* button in the *Checks* tab of the GitHub interface.

* This update adds a new `tkn pac info` command to the {pac} CLI. As an administrator, you can use the `tkn pac info` command to obtain the following details about the {pac} installation:
** The location where {pac} is installed.
** The version number of {pac}.
** An overview of the `Repository` CR created on the cluster and the URL associated with the repository.
** Details of any installed GitHub applications.
+
With this command, you can also specify a custom GitHub API URL by using the `--github-api-url` argument.

* This update enables error detection for all `PipelineRun` resources by default. {pac} detects if a `PipelineRun` resource execution has failed and shows a snippet of the last few lines of the error. For a GitHub application, {pac} detects error messages in the container logs and exposes them as annotations on a pull request.

* With this update, you can fetch tasks from a private {tekton-hub} instance attached to a private Git repository. To enable this update, {pac} uses the internal raw URL of the private {tekton-hub} instance instead of using the GitHub raw URL.

* Before this update, {pac} provided logs that would not include the namespace detail. With this update, {pac} adds the namespace information to the pipeline logs so that you can filter them based on a namespace and debug easily.

* With this update, you can define the provenance source from where the `PipelineRun` resource definition is to be fetched. By default, {pac} fetches the `PipelineRun` resource definition from the branch where the event has been triggered. Now, you can configure the value of the `pipelinerun_provenance` setting to `default_branch` so that the `PipelineRun` resource definition is fetched from the default branch of the repository as configured on GitHub.

* With this update, you can extend the scope of the GitHub token at the following levels:
** Repository-level: Use this level to extend the scope to the repositories that exist in the same namespace in which the original repository exists.
** Global-level: Use this level to extend the scope to the repositories that exist in a different namespace.

* With this update, {pac} triggers a CI pipeline for a pull request created by a user who is not an owner, collaborator, or public member or is not listed in the `owner` file but has permission to push changes to the repository.

* With this update, the custom console setting allows you to use custom parameters from a `Repository` CR.

* With this update, {pac} changes all `PipelineRun` labels to `PipelineRun` annotations. You can use a `PipelineRun` annotation to mark a Tekton resource, instead of using a `PipelineRun` label.

* With this update, you can use the `pac-config-logging` config map for watcher and webhook resources, but not for the {pac} controller.

[id="breaking-changes-1-11_{context}"]
== Breaking changes

* This update replaces the `resource-verification-mode` feature flag with a new `trusted-resources-verification-no-match-policy` flag in the pipeline specification.

* With this update, you cannot edit the {tekton-chains} CR. Instead, edit the `TektonConfig` CR to configure {tekton-chains}.

[id="deprecated-features-1-11_{context}"]
== Deprecated and removed features

* This update removes support for the `PipelineResource` commands and references from Tekton CLI:
** Removal of pipeline resources from cluster tasks
** Removal of pipeline resources from tasks
** Removal of pipeline resources from pipelines
** Removal of resource commands
** Removal of input and output resources from the `clustertask describe` command

* This update removes support for the `full` embedded status from Tekton CLI.

* The `taskref.bundle` and `pipelineref.bundle` bundles are deprecated and will be removed in a future release.

* In {pipelines-title} 1.11, support for the `PipelineResource` CR has been removed, use the `Task` CR instead.

* In {pipelines-title} 1.11, support for the `v1alpha1.Run` objects has been removed. You must upgrade the objects from `v1alpha1.Run` to `v1beta1.CustomRun` before upgrading to this release.

* In {pipelines-title} 1.11, the `custom-task-version` feature flag has been removed.

* In {pipelines-title} 1.11, the `pipelinerun.status.taskRuns` and `pipelinerun.status.runs` fields have been removed along with the `embedded-status` feature flag. Use the `pipelinerun.status.childReferences` field instead.

[id="known-issues-1-11_{context}"]
== Known issues

* Setting the `prune-per-resource` boolean field does not delete `PipelineRun` or `TaskRun` resources if they were not part of any pipeline or task.

* Tekton CLI does not show logs of the `PipelineRun` resources that are created by using resolvers.

* When you filter your pipeline results based on the `order_by=created_time+desc&page_size=1` query, you get zero records without any `nextPageToken` value in the output.

* When you set the value of the `loglevel.pipelinesascode` field to `debug`, no debugging logs are generated in the {pac} controller pod. As a workaround, restart the {pac} controller pod.

[id="fixed-issues-1-11_{context}"]
== Fixed issues

* Before this update, {pac} failed to create a `PipelineRun` resource while detecting the `generateName` field in the `PipelineRun` CR. With this update, {pac} supports providing the `generateName` field in the `PipelineRun` CR.

* Before this update, when you created a `PipelineRun` resource from the web console, all annotations would be copied from the pipeline, causing issues for the running nodes. This update now resolves the issue.

* This update fixes the `tkn pr delete` command for the `keep` flag. Now, if the value of the `keep` flag is equal to the number of the associated task runs or pipeline runs, then the command returns the exit code `0` along with a message.

* Before this update, the Tekton Operator did not expose the performance configuration fields for any customizations. With this update, as a cluster administrator, you can customize the following performance configuration fields in the `TektonConfig` CR based on your needs:
** `disable-ha`
** `buckets`
** `kube-api-qps`
** `kube-api-burst`
** `threads-per-controller`

* This update fixes the remote bundle resolver to perform a case-insensitive comparison of the `kind` field with the `dev.tekton.image.kind` annotation value in the bundle.

* Before this update, pods for remote resolvers were terminated because of insufficient memory when you would clone a large Git repository. This update fixes the issue and increases the memory limit for deploying remote resolvers.

* With this update, task and pipeline resources of `v1` type are supported in remote resolution.

* This update reverts the removal of embedded `TaskRun` status from the API.  The embedded `TaskRun` status is now available as a deprecated feature to support compatibility with older versions of the client-server.

* Before this update, all annotations were merged into `PipelineRun` and `TaskRun` resources even if they were not required for the execution. With this update, when you merge annotations into `PipelineRun` and `TaskRun` resources, the `last-applied-configuration` annotation is skipped.

* This update fixes a regression issue and prevents the validation of a skipped task result in pipeline results. For example, if the pipeline result references a skipped `PipelineTask` resource, then the pipeline result is not emitted and the `PipelineRun` execution does not fail due to a missing result.

* This update uses the pod status message to determine the cause of a pod termination.

* Before this update, the default resolver was not set for the execution of the `finally` tasks. This update sets the default resolver for the `finally` tasks.

* With this update, {pipelines-title} avoids occasional failures of the `TaskRun` or `PipelineRun` execution when you use remote resolution.

* Before this update, a long pipeline run would be stuck in the running state on the cluster, even after the timeout. This update fixes the issue.

* This update fixes the `tkn pr delete` command for correctly using the `keep` flag. With this update, if the value of the `keep` flag equals the number of associated task runs or pipeline runs, the `tkn pr delete` command returns exit code `0` along with a message.

[id="release-notes-1-11-1_{context}"]
== Release notes for {pipelines-title} General Availability 1.11.1

With this update, {pipelines-title} General Availability (GA) 1.11.1 is available on OpenShift Container Platform 4.12 and later versions.

[id="fixed-issues-1-11-1_{context}"]
=== Fixed issues

* Before this update, a task run could fail with a mount path error message, when a running or pending pod was preempted. With this update, a task run does not fail when the cluster causes a pod to be deleted and re-created.

* Before this update, a shell script in a task had to be run as root. With this update, the shell script image has the non-root user ID set so that you can run a task that includes a shell script, such as the `git-clone` task, as a non-root user within the pod.

* Before this update, in {pipelines-title} 1.11.0, when a pipeline run is defined using {pac}, the definition in the Git repository references the `tekton.dev/v1beta1` API version and includes a `spec.pipelineRef.bundle` entry, the `kind` parameter for the bundle reference was wrongly set to `Task`. The issue did not exist in earlier versions of {pipelines-title}. With this update, the `kind` parameter is set correctly.

* Before this update, the `disable-ha` flag was not correctly passed to the `tekton-pipelines` controller, so the High Availability (HA) feature of {pipelines-title} could not be enabled. With this update, the `disable-ha` flag  is correctly passed and you can enable the HA feature as required.

* Before this update, you could not set the URL for {tekton-hub} and {artifact-hub} for the hub resolver, so you could use only the preset addresses of {tekton-hub} and {artifact-hub}. With this update, you can configure the URL for {tekton-hub} and {artifact-hub} for the hub resolver, for example, to use a custom {tekton-hub} instance that you installed.

* With this update, the SHA digest of the `git-init` image corresponds to version 1.10.5, which is the current released version of the image.

* Before this update, the `tekton-pipelines-controller` component used a config map named `config-leader-election`. This name is the default value for knative controllers, so the configuration process for {pipelines-shortname} could affect other controllers and vice versa. With this update, the component uses a unique config name, so the configuration process for {pipelines-shortname} does not affect other controllers and is not affected by other controllers.

* Before this update, when a user without write access to a GitHub repository opened a pull request, {pac} CI/CD actions would show as `skipped` in GitHub. With this update, {pac} CI/CD actions are shown as `Pending approval` in GitHub.

* Before this update, {pac} ran CI/CD actions for every pull request into a branch that matched a configured branch name. With this update, {pac} runs CI/CD actions only when the source branch of the pull request matches the exact configured branch name.

* Before this update, metrics for the {pac} controller were not visible in the OpenShift Container Platform developer console. With this update, metrics for the {pac} controller are displayed in the developer console.

* Before this update, in {pipelines-title} 1.11.0, the Operator always installed {tekton-chains} and you could not disable installation of the {tekton-chains} component. With this update, you can set the value of the `disabled` parameter to `true` in the `TektonConfig` CR  to disable installation okindf {tekton-chains}.

* Before this update, if you configured {tekton-chains} on an older version of {pipelines-shortname} using the `TektonChain` CR and then upgraded to {pipelines-shortname} version 1.11.0, the configuration information was overwritten. With this update, if you upgrade from an older version of {pipelines-shortname} and {tekton-chains} was configured in the same namespace where the `TektonConfig` is installed (`openshift-pipelines`), {tekton-chains} configuration information is preserved.

// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc
[id="op-release-notes-1-10_{context}"]
= Release notes for {pipelines-title} General Availability 1.10

With this update, {pipelines-title} General Availability (GA) 1.10 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="new-features-1-10_{context}"]
== New features

In addition to fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.10.

[id="pipelines-new-features-1-10_{context}"]
=== Pipelines

* With this update, you can specify environment variables in a `PipelineRun` or `TaskRun` pod template to override or append the variables that are configured in a task or step. Also, you can specify environment variables in a default pod template to use those variables globally for all `PipelineRuns` and `TaskRuns`. This update also adds a new default configuration named `forbidden-envs` to filter environment variables while propagating from pod templates.
* With this update, custom tasks in pipelines are enabled by default.
+
[NOTE]
====
To disable this update, set the `enable-custom-tasks` flag to `false` in the `feature-flags` config custom resource.
====

* This update supports the `v1beta1.CustomRun` API version for custom tasks.
* This update adds support for the `PipelineRun` reconciler to create a custom run. For example, custom `TaskRuns` created from `PipelineRuns` can now use the `v1beta1.CustomRun` API version instead of `v1alpha1.Run`, if the `custom-task-version` feature flag is set to `v1beta1`, instead of the default value `v1alpha1`.
+
[NOTE]
====
You need to update the custom task controller to listen for the `*v1beta1.CustomRun` API version instead of `*v1alpha1.Run` in order to respond to `v1beta1.CustomRun` requests.
====

* This update adds a new `retries` field to the `v1beta1.TaskRun` and `v1.TaskRun` specifications.

[id="triggers-new-features-1-10_{context}"]
=== Triggers

* With this update, triggers support the creation of `Pipelines`, `Tasks`, `PipelineRuns`, and `TaskRuns` objects of the `v1` API version along with `CustomRun` objects of the `v1beta1` API version.
* With this update, GitHub Interceptor blocks a pull request trigger from being executed unless invoked by an owner or with a configurable comment by an owner.
+
[NOTE]
====
To enable or disable this update, set the value of the `githubOwners` parameter to `true` or `false` in the GitHub Interceptor configuration file.
====

* With this update, GitHub Interceptor has the ability to add a comma delimited list of all files that have changed for the push and pull request events. The list of changed files is added to the `changed_files` property of the event payload in the top-level extensions field.
* This update changes the `MinVersion` of TLS to `tls.VersionTLS12` so that triggers run on OpenShift Container Platform when the Federal Information Processing Standards (FIPS) mode is enabled.

[id="cli-new-features-1-10_{context}"]
=== CLI

* This update adds support to pass a Container Storage Interface (CSI) file as a workspace at the time of starting a `Task`, `ClusterTask` or `Pipeline`.
* This update adds `v1` API support to all CLI commands associated with task, pipeline, pipeline run, and task run resources. Tekton CLI works with both `v1beta1` and `v1` APIs for these resources.
* This update adds support for an object type parameter in the `start` and `describe` commands.

[id="operator-new-features-1-10_{context}"]
=== Operator

* This update adds a `default-forbidden-env` parameter in optional pipeline properties. The parameter includes forbidden environment variables that should not be propagated if provided through pod templates.
* This update adds support for custom logos in Tekton Hub UI. To add a custom logo, set the value of the `customLogo` parameter to base64 encoded URI of logo in the Tekton Hub CR.
* This update increments the version number of the git-clone task to 0.9.

[id="chains-new-features-1-10_{context}"]
=== {tekton-chains}

* This update adds annotations and labels to the `PipelineRun` and `TaskRun` attestations.
* This update adds a new format named `slsa/v1`, which generates the same provenance as the one generated when requesting in the `in-toto` format.
* With this update, Sigstore features are moved out from the experimental features.
* With this update, the `predicate.materials` function includes image URI and digest information from all steps and sidecars for a `TaskRun` object.

[id="tekton-hub-new-features-1-10_{context}"]
=== {tekton-hub}

* This update supports installing, upgrading, or downgrading Tekton resources of the `v1` API version on the cluster.
* This update supports adding a custom logo in place of the {tekton-hub} logo in UI.
* This update extends the `tkn hub install` command functionality by adding a `--type artifact` flag, which fetches resources from the Artifact Hub and installs them on your cluster.
* This update adds support tier, catalog, and org information as labels to the resources being installed from Artifact Hub to your cluster.

[id="pac-new-features-1-10_{context}"]
=== {pac}

* This update enhances incoming webhook support. For a GitHub application installed on the OpenShift Container Platform cluster, you do not need to provide the `git_provider` specification for an incoming webhook. Instead, {pac} detects the secret and use it for the incoming webhook.
* With this update, you can use the same token to fetch remote tasks from the same host on GitHub with a non-default branch.
* With this update, {pac} supports Tekton `v1` templates. You can have `v1` and `v1beta1` templates, which {pac} reads for PR generation. The PR is created as `v1` on cluster.
* Before this update, OpenShift console UI would use a hardcoded pipeline run template as a fallback template when a runtime template was not found in the OpenShift namespace. This update in the `pipelines-as-code` config map provides a new default pipeline run template named, `pipelines-as-code-template-default` for the console to use.
* With this update, {pac} supports Tekton Pipelines 0.44.0 minimal status.
* With this update, {pac} supports Tekton `v1` API, which means {pac} is now compatible with Tekton v0.44 and later.
* With this update, you can configure custom console dashboards in addition to configuring a console for OpenShift and Tekton dashboards for k8s.
* With this update, {pac} detects the installation of a GitHub application initiated using the `tkn pac create repo` command and does not require a GitHub webhook if it was installed globally.
* Before this update, if there was an error on a `PipelineRun` execution and not on the tasks attached to `PipelineRun`, {pac} would not report the failure properly. With this update, {pac} reports the error properly on the GitHub checks when a `PipelineRun` could not be created.
* With this update, {pac} includes a `target_namespace` variable, which expands to the currently running namespace where the `PipelineRun` is executed.
* With this update, {pac} lets you bypass GitHub enterprise questions in the CLI bootstrap GitHub application.
* With this update, {pac} does not report errors when the repository CR was not found.
* With this update, {pac} reports an error if multiple pipeline runs with the same name were found.

[id="breaking-changes-1-10_{context}"]
== Breaking changes

* With this update, the prior version of the `tkn` command is not compatible with {pipelines-title} 1.10.
* This update removes support for `Cluster` and `CloudEvent` pipeline resources from Tekton CLI. You cannot create pipeline resources by using the `tkn pipelineresource create` command. Also, pipeline resources are no longer supported in the `start` command of a task, cluster task, or pipeline.
* This update removes `tekton` as a provenance format from Tekton Chains.

[id="deprecated-features-1-10_{context}"]
== Deprecated and removed features

* In {pipelines-title} 1.10, the `ClusterTask` commands are now deprecated and are planned to be removed in a future release. The `tkn task create` command is also deprecated with this update.
* In {pipelines-title} 1.10, the flags `-i` and `-o` that were used with the `tkn task start` command are now deprecated because the `v1` API does not support pipeline resources.
* In {pipelines-title} 1.10, the flag `-r` that was used with the `tkn pipeline start` command is deprecated because the `v1` API does not support pipeline resources.
* The {pipelines-title} 1.10 update sets the `openshiftDefaultEmbeddedStatus` parameter to `both` with `full` and `minimal` embedded status. The flag to change the default embedded status  is also deprecated and will be removed. In addition, the pipeline default embedded status will be changed to `minimal` in a future release.

[id="known-issues-1-10_{context}"]
== Known issues

* This update includes the following backward incompatible changes:
** Removal of the `PipelineResources` cluster
** Removal of the `PipelineResources` cloud event
* If the pipelines metrics feature does not work after a cluster upgrade, run the following command as a workaround:
+
[source,terminal]
----
$ oc get tektoninstallersets.operator.tekton.dev | awk '/pipeline-main-static/ {print $1}' | xargs oc delete tektoninstallersets
----
* With this update, usage of external databases, such as the Crunchy PostgreSQL is not supported on {ibm-power-name}, {ibm-z-name}, and {ibm-linuxone-name}. Instead, use the default {tekton-hub} database.

[id="fixed-issues-1-10_{context}"]
== Fixed issues

* Before this update, the `opc pac` command generated a runtime error instead of showing any help. This update fixes the `opc pac` command to show the help message.
* Before this update, running the `tkn pac create repo` command needed the webhook details for creating a repository. With this update, the `tkn-pac create repo` command does not configure a webhook when your GitHub application is installed.
* Before this update, {pac} would not report a pipeline run creation error when Tekton Pipelines had issues creating the `PipelineRun` resource. For example, a non-existing task in a pipeline run would show no status. With this update, {pac} shows the proper error message coming from Tekton Pipelines along with the task that is missing.
* This update fixes UI page redirection after a successful authentication. Now, you are redirected to the same page where you had attempted to log in to Tekton Hub.
* This update fixes the `list` command with these flags, `--all-namespaces` and `--output=yaml`, for a cluster task, an individual task, and a pipeline.
* This update removes the forward slash in the end of the `repo.spec.url` URL so that it matches the URL coming from GitHub.
* Before this update, the `marshalJSON` function would not marshal a list of objects. With this update, the `marshalJSON` function marshals the list of objects.
* With this update, {pac} lets you bypass GitHub enterprise questions in the CLI bootstrap GitHub application.
* This update fixes the GitHub collaborator check when your repository has more than 100 users.
* With this update, the `sign` and `verify` commands for a task or pipeline now work without a kubernetes configuration file.
* With this update, Tekton Operator cleans leftover pruner cron jobs if pruner has been skipped on a namespace.
* Before this update, the API `ConfigMap` object would not be updated with a user configured value for a catalog refresh interval. This update fixes the `CATALOG_REFRESH_INTERVAL` API in the Tekon Hub CR.
* This update fixes reconciling of `PipelineRunStatus` when changing the `EmbeddedStatus` feature flag. This update resets the following parameters:
** The `status.runs` and `status.taskruns` parameters to `nil` with `minimal EmbeddedStatus`
** The `status.childReferences` parameter to `nil` with `full EmbeddedStatus`
* This update adds a conversion configuration to the `ResolutionRequest` CRD. This update properly configures conversion from the `v1alpha1.ResolutionRequest` request to the `v1beta1.ResolutionRequest` request.
* This update checks for duplicate workspaces associated with a pipeline task.
* This update fixes the default value for enabling resolvers in the code.
* This update fixes `TaskRef` and `PipelineRef` names conversion by using a resolver.

[id="release-notes-1-10-1_{context}"]
== Release notes for {pipelines-title} General Availability 1.10.1

With this update, {pipelines-title} General Availability (GA) 1.10.1 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="fixed-issues-1-10-1_{context}"]
=== Fixed issues for {pac}

* Before this update, if the source branch information coming from payload included `refs/heads/` but the user-configured target branch only included the branch name, `main`, in a CEL expression, the push request would fail. With this update, {pac} passes the push request and triggers a pipeline if either the base branch or target branch has `refs/heads/` in the payload.
* Before this update, when a `PipelineRun` object could not be created, the error received from the Tekton controller was not reported to the user. With this update, {pac} reports the error messages to the GitHub interface so that users can troubleshoot the errors. {pac} also reports the errors that occurred during pipeline execution.
* With this update, {pac} does not echo a secret to the GitHub checks interface when it failed to create the secret on the OpenShift Container Platform cluster because of an infrastructure issue.
* This update removes the deprecated APIs that are no longer in use from {pipelines-title}.

[id="release-notes-1-10-2_{context}"]
== Release notes for {pipelines-title} General Availability 1.10.2

With this update, {pipelines-title} General Availability (GA) 1.10.2 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="fixed-issues-1-10-2_{context}"]
=== Fixed issues

Before this update, an issue in the Tekton Operator prevented the user from setting the value of the `enable-api-fields` flag to `beta`. This update fixes the issue. Now, you can set the value of the `enable-api-fields` flag to `beta` in the `TektonConfig` CR.

[id="release-notes-1-10-3_{context}"]
== Release notes for {pipelines-title} General Availability 1.10.3

With this update, {pipelines-title} General Availability (GA) 1.10.3 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="fixed-issues-1-10-3_{context}"]
=== Fixed issues

Before this update, the Tekton Operator did not expose the performance configuration fields for any customizations. With this update, as a cluster administrator, you can customize the following performance configuration fields in the `TektonConfig` CR based on your needs:

* `disable-ha`
* `buckets`
* `kube-api-qps`
* `kube-api-burst`
* `threads-per-controller`

[id="release-notes-1-10-4_{context}"]
== Release notes for {pipelines-title} General Availability 1.10.4

With this update, {pipelines-title} General Availability (GA) 1.10.4 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="fixed-issues-1-10-4_{context}"]
=== Fixed issues

* This update fixes the bundle resolver conversion issue for the `PipelineRef` field in a pipeline run. Now, the conversion feature sets the value of the `kind` field to `Pipeline` after conversion.

* Before this update, the `pipelinerun.timeouts` field was reset to the `timeouts.pipeline` value, ignoring the `timeouts.tasks` and `timeouts.finally` values. This update fixes the issue and sets the correct default timeout value for a `PipelineRun` resource.

* Before this update, the controller logs contained unnecessary data. This update fixes the issue.

[id="release-notes-1-10-5_{context}"]
== Release notes for {pipelines-title} General Availability 1.10.5

With this update, {pipelines-title} General Availability (GA) 1.10.5 is available on OpenShift Container Platform 4.10 in addition to 4.11, 4.12, and 4.13.

[IMPORTANT]
====
{pipelines-title} 1.10.5 is only available in the `pipelines-1.10` channel on OpenShift Container Platform 4.10, 4.11, 4.12, and 4.13. It is not available in the `latest` channel for any OpenShift Container Platform version.
====

[id="fixed-issues-1-10-5_{context}"]
=== Fixed issues

* Before this update, huge pipeline runs were not getting listed or deleted using the `oc` and `tkn` commands. This update mitigates this issue by compressing the huge annotations that were causing this problem. Remember that if the pipeline runs are still too huge after compression, then the same error still recurs.

* Before this update, only the pod template specified in the `pipelineRun.spec.taskRunSpecs[].podTemplate` object would be considered for a pipeline run. With this update, the pod template specified in the `pipelineRun.spec.podTemplate` object is also considered and merged with the template specified in the `pipelineRun.spec.taskRunSpecs[].podTemplate` object.

// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc
[id="op-release-notes-1-9_{context}"]
= Release notes for {pipelines-title} General Availability 1.9

With this update, {pipelines-title} General Availability (GA) 1.9 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="new-features-1-9_{context}"]
== New features

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.9.

[id="pipelines-new-features-1-9_{context}"]
=== Pipelines

* With this update, you can specify pipeline parameters and results in arrays and object dictionary forms.

* This update provides support for Container Storage Interface (CSI) and projected volumes for your workspace.

* With this update, you can specify the `stdoutConfig` and `stderrConfig` parameters when defining pipeline steps. Defining these parameters helps to capture standard output and standard error, associated with steps, to local files.

* With this update, you can add variables in the `steps[].onError` event handler, for example, `$(params.CONTINUE)`.

* With this update, you can use the output from the `finally` task in the `PipelineResults` definition. For example, `$(finally.<pipelinetask-name>.result.<result-name>)`, where `<pipelinetask-name>` denotes the pipeline task name and `<result-name>` denotes the result name.

* This update supports task-level resource requirements for a task run.

* With this update, you do not need to recreate parameters that are shared, based on their names, between a pipeline and the defined tasks. This update is part of a developer preview feature.

* This update adds support for remote resolution, such as built-in git, cluster, bundle, and hub resolvers.

[id="triggers-new-features-1-9_{context}"]
=== Triggers

* This update adds the `Interceptor` CRD to define `NamespacedInterceptor`. You can use `NamespacedInterceptor` in the `kind` section of interceptors reference in triggers or in the `EventListener` specification.

* This update enables `CloudEvents`.

* With this update, you can configure the webhook port number when defining a trigger.

* This update supports using trigger `eventID` as input to `TriggerBinding`.

* This update supports validation and rotation of certificates for the `ClusterInterceptor` server.
** Triggers perform certificate validation for core interceptors and rotate a new certificate to `ClusterInterceptor` when its certificate expires.

[id="cli-new-features-1-9_{context}"]
=== CLI

* This update supports showing annotations in the `describe` command.

* This update supports showing pipeline, tasks, and timeout in the `pr describe` command.

* This update adds flags to provide pipeline, tasks, and timeout in the `pipeline start` command.

* This update supports showing the presence of workspace, optional or mandatory, in the `describe` command of a task and pipeline.

* This update adds the `timestamps` flag to show logs with a timestamp.

* This update adds a new flag `--ignore-running-pipelinerun`, which ignores the deletion of `TaskRun` associated with `PipelineRun`.

* This update adds support for experimental commands. This update also adds experimental subcommands, `sign` and `verify` to the `tkn` CLI tool.

* This update makes the Z shell (Zsh) completion feature usable without generating any files.

* This update introduces a new CLI tool called `opc`. It is anticipated that an upcoming release will replace the `tkn` CLI tool with `opc`.
+
[IMPORTANT]
====
* The new CLI tool `opc` is a Technology Preview feature.
* `opc` will be a replacement for `tkn` with additional {pipelines-title} specific features, which do not necessarily fit in `tkn`.
====

[id="operator-new-features-1-9_{context}"]
=== Operator

* With this update, {pac} is installed by default. You can disable {pac} by using the `-p` flag:
+
[source,terminal]
----
$ oc patch tektonconfig config --type="merge" -p '{"spec": {"platforms": {"openshift":{"pipelinesAsCode": {"enable": false}}}}}'
----

* With this update, you can also modify {pac} configurations in the `TektonConfig` CRD.

* With this update, if you disable the developer perspective, the Operator does not install developer console related custom resources.

* This update includes `ClusterTriggerBinding` support for Bitbucket Server and Bitbucket Cloud and helps you to reuse a `TriggerBinding` across your entire cluster.

[id="resolver-new-features-1-9_{context}"]
=== Resolvers

* With this update, you can configure pipeline resolvers in the `TektonConfig` CRD. You can enable or disable these pipeline resolvers:  `enable-bundles-resolver`, `enable-cluster-resolver`, `enable-git-resolver`, and `enable-hub-resolver`.
+
[source,yaml,subs="attributes+"]
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
...
----
+
You can also provide resolver specific configurations in `TektonConfig`. For example, you can define the following fields in the `map[string]string` format to set configurations for individual resolvers:
+
[source,yaml,subs="attributes+"]
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
...
----

[id="chains-new-features-1-9_{context}"]
=== {tekton-chains}

* Before this update, only Open Container Initiative (OCI) images were supported as outputs of `TaskRun` in the in-toto provenance agent. This update adds in-toto provenance metadata as outputs with these suffixes, `ARTIFACT_URI` and `ARTIFACT_DIGEST`.

* Before this update, only `TaskRun` attestations were supported. This update adds support for `PipelineRun` attestations as well.

* This update adds support for {tekton-chains} to get the `imgPullSecret` parameter from the pod template. This update helps you to configure repository authentication based on each pipeline run or task run without modifying the service account.

[id="tekton-hub-new-features-1-9_{context}"]
=== {tekton-hub}

* With this update, as an administrator, you can use an external database, such as Crunchy PostgreSQL with {tekton-hub}, instead of using the default {tekton-hub} database. This update helps you to perform the following actions:
** Specify the coordinates of an external database to be used with {tekton-hub}
** Disable the default {tekton-hub} database deployed by the Operator

* This update removes the dependency of `config.yaml` from external Git repositories and moves the complete configuration data into the API `ConfigMap`. This update helps an administrator to perform the following actions:
** Add the configuration data, such as categories, catalogs, scopes, and defaultScopes in the {tekton-hub} custom resource.
** Modify {tekton-hub} configuration data on the cluster. All modifications are preserved upon Operator upgrades.
** Update the list of catalogs for {tekton-hub}
** Change the categories for {tekton-hub}
+
[NOTE]
====
If you do not add any configuration data, you can use the default data in the API `ConfigMap` for {tekton-hub} configurations.
====

[id="pac-new-features-1-9_{context}"]
=== {pac}

* This update adds support for concurrency limit in the `Repository` CRD to define the maximum number of `PipelineRuns` running for a repository at a time. The `PipelineRuns` from a pull request or a push event are queued in alphabetical order.

* This update adds a new command `tkn pac logs` for showing the logs of the latest pipeline run for a repository.

* This update supports advanced event matching on file path for push and pull requests to GitHub and GitLab. For example, you can use the Common Expression Language (CEL) to run a pipeline only if a path has changed for any markdown file in the `docs` directory.
+
[source,yaml]
----
  ...
  annotations:
     pipelinesascode.tekton.dev/on-cel-expression: |
      event == "pull_request" && "docs/*.md".pathChanged()
----

* With this update, you can reference a remote pipeline in the `pipelineRef:` object using annotations.

* With this update, you can auto-configure new GitHub repositories with {pac}, which sets up a namespace and creates a `Repository` CRD for your GitHub repository.

* With this update, {pac} generates metrics for `PipelineRuns` with provider information.

* This update provides the following enhancements for the `tkn-pac` plugin:
** Detects running pipelines correctly
** Fixes showing duration when there is no failure completion time
** Shows an error snippet and highlights the error regular expression pattern in the `tkn-pac describe` command
** Adds the `use-real-time` switch to the `tkn-pac ls` and `tkn-pac describe` commands
** Imports the `tkn-pac` logs documentation
** Shows `pipelineruntimeout` as a failure in the `tkn-pac ls` and `tkn-pac describe` commands.
** Show a specific pipeline run failure with the `--target-pipelinerun` option.

* With this update, you can view the errors for your pipeline run in the form of a version control system (VCS) comment or a small snippet in the GitHub checks.

* With this update, {pac} optionally can detect errors inside the tasks if they are of a simple format and add those tasks as annotations in GitHub. This update is part of a developer preview feature.

* This update adds the following new commands:
** `tkn-pac webhook add`: Adds a webhook to project repository settings and updates the `webhook.secret` key in the existing `k8s Secret` object without updating the repository.
** `tkn-pac webhook update-token`: Updates provider token for an existing `k8s Secret` object without updating the repository.

* This update enhances functionality of the `tkn-pac create repo` command, which creates and configures webhooks for GitHub, GitLab, and BitbucketCloud along with creating repositories.

* With this update, the `tkn-pac describe` command shows the latest fifty events in a sorted order.

* This update adds the `--last` option to the `tkn-pac logs` command.

* With this update, the `tkn-pac resolve` command prompts for a token on detecting a `git_auth_secret` in the file template.

* With this update, {pac} hides secrets from log snippets to avoid exposing secrets in the GitHub interface.

* With this update, the secrets automatically generated for `git_auth_secret` are an owner reference with `PipelineRun`. The secrets get cleaned with the `PipelineRun`, not after the pipeline run execution.

* This update adds support to cancel a pipeline run with the `/cancel` comment.

* Before this update, the GitHub apps token scoping was not defined and tokens would be used on every repository installation. With this update, you can scope the GitHub apps token to the target repository using the following parameters:
** `secret-github-app-token-scoped`: Scopes the app token to the target repository, not to every repository the app installation has access to.
** `secret-github-app-scope-extra-repos`: Customizes the scoping of the  app token with an additional owner or repository.

* With this update, you can use {pac} with your own Git repositories that are hosted on GitLab.

* With this update, you can access pipeline execution details in the form of kubernetes events in your namespace. These details help you to troubleshoot pipeline errors without needing access to admin namespaces.

* This update supports authentication of URLs in the {pac} resolver with the Git provider.

* With this update, you can set the name of the hub catalog by using a setting in the `pipelines-as-code` config map.

* With this update, you can set the maximum and default limits for the `max-keep-run` parameter.

* This update adds documents on how to inject custom Secure Sockets Layer (SSL) certificates in {pac} to let you connect to provider instance with custom certificates.

* With this update, the `PipelineRun` resource definition has the log URL included as an annotation. For example, the `tkn-pac describe` command shows the log link when describing a `PipelineRun`.

* With this update, `tkn-pac` logs show repository name, instead of `PipelineRun` name.

[id="breaking-changes-1-9_{context}"]
== Breaking changes

// .Pipelines

* With this update, the `Conditions` custom resource definition (CRD) type has been removed. As an alternative, use the `WhenExpressions` instead.

* With this update, support for `tekton.dev/v1alpha1` API pipeline resources, such as Pipeline, PipelineRun, Task, Clustertask, and TaskRun has been removed.

* With this update, the `tkn-pac setup` command has been removed. Instead, use the `tkn-pac webhook add` command to re-add a webhook to an existing Git repository. And use the `tkn-pac webhook update-token` command to update the personal provider access token for an existing Secret object in the Git repository.

* With this update, a namespace that runs a pipeline with default settings does not apply the `pod-security.kubernetes.io/enforce:privileged` label to a workload.

[id="deprecated-features-1-9_{context}"]
== Deprecated and removed features

* In the {pipelines-title} 1.9.0 release, `ClusterTasks` are deprecated and planned to be removed in a future release. As an alternative, you can use `Cluster Resolver`.

* In the {pipelines-title} 1.9.0 release, the use of the `triggers` and the `namespaceSelector` fields in a single `EventListener` specification is deprecated and planned to be removed in a future release. You can use these fields in different `EventListener` specifications successfully.

* In the {pipelines-title} 1.9.0 release, the `tkn pipelinerun describe` command does not display timeouts for the `PipelineRun` resource.

* In the {pipelines-title} 1.9.0 release, the PipelineResource` custom resource (CR) is deprecated. The `PipelineResource` CR was a Tech Preview feature and part of the `tekton.dev/v1alpha1` API.

* In the {pipelines-title} 1.9.0 release, custom image parameters from cluster tasks are deprecated. As an alternative, you can copy a cluster task and use your custom image in it.

[id="known-issues-1-9_{context}"]
== Known issues

// .Operator

* The `chains-secret` and `chains-config` config maps are removed after you uninstall the {pipelines-title} Operator. As they contain user data, they should be preserved and not deleted.
// https://issues.redhat.com/browse/SRVKP-2396

// .PAC

* When running the `tkn pac` set of commands on Windows, you may receive the following error message: `Command finished with error: not supported by Windows.`
+

Workaround: Set the `NO_COLOR` environment variable to `true`.
// https://issues.redhat.com/browse/SRVKP-2197

* Running the `tkn pac resolve -f <filename> | oc create -f` command may not provide expected results, if the `tkn pac resolve` command uses a templated parameter value to function.
+
Workaround: To mitigate this issue, save the output of `tkn pac resolve` in a temporary file by running the `tkn pac resolve -f <filename> -o tempfile.yaml` command and then run the `oc create -f tempfile.yaml` command. For example, `tkn pac resolve -f <filename> -o /tmp/pull-request-resolved.yaml && oc create -f /tmp/pull-request-resolved.yaml`.

[id="fixed-issues-1-9_{context}"]
== Fixed issues

// .Pipelines

* Before this update, after replacing an empty array, the original array returned an empty string rendering the paramaters inside it invalid. With this update, this issue is resolved and the original array returns as empty.
// Vincent Demeester

* Before this update, if duplicate secrets were present in a service account for a pipelines run, it resulted in failure in task pod creation. With this update, this issue is resolved and the task pod is created successfully even if duplicate secrets are present in a service account.
// Vincent Demeester

* Before this update, by looking at the TaskRun's `spec.StatusMessage` field, users could not distinguish whether the `TaskRun` had been cancelled by the user or by a `PipelineRun` that was part of it. With this update, this issue is resolved and users can distinguish the status of the `TaskRun` by looking at the TaskRun's `spec.StatusMessage` field.
// Vincent Demeester

* Before this update, webhook validation was removed on deletion of old versions of invalid objects. With this update, this issue is resolved.
// Vincent Demeester @vdeemester

* Before this update, if you set the `timeouts.pipeline` parameter to `0`, you could not set the `timeouts.tasks` parameter or the `timeouts.finally` parameters. This update resolves the issue. Now, when you set the `timeouts.pipeline` parameter value, you can set the value of either the`timeouts.tasks` parameter or the `timeouts.finally` parameter. For example:
+
[source,yaml]
----
yaml
kind: PipelineRun
spec:
  timeouts:
    pipeline: "0"  # No timeout
    tasks: "0h3m0s"
----
// Vincent Demeester @vdeemester

* Before this update, a race condition could occur if another tool updated labels or annotations on a PipelineRun or TaskRun. With this update, this issue is resolved and you can merge labels or annotations.
// Vincent Demeester @vdeemester

// .Triggers

* Before this update, log keys did not have the same keys as in pipelines controllers. With this update, this issue has been resolved and the log keys have been updated to match the log stream of pipeline controllers. The keys in logs have been changed from "ts" to "timestamp", from "level" to "severity", and from "message" to "msg".
// https://issues.redhat.com/browse/SRVKP-1959
// @KhurramBaig

// .CLI

* Before this update, if a PipelineRun was deleted with an unknown status, an error message was not generated. With this update, this issue is resolved and an error message is generated.
// https://github.com/tektoncd/cli/pull/1684
// Piyush Garg @piyush-garg

* Before this update, to access bundle commands like `list` and `push`, it was required to use the `kubeconfig` file . With this update, this issue has been resolved and the `kubeconfig` file is not required to access bundle commands.
// https://github.com/tektoncd/cli/pull/1557
// Piyush Garg @piyush-garg

* Before this update, if the parent PipelineRun was running while deleting TaskRuns, then TaskRuns would be deleted. With this update, this issue is resolved and TaskRuns are not getting deleted if the parent PipelineRun is running.
// https://github.com/tektoncd/cli/pull/1736
// Piyush Garg @piyush-garg

* Before this update, if the user attempted to build a bundle with more objects than the pipeline controller permitted, the Tekton CLI did not display an error message. With this update, this issue is resolved and the Tekton CLI displays an error message if the user attempts to build a bundle with more objects than the limit permitted in the pipeline controller.
// https://github.com/tektoncd/cli/pull/1572
// Piyush Garg @piyush-garg

// .Operator

* Before this update, if namespaces were removed from the cluster, then the operator did not remove namespaces from the `ClusterInterceptor ClusterRoleBinding` subjects. With this update, this issue has been resolved, and the operator removes the namespaces from the `ClusterInterceptor ClusterRoleBinding` subjects.
// Shubham Minglani

* Before this update, the default installation of the {pipelines-title} Operator resulted in the `pipelines-scc-rolebinding security context constraint` (SCC) role binding resource remaining in the cluster. With this update, the default installation of the {pipelines-title} Operator results in the `pipelines-scc-rolebinding security context constraint` (SCC) role binding resource resource being removed from the cluster.
// https://github.com/tektoncd/operator/pull/1156
// https://issues.redhat.com/browse/SRVKP-2520
// Shubham Minglani

// .PAC

* Before this update, {pac} did not get updated values from the {pac} `ConfigMap` object. With this update, this issue is fixed and the {pac} `ConfigMap` object looks for any new changes.
// Savita Ashture

* Before this update, {pac} controller did not wait for the `tekton.dev/pipeline` label to be updated and added the `checkrun id` label, which would cause race conditions. With this update, the {pac} controller waits for the `tekton.dev/pipeline` label to be updated and then adds the `checkrun id` label, which helps to avoid race conditions.
// Savita Ashture

* Before this update, the `tkn-pac create repo` command did not override a `PipelineRun` if it already existed in the git repository. With this update, `tkn-pac create` command is fixed to override a `PipelineRun` if it exists in the git repository and this resolves the issue successfully.
// Savita Ashture

* Before this update, the `tkn pac describe` command did not display reasons for every message. With this update, this issue is fixed and the `tkn pac describe` command displays reasons for every message.
// Savita Ashture

* Before this update, a pull request failed if the user in the annotation provided values by using a regex form, for example, `refs/head/rel-*`. The pull request failed because it was missing `refs/heads` in its base branch. With this update, the prefix is added and checked that it matches. This resolves the issue and the pull request is successful.
// Savita Ashture

[id="release-notes-1-9-1_{context}"]
== Release notes for {pipelines-title} General Availability 1.9.1

With this update, {pipelines-title} General Availability (GA) 1.9.1 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="fixed-issues-1-9-1_{context}"]
== Fixed issues

* Before this update, the `tkn pac repo list` command did not run on Microsoft Windows. This update fixes the issue, and now you can run the `tkn pac repo list` command on Microsoft Windows.

* Before this update, {pac} watcher did not receive all the configuration change events. With this update, the {pac} watcher is updated, and now the {pac} watcher does not miss the configuration change events.

* Before this update, the pods created by {pac}, such as `TaskRuns` or `PipelineRuns` could not access custom certificates exposed by the user in the cluster. This update fixes the issue, and you can now access custom certificates from the `TaskRuns` or `PipelineRuns` pods in the cluster.

* Before this update, on a cluster enabled with FIPS, the `tekton-triggers-core-interceptors` core interceptor used in the `Trigger` resource did not function after the Pipelines Operator was upgraded to version 1.9. This update resolves the issue. Now, OpenShift uses MInTLS 1.2 for all its components. As a result, the `tekton-triggers-core-interceptors` core interceptor updates to TLS version 1.2and its functionality runs accurately.

* Before this update, when using a pipeline run with an internal OpenShift image registry, the URL to the image had to be hardcoded in the pipeline run definition. For example:
+
[source,yaml]
----
...
  - name: IMAGE_NAME
    value: 'image-registry.openshift-image-registry.svc:5000/<test_namespace>/<test_pipelinerun>'
...
----
+
When using a pipeline run in the context of {pac}, such hardcoded values prevented the pipeline run definitions from being used in different clusters and namespaces.
+
With this update, you can use the dynamic template variables instead of hardcoding the values for namespaces and pipeline run names to generalize pipeline run definitions. For example:
+
[source,yaml]
----
...
  - name: IMAGE_NAME
    value: 'image-registry.openshift-image-registry.svc:5000/{{ target_namespace }}/$(context.pipelineRun.name)'
...
----

* Before this update, {pac} used the same GitHub token to fetch a remote task available in the same host only on the default GitHub branch. This update resolves the issue. Now {pac} uses the same GitHub token to fetch a remote task from any GitHub branch.

[id="known-issues-1-9-1_{context}"]
== Known issues

* The value for `CATALOG_REFRESH_INTERVAL`, a field in the Hub API `ConfigMap` object used in the Tekton Hub CR, is not getting updated with a custom value provided by the user.
+
Workaround: None. You can track the issue SRVKP-2854.

[id="breaking-changes-1-9-1_{context}"]
== Breaking changes

* With this update, an OLM misconfiguration issue has been introduced, which prevents the upgrade of the OpenShift Container Platform. This issue will be fixed in a future release.

[id="release-notes-1-9-2_{context}"]
== Release notes for {pipelines-title} General Availability 1.9.2

With this update, {pipelines-title} General Availability (GA) 1.9.2 is available on OpenShift Container Platform 4.11, 4.12, and 4.13.

[id="fixed-issues-1-9-2_{context}"]
== Fixed issues

* Before this update, an OLM misconfiguration issue had been introduced in the previous version of the release, which prevented the upgrade of OpenShift Container Platform. With this update, this misconfiguration issue has been fixed.

[id="release-notes-1-9-3_{context}"]
== Release notes for {pipelines-title} General Availability 1.9.3

With this update, {pipelines-title} General Availability (GA) 1.9.3 is available on OpenShift Container Platform 4.10 in addition to 4.11, 4.12, and 4.13.

[id="fixed-issues-1-9-3_{context}"]
== Fixed issues

* This update fixes the performance issues for huge pipelines. Now, the CPU usage is reduced by 61% and the memory usage is reduced by 44%.

* Before this update, a pipeline run would fail if a task did not run because of its `when` expression. This update fixes the issue by preventing the validation of a skipped task result in pipeline results. Now, the pipeline result is not emitted and the pipeline run does not fail because of a missing result.

* This update fixes the `pipelineref.bundle` conversion to the bundle resolver for the `v1beta1` API. Now, the conversion feature sets the value of the `kind` field to `Pipeline` after conversion.

* Before this update, an issue in the {pipelines-shortname} Operator prevented the user from setting the value of the `spec.pipeline.enable-api-fields` field to `beta`. This update fixes the issue. Now, you can set the value to `beta` along with `alpha` and `stable` in the `TektonConfig` custom resource.

* Before this update, when {pac} could not create a secret due to a cluster error, it would show the temporary token on the GitHub check run, which is public. This update fixes the issue. Now, the token is no longer displayed on the GitHub checks interface when the creation of the secret fails.

[id="known-issues-1-9-3_{context}"]
== Known issues

* There is currently a known issue with the *stop* option for pipeline runs in the OpenShift Container Platform web console. The *stop* option in the *Actions* drop-down list is not working as expected and does not cancel the pipeline run.

* There is currently a known issue with upgrading to {pipelines-shortname} version 1.9.x due to a failing custom resource definition conversion.
+
Workaround: Before upgrading to {pipelines-shortname} version 1.9.x, perform the step mentioned in the solution on the Red Hat Customer Portal.

// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc
[id="op-release-notes-1-8_{context}"]
= Release notes for {pipelines-title} General Availability 1.8

With this update, {pipelines-title} General Availability (GA) 1.8 is available on OpenShift Container Platform 4.10, 4.11, and 4.12.

[id="new-features-1-8_{context}"]
== New features

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.8.

[id="pipelines-new-features-1-8_{context}"]
=== Pipelines

* With this update, you can run {pipelines-title} GA 1.8 and later on an OpenShift Container Platform cluster that is running on ARM hardware. This includes support for `ClusterTask` resources and the `tkn` CLI tool.
// Shubham Minglani

* This update implements `Step` and `Sidecar` overrides for `TaskRun` resources.
// source,yaml
----
kind: Task
apiVersion: tekton.dev/v1beta1
metadata:
  name: write-array
  annotations:
    description: |
      A simple task that writes array
spec:
  results:
    - name: array-results
      type: array
      description: The array results
...
----
+
Additionally, you can run a task script to populate the results with an array:
+
[source,terminal]
----
$ echo -n "[\"hello\",\"world\"]" | tee $(results.array-results.path)
----
+
To enable this feature, in the `TektonConfig` custom resource definition, in the `pipeline` section, you must set the `enable-api-fields` field to `alpha`.
+
This feature is in progress and is part of TEP-0076.
// id="triggers-new-features-1-8_{context}"
=== Triggers

* This update transitions the `TriggerGroups` field in the `EventListener` specification from an alpha feature to a stable feature. Using this field, you can specify a set of interceptors before selecting and running a group of triggers.
+
Because this feature is available by default, you no longer need to set the `pipeline.enable-api-fields` field to `alpha` in the `TektonConfig` custom resource definition.
// id="cli-new-features-1-8_{context}"
=== CLI

* With this update, you can use the `tkn taskrun export` command to export a live task run from a cluster to a YAML file, which you can use to import the task run to another cluster.
// (#1531)
// Chmouel Boudjnah @chmouel

* With this update, you can add the `-o name` flag to the `tkn pipeline start` command to print the name of the pipeline run right after it starts.
// (#1540)
// Chmouel Boudjnah @chmouel

* This update adds a list of available plugins to the output of the `tkn --help` command.
// (#1535)
// Chmouel Boudjnah @chmouel

* With this update, while deleting a pipeline run or task run, you can use both the `--keep` and `--keep-since` flags together.
// (#1533)
// Divyanshu Agrawal @divyansh42

* With this update, you can use `Cancelled` as the value of the `spec.status` field rather than the deprecated `PipelineRunCancelled` value.
// (#1554)
// Vinamra Jain @vinamra28

[id="operator-new-features-1-8_{context}"]
=== Operator

// [Hub]
* With this update, as an administrator, you can configure your local {tekton-hub} instance to use a custom database rather than the default database.
// SRVKP-2309 Pipeline as code: validate repository URL uniqueness)
// Puneet Punamiya

* With this update, as a cluster administrator, if you enable your local {tekton-hub} instance, it periodically refreshes the database so that changes in the catalog appear in the {tekton-hub} web console. You can adjust the period between refreshes.
+
Previously, to add the tasks and pipelines in the catalog to the database, you performed that task manually or set up a cron job to do it for you.
// SRVKP-2252 Refresh catalogs on schedule)
// Puneet Punamiya

* With this update, you can install and run a {tekton-hub} instance with minimal configuration. This way, you can start working with your teams to decide which additional customizations they might want.
// SRVKP-2250 Install Hub with default configs)
// Shiv Verma

* This update adds `GIT_SSL_CAINFO` to the `git-clone` task so you can clone secured repositories.
// id="chains-new-features-1-8_{context}"
=== Tekton Chains

* With this update, you can log in to a vault by using OIDC rather than a static token. This change means that Spire can generate the OIDC credential so that only trusted workloads are allowed to log in to the vault. Additionally, you can pass the vault address as a configuration value rather than inject it as an environment variable.
// id="tekton-hub-new-features-1-8_{context}"
=== {tekton-hub}

* With this update, if you install a fresh instance of {tekton-hub} by using the Operator, the {tekton-hub} login is disabled by default. To enable the login and rating features, you must create the Hub API secret while installing {tekton-hub}.
+
[NOTE]
====
Because {tekton-hub} login was enabled by default in {pipelines-title} 1.7, if you upgrade the Operator, the login is enabled by default in {pipelines-title} 1.8. To disable this login, see Disabling Tekton Hub login after upgrading from OpenShift Pipelines 1.7.x --> 1.8.x
====
// source,yaml
----
apiVersion: v1
kind: Secret
metadata:
  name: tekton-hub-db
  labels:
    app: tekton-hub-db
type: Opaque
stringData:
  POSTGRES_HOST: <hostname>
  POSTGRES_DB: <database_name>
  POSTGRES_USER: <username>
  POSTGRES_PASSWORD: <password>
  POSTGRES_PORT: <listening_port_number>
----
// SRVKP-2309 Pipeline as code: validate repository URL uniqueness)
// Puneet Punamiya

* With this update, you no longer need to log in to the {tekton-hub} web console to add resources from the catalog to the database. Now, these resources are automatically added when the {tekton-hub} API starts running for the first time.
// id="pac-new-features-1-8_{context}"
=== {pac}
// {pac} owners: Shivam Mukhade Savita Ashture

* With this update, as a developer, you get a notification from the `tkn-pac` CLI tool if you try to add a duplicate repository to a {pac} run. When you enter `tkn pac create repository`, each repository must have a unique URL. This notification also helps prevent hijacking exploits.
// SRVKP-1758 Pipeline as code: validate repository URL uniqueness)
// Shivam Mukhade

* With this update, as a developer, you can use the new `tkn-pac setup cli` command to add a Git repository to {pac} by using the webhook mechanism. This way, you can use {pac} even when using GitHub Apps is not feasible. This capability includes support for repositories on GitHub, GitLab, and BitBucket.
// SRVKP-2137 Pipeline as code - CLI add repository via webhooks)
// Shivam Mukhade

* With this update, {pac} supports GitLab integration with features such as the following:
** ACL (Access Control List) on project or group
** `/ok-to-test` support from allowed users
** `/retest` support.
//For more information, https://pkg.go.dev/github.com/openshift-pipelines/pipelines-as-code/pkg/provider/gitlab#section-readme
// no link

* With this update, you can perform advanced pipeline filtering with Common Expression Language (CEL). With CEL, you can match pipeline runs with different Git provider events by using annotations in the `PipelineRun` resource. For example:
+
[source,yaml]
----
  ...
  annotations:
     pipelinesascode.tekton.dev/on-cel-expression: |
      event == "pull_request" && target_branch == "main" && source_branch == "wip"
----
// no link

* Previously, as a developer, you could have only one pipeline run in your `.tekton` directory for each Git event, such as a pull request. With this update, you can have multiple pipeline runs in your `.tekton` directory. The web console displays the status and reports of the runs. The pipeline runs operate in parallel and report back to the Git provider interface.
// SRVKP-1781 Multiple Pipelines runs match on events)
// Chmouel Boudjnah

* With this update, you can test or retest a pipeline run by commenting `/test` or `/retest` on a pull request. You can also specify the pipeline run by name. For example, you can enter `/test <pipelinerun_name>` or  `/retest <pipelinerun-name>`.
// no link

* With this update, you can delete a repository custom resource and its associated secrets by using the new `tkn-pac delete repository` command.
// no link

[id="breaking-changes-1-8_{context}"]
== Breaking changes

// .Pipelines

* This update changes the default metrics level of `TaskRun` and `PipelineRun` resources to the following values:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: config-observability
  namespace: tekton-pipelines
  labels:
    app.kubernetes.io/instance: default
    app.kubernetes.io/part-of: tekton-pipelines
data:
  _example: |
  ...
    metrics.taskrun.level: "task"
    metrics.taskrun.duration-type: "histogram"
    metrics.pipelinerun.level: "pipeline"
    metrics.pipelinerun.duration-type: "histogram"
----
// source,terminal
----
$ oc get route -n openshift-pipelines pipelines-as-code-controller \
  --template='https://{{ .spec.host }}'
----
// no link

* With this update, {pac} renames the default secret keys for the `Repository` custom resource definition (CRD). In your CRD, replace `token` with `provider.token`, and replace `secret` with `webhook.secret`.

* With this update, {pac} replaces a special template variable with one that supports multiple pipeline runs for private repositories. In your pipeline runs, replace `secret: pac-git-basic-auth-{{repo_owner}}-{{repo_name}}` with `secret: {{ git_auth_secret }}`.

*  With this update, {pac} updates the following commands in the `tkn-pac` CLI tool:
** Replace `tkn pac repository create` with `tkn pac create repository`.
** Replace `tkn pac repository delete` with `tkn pac delete repository`.
** Replace `tkn pac repository list` with `tkn pac list`.

[id="deprecated-features-1-8_{context}"]
== Deprecated and removed features

* Starting with OpenShift Container Platform 4.11, the `preview` and `stable` channels for installing and upgrading the {pipelines-title} Operator are removed. To install and upgrade the Operator, use the appropriate `pipelines-<version>` channel, or the `latest` channel for the most recent stable version. For example, to install the {pipelines-shortname} Operator version `1.8.x`, use the `pipelines-1.8` channel.
+
[NOTE]
====
In OpenShift Container Platform 4.10 and earlier versions, you can use the `preview` and `stable` channels for installing and upgrading the Operator.
====

* Support for the `tekton.dev/v1alpha1` API version, which was deprecated in {pipelines-title} GA 1.6, is planned to be removed in the upcoming {pipelines-title} GA 1.9 release.
+
This change affects the pipeline component, which includes the `TaskRun`, `PipelineRun`, `Task`, `Pipeline`, and similar `tekton.dev/v1alpha1` resources. As an alternative, update existing resources to use `apiVersion: tekton.dev/v1beta1` as described in Migrating From Tekton v1alpha1 to Tekton v1beta1.
+
Bug fixes and support for the `tekton.dev/v1alpha1` API version are provided only through the end of the current GA 1.8 lifecycle.
+
[IMPORTANT]
====
For the *Tekton Operator*, the `operator.tekton.dev/v1alpha1` API version is *not* deprecated. You do not need to make changes to this value.
====
// #1103)

* In {pipelines-title} 1.8, the `PipelineResource` custom resource (CR) is available but no longer supported. The `PipelineResource` CR was a Tech Preview feature and part of the `tekton.dev/v1alpha1` API, which had been deprecated and planned to be removed in the upcoming {pipelines-title} GA 1.9 release.

* In {pipelines-title} 1.8, the `Condition` custom resource (CR) is removed. The `Condition` CR was part of the `tekton.dev/v1alpha1` API, which has been deprecated and is planned to be removed in the upcoming {pipelines-title} GA 1.9 release.

* In {pipelines-title} 1.8, the `gcr.io` image for `gsutil` has been removed. This removal might break clusters with `Pipeline` resources that depend on this image. Bug fixes and support are provided only through the end of the {pipelines-title} 1.7 lifecycle.
// TEP-0100: Embedded TaskRuns and Runs Status in PipelineRuns.

* In {pipelines-title} 1.8, the `pipelineRunCancelled` state is deprecated and planned to be removed in a future release. Graceful termination of `PipelineRun` objects is now promoted from an alpha feature to a stable feature. (See TEP-0058: Graceful Pipeline Run Termination.) As an alternative, you can use the `Cancelled` state, which replaces the `pipelineRunCancelled` state.
+
You do not need to make changes to your `Pipeline` and `Task` resources. If you have tools that cancel pipeline runs, you must update tools in the next release. This change also affects tools such as the CLI, IDE extensions, and so on, so that they support the new `PipelineRun` statuses.
+
Because this feature is available by default, you no longer need to set the `pipeline.enable-api-fields` field to `alpha` in the `TektonConfig` custom resource definition.

* In {pipelines-title} 1.8, the `timeout` field in `PipelineRun` has been deprecated. Instead, use the `PipelineRun.Timeouts` field, which is now promoted from an alpha feature to a stable feature.
+
Because this feature is available by default, you no longer need to set the `pipeline.enable-api-fields` field to `alpha` in the `TektonConfig` custom resource definition.
// id="known-issues-1-8_{context}"
== Known issues

// .Operator

* The `s2i-nodejs` pipeline cannot use the `nodejs:14-ubi8-minimal` image stream to perform source-to-image (S2I) builds. Using that image stream produces an `error building at STEP "RUN /usr/libexec/s2i/assemble": exit status 127` message.
+
Workaround: Use `nodejs:14-ubi8` rather than the `nodejs:14-ubi8-minimal` image stream.
// #SRVKP-1782)
// Writer, also see https://github.com/tektoncd/operator/blob/main/cmd/openshift/operator/kodata/tekton-addon/addons/02-clustertasks/source_local/s2i-nodejs/s2i-nodejs-task.yaml. Overkill: The user can run the `$ oc edit clustertask s2i-nodejs` command and replace `$(params.VERSION)` with `14-ubi8`. Alternatively, you can use a `TaskRun` resource to set the tag of the `nodejs` image stream to `14-ubi8`.

// .ARM (Tech Preview feature)

* When you run Maven and Jib-Maven cluster tasks, the default container image is supported only on Intel (x86) architecture. Therefore, tasks will fail on ARM, {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) clusters.
+
Workaround: Specify a custom image by setting the `MAVEN_IMAGE` parameter value to `maven:3.6.3-adoptopenjdk-11`.
+
[TIP]
====
Before you install tasks that are based on the Tekton Catalog on ARM, {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) using `tkn hub`, verify if the task can be executed on these platforms. To check if `ppc64le` and `s390x` are listed in the "Platforms" section of the task information, you can run the following command: `tkn hub info task <name>`
// issue # is unknown.
====
// id="fixed-issues-1-8_{context}"
== Fixed issues

// .Pipelines

* Before this update, the metrics for pipeline runs in the Developer view of the web console were incomplete and outdated. With this update, the issue has been fixed so that the metrics are correct.
// "<NAME>"` or `$params['<NAME>']` contained a dot character (`.`),  any part of the name to the right of the dot was not extracted. For example, from `$params["org.ipsum.lorem"]`, only `org` was extracted.
+
This update fixes the issue so that `$params` fetches the complete value. For example, `$params["org.ipsum.lorem"]` and `$params['org.ipsum.lorem']` are valid and the entire value of `<NAME>`, `org.ipsum.lorem`, is extracted.
+
It also throws an error if `<NAME>` is not enclosed in single or double quotes. For example, `$params.org.ipsum.lorem` is not valid and generates a validation error.
// (#1383)
// @savitaashture

// .CLI

* Before this update, the `tkn version` command for {tekton-chains} and Operator components did not work correctly. This update fixes the issue so that the command works correctly and returns version information for those components.
// source,terminal
----
error updating rolebinding openshift-operators-prometheus-k8s-read-binding: RoleBinding.rbac.authorization.k8s.io
"openshift-operators-prometheus-k8s-read-binding" is invalid:
roleRef: Invalid value: rbac.RoleRef{APIGroup:"rbac.authorization.k8s.io", Kind:"Role", Name:"openshift-operator-read"}: cannot change roleRef
----
+
This update fixes the issue so that the failure no longer occurs.
// (borrowed from 1.7.2 release notes) https://issues.redhat.com/browse/SRVKP-2327
// Khurram Baig

* Previously, upgrading the {pipelines-title} Operator caused the `pipeline` service account to be recreated, which meant that the secrets linked to the service account were lost. This update fixes the issue. During upgrades, the Operator no longer recreates the `pipeline` service account. As a result, secrets attached to the `pipeline` service account persist after upgrades, and the resources (tasks and pipelines) continue to work correctly.
// SRVKP-2160)
// Pradeep Kumar

* In {tekton-chains}, you must define a secret called `signing-secrets` to hold the key used for signing tasks and images. However, before this update, updating the {pipelines-title} Operator reset or overwrote this secret, and the key was lost. This update fixes the issue. Now, if the secret is configured after installing {tekton-chains} through the Operator, the secret persists, and it is not overwritten by upgrades.
// source,terminal
----
Error: error writing "0 0 4294967295\n" to /proc/22/uid_map: write /proc/22/uid_map: operation not permitted
time="2022-03-04T09:47:57Z" level=error msg="error writing \"0 0 4294967295\\n\" to /proc/22/uid_map: write /proc/22/uid_map: operation not permitted"
time="2022-03-04T09:47:57Z" level=error msg="(unable to determine exit status)"
----
+
With this update, the `pipelines-scc` security context constraint (SCC) is compatible with the `SETFCAP` capability necessary for `Buildah` and `S2I` cluster tasks. As a result, the `Buildah` and `S2I` build tasks can run successfully.
+
To successfully run the `Buildah` cluster task and `S2I` build tasks for applications written in various languages and frameworks, add the following snippet for appropriate `steps` objects such as `build` and `push`:
+
[source,yaml]
----
securityContext:
  capabilities:
    add: ["SETFCAP"]
----
+
// (borrowed from 1.7.2 release notes) https://issues.redhat.com/browse/SRVKP-2091
// Piyush Garg

* Before this update, installing the {pipelines-title} Operator took longer than expected. This update optimizes some settings to speed up the installation process.
// id="release-notes-1-8-1_{context}"
== Release notes for {pipelines-title} General Availability 1.8.1

With this update, {pipelines-title} General Availability (GA) 1.8.1 is available on OpenShift Container Platform 4.10, 4.11, and 4.12.

[id="known-issues-1-8-1_{context}"]
=== Known issues

* By default, the containers have restricted permissions for enhanced security. The restricted permissions apply to all controller pods in the {pipelines-title} Operator, and to some cluster tasks. Due to restricted permissions, the `git-clone` cluster task fails under certain configurations.
+
Workaround: None. You can track the issue SRVKP-2634.

* When installer sets are in a failed state, the status of the `TektonConfig` custom resource is incorrectly displayed as `True` instead of `False`.
+
.Example: Failed installer sets
[source,terminal]
----
$ oc get tektoninstallerset
NAME                                     READY   REASON
addon-clustertasks-nx5xz                 False   Error
addon-communityclustertasks-cfb2p        True
addon-consolecli-ftrb8                   True
addon-openshift-67dj2                    True
addon-pac-cf7pz                          True
addon-pipelines-fvllm                    True
addon-triggers-b2wtt                     True
addon-versioned-clustertasks-1-8-hqhnw   False   Error
pipeline-w75ww                           True
postpipeline-lrs22                       True
prepipeline-ldlhw                        True
rhosp-rbac-4dmgb                         True
trigger-hfg64                            True
validating-mutating-webhoook-28rf7       True
----
+
.Example: Incorrect `TektonConfig` status
[source,terminal]
----
$ oc get tektonconfig config
NAME     VERSION   READY   REASON
config   1.8.1     True
----

// https://issues.redhat.com/browse/SRVKP-2556

[id="fixed-issues-1-8-1_{context}"]
=== Fixed issues

* Before this update, the pruner deleted task runs of running pipelines and displayed the following warning: `some tasks were indicated completed without ancestors being done`. With this update, the pruner retains the task runs that are part of running pipelines.
// https://issues.redhat.com/browse/SRVKP-2419

* Before this update, `pipeline-1.8` was the default channel for installing the {pipelines-title} Operator 1.8.x. With this update, `latest` is the default channel.
// https://issues.redhat.com/browse/SRVKP-2412

* Before this update, the {pac} controller pods did not have access to certificates exposed by the user. With this update, {pac} can now access routes and Git repositories guarded by a self-signed or a custom certificate.
// https://issues.redhat.com/browse/SRVKP-2470

* Before this update, the task failed with RBAC errors after upgrading from {pipelines-title} 1.7.2 to 1.8.0. With this update, the tasks run successfully without any RBAC errors.
// https://issues.redhat.com/browse/SRVKP-2472

* Before this update, using the `tkn` CLI tool, you could not remove task runs and pipeline runs that contained a `result` object whose type was `array`. With this update, you can use the `tkn` CLI tool to remove task runs and pipeline runs that contain a `result` object whose type is `array`.
// https://issues.redhat.com/browse/SRVKP-2478

* Before this update, if a pipeline specification contained a task with an `ENV_VARS` parameter of `array` type, the pipeline run failed with the following error: `invalid input params for task func-buildpacks: param types do not match the user-specified type: [ENV_VARS]`. With this update, pipeline runs with such pipeline and task specifications do not fail.
// https://issues.redhat.com/browse/SRVKP-2422

* Before this update, cluster administrators could not provide a `config.json` file to the `Buildah` cluster task for accessing a container registry. With this update, cluster administrators can provide the `Buildah` cluster task with a `config.json` file by using the `dockerconfig` workspace.
// https://issues.redhat.com/browse/SRVKP-2424

[id="release-notes-1-8-2_{context}"]
== Release notes for {pipelines-title} General Availability 1.8.2

With this update, {pipelines-title} General Availability (GA) 1.8.2 is available on OpenShift Container Platform 4.10, 4.11, and 4.12.

[id="fixed-issues-1-8-2_{context}"]
=== Fixed issues

* Before this update, the `git-clone` task failed when cloning a repository using SSH keys. With this update, the role of the non-root user in the `git-init` task is removed, and the SSH program looks in the `$HOME/.ssh/` directory for the correct keys.
// https://issues.redhat.com/browse/SRVKP-2634

// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc
[id="op-release-notes-1-7_{context}"]
= Release notes for {pipelines-title} General Availability 1.7

With this update, {pipelines-title} General Availability (GA) 1.7 is available on OpenShift Container Platform 4.9, 4.10, and 4.11.

[id="new-features-1-7_{context}"]
== New features

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.7.

[id="pipelines-new-features-1-7_{context}"]
=== Pipelines

* With this update, `pipelines-<version>` is the default channel to install the {pipelines-title} Operator. For example, the default channel to install the {pipelines-shortname} Operator version `1.7` is `pipelines-1.7`. Cluster administrators can also use the `latest` channel to install the most recent stable version of the Operator.
+
[NOTE]
====
The `preview` and `stable` channels will be deprecated and removed in a future release.
====

* When you run a command in a user namespace, your container runs as `root` (user id `0`) but has user privileges on the host. With this update, to run pods in the user namespace, you must pass the annotations that CRI-O expects.
** To add these annotations for all users, run the `oc edit clustertask buildah` command and edit the `buildah` cluster task.
** To add the annotations to a specific namespace, export the cluster task as a task to that namespace.
// https://issues.redhat.com/browse/SRVKP-1514

* Before this update, if certain conditions were not met, the `when` expression skipped a `Task` object and its dependent tasks. With this update, you can scope the `when` expression to guard the `Task` object only, not its dependent tasks. To enable this update, set the `scope-when-expressions-to-task` flag to `true` in the `TektonConfig` CRD.
+
[NOTE]
====
The `scope-when-expressions-to-task` flag is deprecated and will be removed in a future release. As a best practice for {pipelines-shortname}, use `when` expressions scoped to the guarded `Task` only.
====
// https://github.com/tektoncd/pipeline/pull/4580

* With this update, you can use variable substitution in the `subPath` field of a workspace within a task.
// https://github.com/tektoncd/pipeline/pull/4351

* With this update, you can reference parameters and results by using a bracket notation with single or double quotes. Prior to this update, you could only use the dot notation. For example, the following are now equivalent:
** `$(param.myparam)`, `$(param['myparam'])`, and `$(param["myparam"])`.
+
You can use single or double quotes to enclose parameter names that contain problematic characters, such as `"."`. For example, `$(param['my.param'])` and `$(param["my.param"])`.
// https://github.com/tektoncd/pipeline/pull/4268

* With this update, you can include the `onError` parameter of a step in the task definition without enabling the `enable-api-fields` flag.
// https://github.com/tektoncd/pipeline/pull/4251

[id="triggers-new-features-1-7_{context}"]
=== Triggers

* With this update, the `feature-flag-triggers` config map has a new field `labels-exclusion-pattern`. You can set the value of this field to a regular expression (regex) pattern. The controller filters out labels that match the regex pattern from propagating from the event listener to the resources created for the event listener.
// https://github.com/tektoncd/triggers/pull/1227

* With this update, the `TriggerGroups` field is added to the `EventListener` specification. Using this field, you can specify a set of interceptors to run before selecting and running a group of triggers. To enable this feature, in the `TektonConfig` custom resource definition, in the `pipeline` section, you must set the `enable-api-fields` field to `alpha`.
// https://github.com/tektoncd/triggers/pull/1232

* With this update, `Trigger` resources support custom runs defined by a `TriggerTemplate` template.
// https://github.com/tektoncd/triggers/pull/1283/files

* With this update, Triggers support emitting Kubernetes events from an `EventListener` pod.
// https://github.com/tektoncd/triggers/pull/1222

* With this update, count metrics are available for the following objects: `ClusterInteceptor`, `EventListener`, `TriggerTemplate`, `ClusterTriggerBinding`, and `TriggerBinding`.
// https://github.com/tektoncd/triggers/pull/1305

* This update adds the `ServicePort` specification to Kubernetes resource. You can use this specification to modify which port exposes the event listener service. The default port is `8080`.
// https://github.com/tektoncd/triggers/pull/1272

* With this update, you can use the `targetURI` field in the `EventListener` specification to send cloud events during trigger processing. To enable this feature, in the `TektonConfig` custom resource definition, in the `pipeline` section, you must set the `enable-api-fields` field to `alpha`.
// https://github.com/tektoncd/triggers/pull/1259

* With this update, the `tekton-triggers-eventlistener-roles` object now has a `patch` verb, in addition to the `create` verb that already exists.
// https://github.com/tektoncd/triggers/pull/1291

* With this update, the `securityContext.runAsUser` parameter is removed from event listener deployment.
// https://github.com/tektoncd/triggers/pull/1213

[id="cli-new-features-1-7_{context}"]
=== CLI

* With this update, the `tkn [pipeline | pipelinerun] export` command exports a pipeline or pipeline run as a YAML file. For example:
** Export a pipeline named `test_pipeline` in the `openshift-pipelines` namespace:
+
[source,terminal]
----
$ tkn pipeline export test_pipeline -n openshift-pipelines
----
** Export a pipeline run named `test_pipeline_run` in the `openshift-pipelines` namespace:
+
[source,terminal]
----
$ tkn pipelinerun export test_pipeline_run -n openshift-pipelines
----
// https://github.com/tektoncd/cli/pull/1398 and https://github.com/tektoncd/cli/pull/1500

* With this update, the `--grace` option is added to the `tkn pipelinerun cancel`. Use the `--grace` option to terminate a pipeline run gracefully instead of forcing the termination. To enable this feature, in the `TektonConfig` custom resource definition, in the `pipeline` section, you must set the `enable-api-fields` field to `alpha`.
// https://github.com/tektoncd/cli/pull/1479

* This update adds the Operator and Chains versions to the output of the `tkn version` command.
+
[IMPORTANT]
====
Tekton Chains is a Technology Preview feature.
====
// https://github.com/tektoncd/cli/pull/1486 and https://github.com/tektoncd/cli/pull/1509

* With this update, the `tkn pipelinerun describe` command displays all canceled task runs, when you cancel a pipeline run. Before this fix, only one task run was displayed.
// https://github.com/tektoncd/cli/pull/1482

* With this update, you can skip supplying the asking specifications for optional workspace when you run the `tkn [t | p | ct] start` command skips with the `--skip-optional-workspace` flag. You can also skip it when running in interactive mode.
// https://github.com/tektoncd/cli/pull/1465

* With this update, you can use the `tkn chains` command to manage Tekton Chains. You can also use the `--chains-namespace` option to specify the namespace where you want to install Tekton Chains.
+
[IMPORTANT]
====
Tekton Chains is a Technology Preview feature.
====
// https://github.com/tektoncd/cli/pull/1440 and https://github.com/tektoncd/cli/pull/1522

[id="operator-new-features-1-7_{context}"]
=== Operator

* With this update, you can use the {pipelines-title} Operator to install and deploy Tekton Hub and Tekton Chains.
+
[IMPORTANT]
====
Tekton Chains and deployment of Tekton Hub on a cluster are Technology Preview features.
====
// https://github.com/tektoncd/operator/pull/467, https://github.com/tektoncd/operator/pull/479, https://github.com/tektoncd/operator/pull/467, https://github.com/tektoncd/operator/pull/630, and https://github.com/tektoncd/operator/pull/630

* With this update, you can find and use Pipelines as Code (PAC) as an add-on option.
+
[IMPORTANT]
====
Pipelines as Code is a Technology Preview feature.
====
// https://github.com/tektoncd/operator/pull/550

* With this update, you can now disable the installation of community cluster tasks by setting the `communityClusterTasks` parameter to `false`. For example:
+
[source,yaml]
----
...
spec:
  profile: all
  targetNamespace: openshift-pipelines
  addon:
    params:
    - name: clusterTasks
      value: "true"
    - name: pipelineTemplates
      value: "true"
    - name: communityClusterTasks
      value: "false"
...
----
// https://github.com/tektoncd/operator/pull/658

* With this update, you can disable the integration of Tekton Hub with the **Developer** perspective by setting the `enable-devconsole-integration` flag in the `TektonConfig` custom resource to `false`. For example:
+
[source,yaml]
----
...
hub:
  params:
    - name: enable-devconsole-integration
      value: "true"
...
----
// https://github.com/tektoncd/operator/pull/569

* With this update, the `operator-config.yaml` config map enables the output of the `tkn version` command to display of the Operator version.
// https://github.com/tektoncd/operator/pull/563

* With this update, the version of the `argocd-task-sync-and-wait` tasks is modified to `v0.2`.
// https://github.com/tektoncd/operator/pull/642

* With this update to the `TektonConfig` CRD, the `oc get tektonconfig` command displays the OPerator version.
// https://github.com/tektoncd/operator/pull/644

* With this update, service monitor is added to the Triggers metrics.
// https://github.com/tektoncd/operator/pull/635

[id="hub-new-features-1-7_{context}"]
=== Hub

[IMPORTANT]
====
Deploying Tekton Hub on a cluster is a Technology Preview feature.
====

Tekton Hub helps you discover, search, and share reusable tasks and pipelines for your CI/CD workflows. A public instance of Tekton Hub is available at hub.tekton.dev.

Staring with {pipelines-title} 1.7, cluster administrators can also install and deploy a custom instance of Tekton Hub on enterprise clusters. You can curate a catalog with reusable tasks and pipelines specific to your organization.

[id="chains-new-features-1-7_{context}"]
=== Chains

[IMPORTANT]
====
Tekton Chains is a Technology Preview feature.
====

Tekton Chains is a Kubernetes Custom Resource Definition (CRD) controller. You can use it to manage the supply chain security of the tasks and pipelines created using {pipelines-title}.

By default, Tekton Chains monitors the task runs in your OpenShift Container Platform cluster. Chains takes snapshots of completed task runs, converts them to one or more standard payload formats, and signs and stores all artifacts.

Tekton Chains supports the following features:

* You can sign task runs, task run results, and OCI registry images with cryptographic key types and services such as `cosign`.

* You can use attestation formats such as `in-toto`.

* You can securely store signatures and signed artifacts using OCI repository as a storage backend.

[id="pac-new-features-1-7_{context}"]
=== Pipelines as Code (PAC)

[IMPORTANT]
====
Pipelines as Code is a Technology Preview feature.
====

With Pipelines as Code, cluster administrators and users with the required privileges can define pipeline templates as part of source code Git repositories. When triggered by a source code push or a pull request for the configured Git repository, the feature runs the pipeline and reports status.

Pipelines as Code supports the following features:

* Pull request status. When iterating over a pull request, the status and control of the pull request is exercised on the platform hosting the Git repository.

* GitHub checks the API to set the status of a pipeline run, including rechecks.

* GitHub pull request and commit events.

* Pull request actions in comments, such as `/retest`.

* Git events filtering, and a separate pipeline for each event.

* Automatic task resolution in {pipelines-shortname} for local tasks, Tekton Hub, and remote URLs.

* Use of GitHub blobs and objects API for retrieving configurations.

* Access Control List (ACL) over a GitHub organization, or using a Prow-style `OWNER` file.

* The `tkn pac` plugin for the `tkn` CLI tool, which you can use to manage {pac} repositories and bootstrapping.

* Support for GitHub Application, GitHub Webhook, Bitbucket Server, and Bitbucket Cloud.

[id="deprecated-features-1-7_{context}"]
== Deprecated features

// Pipelines
* Breaking change: This update removes the `disable-working-directory-overwrite` and `disable-home-env-overwrite` fields from the `TektonConfig` custom resource (CR). As a result, the `TektonConfig` CR no longer automatically sets the `$HOME` environment variable and `workingDir` parameter. You can still set the `$HOME` environment variable and `workingDir` parameter by using the `env` and `workingDir` fields in the `Task` custom resource definition (CRD).

// https://github.com/tektoncd/pipeline/pull/4587

* The `Conditions` custom resource definition (CRD) type is deprecated and planned to be removed in a future release. Instead, use the recommended `When` expression.
// issue # unknown; discussed in Slack.

// Triggers
* Breaking change: The `Triggers` resource validates the templates and generates an error if you do not specify the `EventListener` and `TriggerBinding` values.
// https://github.com/tektoncd/triggers/pull/1277 and https://github.com/tektoncd/triggers/pull/1264

[id="known-issues-1-7_{context}"]
== Known issues

* When you run Maven and Jib-Maven cluster tasks, the default container image is supported only on Intel (x86) architecture. Therefore, tasks will fail on ARM, {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) clusters. As a workaround, you can specify a custom image by setting the `MAVEN_IMAGE` parameter value to `maven:3.6.3-adoptopenjdk-11`.
// issue # is unknown.
+
[TIP]
====
Before you install tasks that are based on the Tekton Catalog on ARM, {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) using `tkn hub`, verify if the task can be executed on these platforms. To check if `ppc64le` and `s390x` are listed in the "Platforms" section of the task information, you can run the following command: `tkn hub info task <name>`
// issue # is unknown.
====

* On {ibm-power-name} Systems, {ibm-z-name}, and {ibm-linuxone-name}, the `s2i-dotnet` cluster task is unsupported.
// issue # is unknown.

* You cannot use the `nodejs:14-ubi8-minimal` image stream because doing so generates the following errors:
+
[source,terminal]
----
STEP 7: RUN /usr/libexec/s2i/assemble
/bin/sh: /usr/libexec/s2i/assemble: No such file or directory
subprocess exited with status 127
subprocess exited with status 127
error building at STEP "RUN /usr/libexec/s2i/assemble": exit status 127
time="2021-11-04T13:05:26Z" level=error msg="exit status 127"
----
// https://issues.redhat.com/browse/SRVKP-1782

// Pipelines
* Implicit parameter mapping incorrectly passes parameters from the top-level `Pipeline` or `PipelineRun` definitions to the `taskRef` tasks. Mapping should only occur from a top-level resource to tasks with in-line `taskSpec` specifications. This issue only affects clusters where this feature was enabled by setting the `enable-api-fields` field to `alpha` in the `pipeline` section of the `TektonConfig` custom resource definition.

[id="fixed-issues-1-7_{context}"]
== Fixed issues

// Pipelines
* With this update, if metadata such as `labels` and `annotations` are present in both `Pipeline` and `PipelineRun` object definitions, the values in the `PipelineRun` type takes precedence. You can observe similar behavior for `Task` and `TaskRun` objects.
// https://github.com/tektoncd/pipeline/pull/4638

* With this update, if the `timeouts.tasks` field or the `timeouts.finally` field is set to `0`, then the `timeouts.pipeline` is also set to `0`.
// https://github.com/tektoncd/pipeline/pull/4539

* With this update, the `-x` set flag is removed from scripts that do not use a shebang. The fix reduces potential data leak from script execution.
// https://github.com/tektoncd/pipeline/pull/4451

* With this update, any backslash character present in the usernames in Git credentials is escaped with an additional backslash in the `.gitconfig` file.
// https://github.com/tektoncd/pipeline/pull/4337

// Triggers
* With this update, the `finalizer` property of the `EventListener` object is not necessary for cleaning up logging and config maps.
// https://github.com/tektoncd/triggers/pull/1244

* With this update, the default HTTP client associated with the event listener server is removed, and a custom HTTP client added. As a result, the timeouts have improved.
// https://github.com/tektoncd/triggers/pull/1308

* With this update, the Triggers cluster role now works with owner references.
// https://github.com/tektoncd/triggers/pull/1267

* With this update, the race condition in the event listener does not happen when multiple interceptors return extensions.
// https://github.com/tektoncd/triggers/pull/1282

// CLI
* With this update, the `tkn pr delete` command does not delete the pipeline runs with the `ignore-running` flag.
// https://github.com/tektoncd/cli/pull/1532

// Operator
* With this update, the Operator pods do not continue restarting when you modify any add-on parameters.
// https://github.com/tektoncd/operator/pull/631

* With this update, the `tkn serve` CLI pod is scheduled on infra nodes, if not configured in the subscription and config custom resources.
// https://github.com/tektoncd/operator/pull/544

* With this update, cluster tasks with specified versions are not deleted during upgrade.
// https://github.com/tektoncd/operator/pull/599

[id="release-notes-1-7-1_{context}"]
== Release notes for {pipelines-title} General Availability 1.7.1

With this update, {pipelines-title} General Availability (GA) 1.7.1 is available on OpenShift Container Platform 4.9, 4.10, and 4.11.

[id="fixed-issues-1-7-1_{context}"]
=== Fixed issues

* Before this update, upgrading the {pipelines-title} Operator deleted the data in the database associated with {tekton-hub} and installed a new database. With this update, an Operator upgrade preserves the data.
// https://issues.redhat.com/browse/SRVKP-2280

* Before this update, only cluster administrators could access pipeline metrics in the OpenShift Container Platform console. With this update, users with other cluster roles also can access the pipeline metrics.
// https://issues.redhat.com/browse/SRVKP-2129

* Before this update, pipeline runs failed for pipelines containing tasks that emit large termination messages. The pipeline runs failed because the total size of termination messages of all containers in a pod cannot exceed 12 KB. With this update, the `place-tools` and `step-init` initialization containers that uses the same image are merged to reduce the number of containers running in each tasks's pod. The solution reduces the chance of failed pipeline runs by minimizing the number of containers running in a task's pod. However, it does not remove the limitation of the maximum allowed size of a termination message.
// https://issues.redhat.com/browse/SRVKP-2243

* Before this update, attempts to access resource URLs directly from the {tekton-hub} web console resulted in an Nginx `404` error. With this update, the {tekton-hub} web console image is fixed to allow accessing resource URLs directly from the {tekton-hub} web console.
// https://issues.redhat.com/browse/SRVKP-2196

* Before this update, for each namespace the resource pruner job created a separate container to prune resources. With this update, the resource pruner job runs commands for all namespaces as a loop in one container.
// https://issues.redhat.com/browse/SRVKP-2160

[id="release-notes-1-7-2_{context}"]
== Release notes for {pipelines-title} General Availability 1.7.2

With this update, {pipelines-title} General Availability (GA) 1.7.2 is available on OpenShift Container Platform 4.9, 4.10, and the upcoming version.

[id="known-issues-1-7-2_{context}"]
=== Known issues

* The `chains-config` config map for {tekton-chains} in the `openshift-pipelines` namespace is automatically reset to default after upgrading the {pipelines-title} Operator. Currently, there is no workaround for this issue.
// https://issues.redhat.com/browse/SRVKP-2349

[id="fixed-issues-1-7-2_{context}"]
=== Fixed issues

* Before this update, tasks on {pipelines-shortname} 1.7.1 failed on using `init` as the first argument, followed by two or more arguments. With this update, the flags are parsed correctly and the task runs are successful.
// https://issues.redhat.com/browse/SRVKP-2340

* Before this update, installation of the {pipelines-title} Operator on OpenShift Container Platform 4.9 and 4.10 failed due to invalid role binding, with the following error message:
+
[source,terminal]
----
error updating rolebinding openshift-operators-prometheus-k8s-read-binding: RoleBinding.rbac.authorization.k8s.io "openshift-operators-prometheus-k8s-read-binding" is invalid: roleRef: Invalid value: rbac.RoleRef{APIGroup:"rbac.authorization.k8s.io", Kind:"Role", Name:"openshift-operator-read"}: cannot change roleRef
----
+
With this update, the {pipelines-title} Operator installs with distinct role binding namespaces to avoid conflict with installation of other Operators.
// https://issues.redhat.com/browse/SRVKP-2327

* Before this update, upgrading the Operator triggered a reset of the `signing-secrets` secret key for {tekton-chains} to its default value. With this update, the custom secret key persists after you upgrade the Operator.
+
[NOTE]
====
Upgrading to {pipelines-title} 1.7.2 resets the key. However, when you upgrade to future releases, the key is expected to persist.
====
+
// https://issues.redhat.com/browse/SRVKP-2304

* Before this update, all S2I build tasks failed with an error similar to the following message:
+
[source,terminal]
----
Error: error writing "0 0 4294967295\n" to /proc/22/uid_map: write /proc/22/uid_map: operation not permitted
time="2022-03-04T09:47:57Z" level=error msg="error writing \"0 0 4294967295\\n\" to /proc/22/uid_map: write /proc/22/uid_map: operation not permitted"
time="2022-03-04T09:47:57Z" level=error msg="(unable to determine exit status)"
----
+
With this update, the `pipelines-scc` security context constraint (SCC) is compatible with the `SETFCAP` capability necessary for `Buildah` and `S2I` cluster tasks. As a result, the `Buildah` and `S2I` build tasks can run successfully.
+
To successfully run the `Buildah` cluster task and `S2I` build tasks for applications written in various languages and frameworks, add the following snippet for appropriate `steps` objects such as `build` and `push`:
+
[source,yaml]
----
securityContext:
  capabilities:
    add: ["SETFCAP"]
----
+
// https://issues.redhat.com/browse/SRVKP-2091

[id="release-notes-1-7-3_{context}"]
== Release notes for {pipelines-title} General Availability 1.7.3

With this update, {pipelines-title} General Availability (GA) 1.7.3 is available on OpenShift Container Platform 4.9, 4.10, and 4.11.

[id="fixed-issues-1-7-3_{context}"]
=== Fixed issues

* Before this update, the Operator failed when creating RBAC resources if any namespace was in a `Terminating` state. With this update, the Operator ignores namespaces in a `Terminating` state and creates the RBAC resources.
// id="op-release-notes-1-6_{context}"
= Release notes for {pipelines-title} General Availability 1.6

With this update, {pipelines-title} General Availability (GA) 1.6 is available on OpenShift Container Platform 4.9.

[id="new-features-1-6_{context}"]
== New features

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.6.

//[id="new-features-cli-0-21-0-release-1-6_{context}"]
//=== CLI

* With this update, you can configure a pipeline or task `start` command to return a YAML or JSON-formatted string by using the `--output <string>`, where `<string>` is `yaml` or `json`. Otherwise, without the `--output` option, the `start` command returns a human-friendly message that is hard for other programs to parse. Returning a YAML or JSON-formatted string is useful for continuous integration (CI) environments. For example, after a resource is created, you can use `yq` or `jq` to parse the YAML or JSON-formatted message about the resource and wait until that resource is terminated without using the `showlog` option.
// (#1326)

* With this update, you can authenticate to a registry using the `auth.json` authentication file of Podman. For example, you can use `tkn bundle push` to push to a remote registry using Podman instead of Docker CLI.
// (#1430)

* With this update, if you use the `tkn [taskrun | pipelinerun] delete --all` command, you can preserve runs that are younger than a specified number of minutes by using the new `--keep-since <minutes>` option. For example, to keep runs that are less than five minutes old, you enter `tkn [taskrun | pipelinerun] delete -all --keep-since 5`.
// (#1435)

* With this update, when you delete task runs or pipeline runs, you can use the `--parent-resource` and `--keep-since` options together. For example, the `tkn pipelinerun delete --pipeline pipelinename --keep-since 5` command preserves pipeline runs whose parent resource is named `pipelinename` and whose age is five minutes or less. The `tkn tr delete -t <taskname> --keep-since 5` and `tkn tr delete --clustertask <taskname> --keep-since 5` commands work similarly for task runs.
// (#1443)

* This update adds support for the triggers resources to work with `v1beta1` resources.

// (#1446, #1449, #1450, #1454, #1455)

* This update adds an `ignore-running` option to the `tkn pipelinerun delete` and `tkn taskrun delete` commands.
// (#1445)

* This update adds a `create` subcommand to the `tkn task` and `tkn clustertask` commands.
// (#1359)

* With this update, when you use the `tkn pipelinerun delete --all` command, you can use the new `--label <string>` option to filter the pipeline runs by label. Optionally, you can use the `--label` option with `=` and `==` as equality operators, or `!=` as an inequality operator. For example, the `tkn pipelinerun delete --all --label asdf` and  `tkn pipelinerun delete --all --label==asdf` commands both delete all the pipeline runs that have the `asdf` label.
// (#1402)

* With this update, you can fetch the version of installed Tekton components from the config map or, if the config map is not present, from the deployment controller.
//  (#1393)

//[id="new-features-tekton-triggers-0-16-0-release-1-6_{context}"]
//=== Tekton Triggers

* With this update, triggers support the `feature-flags` and `config-defaults` config map to configure feature flags and to set default values respectively.
//  (#1182, #1110)

* This update adds a new metric, `eventlistener_event_count`, that you can use to count events received by the `EventListener` resource.
//  (#1160)

* This update adds `v1beta1` Go API types. With this update, triggers now support the `v1beta1` API version.
+
With the current release, the `v1alpha1` features are now deprecated and will be removed in a future release. Begin using the `v1beta1` features instead.
//  (#1103)

//[id="new-features-pipelines-operator-1-6_{context}"]
//=== {pipelines-title} Operator

* In the current release, auto-prunning of resources is enabled by default. In addition, you can configure auto-prunning of task run and pipeline run for each namespace separately, by using the following new annotations:

** `operator.tekton.dev/prune.schedule`: If the value of this annotation is different from the value specified at the `TektonConfig` custom resource definition, a new cron job in that namespace is created.
** `operator.tekton.dev/prune.skip`: When set to `true`, the namespace for which it is configured will not be prunned.
** `operator.tekton.dev/prune.resources`: This annotation accepts a comma-separated list of resources. To prune a single resource such as a pipeline run, set this annotation to `"pipelinerun"`. To prune multiple resources, such as task run and pipeline run, set this annotation to `"taskrun, pipelinerun"`.
** `operator.tekton.dev/prune.keep`: Use this annotation to retain a resource without prunning.
** `operator.tekton.dev/prune.keep-since`: Use this annotation to retain resources based on their age. The value for this annotation must be equal to the age of the resource in minutes. For example, to retain resources which were created not more than five days ago, set `keep-since` to `7200`.
+
[NOTE]
====
The `keep` and `keep-since` annotations are mutually exclusive. For any resource, you must configure only one of them.
====
+
** `operator.tekton.dev/prune.strategy`: Set the value of this annotation to either `keep` or `keep-since`.

* Administrators can disable the creation of the `pipeline` service account for the entire cluster, and prevent privilege escalation by misusing the associated SCC, which is very similar to `anyuid`.

* You can now configure feature flags and components by using the `TektonConfig` custom resource (CR) and the CRs for individual components, such as `TektonPipeline` and `TektonTriggers`. This level of granularity helps customize and test alpha features such as the Tekton OCI bundle for individual components.

* You can now configure optional `Timeouts` field for the `PipelineRun` resource. For example, you can configure timeouts separately for a pipeline run, each task run, and the `finally` tasks.

* The pods generated by the `TaskRun` resource now sets the `activeDeadlineSeconds` field of the pods. This enables OpenShift to consider them as terminating, and allows you to use specifically scoped `ResourceQuota` object for the pods.

* You can use configmaps to eliminate metrics tags or labels type on a task run, pipeline run, task, and pipeline. In addition, you can configure different types of metrics for measuring duration, such as a histogram, gauge, or last value.

* You can define requests and limits on a pod coherently, as Tekton now fully supports the `LimitRange` object by considering the `Min`, `Max`, `Default`, and `DefaultRequest` fields.

* The following alpha features are introduced:

** A pipeline run can now stop after running the `finally` tasks, rather than the previous behavior of stopping the execution of all task run directly. This update adds the following `spec.status` values:

*** `StoppedRunFinally` will stop the currently running tasks after they are completed, and then run the `finally` tasks.
*** `CancelledRunFinally` will immediately cancel the running tasks, and then run the `finally` tasks.
*** `Cancelled` will retain the previous behavior provided by the `PipelineRunCancelled` status.
+
[NOTE]
====
The `Cancelled` status replaces the deprecated `PipelineRunCancelled` status, which will be removed in the `v1` version.
====
+

** You can now use the `oc debug` command to put a task run into debug mode, which pauses the execution and allows you to inspect specific steps in a pod.

** When you set the `onError` field of a step to `continue`, the exit code for the step is recorded and passed on to subsequent steps. However, the task run does not fail and the execution of the rest of the steps in the task continues. To retain the existing behavior, you can set the value of the `onError` field to `stopAndFail`.

** Tasks can now accept more parameters than are actually used. When the alpha feature flag is enabled, the parameters can implicitly propagate to inlined specs. For example, an inlined task can access parameters of its parent pipeline run, without explicitly defining each parameter for the task.

** If you enable the flag for the alpha features, the conditions under `When` expressions will only apply to the task with which it is directly associated, and not the dependents of the task. To apply the `When` expressions to the associated task and its dependents, you must associate the expression with each dependent task separately. Note that, going forward, this will be the default behavior of the `When` expressions in any new API versions of Tekton. The existing default behavior will be deprecated in favor of this update.

* The current release enables you to configure node selection by specifying the `nodeSelector` and `tolerations` values in the `TektonConfig` custom resource (CR). The Operator adds these values to all the deployments that it creates.

** To configure node selection for the Operator's controller and webhook deployment, you edit the `config.nodeSelector` and `config.tolerations` fields in the specification for the `Subscription` CR, after installing the Operator.

** To deploy the rest of the control plane pods of {pipelines-shortname} on an infrastructure node, update the `TektonConfig` CR with the `nodeSelector` and `tolerations` fields. The modifications are then applied to all the pods created by Operator.

[id="deprecated-features-1-6_{context}"]
== Deprecated features

//[id="deprecated-cli-0-21-0-release-1-6_{context}"]
//=== CLI

* In CLI 0.21.0, support for all `v1alpha1` resources for `clustertask`, `task`, `taskrun`, `pipeline`, and `pipelinerun` commands are deprecated. These resources are now deprecated and will be removed in a future release.

//[id="deprecated-tekton-0-16-0-1-6_{context}"]
//=== Tekton Triggers

* In Tekton Triggers v0.16.0, the redundant `status` label is removed from the metrics for the `EventListener` resource.
//  (#1166)
+
[IMPORTANT]
====
Breaking change: The `status` label has been removed from the `eventlistener_http_duration_seconds_*` metric.
Remove queries that are based on the `status` label.
====

* With the current release, the `v1alpha1` features are now deprecated and will be removed in a future release. With this update, you can begin using the `v1beta1` Go API types instead. Triggers now supports the `v1beta1` API version.
//  (#1103)

* With the current release, the `EventListener` resource sends a response before the triggers finish processing.
//  (#1132)
+
[IMPORTANT]
====
Breaking change: With this change, the `EventListener` resource stops responding with a `201 Created` status code when it creates resources. Instead, it responds with a `202 Accepted` response code.
====

* The current release removes the `podTemplate` field from the `EventListener` resource.
//  (#1118)
+
[IMPORTANT]
====
Breaking change: The `podTemplate` field, which was deprecated as part of #1100, has been removed.
====

* The current release removes the deprecated `replicas` field from the specification for the `EventListener` resource.
//  (#1113)
+
[IMPORTANT]
====
Breaking change: The deprecated `replicas` field has been removed.
====

//[id="deprecated-features-pipelines-operator-1-6_{context}"]
//=== {pipelines-title} Operator

* In {pipelines-title} 1.6, the values of `HOME="/tekton/home"` and `workingDir="/workspace"` are removed from the specification of the `Step` objects.
+
Instead, {pipelines-title} sets `HOME` and `workingDir` to the values defined by the containers running the `Step` objects. You can override these values in the specification of your `Step` objects.
+
To use the older behavior, you can change the `disable-working-directory-overwrite` and `disable-home-env-overwrite` fields in the `TektonConfig` CR to `false`:
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
  kind: TektonConfig
  metadata:
    name: config
  spec:
    pipeline:
      disable-working-directory-overwrite: false
      disable-home-env-overwrite: false
  ...
----
+
[IMPORTANT]
====
The `disable-working-directory-overwrite` and `disable-home-env-overwrite` fields in the `TektonConfig` CR are now deprecated and will be removed in a future release.
====
// (SRVKP-1465)

[id="known-issues-1-6_{context}"]
== Known issues

* When you run Maven and Jib-Maven cluster tasks, the default container image is supported only on Intel (x86) architecture. Therefore, tasks will fail on {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) clusters. As a workaround, you can specify a custom image by setting the `MAVEN_IMAGE` parameter value to `maven:3.6.3-adoptopenjdk-11`.
// issue # is unknown.

* On {ibm-power-name} Systems, {ibm-z-name}, and {ibm-linuxone-name}, the `s2i-dotnet` cluster task is unsupported.
// issue # is unknown.

* Before you install tasks based on the Tekton Catalog on {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) using `tkn hub`, verify if the task can be executed on these platforms. To check if `ppc64le` and `s390x` are listed in the "Platforms" section of the task information, you can run the following command: `tkn hub info task <name>`
// issue # is unknown.

* You cannot use the `nodejs:14-ubi8-minimal` image stream because doing so generates the following errors:
+
[source,terminal]
----
STEP 7: RUN /usr/libexec/s2i/assemble
/bin/sh: /usr/libexec/s2i/assemble: No such file or directory
subprocess exited with status 127
subprocess exited with status 127
error building at STEP "RUN /usr/libexec/s2i/assemble": exit status 127
time="2021-11-04T13:05:26Z" level=error msg="exit status 127"
----
// https://issues.redhat.com/browse/SRVKP-1782

[id="fixed-issues-1-6_{context}"]
== Fixed issues

* The `tkn hub` command is now supported on {ibm-power-name}, {ibm-z-name}, and LinuxONE.
// issue # is unknown.

//[id="fixed-cli-0-21-0-1-6_{context}"]
//=== CLI

* Before this update, the terminal was not available after the user ran a `tkn` command, and the pipeline run was done, even if `retries` were specified. Specifying a timeout in the task run or pipeline run had no effect. This update fixes the issue so that the terminal is available after running the command.
//  (#1459)

* Before this update, running `tkn pipelinerun delete --all` would delete all resources. This update prevents the resources in the running state from getting deleted.
//  https://issues.redhat.com/browse/SRVKP-1638

* Before this update, using the `tkn version --component=<component>` command did not return the component version. This update fixes the issue so that this command returns the component version.
//  (https://github.com/tektoncd/cli/pull/1408[#1408])

* Before this update, when you used the `tkn pr logs` command, it displayed the pipelines output logs in the wrong task order. This update resolves the issue so that logs of completed `PipelineRuns` are listed in the appropriate `TaskRun` execution order.
//  (#1385)

//[id="fixed-pipelines-operator-1-6_{context}"]
//=== {pipelines-title} Operator

* Before this update, editing the specification of a running pipeline might prevent the pipeline run from stopping when it was complete. This update fixes the issue by fetching the definition only once and then using the specification stored in the status for verification. This change reduces the probability of a race condition when a `PipelineRun` or a `TaskRun` refers to a `Pipeline` or `Task` that changes while it is running.
//  (SRVKP-718)

* `When` expression values can now have array parameter references, such as: `values: [$(params.arrayParam[*])]`.

[id="release-notes-1-6-1_{context}"]
== Release notes for {pipelines-title} General Availability 1.6.1

[id="known-issues-1-6-1_{context}"]
=== Known issues

* After upgrading to {pipelines-title} 1.6.1 from an older version, {pipelines-shortname} might enter an inconsistent state where you are unable to perform any operations (create/delete/apply) on Tekton resources (tasks and pipelines). For example, while deleting a resource, you might encounter the following error:
+
[source,terminal]
----
Error from server (InternalError): Internal error occurred: failed calling webhook "validation.webhook.pipeline.tekton.dev": Post "https://tekton-pipelines-webhook.openshift-pipelines.svc:443/resource-validation?timeout=10s": service "tekton-pipelines-webhook" not found.
----

[id="fixed-issues-1-6-1_{context}"]
=== Fixed issues

* The `SSL_CERT_DIR` environment variable (`/tekton-custom-certs`) set by {pipelines-title} will not override the following default system directories with certificate files:
** `/etc/pki/tls/certs`
** `/etc/ssl/certs`
** `/system/etc/security/cacerts`
// https://issues.redhat.com/browse/SRVKP-1687

* The Horizontal Pod Autoscaler can manage the replica count of deployments controlled by the {pipelines-title} Operator. From this release onward, if the count is changed by an end user or an on-cluster agent, the {pipelines-title} Operator will not reset the replica count of deployments managed by it. However, the replicas will be reset when you upgrade the {pipelines-title} Operator.
// https://issues.redhat.com/browse/SRVKP-1783

* The pod serving the `tkn` CLI will now be scheduled on nodes, based on the node selector and toleration limits specified in the `TektonConfig` custom resource.
// https://issues.redhat.com/browse/SRVKP-1804

[id="release-notes-1-6-2_{context}"]
== Release notes for {pipelines-title} General Availability 1.6.2

[id="known-issues-1-6-2_{context}"]
=== Known issues

* When you create a new project, the creation of the `pipeline` service account is delayed, and removal of existing cluster tasks and pipeline templates takes more than 10 minutes.
// https://issues.redhat.com/browse/SRVKP-2043

[id="fixed-issues-1-6-2_{context}"]
=== Fixed issues

* Before this update, multiple instances of Tekton installer sets were created for a pipeline after upgrading to {pipelines-title} 1.6.1 from an older version. With this update, the Operator ensures that only one instance of each type of `TektonInstallerSet` exists after an upgrade.
// https://issues.redhat.com/browse/SRVKP-1926

* Before this update, all the reconcilers in the Operator used the component version to decide resource recreation during an upgrade to {pipelines-title} 1.6.1 from an older version. As a result, those resources were not recreated whose component versions did not change in the upgrade. With this update, the Operator uses the Operator version instead of the component version to decide resource recreation during an upgrade.
// https://issues.redhat.com/browse/SRVKP-1928

* Before this update, the pipelines webhook service was missing in the cluster after an upgrade. This was due to an upgrade deadlock on the config maps. With this update, a mechanism is added to disable webhook validation if the config maps are absent in the cluster. As a result, the pipelines webhook service persists in the cluster after an upgrade.
// https://issues.redhat.com/browse/SRVKP-1939

* Before this update, cron jobs for auto-pruning got recreated after any configuration change to the namespace. With this update, cron jobs for auto-pruning get recreated only if there is a relevant annotation change in the namespace.
// https://issues.redhat.com/browse/SRVKP-1826

* The upstream version of Tekton Pipelines is revised to `v0.28.3`, which has the following fixes:
** Fix `PipelineRun` or `TaskRun` objects to allow label or annotation propagation.
** For implicit params:
*** Do not apply the `PipelineSpec` parameters to the `TaskRefs` object.
*** Disable implicit param behavior for the `Pipeline` objects.
// https://github.com/tektoncd/pipeline/releases/tag/v0.28.3

[id="release-notes-1-6-3_{context}"]
== Release notes for {pipelines-title} General Availability 1.6.3

[id="fixed-issues-1-6-3_{context}"]
=== Fixed issues

* Before this update, the {pipelines-title} Operator installed pod security policies from components such as Pipelines and Triggers. However, the pod security policies shipped as part of the components were deprecated in an earlier release. With this update, the Operator stops installing pod security policies from components. As a result, the following upgrade paths are affected:
** Upgrading from {pipelines-shortname} 1.6.1 or 1.6.2 to {pipelines-shortname} 1.6.3 deletes the pod security policies, including those from the Pipelines and Triggers components.
** Upgrading from {pipelines-shortname} 1.5.x to 1.6.3 retains the pod security policies installed from components. As a cluster administrator, you can delete them manually.
+
[NOTE]
====
When you upgrade to future releases, the {pipelines-title} Operator will automatically delete all obsolete pod security policies.
====
// https://issues.redhat.com/browse/SRVKP-2259

* Before this update, only cluster administrators could access pipeline metrics in the OpenShift Container Platform console. With this update, users with other cluster roles also can access the pipeline metrics.
// https://issues.redhat.com/browse/SRVKP-2129

* Before this update, role-based access control (RBAC) issues with the {pipelines-shortname} Operator caused problems upgrading or installing components. This update improves the reliability and consistency of installing various {pipelines-title} components.
// https://issues.redhat.com/browse/SRVKP-2249

* Before this update, setting the `clusterTasks` and `pipelineTemplates` fields to `false` in the `TektonConfig` CR slowed the removal of cluster tasks and pipeline templates. This update improves the speed of lifecycle management of Tekton resources such as cluster tasks and pipeline templates.
// https://issues.redhat.com/browse/SRVKP-2043

[id="release-notes-1-6-4_{context}"]
== Release notes for {pipelines-title} General Availability 1.6.4

[id="known-issues-1-6-4_{context}"]
=== Known issues

* After upgrading from {pipelines-title} 1.5.2 to 1.6.4, accessing the event listener routes returns a `503` error.
+
Workaround: Modify the target port in the YAML file for the event listener's route.
+
. Extract the route name for the relevant namespace.
+
[source,terminal]
----
$ oc get route -n <namespace>
----
+
. Edit the route to modify the value of the `targetPort` field.
+
[source,terminal]
----
$ oc edit route -n <namespace> <el-route_name>
----
+
.Example: Existing event listener route
+
[source,yaml]
----
...
spec:
  host: el-event-listener-q8c3w5-test-upgrade1.apps.ve49aws.aws.ospqa.com
  port:
    targetPort: 8000
  to:
    kind: Service
    name: el-event-listener-q8c3w5
    weight: 100
  wildcardPolicy: None
...
----
+
.Example: Modified event listener route
+
[source,yaml]
----
...
spec:
  host: el-event-listener-q8c3w5-test-upgrade1.apps.ve49aws.aws.ospqa.com
  port:
    targetPort: http-listener
  to:
    kind: Service
    name: el-event-listener-q8c3w5
    weight: 100
  wildcardPolicy: None
...
----

// https://issues.redhat.com/browse/SRVKP-2502

[id="fixed-issues-1-6-4_{context}"]
=== Fixed issues

* Before this update, the Operator failed when creating RBAC resources if any namespace was in a `Terminating` state. With this update, the Operator ignores namespaces in a `Terminating` state and creates the RBAC resources.
// https://issues.redhat.com/browse/SRVKP-2248

* Before this update, the task runs failed or restarted due to absence of annotation specifying the release version of the associated Tekton controller. With this update, the inclusion of the appropriate annotations are automated, and the tasks run without failure or restarts.
// https://issues.redhat.com/browse/SRVKP-2445

// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc

[id="op-release-notes-1-5_{context}"]
= Release notes for {pipelines-title} General Availability 1.5

{pipelines-title} General Availability (GA) 1.5 is now available on OpenShift Container Platform 4.8.

[id="compatibility-support-matrix-1-5_{context}"]
== Compatibility and support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

In the table, features are marked with the following statuses:

[horizontal]
TP:: Technology Preview
GA:: General Availability

Note the following scope of support on the Red Hat Customer Portal for these features:

.Compatibility and support matrix
[cols="1,1,1",options="header"]
|===
| Feature | Version | Support Status
| Pipelines | 0.24 | GA
| CLI | 0.19 | GA
| Catalog | 0.24 | GA
| Triggers | 0.14 | TP
| Pipeline resources | - | TP
|===

For questions and feedback, you can send an email to the product team at pipelines-interest@redhat.com.

[id="new-features-1-5_{context}"]
== New features

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.5.

* Pipeline run and task runs will be automatically pruned by a cron job in the target namespace. The cron job uses the `IMAGE_JOB_PRUNER_TKN` environment variable to get the value of `tkn image`. With this enhancement, the following fields are introduced to the `TektonConfig` custom resource:
+
[source,yaml,subs="attributes+"]
----
...
pruner:
  resources:
    - pipelinerun
    - taskrun
  schedule: "*/5 * * * *" # cron schedule
  keep: 2 # delete all keeping n
...
----

* In OpenShift Container Platform, you can customize the installation of the Tekton Add-ons component by modifying the values of the new parameters `clusterTasks` and `pipelinesTemplates` in the `TektonConfig` custom resource:
+
[source,yaml,subs="attributes+"]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  profile: all
  targetNamespace: openshift-pipelines
  addon:
    params:
    - name: clusterTasks
      value: "true"
    - name: pipelineTemplates
      value: "true"
...
----
+
The customization is allowed if you create the add-on using `TektonConfig`, or directly by using Tekton Add-ons. However, if the parameters are not passed, the controller adds parameters with default values.
+
[NOTE]
====
* If add-on is created using the `TektonConfig` custom resource, and you change the parameter values later in the
`Addon` custom resource, then the values in the `TektonConfig` custom resource overwrites the changes.

* You can set the value of the `pipelinesTemplates` parameter to `true` only when the value of the `clusterTasks` parameter is `true`.
====

* The `enableMetrics` parameter is added to the `TektonConfig` custom resource. You can use it to disable the service monitor, which is part of Tekton Pipelines for OpenShift Container Platform.
+
[source,yaml,subs="attributes+"]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  profile: all
  targetNamespace: openshift-pipelines
  pipeline:
    params:
    - name: enableMetrics
      value: "true"
...
----

* Eventlistener OpenCensus metrics, which captures metrics at process level, is added.

* Triggers now has label selector; you can configure triggers for an event listener using labels.

* The `ClusterInterceptor` custom resource definition for registering interceptors is added, which allows you to register new `Interceptor` types that you can plug in. In addition, the following relevant changes are made:

** In the trigger specifications, you can configure interceptors using a new API that includes a `ref` field to refer to a cluster interceptor. In addition, you can use the `params` field to add parameters that pass on to the interceptors for processing.

** The bundled interceptors CEL, GitHub, GitLab, and BitBucket, have been migrated. They are implemented using the new `ClusterInterceptor` custom resource definition.

** Core interceptors are migrated to the new format, and any new triggers created using the old syntax automatically switch to the new `ref` or `params` based syntax.

* To disable prefixing the name of the task or step while displaying logs, use the `--prefix` option for `log` commands.

* To display the version of a specific component, use the new `--component` flag in the `tkn version` command.

* The `tkn hub check-upgrade` command is added, and other commands are revised to be based on the pipeline version. In addition, catalog names are displayed in the `search` command output.

* Support for optional workspaces are added to the `start` command.

* If the plugins are not present in the `plugins` directory, they are searched in the current path.

* The `tkn start [task | clustertask | pipeline]` command starts interactively and ask for the `params` value, even when you specify the default parameters are specified. To stop the interactive prompts, pass the `--use-param-defaults` flag at the time of invoking the command. For example:
+
[source,terminal,subs="attributes+"]
----
$ tkn pipeline start build-and-deploy \
    -w name=shared-workspace,volumeClaimTemplateFile=https://raw.githubusercontent.com/openshift/pipelines-tutorial/{pipelines-ver}/01_pipeline/03_persistent_volume_claim.yaml \
    -p deployment-name=pipelines-vote-api \
    -p git-url=https://github.com/openshift/pipelines-vote-api.git \
    -p IMAGE=image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/pipelines-vote-api \
    --use-param-defaults
----

* The `version` field is added in the `tkn task describe` command.

* The option to automatically select resources such as `TriggerTemplate`, or `TriggerBinding`, or `ClusterTriggerBinding`, or `Eventlistener`, is added in the `describe` command, if only one is present.

* In the `tkn pr describe` command, a section for skipped tasks is added.

* Support for the `tkn clustertask logs` is added.

* The YAML merge and variable from `config.yaml` is removed. In addition, the `release.yaml` file can now be more easily consumed by tools such as `kustomize` and `ytt`.

* The support for resource names to contain the dot character (".") is added.

* The `hostAliases` array in the `PodTemplate` specification is added to the pod-level override of hostname resolution. It is achieved by modifying the `/etc/hosts` file.

* A variable `$(tasks.status)` is introduced to access the aggregate execution status of tasks.

* An entry-point binary build for Windows is added.

[id="deprecated-features-1-5_{context}"]
== Deprecated features

* In the `when` expressions, support for fields written is PascalCase is removed. The `when` expressions only support fields written in lowercase.
+
[NOTE]
====
If you had applied a pipeline with `when` expressions in Tekton Pipelines `v0.16` (Operator `v1.2.x`), you have to reapply it.
====

* When you upgrade the {pipelines-title} Operator to `v1.5`, the `openshift-client` and the `openshift-client-v-1-5-0` cluster tasks have the `SCRIPT` parameter. However, the `ARGS` parameter and the `git` resource are removed from the specification of the `openshift-client` cluster task. This is a breaking change, and only those cluster tasks that do not have a specific version in the `name` field of the `ClusterTask` resource upgrade seamlessly.
+
To prevent the pipeline runs from breaking, use the `SCRIPT` parameter after the upgrade because it moves the values previously specified in the `ARGS` parameter into the `SCRIPT` parameter of the cluster task. For example:
+
[source,yaml,subs="attributes+"]
----
...
- name: deploy
  params:
  - name: SCRIPT
    value: oc rollout status <deployment-name>
  runAfter:
    - build
  taskRef:
    kind: ClusterTask
    name: openshift-client
...
----
+

* When you upgrade from {pipelines-title} Operator `v1.4` to `v1.5`, the profile names in which the `TektonConfig` custom resource is installed now change.

+
.Profiles for `TektonConfig` custom resource
[cols="1,1,1",options="header"]
|===
| Profiles in Pipelines 1.5 | Corresponding profile in Pipelines 1.4 | Installed Tekton components
| All (_default profile_) | All (_default profile_) | Pipelines, Triggers, Add-ons
| Basic | Default | Pipelines, Triggers
| Lite | Basic | Pipelines

|===

+
[NOTE]
====
If you used `profile: all` in the `config` instance of the `TektonConfig` custom resource, no change is necessary in the resource specification.

However, if the installed Operator is either in the Default or the Basic profile before the upgrade, you must edit the `config` instance of the `TektonConfig` custom resource after the upgrade. For example, if the configuration was `profile: basic` before the upgrade, ensure that it is `profile: lite` after upgrading to Pipelines 1.5.
====
+

* The `disable-home-env-overwrite` and `disable-working-dir-overwrite` fields are now deprecated and will be removed in a future release. For this release, the default value of these flags is set to `true` for backward compatibility.
+
[NOTE]
====
In the next release ({pipelines-title} 1.6), the `HOME` environment variable will not be automatically set to `/tekton/home`, and the default working directory will not be set to `/workspace` for task runs. These defaults collide with any value set by image Dockerfile of the step.
====

* The `ServiceType` and `podTemplate` fields are removed from the `EventListener` spec.

* The controller service account no longer requests cluster-wide permission to list and watch namespaces.

* The status of the `EventListener` resource has a new condition called `Ready`.
+
[NOTE]
====
In the future, the other status conditions for the `EventListener` resource will be deprecated in favor of the `Ready` status condition.
====

* The `eventListener` and `namespace` fields in the `EventListener` response are deprecated. Use the `eventListenerUID` field instead.

* The `replicas` field is deprecated from the `EventListener` spec. Instead, the `spec.replicas` field is moved to `spec.resources.kubernetesResource.replicas` in the `KubernetesResource` spec.
+
[NOTE]
====
The `replicas` field will be removed in a future release.
====

* The old method of configuring the core interceptors is deprecated. However, it continues to work until it is removed in a future release. Instead, interceptors in a `Trigger` resource are now configured using a new `ref` and `params` based syntax. The resulting default webhook automatically switch the usages of the old syntax to the new syntax for new triggers.

* Use `rbac.authorization.k8s.io/v1` instead of the deprecated `rbac.authorization.k8s.io/v1beta1` for the `ClusterRoleBinding` resource.

* In cluster roles, the cluster-wide write access to resources such as `serviceaccounts`, `secrets`, `configmaps`, and `limitranges` are removed. In addition, cluster-wide access to resources such as `deployments`, `statefulsets`, and `deployment/finalizers` are removed.

* The `image` custom resource definition in the `caching.internal.knative.dev` group is not used by Tekton anymore, and is excluded in this release.

[id="known-issues-1-5_{context}"]
== Known issues

* The git-cli cluster task is built off the alpine/git base image, which expects `/root` as the user's home directory. However, this is not explicitly set in the `git-cli` cluster task.
+
In Tekton, the default home directory is overwritten with `/tekton/home` for every step of a task, unless otherwise specified. This overwriting of the `$HOME` environment variable of the base image causes the `git-cli` cluster task to fail.
+
This issue is expected to be fixed in the upcoming releases. For {pipelines-title} 1.5 and earlier versions, you can _use any one of the following workarounds_ to avoid the failure of the `git-cli` cluster task:

** Set the `$HOME` environment variable in the steps, so that it is not overwritten.

. [OPTIONAL] If you installed {pipelines-title} using the Operator, then clone the `git-cli` cluster task into a separate task. This approach ensures that the Operator does not overwrite the changes made to the cluster task.
. Execute the `oc edit clustertasks git-cli` command.
. Add the expected `HOME` environment variable to the YAML of the step:
+
[source,yaml,subs="attributes+"]
----
...
steps:
  - name: git
    env:
    - name: HOME
      value: /root
    image: $(params.BASE_IMAGE)
    workingDir: $(workspaces.source.path)
...
----
+
[WARNING]
====
For {pipelines-title} installed by the Operator, if you do not clone the `git-cli` cluster task into a separate task before changing the `HOME` environment variable, then the changes are overwritten during Operator reconciliation.
====

** Disable overwriting the `HOME` environment variable in the `feature-flags` config map.

. Execute the `oc edit -n openshift-pipelines configmap feature-flags` command.
. Set the value of the `disable-home-env-overwrite` flag to `true`.
+
[WARNING]
====
* If you installed {pipelines-title} using the Operator, then the changes are overwritten during Operator reconciliation.

* Modifying the default value of the `disable-home-env-overwrite` flag can break other tasks and cluster tasks, as it changes the default behavior for all tasks.
====

** Use a different service account for the `git-cli` cluster task, as the overwriting of the `HOME` environment variable happens when the default service account for pipelines is used.

. Create a new service account.
. Link your Git secret to the service account you just created.
. Use the service account while executing a task or a pipeline.

* On {ibm-power-name} Systems, {ibm-z-name}, and {ibm-linuxone-name}, the `s2i-dotnet` cluster task and the `tkn hub` command are unsupported.

* When you run Maven and Jib-Maven cluster tasks, the default container image is supported only on Intel (x86) architecture. Therefore, tasks will fail on {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) clusters. As a workaround, you can specify a custom image by setting the `MAVEN_IMAGE` parameter value to `maven:3.6.3-adoptopenjdk-11`.

[id="fixed-issues-1-5_{context}"]
== Fixed issues

* The `when` expressions in `dag` tasks are not allowed to specify the context variable accessing the execution status (`$(tasks.<pipelineTask>.status)`) of any other task.

* Use Owner UIDs instead of Owner names, as it helps avoid race conditions created by deleting a `volumeClaimTemplate` PVC, in situations where a `PipelineRun` resource is quickly deleted and then recreated.

* A new Dockerfile is added for `pullrequest-init` for `build-base` image triggered by non-root users.

* When a pipeline or task is executed with the `-f` option and the `param` in its definition does not have a `type` defined, a validation error is generated instead of the pipeline or task run failing silently.

* For the `tkn start [task | pipeline | clustertask]` commands, the description of the `--workspace` flag is now consistent.

* While parsing the parameters, if an empty array is encountered, the corresponding interactive help is displayed as an empty string now.

// Module included in the following assembly:
//
// * cicd/pipelines/op-release-notes.adoc

[id="op-release-notes-1-4_{context}"]
= Release notes for {pipelines-title} General Availability 1.4

{pipelines-title} General Availability (GA) 1.4 is now available on OpenShift Container Platform 4.7.

[NOTE]
====
In addition to the stable and preview Operator channels, the {pipelines-title} Operator 1.4.0 comes with the ocp-4.6, ocp-4.5, and ocp-4.4 deprecated channels. These deprecated channels and support for them will be removed in the following release of {pipelines-title}.
====

[id="compatibility-support-matrix-1-4_{context}"]
== Compatibility and support matrix

Some features in this release are currently in Technology Preview. These experimental features are not intended for production use.

In the table, features are marked with the following statuses:

[horizontal]
TP:: Technology Preview
GA:: General Availability

Note the following scope of support on the Red Hat Customer Portal for these features:

.Compatibility and support matrix
[cols="1,1,1",options="header"]
|===
| Feature | Version | Support Status
| Pipelines | 0.22 | GA
| CLI | 0.17 | GA
| Catalog | 0.22 | GA
| Triggers | 0.12 | TP
| Pipeline resources | - | TP
|===

For questions and feedback, you can send an email to the product team at pipelines-interest@redhat.com.

[id="new-features-1-4_{context}"]
== New features

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.4.

* The custom tasks have the following enhancements:
** Pipeline results can now refer to results produced by custom tasks.
** Custom tasks can now use workspaces, service accounts, and pod templates to build more complex custom tasks.

* The `finally` task has the following enhancements:
** The `when` expressions are supported in `finally` tasks, which provides efficient guarded execution and improved reusability of tasks.
** A `finally` task can be configured to consume the results of any task within the same pipeline.
+
[NOTE]
====
Support for `when` expressions and `finally` tasks are unavailable in the OpenShift Container Platform 4.7 web console.
====

* Support for multiple secrets of the type `dockercfg` or `dockerconfigjson` is added for authentication at runtime.

* Functionality to support sparse-checkout with the `git-clone` task is added. This enables you to clone only a subset of the repository as your local copy, and helps you to restrict the size of the cloned repositories.

* You can create pipeline runs in a pending state without actually starting them. In clusters that are under heavy load, this allows Operators to have control over the start time of the pipeline runs.

* Ensure that you set the `SYSTEM_NAMESPACE` environment variable manually for the controller; this was previously set by default.

* A non-root user is now added to the build-base image of pipelines so that `git-init` can clone repositories as a non-root user.

* Support to validate dependencies between resolved resources before a pipeline run starts is added. All result variables in the pipeline must be valid, and optional workspaces from a pipeline can only be passed to tasks expecting it for the pipeline to start running.

* The controller and webhook runs as a non-root group, and their superfluous capabilities have been removed to make them more secure.

* You can use the `tkn pr logs` command to see the log streams for retried task runs.

* You can use the `--clustertask` option in the `tkn tr delete` command to delete all the task runs associated with a particular cluster task.

* Support for using Knative service with the `EventListener` resource is added by introducing a new `customResource` field.

* An error message is displayed when an event payload does not use the JSON format.

* The source control interceptors such as GitLab, BitBucket, and GitHub, now use the new `InterceptorRequest` or `InterceptorResponse` type interface.

* A new CEL function `marshalJSON` is implemented so that you can encode a JSON object or an array to a string.

* An HTTP handler for serving the CEL and the source control core interceptors is added. It packages four core interceptors into a single HTTP server that is deployed in the `tekton-pipelines` namespace. The `EventListener` object forwards events over the HTTP server to the interceptor. Each interceptor is available at a different path. For example, the CEL interceptor is available on the `/cel` path.

* The `pipelines-scc` Security Context Constraint (SCC) is used with the default `pipeline` service account for pipelines. This new service account is similar to `anyuid`, but with a minor difference as defined in the YAML for SCC of OpenShift Container Platform 4.7:
+
[source,yaml,subs="attributes+"]
----
fsGroup:
  type: MustRunAs
----

[id="deprecated-features-1-4_{context}"]
== Deprecated features

* The `build-gcs` sub-type in the pipeline resource storage, and the `gcs-fetcher` image, are not supported.

* In the `taskRun` field of cluster tasks, the label `tekton.dev/task` is removed.

* For webhooks, the value `v1beta1` corresponding to the field `admissionReviewVersions` is removed.

* The `creds-init` helper image for building and deploying is removed.

* In the triggers spec and binding, the deprecated field `template.name` is removed in favor of `template.ref`. You should update all `eventListener` definitions to use the `ref` field.
+
[NOTE]
====
Upgrade from {pipelines-shortname} 1.3.x and earlier versions to {pipelines-shortname} 1.4.0 breaks event listeners because of the unavailability of the `template.name` field. For such cases, use {pipelines-shortname} 1.4.1 to avail the restored `template.name` field.
====

* For `EventListener` custom resources/objects, the fields `PodTemplate` and `ServiceType` are deprecated in favor of `Resource`.

* The deprecated spec style embedded bindings is removed.

* The `spec` field is removed from the `triggerSpecBinding`.

* The event ID representation is changed from a five-character random string to a UUID.

[id="known-issues-1-4_{context}"]
== Known issues

* In the *Developer* perspective, the pipeline metrics and triggers features are available only on OpenShift Container Platform 4.7.6 or later versions.

* On {ibm-power-name} Systems, {ibm-z-name}, and {ibm-linuxone-name}, the `tkn hub` command is not supported.

* When you run Maven and Jib Maven cluster tasks on an {ibm-power-name} Systems (ppc64le), {ibm-z-name}, and {ibm-linuxone-name} (s390x) clusters, set the `MAVEN_IMAGE` parameter value to `maven:3.6.3-adoptopenjdk-11`.

* Triggers throw error resulting from bad handling of the JSON format, if you have the following configuration in the trigger binding:
+
[source,yaml,subs="attributes+"]
----
params:
  - name: github_json
    value: $(body)
----
To resolve the issue:
** If you are using triggers v0.11.0 and above, use the `marshalJSON` CEL function, which takes a JSON object or array and returns the JSON encoding of that object or array as a string.
** If you are using older triggers version, add the following annotation in the trigger template:
+
[source,yaml,subs="attributes+"]
----
annotations:
  triggers.tekton.dev/old-escape-quotes: "true"
----

* When upgrading from {pipelines-shortname} 1.3.x to 1.4.x, you must recreate the routes.

[id="fixed-issues-1-4_{context}"]
== Fixed issues

* Previously, the `tekton.dev/task` label was removed from the task runs of cluster tasks, and the `tekton.dev/clusterTask` label was introduced. The problems resulting from that change is resolved by fixing the `clustertask describe` and  `delete` commands. In addition, the `lastrun` function for tasks is modified, to fix the issue of the `tekton.dev/task` label being applied to the task runs of both tasks and cluster tasks in older versions of pipelines.

* When doing an interactive `tkn pipeline start pipelinename`, a `PipelineResource` is created interactively. The `tkn p start` command prints the resource status if the resource status is not `nil`.

* Previously, the `tekton.dev/task=name` label was removed from the task runs created from cluster tasks. This fix modifies the `tkn clustertask start` command with the `--last` flag to check for the `tekton.dev/task=name` label in the created task runs.

* When a task uses an inline task specification, the corresponding task run now gets embedded in the pipeline when you run the `tkn pipeline describe` command, and the task name is returned as embedded.

* The `tkn version` command is fixed to display the version of the installed Tekton CLI tool, without a configured `kubeConfiguration namespace` or access to a cluster.

* If an argument is unexpected or more than one arguments are used, the `tkn completion` command gives an error.

* Previously, pipeline runs with the `finally` tasks nested in a pipeline specification would lose those `finally` tasks, when converted to the `v1alpha1` version and restored back to the `v1beta1` version. This error occurring during conversion is fixed to avoid potential data loss. Pipeline runs with the `finally` tasks nested in a pipeline specification is now serialized and stored on the alpha version, only to be deserialized later.

* Previously, there was an error in the pod generation when a service account had the `secrets` field as `{}`. The task runs failed with `CouldntGetTask` because the GET request with an empty secret name returned an error, indicating that the resource name may not be empty. This issue is fixed by avoiding an empty secret name in the `kubeclient` GET request.

* Pipelines with the `v1beta1` API versions can now be requested along with the `v1alpha1` version, without losing the `finally` tasks. Applying the returned `v1alpha1` version will store the resource as `v1beta1`, with the `finally` section restored to its original state.

* Previously, an unset `selfLink` field in the controller caused an error in the Kubernetes v1.20 clusters. As a temporary fix, the `CloudEvent` source field is set to a value that matches the current source URI, without the value of the auto-populated `selfLink` field.

* Previously, a secret name with dots such as `gcr.io` led to a task run creation failure. This happened because of the secret name being used internally as part of a volume mount name. The volume mount name conforms to the RFC1123 DNS label and disallows dots as part of the name. This issue is fixed by replacing the dot with a dash that results in a readable name.

* Context variables are now validated in the `finally` tasks.

* Previously, when the task run reconciler was passed a task run that did not have a previous status update containing the name of the pod it created, the task run reconciler listed the pods associated with the task run. The task run reconciler used the labels of the task run, which were propagated to the pod, to find the pod. Changing these labels while the task run was running, caused the code to not find the existing pod. As a result, duplicate pods were created. This issue is fixed by changing the task run reconciler to only use the `tekton.dev/taskRun` Tekton-controlled label when finding the pod.

* Previously, when a pipeline accepted an optional workspace and passed it to a pipeline task, the pipeline run reconciler stopped with an error if the workspace was not provided, even if a missing workspace binding is a valid state for an optional workspace. This issue is fixed by ensuring that the pipeline run reconciler does not fail to create a task run, even if an optional workspace is not provided.

* The sorted order of step statuses matches the order of step containers.

* Previously, the task run status was set to `unknown` when a pod encountered the `CreateContainerConfigError` reason, which meant that the task and the pipeline ran until the pod timed out. This issue is fixed by setting the task run status to `false`, so that the task is set as failed when the pod encounters the `CreateContainerConfigError` reason.

* Previously, pipeline results were resolved on the first reconciliation, after a pipeline run was completed. This could fail the resolution resulting in the `Succeeded` condition of the pipeline run being overwritten. As a result, the final status information was lost, potentially confusing any services watching the pipeline run conditions. This issue is fixed by moving the resolution of pipeline results to the end of a reconciliation, when the pipeline run is put into a `Succeeded` or `True` condition.

* Execution status variable is now validated. This avoids validating task results while validating context variables to access execution status.

* Previously, a pipeline result that contained an invalid variable would be added to the pipeline run with the literal expression of the variable intact. Therefore, it was difficult to assess whether the results were populated correctly. This issue is fixed by filtering out the pipeline run results that reference failed task runs. Now, a pipeline result that contains an invalid variable will not be emitted by the pipeline run at all.

* The `tkn eventlistener describe` command is fixed to avoid crashing without a template. It also displays the details about trigger references.

* Upgrades from {pipelines-shortname} 1.3.x and earlier versions to {pipelines-shortname} 1.4.0 breaks event listeners because of the unavailability of `template.name`. In {pipelines-shortname} 1.4.1, the `template.name` has been restored to avoid breaking event listeners in triggers.

* In {pipelines-shortname} 1.4.1, the `ConsoleQuickStart` custom resource has been updated to align with OpenShift Container Platform 4.7 capabilities and behavior.

// Module included in the following assembly:
//
// * openshift_pipelines/op-release-notes.adoc

[id="op-release-notes-1-3_{context}"]
= Release notes for {pipelines-title} Technology Preview 1.3

[id="new-features-1-3_{context}"]
== New features
{pipelines-title} Technology Preview (TP) 1.3 is now available on OpenShift Container Platform 4.7. {pipelines-title} TP 1.3 is updated to support:

* Tekton Pipelines 0.19.0
* Tekton `tkn` CLI 0.15.0
* Tekton Triggers 0.10.2
* cluster tasks based on Tekton Catalog 0.19.0
* {ibm-power-name} Systems on OpenShift Container Platform 4.7
* {ibm-z-name} and {ibm-linuxone-name} on OpenShift Container Platform 4.7

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.3.

[id="pipeline-new-features-1-3_{context}"]
=== Pipelines

* Tasks that build images, such as S2I and Buildah tasks, now emit a URL of the image built that includes the image SHA.

* Conditions in pipeline tasks that reference custom tasks are disallowed because the `Condition` custom resource definition (CRD) has been deprecated.

* Variable expansion is now added in the `Task` CRD for the following fields:
`spec.steps[].imagePullPolicy` and `spec.sidecar[].imagePullPolicy`.

* You can disable the built-in credential mechanism in Tekton by setting the `disable-creds-init` feature-flag to `true`.

* Resolved when expressions are now listed in the `Skipped Tasks` and the `Task Runs` sections in the `Status` field of the `PipelineRun` configuration.

* The `git init` command can now clone recursive submodules.

* A `Task` CR author can now specify a timeout for a step in the `Task` spec.

* You can now base the entry point image on the `distroless/static:nonroot` image and give it a mode to copy itself to the destination, without relying on the `cp` command being present in the base image.

* You can now use the configuration flag `require-git-ssh-secret-known-hosts` to disallow omitting known hosts in the Git SSH secret. When the flag value is set to `true`, you must include the `known_host` field in the Git SSH secret. The default value for the flag is `false`.

* The concept of optional workspaces is now introduced. A task or pipeline might declare a workspace optional and conditionally change their behavior based on its presence. A task run or pipeline run might also omit that workspace, thereby modifying the task or pipeline behavior. The default task run workspaces are not added in place of an omitted optional workspace.

* Credentials initialization in Tekton now detects an SSH credential that is used with a non-SSH URL, and vice versa in Git pipeline resources, and logs a warning in the step containers.

* The task run controller emits a warning event if the affinity specified by the pod template is overwritten by the affinity assistant.

* The task run reconciler now records metrics for cloud events that are emitted once a task run is completed. This includes retries.

[id="cli-new-features-1-3_{context}"]
=== Pipelines CLI

* Support for `--no-headers flag` is now added to the following commands:
`tkn condition list`,`tkn triggerbinding list`,`tkn eventlistener list`,`tkn clustertask list`, `tkn clustertriggerbinding list`.

* When used together, the `--last` or `--use` options override the `--prefix-name` and `--timeout` options.

* The `tkn eventlistener logs` command is now added to view the `EventListener` logs.

* The `tekton hub` commands are now integrated into the `tkn` CLI.

* The `--nocolour` option is now changed to `--no-color`.

* The `--all-namespaces` flag is added to the following commands:
`tkn triggertemplate list`, `tkn condition list`, `tkn triggerbinding list`, `tkn eventlistener list`.

[id="triggers-new-features-1-3_{context}"]
=== Triggers

* You can now specify your resource information in the `EventListener` template.

* It is now mandatory for `EventListener` service accounts to have the `list` and `watch` verbs, in addition to the `get` verb for all the triggers resources. This enables you to use `Listers` to fetch data from `EventListener`, `Trigger`, `TriggerBinding`, `TriggerTemplate`, and `ClusterTriggerBinding` resources. You can use this feature to create a `Sink` object rather than specifying multiple informers, and directly make calls to the API server.

* A new `Interceptor` interface is added to support immutable input event bodies. Interceptors can now add data or fields to a new `extensions` field, and cannot modify the input bodies making them immutable. The CEL interceptor uses this new `Interceptor` interface.

* A `namespaceSelector` field is added to the `EventListener` resource. Use it to specify the namespaces from where the `EventListener` resource can fetch the `Trigger` object for processing events. To use the `namespaceSelector` field, the service account for the `EventListener` resource must have a cluster role.

* The triggers `EventListener` resource now supports end-to-end secure connection to the `eventlistener` pod.

* The escaping parameters behavior in the `TriggerTemplates` resource by replacing `"` with `\"` is now removed.

* A new `resources` field, supporting Kubernetes resources, is introduced as part of the `EventListener` spec.

* A new functionality for the CEL interceptor, with support for upper and lower-casing of ASCII strings, is added.

* You can embed `TriggerBinding` resources by using the `name` and `value` fields in a trigger, or an event listener.

* The `PodSecurityPolicy` configuration is updated to run in restricted environments. It ensures that containers must run as non-root. In addition, the role-based access control for using the pod security policy is moved from cluster-scoped to namespace-scoped. This ensures that the triggers cannot use other pod security policies that are unrelated to a namespace.

* Support for embedded trigger templates is now added. You can either use the `name` field to refer to an embedded template or embed the template inside the `spec` field.

[id="deprecated-features-1-3_{context}"]
== Deprecated features

* Pipeline templates that use `PipelineResources` CRDs are now deprecated and will be removed in a future release.

* The `template.name` field is deprecated in favor of the `template.ref` field and will be removed in a future release.

* The `-c` shorthand for the `--check` command has been removed. In addition, global `tkn` flags are added to the `version` command.

[id="known-issues-1-3_{context}"]
== Known issues

* CEL overlays add fields to a new top-level `extensions` function, instead of modifying the incoming event body. `TriggerBinding` resources can access values within this new `extensions` function using the `$(extensions.<key>)` syntax. Update your binding to use the `$(extensions.<key>)` syntax instead of the `$(body.<overlay-key>)` syntax.

* The escaping parameters behavior by replacing `"` with `\"` is now removed. If you need to retain the old escaping parameters behavior add the `tekton.dev/old-escape-quotes: true"` annotation to your `TriggerTemplate` specification.

* You can embed `TriggerBinding` resources by using the `name` and `value` fields inside a trigger or an event listener. However, you cannot specify both `name` and `ref` fields for a single binding. Use the `ref` field to refer to a `TriggerBinding` resource and the `name` field for embedded bindings.

* An interceptor cannot attempt to reference a `secret` outside the namespace of an `EventListener` resource. You must include secrets in the namespace of the `EventListener`resource.

* In Triggers 0.9.0 and later, if a body or header based `TriggerBinding` parameter is missing or malformed in an event payload, the default values are used instead of displaying an error.

* Tasks and pipelines created with `WhenExpression` objects using Tekton Pipelines 0.16.x must be reapplied to fix their JSON annotations.

* When a pipeline accepts an optional workspace and gives it to a task, the pipeline run stalls if the workspace is not provided.

* To use the Buildah cluster task in a disconnected environment, ensure that the Dockerfile uses an internal image stream as the base image, and then use it in the same manner as any S2I cluster task.

[id="fixed-issues-1-3_{context}"]
== Fixed issues

* Extensions added by a CEL Interceptor are passed on to webhook interceptors by adding the `Extensions` field within the event body.

* The activity timeout for log readers is now configurable using the `LogOptions` field. However, the default behavior of timeout in 10 seconds is retained.

* The `log` command ignores the `--follow` flag when a task run or pipeline run is complete, and reads available logs instead of live logs.

* References to the following Tekton resources: `EventListener`, `TriggerBinding`, `ClusterTriggerBinding`, `Condition`, and `TriggerTemplate` are now standardized and made consistent across all user-facing messages in `tkn` commands.

* Previously, if you started a canceled task run or pipeline run with the `--use-taskrun <canceled-task-run-name>`, `--use-pipelinerun <canceled-pipeline-run-name>` or `--last` flags, the new run would be canceled. This bug is now fixed.

* The `tkn pr desc` command  is now enhanced to ensure that it does not fail in case of pipeline runs with conditions.

* When you delete a task run using the `tkn tr delete` command with the `--task` option, and a cluster task exists with the same name, the task runs for the cluster task also get deleted. As a workaround, filter the task runs by using the `TaskRefKind` field.

* The `tkn triggertemplate describe` command would display only part of the `apiVersion` value in the output. For example, only `triggers.tekton.dev` was displayed instead of `triggers.tekton.dev/v1alpha1`. This bug is now fixed.

* The webhook, under certain conditions, would fail to acquire a lease and not function correctly. This bug is now fixed.

* Pipelines with when expressions created in v0.16.3 can now be run in v0.17.1 and later. After an upgrade, you do not need to reapply pipeline definitions created in previous versions because both the uppercase and lowercase first letters for the annotations are now supported.

* By default, the `leader-election-ha` field is now enabled for high availability. When the `disable-ha` controller flag is set to `true`, it disables high availability support.

* Issues with duplicate cloud events are now fixed. Cloud events are now sent only when a condition changes the state, reason, or message.

* When a service account name is missing from a `PipelineRun` or `TaskRun` spec, the controller uses the service account name from the `config-defaults` config map. If the service account name is also missing in the `config-defaults` config map, the controller now sets it to `default` in the spec.

* Validation for compatibility with the affinity assistant is now supported when the same persistent volume claim is used for multiple workspaces, but with different subpaths.

// Module included in the following assembly:
//
// * openshift_pipelines/op-release-notes.adoc

[id="op-release-notes-1-2_{context}"]
= Release notes for {pipelines-title} Technology Preview 1.2

[id="new-features-1-2_{context}"]
== New features
{pipelines-title} Technology Preview (TP) 1.2 is now available on OpenShift Container Platform 4.6. {pipelines-title} TP 1.2 is updated to support:

* Tekton Pipelines 0.16.3
* Tekton `tkn` CLI 0.13.1
* Tekton Triggers 0.8.1
* cluster tasks based on Tekton Catalog 0.16
* IBM Power Systems on OpenShift Container Platform 4.6
* {ibm-z-name} and {ibm-linuxone-name} on OpenShift Container Platform 4.6

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.2.

[id="pipeline-new-features-1-2_{context}"]
=== Pipelines

* This release of {pipelines-title} adds support for a disconnected installation.

+
[NOTE]
====
Installations in restricted environments are currently not supported on {ibm-power-name} Systems, {ibm-z-name}, and {ibm-linuxone-name}.
====

* You can now use the `when` field, instead of `conditions` resource, to run a task only when certain criteria are met. The key components of `WhenExpression` resources are `Input`, `Operator`, and `Values`. If all the when expressions evaluate to `True`, then the task is run. If any of the when expressions evaluate to `False`, the task is skipped.
* Step statuses are now updated if a task run is canceled or times out.
* Support for Git Large File Storage (LFS) is now available to build the base image used by `git-init`.
* You can now use the `taskSpec` field to specify metadata, such as labels and annotations, when a task is embedded in a pipeline.
* Cloud events are now supported by pipeline runs. Retries with `backoff` are now enabled for cloud events sent by the cloud event pipeline resource.
* You can now set a default `Workspace` configuration for any workspace that a `Task` resource declares, but that a `TaskRun` resource does not explicitly provide.
* Support is available for namespace variable interpolation for the `PipelineRun` namespace and `TaskRun` namespace.
* Validation for `TaskRun` objects is now added to check that not more than one persistent volume claim workspace is used when a `TaskRun` resource is associated with an Affinity Assistant. If more than one persistent volume claim workspace is used, the task run fails with a `TaskRunValidationFailed` condition. Note that by default, the Affinity Assistant is disabled in {pipelines-title}, so you will need to enable the assistant to use it.

[id="cli-new-features-1-2_{context}"]
=== Pipelines CLI

* The `tkn task describe`, `tkn taskrun describe`,  `tkn clustertask describe`, `tkn pipeline describe`, and `tkn pipelinerun describe` commands now:
** Automatically select the `Task`, `TaskRun`, `ClusterTask`, `Pipeline` and `PipelineRun` resource, respectively, if only one of them is present.
** Display the results of the `Task`, `TaskRun`, `ClusterTask`, `Pipeline` and `PipelineRun` resource in their outputs, respectively.
** Display workspaces declared in the `Task`, `TaskRun`, `ClusterTask`, `Pipeline` and `PipelineRun` resource in their outputs, respectively.
* You can now use the `--prefix-name` option with the `tkn clustertask start` command to specify a prefix for the name of a task run.
* Interactive mode support has now been provided to the `tkn clustertask start` command.
* You can now specify `PodTemplate` properties supported by pipelines using local or remote file definitions for `TaskRun` and `PipelineRun` objects.
* You can now use the `--use-params-defaults` option with the `tkn clustertask start` command to use the default values set in the `ClusterTask` configuration and create the task run.
* The `--use-param-defaults` flag for the `tkn pipeline start` command now prompts the interactive mode if the default values have not been specified for some of the parameters.

[id="triggers-new-features-1-2_{context}"]
=== Triggers

* The Common Expression Language (CEL) function named `parseYAML` has been added to parse a YAML string into a map of strings.
* Error messages for parsing CEL expressions have been improved to make them more granular while evaluating expressions and when parsing the hook body for creating the evaluation environment.
* Support is now available for marshaling boolean values and maps if they are used as the values of expressions in a CEL overlay mechanism.
* The following fields have been added to the `EventListener` object:
** The `replicas` field enables the event listener to run more than one pod by specifying the number of replicas in the YAML file.
** The `NodeSelector` field enables the `EventListener` object to schedule the event listener pod to a specific node.
* Webhook interceptors can now parse the `EventListener-Request-URL` header to extract parameters from the original request URL being handled by the event listener.
* Annotations from the event listener can now be propagated to the deployment, services, and other pods. Note that custom annotations on services or deployment are overwritten, and hence, must be added to the event listener annotations so that they are propagated.
* Proper validation for replicas in the `EventListener` specification is now available for cases when a user specifies the `spec.replicas` values as `negative` or `zero`.
* You can now specify the `TriggerCRD` object inside the `EventListener` spec as a reference using the `TriggerRef` field to create the `TriggerCRD` object separately and then bind it inside the `EventListener` spec.
* Validation and defaults for the `TriggerCRD` object are now available.

[id="deprecated-features-1-2_{context}"]
== Deprecated features

* `$(params)` parameters are now removed from the `triggertemplate` resource and replaced by `$(tt.params)` to avoid confusion between the `resourcetemplate` and `triggertemplate` resource parameters.
* The `ServiceAccount` reference of the optional `EventListenerTrigger`-based authentication level has changed from an object reference to a `ServiceAccountName` string. This ensures that the `ServiceAccount` reference is in the same namespace as the `EventListenerTrigger` object.
* The `Conditions` custom resource definition (CRD) is now deprecated; use the `WhenExpressions` CRD instead.
* The `PipelineRun.Spec.ServiceAccountNames` object is being deprecated and replaced by the `PipelineRun.Spec.TaskRunSpec[].ServiceAccountName` object.

[id="known-issues-1-2_{context}"]
== Known issues

* This release of {pipelines-title} adds support for a disconnected installation. However, some images used by the cluster tasks must be mirrored for them to work in disconnected clusters.
* Pipelines in the `openshift` namespace are not deleted after you uninstall the {pipelines-title} Operator. Use the `oc delete pipelines -n openshift --all` command to delete the pipelines.
* Uninstalling the {pipelines-title} Operator does not remove the event listeners.
+
As a workaround, to remove the `EventListener` and `Pod` CRDs:
+
. Edit the `EventListener` object with the `foregroundDeletion` finalizers:
+
[source,terminal]
----
$ oc patch el/<eventlistener_name> -p '{"metadata":{"finalizers":["foregroundDeletion"]}}' --type=merge
----
+
For example:
+
[source,terminal]
----
$ oc patch el/github-listener-interceptor -p '{"metadata":{"finalizers":["foregroundDeletion"]}}' --type=merge
----
+
. Delete the `EventListener` CRD:
+
[source,terminal]
----
$ oc patch crd/eventlisteners.triggers.tekton.dev -p '{"metadata":{"finalizers":[]}}' --type=merge
----

* When you run a multi-arch container image task without command specification on an {ibm-power-name} Systems (ppc64le) or {ibm-z-name} (s390x) cluster, the `TaskRun` resource fails with the following error:
+
[source,terminal]
----
Error executing command: fork/exec /bin/bash: exec format error
----
+
As a workaround, use an architecture specific container image or specify the sha256 digest to point to the correct architecture.
To get the sha256 digest enter:
+
[source,terminal]
----
$ skopeo inspect --raw <image_name>| jq '.manifests[] | select(.platform.architecture == "<architecture>") | .digest'
----

[id="fixed-issues-1-2_{context}"]
== Fixed issues

* A simple syntax validation to check the CEL filter, overlays in the Webhook validator, and the expressions in the interceptor has now been added.
* Triggers no longer overwrite annotations set on the underlying deployment and service objects.
* Previously, an event listener would stop accepting events. This fix adds an idle timeout of 120 seconds for the `EventListener` sink to resolve this issue.
* Previously, canceling a pipeline run with a `Failed(Canceled)` state gave a success message. This has been fixed to display an error instead.
* The `tkn eventlistener list` command now provides the status of the listed event listeners, thus enabling you to easily identify the available ones.
* Consistent error messages are now displayed for the `triggers list` and `triggers describe` commands when triggers are not installed or when a resource cannot be found.
* Previously, a large number of idle connections would build up during cloud event delivery. The `DisableKeepAlives: true` parameter was added to the `cloudeventclient` config to fix this issue. Thus, a new connection is set up for every cloud event.
* Previously, the `creds-init` code would write empty files to the disk even if credentials of a given type were not provided. This fix modifies the `creds-init` code to write files for only those credentials that have actually been mounted from correctly annotated secrets.

// Module included in the following assembly:
//
// * openshift_pipelines/op-release-notes.adoc

[id="op-release-notes-1-1_{context}"]
= Release notes for {pipelines-title} Technology Preview 1.1

[id="new-features-1-1_{context}"]
== New features
{pipelines-title} Technology Preview (TP) 1.1 is now available on OpenShift Container Platform 4.5. {pipelines-title} TP 1.1 is updated to support:

* Tekton Pipelines 0.14.3
* Tekton `tkn` CLI 0.11.0
* Tekton Triggers 0.6.1
* cluster tasks based on Tekton Catalog 0.14

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.1.

[id="pipeline-new-features-1-1_{context}"]
=== Pipelines

* Workspaces can now be used instead of pipeline resources. It is recommended that you use workspaces in {pipelines-shortname}, as pipeline resources are difficult to debug, limited in scope, and make tasks less reusable. For more details on workspaces, see the Understanding {pipelines-shortname} section.
* Workspace support for volume claim templates has been added:
** The volume claim template for a pipeline run and task run can now be added as a volume source for workspaces. The tekton-controller then creates a persistent volume claim (PVC) using the template that is seen as a PVC for all task runs in the pipeline. Thus you do not need to define the PVC configuration every time it binds a workspace that spans multiple tasks.
** Support to find the name of the PVC when a volume claim template is used as a volume source is now available using variable substitution.
* Support for improving audits:
** The `PipelineRun.Status` field now contains the status of every task run in the pipeline and the pipeline specification used to instantiate a pipeline run to monitor the progress of the pipeline run.
** Pipeline results have been added to the pipeline specification and `PipelineRun` status.
** The `TaskRun.Status` field now contains the exact task specification used to instantiate the `TaskRun` resource.
* Support to apply the default parameter to conditions.
* A task run created by referencing a cluster task now adds the `tekton.dev/clusterTask` label instead of the `tekton.dev/task` label.
* The kube config writer now adds the `ClientKeyData` and the `ClientCertificateData` configurations in the resource structure to enable replacement of the pipeline resource type cluster with the kubeconfig-creator task.
* The names of the `feature-flags` and the `config-defaults` config maps are now customizable.
* Support for the host network in the pod template used by the task run is now available.
* An Affinity Assistant is now available to support node affinity in task runs that share workspace volume. By default, this is disabled on {pipelines-shortname}.
* The pod template has been updated to specify `imagePullSecrets` to identify secrets that the container runtime should use to authorize container image pulls when starting a pod.
* Support for emitting warning events from the task run controller if the controller fails to update the task run.
* Standard or recommended k8s labels have been added to all resources to identify resources belonging to an application or component.
* The `Entrypoint` process is now notified for signals and these signals are then propagated using a dedicated PID Group of the `Entrypoint` process.
* The pod template can now be set on a task level at runtime using task run specs.
* Support for emitting Kubernetes events:
** The controller now emits events for additional task run lifecycle events - `taskrun started` and `taskrun running`.
** The pipeline run controller now emits an event every time a pipeline starts.
* In addition to the default Kubernetes events, support for cloud events for task runs is now available. The controller can be configured to send any task run events, such as create, started, and failed, as cloud events.
* Support for using the `$context.<task|taskRun|pipeline|pipelineRun>.name` variable to reference the appropriate name when in pipeline runs and task runs.
* Validation for pipeline run parameters is now available to ensure that all the parameters required by the pipeline are provided by the pipeline run. This also allows pipeline runs to provide extra parameters in addition to the required parameters.
* You can now specify tasks within a pipeline that will always execute before the pipeline exits, either after finishing all tasks successfully or after a task in the pipeline failed, using the `finally` field in the pipeline YAML file.
* The `git-clone` cluster task is now available.

[id="cli-new-features-1-1_{context}"]
=== Pipelines CLI

* Support for embedded trigger binding is now available to the `tkn evenlistener describe` command.
* Support to recommend subcommands and make suggestions if an incorrect subcommand is used.
* The `tkn task describe` command now auto selects the task if only one task is present in the pipeline.
* You can now start a task using default parameter values by specifying the `--use-param-defaults` flag in the `tkn task start` command.
* You can now specify a volume claim template for pipeline runs or task runs using the `--workspace` option with the  `tkn pipeline start` or  `tkn task start` commands.
* The `tkn pipelinerun logs` command now displays logs for the final tasks listed in the `finally` section.
* Interactive mode support has now been provided to the `tkn task start` command and the `describe` subcommand for the following `tkn` resources:  `pipeline`, `pipelinerun`, `task`, `taskrun`, `clustertask`, and `pipelineresource`.
* The `tkn version` command now displays the version of the triggers installed in the cluster.
* The `tkn pipeline describe` command now displays parameter values and timeouts specified for tasks used in the pipeline.
* Support added for the `--last` option for the `tkn pipelinerun describe` and the `tkn taskrun describe` commands to describe the most recent pipeline run or task run, respectively.
* The `tkn pipeline describe` command now displays the conditions applicable to the tasks in the pipeline.
* You can now use the `--no-headers` and `--all-namespaces` flags with the `tkn resource list` command.

[id="triggers-new-features-1-1_{context}"]
=== Triggers
* The following Common Expression Language (CEL) functions are now available:
** `parseURL`  to parse and extract portions of a URL
** `parseJSON` to parse JSON value types embedded in a string in the `payload` field of the `deployment` webhook
* A new interceptor for webhooks from Bitbucket has been added.
* Event listeners now display the `Address URL` and the `Available status` as additional fields when listed with the `kubectl get` command.
* trigger template params now use the `$(tt.params.<paramName>)` syntax instead of `$(params.<paramName>)` to reduce the confusion between trigger template and resource templates params.
* You can now add `tolerations` in the `EventListener` CRD to ensure that event listeners are deployed with the same configuration even if all nodes are tainted due to security or management issues.
* You can now add a Readiness Probe for event listener Deployment at `URL/live`.
* Support for embedding `TriggerBinding` specifications in event listener triggers is now added.
* Trigger resources are now annotated with the recommended `app.kubernetes.io` labels.

[id="deprecated-features-1-1_{context}"]
== Deprecated features
The following items are deprecated in this release:

* The `--namespace` or `-n` flags for all cluster-wide commands, including the `clustertask` and `clustertriggerbinding` commands, are deprecated. It will be removed in a future release.
* The `name` field in `triggers.bindings` within an event listener has been deprecated in favor of the `ref` field and will be removed in a future release.
* Variable interpolation in trigger templates using `$(params)` has been deprecated in favor of using `$(tt.params)` to reduce confusion with the pipeline variable interpolation syntax. The `$(params.<paramName>)` syntax will be removed in a future release.
* The `tekton.dev/task` label is deprecated on cluster tasks.
* The `TaskRun.Status.ResourceResults.ResourceRef` field is deprecated and will be removed.
* The `tkn pipeline create`, `tkn task create`, and `tkn resource create -f` subcommands have been removed.
* Namespace validation has been removed from `tkn` commands.
* The default timeout of `1h` and the  `-t` flag for the `tkn ct start` command have been removed.
* The `s2i` cluster task has been deprecated.

[id="known-issues-1-1_{context}"]
== Known issues
* Conditions do not support workspaces.
* The `--workspace` option and the interactive mode is not supported for the `tkn clustertask start` command.
* Support of backward compatibility for `$(params.<paramName>)` syntax forces you to use trigger templates with pipeline specific params as the trigger s webhook is unable to differentiate trigger  params from pipelines params.
* Pipeline metrics report incorrect values when you run a  promQL query for `tekton_taskrun_count`  and `tekton_taskrun_duration_seconds_count`.
* pipeline runs and task runs continue to be in the `Running` and `Running(Pending)` states respectively even when a non existing PVC name is given to a workspace.

[id="fixed-issues-1-1_{context}"]
== Fixed issues
* Previously, the `tkn task delete <name> --trs` command would delete both the task and cluster task if the name of the task and cluster task were the same. With this fix, the command deletes only the task runs that are created by the task `<name>`.
* Previously the  `tkn pr delete -p <name> --keep 2` command would disregard the `-p` flag when used with the `--keep` flag and would delete all the pipeline runs except the latest two. With this fix, the command deletes only the pipeline runs that are created by the pipeline `<name>`, except for the latest two.
* The `tkn triggertemplate describe` output now displays resource templates in a table format instead of YAML format.
* Previously the `buildah` cluster task failed when a new user was added to a container. With this fix, the issue has been resolved.

// Module included in the following assembly:
//
// * openshift_pipelines/op-release-notes.adoc

[id="op-release-notes-1-0_{context}"]
= Release notes for {pipelines-title} Technology Preview 1.0

[id="new-features-1-0_{context}"]
== New features
{pipelines-title} Technology Preview (TP) 1.0 is now available on OpenShift Container Platform 4.4. {pipelines-title} TP 1.0 is updated to support:

* Tekton Pipelines 0.11.3
* Tekton `tkn` CLI 0.9.0
* Tekton Triggers 0.4.0
* cluster tasks based on Tekton Catalog 0.11

In addition to the fixes and stability improvements, the following sections highlight what is new in {pipelines-title} 1.0.

[id="pipeline-new-features-1-0_{context}"]
=== Pipelines
* Support for  v1beta1 API Version.
* Support for an improved limit range. Previously, limit range was specified exclusively for the task run and the pipeline run. Now there is no need to explicitly specify the limit range. The minimum limit range across the namespace is used.
* Support for sharing data between tasks using task results and task params.
* Pipelines can now be configured to not overwrite the `HOME` environment variable and the working directory of steps.
* Similar to task steps, `sidecars` now support script mode.
* You can now specify a different scheduler name in task run `podTemplate` resource.
* Support for variable substitution using Star Array Notation.
* Tekton controller can now be configured to monitor an individual namespace.
* A new description field is now added to the specification of pipelines, tasks, cluster tasks, resources, and conditions.
* Addition of proxy parameters to Git pipeline resources.

[id="cli-new-features-1-0_{context}"]
=== Pipelines CLI

* The `describe` subcommand is now added for the following `tkn` resources: `EventListener`, `Condition`, `TriggerTemplate`, `ClusterTask`, and `TriggerSBinding`.
* Support added for `v1beta1` to the following resources along with backward compatibility for `v1alpha1`: `ClusterTask`, `Task`, `Pipeline`, `PipelineRun`,  and `TaskRun`.
* The following commands can now list output from all namespaces using the `--all-namespaces` flag option: `tkn task list`, `tkn pipeline list`, `tkn taskrun list`, `tkn pipelinerun list`
+
The output of these commands is also enhanced to display information without headers using the `--no-headers` flag option.

* You can now start a pipeline using default parameter values by specifying `--use-param-defaults` flag in the `tkn pipelines start` command.
* Support for workspace is now added to `tkn pipeline start` and `tkn task start` commands.
* A new `clustertriggerbinding` command is now added with the following subcommands: `describe`, `delete`, and `list`.
* You can now directly start a pipeline run using a local or remote `yaml` file.
* The `describe` subcommand now displays an enhanced and detailed output. With the addition of new fields,  such as `description`, `timeout`, `param description`, and `sidecar status`, the command output now provides more detailed information about a specific `tkn` resource.
* The `tkn task log` command now displays logs directly if only one task is present in the namespace.

[id="triggers-new-features-1-0_{context}"]
=== Triggers
* Triggers can now create both `v1alpha1` and `v1beta1` pipeline resources.
* Support for new Common Expression Language (CEL) interceptor function - `compareSecret`. This function securely compares strings to secrets in CEL expressions.
* Support for authentication and authorization at the event listener trigger  level.

[id="deprecated-features-1-0_{context}"]
== Deprecated features
The following items are deprecated in this release:

* The environment variable `$HOME`, and variable `workingDir` in the `Steps` specification are deprecated and might be changed in a future release. Currently in a `Step` container, the `HOME` and  `workingDir` variables are overwritten to `/tekton/home` and `/workspace` variables, respectively.
+
In a later release, these two fields will not be modified, and will be set to values defined in the container image and the `Task` YAML.
For this release, use the `disable-home-env-overwrite` and `disable-working-directory-overwrite` flags to disable overwriting of the `HOME` and `workingDir` variables.

* The following commands are deprecated and might be removed in the future release: `tkn pipeline create`, `tkn task create`.

* The `-f` flag with the `tkn resource create` command is now deprecated. It might be removed in the future release.

* The `-t` flag and the `--timeout` flag (with seconds format) for the `tkn clustertask create` command are now deprecated. Only duration timeout format is now supported, for example `1h30s`. These deprecated flags might be removed in the future release.

[id="known-issues-1-4-0_{context}"]
== Known issues
* If you are upgrading from an older version of {pipelines-title}, you must delete your existing deployments before upgrading to {pipelines-title} version 1.0. To delete an existing deployment, you must first delete Custom Resources and then uninstall the {pipelines-title} Operator. For more details, see the uninstalling {pipelines-title} section.
* Submitting the same `v1alpha1` tasks more than once results in an error. Use the `oc replace` command instead of `oc apply` when re-submitting a `v1alpha1` task.
* The `buildah` cluster task does not work when a new user is added to a container.
+
When the Operator is installed, the `--storage-driver` flag for the `buildah` cluster task is not specified, therefore the flag is set to its default value. In some cases, this causes the storage driver to be set incorrectly. When a new user is added, the incorrect storage-driver results in the failure of the `buildah` cluster task with the following error:
+
----
useradd: /etc/passwd.8: lock file already used
useradd: cannot lock /etc/passwd; try again later.
----
+
As a workaround, manually set the `--storage-driver` flag value to `overlay` in the `buildah-task.yaml` file:
+
. Login to your cluster as a `cluster-admin`:
+
----
$ oc login -u <login> -p <password> https://openshift.example.com:6443
----
. Use the `oc edit` command to edit `buildah` cluster task:
+
----
$ oc edit clustertask buildah
----
+
The current version of the `buildah` clustertask YAML file opens in the editor set by your `EDITOR` environment variable.
. Under the `Steps` field, locate the following `command` field:
+
----
 command: ['buildah', 'bud', '--format=$(params.FORMAT)', '--tls-verify=$(params.TLSVERIFY)', '--layers', '-f', '$(params.DOCKERFILE)', '-t', '$(resources.outputs.image.url)', '$(params.CONTEXT)']
----

. Replace the `command` field with the following:
+
----
 command: ['buildah', '--storage-driver=overlay', 'bud', '--format=$(params.FORMAT)', '--tls-verify=$(params.TLSVERIFY)', '--no-cache', '-f', '$(params.DOCKERFILE)', '-t', '$(params.IMAGE)', '$(params.CONTEXT)']
----
. Save the file and exit.

+
Alternatively, you can also modify the `buildah` cluster task YAML file directly on the web console by navigating to *Pipelines* -> *Cluster Tasks* -> *buildah*. Select *Edit Cluster Task* from the *Actions* menu and replace the `command` field as shown in the previous procedure.

[id="fixed-issues-1-0_{context}"]
== Fixed issues
* Previously, the `DeploymentConfig` task triggered a new deployment build even when an image build was already in progress. This caused the deployment of the pipeline to fail. With this fix, the `deploy task` command  is now replaced with the `oc rollout status` command which waits for the in-progress deployment to finish.
* Support for `APP_NAME` parameter is now added in pipeline templates.
* Previously, the pipeline template for Java S2I failed to look up the image in the registry. With this fix, the image is looked up using the existing image pipeline resources instead of the user provided `IMAGE_NAME` parameter.
* All the {pipelines-shortname} images are now based on the Red Hat Universal Base Images (UBI).
* Previously, when the pipeline was installed in a namespace other than `tekton-pipelines`, the `tkn version` command displayed the pipeline version as `unknown`. With this fix, the `tkn version` command now displays the correct pipeline version in any namespace.
* The `-c` flag is no longer supported for the `tkn version` command.
* Non-admin users can now list the cluster trigger bindings.
* The event listener `CompareSecret` function is now fixed for the CEL Interceptor.
* The `list`, `describe`, and `start` subcommands for tasks and cluster tasks now correctly display the output in case a task and cluster task have the same name.
* Previously, the {pipelines-shortname} Operator modified the privileged security context constraints (SCCs), which caused an error during cluster upgrade. This error is now fixed.
* In the `tekton-pipelines` namespace, the timeouts of all task runs and pipeline runs are now set to the value of `default-timeout-minutes` field using the config map.
* Previously, the pipelines section in the web console was not displayed for non-admin users. This issue is now resolved.
