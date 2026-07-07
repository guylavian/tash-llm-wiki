---
title: "Creating the ServiceMeshControlPlane"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-create-smcp
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-create-smcp
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Creating the ServiceMeshControlPlane

[id="ossm-create-smcp"]
= Creating the ServiceMeshControlPlane

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-create-smcp.adoc

[id="ossm-about-smcp_{context}"]
= About ServiceMeshControlPlane

The control plane includes Istiod, Ingress and Egress Gateways, and other components, such as Kiali and Jaeger. The control plane must be deployed in a separate namespace than the {SMProductShortName} Operators and the data plane applications and services. You can deploy a basic installation of the `ServiceMeshControlPlane`(SMCP) from the OpenShift Container Platform web console or the command line using the `oc` client tool.

[NOTE]
====
This basic installation is configured based on the default OpenShift Container Platform settings and is not designed for production use. Use this default installation to verify your installation, and then configure your `ServiceMeshControlPlane` settings for your environment.
====

[NOTE]
====
The {SMProductShortName} documentation uses `istio-system` as the example project, but you can deploy the service mesh to any project.
====

If you are deploying the control plane for use on {product-rosa}, see the Red Hat Knowledgebase article OpenShift service mesh operator Istio basic not starting due to authentication errors, which discusses adding a new project and starting pods.
If you are deploying the control plane for use on {product-dedicated}, see the Red Hat Knowledgebase article OpenShift service mesh operator Istio basic not starting due to authentication errors, which discusses adding a new project and starting pods.

// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-control-plane-deploy-operatorhub_{context}"]
= Deploying the {SMProductShortName} control plane from the web console

You can deploy a basic `ServiceMeshControlPlane` by using the web console.  In this example, `istio-system` is the name of the {SMProductShortName} control plane project.

.Prerequisites

* The {SMProductName} Operator must be installed.
* You are logged in to the OpenShift Container Platform web console as `cluster-admin`.
* You are logged in to the OpenShift Container Platform web console as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role. If you use {product-dedicated}, you must have an account with the `dedicated-admin` role.

. Create a project named `istio-system`.
+
.. Navigate to *Home* -> *Projects*.
+
.. Click *Create Project*.
+
.. In the *Name* field, enter `istio-system`. The `ServiceMeshControlPlane` resource must be installed in a project that is separate from your microservices and Operators.
+
These steps use `istio-system` as an example, but you can deploy your {SMProductShortName} control plane in any project as long as it is separate from the project that contains your services.
+
.. In the *Name* field, enter `istio-system`. The `ServiceMeshControlPlane` resource must be installed in the `istio-system` project, separate from your microservices and Operators.
+
.. Click *Create*.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator, then click *Istio Service Mesh Control Plane*.

. On the *Istio Service Mesh Control Plane* tab, click *Create ServiceMeshControlPlane*.
+
--
.. Accept the default {SMProductShortName} control plane version to take advantage of the features available in the most current version of the product. The version of the control plane determines the features available regardless of the version of the Operator.

.. Add the `spec.security.identity.type.ThirdParty` field, required by {product-rosa}.
.. Add the `spec.security.identity.type.ThirdParty` field, required by {product-dedicated}.
+
.. Click *Create*.
--
+
The Operator creates pods, services, and {SMProductShortName} control plane components based on your configuration parameters. You can configure `ServiceMeshControlPlane` settings at a later time.

.Verification

* To verify the control plane installed correctly, click the *Istio Service Mesh Control Plane* tab.
+
.. Click the name of the new control plane.
+
.. Click the *Resources* tab to see the {SMProductName} control plane resources the Operator created and configured.

This module is included in the following assemblies:
* service_mesh/v2x/ossm-create-smcp.adoc

[id="ossm-control-plane-deploy-cli_{context}"]
= Deploying the {SMProductShortName} control plane using the CLI

You can deploy a basic `ServiceMeshControlPlane` from the command line.

.Prerequisites

* The {SMProductName} Operator must be installed.
* Access to the OpenShift CLI (`oc`).
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Create a project named `istio-system`.
+
[source,terminal]
----
$ oc new-project istio-system
----
+
The `ServiceMeshControlPlane` resource must be installed in the `istio-system` project, separate from your microservices and Operators.

