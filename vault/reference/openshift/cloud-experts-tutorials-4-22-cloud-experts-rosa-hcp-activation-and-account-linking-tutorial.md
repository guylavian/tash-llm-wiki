---
title: "Tutorial: {product-title} activation and account linking"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-rosa-hcp-activation-and-account-linking-tutorial
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-rosa-hcp-activation-and-account-linking-tutorial
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: {product-title} activation and account linking

[id="cloud-experts-activation-account-linking"]
= Tutorial: OpenShift Container Platform activation and account linking

[role="_abstract"]
This tutorial describes the process for activating OpenShift Container Platform and linking to an AWS account, before deploying the first cluster.

[IMPORTANT]
====
If you have received a private offer for the product, make sure to proceed according to the instructions provided with the private offer before following this tutorial. The private offer is designed either for a case when the product is already activated, which replaces an active subscription, or for first time activations.
====

== Prerequisites

* Log in to the Red{nbsp}Hat account that you want to associate with the AWS account that will activate the OpenShift Container Platform product subscription.
* The AWS account used for service billing can only be associated with a single Red{nbsp}Hat account. Typically an AWS payer account is the one that is used to subscribe to OpenShift Container Platform and used for account linking and billing.
* All team members belonging to the same Red{nbsp}Hat organization can use the linked AWS account for service billing while creating OpenShift Container Platform clusters.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-rosa-hcp-activation-and-account-linking-tutorial.adoc

[id="subscription-enablement_{context}"]
= Subscription enablement and AWS account setup

[role="_abstract"]
You can activate the OpenShift Container Platform product at the AWS console page by clicking the *Get started* button:

.Procedure
. Click the *Get started* button on AWS console page:
+
image::rosa-get-started.png[]
+
If you have activated OpenShift Container Platform before but did not complete the process, you can click the button and complete the account linking as described in the following steps.

. Confirm that you want your contact information to be shared with Red{nbsp}Hat and enable the service:
+
[caption="Enable OpenShift Container Platform"]
image::rosa-enable-2.png[]
+
* You will not be charged by enabling the service in this step. The connection is made for billing and metering that will take place only after you deploy your first cluster. This could take a few minutes.
+
. After the process is completed, you will see a confirmation:
+
[caption="OpenShift Container Platform enablement confirmation"]
+
image::rosa-prereq-enable-3.png[]
+
. Other sections on this verification page show the status of additional prerequisites. In case any of these prerequisites are not met, a corresponding message is shown. Here is an example of insufficient quotas in the selected region:
+
[caption="Service quota"]
+
image::rosa-service-quota-4.png[]
+
** Click the *Increase service quotas* button or use the *Learn more* link to get more information about the about how to manage service quotas. In the case of insufficient quotas, note that quotas are region-specific. You can use the region switcher in the upper right corner of the web console to re-run the quota check for any region you are interested in and then submit service quota increase requests as needed.

. If all the prerequisites are met, the page will look like this:
+
[caption="Verifying OpenShift Container Platform prerequisites"]
image::rosa-prereq-5.png[]
+
The ELB service-linked role is created for you automatically. You can click any of the small *Info* blue links to get contextual help and resources.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-rosa-hcp-activation-and-account-linking-tutorial.adoc

[id="aws-rh-linking_{context}"]
= AWS and Red{nbsp}Hat account and subscription linking

[role="_abstract"]
You must link your AWS and Red{nbsp}Hat accounts and subscriptions.

.Procedure
. Click the orange *Continue to Red{nbsp}Hat* button to proceed with account linking:
+
image::rosa-continue-rh-6.png[]

. If you are not already logged in to your Red{nbsp}Hat account in your current browser's session, you will be asked to log in to your account:
+
[NOTE]
====
Your AWS account must be linked to a single Red{nbsp}Hat organization.
====
+
. Log in to your Red{nbsp}Hat account:
+
image::rosa-login-rh-account-7.png[]
+
* You can also register for a new Red{nbsp}Hat account or reset your password on this page.
* Log in to the Red{nbsp}Hat account that you want to associate with the AWS account that has activated the OpenShift Container Platform product subscription.
* The AWS account used for service billing can only be associated with a single Red{nbsp}Hat account. Typically an AWS payer account is the one that is used to subscribe to OpenShift Container Platform and used for account linking and billing.
* All team members belonging to the same Red{nbsp}Hat organization can use the linked AWS account for service billing while creating OpenShift Container Platform clusters.

. Complete the Red{nbsp}Hat account linking after reviewing the terms and conditions:
+
[NOTE]
====
This step is available only if the AWS account was not linked to any Red{nbsp}Hat account before.

This step is skipped if the AWS account is already linked to the user's logged in Red{nbsp}Hat account.

If the AWS account is linked to a different Red{nbsp}Hat account, an error will be displayed. See Correcting Billing Account Information for HCP clusters for troubleshooting.
====
+
. Complete your account connection
+
image::rosa-rh-account-connection-8.png[]
+
Both the Red{nbsp}Hat and AWS account numbers are shown on this screen.

. Click the *Connect accounts* button if you agree with the service terms.
+
If this is the first time you are using the {hybrid-console}, you will be asked to agree with the general managed services terms and conditions before being able to create the first cluster:
+
[caption="Terms and conditions"]
image::rosa-terms-conditions-9.png[]
+
Additional terms that need to be reviewed and accepted are shown after clicking the *View Terms and Conditions* button:
+
[caption="Red{nbsp}Hat terms and conditions"]
image::rosa-terms-conditions-9-5.png[]
+
Submit your agreement once you have reviewed any additional terms when prompted at this time.

