---
title: "Using the web terminal"
type: reference
domain: openshift
slug: web-console-4-22-odc-using-web-terminal
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/odc-using-web-terminal
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Using the web terminal

[id="odc-using-web-terminal"]
= Using the web terminal

[role="_abstract"]
You can launch an embedded command-line terminal instance in the web console. This terminal instance is preinstalled with common CLI tools for interacting with the cluster, such as `oc`, `kubectl`,`odo`, `kn`, `tkn`, `helm`, and `subctl`. It also has the context of the project you are working on and automatically logs you in using your credentials.

// Module included in the following assemblies:
//
// web_console/web_terminal/odc-using-web-terminal.adoc

[id="odc-access-web-terminal_{context}"]
= Accessing the web terminal

[role="_abstract"]
After the {web-terminal-op} is installed, you can access the web terminal. After the web terminal is initialized, you can use the preinstalled CLI tools like `oc`, `kubectl`, `odo`, `kn`, `tkn`, `helm`, and `subctl` in the web terminal.
You can re-run commands by selecting them from the list of commands you have run in the terminal. These commands persist across multiple terminal sessions.
The web terminal remains open until you close it or until you close the browser window or tab.

.Prerequisites

* You have access to
an OpenShift Container Platform
a OpenShift Container Platform
cluster and are logged into the web console.
* The {web-terminal-op} is installed on your cluster.

.Procedure

. To launch the web terminal, click the command-line terminal icon (image:odc-wto-icon.png[title="wto icon"]) in the masthead of the console. A web terminal instance is displayed in the *Command line terminal* pane. This instance is automatically logged in with your credentials.

. If a project has not been selected in the current session, select the project where the `DevWorkspace` CR must be created from the *Project* drop-down list. By default, the current project is selected.
+
[NOTE]
====
* One `DevWorkspace` CR defines the web terminal of one user. This CR contains details about the user's web terminal status and container image components.
* The `DevWorkspace` CR is created only if it does not already exist.
* The `openshift-terminal` project is the default project used for cluster administrators. They do not have the option to choose another project.  The {web-terminal-op} installs the DevWorkspace Operator as a dependency.
====

. Optional: Set the web terminal timeout for the current session:
.. Click Timeout.
.. In the field that appears, enter the timeout value.
.. From the drop-down list, select a timeout interval of *Seconds*, *Minutes*, *Hours*, or *Milliseconds*.

. Optional: Select a custom image for the web terminal to use.
.. Click Image.
.. In the field that appears, enter the URL of the image that you want to use.

. Click *Start* to initialize the web terminal using the selected project.

. Click *+* to open multiple tabs within the web terminal in the console.
