---
title: "Forwarding control plane logs"
type: reference
domain: openshift
slug: observability-4-22-rosa-forwarding-control-plane-logs
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/rosa-forwarding-control-plane-logs
version: 4.22
family: observability
documentKind: "Documentation"
---

# Forwarding control plane logs

[id="rosa-forwarding-control-plane-logs"]
= Forwarding control plane logs

[role="_abstract"]
OpenShift Container Platform provides a control plane log forwarder that is a separate system outside your cluster. You can use the control plane log forwarder to send your logs to either an Amazon CloudWatch group or Amazon S3 bucket.

The OpenShift Container Platform control plane log forwarder is a managed system and it does not use resources reserved for workloads on your worker nodes.

// Module included in the following assemblies:
//
// * observability/logging/rosa-configuring-the-log-forwarder.adoc
[id="rosa-determine-log-groups_{context}"]
= Determining what log groups to use

[role="_abstract"]
When you forward control plane logs to Amazon CloudWatch or S3, you must decide on what log groups you want to use. Because of the existing AWS pricing for the respective services, you can expect additional costs associated with forwarding and storing your logs in S3 and CloudWatch. When you determine what log group to use, consider these additional costs along with other factors, such as your log retention requirements.

For each log group, you have access to different applications, and these applications can change depending on what you choose to enable and disable with your logs.

When you forward log groups, you must specify a group or application. When you specify a group, the log forwarder collects all the applications in that group. Instead of selecting a group, you can select individual applications. When you set up your log forwarder, you must specify at least one group or application, but you do not need to specify both.

The following table lists available log groups:

.Log groups
[cols="1,2,2",options="header"]
|====
| Log group name| Benefit of that log group| Example applications available for that log group

| api
| Records every request made to the cluster. Supports security by detecting unauthorized access attempts.
a|
* `audit-webhook`
* `kube-apiserver`
* `oauth-openshift`
* `openshift-apiserver`
* `openshift-oauth-apiserver`
* `packageserver`
* `validation-webhook`

| authentication
| Tracks login attempts and requests for tokens. Supports security by recording authenticated user information.
a|
* `ignition-server`
* `konnectivity-agent`

| controller manager
| Monitors the controllers that manage the state of your clusters. Clarifies differences among the different cluster states, for example, the `Current`, `Desired`, `Health`, and `Feature` state.
a|
* `aws-ebs-csi-driver-controller`
* `capi-provider-controller-manager`
* `catalog-operator`
* `cloud-controller-manager`
* `cloud-credential-operator`
* `cloud-network-config-controller`
* `cluster-network-operator`
* `cluster-node-tuning-operator`
* `cluster-policy-controller`
* `cluster-version-operator`
* `control-plane-operator`
* `control-plane-pki-operator`
* `csi-snapshot-controller-operator`
* `csi-snapshot-controller`
* `dns-operator`
* `hosted-cluster-config-operator`
* `ingress-operator`
* `kube-controller-manager`
* `machine-approver`
* `multus-admission-controller`
* `network-node-identity`
* `olm-operator`
* `openshift-controller-manager`
* `openshift-route-controller-manager`
* `ovnkube-control-plane`

| scheduler
| Records the placement of each pod on every node. Shows why pods are in a `Running` or `Pending` state.
a|
* `kube-scheduler`

| not applicable
| These applications do not belong to a defined log group. To forward their logs, set these applications in the `applications` array.
a|
* `certified-operators-catalog`
* `cluster-api`
* `community-operators-catalog`
* `etcd`
* `private-router`
* `redhat-marketplace-catalog`
* `redhat-operators-catalog`
|====

// Module included in the following assemblies:
//
// * observability/logging/rosa-forwarding-control-plane-logs.adoc
[id="rosa-create-an-iam-role-policy_{context}"]
= Creating an IAM role and policy

[role="_abstract"]
When you forward your logs to an Amazon CloudWatch group or S3 bucket, those locations exist outside your control plane. You must create an Identity and Access Management (IAM) role and policy so that your log forwarder has the right permissions and capabilities to send these logs to your chosen destination, CloudWatch, or S3.

[NOTE]
====
* To use a CloudWatch group, you must create an IAM role and policy.
* To use an S3 bucket, you do not need an IAM role and policy.
* The only supported Amazon S3-managed encryption method is `SSE-S3`.
====

.Prerequisites

* You have ensured that the name of you your IAM role has the prefix, `arn:aws:iam::*:role/CustomerLogDistribution-*`.
* You have installed and configured the latest {rosa-cli-first} on your installation host.
* You have installed and configured the latest {aws-first} command-line interface (CLI) on your installation host.

