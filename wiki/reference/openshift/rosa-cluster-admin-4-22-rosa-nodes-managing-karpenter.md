---
title: "Manage compute nodes using {autonode}"
type: reference
domain: openshift
slug: rosa-cluster-admin-4-22-rosa-nodes-managing-karpenter
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_cluster_admin/rosa-nodes-managing-karpenter
version: 4.22
family: rosa_cluster_admin
documentKind: "Documentation"
---

# Manage compute nodes using {autonode}

[id="rosa-nodes-autonode-managing"]
= Manage compute nodes using {autonode}

[role="_abstract"]
{autonode} provisions compute nodes automatically based on workload demand. By automatically provisioning your nodes, {autonode} helps improve cluster efficiency and reduce costs.

== Prerequisites

* You have installed the {rosa-cli-first} version 1.2.61 or later.
* You have an {ocp-short} cluster version 4.22.0 or later.
* You have installed the `jq` CLI tool.
* You have installed the `curl` CLI tool.
* You have the required AWS Identity and Access Management (IAM) permissions to create policies and roles.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-nodes-managing-karpenter.adoc

[id="rosa-nodes-autonode-about_{context}"]
= About {autonode}

[role="_abstract"]
{autonode} builds on the open source Karpenter project and provides automatic node provisioning for OpenShift Container Platform clusters. Karpenter watches for pods that the Kubernetes scheduler marks as unschedulable and evaluates their scheduling constraints, including resource requests, node selectors, affinities, tolerations, and topology spread constraints. Karpenter then provisions nodes that meet the specific requirements of those waiting pods.

Karpenter improves cluster efficiency by provisioning nodes that match workload requirements instead of requiring pre-configured node pools. When nodes are no longer needed, Karpenter removes them to reduce costs. For more information about Karpenter capabilities and architecture, see _Karpenter project documentation_ in the Additional resources.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-nodes-managing-karpenter.adoc

[id="rosa-nodes-autonode-managing-setup_{context}"]
= Prepare an AWS IAM role for {autonode}

[role="_abstract"]
Create the IAM policy and role that {autonode} requires to provision Amazon Elastic Compute Cloud (Amazon EC2) instances.

This policy grants {autonode} the following permissions:

* Create and terminate EC2 instances and fleets
* Create and manage launch templates
* Tag resources with Karpenter-specific tags
* Describe EC2 resources such as instances, instance types, and subnets
* Access Systems Manager (SSM) parameters for Amazon Machine Image (AMI) information
* Query EC2 pricing information
* Manage Simple Queue Service (SQS) interruption queues for Spot instance handling
* Create and manage IAM instance profiles
+
[NOTE]
====
All permissions are restricted to resources tagged with Karpenter-specific tags to ensure {autonode} manages only nodes that it provisions.
====

.Procedure

. Download the latest {autonode} IAM policy:
+
[source,terminal]
----
$ curl -o autonode-policy.json https://raw.githubusercontent.com/openshift/managed-cluster-config/refs/heads/master/resources/sts/hypershift/openshift_hcp_karpenter_controller_credentials_policy.json
----

. Export your cluster name and ID to environment variables:
+
[source,terminal,subs="+quotes"]
----
$ export CLUSTER_NAME=<cluster_name>
$ export CLUSTER_ID=$(rosa describe cluster -c "$CLUSTER_NAME" -o json | jq -r '.id')
$ echo $CLUSTER_NAME $CLUSTER_ID
----

. Create the IAM policy:
+
[source,terminal]
----
$ POLICY_ARN=$(aws iam create-policy \
  --policy-name rosa-karpenter-controller-role-${CLUSTER_NAME} \
  --policy-document file://autonode-policy.json \
  --query 'Policy.Arn' \
  --output text)
----

. Create the trust policy for the Karpenter service account:
+
[source,terminal]
----
$ cat > trust-policy.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):oidc-provider/$(rosa describe cluster -c $CLUSTER_NAME -o json | jq -r .aws.sts.oidc_endpoint_url | sed 's|https://||')"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "$(rosa describe cluster -c $CLUSTER_NAME -o json | jq -r .aws.sts.oidc_endpoint_url | sed 's|https://||'):sub": "system:serviceaccount:kube-system:karpenter"
                }
            }
        }
    ]
}
EOF
----

