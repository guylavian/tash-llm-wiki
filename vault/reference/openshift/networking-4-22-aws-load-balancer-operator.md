---
title: "AWS Load Balancer Operator"
type: reference
domain: openshift
slug: networking-4-22-aws-load-balancer-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/aws-load-balancer-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# AWS Load Balancer Operator

[id="aws-load-balancer"]
= AWS Load Balancer Operator

[role="_abstract"]
The AWS Load Balancer Operator is an Operator supported by Red{nbsp}Hat that you can optionally install on Site Reliability Engineering (SRE)-managed OpenShift Container Platform clusters.

[IMPORTANT]
====
Load balancers created by the AWS Load Balancer Operator cannot serve OpenShift Routes, and should only serve individual services or ingress resources that do not need the full layer 7 capabilities of an OpenShift Route.
====

The AWS Load Balancer Operator installs, manages, and configures the AWS Load Balancer Controller in a OpenShift Container Platform cluster.

The AWS Load Balancer Controller provisions AWS Application Load Balancers (ALBs) when you create Kubernetes Ingress resources and AWS Network Load Balancers (NLBs) when you create a Kubernetes Service resource with a type of `LoadBalancer`.

Compared with the default AWS in-tree load balancer provider, this controller provides advanced annotations for both ALBs and NLBs. Some advanced use cases are:

* Using native Kubernetes Ingress objects with ALBs
* Integrate ALBs with the AWS Web Application Firewall (WAF) service
* Specify custom Network Load Balancer (NLB) source IP ranges
* Specify custom NLB internal IP addresses

// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator.adoc

[id="aws-load-balancer-operator-prerequisites_{context}"]
= Prepare to install the AWS Load Balancer Operator

[role="_abstract"]
Before you install the AWS Load Balancer Operator, ensure that your cluster fulfills requirements and that your AWS Virtual Private Cloud (VPC) resources are appropriately tagged. You also have the option to configure some helpful environment variables.

Cluster requirements::

Your cluster must deploy across three availability zones and use a pre-existing VPC that has three public subnets.

[IMPORTANT]
====
These requirements mean that the AWS Load Balancer Operator might not be suitable for some PrivateLink clusters. AWS Network Load Balancers (NLBs) might be a better choice for such clusters.
====

// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator.adoc

[id="aws-load-balancer-operator-environment_{context}"]
= Set up temporary environment variables

[role="_abstract"]
You have the option to set up temporary environment variables to hold resource identifiers and configuration details. Using temporary environment variables streamlines the process of running the installation commands for the AWS Load Balancer Operator.

If you do not want to use environment variables to store certain values, you can manually enter those values in the relevant installation commands.

.Prerequisites

* You have installed the AWS CLI (`aws`).
* You have installed the {oc-first}.

.Procedure

. Log in to your cluster as a cluster administrator using the {oc-first}.
+
[source,terminal]
----
$ oc login --token=<token> --server=<cluster_url>
----

. Run the following commands to set up environment variables.
+
[source,terminal]
----
$ export CLUSTER_NAME=$(oc get infrastructure cluster -o=jsonpath="{.status.apiServerURL}" | sed  's|^https://||' | awk -F . '{print $2}')
----
+
[source,terminal]
----
$ export REGION=$(oc get infrastructure cluster -o=jsonpath="{.status.platformStatus.aws.region}")
----
+
[source,terminal]
----
$ export OIDC_ENDPOINT=$(oc get authentication.config.openshift.io cluster -o jsonpath='{.spec.serviceAccountIssuer}' | sed  's|^https://||')
----
+
[source,terminal]
----
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
----
+
[source,terminal]
----
$ export SCRATCH="/tmp/${CLUSTER_NAME}/alb-operator"
----
+
[source,terminal]
----
$ mkdir -p ${SCRATCH}
----
+
These commands create environment variables that you can use in this terminal session to pass their values to the command line interface.

