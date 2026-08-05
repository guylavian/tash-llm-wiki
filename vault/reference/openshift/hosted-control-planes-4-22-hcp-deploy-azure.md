---
title: "Deploying {hcp} on {azure-short}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-deploy-azure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-deploy-azure
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Deploying {hcp} on {azure-short}

[id="hcp-deploy-azure"]
= Deploying {hcp} on {azure-short}

[role="_abstract"]
With {hcp} on {azure-first}, you can reduce the cost associated with dedicated control-plane node VMs for each cluster. You can provision compute nodes as {azure-short} Virtual Machine Scale sets for dynamic scaling, and ensure credential isolation with per-cluster {azure-short} service principals.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-overview_{context}"]
= Overview of {hcp} on {azure-short}

[role="_abstract"]
You can deploy and manage hosted clusters on an OpenShift management cluster that runs in {azure-first}. With a self-managed deployment model, you manage your own OpenShift cluster.

[id="hcp-azure-arch_{context}"]
== Architecture of {hcp} on {azure-short}

At a high level, the architecture of {hcp} on {azure-short} consists of three layers:

Management cluster:: An {azure-short} OpenShift cluster that hosts the HyperShift Operator and the control planes for your hosted clusters.
Control plane:: Kubernetes control-plane components that run as pods on the management cluster.
Data plane:: Compute nodes that run as {azure-short} virtual machines (VMs) in your {azure-short} subscription.

The architecture uses {azure-short} Workload Identity for secure, credential-free authentication between OpenShift Container Platform components and {azure-short} services. As a result, you do not need to manage long-lived service principal credentials, and you get better security through federated identity credentials.

[id="hcp-azure-deployment-workflow_{context}"]
== Deployment workflow for {hcp} on {azure-short}

Deploying self-managed {hcp} on {azure-short} involves a three-phase process in the following order:

Phase 1: Set up {azure-short} Workload Identity:: This phase establishes secure authentication infrastructure so that OpenShift Container Platform components can access {azure-short} services. During this phase, the security infrastructure that your hosted clusters require is created:
+
* Managed identities for each OpenShift Container Platform component, including the image registry, ingress, CSI drivers, cloud provider, network operator, and so on
* OIDC issuer in {azure-short} Blob Storage for service account token validation
* Federated credentials that establish trust relationships between {azure-short} Entra ID and OpenShift Container Platform service accounts

Phase 2: Set up the management cluster:: In this phase, you prepare your OpenShift Container Platform management cluster on {azure-short} to host and manage hosted clusters. During this phase, you install the following components:
+
* {azure-short} DNS zones, for private and public-private topologies
* External DNS, for private and public-private topologies
* HyperShift Operator

Phase 3: Create hosted clusters:: In this phase, you create and configure hosted clusters. This phase involves the following steps:
+
.. Setting up infrastructure
.. Creating a hosted cluster
.. Integrating workload identity
.. Configuring private endpoint access (optional)

[role="_additional-resources"]
.Additional resources

* {azure-short} Workload Identity documentation

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-infra-creds_{context}"]
= {azure-short} infrastructure and credentials

[role="_abstract"]
Before you get started with {hcp} on {azure-first}, get familiar with the required {azure-short} resources and the necessary permissions.

[id="hcp-azure-prereq-summary_{context}"]
== Summary of requirements

You need the following resources, tools, access, and permissions to set up {hcp} on {azure-short}:

{azure-short} resources::

** An OpenShift Container Platform management cluster on {azure-short}.
** An {azure-short} subscription with contributor and user-access administrator permissions.
** (Optional) A parent DNS zone in {azure-short} for delegating cluster DNS records. This DNS zone is required only if you plan to use external DNS.

Tools and access::

** {azure-short} command-line interface (CLI), `az`, configured with your subscription
** {oc-first}
** {hcp} CLI, `hcp`
** `jq` command-line JSON processor
** Cloud Credential Operator utility (`ccoctl`)
** A valid OpenShift Container Platform pull secret

Permissions::

** Subscription-level contributor and user access administrator roles
** Microsoft Graph API permissions for creating service principals

[id="hcp-azure-dns-options_{context}"]
== DNS management options

You can set up {hcp} on {azure-short} with or without external DNS. If you plan to use a private or a public-private topology, external DNS is required. See the following table for more information:

.DNS approaches for {hcp} on {azure-short}
[cols="3",options="header"]
|===
| |With external DNS |Without external DNS

|*Best for*
|Production, multi-cluster
|Development, testing

|*API server DNS*
|Custom (`api-cluster.example.com`)
|{azure-short} Load Balancer (`abc123.region.cloudapp.azure.com`)

|*Setup complexity*
|Low, requires DNS zones and service principals
|None

|*Management*
|Fully automatic
|Manual or {azure-short}-provided

|===

[id="hcp-azure-resource-group_{context}"]
== Resource group strategy

Cluster-specific resource groups are created and deleted with each hosted cluster. These resources include managed resource groups for cluster infrastructure. If you use custom networking, these resources also include Virtual Network (VNet) resource groups and Network Security Group (NSG) resource groups.

[id="hcp-azure-security_{context}"]
== Security considerations for {hcp} on {azure-short}

{hcp-capital} on {azure-short} employs the following security best practices:

* Workload identity federation, which eliminates long-lived credentials by using OIDC-based authentication.
* Least-privilege access, where each component has its own managed identity with minimal required permissions.
* Network isolation, where you can use custom VNets and NSGs to implement network segmentation and security policies.
* Federated credentials, where trust relationships are scoped to specific service accounts, preventing unauthorized access.
* Private connectivity, available as an option through Azure Private Link, which provides private API server access to ensure that control-plane traffic never traverses the public internet. Private connectivity is available for private and public-private topologies only.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-setup-resources_{context}"]
= Setting up {azure-short} resources

[role="_abstract"]
Before you can create management and hosted clusters for your deployment of {hcp} on {azure-short}, you need to set up an OIDC issuer, Workload Identities, and your {azure-short} infrastructure.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-oidc_{context}"]
= Setting up an OIDC issuer

[role="_abstract"]
To prepare to deploy {hcp} on {azure-short}, you need to set up an OIDC issuer for hosted clusters.

.Prerequisites

* The {azure-short} command-line interface (CLI) is installed and configured.
* The `jq` command-line JSON processor is installed.
* The Cloud Credential Operator utility (`ccoctl`) is installed. For more information, see "How to obtain the ccoctl tool for OpenShift 4".
* The appropriate {azure-short} permissions are set.

.Procedure

. Set your environment variables as shown in the following example:
+
[source,terminal]
----
PERSISTENT_RG_NAME="os4-common"
LOCATION="eastus"
AZURE_CREDS="/path/to/azure-creds.json"
SUBSCRIPTION_ID="my-subscription-id"
----

. Create a persistent resource group by entering the following command:
+
[source,terminal]
----
$ az group create --name $PERSISTENT_RG_NAME --location $LOCATION
----

