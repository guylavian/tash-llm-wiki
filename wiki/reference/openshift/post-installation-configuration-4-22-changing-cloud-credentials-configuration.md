---
title: "Changing the cloud provider credentials configuration"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-changing-cloud-credentials-configuration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/changing-cloud-credentials-configuration
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Changing the cloud provider credentials configuration

[id="changing-cloud-credentials-configuration"]
= Changing the cloud provider credentials configuration

For supported configurations, you can change how OpenShift Container Platform authenticates with your cloud provider.

To determine which cloud credentials strategy your cluster uses, see Determining the Cloud Credential Operator mode.

[id="ccoctl-rotate-cloud-creds_{context}"]
== Rotating cloud provider service keys with the Cloud Credential Operator utility

Some organizations require the rotation of the service keys that authenticate the cluster.
You can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to update keys for clusters installed on the following cloud providers:

* {aws-first} with {sts-first}
* {gcp-first} with {gcp-wid-short}
* {azure-first} with {entra-short}
* {ibm-cloud-title}

//Rotating OIDC bound service account signer keys
// Module included in the following assemblies:
//
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc

[id="rotating-bound-service-keys_{context}"]

[role="_abstract"]
You can rotate the bound service account signer key for an OpenShift Container Platform cluster
that uses the Cloud Credential Operator (CCO) in manual mode with

To rotate the key, you delete the existing key on your cluster, which causes the Kubernetes API server to create a new key.
To reduce authentication failures during this process, you must immediately add the new public key to the existing issuer file.
After the cluster is using the new key for authentication, you can remove any remaining keys.

//Modified version of the disclaimer from enabling Azure WID on an existing cluster, since there are similar concerns:
[IMPORTANT]
====
The process to rotate OIDC bound service account signer keys is disruptive and takes a significant amount of time.
Some steps are time-sensitive.
Before proceeding, observe the following considerations:

* Read the following steps and ensure that you understand and accept the time requirement.
The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour.

* To reduce the risk of authentication failures, ensure that you understand and prepare for the time-sensitive steps.

* During this process, you must refresh all service accounts and restart all pods on the cluster.
These actions are disruptive to workloads.
To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready.
====

.Prerequisites

* You have access to the {oc-first} as a user with the `cluster-admin` role.

//Permissions requirements (per platform, for install and key rotation)

* You have configured the `ccoctl` utility.
* Your cluster is in a stable state.
You can confirm that the cluster is stable by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster --minimum-stable-period=5s
----

.Procedure

. Configure the following environment variables:
+
[source,text]
----
INFRA_ID=$(oc get infrastructures cluster -o jsonpath='{.status.infrastructureName}')
CLUSTER_NAME=${INFRA_ID%-*} <1>
CURRENT_ISSUER=$(oc get authentication cluster -o jsonpath='{.spec.serviceAccountIssuer}')
GCP_BUCKET=$(echo ${CURRENT_ISSUER} | cut -d "/" -f4)
CLUSTER_NAME=${GCP_BUCKET%-*}
CURRENT_ISSUER=$(oc get authentication cluster -o jsonpath='{.spec.serviceAccountIssuer}')
AZURE_STORAGE_ACCOUNT=$(echo ${CURRENT_ISSUER} | cut -d "/" -f3 | cut -d "." -f1)
AZURE_STORAGE_CONTAINER=$(echo ${CURRENT_ISSUER} | cut -d "/" -f4)
----
<1> This value should match the name of the cluster that was specified in the `metadata.name` field of the `install-config.yaml` file during installation.
+
[NOTE]
====
Your cluster might differ from this example, and the resource names might not be derived identically from the cluster name.
Ensure that you specify the correct corresponding resource names for your cluster.
====
** For {aws-short} clusters that store the OIDC configuration in a public S3 bucket, configure the following environment variable:
+
[source,text]
----
AWS_BUCKET=$(oc get authentication cluster -o jsonpath={'.spec.serviceAccountIssuer'} | awk -F'://' '{print$2}' |awk -F'.' '{print$1}')
----

** For {aws-short} clusters that store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL, complete the following steps:

... Extract the public CloudFront distribution URL by running the following command:
+
[source,terminal]
----
$ basename $(oc get authentication cluster -o jsonpath={'.spec.serviceAccountIssuer'} )
----
+
.Example output
[source,text]
----
<subdomain>.cloudfront.net
----
+
where `<subdomain>` is an alphanumeric string.

