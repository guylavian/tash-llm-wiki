---
title: "Ingress Operator in {product-title}"
type: reference
domain: openshift
slug: networking-4-22-ingress-operator
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/ingress-operator
version: 4.22
family: networking
documentKind: "Documentation"
---

# Ingress Operator in {product-title}

[id="configuring-ingress"]
= Ingress Operator in OpenShift Container Platform

The Ingress Operator implements the `IngressController` API and is the component responsible for enabling external access to OpenShift Container Platform cluster services.

This Operator is installed on OpenShift Container Platform clusters by default.

// Module included in the following assemblies:
// * networking/networking_operators/ingress-operator.adoc
// * understanding-networking.adoc

[id="nw-ne-openshift-ingress_{context}"]
= OpenShift Container Platform Ingress Operator

When you create your OpenShift Container Platform cluster, pods and services running on the cluster are each allocated their own IP addresses. The IP addresses are accessible to other pods and services running nearby but are not accessible to outside clients.

The Ingress Operator makes it possible for external clients to access your service by deploying and managing one or more HAProxy-based
Ingress Controllers to handle routing. You can use the Ingress Operator to route traffic by specifying OpenShift Container Platform `Route` and Kubernetes `Ingress` resources. Configurations within the Ingress Controller, such as the ability to define `endpointPublishingStrategy` type and internal load balancing, provide ways to publish Ingress Controller endpoints.

The Ingress Operator makes it possible for external clients to access your service by deploying and managing one or more HAProxy-based Ingress Controllers to handle routing.

Red Hat Site Reliability Engineers (SRE) manage the Ingress Operator for OpenShift Container Platform clusters. While you cannot alter the settings for the Ingress Operator, you may view the default Ingress Controller configurations, status, and logs as well as the Ingress Operator status.

// Module included in the following assemblies:
//
// * networking/ingress/configuring_ingress_operator.adoc

[id="nw-installation-ingress-config-asset_{context}"]
= The Ingress configuration asset

The installation program generates an asset with an `Ingress` resource in the `config.openshift.io` API group, `cluster-ingress-02-config.yml`.

.YAML Definition of the `Ingress` resource
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
spec:
  domain: apps.openshiftdemos.com
----

The installation program stores this asset in the `cluster-ingress-02-config.yml` file in the `manifests/` directory. This `Ingress` resource defines the cluster-wide configuration for Ingress. This Ingress configuration is used as follows:

* The Ingress Operator uses the domain from the cluster Ingress configuration as the domain for the default Ingress Controller.

* The OpenShift API Server Operator uses the domain from the cluster Ingress configuration. This domain is also used when generating a default host for a `Route` resource that does not specify an explicit host.

// Ingress Controller configuration parameters
// Module included in the following assemblies:
//
// * ingress/ingress-operator.adoc

[id="nw-ingress-controller-configuration-parameters_{context}"]
= Ingress Controller configuration parameters

The `IngressController` custom resource (CR) includes optional configuration parameters that you can configure to meet specific needs for your organization.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`domain`
|`domain` is a DNS name serviced by the Ingress Controller and is used to configure multiple features:

* For the `LoadBalancerService` endpoint publishing strategy, `domain` is used to configure DNS records. See `endpointPublishingStrategy`.

* When using a generated default certificate, the certificate is valid for `domain` and its `subdomains`. See `defaultCertificate`.

* The value is published to individual Route statuses so that users know where to target external DNS records.

The `domain` value must be unique among all Ingress Controllers and cannot be updated.

If empty, the default value is `ingress.config.openshift.io/cluster` `.spec.domain`.

|`replicas`
|`replicas` is the number of Ingress Controller replicas. If not set, the default value is `2`.

|`endpointPublishingStrategy`
|`endpointPublishingStrategy` is used to publish the Ingress Controller endpoints to other networks, enable load balancer integrations, and provide access to other systems.

For cloud environments, use the `loadBalancer` field to configure the endpoint publishing strategy for your Ingress Controller.

On {gcp-short}, AWS, and Azure you can configure the following `endpointPublishingStrategy` fields:

You can configure the following `endpointPublishingStrategy` fields:

* `loadBalancer.scope`
* `loadBalancer.allowedSourceRanges`

If not set, the default value is based on `infrastructure.config.openshift.io/cluster` `.status.platform`:

* Amazon Web Services (AWS): `LoadBalancerService` (with External scope)
* {gcp-first}: `LoadBalancerService` (with External scope)
* Azure: `LoadBalancerService` (with External scope)
* {gcp-first}: `LoadBalancerService` (with External scope)

For most platforms, the `endpointPublishingStrategy` value can be updated. On {gcp-short}, you can configure the following `endpointPublishingStrategy` fields:

* `loadBalancer.scope`
* `loadbalancer.providerParameters.gcp.clientAccess`

For non-cloud environments, such as a bare-metal platform, use the `NodePortService`, `HostNetwork`, or `Private` fields to configure the endpoint publishing strategy for your Ingress Controller.

If you do not set a value in one of these fields, the default value is based on binding ports specified in the `.status.platform` value in the `IngressController` CR.

If you need to update the `endpointPublishingStrategy` value after your cluster is deployed, you can configure the following `endpointPublishingStrategy` fields:

* `hostNetwork.protocol`
* `nodePort.protocol`
* `private.protocol`

|`defaultCertificate`
|The `defaultCertificate` value is a reference to a secret that contains the default certificate that is served by the Ingress Controller. When Routes do not specify their own certificate, `defaultCertificate` is used.

The secret must contain the following keys and data:
* `tls.crt`: certificate file contents
* `tls.key`: key file contents

If not set, a wildcard certificate is automatically generated and used. The certificate is valid for the Ingress Controller `domain` and `subdomains`, and
the generated certificate's CA is automatically integrated with the
cluster's trust store.

The in-use certificate, whether generated or user-specified, is automatically integrated with OpenShift Container Platform built-in OAuth server.

|`namespaceSelector`
|`namespaceSelector` is used to filter the set of namespaces serviced by the
Ingress Controller. This is useful for implementing shards.

|`routeSelector`
|`routeSelector` is used to filter the set of Routes serviced by the Ingress Controller. This is useful for implementing shards.

|`nodePlacement`
|`nodePlacement` enables explicit control over the scheduling of the Ingress Controller.

If not set, the defaults values are used.

[NOTE]
====
The `nodePlacement` parameter includes two parts, `nodeSelector` and `tolerations`. For example:

[source,yaml]
----
nodePlacement:
 nodeSelector:
   matchLabels:
     kubernetes.io/os: linux
 tolerations:
 - effect: NoSchedule
   operator: Exists
----
====

|`tlsSecurityProfile`
|`tlsSecurityProfile` specifies settings for TLS connections for Ingress Controllers.

If not set, the default value is based on the `apiservers.config.openshift.io/cluster` resource.

When using the `Old`, `Intermediate`, and `Modern` profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the `Intermediate` profile deployed on release `X.Y.Z`, an upgrade to release `X.Y.Z+1` may cause a new profile configuration to be applied to the Ingress Controller, resulting in a rollout.

The minimum TLS version for Ingress Controllers is `1.1`, and the maximum TLS version is `1.3`.

[NOTE]
====
Ciphers and the minimum TLS version of the configured security profile are reflected in the `TLSProfile` status.
====

