---
title: "Deploying a Spring Boot application with Argo CD"
type: reference
domain: openshift
slug: cicd-4-22-deploying-a-spring-boot-application-with-argo-cd
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/deploying-a-spring-boot-application-with-argo-cd
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Deploying a Spring Boot application with Argo CD

[id="deploying-a-spring-boot-application-with-argo-cd"]
= Deploying a Spring Boot application with Argo CD

With Argo CD, you can deploy your applications to the OpenShift cluster either by using the Argo CD dashboard or by using the `oc` tool.

.Prerequisites

* Red Hat OpenShift GitOps is installed in your cluster.
* Logged into Argo CD instance.

// Module included in the following assemblies:
//
// * configuring-an-openshift-cluster-with-argo-cd.adoc
// * depoying-an-application-with-argo-cd.adoc

[id="creating-an-application-by-using-the-argo-cd-dashboard_{context}"]
= Creating an application by using the Argo CD dashboard

Argo CD provides a dashboard which allows you to create applications.

This sample workflow walks you through the process of configuring Argo CD to recursively sync the content of the `cluster` directory to the `cluster-configs` application. The directory defines the OpenShift Container Platform web console cluster configurations that add a link to the *Red Hat Developer Blog - Kubernetes* under the {rh-app-icon} menu in the web console, and defines a namespace `spring-petclinic` on the cluster.

.Procedure

. In the Argo CD dashboard, click *NEW APP* to add a new Argo CD application.

. For this workflow, create a *cluster-configs* application with the following configurations:
+
Application Name:: `cluster-configs`
Project:: `default`
Sync Policy:: `Manual`
Repository URL:: `https://github.com/redhat-developer/openshift-gitops-getting-started`
Revision:: `HEAD`
Path:: `cluster`
Destination:: `https://kubernetes.default.svc`
Namespace:: `spring-petclinic`
Directory Recurse:: `checked`

. For this workflow, create a *spring-petclinic* application with the following configurations:
+
Application Name:: `spring-petclinic`
Project:: `default`
Sync Policy:: `Automatic`
Repository URL:: `https://github.com/redhat-developer/openshift-gitops-getting-started`
Revision:: `HEAD`
Path:: `app`
Destination:: `https://kubernetes.default.svc`
Namespace:: `spring-petclinic`

. Click *CREATE* to create your application.

. Open the *Administrator* perspective of the web console and navigate to *Administration* -> *Namespaces* in the menu on the left.

. Search for and select the namespace, then enter `argocd.argoproj.io/managed-by=openshift-gitops` in the *Label* field so that the Argo CD instance in the `openshift-gitops` namespace can manage your namespace.

// Module included in the following assemblies:
//
// * configuring-an-openshift-cluster-with-argo-cd.adoc
// * depoying-an-application-with-argo-cd.adoc

[id="creating-an-application-by-using-the-oc-tool_{context}"]
= Creating an application by using the `oc` tool

You can create Argo CD applications in your terminal by using the `oc` tool.

.Procedure

. Download the sample application:
+
[source,terminal]
----
$ git clone git@github.com:redhat-developer/openshift-gitops-getting-started.git
----

. Create the application:
+
[source,terminal]
----
$ oc create -f openshift-gitops-getting-started/argo/app.yaml
----

+
[source,terminal]
----
$ oc create -f openshift-gitops-getting-started/argo/app.yaml
----

. Run the `oc get` command to review the created application:
+
[source,terminal]
----
$ oc get application -n openshift-gitops
----

. Add a label to the namespace your application is deployed in so that the Argo CD instance in the `openshift-gitops` namespace can manage it:

+
[source,terminal]
----
$ oc label namespace spring-petclinic argocd.argoproj.io/managed-by=openshift-gitops
----
+
[source,terminal]
----
$ oc label namespace spring-petclinic argocd.argoproj.io/managed-by=openshift-gitops
----

// Module is included in the following assemblies:
//
// * deploying-a-spring-boot-application-with-argo-cd

[id="verifying-argo-cd-self-healing-behavior_{context}"]
= Verifying Argo CD self-healing behavior

Argo CD constantly monitors the state of deployed applications, detects differences between the specified manifests in Git and live changes in the cluster, and then automatically corrects them. This behavior is referred to as self-healing.

You can test and observe the self-healing behavior in Argo CD.

.Prerequisites

* The sample `app-spring-petclinic` application is deployed and configured.

.Procedure

. In the Argo CD dashboard, verify that your application has the `Synced` status.

. Click the `app-spring-petclinic` tile in the Argo CD dashboard to view the application resources that are deployed to the cluster.

. In the OpenShift Container Platform web console, navigate to the *Developer* perspective.

. Modify the Spring PetClinic deployment and commit the changes to the `app/` directory of the Git repository. Argo CD will automatically deploy the changes to the cluster.

.. Fork the OpenShift GitOps getting started repository.

.. In the `deployment.yaml` file, change the `failureThreshold` value to `5`.

.. In the deployment cluster, run the following command to verify the changed value of the `failureThreshold` field:
+
[source,terminal]
----
$ oc edit deployment spring-petclinic -n spring-petclinic
----

. Test the self-healing behavior by modifying the deployment on the cluster and scaling it up to two pods while watching the application in the OpenShift Container Platform web console.
+
.. Run the following command to modify the deployment:
+
[source,terminal]
----
$ oc scale deployment spring-petclinic --replicas 2  -n spring-petclinic
----
.. In the OpenShift Container Platform web console, notice that the deployment scales up to two pods and immediately scales down again to one pod. Argo CD detected a difference from the Git repository and auto-healed the application on the OpenShift Container Platform cluster.

. In the Argo CD dashboard, click the *app-spring-petclinic* tile → *APP DETAILS* → *EVENTS*. The *EVENTS* tab displays the following events: Argo CD detecting out of sync deployment resources on the cluster and then resyncing the Git repository to correct it.
