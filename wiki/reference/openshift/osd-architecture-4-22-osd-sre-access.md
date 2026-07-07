---
title: "SRE and service account access"
type: reference
domain: openshift
slug: osd-architecture-4-22-osd-sre-access
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/osd_architecture/osd-sre-access
version: 4.22
family: osd_architecture
documentKind: "Documentation"
---

# SRE and service account access

[id="osd-sre-access"]
= SRE and service account access

[role="_abstract"]
Red Hat Site Reliability Engineers (SREs) require access to OpenShift Container Platform clusters to perform operational tasks, such as monitoring cluster health, responding to incidents, and performing maintenance activities. This document outlines the identity and access management (IAM) policies and procedures that govern SRE access to OpenShift Container Platform clusters.

// Module included in the following assemblies:
//
// * osd_architecture/osd_policy/osd-sre-access.adoc

[id="policy-identity-access-management_{context}"]
= Identity and access management

[role="_abstract"]
Most access by Red Hat site reliability engineering (SRE) teams is done by using cluster Operators through automated configuration management.

[NOTE]
====
OpenShift Container Platform on {GCP} clusters that are created with the Workload Identify Federation (WIF) authentication type do not use Operators for SRE access. Instead, the required roles necessary for SRE account access are assigned to the sd-sre-platform-gcp-access group as part of the WIF configuration creation and are validated prior to the deployment of the cluster by the {cluster-manager}. For more information about WIF configurations, see _Additional resources_.
====

[id="subprocessors_{context}"]
== Subprocessors
For a list of the available subprocessors, see the Red Hat Subprocessor List on the Red Hat Customer Portal.

[id="sre-access-all_{context}"]
== SRE access to all OpenShift Container Platform clusters
SREs access OpenShift Container Platform clusters through a proxy. The proxy mints a service account in an OpenShift Container Platform cluster for the SREs when they log in. As no identity provider is configured for OpenShift Container Platform clusters, SREs access the proxy by running a local web console container. SREs do not access the cluster web console directly. SREs must authenticate as individual users to ensure auditability. All authentication attempts are logged to a Security Information and Event Management (SIEM) system.

[id="privileged-access_{context}"]
== Privileged access controls in OpenShift Container Platform
Red Hat SRE adheres to the principle of least privilege when accessing OpenShift Container Platform and public cloud provider components. There are four basic categories of manual SRE access:

* SRE admin access through the Red Hat Customer Portal with normal two-factor authentication and no privileged elevation.

* SRE admin access through the Red Hat corporate SSO with normal two-factor authentication and no privileged elevation.

* OpenShift elevation, which is a manual elevation using Red Hat SSO. It is fully audited and management approval is required for every operation SREs make.

* Cloud provider access or elevation, which is a manual elevation for cloud provider console or CLI access. Access is limited to 60 minutes and is fully audited.

Each of these access types has different levels of access to components:

[cols= "3a,3a,3a,3a,3a",options="header"]

|===

| Component | Typical SRE admin access (Red Hat Customer Portal) | Typical SRE admin access (Red Hat SSO) |OpenShift elevation | Cloud provider access

| {cluster-manager} | R/W | No access | No access | No access
| OpenShift web console | No access | R/W | R/W | No access
| Node operating  system | No access | A specific list of elevated OS and network permissions. | A specific list of elevated OS and network permissions. | No access
| AWS Console | No access | No access, but this is the account used to request cloud provider access. | No access | All cloud provider permissions using the SRE identity.

|===

[id="sre-access-cloud-infra_{context}"]
== SRE access to cloud infrastructure accounts
Red Hat personnel do not access cloud infrastructure accounts in the course of routine OpenShift Container Platform operations. For emergency troubleshooting purposes, Red Hat SRE have well-defined and auditable procedures to access cloud infrastructure accounts.

In AWS, SREs generate a short-lived AWS access token for the `BYOCAdminAccess` user using the AWS Security Token Service (STS). Access to the STS token is audit logged and traceable back to individual users. The `BYOCAdminAccess` has the `AdministratorAccess` IAM policy attached.

In {gcp-full}, SREs access resources after being authenticated against a Red Hat SAML identity provider (IDP). The IDP authorizes tokens that have time-to-live expirations. The issuance of the token is auditable by corporate Red Hat IT and linked back to an individual user.

[id="support-access_{context}"]
== Red Hat support access
Members of the Red Hat CEE team typically have read-only access to parts of the cluster. Specifically, CEE has limited access to the core and product namespaces and does not have access to the customer namespaces.

[cols= "3,2a,2a,2a,2a",options="header"]

|===