... Determine the private S3 bucket name by running the following command:
+
[source,terminal]
----
$ aws cloudfront list-distributions --query "DistributionList.Items[].{DomainName: DomainName, OriginDomainName: Origins.Items[0].DomainName}[?contains(DomainName, '<subdomain>.cloudfront.net')]"
----
+
.Example output
[source,text]
----
[
    {
        "DomainName": "<subdomain>.cloudfront.net",
        "OriginDomainName": "<s3_bucket>.s3.us-east-2.amazonaws.com"
    }
]
----
+
where `<s3_bucket>` is the private S3 bucket name for your cluster.

... Configure the following environment variable:
+
[source,text]
----
AWS_BUCKET=$<s3_bucket>
----
+
where `<s3_bucket>` is the private S3 bucket name for your cluster.

. Create a temporary directory to use and assign it an environment variable by running the following command:
+
[source,terminal]
----
$ TEMPDIR=$(mktemp -d)
----

. To cause the Kubernetes API server to create a new bound service account signing key, you delete the next bound service account signing key.
+
[IMPORTANT]
====
After you complete this step, the Kubernetes API server starts to roll out a new key.
To reduce the risk of authentication failures, complete the remaining steps as quickly as possible.
The remaining steps might be disruptive to workloads.
====
+
When you are ready, delete the next bound service account signing key by running the following command:
+
[source,terminal]
----
$ oc delete secrets/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator
----

. Download the public key from the service account signing key secret that the Kubernetes API server created by running the following command:
+
[source,terminal]
----
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 \
  -d > ${TEMPDIR}/serviceaccount-signer.public
----

. Use the public key to create a `keys.json` file by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-identity-provider \
  --dry-run \// <1>
  --output-dir ${TEMPDIR} \
  --public-key-file=${TEMPDIR}/serviceaccount-signer.public \// <2>
  --name fake \// <3>
  --region us-east-1 <4>
----
<1> The `--dry-run` option outputs files, including the new `keys.json` file, to the disk without making API calls.
<2> Specify the path to the public key that you downloaded in the previous step.
<3> Because the `--dry-run` option does not make any API calls, some parameters do not require real values.
<4> Specify any valid {aws-short} region, such as `us-east-1`.
This value does not need to match the region the cluster is in.
+
[source,terminal]
----
$ ccoctl gcp create-workload-identity-provider \
  --dry-run \// <1>
  --output-dir=${TEMPDIR} \
  --public-key-file=${TEMPDIR}/serviceaccount-signer.public \// <2>
  --name fake \// <3>
  --project fake \
  --workload-identity-pool fake
----
<1> The `--dry-run` option outputs files, including the new `keys.json` file, to the disk without making API calls.
<2> Specify the path to the public key that you downloaded in the previous step.
<3> Because the `--dry-run` option does not make any API calls, some parameters do not require real values.
+
[source,terminal]
----
$ ccoctl aws create-identity-provider \// <1>
  --dry-run \// <2>
  --output-dir ${TEMPDIR} \
  --public-key-file=${TEMPDIR}/serviceaccount-signer.public \// <3>
  --name fake \// <4>
  --region us-east-1 <5>
----
<1> The `ccoctl azure` command does not include a `--dry-run` option.
To use the `--dry-run` option, you must specify `aws` for an {azure-short} cluster.
<2> The `--dry-run` option outputs files, including the new `keys.json` file, to the disk without making API calls.
<3> Specify the path to the public key that you downloaded in the previous step.
<4> Because the `--dry-run` option does not make any API calls, some parameters do not require real values.
<5> Specify any valid {aws-short} region, such as `us-east-1`.
This value does not need to match the region the cluster is in.

. Rename the `keys.json` file by running the following command:
+
[source,terminal]
----
$ cp ${TEMPDIR}/<number>-keys.json ${TEMPDIR}/jwks.new.json
----
+
where `<number>` is a two-digit numerical value that varies depending on your environment.

. Download the existing `keys.json` file from the cloud provider by running the following command:
+
[source,terminal]
----
$ aws s3api get-object \
  --bucket ${AWS_BUCKET} \
  --key keys.json ${TEMPDIR}/jwks.current.json
----
** For {gcp-short} clusters that store OIDC keys in a public bucket, run the following command:
+
[source,terminal]
----
$ gcloud storage cp gs://${GCP_BUCKET}/keys.json ${TEMPDIR}/jwks.current.json
----

** For {gcp-short} clusters that attach OIDC keys directly to the workload identity pool, run the following command:
+
[source,terminal]
----
$ gcloud iam workload-identity-pools providers describe \
  --format json \
  --location global \
  --workload-identity-pool ${CLUSTER_NAME} ${CLUSTER_NAME} \
  | jq -r ".oidc.jwksJson" > ${TEMPDIR}/jwks.current.json
----
+
[source,terminal]
----
$ az storage blob download \
  --container-name ${AZURE_STORAGE_CONTAINER} \
  --account-name ${AZURE_STORAGE_ACCOUNT} \
  --name 'openid/v1/jwks' \
  -f ${TEMPDIR}/jwks.current.json
