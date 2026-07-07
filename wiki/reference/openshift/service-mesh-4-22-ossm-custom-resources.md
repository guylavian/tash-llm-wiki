---
title: "Custom resources"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-custom-resources
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-custom-resources
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Custom resources

[id="ossm-custom-resources-v1x"]
= Custom resources

You can customize your {SMProductName} by modifying the default {SMProductShortName} custom resource or by creating a new custom resource.

== Prerequisites
* An account with the `cluster-admin` role.
* Completed the Preparing to install {SMProductName} process.
* Have installed the operators.

// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc

[id="ossm-cr-example-1x_{context}"]
= {SMProductName} custom resources

[NOTE]
====
The `istio-system` project is used as an example throughout the {SMProductShortName} documentation, but you can use other projects as necessary.
====

A _custom resource_ allows you to extend the API in an {SMProductName} project or cluster. When you deploy {SMProductShortName} it creates a default `ServiceMeshControlPlane` that you can modify to change the project parameters.

The {SMProductShortName} operator extends the API by adding the `ServiceMeshControlPlane` resource type, which enables you to create `ServiceMeshControlPlane` objects within projects. By creating a `ServiceMeshControlPlane` object, you instruct the Operator to install a {SMProductShortName} control plane into the project, configured with the parameters you set in the `ServiceMeshControlPlane` object.

This example `ServiceMeshControlPlane` definition contains all of the supported parameters and deploys {SMProductName} {SMProductVersion1x} images based on Red Hat Enterprise Linux (RHEL).

[IMPORTANT]
====
The 3scale Istio Adapter is deployed and configured in the custom resource file. It also requires a working 3scale account (SaaS or On-Premises).
====

.Example istio-installation.yaml

