---
title: "Comprehensive guide to getting started with {product-title}"
type: reference
domain: openshift
slug: rosa-getting-started-4-22-rosa-getting-started
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_getting_started/rosa-getting-started
version: 4.22
family: rosa_getting_started
documentKind: "Documentation"
---

# Comprehensive guide to getting started with {product-title}

[id="rosa-getting-started"]
= Comprehensive guide to getting started with OpenShift Container Platform

[role="_abstract"]
Create a OpenShift Container Platform cluster, grant user access, deploy your first application, revoke user access, and delete your cluster.

[NOTE]
====
If you need a quick start guide, see the OpenShift Container Platform quick start guide.
====

You can create a OpenShift Container Platform cluster that uses AWS Security Token Service (STS).

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc

[id="rosa-getting-started-prerequisites_{context}"]
= Prerequisites

[role="_abstract"]
* You reviewed the introduction to OpenShift Container Platform, and the documentation on OpenShift Container Platform architecture models and architecture concepts.

* You have read the documentation on the guidelines for planning your environment.
// Removed as part of OSDOCS-13310, until figures are verified.
//limits and scalability and

* You have reviewed the detailed AWS prerequisites for OpenShift Container Platform with STS.

* You have the AWS service quotas required to run a OpenShift Container Platform cluster.

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc

[id="rosa-getting-started-environment-setup_{context}"]
= Set up environment for cluster creation

[role="_abstract"]
Before you create a OpenShift Container Platform cluster, you must configure your environment.

You must complete the following tasks:

* Verify OpenShift Container Platform prerequisites against your AWS and Red{nbsp}Hat accounts.
* Install and configure the required command-line interface (CLI) tools.
* Verify the configuration of the CLI tools.
// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-verifying-rosa-prerequisites_{context}"]
= Verify OpenShift Container Platform prerequisites

[role="_abstract"]
You can enable OpenShift Container Platform in your AWS account by verifying prerequisites in the AWS Management Console.

.Prerequisites

* You have a Red{nbsp}Hat account.
* You have an AWS account.
+
[NOTE]
====
Consider using a dedicated AWS account to run production clusters. If you are using AWS Organizations, you can use an AWS account within your organization or create a new one.
====

.Procedure

. Sign in to the https://console.aws.amazon.com/rosa/home[AWS Management Console].

. Navigate to the ROSA service.

. Click *Get started*.
+
The *Verify ROSA prerequisites* page opens.

. Under *ROSA enablement*, ensure that a checkmark and `You previously enabled ROSA` are displayed.
+
If not, follow these steps:

.. Select the checkbox beside `I agree to share my contact information with Red{nbsp}Hat`.
.. Click *Enable ROSA*.
+
After a short wait, a checkmark and `You enabled ROSA` message are displayed.

. Under *Service Quotas*, ensure that a checkmark and `Your quotas meet the requirements for ROSA` are displayed.
+
If you see `Your quotas don't meet the minimum requirements`, take note of the quota type and the minimum listed in the error message. See the Amazon documentation on requesting a quota increase for guidance. It might take several hours for Amazon to approve your quota request.

. Under *ELB service-linked role*, ensure that a checkmark and `AWSServiceRoleForElasticLoadBalancing already exists` are displayed.

. Click *Continue to Red{nbsp}Hat*.
+
The *Get started with OpenShift Container Platform (ROSA)* page opens in a new tab. You have already completed Step 1 on this page, and can now continue with Step 2.

.Verification

* Go to the {cluster-manager-url} to verify that your AWS account is associated with your Red{nbsp}Hat organization.

[role="_additional-resources"]
.Additional resources
* Troubleshoot Red{nbsp}Hat OpenShift Service on AWS enablement errors
// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_planning/rosa-sts-setting-up-environment.adoc

[id="rosa-getting-started-install-configure-cli-tools_{context}"]
= Install and configure the required CLI tools

[role="_abstract"]
Several command-line interface (CLI) tools are required to deploy and work with your cluster.

.Prerequisites

* You have an AWS account.
* You have a Red{nbsp}Hat account.

.Procedure

