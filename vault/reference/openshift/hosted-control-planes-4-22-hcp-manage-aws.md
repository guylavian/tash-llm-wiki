---
title: "Managing {hcp} on {aws-short}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-manage-aws
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-manage-aws
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Managing {hcp} on {aws-short}

[id="hcp-manage-aws"]
= Managing {hcp} on {aws-short}

When you use {hcp} for OpenShift Container Platform on {aws-first}, the infrastructure requirements vary based on your setup.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-manage-aws-prereq_{context}"]
= Prerequisites to manage {aws-short} infrastructure and IAM permissions

To configure {hcp} for OpenShift Container Platform on {aws-first}, you must meet the following the infrastructure requirements:

* You configured {hcp} before you can create hosted clusters.
* You created an {aws-short} Identity and Access Management (IAM) role and {aws-short} Security Token Service (STS) credentials.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-manage-aws-infra-req_{context}"]
= Infrastructure requirements for {aws-short}

When you use {hcp} on {aws-first}, the infrastructure requirements fit in the following categories:

* Prerequired and unmanaged infrastructure for the HyperShift Operator in an arbitrary {aws-short} account
* Prerequired and unmanaged infrastructure in a hosted cluster {aws-short} account
* {hcp-capital}-managed infrastructure in a management {aws-short} account
* {hcp-capital}-managed infrastructure in a hosted cluster {aws-short} account
* Kubernetes-managed infrastructure in a hosted cluster {aws-short} account

Prerequired means that {hcp} requires {aws-short} infrastructure to properly work. Unmanaged means that no Operator or controller creates the infrastructure for you.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-manage-aws-infra-ho-req_{context}"]
= Unmanaged infrastructure for the HyperShift Operator in an {aws-short} account

An arbitrary {aws-first} account depends on the provider of the {hcp} service.

In self-managed {hcp}, the cluster service provider controls the {aws-short} account. The cluster service provider is the administrator who hosts cluster control planes and is responsible for uptime. In managed {hcp}, the {aws-short} account belongs to Red Hat.

In a prerequired and unmanaged infrastructure for the HyperShift Operator, the following infrastructure requirements apply for a management cluster {aws-short} account:

* One S3 Bucket
** OpenID Connect (OIDC)

* Route 53 hosted zones
** A domain to host private and public entries for hosted clusters

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-unmanaged-aws-hc-prereq_{context}"]
= Unmanaged infrastructure requirements for a management {aws-short} account

When your infrastructure is prerequired and unmanaged in a hosted cluster {aws-first} account, the infrastructure requirements for all access modes are as follows:

* One VPC
* One DHCP Option
* Two subnets
** A private subnet that is an internal data plane subnet
** A public subnet that enables access to the internet from the data plane
* One internet gateway
* One elastic IP
* One NAT gateway
* One security group (worker nodes)
* Two route tables (one private and one public)
* Two Route 53 hosted zones
* Enough quota for the following items:
** One Ingress service load balancer for public hosted clusters
** One private link endpoint for private hosted clusters

[NOTE]
====
For private link networking to work, the endpoint zone in the hosted cluster {aws-short} account must match the zone of the instance that is resolved by the service endpoint in the management cluster {aws-short} account. In {aws-short}, the zone names are aliases, such as us-east-2b, which do not necessarily map to the same zone in different accounts. As a result, for private link to work, the management cluster must have subnets or workers in all zones of its region.
====

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-managed-aws-infra-mgmt_{context}"]
= Infrastructure requirements for a management {aws-short} account

When your infrastructure is managed by {hcp} in a management AWS account, the infrastructure requirements differ depending on whether your clusters are public, private, or a combination.

For accounts with public clusters, the infrastructure requirements are as follows:

* Network load balancer: a load balancer Kube API server
** Kubernetes creates a security group

* Volumes
** For etcd (one or three depending on high availability)
** For OVN-Kube

For accounts with private clusters, the infrastructure requirements are as follows:

* Network load balancer: a load balancer private router
* Endpoint service (private link)

For accounts with public and private clusters, the infrastructure requirements are as follows:

* Network load balancer: a load balancer public router
* Network load balancer: a load balancer private router
* Endpoint service (private link)
* Volumes
** For etcd (one or three depending on high availability)
** For OVN-Kube

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-managed-aws-infra-hc_{context}"]
= Infrastructure requirements for an {aws-short} account in a hosted cluster

When your infrastructure is managed by {hcp} in a hosted cluster {aws-first} account, the infrastructure requirements differ depending on whether your clusters are public, private, or a combination.

For accounts with public clusters, the infrastructure requirements are as follows:

* Node pools must have EC2 instances that have `Role` and `RolePolicy` defined.

For accounts with private clusters, the infrastructure requirements are as follows:

* One private link endpoint for each availability zone
* EC2 instances for node pools

For accounts with public and private clusters, the infrastructure requirements are as follows:

* One private link endpoint for each availability zone
* EC2 instances for node pools

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-k8s-managed-aws-infra-hc_{context}"]
= Kubernetes-managed infrastructure in a hosted cluster {aws-short} account

When Kubernetes manages your infrastructure in a hosted cluster {aws-first} account, the infrastructure requirements are as follows:

* A network load balancer for default Ingress
* An S3 bucket for registry

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-managed-aws-iam_{context}"]
= Identity and Access Management (IAM) permissions

In the context of {hcp}, the consumer is responsible to create the Amazon Resource Name (ARN) roles. The _consumer_ is an automated process to generate the permissions files. The consumer might be the CLI or {cluster-manager}. {hcp-capital} can enable granularity to honor the principle of least-privilege components, which means that every component uses its own role to operate or create {aws-first} objects, and the roles are limited to what is required for the product to function normally.

The hosted cluster receives the ARN roles as input and the consumer creates an {aws-short} permission configuration for each component. As a result, the component can authenticate through STS and preconfigured OIDC IDP.

The following roles are consumed by some of the components from {hcp} that run on the control plane and operate on the data plane:

* `controlPlaneOperatorARN`
* `imageRegistryARN`
* `ingressARN`
* `kubeCloudControllerARN`
* `nodePoolManagementARN`
* `storageARN`
* `networkARN`

The following example shows a reference to the IAM roles from the hosted cluster:

[source,yaml]
----
...
endpointAccess: Public
  region: us-east-2
  resourceTags:
  - key: kubernetes.io/cluster/example-cluster-bz4j5
    value: owned
rolesRef:
    controlPlaneOperatorARN: arn:aws:iam::820196288204:role/example-cluster-bz4j5-control-plane-operator
    imageRegistryARN: arn:aws:iam::820196288204:role/example-cluster-bz4j5-openshift-image-registry
    ingressARN: arn:aws:iam::820196288204:role/example-cluster-bz4j5-openshift-ingress
    kubeCloudControllerARN: arn:aws:iam::820196288204:role/example-cluster-bz4j5-cloud-controller
    networkARN: arn:aws:iam::820196288204:role/example-cluster-bz4j5-cloud-network-config-controller
    nodePoolManagementARN: arn:aws:iam::820196288204:role/example-cluster-bz4j5-node-pool
    storageARN: arn:aws:iam::820196288204:role/example-cluster-bz4j5-aws-ebs-csi-driver-controller
type: AWS
...
----

The roles that {hcp} uses are shown in the following examples:

* `ingressARN`
+
[source,yaml]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeLoadBalancers",
                "tag:GetResources",
                "route53:ListHostedZones"
            ],
            "Resource": "\*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "route53:ChangeResourceRecordSets"
            ],
            "Resource": [
                "arn:aws:route53:::PUBLIC_ZONE_ID",
                "arn:aws:route53:::PRIVATE_ZONE_ID"
            ]
        }
    ]
}
----
* `imageRegistryARN`
+
[source,yaml]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:PutBucketTagging",
                "s3:GetBucketTagging",
                "s3:PutBucketPublicAccessBlock",
                "s3:GetBucketPublicAccessBlock",
                "s3:PutEncryptionConfiguration",
                "s3:GetEncryptionConfiguration",
                "s3:PutLifecycleConfiguration",
                "s3:GetLifecycleConfiguration",
                "s3:GetBucketLocation",
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:ListBucketMultipartUploads",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": "\*"
        }
    ]
}
----
* `storageARN`
+
[source,yaml]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AttachVolume",
                "ec2:CreateSnapshot",
                "ec2:CreateTags",
                "ec2:CreateVolume",
                "ec2:DeleteSnapshot",
                "ec2:DeleteTags",
                "ec2:DeleteVolume",
                "ec2:DescribeInstances",
                "ec2:DescribeSnapshots",
                "ec2:DescribeTags",
                "ec2:DescribeVolumes",
                "ec2:DescribeVolumesModifications",
                "ec2:DetachVolume",
                "ec2:ModifyVolume"
            ],
            "Resource": "\*"
        }
    ]
}
----
* `networkARN`
+
[source,yaml]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInstanceTypes",
                "ec2:UnassignPrivateIpAddresses",
                "ec2:AssignPrivateIpAddresses",
                "ec2:UnassignIpv6Addresses",
                "ec2:AssignIpv6Addresses",
                "ec2:DescribeSubnets",
                "ec2:DescribeNetworkInterfaces"
            ],
            "Resource": "\*"
        }
    ]
}
----
* `kubeCloudControllerARN`
+
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeRegions",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVolumes",
                "ec2:CreateSecurityGroup",
                "ec2:CreateTags",
                "ec2:CreateVolume",
                "ec2:ModifyInstanceAttribute",
                "ec2:ModifyVolume",
                "ec2:AttachVolume",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateRoute",
                "ec2:DeleteRoute",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteVolume",
                "ec2:DetachVolume",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:DescribeVpcs",
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:AttachLoadBalancerToSubnets",
                "elasticloadbalancing:ApplySecurityGroupsToLoadBalancer",
                "elasticloadbalancing:CreateLoadBalancer",
                "elasticloadbalancing:CreateLoadBalancerPolicy",
                "elasticloadbalancing:CreateLoadBalancerListeners",
                "elasticloadbalancing:ConfigureHealthCheck",
                "elasticloadbalancing:DeleteLoadBalancer",
                "elasticloadbalancing:DeleteLoadBalancerListeners",
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeLoadBalancerAttributes",
                "elasticloadbalancing:DetachLoadBalancerFromSubnets",
                "elasticloadbalancing:DeregisterInstancesFromLoadBalancer",
                "elasticloadbalancing:ModifyLoadBalancerAttributes",
                "elasticloadbalancing:RegisterInstancesWithLoadBalancer",
                "elasticloadbalancing:SetLoadBalancerPoliciesForBackendServer",
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateListener",
                "elasticloadbalancing:CreateTargetGroup",
                "elasticloadbalancing:DeleteListener",
                "elasticloadbalancing:DeleteTargetGroup",
                "elasticloadbalancing:DescribeListeners",
                "elasticloadbalancing:DescribeLoadBalancerPolicies",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:ModifyListener",
                "elasticloadbalancing:ModifyTargetGroup",
                "elasticloadbalancing:RegisterTargets",
                "elasticloadbalancing:SetLoadBalancerPoliciesOfListener",
                "iam:CreateServiceLinkedRole",
                "kms:DescribeKey"
            ],
            "Resource": [
                "\*"
            ],
            "Effect": "Allow"
        }
    ]
}
----
* `nodePoolManagementARN`
+
[source,yaml]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:AllocateAddress",
                "ec2:AssociateRouteTable",
                "ec2:AttachInternetGateway",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:CreateInternetGateway",
                "ec2:CreateNatGateway",
                "ec2:CreateRoute",
                "ec2:CreateRouteTable",
                "ec2:CreateSecurityGroup",
                "ec2:CreateSubnet",
                "ec2:CreateTags",
                "ec2:DeleteInternetGateway",
                "ec2:DeleteNatGateway",
                "ec2:DeleteRouteTable",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteSubnet",
                "ec2:DeleteTags",
                "ec2:DescribeAccountAttributes",
                "ec2:DescribeAddresses",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeImages",
                "ec2:DescribeInstances",
                "ec2:DescribeInternetGateways",
                "ec2:DescribeNatGateways",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeNetworkInterfaceAttribute",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:DescribeVpcAttribute",
                "ec2:DescribeVolumes",
                "ec2:DetachInternetGateway",
                "ec2:DisassociateRouteTable",
                "ec2:DisassociateAddress",
                "ec2:ModifyInstanceAttribute",
                "ec2:ModifyNetworkInterfaceAttribute",
                "ec2:ModifySubnetAttribute",
                "ec2:ReleaseAddress",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:RunInstances",
                "ec2:TerminateInstances",
                "tag:GetResources",
                "ec2:CreateLaunchTemplate",
                "ec2:CreateLaunchTemplateVersion",
                "ec2:DescribeLaunchTemplates",
                "ec2:DescribeLaunchTemplateVersions",
                "ec2:DeleteLaunchTemplate",
                "ec2:DeleteLaunchTemplateVersions"
            ],
            "Resource": [
                "\*"
            ],
            "Effect": "Allow"
        },
        {
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
                }
            },
            "Action": [
                "iam:CreateServiceLinkedRole"
            ],
            "Resource": [
                "arn:*:iam::*:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:*:iam::*:role/*-worker-role"
            ],
            "Effect": "Allow"
        }
    ]
}
----
* `controlPlaneOperatorARN`
+
[source,yaml]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateVpcEndpoint",
                "ec2:DescribeVpcEndpoints",
                "ec2:ModifyVpcEndpoint",
                "ec2:DeleteVpcEndpoints",
                "ec2:CreateTags",
                "route53:ListHostedZones"
            ],
            "Resource": "\*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "route53:ChangeResourceRecordSets",
                "route53:ListResourceRecordSets"
            ],
            "Resource": "arn:aws:route53:::%s"
        }
    ]
}
----

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-managed-aws-infra-iam-separate_{context}"]
= Creating {aws-short} infrastructure and IAM resources separate