. Create the IAM role and attach the policy:
+
[source,terminal]
----
$ ROLE_ARN=$(aws iam create-role \
  --role-name rosa-karpenter-controller-role-${CLUSTER_NAME} \
  --assume-role-policy-document file://trust-policy.json \
  --query 'Role.Arn' \
  --output text)

$ aws iam attach-role-policy \
  --role-name rosa-karpenter-controller-role-${CLUSTER_NAME} \
  --policy-arn $POLICY_ARN
----
+

.Verification

Verify that policies are present by running:
[source,terminal]
----
$ aws iam list-attached-role-policies --role-name rosa-karpenter-controller-role-${CLUSTER_NAME}
----

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-nodes-managing-karpenter.adoc

[id="rosa-nodes-autonode-managing-tagging-setup_{context}"]
= Tag your AWS resources for {autonode}

[role="_abstract"]
Create the necessary AWS tags so that {autonode} discovers the security group to use when provisioning nodes. Tag the security group for the cluster that was created during cluster installation.

.Procedure

. Export your cluster name and ID to environment variables:
+
[source,terminal,subs="+quotes"]
----
$ export CLUSTER_NAME=<cluster_name>
$ export AWS_REGION=us-east-2
$ export CLUSTER_ID=$(rosa describe cluster -c "$CLUSTER_NAME" -o json | jq -r '.id')
$ echo $CLUSTER_NAME $CLUSTER_ID
----
+
[IMPORTANT]
====
Ensure that your AWS client is using the region where your cluster is deployed. In this example, `us-east-2` is used.
====

. Find your cluster's security group by running the following command:
+
[source,terminal]
----
$ SECURITY_GROUP_ID=$(aws ec2 describe-security-groups --filters "Name=tag:Name,Values=$CLUSTER_ID-default-sg" | jq -r .SecurityGroups[0].GroupId)
----

. Tag the security group with the {autonode} auto-discovery tags by running the following command:
+
[source,terminal]
----
$ aws ec2 create-tags --resources "$SECURITY_GROUP_ID" --tags Key="karpenter.sh/discovery",Value="$CLUSTER_ID"
----

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-nodes-managing-karpenter.adoc

[id="rosa-nodes-autonode-managing-enable-cli_{context}"]
= Enable {autonode} using {rosa-cli}

[role="_abstract"]
Enable {autonode} on your cluster by using {rosa-cli-first} after it finishes installing.

.Procedure

. Export your cluster name and ID to environment variables:
+
[source,terminal,subs="+quotes"]
----
$ export CLUSTER_NAME=<cluster_name>
$ export CLUSTER_ID=$(rosa describe cluster -c "$CLUSTER_NAME" -o json | jq -r '.id')
$ echo $CLUSTER_NAME $CLUSTER_ID
----

. Wait for the cluster to become ready:
+
[source,terminal]
----
$ rosa describe cluster -c $CLUSTER_ID | grep -i State
----
+
*Example output*
+
[source,terminal]
----
State:                      ready
----

. Ensure that your {autonode} IAM role is correctly set:
+
[source,terminal]
----
$ ROLE_ARN=$(aws iam get-role --role-name rosa-karpenter-controller-role-${CLUSTER_NAME} --query 'Role.Arn' --output text)
----

. Enable {autonode}:
+
[source,terminal]
----
$ rosa edit cluster -c $CLUSTER_ID \
  --autonode=enabled \
  --autonode-iam-role-arn=$ROLE_ARN
----

. If you do not already have cluster admin access, create a cluster admin user:
+
[source,terminal]
----
$ rosa create admin -c $CLUSTER_ID
----

. Log in to the cluster using the credentials from the previous command:
+
[source,terminal]
----
$ oc login <api_url> --username cluster-admin --password <password>
----