. Log in to your Red{nbsp}Hat and AWS accounts to access the download page for each required tool.
.. Log in to your Red{nbsp}Hat account at console.redhat.com.
.. Log in to your AWS account at aws.amazon.com.
. Install and configure the latest AWS CLI (`aws`).
.. Install the AWS CLI by following the AWS Command Line Interface documentation appropriate for your workstation.
.. Configure the AWS CLI by specifying your `aws_access_key_id`, `aws_secret_access_key`, and `region` in the `.aws/credentials` file. For more information, see AWS Configuration basics in the AWS documentation.
+
[NOTE]
====
Optional: Use the `AWS_DEFAULT_REGION` environment variable to set the default AWS region.
====
.. Query the AWS API to verify if the AWS CLI is installed and configured correctly:
+
[source,terminal]
----
$ aws sts get-caller-identity  --output text
----
+
For example:
+
[source,terminal]
----
<aws_account_id>    arn:aws:iam::<aws_account_id>:user/<username>  <aws_user_id>
----
+
. Install and configure the latest {rosa-cli}.
.. Navigate to *Downloads*.
.. Find *Red Hat OpenShift Service on AWS command line interface (`rosa`)* in the list of tools and click *Download*.
+
The `rosa-linux.tar.gz` file is downloaded to your default download location.
.. Extract the `rosa` binary file from the downloaded archive. The following example extracts the binary from a Linux tar archive:
+
[source,terminal]
----
$ tar xvf rosa-linux.tar.gz
----
.. Move the `rosa` binary file to a directory in your execution path. In the following example, the `/usr/local/bin` directory is included in the path of the user:
+
[source,terminal]
----
$ sudo mv rosa /usr/local/bin/rosa
----
.. Verify that the {rosa-cli} is installed correctly by querying the `rosa` version:
+
[source,terminal]
----
$ rosa version
----
+
For example:
+
[source,terminal,subs="attributes+"]
----
1.2.47
Your {rosa-cli} is up to date.
----

. Log in to the {rosa-cli} using an offline access token.
.. Run the login command:
+
[source,terminal]
----
$ rosa login
----
+
For example:
+
[source,terminal]
----
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa
? Copy the token and paste it here:
----
.. Navigate to the URL listed in the command output to view your offline access token.
.. Enter the offline access token at the command-line prompt to log in.
+
[source,terminal]
----
? Copy the token and paste it here: *******************
[full token length omitted]
----
+
[NOTE]
====
In the future you can specify the offline access token by using the `--token="<offline_access_token>"` argument when you run the `rosa login` command.
====
.. Verify that you are logged in and confirm that your credentials are correct before proceeding:
+
[source,terminal]
----
$ rosa whoami
----
+
For example:
+
[source,terminal]
----
AWS Account ID:               <aws_account_number>
AWS Default Region:           us-east-1
AWS ARN:                      arn:aws:iam::<aws_account_number>:user/<aws_user_name>
OCM API:                      https://api.openshift.com
OCM Account ID:               <red_hat_account_id>
OCM Account Name:             Your Name
OCM Account Username:         you@domain.com
OCM Account Email:            you@domain.com
OCM Organization ID:          <org_id>
OCM Organization Name:        Your organization
OCM Organization External ID: <external_org_id>
----
. Install and configure the latest OpenShift CLI (`oc`).
.. Use the {rosa-cli} to download the `oc` CLI.
+
The following command downloads the latest version of the CLI to the current working directory:
+
[source,terminal]
----
$ rosa download openshift-client
----
.. Extract the `oc` binary file from the downloaded archive. The following example extracts the files from a Linux tar archive:
+
[source,terminal]
----
$ tar xvf openshift-client-linux.tar.gz
----
.. Move the `oc` binary to a directory in your execution path. In the following example, the `/usr/local/bin` directory is included in the path of the user:
+
[source,terminal]
----
$ sudo mv oc /usr/local/bin/oc
----
.. Verify that the `oc` CLI is installed correctly:
+
[source,terminal]
----
$ rosa verify openshift-client
----
+
For example:
+
[source,terminal]
----
I: Verifying whether OpenShift command-line tool is available...
I: Current OpenShift Client Version: 4.17.3
----

.Verification

* Verify the installation of each CLI tool:
+
[source,terminal]
----
$ rosa version
$ aws --version
$ oc version
----

[role="_additional-resources"]
.Additional resources

* AWS Command Line Interface documentation
* Getting started with the OpenShift CLI

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc

[id="rosa-getting-started-creating-a-cluster_{context}"]
= Creating a OpenShift Container Platform cluster with STS

[role="_abstract"]
Choose from one of the following methods to deploy a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS). In each scenario, you can deploy your cluster by using {cluster-manager-first} or the {rosa-cli} (`rosa`):

* *Creating a OpenShift Container Platform cluster with STS using the default options*: You can create a OpenShift Container Platform cluster with STS quickly by using the default options and automatic STS resource creation.

* *Creating a OpenShift Container Platform cluster with STS using customizations*: You can create a OpenShift Container Platform cluster with STS using customizations. You can also choose between the `auto` and `manual` modes when creating the required STS resources.

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-create-cluster-admin-user_{context}"]
= Create a cluster administrator user for quick cluster access

[role="_abstract"]
Before configuring an identity provider, you can create a user with `cluster-admin` privileges for immediate access to your OpenShift Container Platform cluster.

[NOTE]
====
The cluster administrator user is useful when you need quick access to a newly deployed cluster. However, consider configuring an identity provider and granting cluster administrator privileges to the identity provider users as required. For more information about setting up an identity provider for your OpenShift Container Platform cluster, see _Configuring an identity provider and granting cluster access_.
====

.Prerequisites

* You have an AWS account.
* You installed and configured the latest {rosa-cli}, `rosa`, on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.

.Procedure

. Create a cluster administrator user, replacing `<cluster_name>` with the name of your cluster:
+
[source,terminal]
----
$ rosa create admin --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
W: It is recommended to add an identity provider to login to this cluster. See 'rosa create idp --help' for more information.
I: Admin account has been added to cluster '<cluster_name>'.
I: Please securely store this generated password. If you lose this password you can delete and recreate the cluster admin user.
I: To login, run the following command:

   oc login https://api.example-cluster.wxyz.p1.openshiftapps.com:6443 --username cluster-admin --password d7Rca-Ba4jy-YeXhs-WU42J

I: It may take up to a minute for the account to become active.
----
+
[NOTE]
====
It might take approximately one minute for the `cluster-admin` user to become active.
====

. Log in to the cluster through the CLI by running the command provided in the output of the preceding step, replacing `<api_url>` and `<cluster_admin_password>` with the API URL and cluster administrator password for your environment:
+
[source,terminal]
----
$ oc login <api_url> --username cluster-admin --password <cluster_admin_password>
----

. Log in to the cluster through the {cluster-manager} {hybrid-console-second}:
.. Navigate to {cluster-manager-url} and select your cluster.
.. In your cluster, click *Open console*.
.. Under the _Log in with..._ prompt, click *Cluster-Admin*.
.. Enter your credentials.
.. Click *Log in*.

.Verification

* Verify that you are logged in as the cluster administrator:
+
[source,terminal]
----
$ oc whoami
----
+
.Example output
[source,terminal]
----
cluster-admin
----

* Verify that you can access the web console with the cluster administrator credentials.

[role="_additional-resources"]
.Additional resources

* Understanding authentication
* Understanding identity provider configuration
* Cluster administration role

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-configure-an-idp-and-grant-access_{context}"]
= Identity provider configuration and cluster access

[role="_abstract"]
OpenShift Container Platform includes a built-in OAuth server. After your OpenShift Container Platform cluster is created, you must configure OAuth to use an identity provider. You can then add members to your configured identity provider to grant them access to your cluster.

You can also grant the identity provider users with `cluster-admin` or `dedicated-admin` privileges as required.
// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-configure-an-idp_{context}"]
= Configure an identity provider

[role="_abstract"]
You can configure different identity provider types for your OpenShift Container Platform  cluster. Supported types include GitHub, GitHub Enterprise, GitLab, Google, LDAP, OpenID Connect and htpasswd identity providers.

[IMPORTANT]
====
The htpasswd identity provider option is included only to enable the creation of a single, static administration user. htpasswd is not supported as a general-use identity provider for OpenShift Container Platform.
====

The following procedure configures a GitHub identity provider as an example.

.Prerequisites

* You have an AWS account.
* You installed and configured the latest {rosa-cli}, `rosa`, on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.
* You have a GitHub user account.

.Procedure

. Go to github.com and log in to your GitHub account.

