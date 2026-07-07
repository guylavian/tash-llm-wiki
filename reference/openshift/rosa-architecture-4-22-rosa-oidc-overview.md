---
title: "OpenID Connect Overview"
type: reference
domain: openshift
slug: rosa-architecture-4-22-rosa-oidc-overview
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_architecture/rosa-oidc-overview
version: 4.22
family: rosa_architecture
documentKind: "Documentation"
---

# OpenID Connect Overview

[id="rosa-oidc-overview"]
= OpenID Connect Overview

[role="_abstract"]
OpenID Connect (OIDC) uses Security Token Service (STS) to allow clients to provide a web identity token to gain access to multiple services. When a client signs into a service using STS, the token is validated against the OIDC identity provider.

The OIDC protocol uses a configuration URL that contains the necessary information to authenticate a client's identity. The protocol responds to the provider with the credentials needed for the provider to validate the client and sign them in.

OpenShift Container Platform clusters use STS and OIDC to grant the in-cluster operators access to necessary AWS resources.

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-oidc-overview.adoc

[id=rosa-oidc-understanding_{context}]
= Understanding the OIDC verification options

You can configure the following types of OIDC verification:

* Unregistered, managed OIDC configuration
+
An unregistered, managed OIDC configuration is created for you during the cluster installation process. The configuration is hosted under Red{nbsp}Hat's AWS account. This option does not give you the ID that links to the OIDC configuration, so you can only use this type of OIDC configuration on a single cluster.

* Registered, managed OIDC configuration
+
You create a registered, managed OIDC configuration before you start creating your clusters. This configuration is hosted under Red{nbsp}Hat's AWS account like the unregistered managed OIDC configuration. When you use this option for your OIDC configuration, you receive an ID that links to the OIDC configuration. Red{nbsp}Hat uses this ID to identify the issuer URL and private key. You can then use this URL and private key to create an identity provider and Operator roles. These resources are created under your AWS account by using Identity and Access Management (IAM) AWS services. You can also use the OIDC configuration ID during the cluster creation process.

* Registered, unmanaged OIDC configuration
+
You can create a registered, unmanaged OIDC configuration before you start creating your clusters. This configuration is hosted under your AWS account. When you use this option, you are responsible for managing the private key. You can register the configuration with {cluster-manager-first} by storing the private key in an AWS secrets file by using the AWS Secrets Manager (SM) service and the issuer URL which hosts the configuration. You can use the OpenShift Container Platform (ROSA) CLI, `rosa`, to create a registered, unmanaged OIDC configuration with the `rosa create oidc-config --managed=false` command. This command creates and hosts the configuration under your account and creates the necessary files and private secret key. This command also registers the configuration with {cluster-manager}.

The registered options can be used to create the required IAM resources before you start creating a cluster. This option results in faster install times since there is a waiting period during cluster creation where the installation pauses until you create an OIDC provider and Operator roles.

For ROSA Classic, you may use any of the OIDC configuration options. If you are using {hcp-title}, you must create registered OIDC configuration, either as managed or unmanaged. You can share the registered OIDC configurations with other clusters. This ability to share the configuration also allows you to share the provider and Operator roles.

[NOTE]
====
Reusing the OIDC configurations, OIDC provider, and Operator roles between clusters is not recommended for production clusters since the authentication verification is used throughout all of these clusters. Red{nbsp}Hat recommends only reusing resources between non-production test environments.
====

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-byo-odic-overview_{context}"]
= Creating an OpenID Connect Configuration

When using a cluster hosted by Red{nbsp}Hat, you can create a managed or unmanaged OpenID Connect (OIDC) configuration by using the OpenShift Container Platform (ROSA) CLI, `rosa`. A managed OIDC configuration is stored within Red{nbsp}Hat's AWS account, while a generated unmanaged OIDC configuration is stored within your AWS account. The OIDC configuration is registered to be used with {cluster-manager}. When creating an unmanaged OIDC configuration, the CLI provides the private key for you.

// Module included in the following assemblies:
//
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_architecture/rosa-oidc-overview.adoc
// * rosa_hcp/rosa-hcp-quickstart-guide.adoc
// * rosa_hcp/rosa-hcp-egress-zero-install.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-quickly.adoc
// * rosa_install_access_delete_clusters/rosa-sts-creating-a-cluster-with-customizations.adoc
// * rosa_planning/rosa-hcp-prepare-iam-roles-resources.adoc

