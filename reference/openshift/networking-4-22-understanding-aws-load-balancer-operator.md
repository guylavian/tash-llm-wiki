---
title: "AWS Load Balancer Operator in {product-title}"
type: reference
domain: openshift
slug: networking-4-22-understanding-aws-load-balancer-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/understanding-aws-load-balancer-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# AWS Load Balancer Operator in {product-title}

[id="aws-load-balancer-operator"]
= AWS Load Balancer Operator in OpenShift Container Platform

[role="_abstract"]
To deploy and manage the AWS Load Balancer Controller, install the AWS Load Balancer Operator from the software catalog by using the OpenShift Container Platform web console or CLI. You can use the Operator to integrate AWS load balancers directly into your cluster infrastructure.

// Module included in the following assemblies:
// * networking/aws_load_balancer_operator/understanding-aws-load-balancer-operator.adoc

[id="nw-aws-load-balancer-operator-considerations_{context}"]
= AWS Load Balancer Operator considerations

[role="_abstract"]
To ensure a successful deployment, review the limitations of the AWS Load Balancer Operator. Understanding these constraints helps avoid compatibility issues and ensures the Operator meets your architectural requirements before installation.

Review the following limitations before installing and using the AWS Load Balancer Operator:

* The IP traffic mode only works on AWS Elastic Kubernetes Service (EKS). The AWS Load Balancer Operator disables the IP traffic mode for the AWS Load Balancer Controller. As a result of disabling the IP traffic mode, the AWS Load Balancer Controller cannot use the pod readiness gate.

* The AWS Load Balancer Operator adds command-line flags such as `--disable-ingress-class-annotation` and `--disable-ingress-group-name-annotation` to the AWS Load Balancer Controller. Therefore, the AWS Load Balancer Operator does not allow using the `kubernetes.io/ingress.class` and `alb.ingress.kubernetes.io/group.name` annotations in the `Ingress` resource.

* The AWS Load Balancer Operator requires that the service type is `NodePort` and not `LoadBalancer` or `ClusterIP`.

// Module included in the following assemblies:
// * networking/aws_load_balancer_operator/understanding-aws-load-balancer-operator.adoc

[id="nw-aws-load-balancer-operator_{context}"]
= Deploying the AWS Load Balancer Operator

[role="_abstract"]
The {aws-short} Load Balancer Operator can tag the public subnets if the `kubernetes.io/role/elb` tag is missing. Also, the {aws-short} Load Balancer Operator detects information from the underlying {aws-short} cloud.

The {aws-short} Load Balancer Operator detects the following information from the underlying {aws-short} cloud:

* The ID of the virtual private cloud (VPC) on which the cluster hosting the Operator is deployed.

* Public and private subnets of the discovered VPC.

The {aws-short} Load Balancer Operator supports the Kubernetes service resource of type `LoadBalancer` by using Network Load Balancer (NLB) with the `instance` target type only.

.Procedure

. To deploy the {aws-short} Load Balancer Operator on-demand from the software catalog, create a `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc -n aws-load-balancer-operator get sub aws-load-balancer-operator --template='{{.status.installplan.name}}{{"\n"}}'
----

. Check if the status of an install plan is `Complete` by running the following command:
+
[source,terminal]
----
$ oc -n aws-load-balancer-operator get ip <install_plan_name> --template='{{.status.phase}}{{"\n"}}'
----

. View the status of the `aws-load-balancer-operator-controller-manager` deployment by running the following command:
+
[source,terminal]
----
$ oc get -n aws-load-balancer-operator deployment/aws-load-balancer-operator-controller-manager
----
+
.Example output
[source,terminal]
----
NAME                                           READY     UP-TO-DATE   AVAILABLE   AGE
aws-load-balancer-operator-controller-manager  1/1       1            1           23h
----

// Module included in the following assemblies:
//
// * networking/aws_load_balancer_operator/understanding-aws-load-balancer-operator.adoc
// * installing/installing_aws/ipi/installing-aws-outposts.adoc

[id="nw-aws-load-balancer-with-outposts_{context}"]
= Using the AWS Load Balancer Operator in an AWS VPC cluster extended into an Outpost

[role="_abstract"]
You can configure the AWS Load Balancer Operator to provision an {aws-short} Application Load Balancer in an {aws-short} VPC cluster extended into an Outpost. {aws-short} Outposts does not support {aws-short} Network Load Balancers. As a result, the {aws-short} Load Balancer Operator cannot provision Network Load Balancers in an Outpost.

You can create an {aws-short} Application Load Balancer either in the cloud subnet or in the Outpost subnet.

An Application Load Balancer in the cloud can attach to cloud-based compute nodes. An Application Load Balancer in the Outpost can attach to edge compute nodes.

You must annotate Ingress resources with the Outpost subnet or the VPC subnet, but not both.

.Prerequisites

* You have extended an {aws-short} VPC cluster into an Outpost.
* You have installed the {oc-first}.
* You have installed the {aws-short} Load Balancer Operator and created the {aws-short} Load Balancer Controller.

.Procedure

* Configure the `Ingress` resource to use a specified subnet:
+
.Example `Ingress` resource configuration
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <application_name>
  annotations:
    alb.ingress.kubernetes.io/subnets: <subnet_id>
spec:
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /
            pathType: Exact
            backend:
              service:
                name: <application_name>
                port:
                  number: 80
----
+
where:
+
`<subnet_id>`:: Specifies the subnet to use. To use the Application Load Balancer in an Outpost, specify the Outpost subnet ID. To use the Application Load Balancer in the cloud, you must specify at least two subnets in different availability zones.
