---
title: "Log visualization with the web console"
type: reference
domain: openshift
slug: observability-4-22-log-visualization-ocp-console
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/log-visualization-ocp-console
version: 4.22
family: observability
documentKind: "Documentation"
---

# Log visualization with the web console

[id="log-visualization-ocp-console"]
= Log visualization with the web console

You can use the OpenShift Container Platform web console to visualize log data by configuring the {log-plug}. Options for configuration are available during installation of {logging} on the web console.

If you have already installed {logging} and want to configure the plugin, use one of the following procedures.

// Module included in the following assemblies:
//
// * observability/logging/log_visualization/log-visualization-ocp-console.adoc

[id="enabling-log-console-plugin_{context}"]
= Enabling the {log-plug} after you have installed the {clo}

You can enable the {log-plug} as part of the {clo} installation, but you can also enable the plugin if you have already installed the {clo} with the plugin disabled.

.Prerequisites

* You have administrator permissions.
* You have installed the {clo} and selected *Disabled* for the *Console plugin*.
* You have access to the OpenShift Container Platform web console.

.Procedure

. In the OpenShift Container Platform web console *Administrator* perspective, navigate to *Ecosystem* -> *Installed Operators*.
. Click *Red Hat OpenShift Logging*. This takes you to the Operator *Details* page.
. In the *Details* page, click *Disabled* for the *Console plugin* option.
. In the *Console plugin enablement* dialog, select *Enable*.
. Click *Save*.
. Verify that the *Console plugin* option now shows *Enabled*.
. The web console displays a pop-up window when changes have been applied. The window prompts you to reload the web console. Refresh the browser when you see the pop-up window to apply the changes.
// Module included in the following assemblies:
//
// * observability/logging/log_visualization/log-visualization-ocp-console.adoc

[id="logging-plugin-es-loki_{context}"]
= Configuring the {log-plug} when you have the Elasticsearch log store and LokiStack installed

In {logging} version 5.8 and later, if the Elasticsearch log store is your default log store but you have also installed the LokiStack, you can enable the {log-plug} by using the following procedure.

.Prerequisites

* You have administrator permissions.
* You have installed the {clo}, the {es-op}, and the {loki-op}.
* You have installed the {oc-first}.
* You have created a `ClusterLogging` custom resource (CR).

.Procedure

. Ensure that the {log-plug} is enabled by running the following command:
+
[source,terminal]
----
$ oc get consoles.operator.openshift.io cluster -o yaml |grep logging-view-plugin  \
|| oc patch consoles.operator.openshift.io cluster  --type=merge \
--patch '{ "spec": { "plugins": ["logging-view-plugin"]}}'
----

. Add the `.metadata.annotations.logging.openshift.io/ocp-console-migration-target: lokistack-dev` annotation to the `ClusterLogging` CR, by running the following command:
+
[source,terminal]
----
$ oc patch clusterlogging instance --type=merge --patch \
'{ "metadata": { "annotations": { "logging.openshift.io/ocp-console-migration-target": "lokistack-dev" }}}' \
-n openshift-logging
----
+
.Example output
[source,terminal]
----
clusterlogging.logging.openshift.io/instance patched
----

.Verification

* Verify that the annotation was added successfully, by running the following command and observing the output:
+
[source,terminal]
----
$ oc get clusterlogging instance \
-o=jsonpath='{.metadata.annotations.logging\.openshift\.io/ocp-console-migration-target}' \
-n openshift-logging
----
+
.Example output
[source,terminal]
----
"lokistack-dev"
----

The {log-plug} pod is now deployed. You can view logging data by navigating to the OpenShift Container Platform web console and viewing the *Observe* -> *Logs* page.