[id="rosa-sts-byo-oidc_{context}"]
= Creating an OpenID Connect configuration

[role="_abstract"]
OpenShift Container Platform clusters use OIDC and the AWS Security Token Service (STS) to authenticate Operator access to AWS resources they require to perform their functions. Each production cluster requires its own OIDC configuration. When creating a OpenShift Container Platform cluster, you can create the OpenID Connect (OIDC) configuration before creating your cluster.

.Prerequisites

* You have completed the AWS prerequisites for OpenShift Container Platform.
* You have installed and configured the latest {rosa-cli-first} on your installation host.

.Procedure

. To create your OIDC configuration alongside the AWS resources, run the following command:
+
[source,terminal]
----
$ rosa create oidc-config --mode=auto --yes
----
+
This command returns the following information.
+
For example:
+
[source,terminal]
----
? Would you like to create a Managed (Red Hat hosted) OIDC Configuration Yes
I: Setting up managed OIDC configuration
I: To create Operator Roles for this OIDC Configuration, run the following command and remember to replace <user-defined> with a prefix of your choice:
	rosa create operator-roles --prefix <user-defined> --oidc-config-id 13cdr6b
If you are going to create a Hosted Control Plane cluster please include '--hosted-cp'
I: Creating OIDC provider using 'arn:aws:iam::4540112244:user/userName'
? Create the OIDC provider? Yes
I: Created OIDC provider with ARN 'arn:aws:iam::4540112244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/13cdr6b'
----
+
When creating your cluster, you must supply the OIDC config ID. The CLI output provides this value for `--mode auto`, otherwise you must determine these values based on `aws` CLI output for `--mode manual`.

. Optional: you can save the OIDC configuration ID as a variable to use later. Run the following command to save the variable:
+
--
[source,terminal]
----
$ export OIDC_ID=<oidc_config_id>
----
`<oidc_config_id>`:: In this example output, the OIDC configuration ID is `13cdr6b`.
--

** View the value of the variable by running the following command:
+
[source,terminal]
----
$ echo $OIDC_ID
----
+
For example:
+
[source,terminal]
----
13cdr6b
----

.Verification

* You can list the possible OIDC configurations available for your clusters that are associated with your user organization. Run the following command:
+
[source,terminal]
----
$ rosa list oidc-config
----
+
For example:
+
[source,terminal]
----
ID                                MANAGED  ISSUER URL                                                             SECRET ARN
2330dbs0n8m3chkkr25gkkcd8pnj3lk2  true     https://dvbwgdztaeq9o.cloudfront.net/2330dbs0n8m3chkkr25gkkcd8pnj3lk2
233hvnrjoqu14jltk6lhbhf2tj11f8un  false    https://oidc-r7u1.s3.us-east-1.amazonaws.com                           aws:secretsmanager:us-east-1:242819244:secret:rosa-private-key-oidc-r7u1-tM3MDN
----

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-oidc-overview.adoc
// * rosa_architecture/rosa-sts-about-iam-resources.adoc

[id="rosa-sts-byo-oidc-options_{context}"]
= Parameter options for creating your own OpenID Connect configuration

The following options may be added to the `rosa create oidc-config` command. All of these parameters are optional. Running the `rosa create oidc-config` command without parameters creates an unmanaged OIDC configuration.

[NOTE]
====
You are required to register the unmanaged OIDC configuration by posting a request to `/oidc_configs` through OpenShift Cluster Manager. You receive an ID in the response. Use this ID to create a cluster.
====

[id="rosa-sts-byo-oidc-raw-files_{context}"]
== raw-files

Allows you to provide raw files for the private RSA key. This key is named `rosa-private-key-oidc-<random_label_of_length_4>.key`. You also receive a discovery document, named `discovery-document-oidc-<random_label_of_length_4>.json`, and a JSON Web Key Set, named `jwks-oidc-<random_label_of_length_4>.json`.

You use these files to set up the endpoint. This endpoint responds to `/.well-known/openid-configuration` with the discovery document and on `keys.json` with the JSON Web Key Set. The private key is stored in Amazon Web Services (AWS) Secrets Manager Service (SMS) as plaintext.

.Example
[source,terminal]
----
$ rosa create oidc-config --raw-files
----

[id="rosa-sts-byo-oidc-mode_{context}"]
== mode