. Create a `ServiceMeshControlPlane` file named `istio-installation.yaml` using the following example. The version of the {SMProductShortName} control plane determines the features available regardless of the version of the Operator.
+
.Example version {MaistraVersion} istio-installation.yaml
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  version: v{MaistraVersion}
  tracing:
    type: None
    sampling: 10000
  addons:
    kiali:
      enabled: true
      name: kiali
    grafana:
      enabled: true
----
. Create a `ServiceMeshControlPlane` file named `istio-installation.yaml` using the following example. The version of the {SMProductShortName} control plane determines the features available regardless of the version of the Operator.
+
.Example `ServiceMeshControlPlane` resource
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  version: v{MaistraVersion}
  security:
    identity:
      type: ThirdParty <1>
  tracing:
    type: None
    sampling: 10000
  policy:
    type: Istiod
  addons:
    grafana:
      enabled: true
    kiali:
      enabled: true
    prometheus:
      enabled: true
  telemetry:
    type: Istiod
----
<1> Specifies a required setting for {product-rosa}.
<1> Specifies a required setting for {product-dedicated}.
+
. Run the following command to deploy the {SMProductShortName} control plane, where `<istio_installation.yaml>` includes the full path to your file.
+
[source,terminal]
----
$ oc create -n istio-system -f <istio_installation.yaml>
----
+
. To watch the progress of the pod deployment, run the following command:
+
[source,terminal]
----
$ oc get pods -n istio-system -w
----
+
You should see output similar to the following:
+
[source,terminal]
----
NAME                                   READY   STATUS    RESTARTS   AGE
grafana-b4d59bd7-mrgbr                 2/2     Running   0          65m
istio-egressgateway-678dc97b4c-wrjkp   1/1     Running   0          108s
istio-ingressgateway-b45c9d54d-4qg6n   1/1     Running   0          108s
istiod-basic-55d78bbbcd-j5556          1/1     Running   0          108s
kiali-6476c7656c-x5msp                 1/1     Running   0          43m
prometheus-58954b8d6b-m5std            2/2     Running   0          66m
----

This module is included in the following assemblies:
* service_mesh/v2x/ossm-create-smcp.adoc
[id="ossm-validate-control-plane-cli_{context}"]
= Validating your SMCP installation with the CLI
You can validate the creation of the `ServiceMeshControlPlane` from the command line.

. Prerequisites

* The {SMProductName} Operator must be installed.
* Access to the OpenShift CLI (`oc`).
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Run the following command to verify the {SMProductShortName} control plane installation, where `istio-system` is the namespace where you installed the {SMProductShortName} control plane.
+
[source,terminal]
----
$ oc get smcp -n istio-system
----
+
The installation has finished successfully when the `STATUS` column is `ComponentsReady`.
+
[source,terminal,subs="attributes+"]
----
NAME    READY   STATUS            PROFILES      VERSION   AGE
basic   10/10   ComponentsReady   ["default"]   {SMProductVersion}     66m
----

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-create-smcp.adoc

[id="ossm-about-control-plane-components-and-infrastructure-nodes_{context}"]
= About control plane components and infrastructure nodes

Infrastructure nodes provide a way to isolate infrastructure workloads for two primary purposes:

* To prevent incurring billing costs against subscription counts
* To separate maintenance and management of infrastructure workloads

You can configure some or all of the {SMProductShortName} control plane components to run on infrastructure nodes.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-config-control-plane-infrastructure-node-console_{context}"]
= Configuring all control plane components to run on infrastructure nodes using the web console

Perform this task if all of the components deployed by the {SMProductShortName} control plane will run on infrastructure nodes. These deployed components include Istiod, Ingress Gateway, and Egress Gateway, and optional applications such as Prometheus, Grafana, and Distributed Tracing.

If the control plane will run on a worker node, skip this task.

.Prerequisites

* You have installed the {SMProductName} Operator.
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator, and then click *Istio Service Mesh Control Plane*.

. Click the name of the control plane resource. For example, `basic`.

. Click *YAML*.

. Add the `nodeSelector` and `tolerations` fields to the `spec.runtime.defaults.pod` specification in the `ServiceMeshControlPlane` resource, as shown in the following example:
+
[source,yaml]
----
spec:
  runtime:
    defaults:
      pod:
        nodeSelector: <1>
          node-role.kubernetes.io/infra: ""
        tolerations: <2>
        - effect: NoSchedule
          key: node-role.kubernetes.io/infra
          value: reserved
        - effect: NoExecute
          key: node-role.kubernetes.io/infra
          value: reserved
