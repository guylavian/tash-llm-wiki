---
title: "Getting started with the ROSA CLI"
type: reference
domain: openshift
slug: cli-reference-4-22-rosa-get-started-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cli_reference/rosa-get-started-cli
version: 4.22
family: cli_reference
documentKind: "Documentation"
---

# Getting started with the ROSA CLI

[id="rosa-get-started-cli"]
= Getting started with the ROSA CLI

[role="_abstract"]
Use this guide to learn how to install, configure, and update the {rosa-cli-first}.

// Module included in the following assemblies:
//
// * rosa_cli/rosa-get-started-cli.adoc

[id="rosa-about_{context}"]
= About the ROSA CLI

[role="_abstract"]
Use the {rosa-cli-first} to create, update, manage, and delete OpenShift Container Platform clusters and resources.

// Module included in the following assemblies:
//
// * rosa_cli/rosa-get-started-cli.adoc

[id="rosa-setting-up-cli_{context}"]
= Setting up the {rosa-cli}

[role="_abstract"]
Put the {rosa-cli-first} on the computer you use to run cluster commands.

.Procedure

. Install and configure the latest AWS CLI (`aws`).
.. Follow the AWS Command Line Interface documentation to install and configure the AWS CLI for your operating system.
+
Put `aws_access_key_id`, `aws_secret_access_key`, and `region` in the `.aws/credentials` file. See AWS Configuration basics in the AWS documentation.
+
[NOTE]
====
You can optionally use the `AWS_DEFAULT_REGION` environment variable to set the default AWS region.
====
.. Query the AWS API to verify if the AWS CLI is installed and configured correctly:
+
[source,terminal]
----
$ aws sts get-caller-identity  --output text
----
+
.Example output
[source,terminal]
----
<aws_account_id>    arn:aws:iam::<aws_account_id>:user/<username>  <aws_user_id>
----

. Download the latest version of the {rosa-cli-first} for your operating system from the *Downloads* page on {cluster-manager}.

. Extract the `rosa` binary file from the downloaded archive. The following example extracts the binary from a Linux tar archive:
+
[source,terminal]
----
$ tar xvf rosa-linux.tar.gz
----

. Add `rosa` to your path. In the following example, the `/usr/local/bin` directory is included in the path of the user:
+
[source,terminal]
----
$ sudo mv rosa /usr/local/bin/rosa
----

. Verify if the {rosa-cli} is installed correctly by querying the `rosa` version:
+
[source,terminal]
----
$ rosa version
----
+
.Example output
[source,terminal]
----
1.2.15
Your {rosa-cli} is up to date.
----

. Optional: Turn on tab completion for the {rosa-cli}. Press `Tab` twice to finish subcommands or see hints:
+
--
** To enable persistent tab completion for Bash on a Linux host:
.. Generate a `rosa` tab completion configuration file for Bash and save it to your `/etc/bash_completion.d/` directory:
+
[source,terminal]
----
# rosa completion bash > /etc/bash_completion.d/rosa
----
+
.. Open a new terminal to activate the configuration.
** To enable persistent tab completion for Bash on a macOS host:
.. Generate a `rosa` tab completion configuration file for Bash and save it to your `/usr/local/etc/bash_completion.d/` directory:
+
[source,terminal]
----
$ rosa completion bash > /usr/local/etc/bash_completion.d/rosa
----
+
.. Open a new terminal to activate the configuration.
** To enable persistent tab completion for Zsh:
.. If tab completion is not enabled for your Zsh environment, enable it by running the following command:
+
[source,terminal]
----
$ echo "autoload -U compinit; compinit" >> ~/.zshrc
----
+
.. Generate a `rosa` tab completion configuration file for Zsh and save it to the first directory in your functions path:
+
[source,terminal]
----
$ rosa completion zsh > "${fpath[1]}/_rosa"
----
+
.. Open a new terminal to activate the configuration.
** To enable persistent tab completion for fish:
.. Generate a `rosa` tab completion configuration file for fish and save it to your `~/.config/fish/completions/` directory:
+
[source,terminal]
----
$ rosa completion fish > ~/.config/fish/completions/rosa.fish
----
+
.. Open a new terminal to activate the configuration.
** To enable persistent tab completion for PowerShell:
.. Generate a `rosa` tab completion configuration file for PowerShell and save it to a file named `rosa.ps1`:
+
[source,terminal]
----
PS> rosa completion powershell | Out-String | Invoke-Expression
----
+
.. Source the `rosa.ps1` file from your PowerShell profile.
--
+
[NOTE]
====
For more information about configuring `rosa` tab completion, see the help menu by running the `rosa completion --help` command.
====