By default, the `hcp create cluster aws` command creates cloud infrastructure with the hosted cluster and applies it. You can create the cloud infrastructure portion separately so that you can use the `hcp create cluster aws` command only to create the cluster, or render it to modify it before you apply it.

To create the cloud infrastructure portion separately, you need to create the {aws-first} infrastructure, create the {aws-short} Identity and Access (IAM) resources, and create the cluster.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-managed-aws-infra-separate_{context}"]
= Creating the {aws-short} infrastructure separately

To create the {aws-first} infrastructure, you need to create a Virtual Private Cloud (VPC) and other resources for your cluster. You can use the {aws-short} console or an infrastructure automation and provisioning tool. For instructions to use the {aws-short} console, see Create a VPC plus other VPC resources in the {aws-short} Documentation.

The VPC must include private and public subnets and resources for external access, such as a network address translation (NAT) gateway and an internet gateway. In addition to the VPC, you need a private hosted zone for the ingress of your cluster. If you are creating clusters that use PrivateLink (`Private` or `PublicAndPrivate` access modes), you need an additional hosted zone for PrivateLink.

Create the {aws-short} infrastructure for your hosted cluster by using the following example configuration:

[source,yaml]
[subs="+quotes"]
----
---
apiVersion: v1
kind: Namespace
metadata:
  creationTimestamp: null
  name: clusters
spec: {}
status: {}
---
apiVersion: v1
data:
  .dockerconfigjson: xxxxxxxxxxx
kind: Secret
metadata:
  creationTimestamp: null
  labels:
    hypershift.openshift.io/safe-to-delete-with-cluster: "true"
  name: <pull_secret_name> <1>
  namespace: clusters
---
apiVersion: v1
data:
  key: xxxxxxxxxxxxxxxxx
kind: Secret
metadata:
  creationTimestamp: null
  labels:
    hypershift.openshift.io/safe-to-delete-with-cluster: "true"
  name: <etcd_encryption_key_name> <2>
  namespace: clusters
type: Opaque
---
apiVersion: v1
data:
  id_rsa: xxxxxxxxx
  id_rsa.pub: xxxxxxxxx
kind: Secret
metadata:
  creationTimestamp: null
  labels:
    hypershift.openshift.io/safe-to-delete-with-cluster: "true"
  name: <ssh-key-name> <3>
  namespace: clusters
---
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  creationTimestamp: null
  name: <hosted_cluster_name> <4>
  namespace: clusters
spec:
  autoscaling: {}
  configuration: {}
  controllerAvailabilityPolicy: SingleReplica
  dns:
    baseDomain: <dns_domain> <5>
    privateZoneID: xxxxxxxx
    publicZoneID: xxxxxxxx
  etcd:
    managed:
      storage:
        persistentVolume:
          size: 8Gi
          storageClassName: gp3-csi
        type: PersistentVolume
    managementType: Managed
  fips: false
  infraID: <infra_id> <6>
  issuerURL: <issuer_url> <7>
  networking:
    clusterNetwork:
    - cidr: 10.132.0.0/14
    machineNetwork:
    - cidr: 10.0.0.0/16
    networkType: OVNKubernetes
    serviceNetwork:
    - cidr: 172.31.0.0/16
  olmCatalogPlacement: management
  platform:
    aws:
      cloudProviderConfig:
        subnet:
          id: <subnet_xxx> <8>
        vpc: <vpc_xxx> <9>
        zone: us-west-1b
      endpointAccess: Public
      multiArch: false
      region: us-west-1
      rolesRef:
        controlPlaneOperatorARN: arn:aws:iam::820196288204:role/<infra_id>-control-plane-operator
        imageRegistryARN: arn:aws:iam::820196288204:role/<infra_id>-openshift-image-registry
        ingressARN: arn:aws:iam::820196288204:role/<infra_id>-openshift-ingress
        kubeCloudControllerARN: arn:aws:iam::820196288204:role/<infra_id>-cloud-controller
        networkARN: arn:aws:iam::820196288204:role/<infra_id>-cloud-network-config-controller
        nodePoolManagementARN: arn:aws:iam::820196288204:role/<infra_id>-node-pool
        storageARN: arn:aws:iam::820196288204:role/<infra_id>-aws-ebs-csi-driver-controller
    type: AWS
  pullSecret:
    name: <pull_secret_name>
  release:
    image: quay.io/openshift-release-dev/ocp-release:4.16-x86_64
  secretEncryption:
    aescbc:
      activeKey:
        name: <etcd_encryption_key_name>
    type: aescbc
  services:
  - service: APIServer
    servicePublishingStrategy:
      type: LoadBalancer
  - service: OAuthServer
    servicePublishingStrategy:
      type: Route
  - service: Konnectivity
    servicePublishingStrategy:
      type: Route
  - service: Ignition
    servicePublishingStrategy:
      type: Route
  - service: OVNSbDb
    servicePublishingStrategy:
      type: Route
  sshKey:
    name: <ssh_key_name>
