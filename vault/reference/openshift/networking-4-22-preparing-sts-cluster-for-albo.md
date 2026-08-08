---
title: "Preparing an AWS STS cluster for the AWS Load Balancer Operator"
type: reference
domain: openshift
slug: networking-4-22-preparing-sts-cluster-for-albo
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/preparing-sts-cluster-for-albo
version: 4.22
family: networking
documentKind: "Documentation"
---

# Preparing an AWS STS cluster for the AWS Load Balancer Operator

[id="albo-sts-cluster"]
= Preparing an AWS STS cluster for the AWS Load Balancer Operator

[role="_abstract"]
To install the {aws-first} Load Balancer Operator on a cluster that uses the {sts-first}, prepare the cluster by configuring the `CredentialsRequest` object. This ensures the Operator can bootstrap the {aws-short} Load Balancer Controller and access the required secrets.

The {aws-short} Load Balancer Operator waits until the required secrets are created and available.

Before you start any {sts-first} procedures, ensure that you meet the following prerequisites:

* You installed the {oc-first}.

* You know the infrastructure ID of your cluster. To show this ID, run the following command in your CLI:
+
[source,terminal]
----
$ oc get infrastructure cluster -o=jsonpath="{.status.infrastructureName}"
----

* You know the OpenID Connect (OIDC) DNS information for your cluster. To show this information, enter the following command in your CLI:
+
[source,terminal]
----
$ oc get authentication.config cluster -o=jsonpath="{.spec.serviceAccountIssuer}"
----
+
where:
+
`{.spec.serviceAccountIssuer}`:: Specifies an OIDC DNS URL. An example URL is `\https://rh-oidc.s3.us-east-1.amazonaws.com/28292va7ad7mr9r4he1fb09b14t59t4f`.

* You logged into the {aws-short} management console, navigated to *IAM* -> *Access management* -> *Identity providers*, and located the OIDC Amazon Resource Name (ARN) information. An OIDC ARN example is `arn:aws:iam::777777777777:oidc-provider/<oidc_dns_url>`.

[role="_additional-resources"]
.Additional resources

* the Cloud Credential Operator utility (`ccoctl`)

// The IAM role for the AWS Load Balancer Operator
// Module included in the following assemblies:
//
// * networking/networking_operators/preparing-sts-cluster-for-albo.adoc

[id="the-iam-role-albo-operator_{context}"]
= The IAM role for the AWS Load Balancer Operator

[role="_abstract"]
To install the {aws-first} Load Balancer Operator on a cluster by using {sts-short}, configure an additional Identity and Access Management (IAM) role.

You can create the IAM role by using the following options:

* Using the Cloud Credential Operator utility (`ccoctl`) and a predefined `CredentialsRequest` object.
* Using the {aws-short} CLI and predefined {aws-short} manifests.

Use the {aws-short} CLI if your environment does not support the `ccoctl` command.

// Creating an AWS IAM role by using the Cloud Credential Operator utility
// Module included in the following assemblies:
//
// * networking/networking_operators/preparing-sts-cluster-for-albo.adoc

[id="using-ccoctl-create-iam-role-alb-operator_{context}"]
= Creating an AWS IAM role by using the Cloud Credential Operator utility

[role="_abstract"]
To enable the {aws-short} Load Balancer Operator to interact with subnets and VPCs, create an {aws-short} IAM role by using the Cloud Credential Operator utility (`ccoctl`).

.Prerequisites

* You must extract and prepare the `ccoctl` binary.

.Procedure

. Download the `CredentialsRequest` custom resource (CR) and store it in a directory by running the following command:
+
[source,terminal]
----
$ curl --create-dirs -o <credentials_requests_dir>/operator.yaml https://raw.githubusercontent.com/openshift/aws-load-balancer-operator/main/hack/operator-credentials-request.yaml
----

. Use the `ccoctl` utility to create an {aws-short} IAM role by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-iam-roles \
    --name <name> \
    --region=<aws_region> \
    --credentials-requests-dir=<credentials_requests_dir> \
    --identity-provider-arn <oidc_arn>
