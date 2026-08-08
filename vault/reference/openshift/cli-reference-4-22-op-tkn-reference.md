---
title: "OpenShift Pipelines tkn reference"
type: reference
domain: openshift
slug: cli-reference-4-22-op-tkn-reference
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/op-tkn-reference
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# OpenShift Pipelines tkn reference

[id='op-tkn-reference']
= OpenShift Pipelines tkn reference

This section lists the basic `tkn` CLI commands.

== Basic syntax
`tkn [command or options] [arguments...]`

== Global options
`--help, -h`

// Utility commands
// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-utility-commands_{context}"]
= Utility commands

== tkn
Parent command for `tkn` CLI.

.Example: Display all options
[source,terminal]
----
$ tkn
----

== completion [shell]
Print shell completion code which must be evaluated to provide interactive completion. Supported shells are `bash` and `zsh`.

.Example: Completion code for `bash` shell
[source,terminal]
----
$ tkn completion bash
----

== version
Print version information of the `tkn` CLI.

.Example: Check the `tkn` version
[source,terminal]
----
$ tkn version
----

// Pipeline management commands
// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/op-tkn-references.adoc

[id="op-tkn-pipeline-management_{context}"]
= Pipelines management commands

== pipeline
Manage pipelines.

.Example: Display help
[source,terminal]
----
$ tkn pipeline --help
----

== pipeline delete

Delete a pipeline.

.Example: Delete the `mypipeline` pipeline from a namespace
[source,terminal]
----
$ tkn pipeline delete mypipeline -n myspace
----

== pipeline describe
Describe a pipeline.

.Example: Describe the `mypipeline` pipeline
[source,terminal]
----
$ tkn pipeline describe mypipeline
----

== pipeline list
Display a list of pipelines.

.Example: Display a list of pipelines
[source,terminal]
-----
$ tkn pipeline list
-----

== pipeline logs
Display the logs for a specific pipeline.

.Example: Stream the live logs for the `mypipeline` pipeline
[source,terminal]
----
$ tkn pipeline logs -f mypipeline
----

== pipeline start
Start a pipeline.

.Example: Start the `mypipeline` pipeline
[source,terminal]
----
$ tkn pipeline start mypipeline
----

// Pipeline run commands
// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/op-tkn-references.adoc

[id="op-tkn-pipeline-run_{context}"]
= Pipeline run commands

== pipelinerun
Manage pipeline runs.

.Example: Display help
[source,terminal]
----
$ tkn pipelinerun -h
----

== pipelinerun cancel
Cancel a pipeline run.

.Example: Cancel the `mypipelinerun` pipeline run from a namespace
[source,terminal]
----
$ tkn pipelinerun cancel mypipelinerun -n myspace
----

== pipelinerun delete
Delete a pipeline run.

.Example: Delete pipeline runs from a namespace
[source,terminal]
----
$ tkn pipelinerun delete mypipelinerun1 mypipelinerun2 -n myspace
----

.Example: Delete all pipeline runs from a namespace, except the five most recently executed pipeline runs
[source,terminal]
----
$ tkn pipelinerun delete -n myspace --keep 5 <1>
----
<1> Replace `5` with the number of most recently executed pipeline runs you want to retain.

.Example: Delete all pipelines
[source,terminal]
----
$ tkn pipelinerun delete --all
----

[NOTE]
====
Starting with {pipelines-title} 1.6, the `tkn pipelinerun delete --all` command does not delete any resources that are in the running state.
====

== pipelinerun describe
Describe a pipeline run.

.Example: Describe the `mypipelinerun` pipeline run in a namespace
[source,terminal]
----
$ tkn pipelinerun describe mypipelinerun -n myspace
----

== pipelinerun list
List pipeline runs.

.Example: Display a list of pipeline runs in a namespace
[source,terminal]
----
$ tkn pipelinerun list -n myspace
----

== pipelinerun logs
Display the logs of a pipeline run.

.Example: Display the logs of the `mypipelinerun` pipeline run with all tasks and steps in a namespace
[source,terminal]
----
$ tkn pipelinerun logs mypipelinerun -a -n myspace
----

// Task management commands
// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-task-management_{context}"]
= Task management commands

== task
Manage tasks.

.Example: Display help
[source,terminal]
----
$ tkn task -h
----

== task delete
Delete a task.

.Example: Delete `mytask1` and `mytask2` tasks from a namespace
[source,terminal]
----
$ tkn task delete mytask1 mytask2 -n myspace
----

== task describe
Describe a task.

.Example: Describe the `mytask` task in a namespace
[source,terminal]
----
$ tkn task describe mytask -n myspace
----

== task list
List tasks.

.Example: List all the tasks in a namespace
[source,terminal]
----
$ tkn task list -n myspace
----

== task logs
Display task logs.

.Example: Display logs for the `mytaskrun` task run of the `mytask` task
[source,terminal]
----
$ tkn task logs mytask mytaskrun -n myspace
----

== task start
Start a task.

.Example: Start the `mytask` task in a namespace
[source,terminal]
----
$ tkn task start mytask -s <ServiceAccountName> -n myspace
----

