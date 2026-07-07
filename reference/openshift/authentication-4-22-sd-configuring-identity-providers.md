---
title: "Identity providers overview"
type: reference
domain: openshift
slug: authentication-4-22-sd-configuring-identity-providers
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/sd-configuring-identity-providers
version: 4.22
family: authentication
documentKind: "Documentation"
---

# Identity providers overview

[id="sd-configuring-identity-providers"]
= Identity providers overview

[role="_abstract"]
After you create your OpenShift Container Platform cluster, configure identity providers so users can log in and access the cluster.

The following topics describe how to configure an identity provider using the {cluster-manager} console. Alternatively, you can use the {rosa-cli-first} to configure an identity provider and access the cluster.

// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc

[id="understanding-idp_{context}"]
= Understanding identity providers

[role="_abstract"]
OpenShift Container Platform includes a built-in OAuth server. Developers and administrators obtain OAuth access tokens to authenticate themselves to the API. As an administrator, you can configure OAuth to specify an identity provider after you install your cluster. Configuring identity providers allows users to log in and access the cluster.

[id="understanding-idp-supported_{context}"]
== Supported identity providers
// This section is sourced from authentication/understanding-identity-provider.adoc

You can configure the following types of identity providers:

[cols="2a,8a",options="header"]
|===

|Identity provider
|Description

|GitHub or GitHub Enterprise
|Configure a GitHub identity provider to validate usernames and passwords against GitHub or GitHub Enterprise's OAuth authentication server.

|GitLab
|Configure a GitLab identity provider to use GitLab.com or any other GitLab instance as an identity provider.

|Google
|Configure a Google identity provider using Google's OpenID Connect integration.

|LDAP
|Configure an LDAP identity provider to validate usernames and passwords against an LDAPv3 server, using simple bind authentication.

|OpenID Connect
|Configure an OpenID Connect (OIDC) identity provider to integrate with an OIDC identity provider using an Authorization Code Flow.

|htpasswd
|Configure an htpasswd identity provider for a single, static administration user. You can log in to the cluster as the user to troubleshoot issues.

[IMPORTANT]
====
The htpasswd identity provider option is included only to enable the creation of a single, static administration user. htpasswd is not supported as a general-use identity provider for OpenShift Container Platform. For the steps to configure the single user, see _Configuring an htpasswd identity provider_.
====

|===
// Module included in the following assemblies:
//
// * authentication/understanding-identity-provider.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="identity-provider-parameters_{context}"]
= Identity provider parameters

[role="_abstract"]
The following parameters are common to all identity providers:

[cols="2a,8a",options="header"]
|===
|Parameter     | Description
|`name`      | The provider name is prefixed to provider user names to form an
identity name.

|`mappingMethod`  | Defines how new identities are mapped to users when they log in.
Enter one of the following values:

claim:: The default value. Provisions a user with the identity's preferred
user name. Fails if a user with that user name is already mapped to another
identity.
lookup:: Looks up an existing identity, user identity mapping, and user,
but does not automatically provision users or identities. This allows cluster
administrators to set up identities and users manually, or using an external
process. Using this method requires you to manually provision users.
add:: Provisions a user with the identity's preferred user name. If a user
with that user name already exists, the identity is mapped to the existing user,
adding to any existing identity mappings for the user. Required when multiple
identity providers are configured that identify the same set of users and map to
the same user names.
|===

[NOTE]
When adding or changing identity providers, you can map identities from the new
provider to existing users by setting the `mappingMethod` parameter to
`add`.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc

[id="config-github-idp_{context}"]
= Configuring a GitHub identity provider

[role="_abstract"]
Configure a GitHub identity provider to validate user names and passwords against GitHub or GitHub Enterprise's OAuth authentication server and access your OpenShift Container Platform cluster. OAuth facilitates a token exchange flow between OpenShift Container Platform and GitHub or GitHub Enterprise.

[WARNING]
====
Configuring GitHub authentication allows users to log in to OpenShift Container Platform with their GitHub credentials. To prevent anyone with any GitHub user ID from logging in to your OpenShift Container Platform cluster, you must restrict access to only those in specific GitHub organizations or teams.
====

.Prerequisites

* The OAuth application must be created directly within the GitHub organization settings by the GitHub organization administrator.
* GitHub organizations or teams are set up in your GitHub account.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that you need to configure identity providers for.

