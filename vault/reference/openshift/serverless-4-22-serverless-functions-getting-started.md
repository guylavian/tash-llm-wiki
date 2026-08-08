---
title: "Getting started with functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-functions-getting-started
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-functions-getting-started
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Getting started with functions

[id="serverless-functions-getting-started"]
= Getting started with functions

Function lifecycle management includes creating, building, and deploying a function. Optionally, you can also test a deployed function by invoking it. You can do all of these operations on {ServerlessProductName} using the `kn func` tool.

[id="prerequisites_serverless-functions-getting-started"]
== Prerequisites

Before you can complete the following procedures, you must ensure that you have completed all of the prerequisite tasks in Setting up {FunctionsProductName}.

// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-getting-started.adoc
// * serverless/reference/kn-func-ref.adoc

[id="serverless-create-func-kn_{context}"]
= Creating functions

Before you can build and deploy a function, you must create it by using the Knative (`kn`) CLI. You can specify the path, runtime, template, and image registry as flags on the command line, or use the `-c` flag to start the interactive experience in the terminal.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.

.Procedure

* Create a function project:
+
[source,terminal]
----
$ kn func create -r <repository> -l <runtime> -t <template> <path>
----
** Accepted runtime values include `quarkus`, `node`, `typescript`, `go`, `python`, `springboot`, and `rust`.
** Accepted template values include `http` and `cloudevents`.
+
.Example command
[source,terminal]
----
$ kn func create -l typescript -t cloudevents examplefunc
----
+
.Example output
[source,terminal]
----
Created typescript function in /home/user/demo/examplefunc
----
+
** Alternatively, you can specify a repository that contains a custom template.
+
.Example command
[source,terminal]
----
$ kn func create -r https://github.com/boson-project/templates/ -l node -t hello-world examplefunc
----
+
.Example output
[source,terminal]
----
Created node function in /home/user/demo/examplefunc
----
// Module included in the following assemblies:
//
// * serverless/cli_tools/kn-func-ref.adoc
// * serverless/functions/serverless-functions-getting-started.adoc

[id="serverless-kn-func-run_{context}"]
= Running a function locally

You can use the `kn func run` command to run a function locally in the current directory or in the directory specified by the `--path` flag. If the function that you are running has never previously been built, or if the project files have been modified since the last time it was built, the `kn func run` command builds the function before running it by default.

.Example command to run a function in the current directory
[source,terminal]
----
$ kn func run
----

.Example command to run a function in a directory specified as a path
[source,terminal]
----
$ kn func run --path=<directory_path>
----

You can also force a rebuild of an existing image before running the function, even if there have been no changes to the project files, by using the `--build` flag:

.Example run command using the build flag
[source,terminal]
----
$ kn func run --build
----

If you set the `build` flag as false, this disables building of the image, and runs the function using the previously built image:

.Example run command using the build flag
[source,terminal]
----
$ kn func run --build=false
----

You can use the help command to learn more about `kn func run` command options:

.Build help command
[source,terminal]
----
$ kn func help run
----
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-getting-started.adoc

[id="serverless-build-func-kn_{context}"]
= Building functions

Before you can run a function, you must build the function project. If you are using the `kn func run` command, the function is built automatically. However, you can use the `kn func build` command to build a function without running it, which can be useful for advanced users or debugging scenarios.

The `kn func build` command creates an OCI container image that can be run locally on your computer or on an OpenShift Container Platform cluster. This command uses the function project name and the image registry name to construct a fully qualified image name for your function.

[id="serverless-build-func-kn-image-containers_{context}"]
== Image container types

By default, `kn func build` creates a container image by using Red Hat Source-to-Image (S2I) technology.

.Example build command using Red Hat Source-to-Image (S2I)
[source,terminal]
----
$ kn func build
----

[id="serverless-build-func-kn-image-registries_{context}"]
== Image registry types