Allows you to specify the mode to create your OIDC configuration. With the `manual` option, you receive AWS commands that set up the OIDC configuration in an S3 bucket. This option stores the private key in the Secrets Manager. With the `manual` option, the OIDC Endpoint URL is the URL for the S3 bucket. You must retrieve the Secrets Manager ARN to register the OIDC configuration with OpenShift Cluster Manager.

You receive the same OIDC configuration and AWS resources as the `manual` mode when using the `auto` option. A significant difference between the two options is that when using the `auto` option, ROSA calls AWS, so you do not need to take any further actions. The OIDC Endpoint URL is the URL for the S3 bucket. The CLI retrieves the Secrets Manager ARN, registers the OIDC configuration with OpenShift Cluster Manager, and reports the second `rosa` command that the user can run to continue with the creation of the STS cluster.

.Example
[source,terminal]
----
$ rosa create oidc-config --mode=<auto|manual>
----

[id="rosa-sts-byo-oidc-managed_{context}"]
== managed

Creates an OIDC configuration that is hosted under Red{nbsp}Hat's AWS account. This command creates a private key that responds directly with an OIDC Config ID for you to use when creating the STS cluster.

.Example
[source,terminal]
----
$ rosa create oidc-config --managed
----

.Example output
[source,terminal]
----
W: For a managed OIDC Config only auto mode is supported. However, you may choose the provider creation mode
? OIDC Provider creation mode: auto
I: Setting up managed OIDC configuration
I: Please run the following command to create a cluster with this oidc config
rosa create cluster --sts --oidc-config-id 233jnu62i9aphpucsj9kueqlkr1vcgra
I: Creating OIDC provider using 'arn:aws:iam::242819244:user/userName'
? Create the OIDC provider? Yes
I: Created OIDC provider with ARN 'arn:aws:iam::242819244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/233jnu62i9aphpucsj9kueqlkr1vcgra'
----

// Module included in the following assemblies:
//
// * rosa_architecture/rosa-sts-about-iam-resources.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-oidc-overview.adoc
// * rosa_planning/rosa-hcp-prepare-iam-resources.adoc
[id="rosa-sts-oidc-provider-for-operators-aws-cli_{context}"]
= Creating an OIDC provider using the CLI

You can create an OIDC provider that is hosted in your AWS account with the OpenShift Container Platform (ROSA) CLI, `rosa`.

.Prerequisites

* You have installed the latest version of the ROSA CLI.

.Procedure

* To create an OIDC provider, by using an unregistered or a registered OIDC configuration.
** Unregistered OIDC configurations require you to create the OIDC provider through the cluster. Run the following to create the OIDC provider:
+
[source,terminal]
----
$ rosa create oidc-provider --mode manual --cluster <cluster_name>
----
+
[NOTE]
====
When using `manual` mode, the `aws` command is printed to the terminal for your review. After reviewing the `aws` command, you must run it manually. Alternatively, you can specify `--mode auto` with the `rosa create` command to run the `aws` command immediately.
====
+
.Command output
[source,terminal]
----
aws iam create-open-id-connect-provider \
	--url https://oidc.op1.openshiftapps.com/<oidc_config_id> \// <1>
	--client-id-list openshift sts.<aws_region>.amazonaws.com \
	--thumbprint-list <thumbprint> <2>
----
<1> The URL used to reach the OpenID Connect (OIDC) identity provider after the cluster is created.
<2> The thumbprint is generated automatically when you run the `rosa create oidc-provider` command. For more information about using thumbprints with AWS Identity and Access Management (IAM) OIDC identity providers, see the AWS documentation.

** Registered OIDC configurations use an OIDC configuration ID. Run the following command with your OIDC configuration ID:
+
[source,terminal]
----
$ rosa create oidc-provider --oidc-config-id <oidc_config_id> --mode auto -y
----
+
.Command output
[source,terminal]
----
I: Creating OIDC provider using 'arn:aws:iam::4540112244:user/userName'
I: Created OIDC provider with ARN 'arn:aws:iam::4540112244:oidc-provider/dvbwgdztaeq9o.cloudfront.net/241rh9ql5gpu99d7leokhvkp8icnalpf'
----

[role="_additional-resources"]
[id="additional-resources_rosa-oidc-config"]
== Additional resources

* Creating an OpenID Connect Configuration
* Creating an OpenID Connect Configuration