. Click the *Access control* tab.

. Click *Add identity provider*.
+
[NOTE]
====
You can also click the *Add Oauth configuration* link in the warning message displayed after cluster creation to configure your identity providers.
====

. Select *GitHub* from the drop-down menu.

. Enter a unique name for the identity provider. This name cannot be changed later.
** An *OAuth callback URL* is automatically generated in the provided field. You will use this to register the GitHub application.
+
----
https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
+
For example:
+
----
https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/github
----
----
https://oauth.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----

. Register an application on GitHub.

. Return to OpenShift Container Platform and select a mapping method from the drop-down menu. *Claim* is recommended in most cases.

. Enter the *Client ID* and *Client secret* provided by GitHub.

. Enter a *hostname*. A hostname must be entered when using a hosted instance of GitHub Enterprise.

. Optional: You can use a certificate authority (CA) file to validate server certificates for the configured GitHub Enterprise URL. Click *Browse* to locate and attach a *CA file* to the identity provider.

. Select *Use organizations* or *Use teams* to restrict access to a particular GitHub organization or a GitHub team.

. Enter the name of the organization or team you want to restrict access to. Click *Add more* to specify multiple organizations or teams that users can be a member of.

. Click *Confirm*.

.Verification

* The configured identity provider is now visible on the *Access control* tab of the *Cluster List* page.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc

[id="config-gitlab-idp_{context}"]
= Configuring a GitLab identity provider

[role="_abstract"]
Configure a GitLab identity provider to use GitLab.com or any other GitLab instance as an identity provider.

.Prerequisites

- If you use GitLab version 7.7.0 to 11.0, you connect using the OAuth integration. If you use GitLab version 11.1 or later, you can use OpenID Connect (OIDC) to connect instead of OAuth.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that you need to configure identity providers for.

. Click the *Access control* tab.

. Click *Add identity provider*.
+
[NOTE]
====
You can also click the *Add Oauth configuration* link in the warning message displayed after cluster creation to configure your identity providers.
====

. Select *GitLab* from the drop-down menu.

. Enter a unique name for the identity provider. This name cannot be changed later.
** An *OAuth callback URL* is automatically generated in the provided field. You will provide this URL to GitLab.
+
----
https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
----
https://oauth.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
+
For example:
+
----
https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/gitlab
----

. Add a new application in GitLab.

. Return to OpenShift Container Platform and select a mapping method from the drop-down menu. *Claim* is recommended in most cases.

. Enter the *Client ID* and *Client secret* provided by GitLab.

. Enter the *URL* of your GitLab provider.

. Optional: You can use a certificate authority (CA) file to validate server certificates for the configured GitLab URL. Click *Browse* to locate and attach a *CA file* to the identity provider.

. Click *Confirm*.

.Verification

* The configured identity provider is now visible on the *Access control* tab of the *Cluster List* page.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc

[id="config-google-idp_{context}"]
= Configuring a Google identity provider

[role="_abstract"]
Configure a Google identity provider to allow users to authenticate with their Google credentials.

[WARNING]
====
Using Google as an identity provider allows any Google user to authenticate to your server.
You can limit authentication to members of a specific hosted domain with the
`hostedDomain` configuration attribute.
====

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that you need to configure identity providers for.

. Click the *Access control* tab.

. Click *Add identity provider*.
+
[NOTE]
====
You can also click the *Add Oauth configuration* link in the warning message displayed after cluster creation to configure your identity providers.
====

. Select *Google* from the drop-down menu.

. Enter a unique name for the identity provider. This name cannot be changed later.
** An *OAuth callback URL* is automatically generated in the provided field. You will provide this URL to Google.
+
----
https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
----
https://oauth.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
+
For example:
+
----
https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/google
----

. Configure a Google identity provider using Google's OpenID Connect integration.

. Return to OpenShift Container Platform and select a mapping method from the drop-down menu. *Claim* is recommended in most cases.

. Enter the *Client ID* of a registered Google project and the *Client secret* issued by Google.

. Enter a hosted domain to restrict users to a Google Apps domain.

. Click *Confirm*.

.Verification

* The configured identity provider is now visible on the *Access control* tab of the *Cluster List* page.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc

[id="config-ldap-idp_{context}"]
= Configuring a LDAP identity provider

[role="_abstract"]
Configure the LDAP identity provider to validate user names and passwords against an LDAPv3 server, using simple bind authentication.