.Procedure

. To enable the log forwarder delivery capability, prepare the IAM policy by creating an `assume-role-policy.json` file. Apply the following IAM policy sample:
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::859037107838:role/ROSA-CentralLogDistributionRole-241c1a86"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
----
+
. To enable the log forwarder distribution capability, create an IAM role that must include the `CustomerLogDistribution` name by running the following command:
+
[source,terminal]
----
$ aws iam create-role \
    --role-name CustomerLogDistribution-RH \
    --assume-role-policy-document file://assume-role-policy.json
----

.Next steps

After you create an IAM role and policy, you must decide to send your control plane logs to either a CloudWatch log group, an S3 bucket, or both. See the following summary about CloudWatch and S3 to help you decide what you want to do:

* Use CloudWatch for logs requiring immediate action or organization.
* Use S3 for logs requiring long-term storage or large-scale data analysis.

// Module included in the following assemblies:
//
// * observability/logging/rosa-forwarding-control-plane-logs.adoc
[id="rosa-set-up-cloudwatch-log-group_{context}"]
= Setting up the CloudWatch log group

[role="_abstract"]
If you have logs that require immediate action or organization, set up an Amazon CloudWatch log group.

.Prerequisites

* You have created an IAM role and policy.
* You have ensured that the name of you your IAM role has the prefix, `CustomerLogDistribution`.

.Procedure

. Create the CloudWatch log group by running the following command:
+
[source,terminal]
----
$ aws logs create-log-group --log-group-name <your_log_group_name>
----
+
. In your OpenShift Container Platform cluster, configure the log forwarder to use the CloudWatch log group by applying the following JSON sample:
+
[source,json]
----
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CreatePutLogs",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "<your_log_group_arn>:*"
        },
        {
            "Sid": "DescribeLogs",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
            ],
            "Resource": "*"
        }
    ]
}
----
+
. Attach the policy to the CloudWatch role by running the following command:
+
[source,terminal]
----
$ aws iam put-role-policy \
    --role-name CustomerLogDistribution-RH \
    --policy-name Allow-CloudWatch-Writes \
    --policy-document file://cloudwatch-policy.json
----
+
. Configure your OpenShift Container Platform cluster to forward logs to the CloudWatch log group by applying the following sample YAML list. Specify an application, or group, or both:
+
[source,yaml]
----
cloudwatch:
  cloudwatch_log_role_arn: "arn:aws:iam::123456789012:role/RosaCloudWatch"
  cloudwatch_log_group_name: "rosa-logs"
  applications:
    - "<example_app1>"
  groups:
    - "<example_group1>"
----
+
where:

<example_app1>:: Add one or more applications. For a list of applications, see the table in "Determining what log groups to use".
<example_group1>:: Add one or more of the following groups: `api`, `authentication`, `controller manager`, `scheduler`.

. Enable the log forwarder to send logs to your OpenShift Container Platform cluster.
.. To enable control plane log forwarding on a new cluster, include the log forwarding configuration by running the following command:
+
[source,terminal]
----
$ rosa create cluster --log-fwd-config="<path_to_file>.yaml"
----
+
.. To enable control plane log forwarding on an existing cluster, include the log forwarding configuration by running the following command:
+
[source,terminal]
----
$ rosa create log-forwarder -c <cluster> --log-fwd-config="<path_to_file>.yaml" -o yaml
----
. Optional: For an example for forwarding logs to the CloudWatch log group, apply the following sample YAML:
+
[source,yaml]
----
cloudwatch:
  cloudwatch_log_role_arn: "cloudwatch-log-role-arn"
  cloudwatch_log_group_name: "cloudwatch-group-name"
  applications:
    - "<example_app1>"
  groups:
    - "<example_group1>"
----

// Module included in the following assemblies:
//
// * observability/logging/rosa-forwarding-control-plane-logs.adoc
[id="rosa-set-up-s3-bucket_{context}"]
= Setting up the S3 bucket

[role="_abstract"]
If you have logs that need long-term storage or large-scale data analysis, set up an Amazon S3 bucket.

.Prerequisites

* If you want to prevent limitations for the managed keys for your S3 bucket, you must have created an IAM role and policy.
* You have ensured that the name of you your IAM role has the prefix, `CustomerLogDistribution`.

.Procedure

. Create the S3 bucket by running the following command:
+
[source,terminal]
----
$ aws s3api create-bucket \
    --bucket <your_s3_bucket_name> \
    --region <your_aws_region> \
    --create-bucket-configuration LocationConstraint=<cluster_aws_region>