. Configure an OIDC issuer URL by using the Cloud Credential Operator tool to complete the following steps:
+
.. Set the OIDC issuer variables as shown in the following example:
+
[source,terminal]
----
OIDC_STORAGE_ACCOUNT_NAME="yourstorageaccount"
TENANT_ID="your-tenant-id"
----
+
.. Create an RSA key pair and save the private and public key by entering the following command:
+
[source,terminal]
----
$ ccoctl azure create-key-pair
----
+
.. Set variables for the token issuer key paths as shown in the following example:
+
[source,terminal]
----
SA_TOKEN_ISSUER_PRIVATE_KEY_PATH="/path/to/serviceaccount-signer.private"
SA_TOKEN_ISSUER_PUBLIC_KEY_PATH="/path/to/serviceaccount-signer.public"
----
+
.. Create an OIDC issuer by entering the following command:
+
[source,terminal]
----
$ ccoctl azure create-oidc-issuer \
    --oidc-resource-group-name ${PERSISTENT_RG_NAME} \
    --tenant-id ${TENANT_ID} \
    --region ${LOCATION} \
    --name ${OIDC_STORAGE_ACCOUNT_NAME} \
    --subscription-id ${SUBSCRIPTION_ID} \
    --public-key-file ${SA_TOKEN_ISSUER_PUBLIC_KEY_PATH}
----
+
.. Set the OIDC issuer URL as shown in the following example:
+
[source,terminal]
----
OIDC_ISSUER_URL="https://${OIDC_STORAGE_ACCOUNT_NAME}.blob.core.windows.net/${OIDC_STORAGE_ACCOUNT_NAME}"
----

.Verification

* Try to access the OIDC issuer by entering the following command:
+
[source,terminal]
----
$ curl -s "${OIDC_ISSUER_URL}/.well-known/openid-configuration" | jq .
----

[role="_additional-resources"]
.Additional resources

* How to obtain the ccoctl tool for OpenShift 4 (Red{nbsp}Hat Knowledgebase article)

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-workload-id_{context}"]
= Creating {azure-short} Workload Identities

[role="_abstract"]
To ensure control over Identity and Access Management (IAM) resources in your {azure-short} deployment, create Workload Identities separately from your infrastructure.

Workload Identities authenticate hosted cluster components to {azure-short} services by using OIDC federation. You must create identities separately and then consume them during infrastructure or cluster creation.

.Prerequisites

* You have an {azure-short} credentials file in the following format:
+
.Example file
[source,terminal]
----
{
  "subscriptionId": "your-subscription-id",
  "tenantId": "your-tenant-id",
  "clientId": "your-client-id",
  "clientSecret": "your-client-secret"
}
----

* You have a resource group to create the managed identities in.
* You have an OIDC issuer URL for Workload Identity federation. For more information, see "Setting up an OIDC issuer".

.Procedure

. Set environment variables as shown in the following example:
+
[source,terminal]
----
CLUSTER_NAME="my-self-managed-cluster"
INFRA_ID="${CLUSTER_NAME}-$(openssl rand -hex 4)"
----

. On the {hcp} command-line interface, `hcp`, enter the following command:
+
[source,terminal]
----
$ hcp create iam azure \
    --name <my_cluster_name> \
    --infra-id <infra_id> \
    --azure-creds <azure_credentials_file> \
    --resource-group-name <resource_group> \
    --oidc-issuer-url <oidc_issuer_url> \
    --output-file <workload_identities_file> \
    --location <my_region> \
    --cloud <my_cloud_environment>
----
+
where:
+
`<my_cluster_name>`:: Specifies the name of the cluster you intend to create.
`<infra_id>`:: Specifies the unique identifier for naming {azure-short} resources. Typically, this identifier is the cluster name with a suffix.
`<azure_credentials_file>`:: Specifies the {azure-short} credentials file with permission to create managed identities and federated credentials.
`<resource_group>`:: Specifies the name of the resource group where you intend to create identities.
`<oidc_issuer_url>`:: Specifies the URL of the OIDC identity provider for Workload Identity federation.
`<workload_identities_file>`:: Specifies the output file path, such as `my-cluster-name-iam-output.json`.
+
You can also add these optional flags to the `hcp create iam azure` command:
+
`<my_region>`:: Specifies the {azure-short} region for the managed identities. The default value is `eastus`.
`<my_cloud_environment>`:: Specifies the {azure-short} cloud environment. The default value is `AzurePublicCloud`.

.Verification

* Review the output file, which looks like the following example:
+
.Example output
[source,terminal]
----
{
  "disk": {
    "tenantID": "...",
    "clientID": "...",
    "resourceID": "/subscriptions/.../providers/Microsoft.ManagedIdentity/userAssignedIdentities/my-cluster-abc123-disk"
  },
  "file": {
    "tenantID": "...",
    "clientID": "...",
    "resourceID": "..."
  },
  "imageRegistry": { ... },
  "ingress": { ... },
  "cloudProvider": { ... },
  "nodePoolManagement": { ... },
  "network": { ... },
  "controlPlaneOperator": { ... }
}
----
+
The output includes 8 user-assigned identities, one per cluster component, along with federated credentials for each identity:
+
** Disk CSI driver
** File CSI driver
** Image registry
** Ingress Operator
** Cloud provider
** Node pool management
** Network Operator
** Control Plane Operator

// Add note about private endpoint access? or include that in the steps to deploy private clusters on Azure?

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-infra_{context}"]
= Creating {azure-short} infrastructure

[role="_abstract"]
Create an {azure-short} infrastructure separately so that when you create a hosted cluster on {azure-short}, you can use pre-existing infrastructure.

.Prerequisites

* You have an {azure-short} credentials file with the following format:
+
[source,json]
----
{
  "subscriptionId": "<my_subscription_id>",
  "tenantId": "<my_tenant_id>",
  "clientId": "<my_client_id>",
  "clientSecret": "<my_client_secret>"
}
----

* You have an existing public DNS zone in your {azure-short} subscription for your base domain.

* You created Workload Identities. For more information, see "Creating {azure-short} Workload Identities".

.Procedure

* To create the infrastructure with a new virtual network, subnet, and network security group, enter the following command:
+
[source,terminal]
----
$ hcp create infra azure \
  --name <my_cluster_name> \
  --infra-id <infra_id> \
  --azure-creds <azure_credentials_file> \
  --base-domain <base_domain> \
  --location <location> \
  --workload-identities-file <workload_identities_file> \
  --assign-identity-roles \
  --dns-zone-rg-name <dns_zone_rg> \
  --output-file <output_infra_file>
----
+
where:
+
** `--name` specifies the name of the hosted cluster you intend to create.
** `--infra-id` specifies a unique name that identifies your infrastructure. This value is used to name and tag {azure-short} resources. Typically, it is the name of your cluster with a suffix appended to it.
** `--azure-creds` specifies an {azure-short} credentials file that has permission to create infrastructure resources, such as virtual networks, subnets, and load balancers.
** `--base-domain` specifies the base domain for the ingress of your hosted cluster. The base domain must correspond to an existing public DNS zone in your {azure-short} subscription.
** `--location` specifies the {azure-short} region where you want to create the infrastructure, such as `eastus` or `westus2`.
** `--workload-identities-file` specifies the path to the JSON file that contains the Workload Identity configuration.
** `--assign-identity-roles` specifies that automatic RBAC role assignment is enabled for Workload Identities.
** `--dns-zone-rg-name` specifies the name of the resource group that contains your public DNS zone.
** `--output-file` specifies the file where the details of the infrastructure are stored in YAML format.

