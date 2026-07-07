---
title: "Setting up the environment for using STS"
type: reference
domain: openshift
slug: rosa-planning-4-22-rosa-sts-setting-up-environment
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_planning/rosa-sts-setting-up-environment
version: 4.22
family: rosa_planning
documentKind: "Documentation"
---

# Setting up the environment for using STS

[id="rosa-sts-setting-up-environment"]
= Setting up the environment for using STS

[id="rosa-hcp-setting-up-environment"]
= Setting up the environment

[role="_abstract"]
After you meet the AWS prerequisites, set up your environment and install OpenShift Container Platform.

//For ROSA clusters
// Module included in the following assemblies:
//
// * rosa_planning/rosa-sts-setting-up-environment.adoc
[id="rosa-sts-setting-up-environment_{context}"]
= Setting up the environment for STS

[role="_abstract"]
Before you create a OpenShift Container Platform cluster that uses the AWS Security Token Service (STS), complete the following steps to set up your environment.

.Prerequisites

* Review and complete the deployment prerequisites and policies.
* Create a Red{nbsp}Hat account, if you do not already have one. Then, check your email for a verification link. You will need these credentials to install OpenShift Container Platform.

.Procedure

. Log in to the Amazon Web Services (AWS) account that you want to use.
+
It is recommended to use a dedicated AWS account to run production clusters. If you are using AWS Organizations, you can use an AWS account within your organization or create a new one.
+
If you are using AWS Organizations and you need to have a service control policy (SCP) applied to the AWS account you plan to use, these policies must not be more restrictive than the roles and policies required by the cluster.
+
. Enable OpenShift Container Platform in the AWS Management Console.
.. Sign in to your AWS account.
.. To enable OpenShift Container Platform, go to the ROSA service and select *Enable OpenShift*.

. Install and configure the AWS CLI.
.. Follow the AWS command-line interface documentation to install and configure the AWS CLI for your operating system.
+
Specify the correct `aws_access_key_id` and `aws_secret_access_key` in the `.aws/credentials` file. See AWS Configuration basics in the AWS documentation.

.. Set a default AWS region.
+
[NOTE]
====
You can use the environment variable to set the default AWS region.
====
+
OpenShift Container Platform evaluates regions in the following priority order:
+
... The region specified when running the `rosa` command with the `--region` flag.
... The region set in the `AWS_DEFAULT_REGION` environment variable. See Environment variables to configure the AWS CLI in the AWS documentation.
... The default region set in your AWS configuration file. See Quick configuration with aws configure in the AWS documentation.
.. Optional: Configure your AWS CLI settings and credentials by using an AWS named profile. `rosa` evaluates AWS named profiles in the following priority order:
... The profile specified when running the `rosa` command with the `--profile` flag.
... The profile set in the `AWS_PROFILE` environment variable. See Named profiles in the AWS documentation.
.. Verify the AWS CLI is installed and configured correctly by running the following command to query the AWS API:
+
[source,terminal]
----
$ aws sts get-caller-identity
----
+
. Install the latest version of the ROSA CLI (`rosa`).
.. Download the latest release of the ROSA CLI for your operating system.
.. Optional: Rename the file you downloaded to `rosa` and make the file executable. This documentation uses `rosa` to refer to the executable file.
+
[source,terminal]
----
$ chmod +x rosa
----
.. Optional: Add `rosa` to your path.
+
[source,terminal]
----
$ mv rosa /usr/local/bin/rosa
----
.. Enter the following command to verify your installation:
+
[source,terminal]
----
$ rosa
----
+
For example:
+
[source,terminal]
----
Command-line tool for OpenShift Container Platform. For further documentation visit https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws

Usage:
  rosa [command]

