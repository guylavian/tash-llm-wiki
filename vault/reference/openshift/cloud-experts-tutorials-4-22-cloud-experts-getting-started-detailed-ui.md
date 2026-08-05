---
title: "Tutorial: Detailed UI guide"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-getting-started-detailed-ui
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-getting-started-detailed-ui
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Detailed UI guide

[id="cloud-experts-getting-started-detailed-ui"]
= Tutorial: Detailed UI guide

[role="_abstract"]
This tutorial outlines the detailed steps to deploy a OpenShift Container Platform cluster using the Red{nbsp}Hat OpenShift Cluster Manager user interface (UI).

== Deployment workflow
The overall deployment workflow follows these steps:

. Create the account wide roles and policies.
. Associate your AWS account with your Red{nbsp}Hat account.
.. Create and link the Red{nbsp}Hat OpenShift Cluster Manager role.
.. Create and link the user role.
. Create the cluster.

Step 1 only needs to be performed the *first time* you are deploying into an AWS account. Step 2 only needs to be performed the *first time* you are using the UI. For successive clusters of the same y-stream version, you only need to create the cluster.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-cluster-roles_{context}"]
= Creating account wide roles

[role="_abstract"]
You create your account wide roles to create your cluster by using the {rosa-cli-first} tool.

[NOTE]
====
If you already have account roles from an earlier deployment, skip this step. The UI will detect your existing roles after you select an associated AWS account.
====

If this is the _first time_ you are deploying OpenShift Container Platform in this account and you have _not_ yet created the account roles, create the account-wide roles and policies, including the Operator policies.

.Procedure
* In your terminal, run the following command to create the account-wide roles:
+
[source,terminal]
----
$ rosa create account-roles --mode auto --yes
----
+
**Example output**
+
[source,terminal]
----
I: Creating roles using 'arn:aws:iam::000000000000:user/rosa-user'
I: Created role 'ManagedOpenShift-ControlPlane-Role' with ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-ControlPlane-Role'
I: Created role 'ManagedOpenShift-Worker-Role' with ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-Worker-Role'
I: Created role 'ManagedOpenShift-Support-Role' with ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-Support-Role'
I: Created role 'ManagedOpenShift-Installer-Role' with ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-Installer-Role'
I: Created policy with ARN 'arn:aws:iam::000000000000:policy/ManagedOpenShift-openshift-machine-api-aws-cloud-credentials'
I: Created policy with ARN 'arn:aws:iam::000000000000:policy/ManagedOpenShift-openshift-cloud-credential-operator-cloud-crede'
I: Created policy with ARN 'arn:aws:iam::000000000000:policy/ManagedOpenShift-openshift-image-registry-installer-cloud-creden'
I: Created policy with ARN 'arn:aws:iam::000000000000:policy/ManagedOpenShift-openshift-ingress-operator-cloud-credentials'
I: Created policy with ARN 'arn:aws:iam::000000000000:policy/ManagedOpenShift-openshift-cluster-csi-drivers-ebs-cloud-credent'
I: To create a cluster with these roles, run the following command:
rosa create cluster --sts
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-associate-associate-roles_{context}"]
= Creating and associating an {cluster-manager} role

[role="_abstract"]
Create and associate an {cluster-manager} role to enable cluster management through the {cluster-manager} {hybrid-console-second}.

.Procedure
. Run the following command to see if an {cluster-manager} role exists:
+
[source,terminal]
----
$ rosa list ocm-role
----

. The UI displays the commands to create an {cluster-manager} role with two different levels of permissions:
+
* *Basic {cluster-manager} role:* Allows the {cluster-manager} to have read-only access to the account to check if the roles and policies that are required by OpenShift Container Platform are present before creating a cluster. You will need to manually create the required roles, policies, and OIDC provider using the CLI.
* *Admin {cluster-manager} role:* Grants the {cluster-manager} additional permissions to create the required roles, policies, and OIDC provider for OpenShift Container Platform. Using this makes the deployment of a OpenShift Container Platform cluster quicker since the {cluster-manager} will be able to create the required resources for you.
+
To read more about these roles, see the "{cluster-manager} roles and permissions" documentation in the _Additional resources_.
+
For the purposes of this tutorial, use the *Admin {cluster-manager} role* for the simplest and quickest approach.

. Copy the command to create the Admin {cluster-manager} role from the sidebar or switch to your terminal and enter the following command:
+
[source,terminal]
----
$ rosa create ocm-role --mode auto --admin --yes
----
+
This command creates the {cluster-manager} role and associates it with your Red{nbsp}Hat account.
+
**Example output**
+
[source,terminal]
----
I: Creating ocm role
I: Creating role using 'arn:aws:iam::000000000000:user/rosa-user'
I: Created role 'ManagedOpenShift-OCM-Role-12561000' with ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-OCM-Role-12561000'
I: Linking OCM role
I: Successfully linked role-arn 'arn:aws:iam::000000000000:role/ManagedOpenShift-OCM-Role-12561000' with organization account '1MpZfntsZeUdjWHg7XRgP000000'
----

