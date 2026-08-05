---
title: "Creating a {product-title} cluster that uses external authentication"
type: reference
domain: openshift
slug: rosa-hcp-4-22-rosa-hcp-sts-creating-a-cluster-ext-auth
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth
version: 4.22
family: rosa_hcp
documentKind: "Documentation"
---

# Creating a {product-title} cluster that uses external authentication

[id="rosa-hcp-sts-creating-a-cluster-ext-auth"]
= Creating a OpenShift Container Platform cluster that uses external authentication

[role="_abstract"]
You can create OpenShift Container Platform clusters that use an external OpenID Connect (OIDC) identity provider to issue tokens for authentication, replacing the built-in OpenShift OAuth server.

While the built-in OpenShift OAuth server supports integration with a variety of identity providers, including external OIDC identity providers, it is limited to the capabilities of the OAuth server itself. You can directly integrate external OIDC identity providers with OpenShift Container Platform clusters to enable machine-to-machine workflows and capabilities beyond the built-in OpenShift OAuth server.

[IMPORTANT]
====
You cannot upgrade or convert existing {rosa-classic-title} clusters to {hcp} architecture. You must create a new OpenShift Container Platform cluster. You also cannot convert a cluster that was created to use external authentication providers to use the internal OAuth2 server. You must also create a new cluster.
====

[NOTE]
====
OpenShift Container Platform clusters only support {sts-first} authentication.
====

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-aws-private-creating-cluster.adoc
// * rosa_hcp/rosa-hcp-cluster-no-cni.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-aws-kms-key.adoc
// * rosa_hcp/rosa-hcp-creating-cluster-with-fips-encryption.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-prerequisites_{context}"]
= OpenShift Container Platform prerequisites

[role="_abstract"]
Before you can create a OpenShift Container Platform cluster,  you must complete the following prerequisites. Use each link to find detailed instructions for completing that specific prerequisite:

* Configure a virtual private cloud (VPC)
* Create account-wide roles
* Create the ocm-role IAM role
* Create an OIDC configuration
* Create Operator roles

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc

[id="rosa-hcp-sts-creating-a-cluster-external-auth-cluster-cli_{context}"]
= Creating a OpenShift Container Platform cluster that uses external authentication

[role="_abstract"]
Use the `--external-auth-providers-enabled` flag in the ROSA CLI to create a cluster that uses an external authentication service.

[NOTE]
====
When creating a OpenShift Container Platform cluster, the default machine Classless Inter-Domain Routing (CIDR) is `10.0.0.0/16`. If this does not correspond to the CIDR range for your VPC subnets, add `--machine-cidr <address_block>` to the following commands.
====

.Procedure

* If you used the `OIDC_ID`, `SUBNET_IDS`, and `OPERATOR_ROLES_PREFIX` variables to prepare your environment, you can continue to use those variables when creating your cluster. For example, run the following command:
+
[source,terminal]
----
$ rosa create cluster --hosted-cp --subnet-ids=$SUBNET_IDS \
   --oidc-config-id=$OIDC_ID --cluster-name=<cluster_name> \
   --operator-roles-prefix=$OPERATOR_ROLES_PREFIX \
   --external-auth-providers-enabled
----

* If you did not set environmental variables, run the following command:
+
[source,terminal]
----
$ rosa create cluster --cluster-name=<cluster_name> --sts --mode=auto \
    --hosted-cp --operator-roles-prefix <operator-role-prefix> \
    --oidc-config-id <ID-of-OIDC-configuration> \
    --external-auth-providers-enabled \
    --subnet-ids=<public-subnet-id>,<private-subnet-id>
----

.Verification
* Verify that your external authentication is enabled in the cluster details by running the following command:
+
[source,terminal]
----
$ rosa describe cluster --cluster=<cluster_name>
----
+
In the following example output, the `External Authentication` field shows that the external authentication is enabled:
+
--
[source,terminal]
----
Name:                       rosa-ext-test
Display Name:               rosa-ext-test
ID:                         <cluster_id>
External ID:                <cluster_ext_id>
Control Plane:              ROSA Service Hosted
OpenShift Version:          4.22.0
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <AWS_id>
AWS Billing Account:        <AWS_id>
API URL:                    <ocm_api>
Console URL:
Region:                     us-east-1
Availability:
 - Control Plane:           MultiAZ
 - Data Plane:              SingleAZ