. Verify that the environment variables have correct values by running the following command:
+
[source,terminal]
----
$ echo "Cluster name: ${CLUSTER_NAME}
Region: ${REGION}
OIDC Endpoint: ${OIDC_ENDPOINT}
AWS Account ID: ${AWS_ACCOUNT_ID}"
----
+
.Example output
[source,terminal]
----
Cluster name: <cluster_id>
Region: <region>
OIDC Endpoint: oidc.op1.openshiftapps.com/<oidc_id>
AWS Account ID: <aws_id>
----

. Use the same terminal session to continue with AWS Load Balancer Operator installation, to ensure that your environment variables are not lost.

// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator.adoc

[id="tagging-aws-vpc-subnets_{context}"]
= Tag the AWS VPC and subnets

[role="_abstract"]
To prepare your environment for the AWS Load Balancer Operator, tag your AWS Virtual Private Cloud (VPC) resources. This configuration ensures that the Operator can correctly identify and manage your network resources.

.Prerequisites

* You have installed the AWS CLI (`aws`).
* You have installed the {oc-first}.

.Procedure

. Optional: Set up environment variables for AWS VPC resources.
+
[source,terminal]
----
$ export VPC_ID=<vpc_id>
----
+
[source,terminal]
----
$ export PUBLIC_SUBNET_IDS="<public_subnet_a_id> <public_subnet_b_id> <public_subnet_c_id>"
----
+
[source,terminal]
----
$ export PRIVATE_SUBNET_IDS="<private_subnet_a_id> <private_subnet_b_id> <private_subnet_c_id>"
----

. Tag your VPC to associate it with your cluster:
+
[source,terminal]
----
$ aws ec2 create-tags --resources ${VPC_ID} --tags Key=kubernetes.io/cluster/${CLUSTER_NAME},Value=owned --region ${REGION}
----

. Tag your public subnets to allow changes by elastic load balancing roles, and tag your private subnets to allow changes by internal elastic load balancing roles:
+
[source,bash]
----
cat <<EOF > "${SCRATCH}/tag-subnets.sh"
#!/bin/bash

aws ec2 create-tags \
     --resources ${PUBLIC_SUBNET_IDS} \
     --tags Key=kubernetes.io/role/elb,Value='' \
     --region ${REGION}

aws ec2 create-tags \
     --resources ${PRIVATE_SUBNET_IDS} \
     --tags Key=kubernetes.io/role/internal-elb,Value='' \
     --region ${REGION}

EOF
----

. Run the script:
+
[source,bash]
----
bash ${SCRATCH}/tag-subnets.sh
----

[role="_additional-resources"]
.Additional resources
* Creating a OpenShift Container Platform cluster with STS using the default options
* Creating OpenShift Container Platform clusters using the default options
* AWS Load Balancer Operator on GitHub
* AWS Load Balancer Controller documentation
* AWS Application Load Balancers
* AWS Network Load Balancers
* Creating basic routes

// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator.adoc

[id="aws-load-balancer-operator-installation_{context}"]
= Installing the AWS Load Balancer Operator

[role="_abstract"]
You can install the AWS Load Balancer Operator by using the {oc-first}. Use the same terminal session you used in _Setting up your environment to install the AWS Load Balancer Operator_ to make use of the environment variables.

.Procedure

. Create a new project within your cluster for the AWS Load Balancer Operator:
+
[source,terminal]
----
$ oc new-project aws-load-balancer-operator
----

. Create an AWS IAM policy for the AWS Load Balancer Operator.
+
.. Download the appropriate IAM policy:
+
----
$ curl -o ${SCRATCH}/operator-permission-policy.json https://raw.githubusercontent.com/openshift/aws-load-balancer-operator/refs/heads/main/hack/operator-permission-policy.json
----
+
.. Create the permission policy for the Operator:
+
[source,terminal]
----
$ aws iam create-policy \
        --policy-name aws-load-balancer-operator-policy \
        --policy-document file://${SCRATCH}/operator-permission-policy.json \
        --region ${REGION}
----
+
Take note of the Operator policy Amazon Resource Name (ARN) in the output. The remainder of this process refers to this as `$OPERATOR_POLICY_ARN`.