The OpenShift Container Registry is used by default as the image registry for storing function images.

.Example build command using OpenShift Container Registry
[source,terminal]
----
$ kn func build
----

.Example output
[source,terminal]
----
Building function image
Function image has been built, image: registry.redhat.io/example/example-function:latest
----

You can override using OpenShift Container Registry as the default image registry by using the `--registry` flag:

.Example build command overriding OpenShift Container Registry to use quay.io
[source,terminal]
----
$ kn func build --registry quay.io/username
----

.Example output
[source,terminal]
----
Building function image
Function image has been built, image: quay.io/username/example-function:latest
----

[id="serverless-build-func-kn-push_{context}"]
== Push flag

You can add the `--push` flag to a `kn func build` command to automatically push the function image after it is successfully built:

.Example build command using OpenShift Container Registry
[source,terminal]
----
$ kn func build --push
----

[id="serverless-build-func-kn-help_{context}"]
== Help command

You can use the help command to learn more about `kn func build` command options:

.Build help command
[source,terminal]
----
$ kn func help build
----
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-getting-started.adoc

[id="serverless-deploy-func-kn_{context}"]
= Deploying functions

You can deploy a function to your cluster as a Knative service by using the `kn func deploy` command. If the targeted function is already deployed, it is updated with a new container image that is pushed to a container image registry, and the Knative service is updated.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You must have already created and initialized the function that you want to deploy.

.Procedure

* Deploy a function:
+
[source,terminal]
----
$ kn func deploy [-n <namespace> -p <path> -i <image>]
----
+
.Example output
[source,terminal]
----
Function deployed at: http://func.example.com
----
** If no `namespace` is specified, the function is deployed in the current namespace.
** The function is deployed from the current directory, unless a `path` is specified.
** The Knative service name is derived from the project name, and cannot be changed using this command.

[NOTE]
====
You can create a serverless function with a Git repository URL by using *Import from Git* or *Create Serverless Function* in the *+Add* view of the *Developer* perspective.
====
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-getting-started.adoc
// * serverless/cli_tools/kn-func-ref.adoc

[id="serverless-kn-func-invoke_{context}"]
= Invoking a deployed function with a test event

You can use the `kn func invoke` CLI command to send a test request to invoke a function either locally or on your OpenShift Container Platform cluster. You can use this command to test that a function is working and able to receive events correctly. Invoking a function locally is useful for a quick test during function development. Invoking a function on the cluster is useful for testing that is closer to the production environment.

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on the cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.
* You must have already deployed the function that you want to invoke.

.Procedure

* Invoke a function:
+
[source,terminal]
----
$ kn func invoke
----
** The `kn func invoke` command only works when there is either a local container image currently running, or when there is a function deployed in the cluster.
** The `kn func invoke` command executes on the local directory by default, and assumes that this directory is a function project.
// Module included in the following assemblies

// * serverless/cli_tools/kn-func-ref.adoc

[id="serverless-kn-func-delete_{context}"]
= Deleting a function

You can delete a function by using the `kn func delete` command. This is useful when a function is no longer required, and can help to save resources on your cluster.

.Procedure

* Delete a function:
+
[source,terminal]
----
$ kn func delete [<function_name> -n <namespace> -p <path>]
----
** If the name or path of the function to delete is not specified, the current directory is searched for a `func.yaml` file that is used to determine the function to delete.
** If the namespace is not specified, it defaults to the `namespace` value in the `func.yaml` file.

[id="additional-resources_serverless-functions-getting-started"]
[role="_additional-resources"]
== Additional resources
* Exposing a default registry manually
* Marketplace page for the Intellij Knative plugin
* Marketplace page for the Visual Studio Code Knative plugin
* Creating applications using the Developer perspective
// This Additional resource applies only to OCP, but not to OSD nor ROSA.

[id="next-steps_serverless-functions-getting-started"]
== Next steps

* See Using functions with Knative Eventing