Available Commands:
  completion  Generates completion scripts
  create      Create a resource from stdin
  delete      Delete a specific resource
  describe    Show details of a specific resource
  download    Download necessary tools for using your cluster
  edit        Edit a specific resource
  grant       Grant role to a specific resource
  help        Help about any command
  init        Applies templates to support Red Hat OpenShift Service on AWS
  install     Installs a resource into a cluster
  link        Link a ocm/user role from stdin
  list        List all resources of a specific type
  login       Log in to your Red Hat account
  logout      Log out
  logs        Show installation or uninstallation logs for a cluster
  revoke      Revoke role from a specific resource
  uninstall   Uninstalls a resource from a cluster
  unlink      UnLink a ocm/user role from stdin
  upgrade     Upgrade a resource
  verify      Verify resources are configured correctly for cluster install
  version     Prints the version of the tool
  whoami      Displays user account information

Flags:
      --color string   Surround certain characters with escape sequences to display them in color on the terminal. Allowed options are [auto never always] (default "auto")
      --debug          Enable debug mode.
  -h, --help           help for rosa

Use "rosa [command] --help" for more information about a command.
----
+
.. Generate the command completion scripts for the ROSA CLI. The following example generates the Bash completion scripts for a Linux machine:
+
[source,terminal]
----
$ rosa completion bash | sudo tee /etc/bash_completion.d/rosa
----
.. Source the scripts to enable `rosa` command completion from your existing terminal. The following example sources the Bash completion scripts for `rosa` on a Linux machine:
+
[source,terminal]
----
$ source /etc/bash_completion.d/rosa
----

. Log in to your Red{nbsp}Hat account with the ROSA CLI.
+
.. Enter the following command.
+
[source,terminal]
----
$ rosa login
----
+
.. Replace `<my_offline_access_token>` with your token.
+
For example:
+
[source,terminal]
----
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa
? Copy the token and paste it here: <my-offline-access-token>
----
+
The following shows the next step of the example:
+
[source,terminal]
----
I: Logged in as '<rh-rosa-user>' on 'https://api.openshift.com'
----

. Verify that your AWS account has the necessary quota to deploy a OpenShift Container Platform cluster.
+
[source,terminal]
----
$ rosa verify quota [--region=<aws_region>]
----
+
For example:
+
[source,terminal]
----
I: Validating AWS quota...
I: AWS quota ok
----
+
[NOTE]
====
Sometimes your AWS quota varies by region. If you receive any errors, try a different region.
====
+
If you need to increase your quota, go to the AWS Management Console and request a quota increase for the service that failed.
+
After the quota check succeeds, proceed to the next step.
+
. Prepare your AWS account for cluster deployment:
+
.. Run the following command to verify your Red{nbsp}Hat and AWS credentials are setup correctly.  Check that your AWS Account ID, Default Region and ARN match what you expect. You can safely ignore the rows beginning with {cluster-manager} for now.
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
AWS Account ID:               000000000000
AWS Default Region:           us-east-1
AWS ARN:                      arn:aws:iam::000000000000:user/hello
OCM API:                      https://api.openshift.com
OCM Account ID:               1DzGIdIhqEWyt8UUXQhSoWaaaaa
OCM Account Name:             Your Name
OCM Account Username:         you@domain.com
OCM Account Email:            you@domain.com
OCM Organization ID:          1HopHfA2hcmhup5gCr2uH5aaaaa
OCM Organization Name:        Red Hat
OCM Organization External ID: 0000000
----

. Install the OpenShift CLI (`oc`), version 4.7.9 or greater, from the ROSA (`rosa`) CLI.
.. Enter this command to download the latest version of the `oc` CLI:
+
[source,terminal]
----
$ rosa download openshift-client
----

.. After downloading the `oc` CLI, unzip it and add it to your path.
.. Enter this command to verify that the `oc` CLI is installed correctly:
+
[source,terminal]
----
$ rosa verify openshift-client
----

. After completing these steps, you are ready to set up IAM and OIDC access-based roles.

//For HCP clusters
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

[id="next-steps_rosa-sts-setting-up-environment"]
== Next steps
* Create a OpenShift Container Platform cluster with STS quickly or create a cluster using customizations.
* Create a OpenShift Container Platform cluster

[id="additional-resources"]
[role="_additional-resources"]
== Additional resources
* AWS Prerequisites
* Required AWS service quotas and increase requests
* AWS Prerequisites
// // TODO OSDOCS-11789: AWS quotas for HCP