Nodes:
 - Compute (desired):       2
 - Compute (current):       0
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             /23
 - Subnets:                 <subnet_ids>
EC2 Metadata Http Tokens:   optional
Role (STS) ARN:             arn:aws:iam::<AWS_id>:role/<account_roles_prefix>-HCP-ROSA-Installer-Role
Support Role ARN:           arn:aws:iam::<AWS_id>:role/<account_roles_prefix>-HCP-ROSA-Support-Role
Instance IAM Roles:
 - Worker:                  arn:aws:iam::<AWS_id>:role/<account_roles_prefix>-HCP-ROSA-Worker-Role
Operator IAM Roles:
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-openshift-cloud-network-config-controller-clo
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-kube-system-capa-controller-manager
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-kube-system-control-plane-operator
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-kube-system-kms-provider
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-kube-system-kube-controller-manager
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-openshift-image-registry-installer-cloud-cred
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-openshift-ingress-operator-cloud-credentials
 - arn:aws:iam::<AWS_id>:role/<operator_roles_prefix>-openshift-cluster-csi-drivers-ebs-cloud-crede
Managed Policies:           Yes
State:                      ready
Private:                    No
Created:                    Mar 29 2024 14:25:52 UTC
User Workload Monitoring:   Enabled
Details Page:               https://<url>
OIDC Endpoint URL:          https://<endpoint> (Managed)
Audit Log Forwarding:       Disabled
External Authentication:    Enabled
----
--

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
[id="rosa-hcp-sts-creating-a-cluster-external-auth-provider-cli_{context}"]
= Creating an external authentication provider

[role="_abstract"]
After you have created a OpenShift Container Platform cluster with the enabled option for external authentication providers, you must create a provider using the ROSA CLI.

[NOTE]
====
Similar to the `rosa create|delete|list idp[s]` command in the ROSA CLI, you cannot edit an existing identity provider that you created using `rosa create external-auth-provider`. Instead, you must delete the external authentication provider and create a new one.
====

.Procedure

* Do one of the following:
** To create your external authentication provider using interactive mode, run the following command:
+
[source,terminal]
----
$ rosa create external-auth-provider -c <cluster_name>
----

** To create your external authentication provider by entering each argument, run the following command:
+
[source,terminal]
----
$ rosa create external-auth-provider --cluster=<cluster_name> \
    --name=<provider_name> \
    --issuer-url=<issuing_url> \
    --issuer-audiences=<audience_id> \
    --issuer-ca-file=<ca_file_path> \
    --claim-mapping-username-claim=<claim_username> \
    --claim-mapping-groups-claim=<method> \
    --console-client-id=<client_id_for_app_registration> \
    --console-client-secret=<client_secret> \
    --claim-validation-rule=<claim_validation_rule>
----
+
--
where:

`<cluster_id>`:: The name or the ID of your cluster.
`<provider_name>`:: The name of your external authentication provider. This name should be a lower-case with numbers and dashes.
`<issuing_url>`:: The URL of the token issuer.
`<audience_id>`:: The audience IDs that this authentication provider issues tokens for. This is a comma-separated list of token audiences.
`<ca_file_path>`:: Optional. The certificate file to use when making requests.
`<claim_username>`:: The name of the claim that is used to construct the user names for cluster identity, such as using `email`.
`<method>`:: The method with which to transform the ID token into a cluster identity, such as using `groups`.
`<client_id_for_app_registration>`:: Optional. The application or client ID that your app registration uses for the console.
`<client_secret>`:: The client secret that is used to associate your account with the application. If you do not include the client secret, this command uses a public OIDC OAuthClient.
`<claim_validation_rule>`:: Optional. The rules that help validate token claims which authenticate your users. This field should be formatted as `:<required_value>`.
--
+
.Example output
[source,terminal]
----
I: Successfully created an external authentication provider for cluster 'ext-auth-test'
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
[id="rosa-hcp-sts-example-microsoft-entra-id-configuration_{context}"]
= Configuring Microsoft Entra ID as an external provider