. Click *Step 2: User role*.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-associate-ocm-role_{context}"]
= Creating and associating an {cluster-manager} role

[role="_abstract"]

You need the {cluster-manager} role to create your cluster.

.Procedure
. Run the following command to see if an {cluster-manager} role exists:
+
[source,terminal]
----
$ rosa list ocm-role
----

. The UI displays the commands to create an {cluster-manager} role with two different levels of permissions:
+
* *Basic {cluster-manager} role:* Allows the {cluster-manager} to have read-only access to the account to check if the roles and policies that are required by OpenShift Container Platform are present before creating a cluster. You will need to manually create the required roles, policies, and OIDC provider using the CLI.
* *Admin {cluster-manager} role:* Grants the {cluster-manager} additional permissions to create the required roles, policies, and OIDC provider for OpenShift Container Platform. Using this makes the deployment of a OpenShift Container Platform cluster quicker since the {cluster-manager} will be able to create the required resources for you.
+
To read more about these roles, see the "{cluster-manager} roles and permissions" documentation in the _Additional resources_.
+
For the purposes of this tutorial, use the *Admin {cluster-manager} role* for the simplest and quickest approach.

. Copy the command to create the Admin {cluster-manager} role from the sidebar or switch to your terminal and enter the following command:
+
[source,terminal]
----
$ rosa create ocm-role --mode auto --admin --yes
----
+
This command creates the {cluster-manager} role and associates it with your Red{nbsp}Hat account.
+
**Example output**
+
[source,terminal]
----
I: Creating ocm role
I: Creating role using 'arn:aws:iam::000000000000:user/rosa-user'
I: Created role 'ManagedOpenShift-OCM-Role-12561000' with ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-OCM-Role-12561000'
I: Linking OCM role
I: Successfully linked role-arn 'arn:aws:iam::000000000000:role/ManagedOpenShift-OCM-Role-12561000' with organization account '1MpZfntsZeUdjWHg7XRgP000000'
----

. Click *Step 2: User role*.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-other-cluster-roles_{context}"]
= Other {cluster-manager} role creation options

[role="_abstract"]
You can use the {rosa-cli} tool to create your cluster roles.

.Procedure
* *Manual mode:* If you prefer to run the AWS CLI commands yourself, you can define the mode as `manual` rather than `auto`. The CLI will output the AWS commands and the relevant JSON files are created in the current directory.
+
Use the following command to create the {cluster-manager} role in manual mode:
+
[source,terminal]
----
$ rosa create ocm-role --mode manual --admin --yes
----
* *Basic {cluster-manager} role:* If you prefer that the {cluster-manager} has read only access to the account, create a basic {cluster-manager} role. You will then need to manually create the required roles, policies, and OIDC provider using the CLI.
+
Use the following command to create a Basic {cluster-manager} role:
+
[source,terminal]
----
$ rosa create ocm-role --mode auto --yes
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-ocm-manager-role_{context}"]
= Creating an {cluster-manager} user role

[role="_abstract"]
The user role needs to be created so that OpenShift Container Platform can verify your AWS identity. This role has no permissions, and it is only used to create a trust relationship between the installation program account and your {cluster-manager} role resources. For more information, see the user role documentation in _Additional resources_.

.Procedure
. Check if a user role already exists by running the following command:
+
[source,terminal]
----
$ rosa list user-role
----

. Run the following command to create the user role and to link it to your Red{nbsp}Hat account:
+
[source,terminal]
----
$ rosa create user-role --mode auto --yes
----
+
**Example output**
+
[source,terminal]
----
I: Creating User role
I: Creating ocm user role using 'arn:aws:iam::000000000000:user/rosa-user'
I: Created role 'ManagedOpenShift-User-rosa-user-Role' with ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-User-rosa-user-Role'
I: Linking User role
I: Successfully linked role ARN 'arn:aws:iam::000000000000:role/ManagedOpenShift-User-rosa-user-Role' with account '1rbOQez0z5j1YolInhcXY000000'
----
+
[NOTE]
====
As before, you can define `--mode manual` if you'd prefer to run the AWS CLI commands yourself. The CLI outputs the AWS commands and the relevant JSON files are created in the current directory. Make sure to link the role.
====

. Click *Step 3: Account roles*.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-account-roles_{context}"]
= Creating account roles

[role="_abstract"]
You can create your account roles using the {rosa-cli} tool.

.Procedure
. Create your account roles by running the following command:
+
[source,terminal]
----
$ rosa create account-roles --mode auto
----

. Click *OK* to close the sidebar.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-confirm-assocation_{context}"]
= Confirming successful account association

[role="_abstract"]
You should now see your AWS account in the *Associated AWS infrastructure account* dropdown menu.

.Procedure
. If you see your account, account association was successful.
. Select the account.
. You will see the account role ARNs populated below.
+
image::cloud-experts-getting-started-rosa-deployment-detailed-ui-account-roles.png[]

. Click *Next*.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-create-cluster_{context}"]
= Creating the cluster

