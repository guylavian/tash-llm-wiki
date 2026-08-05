---
title: "Configuring custom Helm chart repositories"
type: reference
domain: openshift
slug: applications-4-22-configuring-custom-helm-chart-repositories
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/configuring-custom-helm-chart-repositories
version: 4.22
family: applications
documentKind: "Documentation"
---

# Configuring custom Helm chart repositories

[id="configuring-custom-helm-chart-repositories"]
= Configuring custom Helm chart repositories

[role="_abstract"]
You can create Helm releases on an OpenShift Container Platform cluster using the following methods:

* The CLI.
* The *Developer* perspective of the web console.

The *Developer Catalog*, in the *Developer* perspective of the web console, displays the Helm charts available in the cluster. By default, it lists the Helm charts from the Red Hat OpenShift Helm chart repository. For a list of the charts, see the Red Hat `Helm index` file.

As a cluster administrator, you can add multiple cluster-scoped and namespace-scoped Helm chart repositories, separate from the default cluster-scoped Helm repository, and display the Helm charts from these repositories in the *Developer Catalog*.

As a regular user or project member with the appropriate role-based access control (RBAC) permissions, you can add multiple namespace-scoped Helm chart repositories, apart from the default cluster-scoped Helm repository, and display the Helm charts from these repositories in the *Developer Catalog*.

In the *Developer* perspective of the web console, you can use the *Helm* page to:

* Create Helm Releases and Repositories using the *Create* button.

* Create, update, or delete a cluster-scoped or namespace-scoped Helm chart repository.

* View the list of the existing Helm chart repositories in the Repositories tab, which can also be easily distinguished as either cluster scoped or namespace scoped.

[id="installing-a-helm-chart-on-an-openshift-cluster_{context}"]

= Installing a Helm chart on an OpenShift Container Platform cluster

.Prerequisites
* You have a running OpenShift Container Platform cluster and you have logged into it.
* You have installed Helm.

.Procedure

. Create a new project:
+
[source,terminal]
----
$ oc new-project vault
----

. Add a repository of Helm charts to your local Helm client:
+
[source,terminal]
----
$ helm repo add openshift-helm-charts https://charts.openshift.io/
----
+
.Example output
[source,terminal]
----
"openshift-helm-charts" has been added to your repositories
----

. Update the repository:
+
[source,terminal]
----
$ helm repo update
----

. Install an example HashiCorp Vault:
+
[source,terminal]
----
$ helm install example-vault openshift-helm-charts/hashicorp-vault
----
+
.Example output
[source,terminal]
----
NAME: example-vault
LAST DEPLOYED: Fri Mar 11 12:02:12 2022
NAMESPACE: vault
STATUS: deployed
REVISION: 1
NOTES:
Thank you for installing HashiCorp Vault!
----

. Verify that the chart has installed successfully:
+
[source,terminal]
----
$ helm list
----
+
.Example output
[source,terminal]
----
NAME         	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART       	APP VERSION
example-vault	vault    	1       	2022-03-11 12:02:12.296226673 +0530 IST	deployed	vault-0.19.0	1.9.2
----

[id="odc-creating-helm-releases-using-developer-perspective_{context}"]
= Creating Helm releases using the Developer perspective

You can use either the *Developer* perspective in the web console or the CLI to select and create a release from the Helm charts listed in the *Developer Catalog*. You can create Helm releases by installing Helm charts and see them in the *Developer* perspective of the web console.

.Prerequisites

* You have logged in to the web console and have switched to the *Developer* perspective.
* You have logged in to the web console and have switched to the *Developer* perspective.

.Procedure
To create Helm releases from the Helm charts provided in the *Developer Catalog*:

