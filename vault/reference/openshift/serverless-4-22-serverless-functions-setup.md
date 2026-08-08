---
title: "Setting up {FunctionsProductName}"
type: reference
domain: openshift
slug: serverless-4-22-serverless-functions-setup
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-functions-setup
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Setting up {FunctionsProductName}

[id="serverless-functions-setup"]
= Setting up {FunctionsProductName}

To improve the process of deployment of your application code, you can use {ServerlessProductName} to deploy stateless, event-driven functions as a Knative service on OpenShift Container Platform. If you want to develop functions, you must complete the set up steps.

[id="prerequisites_serverless-functions-setup"]
== Prerequisites

To enable the use of {FunctionsProductName} on your cluster, you must complete the following steps:

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.
+
[NOTE]
====
Functions are deployed as a Knative service. If you want to use event-driven architecture with your functions, you must also install Knative Eventing.
====

* You have the `oc` CLI installed.
// need to wait til CLI docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available
* You have the `oc` CLI installed.

* You have the Knative (`kn`) CLI installed. Installing the Knative CLI enables the use of `kn func` commands which you can use to create and manage functions.

* You have installed Docker Container Engine or Podman version 3.4.7 or higher.

* You have access to an available image registry, such as the OpenShift Container Registry.

* If you are using Quay.io as the image registry, you must ensure that either the repository is not private, or that you have followed the OpenShift Container Platform documentation on Allowing pods to reference images from other secured registries.
// need to wait til images docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available
* If you are using Quay.io as the image registry, you must ensure that either the repository is not private, or that you have allowed pods on your cluster to reference images from other secured registries.

* If you are using the OpenShift Container Registry, a cluster administrator must expose the registry.
// need to wait til registry docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available
* If you are using the OpenShift Container Registry, a cluster or dedicated administrator must expose the registry.

// Module included in the following assemblies:
//
// * serverless/serverless-functions-setup.adoc

[id="serverless-functions-podman_{context}"]
= Setting up Podman

To use advanced container management features, you might want to use Podman with {FunctionsProductName}. To do so, you need to start the Podman service and configure the Knative (`kn`) CLI to connect to it.

.Procedure

// This step might no longer be needed in the future, when automatic
// podman startup is reliable.
// https://github.com/openshift/openshift-docs/pull/46660/files#r907310116
. Start the Podman service that serves the Docker API on a UNIX socket at `${XDG_RUNTIME_DIR}/podman/podman.sock`:
+
[source,terminal]
----
$ systemctl start --user podman.socket
----
+
[NOTE]
====
On most systems, this socket is located at `/run/user/$(id -u)/podman/podman.sock`.
====

. Establish the environment variable that is used to build a function:
+
[source,terminal]
----
$ export DOCKER_HOST="unix://${XDG_RUNTIME_DIR}/podman/podman.sock"
----

. Run the build command inside your function project directory with the `-v` flag to see verbose output. You should see a connection to your local UNIX socket:
+
[source,terminal]
----
$ kn func build -v
----
// Module included in the following assemblies:
//
// * serverless/functions/serverless-functions-setup.adoc

[id="serverless-functions-podman-macos_{context}"]
= Setting up Podman on macOS

To use advanced container management features, you might want to use Podman with {FunctionsProductName}. To do so on macOS, you need to start the Podman machine and configure the Knative (`kn`) CLI to connect to it.

.Procedure

. Create the Podman machine:
+
[source,terminal]
----
$ podman machine init --memory=8192 --cpus=2 --disk-size=20
----

. Start the Podman machine, which serves the Docker API on a UNIX socket:
+
[source,terminal]
----
$ podman machine start
Starting machine "podman-machine-default"
Waiting for VM ...
Mounting volume... /Users/myuser:/Users/user

[...truncated output...]

You can still connect Docker API clients by setting DOCKER_HOST using the
following command in your terminal session:

	export DOCKER_HOST='unix:///Users/myuser/.local/share/containers/podman/machine/podman-machine-default/podman.sock'

Machine "podman-machine-default" started successfully
----
+
[NOTE]
====
On most macOS systems, this socket is located at `/Users/myuser/.local/share/containers/podman/machine/podman-machine-default/podman.sock`.
====

. Establish the environment variable that is used to build a function:
+
[source,terminal]
----
$ export DOCKER_HOST='unix:///Users/myuser/.local/share/containers/podman/machine/podman-machine-default/podman.sock'
----

. Run the build command inside your function project directory with the `-v` flag to see verbose output. You should see a connection to your local UNIX socket:
+
[source,terminal]
----
$ kn func build -v
----

[id="next-steps_serverless-functions-setup"]
== Next steps

* For more information about Docker Container Engine or Podman, see Container build tool options.
// need to wait til build tool docs are added to OSD and ROSA for this link to work
// TODO: remove these conditionals once this is available

* See Getting started with functions.
