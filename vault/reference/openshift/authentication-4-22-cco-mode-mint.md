---
title: "The Cloud Credential Operator in mint mode"
type: reference
domain: openshift
slug: authentication-4-22-cco-mode-mint
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication/cco-mode-mint
version: 4.22
family: authentication
documentKind: "Documentation"
---

# The Cloud Credential Operator in mint mode

[id="cco-mode-mint"]
= The Cloud Credential Operator in mint mode

Mint mode is the default Cloud Credential Operator (CCO) credentials mode for OpenShift Container Platform on platforms that support it. Mint mode supports Amazon Web Services (AWS) and {gcp-first} clusters.

[id="mint-mode-about"]
== Mint mode credentials management

For clusters that use the CCO in mint mode, the administrator-level credential is stored in the `kube-system` namespace.
The CCO uses the `admin` credential to process the `CredentialsRequest` objects in the cluster and create users for components with limited permissions.

With mint mode, each cluster component has only the specific permissions it requires.
Cloud credential reconciliation is automatic and continuous so that components can perform actions that require additional credentials or permissions.

For example, a minor version cluster update (such as updating from OpenShift Container Platform {ocp-nminus1} to ) might include an updated `CredentialsRequest` resource for a cluster component.
The CCO, operating in mint mode, uses the `admin` credential to process the `CredentialsRequest` resource and create users with limited permissions to satisfy the updated authentication requirements.

[NOTE]
====
By default, mint mode requires storing the `admin` credential in the cluster `kube-system` namespace. If this approach does not meet the security requirements of your organization, you can remove the credential after installing the cluster.
====

[id="mint-mode-permissions"]
=== Mint mode permissions requirements
When using the CCO in mint mode, ensure that the credential you provide meets the requirements of the cloud on which you are running or installing OpenShift Container Platform. If the provided credentials are not sufficient for mint mode, the CCO cannot create an IAM user.

The credential you provide for mint mode in Amazon Web Services (AWS) must have the following permissions:

.Required AWS permissions
[%collapsible]
====
* `iam:CreateAccessKey`
* `iam:CreateUser`
* `iam:DeleteAccessKey`
* `iam:DeleteUser`
* `iam:DeleteUserPolicy`
* `iam:GetUser`
* `iam:GetUserPolicy`
* `iam:ListAccessKeys`
* `iam:PutUserPolicy`
* `iam:TagUser`
* `iam:SimulatePrincipalPolicy`
====

The credential you provide for mint mode in {gcp-first} must have the following permissions:

.Required {gcp-short} permissions
[%collapsible]
====
* `resourcemanager.projects.get`
* `serviceusage.services.list`
* `iam.serviceAccountKeys.create`
* `iam.serviceAccountKeys.delete`
* `iam.serviceAccountKeys.list`
* `iam.serviceAccounts.create`
* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.roles.create`
* `iam.roles.get`
* `iam.roles.list`
* `iam.roles.undelete`
* `iam.roles.update`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`
====

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
== Additional resources
* Removing cloud provider credentials
