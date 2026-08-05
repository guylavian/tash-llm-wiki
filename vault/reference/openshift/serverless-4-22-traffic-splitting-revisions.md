---
title: "Splitting traffic between revisions"
type: reference
domain: openshift
slug: serverless-4-22-traffic-splitting-revisions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/traffic-splitting-revisions
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Splitting traffic between revisions

[id="traffic-splitting-revisions"]
= Splitting traffic between revisions

After you create a serverless application, the application is displayed in the *Topology* view of the *Developer* perspective in the OpenShift Container Platform web console. The application revision is represented by the node, and the Knative service is indicated by a quadrilateral around the node.

Any new change in the code or the service configuration creates a new revision, which is a snapshot of the code at a given time. For a service, you can manage the traffic between the revisions of the service by splitting and routing it to the different revisions as required.

// ODC
// Module included in the following assemblies:
//
// * serverless/develop/serverless-traffic-management.adoc

[id="odc-splitting-traffic-between-revisions-using-developer-perspective_{context}"]
= Managing traffic between revisions by using the OpenShift Container Platform web console

.Prerequisites

* The {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have logged in to the OpenShift Container Platform web console.

.Procedure

To split traffic between multiple revisions of an application in the *Topology* view:

. Click the Knative service to see its overview in the side panel.
. Click the *Resources* tab, to see a list of *Revisions* and *Routes* for the service.
+
.Serverless application
image::odc-serverless-app.png[]

. Click the service, indicated by the *S* icon at the top of the side panel, to see an overview of the service details.
. Click the *YAML* tab and modify the service configuration in the YAML editor, and click *Save*. For example, change the `timeoutseconds` from 300 to 301 . This change in the configuration triggers a new revision. In the *Topology* view, the latest revision is displayed and the *Resources* tab for the service now displays the two revisions.
. In the *Resources* tab, click btn:[Set Traffic Distribution] to see the traffic distribution dialog box:
.. Add the split traffic percentage portion for the two revisions in the *Splits* field.
.. Add tags to create custom URLs for the two revisions.
.. Click *Save* to see two nodes representing the two revisions in the Topology view.
+
.Serverless application revisions
image::odc-serverless-revisions.png[]
