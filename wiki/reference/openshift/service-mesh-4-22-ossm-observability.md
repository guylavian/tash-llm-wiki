---
title: "Metrics, logs, and traces"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-observability
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-observability
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Metrics, logs, and traces

[id="ossm-observability-v1x"]
= Data visualization and observability

You can view your application's topology, health and metrics in the Kiali console. If your service is having issues, the Kiali console offers ways to visualize the data flow through your service. You can view insights about the mesh components at different levels, including abstract applications, services, and workloads. It also provides an interactive graph view of your namespace in real time.

.Before you begin

You can observe the data flow through your application if you have an application installed.

If you don't have your own application installed, you can see how observability works in {SMProductName} by installing the Bookinfo sample application.

// Module included in the following assemblies:
//
//* service_mesh/v1x/ossm-observability.adoc
//* service_mesh/v2x/ossm-observability.adoc

[id="ossm-observability-access-console_{context}"]
= Viewing service mesh data

The Kiali operator works with the telemetry data gathered in {SMProductName} to provide graphs and real-time network diagrams of the applications, services, and workloads in your namespace.

To access the Kiali console you must have {SMProductName} installed and projects configured for the service mesh.

.Procedure

. Use the perspective switcher to switch to the *Administrator* perspective.

. Click *Home* -> *Projects*.

. Click the name of your project. For example, click `bookinfo`.

. In the *Launcher* section, click *Kiali*.

. Log in to the Kiali console with the same user name and password that you use to access the OpenShift Container Platform console.

When you first log in to the Kiali Console, you see the *Overview* page which displays all the namespaces in your service mesh that you have permission to view.

If you are validating the console installation, there might not be any data to display.

This module is included in the following assemblies:
* service_mesh/v1x/ossm-observability.adoc
* service_mesh/v2x/ossm-observability.adoc

[id="ossm-observability-visual_{context}"]
= Viewing service mesh data in the Kiali console

The Kiali Graph offers a powerful visualization of your mesh traffic. The topology combines real-time request traffic with your Istio configuration information to present immediate insight into the behavior of your service mesh, letting you quickly pinpoint issues. Multiple Graph Types let you visualize traffic as a high-level service topology, a low-level workload topology, or as an application-level topology.

There are several graphs to choose from:

* The *App graph* shows an aggregate workload for all applications that are labeled the same.

* The *Service graph* shows a node for each service in your mesh but excludes all applications and workloads from the graph. It provides a high level view and aggregates all traffic for defined services.

* The *Versioned App graph* shows a node for each version of an application. All versions of an application are grouped together.

* The *Workload graph* shows a node for each workload in your service mesh. This graph does not require you to use the application and version labels. If your application does not use version labels, use this the graph.

Graph nodes are decorated with a variety of information, pointing out various route routing options like virtual services and service entries, as well as special configuration like fault-injection and circuit breakers. It can identify mTLS issues, latency issues, error traffic and more. The Graph is highly configurable, can show traffic animation, and has powerful Find and Hide abilities.

Click the *Legend* button to view information about the shapes, colors, arrows, and badges displayed in the graph.

To view a summary of metrics, select any node or edge in the graph to display its metric details in the summary details panel.

[id="ossm-observability-topology_{context}"]
== Changing graph layouts in Kiali

The layout for the Kiali graph can render differently depending on your application architecture and the data to display. For example, the number of graph nodes and their interactions can determine how the Kiali graph is rendered. Because it is not possible to create a single layout that renders nicely for every situation, Kiali offers a choice of several different layouts.

.Prerequisites

*  If you do not have your own application installed, install the Bookinfo sample application.  Then generate traffic for the Bookinfo application by entering the following command several times.
+
[source,terminal]
----
$ curl "http://$GATEWAY_URL/productpage"
----
+
This command simulates a user visiting the `productpage` microservice of the application.

.Procedure

. Launch the Kiali console.

. Click *Log In With OpenShift*.

. In Kiali console, click *Graph* to view a namespace graph.

. From the *Namespace* menu, select your application namespace, for example, `bookinfo`.

. To choose a different graph layout, do either or both of the following:

* Select different graph data groupings from the menu at the top of the graph.

** App graph
** Service graph
** Versioned App graph (default)
** Workload graph

* Select a different graph layout from the Legend at the bottom of the graph.
** Layout default dagre
** Layout 1 cose-bilkent
** Layout 2 cola