| Role | Core namespace | Layered product namespace | Customer namespace | Cloud infrastructure account^*^

|OpenShift SRE| Read: All

Write: Very

Limited ^[1]^
| Read: All

Write: None
| Read: None^[2]^

Write: None
|Read: All ^[3]^

Write: All ^[3]^

|CEE
|Read: All

Write: None

|Read: All

Write: None

|Read: None^[2]^

Write: None

|Read: None

Write: None

|Customer administrator
|Read: None

Write: None

|Read: None

Write: None

| Read: All

Write: All

|Read: Limited^[4]^

Write: Limited^[4]^

|Customer user
|Read: None

Write: None

|Read: None

Write: None

|Read: Limited^[5]^

Write: Limited^[5]^

|Read: None

Write: None

|Everybody else
|Read: None

Write: None
|Read: None

Write: None
|Read: None

Write: None
|Read: None

Write: None

|===
[.small]
--
Cloud Infrastructure Account refers to the underlying AWS or {gcp-full} account

1. Limited to addressing common use cases such as failing deployments, upgrading a cluster, and replacing bad worker nodes.
2. Red Hat associates have no access to customer data by default.
3. SRE access to the cloud infrastructure account is a "break-glass" procedure for exceptional troubleshooting during a documented incident.
4. Customer administrator has limited access to the cloud infrastructure account console through Cloud Infrastructure Access.
5. Limited to what is granted through RBAC by the customer administrator, as well as namespaces created by the user.
--

// TODO: The above uses an asterisk as a footnote I think for the first sentence (though it does not show it as a reference below the table), then numbers for the rest of the footnote items. I would suggest bumping all the numbers and using a number for the first header asterisk as well.

[id="customer-access_{context}"]
== Customer access
Customer access is limited to namespaces created by the customer and permissions that are granted using RBAC by the customer administrator role. Access to the underlying infrastructure or product namespaces is generally not permitted without `cluster-admin` access. More information on customer access and authentication can be found in the Understanding Authentication section of the documentation.

// TODO: I do not think there is this "Understanding Authentication" section in the OSD docs

[id="access-approval_{context}"]
== Access approval and review
New SRE user access requires management approval. Separated or transferred SRE accounts are removed as authorized users through an automated process. Additionally, SRE performs periodic access review including management sign-off of authorized user lists.
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-sre-access.adoc
// * osd_architecture/osd_policy/osd-sre-access.adoc
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc

[id="sre-cluster-access_{context}"]
= SRE cluster access

[role="_abstract"]
Red{nbsp}Hat SRE access to OpenShift Container Platform
(ROSA)
clusters is controlled through several layers of required authentication, all of which are managed by strict company policy. All authentication attempts to access a cluster and changes made within a cluster are recorded within audit logs, along with the specific account identity of the SRE responsible for those actions. These audit logs help ensure that all changes made by SREs to a customer's cluster adhere to the strict policies and procedures that make up Red{nbsp}Hat's managed services guidelines.

The information presented below is an overview of the process an SRE must perform to access a customer's cluster.

** Red{nbsp}Hat SRE requests a refreshed ID token from the Red{nbsp}Hat SSO (Cloud Services). This request is authenticated. The token is valid for fifteen minutes. After the token expires, you can refresh the token again and receive a new token. The ability to refresh to a new token is indefinite; however, the ability to refresh to a new token is revoked after 30 days of inactivity.

** Red{nbsp}Hat SRE connects to the Red{nbsp}Hat VPN. The authentication to the VPN is completed by the Red{nbsp}Hat Corporate Identity and Access Management system (RH IAM). With RH IAM, SREs are multifactor and can be managed internally per organization by groups and existing onboarding and offboarding processes. After an SRE is authenticated and connected, the SRE can access the cloud services fleet management plane. Changes to the cloud services fleet management plane require many layers of approval and are maintained by strict company policy.

** After authorization is complete, the SRE logs into the fleet management plane and receives a service account token that the fleet management plane created. The token is valid for 15 minutes. After the token is no longer valid, it is deleted.

** With access granted to the fleet management plane, SRE uses various methods to access clusters, depending on network configuration.

*** Accessing a private or public cluster: Request is sent through a specific Network Load Balancer (NLB) by using an encrypted HTTP connection on port 6443.

*** Accessing a PrivateLink cluster: Request is sent to the Red{nbsp}Hat Transit Gateway, which then connects to a Red{nbsp}Hat VPC per region. The VPC that receives the request will be dependent on the target private cluster's region. Within the VPC, there is a private subnet that contains the PrivateLink endpoint to the customer's PrivateLink cluster.

