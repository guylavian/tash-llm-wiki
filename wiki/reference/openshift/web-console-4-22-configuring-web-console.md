---
title: "Configuring the web console in {product-title}"
type: reference
domain: openshift
slug: web-console-4-22-configuring-web-console
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/configuring-web-console
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Configuring the web console in {product-title}

[id="configuring-web-console"]
= Configuring the web console in OpenShift Container Platform

You can modify the OpenShift Container Platform web console to set a logout redirect URL
or disable the quick start tutorials.

== Prerequisites

* Deploy an OpenShift Container Platform cluster.

// Hiding in ROSA/OSD, as dedicated-admins cannot create "consoles" resource
// Module included in the following assemblies:
//
// * web_console/configuring-web-console.adoc

[id="web-console-configuration_{context}"]
= Configuring the web console

You can configure the web console settings by editing the `console.config.openshift.io` resource.

* Edit the `console.config.openshift.io` resource:
+
[source,terminal]
----
$ oc edit console.config.openshift.io cluster
----
+
The following example displays the sample resource definition for the console:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  authentication:
    logoutRedirect: "" <1>
status:
  consoleURL: "" <2>
----
<1> Specify the URL of the page to load when a user logs out of the web console. If you do not specify a value, the user returns to the login page for the web console. Specifying a `logoutRedirect` URL allows your users to perform single logout (SLO) through the identity provider to destroy their single sign-on session.
<2> The web console URL. To update this to a custom value, see *Customizing the web console URL*.

// Hiding in ROSA/OSD, as dedicated-admins do not have sufficient permissions to read any cluster configuration
// Module included in the following assemblies:
//
// * web_console/configuring-web-console.adoc

[id="disable-quickstarts-admin-console_{context}"]
= Disabling quick starts in the web console

You can use the *Administrator* perspective of the web console to disable one or more quick starts.

.Prerequisites

* You have cluster administrator permissions and are logged in to the web console.

. On the *General* tab, in the *Quick starts* section, you can select items in either the *Enabled* or *Disabled* list, and move them from one list to the other by using the arrow buttons.

** To enable or disable a single quick start, click the quick start, then use the single arrow buttons to move the quick start to the appropriate list.
** To enable or disable multiple quick starts at once, press Ctrl and click the quick starts you want to move. Then, use the single arrow buttons to move the quick starts to the appropriate list.
** To enable or disable all quick starts at once, click the double arrow buttons to move all of the quick starts to the appropriate list.