----
+
.Example output
[source,terminal]
----
2023/09/12 11:38:57 Role arn:aws:iam::777777777777:role/<name>-aws-load-balancer-operator-aws-load-balancer-operator created
2023/09/12 11:38:57 Saved credentials configuration to: /home/user/<credentials_requests_dir>/manifests/aws-load-balancer-operator-aws-load-balancer-operator-credentials.yaml
2023/09/12 11:38:58 Updated Role policy for Role <name>-aws-load-balancer-operator-aws-load-balancer-operator created
----
+
where:
+
`<name>`:: Specifies the Amazon Resource Name (ARN) for an {aws-short} IAM role that was created for the {aws-short} Load Balancer Operator, such as `arn:aws:iam::777777777777:role/<name>-aws-load-balancer-operator-aws-load-balancer-operator`.
+
[NOTE]
====
The length of an {aws-short} IAM role name must be less than or equal to 12 characters.
====

// Creating an AWS IAM role by using the AWS CLI
// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator/preparing-sts-cluster-for-albo.adoc

[id="using-aws-cli-create-iam-role-alb-operator_{context}"]
= Creating an AWS IAM role by using the AWS CLI

[role="_abstract"]
To enable the {aws-short} Load Balancer Operator to interact with subnets and VPCs, create an {aws-short} IAM role by using the {aws-short} CLI. This enables the Operator to access and manage the necessary network resources within the cluster.

.Prerequisites

* You must have access to the {aws-short} Command Line Interface (`aws`).

.Procedure

. Generate a trust policy file by using your identity provider by running the following command:
+
[source,terminal]
----
$ cat <<EOF > albo-operator-trust-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "<oidc_arn>"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "<cluster_oidc_endpoint>:sub": "system:serviceaccount:aws-load-balancer-operator:aws-load-balancer-operator-controller-manager"
                }
            }
        }
    ]
}
EOF
----
+
where:
+
`<oidc_arn>`:: Specifies the Amazon Resource Name (ARN) of the OIDC identity provider, such as `arn:aws:iam::777777777777:oidc-provider/rh-oidc.s3.us-east-1.amazonaws.com/28292va7ad7mr9r4he1fb09b14t59t4f`.
`serviceaccount`:: Specifies the service account for the {aws-short} Load Balancer Controller. An example of `<cluster_oidc_endpoint>` is `rh-oidc.s3.us-east-1.amazonaws.com/28292va7ad7mr9r4he1fb09b14t59t4f`.

. Create the IAM role with the generated trust policy by running the following command:
+
[source,terminal]
----
$ aws iam create-role --role-name albo-operator --assume-role-policy-document file://albo-operator-trust-policy.json
----
+
.Example output
[source,terminal]
----
ROLE	arn:aws:iam::<aws_account_number>:role/albo-operator	2023-08-02T12:13:22Z <1>
ASSUMEROLEPOLICYDOCUMENT	2012-10-17
STATEMENT	sts:AssumeRoleWithWebIdentity	Allow
STRINGEQUALS	system:serviceaccount:aws-load-balancer-operator:aws-load-balancer-controller-manager
PRINCIPAL	arn:aws:iam:<aws_account_number>:oidc-provider/<cluster_oidc_endpoint>
----
+
where:
+
`<aws_account_number>`:: Specifies the ARN of the created {aws-short} IAM role for the {aws-short} Load Balancer Operator, such as `arn:aws:iam::777777777777:role/albo-operator`.

. Download the permission policy for the {aws-short} Load Balancer Operator by running the following command:
+
[source,terminal]
----
$ curl -o albo-operator-permission-policy.json https://raw.githubusercontent.com/openshift/aws-load-balancer-operator/main/hack/operator-permission-policy.json
----

. Attach the permission policy for the {aws-short} Load Balancer Controller to the IAM role by running the following command:
+
[source,terminal]
----
$ aws iam put-role-policy --role-name albo-operator --policy-name perms-policy-albo-operator --policy-document file://albo-operator-permission-policy.json
----

// Configuring the ARN role for the AWS Load Balancer Operator
// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator/preparing-sts-cluster-for-albo.adoc

[id="specifying-role-arn-albo-sts_{context}"]
= Configuring the ARN role for the AWS Load Balancer Operator