----

. Combine the two `keys.json` files by running the following command:
+
[source,terminal]
----
$ jq -s '{ keys: map(.keys[])}' ${TEMPDIR}/jwks.current.json ${TEMPDIR}/jwks.new.json > ${TEMPDIR}/jwks.combined.json
----

. To enable authentication for the old and new keys during the rotation, upload the combined `keys.json` file to the cloud provider by running the following command:
+
[source,terminal]
----
$ aws s3api put-object \
  --bucket ${AWS_BUCKET} \
  --tagging "openshift.io/cloud-credential-operator/${CLUSTER_NAME}=owned" \
  --key keys.json \
  --body ${TEMPDIR}/jwks.combined.json
----
** For {gcp-short} clusters that store OIDC keys in a public bucket, run the following command:
+
[source,terminal]
----
$ gcloud storage cp ${TEMPDIR}/jwks.combined.json gs://${GCP_BUCKET}/keys.json
----

** For {gcp-short} clusters that attach OIDC keys directly to the workload identity pool, run the following command:
+
[source,terminal]
----
$ gcloud iam workload-identity-pools providers update-oidc ${CLUSTER_NAME} \
  --location=global \
  --workload-identity-pool=${CLUSTER_NAME} \
  --jwk-json-path=${TEMPDIR}/jwks.combined.json
----
+
[source,terminal]
----
$ az storage blob upload \
  --overwrite \
  --account-name ${AZURE_STORAGE_ACCOUNT} \
  --container-name ${AZURE_STORAGE_CONTAINER} \
  --name 'openid/v1/jwks' \
  -f ${TEMPDIR}/jwks.combined.json
----

. Wait for the Kubernetes API server to update and use the new key.
You can monitor the update progress by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All clusteroperators are stable
----

. To ensure that all pods on the cluster use the new key, you must restart them.
+
[IMPORTANT]
====
This step maintains uptime for services that are configured for high availability across multiple nodes, but might cause downtime for any services that are not.
====
+
Restart all of the pods in the cluster by running the following command:
+
[source,terminal]
----
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
----

. Monitor the restart and update process by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-node-reboot nodes --all
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All nodes rebooted
----

. Monitor the update progress by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All clusteroperators are stable
----

. Replace the combined `keys.json` file with the updated `keys.json` file on the cloud provider by running the following command:
+
[source,terminal]
----
$ aws s3api put-object \
  --bucket ${AWS_BUCKET} \
  --tagging "openshift.io/cloud-credential-operator/${CLUSTER_NAME}=owned" \
  --key keys.json \
  --body ${TEMPDIR}/jwks.new.json
----
** For {gcp-short} clusters that store OIDC keys in a public bucket, run the following command:
+
[source,terminal]
----
$ gcloud storage cp ${TEMPDIR}/jwks.new.json gs://${GCP_BUCKET}/keys.json
----

** For {gcp-short} clusters that attach OIDC keys directly to the workload identity pool, run the following command:
+
[source,terminal]
----
$ gcloud iam workload-identity-pools providers update-oidc ${CLUSTER_NAME} \
  --location=global \
  --workload-identity-pool=${CLUSTER_NAME} \
  --jwk-json-path=${TEMPDIR}/jwks.new.json
----
+
[source,terminal]
----
$ az storage blob upload \
  --overwrite \
  --account-name ${AZURE_STORAGE_ACCOUNT} \
  --container-name ${AZURE_STORAGE_CONTAINER} \
  --name 'openid/v1/jwks' \
  -f ${TEMPDIR}/jwks.new.json
----

//Rotating OIDC bound service account signer keys

//Rotating OIDC bound service account signer keys

//Rotating {ibm-cloud-title} credentials
// Module included in the following assemblies:
//
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc

[id="refreshing-service-ids-ibm-cloud_{context}"]
= Rotating {ibm-cloud-title} credentials

You can rotate API keys for your existing service IDs and update the corresponding secrets.

.Prerequisites

* You have configured the `ccoctl` utility.
* You have existing service IDs in a live OpenShift Container Platform cluster installed.

.Procedure

* Use the `ccoctl` utility to rotate your API keys for the service IDs and update the secrets by running the following command:
+
[source,terminal]
----
$ ccoctl <provider_name> refresh-keys \// <1>
    --kubeconfig <openshift_kubeconfig_file> \// <2>
    --credentials-requests-dir <path_to_credential_requests_directory> \// <3>
    --name <name> <4>
----
<1> The name of the provider. For example: `ibmcloud` or `powervs`.
<2> The `kubeconfig` file associated with the cluster. For example, `<installation_directory>/auth/kubeconfig`.
<3> The directory where the credential requests are stored.
<4> The name of the OpenShift Container Platform cluster.
+
--
[NOTE]
====
If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.
====
--