* To create the infrastructure with an existing virtual network, subnet, and network security group, enter the following command:
+
[source,terminal]
----
$ hcp create infra azure \
  --name <my_cluster_name> \
  --infra-id <infra_id> \
  --azure-creds <azure_credentials_file> \
  --base-domain <base_domain> \
  --location <location> \
  --workload-identities-file <workload_identities_file> \
  --vnet-id /subscriptions/<subscription_id>/resourceGroups/<resource_group>/providers/Microsoft.Network/virtualNetworks/<vnet_name> \
  --subnet-id /subscriptions/<subscription_id>/resourceGroups/<resource_group>/providers/Microsoft.Network/virtualNetworks/<vnet_name>/subnets/<subnet_name> \
  --network-security-group-id /subscriptions/<subscription_id>/resourceGroups/<resource_group>/providers/Microsoft.Network/networkSecurityGroups/<network_security_group_name> \
  --assign-identity-roles \
  --dns-zone-rg-name <dns_zone_rg> \
  --output-file <output_infra_file>
----
+
where:
+
** `--name` specifies the name of the hosted cluster you intend to create.
** `--infra-id` specifies a unique name that identifies your infrastructure. This value is used to name and tag {azure-short} resources. Typically, it is the name of your cluster with a suffix appended to it.
** `--azure-creds` specifies an {azure-short} credentials file that has permission to create infrastructure resources, such as virtual networks, subnets, and load balancers.
** `--base-domain` specifies the base domain for the ingress of your hosted cluster. The base domain must correspond to an existing public DNS zone in your {azure-short} subscription.
** `--location` specifies the {azure-short} region where you want to create the infrastructure, such as `eastus` or `westus2`.
** `--workload-identities-file` specifies the path to the JSON file that contains the Workload Identity configuration.
** `--vnet-id` specifies your existing virtual network ID, which includes your subscription ID and your virtual network name.
** `--subnet-id` specifies the ARM resource ID of your subnet, which includes your subscription ID, virtual network name, and subnet name.
** `--network-security-group-id` specifies your existing network security group ID, which includes your subscription ID and your network security group name.
** `--assign-identity-roles` specifies that automatic RBAC role assignment is enabled for Workload Identities.
** `--dns-zone-rg-name` specifies the name of the resource group that contains your public DNS zone.
** `--output-file` specifies the file where the details of the infrastructure are stored in YAML format.

[role="_additional-resources"]
.Additional resources

* Creating {azure-short} Workload Identities

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-mgmt-cluster_{context}"]
= Configuring an {azure-short} management cluster for {hcp}

[role="_abstract"]
To configure the management cluster for {hcp} on {azure-short}, you need to ensure that external DNS and the HyperShift Operator are set up on the cluster.

The configuration steps include configuring the DNS zone, delegating the DNS records for your cluster, and creating a dedicated service principal for external DNS.

.Prerequisites

* You installed the {mce-short} 2.5 or later on an OpenShift Container Platform cluster. You can install {mce-short} as an Operator from the OpenShift Container Platform software catalog. Or, if you already use {rh-rhacm-title}, the Operator is automatically installed. The HyperShift Operator is enabled by default in the operator package for {mce-short}.

* The {azure-short} command-line interface (CLI) is installed and configured.

* The {oc-first} is installed.

* You have an OpenShift Container Platform management cluster on {azure-short}.

* If you are using external DNS, the `jq` command-line JSON processor is installed.

.Procedure

. Set the DNS configuration variables as shown in the following example:
+
[source,bash]
----
PARENT_DNS_RG="<my_parent_dns_resource_group>"
PARENT_DNS_ZONE="<my_parent.dns.zone.com>"
DNS_RECORD_NAME="<my_subdomain>"
RESOURCE_GROUP_NAME="<my_resource_group>"
DNS_ZONE_NAME="<my_subdomain.my_parent.dns.zone.com>"
LOCATION="<my_region>"
----

. Create the {azure-short} group by entering the following command:
+
[source,terminal]
----
$ az group create \
  --name $RESOURCE_GROUP_NAME \
  --location $LOCATION
----

. Create the {azure-short} DNS zone by entering the following command:
+
[source,terminal]
----
$ az network dns zone create \
  --resource-group $RESOURCE_GROUP_NAME \
  --name $DNS_ZONE_NAME
----

. If an existing name server record exists, delete it by entering the following command:
+
[source,terminal]
----
$ az network dns record-set ns delete \
  --resource-group $PARENT_DNS_RG \
  --zone-name $PARENT_DNS_ZONE \
  --name $DNS_RECORD_NAME -y
----

. Get the name servers from your DNS zone by entering the following command:
+
[source,bash]
----
name_servers=$(az network dns zone show \
  --resource-group $RESOURCE_GROUP_NAME \
  --name $DNS_ZONE_NAME \
  --query nameServers \
  --output tsv)
----

. Create an array of name servers as shown in the following example:
+
[source,bash]
----
ns_array=()
while IFS= read -r ns; do
    ns_array+=("$ns")
done <<< "$name_servers"
----

. Add name server records to the parent zone as shown in the following example:
+
[source,bash]
----
for ns in "${ns_array[@]}"; do
    az network dns record-set ns add-record \
        --resource-group $PARENT_DNS_RG \
        --zone-name $PARENT_DNS_ZONE \
        --record-set-name $DNS_RECORD_NAME \
        --nsdname "$ns"
done
----

. Set the external DNS configuration variables as shown in the following example:
+
[source,bash]
----
EXTERNAL_DNS_NEW_SP_NAME="<external_dns_service_principal>"
SERVICE_PRINCIPAL_FILEPATH="<path_to_azure_mgmt_json_file>"
RESOURCE_GROUP_NAME="<my_resource_group>"
----

. Create the service principal for external DNS by entering the following command:
+
[source,bash]
----
DNS_SP=$(az ad sp create-for-rbac --name ${EXTERNAL_DNS_NEW_SP_NAME})
EXTERNAL_DNS_SP_APP_ID=$(echo "$DNS_SP" | jq -r '.appId')
EXTERNAL_DNS_SP_PASSWORD=$(echo "$DNS_SP" | jq -r '.password')
----

. Get the DNS zone ID by entering the following command:
+
[source,bash]
----
DNS_ID=$(az network dns zone show \
  --name ${DNS_ZONE_NAME} \
  --resource-group ${RESOURCE_GROUP_NAME} \
  --query "id" \
  --output tsv)
----

. Assign the `Reader` role to the service principal by entering the following command:
+
[source,terminal]
----
$ az role assignment create \
  --role "Reader" \
  --assignee "${EXTERNAL_DNS_SP_APP_ID}" \
  --scope "${DNS_ID}"