. If you do not have an existing GitHub organization to use for identity provisioning for your OpenShift Container Platform cluster, create one. Follow the steps in the GitHub documentation.

. Configure a GitHub identity provider for your cluster that is restricted to the members of your GitHub organization.
.. Configure an identity provider using the interactive mode, replacing `<cluster_name>` with the name of your cluster:
+
[source,terminal]
----
$ rosa create idp --cluster=<cluster_name> --interactive
----
+
The following example output prompts you to enter information about your GitHub organization, replacing `<github_org_name>` with the name of your GitHub organization:
+
.Example output
[source,terminal]
----
I: Interactive mode enabled.
Any optional fields can be left empty and a default will be selected.
? Type of identity provider: github
? Identity provider name: github-1
? Restrict to members of: organizations
? GitHub organizations: <github_org_name>
? To use GitHub as an identity provider, you must first register the application:
  - Open the following URL:
    https://github.com/organizations/<github_org_name>/settings/applications/new?oauth_application%5Bcallback_url%5D=https%3A%2F%2Foauth-openshift.apps.<cluster_name>/<random_string>.p1.openshiftapps.com%2Foauth2callback%2Fgithub-1&oauth_application%5Bname%5D=<cluster_name>&oauth_application%5Burl%5D=https%3A%2F%2Fconsole-openshift-console.apps.<cluster_name>/<random_string>.p1.openshiftapps.com
  - Click on 'Register application'
...
----
.. Follow the URL in the output and select *Register application* to register a new OAuth application in your GitHub organization. By registering the application, you enable the OAuth server that is built into OpenShift Container Platform to authenticate members of your GitHub organization into your cluster.
+
[NOTE]
====
The fields in the *Register a new OAuth application* GitHub form are automatically filled with the required values through the URL defined by the {rosa-cli}.
====
.. Use the information from your GitHub OAuth application page to populate the remaining `rosa create idp` interactive prompts, replacing `<github_client_id>` with the client ID for your GitHub OAuth application and `<github_client_secret>` with a client secret for your GitHub OAuth application. Specify `claim` as the mapping method:
+
.Continued example output
[source,terminal]
----
...
? Client ID: <github_client_id>
? Client Secret: [? for help] <github_client_secret>
? GitHub Enterprise Hostname (optional):
? Mapping method: claim
I: Configuring IDP for cluster '<cluster_name>'
I: Identity Provider 'github-1' has been created.
   It will take up to 1 minute for this configuration to be enabled.
   To add cluster administrators, see 'rosa grant user --help'.
   To login into the console, open https://console-openshift-console.apps.<cluster_name>.<random_string>.p1.openshiftapps.com and click on github-1.
----
+
[NOTE]
====
It might take approximately two minutes for the identity provider configuration to become active. If you have configured a `cluster-admin` user, you can watch the OAuth pods redeploy with the updated configuration by running `oc get pods -n openshift-authentication --watch`.
====

.Verification

* Verify that the identity provider has been configured:
+
[source,terminal]
----
$ rosa list idps --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
NAME        TYPE      AUTH URL
github-1    GitHub    https://oauth-openshift.apps.<cluster_name>.<random_string>.p1.openshiftapps.com/oauth2callback/github-1
----

[role="_additional-resources"]
.Additional resources

* Understanding identity provider configuration
* GitHub OAuth apps documentation
* Configuring identity providers for STS

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-grant-user-access_{context}"]
= Grant user access to a cluster

[role="_abstract"]
You can grant a user access to your OpenShift Container Platform cluster by adding them to your configured identity provider.

You can configure different types of identity providers for your OpenShift Container Platform cluster. The following example procedure adds a user to a GitHub organization that is configured for identity provision to the cluster.

.Prerequisites

* You have an AWS account.
* You installed and configured the latest {rosa-cli} on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.
* You have a GitHub user account.
* You have configured a GitHub identity provider for your cluster.

.Procedure

. Go to github.com and log in to your GitHub account.

. Invite users that require access to the OpenShift Container Platform cluster to your GitHub organization. Follow the steps in Inviting users to join your organization in the GitHub documentation.

.Verification

* Verify that the user was granted access:
+
[source,terminal]
----
$ rosa list users --cluster=<cluster_name>
----

[role="_additional-resources"]
.Additional resources

