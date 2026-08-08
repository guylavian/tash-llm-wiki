---
title: "Setting up an Argo CD instance"
type: reference
domain: openshift
slug: cicd-4-22-setting-up-argocd-instance
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/setting-up-argocd-instance
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Setting up an Argo CD instance

[id="setting-up-argocd-instance"]
= Setting up an Argo CD instance

By default, the {gitops-title} installs an instance of Argo CD in the `openshift-gitops` namespace with additional permissions for managing certain cluster-scoped resources. To manage cluster configurations or deploy applications, you can install and deploy a new Argo CD instance. By default, any new instance has permissions to manage resources only in the namespace where it is deployed.

// Module included in the following assemblies:
//
// * cicd/gitops/setting-up-argocd-instance.adoc

[id="gitops-argo-cd-installation_{context}"]
= Installing Argo CD

To manage cluster configurations or deploy applications, you can install and deploy a new Argo CD instance.

.Procedure
. Log in to the OpenShift Container Platform web console.

. Click *Ecosystem* -> *Installed Operators*.

. Create or select the project where you want to install the Argo CD instance from the *Project* drop-down menu.

. Select *OpenShift GitOps Operator* from the installed operators and select the *Argo CD* tab.

. Click *Create* to configure the parameters:

.. Enter the **Name** of the instance. By default, the *Name* is set to *argocd*.

.. Create an external OS Route to access Argo CD server. Click *Server* -> *Route* and check *Enabled*.

. To open the Argo CD web UI, click the route by navigating to **Networking -> Routes -> <instance name>-server** in the project where the Argo CD instance is installed.

// Module included in the following assemblies:
//
// * cicd/gitops/setting-up-argocd-instance.adoc

[id="gitops-enable-replicas-for-argo-cd-server_{context}"]
= Enabling replicas for Argo CD server and repo server

Argo CD-server and Argo CD-repo-server workloads are stateless. To better distribute your workloads among pods, you can increase the number of Argo CD-server and  Argo CD-repo-server replicas. However, if a horizontal autoscaler is enabled on the Argo CD-server, it overrides the number of replicas you set.

.Procedure

* Set the `replicas` parameters for the `repo` and `server` spec to the number of replicas you want to run:
+
.Example Argo CD custom resource

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: repo
spec:
  repo:
    replicas: <number_of_replicas>
  server:
    replicas: <number_of_replicas>
    route:
      enabled: true
      path: /
      tls:
        insecureEdgeTerminationPolicy: Redirect
        termination: passthrough
      wildcardPolicy: None
----

// Module included in the following assemblies:
//
// * cicd/gitops/setting-up-argocd-instance.adoc

[id="gitops-deploy-resources-different-namespaces_{context}"]
= Deploying resources to a different namespace

To allow Argo CD to manage resources in other namespaces apart from where it is installed, configure the target namespace with a `argocd.argoproj.io/managed-by` label.

.Procedure

* Configure the namespace:
+
[source,terminal]
----
$ oc label namespace <namespace> \
argocd.argoproj.io/managed-by=<namespace> <1>
----
<1> The namespace where Argo CD is installed.

// Module included in the following assembly:
//
// * cicd/gitops/setting-up-argocd-instance.adoc

[id="gitops-customize-argo-cd-consolelink_{context}"]
= Customizing the Argo CD console link

In a multi-tenant cluster, users might have to deal with multiple instances of Argo CD. For example, after installing an Argo CD instance in your namespace, you might find a different Argo CD instance attached to the Argo CD console link, instead of your own Argo CD instance, in the Console Application Launcher.

You can customize the Argo CD console link by setting the `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` environment variable:

* When you set `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` to `true`, the Argo CD console link is permanently deleted.
* When you set `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` to `false` or use the default value, the Argo CD console link is temporarily deleted and visible again when the Argo CD route is reconciled.

.Prerequisites
* You have logged in to the OpenShift Container Platform cluster as an administrator.
* You have installed the {gitops-title} Operator.

.Procedure

. In the *Administrator* perspective, navigate to *Administration* -> *CustomResourceDefinitions*.
. Find the *Subscription* CRD and click to open it.
. Select the *Instances* tab and click the *openshift-gitops-operator* subscription.
. Select the *YAML* tab and make your customization:
** To enable or disable the Argo CD console link, edit the value of `DISABLE_DEFAULT_ARGOCD_CONSOLELINK` as needed:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-gitops-operator
spec:
  config:
    env:
    - name: DISABLE_DEFAULT_ARGOCD_CONSOLELINK
      value: 'true'
----