status:
  controlPlaneEndpoint:
    host: ""
    port: 0
---
apiVersion: hypershift.openshift.io/v1beta1
kind: NodePool
metadata:
  creationTimestamp: null
  name: <node_pool_name> <10>
  namespace: clusters
spec:
  arch: amd64
  clusterName: <hosted_cluster_name>
  management:
    autoRepair: true
    upgradeType: Replace
  nodeDrainTimeout: 0s
  platform:
    aws:
      instanceProfile: <instance_profile_name> <11>
      instanceType: m6i.xlarge
      rootVolume:
        size: 120
        type: gp3
      subnet:
        id: <subnet_xxx>
    type: AWS
  release:
    image: quay.io/openshift-release-dev/ocp-release:4.16-x86_64
  replicas: 2
status:
  replicas: 0
----
<1> Replace `<pull_secret_name>` with the name of your pull secret.
<2> Replace `<etcd_encryption_key_name>` with the name of your etcd encryption key.
<3> Replace `<ssh_key_name>` with the name of your SSH key.
<4> Replace `<hosted_cluster_name>` with the name of your hosted cluster.
<5> Replace `<dns_domain>` with your base DNS domain, such as `example.com`.
<6> Replace `<infra_id>` with the value that identifies the IAM resources that are associated with the hosted cluster.
<7> Replace `<issuer_url>` with your issuer URL, which ends with your `infra_id` value. For example, `https://example-hosted-us-west-1.s3.us-west-1.amazonaws.com/example-hosted-infra-id`.
<8> Replace `<subnet_xxx>` with your subnet ID. Both private and public subnets need to be tagged. For public subnets, use `kubernetes.io/role/elb=1`. For private subnets, use `kubernetes.io/role/internal-elb=1`.
<9> Replace `<vpc_xxx>` with your VPC ID.
<10> Replace `<node_pool_name>` with the name of your `NodePool` resource.
<11> Replace `<instance_profile_name>` with the name of your {aws-short} instance.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id=" hcp-managed-aws-iam-separate_{context}"]
= Creating the {aws-short} IAM resources

In {aws-first}, you must create the following IAM resources:

* An OpenID Connect (OIDC) identity provider in IAM, which is required to enable STS authentication.
* Seven roles, which are separate for every component that interacts with the provider, such as the Kubernetes controller manager, cluster API provider, and registry
* The instance profile, which is the profile that is assigned to all worker instances of the cluster

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-managed-aws-hc-separate_{context}"]
= Creating a hosted cluster separately

You can create a hosted cluster separately on {aws-first}.

To create a hosted cluster separately, enter the following command:

[source,terminal]
[subs="+quotes"]
----
$ hcp create cluster aws \
    --infra-id <infra_id> \// <1>
    --name <hosted_cluster_name> \// <2>
    --sts-creds <path_to_sts_credential_file> \// <3>
    --pull-secret <path_to_pull_secret> \// <4>
    --generate-ssh \// <5>
    --node-pool-replicas 3
    --role-arn <role_name> <6>
