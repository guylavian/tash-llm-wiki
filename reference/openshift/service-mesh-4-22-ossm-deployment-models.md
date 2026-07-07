---
title: "Service mesh deployment models"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-deployment-models
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-deployment-models
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Service mesh deployment models

[id="ossm-deployment-models"]
= Service mesh deployment models

{SMProductName} supports several different deployment models that can be combined in different ways to best suit your business requirements.

In Istio, a tenant is a group of users that share common access and privileges for a set of deployed workloads. You can use tenants to provide a level of isolation between different teams. You can segregate access to different tenants using `NetworkPolicies`, `AuthorizationPolicies`, and `exportTo` annotations on istio.io or service resources.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-deploy-cluster-wide-mesh_{context}"]
= Cluster-Wide (Single Tenant) mesh deployment model

A cluster-wide deployment contains a Service Mesh Control Plane that monitors resources for an entire cluster. Monitoring resources for an entire cluster closely resembles Istio functionality in that the control plane uses a single query across all namespaces to monitor Istio and Kubernetes resources. As a result, cluster-wide deployments decrease the number of requests sent to the API server.

Similar to Istio, a cluster-wide mesh includes namespaces with the `istio-injection=enabled` namespace label by default. You can change this label by modifying the `spec.memberSelectors` field of the `ServiceMeshMemberRoll` resource.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deploy-mod-v2x.adoc

[id="ossm-deploy-multitenant_{context}"]
= Multitenant deployment model

{SMProductName} installs a `ServiceMeshControlPlane` that is configured for multitenancy by default. {SMProductName} uses a multitenant Operator to manage the {SMProductShortName} control plane lifecycle. Within a mesh, namespaces are used for tenancy.

{SMProductName} uses `ServiceMeshControlPlane` resources to manage mesh installations, whose scope is limited by default to namespace that contains the resource. You use `ServiceMeshMemberRoll` and `ServiceMeshMember` resources to include additional namespaces into the mesh. A namespace can only be included in a single mesh, and multiple meshes can be installed in a single OpenShift cluster.

Typical service mesh deployments use a single {SMProductShortName} control plane to configure communication between services in the mesh. {SMProductName} supports “soft multitenancy”, where there is one control plane and one mesh per tenant, and there can be multiple independent control planes within the cluster. Multitenant deployments specify the projects that can access the {SMProductShortName} and isolate the {SMProductShortName} from other control plane instances.

The cluster administrator gets control and visibility across all the Istio control planes, while the tenant administrator only gets control over their specific {SMProductShortName}, Kiali, and Jaeger instances.

You can grant a team permission to deploy its workloads only to a given namespace or set of namespaces. If granted the `mesh-user` role by the service mesh administrator, users can create a `ServiceMeshMember` resource to add namespaces to the `ServiceMeshMemberRoll`.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-about-about-migrating-to-cluster-wide_{context}"]
= About migrating to a cluster-wide mesh

In a cluster-wide mesh, one `ServiceMeshControlPlane` (SMCP) watches all of the namespaces for an entire cluster. You can migrate an existing cluster from a multitenant mesh to a cluster-wide mesh using {SMProductName} version 2.5 or later.

[NOTE]
====
If a cluster must have more than one SMCP, then you cannot migrate to a cluster-wide mesh.
====

By default, a cluster-wide mesh discovers all of the namespaces that comprise a cluster. However, you can configure the mesh to access a limited set of namespaces. Namespaces do not receive sidecar injection by default. You must specify which namespaces receive sidecar injection.

Similarly, you must specify which pods receive sidecar injection. Pods that exist in a namespace that receives sidecar injection do not inherit sidecar injection. Applying sidecar injection to namespaces and to pods are separate operations.

If you change the Istio version when migrating to a cluster-wide mesh, then you must restart the applications. If you use the same Istio version, the application proxies will connect to the new SMCP for the cluster-wide mesh, and work the same way they did for a multitenant mesh.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-excluding-namespaces-from-cluster-wide-mesh-console_{context}"]
= Including and excluding namespaces from a cluster-wide mesh by using the web console

Using the OpenShift Container Platform web console, you can add discovery selectors to the `ServiceMeshControlPlane` resource in a cluster-wide mesh. Discovery selectors define the namespaces that the control plane can discover. The control plane ignores any namespace that does not match one of the discovery selectors, which excludes the namespace from the mesh.

[NOTE]
====
If you install ingress or egress gateways in the control plane namespace, you must include the control plane namespace in the discovery selectors.
====

.Prerequisites

* You have installed the {SMProductName} Operator.
* You have deployed a `ServiceMeshControlPlane` resource.
* You are logged in as a user with the `cluster-admin` role. If you use {product-dedicated}, you are logged in as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator.

. Click *Istio Service Mesh Control Plane*.

. Click the name of the control plane.

. Click *YAML*.