[id="post-install-rotate-cloud-creds_{context}"]
== Rotating cloud provider credentials

Some organizations require the rotation of the cloud provider credentials.
To allow the cluster to use the new credentials, you must update the secrets that the Cloud Credential Operator (CCO) uses to manage cloud provider credentials.

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
* The Cloud Credential Operator in mint mode
* The Cloud Credential Operator in passthrough mode
* vSphere CSI Driver Operator

[id="post-install-remove-cloud-creds_{context}"]
== Removing cloud provider credentials
//TODO: split out rotate, maintain, and remove and bumpe everything up one level

After installing OpenShift Container Platform, some organizations require the removal of the cloud provider credentials that were used during the initial installation.
To allow the cluster to use the new credentials, you must update the secrets that the Cloud Credential Operator (CCO) uses to manage cloud provider credentials.

//Removing cloud provider credentials manually
// Module included in the following assemblies:
//
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc

[id="manually-removing-cloud-creds_{context}"]
= Removing cloud provider credentials

For clusters that use the Cloud Credential Operator (CCO) in mint mode, the administrator-level credential is stored in the `kube-system` namespace.
The CCO uses the `admin` credential to process the `CredentialsRequest` objects in the cluster and create users for components with limited permissions.

After installing an OpenShift Container Platform cluster with the CCO in mint mode, you can remove the administrator-level credential secret from the `kube-system` namespace in the cluster.
The CCO only requires the administrator-level credential during changes that require reconciling new or modified `CredentialsRequest` custom resources, such as minor cluster version updates.

[NOTE]
====
Before performing a minor version cluster update (for example, updating from OpenShift Container Platform {ocp-nminus1} to ), you must reinstate the credential secret with the administrator-level credential.
If the credential is not present, the update might be blocked.
====

.Prerequisites

* Your cluster is installed on a platform that supports removing cloud credentials from the CCO.
Supported platforms are AWS and {gcp-short}.

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

|{gcp-short}
|`gcp-credentials`

|===

. Click the Options menu {kebab} in the same row as the secret and select *Delete Secret*.

[role="_additional-resources"]
.Additional resources
* The Cloud Credential Operator in mint mode

[id="post-install-enable-token-auth_{context}"]
== Enabling token-based authentication
//Today, just Entra. But this should be a section that anticipates the addition of AWS STS and GCP WID.

After installing an OpenShift Container Platform cluster on {azure-first} or {aws-first}, you can enable {entra-first} or {sts-first} to use short-term credentials.

//Configuring the Cloud Credential Operator utility
// Module included in the following assemblies:
//
//Postinstall and update content
// * post_installation_configuration/changing-cloud-credentials-configuration.adoc
// * updating/preparing_for_updates/preparing-manual-creds-update.adoc
//
//Platforms that must use `ccoctl` and update content
// * installing/installing_ibm_cloud/configuring-iam-ibm-cloud.adoc
// * installing/installing_ibm_powervs/preparing-to-install-on-ibm-power-vs.doc
// * installing/installing_nutanix/preparing-to-install-on-nutanix.adoc
//
// AWS assemblies:
// * installing/installing_aws/installing-aws-customizations.adoc
// * installing/installing_aws/installing-restricted-networks-aws-installer-provisioned.adoc
// * installing/installing_aws/installing-aws-vpc.adoc
// * installing/installing_aws/installing-aws-private.adoc
// * installing/installing_aws/installing-aws-government-region.adoc
// * installing/installing_aws/installing-aws-secret-region.adoc
// * installing/installing_aws/installing-aws-china.adoc
// * installing/installing_aws/installing-aws-outposts-remote-workers.adoc
//
// GCP assemblies:
// * installing/installing_gcp/installing-gcp-customizations.adoc
// * installing/installing_gcp/installing-gcp-network-customizations.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp-installer-provisioned.adoc
// * installing/installing_gcp/installing-gcp-vpc.adoc
// * installing/installing_gcp/installing-gcp-shared-vpc.adoc
// * installing/installing_gcp/installing-gcp-private.adoc
//
// Azure assemblies
// * installing/installing_azure/installing-azure-customizations.adoc
// * installing/installing_azure/installing-azure-government-region.adoc
// * installing/installing_azure/installing-azure-private.adoc
// * installing/installing_azure/installing-azure-vnet.adoc
// * installing/installing_azure/installing-restricted-networks-azure-installer-provisioned.adoc

//Postinstall  and update content

//Platforms that must use `ccoctl`

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

[id="cco-ccoctl-configuring_{context}"]

