---
title: "Installing {gitops-title}"
type: reference
domain: openshift
slug: cicd-4-22-installing-openshift-gitops
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/installing-openshift-gitops
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Installing {gitops-title}

[id="getting-started-with-openshift-gitops"]
= Installing {gitops-title}

[role="_abstract"]
{gitops-title} uses Argo CD to manage specific cluster-scoped resources, including cluster Operators, optional Operator Lifecycle Manager (OLM) Operators, and user management.

[discrete]
== Prerequisites

* You have access to the OpenShift Container Platform web console.
* You are logged in as a user with the `cluster-admin` role.
* You are logged in to the OpenShift Container Platform cluster as an administrator.
* Your cluster has the Marketplace capability enabled or the Red Hat Operator catalog source configured manually.

[WARNING]
====
If you have already installed the Community version of the Argo CD Operator, remove the Argo CD Community Operator before you install the {gitops-title} Operator.
====

This guide explains how to install the {gitops-title} Operator to an OpenShift Container Platform cluster and log in to the Argo CD instance.

[IMPORTANT]
====
The `latest` channel enables installation of the most recent stable version of the {gitops-title} Operator. Currently, it is the default channel for installing the {gitops-title} Operator.

To install a specific version of the {gitops-title} Operator, cluster administrators can use the corresponding `gitops-<version>` channel. For example, to install the {gitops-title} Operator version 1.8.x, you can use the `gitops-1.8` channel.
====

// Module is included in the following assemblies:
//
// * /cicd/gitops/installing-openshift-gitops.adoc

[id="logging-in-to-the-argo-cd-instance-by-using-the-argo-cd-admin-account_{context}"]
= Logging in to the Argo CD instance by using the Argo CD admin account

[role="_abstract"]
{gitops-title} Operator automatically creates a ready-to-use Argo CD instance that is available in the `openshift-gitops` namespace.

.Prerequisites

* You have installed the {gitops-title} Operator in your cluster.

.Procedure

. In the *Administrator* perspective of the web console, navigate to *Ecosystem* -> *Installed Operators* to verify that the {gitops-title} Operator is installed.
. Navigate to the {rh-app-icon} menu -> *OpenShift GitOps* -> *Cluster Argo CD*. The login page of the Argo CD UI is displayed in a new window.
. Optional: To log in with your OpenShift Container Platform credentials, ensure you are a user of the `cluster-admins` group and then select the `LOG IN VIA OPENSHIFT` option in the Argo CD user interface.
+
[NOTE]
====
To be a user of the `cluster-admins` group, use the `oc adm groups new cluster-admins <user>` command, where `<user>` is the default cluster role that you can bind to users and groups cluster-wide or locally.
====
. To log in with your username and password, obtain the password for the Argo CD instance:
.. In the left panel of the console, use the perspective switcher to switch to the *Developer* perspective.
.. Use the *Project* drop-down list and select the `openshift-gitops` project.
.. Use the left navigation panel to navigate to the *Secrets* page.
.. Select the *openshift-gitops-cluster* instance to display the password.
.. Copy the password.
. Use this password and `admin` as the username to log in to the Argo CD UI in the new window.

[NOTE]
====
You cannot create two Argo CD CRs in the same namespace.
====