[role="_abstract"]
You can configure the Amazon Resource Name (ARN) role for the {aws-short} Load Balancer Operator as an environment variable. You can configure the ARN role by using the CLI.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Create the `aws-load-balancer-operator` project by running the following command:
+
[source,terminal]
----
$ oc new-project aws-load-balancer-operator
----

. Create the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: aws-load-balancer-operator
  namespace: aws-load-balancer-operator
spec:
  targetNamespaces: []
EOF
----

. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: aws-load-balancer-operator
  namespace: aws-load-balancer-operator
spec:
  channel: stable-v1
  name: aws-load-balancer-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  config:
    env:
    - name: ROLEARN
      value: "<albo_role_arn>"
EOF
----
+
where:
+
`<albo_role_arn>`:: Specifies the ARN role to be used in the `CredentialsRequest` to provision the {aws-short} credentials for the {aws-short} Load Balancer Operator. An example for `<albo_role_arn>` is `arn:aws:iam::<aws_account_number>:role/albo-operator`.
+
[NOTE]
====
The {aws-short} Load Balancer Operator waits until the secret is created before moving to the `Available` status.
====

// The IAM role for the AWS Load Balancer Controller
// Module included in the following assemblies:
//
// * networking/networking_operators/preparing-sts-cluster-for-albo.adoc

[id="the-iam-role-albo-controller.adoc_{context}"]
= The IAM role for the AWS Load Balancer Controller

[role="_abstract"]
The `CredentialsRequest` object for the {aws-short} Load Balancer Controller must be set with a manually provisioned Identity and Access Management (IAM) role.

You can create the IAM role by using the following options:

* Using the Cloud Credential Operator utility (`ccoctl`) and a predefined `CredentialsRequest` object.
* Using the {aws-short} CLI and predefined {aws-short} manifests.

If your environment does not support the `ccoctl` `command.ws-short` CLI, use the {aws-short} CLI.

[role="_additional-resources"]
.Additional resources

* the Cloud Credential Operator utility (`ccoctl`)

// Creating an AWS IAM role for the controller by using the Cloud Credential Operator utility
// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator/preparing-sts-cluster-for-albo.adoc

[id="using-ccoctl-create-iam-role-alb-controller_{context}"]
= Creating an AWS IAM role for the controller by using the Cloud Credential Operator utility

[role="_abstract"]
To enable the {aws-short} Load Balancer Controller to interact with subnets and VPCs, create an IAM role by using the Cloud Credential Operator utility (`ccoctl`). This utility ensures the controller has the specific permissions required to manage network resources within the cluster.

.Prerequisites

* You must extract and prepare the `ccoctl` binary.

.Procedure

. Download the `CredentialsRequest` custom resource (CR) and store it in a directory by running the following command:
+
[source,terminal]
----
$ curl --create-dirs -o <credentials_requests_dir>/controller.yaml https://raw.githubusercontent.com/openshift/aws-load-balancer-operator/main/hack/controller/controller-credentials-request.yaml
----

. Use the `ccoctl` utility to create an {aws-short} IAM role by running the following command:
+
[source,terminal]
----
$ ccoctl aws create-iam-roles \
    --name <name> \
    --region=<aws_region> \
    --credentials-requests-dir=<credentials_requests_dir> \
    --identity-provider-arn <oidc_arn>
----
+
.Example output
[source,terminal]
----
2023/09/12 11:38:57 Role arn:aws:iam::777777777777:role/<name>-aws-load-balancer-operator-aws-load-balancer-controller created
2023/09/12 11:38:57 Saved credentials configuration to: /home/user/<credentials_requests_dir>/manifests/aws-load-balancer-operator-aws-load-balancer-controller-credentials.yaml
2023/09/12 11:38:58 Updated Role policy for Role <name>-aws-load-balancer-operator-aws-load-balancer-controller created
----
+
where:
+
`<name>`:: Specifies the Amazon Resource Name (ARN) for an {aws-short} IAM role that was created for the {aws-short} Load Balancer Controller, such as `arn:aws:iam::777777777777:role/<name>-aws-load-balancer-operator-aws-load-balancer-controller`.
+
[NOTE]
====
The length of an AWS IAM role name must be less than or equal to 12 characters.
====