. Verify that the {autonode} custom resource definitions (CRDs) are present:
+
[source,terminal]
----
$ oc get ec2nodeclass
----
+
[NOTE]
====
The node pool manifest uses the `EC2NodeClass` resource.
====
+
*Example output*
+
[source,terminal]
----
NAME      READY   AGE
default   True    5m
----
+
[source,terminal]
----
$ oc get openshiftec2nodeclass
----
+
[NOTE]
====
The `OpenShiftEC2NodeClass` resource is Red{nbsp}Hat's wrapper to communicate with the `EC2NodeClass` resource.
====
+
*Example output*
+
[source,terminal]
----
NAME      READY
default   True
----

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-nodes-managing-karpenter.adoc

[id="rosa-nodes-autonode-managing-enable-ui_{context}"]
= Enable {autonode} using {cluster-manager}

[role="_abstract"]
Enable {autonode} on your cluster by using {cluster-manager} after it finishes installing.

.Prerequisites
* You have created a OpenShift Container Platform cluster, version 4.22.0 or later.
* You have created an AWS Identity and Access Management (IAM) role to be configured for {autonode}.
* You have your cluster's Open ID Connect (OIDC) Endpoint URL.
+
[NOTE]
====
Run `rosa describe cluster -c $CLUSTER_NAME | grep "OIDC Endpoint URL"` to see this URL. Do not include the `https://` prefix from the OIDC Endpoint URL. For example, use  `example-oidc-endpoint.cloudfront.net/abcd1234examplehash5678` instead of `https://example-oidc-endpoint.cloudfront.net/abcd1234examplehash5678`.
====
* You have the proper credentials to access the AWS console.

.Procedure

. Export your AWS ID:
+
[source,terminal]
----
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
----

. Log in to the AWS console.
. In the AWS console, navigate to **IAM > Roles**.
. On your {autonode} Amazon Resource Name (ARN), update the trust policy to include the following policy specifications:
+
[NOTE]
====
To access this ARN, run:

[source,terminal]
----
$ echo $ROLE_ARN
----
====
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::<aws_account_id>:oidc-provider/<oidc-endpoint-url>"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "<oidc-endpoint-url>:sub": "system:serviceaccount:kube-system:karpenter"
                }
            }
        }
    ]
}
----
where:
<aws_account_id>::
Specifies your AWS Account ID.
<oidc-endpoint-url>::
Specifies the OIDC endpoint URL that you acquired.

. In {cluster-manager-url}, select your cluster from the cluster list.
. On the cluster details screen, select the *Edit* button next to the status for {autonode}.
. On the *Edit Autonode settings* dialog box, toggle *Enable Autonode*.
. Add your {autonode} IAM role ARN to the field in this dialog box.
. Select *Save* to save your configurations and close the *Edit Autonode settings* box.

// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa-nodes-managing-karpenter.adoc

[id="rosa-nodes-autonode-managing-nodepool_{context}"]
= Create a node pool

[role="_abstract"]
Create a node pool to define the compute capacity that {autonode} can provision.

.Procedure

. Create a node pool manifest:
+
[source,terminal]
----
$ cat > nodepool.yaml <<'EOF'
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default-np
spec:
  template:
    metadata:
      labels:
        autonode: "true"
    spec:
      requirements:
      - key: node.kubernetes.io/instance-type
        operator: In
        values:
        - c5.xlarge
      - key: karpenter.sh/capacity-type
        operator: In
        values: ["on-demand"]
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default
EOF
----
where:
`nodeClassRef.kind`::
Required field that must use the `EC2NodeClass` type.
`spec.labels`::
Optional field that you can use to place pods by using labels.
+
[NOTE]
====
For a list of all requirements available under `spec.requirements`, see the _Additional resources_.
====

. Apply the node pool:
+
[source,terminal]
----
$ oc apply -f nodepool.yaml
----

. Verify the node pool is ready:
+
[source,terminal]
----
$ oc get nodepool
----
+
*Example output*
+
[source,terminal]
----
NAME         NODECLASS   NODES   READY   AGE
default-np   default     0       True    3s
----

[role="_additional-resources"]
.Additional resources

* Karpenter project documentation
* `NodePools` reference
* Identity providers overview
* Update options for OpenShift Container Platform clusters configured with {autonode}
