---
title: "Deploying {hcp} on {aws-short}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-deploy-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-deploy-aws
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Deploying {hcp} on {aws-short}

[id="hcp-deploy-aws"]
= Deploying {hcp} on {aws-short}

[role="_abstract"]
To reduce infrastructure costs and improve cluster management efficiency, you can deploy {hcp} on {aws-short}. This configuration decouples the control plane from the data plane so that you can manage multiple clusters from a central management service.

A _hosted cluster_ is an OpenShift Container Platform cluster with its API endpoint and control plane that are hosted on the management cluster. The hosted cluster includes the control plane and its corresponding data plane. To configure {hcp} on premises, you must install {mce} in a management cluster. By deploying the HyperShift Operator on an existing managed cluster by using the `hypershift-addon` managed cluster add-on, you can enable that cluster as a management cluster and start to create the hosted cluster. The `hypershift-addon` managed cluster add-on is enabled by default for the `local-cluster` managed cluster.

You can use the {mce-short} console or the hosted control plane command-line interface (CLI), `hcp`, to create a hosted cluster. The hosted cluster is automatically imported as a managed cluster. However, you can disable this automatic import feature into {mce-short}.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-prepare_{context}"]
= Preparing to deploy {hcp} on {aws-short}

[role="_abstract"]
Preparing to deploy {hcp} on {aws-first} involves meeting several prerequisites and creating resources, including an S3 bucket, an OIDC secret, a routable public zone, IAM role and STS credentials.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-prereqs_{context}"]
= Prerequisites to deploy {hcp} on {aws-short}

[role="_abstract"]
To ensure successful deployment of {hcp} on {aws-first}, your environment must meet the following requirements.

* You installed the {mce} 2.5 and later on an OpenShift Container Platform cluster. The {mce-short} is automatically installed when you install {rh-rhacm-first}. The {mce-short} can also be installed without {rh-rhacm} as an Operator from the OpenShift Container Platform software catalog.

* You have at least one managed OpenShift Container Platform cluster for the {mce-short}. The `local-cluster` is automatically imported in the {mce-short} version 2.5 and later. You can check the status of your hub cluster by running the following command:
+
[source,terminal]
----
$ oc get managedclusters local-cluster
----

* You installed the `aws` command-line interface (CLI).

* You installed the hosted control plane CLI, `hcp`.

[IMPORTANT]
====
* Run the management cluster and compute nodes on the same platform.

* For each hosted cluster, provide a cluster-wide unique name. A hosted cluster name cannot be the same as any existing managed cluster in order for {mce-short} to manage it.

* Do not use `clusters` as a hosted cluster name.

* Do not create a hosted cluster in the namespace of a {mce-short} managed cluster.
====

[role="_additional-resources"]
.Additional resources

* Configuring Ansible Automation Platform jobs to run on hosted clusters

* Advanced configuration

* Enabling the central infrastructure management service

* Manually enabling the {hcp} feature

* Disabling the {hcp} feature

* Deploying the SR-IOV Operator for {hcp}

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-create-secret-s3_{context}"]
= Creating the {aws-full} S3 bucket and S3 OIDC secret

[role="_abstract"]
Before you can create and manage a hosted cluster on {aws-first}, you must create the S3 bucket and S3 OIDC secret. These resources provide a place for the cluster to store information about itself and a way for the cluster to prove its identity to {aws-short}.

.Procedure

. Create an S3 bucket that has public access to host OIDC discovery documents for your clusters.

.. Enter the following command:
+
[source,terminal]
----
$ aws s3api create-bucket --bucket <bucket_name> \
  --create-bucket-configuration LocationConstraint=<region> \
  --region <region> <2>
----
+
where:
+
--
`<bucket_name>`:: Specifies the name of the S3 bucket you are creating.
`<region>`:: Specifies that you want to create the bucket in a region other than the `us-east-1` region. Include this line and replace `<region>` with the region you want to use. To create a bucket in the `us-east-1` region, omit this line.
--

.. Enter the following command:
+
[source,terminal]
----
$ aws s3api delete-public-access-block --bucket <bucket_name>
----
+
Replace `<bucket_name>` with the name of the S3 bucket you are creating.

.. Enter the following command:
+
[source,terminal]
----
$ echo '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<bucket_name>/*"
        }
    ]
}' | envsubst > policy.json
----
+
Replace `<bucket_name>` with the name of the S3 bucket you are creating.

.. Enter the following command:
+
[source,terminal]
----
$ aws s3api put-bucket-policy --bucket <bucket_name> \
  --policy file://policy.json
----
+
Replace `<bucket_name>` with the name of the S3 bucket you are creating.
+
[NOTE]
====
If you are using a Mac computer, you must export the bucket name in order for the policy to work.
====

. Create an OIDC S3 secret named `hypershift-operator-oidc-provider-s3-credentials` for the HyperShift Operator.

. Save the secret in the `local-cluster` namespace.

. See the following table to verify that the secret contains the following fields:
+
.Required fields for the {aws-short} secret
[cols="2,2",options="header"]
|===
| Field name | Description

| `bucket`
| Contains an S3 bucket with public access to host OIDC discovery documents for your hosted clusters.

| `credentials`
| A reference to a file that contains the credentials of the `default` profile that can access the bucket. By default, HyperShift only uses the `default` profile to operate the `bucket`.

| `region`
| Specifies the region of the S3 bucket.
|===

. To create an {aws-short} secret, run the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
  --from-file=credentials=<path>/.aws/credentials \
  --from-literal=bucket=<s3_bucket> \
  --from-literal=region=<region> \
  -n local-cluster
----
+
[NOTE]
====
Disaster recovery backup for the secret is not automatically enabled. To add the label that enables the `hypershift-operator-oidc-provider-s3-credentials` secret to be backed up for disaster recovery, run the following command:
[source,terminal]
----
$ oc label secret hypershift-operator-oidc-provider-s3-credentials \
  -n local-cluster cluster.open-cluster-management.io/backup=true
