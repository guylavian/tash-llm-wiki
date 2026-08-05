---
title: "Extending the OpenShift CLI with plugins"
type: reference
domain: openshift
slug: cli-reference-4-22-extending-cli-plugins
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/extending-cli-plugins
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Extending the OpenShift CLI with plugins

[id="cli-extend-plugins"]
= Extending the OpenShift CLI with plugins

You can write and install plugins to build on the default `oc` commands,
allowing you to perform new and more complex tasks with the
OpenShift Container Platform
OpenShift
CLI.

// Writing CLI plugins
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/extending-cli-plugins.adoc

[id="cli-writing-plugins_{context}"]
= Writing CLI plugins

You can write a plugin for the
OpenShift Container Platform
OpenShift
CLI in any programming language
or script that allows you to write command-line commands. Note that you can not
use a plugin to overwrite an existing `oc` command.

.Procedure

This procedure creates a simple Bash plugin that prints a message to the
terminal when the `oc foo` command is issued.

. Create a file called `oc-foo`.
+
When naming your plugin file, keep the following in mind:

* The file must begin with `oc-` or `kubectl-` to be recognized as a
plugin.
* The file name determines the command that invokes the plugin. For example, a
plugin with the file name `oc-foo-bar` can be invoked by a command of
`oc foo bar`. You can also use underscores if you want the command to contain
dashes. For example, a plugin with the file name `oc-foo_bar` can be invoked
by a command of `oc foo-bar`.

. Add the following contents to the file.
+
[source,bash]
----
#!/bin/bash

# optional argument handling
if [[ "$1" == "version" ]]
then
    echo "1.0.0"
    exit 0
fi

# optional argument handling
if [[ "$1" == "config" ]]
then
    echo $KUBECONFIG
    exit 0
fi

echo "I am a plugin named kubectl-foo"
----

After you install this plugin for the
OpenShift Container Platform
OpenShift
CLI, it can be invoked
using the `oc foo` command.

[role="_additional-resources"]
.Additional resources

* Review the Sample plugin repository
for an example of a plugin written in Go.
* Review the CLI runtime repository for a set of utilities to assist in writing plugins in Go.

// Installing and using CLI plugins
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/extending-cli-plugins.adoc

[id="cli-installing-plugins_{context}"]
= Installing and using CLI plugins

After you write a custom plugin for the
OpenShift Container Platform
OpenShift
CLI, you must install
the plugin before use.

.Prerequisites

* You must have the `oc` CLI tool installed.
* You must have a CLI plugin file that begins with `oc-` or `kubectl-`.

.Procedure

. If necessary, update the plugin file to be executable.
+
[source,terminal]
----
$ chmod +x <plugin_file>
----
. Place the file anywhere in your `PATH`, such as `/usr/local/bin/`.
+
[source,terminal]
----
$ sudo mv <plugin_file> /usr/local/bin/.
----
. Run `oc plugin list` to make sure that the plugin is listed.
+
[source,terminal]
----
$ oc plugin list
----
+
.Example output
[source,terminal]
----
The following compatible plugins are available:

/usr/local/bin/<plugin_file>
----
+
If your plugin is not listed here, verify that the file begins with `oc-`
or `kubectl-`, is executable, and is on your `PATH`.
. Invoke the new command or option introduced by the plugin.
+
For example, if you built and installed the `kubectl-ns` plugin from the
 Sample plugin repository,
  you can use the following command to view the current namespace.
+
[source,terminal]
----
$ oc ns
----
+
Note that the command to invoke the plugin depends on the plugin file name.
For example, a plugin with the file name of `oc-foo-bar` is invoked by the `oc foo bar`
command.
