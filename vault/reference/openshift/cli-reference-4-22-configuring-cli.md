---
title: "Configuring the OpenShift CLI"
type: reference
domain: openshift
slug: cli-reference-4-22-configuring-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/configuring-cli
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Configuring the OpenShift CLI

[id="cli-configuring-cli"]
= Configuring the OpenShift CLI

[id="cli-enabling-tab-completion"]
== Enabling tab completion

You can enable tab completion for the Bash or Zsh shells.

// Enabling tab completion for Bash
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/configuring-cli.adoc

[id="cli-enabling-tab-completion_{context}"]
= Enabling tab completion for Bash

[role="_abstract"]
After you install the OpenShift CLI (`oc`), you can enable tab completion to automatically complete `oc` commands or suggest options when you press Tab. The following procedure enables tab completion for the Bash shell.

.Prerequisites

* You must have the OpenShift CLI (`oc`) installed.
* You must have the package `bash-completion` installed.

.Procedure

. Save the Bash completion code to a file:
+
[source,terminal]
----
$ oc completion bash > oc_bash_completion
----

. Copy the file to `/etc/bash_completion.d/`:
+
[source,terminal]
----
$ sudo cp oc_bash_completion /etc/bash_completion.d/
----
+
You can also save the file to a local directory and source it from your `.bashrc` file instead. Tab completion is enabled when you open a new terminal.

// Enabling tab completion for Zsh
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/configuring-cli.adoc

[id="cli-enabling-tab-completion-zsh_{context}"]
= Enabling tab completion for Zsh

[role="_abstract"]
After you install the OpenShift CLI (`oc`), you can enable tab completion to automatically complete `oc` commands or suggest options when you press Tab. The following procedure enables tab completion for the Zsh shell.

.Prerequisites

* You must have the OpenShift CLI (`oc`) installed.

.Procedure

* To add tab completion for `oc` to your `.zshrc` file, run the following command:
+
[source,terminal]
----
$ cat >>~/.zshrc<<EOF
autoload -Uz compinit
compinit
if [ $commands[oc] ]; then
  source <(oc completion zsh)
  compdef _oc oc
fi
EOF
----
+
Tab completion is enabled when you open a new terminal.

// Configuring a kubeconfig file by using the oc CLI
// Module included in the following assemblies:
//
// * cli_reference/openshift_cli/configuring-cli.adoc

[id="cli-accessing-kubeconfig-using-cli_{context}"]
= Accessing kubeconfig by using the oc CLI

You can use the `oc` CLI to log in to your OpenShift cluster and retrieve a kubeconfig file for accessing the cluster from the command line.

.Prerequisites

* You have access to the OpenShift Container Platform web console or API server endpoint.

.Procedure

. Log in to your OpenShift cluster by running the following command:
+
[source,terminal]
----
$ oc login <api-server-url> -u <username> -p <password> <1><2><3>
----
+
<1> Specify the full API server URL. For example: `https://api.my-cluster.example.com:6443`.
<2> Specify a valid username. For example: `kubeadmin`.
<3> Provide the password for the specified user. For example, the `kubeadmin` password generated during cluster installation.

. Save the cluster configuration to a local file by running the following command:
+
[source,terminal]
----
$ oc config view --raw > kubeconfig
----

. Set the `KUBECONFIG` environment variable to point to the exported file by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=./kubeconfig
----

. Use `oc` to interact with your OpenShift cluster by running the following command:
+
[source,terminal]
----
$ oc get nodes
----

[NOTE]
====
If you plan to reuse the exported `kubeconfig` file across sessions or machines, store it securely and avoid committing it to source control.
====
