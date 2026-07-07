---
title: "Installing the ROSA CLI (`rosa`)"
type: reference
domain: openshift
slug: rosa-install-access-delete-clusters-4-22-rosa-installing-rosa
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_install_access_delete_clusters/rosa-installing-rosa
version: 4.22
family: rosa_install_access_delete_clusters
documentKind: "Documentation"
---

# Installing the ROSA CLI (`rosa`)

[id="rosa-installing-cli"]
= Installing the ROSA CLI (`rosa`)

[role="_abstract"]
After you configure your AWS account, install and configure the {rosa-cli-first}.

// Module included in the following assemblies:
//
// * rosa_install_access_delete_clusters/rosa_getting_started_iam/rosa-installing-rosa.adoc

[id="rosa-installing-and-configuring-the-rosa-cli_{context}"]
= Installing and configuring the {rosa-cli}

[role="_abstract"]
Install and configure the {rosa-cli-first}. You can also install the {oc-first} and verify if the required AWS resource quotas are available by using the {rosa-cli}.

.Prerequisites

* Review and complete the AWS prerequisites and OpenShift Container Platform policies.
* Create a Red{nbsp}Hat account, if you do not already have one. Then, check your email for a verification link. You will need these credentials to install OpenShift Container Platform.
* Configure your AWS account and enable the OpenShift Container Platform service in your AWS account.

.Procedure

. Install `rosa`, the {rosa-cli}.
.. Download the latest release of the {rosa-cli} for your operating system.
.. Optional: Rename the executable file you downloaded to `rosa`. This documentation uses `rosa` to refer to the executable file.
.. Optional: Add `rosa` to your path.
+
.Example
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
.Example output
[source,terminal]
----
Command-line tool for Red Hat OpenShift Service on AWS.
For further documentation visit https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws

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
.. Optional: Generate the command completion scripts for the {rosa-cli}. The following example generates the Bash completion scripts for a Linux machine:
+
[source,terminal]
----
$ rosa completion bash | sudo tee /etc/bash_completion.d/rosa
----
.. Optional: Enable command completion for the {rosa-cli} from your existing terminal. The following example enables Bash completion for `rosa` in an existing terminal on a Linux machine:
+
[source,terminal]
----
$ source /etc/bash_completion.d/rosa
----

. Log in to your Red{nbsp}Hat account with `rosa`.
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
.Example output
[source,terminal]
----
To login to your Red Hat account, get an offline access token at https://console.redhat.com/openshift/token/rosa
? Copy the token and paste it here: <my-offline-access-token>
----
+
.Example output continued
[source,terminal]
----
I: Logged in as 'rh-rosa-user' on 'https://api.openshift.com'
----

. Enter the following command to verify that your AWS account has the necessary permissions.
+
[source,terminal]
----
$ rosa verify permissions
----
+
.Example output
[source,terminal]
----
I: Validating SCP policies...
I: AWS SCP policies ok
----
+
[NOTE]
====
This command verifies permissions only for OpenShift Container Platform clusters that do not use the AWS Security Token Service (STS).
====

. Verify that your AWS account has the necessary quota to deploy a OpenShift Container Platform cluster.
+
[source,terminal]
----
$ rosa verify quota --region=us-west-2
----
+
.Example output
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
If you need to increase your quota, go to your AWS console, and request a quota increase for the service that failed.
+
After both the permissions and quota checks pass, proceed to the next step.
+
. Prepare your AWS account for cluster deployment:
+
.. Run the following command to verify your Red{nbsp}Hat and AWS credentials are setup correctly. Check that your AWS Account ID, Default Region and ARN match what you expect. You can safely ignore the rows beginning with `OCM` for now.
+
[source,terminal]
----
$ rosa whoami
----
+
.Example output
[source,terminal]
----
AWS Account ID:               000000000000
AWS Default Region:           us-east-2
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
+
.. Initialize your AWS account. This step runs a CloudFormation template that prepares your AWS account for cluster deployment and management. This step typically takes 1-2 minutes to complete.
+
[source,terminal]
----
$ rosa init
----
+
.Example output
[source,terminal]
----
I: Logged in as 'rh-rosa-user' on 'https://api.openshift.com'
I: Validating AWS credentials...
I: AWS credentials are valid!
I: Validating SCP policies...
I: AWS SCP policies ok
I: Validating AWS quota...
I: AWS quota ok
I: Ensuring cluster administrator user 'osdCcsAdmin'...
I: Admin user 'osdCcsAdmin' created successfully!
I: Verifying whether OpenShift command-line tool is available...
E: OpenShift command-line tool is not installed.
Run 'rosa download oc' to download the latest version, then add it to your PATH.
----

. Install the {oc-first} from the {rosa-cli}.
.. Enter this command to download the latest version of the OpenShift CLI:
+
[source,terminal]
----
$ rosa download oc
----

.. After downloading the OpenShift CLI, extract it and add it to your path.
.. Enter this command to verify that the OpenShift CLI is installed correctly:
+
[source,terminal]
----
$ rosa verify oc
----

.Next steps

* Create a OpenShift Container Platform cluster.

[id="additional-resources_rosa-installing-cli"]
[role="_additional-resources"]
== Additional resources

* AWS prerequisites
* Required AWS service quotas and requesting increases
* Understanding the ROSA deployment workflow