----
<1> Replace `<infra_id>` with the same ID that you specified in the `create infra aws` command. This value identifies the IAM resources that are associated with the hosted cluster.
<2> Replace `<hosted_cluster_name>` with the name of your hosted cluster.
<3> Replace `<path_to_sts_credential_file>` with the same name that you specified in the `create infra aws` command.
<4> Replace `<path_to_pull_secret>` with the name of the file that contains a valid OpenShift Container Platform pull secret.
<5> The `--generate-ssh` flag is optional, but is good to include in case you need to SSH to your workers. An SSH key is generated for you and is stored as a secret in the same namespace as the hosted cluster.
<6> Replace `<role_name>` with the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`. Specify the Amazon Resource Name (ARN), for example, `arn:aws:iam::820196288204:role/myrole`. For more information about ARN roles, see "Identity and Access Management (IAM) permissions".

You can also add the `--render` flag to the command and redirect output to a file where you can edit the resources before you apply them to the cluster.

After you run the command, the following resources are applied to your cluster:

* A namespace
* A secret with your pull secret
* A `HostedCluster`
* A `NodePool`
* Three AWS STS secrets for control plane components
* One SSH key secret if you specified the `--generate-ssh` flag.

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-migrate-aws-single-to-multiarch_{context}"]
= Transitioning a hosted cluster from single-architecture to multi-architecture

You can transition your single-architecture 64-bit AMD hosted cluster to a multi-architecture hosted cluster on {aws-first}, to reduce the cost of running workloads on your cluster. For example, you can run existing workloads on 64-bit AMD while transitioning to 64-bit ARM and you can manage these workloads from a central Kubernetes cluster.

A single-architecture hosted cluster can manage node pools of only one particular CPU architecture. However, a multi-architecture hosted cluster can manage node pools with different CPU architectures. On {aws-short}, a multi-architecture hosted cluster can manage both 64-bit AMD and 64-bit ARM node pools.

.Prerequisites

* You have installed an OpenShift Container Platform management cluster for {aws-short} on {rh-rhacm-first} with the {mce}.
* You have an existing single-architecture hosted cluster that uses 64-bit AMD variant of the OpenShift Container Platform release payload.
* An existing node pool that uses the same 64-bit AMD variant of the OpenShift Container Platform release payload and is managed by an existing hosted cluster.
* Ensure that you installed the following command-line tools:

** `oc`
** `kubectl`
** `hcp`
** `skopeo`

.Procedure

. Review an existing OpenShift Container Platform release image of the single-architecture hosted cluster by running the following command:
+
[source,terminal]
----
$ oc get hostedcluster/<hosted_cluster_name> \// <1>
  -o jsonpath='{.spec.release.image}'
----
+
<1> Replace `<hosted_cluster_name>` with your hosted cluster name.
+
.Example output
[source,terminal]
----
quay.io/openshift-release-dev/ocp-release:<4.y.z>-x86_64 <1>
----
<1> Replace `<4.y.z>` with the supported OpenShift Container Platform version that you use.

. In your OpenShift Container Platform release image, if you use the digest instead of a tag, find the multi-architecture tag version of your release image:

.. Set the `OCP_VERSION` environment variable for the OpenShift Container Platform version by running the following command:
+
[source,terminal]
----
$ OCP_VERSION=$(oc image info quay.io/openshift-release-dev/ocp-release@sha256:ac78ebf77f95ab8ff52847ecd22592b545415e1ff6c7ff7f66bf81f158ae4f5e \
  -o jsonpath='{.config.config.Labels["io.openshift.release"]}')
----

.. Set the `MULTI_ARCH_TAG` environment variable for the multi-architecture tag version of your release image by running the following command:
+
[source,terminal]
----
$ MULTI_ARCH_TAG=$(skopeo inspect docker://quay.io/openshift-release-dev/ocp-release@sha256:ac78ebf77f95ab8ff52847ecd22592b545415e1ff6c7ff7f66bf81f158ae4f5e \
  | jq -r '.RepoTags' | sed 's/"//g' | sed 's/,//g' \
  | grep -w "$OCP_VERSION-multi$" | xargs)
----

.. Set the `IMAGE` environment variable for the multi-architecture release image name by running the following command:
+
[source,terminal]
----
$ IMAGE=quay.io/openshift-release-dev/ocp-release:$MULTI_ARCH_TAG
----

.. To see the list of multi-architecture image digests, run the following command:
+
[source,terminal]
----
$ oc image info $IMAGE
----
+
.Example output
[source,terminal]
----
OS            DIGEST
linux/amd64   sha256:b4c7a91802c09a5a748fe19ddd99a8ffab52d8a31db3a081a956a87f22a22ff8
linux/ppc64le sha256:66fda2ff6bd7704f1ba72be8bfe3e399c323de92262f594f8e482d110ec37388
linux/s390x   sha256:b1c1072dc639aaa2b50ec99b530012e3ceac19ddc28adcbcdc9643f2dfd14f34
linux/arm64   sha256:7b046404572ac96202d82b6cb029b421dddd40e88c73bbf35f602ffc13017f21
----

. Transition the hosted cluster from single-architecture to multi-architecture:

.. Set the multi-architecture OpenShift Container Platform release image for the hosted cluster by ensuring that you use the same OpenShift Container Platform version as the hosted cluster. Run the following command:
+
[source,terminal]
----
$ oc patch -n clusters hostedclusters/<hosted_cluster_name> -p \
  '{"spec":{"release":{"image":"quay.io/openshift-release-dev/ocp-release:<4.x.y>-multi"}}}' \// <1>
  --type=merge
----
<1> Replace `<4.y.z>` with the supported OpenShift Container Platform version that you use.

.. Confirm that the multi-architecture image is set in your hosted cluster by running the following command:
+
[source,terminal]
----
$ oc get hostedcluster/<hosted_cluster_name> \
  -o jsonpath='{.spec.release.image}'
----

. Check that the status of the `HostedControlPlane` resource is `Progressing` by running the following command:
+
[source,terminal]
----
$ oc get hostedcontrolplane -n <hosted_control_plane_namespace> -oyaml
----
+
.Example output
[source,yaml]
----
#...
  - lastTransitionTime: "2024-07-28T13:07:18Z"
    message: HostedCluster is deploying, upgrading, or reconfiguring
    observedGeneration: 5
    reason: Progressing
    status: "True"
    type: Progressing
#...
----

. Check that the status of the `HostedCluster` resource is `Progressing` by running the following command:
+
[source,terminal]
----
$ oc get hostedcluster <hosted_cluster_name> \
  -n <hosted_cluster_namespace> -oyaml
----

.Verification

* Verify that a node pool is using the multi-architecture release image in your `HostedControlPlane` resource by running the following command:
+
[source,terminal]
----
$ oc get hostedcontrolplane -n clusters-example -oyaml
----
+
.Example output
[source,yaml]
----
#...
version:
    availableUpdates: null
    desired:
      image: quay.io/openshift-release-dev/ocp-release:<4.x.y>-multi <1>
      url: https://access.redhat.com/errata/RHBA-2024:4855
      version: 4.16.5
    history:
    - completionTime: "2024-07-28T13:10:58Z"
      image: quay.io/openshift-release-dev/ocp-release:<4.x.y>-multi
      startedTime: "2024-07-28T13:10:27Z"
      state: Completed
      verified: false
      version: <4.x.y>
----
<1> Replace `<4.y.z>` with the supported OpenShift Container Platform version that you use.

+
[NOTE]
====
The multi-architecture OpenShift Container Platform release image is updated in your `HostedCluster`, `HostedControlPlane` resources, and hosted control plane pods. However, your existing node pools do not transition with the multi-architecture image automatically, because the release image transition is decoupled between the hosted cluster and node pools. You must create new node pools on your new multi-architecture hosted cluster.
====

.Next steps

* Creating node pools on the multi-architecture hosted cluster

// Module included in the following assemblies:
//
// * hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-migrate-aws-multiarch-nodepools_{context}"]
= Creating node pools on the multi-architecture hosted cluster

After transitioning your hosted cluster from single-architecture to multi-architecture, create node pools on compute machines based on 64-bit AMD and 64-bit ARM architectures.

.Procedure

. Create node pools based on 64-bit ARM architecture by entering the following command:
+
[source,terminal]
----
$ hcp create nodepool aws \
  --cluster-name <hosted_cluster_name> \// <1>
  --name <nodepool_name> \// <2>
  --node-count=<node_count> \// <3>
  --arch arm64
----
<1> Replace `<hosted_cluster_name>` with your hosted cluster name.
<2> Replace `<nodepool_name>` with your node pool name.
<3> Replace `<node_count>` with integer for your node count, for example, `2`.

. Create node pools based on 64-bit AMD architecture by entering the following command:
+
[source,terminal]
----
$ hcp create nodepool aws \
  --cluster-name <hosted_cluster_name> \// <1>
  --name <nodepool_name> \// <2>
  --node-count=<node_count> \// <3>
  --arch amd64
----
<1> Replace `<hosted_cluster_name>` with your hosted cluster name.
<2> Replace `<nodepool_name>` with your node pool name.
<3> Replace `<node_count>` with integer for your node count, for example, `2`.

.Verification

* Verify that a node pool is using the multi-architecture release image by entering the following command:
+
[source,terminal]
----
$ oc get nodepool/<nodepool_name> -oyaml
----
+
.Example output for 64-bit AMD node pools
[source,yaml]
----
#...
spec:
  arch: amd64
#...
  release:
    image: quay.io/openshift-release-dev/ocp-release:<4.x.y>-multi <1>
----
<1> Replace `<4.y.z>` with the supported OpenShift Container Platform version that you use.
+
.Example output for 64-bit ARM node pools
[source,yaml]
----
#...
spec:
  arch: arm64
#...
  release:
    image: quay.io/openshift-release-dev/ocp-release:<4.x.y>-multi
----

//Module included in the following assemblies:
// hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-aws-tags_{context}"]
= Adding or updating {aws-short} tags for a hosted cluster

As a cluster instance administrator, you can add or update {aws-first} tags without needing to re-create your hosted cluster. _Tags_ are key-value pairs that are attached to {aws-short} resources for management and automation.

You might want to use tags for the following purposes:

* Managing access controls.
* Tracking chargeback or showback.
* Managing cloud IAM conditional permissions.
* Aggregating resources based on tags. For example, you can query tags to calculate resource usage and billing costs.

You can add or update tags for several different types of resources, including EFS access points, load balancer resources, Amazon EBS volumes, IAM users, and {aws-short} S3.

[IMPORTANT]
====
On network load balancers, tags cannot be added or updated. The {aws-short} load balancer reconciles whatever tags are in the `HostedCluster` resource. If you try to add or update a tag, the load balancer overwrites the tag.

In addition, tags cannot be updated on the default security group resource that is created directly by {hcp}.
====

.Prerequisites

* You must have cluster administrator permissions for your hosted cluster on {aws-short}.

.Procedure

. If you want to add or update tags for EFS access points, complete steps 1 and 2. If you are adding or updating tags for other types of resources, complete only step 2.

.. In the `aws-efs-csi-driver-operator` service account, add two annotations, as shown in the following example. These annotations are required so that the {aws-short} EKS pod identity webhook that runs on the cluster can correctly assign {aws-short} roles to the pods that the EFS Operator uses.
+
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <service_account_name>
  namespace: <project_name>
  annotations:
    eks.amazonaws.com/role-arn:<role_arn>
    eks.amazonaws.com/audience:sts.amazonaws.com
----

.. Delete the Operator pod or roll out a restart of the `aws-efs-csi-driver-operator` deployment.

. In the `HostedCluster` resource, enter information in the `resourceTags` fields, as shown in the following example:
+
.Example `HostedCluster` resource
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  #...
spec:
  autoscaling: {}
  clusterID: <cluster_id>
  configuration: {}
  controllerAvailabilityPolicy: SingleReplica
  dns:
    #...
  etcd:
    #...
  fips: false
  infraID: <infra_id>
  infrastructureAvailabilityPolicy: SingleReplica
  issuerURL: https://<issuer_url>.s3.<region>.amazonaws.com
  networking:
    #...
  olmCatalogPlacement: management
  platform:
    aws:
      #...
      resourceTags:
      - key: kubernetes.io/cluster/<tag> #<1>
        value: owned
      rolesRef:
        #...
    type: AWS
----

<1> Specify the tag that you want to add to your resource.

// Module included in the following assemblies:
// hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-np-capacity-blocks_{context}"]
= Configuring node pool capacity blocks on {aws-short}

After creating a hosted cluster, you can configure node pool capacity blocks for graphics processing unit (GPU) reservations on {aws-first}.

.Procedure

. Create GPU reservations on {aws-short} by running the following command:
+
[IMPORTANT]
====
The zone of the GPU reservation must match your hosted cluster zone.
====
+
[source,terminal]
----
$ aws ec2 describe-capacity-block-offerings \
      --instance-type "p4d.24xlarge"\ #<1>
      --instance-count  "1" \ #<2>
      --start-date-range "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"  \ #<3>
      --end-date-range "$(date -u -d "2 day" +"%Y-%m-%dT%H:%M:%SZ")" \ #<4>
      --capacity-duration-hours 24 \ #<5>
      --output json
----
<1> Defines the type of your {aws-short} instance, for example, `p4d.24xlarge`.
<2> Defines your instance purchase quantity, for example, `1`. Valid values are integers ranging from `1` to `64`.
<3> Defines the start date range, for example, `2025-07-21T10:14:39Z`.
<4> Defines the end date range, for example, `2025-07-22T10:16:36Z`.
<5> Defines the duration of capacity blocks in hours, for example, `24`.

. Purchase the minimum fee capacity block by running the following command:
+
[source,terminal]
----
$ aws ec2 purchase-capacity-block \
      --capacity-block-offering-id "${MIN_FEE_ID}" \ #<1>
      --instance-platform "Linux/UNIX"\ #<2>
      --tag-specifications 'ResourceType=capacity-reservation,Tags=[{Key=usage-cluster-type,Value=hypershift-hosted}]' \ #<3>
      --output json   > "${CR_OUTPUT_FILE}"
----
<1> Defines the ID of the capacity block offering.
<2> Defines the platform of your instance.
<3> Defines the tag for your instance.

. Create an environment variable to set the capacity reservation ID by running the following command:
+
[source,terminal]
----
$ CB_RESERVATION_ID=$(jq -r '.CapacityReservation.CapacityReservationId' "${CR_OUTPUT_FILE}")
----
+
Wait for a couple of minutes for the GPU reservation to become available.

. Add a node pool to use the GPU reservation by running the following command:
+
[source,terminal]
----
$ hcp create nodepool aws \
  --cluster-name <hosted_cluster_name> \ #<1>
  --name <node_pool_name> \ #<2>
  --node-count 1 \ #<3>
  --instance-type p4d.24xlarge \ #<4>
  --arch amd64 \ #<5>
  --release-image <release_image> \ #<6>
  --render > /tmp/np.yaml
----
<1> Replace `<hosted_cluster_name>` with the name of your hosted cluster.
<2> Replace `<node_pool_name>` with the name of your node pool.
<3> Defines the node pool count, for example, `1`.
<4> Defines the instance type, for example, `p4d.24xlarge`.
<5> Defines an architecture type, for example, `amd64`.
<6> Replace `<release_image>` with the release image you want to use.

. Add the `capacityReservation` setting in your `NodePool` resource by using the following example configuration:
+
[source,yaml]
----
# ...
spec:
  arch: amd64
  clusterName: cb-np-hcp
  management:
    autoRepair: false
    upgradeType: Replace
  platform:
    aws:
      instanceProfile: cb-np-hcp-dqppw-worker
      instanceType: p4d.24xlarge
      rootVolume:
        size: 120
        type: gp3
      subnet:
        id: subnet-00000
      placement:
        capacityReservation:
          id: ${CB_RESERVATION_ID}
          marketType: CapacityBlocks
    type: AWS
# ...
----

. Apply the node pool configuration by running the following command:
+
[source,terminal]
----
$ oc apply -f /tmp/np.yaml
----

.Verification

. Verify that your new node pool is created successfully by running the following command:
+
[source,terminal]
----
$ oc get np -n clusters
----
+
.Example output
[source,terminal]
----
NAMESPACE   NAME    CLUSTER     DESIRED NODES   CURRENT  NODES   AUTOSCALING     AUTOREPAIR   VERSION                               UPDATINGVERSION   UPDATINGCONFIG   MESSAGE
clusters    cb-np   cb-np-hcp   1               1                False           False        4.22.0-0.nightly-2025-06-05-224220    False             False
----

. Verify that your new compute nodes are created in the hosted cluster by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source, terminal]
----
NAME                           STATUS   ROLES    AGE    VERSION
ip-10-0-132-74.ec2.internal    Ready    worker   17m    v1.35.4
ip-10-0-134-183.ec2.internal   Ready    worker   4h5m   v1.35.4
----

// Module included in the following assemblies:
// hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-np-capacity-blocks-destroy_{context}"]
= Destroying a hosted cluster after configuring node pool capacity blocks

After you configured node pool capacity blocks, you can optionally destroy a hosted cluster and uninstall the HyperShift Operator.

.Procedure

. To destroy a hosted cluster, run the following example command:
+
[source,terminal]
----
$ hcp destroy cluster aws \
  --name cb-np-hcp \
  --aws-creds $HOME/.aws/credentials \
  --namespace clusters \
  --region us-east-2
----

. To uninstall the HyperShift Operator, run the following command:
+
[source,terminal]
----
$ hcp install render --format=yaml | oc delete -f -
----

// Module included in the following assemblies:
// hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-aws-spot-instance_{context}"]
= Amazon Spot Instance support for node pools

[role="_abstract"]
To reduce cloud infrastructure costs for non-critical and fault-tolerant workloads, you can use Amazon Spot Instances for your compute nodes in hosted clusters.

Spot Instances use spare Amazon Elastic Compute Cloud (Amazon EC2) capacity at reduced prices compared to on-demand instances. When Amazon EC2 needs the capacity block, it can interrupt a Spot Instance with a 2-minute warning. You can use Spot Instances for node pools in hosted clusters on {aws-short}. However, you cannot combine Spot Instances with Amazon EC2 Capacity Reservations.

[IMPORTANT]
====
Spot Instances are suitable for fault-tolerant, stateless, and flexible workloads. Do not use Spot Instances for workloads that cannot tolerate interruptions. Spot Instances require default tenancy. Dedicated tenancy is not supported.
====

// Module included in the following assemblies:
// hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-aws-config-sqs-eventbridge_{context}"]
= Configuring Amazon SQS and Amazon EventBridge to receive Amazon EC2 interruption events

[role="_abstract"]
Before you enable Amazon Spot Instances, you must set up Amazon Simple Queue Service (SQS) and Amazon EventBridge to receive Amazon EC2 interruption events.

For {hcp} to be able to provide a graceful shut down, it needs to poll the SQS queue and cordon or drain nodes before they are deleted. For more information about Amazon SQS and Amazon EventBridge, see "Getting started with Amazon SQS" and "Getting started: Create an Amazon EventBridge bus rule".

.Procedure

. Create an Amazon SQS queue to receive Spot Instance notifications by entering the following command:
+
[source,terminal]
----
CLUSTER_NAME="my-cluster"
AWS_REGION="us-east-1"

$ aws sqs create-queue \
  --queue-name "${CLUSTER_NAME}-spot-interruption-queue" \
  --region "${AWS_REGION}"
----
+
** Be sure to replace `my-cluster` and `us-east-1` with your cluster name and {aws-short} region.
** Take note of the URL from the output. You need the URL when you create the hosted cluster.

. Create Amazon EventBridge rules to route Amazon EC2 Spot interruption warnings and rebalance recommendations to the SQS queue.
+
.. Set the attributes by entering the following command:
+
[source,terminal]
----
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
QUEUE_URL="https://sqs.${AWS_REGION}.amazonaws.com/${ACCOUNT_ID}/${CLUSTER_NAME}-spot-interruption-queue"

QUEUE_ARN=$(aws sqs get-queue-attributes \
  --queue-url "${QUEUE_URL}" \
  --attribute-names QueueArn \
  --query 'Attributes.QueueArn' --output text)
----
+
.. Set the interruption warning by entering the following command:
+
[source,terminal]
----
$ aws events put-rule \
  --name "${CLUSTER_NAME}-spot-interruption-warning" \
  --event-pattern '{"source":["aws.ec2"],"detail-type":["EC2 Spot Instance Interruption Warning"]}' \
  --region "${AWS_REGION}"
----
+
.. Set the target for the interruption warning by entering the following command:
+
[source,terminal]
----
$ aws events put-targets \
  --rule "${CLUSTER_NAME}-spot-interruption-warning" \
  --targets "Id=1,Arn=${QUEUE_ARN}" \
  --region "${AWS_REGION}"
----
+
.. Set the recommendations by entering the following command:
+
[source,terminal]
----
$ aws events put-rule \
  --name "${CLUSTER_NAME}-rebalance-recommendation" \
  --event-pattern '{"source":["aws.ec2"],"detail-type":["EC2 Instance Rebalance Recommendation"]}' \
  --region "${AWS_REGION}"
----
+
.. Set the target for the recommendations by entering the following command:
+
[source,terminal]
----
$ aws events put-targets \
  --rule "${CLUSTER_NAME}-rebalance-recommendation" \
  --targets "Id=1,Arn=${QUEUE_ARN}" \
  --region "${AWS_REGION}"
----

. Configure the Amazon SQS queue policy to allow EventBridge to send messages to the queue by entering the following command:
+
[source,terminal]
----
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
QUEUE_URL="https://sqs.${AWS_REGION}.amazonaws.com/${ACCOUNT_ID}/${CLUSTER_NAME}-spot-interruption-queue"

$ aws sqs set-queue-attributes \
  --queue-url "${QUEUE_URL}" \
  --attributes '{
    "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"events.amazonaws.com\"},\"Action\":\"sqs:SendMessage\",\"Resource\":\"'${QUEUE_ARN}'\"}]}"
  }'
----

[role="_additional-resources"]
.Additional resources

* Getting started with Amazon SQS
* Getting started: Create an Amazon EventBridge event bus rule

// Module included in the following assemblies:
// hosted_control_planes/hcp-manage/hcp-manage-aws.adoc

[id="hcp-aws-spot-instance-enable_{context}"]
= Enabling Amazon Spot Instance support for node pools

[role="_abstract"]
Enable Amazon Spot Instances for your compute nodes in hosted cluster node pools to reduce cloud infrastructure costs for non-critical and fault-tolerant workloads.

.Prerequisites

* You set up Amazon Simple Queue Service (SQS) and Amazon EventBridge to receive Amazon EC2 interruption events.

* You have the URL of your Amazon SQS queue, which you created in "Configuring Amazon SQS and Amazon EventBridge to receive Amazon EC2 interruption events".

.Procedure

. Set the Amazon SQS queue URL on your hosted cluster.

** If you are setting the SQS queue URL on a new hosted cluster, take the following steps:

... Configure the `HostedCluster` resource as follows:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <my_hosted_cluster>
  namespace: <my_hosted_cluster_namespace>
spec:
  platform:
    type: AWS
    aws:
      region: us-east-1
      terminationHandlerQueueURL: "https://sqs.us-east-1.amazonaws.com/123456789012/my-cluster-spot-interruption-queue"
...
----
+
where:
+
`spec.platform.aws.terminationHandlerQueueURL`:: Specifies the SQS queue URL.

... Apply the configuration by entering the following command:
+
[source,terminal]
----
$ oc apply -f <hosted_cluster_config>.yaml
----

** If you are setting the SQS queue URL on an existing hosted cluster, patch the `HostedCluster` resource as follows:
+
[source,terminal]
----
$ oc patch hostedcluster my-cluster -n clusters --type merge -p '{
  "spec": {
    "platform": {
      "aws": {
        "terminationHandlerQueueURL": "https://sqs.us-east-1.amazonaws.com/123456789012/my-cluster-spot-interruption-queue"
      }
    }
  }
}'
----

. Create a `NodePool` object that has the Spot market type configured, as shown in the following example:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: NodePool
metadata:
  name: spot-workers
  namespace: <my_hosted_cluster_namespace>
spec:
  clusterName: <my_hosted_cluster>
  replicas: 3
  release:
    image: quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64
  management:
    autoRepair: true
    upgradeType: Replace
  platform:
    type: AWS
    aws:
      instanceType: m5.xlarge
      instanceProfile: my-cluster-worker
      rootVolume:
        size: 120
        type: gp3
      placement:
        marketType: Spot
----
+
`marketType: Spot`:: Specifies that all `Machine` objects and `Node` objects have the `hypershift.openshift.io/interruptible-instance` label and that the EC2 instances have the `aws-node-termination-handler/managed` tag so they can be identified by the termination-handling components. You can specify `spot` options only when the `marketType` field is set to `Spot`.

. Apply the configuration by entering the following command:
+
[source,terminal]
----
$ oc apply -f <node_pool_config>.yaml
----