[role="_abstract"]
//Nutanix-only intro because it needs context in its install procedure.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on Nutanix, you must set the CCO to `manual` mode as part of the installation process.
The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). To install a cluster on {ibm-power-server-name}, you must set the CCO to `manual` mode as part of the installation process.

//The upgrade and postinstall procs also have a different intro, so they are excluded here.
To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

//Intro for the postinstall procs.
To configure an existing cluster to create and manage cloud credentials from outside of the cluster, extract and prepare the Cloud Credential Operator utility (`ccoctl`) binary.

//Intro for the upgrade procs.
To upgrade a cluster that uses the Cloud Credential Operator (CCO) in manual mode to create and manage cloud credentials from outside of the cluster, extract and prepare the CCO utility (`ccoctl`) binary.

[NOTE]
====
The `ccoctl` utility is a Linux binary that must run in a Linux environment.
====

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the {oc-first}.

//Upgrade prereqs
* Your cluster was configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

//Permissions requirements (per platform, for install and key rotation)

.Procedure

. Set a variable for the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----
----
$ RELEASE_IMAGE=$(oc get clusterversion -o jsonpath={..desired.image})
----

. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
----
+
[NOTE]
====
Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
====

. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
----
+
For `<rhel_version>`, specify the value that corresponds to the version of {op-system-base-full} that the host uses.
If no value is specified, `ccoctl.rhel8` is used by default.
The following values are valid:
+
* `rhel8`: Specify this value for hosts that use {op-system-base} 8.
* `rhel9`: Specify this value for hosts that use {op-system-base} 9.

+
[NOTE]
====
The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
====

. Change the permissions to make `ccoctl` executable by running the following command:
+
[source,terminal]
----
$ chmod 775 ccoctl
----

.Verification

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:
+
[source,terminal]
----
$ ./ccoctl
----
+
.Example output
[source,terminal]
----
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
----

//Postinstall and update content

//Platforms that must use `ccoctl` and update content

//AWS install assemblies

//GCP install assemblies

//global Azure install assemblies

//Enabling {entra-first} on an existing cluster
// Module included in the following assemblies:
//
// * post_installation_configuration/cluster-tasks.adoc

[id="enabling-entra-workload-id-existing-cluster_{context}"]
= Enabling {entra-first} on an existing cluster

[role="_abstract"]
Enable {entra-first} on an existing {azure-first} OpenShift Container Platform cluster. If you did not configure your cluster to use {entra-first} during installation, you can enable this authentication method post-installation.

[IMPORTANT]
====
The process to enable {entra-short} on an existing cluster is disruptive and takes a significant amount of time.
Before proceeding, observe the following considerations:

* Read the following steps and ensure that you understand and accept the time requirement.
The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour.

* During this process, you must refresh all service accounts and restart all pods on the cluster.
These actions are disruptive to workloads.
To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready.

* After starting this process, do not attempt to update the cluster until it is complete.
If an update is triggered, the process to enable {entra-short} on an existing cluster fails.
====

.Prerequisites

* You have installed an OpenShift Container Platform cluster on {azure-first}.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the {oc-first}.
* You have extracted and prepared the Cloud Credential Operator utility (`ccoctl`) binary.
* You have access to your {azure-short} account by using the {azure-short} CLI (`az`).

.Procedure

. Create an output directory for the manifests that the `ccoctl` utility generates.
This procedure uses `./output_dir` as an example.

. Extract the service account public signing key for the cluster to the output directory by running the following command:
+
[source,terminal]
----
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 -d \
  > output_dir/serviceaccount-signer.public <1>
----
<1> This procedure uses a file named `serviceaccount-signer.public` as an example.

. Use the extracted service account public signing key to create an OpenID Connect (OIDC) issuer and {azure-short} blob storage container with OIDC configuration files by running the following command:
+
[source,terminal]
----
$ ./ccoctl azure create-oidc-issuer \
  --name <azure_infra_name> \// <1>
  --output-dir ./output_dir \
  --region <azure_region> \// <2>
  --subscription-id <azure_subscription_id> \// <3>
  --tenant-id <azure_tenant_id> \
  --public-key-file ./output_dir/serviceaccount-signer.public <4>
----
<1> The value of the `name` parameter is used to create an Azure resource group.
To use an existing Azure resource group instead of creating a new one, specify the `--oidc-resource-group-name` argument with the existing group name as its value.
<2> Specify the region of the existing cluster.
<3> Specify the subscription ID of the existing cluster.
<4> Specify the file that contains the service account public signing key for the cluster.