----

. Assign the `Contributor` role to the service principal by entering the following command:
+
[source,terminal]
----
$ az role assignment create \
  --role "Contributor" \
  --assignee "${EXTERNAL_DNS_SP_APP_ID}" \
  --scope "${DNS_ID}"
----

. Create the content for the {azure-short} credentials file as shown in the following example:
+
[source,json]
----
{
  "tenantId": "$(az account show --query tenantId -o tsv)",
  "subscriptionId": "$(az account show --query id -o tsv)",
  "resourceGroup": "$RESOURCE_GROUP_NAME",
  "aadClientId": "$EXTERNAL_DNS_SP_APP_ID",
  "aadClientSecret": "$EXTERNAL_DNS_SP_PASSWORD"
}
----

. Create the credentials file by entering the following command:
+
[source,terminal]
----
$ oc apply -f <service_principal_filepath>.json
----

. If an existing Kubernetes secret for the {azure-short} credentials exists, delete it by entering the following command:
+
[source,terminal]
----
$ oc delete secret/azure-config-file --namespace "default" || true
----

. Create the Kubernetes secret for the {azure-short} credentials by entering the following command:
+
[source,terminal]
----
$ oc create secret generic azure-config-file \
  --namespace "default" \
  --from-file ${SERVICE_PRINCIPAL_FILEPATH}
----

. Configure the HyperShift Operator to use external DNS by creating the following `ConfigMap` object:
+
[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: hypershift-operator-install-flags
  namespace: local-cluster
data:
  installFlagsToAdd: "--external-dns-provider=azure --external-dns-credentials <secret> --external-dns-domain-filter <dns_zone>"
  installFlagsToRemove: ""
----
+
The `data.installFlagsToAdd` parameter specifies the flags to pass to the Operator so it detects the DNS.

. Apply the config map by entering the following command:
+
[source,terminal]
----
$ oc apply -f hypershift-operator-install-flags.yaml
----

.Verification

* Verify that both the HyperShift Operator and the external DNS are running by entering the following command:
+
[source,terminal]
----
$ oc get pods -n hypershift
----
+
.Example output
[source,terminal]
----
NAME                           READY   STATUS    RESTARTS   AGE
external-dns-xxxxx-xxxxx       1/1     Running   0          1m
operator-xxxxx-xxxxx           1/1     Running   0          1m
----

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-hosted_{context}"]
= Creating a hosted cluster on {azure-short}

[role="_abstract"]
Hosted clusters are where your applications run. Each hosted cluster has its own control plane that runs on the management cluster and a set of compute node virtual machines (VMs) in {azure-short}.

The hosted cluster uses Workload Identities to securely access {azure-short} services without storing credentials.

.Prerequisites

* You installed the {azure-short} command-line interface (CLI).

* You installed the {hcp} CLI, `hcp`.

* You installed the {oc-first}.

* You installed the `jq` command-line JSON processor.

* You have a management cluster where the HyperShift Operator is installed and external DNS is configured.

* You set up {azure-short} resources, including Workload Identities, an OIDC issuer, and infrastructure.

* You have the appropriate {azure-short} permissions.

** At the subscription level, you must have the `Contributor` role and the `User Access Administrator` role.
** For Microsoft Graph API, you must have the `Application.ReadWrite.OwnedBy` permission.

.Procedure

* Create the `HostedCluster` custom resource by entering the following command:
+
[source,terminal]
----
$ hcp create cluster azure \
  --name "$CLUSTER_NAME" \
  --infra-id "$INFRA_ID" \
  --azure-creds $AZURE_CREDS \
  --location ${LOCATION} \
  --node-pool-replicas 2 \
  --base-domain $BASE_DOMAIN \
  --pull-secret $PULL_SECRET \
  --generate-ssh \
  --release-image ${RELEASE_IMAGE} \
  --sa-token-issuer-private-key-path "${SA_TOKEN_ISSUER_PRIVATE_KEY_PATH}" \
  --oidc-issuer-url "${OIDC_ISSUER_URL}" \
  --dns-zone-rg-name ${PERSISTENT_RG_NAME} \
  --assign-service-principal-roles \
  --infra-json <output_infra_file> \
  --diagnostics-storage-account-type Managed \
  --external-dns-domain "${DNS_ZONE_NAME}"
----

.Verification

. Check the cluster status by entering the following command:
+
[source,terminal]
----
$ oc get hostedcluster $CLUSTER_NAME -n clusters
----

. Wait for the cluster to be complete by entering the following command:
+
[source,terminal]
----
$ oc wait \
  --for=jsonpath='{.status.version.history[0].state}'=Completed \
  hostedcluster/$CLUSTER_NAME \
  -n clusters --timeout=20m
----

. Create the `kubeconfig` file for the cluster by entering the following command:
+
[source,terminal]
----
$ hcp create kubeconfig \
  --name $CLUSTER_NAME > $CLUSTER_NAME-kubeconfig
----

. Get the `kubeconfig` file by entering the following command:
+
[source,terminal]
----
$ export KUBECONFIG=$CLUSTER_NAME-kubeconfig
----

. Access the cluster nodes by entering the following command:
+
[source,terminal]
----
$ oc get nodes
----

. Access the cluster by entering the following command:
+
[source,terminal]
----
$ oc get clusterversion
----

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private_{context}"]
= Private hosted clusters on {azure-short}

[role="_abstract"]
By default, hosted clusters are accessible through public DNS and the default router of the management cluster. If you want communication between your compute nodes and the hosted control plane to be private, you can create hosted clusters that use {azure-short} Private Link for communication.

Private endpoint access uses {azure-short} Private Link to expose the internal load balancer of the hosted control plane to the {azure-short} Virtual Network (VNet) of the hosted cluster. Compute nodes resolve the API server hostname by using private DNS zones that point to the private endpoint IP address.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private-subnet_{context}"]
= Preparing a subnet for a private hosted cluster on {azure-short}

[role="_abstract"]
{azure-short} Private Link requires a dedicated subnet for network address translator (NAT) IP address allocation. You can manually create the subnet, or it can be automatically created during cluster creation.

By manually creating the subnet, you have control over classless inter-domain routing (CIDR) allocation and naming. The following steps apply to manually creating the subnet. If you want the subnet to be automatically created, skip this procedure.

[NOTE]
====
{azure-short} Private Link, the NAT subnet, and the internal load balancer of the management cluster must all be in the same {azure-short} region. Private Link is automatically created in the location where the hosted cluster is created. {azure-short} rejects the creation of Private Link if the NAT subnet is in a different region.
====

.Prerequisites

* You have an OpenShift Container Platform management cluster on {azure-short}. For more information, see "Configuring an {azure-short} management cluster for {hcp}".

* The {azure-short} command-line interface (CLI) is installed and configured.

* The {oc-first} is installed.

* If you are using external DNS, the `jq` command-line JSON processor is installed.

* You configured an OIDC issuer. For more information, see "Setting up an OIDC issuer".

.Procedure

. Identify the {azure-short} Virtual Network (VNet) of the management cluster.
+
.. Obtain the infrastructure resource group of the management cluster as shown in the following example:
+
[source,bash]
----
$ MGMT_INFRA_RG=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.azure.resourceGroupName}')
----
+
.. Find the VNet in the infrastructure resource group as shown in the following example:
+
[source,bash]
----
$ MGMT_VNET_NAME=$(az network vnet list --resource-group "${MGMT_INFRA_RG}" --query "[0].name" -o tsv)
----
+
.. Set the environment variable for the VNet by entering the following command:
+
[source,bash]
----
$ MGMT_VNET_RG="${MGMT_INFRA_RG}"
----

