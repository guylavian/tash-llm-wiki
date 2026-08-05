---
title: "Configuring the web terminal"
type: reference
domain: openshift
slug: web-console-4-22-configuring-web-terminal
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/configuring-web-terminal
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Configuring the web terminal

[id="configuring-web-terminal"]
= Configuring the web terminal

You can configure timeout and image settings for the web terminal, either for your current session or for all user sessions if you are a cluster administrator.

// Module is included in the following assemblies:
//
// * web_console/web_terminal/configuring-web-terminal.adoc

[id="odc-configure-web-terminal-timeout-session_{context}"]
= Configuring the web terminal timeout for a session

You can change the default timeout period for the web terminal for your current session.

.Prerequisites

* You have access to
an OpenShift Container Platform
a OpenShift Container Platform
cluster that has the {web-terminal-op} installed.
* You are logged into the web console.

.Procedure

. Click the web terminal icon (image:odc-wto-icon.png[title="web terminal icon"]).
. Optional: Set the web terminal timeout for the current session:
.. Click Timeout.
.. In the field that appears, enter the timeout value.
.. From the drop-down list, select a timeout interval of *Seconds*, *Minutes*, *Hours*, or *Milliseconds*.
. Optional: Select a custom image for the web terminal to use.
.. Click Image.
.. In the field that appears, enter the URL of the image that you want to use.
. Click *Start* to begin a terminal instance using the specified timeout setting.

// Module is included in the following assemblies:
//
// * web_console/web_terminal/configuring-web-terminal.adoc

[id="configure-web-terminal-timeout-admin_{context}"]
= Configuring the web terminal timeout for all users

You can use the *Administrator* perspective of the web console to set the default web terminal timeout period for all users.

.Prerequisites

* You have cluster administrator permissions and are logged in to the web console.
* You have installed the {web-terminal-op}.

. Click the *Web Terminal* tab, which opens the *Web Terminal Configuration* page.
. Set a value for the timeout. From the drop-down list, select a time interval of *Seconds*, *Minutes*, *Hours*, or *Milliseconds*.
. Click *Save*.

// Module is included in the following assemblies:
//
// * web_console/web_terminal/configuring-web-terminal.adoc

[id="odc-configure-web-terminal-image-session_{context}"]
= Configuring the web terminal image for a session

You can change the default image for the web terminal for your current session.

.Prerequisites

* You have access to
an OpenShift Container Platform
a OpenShift Container Platform
cluster that has the {web-terminal-op} installed.
* You are logged into the web console.

.Procedure

. Click the web terminal icon (image:odc-wto-icon.png[title="web terminal icon"]).
. Click *Image* to display advanced configuration options for the web terminal image.
. Enter the URL of the image that you want to use.
. Click *Start* to begin a terminal instance using the specified image setting.

// Module is included in the following assemblies:
//
// * web_console/web_terminal/configuring-web-terminal.adoc

[id="configure-web-terminal-image-admin_{context}"]
= Configuring the web terminal image for all users

You can use the *Administrator* perspective of the web console to set the default web terminal image for all users.

.Prerequisites

* You have cluster administrator permissions and are logged in to the web console.
* You have installed the {web-terminal-op}.

. Click the *Web Terminal* tab, which opens the *Web Terminal Configuration* page.
. Enter the URL of the image that you want to use.
. Click *Save*.