----
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-create-public-zone_{context}"]
= Creating a routable public zone for hosted clusters

[role="_abstract"]
In order to access applications in your hosted clusters, you must configure the routable public zone.

If the public zone exists, skip this step. Otherwise, the public zone affects the existing functions.

.Procedure

* To create a routable public zone for DNS records, enter the following command:
+
[source,terminal]
----
$ aws route53 create-hosted-zone \
  --name <basedomain> \
  --caller-reference $(whoami)-$(date --rfc-3339=date)
----
+
Replace `<basedomain>` with your base domain, for example, `www.example.com`.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-create-role-sts-creds_{context}"]
= Creating an {aws-short} IAM role and STS credentials

[role="_abstract"]
Before you create a hosted cluster on {aws-first}, you must create an {aws-short} IAM role and STS credentials.

.Procedure

. Get the Amazon Resource Name (ARN) of your user by running the following command:
+
[source,terminal]
----
$ aws sts get-caller-identity --query "Arn" --output text
----
+
.Example output
[source,terminal]
----
arn:aws:iam::1234567890:user/<aws_username>
----
+
Use this output as the value for the `<arn>` value in the next step.

. Create a JSON file that contains the trust relationship configuration for your role. See the following example:
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "<arn>"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
----
+
Replace `<arn>` with the ARN of your user that you noted in the previous step.

. Create the Identity and Access Management (IAM) role by running the following command:
+
[source,terminal]
----
$ aws iam create-role \
  --role-name <name> \
  --assume-role-policy-document file://<file_name>.json \
  --query "Role.Arn"
----
+
where:
+
--
`<name>`:: Specifies the role name, for example, `hcp-cli-role`.
`<file_name>`:: Specifies the name of the JSON file you created in the previous step.
--
+
.Example output
[source,terminal]
----
arn:aws:iam::820196288204:role/myrole
----

. Create a JSON file named `policy.json` that contains the following permission policies for your role:
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EC2",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateDhcpOptions",
                "ec2:DeleteSubnet",
                "ec2:ReplaceRouteTableAssociation",
                "ec2:DescribeAddresses",
                "ec2:DescribeInstances",
                "ec2:DeleteVpcEndpoints",
                "ec2:CreateNatGateway",
                "ec2:CreateVpc",
                "ec2:DescribeDhcpOptions",
                "ec2:AttachInternetGateway",
                "ec2:DeleteVpcEndpointServiceConfigurations",
                "ec2:DeleteRouteTable",
                "ec2:AssociateRouteTable",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeAvailabilityZones",
                "ec2:CreateRoute",
                "ec2:CreateInternetGateway",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:ModifyVpcAttribute",
                "ec2:DeleteInternetGateway",
                "ec2:DescribeVpcEndpointConnections",
                "ec2:RejectVpcEndpointConnections",
                "ec2:DescribeRouteTables",
                "ec2:ReleaseAddress",
                "ec2:AssociateDhcpOptions",
                "ec2:TerminateInstances",
                "ec2:CreateTags",
                "ec2:DeleteRoute",
                "ec2:CreateRouteTable",
                "ec2:DetachInternetGateway",
                "ec2:DescribeVpcEndpointServiceConfigurations",
                "ec2:DescribeNatGateways",
                "ec2:DisassociateRouteTable",
                "ec2:AllocateAddress",
                "ec2:DescribeSecurityGroups",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:CreateVpcEndpoint",
                "ec2:DescribeVpcs",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteDhcpOptions",
                "ec2:DeleteNatGateway",
                "ec2:DescribeVpcEndpoints",
                "ec2:DeleteVpc",
                "ec2:CreateSubnet",
                "ec2:DescribeSubnets"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ELB",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DeleteLoadBalancer",
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DeleteTargetGroup"
            ],
            "Resource": "*"
        },
        {
            "Sid": "IAMPassRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:*:iam::*:role/*-worker-role",
            "Condition": {
                "ForAnyValue:StringEqualsIfExists": {
                    "iam:PassedToService": "ec2.amazonaws.com"
                }
            }
        },
        {
            "Sid": "IAM",
            "Effect": "Allow",
            "Action": [
                "iam:CreateInstanceProfile",
                "iam:DeleteInstanceProfile",
                "iam:GetRole",
                "iam:UpdateAssumeRolePolicy",
                "iam:GetInstanceProfile",
                "iam:TagRole",
                "iam:RemoveRoleFromInstanceProfile",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:PutRolePolicy",
                "iam:AddRoleToInstanceProfile",
                "iam:CreateOpenIDConnectProvider",
                "iam:ListOpenIDConnectProviders",
                "iam:DeleteRolePolicy",
                "iam:UpdateRole",
                "iam:DeleteOpenIDConnectProvider",
                "iam:GetRolePolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "Route53",
            "Effect": "Allow",
            "Action": [
                "route53:ListHostedZonesByVPC",
                "route53:CreateHostedZone",
                "route53:ListHostedZones",
                "route53:ChangeResourceRecordSets",
                "route53:ListResourceRecordSets",
                "route53:DeleteHostedZone",
                "route53:AssociateVPCWithHostedZone",
                "route53:ListHostedZonesByName"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:DeleteBucket"
            ],
            "Resource": "*"
        }
    ]
}
----

. Attach the `policy.json` file that contains the permissions policies for your role by running the following command:
+
[source,terminal]
----
$ aws iam put-role-policy \
  --role-name <role_name> \
  --policy-name <policy_name> \
  --policy-document file://policy.json
----
+
where:
+
--
`<role_name>`:: Specifies the name of your role.
`<policy_name>`:: Specifies your policy name.
--

. Retrieve STS credentials in a JSON file named `sts-creds.json` by running the following command:
+
[source,terminal]
----
$ aws sts get-session-token --output json > sts-creds.json
----
+
.Example `sts-creds.json` file
[source,json]
----
{
    "Credentials": {
        "AccessKeyId": "<access_key_id",
        "SecretAccessKey": "<secret_access_key>”,
        "SessionToken": "<session_token>",
        "Expiration": "<time_stamp>"
    }
}
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-enable-private-link_{context}"]
= Enabling {aws-short} PrivateLink for {hcp}

