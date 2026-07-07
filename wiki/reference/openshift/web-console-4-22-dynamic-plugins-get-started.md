---
title: "Getting started with dynamic plugins"
type: reference
domain: openshift
slug: web-console-4-22-dynamic-plugins-get-started
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/dynamic-plugins-get-started
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Getting started with dynamic plugins

[id="dynamic-plugins-get-started_{context}"]
= Getting started with dynamic plugins

[role="_abstract"]
To get started using the dynamic plugin, you must set up your environment to write a new OpenShift Container Platform dynamic plugin. For an example of how to write a new plugin, see Adding a tab to the pods page.

// Module included in the following assemblies:
//
// * web_console/dynamic-plugin/dynamic-plugins-get-started.adoc

[id="dynamic-plugin-development_{context}"]
= Dynamic plugin development

[role="_abstract"]
You can run the plugin using a local development environment. The OpenShift Container Platform web console runs in a container connected to the cluster you have logged into.

.Prerequisites

* You must have cloned the `console-plugin-template` repository, which contains a template for creating plugins.
+
[IMPORTANT]
====
Red{nbsp}Hat does not support custom plugin code. Only Cooperative community support is available for your plugin.
====
* You must have
an OpenShift Container Platform
a OpenShift Container Platform
cluster running.
* You must have the {oc-first} installed.
* You must have `yarn` installed.
* You must have Docker v3.2.0 or later or Podman v3.2.0 or later installed and running.

.Procedure

. Open two terminal windows.

. In one terminal window, run the following command to install the dependencies for your plugin using yarn.

+
[source,terminal]
----
$ yarn install
----

. After installing, run the following command to start yarn.
+
[source,terminal]
----
$ yarn run start
----

. In another terminal window, login to the OpenShift Container Platform web console through the CLI.
+
[source,terminal]
----
$ oc login
----

. Run the OpenShift Container Platform web console in a container connected to the cluster you have logged in to by running the following command:
+
[source,terminal]
----
$ yarn run start-console
----
+
[NOTE]
====
The `yarn run start-console` command runs an `amd64` image and might fail when run with Apple Silicon and Podman. You can work around it with `qemu-user-static` by running the following commands:

[source,terminal]
----
$ podman machine ssh
----

[source,terminal]
----
$ sudo -i
----

[source,terminal]
----
$ rpm-ostree install qemu-user-static
----

[source,terminal]
----
$ systemctl reboot
----
====

.Verification

* Visit localhost:9000 to view the running plugin. Inspect the value of `window.SERVER_FLAGS.consolePlugins` to see the list of plugins which load at runtime.
