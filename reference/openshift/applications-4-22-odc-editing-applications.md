---
title: "Editing applications"
type: reference
domain: openshift
slug: applications-4-22-odc-editing-applications
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/odc-editing-applications
version: 4.22
family: applications
documentKind: "Documentation"
---

# Editing applications

[id="odc-editing-applications"]
= Editing applications

You can edit the configuration and the source code of the application you create using the *Topology* view.

== Prerequisites
// When the Authentication book is added to ROSA/OSD, check if this link is valid.
* You have the appropriate roles and permissions in a project to create and modify applications in OpenShift Container Platform.
* You have created and deployed an application on OpenShift Container Platform using the *Developer* perspective.
* You have logged in to the web console and have switched to the *Developer* perspective.
* You have logged in to the web console and have switched to the *Developer* perspective.

[id="odc-editing-source-code-using-developer-perspective_{context}"]
= Editing the source code of an application using the Developer perspective

You can use the *Topology* view in the *Developer* perspective to edit the source code of your application.

.Procedure

* In the *Topology* view, click the *Edit Source code* icon, displayed at the bottom-right of the deployed application, to access your source code and modify it.
+
[NOTE]
====
This feature is available only when you create applications using the *From Git*, *From Catalog*, and the *From Dockerfile* options.
====
+
If the *Eclipse Che* Operator is installed in your cluster, a Che workspace (image:odc_che_workspace.png[title="Che Workspace"]) is created and you are directed to the workspace to edit your source code. If it is not installed, you will be directed to the Git repository (image:odc_git_repository.png[title="Git Repository"]) your source code is hosted in.

[id="odc-editing-application-configuration-using-developer-perspective_{context}"]
= Editing the application configuration using the Developer perspective

You can use the *Topology* view in the *Developer* perspective to edit the configuration of your application.

[NOTE]
====
Currently, only configurations of applications created by using the *From Git*, *Container Image*, *From Catalog*, or *From Dockerfile* options in the *Add* workflow of the *Developer* perspective can be edited. Configurations of applications created by using the CLI or the *YAML* option from the *Add* workflow cannot be edited.
====

.Prerequisites
Ensure that you have created an application using  the *From Git*, *Container Image*, *From Catalog*, or *From Dockerfile* options in the *Add* workflow.

.Procedure

. After you have created an application and it is displayed in the *Topology* view, right-click the application to see the edit options available.
+
.Edit application
image::odc_edit_app.png[]
+
. Click *Edit _application-name_* to see the *Add* workflow you used to create the application. The form is pre-populated with the values you had added while creating the application.
. Edit the necessary values for the application.
+
[NOTE]
====
You cannot edit the *Name* field in the *General* section, the CI/CD pipelines, or the *Create a route to the application* field in the *Advanced Options* section.
====
+
. Click *Save* to restart the build and deploy a new image.
+
.Edit and redeploy application
image::odc_edit_redeploy.png[]
