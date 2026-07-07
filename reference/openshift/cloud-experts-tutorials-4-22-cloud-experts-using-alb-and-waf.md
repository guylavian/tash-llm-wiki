---
title: "Tutorial: Using AWS WAF and AWS ALBs to protect {product-title} workloads"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-using-alb-and-waf
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-using-alb-and-waf
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Using AWS WAF and AWS ALBs to protect {product-title} workloads

[id="cloud-experts-using-alb-and-waf"]
= Tutorial: Using AWS WAF and AWS ALBs to protect OpenShift Container Platform workloads

[role="_abstract"]
AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to your protected web application resources.

You can use an AWS Application Load Balancer (ALB) to add a Web Application Firewall (WAF) to your OpenShift Container Platform workloads. Using an external solution protects OpenShift Container Platform resources from experiencing denial of service due to handling the WAF.

[IMPORTANT]
====
It is recommended that you use the more flexible CloudFront method unless you absolutely must use an ALB based solution.
====

[id="prerequisites_{context}"]
== Prerequisites

* Multiple availability zone (AZ) OpenShift Container Platform cluster.
+
[NOTE]
====
AWS ALBs require at least two _public_ subnets across AZs, per the AWS documentation. For this reason, only multiple AZ OpenShift Container Platform clusters can be used with ALBs.
====
+
* You have access to the OpenShift CLI (`oc`).
* You have access to the AWS CLI (`aws`).

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-using-alb-and-waf.adoc

[id="cloud-experts-using-alb-and-waf-environment-setup_{context}"]
= Setting up your environment

[role="_abstract"]
You can use environment variables to ensure consistency across the commands within this lab.

.Procedure

* Configure the following environment variables:
+
[source,terminal]
----
$ export AWS_PAGER=""
$ export CLUSTER=$(oc get infrastructure cluster -o=jsonpath="{.status.infrastructureName}")
$ export REGION=$(oc get infrastructure cluster -o=jsonpath="{.status.platformStatus.aws.region}")
$ export OIDC_ENDPOINT=$(oc get authentication.config.openshift.io cluster -o jsonpath='{.spec.serviceAccountIssuer}' | sed  's|^https://||')
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
$ export SCRATCH="/tmp/${CLUSTER}/alb-waf"
$ mkdir -p ${SCRATCH}
$ echo "Cluster: $(echo ${CLUSTER} | sed 's/-[a-z0-9]\{5\}$//'), Region: ${REGION}, OIDC Endpoint: ${OIDC_ENDPOINT}, AWS Account ID: ${AWS_ACCOUNT_ID}"
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-using-alb-and-waf.adoc

[id="cloud-experts-using-alb-and-waf-aws-vpc-and-subnets_{context}"]
= AWS VPC and subnets

[NOTE]
====
This section only applies to clusters that were deployed into existing VPCs. If you did not deploy your cluster into an existing VPC, skip this section and proceed to the installation section below.
====

[role="_abstract"]
You need to tag your subnets and VPCs before using these resources in this tutorial.

.Procedure
. Set the below variables to the proper values for your OpenShift Container Platform deployment:
+
[source,terminal]
----
$ export VPC_ID=<vpc-id>
$ export PUBLIC_SUBNET_IDS=(<space-separated-list-of-ids>)
$ export PRIVATE_SUBNET_IDS=(<space-separated-list-of-ids>)
----
+
--
where:

`VPC_ID=<vpc-id>`:: Replace with the VPC ID of the cluster, for example: `export VPC_ID=vpc-04c429b7dbc4680ba`.
`PUBLIC_SUBNET_IDS=(<space-separated-list-of-ids>)`:: Replace with a space-separated list of the private subnet IDs of the cluster, making sure to preserve the `()`. For example: `export PUBLIC_SUBNET_IDS=(subnet-056fd6861ad332ba2 subnet-08ce3b4ec753fe74c subnet-071aa28228664972f)`.
`PRIVATE_SUBNET_IDS=(<space-separated-list-of-ids>)`:: Replace with a space-separated list of the private subnet IDs of the cluster, making sure to preserve the `()`. For example: `export PRIVATE_SUBNET_IDS=(subnet-0b933d72a8d72c36a subnet-0817eb72070f1d3c2 subnet-0806e64159b66665a)`.
--
+
. Add a tag to your cluster's VPC with the cluster identifier:
+
[source,terminal]
----
$ aws ec2 create-tags --resources ${VPC_ID} \
  --tags Key=kubernetes.io/cluster/${CLUSTER},Value=shared --region ${REGION}
----
+
. Add a tag to your public subnets:
+
[source,terminal]
----
$ aws ec2 create-tags \
  --resources ${PUBLIC_SUBNET_IDS} \
  --tags Key=kubernetes.io/role/elb,Value='1' \
        Key=kubernetes.io/cluster/${CLUSTER},Value=shared \
  --region ${REGION}