. The {hybrid-console-second} provides a confirmation that AWS account setup was completed and lists the prerequisites for cluster deployment:
+
[caption="Complete OpenShift Container Platform prerequisites"]
image::rosa-cluster-create-10.png[]
+
The last section of this page shows cluster deployment options, either using the `rosa` CLI or through the web console:
+
[caption="Deploy the cluster and set up access"]
image::rosa-cli-ui-12.png[]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-rosa-hcp-activation-and-account-linking-tutorial.adoc

[id="selecting-billing-account-cli_{context}"]
= Selecting the AWS billing account for OpenShift Container Platform during cluster deployment using the CLI

[role="_abstract"]
When deploying your cluster using {rosa-cli}, you must select the correct AWS billing account.

[IMPORTANT]
====
Make sure that you have the most recent ROSA command-line interface (CLI) and AWS CLI installed and have completed the OpenShift Container Platform prerequisites covered in the previous section. See Help with ROSA CLI setup and Instructions to install the AWS CLI for more information.
====

.Procedure
. Initiate the cluster deployment using the `rosa create cluster` command. You can click the *copy* button on the Set up Red{nbsp}Hat OpenShift Service on AWS (ROSA) console page and paste the command in your terminal. This launches the cluster creation process in interactive mode:
+
[caption="Deploy the cluster and set up access"]
image::rosa-cli-15.png[]

. To use a custom AWS profile, one of the non-default profiles specified in your `~/.aws/credentials`, you can add the `–profile <profile_name>` selector to the rosa create cluster command so that the command looks like rosa create cluster `–profile stage`. If no AWS CLI profile is specified using this option, the default AWS CLI profile will determine the AWS infrastructure profile into which the cluster is deployed. The billing AWS profile is selected in one of the following steps.

. When deploying a OpenShift Container Platform cluster, the billing AWS account needs to be specified:
+
[caption="Specify the Billing Account"]
image::rosa-create-cli-billing-17.png[]
+
* Only AWS accounts that are linked to the user's logged in Red{nbsp}Hat account are shown.
* The specified AWS account is charged for using the OpenShift Container Platform service.
* An indicator shows if the OpenShift Container Platform contract is enabled or not enabled for a given AWS billing account.
** If you select an AWS billing account that shows the _Contract enabled_ label, on-demand consumption rates are charged only after the capacity of your pre-paid contract is consumed.
** AWS accounts without the _Contract enabled_ label are charged the applicable on-demand consumption rates.

[IMPORTANT]
====
The detailed cluster deployment steps are beyond the scope of this tutorial. See the _Additional resources_ for cluster creation guides.
====

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-rosa-hcp-activation-and-account-linking-tutorial.adoc

[id="selecting-billing-account-ui_{context}"]
= Selecting the AWS billing account for OpenShift Container Platform during cluster deployment using the web console

[role="_abstract"]
When deploying your cluster using {cluster-manager}, you must select the correct AWS billing account.

.Procedure
. A cluster can be created using the web console by selecting the second option in the bottom section of the introductory *Set up OpenShift Container Platform* page:
+
[caption="Deploy with web interface"]
image::rosa-deploy-ui-19.png[]
+
[NOTE]
====
Complete the prerequisites before starting the web console deployment process.

The `rosa` CLI is required for certain tasks, such as creating the account roles. If you are deploying OpenShift Container Platform for the first time, follow this the CLI steps until running the `rosa whoami` command, before starting the web console deployment steps.
====

. The first step when creating a OpenShift Container Platform cluster using the web console is the control plane selection. Make sure the *Hosted* option is selected before clicking the *Next* button:
+
[caption="Select hosted option"]
+
image::rosa-deploy-ui-hcp-20.png[]

. The next step *Accounts and roles* allows you specifying the infrastructure AWS account, into which the OpenShift Container Platform cluster is deployed and where the resources are consumed and managed:
+
[caption="AWS infrastructure account"]
image::rosa-ui-account-21.png[]
+
* Click the *How to associate a new AWS account*, if you don not see the account into which you want to deploy the OpenShift Container Platform cluster for detailed information on how to create or link account roles for this association.
* The `rosa` CLI is used for this.
* If you are using multiple AWS accounts and have their profiles configured for the AWS CLI, you can use the `--profile` selector to specify the AWS profile when working with the `rosa` CLI commands.

. The billing AWS account is selected in the immediately following section:
+
[caption="AWS billing account"]
image::rosa-ui-billing-22.png[]
+
* Only AWS accounts that are linked to the user's logged in Red{nbsp}Hat account are shown.
* The specified AWS account is charged for using the OpenShift Container Platform service.
* An indicator shows if the OpenShift Container Platform contract is enabled or not enabled for a given AWS billing account.
** If you select an AWS billing account that shows the _Contract enabled_ label, on-demand consumption rates are charged only after the capacity of your pre-paid contract is consumed.
** AWS accounts without the _Contract enabled_ label are charged the applicable on-demand consumption rates.
+
[NOTE]
====
The following steps past the billing AWS account selection are beyond the scope of this tutorial.
====

[role="_additional-resources"]
.Additional resources

* Creating OpenShift Container Platform clusters using the default options
* Creating a OpenShift Container Platform cluster using the CLI
* Getting started with Red Hat OpenShift Service on AWS learning path