// Task run commands
// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-task-run_{context}"]
= Task run commands

== taskrun
Manage task runs.

.Example: Display help
[source,terminal]
----
$ tkn taskrun -h
----

== taskrun cancel
Cancel a task run.

.Example: Cancel the `mytaskrun` task run from a namespace
[source,terminal]
----
$ tkn taskrun cancel mytaskrun -n myspace
----

== taskrun delete
Delete a TaskRun.

.Example: Delete the `mytaskrun1` and `mytaskrun2` task runs from a namespace
[source,terminal]
----
$ tkn taskrun delete mytaskrun1 mytaskrun2 -n myspace
----

.Example: Delete all but the five most recently executed task runs from a namespace
[source,terminal]
----
$ tkn taskrun delete -n myspace --keep 5 <1>
----
<1> Replace `5` with the number of most recently executed task runs you want to retain.

== taskrun describe
Describe a task run.

.Example: Describe the `mytaskrun` task run in a namespace
[source,terminal]
----
$ tkn taskrun describe mytaskrun -n myspace
----

== taskrun list
List task runs.

.Example: List all the task runs in a namespace
[source,terminal]
----
$ tkn taskrun list -n myspace
----

== taskrun logs
Display task run logs.

.Example: Display live logs for the `mytaskrun` task run in a namespace

[source,terminal]
----
$ tkn taskrun logs -f mytaskrun -n myspace
----

// Condition management commands
// Module included in the following assemblies:
//
// * cli_reference/tkn_cli/op-tkn-references.adoc

[id="op-tkn-condition-management_{context}"]
= Condition management commands

== condition
Manage Conditions.

.Example: Display help
[source,terminal]
----
$ tkn condition --help
----

== condition delete
Delete a Condition.

.Example: Delete the `mycondition1` Condition from a namespace
[source,terminal]
----
$ tkn condition delete mycondition1 -n myspace
----

== condition describe
Describe a Condition.

.Example: Describe the `mycondition1` Condition in a namespace
[source,terminal]
----
$ tkn condition describe mycondition1 -n myspace
----

== condition list
List Conditions.

.Example: List Conditions in a namespace
[source,terminal]
----
$ tkn condition list -n myspace
----

// Pipeline resources commands
// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-pipeline-resource-management_{context}"]
= Pipeline Resource management commands

== resource
Manage Pipeline Resources.

.Example: Display help
[source,terminal]
----
$ tkn resource -h
----

== resource create
Create a Pipeline Resource.

.Example: Create a Pipeline Resource in a namespace
[source,terminal]
----
$ tkn resource create -n myspace
----
This is an interactive command that asks for input on the name of the Resource, type of the Resource, and the values based on the type of the Resource.

== resource delete
Delete a Pipeline Resource.

.Example: Delete the `myresource` Pipeline Resource from a namespace
[source,terminal]
----
$ tkn resource delete myresource -n myspace
----

== resource describe
Describe a Pipeline Resource.

.Example: Describe the `myresource` Pipeline Resource
[source,terminal]
----
$ tkn resource describe myresource -n myspace
----
== resource list
List Pipeline Resources.

.Example: List all Pipeline Resources in a namespace
[source,terminal]
----
$ tkn resource list -n myspace
----

// ClusterTask management commands
// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-clustertask-management-commands_{context}"]
= ClusterTask management commands

[IMPORTANT]
====
In {pipelines-title} 1.10, ClusterTask functionality of the `tkn` command-line utility is deprecated and is planned to be removed in a future release.
====

== clustertask
Manage ClusterTasks.

.Example: Display help
[source,terminal]
----
$ tkn clustertask --help
----

== clustertask delete
Delete a ClusterTask resource in a cluster.

.Example: Delete `mytask1` and `mytask2` ClusterTasks
[source,terminal]
----
$ tkn clustertask delete mytask1 mytask2
----

== clustertask describe
Describe a ClusterTask.

.Example: Describe the `mytask` ClusterTask
[source,terminal]
----
$ tkn clustertask describe mytask1
----

== clustertask list
List ClusterTasks.

.Example: List ClusterTasks
[source,terminal]
----
$ tkn clustertask list
----
== clustertask start
Start ClusterTasks.

.Example: Start the `mytask` ClusterTask
[source,terminal]
----
$ tkn clustertask start mytask
----

// Trigger management commands
// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-trigger-management_{context}"]
= Trigger management commands

== eventlistener
Manage EventListeners.

.Example: Display help
[source,terminal]
----
$ tkn eventlistener -h
----

== eventlistener delete
Delete an EventListener.

.Example: Delete `mylistener1` and `mylistener2` EventListeners in a namespace
[source,terminal]
----
$ tkn eventlistener delete mylistener1 mylistener2 -n myspace
----
== eventlistener describe
Describe an EventListener.

.Example: Describe the `mylistener` EventListener in a namespace
[source,terminal]
----
$ tkn eventlistener describe mylistener -n myspace
----

== eventlistener list
List EventListeners.

.Example: List all the EventListeners in a namespace
[source,terminal]
----
$ tkn eventlistener list -n myspace
----