. Create an AWS IAM role for the AWS Load Balancer Operator:
+
.. Create the trust policy for the Operator role:
+
[source,terminal,subs="quotes,verbatim"]
----
$ cat <<EOF > "${SCRATCH}/operator-trust-policy.json"
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
   "Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_ENDPOINT}"
 },
 "Action": "sts:AssumeRoleWithWebIdentity"
 }
 ]
}
EOF
----
+
.. Create the Operator role using the trust policy:
+
[source,terminal]
----
$ aws iam create-role --role-name "${CLUSTER_NAME}-alb-operator" \
    --assume-role-policy-document "file://${SCRATCH}/operator-trust-policy.json"
----
+
Take note of the Operator role ARN in the output. The remainder of this process refers to this as `$OPERATOR_ROLE_ARN`.
+
.. Associate the Operator role and policy:
+
[source,terminal]
----
$ aws iam attach-role-policy --role-name "${CLUSTER_NAME}-alb-operator" \
    --policy-arn $OPERATOR_POLICY_ARN
----

. Install the AWS Load Balancer Operator by creating an `OperatorGroup` and a `Subscription`:
+
[source,terminal,subs="quotes,verbatim"]
----
$ cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: aws-load-balancer-operator
  namespace: aws-load-balancer-operator
spec:
  targetNamespaces: []
---
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
      value: "${OPERATOR_ROLE_ARN}"
EOF
----

. Create an AWS IAM policy for the AWS Load Balancer Controller.
+
.. Download the appropriate IAM policy:
+
[source,terminal]
----
$ curl -o ${SCRATCH}/controller-permission-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.12.0/docs/install/iam_policy.json
----
+
.. Create the permission policy for the Controller:
+
[source,terminal]
----
$ aws iam create-policy \
    --region ${REGION} \
    --policy-name aws-load-balancer-controller-policy \
    --policy-document file://${SCRATCH}/controller-permission-policy.json
----
+
Take note of the Controller policy ARN in the output. The remainder of this process refers to this as `$CONTROLLER_POLICY_ARN`.

. Create an AWS IAM role for the AWS Load Balancer Controller:
+
.. Create the trust policy for the Controller role:
+
[source,terminal]
----
$ cat <<EOF > ${SCRATCH}/controller-trust-policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
          "Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_ENDPOINT}"
        },
        "Action": "sts:AssumeRoleWithWebIdentity",
        "Condition": {
          "StringEquals": {
            "${OIDC_ENDPOINT}:sub": "system:serviceaccount:aws-load-balancer-operator:aws-load-balancer-controller-cluster"
            }
        }
      }
    ]
  }
EOF
----
+
.. Create the Controller role using the trust policy:
+
[source,terminal]
----
CONTROLLER_ROLE_ARN=$(aws iam create-role --role-name "${CLUSTER_NAME}-albo-controller" \ --assume-role-policy-document "file://${SCRATCH}/controller-trust-policy.json" \ --query Role.Arn --output text) echo ${CONTROLLER_ROLE_ARN}
----
+
Take note of the Controller role ARN in the output. The remainder of this process refers to this as `$CONTROLLER_ROLE_ARN`.
+
.. Associate the Controller role and policy:
+
[source,terminal]
----
$ aws iam attach-role-policy \
    --role-name "${CLUSTER_NAME}-albo-controller" \
    --policy-arn ${CONTROLLER_POLICY_ARN}
----

. Deploy an instance of the AWS Load Balancer Controller:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: networking.olm.openshift.io/v1
kind: AWSLoadBalancerController
metadata:
 name: cluster
spec:
 credentialsRequestConfig:
   stsIAMRoleARN: ${CONTROLLER_ROLE_ARN}
EOF
----
+
[NOTE]
====
If you get an error here, wait a minute and try again. This situation happens because the Operator has not completed installation yet.
====

. Confirm that the Operator and Controller pods are both running:
+
[source,terminal]
----
$ oc -n aws-load-balancer-operator get pods
----
+
If you do not see output similar to the following, wait a few moments and retry.
+
.Example output
[source,terminal]
----
NAME                                                             READY   STATUS    RESTARTS   AGE
aws-load-balancer-controller-cluster-6ddf658785-pdp5d            1/1     Running   0          99s
aws-load-balancer-operator-controller-manager-577d9ffcb9-w6zqn   2/2     Running   0          2m4s
----

