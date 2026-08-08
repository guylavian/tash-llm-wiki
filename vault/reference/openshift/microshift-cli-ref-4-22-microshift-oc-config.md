---
title: "Configuring the OpenShift CLI"
type: reference
domain: openshift
slug: microshift-cli-ref-4-22-microshift-oc-config
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_cli_ref/microshift-oc-config
version: 4.22
family: microshift_cli_ref
documentKind: "Documentation"
---

# Configuring the OpenShift CLI

[id="cli-configuring-cli"]
= Configuring the OpenShift CLI

[role="_abstract"]
Configure {oc-first} based on your preferences for working with it.

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
