---
title: "Configuring SSO for Argo CD on OpenShift"
type: reference
domain: openshift
slug: cicd-4-22-configuring-sso-for-argo-cd-on-openshift
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/configuring-sso-for-argo-cd-on-openshift
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring SSO for Argo CD on OpenShift

[id="configuring-sso-for-argo-cd-on-openshift"]
= Configuring SSO for Argo CD on OpenShift

After the {gitops-title} Operator is installed, Argo CD automatically creates a user with `admin` permissions. To manage multiple users, Argo CD allows cluster administrators to configure SSO.

.Prerequisites
* Red Hat SSO is installed on the cluster.

// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift

[id="creating-a-new-client-in-keycloak_{context}"]
= Creating a new client in Keycloak

.Procedure

. Log in to your Keycloak server, select the realm you want to use, navigate to the *Clients* page, and then click *Create* in the upper-right section of the screen.

. Specify the following values:
Client ID:: `argocd`
Client Protocol:: `openid-connect`
Route URL:: <your-argo-cd-route-url>
Access Type:: `confidential`
Valid Redirect URIs:: <your-argo-cd-route-url>/auth/callback
Base URL:: `/applications`

. Click *Save* to see the *Credentials* tab added to the *Client* page.

. Copy the secret from the *Credentials* tab for further configuration.

// Module included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift.adoc

[id="configuring-the-groups-claim_{context}"]
= Configuring the groups claim

To manage users in Argo CD, you must configure a groups claim that can be included in the authentication token.

.Procedure

. In the Keycloak dashboard, navigate to *Client Scope* and add a new client with the following values:
Name:: `groups`
Protocol:: `openid-connect`
Display On Content Scope:: `On`
Include to Token Scope:: `On`

. Click *Save* and navigate to `groups` -> *Mappers*.

. Add a new token mapper with the following values:
Name:: `groups`
Mapper Type:: `Group Membership`
Token Claim Name:: `groups`
+
The token mapper adds the `groups` claim to the token when the client requests `groups`.

. Navigate to *Clients* -> *Client Scopes* and configure the client to provide the groups scope. Select `groups` in the *Assigned Default Client Scopes* table and click *Add selected*. The `groups` scope must be in the *Available Client Scopes* table.

. Navigate to *Users* -> *Admin* -> *Groups* and create a group `ArgoCDAdmins`.

// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-sso-for-argo-cd-on-openshift.adoc

[id="configuring-argo-cd-oidc_{context}"]
= Configuring Argo CD OIDC

To configure Argo CD OpenID Connect (OIDC), you must generate your client secret, encode it, and add it to your custom resource.

.Prerequisites

* You have obtained your client secret.

.Procedure

. Store the client secret you generated.

.. Encode the client secret in base64:
+
[source,terminal]
----
$ echo -n '83083958-8ec6-47b0-a411-a8c55381fbd2' | base64
----

.. Edit the secret and add the base64 value to an `oidc.keycloak.clientSecret` key:
+
[source,terminal]
----
$ oc edit secret argocd-secret -n <namespace>
----
+
.Example YAML of the secret
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: argocd-secret
data:
  oidc.keycloak.clientSecret: ODMwODM5NTgtOGVjNi00N2IwLWE0MTEtYThjNTUzODFmYmQy
----