----
<1> Ensures that the `ServiceMeshControlPlane` pod is only scheduled on an infrastructure node.
<2> Ensures that the pod is accepted by the infrastructure node for execution.

. Click *Save*.

. Click *Reload*.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-config-individual-control-plane-infrastructure-node-console_{context}"]
= Configuring individual control plane components to run on infrastructure nodes using the web console

Perform this task if individual components deployed by the {SMProductShortName} control plane will run on infrastructure nodes. These deployed components include Istiod, the Ingress Gateway, and the Egress Gateway.

If the control plane will run on a worker node, skip this task.

.Prerequisites

* You have installed the {SMProductName} Operator.
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator, and then click *Istio Service Mesh Control Plane*.

. Click the name of the control plane resource. For example, `basic`.

. Click *YAML*.

. Add the `nodeSelector` and `tolerations` fields to the `spec.runtime.components.pilot.pod` specification in the `ServiceMeshControlPlane` resource, as shown in the following example:
+
[source,yaml]
----
spec:
  runtime:
    components:
      pilot:
        pod:
          nodeSelector: <1>
            node-role.kubernetes.io/infra: ""
          tolerations: <2>
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra
            value: reserved
          - effect: NoExecute
            key: node-role.kubernetes.io/infra
            value: reserved
----
<1> Ensures that the `Istiod` pod is only scheduled on an infrastructure node.
<2> Ensures that the pod is accepted by the infrastructure node for execution.

. Add the `nodeSelector` and the `tolerations` fields to the `spec.gateways.ingress.runtime.pod` and `spec.gateways.egress.runtime.pod` specifications in the `ServiceMeshControlPlane` resource, as shown in the following example:
+
[source,yaml]
----
spec:
  gateways:
    ingress:
      runtime:
        pod:
          nodeSelector: <1>
            node-role.kubernetes.io/infra: ""
          tolerations: <2>
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra
            value: reserved
          - effect: NoExecute
            key: node-role.kubernetes.io/infra
            value: reserved
    egress:
      runtime:
        pod:
          nodeSelector: <1>
            node-role.kubernetes.io/infra: ""
          tolerations: <2>
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra
            value: reserved
          - effect: NoExecute
            key: node-role.kubernetes.io/infra
            value: reserved
----
<1> Ensures that the gateway pod is only scheduled on an infrastructure node
<2> Ensures that the pod is accepted by the infrastructure node for execution.

. Click *Save*.

. Click *Reload*.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-config-control-plane-infrastructure-node-cli_{context}"]
= Configuring all control plane components to run on infrastructure nodes using the CLI

Perform this task if all of the components deployed by the {SMProductShortName} control plane will run on infrastructure nodes. These deployed components include Istiod, Ingress Gateway, and Egress Gateway, and optional applications such as Prometheus, Grafana, and Distributed Tracing.

If the control plane will run on a worker node, skip this task.

.Prerequisites

* You have installed the {SMProductName} Operator.
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Open the `ServiceMeshControlPlane` resource as a YAML file:
+
[source,terminal]
----
$ oc -n istio-system edit smcp <name> <1>
----
<1> `<name>` represents the name of the `ServiceMeshControlPlane` resource.

. To run all of the {SMProductShortName} components deployed by the `ServiceMeshControlPlane` on infrastructure nodes, add the `nodeSelector` and `tolerations` fields to the `spec.runtime.defaults.pod` spec in the `ServiceMeshControlPlane` resource:
+
[source,yaml]
----
spec:
  runtime:
    defaults:
      pod:
        nodeSelector: <1>
          node-role.kubernetes.io/infra: ""
        tolerations: <2>
        - effect: NoSchedule
          key: node-role.kubernetes.io/infra
          value: reserved
        - effect: NoExecute
          key: node-role.kubernetes.io/infra
          value: reserved
----
<1> Ensures that the SMCP pods are only scheduled on an infrastructure node.
<2> Ensures that the pods are accepted by the infrastructure node.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-config-individual-control-plane-infrastructure-node-cli_{context}"]
= Configuring individual control plane components to run on infrastructure nodes using the CLI

Perform this task if individual components deployed by the {SMProductShortName} control plane will run on infrastructure nodes. These deployed components include Istiod, the Ingress Gateway, and the Egress Gateway.

If the control plane will run on a worker node, skip this task.

.Prerequisites