.Prerequisites

* When configuring a LDAP identity provider, you will need to enter a configured *LDAP URL*. The configured URL is an RFC 2255 URL, which specifies the LDAP host and
search parameters to use. The syntax of the URL is:
+
----
ldap://host:port/basedn?attribute?scope?filter
----
+
[cols="2a,8a",options="header"]
|===
|URL component | Description
.^|`ldap`      | For regular LDAP, use the string `ldap`. For secure LDAP
(LDAPS), use `ldaps` instead.
.^|`host:port` | The name and port of the LDAP server. Defaults to
`localhost:389` for ldap and `localhost:636` for LDAPS.
.^|`basedn`    | The DN of the branch of the directory where all searches should
start from. At the very least, this must be the top of your directory tree, but
it could also specify a subtree in the directory.
.^|`attribute` | The attribute to search for. Although RFC 2255 allows a
comma-separated list of attributes, only the first attribute will be used, no
matter how many are provided. If no attributes are provided, the default is to
use `uid`. It is recommended to choose an attribute that will be unique across
all entries in the subtree you will be using.
.^|`scope`     | The scope of the search. Can be either `one` or `sub`.
If the scope is not provided, the default is to use a scope of `sub`.
.^|`filter`    | A valid LDAP search filter. If not provided, defaults to
`(objectClass=*)`
|===
+
When doing searches, the attribute, filter, and provided user name are combined
to create a search filter that looks like:
+
----
(&(<filter>)(<attribute>=<username>))
----
+
[IMPORTANT]
If the LDAP directory requires authentication to search, specify a `bindDN` and
`bindPassword` to use to perform the entry search.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that you need to configure identity providers for.

. Click the *Access control* tab.

. Click *Add identity provider*.
+
[NOTE]
====
You can also click the *Add Oauth configuration* link in the warning message displayed after cluster creation to configure your identity providers.
====

. Select *LDAP* from the drop-down menu.

. Enter a unique name for the identity provider. This name cannot be changed later.

. Select a mapping method from the drop-down menu. *Claim* is recommended in most cases.

. Enter a *LDAP URL* to specify the LDAP search parameters to use.

. Optional: Enter a *Bind DN* and *Bind password*.

. Enter the attributes that will map LDAP attributes to identities.
** Enter an *ID* attribute whose value should be used as the user ID. Click *Add more* to add multiple ID attributes.
** Optional: Enter a *Preferred username* attribute whose value should be used as the display name. Click *Add more* to add multiple preferred username attributes.
** Optional: Enter an *Email* attribute whose value should be used as the email address. Click *Add more* to add multiple email attributes.

. Optional: Click *Show advanced Options* to add a certificate authority (CA) file to your LDAP identity provider to validate server certificates for the configured URL. Click *Browse* to locate and attach a *CA file* to the identity provider.

