---
title: "The Cloud Credential Operator in passthrough mode"
type: reference
domain: openshift
slug: authentication-4-22-cco-mode-passthrough
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/cco-mode-passthrough
version: 4.22
family: authentication
documentKind: "Documentation"
---

# The Cloud Credential Operator in passthrough mode

[id="cco-mode-passthrough"]
= The Cloud Credential Operator in passthrough mode

Passthrough mode is supported for Amazon Web Services (AWS), Microsoft Azure, {gcp-first}, {rh-openstack-first}, and VMware vSphere.

In passthrough mode, the Cloud Credential Operator (CCO) passes the provided cloud credential to the components that request cloud credentials. The credential must have permissions to perform the installation and complete the operations that are required by components in the cluster, but does not need to be able to create new credentials. The CCO does not attempt to create additional limited-scoped credentials in passthrough mode.

[NOTE]
====
Manual mode is the only supported CCO configuration for Microsoft Azure Stack Hub.
====

[id="passthrough-mode-permissions"]
== Passthrough mode permissions requirements
When using the CCO in passthrough mode, ensure that the credential you provide meets the requirements of the cloud on which you are running or installing OpenShift Container Platform. If the provided credentials the CCO passes to a component that creates a `CredentialsRequest` CR are not sufficient, that component will report an error when it tries to call an API that it does not have permissions for.

[id="passthrough-mode-permissions-aws"]
=== Amazon Web Services (AWS) permissions
The credential you provide for passthrough mode in AWS must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of OpenShift Container Platform you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see Manually creating long-term credentials for AWS.

[id="passthrough-mode-permissions-azure"]
=== Microsoft Azure permissions
The credential you provide for passthrough mode in Azure must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of OpenShift Container Platform you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see Manually creating long-term credentials for Azure.

[id="passthrough-mode-permissions-gcp"]
=== {gcp-first} permissions
The credential you provide for passthrough mode in {gcp-short} must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of OpenShift Container Platform you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see Manually creating long-term credentials for {gcp-short}.

[id="passthrough-mode-permissions-rhosp"]
=== {rh-openstack-first} permissions
To install an OpenShift Container Platform cluster on {rh-openstack}, the CCO requires a credential with the permissions of a `member` user role.

[id="passthrough-mode-permissions-vsware"]
=== VMware vSphere permissions
To install an OpenShift Container Platform cluster on VMware vSphere, the CCO requires a credential with the following vSphere privileges:

.Required vSphere privileges
[cols="1,2"]
|====
|Category |Privileges

|Datastore
|_Allocate space_

|Folder
|_Create folder_, _Delete folder_

|vSphere Tagging
|All privileges

|Network
|_Assign network_

|Resource
|_Assign virtual machine to resource pool_

|Profile-driven storage
|All privileges

|vApp
|All privileges

|Virtual machine
|All privileges

|====

//Admin credentials root secret format
// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-mode-mint.adoc
// * authentication/managing_cloud_provider_credentials/cco-mode-passthrough.adoc

[id="admin-credentials-root-secret-formats_{context}"]
= Admin credentials root secret format

Each cloud provider uses a credentials root secret in the `kube-system`
namespace by convention, which is then used to satisfy all credentials requests
and create their respective secrets.
This is done either by minting new credentials with _mint mode_, or by copying the credentials root secret with _passthrough mode_.

The format for the secret varies by cloud, and is also used for each
`CredentialsRequest` secret.

.Amazon Web Services (AWS) secret format

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: aws-creds
stringData:
  aws_access_key_id: <base64-encoded_access_key_id>
  aws_secret_access_key: <base64-encoded_secret_access_key>
----

.Microsoft Azure secret format

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: azure-credentials
stringData:
  azure_subscription_id: <base64-encoded_subscription_id>
  azure_client_id: <base64-encoded_client_id>
  azure_client_secret: <base64-encoded_client_secret>
  azure_tenant_id: <base64-encoded_tenant_id>
  azure_resource_prefix: <base64-encoded_resource_prefix>
  azure_resourcegroup: <base64-encoded_resource_group>
  azure_region: <base64-encoded_region>
----

On Microsoft Azure, the credentials secret format includes two properties that must contain the cluster's infrastructure ID, generated randomly for each cluster installation. This value can be found after running create manifests:

[source,terminal]
----
$ cat .openshift_install_state.json | jq '."*installconfig.ClusterID".InfraID' -r
----

.Example output
[source,terminal]
----
mycluster-2mpcn
----

This value would be used in the secret data as follows:

[source,yaml]
----
azure_resource_prefix: mycluster-2mpcn
azure_resourcegroup: mycluster-2mpcn-rg
----

.{gcp-first} secret format

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: gcp-credentials
stringData:
  service_account.json: <base64-encoded_service_account>
----

.{rh-openstack-first} secret format

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: openstack-credentials
data:
  clouds.yaml: <base64-encoded_cloud_creds>
  clouds.conf: <base64-encoded_cloud_creds_init>
----

.VMware vSphere secret format

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: vsphere-creds
data:
 vsphere.openshift.example.com.username: <base64-encoded_username>
 vsphere.openshift.example.com.password: <base64-encoded_password>
----

[id="passthrough-mode-maintenance"]
== Passthrough mode credential maintenance
If `CredentialsRequest` CRs change over time as the cluster is upgraded, you must manually update the passthrough mode credential to meet the requirements. To avoid credentials issues during an upgrade, check the `CredentialsRequest` CRs in the release image for the new version of OpenShift Container Platform before upgrading. To locate the `CredentialsRequest` CRs that are required for your cloud provider, see _Manually creating long-term credentials_ for AWS, Azure, or {gcp-short}.

//Rotating cloud provider credentials manually
// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc
// * authentication/managing_cloud_provider_credentials/cco-mode-mint.adoc
// * authentication/managing_cloud_provider_credentials/cco-mode-passthrough.adoc

[id="manually-rotating-cloud-creds_{context}"]

If your cloud provider credentials are changed for any reason, you must manually update the secret that the Cloud Credential Operator (CCO) uses to manage cloud provider credentials.

The process for rotating cloud credentials depends on the mode that the CCO is configured to use. After you rotate credentials for a cluster that is using mint mode, you must manually remove the component credentials that were created by the removed credential.

[NOTE]
====
You can also use the command-line interface to complete all parts of this procedure.
====

.Prerequisites

* Your cluster is installed on a platform that supports rotating cloud credentials manually with the CCO mode that you are using:

** For mint mode, Amazon Web Services (AWS) and {gcp-first} are supported.

** For passthrough mode, Amazon Web Services (AWS), Microsoft Azure, {gcp-first}, {rh-openstack-first}, and VMware vSphere are supported.

* You have changed the credentials that are used to interface with your cloud provider.

* The new credentials have sufficient permissions for the mode CCO is configured to use in your cluster.

.Procedure

. In the *Administrator* perspective of the web console, navigate to *Workloads* -> *Secrets*.

. In the table on the *Secrets* page, find the root secret for your cloud provider.
+
[cols=2,options=header]
|===
|Platform
|Secret name

|AWS
|`aws-creds`

|Azure
|`azure-credentials`

|{gcp-short}
|`gcp-credentials`

|{rh-openstack}
|`openstack-credentials`

|VMware vSphere
|`vsphere-creds`

|===

. Click the Options menu {kebab} in the same row as the secret and select *Edit Secret*.

. Record the contents of the *Value* field or fields. You can use this information to verify that the value is different after updating the credentials.

. Update the text in the *Value* field or fields with the new authentication information for your cloud provider, and then click *Save*.

. If you are updating the credentials for a vSphere cluster that does not have the vSphere CSI Driver Operator enabled, you must force a rollout of the Kubernetes controller manager to apply the updated credentials.
+
[NOTE]
====
If the vSphere CSI Driver Operator is enabled, this step is not required.
====
+
To apply the updated vSphere credentials, log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role and run the following command:
+
[source,terminal]
----
$ oc patch kubecontrollermanager cluster \
  -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date )"'"}}' \
  --type=merge
----
+
While the credentials are rolling out, the status of the Kubernetes Controller Manager Operator reports `Progressing=true`. To view the status, run the following command:
+
[source,terminal]
----
$ oc get co kube-controller-manager
----

