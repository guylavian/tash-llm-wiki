---
title: "Working with projects"
type: reference
domain: openshift
slug: applications-4-22-working-with-projects
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/working-with-projects
version: 4.22
family: applications
documentKind: "Documentation"
---

# Working with projects

[id="working-with-projects"]
= Working with projects

A _project_ allows a community of users to organize and manage their content in
isolation from other communities.

[NOTE]
====
Projects starting with `openshift-` and `kube-` are
default projects.
default projects.
These projects host cluster components that run as pods and other infrastructure components. As such, OpenShift Container Platform does not allow you to create projects starting with `openshift-` or `kube-` using the `oc new-project` command.
Cluster administrators can create these projects using the `oc adm new-project` command.
For OpenShift Container Platform clusters that use the Customer Cloud Subscription (CCS) model, users with `cluster-admin` privileges can create these projects using the `oc adm new-project` command.
====

[NOTE]
====
In OpenShift Container Platform clusters that use the Customer Cloud Subscription (CCS) model, you cannot assign an SCC to pods created in one of the default namespaces: `default`, `kube-system`, `kube-public`, `openshift-node`, `openshift-infra`, and `openshift`. You cannot use these namespaces for running pods or services. You cannot create any SCCs for OpenShift Container Platform clusters that use a Red Hat cloud account, because SCC resource creation requires `cluster-admin` privileges.
====

[id="working-with-projects-create-project"]
== Creating a project

You can use the OpenShift Container Platform web console or the {oc-first} to create a project in your cluster.

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="creating-a-project-using-the-web-console_{context}"]
= Creating a project by using the web console

You can use the OpenShift Container Platform web console to create a project in your cluster.

[NOTE]
====
Projects starting with `openshift-` and `kube-` are considered critical by OpenShift Container Platform. As such, OpenShift Container Platform does not allow you to create projects starting with `openshift-` using the web console.
====

.Prerequisites

* Ensure that you have the appropriate roles and permissions to create projects, applications, and other workloads in OpenShift Container Platform.

.Procedure

** If you are using the *Administrator* perspective:
.. Navigate to *Home* -> *Projects*.
.. Click *Create Project*:
... In the *Create Project* dialog box, enter a unique name, such as `myproject`, in the *Name* field.
... Optional: Add the *Display name* and *Description* details for the project.
... Click *Create*.
+
The dashboard for your project is displayed.

.. Optional: Select the *Details* tab to view the project details.
.. Optional: If you have adequate permissions for a project, you can use the *Project Access* tab to provide or revoke admin, edit, and view privileges for the project.

** If you are using the *Developer* perspective:
.. Click the *Project* menu and select *Create Project*:
+
.Create project
image::odc_create_project.png[]

... In the *Create Project* dialog box, enter a unique name, such as `myproject`, in the *Name* field.
... Optional: Add the *Display name* and *Description* details for the project.
... Click *Create*.
.. Optional: Use the left navigation panel to navigate to the *Project* view and see the dashboard for your project.
.. Optional: In the project dashboard, select the *Details* tab to view the project details.
.. Optional: If you have adequate permissions for a project, you can use the *Project Access* tab of the project dashboard to provide or revoke admin, edit, and view privileges for the project.

// include modules/odc-creating-projects-using-developer-perspective.adoc[leveloffset=+2]

.Additional resources

* Customizing the available cluster roles using the web console

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="creating-a-project-using-the-CLI_{context}"]
= Creating a project by using the CLI

If allowed by your cluster administrator, you can create a new project.

[NOTE]
====
Projects starting with `openshift-` and `kube-` are considered critical by OpenShift Container Platform. As such, OpenShift Container Platform does not allow you to create Projects starting with `openshift-` or `kube-` using the `oc new-project` command.
Cluster administrators can create these projects using the `oc adm new-project` command.
For OpenShift Container Platform clusters that use the Customer Cloud Subscription (CCS) model, users with `cluster-admin` privileges can create these projects using the `oc adm new-project` command.
====

