---
title: "kn functions commands"
type: reference
domain: openshift
slug: serverless-4-22-kn-functions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/kn-functions
version: 4.22
family: serverless
documentKind: "Documentation"
---

# kn functions commands

[id="kn-functions"]
= kn functions commands

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
// Module included in the following assemblies

// * /serverless/cli_tools/kn-func-ref.adoc

[id="functions-list-kn_{context}"]
= Listing existing functions

You can list existing functions by using `kn func list`. If you want to list functions that have been deployed as Knative services, you can also use `kn service list`.

.Procedure

* List existing functions:
+
[source,terminal]
----
$ kn func list [-n <namespace> -p <path>]
----
+
.Example output
[source,terminal]
----
NAME           NAMESPACE  RUNTIME  URL                                                                                      READY
example-function  default    node     http://example-function.default.apps.ci-ln-g9f36hb-d5d6b.origin-ci-int-aws.dev.rhcloud.com  True
----

* List functions deployed as Knative services:
+
[source,terminal]
----
$ kn service list -n <namespace>
----
+
.Example output
[source,terminal]
----
NAME            URL                                                                                       LATEST                AGE   CONDITIONS   READY   REASON
example-function   http://example-function.default.apps.ci-ln-g9f36hb-d5d6b.origin-ci-int-aws.dev.rhcloud.com   example-function-gzl4c   16m   3 OK / 3     True
----
[id="describe-function-kn_{context}"]
= Describing a function

The `kn func info` command prints information about a deployed function, such as the function name, image, namespace, Knative service information, route information, and event subscriptions.

.Procedure

* Describe a function:
+
[source,terminal]
----
$ kn func info [-f <format> -n <namespace> -p <path>]
----
+
.Example command
[source,terminal]
----
$ kn func info -p function/example-function
----
+
.Example output
[source,terminal]
----
Function name:
  example-function
Function is built in image:
  docker.io/user/example-function:latest
Function is deployed as Knative Service:
  example-function
Function is deployed in namespace:
  default
Routes:
  http://example-function.default.apps.ci-ln-g9f36hb-d5d6b.origin-ci-int-aws.dev.rhcloud.com
----
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
// Module included in the following assemblies:
//
// * serverless/reference/kn-func-ref.adoc

[id="serverless-kn-func-invoke-reference_{context}"]
= kn func invoke optional parameters

You can specify optional parameters for the request by using the following `kn func invoke` CLI command flags.

[options="header",cols="1,3"]
|===
| Flags | Description
| `-t`, `--target` | Specifies the target instance of the invoked function, for example, `local` or `remote` or `https://staging.example.com/`. The default target is `local`.
| `-f`, `--format` | Specifies the format of the message, for example, `cloudevent` or `http`.
| `--id` | Specifies a unique string identifier for the request.
| `-n`, `--namespace` | Specifies the namespace on the cluster.
| `--source` | Specifies sender name for the request. This corresponds to the CloudEvent `source` attribute.
| `--type` | Specifies the type of request, for example, `boson.fn`. This corresponds to the CloudEvent `type` attribute.
| `--data` | Specifies content for the request. For CloudEvent requests, this is the CloudEvent `data` attribute.
| `--file` | Specifies path to a local file containing data to be sent.
| `--content-type` | Specifies the MIME content type for the request.
| `-p`, `--path` | Specifies path to the project directory.
| `-c`, `--confirm` | Enables prompting to interactively confirm all options.
| `-v`, `--verbose` | Enables printing verbose output.
| `-h`, `--help` | Prints information on usage of `kn func invoke`.
|===

[id="serverless-kn-func-invoke-main-parameters_{context}"]
== Main parameters

The following parameters define the main properties of the `kn func invoke` command:

Event target (`-t`, `--target`):: The target instance of the invoked function. Accepts the `local` value for a locally deployed function, the `remote` value for a remotely deployed function, or a URL for a function deployed to an arbitrary endpoint. If a target is not specified, it defaults to `local`.
Event message format (`-f`, `--format`):: The message format for the event, such as `http` or `cloudevent`. This defaults to the format of the template that was used when creating the function.
Event type (`--type`):: The type of event that is sent. You can find information about the `type` parameter that is set in the documentation for each event producer. For example, the API server source might set the `type` parameter of produced events as `dev.knative.apiserver.resource.update`.
Event source (`--source`):: The unique event source that produced the event. This might be a URI for the event source, for example `https://10.96.0.1/`, or the name of the event source.
Event ID (`--id`):: A random, unique ID that is created by the event producer.
Event data (`--data`):: Allows you to specify a `data` value for the event sent by the `kn func invoke` command. For example, you can specify a `--data` value such as `"Hello World"` so that the event contains this data string. By default, no data is included in the events created by `kn func invoke`.
+
[NOTE]
====
Functions that have been deployed to a cluster can respond to events from an existing event source that provides values for properties such as `source` and `type`. These events often have a `data` value in JSON format, which captures the domain specific context of the event. By using the CLI flags noted in this document, developers can simulate those events for local testing.
====
+
You can also send event data using the `--file` flag to provide a local file containing data for the event. In this case, specify the content type using `--content-type`.
Data content type (`--content-type`):: If you are using the `--data` flag to add data for events, you can use the `--content-type` flag to specify what type of data is carried by the event. In the previous example, the data is plain text, so you might specify `kn func invoke --data "Hello world!" --content-type "text/plain"`.

[id="serverless-kn-func-invoke-example-commands_{context}"]
== Example commands

This is the general invocation of the `kn func invoke` command:

[source,terminal]
----
$ kn func invoke --type <event_type> --source <event_source> --data <event_data> --content-type <content_type> --id <event_ID> --format <format> --namespace <namespace>
----

For example, to send a "Hello world!" event, you can run:

[source,terminal]
----
$ kn func invoke --type ping --source example-ping --data "Hello world!" --content-type "text/plain" --id example-ID --format http --namespace my-ns
----

[id="serverless-kn-func-invoke-example-commands-specifying-file-with-data_{context}"]
=== Specifying the file with data

To specify the file on disk that contains the event data, use the `--file` and `--content-type` flags:

[source,terminal]
----
$ kn func invoke --file <path> --content-type <content-type>
----

For example, to send JSON data stored in the `test.json` file, use this command:

[source,terminal]
----
$ kn func invoke --file ./test.json --content-type application/json
----

[id="serverless-kn-func-invoke-example-commands-specifying-function-project_{context}"]
=== Specifying the function project

You can specify a path to the function project by using the `--path` flag:

[source,terminal]
----
$ kn func invoke --path <path_to_function>
----

For example, to use the function project located in the `./example/example-function` directory, use this command:

[source,terminal]
----
$ kn func invoke --path ./example/example-function
----

[id="serverless-kn-func-invoke-example-commands-specifying-where-function-is-deployed_{context}"]
=== Specifying where the target function is deployed

By default, `kn func invoke` targets the local deployment of the function:

[source,terminal]
----
$ kn func invoke
----

To use a different deployment, use the `--target` flag:

[source,terminal]
----
$ kn func invoke --target <target>
----

For example, to use the function deployed on the cluster, use the `--target remote` flag:

[source,terminal]
----
$ kn func invoke --target remote
----

To use the function deployed at an arbitrary URL, use the `--target <URL>` flag:

[source,terminal]
----
$ kn func invoke --target "https://my-event-broker.example.com"
----

You can explicitly target the local deployment. In this case, if the function is not running locally, the command fails:

[source,terminal]
----
$ kn func invoke --target local
----
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