[role="_abstract"]
In order to provision {hcp} on the {aws-first} with PrivateLink, you need to enable {aws-short} PrivateLink for {hcp}.

.Procedure

. Create an {aws-short} credential secret for the HyperShift Operator and name it `hypershift-operator-private-link-credentials`. The secret must reside in the managed cluster namespace that is the namespace of the managed cluster being used as the management cluster. If you used `local-cluster`, create the secret in the `local-cluster` namespace.

. See the following table to confirm that the secret contains the required fields:
+
.Required fields for the {aws-short} secret
[options="header"]
|===
| Field name | Description | Optional or required
| `region`
| Region for use with Private Link
| Required

| `aws-access-key-id`
| The credential access key id.
| Required

| `aws-secret-access-key`
| The credential access key secret.
| Required
|===

. To create an {aws-short} secret, run the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
  --from-literal=aws-access-key-id=<aws_access_key_id> \
  --from-literal=aws-secret-access-key=<aws_secret_access_key> \
  --from-literal=region=<region> -n local-cluster
----

. Disaster recovery backup for the secret is not automatically enabled. Run the following command to add the label that enables the `hypershift-operator-private-link-credentials` secret to be backed up for disaster recovery:
+
[source,terminal]
----
$ oc label secret hypershift-operator-private-link-credentials \
  -n local-cluster \
  cluster.open-cluster-management.io/backup=""
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-enable-ext-dns_{context}"]
= Enabling external DNS for {hcp} on {aws-short}

[role="_abstract"]
To automate the management of DNS records, you can enable external DNS. By configuring this feature, you provide a way for the cluster to update your {aws-short} Route 53 public hosted zones automatically when you create or delete services and ingresses.

The control plane and the data plane are separate in {hcp}. You can configure DNS in two independent areas:

* Ingress for workloads within the hosted cluster, such as the following domain: `*.apps.service-consumer-domain.com`.

* Ingress for service endpoints within the management cluster, such as API or OAuth endpoints through the service provider domain: `*.service-provider-domain.com`.

The input for `hostedCluster.spec.dns` manages the ingress for workloads within the hosted cluster. The input for `hostedCluster.spec.services.servicePublishingStrategy.route.hostname` manages the ingress for service endpoints within the management cluster.

External DNS creates name records for hosted cluster services that specify a publishing type of `LoadBalancer` or `Route` and provide a hostname for that publishing type. For hosted clusters with `Private` or `PublicAndPrivate` endpoint access types, only the `APIServer` and `OAuth` services support hostnames. For `Private` hosted clusters, the DNS record resolves to a private IP address of a Virtual Private Cloud (VPC) endpoint in your VPC.

A hosted control plane exposes the following services:

* `APIServer`
* `OIDC`

[NOTE]
====
The `NodePort` publishing type is not supported on {hcp} on {aws-short}.
====

You can expose these services by using the `servicePublishingStrategy` field in the `HostedCluster` specification. By default, for the `LoadBalancer` and `Route` types of `servicePublishingStrategy`, you can publish the service in one of the following ways:

* By using the hostname of the load balancer that is in the status of the `Service` with the `LoadBalancer` type.
* By using the `status.host` field of the `Route` resource.

However, when you deploy {hcp} in a managed service context, those methods can expose the ingress subdomain of the underlying management cluster and limit options for the management cluster lifecycle and disaster recovery.

When a DNS indirection is layered on the `LoadBalancer` and `Route` publishing types, a managed service operator can publish all public hosted cluster services by using a service-level domain. This architecture allows remapping on the DNS name to a new `LoadBalancer` or `Route` and does not expose the ingress domain of the management cluster. {hcp-capital} uses external DNS to achieve that indirection layer.

You can deploy `external-dns` alongside the HyperShift Operator in the `hypershift` namespace of the management cluster. External DNS watches for `Services` or `Routes` that have the `external-dns.alpha.kubernetes.io/hostname` annotation. That annotation is used to create a DNS record that points to the `Service`, such as an A record, or the `Route`, such as a CNAME record.

You can use external DNS on cloud environments only. For the other environments, you need to manually configure DNS and services.

For more information about external DNS, see external DNS.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-set-up-ext-dns_{context}"]
= Setting up external DNS for {hcp}

[role="_abstract"]
To automate the management of DNS records, you can set up external DNS for {hcp} on {aws-short}. You need this configuration to ensure that when you create or modify services, the corresponding DNS records in your {aws-short} Route 53 public hosted zones update automatically.

You can provision {hcp} with external DNS or service-level DNS.

.Prerequisites

* You created an external public domain.

* You have access to the {aws-short} Route53 Management console.

* You enabled {aws-short} PrivateLink for {hcp}.

.Procedure

. Create an {aws-first} credential secret for the HyperShift Operator and name it `hypershift-operator-external-dns-credentials` in the `local-cluster` namespace.

. Verify that the secret has the required fields. For your reference, the required fields are detailed in the following table.
+
.Required fields for the {aws-short} secret
[options="header"]
|===
| Field name | Description | Optional or required

| `provider`
| The DNS provider that manages the service-level DNS zone.
| Required

| `domain-filter`
| The service-level domain.
| Required

| `credentials`
| The credential file that supports all external DNS types.
| Optional when you use {aws-short} keys

| `aws-access-key-id`
| The credential access key id.
| Optional when you use the {aws-short} DNS service

| `aws-secret-access-key`
| The credential access key secret.
| Optional when you use the {aws-short} DNS service
|===

. Create an {aws-short} secret by running the following command:
+
[source,terminal]
----
$ oc create secret generic <secret_name> \
  --from-literal=provider=aws \
  --from-literal=domain-filter=<domain_name> \
  --from-file=credentials=<path_to_aws_credentials_file> -n local-cluster