// Creating an AWS IAM role for the controller by using the AWS CLI
// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator/preparing-sts-cluster-for-albo.adoc

[id="using-aws-cli-create-iam-role-alb-controller_{context}"]
= Creating an AWS IAM role for the controller by using the AWS CLI

[role="_abstract"]
To enable the {aws-short} Load Balancer Controller to interact with subnets and Virtual Private Clouds (VPCs), create an IAM role by using the {aws-short} CLI. This ensures the controller has the specific permissions required to manage network resources within the cluster.

.Prerequisites

* You must have access to the {aws-short} command-line interface (`aws`).

.Procedure

. Generate a trust policy file using your identity provider by running the following command:
+
[source,terminal]
----
$ cat <<EOF > albo-controller-trust-policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "<oidc_arn>"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "<cluster_oidc_endpoint>:sub": "system:serviceaccount:aws-load-balancer-operator:aws-load-balancer-operator-controller-manager"
                }
            }
        }
    ]
}
EOF
----
+
where:
+
`<oidc_arn>`:: Specifies the Amazon Resource Name (ARN) of the OIDC identity provider, such as `arn:aws:iam::777777777777:oidc-provider/rh-oidc.s3.us-east-1.amazonaws.com/28292va7ad7mr9r4he1fb09b14t59t4f`.
`serviceaccount`:: Specifies the service account for the {aws-short} Load Balancer Controller. An example of `<cluster_oidc_endpoint>` is `rh-oidc.s3.us-east-1.amazonaws.com/28292va7ad7mr9r4he1fb09b14t59t4f`.

. Create an {aws-short} IAM role with the generated trust policy by running the following command:
+
[source,terminal]
----
$ aws iam create-role --role-name albo-controller --assume-role-policy-document file://albo-controller-trust-policy.json
----
+
.Example output
[source,terminal]
----
ROLE	arn:aws:iam::<aws_account_number>:role/albo-controller	2023-08-02T12:13:22Z <1>
ASSUMEROLEPOLICYDOCUMENT	2012-10-17
STATEMENT	sts:AssumeRoleWithWebIdentity	Allow
STRINGEQUALS	system:serviceaccount:aws-load-balancer-operator:aws-load-balancer-operator-controller-manager
PRINCIPAL	arn:aws:iam:<aws_account_number>:oidc-provider/<cluster_oidc_endpoint>
----
+
where:
+
`<aws_account_number>`:: Specifies the ARN for an {aws-short} IAM role for the {aws-short} Load Balancer Controller, such as `arn:aws:iam::777777777777:role/albo-controller`.

. Download the permission policy for the {aws-short} Load Balancer Controller by running the following command:
+
[source,terminal]
----
$ curl -o albo-controller-permission-policy.json https://raw.githubusercontent.com/openshift/aws-load-balancer-operator/main/assets/iam-policy.json
----

. Attach the permission policy for the {aws-short} Load Balancer Controller to an {aws-short} IAM role by running the following command:
+
[source,terminal]
----
$ aws iam put-role-policy --role-name albo-controller --policy-name perms-policy-albo-controller --policy-document file://albo-controller-permission-policy.json
----

. Create a YAML file that defines the `AWSLoadBalancerController` object:
+
.Example `sample-aws-lb-manual-creds.yaml` file
[source,yaml]
----
apiVersion: networking.olm.openshift.io/v1
kind: AWSLoadBalancerController
metadata:
  name: cluster
spec:
  credentialsRequestConfig:
    stsIAMRoleARN: <albc_role_arn>
----
+
where:
+
`kind`:: Specifies the `AWSLoadBalancerController` object.
`metatdata.name`:: Specifies the {aws-short} Load Balancer Controller name. All related resources use this instance name as a suffix.
`stsIAMRoleARN`:: Specifies the ARN role for the {aws-short} Load Balancer Controller. The `CredentialsRequest` object uses this ARN role to provision the {aws-short} credentials. An example of `<albc_role_arn>` is `arn:aws:iam::777777777777:role/albo-controller`.

[role="_additional-resources"]
[id="additional-resources-albo-sts-cluster_{context}"]
== Additional resources

* Configuring the Cloud Credential Operator utility