* Customer administrator user
* Using RBAC to define and apply permissions

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-grant-admin-privileges_{context}"]
= Grant administrator privileges to a user

[role="_abstract"]
After you have added a user to your configured identity provider, you can grant the user `cluster-admin` or `dedicated-admin` privileges for your OpenShift Container Platform cluster.

.Prerequisites

* You have an AWS account.
* You installed and configured the latest {rosa-cli}, `rosa`, on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.
* You have configured a GitHub identity provider for your cluster and added identity provider users.

.Procedure

* To configure `cluster-admin` privileges for an identity provider user, grant the user `cluster-admin` privileges:
+
[source,terminal]
----
$ rosa grant user cluster-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
I: Granted role 'cluster-admins' to user '<idp_user_name>' on cluster '<cluster_name>'
----

* To configure `dedicated-admin` privileges for an identity provider user, grant the user `dedicated-admin` privileges:
+
[source,terminal]
----
$ rosa grant user dedicated-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
I: Granted role 'dedicated-admins' to user '<idp_user_name>' on cluster '<cluster_name>'
----

.Verification

* Verify that the user is listed as a member of the appropriate group:
+
[source,terminal]
----
$ rosa list users --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
ID                 GROUPS
<idp_user_name>    cluster-admins
----
+
Or for `dedicated-admin`:
+
[source,terminal]
----
ID                 GROUPS
<idp_user_name>    dedicated-admins
----

[role="_additional-resources"]
.Additional resources

* Cluster administration role
* Using RBAC to define and apply permissions

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-access-cluster-web-console_{context}"]
= Access a cluster through the web console

[role="_abstract"]
After creating a cluster administrator or adding a user to your identity provider, you can log in to your OpenShift Container Platform cluster through the web console.

.Prerequisites

* You have an AWS account.
* You installed and configured the latest {rosa-cli}, `rosa`, on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.
* You have created a cluster administrator user or added your user account to the configured identity provider.

.Procedure

. Obtain the console URL for your cluster:
+
[source,terminal]
----
$ rosa describe cluster -c <cluster_name> | grep Console
----
+
.Example output
[source,terminal]
----
Console URL:                https://console-openshift-console.apps.example-cluster.wxyz.p1.openshiftapps.com
----

. Go to the console URL in the output of the preceding step and log in.
+
* If you created a `cluster-admin` user, log in by using the provided credentials.
* If you configured an identity provider for your cluster, select the identity provider name in the *Log in with...* dialog and complete any authorization requests from your provider.

.Verification

* Verify that you can access the OpenShift Container Platform web console and view cluster resources.

[role="_additional-resources"]
.Additional resources

* Accessing the web console
* Understanding identity provider configuration

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * osd_getting_started/osd-getting-started.adoc

[id="deploy-app_{context}"]
= Deploy an application from the Developer Catalog

[role="_abstract"]
From the OpenShift Container Platform web console, you can deploy a test application from the Developer Catalog and expose it with a route.

.Prerequisites

* You logged in to the {hybrid-console-url}.
* You created a OpenShift Container Platform cluster.
* You configured an identity provider for your cluster.
* You added your user account to the configured identity provider.

.Procedure