* You have installed the {SMProductName} Operator.
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Open the `ServiceMeshControlPlane` resource as a YAML file.
+
[source,terminal]
----
$ oc -n istio-system edit smcp <name> <1>
----
<1>  `<name>` represents the name of the `ServiceMeshControlPlane` resource.

. To run the Istiod component on an infrastructure node, add the `nodeSelector` and the `tolerations` fields to the `spec.runtime.components.pilot.pod` spec in the `ServiceMeshControlPlane` resource.
+
[source,yaml]
----
spec:
  runtime:
    components:
      pilot:
        pod:
          nodeSelector: <1>
            node-role.kubernetes.io/infra: ""
          tolerations: <2>
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra
            value: reserved
          - effect: NoExecute
            key: node-role.kubernetes.io/infra
            value: reserved
----
<1> Ensures that the `Istiod` pod is only scheduled on an infrastructure node.
<2> Ensures that the pod is accepted by the infrastructure node.

. To run Ingress and Egress Gateways on infrastructure nodes, add the `nodeSelector` and the `tolerations` fields to the `spec.gateways.ingress.runtime.pod` spec and the `spec.gateways.egress.runtime.pod` spec in the `ServiceMeshControlPlane` resource.
+
[source,yaml]
----
spec:
  gateways:
    ingress:
      runtime:
        pod:
          nodeSelector: <1>
            node-role.kubernetes.io/infra: ""
          tolerations: <2>
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra
            value: reserved
          - effect: NoExecute
            key: node-role.kubernetes.io/infra
            value: reserved
    egress:
      runtime:
        pod:
          nodeSelector: <1>
            node-role.kubernetes.io/infra: ""
          tolerations: <2>
          - effect: NoSchedule
            key: node-role.kubernetes.io/infra
            value: reserved
          - effect: NoExecute
            key: node-role.kubernetes.io/infra
            value: reserved
----
<1> Ensures that the gateway pod is only scheduled on an infrastructure node
<2> Ensures that the pod is accepted by the infrastructure node.

// Module included in the following assemblies:
//
// * service_mesh/v2x/installing-ossm.adoc

[id="ossm-confirm-smcp-infrastructure-node_{context}"]
= Verifying the {SMProductShortName} control plane is running on infrastructure nodes

.Procedure

* Confirm that the nodes associated with Istiod, Ingress Gateway, and Egress Gateway pods are infrastructure nodes:
+
[source,terminal]
----
$ oc -n istio-system get pods -owide
----

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-create-smcp.adoc

[id="ossm-about-control-plane-and-cluster-wide-deployment_{context}"]
= About control plane and cluster-wide deployments

A cluster-wide deployment contains a {SMProductShortName} Control Plane that monitors resources for an entire cluster. Monitoring resources for an entire cluster closely resembles Istio functionality in that the control plane uses a single query across all namespaces to monitor Istio and Kubernetes resources. As a result, cluster-wide deployments decrease the number of requests sent to the API server.

You can configure the {SMProductShortName} Control Plane for cluster-wide deployments using either the OpenShift Container Platform web console or the CLI.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-create-smcp.adoc

[id="ossm-deploy-cluster-wide-control-plane-console_{context}"]
= Configuring the control plane for cluster-wide deployment with the web console

You can configure the `ServiceMeshControlPlane` resource for cluster-wide deployment using the OpenShift Container Platform web console. In this example, `istio-system` is the name of the {SMProductShortName} control plane project.

.Prerequisites

* The {SMProductName} Operator is installed.
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Create a project named `istio-system`.
+
.. Navigate to *Home* -> *Projects*.
+
.. Click *Create Project*.
+
.. In the *Name* field, enter `istio-system`. The `ServiceMeshControlPlane` resource must be installed in a project that is separate from your microservices and Operators.
+
These steps use `istio-system` as an example. You can deploy the {SMProductShortName} control plane to any project as long as it is separate from the project that contains your services.
+
.. Click *Create*.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator, then click *Istio Service Mesh Control Plane*.

. On the *Istio Service Mesh Control Plane* tab, click *Create ServiceMeshControlPlane*.

. Click *YAML view*. The version of the {SMProductShortName} control plane determines the features available regardless of the version of the Operator.

. Modify the `spec.mode` field of the YAML file to specify `ClusterWide`.
+
.Example version {MaistraVersion} istio-installation.yaml
+
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  version: v{MaistraVersion}
  mode: ClusterWide