----
+
. Configure the policy for the S3 bucket by applying the following S3 bucket policy sample:
+
[source,json]
----
 "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCentralLogDistributionWrite",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::859037107838:role/ROSA-CentralLogDistributionRole-241c1a86"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<your_s3_bucket_name>/*",
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-acl": "bucket-owner-full-control"
                }
            }
        }
    ]
}
----
+
. Attach the policy to the S3 role by running the following command:
+
[source,terminal]
----
$ aws s3api put-bucket-policy \
    --bucket <your_s3_bucket_name> \
    --policy file://s3-bucket-policy.json
----
+
. Configure your OpenShift Container Platform cluster to forward logs to the S3 bucket by applying the following sample YAML list. Specify an application, or group, or both:
+
[source,yaml]
----
s3:
  s3_config_bucket_name: "my-log-bucket"
  s3_config_bucket_prefix: "my-bucket-prefix"
  applications:
    - "<example_app1>"
  groups:
    - "<example_group1>"
----
<example_app1>:: Add one or more applications. For a list of applications, see the table in "Determining what log groups to use".
<example_group1>:: Add one or more of the following groups: `api`, `authentication`, `controller manager`, `scheduler`.
. Enable the log forwarder to send logs to your OpenShift Container Platform cluster.
.. To enable control plane log forwarding on a new cluster, include the log forwarding configuration by running the following command:
+
[source,terminal]
----
$ rosa create cluster --log-fwd-config="<path_to_file>.yaml"
----
+
.. To enable control plane log forwarding on an existing cluster, include the log forwarding configuration by running the following command:
+
[source,terminal]
----
$ rosa create log-forwarder -c <cluster> --log-fwd-config="<path_to_file>.yaml" -o yaml
----
+
. Optional: For an example for forwarding logs to the S3 bucket, apply the following sample YAML:
+
[source,yaml]
----
s3:
  s3_config_bucket_name: "s3-bucket-name"
  s3_config_bucket_prefix: "s3-bucket-prefix"
  groups:
    - "<example_group1>"
----

// Module included in the following assemblies:
//
// * observability/logging/rosa-configuring-the-log-forwarder.adoc
[id="rosa-manage-control-plane-log-forwarding_{context}"]
= Managing control plane log forwarding

[role="_abstract"]
After you configure the OpenShift Container Platform clusters to use your selected log forwarder for control plane logs, see the following commands to run based on your specific needs. For all of these commands, you must provide the `clusterid` or cluster name in the `--cluster` flag:

`rosa create log-forwarder -c <cluster_name|cluster_id>`:: Configures your OpenShift Container Platform cluster to use the log forwarder.
`rosa list log-forwarder -c <cluster_name|cluster_id>`:: Displays all of the log forwarder configurations for a OpenShift Container Platform cluster.
`rosa describe log-forwarder -c <cluster_name|cluster_id> <log_fwd_id>`:: Provides additional details for a specific log forwarder.
`rosa edit log-forwarder -c <cluster_name|cluster_id> <log_fwd_id>`:: Changes the following log forwarder fields: groups, applications, and S3 and CloudWatch configurations.
`rosa delete log-forwarder -c <cluster_name|cluster_id> <log_fwd_id>`:: Deletes the log forwarder configuration. Logs are no longer forwarded to your chosen destinations but are not automatically deleted. If you no longer want to store your logs in the S3 bucket or CloudWatch group, delete those logs.
+
Additionally, use this command to change the following log forwarder fields: ID, cluster ID, and the type for S3 and CloudWatch. Delete a log forwarder and re-create it with the updated values.

// Module included in the following assemblies:
//
// * observability/logging/rosa-configuring-the-log-forwarder.adoc
[id="rosa-create-cluster-ui-log-groups_{context}"]
= Creating a OpenShift Container Platform cluster in the {hybrid-console}

[role="_abstract"]
You can forward logs from your OpenShift Container Platform cluster to `CloudWatch`, `S3`, or both. When you forward your control plane logs, you can store them in the infrastructure that you designated, helping you meet compliance and audit requirements and workflows.

In the {hybrid-console}, you set up your OpenShift Container Platform cluster to forward control plane logs when you create the cluster. Then, you can continue to use the web user interface (UI) to forward your control plane logs.

Enable control plane log forwarding when you create the cluster to ensure a complete audit trail. If enabled later, the feature cannot capture logs generated before the activation, leaving gaps in your data.

// Module included in the following assemblies:
//
// * observability/logging/rosa-forwarding-control-plane-logs.adoc
[id="rosa-create-cluster-log-forwarding-ui_{context}"]
= Create a OpenShift Container Platform cluster with log forwarding

