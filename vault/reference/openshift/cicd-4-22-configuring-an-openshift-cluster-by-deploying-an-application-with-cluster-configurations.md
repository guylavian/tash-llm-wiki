---
title: "Configuring an OpenShift cluster by deploying an application with cluster configurations"
type: reference
domain: openshift
slug: cicd-4-22-configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring an OpenShift cluster by deploying an application with cluster configurations

[id="configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations"]
= Configuring an OpenShift cluster by deploying an application with cluster configurations

With {gitops-title}, you can configure Argo CD to recursively sync the content of a Git directory with an application that contains custom configurations for your cluster.

.Prerequisites

* You have logged in to the OpenShift Container Platform cluster as an administrator.
* You have installed the {gitops-title} Operator in your cluster.
* You have logged into Argo CD instance.

// Module included in the following assembly:
//
// * gitops/configuring_argo_cd_to_recursively_sync_a_git_repository_with_your_application/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc

[id="using-argo-cd-instance-to-manage-cluster-scoped-resources_{context}"]

= Using an Argo CD instance to manage cluster-scoped resources

To manage cluster-scoped resources, update the existing `Subscription` object for the {gitops-title} Operator and add the namespace of the Argo CD instance to the `ARGOCD_CLUSTER_CONFIG_NAMESPACES` environment variable in the `spec` section.

[discrete]
.Procedure
. In the **Administrator** perspective of the web console, navigate to **Operators** → **Installed Operators** → **{gitops-title}** → **Subscription**.
. Click the **Actions** drop-down menu then click **Edit Subscription**.
. On the **openshift-gitops-operator** Subscription details page, under the **YAML** tab, edit the `Subscription` YAML file by adding the namespace of the Argo CD instance to the `ARGOCD_CLUSTER_CONFIG_NAMESPACES` environment variable in the `spec` section:
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-gitops-operator
  namespace: openshift-operators
...
spec:
  config:
    env:
    - name: ARGOCD_CLUSTER_CONFIG_NAMESPACES
      value: openshift-gitops, <list of namespaces of cluster-scoped Argo CD instances>
...
----
+
. To verify that the Argo instance is configured with a cluster role to manage cluster-scoped resources, perform the following steps:
+
.. Navigate to **User Management** → **Roles** and from the **Filter**  drop-down menu select **Cluster-wide Roles**.
.. Search for the `argocd-application-controller` by using the **Search by name** field.
+
The **Roles** page displays the created cluster role.
+
[TIP]
====
Alternatively, in the OpenShift CLI, run the following command:

[source,terminal]
----
oc auth can-i create oauth -n openshift-gitops --as system:serviceaccount:openshift-gitops:openshift-gitops-argocd-application-controller
----

The output `yes` verifies that the Argo instance is configured with a cluster role to manage cluster-scoped resources. Else, check your configurations and take necessary steps as required.
====

// Module included in the following assembly:
//
// * gitops/configuring_argo_cd_to_recursively_sync_a_git_repository_with_your_application/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc

[id="default-permissions-of-an-argocd-instance_{context}"]

= Default permissions of an Argocd instance

By default Argo CD instance has the following permissions:

* Argo CD instance has the `admin` privileges to manage resources only in the namespace where it is deployed. For instance, an Argo CD instance deployed in the *foo* namespace has the `admin` privileges to manage resources only for that namespace.

* Argo CD has the following cluster-scoped permissions because Argo CD requires cluster-wide `read` privileges on resources to function appropriately:
+
[source,yaml,subs="attributes+"]
----
- verbs:
    - get
    - list
    - watch
   apiGroups:
    - /'*'
   resources:
    - /'*'
 - verbs:
    - get
    - list
   nonResourceURLs:
    - /'*'
----

[NOTE]
====
* You can edit the cluster roles used by the `argocd-server` and `argocd-application-controller` components where Argo CD is running such that the `write` privileges are limited to only the namespaces and resources that you wish Argo CD to manage.

[source,terminal]
----
$ oc edit clusterrole argocd-server
----

[source,terminal]
----
$ oc edit clusterrole argocd-application-controller
----
====

// Module included in the following assembly:
//
// * gitops/configuring_argo_cd_to_recursively_sync_a_git_repository_with_your_application/configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc

[id="run-argo-cd-instance-on-cluster_{context}"]

= Running the Argo CD instance at the cluster-level

The default Argo CD instance and the accompanying controllers, installed by the {gitops-title} Operator, can now run on the infrastructure nodes of the cluster by setting a simple configuration toggle.

.Procedure
. Label the existing nodes:
+
[source,terminal]
----
$ oc label node <node-name> node-role.kubernetes.io/infra=""
----
+
. Optional: If required, you can also apply taints and isolate the workloads on infrastructure nodes and prevent other workloads from scheduling on these nodes:
+
[source,terminal]
----
$ oc adm taint nodes -l node-role.kubernetes.io/infra \
infra=reserved:NoSchedule infra=reserved:NoExecute
----
. Add the `runOnInfra` toggle in the `GitOpsService` custom resource:
+
[source,yaml]
----
apiVersion: pipelines.openshift.io/v1alpha1
kind: GitopsService
metadata:
  name: cluster
spec:
  runOnInfra: true
----
. Optional: If taints have been added to the nodes, then add `tolerations` to the `GitOpsService` custom resource, for example:
+
[source,yaml]
----
  spec:
    runOnInfra: true
    tolerations:
    - effect: NoSchedule
      key: infra
      value: reserved
    - effect: NoExecute
      key: infra
      value: reserved
----
. Verify that the workloads in the `openshift-gitops` namespace are now scheduled on the infrastructure nodes by viewing *Pods* -> *Pod details* for any pod in the console UI.

[NOTE]
====
Any `nodeSelectors` and `tolerations` manually added to the default Argo CD custom resource are overwritten by the toggle and `tolerations` in the `GitOpsService` custom resource.
====

[role="_additional-resources"]
.Additional resources
* To learn more about taints and tolerations, see Controlling pod placement using node taints.
* For more information on infrastructure machine sets, see Creating infrastructure machine sets.

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

// Module included in the following assemblies:
//
// * configuring-an-openshift-cluster-with-argo-cd.adoc

[id="synchronizing-your-application-application-with-your-git-repository_{context}"]
= Synchronizing your application with your Git repository

.Procedure
. In the Argo CD dashboard, notice that the *cluster-configs* Argo CD application has the statuses *Missing* and *OutOfSync*. Because the application was configured with a manual sync policy, Argo CD does not sync it automatically.

. Click *SYNC* on the *cluster-configs* tile, review the changes, and then click *SYNCHRONIZE*. Argo CD will detect any changes in the Git repository automatically. If the configurations are changed, Argo CD will change the status of the *cluster-configs* to *OutOfSync*. You can modify the synchronization policy for Argo CD to automatically apply changes from your Git repository to the cluster.

. Notice that the *cluster-configs* Argo CD application now has the statuses *Healthy* and *Synced*. Click the *cluster-configs* tile to check the details of the synchronized resources and their status on the cluster.

. Navigate to the OpenShift Container Platform web console and click {rh-app-icon} to verify that a link to the *Red Hat Developer Blog - Kubernetes* is now present there.

. Navigate to the *Project* page and search for the `spring-petclinic` namespace to verify that it has been added to the cluster.
+
Your cluster configurations have been successfully synchronized to the cluster.

// Module included in the following assembly:
//
// * configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc

[id="gitops-inbuilt-permissions-for-cluster-config_{context}"]
= In-built permissions for cluster configuration

By default, the Argo CD instance has permissions to manage specific cluster-scoped resources such as cluster Operators, optional OLM Operators and user management.

[NOTE]
====
Argo CD does not have cluster-admin permissions.
====

Permissions for the Argo CD instance:
|===
|**Resources** |**Descriptions**
|Resource Groups | Configure the user or administrator
|`operators.coreos.com` | Optional Operators managed by OLM
|`user.openshift.io` , `rbac.authorization.k8s.io`    | Groups, Users and their permissions
|`config.openshift.io` | Control plane Operators managed by CVO used to configure cluster-wide build configuration, registry configuration and scheduler policies
|`storage.k8s.io`   | Storage
|`console.openshift.io`    | Console customization
|===