----
+
[NOTE]
====
Disaster recovery backup for the secret is not automatically enabled. To back up the secret for disaster recovery, add the `hypershift-operator-external-dns-credentials` by entering the following command:
[source,terminal]
----
$ oc label secret hypershift-operator-external-dns-credentials \
  -n local-cluster \
  cluster.open-cluster-management.io/backup=""
----
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-create-dns-hosted-zone_{context}"]
= Creating the public DNS hosted zone

[role="_abstract"]
You can create the public DNS hosted zone to use as the external DNS domain filter. The External DNS Operator uses the public DNS hosted zone to create your public hosted cluster.

.Procedure

. In the {aws-short} Route 53 management console, click *Create hosted zone*.

. On the *Hosted zone configuration* page, type a domain name, verify that *Public hosted zone* is selected as the type, and click *Create hosted zone*.

. After the zone is created, on the *Records* tab, note the values in the *Value/Route traffic to* column.

. In the main domain, create an NS record to redirect the DNS requests to the delegated zone. In the *Value* field, enter the values that you noted in the previous step.

. Click *Create records*.

. Verify that the DNS hosted zone is working by creating a test entry in the new subzone and testing it with a `dig` command, such as in the following example:
+
[source,terminal]
----
$ dig +short test.user-dest-public.aws.kerberos.com
----
+
.Example output
[source,terminal]
----
192.168.1.1
----

. To create a hosted cluster that sets the hostname for the `LoadBalancer` and `Route` services, enter the following command:
+
[source,terminal]
----
$ hcp create cluster aws --name=<hosted_cluster_name> \
  --endpoint-access=PublicAndPrivate \
  --external-dns-domain=<public_hosted_zone> ...
----
+
Replace `<public_hosted_zone>` with the public hosted zone that you created.
+
.Example `services` block for the hosted cluster
[source,yaml]
----
  platform:
    aws:
      endpointAccess: PublicAndPrivate
...
  services:
  - service: APIServer
    servicePublishingStrategy:
      route:
        hostname: api-example.service-provider-domain.com
      type: Route
  - service: OAuthServer
    servicePublishingStrategy:
      route:
        hostname: oauth-example.service-provider-domain.com
      type: Route
  - service: Konnectivity
    servicePublishingStrategy:
      type: Route
  - service: Ignition
    servicePublishingStrategy:
      type: Route
----
+
The Control Plane Operator creates the `Services` and `Routes` resources and annotates them with the `external-dns.alpha.kubernetes.io/hostname` annotation. For `Services` and `Routes`, the Control Plane Operator uses a value of the `hostname` parameter in the `servicePublishingStrategy` field for the service endpoints. To create the DNS records, you can use a mechanism, such as the `external-dns` deployment.
+
You can configure service-level DNS indirection for public services only. You cannot set `hostname` for private services because they use the `hypershift.local` private zone.
+
The following table shows when it is valid to set `hostname` for a service and endpoint combinations:
+
.Service and endpoint combinations to set `hostname`
[cols="4,1,1,1",options="header"]
|===
|Service |Public |PublicAndPrivate |Private

|`APIServer`
|Y
|Y
|N

|`OAuthServer`
|Y
|Y
|N

|`Konnectivity`
|Y
|N
|N

|`Ignition`
|Y
|N
|N
|===

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-hc-ext-dns_{context}"]
= Creating a hosted cluster by using the external DNS on {aws-short}

[role="_abstract"]
When you create a hosted cluster on {aws-short}, using external DNS provides advantages over standard installation methods. With external DNS, you can automatically synchronize your cluster's service endpoints with {aws-short} Route 53.

Without external DNS, you must manually manage DNS records for every new service or ingress, which increases the risk of configuration errors and downtime.

.Prerequisites

* You configured the following artifacts in your management cluster:

** The public DNS hosted zone
** The External DNS Operator
** The HyperShift Operator

.Procedure

. On the `hcp` command-line interface (CLI), enter the following command to access your management cluster:
+
[source,terminal]
----
$ export KUBECONFIG=<path_to_management_cluster_kubeconfig>
----

. Verify that the External DNS Operator is running by entering the following command:
+
[source,terminal]
----
$ oc get pod -n hypershift -lapp=external-dns
----
+
.Example output
[source,terminal]
----
NAME                            READY   STATUS    RESTARTS   AGE
external-dns-7c89788c69-rn8gp   1/1     Running   0          40s
----

. To create a hosted cluster by using external DNS, enter the following command:
+
[source,terminal]
----
$ hcp create cluster aws \
    --role-arn <arn_role> \
    --instance-type <instance_type> \
    --region <region> \
    --auto-repair \
    --generate-ssh \
    --name <hosted_cluster_name> \
    --namespace clusters \
    --base-domain <service_consumer_domain> \
    --node-pool-replicas <node_replica_count> \
    --pull-secret <path_to_your_pull_secret> \
    --release-image quay.io/openshift-release-dev/ocp-release:<ocp_release_image> \
    --external-dns-domain=<service_provider_domain> \
    --endpoint-access=<endpoint_access_configuration> \
    --sts-creds <path_to_sts_credential_file>