[role="_abstract"]
You can set up control plane log forwarding when you create your OpenShift Container Platform cluster in the {hybrid-console}. As you create your OpenShift Container Platform cluster, you have the option to forward your control plane logs to an Amazon `S3` bucket, `CloudWatch` log group, or both.

.Procedure

. In the {hybrid-console}, go to *Clusters* -> *Cluster List*, then click the *Create cluster* button.
. On the *Managed services* offerings page, go to the offering, *Red Hat OpenShift Service on AWS (ROSA)*, and click the *Create cluster* button, then select *With web interface*.
. For *Create a ROSA Cluster* -> *Control plane*, select your *ROSA hosted architecture*.
. For *Accounts and roles*, select your *Associated AWS infrastructure account* and *AWS billing account*.
. For the *Cluster settings* -> *Cluster details*, complete the following text boxes:
+
* *Region*
* *Cluster name*
* *Version*
* *Channel*

+
In about 20 minutes after you complete this information, your cluster is ready to install and you can continue to configure it.
. For *Machine pool* -> *Networking* -> *Configuration* -> *CIDR ranges* -> *Cluster roles and policies*, complete all of the required text boxes with the specifications that you want for your cluster.
. On the *Review and create* -> *Review your ROSA cluster* page, verify that the cluster details are correct.
. Optional: If you want to forward your control plane logs to an Amazon `S3` bucket or `CloudWatch` log group, complete the following instructions:
.. On the *Control plane log forwarding (optional)* page, click *Enable Amazon S3*, or *Enable CloudWatch*, or both.
.. If you enable Amazon `S3`, complete the following fields:
+
* *Bucket name*: Give it a unique identifier across all of {AWS}.
* *Bucket prefix*: Give it an optional path to organize your data.
* *Select groups and applications* (optional): When you select a group, the log forwarder collects all of the applications and related services from that group.
.. If you enable `CloudWatch`, complete the following fields:
+
* *Prerequisite*: Verify that you have created an `IAM` role and policy, then click the box stating that you have.
* *Log group name*: Give it a unique identifier.
* *Role ARN*: Give the `IAM` role ARN. For example, `arn:aws:iam::<12-digit-account-id>:role/<role-name>`.
* *Select groups and applications*: When you select a group, the log forwarder collects all the applications and related services from that group.
.. On the *Review and create* -> *Review your ROSA cluster* page, verify that the cluster details are correct.
.. Click the *Create cluster* button.
. If you want to finish completing your cluster with no designated log forwarding destination, click the *Create cluster* button.

.Verification

. In the {hybrid-console}, go to *Clusters* -> *Cluster List*.  You can see the name and status of your cluster.
. Verify that the status of your cluster is “Ready” and click the name of your cluster.
. In the *Overview* tab, verify that the details of your cluster are what you specified.
. Go to the *Control plane log forwarding* section.
.. If you enabled `Amazon S3`, verify that you see *Amazon S3: Enabled*. If you did not set it up, it shows, *Amazon S3: Disabled*.
.. If you enabled `CloudWatch`, verify that you see *CloudWatch: Enabled*. If you did not set it up, it shows, *CloudWatch: Disabled*.
. Click *View details*, which takes you to the *Settings* tab. Confirm all the specific details for your control plane log forwarding are correct.

// Module included in the following assemblies:
//
// * observability/logging/rosa-forwarding-control-plane-logs.adoc
[id="rosa-edit-cluster-log-forwarding-ui_{context}"]
= Edit a OpenShift Container Platform cluster with log forwarding

[role="_abstract"]
You can verify the status of log forwarding for a cluster and edit the log forwarding configurations.

.Procedure

. In the {hybrid-console}, go to *Clusters* -> *Cluster List*, then click the name of your cluster.
. Go to the *Settings* tab then the *Control plane log forwarding* section.
. To add to your log forwarding, click the *Add configuration* dropdown button.
.. You can add a `CloudWatch` or `Amazon S3` configuration.
. To make changes to your existing log forwarding, click the three dots within your `CloudWatch` or `Amazon S3` log forwarding configuration, then select *Edit configuration* or *Delete configuration*.
. When you click *Edit configuration* for `Amazon S3` log forwarding, you see your configuration and can make changes to the following:
* *Bucket Name*
* *Bucket Prefix*
* *Select groups and applications*
. When you click *Edit configuration* for `CloudWatch` log forwarding, you see your configuration and can make changes to the following:
* *Log group name*
* *Role ARN*
* *Select groups and applications*
. Make the changes to your configuration, then click *Save*.

.Verification

. In the *Settings* tab -> *Control plane log forwarding* section, verify that you see the changes you made to your configuration. The changes you made instantly go through and appear in this section.
