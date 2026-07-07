---
title: "Configuring SSO for Argo CD using Dex"
type: reference
domain: openshift
slug: cicd-4-22-configuring-sso-on-argo-cd-using-dex
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/configuring-sso-on-argo-cd-using-dex
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring SSO for Argo CD using Dex

[id="configuring-sso-for-argo-cd-using-dex"]
= Configuring SSO for Argo CD using Dex

After the {gitops-title} Operator is installed, Argo CD automatically creates a user with `admin` permissions. To manage multiple users, cluster administrators can use Argo CD to configure Single Sign-On (SSO).

[IMPORTANT]
====
The `spec.dex` parameter in the ArgoCD CR is deprecated. In a future release of {gitops-title} v1.10.0, configuring Dex using the `spec.dex` parameter in the ArgoCD CR is planned to be removed. Consider using the `.spec.sso` parameter instead.
====

// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift
[id="gitops-creating-a-new-client-in-dex_{context}"]
= Enabling the Dex OpenShift OAuth Connector

Dex uses the users and groups defined within OpenShift by checking the `OAuth` server provided by the platform. The following example shows the properties of Dex along with example configurations:

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: openshift-oauth
spec:
  dex:
    openShiftOAuth: true <1>
    groups:<2>
     - default
  rbac:<3>
    defaultPolicy: 'role:readonly'
    policy: |
      g, cluster-admins, role:admin
    scopes: '[groups]'
----
<1> The `openShiftOAuth` property triggers the Operator to automatically configure the built-in OpenShift `OAuth` server when the value is set to `true`.
<2> The `groups` property allows users of the specified group(s) to log in.
<3> The RBAC policy property assigns the admin role in the Argo CD cluster to users in the OpenShift `cluster-admins` group.

// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift

[id="gitops-dex-role-mappings_{context}"]
= Mapping users to specific roles

Argo CD cannot map users to specific roles if they have a direct `ClusterRoleBinding` role. You can manually change the role as `role:admin` on SSO through OpenShift.

.Procedure

. Create a group named `cluster-admins`.
+
[source,terminal]
----
$ oc adm groups new cluster-admins
----
. Add the user to the group.
+
[source,terminal]
----
$ oc adm groups add-users cluster-admins USER
----
. Apply the `cluster-admin` `ClusterRole` to the group:
+
[source,terminal]
----
$ oc adm policy add-cluster-role-to-group cluster-admin cluster-admins
----

//include::modules/gitops-configuring-argo-cd-using-dex-github-conector.adoc[leveloffset=+1]

// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-using-dex

[id="gitops-disable-dex_{context}"]
= Disabling Dex

Dex is installed by default for all the Argo CD instances created by the Operator. You can configure {gitops-title} to use Dex as the SSO authentication provider by setting the `.spec.dex` parameter.

[IMPORTANT]
====
In {gitops-title} v1.6.0, `DISABLE_DEX` is deprecated and is planned to be removed in {gitops-title} v1.10.0. Consider using the `.spec.sso.dex` parameter instead. See "Enabling or disabling Dex using .spec.sso".
====

.Procedure

* Set the environmental variable `DISABLE_DEX` to `true` in the YAML resource of the Operator:
+
[source,yaml]
----
...
spec:
  config:
    env:
    - name: DISABLE_DEX
      value: "true"
...
----

// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-using-dex

[id="gitops-disable-dex-using-spec-sso_{context}"]
= Enabling or disabling Dex using .spec.sso

You can configure {gitops-title} to use Dex as its SSO authentication provider by setting the `.spec.sso` parameter.

.Procedure

. To enable Dex, set the `.spec.sso.provider: dex` parameter in the YAML resource of the Operator:

+
[source,yaml]
----
...
spec:
  sso:
    provider: dex
    dex:
      openShiftOAuth: true
...
----
+
. To disable dex, either remove the `spec.sso` element from the Argo CD custom resource, or specify a different SSO provider.

[role="_additional-resources"]
.Additional resources
* `jq` command-line JSON processor documentation.
* Argo CD upstream documentation, RBAC Configuration section.