. Create the NAT subnet.
+
.. Check the existing address space and subnets to ensure that you do not choose an overlapping classless inter-domain routing (CIDR) range. Enter the following command:
+
[source,terminal]
----
$ az network vnet show \
  --resource-group "${MGMT_VNET_RG}" \
  --name "${MGMT_VNET_NAME}" \
  --query '{addressSpace: addressSpace.addressPrefixes, subnets: subnets[].{name: name, prefix: addressPrefix}}' \
  -o json
----
+
.. Create the subnet as shown in the following example:
+
[source,terminal]
----
$ az network vnet subnet create \
  --resource-group "${MGMT_VNET_RG}" \
  --vnet-name "${MGMT_VNET_NAME}" \
  --name "${NAT_SUBNET_NAME}" \
  --address-prefixes 10.1.64.0/24 \
  --disable-private-link-service-network-policies true
----
+
* The NAT subnet must be in the VNet of the management cluster because Private Link is created alongside the internal load balancer of the management cluster.
* The `10.1.64.0/24` address prefix is an example only. Replace it with a CIDR range that does not overlap with any other subnet in the VNet of the management cluster. If the VNet uses `10.0.0.0/16`, the NAT subnet must fall within that range, or you must expand the address space of the VNet.
* The `--disable-private-link-service-network-policies` flag is required and must be set to `true`. Otherwise, {azure-short} rejects the creation of Private Link on the subnet.

. Obtain the NAT subnet resource ID for later use as shown in the following example:
+
[source,bash]
----
$ NAT_SUBNET_ID=$(az network vnet subnet show \
  --resource-group "${MGMT_VNET_RG}" \
  --vnet-name "${MGMT_VNET_NAME}" \
  --name "${NAT_SUBNET_NAME}" \
  --query id -o tsv)
----

[role="_additional-resources"]
.Additional resources

* Configuring an {azure-short} management cluster for {hcp}

* Setting up an OIDC issuer

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private-operator_{context}"]
= Installing the HyperShift Operator with private platform support

[role="_abstract"]
To set up an environment that supports private clusters, you must install the HyperShift Operator with flags that configure {azure-short} Private Link management.

[NOTE]
====
If you already installed the HyperShift Operator but you did not include the `--private-platform Azure` setting, you must run the `hcp install` command again with the private platform flags before you can create private clusters.
====

.Prerequisites

* You have an OpenShift Container Platform management cluster on {azure-short}.

* The {azure-short} command-line interface (CLI) is installed and configured.

* The {oc-first} is installed.

* If you are using external DNS, the `jq` command-line JSON processor is installed.

* You configured an OIDC issuer. For more information, see "Setting up an OIDC issuer".

.Procedure

. Obtain credentials so that the Operator can manage Private Link resources.
+
.. Obtain the credentials file for Private Link management as shown in the following example:
+
[source,bash]
----
$ AZURE_PRIVATE_CREDS="<path_to_azure_private_credentials_json>"
----
+
.. Obtain the infrastructure resource group of the management cluster as shown in the following example:
+
[source,bash]
----
$ MGMT_INFRA_RG=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.azure.resourceGroupName}')
----

. Set the external DNS configuration variables as shown in the following examples:
+
[source,bash]
----
$ SERVICE_PRINCIPAL_FILEPATH="<path_to_azure_mgmt_json_file>"
----
+
[source,bash]
----
$ DNS_ZONE_NAME="<my_subdomain_my_parent_dns_zone_com>"
----

. Install the HyperShift Operator with private platform support as shown in the following example:
+
[source,terminal]
----
$ hcp install \
  --pull-secret ${PULL_SECRET} \
  --private-platform Azure \
  --azure-private-creds ${AZURE_PRIVATE_CREDS} \
  --azure-pls-resource-group ${MGMT_INFRA_RG} \
  --external-dns-provider=azure \
  --external-dns-credentials ${SERVICE_PRINCIPAL_FILEPATH} \
  --external-dns-domain-filter ${DNS_ZONE_NAME}
----
+
* `--private-platform Azure` specifies that {azure-short} Private Link management is to be enabled in the Operator.
* `--azure-private-creds` specifies the path to the {azure-short} credentials file that is used for Private Link operations.
+
[NOTE]
====
Besides using the `--azure-private-creds` flag, you can use one of the following authentication methods. Be sure to use only one authentication method.

** `--azure-private-secret` specifies an existing Kubernetes secret that has {azure-short} credentials. This flag has a companion flag, `--azure-private-secret-key`. Its default value is `credentials`, but you can customize it for secrets that have non-standard key names.
** `--azure-pls-managed-identity-client-id` specifies the client ID of a managed identity for Private Link operations through Workload Identity federation. If you specify this flag, you must also include the `--azure-pls-subscription-id` flag, which specifies the {azure-short} subscription ID for Private Link operations.
====
* `--azure-pls-resource-group` specifies the resource group where the Private Link resources are to be created. This resource group is the same as the resource group of the infrastructure for the management cluster.
* `--external-dns-credentials` specifies the path to a file that contains DNS credentials. If preferred, you can use the `--external-dns-secret` flag instead to specify a Kubernetes secret that has DNS credentials.

[role="_additional-resources"]
.Additional resources

* Setting up an OIDC issuer

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private-iam_{context}"]
= Configuring IAM resources for a private hosted cluster

[role="_abstract"]
Create Workload Identities so that your private clusters can manage private endpoints and private DNS zones.

.Prerequisites

* You have an OpenShift Container Platform management cluster on {azure-short} that has the HyperShift Operator installed.

* The {azure-short} command-line interface (CLI) is installed and configured.

* The {oc-first} is installed.

* If you are using external DNS, the `jq` command-line JSON processor is installed.

* You configured an OIDC issuer. For more information, see "Setting up an OIDC issuer".

.Procedure

. Set your environment variables:
+
.. Set your prefix by entering the following command:
+
[source,bash]
----
$ PREFIX="<my_prefix>"
----
+
.. Set the cluster name by entering the following command:
+
[source,bash]
----
$ CLUSTER_NAME="${PREFIX}-hc"
----
+
.. Set the resource group name by entering the following command:
+
[source,bash]
----
$ RESOURCE_GROUP_NAME="${CLUSTER_NAME}-${PREFIX}"
----
+
.. Set the location by entering the following command:
+
[source,bash]
----
$ LOCATION="<my_region>"
----
+
.. Set the variable for the path to the {azure-short} credentials file by entering the following command:
+
[source,bash]
----
$ AZURE_CREDS="<path_to_azure_credentials_json>"
----
+
.. Set the variable for the OIDC issuer URL by entering the following command:
+
[source,bash]
----
$ OIDC_ISSUER_URL="<my_oidc_url_com>"
----
.. Set the path to the Workload Identities file by entering the following command:
+
[source,bash]
----
$ WORKLOAD_IDENTITIES_FILE="<path_to_workload_identities_file_json>"
----