----
+
where:
+
--
`<arn_role>`:: Specifies the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`.
`<instance_types>`:: Specifies the instance type, for example, `m6i.xlarge`.
`<region>`:: Specifies the {aws-short} region, for example, `us-east-1`.
`<hosted_cluster_name>`:: Specifies your hosted cluster name, for example, `my-external-aws`.
`<service_consumer_domain>`:: Specifies the public hosted zone that the service consumer owns, for example, `service-consumer-domain.com`.
`<node_replica_count>`:: Specifies the node replica count, for example, `2`.
`<path_to_your_pull_secret>`:: Specifies the path to your pull secret file.
`<ocp_release_image>`:: Specifies the supported OpenShift Container Platform version that you want to use, for example, `4.22.0-multi`.
`<service_provider_domain>`:: Specifies the public hosted zone that the service provider owns, for example, `service-provider-domain.com`.
`<endpoint_access_configuraton>`:: Specifies the endpoint access configuration for the external DNS. Set as `PublicAndPrivate`. You can use external DNS with `Public` or `PublicAndPrivate` configurations only.
`<path_to_sts_credential_file>`:: Specifies the path to your {aws-short} STS credentials file, for example, `/home/user/sts-creds/sts-creds.json`.
--

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-bm.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-virt.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-non-bm.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-ibm-power.adoc
// * hosted_control_planes/hcp-deploy/hcp-deploy-ibmz.adoc

[id="hcp-custom-dns_{context}"]
= Defining a custom DNS name

[role="_abstract"]
As a cluster administrator, you can create a hosted cluster with an external API DNS name that differs from the internal endpoint that gets used for node bootstraps and control plane communication.

You might want to define a different DNS name for the following reasons:

* To replace the user-facing TLS certificate with one from a public CA without breaking the control plane functions that bind to the internal root CA
* To support split-horizon DNS and NAT scenarios
* To ensure a similar experience to standalone control planes, where you can use functions, such as the `Show Login Command` function, with the correct `kubeconfig` and DNS configuration

You can define a DNS name either during your initial setup or during postinstallation operations, by entering a domain name in the `kubeAPIServerDNSName` parameter of a `HostedCluster` object.

.Prerequisites

* You have a valid TLS certificate that covers the DNS name that you set in the `kubeAPIServerDNSName` parameter.
* You have a resolvable DNS name URI that can reach and point to the correct address.

.Procedure

* In the specification for the `HostedCluster` object, add the `kubeAPIServerDNSName` parameter and the address for the domain and specify which certificate to use, as shown in the following example:
+
[source,yaml]
----
#...
spec:
  configuration:
    apiServer:
      servingCerts:
        namedCertificates:
        - names:
          - xxx.example.com
          - yyy.example.com
          servingCertificate:
            name: <my_serving_certificate>
  kubeAPIServerDNSName: <custom_address>
----
+
The value for the `kubeAPIServerDNSName` parameter must be a valid and addressable domain.
+
After you define the `kubeAPIServerDNSName` parameter and specify the certificate, the Control Plane Operator controllers create a `kubeconfig` file named `custom-admin-kubeconfig`, where the file gets stored in the `HostedControlPlane` namespace. The generation of certificates happen from the root CA, and the `HostedControlPlane` namespace manages their expiration and renewal.
+
The Control Plane Operator reports a new `kubeconfig` file named `CustomKubeconfig` in the `HostedControlPlane` namespace. That file uses the defined new server in the `kubeAPIServerDNSName` parameter.
+
A reference for the custom `kubeconfig` file exists in the `status` parameter as `CustomKubeconfig` of the `HostedCluster` object. The `CustomKubeConfig` parameter is optional, and you can add the parameter only if the `kubeAPIServerDNSName` parameter is not empty. After you set the `CustomKubeConfig` parameter, the parameter triggers the generation of a secret named `<hosted_cluster_name>-custom-admin-kubeconfig` in the `HostedCluster` namespace. You can use the secret to access the `HostedCluster` API server. If you remove the `CustomKubeConfig` parameter during postinstallation operations, deletion of all related secrets and status references occur.
+
[NOTE]
====
Defining a custom DNS name does not directly impact the data plane, so no expected rollouts occur. The `HostedControlPlane` namespace receives the changes from the HyperShift Operator and deletes the corresponding parameters.
====
+
If you remove the `kubeAPIServerDNSName` parameter from the specification for the `HostedCluster` object, all newly generated secrets and the `CustomKubeconfig` reference are removed from the cluster and from the `status` parameter.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-create-hc-aws_{context}"]
= Creating a hosted cluster on {aws-short}

[role="_abstract"]
On {aws-short}, you can create a hosted cluster by using the command-line interface, `hcp`, or by providing {aws-short} STS credentials. You can also create a hosted cluster in multiple zones on {aws-short}.

A _hosted cluster_ is an OpenShift Container Platform cluster with its API endpoint and control plane hosted on a management cluster. The hosted cluster includes the control plane and its corresponding data plane.

The hosted cluster is automatically imported as a managed cluster. If you want to disable this automatic import feature, see "Disabling the automatic import of hosted clusters into {mce-short}".

By default for {hcp} on {aws-short}, you use an AMD64 hosted cluster. However, you can enable {hcp} to run on an ARM64 hosted cluster. For more information, see "Running hosted clusters on an ARM64 architecture".

For compatible combinations of node pools and hosted clusters, see the following table:

.Compatible architectures for node pools and hosted clusters
[cols="2,2",options="header"]
|===
| Hosted cluster | Node pools
| AMD64 | AMD64 or ARM64
| ARM64 | ARM64 or AMD64
|===

[role="_additional-resources"]
.Additional resources

* Disabling the automatic import of hosted clusters into {mce-short}
* Running hosted clusters on an ARM64 architecture

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-aws-deploy-hc_{context}"]
= Creating a hosted cluster on {aws-short} by using the CLI

[role="_abstract"]
To create a hosted cluster on {aws-first}, you can use the hosted control plane command-line interface (`hcp`).

.Prerequisites

* You have set up the hosted control plane CLI, `hcp`.

* You have enabled the `local-cluster` managed cluster as the management cluster.

* You created an {aws-short} Identity and Access Management (IAM) role and {aws-short} Security Token Service (STS) credentials.

.Procedure

. To create a hosted cluster on {aws-short}, run the following command:
+
[source,terminal]
----
$ hcp create cluster aws \
    --name <hosted_cluster_name> \
    --infra-id <infra_id> \
    --base-domain <basedomain> \
    --sts-creds <path_to_sts_credential_file> \
    --pull-secret <path_to_pull_secret> \
    --region <region> \
    --generate-ssh \
    --node-pool-replicas <node_pool_replica_count> \
    --namespace <hosted_cluster_namespace> \
    --role-arn <role_name> \
    --render-into <file_name>.yaml
----
+
where:

`<hosted_cluster_name>`:: Specifies the name of your hosted cluster.
`<infra_id>`:: Specifies your infrastructure name. You must provide the same value for `<hosted_cluster_name>` and `<infra_id>`. Otherwise the cluster might not appear correctly in the {mce} console.
`<basedomain>`:: Specifies your base domain, for example, `example.com`.
`<path_to_sts_credential_file>`:: Specifies the path to your AWS STS credentials file, for example, `/home/user/sts-creds/sts-creds.json`.
`<path_to_pull_secret>`:: Specifies the path to your pull secret, for example, `/user/name/pullsecret`.
`<region>`:: Specifies the AWS region name, for example, `us-east-1`.
`<node_pool_replica_count>`:: Specifies the node pool replica count, for example, `3`.
`<hosted_cluster_namespace>`:: Specifies that you want to create the `HostedCluster` and `NodePool` custom resource in a specific namespace. Otherwise, by default, all `HostedCluster` and `NodePool` custom resources are created in the `clusters` namespace.
`<role_name>`:: Specifies the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`.
`<file_name>`:: Specifies whether the EC2 instance runs on shared or single tenant hardware. The `--render-into` flag renders Kubernetes resources into the YAML file that you specify in this field. Continue to the next step to edit the YAML file.

