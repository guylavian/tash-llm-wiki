---
title: "Configuring an Azure Stack Hub account"
type: reference
domain: openshift
slug: installing-4-22-installing-azure-stack-hub-account
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-azure-stack-hub-account
version: 4.22
family: installing
documentKind: "Documentation"
---

# Configuring an Azure Stack Hub account

[id="installing-azure-stack-hub-account"]
= Configuring an Azure Stack Hub account

Before you can install OpenShift Container Platform, you must configure a Microsoft Azure account.

[IMPORTANT]
====
All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see Resolve reserved resource name errors in the Azure documentation.
====

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-account.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-limits_{context}"]
= {cp} account limits

The OpenShift Container Platform cluster uses a number of Microsoft {cp} components, and the default Azure subscription and service limits, quotas, and constraints affect your ability to install OpenShift Container Platform clusters.

[IMPORTANT]
====
Default limits vary by offer category types, such as Free Trial and Pay-As-You-Go, and by series, such as Dv2, F, and G. For example, the default for Enterprise Agreement subscriptions is 350 cores.

Check the limits for your subscription type and if necessary, increase quota limits for your account before you install a default
cluster on Azure.
====
The OpenShift Container Platform cluster uses a number of Microsoft Azure Stack Hub components, and the default Quota types in Azure Stack Hub affect your ability to install OpenShift Container Platform clusters.

The following table summarizes the {cp} components whose limits can impact your
ability to install and run OpenShift Container Platform clusters.

[cols="2a,3a,3a,8a",options="header"]
|===
|Component |Number of components required by default| Default {cp} limit |Description
[cols="2a,3a,8a",options="header"]
|===
|Component |Number of components required by default |Description

|vCPU
|44
|40
|20 per region
|A default cluster requires 44 vCPUs, so you must increase the account limit.
|A default cluster requires 40 vCPUs, so you must increase the account limit.

By default, each cluster creates the following instances:

* One bootstrap machine, which is removed after installation
* Three control plane machines
* Three compute machines

Because the bootstrap and control plane machines use `Standard_D8s_v3` virtual
machines, which use 8 vCPUs, and the compute machines use `Standard_D4s_v3`
virtual machines, which use 4 vCPUs, a default cluster requires 44 vCPUs.
The bootstrap node VM, which uses 8 vCPUs, is used only during installation.
Because the bootstrap machine uses `Standard_D4s_v3` machines, which use 4 vCPUs,
the control plane machines use `Standard_D8s_v3` virtual
machines, which use 8 vCPUs, and the worker machines use `Standard_D4s_v3`
virtual machines, which use 4 vCPUs, a default cluster requires 40 vCPUs.
The bootstrap node VM, which uses 4 vCPUs, is used only during installation.
|56
|A default cluster requires 56 vCPUs, so you must increase the account limit.

By default, each cluster creates the following instances:

* One bootstrap machine, which is removed after installation
* Three control plane machines
* Three compute machines

Because the bootstrap, control plane, and worker machines use `Standard_DS4_v2` virtual machines, which use 8 vCPUs, a default cluster requires 56 vCPUs. The bootstrap node VM is used only during installation.

To deploy more worker nodes, enable autoscaling, deploy large workloads, or use
a different instance type, you must further increase the vCPU limit for your
account to ensure that your cluster can deploy the machines that you require.

|OS Disk
|7
|
|Each cluster machine must have a minimum of 100 GB of storage and 300 IOPS.
[NOTE]
====
Faster storage is recommended for production clusters and clusters with intensive workloads. For more information about optimizing storage for performance, see the page titled "Optimizing storage" in the "Scalability and performance" section.
====

|VNet
| 1
| 1000 per region
| Each default cluster requires one Virtual Network (VNet), which contains two
subnets.

|Network interfaces
|7
|65,536 per region
|Each default cluster requires seven network interfaces. If you create more
machines or your deployed workloads create load balancers, your cluster uses
more network interfaces.

|Network security groups
|2
|5000
| Each cluster creates network security groups for each subnet in the VNet.
The default cluster creates network
security groups for the control plane and for the compute node subnets:

[horizontal]
 `controlplane`:: Allows the control plane machines to be reached on port 6443
 from anywhere
`node`:: Allows worker nodes to be reached from the internet on ports 80 and 443

|Network load balancers
| 3
| 1000 per region
|Each cluster creates the following
load balancers:

[horizontal]
`default`:: Public IP address that load balances requests to ports 80 and 443 across worker machines
`internal`:: Private IP address that load balances requests to ports 6443 and 22623 across control plane machines
`external`:: Public IP address that load balances requests to port 6443 across control plane machines

If your applications create more Kubernetes `LoadBalancer` service objects,
your cluster uses more load balancers.

|Public IP addresses
|3
|
|Each of the two public load balancers uses a public IP address. The bootstrap
machine also uses a public IP address so that you can SSH into the
machine to troubleshoot issues during installation. The IP address for the
bootstrap node is used only during installation.
|2
|The public load balancer uses a public IP address. The bootstrap
machine also uses a public IP address so that you can SSH into the
machine to troubleshoot issues during installation. The IP address for the
bootstrap node is used only during installation.

|Private IP addresses
|7
|
|The internal load balancer, each of the three control plane machines, and each
of the three worker machines each use a private IP address.

|Spot VM vCPUs (optional)
|0

If you configure spot VMs, your cluster must have two spot VM vCPUs for every compute node.
|20 per region
|This is an optional component. To use spot VMs, you must increase the Azure default limit to at least twice the number of compute nodes in your cluster.
[NOTE]
====
Using spot VMs for control plane nodes is not recommended.
====
|===

To increase an account limit, file a support request on the Azure portal. For more information, see Request a quota limit increase for Azure Deployment Environments resources.

[role="_additional-resources"]
.Additional resources

* Optimizing storage

// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc

[id="installation-azure-stack-hub-network-config_{context}"]
= Configuring a DNS zone in Azure Stack Hub

To successfully install OpenShift Container Platform on Azure Stack Hub, you must create DNS records in an Azure Stack Hub DNS zone. The DNS zone must be authoritative for the domain. To delegate a registrar's DNS zone to Azure Stack Hub, see Microsoft's documentation for Azure Stack Hub datacenter DNS integration.

// Module included in the following assemblies:
//
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc

[id="installation-azure-stack-hub-permissions_{context}"]
= Required Azure Stack Hub roles

Your Microsoft Azure Stack Hub account must have the following roles for the subscription that you use:

* `Owner`

To set roles on the Azure portal, see the Manage access to resources in Azure Stack Hub with role-based access control in the Microsoft documentation.

// Module included in the following assemblies:
//
// * installing/installing_azure/installing-azure-account.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-account.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc

[id="installation-azure-service-principal_{context}"]
= Creating a service principal

Because OpenShift Container Platform and its installation program create Microsoft Azure resources by using the Azure Resource Manager, you must create a service principal to represent it.

.Prerequisites

* Install or update the Azure CLI.
* Your Azure account has the required roles for the subscription that you use.
* If you want to use a custom role, you have created a custom role with the required permissions listed in the _Required Azure permissions for installer-provisioned infrastructure_ section.
* If you want to use a custom role, you have created a custom role with the required permissions listed in the _Required Azure permissions for user-provisioned infrastructure_ section.

.Procedure

. Register your environment:
+
[source,terminal]
----
$ az cloud register -n AzureStackCloud --endpoint-resource-manager <endpoint> <1>
----
<1> Specify the Azure Resource Manager endpoint, \`https://management.<region>.<fqdn>/`.
+
See the Microsoft documentation for details.

. Set the active environment:
+
[source,terminal]
----
$ az cloud set -n AzureStackCloud
----

. Update your environment configuration to use the specific API version for Azure Stack Hub:
+
[source,terminal]
----
$ az cloud update --profile 2019-03-01-hybrid
----

. Log in to the Azure CLI:
+
[source,terminal]
----
$ az login
----
+
If you are in a multitenant environment, you must also supply the tenant ID.

. If your Azure account uses subscriptions, ensure that you are using the right
subscription:

.. View the list of available accounts and record the `tenantId` value for the
subscription you want to use for your cluster:
+
[source,terminal]
----
$ az account list --refresh
----
+
.Example output
[source,terminal]
----
[
  {
    "cloudName": "AzureCloud",
    "cloudName": AzureStackCloud",
    "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
    "isDefault": true,
    "name": "Subscription Name",
    "state": "Enabled",
    "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee",
    "user": {
      "name": "you@example.com",
      "type": "user"
    }
  }
]
----

.. View your active account details and confirm that the `tenantId` value matches
the subscription you want to use:
+
[source,terminal]
----
$ az account show
----
+
.Example output
[source,terminal]
----
{
  "environmentName": "AzureCloud",
  "environmentName": AzureStackCloud",
  "id": "9bab1460-96d5-40b3-a78e-17b15e978a80",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "6057c7e9-b3ae-489d-a54e-de3f6bf6a8ee", <1>
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
----
<1> Ensure that the value of the `tenantId` parameter is the correct subscription ID.

.. If you are not using the right subscription, change the active subscription:
+
[source,terminal]
----
$ az account set -s <subscription_id> <1>
----
<1> Specify the subscription ID.

.. Verify the subscription ID update:
+
[source,terminal]
----
$ az account show
----
+
.Example output
[source,terminal]
----
{
  "environmentName": "AzureCloud",
  "environmentName": AzureStackCloud",
  "id": "33212d16-bdf6-45cb-b038-f6565b61edda",
  "isDefault": true,
  "name": "Subscription Name",
  "state": "Enabled",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee",
  "user": {
    "name": "you@example.com",
    "type": "user"
  }
}
----

. Record the `tenantId` and `id` parameter values from the output. You need these values during the OpenShift Container Platform installation.

. Create the service principal for your account:
+
[source,terminal]
----
$ az ad sp create-for-rbac --role Contributor --name <service_principal> \ <1>
  --scopes /subscriptions/<subscription_id> <2>
  --years <years> <3>
----
<1> Specify the service principal name.
<2> Specify the subscription ID.
<3> Specify the number of years. By default, a service principal expires in one year. By using the `--years` option you can extend the validity of your service principal.
+
.Example output
[source,terminal]
----
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
}
----

. Create the service principal for your account:
+
[source,terminal]
----
$ az ad sp create-for-rbac --role <role_name> \// <1>
     --name <service_principal> \// <2>
     --scopes /subscriptions/<subscription_id> <3>
----
<1> Defines the role name. You can use the `Contributor` role, or you can specify a custom role which contains the necessary permissions.
<2> Defines the service principal name.
<3> Specifies the subscription ID.
+
.Example output
[source,terminal]
----
Creating 'Contributor' role assignment under scope '/subscriptions/<subscription_id>'
The output includes credentials that you must protect. Be sure that you do not
include these credentials in your code or check the credentials into your source
control. For more information, see https://aka.ms/azadsp-cli
{
  "appId": "ac461d78-bf4b-4387-ad16-7e32e328aec6",
  "displayName": <service_principal>",
  "password": "00000000-0000-0000-0000-000000000000",
  "tenantId": "8049c7e9-c3de-762d-a54e-dc3f6be6a7ee"
}
----

. Record the values of the `appId` and `password` parameters from the previous
output. You need these values during OpenShift Container Platform installation.

. If you applied the `Contributor` role to your service principal, assign the `User Administrator Access` role by running the following command:
+
[source,terminal]
----
$ az role assignment create --role "User Access Administrator" \
  --assignee-object-id $(az ad sp show --id <appId> --query id -o tsv) <1>
----
<1> Specify the `appId` parameter value for your service principal.

[role="_additional-resources"]
.Additional resources

* About the Cloud Credential Operator

[id="next-steps_installing-azure-stack-hub-account"]
== Next steps

* Install an OpenShift Container Platform cluster:
** Installing a cluster on Azure Stack Hub with customizations
** Install an OpenShift Container Platform cluster on Azure Stack Hub with user-provisioned infrastructure by following Installing a cluster on Azure Stack Hub using ARM templates.