.Procedure

* Run:
+
[source,terminal]
----
$ oc new-project <project_name> \
    --description="<description>" --display-name="<display_name>"
----
+
For example:
+
[source,terminal]
----
$ oc new-project hello-openshift \
    --description="This is an example project" \
    --display-name="Hello OpenShift"
----

[NOTE]
====
The number of projects you are allowed to create
might be limited by the system administrator.
is limited.
After your limit is reached, you might have to delete an existing project in
order to create a new one.
====

[id="working-with-projects-viewing-project"]
== Viewing a project

You can use the OpenShift Container Platform web console or the {oc-first} to view a project in your cluster.

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="viewing-a-project-using-the-web-console_{context}"]
= Viewing a project by using the web console

You can view the projects that you have access to by using the OpenShift Container Platform web console.

.Procedure

** If you are logged in as an administrator:
.. Navigate to *Home* -> *Projects* in the navigation menu.
.. Select a project to view. The *Overview* tab includes a dashboard for your project.
.. Select the *Details* tab to view the project details.
.. Select the *YAML* tab to view and update the YAML configuration for the project resource.
.. Select the *Workloads* tab to see workloads in the project.
.. Select the *RoleBindings* tab to view and create role bindings for your project.

** If you are logged in as a developer:
.. Navigate to the *Project* page in the navigation menu.
.. Select *All Projects* from the *Project* drop-down menu at the top of the screen to list all of the projects in your cluster.
.. Select a project to view.
.. Select the *Details* tab to view the project details.
.. If you have adequate permissions for a project, select the **Project access** tab view and update the privileges for the project.

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="viewing-a-project-using-the-CLI_{context}"]
= Viewing a project using the CLI

When viewing projects, you are restricted to seeing only the projects you have
access to view based on the authorization policy.

.Procedure

. To view a list of projects, run:
+
[source,terminal]
----
$ oc get projects
----

. You can change from the current project to a different project for CLI
operations. The specified project is then used in all subsequent operations that
manipulate project-scoped content:
+
[source,terminal]
----
$ oc project <project_name>
----

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="odc-providing-project-permissions-using-developer-perspective_{context}"]
= Providing access permissions to your project using the Developer perspective

You can use the *Project* view in the *Developer* perspective to grant or revoke access permissions to your project.

.Prerequisites

* You have created a project.

.Procedure
To add users to your project and provide *Admin*, *Edit*, or *View* access to them:

. In the *Developer* perspective, navigate to the *Project* page.
. Select your project from the *Project* menu.
. Select the *Project Access* tab.
. Click *Add access* to add a new row of permissions to the default ones.
+
.Project permissions
image::odc_project_permissions.png[]
. Enter the user name, click the *Select a role* drop-down list, and select an appropriate role.
. Click *Save* to add the new permissions.

You can also use:

* The *Select a role* drop-down list, to modify the access permissions of an existing user.
* The *Remove Access* icon, to completely remove the access permissions of an existing user to the project.

[NOTE]
====
Advanced role-based access control is managed in the *Roles* and *Roles Binding* views in the *Administrator* perspective.
====

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="odc-customizing-available-cluster-roles-using-the-web-console_{context}"]
= Customizing the available cluster roles using the web console

In the *Developer* perspective of the web console, the *Project* -> *Project access* page enables a project administrator to grant roles to users in a project. By default, the available cluster roles that can be granted to users in a project are admin, edit, and view.

As a cluster administrator, you can define which cluster roles are available in the *Project access* page for all projects cluster-wide. You can specify the available roles by customizing the `spec.customization.projectAccess.availableClusterRoles` object in the `Console` configuration resource.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. In the *Administrator* perspective, navigate to *Administration* -> *Cluster settings*.
. Click the *Configuration* tab.
. From the *Configuration resource* list, select *Console `operator.openshift.io`*.
. Navigate to the *YAML* tab to view and edit the YAML code.
. In the YAML code under `spec`, customize the list of available cluster roles for project access. The following example specifies the default `admin`, `edit`, and `view` roles:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
# ...
spec:
  customization:
    projectAccess:
      availableClusterRoles:
      - admin
      - edit
      - view