. Go to the *Cluster List* page in {cluster-manager-url}, click the options icon (&#8942;) next to your cluster, and select *Open console*. Log in to your Red{nbsp}Hat account with your configured identity provider credentials.

. In the *Administrator* perspective, select *Home* -> *Projects* -> *Create Project*, enter a name for your project, and click *Create*. Optional: Add a *Display Name* and *Description*.

. Switch to the *Developer* perspective and select *+Add*. Verify that the selected *Project* is the one you created.

. In the *Developer Catalog* dialog, select *All services*, then select *Languages* -> *JavaScript* from the menu and click *Node.js*.
+
[NOTE]
====
You might need to click *Clear All Filters* to display the *Node.js* option.
====

. To open the *Create Source-to-Image application* page, click *Create*.

. In the *Git* section, click *Try sample*, add a unique name in the *Name* field, and confirm that *Deployment* and *Create a route* are selected.

. Click *Create* to deploy the application. It takes a few minutes for the pods to deploy.

. Optional: Monitor the deployment status in the *Topology* pane by selecting your *Node.js* app and reviewing its sidebar. Wait for the `nodejs` build to complete and for the `nodejs` pod to be in a *Running* state.

. Access the deployed application by clicking the route URL, which has a format similar to:
+
----
https://nodejs-<project>.<cluster_name>.<hash>.<region>.openshiftapps.com/
----
+
A new browser tab opens displaying a message similar to:
+
----
Welcome to your Node.js application on OpenShift
----

. Optional: In the *Administrator* perspective, navigate to *Home* -> *Projects*, click the action menu for your project, and select *Delete Project* to clean up resources.

.Verification

* Verify that the application is running:
+
[source,terminal]
----
$ oc get pods -n <project_name>
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS      RESTARTS   AGE
nodejs-1-build             0/1     Completed   0          5m
nodejs-5d9c6c7d9c-kghq2   1/1     Running     0          2m
----

* Access the application route to verify it responds correctly.

[role="_additional-resources"]
.Additional resources

* Creating applications by using the CLI
* Creating applications by using the web console
* Understanding deployments

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-revoking-admin-privileges-and-user-access_{context}"]
= Revoking administrator privileges and user access

[role="_abstract"]
You can revoke `cluster-admin` or `dedicated-admin` privileges from a user by using the {rosa-cli}, `rosa`.

To revoke cluster access from a user, you must remove the user from your configured identity provider.
// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-revoke-admin-privileges_{context}"]
= Revoke administrator privileges from a user

[role="_abstract"]
You can revoke `cluster-admin` or `dedicated-admin` privileges from a user by using the {rosa-cli-first}.

.Prerequisites

* You installed and configured the latest {rosa-cli}, `rosa`, on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.
* You have configured a GitHub identity provider for your cluster and added an identity provider user.
* You granted `cluster-admin` or `dedicated-admin` privileges to a user.

.Procedure

* To revoke `cluster-admin` privileges from an identity provider user, revoke the `cluster-admin` privilege:
+
[source,terminal]
----
$ rosa revoke user cluster-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
? Are you sure you want to revoke role cluster-admins from user <idp_user_name> in cluster <cluster_name>? Yes
I: Revoked role 'cluster-admins' from user '<idp_user_name>' on cluster '<cluster_name>'
----

* To revoke `dedicated-admin` privileges from an identity provider user, revoke the `dedicated-admin` privilege:
+
[source,terminal]
----
$ rosa revoke user dedicated-admin --user=<idp_user_name> --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
? Are you sure you want to revoke role dedicated-admins from user <idp_user_name> in cluster <cluster_name>? Yes
I: Revoked role 'dedicated-admins' from user '<idp_user_name>' on cluster '<cluster_name>'
----

.Verification

* Verify that the user is not listed as a member of the group:
+
[source,terminal]
----
$ rosa list users --cluster=<cluster_name>
----
+
.Example output
[source,terminal]
----
W: There are no users configured for cluster '<cluster_name>'
----

[role="_additional-resources"]
.Additional resources

* Cluster administration role
* Using RBAC to define and apply permissions

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc

[id="rosa-getting-started-revoke-user-access_{context}"]
= Revoke user access to a cluster

[role="_abstract"]
You can revoke cluster access for an identity provider user by removing them from your configured identity provider.

You can configure different types of identity providers for your OpenShift Container Platform cluster. The following example procedure revokes cluster access for a member of a GitHub organization that is configured for identity provision to the cluster.

.Prerequisites

* You have a OpenShift Container Platform cluster.
* You have a GitHub user account.
* You have configured a GitHub identity provider for your cluster and added an identity provider user.

.Procedure

. Go to github.com and log in to your GitHub account.

. Remove the user from your GitHub organization. Follow the steps in Removing a member from your organization in the GitHub documentation.

.Verification

* Verify that the user no longer appears in the cluster users list:
+
[source,terminal]
----
$ rosa list users --cluster=<cluster_name>
----
+
The revoked user should not be displayed in the output.

[role="_additional-resources"]
.Additional resources

* Revoking access to a cluster
* Managing membership in your GitHub organization

// Module included in the following assemblies:
//
// * rosa_getting_started/rosa-getting-started.adoc
// * rosa_getting_started/rosa-quickstart-guide-ui.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc

[id="rosa-getting-started-deleting-a-cluster_{context}"]

= Delete a OpenShift Container Platform cluster and the AWS IAM STS resources

[role="_abstract"]
You can use the {rosa-cli} to delete a OpenShift Container Platform cluster, the AWS Identity and Access Management (IAM) account-wide roles, the cluster-specific Operator roles, and the OpenID Connect (OIDC) provider. To delete the account-wide and Operator policies, use the AWS IAM Console or the AWS CLI.
You can use the {rosa-cli} to delete a OpenShift Container Platform cluster that uses AWS Security Token Service (STS), the AWS Identity and Access Management (IAM) account-wide roles, cluster-specific Operator roles, and the OpenID Connect (OIDC) provider. To delete account-wide inline and Operator policies, use the AWS IAM Console or AWS CLI.

[IMPORTANT]
====
Account-wide IAM roles and policies might be used by other OpenShift Container Platform clusters in the same AWS account. You must only remove the resources if they are not required by other clusters.
====

.Prerequisites

* You installed and configured the latest {rosa-cli} on your workstation.
* You logged in to your Red{nbsp}Hat account using the {rosa-cli}.
* You created a OpenShift Container Platform cluster.

.Procedure

. Delete a cluster and watch the logs, replacing `<cluster_name>` with the name or ID of your cluster:
+
[source,terminal]
----
$ rosa delete cluster --cluster=<cluster_name> --watch
----
+
[IMPORTANT]
====
You must wait for the cluster deletion to complete before you remove the IAM roles, policies, and OIDC provider. The account-wide roles are required to delete the resources created by the installation program. The cluster-specific Operator roles are required to clean-up the resources created by the OpenShift Operators. The Operators use the OIDC provider to authenticate with AWS APIs.
====

.  After the cluster is deleted, delete the OIDC provider that the cluster Operators use to authenticate:
+
[source,terminal]
----
$ rosa delete oidc-provider -c <cluster_id> --mode auto
----
+
[NOTE]
====
You can use the `-y` option to automatically answer yes to the prompts.
====

. Delete the cluster-specific Operator IAM roles:
+
[source,terminal]
----
$ rosa delete operator-roles -c <cluster_id> --mode auto
----

. Delete the account-wide roles:
+
[IMPORTANT]
====
Account-wide IAM roles and policies might be used by other OpenShift Container Platform clusters in the same AWS account. You must only remove the resources if they are not required by other clusters.
====
+
[source,terminal]
----
$ rosa delete account-roles --prefix <prefix> --mode auto
----
+
Replace `<prefix>` with the prefix of the account-wide roles to delete. If you did not specify a custom prefix when you created the account-wide roles, specify the default prefix, depending on how they were created, `HCP-ROSA` or `ManagedOpenShift`.

. Delete the account-wide and Operator IAM policies that you created for OpenShift Container Platform deployments:
. Delete the account-wide and Operator IAM policies that you created for OpenShift Container Platform deployments that use STS:
+
.. Log in to the AWS IAM Console.
.. Go to *Access management* -> *Policies* and select the checkbox for one of the account-wide policies.
.. With the policy selected, click *Actions* -> *Delete* to open the delete policy dialog.
.. Enter the policy name to confirm the deletion and select *Delete* to delete the policy.
.. Repeat this step to delete each of the account-wide and Operator policies for the cluster.

.Verification

* Verify that the cluster has been deleted:
+
[source,terminal]
----
$ rosa list clusters
----
+
The deleted cluster should not appear in the output.

[role="_additional-resources"]
.Additional resources

* About IAM resources for ROSA clusters that use STS
* Deleting a ROSA cluster

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* OpenShift Container Platform quick start guide
* Using the AWS Security Token Service
* Creating a OpenShift Container Platform cluster without AWS STS
* Creating an AWS `PrivateLink` cluster on OpenShift Container Platform
* Account-wide IAM role and policy reference
* Understanding the auto and manual deployment modes
* OpenShift Container Platform update life cycle
* Accessing a cluster through the web console
* Configuring identity providers for STS
* Cluster administration role
* Customer administrator user
* Adding services to a cluster using the {cluster-manager} console
* Managing compute nodes
* Preparing to configure the user workload monitoring stack
* Understanding the OpenShift Container Platform with STS deployment workflow
* Understanding the OpenShift Container Platform deployment workflow
* Upgrading OpenShift Container Platform Classic clusters
