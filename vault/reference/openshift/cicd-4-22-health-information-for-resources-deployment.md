---
title: "Monitoring health information for application resources and deployments"
type: reference
domain: openshift
slug: cicd-4-22-health-information-for-resources-deployment
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/health-information-for-resources-deployment
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Monitoring health information for application resources and deployments

[id="health-information-for-resources-deployment"]
= Monitoring health information for application resources and deployments

The {gitops-title} *Environments* page in the *Developer* perspective of the OpenShift Container Platform web console shows a list of the successful deployments of the application environments, along with links to the revision for each deployment.

The *Application environments* page in the *Developer* perspective of the OpenShift Container Platform web console displays the health status of the application resources, such as routes, synchronization status, deployment configuration, and deployment history.

The environments pages in the *Developer* perspective of the OpenShift Container Platform web console are decoupled from the {gitops-title} Application Manager command-line interface (CLI), `kam`. You do not have to use `kam` to generate Application Environment manifests for the environments to show up in the *Developer* perspective of the OpenShift Container Platform web console. You can use your own manifests, but the environments must still be represented by namespaces. In addition, specific labels and annotations are still needed.

// Module included in the following assemblies:
//
// * /gitops/health-information-for-resources-deployment.adoc

[id="go-settings-for-environment-labels-and-annotations_{context}"]
= Settings for environment labels and annotations

This section provides reference settings for environment labels and annotations required to display an environment application in the *Environments* page, in the *Developer* perspective of the OpenShift Container Platform web console.

== Environment labels

The environment application manifest must contain `labels.openshift.gitops/environment` and `destination.namespace` fields. You must set identical values for the `<environment_name>` variable and the name of the environment application manifest.

.Specification of the environment application manifest
[source,yaml]
----
spec:
  labels:
    openshift.gitops/environment: <environment_name>
  destination:
    namespace: <environment_name>
...
----

.Example of an environment application manifest
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: dev-env <1>
  namespace: openshift-gitops
spec:
  labels:
    openshift.gitops/environment: dev-env
  destination:
    namespace: dev-env
...
----
<1> The name of the environment application manifest. The value set is the same as the value of the `<environment_name>` variable.

== Environment annotations
The environment namespace manifest must contain the `annotations.app.openshift.io/vcs-uri` and `annotations.app.openshift.io/vcs-ref` fields to specify the version controller code source of the application. You must set identical values for the `<environment_name>` variable and the name of the environment namespace manifest.

.Specification of the environment namespace manifest
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    app.openshift.io/vcs-uri: <application_source_url>
    app.openshift.io/vcs-ref: <branch_reference>
  name: <environment_name> <1>
...
----
<1> The name of the environment namespace manifest. The value set is the same as the value of the `<environment_name>` variable.

.Example of an environment namespace manifest
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    app.openshift.io/vcs-uri: https://example.com/<your_domain>/<your_gitops.git>
    app.openshift.io/vcs-ref: main
  labels:
    argocd.argoproj.io/managed-by: openshift-gitops
  name: dev-env
...
----
[id="health-information-resources_{context}"]
= Checking health information

The {gitops-title} Operator will install the GitOps backend service in the `openshift-gitops` namespace.

.Prerequisites

* The {gitops-title} Operator is installed from the software catalog.
* Ensure that your applications are synchronized by Argo CD.

.Procedure

. Click *Environments* under the *Developer* perspective. The *Environments* page shows the list of applications along with their *Environment status*.

. Hover over the icons under the *Environment status* column to see the synchronization status of all the environments.

. Click the application name from the list to view the details of a specific application.

. In the *Application environments* page, if the *Resources* section under the *Overview* tab displays icons, hover over the icons to get status details.
** A broken heart indicates that resource issues have degraded the application's performance.
** A yellow yield sign indicates that resource issues have delayed data about the application's health.

. To view the deployment history of an application, click the *Deployment History* tab. The page includes details such as the *Last deployment*, *Description* (commit message), *Environment*, *Author*, and *Revision*.
