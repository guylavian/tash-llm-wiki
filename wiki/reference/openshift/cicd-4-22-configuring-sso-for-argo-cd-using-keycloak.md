---
title: "Configuring SSO for Argo CD using Keycloak"
type: reference
domain: openshift
slug: cicd-4-22-configuring-sso-for-argo-cd-using-keycloak
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/configuring-sso-for-argo-cd-using-keycloak
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring SSO for Argo CD using Keycloak

[id="configuring-sso-for-argo-cd-using-keycloak"]
= Configuring SSO for Argo CD using Keycloak

After the {gitops-title} Operator is installed, Argo CD automatically creates a user with `admin` permissions. To manage multiple users, cluster administrators can use Argo CD to configure Single Sign-On (SSO).

.Prerequisites
* Red Hat SSO is installed on the cluster.
* {gitops-title} Operator is installed on the cluster.
* Argo CD is installed on the cluster.

// Module included in the following assemblies:
//
// * configuring-sso-for-argo-cd-using-keycloak.adoc

[id="gitops-creating-a-new-client-in-keycloak_{context}"]
= Configuring a new client in Keycloak

Dex is installed by default for all the Argo CD instances created by the Operator. However, you can delete the Dex configuration and add Keycloak instead to log in to Argo CD using your OpenShift credentials. Keycloak acts as an identity broker between Argo CD and OpenShift.

.Procedure

To configure Keycloak, follow these steps:

. Delete the Dex configuration by removing the `.spec.sso.dex` parameter from the Argo CD custom resource (CR), and save the CR:
+
[source,yaml]
----
dex:
    openShiftOAuth: true
    resources:
      limits:
        cpu:
        memory:
      requests:
        cpu:
        memory:
----

. Set the value of the `provider` parameter to `keycloak` in the Argo CD CR.

. Configure Keycloak by performing one of the following steps:

* For a secure connection, set the value of the `rootCA` parameter as shown in the following example:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  sso:
    provider: keycloak
    keycloak:
      rootCA: "<PEM-encoded-root-certificate>" <1>
  server:
    route:
      enabled: true
----
<1> A custom certificate used to verify the Keycloak's TLS certificate.
+
The Operator reconciles changes in the `.spec.keycloak.rootCA` parameter and updates the `oidc.config` parameter with the PEM encoded root certificate in the `argocd-cm` configuration map.

* For an insecure connection, leave the value of the `rootCA` parameter empty and use the `oidc.tls.insecure.skip.verify` parameter as shown below:
+
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example-argocd
  labels:
    example: basic
spec:
  extraConfig:
    oidc.tls.insecure.skip.verify: "true"
  sso:
    provider: keycloak
    keycloak:
      rootCA: ""
----

[NOTE]
====
The Keycloak instance takes 2-3 minutes to install and run.
====

[id="gitops-logging-into-keycloak_{context}"]
= Logging in to Keycloak

Log in to the Keycloak console to manage identities or roles and define the permissions assigned to the various roles.

.Prerequisites

* The default configuration of Dex is removed.
* Your Argo CD CR must be configured to use the Keycloak SSO provider.

.Procedure

. Get the Keycloak route URL for login:
+
[source,terminal]
----
$ oc -n argocd get route keycloak

NAME        HOST/PORT                                                        PATH   SERVICES   PORT    TERMINATION   WILDCARD
keycloak    keycloak-default.apps.ci-ln-******.origin-ci-int-aws.dev.**.com         keycloak   <all>    reencrypt     None
----
. Get the Keycloak pod name that stores the user name and password as environment variables:
+
[source,terminal]
----
$ oc -n argocd get pods

NAME                      READY   STATUS           RESTARTS   AGE
keycloak-1-2sjcl           1/1    Running            0        45m
----
.. Get the Keycloak user name:
+
[source,terminal]
----
$ oc -n argocd exec keycloak-1-2sjcl -- "env" | grep SSO_ADMIN_USERNAME

SSO_ADMIN_USERNAME=<username>
----
.. Get the Keycloak password:
+
[source,terminal]
----
$ oc -n argocd exec keycloak-1-2sjcl -- "env" | grep SSO_ADMIN_PASSWORD

SSO_ADMIN_PASSWORD=<password>
----
. On the login page, click *LOG IN VIA KEYCLOAK*.
+
[NOTE]
====
You only see the option *LOGIN VIA KEYCLOAK* after the Keycloak instance is ready.
====
. Click *Login with OpenShift*.
+
[NOTE]
====
Login using `kubeadmin` is not supported.
====
+
. Enter the OpenShift credentials to log in.
. Optional: By default, any user logged in to Argo CD has read-only access. You can manage the user level access by updating the `argocd-rbac-cm` config map:
+
[source,yaml]
----
policy.csv:
<name>, <email>, role:admin
----

[id="gitops-uninstalling-keycloak_{context}"]
= Uninstalling Keycloak

You can delete the Keycloak resources and their relevant configurations by removing the `SSO` field from the Argo CD Custom Resource (CR) file. After you remove the `SSO` field, the values in the file look similar to the following:

[source,yaml]
----
  apiVersion: argoproj.io/v1alpha1
  kind: ArgoCD
  metadata:
    name: example-argocd
    labels:
      example: basic
  spec:
    server:
      route:
       enabled: true
----

[NOTE]
====
A Keycloak application created by using this method is currently not persistent. Additional configurations created in the Argo CD Keycloak realm are deleted when the server restarts.
====

[role="_additional-resources"]
.Additional resources
* `jq` command-line JSON processor documentation.
* Argo CD upstream documentation, RBAC Configuration section.