[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
metadata:
  name: basic-install
spec:

  istio:
    global:
      proxy:
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 128Mi

    gateways:
      istio-egressgateway:
        autoscaleEnabled: false
      istio-ingressgateway:
        autoscaleEnabled: false
        ior_enabled: false

    mixer:
      policy:
        autoscaleEnabled: false

      telemetry:
        autoscaleEnabled: false
        resources:
          requests:
            cpu: 100m
            memory: 1G
          limits:
            cpu: 500m
            memory: 4G

    pilot:
      autoscaleEnabled: false
      traceSampling: 100

    kiali:
      enabled: true

    grafana:
      enabled: true

    tracing:
      enabled: true
      jaeger:
        template: all-in-one
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-parameters_{context}"]
= ServiceMeshControlPlane parameters

The following examples illustrate use of the `ServiceMeshControlPlane` parameters and the tables provide additional information about supported parameters.

[IMPORTANT]
====
The resources you configure for {SMProductName} with these parameters, including CPUs, memory, and the number of pods, are based on the configuration of your OpenShift Container Platform cluster. Configure these parameters based on the available resources in your current cluster configuration.
====

// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-istio-global_{context}"]
= Istio global example

Here is an example that illustrates the Istio global parameters for the `ServiceMeshControlPlane` and a description of the available parameters with appropriate values.

[NOTE]
====
In order for the 3scale Istio Adapter to work, `disablePolicyChecks` must be `false`.
====

.Example global parameters
[source,yaml]
----
  istio:
    global:
      tag: 1.1.0
      hub: registry.redhat.io/openshift-service-mesh/
      proxy:
        resources:
          requests:
            cpu: 10m
            memory: 128Mi
          limits:
      mtls:
        enabled: false
      disablePolicyChecks: true
      policyCheckFailOpen: false
      imagePullSecrets:
        - MyPullSecret
----

.Global parameters
|===
|Parameter |Description |Values |Default value

|`disablePolicyChecks`
|This parameter enables/disables policy checks.
|`true`/`false`
|`true`

|`policyCheckFailOpen`
|This parameter indicates whether traffic is allowed to pass through to the Envoy sidecar when the Mixer policy service cannot be reached.
|`true`/`false`
|`false`

|`tag`
|The tag that the Operator uses to pull the Istio images.
|A valid container image tag.
|`1.1.0`

|`hub`
|The hub that the Operator uses to pull Istio images.
|A valid image repository.
|`maistra/` or `registry.redhat.io/openshift-service-mesh/`

|`mtls`
|This parameter controls whether to enable/disable Mutual Transport Layer Security (mTLS) between services by default.
|`true`/`false`
|`false`

|`imagePullSecrets`
|If access to the registry providing the Istio images is secure, list an imagePullSecret here.
|redhat-registry-pullsecret OR quay-pullsecret
|None
|===

These parameters are specific to the proxy subset of global parameters.

.Proxy parameters
|===
|Type |Parameter |Description |Values |Default value

|`requests`
|`cpu`
|The amount of CPU resources requested for Envoy proxy.
|CPU resources, specified in cores or millicores (for example, 200m, 0.5, 1) based on your environment's configuration.
|`10m`

|
|`memory`
|The amount of memory requested for Envoy proxy
|Available memory in bytes(for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`128Mi`

|`limits`
|`cpu`
|The maximum amount of CPU resources requested for Envoy proxy.
|CPU resources, specified in cores or millicores (for example, 200m, 0.5, 1) based on your environment's configuration.
|`2000m`

|
|`memory`
|The maximum amount of memory Envoy proxy is permitted to use.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`1024Mi`
|===

// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-gateway_{context}"]
= Istio gateway configuration

Here is an example that illustrates the Istio gateway parameters for the `ServiceMeshControlPlane` and a description of the available parameters with appropriate values.

.Example gateway parameters
[source,yaml]
----
  gateways:
    egress:
      enabled: true
      runtime:
        deployment:
          autoScaling:
            enabled: true
            maxReplicas: 5
            minReplicas: 1
    enabled: true
    ingress:
      enabled: true
      runtime:
        deployment:
          autoScaling:
            enabled: true
            maxReplicas: 5
            minReplicas: 1
----

.Istio Gateway parameters
|===
|Parameter |Description |Values |Default value

|`gateways.egress.runtime.deployment.autoScaling.enabled`
|This parameter enables/disables autoscaling.
|`true`/`false`
|`true`

|`gateways.egress.runtime.deployment.autoScaling.minReplicas`
|The minimum number of pods to deploy for the egress gateway based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`1`

|`gateways.egress.runtime.deployment.autoScaling.maxReplicas`
|The maximum number of pods to deploy for the egress gateway based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`5`

|`gateways.ingress.runtime.deployment.autoScaling.enabled`
|This parameter enables/disables autoscaling.
|`true`/`false`
|`true`

|`gateways.ingress.runtime.deployment.autoScaling.minReplicas`
|The minimum number of pods to deploy for the ingress gateway based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`1`

|`gateways.ingress.runtime.deployment.autoScaling.maxReplicas`
|The maximum number of pods to deploy for the ingress gateway based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`5`
|===

Cluster administrators can refer to "Using wildcard routes" in Ingress Operator in OpenShift Container Platform for instructions on how to enable subdomains.

// Module included in the following assemblies:
//
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-mixer_{context}"]
= Istio Mixer configuration

Here is an example that illustrates the Mixer parameters for the `ServiceMeshControlPlane` and a description of the available parameters with appropriate values.

.Example mixer parameters
[source,yaml]
----
mixer:
  enabled: true
  policy:
    autoscaleEnabled: false
  telemetry:
    autoscaleEnabled: false
    resources:
    requests:
      cpu: 10m
      memory: 128Mi
      limits:
----

.Istio Mixer policy parameters
|===
|Parameter |Description |Values |Default value

|`enabled`
|This parameter enables/disables Mixer.
|`true`/`false`
|`true`

|`autoscaleEnabled`
|This parameter enables/disables autoscaling. Disable this for small environments.
|`true`/`false`
|`true`

|`autoscaleMin`
|The minimum number of pods to deploy based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`1`

|`autoscaleMax`
|The maximum number of pods to deploy based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`5`
|===

.Istio Mixer telemetry parameters
|===
|Type |Parameter |Description |Values |Default

|`requests`
|`cpu`
|The percentage of CPU resources requested for Mixer telemetry.
|CPU resources in millicores based on your environment's configuration.
|`10m`

|
|`memory`
|The amount of memory requested for Mixer telemetry.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`128Mi`

|`limits`
|`cpu`
|The maximum percentage of CPU resources Mixer telemetry is permitted to use.
|CPU resources in millicores based on your environment's configuration.
|`4800m`

|
|`memory`
|The maximum amount of memory Mixer telemetry is permitted to use.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`4G`
|===

// Module included in the following assemblies:
//
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-pilot_{context}"]
= Istio Pilot configuration

You can configure Pilot to schedule or set limits on resource allocation.
The following example illustrates the Pilot parameters for the `ServiceMeshControlPlane` and a description of the available parameters with appropriate values.

.Example pilot parameters
[source,yaml]
----
spec:
  runtime:
    components:
      pilot:
        deployment:
          autoScaling:
            enabled: true
            minReplicas: 1
            maxReplicas: 5
            targetCPUUtilizationPercentage: 85
        pod:
          tolerations:
          - key: node.kubernetes.io/unreachable
            operator: Exists
            effect: NoExecute
            tolerationSeconds: 60
          affinity:
            podAntiAffinity:
              requiredDuringScheduling:
              - key: istio
                topologyKey: kubernetes.io/hostname
                operator: In
                values:
                - pilot
        container:
          resources:
            limits:
              cpu: 100m
              memory: 128M
----

.Istio Pilot parameters
|===
|Parameter |Description |Values |Default value

|`cpu`
|The percentage of CPU resources requested for Pilot.
|CPU resources in millicores based on your environment's configuration.
|`10m`

|`memory`
|The amount of memory requested for Pilot.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`128Mi`

|`autoscaleEnabled`
|This parameter enables/disables autoscaling. Disable this for small environments.
|`true`/`false`
|`true`

|`traceSampling`
|This value controls how often random sampling occurs. *Note:* Increase for development or testing.
|A valid percentage.
|`1.0`
|===

// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc
[id="configuring-kiali_{context}"]
= Configuring Kiali

When the {SMProductShortName} Operator creates the `ServiceMeshControlPlane` it also processes the Kiali resource. The Kiali Operator then uses this object when creating Kiali instances.

The default Kiali parameters specified in the `ServiceMeshControlPlane` are as follows:

.Example Kiali parameters
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
spec:
    kiali:
      enabled: true
      dashboard:
        viewOnlyMode: false
      ingress:
        enabled: true
----

.Kiali parameters
[options="header"]
[cols="l, a, a, a"]
|===
|Parameter |Description |Values |Default value

|enabled
|This parameter enables/disables Kiali. Kiali is enabled by default.
|`true`/`false`
|`true`

|dashboard
   viewOnlyMode
|This parameter enables/disables view-only mode for the Kiali console.  When view-only mode is enabled, users cannot use the console to make changes to the {SMProductShortName}.
|`true`/`false`
|`false`

|ingress
   enabled
|This parameter enables/disables ingress for Kiali.
|`true`/`false`
|`true`
|===

[id="configuring-kiali-grafana_{context}"]
== Configuring Kiali for Grafana

When you install Kiali and Grafana as part of {SMProductName} the Operator configures the following by default:

* Grafana is enabled as an external service for Kiali
* Grafana authorization for the Kiali console
* Grafana URL for the Kiali console

Kiali can automatically detect the Grafana URL. However if you have a custom Grafana installation that is not easily auto-detectable by Kiali, you must update the URL value in the `ServiceMeshControlPlane` resource.

.Additional Grafana parameters
[source,yaml]
----
spec:
  kiali:
    enabled: true
    dashboard:
      viewOnlyMode: false
      grafanaURL:  "https://grafana-istio-system.127.0.0.1.nip.io"
    ingress:
      enabled: true
----

[id="configuring-kiali-jaeger_{context}"]
== Configuring Kiali for Jaeger

When you install Kiali and Jaeger as part of {SMProductName} the Operator configures the following by default:

* Jaeger is enabled as an external service for Kiali
* Jaeger authorization for the Kiali console
* Jaeger URL for the Kiali console

Kiali can automatically detect the Jaeger URL. However if you have a custom Jaeger installation that is not easily auto-detectable by Kiali, you must update the URL value in the `ServiceMeshControlPlane` resource.

.Additional Jaeger parameters
[source,yaml]
----
spec:
  kiali:
    enabled: true
    dashboard:
      viewOnlyMode: false
      jaegerURL: "http://jaeger-query-istio-system.127.0.0.1.nip.io"
    ingress:
      enabled: true
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-custom-resources.adoc

[id="ossm-configuring-jaeger_{context}"]
= Configuring Jaeger

When the {SMProductShortName} Operator creates the `ServiceMeshControlPlane` resource it can also create the resources for distributed tracing. {SMProductShortName} uses Jaeger for distributed tracing.

You can specify your Jaeger configuration in either of two ways:

* Configure Jaeger in the `ServiceMeshControlPlane` resource. There are some limitations with this approach.

* Configure Jaeger in a custom `Jaeger` resource and then reference that Jaeger instance in the  `ServiceMeshControlPlane` resource. If a Jaeger resource matching the value of `name` exists, the control plane will use the existing installation. This approach lets you fully customize your Jaeger configuration.

The default Jaeger parameters specified in the `ServiceMeshControlPlane` are as follows:

.Default `all-in-one` Jaeger parameters
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
spec:
  version: v1.1
  istio:
    tracing:
      enabled: true
      jaeger:
        template: all-in-one
----

.Jaeger parameters
[options="header"]
[cols="l, a, a, a"]
|===
|Parameter |Description |Values |Default value

|tracing:
   enabled:
|This parameter enables/disables installing and deploying tracing by the Service Mesh Operator. Installing Jaeger is enabled by default.  To use an existing Jaeger deployment, set this value to `false`.
|`true`/`false`
|`true`

|jaeger:
   template:
|This parameter specifies which Jaeger deployment strategy to use.
|* `all-in-one`- For development, testing, demonstrations, and proof of concept.
* `production-elasticsearch` - For production use.
|`all-in-one`
|===

[NOTE]
====
The default template in the `ServiceMeshControlPlane` resource is the `all-in-one` deployment strategy which uses in-memory storage. For production, the only supported storage option is Elasticsearch, therefore you must configure the `ServiceMeshControlPlane` to request the `production-elasticsearch` template when you deploy {SMProductShortName} within a production environment.
====

[id="ossm-configuring-jaeger-elasticsearch_{context}"]
== Configuring Elasticsearch

The default Jaeger deployment strategy uses the `all-in-one` template so that the installation can be completed using minimal resources.  However, because the `all-in-one` template uses in-memory storage, it is only recommended for development, demo, or testing purposes and should NOT be used for production environments.

If you are deploying {SMProductShortName} and Jaeger in a production environment you must change the template to the `production-elasticsearch` template, which uses Elasticsearch for Jaeger's storage needs.

Elasticsearch is a memory intensive application. The initial set of nodes specified in the default OpenShift Container Platform installation may not be large enough to support the Elasticsearch cluster.  You should modify the default Elasticsearch configuration to match your use case and the resources you have requested for your OpenShift Container Platform installation. You can adjust both the CPU and memory limits for each component by modifying the resources block with valid CPU and memory values. Additional nodes must be added to the  cluster if you want to run with the recommended amount (or more) of memory. Ensure that you do not exceed the resources requested for your OpenShift Container Platform installation.

.Default "production" Jaeger parameters with Elasticsearch
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
spec:
  istio:
    tracing:
    enabled: true
    ingress:
      enabled: true
    jaeger:
      template: production-elasticsearch
      elasticsearch:
        nodeCount: 3
        redundancyPolicy:
        resources:
          requests:
            cpu: "1"
            memory: "16Gi"
          limits:
            cpu: "1"
            memory: "16Gi"
----

.Elasticsearch parameters
[options="header"]
[cols="l, a, a, a, a"]
|===
|Parameter |Description |Values |Default Value |Examples

|tracing:
  enabled:
|This parameter enables/disables tracing in {SMProductShortName}. Jaeger is installed by default.
|`true`/`false`
|`true`
|

|ingress:
  enabled:
|This parameter enables/disables ingress for Jaeger.
|`true`/`false`
|`true`
|

|jaeger:
   template:
|This parameter specifies which Jaeger deployment strategy to use.
|`all-in-one`/`production-elasticsearch`
|`all-in-one`
|

|elasticsearch:
  nodeCount:
|Number of Elasticsearch nodes to create.
|Integer value.
|1
|Proof of concept = 1,
Minimum deployment =3

|requests:
  cpu:
|Number of central processing units for requests, based on your environment's configuration.
|Specified in cores or millicores (for example, 200m, 0.5, 1).
|1Gi
|Proof of concept = 500m,
Minimum deployment =1

|requests:
  memory:
|Available memory for requests, based on your environment's configuration.
|Specified in bytes (for example, 200Ki, 50Mi, 5Gi).
|500m
|Proof of concept = 1Gi,
Minimum deployment = 16Gi*

|limits:
  cpu:
|Limit on number of central processing units, based on your environment's configuration.
|Specified in cores or millicores (for example, 200m, 0.5, 1).
|
|Proof of concept = 500m,
Minimum deployment =1

|limits:
  memory:
|Available memory limit based on your environment's configuration.
|Specified in bytes (for example, 200Ki, 50Mi, 5Gi).
|
|Proof of concept = 1Gi,
Minimum deployment = 16Gi*

|
4+|{asterisk} Each Elasticsearch node can operate with a lower memory setting though this is *not* recommended for production deployments. For production use, you should have no less than 16Gi allocated to each pod by default, but preferably allocate as much as you can, up to 64Gi per pod.
|===

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator.

. Click the *Istio Service Mesh Control Plane* tab.

. Click the name of your control plane file, for example, `basic-install`.

. Click the *YAML* tab.

. Edit the Jaeger parameters, replacing the default `all-in-one` template with parameters for the `production-elasticsearch` template, modified for your use case.  Ensure that the indentation is correct.

. Click *Save*.

. Click *Reload*.
OpenShift Container Platform redeploys Jaeger and creates the Elasticsearch resources based on the specified parameters.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-custom-resources.adoc

[id="ossm-configuring-jaeger-existing-v1x_{context}"]
= Connecting to an existing Jaeger instance

In order for the SMCP to connect to an existing Jaeger instance, the following must be true:

* The Jaeger instance is deployed in the same namespace as the control plane, for example, into the `istio-system` namespace.

* To enable secure communication between services, you should enable the oauth-proxy, which secures communication to your Jaeger instance, and make sure the secret is mounted into your Jaeger instance so Kiali can communicate with it.

* To use a custom or already existing Jaeger instance, set `spec.istio.tracing.enabled` to "false" to disable the deployment of a Jaeger instance.

* Supply the correct jaeger-collector endpoint to Mixer by setting `spec.istio.global.tracer.zipkin.address` to the hostname and port of your jaeger-collector service. The hostname of the service is usually `<jaeger-instance-name>-collector.<namespace>.svc.cluster.local`.

* Supply the correct jaeger-query endpoint to Kiali for gathering traces by setting `spec.istio.kiali.jaegerInClusterURL` to the hostname of your jaeger-query service - the port is normally not required, as it uses 443 by default. The hostname of the service is usually  `<jaeger-instance-name>-query.<namespace>.svc.cluster.local`.

* Supply the dashboard URL of your Jaeger instance to Kiali to enable accessing Jaeger through the Kiali console. You can retrieve the URL from the OpenShift route that is created by the Jaeger Operator. If your Jaeger resource is called `external-jaeger` and resides in the `istio-system` project, you can retrieve the route using the following command:
+
[source,terminal]
----
$ oc get route -n istio-system external-jaeger
----
+
.Example output
[source,terminal]
----
NAME                   HOST/PORT                                     PATH   SERVICES               [...]
external-jaeger        external-jaeger-istio-system.apps.test        external-jaeger-query  [...]
----
+
The value under `HOST/PORT` is the externally accessible URL of the Jaeger dashboard.

.Example Jaeger resource
[source,yaml]
----
apiVersion: jaegertracing.io/v1
kind: "Jaeger"
metadata:
  name: "external-jaeger"
  # Deploy to the Control Plane Namespace
  namespace: istio-system
spec:
  # Set Up Authentication
  ingress:
    enabled: true
    security: oauth-proxy
    openshift:
      # This limits user access to the Jaeger instance to users who have access
      # to the control plane namespace. Make sure to set the correct namespace here
      sar: '{"namespace": "istio-system", "resource": "pods", "verb": "get"}'
      htpasswdFile: /etc/proxy/htpasswd/auth

  volumeMounts:
  - name: secret-htpasswd
    mountPath: /etc/proxy/htpasswd
  volumes:
  - name: secret-htpasswd
    secret:
      secretName: htpasswd

----

The following `ServiceMeshControlPlane` example assumes that you have deployed Jaeger using the Jaeger Operator and the example Jaeger resource.

.Example `ServiceMeshControlPlane` with external Jaeger
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
metadata:
  name: external-jaeger
  namespace: istio-system
spec:
  version: v1.1
  istio:
    tracing:
      # Disable Jaeger deployment by service mesh operator
      enabled: false
    global:
      tracer:
        zipkin:
          # Set Endpoint for Trace Collection
          address: external-jaeger-collector.istio-system.svc.cluster.local:9411
    kiali:
      # Set Jaeger dashboard URL
      dashboard:
        jaegerURL: https://external-jaeger-istio-system.apps.test
      # Set Endpoint for Trace Querying
      jaegerInClusterURL: external-jaeger-query.istio-system.svc.cluster.local
----

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-custom-resources.adoc

[id="ossm-jaeger-config-elasticsearch-v1x_{context}"]
= Configuring Elasticsearch

The default Jaeger deployment strategy uses the `all-in-one` template so that the installation can be completed using minimal resources.  However, because the `all-in-one` template uses in-memory storage, it is only recommended for development, demo, or testing purposes and should NOT be used for production environments.

If you are deploying {SMProductShortName} and Jaeger in a production environment you must change the template to the `production-elasticsearch` template, which uses Elasticsearch for Jaeger's storage needs.

Elasticsearch is a memory intensive application. The initial set of nodes specified in the default OpenShift Container Platform installation may not be large enough to support the Elasticsearch cluster.  You should modify the default Elasticsearch configuration to match your use case and the resources you have requested for your OpenShift Container Platform installation. You can adjust both the CPU and memory limits for each component by modifying the resources block with valid CPU and memory values. Additional nodes must be added to the  cluster if you want to run with the recommended amount (or more) of memory. Ensure that you do not exceed the resources requested for your OpenShift Container Platform installation.

.Default "production" Jaeger parameters with Elasticsearch
[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
spec:
  istio:
    tracing:
    enabled: true
    ingress:
      enabled: true
    jaeger:
      template: production-elasticsearch
      elasticsearch:
        nodeCount: 3
        redundancyPolicy:
        resources:
          requests:
            cpu: "1"
            memory: "16Gi"
          limits:
            cpu: "1"
            memory: "16Gi"
----

.Elasticsearch parameters
[options="header"]
[cols="l, a, a, a, a"]
|===
|Parameter |Description |Values |Default Value |Examples

|tracing:
  enabled:
|This parameter enables/disables tracing in {SMProductShortName}. Jaeger is installed by default.
|`true`/`false`
|`true`
|

|ingress:
  enabled:
|This parameter enables/disables ingress for Jaeger.
|`true`/`false`
|`true`
|

|jaeger:
   template:
|This parameter specifies which Jaeger deployment strategy to use.
|`all-in-one`/`production-elasticsearch`
|`all-in-one`
|

|elasticsearch:
  nodeCount:
|Number of Elasticsearch nodes to create.
|Integer value.
|1
|Proof of concept = 1,
Minimum deployment =3

|requests:
  cpu:
|Number of central processing units for requests, based on your environment's configuration.
|Specified in cores or millicores (for example, 200m, 0.5, 1).
|1Gi
|Proof of concept = 500m,
Minimum deployment =1

|requests:
  memory:
|Available memory for requests, based on your environment's configuration.
|Specified in bytes (for example, 200Ki, 50Mi, 5Gi).
|500m
|Proof of concept = 1Gi,
Minimum deployment = 16Gi*

|limits:
  cpu:
|Limit on number of central processing units, based on your environment's configuration.
|Specified in cores or millicores (for example, 200m, 0.5, 1).
|
|Proof of concept = 500m,
Minimum deployment =1

|limits:
  memory:
|Available memory limit based on your environment's configuration.
|Specified in bytes (for example, 200Ki, 50Mi, 5Gi).
|
|Proof of concept = 1Gi,
Minimum deployment = 16Gi*

|
4+|{asterisk} Each Elasticsearch node can operate with a lower memory setting though this is *not* recommended for production deployments. For production use, you should have no less than 16Gi allocated to each pod by default, but preferably allocate as much as you can, up to 64Gi per pod.
|===

.Procedure

. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.

. Navigate to *Ecosystem* -> *Installed Operators*.

. Click the {SMProductName} Operator.

. Click the *Istio Service Mesh Control Plane* tab.

. Click the name of your control plane file, for example, `basic-install`.

. Click the *YAML* tab.

. Edit the Jaeger parameters, replacing the default `all-in-one` template with parameters for the `production-elasticsearch` template, modified for your use case.  Ensure that the indentation is correct.

. Click *Save*.

. Click *Reload*.
OpenShift Container Platform redeploys Jaeger and creates the Elasticsearch resources based on the specified parameters.

// Module included in the following assemblies:
//
// * service_mesh/v1x/ossm-custom-resources.adoc

[id="ossm-jaeger-config-es-cleaner-v1x_{context}"]
= Configuring the Elasticsearch index cleaner job

When the {SMProductShortName} Operator creates the `ServiceMeshControlPlane` it also creates the custom resource (CR) for Jaeger. The {JaegerName} Operator then uses this CR when creating Jaeger instances.

When using Elasticsearch storage, by default a job is created to clean old traces from it. To configure the options for this job, you edit the Jaeger custom resource (CR), to customize it for your use case. The relevant options are listed below.

[source,yaml]
----
  apiVersion: jaegertracing.io/v1
  kind: Jaeger
  spec:
    strategy: production
    storage:
      type: elasticsearch
      esIndexCleaner:
        enabled: false
        numberOfDays: 7
        schedule: "55 23 * * *"
----

.Elasticsearch index cleaner parameters
|===
|Parameter |Values |Description

|enabled:
|true/ false
|Enable or disable the index cleaner job.

|numberOfDays:
|integer value
|Number of days to wait before deleting an index.

|schedule:
|"55 23 * * *"
|Cron expression for the job to run
|===

// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-threescale_{context}"]

= 3scale configuration

The following table explains the parameters for the 3scale Istio Adapter in the `ServiceMeshControlPlane` resource.

.Example 3scale parameters
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  addons:
    3Scale:
      enabled: false
      PARAM_THREESCALE_LISTEN_ADDR: 3333
      PARAM_THREESCALE_LOG_LEVEL: info
      PARAM_THREESCALE_LOG_JSON: true
      PARAM_THREESCALE_LOG_GRPC: false
      PARAM_THREESCALE_REPORT_METRICS: true
      PARAM_THREESCALE_METRICS_PORT: 8080
      PARAM_THREESCALE_CACHE_TTL_SECONDS: 300
      PARAM_THREESCALE_CACHE_REFRESH_SECONDS: 180
      PARAM_THREESCALE_CACHE_ENTRIES_MAX: 1000
      PARAM_THREESCALE_CACHE_REFRESH_RETRIES: 1
      PARAM_THREESCALE_ALLOW_INSECURE_CONN: false
      PARAM_THREESCALE_CLIENT_TIMEOUT_SECONDS: 10
      PARAM_THREESCALE_GRPC_CONN_MAX_SECONDS: 60
      PARAM_USE_CACHED_BACKEND: false
      PARAM_BACKEND_CACHE_FLUSH_INTERVAL_SECONDS: 15
      PARAM_BACKEND_CACHE_POLICY_FAIL_CLOSED: true
# ...
----

.3scale parameters
|===
|Parameter |Description |Values |Default value

|`enabled`
|Whether to use the 3scale adapter
|`true`/`false`
|`false`

|`PARAM_THREESCALE_LISTEN_ADDR`
|Sets the listen address for the gRPC server
|Valid port number
|`3333`

|`PARAM_THREESCALE_LOG_LEVEL`
|Sets the minimum log output level.
|`debug`, `info`, `warn`, `error`, or `none`
|`info`

|`PARAM_THREESCALE_LOG_JSON`
|Controls whether the log is formatted as JSON
|`true`/`false`
|`true`

|`PARAM_THREESCALE_LOG_GRPC`
|Controls whether the log contains gRPC info
|`true`/`false`
|`true`

|`PARAM_THREESCALE_REPORT_METRICS`
|Controls whether 3scale system and backend metrics are collected and reported to Prometheus
|`true`/`false`
|`true`

|`PARAM_THREESCALE_METRICS_PORT`
|Sets the port that the 3scale `/metrics` endpoint can be scrapped from
|Valid port number
|`8080`

|`PARAM_THREESCALE_CACHE_TTL_SECONDS`
|Time period, in seconds, to wait before purging expired items from the cache
|Time period in seconds
|`300`

|`PARAM_THREESCALE_CACHE_REFRESH_SECONDS`
|Time period before expiry when cache elements are attempted to be refreshed
|Time period in seconds
|`180`

|`PARAM_THREESCALE_CACHE_ENTRIES_MAX`
|Max number of items that can be stored in the cache at any time. Set to `0` to disable caching
|Valid number
|`1000`

|`PARAM_THREESCALE_CACHE_REFRESH_RETRIES`
|The number of times unreachable hosts are retried during a cache update loop
|Valid number
|`1`

|`PARAM_THREESCALE_ALLOW_INSECURE_CONN`
|Allow to skip certificate verification when calling `3scale` APIs. Enabling this is not recommended.
|`true`/`false`
|`false`

|`PARAM_THREESCALE_CLIENT_TIMEOUT_SECONDS`
|Sets the number of seconds to wait before terminating requests to 3scale System and Backend
|Time period in seconds
|`10`

|`PARAM_THREESCALE_GRPC_CONN_MAX_SECONDS`
|Sets the maximum amount of seconds (+/-10% jitter) a connection may exist before it is closed
|Time period in seconds
|60

|`PARAM_USE_CACHE_BACKEND`
|If true, attempt to create an in-memory apisonator cache for authorization requests
|`true`/`false`
|`false`

|`PARAM_BACKEND_CACHE_FLUSH_INTERVAL_SECONDS`
|If the backend cache is enabled, this sets the interval in seconds for flushing the cache against 3scale
|Time period in seconds
|15

|`PARAM_BACKEND_CACHE_POLICY_FAIL_CLOSED`
|Whenever the backend cache cannot retrieve authorization data, whether to deny (closed) or allow (open) requests
|`true`/`false`
|`true`
|===
