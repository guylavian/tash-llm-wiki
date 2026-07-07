---
title: "Web Console Overview"
type: reference
domain: openshift
slug: web-console-4-22-web-console-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/web_console/web-console-overview
version: 4.22
family: web_console
documentKind: "Documentation"
---

# Web Console Overview

[id="web-console-overview"]
= Web Console Overview

[role="_abstract"]
The OpenShift Container Platform web console provides a graphical user interface to visualize your project data and perform administrative, management, and troubleshooting tasks. The web console runs as pods on the control plane nodes in the openshift-console project. It is managed by a `console-operator` pod.

You can create quick start tutorials for OpenShift Container Platform that provide guided steps within the web console with user tasks. They are helpful for getting oriented with an application, Operator, or other product offering.

// Module included in the following assemblies:
//
// web_console/web-console-overview.adoc

[id="about-administrator-perspective_{context}"]
= Administrator role in the web console

[role="_abstract"]
The cluster administrator role enables you to view the cluster inventory, capacity, general and specific utilization information, and the stream of important events, all of which help you to simplify planning and troubleshooting tasks. Both project administrators and cluster administrators can use all features in the web console.

Cluster administrators can also open an embedded command-line terminal instance with the web terminal Operator in OpenShift Container Platform 4.7 and later.
Cluster administrators can also open an embedded command-line terminal instance with the web terminal Operator.

The *Administrator* perspective provides workflows specific to administrator use cases, such as the ability to:

* Manage workload, storage, networking, and cluster settings.
* Install and manage Operators using the software catalog.
* Add identity providers that allow users to log in and manage user access through roles and role bindings.
* View and manage a variety of advanced settings such as cluster updates, partial cluster updates, cluster Operators, custom resource definitions (CRDs), role bindings, and resource quotas.
* Access and manage monitoring features such as metrics, alerts, and monitoring dashboards.
* View and manage logging, metrics, and high-status information about the cluster.
* Visually interact with applications, components, and services.

// Module included in the following assemblies:
//
// web_console/web-console-overview.adoc

[id="about-developer_web-console_{context}"]
= Developer role in the web console

[role="_abstract"]
The developer role in the web console offers several built-in ways to deploy applications, services, and databases. With the developer role, you can:

* View real-time visualization of rolling and recreating rollouts on the component.
* View the application status, resource utilization, project event streaming, and quota consumption.
* Share your project with others.
* Troubleshoot problems with your applications by running Prometheus Query Language (PromQL) queries on your project and examining the metrics visualized on a plot. The metrics provide information about the state of a cluster and any user-defined workloads that you are monitoring.

Cluster administrators can also open an embedded command-line terminal instance in the web console in OpenShift Container Platform 4.7 and later.
Cluster developers can also open an embedded command-line terminal instance in the web console.

Developers have access to workflows specific to their use cases, such as the ability to:

* Create and deploy applications on OpenShift Container Platform by importing existing codebases, images, and container files.
* Visually interact with applications, components, and services associated with them within a project and monitor their deployment and build status.
* Group components within an application and connect the components within and across applications.
* Integrate serverless capabilities (Technology Preview).
* Create workspaces to edit their application code using Eclipse Che.

You can use the *Topology* view to display applications, components, and workloads of your project. If you have no workloads in the project, the *Topology* view will show some links to create or import them. You can also use the *Quick Search* to import components directly.

.Additional resources
* Viewing application composition using the Topology

// Module included in the following assemblies:
//
// web_console/web-console-overview.adoc

[id="enabling-developer-perspective_web-console_{context}"]
= Enabling the *Developer* perspective in the web console

[role="_abstract"]
Starting with OpenShift Container Platform 4.19, the perspectives in the web console have unified. There is no longer a *Developer* perspective by default; however, cluster administrators can enable the *Developer* perspective for developers to use.
Cluster administrators can enable the *Developer* perspective for developers to use.

You can enable the *Developer* perspective with the following steps:

.Prerequisites

* You have access to the web console as a user with `cluster-admin` privileges.

.Procedure

. Navigate to the *Cluster Settings* page by clicking  *Administration* -> *Cluster Settings*.

. Select the *Configuration* tab on the *Cluster Settings* page.

. Type `console` in the search to locate the Console Operator resource and select `operator.openshift.io`.

. On the *Cluster Details* page, click the *Actions* menu and select *Customize*.

. In the *General* tab, locate the *Perspectives* section. You can enable or disable the *Developer* perspective as needed. Changes are automatically applied.

. Optional: You can enable the *Developer* perspective with the CLI by running the following command:
+
[source,terminal]
----
$ oc patch console.operator.openshift.io/cluster --type='merge' -p '{"spec":{"customization":{"perspectives":[{"id":"dev","visibility":{"state":"Enabled"}}]}}}'
----
+
[NOTE]
====
It will take some time for the change to reflect in the web console as the console pod restarts.
====

[role="_additional-resources"]
.Additional resources

* Learn more about Cluster Administrator
* Viewing the applications in your project, verifying their deployment status, and interacting with them in the *Topology* view
* Viewing cluster information
* Configuring the web console
* Customizing the web console
* About the web console
* Using the web terminal
* Creating quick start tutorials
* Disabling the web console