----
+
. Add a tag to your private subnets:
+
[source,terminal]
----
$ aws ec2 create-tags \
  --resources ${PRIVATE_SUBNET_IDS} \
  --tags Key=kubernetes.io/role/internal-elb,Value='1' \
        Key=kubernetes.io/cluster/${CLUSTER},Value=shared \
  --region ${REGION}
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-using-alb-and-waf.adoc

[id="cloud-experts-using-alb-and-waf-deploy-aws-load-balancer-operator_{context}"]
= Deploy the AWS Load Balancer Operator

[role="_abstract"]
The AWS Load Balancer Operator is used to used to install, manage and configure an instance of `aws-load-balancer-controller` in a OpenShift Container Platform cluster. To deploy ALBs in OpenShift Container Platform, we need to first deploy the AWS Load Balancer Operator.

.Procedure
. Create a new project to deploy the AWS Load Balancer Operator into by running the following command:
+
[source,terminal]
----
$ oc new-project aws-load-balancer-operator
----
+
. Create an AWS IAM policy for the AWS Load Balancer Controller if one does not already exist by running the following command:
+
[NOTE]
====
The policy is sourced from the upstream AWS Load Balancer Controller policy. This is required by the operator to function.
====
+
[source,terminal]
----
$ POLICY_ARN=$(aws iam list-policies --query \
     "Policies[?PolicyName=='aws-load-balancer-operator-policy'].{ARN:Arn}" \
     --output text)
----
+
[source,terminal]
----
$ if [[ -z "${POLICY_ARN}" ]]; then
    wget -O "${SCRATCH}/load-balancer-operator-policy.json" \
       https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
     POLICY_ARN=$(aws --region "$REGION" --query Policy.Arn \
     --output text iam create-policy \
     --policy-name aws-load-balancer-operator-policy \
     --policy-document "file://${SCRATCH}/load-balancer-operator-policy.json")
fi
----
+
. Create an AWS IAM trust policy for AWS Load Balancer Operator:
+
[source,terminal]
----
$ cat <<EOF > "${SCRATCH}/trust-policy.json"
{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Condition": {
   "StringEquals" : {
     "${OIDC_ENDPOINT}:sub": ["system:serviceaccount:aws-load-balancer-operator:aws-load-balancer-operator-controller-manager", "system:serviceaccount:aws-load-balancer-operator:aws-load-balancer-controller-cluster"]
   }
 },
 "Principal": {
   "Federated": "arn:aws:iam::$AWS_ACCOUNT_ID:oidc-provider/${OIDC_ENDPOINT}"
 },
 "Action": "sts:AssumeRoleWithWebIdentity"
 }
 ]
}
EOF
----
+
. Create an AWS IAM role for the AWS Load Balancer Operator:
+
[source,terminal]
----
$ ROLE_ARN=$(aws iam create-role --role-name "${CLUSTER}-alb-operator" \
   --assume-role-policy-document "file://${SCRATCH}/trust-policy.json" \
   --query Role.Arn --output text)
----
+
. Attach the AWS Load Balancer Operator policy to the IAM role we created previously by running the following command:
+
[source,terminal]
----
$ aws iam attach-role-policy --role-name "${CLUSTER}-alb-operator" \
     --policy-arn ${POLICY_ARN}
----
+
. Create a secret for the AWS Load Balancer Operator to assume our newly created AWS IAM role:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: aws-load-balancer-operator
  namespace: aws-load-balancer-operator
stringData:
  credentials: |
    [default]
    role_arn = ${ROLE_ARN}
    web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
EOF
----
+
. Install the AWS Load Balancer Operator:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: aws-load-balancer-operator
  namespace: aws-load-balancer-operator
spec:
  upgradeStrategy: Default
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: aws-load-balancer-operator
  namespace: aws-load-balancer-operator
spec:
  channel: stable-v1.0
  installPlanApproval: Automatic
  name: aws-load-balancer-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  startingCSV: aws-load-balancer-operator.v1.0.0
EOF
----
+
. Deploy an instance of the AWS Load Balancer Controller using the operator:
+
[NOTE]
====
If you get an error here wait a minute and try again, it means the Operator has not completed installing yet.
====
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: networking.olm.openshift.io/v1
kind: AWSLoadBalancerController
metadata:
  name: cluster
spec:
  credentials:
    name: aws-load-balancer-operator
  enabledAddons:
    - AWSWAFv2
EOF
----
+
. Check the that the operator and controller pods are both running:
+
[source,terminal]
----
$ oc -n aws-load-balancer-operator get pods
----
+
You should see the following, if not wait a moment and retry:
+
[source,terminal]
----
NAME                                                             READY   STATUS    RESTARTS   AGE
aws-load-balancer-controller-cluster-6ddf658785-pdp5d            1/1     Running   0          99s
aws-load-balancer-operator-controller-manager-577d9ffcb9-w6zqn   2/2     Running   0          2m4s
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-using-alb-and-waf.adoc

