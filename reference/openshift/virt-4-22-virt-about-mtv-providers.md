---
title: "About {mtv-first} providers"
type: reference
domain: openshift
slug: virt-4-22-virt-about-mtv-providers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-about-mtv-providers
version: 4.22
family: virt
documentKind: "Documentation"
---

# About {mtv-first} providers

[id="virt-about-mtv-providers"]
= About {mtv-first} providers

[role="_abstract"]
To migrate a virtual machine (VM) across OpenShift Container Platform clusters, you must configure an OpenShift Container Platform provider for each cluster that you are including in the migration. If {mtv-short} is already installed on a cluster, a local provider already exists.

// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-mtv-providers.adoc

[id="virt-configuring-root-ca-for-providers_{context}"]
= Configuring the root certificate authority for providers

[role="_abstract"]
You must configure an OpenShift Container Platform provider for each cluster that you are including in the migration, and each provider requires a certificate authority (CA) for the cluster. It is important to configure the root CA for the entire cluster to avoid CA expiration, which causes the provider to fail.

.Procedure

. Run the following command against the cluster for which you are creating the provider:
+
[source,terminal]
----
$ oc get cm kube-root-ca.crt -o=jsonpath={.data.ca\\.crt}
----

. Copy the printed certificate.

. In the {mtv-first} web console, create a provider and select *{VirtProductName}*.

. Paste the certificate into the *CA certificate* field, as shown in the following example:
+
[source,terminal]
----
-----BEGIN CERTIFICATE-----
<CA_certificate_content>
-----END CERTIFICATE-----
----

// Module included in the following assemblies:
//
// * virt/live_migration/virt-about-mtv-providers.adoc

[id="virt-creating-long-lived-account-and-token_{context}"]
= Creating the long-lived service account and token to use with MTV providers

[role="_abstract"]
When you register an {VirtProductName} provider in the {mtv-first} web console, you must supply credentials that allow MTV to interact with the cluster. Creating a long-lived service account and cluster role binding gives MTV persistent permissions to read and create virtual machine resources during migration.

.Procedure

. Create the cluster role as shown in the following example:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: live-migration-role
rules:
  - apiGroups:
      - forklift.konveyor.io
    resources:
      - '*'
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - secrets
      - namespaces
      - configmaps
      - persistentvolumes
      - persistentvolumeclaims
    verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
  - apiGroups:
      - k8s.cni.cncf.io
    resources:
      - network-attachment-definitions
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - storage.k8s.io
    resources:
      - storageclasses
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - kubevirt.io
    resources:
      - virtualmachines
      - virtualmachines/finalizers
      - virtualmachineinstancemigrations
    verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
  - apiGroups:
      - kubevirt.io
    resources:
      - kubevirts
      - virtualmachineinstances
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - cdi.kubevirt.io
    resources:
      - datavolumes
      - datavolumes/finalizers
    verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
  - apiGroups:
      - apps
    resources:
      - deployments
    verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
  - apiGroups:
      - instancetype.kubevirt.io
    resources:
      - virtualmachineclusterpreferences
      - virtualmachineclusterinstancetypes
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - instancetype.kubevirt.io
    resources:
      - virtualmachinepreferences
      - virtualmachineinstancetypes
    verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
----

. Create the cluster role by running the following command:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. Create a service account by running the following command:
+
[source,terminal]
----
$ oc create serviceaccount <service_account_name> -n <service_account_namespace>
----

. Create a cluster role binding that links the service account to the cluster role, by running the following command:
+
[source,terminal]
----
$ oc create clusterrolebinding <service_account_name> --clusterrole=<cluster_role_name> --serviceaccount=<service_account_namespace>:<service_account_name>
----

. Create a secret to hold the token by saving the following manifest as a YAML file:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <name_of_secret>
  namespace: <namespace_for_service_account>
  annotations:
    kubernetes.io/service-account.name: <service_account_name>
type: kubernetes.io/service-account-token
----

. Apply the manifest by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

. After the secret is populated, run the following command to get the service account bearer token:
+
[source,terminal]
----
$ TOKEN_BASE64=$(oc get secret "<name_of_secret>" -n "<namespace_bound_to_service_account>" -o jsonpath='{.data.token}')
  TOKEN=$(echo "$TOKEN_BASE64" | base64 --decode)
  echo "$TOKEN"
----

. Copy the printed token.

. In the {mtv-first} web console, when you create a provider and select *{VirtProductName}*, paste the token into the *Service account bearer token* field.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Adding a Red Hat {VirtProductName} source provider
* Adding an {VirtProductName} destination provider