----
+
. Click *Save* to save the changes to the `Console` configuration resource.

.Verification

. In the *Developer* perspective, navigate to the *Project* page.
. Select a project from the *Project* menu.
. Select the *Project access* tab.
. Click the menu in the *Role* column and verify that the available roles match the configuration that you applied to the `Console` resource configuration.

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="adding-to-a-project_{context}"]
= Adding to a project

You can add items to your project by using the *+Add* page.

.Prerequisites

* You have created a project.

.Procedure

. Navigate to the *+Add* page.

. Select your project from the *Project* menu.

. Click on an item on the *+Add* page and then follow the workflow.

[NOTE]
====
You can also use the search feature in the *+Add* page to find additional items to add to your project. Click *+* under *Add* at the top of the page and type the name of a component in the search field.
====

[id="working-with-projects-viewing-project-status"]
== Checking the project status

You can use the OpenShift Container Platform web console or the {oc-first} to view the status of your project.

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="checking-project-status-using-the-web-console_{context}"]
= Checking project status by using the web console

You can review the status of your project by using the web console.

.Prerequisites

* You have created a project.

.Procedure

. Navigate to *Home* -> *Projects*.
. Select a project from the list.
. Review the project status in the *Overview* page.

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="checking-project-status-using-the-CLI_{context}"]
= Checking project status by using the CLI

You can review the status of your project by using the {oc-first}.

.Prerequisites

* You have installed the {oc-first}.
* You have created a project.

.Procedure

. Switch to your project:
+
[source,terminal]
----
$ oc project <project_name> <1>
----
<1> Replace `<project_name>` with the name of your project.

. Obtain a high-level overview of the project:
+
[source,terminal]
----
$ oc status
----

// The following text comes from deleting-a-project-using-the-CLI.adoc
[id="working-with-projects-deleting-project"]
== Deleting a project

You can use the OpenShift Container Platform web console or the {oc-first} to delete a project.

When you delete a project, the server updates the project status to *Terminating* from *Active*. Then, the server clears all content from a project that is in the *Terminating* state before finally removing the project. While a project is in *Terminating* status, you cannot add new content to the project. Projects can be deleted from the CLI or the web console.

// Module included in the following assemblies:
//
// * applications/projects/working-with-projects.adoc

[id="deleting-a-project-using-the-web-console_{context}"]
= Deleting a project by using the web console

You can delete a project by using the web console.

.Prerequisites

* You have created a project.
* You have the required permissions to delete the project.

.Procedure

** If you are using the *Administrator* perspective:
.. Navigate to *Home* -> *Projects*.
.. Select a project from the list.
.. Click the *Actions* drop-down menu for the project and select *Delete Project*.
+
[NOTE]
====
The *Delete Project* option is not available if you do not have the required permissions to delete the project.
====

. In the *Delete Project?* pane, confirm the deletion by entering the name of your project.
. Click *Delete*.

** If you are using the *Developer* perspective:
.. Navigate to the *Project* page.
.. Select the project that you want to delete from the *Project* menu.
.. Click the *Actions* drop-down menu for the project and select *Delete Project*.
+
[NOTE]
====
If you do not have the required permissions to delete the project, the *Delete Project* option is not available.
====

. In the *Delete Project?* pane, confirm the deletion by entering the name of your project.
. Click *Delete*.

// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="deleting-a-project-using-the-CLI_{context}"]
= Deleting a project by using the CLI

// Moved intro paragraph to working-with-projects.adoc

You can delete a project by using the {oc-first}.

.Prerequisites

* You have installed the {oc-first}.
* You have created a project.
* You have the required permissions to delete the project.

.Procedure

. Delete your project:
+
[source,terminal]
----
$ oc delete project <project_name> <1>
----
<1> Replace `<project_name>` with the name of the project that you want to delete.