*** Accessing a Private Service Connect (PSC) cluster: Request is sent to Red{nbsp}Hat's internal backend infrastructure, which routes the traffic through a secured, trusted network to Red{nbsp}Hat's Management project in {gcp-short}. The Red{nbsp}Hat Management project includes VPC, which is configured with subnets in multiple regions, each containing a PSC endpoint that provides private access to the customer's cluster in the respective region. The traffic is routed through the appropriate regional subnet, ensuring secure and private access to the cluster without traversing the public internet.

SREs access ROSA clusters through the web console or command-line interface (CLI) tools. Authentication requires multi-factor authentication (MFA) with industry-standard requirements for password complexity and account lockouts. SREs must authenticate as individuals to ensure auditability. All authentication attempts are logged to a Security Information and Event Management (SIEM) system.

SREs access private clusters using an encrypted HTTP connection. Connections are permitted only from a secured Red{nbsp}Hat network using either an IP allowlist or a private cloud provider link.

.SRE access to ROSA clusters
image::267_OpenShift_on_AWS_Access_Networking_1222.png[]

[id="rosa-policy-privileged-access-control_{context}"]
== Privileged access controls in ROSA
SRE adheres to the principle of least privilege when accessing ROSA and AWS components. There are four basic categories of manual SRE access:

- SRE admin access through the Red{nbsp}Hat Portal with normal two-factor authentication and no privileged elevation.
- SRE admin access through the Red{nbsp}Hat corporate SSO with normal two-factor authentication and no privileged elevation.
- OpenShift elevation, which is a manual elevation using Red{nbsp}Hat SSO. Access is limited to 2 hours, is fully audited, and requires management approval.
- AWS access or elevation, which is a manual elevation for AWS console or CLI access. Access is limited to 60 minutes and is fully audited.

Each of these access types have different levels of access to components:

[cols= "4a,6a,5a,4a,3a",options="header"]

|===

| Component | Typical SRE admin access (Red{nbsp}Hat Portal) | Typical SRE admin access (Red{nbsp}Hat SSO) |OpenShift elevation | Cloud provider access or elevation

| {cluster-manager} | R/W | No access | No access | No access
| OpenShift console | No access | R/W | R/W | No access
| Node operating system | No access | A specific list of elevated OS and network permissions. | A specific list of elevated OS and network permissions. | No access
| AWS Console | No access | No access, but this is the account used to request cloud provider access. | No access | All cloud provider permissions using the SRE identity.

|===

[id="rosa-policy-sre-aws-infra-access_{context}"]
== SRE access to AWS accounts
Red{nbsp}Hat personnel do not access AWS accounts in the course of routine OpenShift Container Platform operations. For emergency troubleshooting purposes, the SREs have well-defined and auditable procedures to access cloud infrastructure accounts.

In the isolated backplane flow, SREs request access to a customer's support role. This request is just-in-time (JIT) processed by the backplane API which dynamically updates the organization role's permissions to a specific SRE personnel's account. This SRE's account is given access to a specific Red{nbsp}Hat customer's environment. SRE access to a Red{nbsp}Hat customer's environment is a temporary, short-lived access that is only established at the time of the access request.

Access to the STS token is audit-logged and traceable back to individual users. Both STS and non-STS clusters use the AWS STS service for SRE access. Access control uses the unified backplane flow when the `ManagedOpenShift-Technical-Support-Role` has the `ManagedOpenShift-Support-Access` policy attached, and this role is used for administration. Access control uses the isolated backplane flow when the `ManagedOpenShift-Support-Role` has the `ManagedOpenShift-Technical-Support-<org_id>` policy attached. See the KCS article Updating Trust Policies for ROSA clusters for more information.

[id="rosa-sre-sts-view-aws-account_{context}"]
== SRE STS view of AWS accounts

When SREs are on a VPN through two-factor authentication, they and Red{nbsp}Hat Support can assume the `ManagedOpenShift-Support-Role` in your AWS account. The `ManagedOpenShift-Support-Role` has all the permissions necessary for SREs to directly troubleshoot and manage AWS resources. Upon assumption of the `ManagedOpenShift-Support-Role`, SREs use a AWS Security Token Service (STS) to generate a unique, time-expiring URL to the customer's AWS web UI for their account. SREs can then perform multiple troubleshooting actions, which include:

* Viewing CloudTrail logs
* Shutting down a faulty EC2 Instance

All activities performed by SREs arrive from Red{nbsp}Hat IP addresses and are logged to CloudTrail to allow you to audit and review all activity. This role is only used in cases where access to AWS services is required to assist you. The majority of permissions are read-only. However, a select few permissions have more access, including the ability to reboot an instance or spin up a new instance. SRE access is limited to the policy permissions attached to the `ManagedOpenShift-Support-Role`.

