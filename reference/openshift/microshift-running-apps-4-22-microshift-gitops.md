---
title: "Automating application management with the GitOps controller"
type: reference
domain: openshift
slug: microshift-running-apps-4-22-microshift-gitops
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_running_apps/microshift-gitops
version: 4.22
family: microshift_running_apps
documentKind: "Documentation"
---

# Automating application management with the GitOps controller

[id="microshift-gitops"]
= Automating application management with the GitOps controller

[role="_abstract"]
You can consistently configure and deploy Kubernetes-based infrastructure and applications across node and development lifecycles by using the declarative {gitops-title} engine.

// Module included in the following assemblies:
//
// microshift_running_apps/microshift-gitops.adoc

[id="microshift-gitops-can-do_{context}"]
= What you can do with the GitOps agent

[role="_abstract"]
You can manage application lifecycles and use automated processes to manage application changes with {gitops-title}.

{gitops} with Argo CD for {microshift-short} is a lightweight, optional add-on controller derived from the {gitops} Operator.

The {gitops} agent for {microshift-short} uses the command-line interface (CLI) of Argo CD to interact with the {gitops} controller. The controller acts as the declarative {gitops} engine. By using the {gitops} with Argo CD agent for {microshift-short}, you can use the following principles:

* Implement application lifecycle management:

** Create and manage your node and application configuration files using the core principles of developing and maintaining software in a Git repository.
** You can update the single repository and GitOps automates the deployment of new applications or updates to existing ones.
** For example, if you have 1,000 edge devices, each using {microshift-short} and a local GitOps agent, you can easily add or update an application on all 1,000 devices with just one change in your central Git repository.

* The Git repository contains a declarative description of the infrastructure you need in your specified environment and contains an automated process to make your environment match the described state.

* You can also use the Git repository as an audit trail of changes so that you can create processes based on Git flows such as review and approval for merging pull requests that implement configuration changes.

// Module included in the following assemblies:
//
// microshift_running_apps/microshift-gitops.adoc

[id="microshift-gitops-limitations_{context}"]
= Limitations of using the {gitops} agent with {microshift-short}

[role="_abstract"]
Using {gitops-title} with Argo CD for {microshift-short} is different from using the entire {gitops} Operator in the following ways:

* The `gitops-operator` component is not used with {microshift-short}.
* To maintain the small resource use of {microshift-short} use the Argo CD CLI. The Argo CD web console is not available.
* Because {microshift-short} is single-node, there is no multi-node support. Each instance of {microshift-short} is paired with a local {gitops} agent.
* The `oc adm must-gather` command is not available in {microshift-short}.

// Module included in the following assemblies:
//
// microshift/microshift-install-optional-rpms.adoc
// microshift_running_apps/microshift.gitops.adoc

[id="microshift-installing-rpms-for-gitops_{context}"]
= Installing the {gitops} Argo CD manifests from an RPM package

[role="_abstract"]
You can use a lightweight version of {gitops-title} with {microshift-short} to help manage your applications by installing the `microshift-gitops` RPM package.

The `microshift-gitops` RPM package includes the necessary manifests to run core Argo CD.

[IMPORTANT]
====
The Argo CD web console is not available on {microshift-short}. This process installs basic {gitops} functions.
====

.Prerequisites

* You installed {microshift-short} version 4.16 or later.
* You configured 250MB RAM of additional storage.

.Procedure

. Enable the {gitops} repository with the subscription manager by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ sudo subscription-manager repos --enable=gitops-{gitops-ver}-for-{rhel-major}-$(uname -m)-rpms
----

. Install the {microshift-short} {gitops} package by running the following command:
+
[source,terminal]
----
$ sudo dnf install -y microshift-gitops
----

. To deploy Argo CD pods, restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

.Verification

* You can verify that your pods are running properly by entering the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-gitops
----
+
.Example output
[source,terminal]
----
NAME                                  READY   STATUS    RESTARTS   AGE
argocd-application-controller-0       1/1     Running   0          4m11s
argocd-redis-56844446bc-dzmhf         1/1     Running   0          4m12s
argocd-repo-server-57b4f896cf-7qk8l   1/1     Running   0          4m12s
----

// Module included in the following assemblies:
//
// microshift_running_apps/microshift-gitops.adoc

[id="microshift-gitops-adding-apps_{context}"]
= Creating GitOps applications on {microshift-short}

[role="_abstract"]
You can create a custom configuration by using a YAML file to deploy and manage applications in your {microshift-short} service after you install the {gitops-title} Argo CD manifests from an RPM package.

.Prerequisites

* You installed the `microshift-gitops` packages.
* The Argo CD pods are running in the `openshift-gitops` namespace.

.Procedure

. Create a YAML file and add your customized configurations for the application:
+
.Example YAML for a `spring-petclinic` application
[source,yaml]
----
kind: AppProject
apiVersion: argoproj.io/v1alpha1
metadata:
  name: default
  namespace: openshift-gitops
spec:
  clusterResourceWhitelist:
  - group: '*'
    kind: '*'
  destinations:
  - namespace: '*'
    server: '*'
  sourceRepos:
  - '*'
---
kind: Application
apiVersion: argoproj.io/v1alpha1
metadata:
  name: spring-petclinic
  namespace: openshift-gitops
spec:
  destination:
    namespace: spring-petclinic
    server: https://kubernetes.default.svc
  project: default
  source:
    directory:
      recurse: true
    path: app
    repoURL: https://github.com/siamaksade/openshift-gitops-getting-started
  syncPolicy:
    automated: {}
    syncOptions:
    - CreateNamespace=true
    - ServerSideApply=true
----

. To deploy the applications defined in the YAML file, run the following command:
+
[source,terminal,subs="+quotes"]
----
$ oc apply -f _<my_app.yaml>_
----
+
Replace `_<my_app.yaml>_` with the name of your application YAML.

.Verification

* To verify your application is deployed and synced, run the following command:
+
[source,terminal]
----
$ oc get applications -A
----
+
Wait a few minutes for the application to show a `Healthy` status.
+
.Example output
[source,terminal]
----
NAMESPACE          NAME               SYNC STATUS   HEALTH STATUS
openshift-gitops   spring-petclinic   Synced        Healthy
----

// Module included in the following assemblies:
//
// microshift_running_apps/microshift-gitops.adoc

[id="microshift-gitops-debug_{context}"]
= Debugging {gitops} with oc adm inspect

[role="_abstract"]
If you have problems with your Argo CD for {microshift-short} {gitops-title} controller, you can use the {oc-first} tool to inspect it for errors.

.Prerequisites

* The `oc` command-line tool is installed.

.Procedure

* Run the `oc adm inspect` command when in the {gitops} namespace:
+
[source,terminal]
----
$ oc adm inspect ns/openshift-gitops
----
+
.Example output
[source,terminal]
----
Gathering data for ns/openshift-gitops...
W0501 20:34:35.978508 57625 util.go:118] the server doesn't have a resource type egressfirewalls, skipping the inspection
W0501 20:34:35.980881 57625 util.go:118] the server doesn't have a resource type egressqoses, skipping the inspection
W0501 20:34:36.040664 57625 util.go:118] the server doesn't have a resource type servicemonitors, skipping the inspection
Wrote inspect data to inspect.local.2673575938140296280.
----

.Next steps

* If `oc adm inspect` did not show the information you need, you can run an sos report.

[id="additional-resources_microshift-gitops_{context}"]
[role="_additional-resources"]
== Additional resources

* Using sos reports
* Generating an sos report for technical support
* {gitops-title}