. Verify that the configuration file for the Azure pod identity webhook was created by running the following command:
+
[source,terminal]
----
$ ll ./output_dir/manifests
----
+
.Example output
+
[source,text]
----
total 8
-rw-------. 1 cloud-user cloud-user 193 May 22 02:29 azure-ad-pod-identity-webhook-config.yaml <1>
-rw-------. 1 cloud-user cloud-user 165 May 22 02:29 cluster-authentication-02-config.yaml
----
<1> The file `azure-ad-pod-identity-webhook-config.yaml` contains the Azure pod identity webhook configuration.

. Set an `OIDC_ISSUER_URL` variable with the OIDC issuer URL from the generated manifests in the output directory by running the following command:
+
[source,terminal]
----
$ OIDC_ISSUER_URL=`awk '/serviceAccountIssuer/ { print $2 }' ./output_dir/manifests/cluster-authentication-02-config.yaml`
----

. Update the `spec.serviceAccountIssuer` parameter of the cluster `authentication` configuration by running the following command:
+
[source,terminal]
----
$ oc patch authentication cluster \
  --type=merge \
  -p "{\"spec\":{\"serviceAccountIssuer\":\"${OIDC_ISSUER_URL}\"}}"
----

. Monitor the configuration update progress by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All clusteroperators are stable
----

. Restart all of the pods in the cluster by running the following command:
+
[source,terminal]
----
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
----
+
Restarting a pod updates the `serviceAccountIssuer` field and refreshes the service account public signing key.

. Monitor the restart and update process by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-node-reboot nodes --all
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All nodes rebooted
----

. Update the Cloud Credential Operator `spec.credentialsMode` parameter to `Manual` by running the following command:
+
[source,terminal]
----
$ oc patch cloudcredential cluster \
  --type=merge \
  --patch '{"spec":{"credentialsMode":"Manual"}}'
----

. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --credentials-requests \
  --included \
  --to <path_to_directory_for_credentials_requests> \
  --registry-config ~/.pull-secret
----
+
[NOTE]
====
This command might take a few moments to run.
====

. Set an `AZURE_INSTALL_RG` variable with the {azure-short} resource group name by running the following command:
+
[source,terminal]
----
$ AZURE_INSTALL_RG=`oc get infrastructure cluster -o jsonpath --template '{ .status.platformStatus.azure.resourceGroupName }'`
----

. Use the `ccoctl` utility to create managed identities for all `CredentialsRequest` objects by running the following command:
+
[NOTE]
====
The following command does not show all available options. For a complete list of options, including those that might be necessary for your specific use case, run `$ ccoctl azure create-managed-identities --help`.
====
+
[source,terminal]
----
$ ccoctl azure create-managed-identities \
  --name <azure_infra_name> \
  --output-dir ./output_dir \
  --region <azure_region> \
  --subscription-id <azure_subscription_id> \
  --credentials-requests-dir <path_to_directory_for_credentials_requests> \
  --issuer-url "${OIDC_ISSUER_URL}" \
  --dnszone-resource-group-name <azure_dns_zone_resourcegroup_name> \// <1>
  --installation-resource-group-name "${AZURE_INSTALL_RG}" \
  --network-resource-group-name <azure_resource_group> \// <2>
  --preserve-existing-roles <3>
----
<1> Specify the name of the resource group that contains the DNS zone.
<2> Optional: Specify the virtual network resource group if it is different from the cluster resource group.
<3> Optional: Specify this flag to ensure that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates.

. Apply the {azure-short} pod identity webhook configuration for {entra-short} by running the following command:
+
[source,terminal]
----
$ oc apply -f ./output_dir/manifests/azure-ad-pod-identity-webhook-config.yaml
----

. Apply the secrets generated by the `ccoctl` utility by running the following command:
+
[source,terminal]
----
$ find ./output_dir/manifests -iname "openshift*yaml" -print0 | xargs -I {} -0 -t oc replace -f {}
----
+
This process might take several minutes.

. Restart all of the pods in the cluster by running the following command:
+
[source,terminal]
----
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
----
+
Restarting a pod updates the `serviceAccountIssuer` field and refreshes the service account public signing key.

. Monitor the restart and update process by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-node-reboot nodes --all
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All nodes rebooted
----

. Monitor the configuration update progress by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All clusteroperators are stable
----

. Optional: Remove the {azure-short} root credentials secret by running the following command:
+
[source,terminal]
----
$ oc delete secret -n kube-system azure-credentials
----

//Enabling AWS {sts-first} on an existing cluster
// Module included in the following assemblies:
//
// /post_installation_configuration/changing-cloud-credentials-configuration.adoc

[id="enabling-aws-sts-existing-cluster_{context}"]
= Enabling {aws-short} {sts-first} on an existing cluster

[role="_abstract"]
Enable {aws-short} {sts-first} on an existing OpenShift Container Platform cluster if you did not configure this authentication method during installation.

[IMPORTANT]
====
The process to enable {sts-short} on an existing cluster is disruptive and takes a significant amount of time.
Before proceeding, observe the following considerations:

* Read the following steps and ensure that you understand and accept the time requirement.
The exact time requirement varies depending on the individual cluster, but it is likely to require at least one hour.

* During this process, you must refresh all service accounts and restart all pods on the cluster.
These actions are disruptive to workloads.
To mitigate this impact, you can temporarily halt these services and then redeploy them when the cluster is ready.

* Do not update the cluster until this process is complete.
====

.Prerequisites

* You have installed an OpenShift Container Platform cluster on {aws-short}.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the {oc-first}.
* You have extracted and prepared the Cloud Credential Operator utility (`ccoctl`) binary.
* You have access to your AWS account by using the AWS CLI (aws).

.Procedure

. Create an output directory for `ccoctl` generated manifests.
+
[source,terminal]
----
$ mkdir ./output_dir
----

. Create the {aws-short} Identity and Access Management (IAM) OpenID Connect (OIDC) provider.

.. Extract the service account public signing key for the cluster by running the following command:
+
[source,terminal]
----
$ oc get secret/next-bound-service-account-signing-key \
  -n openshift-kube-apiserver-operator \
  -ojsonpath='{ .data.service-account\.pub }' | base64 -d \
  > output_dir/serviceaccount-signer.public <1>
----
<1> This procedure uses a file named `serviceaccount-signer.public` as an example.

.. Create the {aws-short} IAM identity provider and S3 bucket by running the following command:
+
[source,terminal]
----
$ ./ccoctl aws create-identity-provider \
  --output-dir output_dir \ <1>
  --name <name_you_choose> \ <2>
  --region us-east-2 \ <3>
  --public-key-file output_dir/serviceaccount-signer.public <4>
----
<1> Specify the output directory you created earlier.
<2> Specify a globally unique name. This name functions as a prefix for AWS resources created by this command.
<3> Specify the AWS region of the cluster.
<4> Specify the relative path to the `serviceaccount-signer.public` file you created earlier.

.. Save or note the Amazon Resource Name (ARN) for the IAM identity provider. You can find this information in the final line of the output of the previous command.

. Update the cluster authentication configuration.

.. Extract the OIDC issuer URL and update the authentication configuration of the cluster by running the following commands:
+
[source,terminal]
----
$ OIDC_ISSUER_URL=`awk '/serviceAccountIssuer/ { print $2 }' output_dir/manifests/cluster-authentication-02-config.yaml`
$ oc patch authentication cluster --type=merge -p "{\"spec\":{\"serviceAccountIssuer\":\"${OIDC_ISSUER_URL}\"}}"
----

.. Monitor the configuration update progress by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All clusteroperators are stable
----

. Restart pods to apply the issuer update.

.. Restart all of the pods in the cluster by running the following command:
+
[source,terminal]
----
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
----
+
Restarting a pod updates the `serviceAccountIssuer` field and refreshes the service account public signing key.

.. Monitor the restart and update process by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-node-reboot nodes --all
----
+
This process might take 15 minutes or longer. The following output indicates that the process is complete:
+
[source,text]
----
All nodes rebooted
----

. Update the Cloud Credential Operator `spec.credentialsMode` parameter to `Manual` by running the following command:
+
[source,terminal]
----
$ oc patch cloudcredential cluster \
  --type=merge \
  --patch '{"spec":{"credentialsMode":"Manual"}}'
----

. Extract `CredentialsRequests` objects.

.. Create a `CLUSTER_VERSION` environment variable by running the following command:
+
[source,terminal]
----
$ CLUSTER_VERSION=$(oc get clusterversion version -o json | jq -r '.status.desired.version')
----

.. Create a `CLUSTER_IMAGE` environment variable by running the following command:
+
[source,terminal]
----
$ CLUSTER_IMAGE=$(oc get clusterversion version -o json | jq -r ".status.history[] | select(.version == \"${CLUSTER_VERSION}\") | .image")
----

.. Extract `CredentialsRequests` objects from the release image by running the following command:
+
[source,terminal]
----
$ oc adm release extract \
  --credentials-requests \
  --cloud=aws \
  --from ${CLUSTER_IMAGE} \
  --to output_dir/cred-reqs
----

. Create {aws-short} IAM roles and apply secrets.

.. Create an IAM role for each `CredentialsRequests` object by running the following command:
+
[source,terminal]
----
$ ./ccoctl aws create-iam-roles \
  --output-dir ./output_dir/ \ <1>
  --name <name_you_choose> \ <2>
  --identity-provider-arn <identity_provider_arn> \ <3>
  --region us-east-2 \ <4>
  --credentials-requests-dir ./output_dir/cred-reqs/ \ <5>
  --permissions-boundary-arn=<policy_arn> <6>