. Modify the YAML file so that the `spec.meshConfig` field of the `ServiceMeshControlPlane` resource includes the discovery selector.
+
[NOTE]
====
When configuring namespaces that the `Istiod` service can discover, exclude namespaces that might contain sensitive services that should not be exposed to the rest of the mesh.
====
+
In the following example, the `Istiod` service discovers any namespace that is labeled `istio-discovery: enabled` or any namespace that has the name `bookinfo`, `httpbin` or `istio-system`:
+
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  mode: ClusterWide
  meshConfig:
    discoverySelectors:
    - matchLabels:
        istio-discovery: enabled <1>
    - matchExpressions:
      - key: kubernetes.io/metadata.name <2>
        operator: In
        values:
        - bookinfo
        - httpbin
        - istio-system
----
<1> Ensures that the mesh discovers namespaces that contain the label `istio-discovery: enabled`.
<2> Ensures that the mesh discovers namespaces `bookinfo`, `httpbin` and `istio-system`.
+
If a namespace matches any of the discovery selectors, then the mesh discovers the namespace. The mesh excludes namespaces that do not match any of the discovery selectors.

. Save the file.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-excluding-namespaces-from-cluster-wide-mesh-cli_{context}"]
= Including and excluding namespaces from a cluster-wide mesh by using the CLI

Using the OpenShift Container Platform CLI, you can add discovery selectors to the `ServiceMeshControlPlane` resource in a cluster-wide mesh. Discovery selectors define the namespaces that the control plane can discover. The control plane ignores any namespace that does not match one of the discovery selectors, which excludes the namespace from the mesh.

[NOTE]
====
If you install ingress or egress gateways in the control plane namespace, you must include the control plane namespace in the discovery selectors.
====

.Prerequisites

* You have installed the {SMProductName} Operator.
* You have deployed a `ServiceMeshControlPlane` resource.
* You are logged in as a user with the `cluster-admin` role. If you use {product-dedicated}, you are logged in as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Open the `ServiceMeshControlPlane` resource as a YAML file by running the following command:
+
[source,terminal]
----
$ oc -n istio-system edit smcp <name> <1>
----
<1> `<name>` represents the name of the `ServiceMeshControlPlane` resource.

. Modify the YAML file so that the `spec.meshConfig` field of the `ServiceMeshControlPlane` resource includes the discovery selector.
+
[NOTE]
====
When configuring namespaces that the `Istiod` service can discover, exclude namespaces that might contain sensitive services that should not be exposed to the rest of the mesh.
====
+
In the following example, the `Istiod` service discovers any namespace that is labeled `istio-discovery: enabled` or any namespace that has the name `bookinfo`, `httpbin` or `istio-system`:
+
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  mode: ClusterWide
  meshConfig:
    discoverySelectors:
    - matchLabels:
        istio-discovery: enabled <1>
    - matchExpressions:
      - key: kubernetes.io/metadata.name <2>
        operator: In
        values:
        - bookinfo
        - httpbin
        - istio-system
----
<1> Ensures that the mesh discovers namespaces that contain the label `istio-discovery: enabled`.
<2> Ensures that the mesh discovers namespaces `bookinfo`, `httpbin` and `istio-system`.
+
If a namespace matches any of the discovery selectors, then the mesh discovers the namespace. The mesh excludes namespaces that do not match any of the discovery selectors.

. Save the file and exit the editor.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-defining-namespace-receive-sidecar-injection-cluster-wide-mesh-console_{context}"]
= Defining which namespaces receive sidecar injection in a cluster-wide mesh by using the web console

By default, the {SMProductName} Operator uses member selectors to identify which namespaces receive sidecar injection. Namespaces that do not match the `istio-injection=enabled` label as defined in the `ServiceMeshMemberRoll` resource do not receive sidecar injection.

[NOTE]
====
Using discovery selectors to determine which namespaces the mesh can discover has no effect on sidecar injection. Discovering namespaces and configuring sidecar injection are separate operations.
====

.Prerequisites

* You have installed the {SMProductName} Operator.
* You have deployed a `ServiceMeshControlPlanae` resource with the `mode: ClusterWide` annotation.
* You are logged in as a user with the `cluster-admin` role. If you use {product-dedicated}, you are logged in as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator.

. Click *Istio Service Mesh Member Roll*.

. Click the `ServiceMeshMemberRoll` resource.

. Click *YAML*.

. Modify the `spec.memberSelectors` field in the `ServiceMeshMemberRoll` resource by adding a member selector that matches the `inject` label. The following example uses `istio-injection: enabled`:
+
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
spec:
  memberSelectors:
  - matchLabels:
      istio-injection: enabled <1>
----
<1> Ensures that the namespace receives sidecar injection.

. Save the file.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-defining-namespace-receive-sidecar-injection-cluster-wide-mesh-cli_{context}"]
= Defining which namespaces receive sidecar injection in a cluster-wide mesh by using the CLI

By default, the {SMProductName} Operator uses member selectors to identify which namespaces receive sidecar injection. Namespaces that do not match the `istio-injection=enabled` label as defined in the `ServiceMeshMemberRoll` resource do not receive sidecar injection.