[IMPORTANT]
====
The Ingress Operator converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`.
====

|`clientTLS`
|`clientTLS` authenticates client access to the cluster and services; as a result, mutual TLS authentication is enabled. If not set, then client TLS is not enabled.

`clientTLS` has the required subfields, `spec.clientTLS.clientCertificatePolicy` and `spec.clientTLS.ClientCA`.

The `ClientCertificatePolicy` subfield accepts one of the two values: `Required` or `Optional`. The `ClientCA` subfield specifies a config map that is in the openshift-config namespace. The config map should contain a CA certificate bundle.

The `AllowedSubjectPatterns` is an optional value that specifies a list of regular expressions, which are matched against the distinguished name on a valid client certificate to filter requests. The regular expressions must use PCRE syntax. At least one pattern must match a client certificate's distinguished name; otherwise, the Ingress Controller rejects the certificate and denies the connection. If not specified, the Ingress Controller does not reject certificates based on the distinguished name.

|`routeAdmission`
|`routeAdmission` defines a policy for handling new route claims, such as allowing or denying claims across namespaces.

`namespaceOwnership` describes how hostname claims across namespaces should be handled. The default is `Strict`.

* `Strict`: does not allow routes to claim the same hostname across namespaces.
* `InterNamespaceAllowed`: allows routes to claim different paths of the same hostname across namespaces.

`wildcardPolicy` describes how routes with wildcard policies are handled by the Ingress Controller.

* `WildcardsAllowed`: Indicates routes with any wildcard policy are admitted by the Ingress Controller.

* `WildcardsDisallowed`: Indicates only routes with a wildcard policy of `None` are admitted by the Ingress Controller. Updating `wildcardPolicy` from `WildcardsAllowed` to `WildcardsDisallowed` causes admitted routes with a wildcard policy of `Subdomain` to stop working. These routes must be recreated to a wildcard policy of `None` to be readmitted by the Ingress Controller. `WildcardsDisallowed` is the default setting.

|`IngressControllerLogging`
|`logging` defines parameters for what is logged where. If this field is empty, operational logs are enabled but access logs are disabled.

* `access` describes how client requests are logged. If this field is empty, access logging is disabled.
** `destination` describes a destination for log messages.
*** `type` is the type of destination for logs:
**** `Container` specifies that logs should go to a sidecar container. The Ingress Operator configures the container, named *logs*, on the Ingress Controller pod and configures the Ingress Controller to write logs to the container. The expectation is that the administrator configures a custom logging solution that reads logs from this container. Using container logs means that logs may be dropped if the rate of logs exceeds the container runtime capacity or the custom logging solution capacity.
**** `Syslog` specifies that logs are sent to a Syslog endpoint. The administrator must specify an endpoint that can receive Syslog messages. The expectation is that the administrator has configured a custom Syslog instance.
*** `container` describes parameters for the `Container` logging destination type. Currently there are no parameters for container logging, so this field must be empty.
*** `syslog` describes parameters for the `Syslog` logging destination type:
**** `address` is the IP address of the syslog endpoint that receives log messages.
**** `port` is the UDP port number of the syslog endpoint that receives log messages.
**** `maxLength` is the maximum length of the syslog message. It must be between `480` and `4096` bytes. If this field is empty, the maximum length is set to the default value of `1024` bytes.
**** `facility` specifies the syslog facility of log messages. If this field is empty, the facility is `local1`. Otherwise, it must specify a valid syslog facility: `kern`, `user`, `mail`, `daemon`, `auth`, `syslog`, `lpr`, `news`, `uucp`, `cron`, `auth2`, `ftp`, `ntp`, `audit`, `alert`, `cron2`, `local0`, `local1`, `local2`, `local3`. `local4`, `local5`, `local6`, or `local7`.
** `httpLogFormat` specifies the format of the log message for an HTTP request. If this field is empty, log messages use the implementation's default HTTP log format. For HAProxy's default HTTP log format, see the HAProxy documentation.

|`httpHeaders`
|`httpHeaders` defines the policy for HTTP headers.

By setting the `forwardedHeaderPolicy` for the `IngressControllerHTTPHeaders`, you specify when and how the Ingress Controller sets the `Forwarded`, `X-Forwarded-For`, `X-Forwarded-Host`, `X-Forwarded-Port`, `X-Forwarded-Proto`, and `X-Forwarded-Proto-Version` HTTP headers.

By default, the policy is set to `Append`.

* `Append` specifies that the Ingress Controller appends the headers, preserving any existing headers.
* `Replace` specifies that the Ingress Controller sets the headers, removing any existing headers.
* `IfNone` specifies that the Ingress Controller sets the headers if they are not already set.
* `Never` specifies that the Ingress Controller never sets the headers, preserving any existing headers.

By setting `headerNameCaseAdjustments`, you can specify case adjustments that can be applied to HTTP header names. Each adjustment is specified as an HTTP header name with the desired capitalization. For example, specifying `X-Forwarded-For` indicates that the `x-forwarded-for` HTTP header should be adjusted to have the specified capitalization.

These adjustments are only applied to cleartext, edge-terminated, and re-encrypt routes, and only when using HTTP/1.

For request headers, these adjustments are applied only for routes that have the `haproxy.router.openshift.io/h1-adjust-case=true` annotation. For response headers, these adjustments are applied to all HTTP responses. If this field is empty, no request headers are adjusted.

`actions` specifies options for performing certain actions on headers. Headers cannot be set or deleted for TLS passthrough connections. The `actions` field has additional subfields `spec.httpHeader.actions.response` and `spec.httpHeader.actions.request`:

* The `response` subfield specifies a list of HTTP response headers to set or delete.

* The `request` subfield specifies a list of HTTP request headers to set or delete.

|`httpCompression`
|`httpCompression` defines the policy for HTTP traffic compression.

* `mimeTypes` defines a list of MIME types to which compression should be applied. For example, `text/css; charset=utf-8`, `text/html`, `text/*`, `image/svg+xml`, `application/octet-stream`, `X-custom/customsub`, using the format pattern, `type/subtype; [;attribute=value]`. The `types` are: application, image, message, multipart, text, video, or a custom type prefaced by `X-`; e.g. To see the full notation for MIME types and subtypes, see RFC1341

|`httpErrorCodePages`
|`httpErrorCodePages` specifies custom HTTP error code response pages. By default, an IngressController uses error pages built into the IngressController image.

|`httpCaptureCookies`
|`httpCaptureCookies` specifies HTTP cookies that you want to capture in access logs. If the `httpCaptureCookies` field is empty, the access logs do not capture the cookies.

For any cookie that you want to capture, the following parameters must be in your `IngressController` configuration:

* `name` specifies the name of the cookie.
* `maxLength` specifies tha maximum length of the cookie.
* `matchType` specifies if the field `name` of the cookie exactly matches the capture cookie setting or is a prefix of the capture cookie setting. The `matchType` field uses the `Exact` and `Prefix` parameters.

For example:
[source,yaml]
----
  httpCaptureCookies:
  - matchType: Exact
    maxLength: 128
    name: MYCOOKIE
----

|`httpCaptureHeaders`
|`httpCaptureHeaders` specifies the HTTP headers that you want to capture in the access logs. If the `httpCaptureHeaders` field is empty, the access logs do not capture the headers.

`httpCaptureHeaders` contains two lists of headers to capture in the access logs. The two lists of header fields are `request` and `response`. In both lists, the `name` field must specify the header name and the `maxlength` field must specify the maximum length of the header. For example:

[source,yaml]
----
  httpCaptureHeaders:
    request:
    - maxLength: 256
      name: Connection
    - maxLength: 128
      name: User-Agent
    response:
    - maxLength: 256
      name: Content-Type
    - maxLength: 256
      name: Content-Length
----
|`tuningOptions`
|`tuningOptions` specifies options for tuning the performance of Ingress Controller pods.

* `clientFinTimeout` specifies how long a connection is held open while waiting for the client response to the server closing the connection. The default timeout is `1s`.

* `clientTimeout` specifies how long a connection is held open while waiting for a client response. The default timeout is `30s`.

* `headerBufferBytes` specifies how much memory is reserved, in bytes, for Ingress Controller connection sessions. This value must be at least `16384` if HTTP/2 is enabled for the Ingress Controller. If not set, the default value is `32768` bytes. Setting this field not recommended because `headerBufferBytes` values that are too small can break the Ingress Controller, and `headerBufferBytes` values that are too large could cause the Ingress Controller to use significantly more memory than necessary.

* `headerBufferMaxRewriteBytes` specifies how much memory should be reserved, in bytes, from `headerBufferBytes` for HTTP header rewriting and appending for Ingress Controller connection sessions. The minimum value for `headerBufferMaxRewriteBytes` is `4096`. `headerBufferBytes` must be greater than `headerBufferMaxRewriteBytes` for incoming HTTP requests. If not set, the default value is `8192` bytes. Setting this field not recommended because `headerBufferMaxRewriteBytes` values that are too small can break the Ingress Controller and `headerBufferMaxRewriteBytes` values that are too large could cause the Ingress Controller to use significantly more memory than necessary.

* `healthCheckInterval` specifies how long the router waits between health checks. The default is `5s`.

* `serverFinTimeout` specifies how long a connection is held open while waiting for the server response to the client that is closing the connection. The default timeout is `1s`.

* `serverTimeout` specifies how long a connection is held open while waiting for a server response. The default timeout is `30s`.

* `threadCount` specifies the number of threads to create per HAProxy process. Creating more threads allows each Ingress Controller pod to handle more connections, at the cost of more system resources being used. HAProxy
supports up to `64` threads. If this field is empty, the Ingress Controller uses the default value of `4` threads. The default value can change in future releases. Setting this field is not recommended because increasing the number of HAProxy threads allows Ingress Controller pods to use more CPU time under load, and prevent other pods from receiving the CPU resources they need to perform. Reducing the number of threads can cause the Ingress Controller to perform poorly.

* `tlsInspectDelay` specifies how long the router can hold data to find a matching route. Setting this value too short can cause the router to fall back to the default certificate for edge-terminated, reencrypted, or passthrough routes, even when using a better matched certificate. The default inspect delay is `5s`.

* `tunnelTimeout` specifies how long a tunnel connection, including websockets, remains open while the tunnel is idle. The default timeout is `1h`.

* `maxConnections` specifies the maximum number of simultaneous connections that can be established per HAProxy process. Increasing this value allows each ingress controller pod to handle more connections at the cost of additional system resources. Permitted values are `0`, `-1`, any value within the range `2000` and `2000000`, or the field can be left empty.

** If this field is left empty or has the value `0`, the Ingress Controller will use the default value of `50000`. This value is subject to change in future releases.

** If the field has the value of `-1`, then HAProxy will dynamically compute a maximum value based on the available `ulimits` in the running container. This process results in a large computed value that will incur significant memory usage compared to the current default value of `50000`.

** If the field has a value that is greater than the current operating system limit, the HAProxy process will not start.

** If you choose a discrete value and the router pod is migrated to a new node, it is possible the new node does not have an identical `ulimit` configured. In such cases, the pod fails to start.

** If you have nodes with different `ulimits` configured, and you choose a discrete value, it is recommended to use the value of `-1` for this field so that the maximum number of connections is calculated at runtime.

|`logEmptyRequests`
|`logEmptyRequests` specifies connections for which no request is received and logged. These empty requests come from load balancer health probes or web browser speculative connections (preconnect) and logging these requests can be undesirable. However, these requests can be caused by network errors, in which case logging empty requests can be useful for diagnosing the errors. These requests can be caused by port scans, and logging empty requests can aid in detecting intrusion attempts. Allowed values for this field are `Log` and `Ignore`. The default value is `Log`.

The `LoggingPolicy` type accepts either one of two values:

* `Log`: Setting this value to `Log` indicates that an event should be logged.
* `Ignore`: Setting this value to `Ignore` sets the `dontlognull` option in the HAproxy configuration.

|`HTTPEmptyRequestsPolicy`
|`HTTPEmptyRequestsPolicy` describes how HTTP connections are handled if the connection times out before a request is received. Allowed values for this field are `Respond` and `Ignore`. The default value is `Respond`.

The `HTTPEmptyRequestsPolicy` type accepts either one of two values:

* `Respond`: If the field is set to `Respond`, the Ingress Controller sends an HTTP `400` or `408` response, logs the connection if access logging is enabled, and counts the connection in the appropriate metrics.
* `Ignore`: Setting this option to `Ignore` adds the `http-ignore-probes` parameter in the HAproxy configuration. If the field is set to `Ignore`, the Ingress Controller closes the connection without sending a response, then logs the connection, or incrementing metrics.

These connections come from load balancer health probes or web browser speculative connections (preconnect) and can be safely ignored. However, these requests can be caused by network errors, so setting this field to `Ignore` can impede detection and diagnosis of problems. These requests can be caused by port scans, in which case logging empty requests can aid in detecting intrusion attempts.
|===

[id="configuring-ingress-controller-tls"]
=== Ingress Controller TLS security profiles

TLS security profiles provide a way for servers to regulate which ciphers a connecting client can use when connecting to the server.

// Understanding TLS security profiles
// Module included in the following assemblies:
//
// * security/tls-security-profiles.adoc

[id="tls-profiles-understanding_{context}"]
= Understanding TLS security profiles

[role="_abstract"]
You can use a TLS (Transport Layer Security) security profile, as described in this section, to define which TLS ciphers are required by various OpenShift Container Platform components.

The OpenShift Container Platform TLS security profiles are based on Mozilla recommended configurations.

You can specify one of the following TLS security profiles for each component:

.TLS security profiles
[cols="1,2a",options="header"]
|===
|Profile
|Description

|`Old`
|This profile is intended for use with legacy clients or libraries. The profile is based on the Old backward compatibility recommended configuration.

The `Old` profile requires a minimum TLS version of 1.0.

[NOTE]
====
For the Ingress Controller, the minimum TLS version is converted from 1.0 to 1.1.
====

|`Intermediate`
|This profile is the default TLS security profile for the Ingress Controller, kubelet, and control plane. The profile is based on the Intermediate compatibility recommended configuration.

The `Intermediate` profile requires a minimum TLS version of 1.2.

[NOTE]
====
This profile is the recommended configuration for the majority of clients.
====

|`Modern`
|This profile is intended for use with modern clients that have no need for backwards compatibility. This profile is based on the Modern compatibility recommended configuration.

The `Modern` profile requires a minimum TLS version of 1.3.

|`Custom`
|This profile allows you to define the TLS version and ciphers to use.

[WARNING]
====
Use caution when using a `Custom` profile, because invalid configurations can cause problems.
====
|===

[NOTE]
====
When using one of the predefined profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the Intermediate profile deployed on release X.Y.Z, an upgrade to release X.Y.Z+1 might cause a new profile configuration to be applied, resulting in a rollout.
====

// TODO: Make sure all this is captured somewhere as necessary
// [IMPORTANT]
// ====
// The HAProxy Ingress Controller image does not support TLS `1.3` and because the `Modern` profile requires TLS `1.3`, it is not supported. The Ingress Operator converts the `Modern` profile to `Intermediate`.
//
// The Ingress Operator also converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`, and TLS `1.3` of a `Custom` profile to `1.2`.
// ====

// Configuring the TLS profile for the Ingress Controller
// Module included in the following assemblies:
//
// * security/tls-profiles.adoc

[id="tls-profiles-ingress-configuring_{context}"]
= Configuring the TLS security profile for the Ingress Controller

To configure a TLS security profile for an Ingress Controller, edit the `IngressController` custom resource (CR) to specify a predefined or custom TLS security profile. If a TLS security profile is not configured, the default value is based on the TLS security profile set for the API server.

.Sample `IngressController` CR that configures the `Old` TLS security profile
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
spec:
  tlsSecurityProfile:
    old: {}
    type: Old
 ...
----

The TLS security profile defines the minimum TLS version and the TLS ciphers for TLS connections for Ingress Controllers.

You can see the ciphers and the minimum TLS version of the configured TLS security profile in the `IngressController` custom resource (CR) under `Status.Tls Profile` and the configured TLS security profile under `Spec.Tls Security Profile`. For the `Custom` TLS security profile, the specific ciphers and minimum TLS version are listed under both parameters.

[NOTE]
====
The HAProxy Ingress Controller image supports TLS `1.3` and the `Modern` profile.

The Ingress Operator also converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`.
====

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

. Edit the `IngressController` CR in the `openshift-ingress-operator` project to configure the TLS security profile:
+
[source,terminal]
----
$ oc edit IngressController default -n openshift-ingress-operator
----

. Add the `spec.tlsSecurityProfile` field:
+
.Sample `IngressController` CR for a `Custom` profile
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
 ...
spec:
  tlsSecurityProfile:
    type: Custom <1>
    custom: <2>
      ciphers: <3>
      - ECDHE-ECDSA-CHACHA20-POLY1305
      - ECDHE-RSA-CHACHA20-POLY1305
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-ECDSA-AES128-GCM-SHA256
      minTLSVersion: VersionTLS11
 ...
----
<1> Specify the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.
<2> Specify the appropriate field for the selected type:
* `old: {}`
* `intermediate: {}`
* `modern: {}`
* `custom:`
<3> For the `custom` type, specify a list of TLS ciphers and minimum accepted TLS version.

. Save the file to apply the changes.

.Verification

* Verify that the profile is set in the `IngressController` CR:
+
[source,terminal]
----
$ oc describe IngressController default -n openshift-ingress-operator
----
+
.Example output
[source,terminal]
----
Name:         default
Namespace:    openshift-ingress-operator
Labels:       <none>
Annotations:  <none>
API Version:  operator.openshift.io/v1
Kind:         IngressController
 ...
Spec:
 ...
  Tls Security Profile:
    Custom:
      Ciphers:
        ECDHE-ECDSA-CHACHA20-POLY1305
        ECDHE-RSA-CHACHA20-POLY1305
        ECDHE-RSA-AES128-GCM-SHA256
        ECDHE-ECDSA-AES128-GCM-SHA256
      Min TLS Version:  VersionTLS11
    Type:               Custom
 ...
----

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id=nw-mutual-tls-auth_{context}]
= Configuring mutual TLS authentication

You can configure the Ingress Controller to enable mutual TLS (mTLS) authentication by setting a `spec.clientTLS` value. The `clientTLS` value configures the Ingress Controller to verify client certificates. This configuration includes setting a `clientCA` value, which is a reference to a config map. The config map contains the PEM-encoded CA certificate bundle that is used to verify a client's certificate. Optionally, you can also configure a list of certificate subject filters.

If the `clientCA` value specifies an X509v3 certificate revocation list (CRL) distribution point, the Ingress Operator downloads and manages a CRL config map based on the HTTP URI X509v3 `CRL Distribution Point` specified in each provided certificate. The Ingress Controller uses this config map during mTLS/TLS negotiation. Requests that do not provide valid certificates are rejected.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have a PEM-encoded CA certificate bundle.
* If your CA bundle references a CRL distribution point, you must have also included the end-entity or leaf certificate to the client CA bundle. This certificate must have included an HTTP URI under `CRL Distribution Points`, as described in RFC 5280. For example:
+
[source,terminal]
----
 Issuer: C=US, O=Example Inc, CN=Example Global G2 TLS RSA SHA256 2020 CA1
         Subject: SOME SIGNED CERT            X509v3 CRL Distribution Points:
                Full Name:
                  URI:http://crl.example.com/example.crl
----

.Procedure
. In the `openshift-config` namespace, create a config map from your CA bundle:
+
[source,terminal]
----
$ oc create configmap \
   router-ca-certs-default \
   --from-file=ca-bundle.pem=client-ca.crt \// <1>
   -n openshift-config
----
<1> The config map data key must be `ca-bundle.pem`, and the data value must be a CA certificate in PEM format.

. Edit the `IngressController` resource in the `openshift-ingress-operator` project:
+
[source,terminal]
----
$ oc edit IngressController default -n openshift-ingress-operator
----

. Add the `spec.clientTLS` field and subfields to configure mutual TLS:
+
.Sample `IngressController` CR for a `clientTLS` profile that specifies filtering patterns
[source,yaml]
----
  apiVersion: operator.openshift.io/v1
  kind: IngressController
  metadata:
    name: default
    namespace: openshift-ingress-operator
  spec:
    clientTLS:
      clientCertificatePolicy: Required
      clientCA:
        name: router-ca-certs-default
      allowedSubjectPatterns:
      - "^/CN=example.com/ST=NC/C=US/O=Security/OU=OpenShift$"
----
. Optional, get the Distinguished Name (DN) for `allowedSubjectPatterns` by entering the following command.
[source,terminal]
----
$ openssl  x509 -in custom-cert.pem  -noout -subject
subject= /CN=example.com/ST=NC/C=US/O=Security/OU=OpenShift
----

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-view_{context}"]
= View the default Ingress Controller

The Ingress Operator is a core feature of OpenShift Container Platform and is enabled out of the
box.

Every new OpenShift Container Platform installation has an `ingresscontroller` named default. It
can be supplemented with additional Ingress Controllers. If the default
`ingresscontroller` is deleted, the Ingress Operator will automatically recreate it
within a minute.

.Procedure

* View the default Ingress Controller:
+
[source,terminal]
----
$ oc describe --namespace=openshift-ingress-operator ingresscontroller/default
----

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-operator-status_{context}"]
= View Ingress Operator status

You can view and inspect the status of your Ingress Operator.

.Procedure

* View your Ingress Operator status:
+
[source,terminal]
----
$ oc describe clusteroperators/ingress
----

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-operator-logs_{context}"]
= View Ingress Controller logs

You can view your Ingress Controller logs.

.Procedure

* View your Ingress Controller logs:
+
[source,terminal]
----
$ oc logs --namespace=openshift-ingress-operator deployments/ingress-operator -c <container_name>
----

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-controller-status_{context}"]
= View Ingress Controller status

Your can view the status of a particular Ingress Controller.

.Procedure

* View the status of an Ingress Controller:
+
[source,terminal]
----
$ oc describe --namespace=openshift-ingress-operator ingresscontroller/<name>
----

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-create-custom-ingress-controller_{context}"]
= Creating a custom Ingress Controller

As a cluster administrator, you can create a new custom Ingress Controller. Because the default Ingress Controller might change during OpenShift Container Platform updates, creating a custom Ingress Controller can be helpful when maintaining a configuration manually that persists across cluster updates.

This example provides a minimal spec for a custom Ingress Controller. To further customize your custom Ingress Controller, see "Configuring the Ingress Controller".

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create a YAML file that defines the custom `IngressController` object:
+
.Example `custom-ingress-controller.yaml` file
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
    name: <custom_name> <1>
    namespace: openshift-ingress-operator
spec:
    defaultCertificate:
        name: <custom-ingress-custom-certs> <2>
    replicas: 1 <3>
    domain: <custom_domain> <4>
----
<1> Specify the a custom `name` for the `IngressController` object.
<2> Specify the name of the secret with the custom wildcard certificate.
<3> Minimum replica needs to be ONE
<4> Specify the domain to your domain name. The domain specified on the IngressController object and the domain used for the certificate must match. For example, if the domain value is "custom_domain.mycompany.com", then the certificate must have SAN \*.custom_domain.mycompany.com (with the `*.` added to the domain).

. Create the object by running the following command:
+
[source,terminal]
----
$ oc create -f custom-ingress-controller.yaml
----

[id="configuring-ingress-controller"]
== Configuring the Ingress Controller

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-ingress-setting-a-custom-default-certificate_{context}"]
= Setting a custom default certificate

As an administrator, you can configure an Ingress Controller to use a custom
certificate by creating a Secret resource and editing the `IngressController`
custom resource (CR).

.Prerequisites

* You must have a certificate/key pair in PEM-encoded files, where the
certificate is signed by a trusted certificate authority or by a private trusted
certificate authority that you configured in a custom PKI.

* Your certificate meets the following requirements:

** The certificate is valid for the ingress domain.

** The certificate uses the `subjectAltName` extension to specify a wildcard domain, such as `*.apps.ocp4.example.com`.

* You must have an `IngressController` CR, which includes just having the `default` `IngressController` CR. You can run the following command to check that you have an `IngressController` CR:
+
[source,terminal]
----
$ oc --namespace openshift-ingress-operator get ingresscontrollers
----

[NOTE]
====
If you have intermediate certificates, they must be included in the `tls.crt`
file of the secret containing a custom default certificate. Order matters when
specifying a certificate; list your intermediate certificate(s) after any server
certificate(s).
====

.Procedure

The following assumes that the custom certificate and key pair are in the
`tls.crt` and `tls.key` files in the current working directory. Substitute the
actual path names for `tls.crt` and `tls.key`. You also may substitute another
name for `custom-certs-default` when creating the Secret resource and
referencing it in the IngressController CR.

[NOTE]
====
This action will cause the Ingress Controller to be redeployed, using a rolling deployment strategy.
====

. Create a Secret resource containing the custom certificate in the
`openshift-ingress` namespace using the `tls.crt` and `tls.key` files.
+
[source,terminal]
----
$ oc --namespace openshift-ingress create secret tls custom-certs-default --cert=tls.crt --key=tls.key
----
+
. Update the IngressController CR to reference the new certificate secret:
+
[source,terminal]
----
$ oc patch --type=merge --namespace openshift-ingress-operator ingresscontrollers/default \
  --patch '{"spec":{"defaultCertificate":{"name":"custom-certs-default"}}}'
----
+
. Verify the update was effective:
+
[source,terminal]
----
$ echo Q |\
  openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null |\
  openssl x509 -noout -subject -issuer -enddate
----
+
where:
+
--
`<domain>`:: Specifies the base domain name for your cluster.
--
+
.Example output
[source,text]
----
subject=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = *.apps.example.com
issuer=C = US, ST = NC, L = Raleigh, O = RH, OU = OCP4, CN = example.com
notAfter=May 10 08:32:45 2022 GM
----
+
[TIP]
====
You can alternatively apply the following YAML to set a custom default certificate:

[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  defaultCertificate:
    name: custom-certs-default
----
====
+
The certificate secret name should match the value used to update the CR.

Once the IngressController CR has been modified, the Ingress Operator
updates the Ingress Controller's deployment to use the custom certificate.

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-ingress-custom-default-certificate-remove_{context}"]
= Removing a custom default certificate

As an administrator, you can remove a custom certificate that you configured an Ingress Controller to use.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You previously configured a custom default certificate for the Ingress Controller.

.Procedure

* To remove the custom certificate and restore the certificate that ships with OpenShift Container Platform, enter the following command:
+
[source,terminal]
----
$ oc patch -n openshift-ingress-operator ingresscontrollers/default \
  --type json -p $'- op: remove\n  path: /spec/defaultCertificate'
----
+
There can be a delay while the cluster reconciles the new certificate configuration.

.Verification

* To confirm that the original cluster certificate is restored, enter the following command:
+
[source,terminal]
----
$ echo Q | \
  openssl s_client -connect console-openshift-console.apps.<domain>:443 -showcerts 2>/dev/null | \
  openssl x509 -noout -subject -issuer -enddate
----
+
where:
+
--
`<domain>`:: Specifies the base domain name for your cluster.
--
+
.Example output
[source,text]
----
subject=CN = *.apps.<domain>
issuer=CN = ingress-operator@1620633373
notAfter=May 10 10:44:36 2023 GMT
----

// Autoscaling an Ingress Controller
// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-autoscaling-ingress-controller_{context}"]
= Autoscaling an Ingress Controller

You can automatically scale an Ingress Controller to dynamically meet routing performance or availability requirements. For example, the requirement to increase throughput.

The following procedure provides an example for scaling up the default Ingress Controller.

.Prerequisites

* You have the {oc-first} installed.
* You have access to an OpenShift Container Platform cluster as a user with the `cluster-admin` role.
* On {vmw-first}, bare-metal, and Nutanix installer-provisioned infrastructure, scaling up Ingress Controller pods does not improve external traffic performance. To improve performance, ensure that you complete the following prerequisites:
** You manually configured a user-managed load balancer for your cluster.
** You ensured that the load balancer was configured for the cluster nodes that handle incoming traffic from the Ingress Controller.
* You installed the Custom Metrics Autoscaler Operator and an associated KEDA Controller.
** You can install the Operator by using the software catalog on the web console. After you install the Operator, you can create an instance of `KedaController`.

.Procedure

. Create a service account to authenticate with Thanos by running the following command:
+
[source,terminal]
----
$ oc create -n openshift-ingress-operator serviceaccount thanos && oc describe -n openshift-ingress-operator serviceaccount thanos
----
+
.Example output
[source,terminal]
----
Name:                thanos
Namespace:           openshift-ingress-operator
Labels:              <none>
Annotations:         <none>
Image pull secrets:  thanos-dockercfg-kfvf2
Mountable secrets:   thanos-dockercfg-kfvf2
Tokens:              <none>
Events:              <none>
----

. Manually create the service account secret token with the following command:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: thanos-token
  namespace: openshift-ingress-operator
  annotations:
    kubernetes.io/service-account.name: thanos
type: kubernetes.io/service-account-token
EOF
----

. Define a `TriggerAuthentication` object within the `openshift-ingress-operator` namespace by using the service account's token.

.. Create the `TriggerAuthentication` object and pass the value of the `secret` variable to the `TOKEN` parameter:
+
[source,terminal]
----
$ oc apply -f - <<EOF
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-prometheus
  namespace: openshift-ingress-operator
spec:
  secretTargetRef:
  - parameter: bearerToken
    name: thanos-token
    key: token
  - parameter: ca
    name: thanos-token
    key: ca.crt
EOF
----

. Create and apply a role for reading metrics from Thanos:

.. Create a new role, `thanos-metrics-reader.yaml`, that reads metrics from pods and nodes:
+
.thanos-metrics-reader.yaml
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: thanos-metrics-reader
  namespace: openshift-ingress-operator
rules:
- apiGroups:
  - ""
  resources:
  - pods
  - nodes
  verbs:
  - get
- apiGroups:
  - metrics.k8s.io
  resources:
  - pods
  - nodes
  verbs:
  - get
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - namespaces
  verbs:
  - get
----

.. Apply the new role by running the following command:
+
[source,terminal]
----
$ oc apply -f thanos-metrics-reader.yaml
----

. Add the new role to the service account by entering the following commands:
+
[source,terminal]
----
$ oc adm policy -n openshift-ingress-operator add-role-to-user thanos-metrics-reader -z thanos --role-namespace=openshift-ingress-operator
----
+
[source,terminal]
----
$ oc adm policy -n openshift-ingress-operator add-cluster-role-to-user cluster-monitoring-view -z thanos
----
+
[NOTE]
====
The argument `add-cluster-role-to-user` is only required if you use cross-namespace queries. The following step uses a query from the `kube-metrics` namespace which requires this argument.
====

. Create a new `ScaledObject` YAML file, `ingress-autoscaler.yaml`, that targets the default Ingress Controller deployment:
+
.Example `ScaledObject` definition
[source,yaml]
----
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: ingress-scaler
  namespace: openshift-ingress-operator
spec:
  scaleTargetRef: <1>
    apiVersion: operator.openshift.io/v1
    kind: IngressController
    name: default
    envSourceContainerName: ingress-operator
  minReplicaCount: 1
  maxReplicaCount: 20 <2>
  cooldownPeriod: 1
  pollingInterval: 1
  triggers:
  - type: prometheus
    metricType: AverageValue
    metadata:
      serverAddress: https://thanos-querier.openshift-monitoring.svc.cluster.local:9091 <3>
      namespace: openshift-ingress-operator <4>
      metricName: 'kube-node-role'
      threshold: '1'
      query: 'sum(kube_node_role{role="worker",service="kube-state-metrics"})' <5>
      authModes: "bearer"
    authenticationRef:
      name: keda-trigger-auth-prometheus
----
<1> The custom resource that you are targeting. In this case, the Ingress Controller.
<2> Optional: The maximum number of replicas. If you omit this field, the default maximum is set to 100 replicas.
<3> The Thanos service endpoint in the `openshift-monitoring` namespace.
<4> The Ingress Operator namespace.
<5> This expression evaluates to however many worker nodes are present in the deployed cluster.
+
[IMPORTANT]
====
If you are using cross-namespace queries, you must target port 9091 and not port 9092 in the `serverAddress` field. You also must have elevated privileges to read metrics from this port.
====

. Apply the custom resource definition by running the following command:
+
[source,terminal]
----
$ oc apply -f ingress-autoscaler.yaml
----

.Verification

* Verify that the default Ingress Controller is scaled out to match the value returned by the `kube-state-metrics` query by running the following commands:

** Use the `grep` command to search the Ingress Controller YAML file for the number of replicas:
+
[source,terminal]
----
$ oc get -n openshift-ingress-operator ingresscontroller/default -o yaml | grep replicas:
----

** Get the pods in the `openshift-ingress` project:
+
[source,terminal]
----
$ oc get pods -n openshift-ingress
----
+
.Example output
[source,terminal]
----
NAME                             READY   STATUS    RESTARTS   AGE
router-default-7b5df44ff-l9pmm   2/2     Running   0          17h
router-default-7b5df44ff-s5sl5   2/2     Running   0          3d22h
router-default-7b5df44ff-wwsth   2/2     Running   0          66s
----

[role="_additional-resources"]
.Additional resources

* Installing the custom metrics autoscaler

* Enabling monitoring for user-defined projects

* Understanding custom metrics autoscaler trigger authentications

* Understanding custom metrics autoscaler triggers

* Understanding how to add custom metrics autoscalers

// Module filename: nw-scaling-ingress-controller.adoc
// Module included in the following assemblies:
// * networking/ingress-controller-configuration.adoc

[id="nw-ingress-controller-configuration_{context}"]
= Scaling an Ingress Controller

Manually scale an Ingress Controller to meeting routing performance or availability requirements such as the requirement to increase throughput. `oc` commands are used to scale the `IngressController` resource. The following procedure provides an example for scaling up the default `IngressController`.

[NOTE]
====
Scaling is not an immediate action, as it takes time to create the desired number of replicas.
====

.Prerequisites

* On {vmw-first}, bare-metal, and Nutanix installer-provisioned infrastructure, scaling up Ingress Controller pods does not improve external traffic performance. To improve performance, ensure that you complete the following prerequisites:
** You manually configured a user-managed load balancer for your cluster.
** You ensured that the load balancer was configured for the cluster nodes that handle incoming traffic from the Ingress Controller.

.Procedure

. View the current number of available replicas for the default `IngressController`:
+
[source,terminal]
----
$ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
----

. Scale the default `IngressController` to the desired number of replicas by using the `oc patch` command. The following example scales the default `IngressController` to 3 replicas.
+
[source,terminal]
----
$ oc patch -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"replicas": 3}}' --type=merge
----

. Verify that the default `IngressController` scaled to the number of replicas that you specified:
+
[source,terminal]
----
$ oc get -n openshift-ingress-operator ingresscontrollers/default -o jsonpath='{$.status.availableReplicas}'
----
+
[TIP]
====
You can alternatively apply the following YAML to scale an Ingress Controller to three replicas:
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  replicas: 3               <1>
----
====
<1> If you need a different amount of replicas, change the `replicas` value.

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-configure-ingress-access-logging_{context}"]
= Configuring Ingress access logging

You can configure the Ingress Controller to enable access logs. If you have clusters that do not receive much traffic, then you can log to a sidecar. If you have high traffic clusters, to avoid exceeding the capacity of the logging stack or  to integrate with a logging infrastructure outside of OpenShift Container Platform, you can forward logs to a custom syslog endpoint. You can also specify the format for access logs.

Container logging is useful to enable access logs on low-traffic clusters when there is no existing Syslog logging infrastructure, or for short-term use while diagnosing problems with the Ingress Controller.

Syslog is needed for high-traffic clusters where access logs could exceed the OpenShift Logging stack's capacity, or for environments where any logging solution needs to integrate with an existing Syslog logging infrastructure. The Syslog use-cases can overlap.

.Prerequisites

* Log in as a user with `cluster-admin` privileges.

.Procedure

* For Ingress access logging to a sidecar, complete the following commands:
+
** To enable Ingress access logging to a sidecar, enter the following command:
+
[source,terminal]
----
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
  -p '{"spec":{"logging":{"access":{"destination":{"type":"Container"}}}}}'
----
+
After you configure the Ingress Controller to log to a sidecar, the Operator creates a container named `logs` inside a router pod that exists in the `openshift-ingress` namespace.
+
** If you need to disable Ingress access logging, enter the following command that does not specify any values for `spec.logging`:
+
[source,terminal]
----
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=json \
  -p='[{"op": "remove", "path": "/spec/logging"}]'
----
+
** To stream the access logs and system events from the OpenShift Container Platform Ingress Controller, enter the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress logs deployment.apps/router-default -c logs
----
+
.Example output
[source,terminal]
----
2020-05-11T19:11:50.135710+00:00 router-default-57dfc6cd95-bpmk6 router-default-57dfc6cd95-bpmk6 haproxy[108]: 174.19.21.82:39654 [11/May/2020:19:11:50.133] public be_http:hello-openshift:hello-openshift/pod:hello-openshift:hello-openshift:10.128.2.12:8080 0/0/1/0/1 200 142 - - --NI 1/1/0/0/0 0/0 "GET / HTTP/1.1"
----

* To enable logging to an external Syslog server, enter the following command. Use this option if you need to forward logs to a centralized logging solution such as Splunk, Rsyslog, or Logstash.
+
[source,terminal]
----
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
  -p '{"spec":{"logging":{"access":{"destination":{"type":"Syslog","syslog":{"address":"1.2.3.4","port":514,"maxLenght":1024}}}}}}'
----
+
** Replace `1.2.3.4` with the destination IP address of your logging server. Syslog does not support a DNS hostname value.
** Replace `514` with the UDP destination port of your logging server.
** Replace `1024` with the maximum length of a log message in bytes that you want to set for log messages.

* To customize the log format, append an HAProxy-compatible log string to the following command. The string determines what information gets captured in the log format, such as a client IP address.
+
[source,terminal]
----
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge \
  -p '{"spec":{"logging":{"access":{"httpLogFormat":"%ci:%cp [%t] %ft %b/%s %B %bq %HM %HU %HV"}}}}'
----
+
[NOTE]
====
For a list of HAProxy log variable descriptions, see Custom log format in the upstream HAProxy documentation.
====

* To capture custom HTTP headers or response headers in your logs, enter the following command. Consider this option if you need to track an `X-Forwarded-For` header or custom application IDs in the Ingress and application logs.
+
[source,terminal]
----
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge -p '{"spec":{"logging":{"access":{"httpCaptureHeaders":{"request":[{"name":"User-Agent","maxLength": 1024}],"response":[{"name":"Content-Type","maxLength": 1024}]}}}}}'
----

* To configure a log empty requests policy, enter the following command and set the `logEmptyRequests` parameter to `Log`. By default, HAProxy might not log empty requests or health checks, so you must manually enable this feature. To disable the feature, set the `logEmptyRequests` parameter to `Ignore`.
+
[source,terminal]
----
$ oc patch ingresscontroller default -n openshift-ingress-operator --type=merge -p '{"spec":{"logging":{"access":{"logEmptyRequests":"Ignore"}}}}'
----

[role="_additional-resources"]
.Additional resources

* Capturing Original Client IP from the X-Forwarded-For Header in Ingress and Application Logs

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-setting-thread-count_{context}"]
= Setting Ingress Controller thread count

A cluster administrator can set the thread count to increase the amount of incoming connections a cluster can handle. You can patch an existing Ingress Controller to increase the amount of threads.

.Prerequisites
* The following assumes that you already created an Ingress Controller.

.Procedure
* Update the Ingress Controller to increase the number of threads:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"threadCount": 8}}}'
----
+
[NOTE]
====
If you have a node that is capable of running large amounts of resources, you can configure `spec.nodePlacement.nodeSelector` with labels that match the capacity of the intended node, and configure `spec.tuningOptions.threadCount` to an appropriately high value.
====

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-ingress-setting-internal-lb_{context}"]
= Configuring an Ingress Controller to use an internal load balancer

When creating an Ingress Controller on cloud platforms, the Ingress Controller is published by a public cloud load balancer by default.
As an administrator, you can create an Ingress Controller that uses an internal cloud load balancer.

[WARNING]
====
If your cloud provider is Microsoft Azure, you must have at least one public load balancer that points to your nodes.
If you do not, all of your nodes will lose egress connectivity to the internet.
====

[IMPORTANT]
====
If you want to change the `scope` for an `IngressController`, you can change the `.spec.endpointPublishingStrategy.loadBalancer.scope` parameter after the custom resource (CR) is created.
====

.Diagram of LoadBalancer
image::202_OpenShift_Ingress_0222_load_balancer.png[OpenShift Container Platform Ingress LoadBalancerService endpoint publishing strategy]

The preceding graphic shows the following concepts pertaining to OpenShift Container Platform Ingress LoadBalancerService endpoint publishing strategy:

* You can load balance externally, using the cloud provider load balancer, or internally, using the OpenShift Ingress Controller Load Balancer.
* You can use the single IP address of the load balancer and more familiar ports, such as 8080 and 4200 as shown on the cluster depicted in the graphic.
* Traffic from the external load balancer is directed at the pods, and managed by the load balancer, as depicted in the instance of a down node.
See the Kubernetes Services documentation
for implementation details.

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create an `IngressController` custom resource (CR) in a file named `<name>-ingress-controller.yaml`, such as in the following example:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: <name> <1>
spec:
  domain: <domain> <2>
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal <3>
----
<1> Replace `<name>` with a name for the `IngressController` object.
<2> Specify the `domain` for the application published by the controller.
<3> Specify a value of `Internal` to use an internal load balancer.

. Create the Ingress Controller defined in the previous step by running the following command:
+
[source,terminal]
----
$ oc create -f <name>-ingress-controller.yaml <1>
----
<1> Replace `<name>` with the name of the `IngressController` object.

. Optional: Confirm that the Ingress Controller was created by running the following command:
+
[source,terminal]
----
$ oc --all-namespaces=true get ingresscontrollers
----

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-controller-configuration-gcp-global-access_{context}"]
= Configuring global access for an Ingress Controller on {gcp-short}

An Ingress Controller created on {gcp-short} with an internal load balancer generates an internal IP address for the service. A cluster administrator can specify the global access option, which enables clients in any region within the same VPC network and compute region as the load balancer, to reach the workloads running on your cluster.

For more information, see the {gcp-short} documentation for global access.

.Prerequisites

* You deployed an OpenShift Container Platform cluster on {gcp-short} infrastructure.
* You configured an Ingress Controller to use an internal load balancer.
* You installed the OpenShift CLI (`oc`).

.Procedure

. Configure the Ingress Controller resource to allow global access.
+
[NOTE]
====
You can also create an Ingress Controller and specify the global access option.
====
+
.. Configure the Ingress Controller resource:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator edit ingresscontroller/default
----
+
.. Edit the YAML file:
+
.Sample `clientAccess` configuration to `Global`
[source,yaml]
----
  spec:
    endpointPublishingStrategy:
      loadBalancer:
        providerParameters:
          gcp:
            clientAccess: Global <1>
          type: GCP
        scope: Internal
      type: LoadBalancerService
----
<1> Set `gcp.clientAccess` to `Global`.

.. Save the file to apply the changes.
+
. Run the following command to verify that the service allows global access:
+
[source,terminal]
----
$ oc -n openshift-ingress edit svc/router-default -o yaml
----
+
The output shows that global access is enabled for {gcp-short} with the annotation, `networking.gke.io/internal-load-balancer-allow-global-access`.

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-ingress-controller-config-tuningoptions-healthcheckinterval_{context}"]
= Setting the Ingress Controller health check interval

A cluster administrator can set the health check interval to define how long the router waits between two consecutive health checks. This value is applied globally as a default for all routes. The default value is 5 seconds.

.Prerequisites
* The following assumes that you already created an Ingress Controller.

.Procedure
* Update the Ingress Controller to change the interval between back end health checks:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"healthCheckInterval": "8s"}}}'
----
+
[NOTE]
====
To override the `healthCheckInterval` for a single route, use the route annotation `router.openshift.io/haproxy.health.check.interval`
====

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-ingress-default-internal_{context}"]
= Configuring the default Ingress Controller for your cluster to be internal

You can configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it.

[WARNING]
====
If your cloud provider is Microsoft Azure, you must have at least one public load balancer that points to your nodes.
If you do not, all of your nodes will lose egress connectivity to the internet.
====

[IMPORTANT]
====
If you want to change the `scope` for an `IngressController`, you can change the `.spec.endpointPublishingStrategy.loadBalancer.scope` parameter after the custom resource (CR) is created.
====

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Configure the `default` Ingress Controller for your cluster to be internal by deleting and recreating it.
+
[source,terminal]
----
$ oc replace --force --wait --filename - <<EOF
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: default
spec:
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal
EOF
----

// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc
// * networking/routes/route-configuration.adoc

[id="nw-route-admission-policy_{context}"]
= Configuring the route admission policy

Administrators and application developers can run applications in multiple namespaces with the same domain name. This is for organizations where multiple teams develop microservices that are exposed on the same hostname.

[WARNING]
====
Allowing claims across namespaces should only be enabled for clusters with trust between namespaces, otherwise a malicious user could take over a hostname. For this reason, the default admission policy disallows hostname claims across namespaces.
====

.Prerequisites

* Cluster administrator privileges.

.Procedure

* Edit the `.spec.routeAdmission` field of the `ingresscontroller` resource variable using the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default --patch '{"spec":{"routeAdmission":{"namespaceOwnership":"InterNamespaceAllowed"}}}' --type=merge
----
+
.Sample Ingress Controller configuration
[source,yaml]
----
spec:
  routeAdmission:
    namespaceOwnership: InterNamespaceAllowed
...
----
+
[TIP]
====
You can alternatively apply the following YAML to configure the route admission policy:
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  routeAdmission:
    namespaceOwnership: InterNamespaceAllowed
----
====

// Module included in the following assemblies:
//
// * networking/configuring-ingress-controller

[id="using-wildcard-routes_{context}"]
= Using wildcard routes

The HAProxy Ingress Controller has support for wildcard routes. The Ingress Operator uses `wildcardPolicy` to configure the `ROUTER_ALLOW_WILDCARD_ROUTES` environment variable of the Ingress Controller.

The default behavior of the Ingress Controller is to admit routes with a wildcard policy of `None`, which is backwards compatible with existing `IngressController` resources.

.Procedure

. Configure the wildcard policy.
.. Use the following command to edit the `IngressController` resource:
+
[source,terminal]
----
$ oc edit IngressController
----
+
.. Under `spec`, set the `wildcardPolicy` field to `WildcardsDisallowed` or `WildcardsAllowed`:
+
[source,yaml]
----
spec:
  routeAdmission:
    wildcardPolicy: WildcardsDisallowed # or WildcardsAllowed
----

.Samples for using a secure wildcard edge terminated route

This example reflects TLS termination occurring on the Ingress Controller before traffic is proxied to the destination. Traffic sent to any hosts in the subdomain
`example.test` (`*.example.test`) is proxied to the exposed service.

The secure edge terminated route specifies the TLS certificate and key
information. The TLS certificate is served by the Ingress Controller front end for all hosts that match the subdomain (`*.example.test`).

. Configure the wildcard policy.

. Create a private key, certificate signing request (CSR), and certificate for the
edge secured route.
+
The instructions on how to do this are specific to your certificate authority and provider. The following example is a simple self-signed certificate for a domain named `*.example.test`:
+
----
# sudo openssl genrsa -out example-test.key 2048
#
# sudo openssl req -new -key example-test.key -out example-test.csr  \
  -subj "/C=US/ST=CA/L=Mountain View/O=OS3/OU=Eng/CN=*.example.test"
#
# sudo openssl x509 -req -days 366 -in example-test.csr  \
      -signkey example-test.key -out example-test.crt
----

. Generate a wildcard route using the certificate and key:
+
----
$ cat > route.yaml  <<REOF
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name:  my-service
spec:
  host: www.example.test
  wildcardPolicy: Subdomain
  to:
    kind: Service
    name: my-service
  tls:
    termination: edge
    key: "$(perl -pe 's/\n/\\n/' example-test.key)"
    certificate: "$(perl -pe 's/\n/\\n/' example-test.cert)"
REOF
$ oc create -f route.yaml
----
+
Ensure your DNS entry for `*.example.test` points to your Ingress Controller instances and the route to your domain is available.
+
This example uses `curl` with a local resolver to simulate the DNS lookup:
+
----
# routerip="4.1.1.1"  #  replace with IP address of one of your router instances.
# curl -k --resolve www.example.test:443:$routerip https://www.example.test/
# curl -k --resolve abc.example.test:443:$routerip https://abc.example.test/
# curl -k --resolve anyname.example.test:443:$routerip https://anyname.example.test/
----

For Ingress Controllers that allow wildcard routes, configure the wildcard policy, there are some caveats to the ownership of a subdomain associated with a wildcard route.

Prior to wildcard routes, ownership was based on the claims made for a hostname with the namespace with the oldest route winning against any other claimants.
For example, route `r1` in namespace `ns1` with a claim for `one.example.test`
would win over another route `r2` in namespace `ns2` for the same hostname
`one.example.test` if route `r1` was older than route `r2`.

In addition, routes in other namespaces were allowed to claim non-overlapping
hostnames. For example, route `rone` in namespace `ns1` could claim
`www.example.test` and another route `rtwo` in namespace `d2` could claim
`c3po.example.test`.

This is still the case if there are _no_ wildcard routes claiming that same
subdomain, such as `example.test` in the previous example.

However, a wildcard route needs to claim all of the hostnames within a
subdomain, hostnames of the form `\*.example.test`. A wildcard route's claim
is allowed or denied based on whether or not the oldest route for that subdomain
(`example.test`) is in the same namespace as the wildcard route. The oldest
route can be either a regular route or a wildcard route.

For example, if there is already a route `eldest` that exists in the `ns1`
namespace that claimed a hostnamed `owner.example.test` and, if at a later
point in time, a new wildcard route `wildthing` requesting for routes in that
subdomain (`example.test`) is added, the claim by the wildcard route will only
be allowed if it is the same namespace (`ns1`) as the owning route.

The following examples illustrate various scenarios in which claims for wildcard
routes will succeed or fail.

In the following example, a Ingress Controller that allows wildcard routes will allow non-overlapping claims for hosts in the subdomain `example.test` as long as a
wildcard route has not claimed a subdomain.

----
$ oc project ns1
$ oc expose service myservice --hostname=owner.example.test
$ oc expose service myservice --hostname=aname.example.test
$ oc expose service myservice --hostname=bname.example.test

$ oc project ns2
$ oc expose service anotherservice --hostname=second.example.test
$ oc expose service anotherservice --hostname=cname.example.test

$ oc project otherns
$ oc expose service thirdservice --hostname=emmy.example.test
$ oc expose service thirdservice --hostname=webby.example.test
----

In the following example, a Ingress Controller that allows wildcard routes will not allow the claim for `owner.example.test` or `aname.example.test` to succeed since the owning namespace is `ns1`.

----
$ oc project ns1
$ oc expose service myservice --hostname=owner.example.test
$ oc expose service myservice --hostname=aname.example.test

$ oc project ns2
$ oc expose service secondservice --hostname=bname.example.test
$ oc expose service secondservice --hostname=cname.example.test

$ # Router will not allow this claim with a different path name `/p1` as
$ # namespace `ns1` has an older route claiming host `aname.example.test`.
$ oc expose service secondservice --hostname=aname.example.test --path="/p1"

$ # Router will not allow this claim as namespace `ns1` has an older route
$ # claiming hostname `owner.example.test`.
$ oc expose service secondservice --hostname=owner.example.test

$ oc project otherns

$ # Router will not allow this claim as namespace `ns1` has an older route
$ # claiming hostname `aname.example.test`.
$ oc expose service thirdservice --hostname=aname.example.test
----

In the following example, a Ingress Controller that allows wildcard routes will allow the claim for `\*.example.test` to succeed since the owning namespace is `ns1` and the wildcard route belongs to that same namespace.

----
$ oc project ns1
$ oc expose service myservice --hostname=owner.example.test

$ # Reusing the route.yaml from the previous example.
$ # spec:
$ #   host: www.example.test
$ #   wildcardPolicy: Subdomain

$ oc create -f route.yaml   #  router will allow this claim.
----

In the following example, a Ingress Controller that allows wildcard routes will not allow the claim for \*.example.test` to succeed since the owning namespace is `ns1` and the wildcard route belongs to another namespace `cyclone`.

----
$ oc project ns1
$ oc expose service myservice --hostname=owner.example.test

$ # Switch to a different namespace/project.
$ oc project cyclone

$ # Reusing the route.yaml from a prior example.
$ # spec:
$ #   host: www.example.test
$ #   wildcardPolicy: Subdomain

$ oc create -f route.yaml   #  router will deny (_NOT_ allow) this claim.
----

Similarly, once a namespace with a wildcard route claims a subdomain, only
routes within that namespace can claim any hosts in that same subdomain.

In the following example, once a route in namespace `ns1` with a wildcard route
claims subdomain `example.test`, only routes in the namespace `ns1` are allowed
to claim any hosts in that same subdomain.

----
$ oc project ns1
$ oc expose service myservice --hostname=owner.example.test

$ oc project otherns

$ # namespace `otherns` is allowed to claim for other.example.test
$ oc expose service otherservice --hostname=other.example.test

$ oc project ns1

$ # Reusing the route.yaml from the previous example.
$ # spec:
$ #   host: www.example.test
$ #   wildcardPolicy: Subdomain

$ oc create -f route.yaml   #  Router will allow this claim.

$ #  In addition, route in namespace otherns will lose its claim to host
$ #  `other.example.test` due to the wildcard route claiming the subdomain.

$ # namespace `ns1` is allowed to claim for deux.example.test
$ oc expose service mysecondservice --hostname=deux.example.test

$ # namespace `ns1` is allowed to claim for deux.example.test with path /p1
$ oc expose service mythirdservice --hostname=deux.example.test --path="/p1"

$ oc project otherns

$ # namespace `otherns` is not allowed to claim for deux.example.test
$ # with a different path '/otherpath'
$ oc expose service otherservice --hostname=deux.example.test --path="/otherpath"

$ # namespace `otherns` is not allowed to claim for owner.example.test
$ oc expose service yetanotherservice --hostname=owner.example.test

$ # namespace `otherns` is not allowed to claim for unclaimed.example.test
$ oc expose service yetanotherservice --hostname=unclaimed.example.test
----

In the following example, different scenarios are shown in which the owner routes
are deleted and ownership is passed within and across namespaces. While a route
claiming host `eldest.example.test` in the namespace `ns1` exists, wildcard
routes in that namespace can claim subdomain `example.test`. When the route for
host `eldest.example.test` is deleted, the next oldest route
`senior.example.test` would become the oldest route and would not affect any
other routes. After the route for host `senior.example.test` is deleted, the next
oldest route `junior.example.test` becomes the oldest route and block the
wildcard route claimant.

----
$ oc project ns1
$ oc expose service myservice --hostname=eldest.example.test
$ oc expose service seniorservice --hostname=senior.example.test

$ oc project otherns

$ # namespace `otherns` is allowed to claim for other.example.test
$ oc expose service juniorservice --hostname=junior.example.test

$ oc project ns1

$ # Reusing the route.yaml from the previous example.
$ # spec:
$ #   host: www.example.test
$ #   wildcardPolicy: Subdomain

$ oc create -f route.yaml   #  Router will allow this claim.

$ #  In addition, route in namespace otherns will lose its claim to host
$ #  `junior.example.test` due to the wildcard route claiming the subdomain.

$ # namespace `ns1` is allowed to claim for dos.example.test
$ oc expose service mysecondservice --hostname=dos.example.test

$ # Delete route for host `eldest.example.test`, the next oldest route is
$ # the one claiming `senior.example.test`, so route claims are unaffacted.
$ oc delete route myservice

$ # Delete route for host `senior.example.test`, the next oldest route is
$ # the one claiming `junior.example.test` in another namespace, so claims
$ # for a wildcard route would be affected. The route for the host
$ # `dos.example.test` would be unaffected as there are no other wildcard
$ # claimants blocking it.
$ oc delete route seniorservice
----

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc
// * networking/route-configuration.adoc

[id="nw-http-header-configuration_{context}"]
= HTTP header configuration

[role="_abstract"]
To customize request and response headers for your applications, configure the Ingress Controller or apply specific route annotations. Understanding the interaction between these configuration methods ensures you effectively manage global and route-specific header policies.

You can also set certain headers by using route annotations. The various ways of configuring headers can present challenges when working together.
To customize request and response headers, modify individual route configurations or apply route annotations. Understanding the interaction between these methods ensures you effectively manage header policies and resolve potential configuration conflicts.

The various ways of configuring headers can present challenges when working together.

[NOTE]
====
You can only set or delete headers within an `IngressController` or `Route` CR, you cannot append them. If an HTTP header is set with a value, that value must be complete and not require appending in the future. In situations where it makes sense to append a header, such as the X-Forwarded-For header, use the `spec.httpHeaders.forwardedHeaderPolicy` field, instead of `spec.httpHeaders.actions`.
====

[NOTE]
====
You can only set or delete headers within a `Route` CR. You cannot append headers. If an HTTP header is set with a value, that value must be complete and not require appending in the future. In situations where it makes sense to append a header, such as the X-Forwarded-For header, use the `spec.httpHeaders.forwardedHeaderPolicy` field, instead of `spec.httpHeaders.actions`.
====

Order of precedence::

When the same HTTP header is modified both in the Ingress Controller and in a route, HAProxy prioritizes the actions in certain ways depending on whether it is a request or response header.

* For HTTP response headers, actions specified in the Ingress Controller are executed after the actions specified in a route. This means that the actions specified in the Ingress Controller take precedence.

* For HTTP request headers, actions specified in a route are executed after the actions specified in the Ingress Controller. This means that the actions specified in the route take precedence.

For example, a cluster administrator sets the X-Frame-Options response header with the value `DENY` in the Ingress Controller using the following configuration:

.Example `IngressController` spec
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: DENY
----

A route owner sets the same response header that the cluster administrator set in the Ingress Controller, but with the value `SAMEORIGIN` using the following configuration:

.Example `Route` spec
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
# ...
spec:
  httpHeaders:
    actions:
      response:
      - name: X-Frame-Options
        action:
          type: Set
          set:
            value: SAMEORIGIN
----
When both the `IngressController` spec and `Route` spec are configuring the X-Frame-Options response header, then the value set for this header at the global level in the Ingress Controller takes precedence, even if a specific route allows frames. For a request header, the `Route` spec value overrides the `IngressController` spec value.

This prioritization occurs because the `haproxy.config` file uses the following logic, where the Ingress Controller is considered the front end and individual routes are considered the back end. The header value `DENY` applied to the front end configurations overrides the same header with the value `SAMEORIGIN` that is set in the back end:

[source,text]
----
frontend public
  http-response set-header X-Frame-Options 'DENY'

frontend fe_sni
  http-response set-header X-Frame-Options 'DENY'

frontend fe_no_sni
  http-response set-header X-Frame-Options 'DENY'

backend be_secure:openshift-monitoring:alertmanager-main
  http-response set-header X-Frame-Options 'SAMEORIGIN'
----

Additionally, any actions defined in either the Ingress Controller or a route override values set using route annotations.

Any actions defined in a route override values set using route annotations.

Special case headers::

The following headers are either prevented entirely from being set or deleted, or allowed under specific circumstances:

.Special case header configuration options
[cols="5*a",options="header"]
|===
|Header name |Configurable using `IngressController` spec |Configurable using `Route` spec |Reason for disallowment |Configurable using another method

|`proxy`
|No
|No
|The `proxy` HTTP request header can be used to exploit vulnerable CGI applications by injecting the header value into the `HTTP_PROXY` environment variable. The `proxy` HTTP request header is also non-standard and prone to error during configuration.
|No

|`host`
|No
|Yes
|When the `host` HTTP request header is set using the `IngressController` CR, HAProxy can fail when looking up the correct route.
|No

|`strict-transport-security`
|No
|No
|The `strict-transport-security` HTTP response header is already handled using route annotations and does not need a separate implementation.
|Yes: the `haproxy.router.openshift.io/hsts_header` route annotation

|`cookie` and `set-cookie`
|No
|No
|The cookies that HAProxy sets are used for session tracking to map client connections to particular back-end servers. Allowing these headers to be set could interfere with HAProxy's session affinity and restrict HAProxy's ownership of a cookie.
|Yes:

* the `haproxy.router.openshift.io/disable_cookie` route annotation
* the `haproxy.router.openshift.io/cookie_name` route annotation

|===

|===
|Header name |Configurable using `Route` spec |Reason for disallowment |Configurable using another method

|`proxy`
|No
|The `proxy` HTTP request header can be used to exploit vulnerable CGI applications by injecting the header value into the `HTTP_PROXY` environment variable. The `proxy` HTTP request header is also non-standard and prone to error during configuration.
|No

|`host`
|Yes
|When the `host` HTTP request header is set using the `IngressController` CR, HAProxy can fail when looking up the correct route.
|No

|`strict-transport-security`
|No
|The `strict-transport-security` HTTP response header is already handled using route annotations and does not need a separate implementation.
|Yes: the `haproxy.router.openshift.io/hsts_header` route annotation

|`cookie` and `set-cookie`
|No
|The cookies that HAProxy sets are used for session tracking to map client connections to particular back-end servers. Allowing these headers to be set could interfere with HAProxy's session affinity and restrict HAProxy's ownership of a cookie.
|Yes:

* the `haproxy.router.openshift.io/disable_cookie` route annotation
* the `haproxy.router.openshift.io/cookie_name` route annotation

|===

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-ingress-set-or-delete-http-headers_{context}"]
= Setting or deleting HTTP request and response headers in an Ingress Controller

You can set or delete certain HTTP request and response headers for compliance purposes or other reasons. You can set or delete these headers either for all routes served by an Ingress Controller or for specific routes.

For example, you might want to migrate an application running on your cluster to use mutual TLS, which requires that your application checks for an X-Forwarded-Client-Cert request header, but the OpenShift Container Platform default Ingress Controller provides an X-SSL-Client-Der request header.

The following procedure modifies the Ingress Controller to set the X-Forwarded-Client-Cert request header, and delete the X-SSL-Client-Der request header.

.Prerequisites
* You have installed the OpenShift CLI (`oc`).
* You have access to an OpenShift Container Platform cluster as a user with the `cluster-admin` role.

.Procedure
. Edit the Ingress Controller resource:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator edit ingresscontroller/default
----

. Replace the X-SSL-Client-Der HTTP request header with the X-Forwarded-Client-Cert HTTP request header:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpHeaders:
    actions: <1>
      request: <2>
      - name: X-Forwarded-Client-Cert <3>
        action:
          type: Set <4>
          set:
           value: "%{+Q}[ssl_c_der,base64]" <5>
      - name: X-SSL-Client-Der
        action:
          type: Delete
----
<1> The list of actions you want to perform on the HTTP headers.
<2> The type of header you want to change. In this case, a request header.
<3> The name of the header you want to change. For a list of available headers you can set or delete, see _HTTP header configuration_.
<4> The type of action being taken on the header. This field can have the value `Set` or `Delete`.
<5> When setting HTTP headers, you must provide a `value`. The value can be a string from a list of available directives for that header, for example `DENY`, or it can be a dynamic value that will be interpreted using HAProxy's dynamic value syntax. In this case, a dynamic value is added.
+
[NOTE]
====
For setting dynamic header values for HTTP responses, allowed sample fetchers are `res.hdr` and `ssl_c_der`. For setting dynamic header values for HTTP requests, allowed sample fetchers are `req.hdr` and `ssl_c_der`. Both request and response dynamic values can use the `lower` and `base64` converters.
====

. Save the file to apply the changes.

// Module included in the following assemblies:
//
// * networking/configuring-ingress-controller

[id="nw-using-ingress-forwarded_{context}"]
= Using X-Forwarded headers

You configure the HAProxy Ingress Controller to specify a policy for how to handle HTTP headers including `Forwarded` and `X-Forwarded-For`. The Ingress Operator uses the `HTTPHeaders` field to configure the `ROUTER_SET_FORWARDED_HEADERS` environment variable of the Ingress Controller.

.Procedure

. Configure the `HTTPHeaders` field for the Ingress Controller.
.. Use the following command to edit the `IngressController` resource:
+
[source,terminal]
----
$ oc edit IngressController
----
+
.. Under `spec`, set the `HTTPHeaders` policy field to `Append`, `Replace`, `IfNone`, or `Never`:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpHeaders:
    forwardedHeaderPolicy: Append
----

== Example use cases

*As a cluster administrator, you can:*

* Configure an external proxy that injects the `X-Forwarded-For` header into each request before forwarding it to an Ingress Controller.
+
To configure the Ingress Controller to pass the header through unmodified, you specify the `never` policy. The Ingress Controller then never sets the headers, and applications receive only the headers that the external proxy provides.

* Configure the Ingress Controller to pass the `X-Forwarded-For` header that your external proxy sets on external cluster requests through unmodified.
+
To configure the Ingress Controller to set the `X-Forwarded-For` header on internal cluster requests, which do not go through the external proxy, specify the `if-none` policy. If an HTTP request already has the header set through the external proxy, then the Ingress Controller preserves it. If the header is absent because the request did not come through the proxy, then the Ingress Controller adds the header.

*As an application developer, you can:*

* Configure an application-specific external proxy that injects the `X-Forwarded-For` header.
+
To configure an Ingress Controller to pass the header through unmodified for an application's Route, without affecting the policy for other Routes, add an annotation `haproxy.router.openshift.io/set-forwarded-headers: if-none` or `haproxy.router.openshift.io/set-forwarded-headers: never` on the Route for the application.
+
[NOTE]
====
You can set the `haproxy.router.openshift.io/set-forwarded-headers` annotation on a per route basis, independent from the globally set value for the Ingress Controller.
====

// Enable or disable HTTP/2 on Ingress Controllers
// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-http2-haproxy_{context}"]
= Enable or disable HTTP/2 on Ingress Controllers

You can enable or disable transparent end-to-end HTTP/2 connectivity in HAProxy. Application owners can use HTTP/2 protocol capabilities, including single connection, header compression, binary streams, and more.

You can enable or disable HTTP/2 connectivity for an individual Ingress Controller or for the entire cluster.

[NOTE]
====
If you enable or disable HTTP/2 connectivity for an individual Ingress Controller and for the entire cluster, the HTTP/2 configuration for the Ingress Controller takes precedence over the HTTP/2 configuration for the cluster.
====

To enable the use of HTTP/2 for a connection from the client to an HAProxy instance, a route must specify a custom certificate. A route that uses the default certificate cannot use HTTP/2. This restriction is necessary to avoid problems from connection coalescing, where the client re-uses a connection for different routes that use the same certificate.

Consider the following use cases for an HTTP/2 connection for each route type:

* For a re-encrypt route, the connection from HAProxy to the application pod can use HTTP/2 if the application supports using Application-Level Protocol Negotiation (ALPN) to negotiate HTTP/2 with HAProxy. You cannot use HTTP/2 with a re-encrypt route unless the Ingress Controller has HTTP/2 enabled.
* For a passthrough route, the connection can use HTTP/2 if the application supports using ALPN to negotiate HTTP/2 with the client. You can use HTTP/2 with a passthrough route if the Ingress Controller has HTTP/2 enabled or disabled.
* For an edge-terminated secure route, the connection uses HTTP/2 if the service specifies only `appProtocol: kubernetes.io/h2c`. You can use HTTP/2 with an edge-terminated secure route if the Ingress Controller has HTTP/2 enabled or disabled.
* For an insecure route, the connection uses HTTP/2 if the service specifies only `appProtocol: kubernetes.io/h2c`. You can use HTTP/2 with an insecure route if the Ingress Controller has HTTP/2 enabled or disabled.

[IMPORTANT]
====
For non-passthrough routes, the Ingress Controller negotiates its connection to the application independently of the connection from the client. This means a client might connect to the Ingress Controller and negotiate HTTP/1.1. The Ingress Controller might then connect to the application, negotiate HTTP/2, and forward the request from the client HTTP/1.1 connection by using the HTTP/2 connection to the application.

This sequence of events causes an issue if the client subsequently tries to upgrade its connection from HTTP/1.1 to the WebSocket protocol. Consider that if you have an application that is intending to accept WebSocket connections, and the application attempts to allow for HTTP/2 protocol negotiation, the client fails any attempt to upgrade to the WebSocket protocol.
====

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-enable-http2_{context}"]
= Enabling HTTP/2

You can enable HTTP/2 on a specific Ingress Controller, or you can enable HTTP/2 for the entire cluster.

.Procedure

* To enable HTTP/2 on a specific Ingress Controller, enter the `oc annotate` command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator annotate ingresscontrollers/<ingresscontroller_name> ingress.operator.openshift.io/default-enable-http2=true <1>
----
+
<1> Replace `<ingresscontroller_name>` with the name of an Ingress Controller to enable HTTP/2.

* To enable HTTP/2 for the entire cluster, enter the `oc annotate` command:
+
[source,terminal]
----
$ oc annotate ingresses.config/cluster ingress.operator.openshift.io/default-enable-http2=true
----

[TIP]
====
Alternatively, you can apply the following YAML code to enable HTTP/2:
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
  annotations:
    ingress.operator.openshift.io/default-enable-http2: "true"
----
====

// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-disable-http2_{context}"]
= Disabling HTTP/2

You can disable HTTP/2 on a specific Ingress Controller, or you can disable HTTP/2 for the entire cluster.

.Procedure

* To disable HTTP/2 on a specific Ingress Controller, enter the `oc annotate` command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator annotate ingresscontrollers/<ingresscontroller_name> ingress.operator.openshift.io/default-enable-http2=false <1>
----
+
<1> Replace `<ingresscontroller_name>` with the name of an Ingress Controller to disable HTTP/2.

* To disable HTTP/2 for the entire cluster, enter the `oc annotate` command:
+
[source,terminal]
----
$ oc annotate ingresses.config/cluster ingress.operator.openshift.io/default-enable-http2=false
----

[TIP]
====
Alternatively, you can apply the following YAML code to disable HTTP/2:
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
  annotations:
    ingress.operator.openshift.io/default-enable-http2: "false"
----
====

// Configuring the PROXY protocol for an Ingress Controller
// Module included in the following assemblies:
//
// * networking/ingress-operator.adoc

[id="nw-ingress-controller-configuration-proxy-protocol_{context}"]
= Configuring the PROXY protocol for an Ingress Controller

A cluster administrator can configure the PROXY protocol when an Ingress Controller uses either the `HostNetwork`, `NodePortService`, or `Private` endpoint publishing strategy types. The PROXY protocol enables the load balancer to preserve the original client addresses for connections that the Ingress Controller receives. The original client addresses are useful for logging, filtering, and injecting HTTP headers. In the default configuration, the connections that the Ingress Controller receives only contain the source address that is associated with the load balancer.

[WARNING]
====
The default Ingress Controller with installer-provisioned clusters on non-cloud platforms that use a Keepalived Ingress Virtual IP (VIP) do not support the PROXY protocol.
====

The PROXY protocol enables the load balancer to preserve the original client addresses for connections that the Ingress Controller receives. The original client addresses are useful for logging, filtering, and injecting HTTP headers. In the default configuration, the connections that the Ingress Controller receives contain only the source IP address that is associated with the load balancer.

[IMPORTANT]
====
For a passthrough route configuration, servers in OpenShift Container Platform clusters cannot observe the original client source IP address. If you need to know the original client source IP address, configure Ingress access logging for your Ingress Controller so that you can view the client source IP addresses.

For re-encrypt and edge routes, the OpenShift Container Platform router sets the `Forwarded` and `X-Forwarded-For` headers so that application workloads check the client source IP address.

For more information about Ingress access logging, see "Configuring Ingress access logging".
====

Configuring the PROXY protocol for an Ingress Controller is not supported when using the `LoadBalancerService` endpoint publishing strategy type. This restriction is because when OpenShift Container Platform runs in a cloud platform, and an Ingress Controller specifies that a service load balancer should be used, the Ingress Operator configures the load balancer service and enables the PROXY protocol based on the platform requirement for preserving source addresses.

[IMPORTANT]
====
You must configure both OpenShift Container Platform and the external load balancer to use either the PROXY protocol or TCP.
====

This feature is not supported in cloud deployments. This restriction is because when OpenShift Container Platform runs in a cloud platform, and an Ingress Controller specifies that a service load balancer should be used, the Ingress Operator configures the load balancer service and enables the PROXY protocol based on the platform requirement for preserving source addresses.

[IMPORTANT]
====
You must configure both OpenShift Container Platform and the external load balancer to either use the PROXY protocol or to use Transmission Control Protocol (TCP).
====

.Prerequisites
* You created an Ingress Controller.

.Procedure
. Edit the Ingress Controller resource by entering the following command in your CLI:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator edit ingresscontroller/default
----

. Set the PROXY configuration:
+
* If your Ingress Controller uses the `HostNetwork` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.hostNetwork.protocol` subfield to `PROXY`:
+
.Sample `hostNetwork` configuration to `PROXY`
[source,yaml]
----
# ...
  spec:
    endpointPublishingStrategy:
      hostNetwork:
        protocol: PROXY
      type: HostNetwork
# ...
----

* If your Ingress Controller uses the `NodePortService` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.nodePort.protocol` subfield to `PROXY`:
+
.Sample `nodePort` configuration to `PROXY`
[source,yaml]
----
# ...
  spec:
    endpointPublishingStrategy:
      nodePort:
        protocol: PROXY
      type: NodePortService
# ...
----

* If your Ingress Controller uses the `Private` endpoint publishing strategy type, set the `spec.endpointPublishingStrategy.private.protocol` subfield to `PROXY`:
+
.Sample `private` configuration to `PROXY`
[source,yaml]
----
# ...
  spec:
    endpointPublishingStrategy:
      private:
        protocol: PROXY
    type: Private
# ...
----

[role="_additional-resources"]
.Additional resources

* Configuring Ingress access logging

// Specifying an alternative cluster domain using the appsDomain option
// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc
//

[id="nw-ingress-configuring-application-domain_{context}"]
= Specifying an alternative cluster domain using the appsDomain option

//OpenShift Dedicated or Amazon RH OpenShift cluster administrator

As a cluster administrator, you can specify an alternative to the default cluster domain for user-created routes by configuring the `appsDomain` field. The `appsDomain` field is an optional domain for OpenShift Container Platform to use instead of the default, which is specified in the `domain` field. If you specify an alternative domain, it overrides the default cluster domain for the purpose of determining the default host for a new route.

For example, you can use the DNS domain for your company as the default domain for routes and ingresses for applications running on your cluster.

.Prerequisites

//* You deployed an {OSD} cluster.
* You deployed an OpenShift Container Platform cluster.
* You installed the `oc` command-line interface.

.Procedure

. Configure the `appsDomain` field by specifying an alternative default domain for user-created routes.
+
.. Edit the ingress `cluster` resource:
+
[source,terminal]
----
$ oc edit ingresses.config/cluster -o yaml
----
+
.. Edit the YAML file:
+
.Sample `appsDomain` configuration to `test.example.com`
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
spec:
  domain: apps.example.com            <1>
  appsDomain: <test.example.com>      <2>
----
<1> Specifies the default domain. You cannot modify the default domain after installation.
<2> Optional: Domain for OpenShift Container Platform infrastructure to use for application routes. Instead of the default prefix, `apps`, you can use an alternative prefix like `test`.
+
. Verify that an existing route contains the domain name specified in the `appsDomain` field by exposing the route and verifying the route domain change:
//+
//.. Access the Ingress Controller Operator YAML file:
//+
//[source,terminal]
//----
//$ oc get ingresses.config/cluster -o yaml
//----
+
[NOTE]
====
Wait for the `openshift-apiserver` finish rolling updates before exposing the route.
====
+
.. Expose the route by entering the following command. The command outputs `route.route.openshift.io/hello-openshift exposed` to designate exposure of the route.
+
[source,terminal]
----
$ oc expose service hello-openshift
----
+
.. Get a list of routes by running the following command:
+
[source,terminal]
----
$ oc get routes
----
+
.Example output
[source,text]
----
NAME              HOST/PORT                                   PATH   SERVICES          PORT       TERMINATION   WILDCARD
hello-openshift   hello_openshift-<my_project>.test.example.com
hello-openshift   8080-tcp                 None
----

// Module included in the following assemblies:
//
// * ingress/ingress-operator.adoc

[id="nw-ingress-converting-http-header-case_{context}"]
= Converting HTTP header case

HAProxy lowercases HTTP header names by default; for example, changing `Host: xyz.com` to `host: xyz.com`. If legacy applications are sensitive to the capitalization of HTTP header names, use the Ingress Controller `spec.httpHeaders.headerNameCaseAdjustments` API field for a solution to accommodate legacy applications until they can be fixed.

[IMPORTANT]
====
OpenShift Container Platform includes HAProxy 2.8. If you want to update to this version of the web-based load balancer, ensure that you add the `spec.httpHeaders.headerNameCaseAdjustments` section to your cluster's configuration file.
====

As a cluster administrator, you can convert the HTTP header case by entering the `oc patch` command or by setting the `HeaderNameCaseAdjustments` field in the Ingress Controller YAML file.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user with the `cluster-admin` role.

.Procedure

* Capitalize an HTTP header by using the `oc patch` command.

.. Change the HTTP header from `host` to `Host` by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontrollers/default --type=merge --patch='{"spec":{"httpHeaders":{"headerNameCaseAdjustments":["Host"]}}}'
----
+
.. Create a `Route` resource YAML file so that the annotation can be applied to the application.
+
.Example of a route named `my-application`
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/h1-adjust-case: true <1>
  name: <application_name>
  namespace: <application_name>
# ...
----
<1> Set `haproxy.router.openshift.io/h1-adjust-case` so that the Ingress Controller can adjust the `host` request header as specified.

* Specify adjustments by configuring the `HeaderNameCaseAdjustments` field in the Ingress Controller YAML configuration file.

.. The following example Ingress Controller YAML file adjusts the `host` header to `Host` for HTTP/1 requests to appropriately annotated routes:
+
.Example Ingress Controller YAML
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpHeaders:
    headerNameCaseAdjustments:
    - Host
----
+
.. The following example route enables HTTP response header name case adjustments by using the `haproxy.router.openshift.io/h1-adjust-case` annotation:
+
.Example route YAML
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    haproxy.router.openshift.io/h1-adjust-case: true <1>
  name: my-application
  namespace: my-application
spec:
  to:
    kind: Service
    name: my-application
----
<1> Set `haproxy.router.openshift.io/h1-adjust-case` to true.

// Module included in the following assemblies:
//
// * networking/ingress_operator.adoc

[id="nw-configuring-router-compression_{context}"]
= Using router compression

You configure the HAProxy Ingress Controller to specify router compression globally for specific MIME types. You can use the `mimeTypes` variable to define the formats of MIME types to which compression is applied. The types are: application, image, message, multipart, text, video, or a custom type prefaced by "X-". To see the full notation for MIME types and subtypes, see RFC1341.

[NOTE]
====
Memory allocated for compression can affect the max connections. Additionally, compression of large buffers can cause latency, like heavy regex or long lists of regex.

Not all MIME types benefit from compression, but HAProxy still uses resources to try to compress if instructed to.  Generally, text formats, such as html, css, and js, formats benefit from compression, but formats that are already compressed, such as image, audio, and video, benefit little in exchange for the time and resources spent on compression.
====

.Procedure

. Configure the `httpCompression` field for the Ingress Controller.
.. Use the following command to edit the `IngressController` resource:
+
[source,terminal]
----
$ oc edit -n openshift-ingress-operator ingresscontrollers/default
----
+
.. Under `spec`, set the `httpCompression` policy field to `mimeTypes` and specify a list of MIME types that should have compression applied:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: default
  namespace: openshift-ingress-operator
spec:
  httpCompression:
    mimeTypes:
    - "text/html"
    - "text/css; charset=utf-8"
    - "application/json"
   ...
----

// Module included in the following assemblies:
//
// * networking/networking_operators/ingress-operator.adoc

[id="nw-exposing-router-metrics_{context}"]
= Exposing router metrics

[role="_abstract"]
You can retrieve Prometheus-format HAProxy ingress router metrics from port `1936` to monitor ingress load and troubleshoot routing behavior. By analyzing these metrics, you can identify capacity bottlenecks and determine when to scale your router deployment.

.Prerequisites

* You have cluster administrator access to the cluster.
* You configured your firewall to allow port `1936`.

[NOTE]
====
The Prometheus `/metrics` endpoint and the HAProxy HTML statistics dashboard are mutually exclusive exposition modes because the HAProxy router process serves one mode at a time. The Ingress Operator configures default Ingress Controller pods for Prometheus scraping (`/metrics` on port `1936`). Browsing `\http://<user>:<password>@<pod_IP>:1936/` for interactive HTML statistics is not supported concurrently with Prometheus metrics on deployments that the Ingress Operator configures in this manner.
====

.Procedure

. List the router pods in the ingress namespace by entering the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ingress
----
+
.Example output
[source,terminal]
----
NAME                               READY   STATUS    RESTARTS   AGE
router-default-76bfffb66c-46qwp   1/1     Running   0          11h
----

. Read the stats user from the router pod under `/var/lib/haproxy/conf/metrics-auth/` by entering the following command:
+
[source,terminal]
----
$ oc rsh <router_pod_name> cat /var/lib/haproxy/conf/metrics-auth/statsUsername
----

. Read the stats password from the router pod under `/var/lib/haproxy/conf/metrics-auth/` by entering the following command:
+
[source,terminal]
----
$ oc rsh <router_pod_name> cat /var/lib/haproxy/conf/metrics-auth/statsPassword
----

. Get pod details, including the IP address for the pod, by entering the following command:
+
[source,terminal]
----
$ oc describe pod <router_pod>
----

. Fetch Prometheus text metrics from the default port `1936` by entering the following command:
+
[source,terminal]
----
$ curl -u <user>:<password> http://<router_IP>:1936/metrics
----
+
If the stats endpoint serves TLS-protected Prometheus text, retrieve metrics over HTTPS instead by entering the following command:
+
[source,terminal]
----
$ curl -u <user>:<password> https://<router_IP>:1936/metrics -k
----
+
.Example output
[source,terminal]
----
...
# HELP haproxy_max_connections Hard limit on the number of connections (configured or imposed by ulimit -n).
# TYPE haproxy_max_connections gauge
haproxy_max_connections 50000
...
----

. Optional: In the OpenShift Container Platform web console, navigate to *Observe* → *Metrics*, or query Prometheus directly, to compare ingress load against the HAProxy allowance.
+
The `haproxy_max_connections` gauge reflects each scraped router endpoint's HAProxy allowance from `spec.tuningOptions.maxConnections` on the `IngressController`, bound by operating system limits such as `ulimit -n`. Before relying on ratios, confirm the labeled metric for front-end sessions that your HAProxy Prometheus exporter emits. For example, use `haproxy_frontend_current_sessions` when that series is available for your deployment.
+
Expressions similar to `sum(haproxy_frontend_current_sessions) / sum(haproxy_max_connections)` can estimate connection load across scrape targets after you verify those series for your deployment.
+
If the ratio approaches `1`, adjust `spec.tuningOptions.maxConnections` on the `IngressController` or scale the router deployment.

// Module filename: nw-customize-ingress-error-pages.adoc
// Module included in the following assemblies:
// * networking/ingress-controller-configuration.adoc

[id="nw-customize-ingress-error-pages_{context}"]
= Customizing HAProxy error code response pages

As a cluster administrator, you can specify a custom error code response page for either 503, 404, or both error pages. The HAProxy router serves a 503 error page when the application pod is not running or a 404 error page when the requested URL does not exist. For example, if you customize the 503 error code response page, then the page is served when the application pod is not running, and the default 404 error code HTTP response page is served by the HAProxy router for an incorrect route or a non-existing route.

Custom error code response pages are specified in a config map then patched to the Ingress Controller. The config map keys have two available file names as follows:
`error-page-503.http` and `error-page-404.http`.

Custom HTTP error code response pages must follow the HAProxy HTTP error page configuration guidelines. Here is an example of the default OpenShift Container Platform HAProxy router http 503 error code response page. You can use the default content as a template for creating your own custom page.

By default, the HAProxy router serves only a 503 error page when the application is not running or when the route is incorrect or non-existent. This default behavior is the same as the behavior on OpenShift Container Platform 4.8 and earlier. If a config map for the customization of an HTTP error code response is not provided, and you are using a custom HTTP error code response page, the router serves a default 404 or 503 error code response page.

[NOTE]
====
If you use the OpenShift Container Platform default 503 error code page as a template for your customizations, the headers in the file require an editor that can use CRLF line endings.
====

.Procedure

. Create a config map named `my-custom-error-code-pages` in the `openshift-config` namespace:
+
[source,terminal]
----
$ oc -n openshift-config create configmap my-custom-error-code-pages \
  --from-file=error-page-503.http \
  --from-file=error-page-404.http
----
+
[IMPORTANT]
====
If you do not specify the correct format for the custom error code response page, a router pod outage occurs. To resolve this outage, you must delete or correct the config map and delete the affected router pods so they can be recreated with the correct information.
====

. Patch the Ingress Controller to reference the `my-custom-error-code-pages` config map by name:
+
[source,terminal]
----
$ oc patch -n openshift-ingress-operator ingresscontroller/default --patch '{"spec":{"httpErrorCodePages":{"name":"my-custom-error-code-pages"}}}' --type=merge
----
+
The Ingress Operator copies the `my-custom-error-code-pages` config map from the `openshift-config` namespace to the `openshift-ingress` namespace. The Operator names the config map according to the pattern, `<your_ingresscontroller_name>-errorpages`, in the `openshift-ingress` namespace.

. Display the copy:
+
[source,terminal]
----
$ oc get cm default-errorpages -n openshift-ingress
----
+
.Example output
----
NAME                       DATA   AGE
default-errorpages         2      25s  <1>
----
<1> The example config map name is `default-errorpages` because the `default` Ingress Controller custom resource (CR) was patched.
+

. Confirm that the config map containing the custom error response page mounts on the router volume where the config map key is the filename that has the custom HTTP error code response:
+
* For 503 custom HTTP custom error code response:
+
[source,terminal]
----
$ oc -n openshift-ingress rsh <router_pod> cat /var/lib/haproxy/conf/error_code_pages/error-page-503.http
----
+
* For 404 custom HTTP custom error code response:
+
[source,terminal]
----
$ oc -n openshift-ingress rsh <router_pod> cat /var/lib/haproxy/conf/error_code_pages/error-page-404.http
----

.Verification

Verify your custom error code HTTP response:

. Create a test project and application:
+
[source,terminal]
----
$ oc new-project test-ingress
----
+
[source,terminal]
----
$ oc new-app django-psql-example
----

. For 503 custom http error code response:
.. Stop all the pods for the application.
.. Run the following curl command or visit the route hostname in the browser:
+
[source,terminal]
----
$ curl -vk <route_hostname>
----
. For 404 custom http error code response:
.. Visit a non-existent route or an incorrect route.
.. Run the following curl command or visit the route hostname in the browser:
+
[source,terminal]
----
$ curl -vk <route_hostname>
----

. Check if the `errorfile` attribute is properly in the `haproxy.config` file:
+
[source,terminal]
----
$ oc -n openshift-ingress rsh <router> cat /var/lib/haproxy/conf/haproxy.config | grep errorfile
----

//include::modules/nw-ingress-select-route.adoc[leveloffset=+2]

// Modules included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

[id="nw-ingress-setting-max-connections_{context}"]
= Setting the Ingress Controller maximum connections

A cluster administrator can set the maximum number of simultaneous connections for OpenShift router deployments. You can patch an existing Ingress Controller to increase the maximum number of connections.

.Prerequisites
* The following assumes that you already created an Ingress Controller

.Procedure
* Update the Ingress Controller to change the maximum number of connections for HAProxy:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"maxConnections": 7500}}}'
----
+
[WARNING]
====
If you set the `spec.tuningOptions.maxConnections` value greater than the current operating system limit, the HAProxy process will not start. See the table in the "Ingress Controller configuration parameters" section for more information about this parameter.
====

// Module included in the following assemblies:
// * understanding-networking.adoc

[id="sd-ingress-responsibility-matrix_{context}"]
= Management of default Ingress Controller functions

[role="_abstract"]
The following table details the components of the `default` Ingress Controller managed by the Ingress Operator and whether Red Hat Site Reliability Engineering (SRE) maintains this component on OpenShift Container Platform clusters.

.Ingress Operator Responsibility Chart

[cols="3,2a,2a",options="header"]
|===

|Ingress component
|Managed by
|Default configuration?

|Scaling Ingress Controller | SRE | Yes

|Ingress Operator thread count | SRE | Yes

|Ingress Controller access logging | SRE | Yes

|Ingress Controller sharding | SRE | Yes

|Ingress Controller route admission policy | SRE | Yes

|Ingress Controller wildcard routes | SRE | Yes

|Ingress Controller X-Forwarded headers | SRE | Yes

|Ingress Controller route compression | SRE | Yes

|===

// Module included in the following assemblies:
//
// * networking/networking_operators/ingress-operator.adoc

[id="osd-create-cluster-exclude-namespace-selector-settings_{context}"]
= Set namespace exclusions for the default ingress when creating a cluster

[role="_abstract"]
When you create an OpenShift Container Platform cluster, you can specify a namespace label selector so that namespaces matching those labels are excluded from the default `application ingress`. This allows you to exclude namespaces that host workloads through the default ingress, such as namespaces with sensitive data or internal services.

[NOTE]
====
Do not exclude namespaces that host required platform routes (for example, `openshift-console` or `openshift-authentication`). Excluding them can break the web console, downloads, or OAuth flows.
====

// Module included in the following assemblies:
//
// * networking/networking_operators/ingress-operator.adoc

[id="osd-create-cluster-exclude-namespace-selector-day1-cli_{context}"]
= Set namespace exclusions for the default ingress when creating a cluster in the CLI

[role="_abstract"]
Use the `ocm` CLI to pass namespace exclusions for the default ingress while creating your cluster.

.Prerequisites

* You installed the `ocm` CLI and logged in with credentials that can create clusters in {cluster-manager-first}.
* You are using the noninteractive mode for `ocm create cluster`. For interactive mode, use the prompts for ingress settings when they are available for your `ocm` version.

.Procedure

. Run `ocm create cluster -h` and confirm that your `ocm` version lists the `--exclude-namespace-selector` flag.

. Build your `ocm create cluster` command with the required parameters for your cloud provider and subscription model.
+
The following example shows only the ingress-related fragment. Replace the rest of the flags with the values required for your environment.
+
[source,terminal]
----
$ ocm create cluster <cluster_name> \
  --provider=<aws_or_gcp> \
  <other_required_flags> \
  --default-ingress-excluded-namespace-selectors '<key>=<value>,<key2>=<value2>'
----
+
where:

`<cluster_name>`:: Specifies the cluster name.

`--provider=<aws_or_gcp>`:: Specifies the cloud provider.

`<other_required_flags>`:: Required parameters such as region, version, Customer Cloud Subscription (CCS) settings, or billing flags, as described in the cluster creation documentation for your platform.

`--default-ingress-excluded-namespace-selectors`:: Specifies label selectors that exclude matching namespaces from the default application ingress. The service validates these exclusions. Replace `<key>=<value>` with your labels. Do not include spaces around the `=` sign.

.Verification

* After the cluster reaches `ready` state, confirm ingress settings and inspect the default ingress object for the configured exclusion data.
+
[source,terminal]
----
$ ocm list ingress -c <cluster_name>
----

// Module included in the following assemblies:
//
// * networking/networking_operators/ingress-operator.adoc

[id="osd-create-cluster-exclude-namespace-selector-day2-cli_{context}"]
= Changing namespace exclusions for the default ingress on your cluster in the CLI

[role="_abstract"]
Use the `ocm` CLI to pass namespace exclusions for the default ingress to your OpenShift Container Platform cluster.

.Prerequisites

* You installed the `ocm` CLI and logged in with credentials that can modify clusters in {cluster-manager-first}.
* You have configured a OpenShift Container Platform cluster.

.Procedure

. Run the following command to pass the namespace exclusions to your cluster:
+
[source,terminal]
----
$ ocm edit ingress <ingress_name> -c <cluster_id> \
  --excluded-namespace-selectors "key1=val1,key2=val2,key1=val3,foo=bar" \
  <cluster_name>
----
+
where:

`<ingress_name>`:: Specifies your ingress name.

`<cluster_id>`:: Specifies your cluster ID.

`--excluded-namespace-selectors "key1=val1,key2=val2,key1=val3,foo=bar"`:: Specifies label selectors that exclude matching namespaces from the default application ingress. The service validates these exclusions. Replace `<key>=<value>` with your labels. Do not include spaces around the `=` sign.

`<cluster_name>`:: Specifies the cluster name.

// Module included in the following assemblies:
//
// * networking/networking_operators/ingress-operator.adoc

[id="osd-create-cluster-exclude-namespace-selector-day1-ui_{context}"]
= Set namespace exclusions for the default ingress when creating a cluster in {cluster-manager-first}

[role="_abstract"]
Specify a namespace label selector so that namespaces matching those labels are excluded from the default `application ingress` when creating an OpenShift Container Platform cluster in {cluster-manager-url}.

.Procedure

. On the *Networking* screen, select *Custom Settings* under *Application ingress settings*.
+
[NOTE]
====
All of the custom settings are optional.
====
+
. In *Route selector*, enter a comma-separated list of `key=value` pairs to limit which routes this ingress exposes.
Leave the field empty if all routes should remain eligible based on your other choices.
. In *Excluded namespaces*, enter a comma-separated list of namespace names whose routes must not use this ingress.
. In *Exclude namespace selectors*, specify one or more label selectors. For each selector, provide a label key and a comma-separated list of label values. The default Ingress Controller does not apply to namespaces whose labels satisfy any of the configured selectors.
+
[IMPORTANT]
====
Do not include spaces around commas, for example, use `finance,HR,legal`, and not `finance, HR, legal`.
====
+
. Set *Namespace ownership policy* for route admission when namespaces share hostnames, for example, select *Strict* for restrictive admission.
. Set *Wildcard policy* to allow or disallow wildcard patterns in route hostnames, for example, select *Disallowed* to block wildcard host routes.
+
For more information about custom application ingress settings, click the information icon provided for each setting.

// Module included in the following assemblies:
//
// * networking/networking_operators/ingress-operator.adoc

[id="osd-create-cluster-exclude-namespace-selector-day2-ui_{context}"]
= Change namespace exclusions for the ingress on a cluster in {cluster-manager-first}

[role="_abstract"]
Specify a namespace label selector so that namespaces matching those labels are excluded from the default `application ingress` on your configured OpenShift Container Platform cluster in {cluster-manager}.

.Procedure

. From {cluster-manager-url}, navigate to the *Cluster List* page and select the cluster that you want to set namespace exclusions for.

. On the selected cluster, select the *Networking* tab.

. Select *Edit application ingress*.
+
[NOTE]
====
All of the custom settings are optional.
====
+
. In *Route selector*, enter a comma-separated list of `key=value` pairs to limit which routes this ingress exposes.
Leave the field empty if all routes should remain eligible based on your other choices.
. In *Excluded namespaces*, enter a comma-separated list of namespace names whose routes must not use this ingress.
. In *Exclude namespace selectors*, specify one or more label selectors. For each selector, provide a label key and a comma-separated list of label values. The default Ingress Controller does not apply to namespaces whose labels satisfy any of the configured selectors.
+
[IMPORTANT]
====
Do not include spaces around commas, for example, use `finance,HR,legal`, and not `finance, HR, legal`.
====
+
. Set *Namespace ownership policy* for route admission when namespaces share hostnames, for example, select *Strict* for restrictive admission.
. Set *Wildcard policy* to allow or disallow wildcard patterns in route hostnames, for example, select *Disallowed* to block wildcard host routes.
+
For more information about custom application ingress settings, click the information icon provided for each setting.

. Select *Save* to configure the ingress with your changes.

[role="_additional-resources"]
== Additional resources

* Configuring a custom PKI
* Creating a Workload Identity Federation cluster using {cluster-manager}
* Creating a cluster on Google Cloud with a Red Hat cloud account using {cluster-manager}
* Creating a cluster with Service Account authentication using {cluster-manager}