[role="_abstract"]
This tutorial uses the default options for creating a cluster.

.Procedure
. In **Cluster settings**, select:
+
* Cluster name: **<pick a name\>**
* Version: **<select latest version\>**
* Region: **<select region\>**
* Availability: **Single zone**
* Enable user workload monitoring: **leave checked**
* Enable additional etcd encryption: **leave unchecked**
* Encrypt persistent volumes with customer keys: **leave unchecked**

. Click *Next*.

. Leave the default settings on for the machine pool:
+
* Compute node instance type: **m5.xlarge - 4 vCPU 16 GiB RAM**
* Enable autoscaling: **unchecked**
* Compute node count: **2**
* Leave node labels blank

. Click *Next*.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-installation-details_{context}"]
= Finalizing cluster creation

[role="_abstract"]
You can select the defaults to complete cluster installation.

.Procedure
. For **Networking**, leave all the default values for configuration.
. Click *Next*.
. Leave all the default values for CIDR ranges.
. Click *Next*.
. For **Cluster roles and policies**, leave *Auto* selected. It makes the cluster deployment process simpler and quicker.
+
[NOTE]
====
If you selected a *Basic {cluster-manager} role* earlier, you can only use manual mode. You must manually create the operator roles and OIDC provider. See the "Basic {cluster-manager} role" section below after you have completed the "Cluster updates" section and started cluster creation.
====
+
Leave all of the **Cluster update** options at default in this section.

. Review the content for the cluster configuration.
. Click *Create cluster*.
. Stay on the current page to monitor the installation progress. It should take about 40 minutes.
+
image::cloud-experts-getting-started-rosa-deployment-detailed-ui-cluster-create.png[]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-getting-started/cloud-experts-getting-started-deploying/cloud-experts-getting-started-detailed-ui.adoc

[id="cloud-experts-getting-started-detailed-ui-admin-role_{context}"]
= Basic OpenShift Cluster Manager Role

[role="_abstract"]
You need to create the Operator roles to manage your cluster.

[NOTE]
====
If you created an *Admin OpenShift Cluster Manager role* as directed above *ignore* this entire section. The OpenShift Cluster Manager will create the resources for you.

If you created a *Basic OpenShift Cluster Manager role* earlier, you will need to manually create two more elements before cluster installation can continue:

* Operator roles
* OIDC provider
====

.Procedure
. A pop up window will show you the commands to run.
+
image::cloud-experts-getting-started-rosa-deployment-detailed-ui-create-cmds.png[]

. Run the commands from the window in your terminal to launch interactive mode. Or, for simplicity, run the following command to create the Operator roles:
+
[source,terminal]
----
$ rosa create operator-roles --mode auto --cluster <cluster-name> --yes
----
+
**Example output**
+
[source,terminal]
----
I: Creating roles using 'arn:aws:iam::000000000000:user/rosauser'
I: Created role 'rosacluster-b736-openshift-ingress-operator-cloud-credentials' with ARN 'arn:aws:iam::000000000000:role/rosacluster-b736-openshift-ingress-operator-cloud-credentials'
I: Created role 'rosacluster-b736-openshift-cluster-csi-drivers-ebs-cloud-credent' with ARN 'arn:aws:iam::000000000000:role/rosacluster-b736-openshift-cluster-csi-drivers-ebs-cloud-credent'
I: Created role 'rosacluster-b736-openshift-cloud-network-config-controller-cloud' with ARN 'arn:aws:iam::000000000000:role/rosacluster-b736-openshift-cloud-network-config-controller-cloud'
I: Created role 'rosacluster-b736-openshift-machine-api-aws-cloud-credentials' with ARN 'arn:aws:iam::000000000000:role/rosacluster-b736-openshift-machine-api-aws-cloud-credentials'
I: Created role 'rosacluster-b736-openshift-cloud-credential-operator-cloud-crede' with ARN 'arn:aws:iam::000000000000:role/rosacluster-b736-openshift-cloud-credential-operator-cloud-crede'
I: Created role 'rosacluster-b736-openshift-image-registry-installer-cloud-creden' with ARN 'arn:aws:iam::000000000000:role/rosacluster-b736-openshift-image-registry-installer-cloud-creden'
----
[id="cloud-experts-getting-started-detailed-ui-oidc-provider_{context}"]
= Creating the OIDC provider

[role="_abstract"]
You need to use the {rosa-cli} tool to create your OpenID Connect provider for your cluster.

.Procedure
* In your terminal, run the following command to create the OIDC provider:
+
[source,terminal]
----
$ rosa create oidc-provider --mode auto --cluster <cluster-name> --yes
----
+
**Example output**
+
[source,terminal]
----
I: Creating OIDC provider using 'arn:aws:iam::000000000000:user/rosauser'
I: Created OIDC provider with ARN 'arn:aws:iam::000000000000:oidc-provider/rh-oidc.s3.us-east-1.amazonaws.com/1tt4kvrr2kha2rgs8gjfvf0000000000'
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* User role documentation
* OpenShift Cluster Manager roles and permissions