. In the *Developer* perspective, navigate to the *+Add* view and select a project. Then click *Helm Chart* option to see all the Helm Charts in the *Developer Catalog*.
. Select a chart and read the description, README, and other details about the chart.
. Click *Create*.
+
.Helm charts in developer catalog
image::odc_helm_chart_devcatalog_new.png[]
+
. In the *Create Helm Release* page:
.. Enter a unique name for the release in the *Release Name* field.
.. Select the required chart version from the *Chart Version* drop-down list.
.. Configure your Helm chart by using the *Form View* or the *YAML View*.
+
[NOTE]
====
Where available, you can switch between the *YAML View* and *Form View*. The data is persisted when switching between the views.
====
+
.. Click *Create* to create a Helm release. The web console displays the new release in the *Topology* view.
+
If a Helm chart has release notes, the web console displays them.
+
If a Helm chart creates workloads, the web console displays them on the *Topology* or *Helm release details* page. The workloads are `DaemonSet`, `CronJob`, `Pod`, `Deployment`, and `DeploymentConfig`.

.. View the newly created Helm release in the *Helm Releases* page.

You can upgrade, rollback, or delete a Helm release by using the *Actions* button on the side panel or by right-clicking a Helm release.

== Using Helm in the web terminal

You can use Helm by Accessing the web terminal in the *Developer* perspective of the web console.
You can use Helm by Accessing the web terminal in the *Developer* perspective of the web console.

[id="creating-a-custom-helm-chart-on-openshift_{context}"]
= Creating a custom Helm chart on OpenShift Container Platform

.Procedure
. Create a new project:
+
[source,terminal]
----
$ oc new-project nodejs-ex-k
----

. Download an example Node.js chart that contains OpenShift Container Platform objects:
+
[source,terminal]
----
$ git clone https://github.com/redhat-developer/redhat-helm-charts
----

. Go to the directory with the sample chart:
+
[source,terminal]
----
$ cd redhat-helm-charts/alpha/nodejs-ex-k/
----

. Edit the `Chart.yaml` file  and add a description of your chart:
+
[source,yaml]
----
apiVersion: v2 <1>
name: nodejs-ex-k <2>
description: A Helm chart for OpenShift <3>
icon: https://static.redhat.com/libs/redhat/brand-assets/latest/corp/logo.svg <4>
version: 0.2.1 <5>
----
+
<1> The chart API version. It should be `v2` for Helm charts that require at least Helm 3.
<2> The name of your chart.
<3> The description of your chart.
<4> The URL to an image to be used as an icon.
<5> The Version of your chart as per the Semantic Versioning (SemVer) 2.0.0 Specification.

. Verify that the chart is formatted properly:
+
[source,terminal]
----
$ helm lint
----
+
.Example output
[source,terminal]
----
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
----

. Navigate to the previous directory level:
+
[source,terminal]
----
$ cd ..
----

. Install the chart:
+
[source,terminal]
----
$ helm install nodejs-chart nodejs-ex-k
----

. Verify that the chart has installed successfully:
+
[source,terminal]
----
$ helm list
----
+
.Example output
[source,terminal]
----
NAME NAMESPACE REVISION UPDATED STATUS CHART APP VERSION
nodejs-chart nodejs-ex-k 1 2019-12-05 15:06:51.379134163 -0500 EST deployed nodejs-0.1.0  1.16.0
----

[id="adding-helm-chart-repositories_{context}"]
= Adding custom Helm chart repositories

As a cluster administrator, you can add custom Helm chart repositories to your cluster and enable access to the Helm charts from these repositories in the *Developer Catalog*.

.Procedure

. To add a new Helm Chart Repository, you must add the Helm Chart Repository custom resource (CR) to your cluster.
+
.Sample Helm Chart Repository CR

[source,yaml]
----
apiVersion: helm.openshift.io/v1beta1
kind: HelmChartRepository
metadata:
  name: <name>
spec:
 # optional name that might be used by console
 # name: <chart-display-name>
  connectionConfig:
    url: <helm-chart-repository-url>
----
+
For example, to add an Azure sample chart repository, run:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: helm.openshift.io/v1beta1
kind: HelmChartRepository
metadata:
  name: azure-sample-repo
spec:
  name: azure-sample-repo
  connectionConfig:
    url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
