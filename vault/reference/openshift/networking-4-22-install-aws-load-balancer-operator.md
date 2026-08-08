---
title: "Installing the AWS Load Balancer Operator"
type: reference
domain: openshift
slug: networking-4-22-install-aws-load-balancer-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/install-aws-load-balancer-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Installing the AWS Load Balancer Operator

[id="install-aws-load-balancer-operator"]
= Installing the AWS Load Balancer Operator

[role="_abstract"]
The AWS Load Balancer Operator deploys and manages the AWS Load Balancer Controller. You can install the AWS Load Balancer Operator from the software catalog by using OpenShift Container Platform web console or CLI.

// Module included in the following assemblies:
//
// * networking/aws_load_balancer_operator/install-aws-load-balancer-operator.adoc

[id="nw-installing-aws-load-balancer-operator_{context}"]
= Installing the AWS Load Balancer Operator by using the web console

[role="_abstract"]
To deploy the AWS Load Balancer Operator, install the Operator by using the web console. You can manage the lifecycle of the Operator by using a graphical interface.

.Prerequisites

* You have logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.
* Your cluster is configured with AWS as the platform type and cloud provider.
* If you are using a security token service (STS) or user-provisioned infrastructure, follow the related preparation steps. For example, if you are using AWS Security Token Service, see "Preparing for the AWS Load Balancer Operator on a cluster using the AWS Security Token Service (STS)".

.Procedure

. Navigate to *Ecosystem* -> *Software Catalog* in the OpenShift Container Platform web console.

. Select the *AWS Load Balancer Operator*. You can use the *Filter by keyword* text box or the filter list to search for the AWS Load Balancer Operator from the list of Operators.

. Select the `aws-load-balancer-operator` namespace.

. On the *Install Operator* page, select the following options:
+
.. For the *Update the channel* option, select *stable-v1*.
+
.. For the *Installation mode* option, select *All namespaces on the cluster (default)*.
+
.. For the *Installed Namespace* option, select `aws-load-balancer-operator`. If the `aws-load-balancer-operator` namespace does not exist, it gets created during the Operator installation.
+
.. Select *Update approval* as *Automatic* or *Manual*. By default, the *Update approval* is set to *Automatic*. If you select automatic updates, the Operator Lifecycle Manager (OLM) automatically upgrades the running instance of your Operator without any intervention. If you select manual updates, the OLM creates an update request. As a cluster administrator, you must then manually approve that update request to have the Operator update to the newer version.

. Click *Install*.

.Verification

* Verify that the AWS Load Balancer Operator shows the *Status* as *Succeeded* on the Installed Operators dashboard.

// Module included in the following assemblies:
//
// * networking/aws_load_balancer_operator/install-aws-load-balancer-operator.adoc

[id="nw-installing-aws-load-balancer-operator-cli_{context}"]
= Installing the AWS Load Balancer Operator by using the CLI

[role="_abstract"]
To deploy the AWS Load Balancer Controller, install the AWS Load Balancer Operator by using the command-line interface (CLI).

.Prerequisites

* You are logged in to the OpenShift Container Platform web console as a user with `cluster-admin` permissions.
* Your cluster is configured with AWS as the platform type and cloud provider.
* You have logged into the {oc-first}.

.Procedure