// Module included in the following assembly:
//
// * configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc

[id="gitops-additional-permissions-for-cluster-config_{context}"]
= Adding permissions for cluster configuration

You can grant permissions for an Argo CD instance to manage cluster configuration. Create a cluster role with additional permissions and then create a new cluster role binding to associate the cluster role with a service account.

.Procedure

. Log in to the OpenShift Container Platform web console as an admin.
. In the web console, select **User Management** -> **Roles** -> **Create Role**. Use the following `ClusterRole` YAML template to add rules to specify the additional permissions.
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secrets-cluster-role
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["*"]
----
. Click **Create** to add the cluster role.
. Now create the cluster role binding. In the web console, select **User Management** -> **Role Bindings** -> **Create Binding**.
. Select **All Projects** from the **Project** drop-down.
. Click **Create binding**.
. Select **Binding type** as **Cluster-wide role binding (ClusterRoleBinding)**.
. Enter a unique value for the **RoleBinding name**.
. Select the newly created cluster role or an existing cluster role from the drop down list.
. Select the **Subject** as **ServiceAccount** and the provide the **Subject namespace** and **name**.
.. **Subject namespace**: `openshift-gitops`
.. **Subject name**: `openshift-gitops-argocd-application-controller`
. Click **Create**. The YAML file for the `ClusterRoleBinding` object is as follows:
+
[source,yaml]
----
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: cluster-role-binding
subjects:
  - kind: ServiceAccount
    name: openshift-gitops-argocd-application-controller
    namespace: openshift-gitops
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: admin
----

// Module included in the following assembly:
//
// * configuring-an-openshift-cluster-by-deploying-an-application-with-cluster-configurations.adoc

[id="gitops-installing-olm-operators-using-gitops_{context}"]
= Installing OLM Operators using {gitops-title}

{gitops-title} with cluster configurations manages specific cluster-scoped resources and takes care of installing cluster Operators or any namespace-scoped OLM Operators.

Consider a case where as a cluster administrator, you have to install an OLM Operator such as Tekton. You use the OpenShift Container Platform web console to manually install a Tekton Operator or the OpenShift CLI to manually install a Tekton subscription and Tekton Operator group on your cluster.

{gitops-title} places your Kubernetes resources in your Git repository. As a cluster administrator, use {gitops-title} to manage and automate the installation of other OLM Operators without any manual procedures. For example, after you place the Tekton subscription in your Git repository by using {gitops-title}, the {gitops-title} automatically takes this Tekton subscription from your Git repository and installs the Tekton Operator on your cluster.

== Installing cluster-scoped Operators

Operator Lifecycle Manager (OLM) uses a default `global-operators` Operator group in the `openshift-operators` namespace for cluster-scoped Operators. Hence you do not have to manage the `OperatorGroup` resource in your Gitops repository. However, for namespace-scoped Operators, you must manage the `OperatorGroup` resource in that namespace.

To install cluster-scoped Operators, create and place the `Subscription` resource of the required Operator in your Git repository.

.Example: Grafana Operator subscription

[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: grafana
spec:
  channel: v4
  installPlanApproval: Automatic
  name: grafana-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----

== Installing namepace-scoped Operators

To install namespace-scoped Operators, create and place the `Subscription` and `OperatorGroup` resources of the required Operator in your Git repository.

.Example: Ansible Automation Platform Resource Operator

[source,yaml]
----
...
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
  name: ansible-automation-platform
...
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: ansible-automation-platform-operator
  namespace: ansible-automation-platform
spec:
  targetNamespaces:
    - ansible-automation-platform
...
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: ansible-automation-platform
  namespace: ansible-automation-platform
spec:
  channel: patch-me
  installPlanApproval: Automatic
  name: ansible-automation-platform-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
...
----

[IMPORTANT]
====
When deploying multiple Operators using {gitops-title}, you must create only a single Operator group in the corresponding namespace. If more than one Operator group exists in a single namespace, any CSV created in that namespace transition to a `failure` state with the `TooManyOperatorGroups` reason. After the number of Operator groups in their corresponding namespaces reaches one, all the previous `failure` state CSVs transition to `pending` state. You must manually approve the pending install plan to complete the Operator installation.
====