[role="_additional-resources"]
.Additional resources
* Creating many ingresses through a single AWS Load Balancer
* Adding TLS termination
* Creating an instance of AWS Load Balancer Controller
* AWS Documentation: Tag your Amazon EC2 resources

// Module included in the following assemblies:
//
// * networking/networking_operators/aws-load-balancer-operator.adoc

[id="aws-load-balancer-operator-validate-install_{context}"]
= Validating Operator installation

[role="_abstract"]
To confirm that the AWS Load Balancer Operator and Controller have installed correctly, deploy a basic sample application. This validation process involves creating ingress and load balancing services to test the deployment.

.Procedure

. Create a new project:
+
[source,terminal]
----
$ oc new-project hello-world
----

. Create a new `hello-world` application based on the `hello-openshift` image:
+
[source,terminal]
----
$ oc new-app -n hello-world --image=docker.io/openshift/hello-openshift
----

. Configure a `NodePort` service for an AWS Application Load Balancer (ALB) to connect to:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: v1
kind: Service
metadata:
  name: hello-openshift-nodeport
  namespace: hello-world
spec:
  ports:
    - port: 80
      targetPort: 8080
      protocol: TCP
  type: NodePort
  selector:
    deployment: hello-openshift
EOF
----

. Deploy an AWS ALB for the application:
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
                name: hello-openshift-nodeport
                port:
                  number: 80
EOF
----

. Test access to the AWS ALB endpoint for the application:
+
[NOTE]
====
ALB provisioning takes a few minutes. If you receive an error that says `curl: (6) Could not resolve host`, wait and try again.
====
+
[source,terminal]
----
$ ALB_INGRESS=$(oc -n hello-world get ingress hello-openshift-alb \
    -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
----
+
[source,terminal]
----
$ curl "http://${ALB_INGRESS}"
----
+
.Example output
[source,text]
----
Hello OpenShift!
----

. Deploy an AWS Network Load Balancer (NLB) for the application:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: v1
kind: Service
metadata:
  name: hello-openshift-nlb
  namespace: hello-world
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: external
    service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: instance
    service.beta.kubernetes.io/aws-load-balancer-scheme: internet-facing
spec:
  ports:
    - port: 80
      targetPort: 8080
      protocol: TCP
  type: LoadBalancer
  selector:
    deployment: hello-openshift
EOF
----
+
The `service.beta.kubernetes.io/aws-load-balancer-type` annotation is immutable for existing services. To change the load balancer type, you must recreate the service.

. Test access to the NLB endpoint for the application:
+
[NOTE]
====
NLB provisioning takes a few minutes. If you receive an error that says `curl: (6) Could not resolve host`, wait and try again.
====
+
[source,terminal]
----
$ NLB=$(oc -n hello-world get service hello-openshift-nlb \
  -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
----
+
[source,terminal]
----
$ curl "http://${NLB}"
----
+
Expected output shows `Hello OpenShift!`.

. You can now delete the sample application and all resources in the  `hello-world` namespace.
+
[source,terminal]
----
$ oc delete project hello-world
----

// Module included in the following assemblies:
//
[id="aws-load-balancer-operator-deleting_{context}"]
= Removing the AWS Load Balancer Operator

[role="_abstract"]
If you no longer need to use the AWS Load Balancer Operator, you can remove the Operator and delete any related roles and policies.

.Procedure

. Delete the Operator Subscription:
+
[source,terminal]
----
$ oc delete subscription aws-load-balancer-operator -n aws-load-balancer-operator
----

. Detach and delete the relevant AWS IAM roles:
+
[source,terminal]
----
$ aws iam detach-role-policy \
  --role-name "<cluster_id>-alb-operator" \
  --policy-arn <operator_policy_arn>
----
+
[source,terminal]
----
$ aws iam delete-role \
  --role-name "<cluster_id>-alb-operator"
----

. Delete the AWS IAM policy:
+
[source,terminal]
----
$ aws iam delete-policy --policy-arn <operator_policy_arn>
----