For a full list of permissions, see `sts_support_permission_policy.json` in the About IAM resources user guide.

[id="rosa-sre-access-privatelink-vpc_{context}"]
== SRE access through PrivateLink VPC endpoint service

PrivateLink VPC endpoint service is created as part of the ROSA cluster creation.

When you have a PrivateLink ROSA cluster, its Kubernetes API Server is exposed through a load balancer that can only be accessed from within the VPC by default. Red{nbsp}Hat site reliability engineering (SRE) can connect to this load balancer through a VPC Endpoint Service that has an associated VPC Endpoint in a Red{nbsp}Hat-owned AWS account. This endpoint service contains the name of the cluster, which is also in the ARN.

Under the *Allow principals* tab, a Red{nbsp}Hat-owned AWS account is listed. This specific user ensures that other entities cannot create VPC Endpoint connections to the PrivateLink cluster's Kubernetes API Server.

When Red{nbsp}Hat SREs access the API, this fleet management plane can connect to the internal API through the VPC endpoint service.
// Module included in the following assemblies:
//
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-sre-access.adoc

[id="how-service-accounts-assume-aws-iam-roles-in-sre-owned-projects_{context}"]
= How service accounts assume AWS IAM roles in SRE owned projects

[role="_abstract"]
When you install a OpenShift Container Platform
cluster,
that uses the AWS Security Token Service (STS),
cluster-specific Operator AWS Identity and Access Management (IAM) roles are created. These IAM roles permit the ROSA cluster Operators to run core OpenShift functionality.

Cluster Operators use service accounts to assume IAM roles. When a service account assumes an IAM role, temporary AWS STS credentials are provided for the service account to use in the cluster Operator's pod. If the assumed role has the necessary AWS privileges, the service account can run AWS SDK operations in the pod.

[id="workflow-for-assuming-aws-iam-roles-in-sre-owned-projects_{context}"]
== Workflow for assuming AWS IAM roles in Red{nbsp}Hat SRE owned projects

The following diagram illustrates the workflow for assuming AWS IAM roles in SRE owned projects:

.Workflow for assuming AWS IAM roles in SRE owned projects
image::workflow-assuming-aws-iam-roles-sre-owned-projects.png[Workflow for assuming AWS IAM roles in Red{nbsp}Hat SRE owned projects]

The workflow has the following stages:

. Within each project that a cluster Operator runs, the Operator's deployment spec has a volume mount for the projected service account token, and a secret containing AWS credential configuration for the pod. The token is audience-bound and time-bound. Every hour, ROSA generates a new token, and the AWS SDK reads the mounted secret containing the AWS credential configuration. This configuration has a path to the mounted token and the AWS IAM Role ARN. The secret's credential configuration includes the following:

** An `$AWS_ARN_ROLE` variable that has the ARN for the IAM role that has the permissions required to run AWS SDK operations.

** An `$AWS_WEB_IDENTITY_TOKEN_FILE` variable that has the full path in the pod to the OpenID Connect (OIDC) token for the service account. The full path is `/var/run/secrets/openshift/serviceaccount/token`.

. When a cluster Operator needs to assume an AWS IAM role to access an AWS service (such as EC2), the AWS SDK client code running on the Operator invokes the `AssumeRoleWithWebIdentity` API call.

. The OIDC token is passed from the pod to the OIDC provider. The provider authenticates the service account identity if the following requirements are met:

** The identity signature is valid and signed by the private key.

** The `sts.amazonaws.com` audience is listed in the OIDC token and matches the audience configured in the OIDC provider.
+
[NOTE]
====
In ROSA with STS clusters, the OIDC provider is created during install and set as the service account issuer by default. The `sts.amazonaws.com` audience is set by default in the OIDC provider.
====

** The OIDC token has not expired.

** The issuer value in the token has the URL for the OIDC provider.

. If the project and service account are in the scope of the trust policy for the IAM role that is being assumed, then authorization succeeds.

. After successful authentication and authorization, temporary AWS STS credentials in the form of an AWS access token, secret key, and session token are passed to the pod for use by the service account. By using the credentials, the service account is temporarily granted the AWS permissions enabled in the IAM role.

. When the cluster Operator runs, the Operator that is using the AWS SDK in the pod consumes the secret that has the path to the projected service account and AWS IAM Role ARN to authenticate against the OIDC provider. The OIDC provider returns temporary STS credentials for authentication against the AWS API.

[id="additional-resources_{context}"]
== Additional resources

* Creating a WIF configuration