. If you included the `--render-into` flag in the previous command, edit the specified YAML file. Edit the `NodePool` specification in the YAML file to indicate whether the EC2 instance should run on shared or single-tenant hardware, similar to the following example:
+
.Example YAML file
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: NodePool
metadata:
  name: <nodepool_name>
spec:
  platform:
    aws:
      placement:
        tenancy: "default"
----
+
where:
+
--
`<nodepool_name>`:: Specifies the name of the `NodePool` resource.
`spec.platform.aws.placement.tenancy`:: Specifies a valid value for tenancy: `"default"`, `"dedicated"`, or `"host"`. Use `"default"` when node pool instances run on shared hardware. Use `"dedicated"` when each node pool instance runs on single-tenant hardware. Use `"host"` when node pool instances run on your pre-allocated dedicated hosts.
--

. If you use external load balancers, configure the ingress endpoint by editing the `HostedCluster` resource as shown in the following example. If you do not configure the endpoint, the default behavior is to randomize the node port that the service exposes the ingress on. To configure how the ingress controller publishes the default ingress route, set the `endpointPublishingStrategy` parameter and its underlying functions:
+
[source,yaml]
----
#...
spec:
  operatorConfiguration:
    ingressOperator:
      endpointPublishingStrategy:
        type: LoadBalancerService
        loadBalancer:
          scope: Internal
#...
----
+
The `spec.operatorConfiguration.ingressOperator.endPointPublishingStrategy.type` parameter specifies the endpoint for the load balancer. For {aws-short}, use the `LoadBalancerService` type.

.Verification

. Verify the status of your hosted cluster to check that the value of `AVAILABLE` is `True`. Run the following command:
+
[source,terminal]
----
$ oc get hostedclusters -n <hosted_cluster_namespace>
----

. Get a list of your node pools by running the following command:
+
[source,terminal]
----
$ oc get nodepools --namespace <hosted_cluster_namespace>
----

[role="_additional-resources"]
.Additional resources

* Configuring a custom API server certificate in a hosted cluster

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-create-hc-multi-zone-aws-creds_{context}"]
= Creating a hosted cluster by providing {aws-short} STS credentials

[role="_abstract"]
To enhance the security of your hosted control plane deployment, you can create a hosted cluster on {aws-short} by using the {aws-short} Security Token Service (STS).

When you create a hosted cluster by using the `hcp create cluster aws` command, you must provide an {aws-first} account credentials that have permissions to create infrastructure resources for your hosted cluster.

Infrastructure resources include the following examples:

* Virtual Private Cloud (VPC)
* Subnets
* Network address translation (NAT) gateways

You can provide the {aws-short} credentials by using the either of the following ways:

* The {aws-short} Security Token Service (STS) credentials
* The {aws-short} cloud provider secret from {mce-short}

.Procedure

* To create a hosted cluster on {aws-short} by providing {aws-short} STS credentials, enter the following command:
+
[source,terminal]
----
$ hcp create cluster aws \
  --name <hosted_cluster_name> \
  --node-pool-replicas <node_pool_replica_count> \
  --base-domain <base_domain> \
  --pull-secret <path_to_pull_secret> \
  --sts-creds <path_to_sts_credential_file> \
  --region <region> \
  --role-arn <arn_role>
----
+
where:
+
`<hosted_cluster_name>`:: Specifies the name of your hosted cluster, for example, `my-hosted-cluster-01`.
`<node_pool_replica_count>`:: Specifies the node pool replica count, for example, `2`.
`<base_domain>`:: Specifies your base domain, for example, `example.com`.
`<path_to_pull_secret>`:: Specifies the path to your pull secret, for example, `/user/name/pullsecret`.
`<path_to_sts_credentials>`:: Specifies the path to your {aws-short} STS credentials file, for example, `/home/user/sts-creds/sts-creds.json`.
`<region>`:: Specifies the {aws-short} region name, for example, `us-east-1`.
`<arn_role>`:: Specifies the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hc-create-aws-multiple-zones_{context}"]
= Creating a hosted cluster in multiple zones on {aws-short}

[role="_abstract"]
To improve availability and fault tolerance, you can create a hosted cluster across multiple {aws-short} availability zones. Distributing your node pools and compute nodes across several zones protects your workloads against potential outages in a single geographical region.

You can create a hosted cluster in multiple zones on {aws-first} by using the `hcp` command-line interface (CLI).

.Prerequisites

* You created an {aws-short} Identity and Access Management (IAM) role and {aws-short} Security Token Service (STS) credentials.

.Procedure