EOF
----
+
. Navigate to  the *Developer Catalog* in the web console to verify that the Helm charts from the chart repository are displayed.
+
For example, use the *Chart repositories* filter to search for a Helm chart from the repository.
+
.Chart repositories filter
image::odc_helm_chart_repo_filter.png[]
+
[NOTE]
====
If a cluster administrator removes all of the chart repositories, then you cannot view the Helm option in the *+Add* view, *Developer Catalog*, and left navigation panel.
====
// Module included in the following assemblies:
//
// * applications/working_with_helm_charts/configuring-custom-helm-chart-repositories.adoc

[id="adding-namespace-scoped-helm-chart-repositories_{context}"]
= Adding namespace-scoped custom Helm chart repositories

[role="_abstract"]
The cluster-scoped `HelmChartRepository` custom resource definition (CRD) for Helm repository provides the ability for administrators to add Helm repositories as custom resources. The namespace-scoped `ProjectHelmChartRepository` CRD allows project members with the appropriate role-based access control (RBAC) permissions to create Helm repository resources of their choice but scoped to their namespace. Such project members can see charts from both cluster-scoped and namespace-scoped Helm repository resources.

[NOTE]
====
* Administrators can limit users from creating namespace-scoped Helm repository resources. By limiting users, administrators have the flexibility to control the RBAC through a namespace role instead of a cluster role. This avoids unnecessary permission elevation for the user and prevents access to unauthorized services or applications.
* The addition of the namespace-scoped Helm repository does not impact the behavior of the existing cluster-scoped Helm repository.
====

As a regular user or project member with the appropriate RBAC permissions, you can add custom namespace-scoped Helm chart repositories to your cluster and enable access to the Helm charts from these repositories in the *Developer Catalog*.

.Procedure

. To add a new namespace-scoped Helm Chart Repository, you must add the Helm Chart Repository custom resource (CR) to your namespace.
+
.Sample Namespace-scoped Helm Chart Repository CR

[source,yaml]
----
apiVersion: helm.openshift.io/v1beta1
kind: ProjectHelmChartRepository
metadata:
  name: <name>
spec:
  url: https://my.chart-repo.org/stable

  # optional name that might be used by console
  name: <chart-repo-display-name>

  # optional and only needed for UI purposes
  description: <My private chart repo>

  # required: chart repository URL
  connectionConfig:
    url: <helm-chart-repository-url>
----
+
For example, to add an Azure sample chart repository scoped to your `my-namespace` namespace, run:
+
[source,terminal]
----
$ cat <<EOF | oc apply --namespace my-namespace -f -
apiVersion: helm.openshift.io/v1beta1
kind: ProjectHelmChartRepository
metadata:
  name: azure-sample-repo
spec:
  name: azure-sample-repo
  connectionConfig:
    url: https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
EOF
----
+
The output verifies that the namespace-scoped Helm Chart Repository CR is created:
+
.Example output
----
projecthelmchartrepository.helm.openshift.io/azure-sample-repo created
----

. Navigate to  the *Developer Catalog* in the web console to verify that the Helm charts from the chart repository are displayed in your `my-namespace` namespace.
+
For example, use the *Chart repositories* filter to search for a Helm chart from the repository.
+
.Chart repositories filter in your namespace
image::odc_namespace_helm_chart_repo_filter.png[]
+
Alternatively, run:
+
[source,terminal]
----
$ oc get projecthelmchartrepositories --namespace my-namespace
----
+
.Example output
----
NAME                     AGE
azure-sample-repo        1m
----
+
[NOTE]
====
If a cluster administrator or a regular user with appropriate RBAC permissions removes all of the chart repositories in a specific namespace, then you cannot view the Helm option in the *+Add* view, *Developer Catalog*, and left navigation panel for that specific namespace.
====
[id="creating-credentials-and-certificates-to-add-helm-repositories_{context}"]
= Creating credentials and CA certificates to add Helm chart repositories

Some Helm chart repositories need credentials and custom certificate authority (CA) certificates to connect to it. You can use the web console as well as the CLI to add credentials and certificates.

.Procedure
To configure the credentials and certificates, and then add a Helm chart repository using the CLI:

. In the `openshift-config` namespace, create a `ConfigMap` object with a custom CA certificate in PEM encoded format, and store it under the `ca-bundle.crt` key within the config map:
+
[source,terminal]
----
$ oc create configmap helm-ca-cert \
--from-file=ca-bundle.crt=/path/to/certs/ca.crt \
-n openshift-config
----
+
. In the `openshift-config` namespace, create a `Secret` object to add the client TLS configurations:
+
[source,terminal]
----
$ oc create secret tls helm-tls-configs \
--cert=/path/to/certs/client.crt \
--key=/path/to/certs/client.key \
-n openshift-config
----
+
Note that the client certificate and key must be in PEM encoded format and stored under the keys `tls.crt` and `tls.key`, respectively.

. Add the Helm repository as follows:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: helm.openshift.io/v1beta1
kind: HelmChartRepository
metadata:
  name: <helm-repository>
spec:
  name: <helm-repository>
  connectionConfig:
    url: <URL for the Helm repository>
    tlsConfig:
        name: helm-tls-configs
    ca:
	name: helm-ca-cert
EOF
----
+
The `ConfigMap` and `Secret` are consumed in the HelmChartRepository CR using the `tlsConfig` and `ca` fields. These certificates are used to connect to the Helm repository URL.
. By default, all authenticated users have access to all configured charts. However, for chart repositories where certificates are needed, you must provide users with read access to the `helm-ca-cert` config map and `helm-tls-configs` secret in the `openshift-config` namespace, as follows:
+
[source,terminal]
----
$ cat <<EOF | kubectl apply -f -
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: openshift-config
  name: helm-chartrepos-tls-conf-viewer
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  resourceNames: ["helm-ca-cert"]
  verbs: ["get"]
- apiGroups: [""]
  resources: ["secrets"]
  resourceNames: ["helm-tls-configs"]
  verbs: ["get"]
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  namespace: openshift-config
  name: helm-chartrepos-tls-conf-viewer
subjects:
  - kind: Group
    apiGroup: rbac.authorization.k8s.io
    name: 'system:authenticated'
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: helm-chartrepos-tls-conf-viewer
EOF
----

[id="filtering-helm-charts-by-certification-level_{context}"]
= Filtering Helm Charts by their certification level

You can filter Helm charts based on their certification level in the *Developer Catalog*.

.Procedure

. In the *Developer* perspective, navigate to the *+Add* view and select a project.

. From the *Developer Catalog* tile, select the *Helm Chart* option to see all the Helm charts in the *Developer Catalog*.

. Use the filters to the left of the list of Helm charts to filter the required charts:
* Use the *Chart Repositories* filter to filter charts provided by *Red Hat Certification Charts* or *OpenShift Helm Charts*.
* Use the *Source* filter to filter charts sourced from *Partners*, *Community*, or *Red Hat*. Certified charts are indicated with the (image:odc_verified_icon.png[title="Certified icon"]) icon.

[NOTE]
====
The *Source* filter will not be visible when there is only one provider type.
====

You can now select the required chart and install it.

[id="helm-disabling-helm-chart-repositories_{context}"]
= Disabling Helm Chart repositories

You can disable Helm Charts from a particular Helm Chart Repository in the catalog by setting the `disabled` property in the `HelmChartRepository` custom resource to `true`.

.Procedure

* To disable a Helm Chart repository by using CLI, add the `disabled: true` flag to the custom resource. For example, to remove an Azure sample chart repository, run:
+
----
$ cat <<EOF | oc apply -f -
apiVersion: helm.openshift.io/v1beta1
kind: HelmChartRepository
metadata:
  name: azure-sample-repo
spec:
  connectionConfig:
   url:https://raw.githubusercontent.com/Azure-Samples/helm-charts/master/docs
  disabled: true
EOF
----

*  To disable a recently added Helm Chart repository by using Web Console:
+
. Go to *Custom Resource Definitions* and search for the `HelmChartRepository` custom resource.

. Go to *Instances*, find the repository you want to disable, and click its name.

. Go to the *YAML* tab, add the `disabled: true` flag in the `spec` section, and click `Save`.
+
.Example
----
spec:
  connectionConfig:
    url: <url-of-the-repositoru-to-be-disabled>
  disabled: true
----
+
The repository is now disabled and will not appear in the catalog.