// Module included in the following assemblies:
//
// * rosa_cli/rosa-get-started-cli.adoc

[id="rosa-configure_{context}"]
= Configuring the {rosa-cli}

[role="_abstract"]
Use these commands to log in, log out, verify AWS settings, and download `rosa` or `oc` clients with the {rosa-cli-first}.

[id="rosa-login_{context}"]
== login
There are several methods you can use to log in to your Red{nbsp}Hat account using the {rosa-cli-first}. These methods are described in detail below.

[id="rosa-login-sso_{context}"]
=== Authenticating the {rosa-cli} with Red Hat single sign-on

You can log in to the {rosa-cli} with Red{nbsp}Hat single sign-on. Red{nbsp}Hat recommends using the `rosa` command line tool with Red{nbsp}Hat single sign-on, instead of using an offline authentication token.

An offline authentication token is long-lived, stored on your operating system, and cannot be revoked. These factors increase overall security risks and the likelihood of unauthorized access to your account.

Alternatively, authenticating with the Red{nbsp}Hat single sign-on method automatically sends your `rosa` instance a refresh token that is valid for 10 hours. This unique, temporary authorization code enhances security and reduces the risk of unauthorized access.

[IMPORTANT]
====
The method of authenticating using Red{nbsp}Hat single sign-on does not break any existing automations that rely on offline tokens. Red{nbsp}Hat recommends using services accounts for automation purposes. If you still need to use offline tokens for automation or other purposes, you can download the OpenShift Cluster Manager API token from the OpenShift Cluster Manager API Token page.
====

Use one of the following methods of authentication:

* If your system has a web browser, see the "Authenticating the {rosa-cli} with a single sign-on authorization code" section to authenticate with Red Hat single sign-on.
* If you are working with containers, remote hosts, or other environments without a web browser, see the "Authenticating the {rosa-cli} with a single sign-on device code" section to authenticate with Red{nbsp}Hat single sign-on.
* To authenticate the {rosa-cli} using an offline token, see the "Authenticating the {rosa-cli} with an offline token" section.

[NOTE]
====
Single sign-on authorization is supported with {rosa-cli} version 1.2.36 or later.
====

[id="rosa-login-sso_auth{context}"]
=== Authenticating the {rosa-cli} with a single sign-on authorization code

* To log in to the {rosa-cli} with a Red{nbsp}Hat single sign-on authorization code, run the following command:
+
.Syntax
[source,terminal]
----
$ rosa login --use-auth-code
----

Running this command redirects you to the Red{nbsp}Hat single sign-on login. Log in with your Red{nbsp}Hat login or email.

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|===

To switch accounts, logout from https://sso.redhat.com and run the `rosa logout` command in your terminal before attempting to login again.

[id="rosa-login-sso-device_{context}"]
=== Authenticating the {rosa-cli} with a single sign-on device code

If you are working with containers, remote hosts, and other environments without a web browser, you can use a Red{nbsp}Hat single sign-on device code for secure authentication. To do this, you must use a second device that has a web browser to approve the login.

[NOTE]
====
Single sign-on authorization is supported with {rosa-cli} version 1.2.36 or later.
====

* To log in to the {rosa-cli} with a Red Hat single sign-on device code, run the following command:
+
.Syntax
[source,terminal]
----
$ rosa login --use-device-code
----

Running this command will redirect you to the Red{nbsp}Hat SSO login and provide a log in code.

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|===

To switch accounts, logout from https://sso.redhat.com and run the `rosa logout` command in your terminal before attempting to login again.

[id="rosa-login-token_{context}"]
=== Authenticating the {rosa-cli} with an offline token

Log in to your Red{nbsp}Hat account, saving the credentials to the `rosa` configuration file.