* Create a hosted cluster in multiple zones on {aws-short} by running the following command:
+
[source,terminal]
----
$ hcp create cluster aws \
  --name <hosted_cluster_name> \
  --node-pool-replicas=<node_pool_replica_count> \
  --base-domain <base_domain> \
  --pull-secret <path_to_pull_secret> \
  --role-arn <arn_role> \
  --region <region> \
  --zones <zones> \
  --sts-creds <path_to_sts_credential_file>
----
+
where:
+
`<hosted_cluster_name>`:: Specifies the name of your hosted cluster, such as `my-hosted-cluster-01`.
`<node_pool_replica_count>`:: Specifies the node pool replica count, for example, `2`.
`<base_domain>`:: Specifies your base domain, for example, `example.com`.
`<path_to_pull_secret>`:: Specifies the path to your pull secret, for example, `/user/name/pullsecret`.
`<arn_role>`:: Specifies the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`.
`<region>`:: Specifies the {aws-short} region name, for example, `us-east-1`.
`<zones>`:: Specifies availability zones within your {aws-short} region, for example, `us-east-1a`, and `us-east-1b`. For each specified zone, the following infrastructure is created: public subnet, private subnet, NAT gateway, and private route table. A public route table is shared across public subnets. One `NodePool` resource is created for each zone. The node pool name is suffixed by the zone name. The private subnet for the zone is set in the `spec.platform.aws.subnet.id` parameter.
`<path_to_sts_credential_file>`:: Specifies the path to your {aws-short} STS credentials file, for example, `/home/user/sts-creds/sts-creds.json`.

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-access-hc-aws_{context}"]
= Accessing a hosted cluster on {aws-short}

[role="_abstract"]
After you create a hosted cluster on {aws-short}, you can access it by using your `kubeconfig` file, access secrets, and `kubeadmin` credentials.

The hosted cluster namespace contains hosted cluster resources and the access secrets. The hosted control plane runs in the hosted control plane namespace.

The secret name formats are shown in the following table:

.Access secrets
[cols="3",options="header"]
|===
|Secret |Format |Example

|`kubeconfig` secret
|`<hosted_cluster_namespace>-<name>-admin-kubeconfig`
|`clusters-hypershift-demo-admin-kubeconfig`

|`kubeadmin` password secret
|`<hosted_cluster_namespace>-<name>-kubeadmin-password`
|`clusters-hypershift-demo-kubeadmin-password`
|===

[NOTE]
====
The `kubeadmin` password secret is Base64-encoded and the `kubeconfig` secret contains a Base64-encoded `kubeconfig` configuration. You must decode the Base64-encoded `kubeconfig` configuration and save it into a `<hosted_cluster_name>.kubeconfig` file.
====

.Procedure

. Generate the `kubeconfig` file by entering the following command:
+
[source,terminal]
----
$ hcp create kubeconfig --namespace <hosted_cluster_namespace> \
  --name <hosted_cluster_name> > <hosted_cluster_name>.kubeconfig
----

. Use your `<hosted_cluster_name>.kubeconfig` file that contains the decoded `kubeconfig` configuration to access the hosted cluster. Enter the following command:
+
[source,terminal]
----
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
----
+
You must decode the `kubeadmin` password secret to log in to the API server or the console of the hosted cluster.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-enable-arm-amd_{context}"]
= Running hosted clusters on an ARM64 architecture

[role="_abstract"]
By default for {hcp} on {aws-first}, you use an AMD64 hosted cluster. However, you can enable {hcp} to run on an ARM64 hosted cluster.

For compatible combinations of node pools and hosted clusters, see the following table:

.Compatible architectures for node pools and hosted clusters
[cols="2,2",options="header"]
|===
| Hosted cluster | Node pools
| AMD64 | AMD64 or ARM64
| ARM64 | ARM64 or AMD64
|===

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-create-hc-arm64-aws_{context}"]
= Creating a hosted cluster on an ARM64 OpenShift Container Platform cluster

[role="_abstract"]
You can run a hosted cluster on an ARM64 OpenShift Container Platform cluster for {aws-first} by overriding the default release image with a multi-architecture release image.

If you do not use a multi-architecture release image, the compute nodes in the node pool are not created and reconciliation of the node pool stops until you either use a multi-architecture release image in the hosted cluster or update the `NodePool` custom resource based on the release image.

.Prerequisites

* You must have an OpenShift Container Platform cluster with a 64-bit ARM infrastructure that is installed on {aws-short}. For more information, see "Create an OpenShift Container Platform Cluster: {aws-short} (ARM)".
* You must create an {aws-short} Identity and Access Management (IAM) role and {aws-short} Security Token Service (STS) credentials. For more information, see "Creating an {aws-short} IAM role and STS credentials".

.Procedure

* Create a hosted cluster on an ARM64 OpenShift Container Platform cluster by entering the following command:
+
[source,terminal]
----
$ hcp create cluster aws \
  --name <hosted_cluster_name> \
  --node-pool-replicas <node_pool_replica_count> \
  --base-domain <base_domain> \
  --pull-secret <path_to_pull_secret> \
  --sts-creds <path_to_sts_credential_file> \
  --region <region> \
  --release-image quay.io/openshift-release-dev/ocp-release:<ocp_release_image> \
  --role-arn <role_name>
----
+
where:
+
`<hosted_cluster_name>`:: Specifies the name of your hosted cluster, for example, `my-hosted-cluster-01`.
`<node_pool_replica_count>`:: Specifies the node pool replica count, for example, `3`.
`<base_domain>`:: Specifies your base domain, for example, `example.com`.
`<path_to_pull_secret>`:: Specifies the path to your pull secret, for example, `/user/name/pullsecret`.
`<path_to_sts_credential_file>`:: Specifies the path to your {aws-short} STS credentials file, for example, `/home/user/sts-creds/sts-creds.json`.
`<region>`:: Specifies the {aws-short} region name, for example, `us-east-1`.
`<ocp_release_image>`:: Specifies the supported OpenShift Container Platform version that you want to use, for example, `4.22.0-multi`. If you are using a disconnected environment, replace `<ocp_release_image>` with the digest image. To extract the OpenShift Container Platform release image digest, see "Extracting the OpenShift Container Platform release image digest".
`<role_name>`:: Specifies the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`.

