---
title: "OpenShift Service Mesh Console plugin"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-kiali-ossmc-plugin
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-kiali-ossmc-plugin
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# OpenShift Service Mesh Console plugin

[id="ossm-kiali-ossmc-plugin"]
= OpenShift Service Mesh Console plugin

The {SMPlugin} is an extension to the OpenShift Container Platform web console that provides visibility into your Service Mesh. With the OSSMC plugin installed, a new *Service Mesh* menu option is available in the navigation menu on the left side of the web console, as well as new *Service Mesh* tabs that enhance the existing *Workloads* and *Services* console pages.

[IMPORTANT]
====
If you are using a certificate that your browser does not initially trust, you must tell your browser to trust the certificate first before you are able to access the {SMPluginShort}. To do this, go to the Kiali standalone user interface (UI) and tell the browser to accept its certificate.
====

// Module included in the following assemblies:
//
//* *service_mesh/v2x/ossm-kiali-ossmc-plugin.adoc

[id="ossm-kiali-ossmc-plugin-user-guide_{context}"]
= About the OpenShift Service Mesh Console plugin
//In the title include nouns or noun phrases that are used in the body text.
//Do not start the title of concept modules with a verb.

The {SMPlugin} is an extension to the OpenShift Container Platform web console that provides visibility into your Service Mesh.

[WARNING]
====
The {SMPluginShort} only supports a single Kiali instance. Whether that Kiali instance is configured to access only a subset of OpenShift projects or has access cluster-wide to all projects does not matter. However, only a single Kiali instance can be accessed.
====

You can install the OSSMC plugin in only one of two ways: using the OpenShift Container Platform web console, or through the CLI.

[NOTE]
====
The {SMPluginShort} is only supported on {SMProductShortName} 2.5 or later. Specifically, the `ServiceMeshControlPlane` version must be set to 2.5 or later.
====

Installing the {SMPluginShort} creates a new category, *Service Mesh*, in the main OpenShift Container Platform web console navigation. Click *Service Mesh* to see:

* *Overview* for a summary of your mesh displayed as cards that represent the namespaces in the mesh
* *Graph* for a full topology view of your mesh represented by nodes and edges, each node representing a component of the mesh and each edge representing traffic flowing through the mesh between components
* *Istio config* for a list of all Istio configuration files in your mesh with a column that provides a quick way to know if the configuration for each resource is valid

Under *Workloads*, the OSSMC plugin adds a *Service Mesh* tab that contains the following subtabs:

* *Overview* subtab provides a summary of the selected workload including a localized topology graph showing the workload with all inbound and outbound edges and nodes
* *Traffic* subtab displays information about all inbound and outbound traffic to the workload.
* *Logs* subtab shows the logs for the workload's containers
+
--
** You can view container logs individually or in a unified fashion, ordered by log time. This is especially helpful to see how the Envoy sidecar proxy logs relate to your workload's application logs.
** You can enable the tracing span integration which then allows you to see which logs correspond to trace spans.
--
+
* *Metrics* subtab shows both inbound and outbound metric graphs in the corresponding subtabs. All the workload metrics can be displayed here, providing you with a detail view of the performance of your workload.
+
--
** You can enable the tracing span integration which allows you to see which spans occurred at the same time as the metrics. Click a span marker in the graph to view the specific spans associated with that timeframe.
--
+
* *Traces* provides a chart showing the trace spans collected over the given timeframe.
+
--
** Click a bubble to drill down into those trace spans; the trace spans can provide you the most low-level detail within your workload application, down to the individual request level. The trace details view gives further details, including heatmaps that provide you with a comparison of one span in relation to other requests and spans in the same timeframe.
** If you hover over a cell in a heatmap, a tooltip gives some details on the cell data.
--
+
* *Envoy* subtab provides information about the Envoy sidecar configuration. This is useful when you need to dig down deep into the sidecar configuration when debugging things such as connectivity issues.

Under *Networking*, the OSSMC plugin adds a *Service Mesh* tab to Services and contains the *Overview*, *Traffic*, *Inbound Metrics*, and *Traces* subtabs that are similar to the same subtabs found in *Workloads*.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-kiali-ossmc-plugin.adoc