[role="_abstract"]
You can configure Microsoft Entra ID as an external authentication provider for your OpenShift Container Platform cluster by using the {rosa-cli-first}. Before you configure this provider, you must have a Microsoft Entra ID server already set up.

For more information about setting up Microsoft Entra ID, see the Microsoft Entra ID documentation.

.Procedure

. Create an external authentication provider that uses Microsoft Entra ID by running the following command:
+
[NOTE]
====
You must set your own environment variables with values specific to your Microsoft Entra ID server.
====
+
[source,terminal]
----
$ rosa create external-auth-provider -c $CLUSTER_NAME \
    --claim-mapping-groups-claim groups \
    --claim-mapping-username-claim <authorized_user_name> \
    --console-client-id $CONSOLE_CLIENT_ID \
    --console-client-secret $CONSOLE_CLIENT_SECRET_VALUE \
    --issuer-audiences "$AUDIENCE_1" \
    --issuer-ca-file ca-bundle.crt --issuer-url $ISSUER_URL \
    --name m-entra-id
----
+
The output should indicate that the external authentication provider was successfully created.
+
[source,terminal]
----
I: Successfully created an external authentication provider for cluster 'ext-auth-test'. It can take a few minutes for the creation of an external authentication provider to become fully effective.
----

. List the external authentication provider for your cluster to see the issuer URL, or use `rosa describe` to see all details, by running one of the following commands:
+
.. List the external authentication configuration on a specified cluster by running the following command:
+
[source,terminal]
----
$ rosa list external-auth-provider -c <cluster_name>
----
+
The output should show the issuer URL for the external authentication provider.
+
[source,terminal]
----
NAME        ISSUER URL
m-entra-id  https://login.microsoftonline.com/<group_id>/v2.0
----
+
.. Display the external authentication configuration on a specified cluster by running the following command:
+
[source,terminal]
----
$ rosa describe external-auth-provider \
    -c <cluster_name> --name <name_of_external_authentication>
----
+
The output displays the details of the external authentication provider.
+
[source,terminal]
----
ID:                          ms-entra-id
Cluster ID:                  <cluster_id>
Issuer audiences:
                             - <audience_id>
Issuer Url:                  https://login.microsoftonline.com/<group_id>/v2.0
Claim mappings group:        groups
Claim mappings username:     email
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
[id="rosa-hcp-sts-example-keycloak-configuration_{context}"]
= Configuring Keycloak as an external provider

[role="_abstract"]
You can configure Keycloak as an external authentication provider for your OpenShift Container Platform cluster by using the {rosa-cli-first}. Before you configure this provider, you must have a Keycloak server already set up.

For more information about setting up Keycloak, see the Keycloak documentation.

.Procedure

. Create an external authentication provider that uses Keycloak by running the following command:
+
[NOTE]
====
You must set your own environment variables with values specific to your Keycloak server.
====
+
[source,terminal]
----
$ rosa create external-auth-provider -c $CLUSTER_NAME \
--claim-mapping-groups-claim groups \
    --claim-mapping-username-claim <authorized_user_name> \
    --console-client-id $CONSOLE_CLIENT_ID \
    --console-client-secret $CONSOLE_CLIENT_SECRET_VALUE \
    --issuer-audiences "$AUDIENCE_1,$AUDIENCE_2" \
    --issuer-ca-file ca-bundle.crt --issuer-url $ISSUER_URL --name keycloak
----
+
The output should indicate that the external authentication provider was successfully created.
+
[source,terminal]
----
I: Successfully created an external authentication provider for cluster 'ext-auth-test'. It can take a few minutes for the creation of an external authentication provider to become fully effective.
----