. Create a `Namespace` object:
+
.. Create a YAML file that defines the `Namespace` object:
+
.Example `namespace.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: aws-load-balancer-operator
# ...
----
+
.. Create the `Namespace` object by running the following command:
+
[source,terminal]
----
$ oc apply -f namespace.yaml
----

. Create an `OperatorGroup` object:
+
.. Create a YAML file that defines the `OperatorGroup` object:
+
.Example `operatorgroup.yaml` file
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: aws-lb-operatorgroup
  namespace: aws-load-balancer-operator
spec:
  upgradeStrategy: Default
----
+
.. Create the `OperatorGroup` object by running the following command:
+
[source,terminal]
----
$ oc apply -f operatorgroup.yaml
----

. Create a `Subscription` object:
+
.. Create a YAML file that defines the `Subscription` object:
+
.Example `subscription.yaml` file
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: aws-load-balancer-operator
  namespace: aws-load-balancer-operator
spec:
  channel: stable-v1
  installPlanApproval: Automatic
  name: aws-load-balancer-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
----
+
.. Create the `Subscription` object by running the following command:
+
[source,terminal]
----
$ oc apply -f subscription.yaml
----

.Verification

. Get the name of the install plan from the subscription:
+
[source,terminal]
----
$ oc -n aws-load-balancer-operator \
  get subscription aws-load-balancer-operator \
  --template='{{.status.installplan.name}}{{"\n"}}'
----

. Check the status of the install plan:
+
[source,terminal]
----
$ oc -n aws-load-balancer-operator \
  get ip <install_plan_name> \
  --template='{{.status.phase}}{{"\n"}}'
----
+
The output must be `Complete`.

// Module included in the following assemblies:
//
// * networking/networking_operators/aws_load_balancer_operator/create-instance-aws-load-balancer-controller.adoc

[id="nw-creating-instance-aws-load-balancer-controller_{context}"]
= Creating the AWS Load Balancer Controller

[role="_abstract"]
You can install only a single instance of the `AWSLoadBalancerController` object in a cluster. You can create the AWS Load Balancer Controller by using CLI. The AWS Load Balancer Operator reconciles only the `cluster` named resource.

.Prerequisites

* You have created the `echoserver` namespace.
* You have access to the {oc-first}.

.Procedure

. Create a YAML file that defines the `AWSLoadBalancerController` object:
+
.Example `sample-aws-lb.yaml` file
[source,yaml]
----
apiVersion: networking.olm.openshift.io/v1
kind: AWSLoadBalancerController
metadata:
  name: cluster
spec:
  subnetTagging: Auto
  additionalResourceTags:
  - key: example.org/security-scope
    value: staging
  ingressClass: alb
  config:
    replicas: 2
  enabledAddons:
    - AWSWAFv2
----
+
where:
+
`kind`:: Specifies the `AWSLoadBalancerController` object.
`metadata.name`:: Specifies the AWS Load Balancer Controller name. The Operator adds this instance name as a suffix to all related resources.
`spec.subnetTagging`:: Specifies the subnet tagging method for the AWS Load Balancer Controller. The following values are valid:
* `Auto`: The AWS Load Balancer Operator determines the subnets that belong to the cluster and tags them appropriately. The Operator cannot determine the role correctly if the internal subnet tags are not present on internal subnet.
* `Manual`: You manually tag the subnets that belong to the cluster with the appropriate role tags. Use this option if you installed your cluster on user-provided infrastructure.
`spec.additionalResourceTags`:: Specifies the tags used by the AWS Load Balancer Controller when it provisions AWS resources.
`ingressClass`:: Specifies the ingress class name. The default value is `alb`.
`config.replicas`:: Specifies the number of replicas of the AWS Load Balancer Controller.
`enabledAddons`:: Specifies annotations as an add-on for the AWS Load Balancer Controller.
`AWSWAFv2`:: Specifies that enablement of the `alb.ingress.kubernetes.io/wafv2-acl-arn` annotation.

. Create the `AWSLoadBalancerController` object by running the following command:
+
[source,terminal]
----
$ oc create -f sample-aws-lb.yaml
----

. Create a YAML file that defines the `Deployment` resource:
+
.Example `sample-aws-lb.yaml` file
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: <echoserver>
  namespace: echoserver
spec:
  selector:
    matchLabels:
      app: echoserver
  replicas: 3
  template:
    metadata:
      labels:
        app: echoserver
    spec:
      containers:
        - image: openshift/origin-node
          command:
           - "/bin/socat"
          args:
            - TCP4-LISTEN:8080,reuseaddr,fork
            - EXEC:'/bin/bash -c \"printf \\\"HTTP/1.0 200 OK\r\n\r\n\\\"; sed -e \\\"/^\r/q\\\"\"'
          imagePullPolicy: Always
          name: echoserver
          ports:
            - containerPort: 8080
----
+
where:
+
`kind`:: Specifies the deployment resource.
`metadata.name`:: Specifies the deployment name.
`spec.replicas`:: Specifies the number of replicas of the deployment.

. Create a YAML file that defines the `Service` resource:
+
.Example `service-albo.yaml` file
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: <echoserver>
  namespace: echoserver
spec:
  ports:
    - port: 80
      targetPort: 8080
      protocol: TCP
  type: NodePort
  selector:
    app: echoserver
----
+
where:
+
`apiVersion`:: Specifies the service resource.
`metadata.name`:: Specifies the service name.

. Create a YAML file that defines the `Ingress` resource:
+
.Example `ingress-albo.yaml` file
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <name>
  namespace: echoserver
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: instance
spec:
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /
            pathType: Exact
            backend:
              service:
                name: <echoserver>
                port:
                  number: 80
----
+
where:
+
`metadata.name`:: Specifies a name for the `Ingress` resource.
`service.name`:: Specifies the service name.

.Verification

* Save the status of the `Ingress` resource in the `HOST` variable by running the following command:
+
[source,terminal]
----
$ HOST=$(oc get ingress -n echoserver echoserver --template='{{(index .status.loadBalancer.ingress 0).hostname}}')
----

* Verify the status of the `Ingress` resource by running the following command:
+
[source,terminal]
----
$ curl $HOST
----