----
. Modify the `spec.mode` field and add the `spec.security.identity.type.ThirdParty` field:
+
.Example `ServiceMeshControlPlane` resource
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  version: v{MaistraVersion}
  mode: ClusterWide <1>
  security:
    identity:
      type: ThirdParty <2>
  tracing:
    type: Jaeger
    sampling: 10000
  policy:
    type: Istiod
  addons:
    grafana:
      enabled: true
    jaeger:
      install:
        storage:
          type: Memory
    kiali:
      enabled: true
    prometheus:
      enabled: true
  telemetry:
    type: Istiod
----
<1> Specifies that the resource is for a cluster-wide deployment.
<2> Specifies a required setting for {product-rosa}.
<2> Specifies a required setting for {product-dedicated}.

. Click *Create*. The Operator creates pods, services, and {SMProductShortName} control plane components based on your configuration parameters. The operator also creates the `ServiceMeshMemberRoll` if it does not exist as part of the default configuration.

.Verification

* To verify that the control plane installed correctly:

.. Click the *Istio Service Mesh Control Plane* tab.

.. Click the name of the new `ServiceMeshControlPlane` object.

.. Click the *Resources* tab to see the {SMProductName} control plane resources that the Operator created and configured.

This module is included in the following assemblies:
* service_mesh/v2x/ossm-create-smcp.adoc

[id="ossm-deploy-cluster-wide-control-plane-cli_{context}"]
= Configuring the control plane for cluster-wide deployment with the CLI

You can configure the `ServiceMeshControlPlane` resource for cluster-wide deployment using the CLI. In this example, `istio-system` is the name of the Service Mesh control plane namespace.

.Prerequisites

* The {SMProductName} Operator is installed.
* You have access to the OpenShift CLI (`oc`).
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. Create a project named `istio-system`.
+
[source,terminal]
----
$ oc new-project istio-system
----

. Create a `ServiceMeshControlPlane` file named `istio-installation.yaml` using the following example:
+
.Example version {MaistraVersion} istio-installation.yaml
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  version: v{MaistraVersion}
  mode: ClusterWide
----
.Example `ServiceMeshControlPlane` resource
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
  namespace: istio-system
spec:
  version: v{MaistraVersion}
  mode: ClusterWide <1>
  security:
    identity:
      type: ThirdParty <2>
----
<1> Specifies that the resource is for a cluster-wide deployment.
<2> Specifies a required setting for {product-rosa}.
<2> Specifies a required setting for {product-dedicated}.

. Run the following command to deploy the {SMProductShortName} control plane:
+
[source,terminal]
----
$ oc create -n istio-system -f <istio_installation.yaml>
----
+
where:
+
--
<istio_installation.yaml>:: Specifies the full path to your file.
--

.Verification

. To monitor the progress of the pod deployment, run the following command:
+
[source,terminal]
----
$ oc get pods -n istio-system -w
----
+
You should see output similar to the following example:
+
.Example output
[source,terminal]
----
NAME                                   READY   STATUS    RESTARTS   AGE
grafana-b4d59bd7-mrgbr                 2/2     Running   0          65m
istio-egressgateway-678dc97b4c-wrjkp   1/1     Running   0          108s
istio-ingressgateway-b45c9d54d-4qg6n   1/1     Running   0          108s
istiod-basic-55d78bbbcd-j5556          1/1     Running   0          108s
jaeger-67c75bd6dc-jv6k6                2/2     Running   0          65m
kiali-6476c7656c-x5msp                 1/1     Running   0          43m
prometheus-58954b8d6b-m5std            2/2     Running   0          66m
----

This module is included in the following assemblies:
* service_mesh/v2x/ossm-create-smcp.adoc

[id="ossm-customize-smrr-cluster-wide_{context}"]
= Customizing the member roll for a cluster-wide mesh

In cluster-wide mode, when you create the `ServiceMeshControlPlane` resource, the `ServiceMeshMemberRoll` resource is also created. You can modify the `ServiceMeshMemberRoll` resource after it gets created. After you modify the resource, the {SMProductShortName} operator no longer changes it. If you modify the `ServiceMeshMemberRoll` resource by using the OpenShift Container Platform web console, accept the prompt to overwrite the modifications.

Alternatively, you can create a `ServiceMeshMemberRoll` resource before deploying the `ServiceMeshControlPlane` resource. When you create the `ServiceMeshControlPlane` resource, the {SMProductShortName} Operator will not modify the `ServiceMeshMemberRoll`.