== eventlistener logs
Display logs of an EventListener.

.Example: Display the logs of the `mylistener` EventListener in a namespace
[source,terminal]
----
$ tkn eventlistener logs mylistener -n myspace
----

== triggerbinding
Manage TriggerBindings.

.Example: Display TriggerBindings help
[source,terminal]
----
$ tkn triggerbinding -h
----

== triggerbinding delete
Delete a TriggerBinding.

.Example: Delete `mybinding1` and `mybinding2` TriggerBindings in a namespace
[source,terminal]
----
$ tkn triggerbinding delete mybinding1 mybinding2 -n myspace
----
== triggerbinding describe
Describe a TriggerBinding.

.Example: Describe the `mybinding` TriggerBinding in a namespace
[source,terminal]
----
$ tkn triggerbinding describe mybinding -n myspace
----

== triggerbinding list
List TriggerBindings.

.Example: List all the TriggerBindings in a namespace
[source,terminal]
----
$ tkn triggerbinding list -n myspace
----

== triggertemplate
Manage TriggerTemplates.

.Example: Display TriggerTemplate help
[source,terminal]
----
$ tkn triggertemplate -h
----
== triggertemplate delete
Delete a TriggerTemplate.

.Example: Delete `mytemplate1` and `mytemplate2` TriggerTemplates in a namespace
[source,terminal]
----
$ tkn triggertemplate delete mytemplate1 mytemplate2 -n `myspace`
----
== triggertemplate describe
Describe a TriggerTemplate.

.Example: Describe the `mytemplate` TriggerTemplate in a namespace
[source,terminal]
----
$ tkn triggertemplate describe mytemplate -n `myspace`
----

== triggertemplate list
List TriggerTemplates.

.Example: List all the TriggerTemplates in a namespace
[source,terminal]
----
$ tkn triggertemplate list -n myspace
----
== clustertriggerbinding
Manage ClusterTriggerBindings.

.Example: Display ClusterTriggerBindings help
[source,terminal]
----
$ tkn clustertriggerbinding -h
----

== clustertriggerbinding delete
Delete a ClusterTriggerBinding.

.Example: Delete `myclusterbinding1` and `myclusterbinding2` ClusterTriggerBindings
[source,terminal]
----
$ tkn clustertriggerbinding delete myclusterbinding1 myclusterbinding2
----
== clustertriggerbinding describe
Describe a ClusterTriggerBinding.

.Example: Describe the `myclusterbinding` ClusterTriggerBinding
[source,terminal]
----
$ tkn clustertriggerbinding describe myclusterbinding
----

== clustertriggerbinding list
List ClusterTriggerBindings.

.Example: List all ClusterTriggerBindings
[source,terminal]
----
$ tkn clustertriggerbinding list
----

// Hub interaction commands
// Module included in the following assemblies:
//
// *  cli_reference/tkn_cli/op-tkn-reference.adoc

[id="op-tkn-hub-interaction_{context}"]
= Hub interaction commands

Interact with Tekton Hub for resources such as tasks and pipelines.

== hub
Interact with hub.

.Example: Display help
[source,terminal]
----
$ tkn hub -h
----

.Example: Interact with a hub API server
[source,terminal]
----
$ tkn hub --api-server https://api.hub.tekton.dev
----

[NOTE]
====
For each example, to get the corresponding sub-commands and flags, run `tkn hub <command> --help`.
====

== hub downgrade
Downgrade an installed resource.

.Example: Downgrade the `mytask` task in the `mynamespace` namespace to its older version
[source,terminal]
----
$ tkn hub downgrade task mytask --to version -n mynamespace
----

== hub get
Get a resource manifest by its name, kind, catalog, and version.

.Example: Get the manifest for a specific version of the `myresource` pipeline or task from the `tekton` catalog
[source,terminal]
----
$ tkn hub get [pipeline | task] myresource --from tekton --version version
----

== hub info
Display information about a resource by its name, kind, catalog, and version.

.Example: Display information about a specific version of the `mytask` task from the `tekton` catalog
[source,terminal]
----
$ tkn hub info task mytask --from tekton --version version
----

== hub install
Install a resource from a catalog by its kind, name, and version.

.Example: Install a specific version of the `mytask` task from the `tekton` catalog in the `mynamespace` namespace
[source,terminal]
----
$ tkn hub install task mytask --from tekton --version version -n mynamespace
----

== hub reinstall
Reinstall a resource by its kind and name.

.Example: Reinstall a specific version of the `mytask` task from the `tekton` catalog in the `mynamespace` namespace
[source,terminal]
----
$ tkn hub reinstall task mytask --from tekton --version version -n mynamespace
----

== hub search
Search a resource by a combination of name, kind, and tags.

.Example: Search a resource with a tag `cli`
[source,terminal]
----
$ tkn hub search --tags cli
----

== hub upgrade
Upgrade an installed resource.

.Example: Upgrade the installed `mytask` task in the `mynamespace` namespace to a new version
[source,terminal]
----
$ tkn hub upgrade task mytask --to version -n mynamespace
----