[id="ossm-kiali-ossmc-plugin-install-web-console_{context}"]
= Installing OpenShift Service Mesh Console plugin using the OpenShift Container Platform web console

You can install the {SMPlugin} using the OpenShift Container Platform web console.

.Prerequisites

* OpenShift Container Platform is installed.
* {KialiProduct} 1.73 is installed.
* {SMProductName} (OSSM) is installed.
* `ServiceMeshControlPlane` 2.5 or later is installed.

.Procedure

. Navigate to *Installed Operators*.
. Click *{KialiProduct}*.
. Click *Create instance* on the *{SMProductName}* tile.
. Use the *Create OSSMConsole* form to create an instance of the `OSSMConsole` custom resource (CR).
* *Name* and *Version* are required fields.
+
[NOTE]
====
The *Version* field must match the `spec.version` field in your Kiali CR.
====
. Click *Create*.
. Navigate back to the OpenShift Container Platform web console and use the new menu options for visibility into your Service Mesh.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-kiali-ossmc-plugin.adoc

[id="ossm-kiali-ossmc-plugin-install-cli_{context}"]
= Installing OpenShift Service Mesh Console plugin using the CLI

You can install the {SMPlugin} using the CLI, instead of the OpenShift Container Platform web console.

.Prerequisites

* OpenShift Container Platform is installed.
* {KialiProduct} 1.73 is installed.
* {SMProductName} (OSSM) is installed.
* `ServiceMeshControlPlane` (SMCP) 2.5 or later is installed.

.Procedure

. Create a small `OSSMConsole` custom resource (CR) to instruct the operator to install the plugin:
+
[source, yaml]
----
cat <<EOM | oc apply -f -
apiVersion: kiali.io/v1alpha1
kind: OSSMConsole
metadata:
  namespace: openshift-operators
  name: ossmconsole
EOM
----
+
[NOTE]
====
The plugin resources are deployed in the same namespace where the `OSSMConsole` CR is created.
====
+
. Go to the OpenShift Container Platform web console.
. Refresh the browser window to see the new OSSMC plugin menu options.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-kiali-ossmc-plugin.adoc

[id="ossm-kiali-ossmc-plugin-uninstall-web-console_{context}"]
= Uninstalling OpenShift Service Mesh Console plugin using the OpenShift Container Platform web console

You can uninstall the {SMPlugin} by using the OpenShift Container Platform web console.

.Procedure

. Navigate to *Installed Operators* -> *Operator details*.
. Select the *OpenShift Service Mesh Console* tab.
. Click *Delete OSSMConsole* from the options menu.

[NOTE]
====
If you intend to also uninstall the Kiali Operator provided by Red Hat, you must first uninstall the OSSMC plugin and then uninstall the Operator. If you uninstall the Operator before ensuring the `OSSMConsole` CR is deleted then you may have difficulty removing that CR and its namespace. If this occurs then you must manually remove the finalizer on the CR in order to delete it and its namespace. You can do this using: `$ oc patch ossmconsoles <CR name> -n <CR namespace> -p '{"metadata":{"finalizers": []}}' --type=merge`.
====

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-kiali-ossmc-plugin.adoc

[id="ossm-kiali-ossmc-plugin-uninstall-cli_{context}"]
= Uninstalling OpenShift Service Mesh Console plugin using the CLI

You can uninstall the {SMPlugin} by using the {oc-first}.

.Procedure

. Remove the `OSSMC` custom resource (CR) by running the following command:
+
[source,terminal]
----
 oc delete ossmconsoles <custom_resource_name> -n <custom_resource_namespace>
----
+
. Verify all CRs are deleted from all namespaces by running the following command:
+
[source,terminal]
----
for r in $(oc get ossmconsoles --ignore-not-found=true --all-namespaces -o custom-columns=NS:.metadata.namespace,N:.metadata.name --no-headers | sed 's/  */:/g'); do oc delete ossmconsoles -n $(echo $r|cut -d: -f1) $(echo $r|cut -d: -f2); done
----

[role="_additional-resources"]
[id="additional-resources_ossm-kiali-ossmc-plugin"]
== Additional resources
* .spec.kiali.serviceNamespace