. If the CCO for your cluster is configured to use mint mode, delete each component secret that is referenced by the individual `CredentialsRequest` objects.
. Delete each component secret that is referenced by the individual `CredentialsRequest` objects.

.. Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role.

.. Get the names and namespaces of all referenced component secrets:
+
[source,terminal]
----
$ oc -n openshift-cloud-credential-operator get CredentialsRequest \
  -o json | jq -r '.items[] | select (.spec.providerSpec.kind=="<provider_spec>") | .spec.secretRef'
----
+
where `<provider_spec>` is the corresponding value for your cloud provider:
+
--
* AWS: `AWSProviderSpec`
* {gcp-short}: `GCPProviderSpec`
--
+
.Partial example output for AWS
+
[source,json]
----
{
  "name": "ebs-cloud-credentials",
  "namespace": "openshift-cluster-csi-drivers"
}
{
  "name": "cloud-credential-operator-iam-ro-creds",
  "namespace": "openshift-cloud-credential-operator"
}
----

.. Delete each of the referenced component secrets:
+
[source,terminal]
----
$ oc delete secret <secret_name> \//<1>
  -n <secret_namespace> <2>
----
+
<1> Specify the name of a secret.
<2> Specify the namespace that contains the secret.
+
.Example deletion of an AWS secret
+
[source,terminal]
----
$ oc delete secret ebs-cloud-credentials -n openshift-cluster-csi-drivers
----
+
You do not need to manually delete the credentials from your provider console. Deleting the referenced component secrets will cause the CCO to delete the existing credentials from the platform and create new ones.

.Verification

To verify that the credentials have changed:

. In the *Administrator* perspective of the web console, navigate to *Workloads* -> *Secrets*.

. Verify that the contents of the *Value* field or fields have changed.

// Provider-side verification also possible, though cluster-side is cleaner process.
. To verify that the credentials have changed from the console of your cloud provider:

.. Get the `CredentialsRequest` CR names for your platform:
+
[source,terminal]
----
$ oc -n openshift-cloud-credential-operator get CredentialsRequest -o json | jq -r '.items[] | select (.spec[].kind=="<provider_spec>") | .metadata.name'
----
+
Where `<provider_spec>` is the corresponding value for your cloud provider: `AWSProviderSpec` for AWS, `AzureProviderSpec` for Azure, or `GCPProviderSpec` for {gcp-short}.
+
.Example output for AWS
+
[source,terminal]
----
aws-ebs-csi-driver-operator
cloud-credential-operator-iam-ro
openshift-image-registry
openshift-ingress
openshift-machine-api-aws
----

.. Get the IAM username that corresponds to each `CredentialsRequest` CR name:
+
[source,terminal]
----
$ oc get credentialsrequest <cr_name> -n openshift-cloud-credential-operator -o json | jq -r ".status.providerStatus"
----
+
Where `<cr_name>` is the name of a `CredentialsRequest` CR.
+
.Example output for AWS
+
[source,json]
----
{
  "apiVersion": "cloudcredential.openshift.io/v1",
  "kind": "AWSProviderStatus",
  "policy": "<example-iam-username-policy>",
  "user": "<example-iam-username>"
}
----
+
Where `<example-iam-username>` is the name of an IAM user on the cloud provider.

.. For each IAM username, view the details for the user on the cloud provider. The credentials should show that they were created after being rotated on the cluster.

[role="_additional-resources"]
.Additional resources
* vSphere CSI Driver Operator

[id="passthrough-mode-reduce-permissions"]
== Reducing permissions after installation
When using passthrough mode, each component has the same permissions used by all other components. If you do not reduce the permissions after installing, all components have the broad permissions that are required to run the installer.

After installation, you can reduce the permissions on your credential to only those that are required to run the cluster, as defined by the `CredentialsRequest` CRs in the release image for the version of OpenShift Container Platform that you are using.

To locate the `CredentialsRequest` CRs that are required for AWS, Azure, or {gcp-short} and learn how to change the permissions the CCO uses, see _Manually creating long-term credentials_ for AWS, Azure, or {gcp-short}.

[role="_additional-resources"]
== Additional resources

* Manually creating long-term credentials for AWS
* Manually creating long-term credentials for Azure
* Manually creating long-term credentials for {gcp-short}