. List the external authentication provider for your cluster to see the issuer URL, or use `rosa describe` to see all details, by running one of the following commands:
.. List the external authentication configuration on a specified cluster by running the following command:
+
[source,terminal]
----
$ rosa list external-auth-provider -c <cluster_name>
----
+
The output should display the issuer URL for the external authentication provider.
+
[source,terminal]
----
NAME      ISSUER URL
keycloak  https://keycloak-keycloak.apps.<keycloak_id>.openshift.org/realms/master
----
+
.. Display the external authentication configuration on a specified cluster by running the following command:
+
[source,terminal]
----
$ rosa describe external-auth-provider \
    -c <cluster_name> --name <name_of_external_authentication>
----
+
The output displays the details of the external authentication provider.
+
[source,terminal]
----
ID:                                    keycloak
Cluster ID:                            <cluster_id>
Issuer audiences:
                                       - <audience_id_1>
                                       - <audience_id_2>
Issuer Url:                            https://keycloak-keycloak.apps.<keycloak_id>.openshift.org/realms/master
Claim mappings group:                  groups
Claim mappings username:               <authorized_user_name>
Console client id:                     console-test
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth.adoc

[id="rosa-hcp-sts-creating-a-break-glass-cred-cli_{context}"]
= Creating a break glass credential for a OpenShift Container Platform cluster

[role="_abstract"]
You can create a break glass credential to generate temporary cluster-admin credentials for OpenShift Container Platform clusters that use custom OIDC token issuers. The break glass credential provides a `kubeconfig` file that you can use to access the cluster.

.Prerequisites

* You have created a OpenShift Container Platform cluster with external authentication enabled. For more information, see _Creating a OpenShift Container Platform with HCP cluster that uses external authentication providers_.
* You have created an external authentication provider. For more information, see _Creating an external authentication provider_.
* You have an account with `cluster admin` permissions.

.Procedure

. Create a break glass credential by using one of the following commands:

** To create a break glass credential by using the interactive command interface to interactively specify custom settings, run the following command:
+
[source,terminal]
----
$ rosa create break-glass-credential -c <cluster_name> -i
----
+
This command starts an interactive CLI process:
+
[source,terminal]
----
I: Enabling interactive mode
? Username (optional):
? Expiration duration (optional):
I: Successfully created a break glass credential for cluster 'ac-hcp-test'.
----
+
--
where:

`Username`:: If left blank, the `username` field is set to a randomly generated value.
`Expiration duration`:: The minimum validity of the break glass credential is 10 minutes, and the maximum validity is 24 hours. If left blank, the expiration duration value defaults to 24 hours.
--
+
** To create a break glass credential for cluster called `mycluster` with specified values:
+
[source,terminal]
----
$ rosa create break-glass-credential -c mycluster --username test-username --expiration 1h
----
+
. List the break glass credential IDs, status, and associated users that are available for a cluster called `mycluster` by running the following command:
+
[source,terminal]
----
$ rosa list break-glass-credential -c mycluster
----
+
.Example output
[source,terminal]
----
ID                                USERNAME    STATUS
2a7jli9n4phe6c02ul7ti91djtv2o51d  test-user   issued
----
+
[NOTE]
====
You can also view the credentials in a JSON output by adding the `-o json` argument to the command.
====

. To view the status of a break glass credential, run the following command, replacing `<break_glass_credential_id>` with the break glass credential ID:
+
[source,terminal]
----
$ rosa describe break-glass-credential <break_glass_credential_id> -c <cluster_name>
----
+
.Example output
[source,terminal]
----
ID:                                    2a7jli9n4phe6c02ul7ti91djtv2o51d
Username:                              test-user
Expire at:                             Dec 28 2026 10:23:05 EDT
Status:                                issued
----
+
--
The following is a list of possible `Status` field values:

`issued`:: The break glass credential has been issued and is ready to use.
`expired`:: The break glass credential has expired and can no longer be used.
`failed`:: The break glass credential has failed to create. In this case, you receive a service log detailing the failure. For more information about service logs, see _Accessing the service logs for Red{nbsp}Hat OpenShift Service on AWS clusters_. For steps to contact Red{nbsp}Hat Support for assistance, see _Getting support_.
`awaiting_revocation`:: The break glass credential is currently being revoked, meaning it cannot be used.
`revoked`:: The break glass credential has been revoked and can no longer be used.
--
+
. To retrieve the `kubeconfig`, run the following commands:
** Create a `kubeconfigs` directory:
+
[source,terminal]
----
$ mkdir ~/kubeconfigs
----
+
** Export the newly generated `kubeconfig` file, replacing <cluster_name> with the name of your cluster:
+
[source,terminal]
----
$ export CLUSTER_NAME=<cluster_name> && export KUBECONFIG=~/kubeconfigs/break-glass-${CLUSTER_NAME}.kubeconfig
----
+
** View the `kubeconfig`:
+
[source,terminal]
----
$ rosa describe break-glass-credential <break_glass_credential_id> -c mycluster --kubeconfig
----
+
.Example output
[source,terminal]
----
apiVersion: v1
clusters:
- cluster:
    server: <server_url>
  name: cluster
contexts:
- context:
    cluster: cluster
    namespace: default
    user: test-username
  name: admin
current-context: admin
kind: Config
preferences: {}
users:
- name: test-user
  user:
    client-certificate-data: <client-certificate-data>
    client-key-data: <client-key-data>
----
+
--
where:

`users.user.client-certificate-data`:: The client-certificate contains a certificate for the user signed by the Kubernetes certificate authorities (CA).
`users.user.client-key-data`:: The client-key contains the key that signed the client certificate.
--
+
. Optional: To save the `kubeconfig`, run the following command :
+
[source,terminal]
----
$ rosa describe break-glass-credential <break_glass_credential_id> -c mycluster --kubeconfig > $KUBECONFIG
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth.adoc

[id="rosa-hcp-sts-accessing-a-break-glass-cred-cli_{context}"]
= Accessing a OpenShift Container Platform cluster by using a break glass credential

[role="_abstract"]
Use the new `kubeconfig` from the break glass credential to gain temporary admin access to a OpenShift Container Platform cluster.

.Prerequisites

* You have access to a OpenShift Container Platform cluster with external authentication enabled. For more information, see _Creating a OpenShift Container Platform cluster that uses direct authentication with an external OIDC identity provider_.
* You have installed the `oc` and the `kubectl` CLIs.
* You have configured the new `kubeconfig`. For more information, see _Creating a break glass credential for a OpenShift Container Platform cluster_.

.Procedure

. Access the details for the cluster:
+
[source,terminal]
----
$ rosa describe break-glass-credential <break_glass_credential_id> -c <cluster_name>  --kubeconfig > $KUBECONFIG
----
+
. List the nodes from the cluster:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                        STATUS   ROLES   AGE   VERSION
ip-10-0-0-27.ec2.internal   Ready    worker  8m    v1.28.7+f1b5f6c
ip-10-0-0-67.ec2.internal   Ready    worker  9m    v1.28.7+f1b5f6c
----
. Verify you have the correct credentials:
+
[source,terminal]
----
$ kubectl auth whoami
----
+
.Example output
[source,terminal]
----
ATTRIBUTE    VALUE
Username     system:customer-break-glass:test-user
Groups       [system:masters system:authenticated]
----
. Apply the `ClusterRoleBinding` for the groups defined in the external OIDC provider. The `ClusterRoleBinding` maps the `rosa-hcp-admins` group that is created in Microsoft Entra ID to a group in the OpenShift Container Platform cluster.
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: rosa-hcp-admins
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: f715c264-ab90-45d5-8a29-2e91a609a895
EOF
----
+
The output of this command is:
+
[source,terminal]
----
clusterrolebinding.rbac.authorization.k8s.io/rosa-hcp-admins created
----
+
[NOTE]
====
After applying the `ClusterRoleBinding`, the OpenShift Container Platform cluster is configured and the `rosa` CLI and {hybrid-console-url} authenticate through the external OIDC provider. You can now start assigning roles and deploying applications on the cluster.
====

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-ext-auth.adoc

