---
title: "Using the {cli-manager}"
type: reference
domain: openshift
slug: cli-reference-4-22-cli-manager-using
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/cli-manager-using
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Using the {cli-manager}

[id="cli-manager-using"]
= Using the {cli-manager}

[role="_abstract"]
To install, update, and uninstall CLI plugins in OpenShift Container Platform, you can set up and configure the {cli-manager}.

// Installing a CLI plugin with the CLI Manager
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-using.adoc

[id="cli-manager-adding-plugins_{context}"]
= Installing CLI plugins with the {cli-manager}

[role="_abstract"]
You can install CLI plugins with the {cli-manager} to extend OpenShift CLI functionality in both connected and disconnected environments.

.Prerequisites

* You have installed Krew by following the installation procedure in the Krew documentation.
* The {cli-manager} is installed.
* The {cli-manager} custom index has been added to Krew.
* You are using OpenShift Container Platform 4.17 or later.

.Procedure

. To list all available plugins, run the following command:
+
[source,terminal]
----
$ oc krew search
----

. To get information about a plugin, run the following command:
+
[source,terminal]
----
$ oc krew info <plugin_name>
----

. To install a plugin, run the following command:
+
[source,terminal]
----
$ oc krew install <plugin_name>
----

. To list all plugins that were installed by Krew, run the following command:
+
[source,terminal]
----
$ oc krew list
----

// Upgrading a CLI plugin with the CLI Manager
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-using.adoc

[id="cli-manager-upgrading-plugin-yamls_{context}"]
= Upgrading a plugin with the {cli-manager}

[role="_abstract"]
You can upgrade a CLI plugin to a newer version with the {cli-manager} by directly editing the plugin's resource YAML file.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* The {cli-manager} is installed.
* The plugin you are upgrading is installed.

.Procedure

. Using the CLI, enter the following command:
+
[source,terminal]
----
oc edit plugin/<plugin_name>
----

. Edit the YAML file to include the new specifications for your plugin.
+
.Example YAML file to upgrade a plugin

[source,yaml]
----
apiVersion: config.openshift.io/v1alpha1
kind: Plugin
metadata:
  name: <plugin_name> <1>
spec:
  description: <description_of_plugin>
  homepage: <plugin_homepage>
  platforms:
  - bin: <2>
    files:
    - from: <plugin_file_path>
      to: .
    image: <plugin_image>
    imagePullSecret: <3>
    platform: <platform> <4>
  shortDescription: <short_description_of_plugin>
  version: <version> <5>
----
+
where:
+
--
`<plugin_name>`:: Specifies the name of the plugin you plan to use in commands.
`bin`:: Specifies the path to the plugin executable.
`imagePullSecret`:: Optional field if the registry is not public to add a pull secret to access your plugin image.
`<platform>`:: Add the architecture for your system; for example, `linux/amd64`, `darwin/arm64`, `windows/amd64`, or another architecture.
`<version>`:: The version must be in v0.0.0 format.
--

. Save the file.

// Updating a cli plugin with the CLI Manager
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-using.adoc

[id="cli-manager-updating-plugin_{context}"]
= Updating CLI plugins with the {cli-manager}

[role="_abstract"]
You can update a plugin that was installed for the OpenShift CLI (`oc`) with the {cli-manager} and Krew to keep your plugins current with the latest features.

.Prerequisites

* You have installed Krew by following the installation procedure in the Krew documentation.
* The {cli-manager} is installed.
* The custom index has been added to Krew by the cluster administrator.
* The plugin updates have been added to the {cli-manager} by the cluster administrator.
* The plugin you are updating is already installed.

.Procedure

* To update a single plugin, run the following command:
+
[source,terminal]
----
$ oc krew upgrade <plugin_name>
----

* To update all plugins that were installed by Krew, run the following command:
+
[source,terminal]
----
$ oc krew upgrade
----

// Uninstalling a CLI plugin with the CLI Manager
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-using.adoc

[id="cli-manager-remove-plugin_{context}"]
= Uninstalling a CLI plugin with the {cli-manager}

[role="_abstract"]
You can uninstall a plugin that was installed for the OpenShift CLI (`oc`) with the {cli-manager}.

.Prerequisites

* You have installed Krew by following the installation procedure in the Krew documentation.
* You have installed a plugin for the OpenShift CLI with the {cli-manager}.

.Procedure

* To uninstall a plugin, run the following command:
+
[source,terminal]
----
$ oc krew uninstall <plugin_name>
----