. Create Workload Identities by entering the following command:
+
[source,terminal]
----
$ hcp create iam azure \
  --name "${CLUSTER_NAME}" \
  --infra-id "${PREFIX}" \
  --azure-creds "${AZURE_CREDS}" \
  --location "${LOCATION}" \
  --resource-group-name "${RESOURCE_GROUP_NAME}" \
  --oidc-issuer-url "${OIDC_ISSUER_URL}" \
  --output-file "${WORKLOAD_IDENTITIES_FILE}"
----
+
The command creates 8 Workload Identities. For `Private` and `PublicAndPrivate` clusters, the Control Plane Operator identity is used to create and manage private endpoints, private DNS zones, {azure-short} Virtual Network (VNet) links, and DNS A records. The Control Plane Identity is assigned the `Contributor` role by default. To use a more restrictive role, use the `--assign-custom-hcp-roles` flag.

[role="_additional-resources"]
.Additional resources

* Setting up an OIDC issuer

* Creating {azure-short} Workload Identities

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private-infra_{context}"]
= Creating infrastructure for a private hosted cluster

[role="_abstract"]
Set up infrastructure so that you can create private hosted clusters.

.Prerequisites

* You have an OpenShift Container Platform management cluster on {azure-short} that has the HyperShift Operator installed.

* The {azure-short} command-line interface (CLI) is installed and configured.

* The {oc-first} is installed.

* If you are using external DNS, the `yq` command-line YAML processor is installed.

* You configured an OIDC issuer. For more information, see "Setting up an OIDC issuer".

.Procedure

. Set your environment variables:
+
.. Set the variable for the DNS zone resource group by entering the following command:
+
[source,bash]
----
$ DNS_ZONE_RG_NAME="os4-common"
----
+
.. Set the variable for the base domain of your DNS zone by entering the following command:
+
[source,bash]
----
$ PARENT_DNS_ZONE="<your_base_domain_com>"
----
+
.. Set the variable that points to the infrastructure output file by entering the following command:
+
[source,bash]
----
$ INFRA_OUTPUT_FILE="${PREFIX}-infra-output.json"
----

. Create infrastructure by entering the following command:
+
[source,terminal]
----
$ hcp create infra azure \
  --azure-creds "${AZURE_CREDS}" \
  --infra-id "${PREFIX}" \
  --name "${CLUSTER_NAME}" \
  --location "${LOCATION}" \
  --base-domain "${PARENT_DNS_ZONE}" \
  --dns-zone-rg-name "${DNS_ZONE_RG_NAME}" \
  --workload-identities-file "${WORKLOAD_IDENTITIES_FILE}" \
  --assign-identity-roles \
  --output-file "${INFRA_OUTPUT_FILE}"
----

. Read the infrastructure output to get the resource IDs that you created, as shown in the following example:
+
.. Read the resource group name by entering the following command:
+
[source,bash]
----
$ MANAGED_RG_NAME=$(yq -r -p yaml '.resourceGroupName' "${INFRA_OUTPUT_FILE}")
----
+
.. Read the VNet ID by entering the following command:
+
[source,bash]
----
$ VNET_ID=$(yq -r -p yaml '.vnetID' "${INFRA_OUTPUT_FILE}")
----
+
.. Read the subnet ID by entering the following command:
+
[source,bash]
----
$ SUBNET_ID=$(yq -r -p yaml '.subnetID' "${INFRA_OUTPUT_FILE}")
----
+
.. Read the network security group ID by entering the following command:
+
[source,bash]
----
$ NSG_ID=$(yq -r -p yaml '.securityGroupID' "${INFRA_OUTPUT_FILE}")
----
+
Note the resource IDs because you need them to create the private hosted cluster.

[role="_additional-resources"]
.Additional resources

* Setting up an OIDC issuer

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private-hosted_{context}"]
= Creating a private {azure-short} hosted cluster

[role="_abstract"]
Create a private hosted cluster to ensure that the communication between compute nodes and the hosted control plane occurs over {azure-short} Private Link.

.Prerequisites

* You configured a subnet, as described in "Preparing a subnet for a private hosted cluster on {azure-short}".

* You installed the HyperShift Operator on an OpenShift Container Platform management cluster on {azure-short}, as described in "Installing the HyperShift Operator with private platform support".

* You created Identity and Access Management (IAM) resources, as described in "Configuring IAM resources for a private hosted cluster".

* You created infrastructure, as described in "Creating infrastructure for a private hosted cluster".

* This procedure relies on environment variables that you created in the prerequisite procedures. Be sure to complete this procedure in the same terminal where you already defined the environment variables.

.Procedure

. Create the private hosted cluster by entering the following command:
+
[source,terminal]
----
$ hcp create cluster azure \
  --name "$CLUSTER_NAME" \
  --namespace "clusters" \
  --azure-creds ${AZURE_CREDS} \
  --location ${LOCATION} \
  --node-pool-replicas 2 \
  --base-domain ${PARENT_DNS_ZONE} \
  --pull-secret ${PULL_SECRET} \
  --generate-ssh \
  --release-image ${RELEASE_IMAGE} \
  --resource-group-name "${MANAGED_RG_NAME}" \
  --vnet-id "${VNET_ID}" \
  --subnet-id "${SUBNET_ID}" \
  --network-security-group-id "${NSG_ID}" \
  --sa-token-issuer-private-key-path "${SA_TOKEN_ISSUER_PRIVATE_KEY_PATH}" \
  --oidc-issuer-url "${OIDC_ISSUER_URL}" \
  --dns-zone-rg-name ${DNS_ZONE_RG_NAME} \
  --assign-service-principal-roles \
  --workload-identities-file ${WORKLOAD_IDENTITIES_FILE} \
  --external-dns-domain ${DNS_ZONE_NAME} \
  --endpoint-access Private \
  --endpoint-access-private-nat-subnet-id "${NAT_SUBNET_ID}"
----
+
* When you choose a value for the `--external-dns-domain` flag, ensure that the value does not match `{cluster-name}.{base-domain}`. If you use `{cluster-name}.{base-domain}` for the value, the Control Plane Operator creates a private DNS zone that can shadow the `*.apps` domain, which causes the console and ingress to become unreachable.
* `--endpoint-access` accepts 3 values:
+
** `Public`, which is the default value. When you specify `Public`, the API server is accessible through public endpoint only.
** `PublicAndPrivate`, where the API server is accessible through both public and private endpoints.
** `Private`, where the API server is accessible only through Private Link.
+
After you create a cluster, you cannot change it between `Public` endpoint and non-public (`PublicAndPrivate` or `Private`) endpoint access.
+
If you need to allow `Private` endpoint connections from {azure-short} subscriptions other than the hosted cluster's subscription, use the following flag: `--endpoint-access-private-additional-allowed-subscriptions "sub-id-1, sub-id-2"`.