[NOTE]
====
To use offline tokens for automation purposes, you can download the OpenShift Cluster Manager API token from the OpenShift Cluster Manager API Token page.
To use service accounts for automation purposes, see the Service Accounts page.
====

[IMPORTANT]
====
Red{nbsp}Hat recommends using service accounts for automation purposes.
====

* To log in to {rosa-cli} with a Red{nbsp}Hat offline token, run the following command:
+
.Syntax
[source,terminal]
----
$ rosa login [arguments]
----
+
.Arguments
[cols="30,70"]
|===
|Option |Definition

|--client-id
|The OpenID client identifier (string). Default: `cloud-services`

|--client-secret
|The OpenID client secret (string).

|--insecure
|Enables insecure communication with the server. This disables verification of TLS certificates and host names.

|--scope
|The OpenID scope (string). If this option is used, it replaces the default scopes. This can be repeated multiple times to specify multiple scopes. Default: `openid`

|--token
|Accesses or refreshes the token (string).

|--token-url
|The OpenID token URL (string). Default: `\https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token`
|===
+
.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

[id="rosa-logout_{context}"]
== logout

Log out of `rosa`. Logging out also removes the `rosa` configuration file.

.Syntax
[source,terminal]
----
$ rosa logout [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

[id="rosa-verify-permissions_{context}"]
=== verify permissions

Verify that the AWS permissions required to create a OpenShift Container Platform cluster are configured correctly:

.Syntax
[source,terminal]
----
$ rosa verify permissions [arguments]
----

[NOTE]
====
This command verifies permissions only for clusters that do not use the AWS Security Token Service (STS).
====

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--region
|The AWS region (string) in which to run the command. This value overrides the `AWS_REGION` environment variable.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

.Examples
Verify that the AWS permissions are configured correctly:
[source,terminal]
----
$ rosa verify permissions
----

Verify that the AWS permissions are configured correctly in a specific region:
[source,terminal]
----
$ rosa verify permissions --region=us-west-2
----

[id="rosa-verify-quota_{context}"]
=== verify quota

Verifies that AWS quotas are configured correctly for your default region.

.Syntax
[source,terminal]
----
$ rosa verify quota [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--region
|The AWS region (string) in which to run the command. This value overrides the `AWS_REGION` environment variable.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

.Examples
Verify that the AWS quotas are configured correctly for the default region:

[source,terminal]
----
$ rosa verify quota
----

Verify that the AWS quotas are configured correctly in a specific region:

[source,terminal]
----
$ rosa verify quota --region=us-west-2
----

[id="rosa-download-rosa-client_{context}"]
== download rosa

Download the latest compatible version of the `rosa` CLI.

After you download `rosa`, extract the contents of the archive and add it to your path.

.Syntax
[source,terminal]
----
$ rosa download rosa [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.
|===

[id="rosa-download-ocp-client_{context}"]
== download oc

Download the latest compatible version of the OpenShift Container Platform CLI (`oc`).

After you download `oc`, you must extract the contents of the archive and add it to your path.

.Syntax
[source,terminal]
----
$ rosa download oc [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.
|===

.Examples
Download `oc` client tools:

[source,terminal]
----
$ rosa download oc
----

[id="rosa-verify-ocp-client_{context}"]
== verify oc

Verifies that the OpenShift Container Platform CLI (`oc`) is installed correctly.

.Syntax
[source,terminal]
----
$ rosa verify oc [arguments]
----

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.
|===

*Example*
Verify `oc` client tools:

[source,terminal]
----
$ rosa verify oc
----

[role="_additional-resources"]
.Additional resources

* Setting up the ROSA CLI

* Getting started with the OpenShift CLI

// Module included in the following assemblies:
//
// * rosa_cli/rosa-get-started-cli.adoc

[id="rosa-initialize_{context}"]
= Initializing OpenShift Container Platform

Use the `init` command to initialize OpenShift Container Platform only if you are using non-STS.

[id="rosa-init_{context}"]
== init

Perform a series of checks to verify that you are ready to deploy a OpenShift Container Platform cluster.

The list of checks includes the following:

* Checks to see that you have logged in (see `login`)
* Checks that your AWS credentials are valid
* Checks that your AWS permissions are valid (see `verify permissions`)
* Checks that your AWS quota levels are high enough (see `verify quota`)
* Runs a cluster simulation to ensure cluster creation will perform as expected
* Checks that the `osdCcsAdmin` user has been created in your AWS account
* Checks that the OpenShift Container Platform command-line tool is available on your system

.Syntax
[source,terminal]
----
$ rosa init [arguments]
----

.Arguments
[cols="30,70"]
|===
|Option |Definition

|--region
|The AWS region (string) in which to verify quota and permissions. This value overrides the `AWS_REGION` environment variable only when running the `init` command, but it does not change your AWS CLI configuration.

|--delete
|Deletes the stack template that is applied to your AWS account during the `init` command.

|--client-id
|The OpenID client identifier (string). Default: `cloud-services`

|--client-secret
|The OpenID client secret (string).

|--insecure
|Enables insecure communication with the server. This disables verification of TLS certificates and host names.

|--scope
|The OpenID scope (string). If this option is used, it completely replaces the default scopes. This can be repeated multiple times to specify multiple scopes. Default: `openid`

|--token
|Accesses or refreshes the token (string).

|--token-url
|The OpenID token URL (string). Default: `\https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token`
|===

.Optional arguments inherited from parent commands
[cols="30,70"]
|===
|Option |Definition

|--help
|Shows help for this command.

|--debug
|Enables debug mode.

|--profile
|Specifies an AWS profile (string) from your credentials file.
|===

.Examples
Configure your AWS account to allow ROSA clusters:

[source,terminal]
----
$ rosa init
----

Configure a new AWS account using pre-existing {cluster-manager} credentials:

[source,terminal]
----
$ rosa init --token=$OFFLINE_ACCESS_TOKEN
----

// Module included in the following assemblies:
//
// * rosa_cli/rosa-get-started-cli.adoc

[id="rosa-using-bash-script_{context}"]
= Using a Bash script

This is an example workflow of how to use a Bash script with the {rosa-cli-first}.

.Prerequisites
Make sure that AWS credentials are available as one of the following options:

* AWS profile
* Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)

.Procedure

. Initialize `rosa` using a {cluster-manager-first} offline token from Red{nbsp}Hat:
+
[source,terminal]
----
$ rosa init --token=<token>
----

. Create the OpenShift Container Platform cluster:
+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name>
----
//Note to writers: The create cluster command specifically uses --cluster-name because a cluster ID does not exist yet. All other commands use --cluster because either the name or the ID can be used.

. Add an identity provider (IDP):
+
[source,terminal]
----
$ rosa create idp --cluster=<cluster_name> --type=<identity_provider> [arguments]
----

. Add a `dedicated-admin` user:
+
[source,terminal]
----
$ rosa grant user dedicated-admin --user=<idp_user_name> --cluster=<cluster_name>
----
// Module included in the following assemblies:
//
// * rosa_cli/rosa-get-started-cli.adoc

[id="rosa-updating-the-rosa-cli_{context}"]
= Updating the {rosa-cli}

[role="_abstract"]
Update the {rosa-cli-first} to the latest version that works with your cluster.

.Procedure

. Confirm that a new version of the {rosa-cli} (`rosa`) is available:
+
[source,terminal]
----
$ rosa version
----
+
.Example output
[source,terminal]
----
1.2.12
There is a newer release version '1.2.15', please consider updating: https://mirror.openshift.com/pub/openshift-v4/clients/rosa/latest/
----

. Download the latest compatible version of the {rosa-cli}:
+
[source,terminal]
----
$ rosa download rosa
----
+
This command downloads an archive called `rosa-*.tar.gz` into the current directory. The exact name of the file depends on your operating system and system architecture.

. Extract the contents of the archive:
+
[source,terminal]
----
$ tar -xzf rosa-linux.tar.gz
----

. Install the new version of the {rosa-cli} by moving the extracted file into your path. In the following example, the `/usr/local/bin` directory is included in the path of the user:
+
[source,terminal]
----
$ sudo mv rosa /usr/local/bin/rosa
----

.Verification
* Verify that the new version of the {rosa-cli} is installed.
+
[source,terminal]
----
$ rosa version
----
+
.Example output
[source,terminal]
----
1.2.15
Your {rosa-cli} is up to date.
----
