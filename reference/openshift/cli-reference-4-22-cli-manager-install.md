---
title: "Installing the {cli-manager}"
type: reference
domain: openshift
slug: cli-reference-4-22-cli-manager-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/cli-manager-install
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Installing the {cli-manager}

[id="cli-manager-install"]
= Installing the {cli-manager}

[role="_abstract"]
You can simplify the installation and management of CLI plugins in connected and disconnected environments with the {cli-manager}. The {cli-manager} makes Krew compatible with the `oc` CLI, allowing cluster administrators to manage custom CLI plugin resources.

// Installing the {cli-manager}
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-install.adoc

[id="cli-manager-installing_{context}"]
= Installing the {cli-manager}

[role="_abstract"]
You can install the {cli-manager} to facilitate adding CLI plugins in both connected and disconnected environments.

[NOTE]
====
Krew always works with {oc-first} without the {cli-manager} installed. You can use the same commands outlined in this documentation to use Krew with `oc`. For more information, see Krew documentation.
====

.Prerequisites

* Krew is installed.
* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* You have access to the OpenShift Container Platform web console.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Create the required namespace for the {cli-manager}:
.. Navigate to *Administration* -> *Namespaces* and click *Create Namespace*.
.. In the *Name* field, enter `openshift-cli-manager-operator` and click *Create*.

. Install the {cli-manager}:
.. Navigate to *Ecosystem* -> *Software Catalog*.
.. In the filter box, enter *{cli-manager}*.
.. Select the *{cli-manager}* and click *Install*.
.. On the *Install Operator* page, complete the following steps:
... Ensure that the *Update channel* is set to *tech preview*, which installs the latest Technology Preview release of the {cli-manager}.
... From the drop-down menu, select *A specific namespace on the cluster* and select *openshift-cli-manager-operator*.
... Click *Install*.

. Create the `CliManager` resource by completing the following steps:
.. Navigate to *Installed Operators*.
.. Select *{cli-manager}*.
.. Select the *CLI Manager* tab.
.. Click *Create CliManager*.
.. Use the default *Name*.
.. Click *Create*.
... The new `CliManager` resource is listed in the *CLI Manager* tab.

.Verification

. Navigate to *Ecosystem* -> *Installed Operators*.
. Verify that *{cli-manager}* is listed with a *Status* of *Succeeded*.

// Adding CLI Manager custom index to krew
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-install.adoc

[id="cli-manager-custom-index_{context}"]
= Adding the {cli-manager} custom index to Krew

[role="_abstract"]
You can use the terminal to add the {cli-manager} custom index to Krew so that the {cli-manager} will work in disconnected environments. This procedure is required for the {cli-manager} to function correctly and needs to be done only once.

[NOTE]
====
If you use self-signed certificates, mark the certificate as trusted on your local operating system to use Krew.
====

.Prerequisites

* Krew is installed.
* The {cli-manager} is installed.

.Procedure

. To establish the `ROUTE` variable, enter the following command:
+
[source,terminal]
----
$ ROUTE=$(oc get route/openshift-cli-manager -n openshift-cli-manager-operator -o=jsonpath='{.spec.host}')
----

. To add the custom index to Krew, enter the following command:
+
[source,terminal]
----
$ oc krew index add <custom_index_name> https://$ROUTE/cli-manager
----

. To update Krew, enter the following command and check for any errors:
+
[source,terminal]
----
$ oc krew update
----
+
.Example output
[source,terminal]
----
Updated the local copy of plugin index.
Updated the local copy of plugin index <custom_index_name>.
New plugins available:
* ocp/<plugin_name>
----

// Adding CLI plugins with YAML files
// Module included in the following assemblies:
//
// * cli_reference/cli_manager/cli-manager-install.adoc

[id="cli-manager-adding-plugin-yamls_{context}"]
= Adding a plugin to the {cli-manager}

[role="_abstract"]
You can add a CLI plugin to the {cli-manager} by creating a new plugin resource in the OpenShift Container Platform web console's YAML view.

.Prerequisites

* You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role.
* The {cli-manager} is installed.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. From the list, select *{cli-manager}*.

. Select the *CLI Plugin* tab.

. Click *Create Plugin*.

. In the text box, enter the information for the plugin you are installing. See the following example YAML file.
+
.Example YAML file to add a plugin

[source,yaml]
----
apiVersion: config.openshift.io/v1alpha1
kind: Plugin
metadata:
  name: <plugin_name>
spec:
  description: <description_of_plugin>
  homepage: <plugin_homepage>
  platforms:
  - bin:
    files:
    - from: <plugin_file_path>
      to: .
    image: <plugin_image>
    imagePullSecret:
    platform: <platform>
  shortDescription: <short_description_of_plugin>
  version: <version>
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

. Click *Save*.

.Verification

* Enter the following command to see if the plugin is listed and has been added successfully:

[source,terminal]
----
$ oc get plugin/<plugin_name> -o yaml
----

* Example output:

[source,terminal]
----
<plugin_name> ready to be served.
----