.Verification

. Check the Private Link resources by entering the following command:
+
[source,terminal]
----
$ oc get azureprivatelinkservices -n clusters-${CLUSTER_NAME}
----

. Check the status and connections by entering the following command:
+
[source,terminal]
----
$ oc get azureprivatelinkservices -n clusters-${CLUSTER_NAME} -o yaml
----
+
.Setup progress conditions
[cols="2",options="header"]
|===
|Condition |Description

|`AzureInternalLoadBalancerAvailable`
|The internal load balancer has a front-end IP address.

|`AzurePLSCreated`
|Private Link is created in the management cluster.

|`AzurePrivateEndpointAvailable`
|Private endpoint is created in the hosted cluster VNet.

|`AzurePrivateDNSAvailable`
|Private DNS zones and A records are created.

|`AzurePrivateLinkServiceAvailable`
|All components are ready and private connectivity is available.

|===

. Check the overall cluster status by entering the following command:
+
[source,terminal]
----
$ oc get hostedcluster ${CLUSTER_NAME} -n clusters
----

. Wait for the status by entering the following command:
+
[source,terminal]
----
$ oc wait --for=condition=Available hostedcluster/${CLUSTER_NAME} -n clusters --timeout=30m
----

[role="_additional-resources"]
.Additional resources

* Preparing a subnet for a private hosted cluster on {azure-short}

* Installing the HyperShift Operator with private platform support

* Configuring IAM resources for a private hosted cluster

* Creating infrastructure for a private hosted cluster

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private-access_{context}"]
= Accessing a private {azure-short} hosted cluster

[role="_abstract"]
After you create a private hosted cluster, you need to take additional steps to access it.

.Prerequisites

* You completed the steps in "Creating a private {azure-short} hosted cluster".

.Procedure

* To access a private hosted cluster by generating a `kubeconfig` file, enter the following command:
+
[source,terminal]
----
$ hcp create kubeconfig \
  --name ${CLUSTER_NAME} \
  --port-forward > ${CLUSTER_NAME}-kubeconfig
----

* If you have access to the management cluster, you can port forward to the API server to access the private hosted cluster.
+
.. Port forward to the `kube-apiserver` service by entering the following command:
+
[source,terminal]
----
$ kubectl port-forward svc/kube-apiserver \
  -n clusters-${CLUSTER_NAME} 6443:6443 &
----
+
.. Access the hosted cluster by using the `kubeconfig` file:
+
[source,bash]
----
$ KUBECONFIG=${CLUSTER_NAME}-kubeconfig oc get nodes
----

* If you have a virtual machine (VM) in an {azure-short} Virtual Network (VNet) that is peered with the hosted cluster's VNet, you can access the API server, but you must first link the private DNS zones to the peered VNet.
+
[NOTE]
====
The Control Plane Operator links private DNS zones only to the hosted cluster's VNet. If you want to resolve the API server hostname from a peered VNet, you must manually link the private DNS zones to that VNet as shown in the following steps. Otherwise, DNS resolution fails from the peered VNet.
====
+
.. Link the private DNS zone to your peered VNet as shown in the following example:
+
[source,bash]
----
$ PEERED_VNET_ID="/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Network/virtualNetworks/<vnet>"
----
+
.. Enter the following command:
+
[source,terminal]
----
$ az network private-dns link vnet create \
  --resource-group "${MANAGED_RG_NAME}" \
  --zone-name "${CLUSTER_NAME}.hypershift.local" \
  --name "peered-vnet-link" \
  --virtual-network "${PEERED_VNET_ID}" \
  --registration-enabled false
----
+
.. If you also need base-domain resolution, enter the following command:
+
[source,terminal]
----
$ az network private-dns link vnet create \
  --resource-group "${MANAGED_RG_NAME}" \
  --zone-name "${PARENT_DNS_ZONE}" \
  --name "peered-vnet-basedomain-link" \
  --virtual-network "${PEERED_VNET_ID}" \
  --registration-enabled false
----
+
.. Access the cluster as shown in the following example:
+
[source,bash]
----
$ KUBECONFIG=${CLUSTER_NAME}-kubeconfig oc get nodes
----

[role="_additional-resources"]
.Additional resources

* Creating a private {azure-short} hosted cluster

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-private-ts_{context}"]
= Troubleshooting private hosted clusters on {azure-short}

[role="_abstract"]
If your private hosted cluster gets stuck, check the `AzurePrivateLinkService` custom resource conditions.

.Procedure

. Enter the following command to check the Private Link conditions:
+
[source,terminal]
----
$ oc get azureprivatelinkservices \
  -n clusters-${CLUSTER_NAME} \
  -o jsonpath='{.items[0].status.conditions}' | jq .
----

. Review the output and compare it to the following condition table:
+
.Private cluster stuck conditions
[cols="2",options="header"]
|===
|Condition |Possible cause

|`AzureInternalLoadBalancerAvailable` = `False`
|The `private-router` service has not received an internal load balancer IP address yet. Check the service status and {azure-short} networking.

|`AzurePLSCreated` = `False`
|Private Link creation failed. Check the NAT subnet policies, credentials, and the HyperShift Operator logs.

|`AzurePrivateEndpointAvailable` = `False`
|Private endpoint creation failed or the connection was not approved. Check the Private Link auto-approval list and the Control Plane Operator logs.

|`AzurePrivateDNSAvailable` = `False`
|The DNS zone or record creation failed. In the {azure-short} subscription that stores the infrastructure resources for the hosted cluster, check the Control Plane Operator identity permissions.

|===

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-autoscaling_{context}"]
= Example: Autoscaling a hosted cluster on {azure-short}

[role="_abstract"]
To balance node pools on your {azure-short} hosted cluster, you can configure autoscaling for the cluster.

When you scale up `NodePool` objects, the Cluster API Provider for {azure-short} provisions individual {azure-short} virtual machines.

To configure autoscaling for a hosted cluster on {azure-short}, you edit the `spec.autoscaling` parameters in the `HostedCluster` resource. The following example shows a `HostedCluster` resource with 2 {azure-short} node pools.

[NOTE]
====
This example shows only the autoscaling-related fields.
====

