---
title: "Configuring a GitHub or GitHub Enterprise identity provider"
type: reference
domain: openshift
slug: authentication-4-22-configuring-github-identity-provider
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/configuring-github-identity-provider
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Configuring a GitHub or GitHub Enterprise identity provider

[id="configuring-github-identity-provider"]
= Configuring a GitHub or GitHub Enterprise identity provider

Configure the `github` identity provider to validate user names and passwords against GitHub or GitHub Enterprise's OAuth authentication server. OAuth facilitates a token exchange flow between OpenShift Container Platform and GitHub or GitHub Enterprise.

You can use the GitHub integration to connect to either GitHub or GitHub Enterprise. For GitHub Enterprise integrations, you must provide the `hostname` of your instance and can optionally provide a `ca` certificate bundle to use in requests to the server.

[NOTE]
====
The following steps apply to both GitHub and GitHub Enterprise unless noted.
====

// Module included in the following assemblies:
//
// * authentication/configuring-identity-provider.adoc
// * authentication/identity_providers/configuring-allow-all-identity-provider.adoc
// * authentication/identity_providers/configuring-deny-all-identity-provider.adoc
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-google-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="identity-provider-overview_{context}"]
= About identity providers in OpenShift Container Platform

By default, only a `kubeadmin` user exists on your cluster. To specify an
identity provider, you must create a custom resource (CR) that describes
that identity provider and add it to the cluster.

[NOTE]
====
OpenShift Container Platform user names containing `/`, `:`, and `%` are not supported.
====

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-github-identity-provider.adoc

[id="identity-provider-github-about_{context}"]
= About GitHub authentication

Configuring GitHub authentication allows users to log in to OpenShift Container Platform with their GitHub credentials. To prevent anyone with any GitHub user ID from logging in to your OpenShift Container Platform cluster, you can restrict access to only those in specific GitHub organizations.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-github-identity-provider.adoc

[id="identity-provider-registering-github_{context}"]
= Registering a GitHub application

To use GitHub or GitHub Enterprise as an identity provider, you must register
an application to use.

.Procedure

. Register an application on GitHub:
** For GitHub, click https://github.com/settings/profile[*Settings*] ->
https://github.com/settings/apps[*Developer settings*] ->
https://github.com/settings/developers[*OAuth Apps*] ->
https://github.com/settings/applications/new[*Register a new OAuth application*].
** For GitHub Enterprise, go to your GitHub Enterprise home page and then click
*Settings -> Developer settings -> Register a new application*.
. Enter an application name, for example `My OpenShift Install`.
. Enter a homepage URL, such as
`\https://oauth-openshift.apps.<cluster-name>.<cluster-domain>`.
. Optional: Enter an application description.
. Enter the authorization callback URL, where the end of the URL contains the
identity provider `name`:
+
----
https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>
----
+
For example:
+
----
https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/github
----
. Click *Register application*. GitHub provides a client ID and a client secret.
You need these values to complete the identity provider configuration.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-google-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc

[id="identity-provider-creating-secret_{context}"]
= Creating the secret

Identity providers use OpenShift Container Platform `Secret` objects in the `openshift-config` namespace to contain the client secret, client certificates, and keys.

.Procedure

* Create a `Secret` object containing a string by using the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> --from-literal=clientSecret=<secret> -n openshift-config
----
+
[TIP]
====
You can alternatively apply the following YAML to create the secret:

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: <secret_name>
  namespace: openshift-config
type: Opaque
data:
  clientSecret: <base64_encoded_client_secret>
----
====

* You can define a `Secret` object containing the contents of a file by using the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> --from-file=<path_to_file> -n openshift-config
----

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc

[id="identity-provider-creating-configmap_{context}"]
= Creating a config map

Identity providers use OpenShift Container Platform `ConfigMap` objects in the `openshift-config`
namespace to contain the certificate authority bundle. These are primarily
used to contain certificate bundles needed by the identity provider.

[NOTE]
====
This procedure is only required for GitHub Enterprise.
====

.Procedure

* Define an OpenShift Container Platform `ConfigMap` object containing the
certificate authority by using the following command. The certificate
authority must be stored in the `ca.crt` key of the `ConfigMap` object.
+
[source,terminal]
----
$ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config
----
+
[TIP]
====
You can alternatively apply the following YAML to create the config map:

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: ca-config-map
  namespace: openshift-config
data:
  ca.crt: |
    <CA_certificate_PEM>
----
====

// Undefining attributes

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-github-identity-provider.adoc

[id="identity-provider-github-CR_{context}"]
= Sample GitHub CR

The following custom resource (CR) shows the parameters and acceptable values for a
GitHub identity provider.