[id="rosa-hcp-sts-revoking-a-break-glass-cred-cli_{context}"]
= Revoking a break glass credential for a OpenShift Container Platform cluster

[role="_abstract"]
You can revoke access to any break glass credentials that you have provisioned at any time by using the `revoke break-glass-credentials` command.

.Prerequisites

* You have created a break glass credential.
* You are the cluster owner.

.Procedure

* Revoke the break glass credentials for a OpenShift Container Platform cluster by running the following command.
+
[IMPORTANT]
====
Running this command revokes access for all break glass credentials related to the cluster.
====
+
[source,terminal]
----
$ rosa revoke break-glass-credentials -c <cluster_name>
----
+
.Example output
[source,terminal]
----
? Are you sure you want to revoke all the break glass credentials on cluster 'my-cluster'?: Yes
I: Successfully requested revocation for all break glass credentials from cluster 'my-cluster'
----

.Verification

* The revocation process can take several minutes. You can verify that the break glass credentials for your clusters have been revoked by running one of the following commands:
** List all break glass credentials and check the status of each:
+
[source,terminal]
----
$ rosa list break-glass-credential -c <cluster_name>
----
+
.Example output
[source,terminal]
----
ID                                USERNAME    STATUS
2330dbs0n8m3chkkr25gkkcd8pnj3lk2  test-user   awaiting_revocation
----
+
** You can also verify the status by checking the individual credential:
+
[source,terminal]
----
$ rosa describe break-glass-credential <break_glass_credential_id> -c <cluster_name>
----
+
.Example output
[source,terminal]
----
ID:                                    2330dbs0n8m3chkkr25gkkcd8pnj3lk2
Username:                              test-user
Expire at:                             Dec 28 2026 10:23:05 EDT
Status:                                issued
Revoked at:                            Dec 27 2026 15:30:33 EDT
----

// Module included in the following assemblies:
//
// * rosa_hcp/rosa-hcp-sts-creating-a-cluster-quickly.adoc
[id="rosa-hcp-sts-creating-a-cluster-external-auth-provider-delete-cli_{context}"]
= Deleting an external authentication provider

[role="_abstract"]
You can delete external authentication providers from a cluster by using the {rosa-cli-first}.

.Procedure

. Display your external authentication provider on your cluster by running the following command:
+
[source,terminal]
----
$ rosa list external-auth-provider -c <cluster_name>
----
+
.Example output
[source,terminal]
----
NAME        ISSUER URL
entra-test  https://login.microsoftonline.com/<group_id>/v2.0
----

. Delete the external authentication provider by running the following command:
+
[source,terminal]
----
$ rosa delete external-auth-provider <name_of_provider> -c <cluster_name>
----
+
.Example output
[source,terminal]
----
? Are you sure you want to delete external authentication provider entra-test on cluster rosa-ext-test? Yes
I: Successfully deleted external authentication provider 'entra-test' from cluster 'rosa-ext-test'
----

.Verification
. Query for any external authentication providers on your cluster by running the following command:
+
[source,terminal]
----
$ rosa list external-auth-provider -c <cluster_name>
----
+
.Example output
[source,terminal]
----
E: there are no external authentication providers for this cluster
----

[role="_additional-resources"]
[id="additional-resources_rosa-sts-creating-a-cluster-ext-auth"]
== Additional resources

* Creating a OpenShift Container Platform cluster that uses direct authentication with an external OIDC identity provider
* Using RBAC to define and apply permissions
* Configured virtual private cloud (VPC)
* Account-wide roles
* OIDC configuration
* Operator roles
* About custom Operator IAM role prefixes
* AWS prerequisites for ROSA with STS
* Creating OpenID Connect (OIDC) identity providers (AWS documentation)
* Troubleshooting OpenShift Container Platform cluster installations
* Getting support for OpenShift Container Platform