----
<1> Specify the output directory you created earlier.
<2> Specify a globally unique name. This name functions as a prefix for AWS resources created by this command.
<3> Specify the ARN for the IAM identity provider.
<4> Specify the AWS region of the cluster.
<5> Specify the relative path to the folder where you extracted the `CredentialsRequest` files with the `oc adm release extract` command.
<6> Optional: Specify the Amazon Resource Name (ARN) of the {aws-short} IAM policy to use as the permissions boundary for the IAM roles created by the `ccoctl` utility.

.. Apply the generated secrets by running the following command:
+
[source,terminal]
----
$ find ./output_dir/manifests -iname "openshift*yaml" -print0 | xargs -I {} -0 -t oc replace -f {}
----

. Finish the configuration process by restarting the cluster.

.. Restart all of the pods in the cluster by running the following command:
+
[source,terminal]
----
$ oc adm reboot-machine-config-pool mcp/worker mcp/master
----

.. Monitor the restart and update process by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-node-reboot nodes --all
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All nodes rebooted
----

.. Monitor the configuration update progress by running the following command:
+
[source,terminal]
----
$ oc adm wait-for-stable-cluster
----
+
This process might take 15 minutes or longer.
The following output indicates that the process is complete:
+
[source,text]
----
All clusteroperators are stable
----

. Optional: Remove the {aws-short} root credentials secret by running the following command:
+
[source,terminal]
----
$ oc delete secret -n kube-system aws-creds
----

[role="_additional-resources"]
.Additional resources
* Microsoft Entra Workload ID
* Configuring an Azure cluster to use short-term credentials
* AWS Security Token Service
* Configuring an AWS cluster to use short-term credentials

//Verifying the credentials configuration
// Module included in the following assemblies:
//
// * installing/validation_and_troubleshooting/validating-an-installation.adoc
// * post_installation_configuration/cluster-tasks.adoc

[id="cco-ccoctl-install-verifying_{context}"]
= Verifying that a cluster uses short-term credentials

[role="_abstract"]
You can verify that a cluster uses short-term security credentials for individual components by checking the Cloud Credential Operator (CCO) configuration and other values in the cluster.

.Prerequisites

* You deployed an OpenShift Container Platform cluster using the Cloud Credential Operator utility (`ccoctl`) to implement short-term credentials.

* You installed the {oc-first}.

* You are logged in as a user with `cluster-admin` privileges.

.Procedure

* Verify that the CCO is configured to operate in manual mode by running the following command:
+
[source,terminal]
----
$ oc get cloudcredentials cluster \
  -o=jsonpath={.spec.credentialsMode}
----
+
The following output confirms that the CCO is operating in manual mode:
+
.Example output
[source,text]
----
Manual
----

* Verify that the cluster does not have `root` credentials by running the following command:
+
[source,terminal]
----
$ oc get secrets \
  -n kube-system <secret_name>
----
+
where `<secret_name>` is the name of the root secret for your cloud provider.
+
[cols=2,options=header]
|===
|Platform
|Secret name

|{aws-first}
|`aws-creds`

|{azure-first}
|`azure-credentials`

|{gcp-first}
|`gcp-credentials`

|===
+
An error confirms that the root secret is not present on the cluster.
+
.Example output for an {aws-short} cluster
[source,text]
----
Error from server (NotFound): secrets "aws-creds" not found
----

* Verify that the components are using short-term security credentials for individual components by running the following command:
+
[source,terminal]
----
$ oc get authentication cluster \
  -o jsonpath \
  --template='{ .spec.serviceAccountIssuer }'
----
+
This command displays the value of the `.spec.serviceAccountIssuer` parameter in the cluster `Authentication` object.
An output of a URL that is associated with your cloud provider indicates that the cluster is using manual mode with short-term credentials that are created and managed from outside of the cluster.

* {azure-short} clusters: Verify that the components are assuming the {azure-short} client ID that is specified in the secret manifests by running the following command:
+
[source,terminal]
----
$ oc get secrets \
  -n openshift-image-registry installer-cloud-credentials \
  -o jsonpath='{.data}'
----
+
An output that contains the `azure_client_id` and `azure_federated_token_file` fields confirms that the components are assuming the {azure-short} client ID.

* {azure-short} clusters: Verify that the pod identity webhook is running by running the following command:
+
[source,terminal]
----
$ oc get pods \
  -n openshift-cloud-credential-operator
----
+
.Example output
[source,text]
----
NAME                                         READY   STATUS    RESTARTS   AGE
cloud-credential-operator-59cf744f78-r8pbq   2/2     Running   2          71m
pod-identity-webhook-548f977b4c-859lz        1/1     Running   1          70m
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* About the Cloud Credential Operator