[NOTE]
====
The `ServiceMeshMemberRoll` resource name must be named `default` and must be created in the same project namespace as the `ServiceMeshControlPlane` resource.
====

There are two ways to add a namespace to the mesh. You can either add the namespace by specifying its name in the `spec.members` list, or configure a set of namespace label selectors to include or exclude namespaces based on their labels.

[NOTE]
====
Regardless of how members are specified in the `ServiceMeshMemberRoll` resource, you can also add members to the mesh by creating the `ServiceMeshMember` resource in each namespace.
====

This module is included in the following assemblies:
* service_mesh/v2x/ossm-create-smcp.adoc
[id="ossm-validate-control-plane-kiali_{context}"]
= Validating your SMCP installation with Kiali

You can use the Kiali console to validate your {SMProductShortName} installation. The Kiali console offers several ways to validate your {SMProductShortName} components are deployed and configured properly.

. Prerequisites

* The {SMProductName} Operator must be installed.
* Access to the OpenShift CLI (`oc`).
* You are logged in to OpenShift Container Platform as`cluster-admin`.
* You are logged in to OpenShift Container Platform as a user with the `dedicated-admin` role.

.Procedure

. In the OpenShift Container Platform web console, navigate to *Networking* -> *Routes*.

. On the *Routes* page, select the {SMProductShortName} control plane project, for example `istio-system`, from the *Namespace* menu.
+
The *Location* column displays the linked address for each route.
+
. If necessary, use the filter to find the route for the Kiali console. Click the route *Location* to launch the console.

. Click *Log In With OpenShift*.
+
When you first log in to the Kiali Console, you see the *Overview* page which displays all the namespaces in your service mesh that you have permission to view. When there are multiple namespaces shown on the *Overview* page, Kiali shows namespaces with health or validation problems first.
+
.Kiali Overview page
image::ossm-kiali-overview.png[Kiali Overview page showing istio-system]
+
The tile for each namespace displays the number of labels, the *Istio Config* health, the number of and *Applications* health, and *Traffic* for the namespace. If you are validating the console installation and namespaces have not yet been added to the mesh, there might not be any data to display other than `istio-system`.

. Kiali has four dashboards specifically for the namespace where the {SMProductShortName} control plane is installed.  To view these dashboards, click the Options menu {kebab} on the tile for the control plane namespace, for example, `istio-system`, and select one of the following options:

** *Istio Mesh Dashboard*
** *Istio Control Plane Dashboard*
** *Istio Performance Dashboard*
** *Istio Wasm Exetension Dashboard*
+
.Grafana Istio Control Plane Dashboard
image::ossm-grafana-control-plane-dashboard.png[Istio Control Plane Dashboard showing data for bookinfo sample project]
+
Kiali also installs two additional Grafana dashboards, available from the Grafana *Home* page:
** *Istio Workload Dashboard*
** *Istio Service Dashboard*
+
. To view the {SMProductShortName} control plane nodes, click the *Graph* page, select the *Namespace* where you installed the `ServiceMeshControlPlane` from the menu, for example `istio-system`.

.. If necessary, click *Display idle nodes*.

.. To learn more about the *Graph* page, click the *Graph tour* link.

.. To view the mesh topology, select one or more additional namespaces from the Service Mesh Member Roll from the *Namespace* menu.

. To view the list of applications in the `istio-system` namespace, click the *Applications* page. Kiali displays the health of the applications.

.. Hover your mouse over the information icon to view any additional information noted in the *Details* column.

. To view the list of workloads in the `istio-system` namespace, click the *Workloads* page. Kiali displays the health of the workloads.

.. Hover your mouse over the information icon to view any additional information noted in the *Details* column.

. To view the list of services in the `istio-system` namespace, click the *Services* page. Kiali displays the health of the services and of the configurations.

.. Hover your mouse over the information icon to view any additional information noted in the *Details* column.

. To view a list of the Istio Configuration objects in the `istio-system` namespace, click the *Istio Config* page. Kiali displays the health of the configuration.

.. If there are configuration errors, click the row and Kiali opens the configuration file with the error highlighted.

[role="_additional-resources"]
== Additional resources

{SMProductName} supports multiple independent control planes within the cluster. You can create reusable configurations with `ServiceMeshControlPlane` profiles. For more information, see Creating control plane profiles.

== Next steps

* Add a project to the {SMProductShortName} so that applications can be made available. For more information, see Adding services to a service mesh.