. Optional: Under the advanced options, you can choose to make the LDAP provider *Insecure*. If you select this option, a CA file cannot be used.
+
[IMPORTANT]
====
If you are using an insecure LDAP connection (ldap:// or port 389), then you must check the *Insecure* option in the configuration wizard.
====

. Click *Confirm*.

.Verification

* The configured identity provider is now visible on the *Access control* tab of the *Cluster List* page.
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc

[id="config-openid-idp_{context}"]
= Configuring an OpenID identity provider

[role="_abstract"]
Configure an OpenID identity provider to integrate with an OpenID Connect identity provider using an Authorization Code Flow.

[IMPORTANT]
====
The Authentication Operator in OpenShift Container Platform requires that the configured
OpenID Connect identity provider implements the
OpenID Connect Discovery
specification.
====

Claims are read from the JWT `id_token` returned from the OpenID identity
provider and, if specified, from the JSON returned by the Issuer URL.

At least one claim must be configured to use as the user's identity.

You can also indicate which claims to use as the user's preferred user name,
display name, and email address. If multiple claims are specified, the first one
with a non-empty value is used. The standard claims are:

[cols="1,2",options="header"]
|===

|Claim
|Description

|`preferred_username`
|The preferred user name when provisioning a user. A
shorthand name that the user wants to be referred to as, such as `janedoe`. Typically
a value that corresponding to the user's login or username in the authentication
system, such as username or email.

|`email`
|Email address.

|`name`
|Display name.

|===

See the
OpenID claims documentation
for more information.

.Prerequisites
* Before you configure OpenID Connect, check the installation prerequisites for any Red{nbsp}Hat product or service you want to use with your OpenShift Container Platform cluster.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that you need to configure identity providers for.

. Click the *Access control* tab.

. Click *Add identity provider*.
+
[NOTE]
====
You can also click the *Add Oauth configuration* link in the warning message displayed after cluster creation to configure your identity providers.
====

. Select *OpenID* from the drop-down menu.

. Enter a unique name for the identity provider. This name cannot be changed later.
** An *OAuth callback URL* is automatically generated in the provided field.
+
----
https://oauth-openshift.apps.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
----
https://oauth.<cluster_name>.<cluster_domain>/oauth2callback/<idp_provider_name>
----
+
For example:
+
----
https://oauth-openshift.apps.openshift-cluster.example.com/oauth2callback/openid
----

. Register a new OpenID Connect client in the OpenID identity provider by following the steps to create an authorization request.

. Return to OpenShift Container Platform and select a mapping method from the drop-down menu. *Claim* is recommended in most cases.

. Enter a *Client ID* and *Client secret* provided from OpenID.

. Enter an *Issuer URL*. This is the URL that the OpenID provider asserts as the Issuer Identifier. It must use the https scheme with no URL query parameters or fragments.

. Enter an *Email* attribute whose value should be used as the email address. Click *Add more* to add multiple email attributes.

. Enter a *Name* attribute whose value should be used as the preferred username. Click *Add more* to add multiple preferred usernames.

. Enter a *Preferred username* attribute whose value should be used as the display name. Click *Add more* to add multiple display names.

. Optional: Click *Show advanced Options* to add a certificate authority (CA) file to your OpenID identity provider.

. Optional: Under the advanced options, you can add *Additional scopes*. By default, the `OpenID` scope is requested.

. Click *Confirm*.

.Verification

* The configured identity provider is now visible on the *Access control* tab of the *Cluster List* page.
// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc
// * rosa_install_access_delete_clusters/rosa-sts-config-identity-providers.adoc

[id="config-htpasswd-idp_{context}"]
= Configuring an htpasswd identity provider

[role="_abstract"]
Configure an htpasswd identity provider to create static users. You can log in to your cluster as the user to troubleshoot problems. You can use the web user interface (UI) or your command-line interface (CLI) to create an htpasswd identity provider.

[IMPORTANT]
====
The htpasswd identity provider option is included only to create static administration users. htpasswd is not supported as a general-use identity provider for OpenShift Container Platform.
====

// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc

[id="config-htpasswd-idp-webui_{context}"]
= Configuring an htpasswd identity provider

[role="_abstract"]
You can create an htpasswd identity provider with the {cluster-manager} web user interface (UI).

.Procedure

. Select your cluster from the *Cluster List* page on {cluster-manager-url}.

. Select *Access control* -> *Identity providers*.

. Click *Add identity provider*.

. Select *htpasswd* from the *Identity Provider* list.

. Add a unique name in the *Name* field for the identity provider.

. Select *Add users manually*.

. Use the suggested username and password for the static user, or create your own.
+
[NOTE]
====
You cannot retrieve the credentials defined in this step after you select *Add* in the following step. If you lose the credentials, you must re-create the identity provider and define the credentials again.
====

. You can create a single user account or you can create multiple user accounts:
** Select *Add* to create the htpasswd identity provider and the single, static user.
** Select *Add user* to create another username and password field. When you select *Add*, you create all of the users in the users list.

.Verification

* You can see your configured htpasswd identity provider on the *Access control* -> *Identity providers* page.
+
[NOTE]
====
After creating the identity provider, synchronization usually completes within two minutes. You can log in to the cluster as the user after the htpasswd identity provider becomes available.
====
// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc

[id="config-htpasswd-idp-from-file_{context}"]
= Configuring an htpasswd identity provider by using the file upload

[role="_abstract"]
You can create an htpasswd identity provider by uploading a user file in the {cluster-manager} web user interface (UI).

[NOTE]
====
Ensure that you correctly hashed your htpasswd file by using the htpasswd tool to create this file.
====

.Procedure

. Select your cluster from the *Cluster List* page on {cluster-manager-url}.

. Select *Access control* -> *Identity providers*.

. Click *Add identity provider*.

. Select *htpasswd* from the *Identity Provider* list.

. Add a unique name in the *Name* field for the identity provider.

. Select *Upload an htpasswd file*.

. In the *htpasswd file* field, drag your configured htpasswd file or select *Browse* to locate the file on your local drive.

. Select *Add* to create the htpasswd identity provider and add the users from the uploaded file.

.Verification

* You can see your configured htpasswd identity provider on the *Access control* -> *Identity providers* page.
+
[NOTE]
====
After creating the identity provider, synchronization usually completes within two minutes. You can log in to the cluster as the user after the htpasswd identity provider becomes available.
====
// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc

[id="rosa-config-htpasswd-idp-cli_{context}"]
= Configuring an htpasswd identity provider with the CLI

[role="_abstract"]
You can create an htpasswd identity provider (IDP) with the {rosa-cli-first} tool.

.Prerequisites

* You have installed and configured the latest version of the {rosa-cli}.

.Procedure

* Run the following command to create an htpasswd IDP by passing the usernames and passwords in the command-line interface:
+
[source,terminal]
----
$ rosa create idp --type=htpasswd -c  <cluster_name> --users='user1:password1,user2:password2,user3:password3'
----
+
[NOTE]
====
The `--users` string value must be a comma separated list of `username:password,` within quotes like `"user1:password"` to create a user account with a name of `user1` and a password of `password`. The quotes prevent your password from disrupting the Bash commands.

Passwords must include uppercase letters, lowercase letters, and numbers or symbols, specifically, ASCII-standard characters only. The password must be at least 14 characters.
====
// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc

[id="rosa-config-htpasswd-idp-cli-file_{context}"]
= Configuring an htpasswd identity provider with an htpasswd file

[role="_abstract"]
You can create an htpasswd identity provider (IDP) with the {rosa-cli-first} tool and a well-formed htpasswd file.

.Prerequisites

* You have installed and configured the latest version of the {rosa-cli}.

.Procedure

* Create a text file with a new row for each set of credentials with the username and password being colon separated like the following example:
+
[source,text]
----
johndoe:$apr1$hRY7OJWH$km1EYH.UIRj00000000/
janedoe:$apr1$Q58SO804$B/fECNWfn5F00000000/
----
+
[NOTE]
====
The htpasswd file is encrypted using APR1 hashing. For more information, see "Apache Password Formats" in the _Additional resources_.
====
+
[source,terminal]
----
$ rosa create idp --type=htpasswd -c <cluster_name> --from-file=myhtpassfile.txt
----

// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc
// * rosa_hcp/terraform/rosa-hcp-creating-a-cluster-quickly-terraform.adoc

[id="config-htpasswd-idp-terraform_{context}"]
= Configuring an htpasswd identity provider with Terraform

[role="_abstract"]
After creating your cluster with Terraform, you can permit users access to your cluster by using an htpasswd identity provider (IDP) with the Terraform tool.
[role="_abstract"]
You can create an htpasswd identity provider (IDP) with Terraform.

.Prerequisites

* You have installed and configured the latest version of the {rosa-cli}.
* You have installed and configured the latest version of Terraform.

.Procedure
. Grant permissions to your account by using an offline {cluster-manager-first} token.
. Copy your offline token, and set the token as an environmental variable by running the following command:
+
[source,terminal]
----
$ export RHCS_TOKEN=<your_offline_token>
----
+
[NOTE]
====
This environmental variable resets at the end of each session, such as restarting your machine or closing the terminal.
====

. Create the `htpasswd_idp.tf` file by running one of the following commands:
+
** *Option 1*: To create a user with a generated, randomized password, run:
+
[source,terminal]
----
$ cat<<-EOF>htpasswd_idp.tf
  module "htpasswd_idp" {
    source = "terraform-redhat/rosa-hcp/rhcs//modules/idp"
    version = "1.6.2"

    cluster_id         = "2odpb9p344hnkfvpkluo00qmgkika78l"
    name               = "htpasswd-idp-tf-1"
    idp_type           = "htpasswd"
    htpasswd_idp_users = [{ username = "pej-user-d1", password = random_password.password.result }]
  }

  resource "aws_secretsmanager_secret" "idp_password" {
  name        = "idp-password-secret"
  description = "Any description here"
  }

  resource "random_password" "password" {
      length           = 16
      lower            = true
      special          = true
      override_special = "!#$%&*()-_=+[]{}<>:?"
  }

  # If you need to output the password, mark it as sensitive to hide from CLI logs
  output "password_output" {
      value     = random_password.password.result
      sensitive = true
  }

  # This section sends your credentials to your AWS Secrets Manager to enable you to log in to your cluster.
  resource "aws_secretsmanager_secret_version" "idp_password_val" {
  secret_id     = aws_secretsmanager_secret.idp_password.id
  secret_string = random_password.password.result
  }
EOF
----
+
You must replace the `<cluster_id>` placeholder with the 32-digit ID for your cluster. To find that value, run `rosa list clusters | awk '{print $1}'`. You also must replace the `<user_name>` placeholder with the username you want to create. The randomized password is then stored in your AWS Secrets manager to be used when logging in to the cluster.

*** Run the following command to view your password after setting it:
+
[source,terminal]
----
$ terraform output password_output
----
+
The CLI returns your generated password in plain text.

** *Option 2*: To specify your passwords when creating a user, run:
+
[source,terminal]
----
$ cat<<-EOF>htpasswd_idp.tf
  module "htpasswd_idp" {
    source = "terraform-redhat/rosa-hcp/rhcs//modules/idp"
    version = "1.6.2"

    cluster_id         = "<cluster_id>"
    name               = "htpasswd-idp"
    idp_type           = "htpasswd"
    htpasswd_idp_users = [{ username="<user_name>",password="<password>"}]
  }
EOF
----
+
You must replace the `<cluster_id>` placeholder with the 32-digit ID for your cluster. To find that value, run `rosa list clusters | awk '{print $1}'`. You also must replace the `<user_name>` placeholder with the username you want to create as well as a password for the `<password>` placeholder.

. Run the following command to configure Terraform to create your resources based on your Terraform files:
+
[source,terminal]
----
$ terraform init
----

. Verify that the Terraform you copied is correct by running the following command:
+
[source,terminal]
----
$ terraform validate
----
+
.Example output
[source,terminal]
----
Success! The configuration is valid.
----

. Create your cluster with Terraform by running the following command:
+
[source,terminal]
----
$ terraform apply
----

. Enter `yes` to proceed or `no` to cancel when the Terraform interface lists the resources to be created or changed and prompts for confirmation:
+
[source,terminal]
----
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes
----
+
You see a confirmation that your IDP has been created.
+
[source,terminal]
----
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
----
+
[NOTE]
====
If you used the randomized password template, then the generated password is stored in your AWS Secrets manager.
====

// Module included in the following assemblies:
//
// * authentication/sd-configuring-identity-providers.adoc

[id="sd-config-htpasswd-idp-cli_{context}"]
= Configuring an htpasswd identity provider with the CLI

[role="_abstract"]
You can create an htpasswd identity provider (IDP) with the OCM CLI (`ocm`) tool.

.Prerequisites

* You have installed and configured the latest version of the OCM CLI (`ocm`).

.Procedure

* Run the following command to create an htpasswd IDP by passing the usernames and passwords in the command-line interface:
+
[source,terminal]
----
$ ocm create idp --type htpasswd --cluster <cluster_name> --name <idp_name> --username <user_name> --password '<password>'
----
+
[NOTE]
====
You must include the password within quotes like `'password'` to prevent your password from disrupting the Bash commands.

Passwords must include uppercase letters, lowercase letters, and numbers or symbols, specifically, ASCII-standard characters only. The password must be at least 14 characters.
====
// Module included in the following assemblies:
//
// * osd_install_access_delete_cluster/config-identity-providers.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="access-cluster_{context}"]
= Accessing your cluster

[role="_abstract"]
After you have configured your identity providers, users can access the cluster from {cluster-manager-first}.

.Prerequisites

* You logged in to {cluster-manager-url}.
* You created an OpenShift Container Platform cluster.
* You configured an identity provider for your cluster.
* You added your user account to the configured identity provider.

.Procedure

. From {cluster-manager-url}, select the cluster you want to access.

. Click *Open console* to open the web console for your cluster.

. Select your identity provider and enter your credentials to log in to the cluster. Complete any authorization requests from your provider.

[id="additional-resources-cluster-access-sts"]
[role="_additional-resources"]
== Additional resources
* Accessing a cluster
* Understanding the ROSA with STS deployment workflow
* Apache Password Formats
* Google's OpenID Connect integration
* Authorization Code Flow