.GitHub CR

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: githubidp <1>
    mappingMethod: claim <2>
    type: GitHub
    github:
      ca: <3>
        name: ca-config-map
      clientID: {...} <4>
      clientSecret: <5>
        name: github-secret
      hostname: ... <6>
      organizations: <7>
      - myorganization1
      - myorganization2
      teams: <8>
      - myorganization1/team-a
      - myorganization2/team-b
----
<1> This provider name is prefixed to the GitHub numeric user ID to form an
identity name. It is also used to build the callback URL.
<2> Controls how mappings are established between this provider's identities and `User` objects.
<3> Optional: Reference to an OpenShift Container Platform `ConfigMap` object containing the
PEM-encoded certificate authority bundle to use in validating server
certificates for the configured URL. Only for use in GitHub Enterprise
with a non-publicly trusted root certificate.
<4> The client ID of a
registered GitHub OAuth
application. The application must be configured with a callback URL of
`\https://oauth-openshift.apps.<cluster-name>.<cluster-domain>/oauth2callback/<idp-provider-name>`.
<5> Reference to an OpenShift Container Platform `Secret` object containing the client secret
issued by GitHub.
<6> For GitHub Enterprise, you must provide the hostname of your instance, such as
`example.com`. This value must match the GitHub Enterprise `hostname` value in
in the `/setup/settings` file and cannot include a port number. If this
value is not set, then either `teams` or `organizations` must be defined.
For GitHub, omit this parameter.
<7> The list of organizations. Either the `organizations` or `teams` field must be set unless the `hostname` field is set, or if `mappingMethod` is set to `lookup`. Cannot be used in combination with the `teams` field.
<8> The list of teams. Either the `teams` or `organizations` field must be set unless the `hostname` field is set, or if `mappingMethod` is set to `lookup`. Cannot be used in combination with the `organizations` field.

[NOTE]
====
If `organizations` or `teams` is specified, only GitHub users that are members of
at least one of the listed organizations will be allowed to log in. If the GitHub OAuth
application configured in `clientID` is not owned by the organization, an organization
owner must grant third-party access to use this option. This can be done during
the first GitHub login by the organization's administrator, or from the GitHub organization settings.
====

// Included here so that it is associated with the above module
[role="_additional-resources"]
.Additional resources

* See Identity provider parameters for information on parameters, such as `mappingMethod`, that are common to all identity providers.

// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-allow-all-identity-provider.adoc
// * authentication/identity_providers/configuring-deny-all-identity-provider.adoc
// * authentication/identity_providers/configuring-htpasswd-identity-provider.adoc
// * authentication/identity_providers/configuring-keystone-identity-provider.adoc
// * authentication/identity_providers/configuring-ldap-identity-provider.adoc
// * authentication/identity_providers/configuring-basic-authentication-identity-provider.adoc
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc
// * authentication/identity_providers/configuring-github-identity-provider.adoc
// * authentication/identity_providers/configuring-gitlab-identity-provider.adoc
// * authentication/identity_providers/configuring-google-identity-provider.adoc
// * authentication/identity_providers/configuring-oidc-identity-provider.adoc

// GitHub and Google IDPs do not support username/password login commands
// Only some OIDC IDPs support username/password login commands

[id="add-identity-provider_{context}"]
= Adding an identity provider to your cluster

After you install your cluster, add an identity provider to it so your
users can authenticate.

.Prerequisites

* Create an OpenShift Container Platform cluster.
* Create the custom resource (CR) for your identity providers.
* You must be logged in as an administrator.

.Procedure

. Apply the defined CR:
+
[source,terminal]
----
$ oc apply -f </path/to/CR>
----
+
[NOTE]
====
If a CR does not exist, `oc apply` creates a new CR and might trigger the following warning: `Warning: oc apply should be used on resources created by either oc create --save-config or oc apply`. In this case you can safely ignore this warning.
====

. Log in to the cluster as a user from your identity provider, entering the
password when prompted.
+
[source,terminal]
----
$ oc login -u <username>
----

. Obtain a token from the OAuth server.
+
As long as the `kubeadmin` user has been removed, the `oc login` command provides instructions on how to access a web page where you can retrieve the token.
+
You can also access this page from the web console by navigating to *(?) Help* -> *Command Line Tools* -> *Copy Login Command*.

. Log in to the cluster, passing in the token to authenticate.
+
[source,terminal]
----
$ oc login --token=<token>
----
+
[NOTE]
====
If your OpenID Connect identity provider supports the resource owner password credentials (ROPC) grant flow, you can log in with a user name and password. You might need to take steps to enable the ROPC grant flow for your identity provider.

After the OIDC identity provider is configured in OpenShift Container Platform, you can log in by using the following command, which prompts for your user name and password:

[source,terminal]
----
$ oc login -u <identity_provider_username> --server=<api_server_url_and_port>
----

This identity provider does not support logging in with a user name and password.
====

. Confirm that the user logged in successfully, and display the user name.
+
[source,terminal]
----
$ oc whoami
----

// Undefining attributes
