---
title: "Defining a default network policy for projects"
type: reference
domain: openshift
slug: networking-4-22-default-network-policy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/default-network-policy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Defining a default network policy for projects

[id="default-network-policy"]
= Defining a default network policy for projects

[role="_abstract"]
To enforce consistent network isolation and security controls across projects, configure a default project template to automatically apply network policies to newly created projects.

// TODO OSDOCS-11830 or namespace administrator?
As a cluster administrator, you can modify the new project template to automatically include network policies when you create a new project. If you do not yet have a customized template for new projects, you must first create one.

// Module included in the following assemblies:
//
// * applications/projects/configuring-project-creation.adoc
// * post_installation_configuration/network-configuration.adoc

[id="modifying-template-for-new-projects_{context}"]
= Modifying the template for new projects

[role="_abstract"]
To modify the default project template to customize the resources and settings applied when users create new projects, you can create a custom project template.

As a cluster administrator, you can modify the default project template so that new projects are created using your custom requirements.

To create your own custom project template:

.Prerequisites
* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have access to a OpenShift Container Platform cluster using an account with `dedicated-admin` permissions.

.Procedure

. Log in as a user with `cluster-admin` privileges.

. Generate the default project template:
+
[source,terminal]
----
$ oc adm create-bootstrap-project-template -o yaml > template.yaml
----

. Use a text editor to modify the generated `template.yaml` file by adding
objects or modifying existing objects.

. The project template must be created in the `openshift-config` namespace. Load
your modified template:
+
[source,terminal]
----
$ oc create -f template.yaml -n openshift-config
----

. Edit the project configuration resource using the web console or CLI.

** Using the web console:
... Navigate to the *Administration* -> *Cluster Settings* page.
... Click *Configuration* to view all configuration resources.
... Find the entry for *Project* and click *Edit YAML*.

** Using the CLI:
... Edit the `project.config.openshift.io/cluster` resource:
+
[source,terminal]
----
$ oc edit project.config.openshift.io/cluster
----

. Update the `spec` section to include the `projectRequestTemplate` and `name`
parameters, and set the name of your uploaded project template. The default name
is `project-request`.
+
.Project configuration resource with custom project template
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Project
metadata:
# ...
spec:
  projectRequestTemplate:
    name: <template_name>
# ...
----

. After you save your changes, create a new project to verify that your changes
were successfully applied.

// Module included in the following assemblies:
//
// * networking/network_security/network_policy/default-network-policy.adoc
// * networking/configuring-networkpolicy.adoc
// * post_installation_configuration/network-configuration.adoc

[id="nw-networkpolicy-project-defaults_{context}"]
= Adding network policies to the new project template

[role="_abstract"]
You can add `NetworkPolicy` objects to the default project template so that new projects automatically include predefined network isolation rules. Applying network policies through templates helps enforce consistent network security controls across projects.

.Prerequisites

* Your cluster uses a default container network interface (CNI) network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes.
* You installed the OpenShift CLI (`oc`).
* You must log in to the cluster with a user with `cluster-admin` privileges.
* You must have created a custom default project template for new projects.

.Procedure

. Edit the default template for a new project by running the following command:
+
[source,terminal]
----
$ oc edit template <project_template> -n openshift-config
----
+
Replace `<project_template>` with the name of the default template that you configured for your cluster. The default template name is `project-request`.

. In the template, add each `NetworkPolicy` object as an element to the `objects` parameter. The `objects` parameter accepts a collection of one or more objects.
+
In the following example, the `objects` parameter collection includes several `NetworkPolicy` objects.
+
[source,yaml]
----
objects:
- apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: allow-from-same-namespace
  spec:
    podSelector: {}
    ingress:
    - from:
      - podSelector: {}
- apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: allow-from-openshift-ingress
  spec:
    ingress:
    - from:
      - namespaceSelector:
          matchLabels:
            policy-group.network.openshift.io/ingress:
    podSelector: {}
    policyTypes:
    - Ingress
- apiVersion: networking.k8s.io/v1
  kind: NetworkPolicy
  metadata:
    name: allow-from-kube-apiserver-operator
  spec:
    ingress:
    - from:
      - namespaceSelector:
          matchLabels:
            kubernetes.io/metadata.name: openshift-kube-apiserver-operator
        podSelector:
          matchLabels:
            app: kube-apiserver-operator
    policyTypes:
    - Ingress
...
----

. Optional: Create a new project and confirm the successful creation of your network policy objects.

.. Create a new project:
+
[source,terminal]
----
$ oc new-project <project>
----
+
Replace `<project>` with the name of the project you want to create.

.. Confirm that the network policy objects in the new project template exist in the new project:
+
[source,terminal]
----
$ oc get networkpolicy
----
+
Expected output:
+
[source,terminal]
----
NAME                           POD-SELECTOR   AGE
allow-from-openshift-ingress   <none>         7s
allow-from-same-namespace      <none>         7s
----