[NOTE]
====
Using discovery selectors to determine which namespaces the mesh can discover has no effect on sidecar injection. Discovering namespaces and configuring sidecar injection are separate operations.
====

.Prerequisites

* You have installed the {SMProductName} Operator.
* You have deployed a `ServiceMeshControlPlanae` resource with the `mode: ClusterWide` annotation.
* You are logged in as a user with the `cluster-admin` role. If you use {product-dedicated}, you are logged in as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Edit the `ServiceMeshMemberRoll` resource.
+
[source,terminal]
----
$ oc edit smmr -n <controlplane-namespace>
----

. Modify the `spec.memberSelectors` field in the `ServiceMeshMemberRoll` resource by adding a member selector that matches the `inject` label. The following example uses `istio-injection: enabled`:
+
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshMemberRoll
metadata:
  name: default
spec:
  memberSelectors:
  - matchLabels:
      istio-injection: enabled <1>
----
<1> Ensures that the namespace receives sidecar injection.

. Save the file and exit the editor.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-excluding-individual-pods-from-cluster-wide-mesh-console_{context}"]
= Excluding individual pods from a cluster-wide mesh by using the web console

A pod receives sidecar injection if it has the `sidecar.istio.io/inject: true` annotation applied, and the pod exists in a namespace that matches either the label selector or the members list defined in the `ServiceMeshMemberRoll` resource.

If a pod does not have the `sidecar.istio.io/inject` annotation applied, it cannot receive sidecar injection.

.Prerequisites

* You have installed the {SMProductName} Operator.
* You have deployed a `ServiceMeshControlPlane` resource with the `mode: ClusterWide` annotation.
* You are logged in as a user with the `cluster-admin` role. If you use {product-dedicated}, you are logged in as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform web console.

. Navigate to *Workloads* -> *Deployments*.

. Click the name of the deployment.

. Click *YAML*.

. Modify the YAML file to deploy one application that receives sidecar injection and one that does not, as shown in the following example:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      annotations:
        sidecar.istio.io/inject: 'true' <1>
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-without-sidecar
spec:
  selector:
    matchLabels:
      app: nginx-without-sidecar
  template:
    metadata:
      labels:
        app: nginx-without-sidecar <2>
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
----
<1> This pod has the `sidecar.istio.io/inject` annotation applied, so it receives sidecar injection.
<2> This pod does not have the annotation, so it does not receive sidecar injection.

. Save the file.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deployment-models.adoc

[id="ossm-excluding-individual-pods-from-cluster-wide-mesh-cli_{context}"]
= Excluding individual pods from a cluster-wide mesh by using the CLI

A pod receives sidecar injection if it has the `sidecar.istio.io/inject: true` annotation applied, and the pod exists in a namespace that matches either the label selector or the members list defined in the `ServiceMeshMemberRoll` resource.

If a pod does not have the `sidecar.istio.io/inject` annotation applied, it cannot receive sidecar injection.

.Prerequisites

* You have installed the {SMProductName} Operator.
* You have deployed a `ServiceMeshControlPlane` resource with the `mode: ClusterWide` annotation.
* You are logged in as a user with the `cluster-admin` role. If you use {product-dedicated}, you are logged in as a user with the `dedicated-admin` role.

.Procedure

. Log in to the OpenShift Container Platform CLI.

. Edit the deployment by running the following command:
+
[source,terminal]
----
$ oc edit deployment -n <namespace> <deploymentName>
----

. Modify the YAML file to deploy one application that receives sidecar injection and one that does not, as shown in the following example:
+
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      annotations:
        sidecar.istio.io/inject: 'true' <1>
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-without-sidecar
spec:
  selector:
    matchLabels:
      app: nginx-without-sidecar
  template:
    metadata:
      labels:
        app: nginx-without-sidecar <2>
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
----
<1> This pod has the `sidecar.istio.io/inject` annotation applied, so it receives sidecar injection.
<2> This pod does not have the annotation, so it does not receive sidecar injection.

. Save the file.

// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deploy-mod-v2x.adoc

[id="ossm-deploy-multi-mesh_{context}"]
= Multimesh or federated deployment model

_Federation_ is a deployment model that lets you share services and workloads between separate meshes managed in distinct administrative domains.

The Istio multi-cluster model requires a high level of trust between meshes and remote access to all Kubernetes API servers on which the individual meshes reside. {SMProductName} federation takes an opinionated approach to a multi-cluster implementation of Service Mesh that assumes _minimal_ trust between meshes.

A _federated mesh_ is a group of meshes behaving as a single mesh. The services in each mesh can be unique services, for example a mesh adding services by importing them from another mesh, can provide additional workloads for the same services across the meshes, providing high availability, or a combination of both. All meshes that are joined into a federated mesh remain managed individually, and you must explicitly configure which services are exported to and imported from other meshes in the federation. Support functions such as certificate generation, metrics and trace collection remain local in their respective meshes.