. Edit the `argocd` custom resource and add the OIDC configuration to enable the Keycloak authentication:
+
[source,terminal]
----
$ oc edit argocd -n <your_namespace>
----
+
.Example of `argocd` custom resource
[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  creationTimestamp: null
  name: argocd
  namespace: argocd
spec:
  resourceExclusions: |
    - apiGroups:
      - tekton.dev
      clusters:
      - '*'
      kinds:
      - TaskRun
      - PipelineRun
  oidcConfig: |
    name: OpenShift Single Sign-On
    issuer: https://keycloak.example.com/auth/realms/myrealm <1>
    clientID: argocd <2>
    clientSecret: $oidc.keycloak.clientSecret <3>
    requestedScopes: ["openid", "profile", "email", "groups"] <4>
  server:
    route:
      enabled: true
----
<1> `issuer` must end with the correct realm name (in this example `myrealm`).
<2> `clientID` is the Client ID you configured in your Keycloak account.
<3> `clientSecret` points to the right key you created in the argocd-secret secret.
<4> `requestedScopes` contains the groups claim if you did not add it to the Default scope.

// Module is included in the following assemblies:
//
// *

[id="keycloak-identity-brokering-with-openshift-oauthclient_{context}"]
= Keycloak Identity Brokering with OpenShift Container Platform

You can configure a Keycloak instance to use OpenShift Container Platform for authentication through Identity Brokering. This allows for Single Sign-On (SSO) between the OpenShift Container Platform cluster and the Keycloak instance.

.Prerequisites

* `jq` CLI tool is installed.

.Procedure

. Obtain the OpenShift Container Platform API URL:
+
[source,terminal]
----
$ curl -s -k -H "Authorization: Bearer $(oc whoami -t)" https://<openshift-user-facing-api-url>/apis/config.openshift.io/v1/infrastructures/cluster | jq ".status.apiServerURL".
----
+
[NOTE]
====
The address of the OpenShift Container Platform API is often protected by HTTPS. Therefore, you must configure X509_CA_BUNDLE in the container and set it to `/var/run/secrets/kubernetes.io/serviceaccount/ca.crt`. Otherwise, Keycloak cannot communicate with the API Server.
====

. In the Keycloak server dashboard, navigate to *Identity Providers* and select *Openshift v4*. Specify the following values:
*Base Url*:: OpenShift Container Platform 4 API URL
*Client ID*:: `keycloak-broker`
*Client Secret*:: A secret that you want define
+
Now you can log in to Argo CD with your OpenShift Container Platform credentials through Keycloak as an Identity Broker.

// Module is included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift

[id="registering-an-additional-oauth-client_{context}"]
= Registering an additional an OAuth client

If you need an additional OAuth client to manage authentication for your OpenShift Container Platform cluster, you can register one.

.Procedure

* To register your client:
+
[source,terminal]
----
$ oc create -f <(echo '
kind: OAuthClient
apiVersion: oauth.openshift.io/v1
metadata:
 name: keycloak-broker <1>
secret: "..." <2>
redirectURIs:
- "https://keycloak-keycloak.apps.dev-svc-4.7-020201.devcluster.openshift.com/auth/realms/myrealm/broker/openshift-v4/endpoint" <3>
grantMethod: prompt <4>
')
----

<1> The name of the OAuth client is used as the `client_id` parameter when making requests to `<namespace_route>/oauth/authorize` and `<namespace_route>/oauth/token`.
<2> The `secret` is used as the client_secret parameter when making requests to `<namespace_route>/oauth/token`.
<3> The `redirect_uri` parameter specified in requests to `<namespace_route>/oauth/authorize` and `<namespace_route>/oauth/token` must be equal to or prefixed by one of the URIs listed in the `redirectURIs` parameter value.
<4> If the user has not granted access to this client, the `grantMethod` determines which action to take when this client requests tokens. Specify `auto` to automatically approve the grant and retry the request, or `prompt` to prompt the user to approve or deny the grant.

// Module included in the following assemblies:
//
// * configuring-sso-for-argo-cd-on-openshift.adoc

[id="configuring-groups-and-argocd-rbac_{context}"]
= Configure groups and Argo CD RBAC

Role-based access control (RBAC) allows you to provide relevant permissions to users.

.Prerequisites

* You have created the `ArgoCDAdmins` group in Keycloak.

* The user you want to give permissions to has logged in to Argo CD.

.Procedure

. In the Keycloak dashboard navigate to *Users* -> *Groups*. Add the user to the Keycloak group `ArgoCDAdmins`.

. Ensure that `ArgoCDAdmins` group has the required permissions in the `argocd-rbac` config map.
** Edit the config map:
+
[source,terminal]
----
$ oc edit configmap argocd-rbac-cm -n <namespace>
----
+
.Example of a config map that defines `admin` permissions.
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-rbac-cm
data:
  policy.csv: |
    g, /ArgoCDAdmins, role:admin
----

//include::modules/gitops-enabling-dex.adoc[leveloffset=+1]

// Module is included in the following assemblies:
//
// * openshift-docs/cicd/gitops/configuring-a-cluster-to-use-gitops.adoc

[id="in-built-permissions_{context}"]
= In-built permissions for Argo CD

This section lists the permissions that are granted to ArgoCD to manage specific cluster-scoped resources which include cluster operators, optional OLM operators, and user management. Note that ArgoCD is not granted `cluster-admin` permissions.

.Permissions granted to Argo CD
|==========================
|Resource group|What it configures for a user or an administrator
|operators.coreos.com      |Optional operators managed by OLM
|user.openshift.io, rbac.authorization.k8s.io |Groups, Users, and their permissions
|config.openshift.io       |Control plane operators managed by CVO used to configure cluster-wide build configuration, registry configuration, and scheduler policies
|storage.k8s.io       |Storage
|console.openshift.io|Console customization
|==========================

[role="_additional-resources"]
.Additional resources
* `jq` command-line JSON processor documentation.
* Argo CD upstream documentation, RBAC Configuration section.