[id="cloud-experts-using-alb-and-waf-deploy-sample-application_{context}"]
= Deploy a sample application

[role="_abstract"]
You can use the {oc-first} tool to run a sample application to verify this tutorial.

.Procedure
. Create a new project for our sample application:
+
[source,terminal]
----
$ oc new-project hello-world
----
+
. Deploy a hello world application:
+
[source,terminal]
----
$ oc new-app -n hello-world --image=docker.io/openshift/hello-openshift
----
+
. Convert the pre-created service resource to a NodePort service type:
+
[source,terminal]
----
$ oc -n hello-world patch service hello-openshift -p '{"spec":{"type":"NodePort"}}'
----
+
. Deploy an AWS ALB using the AWS Load Balancer Operator:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: hello-openshift-alb
  namespace: hello-world
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
spec:
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /
            pathType: Exact
            backend:
              service:
                name: hello-openshift
                port:
                  number: 8080
EOF
----
+
. Curl the AWS ALB Ingress endpoint to verify the hello world application is accessible:
+
[NOTE]
====
AWS ALB provisioning takes a few minutes. If you receive an error that says `curl: (6) Could not resolve host`, please wait and try again.
====
+
[source,terminal]
----
$ INGRESS=$(oc -n hello-world get ingress hello-openshift-alb -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
$ curl "http://${INGRESS}"
----
+
.Example output
[source,text]
----
Hello OpenShift!
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-using-alb-and-waf.adoc

[id="cloud-experts-using-alb-and-waf-configure-aws-waf_{context}"]
= Configure the AWS WAF

[role="_abstract"]
The AWS WAF service is a web application firewall that lets you monitor, protect, and control the HTTP and HTTPS requests that are forwarded to your protected web application resources, like OpenShift Container Platform.

.Procedure
. Create a AWS WAF rules file to apply to our web ACL:
+
[source,terminal]
----
$ cat << EOF > ${SCRATCH}/waf-rules.json
[
    {
      "Name": "AWS-AWSManagedRulesCommonRuleSet",
      "Priority": 0,
      "Statement": {
        "ManagedRuleGroupStatement": {
          "VendorName": "AWS",
          "Name": "AWSManagedRulesCommonRuleSet"
        }
      },
      "OverrideAction": {
        "None": {}
      },
      "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWS-AWSManagedRulesCommonRuleSet"
      }
    },
    {
      "Name": "AWS-AWSManagedRulesSQLiRuleSet",
      "Priority": 1,
      "Statement": {
        "ManagedRuleGroupStatement": {
          "VendorName": "AWS",
          "Name": "AWSManagedRulesSQLiRuleSet"
        }
      },
      "OverrideAction": {
        "None": {}
      },
      "VisibilityConfig": {
        "SampledRequestsEnabled": true,
        "CloudWatchMetricsEnabled": true,
        "MetricName": "AWS-AWSManagedRulesSQLiRuleSet"
      }
    }
]
EOF
----
+
This will enable the Core (Common) and SQL AWS Managed Rule Sets.
+
. Create an AWS WAF Web ACL using the rules we specified above:
+
[source,terminal]
----
$ WAF_ARN=$(aws wafv2 create-web-acl \
  --name ${CLUSTER}-waf \
  --region ${REGION} \
  --default-action Allow={} \
  --scope REGIONAL \
  --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=${CLUSTER}-waf-metrics \
  --rules file://${SCRATCH}/waf-rules.json \
  --query 'Summary.ARN' \
  --output text)
----
+
. Annotate the Ingress resource with the AWS WAF Web ACL ARN:
+
[source,terminal]
----
$ oc annotate -n hello-world ingress.networking.k8s.io/hello-openshift-alb \
  alb.ingress.kubernetes.io/wafv2-acl-arn=${WAF_ARN}
----

. Wait for 10 seconds for the rules to propagate and test that the app still works:
+
[source,terminal]
----
$ curl "http://${INGRESS}"
----
+
.Example output
[source,text]
----
Hello OpenShift!
----

. Test that the WAF denies a bad request:
+
[source,terminal]
----
$ curl -X POST "http://${INGRESS}" \
  -F "user='<script><alert>Hello></alert></script>'"
----
+
.Example output
[source,text]
----
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
</body>
</html
----
+
[NOTE]
====
Activation of the AWS WAF integration can sometimes take several minutes. If you do not receive a `403 Forbidden` error, please wait a few seconds and try again.
====
+
The expected result is a `403 Forbidden` error, which means the AWS WAF is protecting your application.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Adding Extra Security with AWS WAF, CloudFront and ROSA | Amazon Web Services on YouTube