[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: my-cluster
  namespace: my-cluster-namespace
spec:
  autoscaling:
    scaling: ScaleUpAndScaleDown
    maxNodesTotal: 12
    expanders:
      - Random
    scaleDown:
      delayAfterAddSeconds: 300
      unneededDurationSeconds: 600
      utilizationThresholdPercent: 40
    balancingIgnoredLabels:
      - "custom.label/environment"
    maxFreeDifferenceRatioPercent: 70
---
apiVersion: hypershift.openshift.io/v1beta1
kind: NodePool
metadata:
  name: my-cluster-nodepool-1
  namespace: my-cluster-namespace
spec:
  clusterName: my-cluster
  autoScaling:
    min: 1
    max: 6
  platform:
    azure:
      vmSize: Standard_D4s_v3
      # ...
---
apiVersion: hypershift.openshift.io/v1beta1
kind: NodePool
metadata:
  name: my-cluster-nodepool-2
  namespace: my-cluster-namespace
spec:
  clusterName: my-cluster
  autoScaling:
    min: 1
    max: 6
  platform:
    azure:
      vmSize: Standard_D4s_v3
      # ...
----

* `spec.autoScaling.min` must be greater than or equal to `1`. Scaling from zero (`autoScaling.min: 0`) is not supported on {azure-short}.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-delete_{context}"]
= Deleting an {azure-short} hosted cluster and its resources

[role="_abstract"]
If you no longer need a hosted cluster, you can remove it and its infrastructure. Any related Workload Identities and OIDC issuers that were created during setup can be reused for other clusters or deleted separately if you no longer need them.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-cluster-delete_{context}"]
= Deleting a hosted cluster on {azure-short}

[role="_abstract"]
If you are no longer using a hosted cluster on {azure-short}, you can delete it.

.Procedure

* To delete a hosted cluster, enter the following command:
+
[source,terminal]
----
$ hcp destroy cluster azure \
  --name $CLUSTER_NAME \
  --azure-creds $AZURE_CREDS \
  --dns-zone-rg-name $PERSISTENT_RG_NAME \
  --preserve-resource-group
----
+
** `--name` specifies your hosted cluster name.
** `--azure-creds` specifies an {azure-short} credentials file that has permission to create infrastructure resources, such as virtual networks, subnets, and load balancers.
** `--dns-zone-rg-name` specifies the name of the resource group that contains your DNS zone.
** `--preserve-resource-group` specifies that the infrastructure will be preserved. If you do not want to preserve the infrastructure, do not include this flag.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-infra-delete_{context}"]
= Deleting {azure-short} infrastructure

[role="_abstract"]
If you have {azure-short} infrastructure without a hosted cluster, you can remove the infrastructure if you are not using it.

For example, this scenario can happen if you created the infrastructure standalone but never created a hosted cluster. Or, you might have manually deleted the hosted cluster or management cluster, but the infrastructure resources still exist.

You can delete the entire infrastructure, or delete cluster-specific resources but preserve the main resource group. Preserving the main resource group is helpful when you have other resources in the same resource group that you want to keep.

If you have a hosted cluster and want to delete infrastructure while you delete the hosted cluster, follow the steps in "Deleting a hosted cluster on {azure-short}", but omit the `--preserve-resource-group` flag.

.Procedure

* To delete the infrastructure, enter one of the following commands:
+
** To delete the infrastructure, including the resource group, enter the following command:
+
[source,terminal]
----
$ hcp destroy infra azure \
  --name <my_cluster_name> \
  --infra-id <infra_id> \
  --azure-creds <azure_credentials_file>
----
+
*** `--name` specifies your hosted cluster name.
*** `--infra-id` specifies a unique name that identifies your infrastructure. This value is used to name and tag {azure-short} resources. Typically, it is the name of your cluster with a suffix appended to it.
*** `--azure-creds` specifies an {azure-short} credentials file that has permission to create infrastructure resources, such as virtual networks, subnets, and load balancers.
+
** To preserve the resource group but delete only cluster-specific resources, enter the following command:
+
[source,terminal]
----
$ hcp destroy infra azure \
  --name <my_cluster_name> \
  --infra-id <infra_id> \
  --azure-creds <azure_credentials_file> \
  --preserve-resource-group
----
+
*** `--name` specifies your hosted cluster name.
*** `--infra-id` specifies a unique name that identifies your infrastructure. This value is used to name and tag {azure-short} resources. Typically, it is the name of your cluster with a suffix appended to it.
*** `--azure-creds` specifies an {azure-short} credentials file that has permission to create infrastructure resources, such as virtual networks, subnets, and load balancers.
*** `--preserve-resource-group` specifies that you want to preserve the resource group.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-workload-id-delete_{context}"]
= Deleting {azure-short} Workload Identities

[role="_abstract"]
As part of the process to delete a hosted cluster on {azure-short}, you need to delete the Workload Identities.

To delete the Workload Identities, you enter a command on the {hcp} command-line interface, `hcp`. The command uses the file that was generated when you created the Workload Identities to identify the identities to delete. Both the managed identities and their federated credentials are removed.

.Prerequisites

* If you created infrastructure by using the Workload Identities, delete the infrastructure before you delete the identities.

.Procedure

* Enter the following command:
+
[source,terminal]
----
$ hcp destroy iam azure \
    --azure-creds <azure_credentials_file> \
    --workload-identities-file <workload_identities_file> \
    --resource-group-name <resource_group> \
    --name <my_cluster_name> \
    --infra-id <infra_id> \
    --dns-zone-rg-name <dns_zone_rg> \
    --cloud <my_cloud_environment>
----
+
** `<azure_credentials_file>` specifies the {azure-short} credentials file with permission to create managed identities and federated credentials.
** `<workload_identities_file>` specifies the path to the Workload Identities JSON file, such as `my-cluster-name-iam-output.json`.
** `<resource_group>` specifies the name of the resource group where you created identities.
** `<my_cluster_name>` specifies the name of your hosted cluster.
** `<infra_id>` specifies the unique identifier for naming {azure-short} resources. Typically, this identifier is the cluster name with a suffix.
** `<dns_zone_rg>` specifies the DNS zone resource group.
** `<my_cloud_environment>` specifies the {azure-short} cloud environment. Setting the `--cloud` flag is optional. The default value is `AzurePublicCloud`.

//Module included in the following assemblies:
// hosted_control_planes/hcp-deploy/hcp-deploy-azure.adoc

[id="hcp-azure-delete-private_{context}"]
= Deleting a private hosted cluster on {azure-short}

[role="_abstract"]
If you are no longer using a private hosted cluster on {azure-short}, you can delete it.

The deletion process automatically cleans up Private Link resources in the following order:

. The Control Plane Operator removes the private endpoint, private DNS zones, VNet links, and A records.
. The `hcp destroy` command removes role-based access control (RBAC) role assignments.
. The HyperShift Operator removes Private Link.

.Procedure

* To delete a private hosted cluster, enter the following command:
+
[source,terminal]
----
$ hcp destroy cluster azure \
  --name ${CLUSTER_NAME} \
  --azure-creds ${AZURE_CREDS} \
  --resource-group-name ${MANAGED_RG_NAME} \
  --dns-zone-rg-name ${DNS_ZONE_RG_NAME}
----
+
** `--name` specifies your hosted cluster name.
** `--azure-creds` specifies an {azure-short} credentials file that has permission to create infrastructure resources, such as virtual networks, subnets, and load balancers. This flag is required because the `hcp destroy cluster azure` command cleans up RBAC role assignments before it deletes infrastructure.
** `--resource-group-name` specifies the name of the resource group where you created identities.
** `--dns-zone-rg-name` specifies the name of the resource group that contains your DNS zone.