[role="_additional-resources"]
.Additional resources

* Create an OpenShift Container Platform Cluster: {aws-short} (ARM)
* Creating an {aws-short} IAM role and STS credentials

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-create-np-arm64-aws_{context}"]
= Creating an ARM or AMD NodePool object on {aws-short} hosted clusters

[role="_abstract"]
You can schedule application workloads that are the `NodePool` objects on 64-bit ARM and AMD from the same hosted control plane. To set the required processor architecture for the `NodePool` object, you define the `arch` field in the `NodePool` specification.

The valid values for the `arch` field are as follows:

* `arm64`
* `amd64`

.Prerequisites

* You must have a multi-architecture image for the `HostedCluster` custom resource to use. You can access multi-architecture nightly images. For more information, see "Multi-architecture nightly images".

.Procedure

* Add an ARM or AMD `NodePool` object to the hosted cluster on {aws-short} by running the following command:
+
[source,terminal]
----
$ hcp create nodepool aws \
  --cluster-name <hosted_cluster_name> \
  --name <node_pool_name> \
  --node-count <node_pool_replica_count> \
  --arch <architecture>
----
+
where:
+
`<hosted_cluster_name>`:: Specifies the name of your hosted cluster, for example, `my-hosted-cluster-01`.
`<node_pool_name>`:: Specifies the node pool name.
`<node_pool_replica_count>`:: Specifies the node pool replica count, for example, `3`.
`<architecture>`:: Specifies the architecture type, such as `arm64` or `amd64`. If you do not specify a value for the `--arch` flag, the `amd64` value is used by default.

[role="_additional-resources"]
.Additional resources

* Multi-architecture nightly images
* Extracting the OpenShift Container Platform release image digest

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-create-private-hc-aws_{context}"]
= Creating a private hosted cluster on {aws-short}

[role="_abstract"]
After you enable the `local-cluster` as the management cluster, you can deploy a hosted cluster or a private hosted cluster on {aws-first}.

By default, hosted clusters are publicly accessible through public DNS and the default router for the management cluster.

For private clusters on {aws-short}, all communication with the hosted cluster occurs over {aws-short} PrivateLink.

.Prerequisites

* You enabled {aws-short} PrivateLink. For more information, see "Enabling {aws-short} PrivateLink".

* You created an {aws-short} Identity and Access Management (IAM) role and {aws-short} Security Token Service (STS) credentials. For more information, see "Creating an {aws-short} IAM role and STS credentials" and "Identity and Access Management (IAM) permissions".

* You configured a bastion instance on {aws-short}. For more information, see "Tutorial: Configuring private network access using a Linux Bastion Host".

.Procedure

* Create a private hosted cluster on {aws-short} by entering the following command:
+
[source,terminal]
----
$ hcp create cluster aws \
  --name <hosted_cluster_name> \
  --node-pool-replicas=<node_pool_replica_count> \
  --base-domain <basedomain> \
  --pull-secret <path_to_pull_secret> \
  --sts-creds <path_to_sts_credential_file> \
  --region <region> \
  --endpoint-access Private \
  --role-arn <role_name>
----
+
where:
+
--
`<hosted_cluster_name>`:: Specifies the name of your hosted cluster, such as, `example`.
`<node_pool_replica_count>`:: Specifies the node pool replica count, for example, `3`.
`<basedomain>`:: Specifies your base domain, for example, `example.com`.
`<path_to_pull_secret>`:: Specifies the path to your pull secret, for example, `/user/name/pullsecret`.
`<path_to_sts_credential_file>`:: Specifies the path to your {aws-short} STS credentials file, for example, `/home/user/sts-creds/sts-creds.json`.
`<region>`:: Specifies the {aws-short} region name, for example, `us-east-1`.
`Private`:: Specifies that the cluster is private.
`<role_name>`:: Specifies the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`. For more information about ARN roles, see "Identity and Access Management (IAM) permissions".
--
+
The following API endpoints for the hosted cluster are accessible through a private DNS zone:

* `api.<hosted_cluster_name>.hypershift.local`
* `*.apps.<hosted_cluster_name>.hypershift.local`

[role="_additional-resources"]
.Additional resources

* Enabling {aws-short} PrivateLink for {hcp}
* Creating an {aws-short} IAM role and STS credentials
* Identity and Access Management (IAM) permissions
* Tutorial: Configuring private network access using a Linux Bastion Host

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-deploy/hcp-deploy-aws.adoc

[id="hcp-access-private-hc-aws_{context}"]
= Accessing a private hosted cluster on {aws-short}

[role="_abstract"]
After you create a private hosted cluster, you can access it by using the command-line interface (CLI).

.Procedure

. Find the private IPs of nodes by entering the following command:
+
[source,terminal]
----
$ aws ec2 describe-instances \
  --filter="Name=tag:kubernetes.io/cluster/<infra_id>,Values=owned" \
  | jq '.Reservations[] | .Instances[] | select(.PublicDnsName=="") \
  | .PrivateIpAddress'
----

. Create a `kubeconfig` file for the hosted cluster that you can copy to a node by entering the following command:
+
[source,terminal]
----
$ hcp create kubeconfig > <hosted_cluster_kubeconfig>
----

. To SSH into one of the nodes through the bastion, enter the following command:
+
[source,terminal]
----
$ ssh -o ProxyCommand="ssh ec2-user@<bastion_ip> \
  -W %h:%p" core@<node_ip>
----

. From the SSH shell, copy the `kubeconfig` file contents to a file on the node by entering the following command:
+
[source,terminal]
----
$ mv <path_to_kubeconfig_file> <new_file_name>
----

. Export the `kubeconfig` file by entering the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<path_to_kubeconfig_file>
----

. Observe the hosted cluster status by entering the following command:
+
[source,terminal]
----
$ oc get clusteroperators clusterversion
----
