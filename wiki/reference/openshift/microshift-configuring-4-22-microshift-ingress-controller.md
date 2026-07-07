---
title: "Using ingress control for a {microshift-short} node"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-ingress-controller
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-ingress-controller
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Using ingress control for a {microshift-short} node

[id="microshift-ingress-controller"]
= Using ingress control for a {microshift-short} node

[role="_abstract"]
To make pods and services accessible outside the node, you must configure the ingress controller options in the {microshift-short} configuration file.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-ingress-controller.adoc

[id="microshift-ingress-control-concept_{context}"]
= Using ingress control in {microshift-short}

[role="_abstract"]
When you create your {microshift-short} node, each pod and service running on the node is allocated an IP address. These IP addresses are accessible to other pods and services running nearby by default, but are not accessible to external clients. {microshift-short} uses a minimal implementation of the {OCP} `IngressController` API to enable external access to node services.

With more configuration options, you can fine-tune ingress to meet your specific needs. To use enhanced ingress control, update the parameters in the {microshift-short} configuration file and restart the service.

Ingress configuration is useful in a variety of ways, for example:

Accommodate server response speed::
* If your application starts processing requests from clients but the connection closes before it can respond, you can set the `ingress.tuningOptions.serverTimeout` parameter in the configuration file to a higher value to accommodate the speed of the response from the server.

Closing router connections::
* If the router has many connections open because an application running on the node does not close connections properly, you can set the `ingress.tuningOptions.serverTimeout` and `spec.tuningOptions.serverFinTimeout` parameters to a lower value, forcing those connections to close sooner.

Verify client certificates::
* If you need to configure the ingress controller to verify client certificates, you can use the `ingress.clientTLS` parameter to set a clientCA value, which is a reference to a config map. The config map contains the PEM-encoded CA certificate bundle that is used to verify a client's certificate. Optionally, you can also configure a list of certificate subject filters.

Configure a TLS security profile::
* If you need to configure a TLS security profile for an ingress controller, you can use the `ingress.tlsSecurityProfile` parameter to specify a default or custom individual TLS security profiles. The TLS security profile defines the minimum TLS version and the TLS ciphers for TLS connections for the ingress controllers.
If a TLS security profile is not configured, the default value is based on the TLS security profile set for the API server.

Create policies for new route claims::
* If you need to define a policy for handling new route claims, you can use the `routeAdmission` parameter to allow or deny claims across namespaces. Set the `routeAdmission` parameter to describe how hostname claims across namespaces should be handled and to describe how the ingress controller handles routes with wildcard policies.

Customize error pages::
* If you want more than the default error pages, which are usually empty and only return the HTTP status code, configure custom error pages.

Capture HTTP headers or cookies::
* If you want to include the capture of HTTP headers or cookies, configure them in the access logging.

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-ingress-controller.adoc

[id="microshift-ingress-control-config_{context}"]
= Configuring ingress control in {microshift-short}

[role="_abstract"]
To apply detailed ingress control such as timeouts, TLS, and logging in {microshift-short}, you can update the `config.yaml` file or add a configuration snippet in the `/etc/microshift/config.d/` directory. Replace the default values in the ingress section and restart the service.

[IMPORTANT]
====
* A `config.yaml` configuration file takes precedence over built-in settings. The `config.yaml` file is read every time the {microshift-short} service starts.
* Configuration snippet YAMLs take precedence over both built-in settings and the `config.yaml` configuration file.
====

.Prerequisites

* You installed the {oc-first}.
* You have root access to the node.
* Your node uses the OVN-Kubernetes Container Network Interface (CNI) plugin.

.Procedure

. Apply ingress control settings in one of the two following ways:

.. Update the {microshift-short} `config.yaml` configuration file by making a copy of the provided `config.yaml.default` file in the `/etc/microshift/` directory, naming it `config.yaml` and keeping it in the source directory.

.. Use a configuration snippet to apply the ingress control settings you want. To do this, create a configuration snippet YAML file and put it in the `/etc/microshift/config.d/` configuration directory.

. Replace the default values in the `ingress` section of the {microshift-short} YAML with your valid values, or create a configuration snippet file with the sections you need.
+
.Ingress controller configuration fields with default values
[source,yaml]
----
apiServer:
# ...
ingress:
  accessLogging:
    destination:
      container:
        maxLength: 1024
      syslog:
        address: ""
        facility: ""
        maxLength: 1024
        port: 0
      type: ""
    httpCaptureCookies:
      - matchType: ""
        maxLength: 0
        name: ""
        namePrefix: ""
    httpCaptureHeaders:
      request:
        - maxLength: 0
          name: ""
      response:
        - maxLength: 0
          name: ""
    httpLogFormat: ""
    status: Disabled
  certificateSecret: router-certs-custom
  clientTLS:
    allowedSubjectPatterns: []
    clientCA:
      name: ""
    clientCertificatePolicy: ""
  defaultHTTPVersion: 1
  forwardedHeaderPolicy: Append
  httpCompression:
    mimeTypes:
      - ""
  httpEmptyRequestsPolicy: Respond
  httpErrorCodePages:
      name: ""
  listenAddress: []
  logEmptyRequests: Log
  ports:
     http: 80
     https: 443
  routeAdmissionPolicy:
    namespaceOwnership: InterNamespaceAllowed
    wildcardPolicy: WildcardsDisallowed
  status: Managed
  tlsSecurityProfile:
    type:
    custom:
      ciphers:[]
      minTLSVersion:""
    intermediate: {}
    old: {}
  tuningOptions:
    clientFinTimeout: 1s
    clientTimeout: 30s
    headerBufferBytes: 0
    headerBufferMaxRewriteBytes: 0
    healthCheckInterval: 5s
    maxConnections: 0
    serverFinTimeout: 1s
    serverTimeout: 30s
    threadCount: 4
    tlsInspectDelay: 5s
    tunnelTimeout: 1h
# ...
----
+
See "Ingress controller configuration fields in {microshift-short}" for more information about each field.

. Complete any other configurations you require, then start or restart {microshift-short} by running one the following commands:
+
[source,terminal]
----
$ sudo systemctl start microshift
----
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

.Verification

After making ingress configuration changes and restarting {microshift-short}, you can check the age of the router pod to ensure that changes are applied.

* To check the status of the router pod, run the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ingress
----
+
.Example output
[source,terminal]
----
NAME                              READY   STATUS    RESTARTS   AGE
router-default-8649b5bf65-w29cn   1/1     Running   0          6m10s
----

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-ingress-controller.adoc

[id="microshift-ingress-control-config-fields_{context}"]
= Ingress controller configuration fields in {microshift-short}

[role="_abstract"]
The following table lists and defines the ingress controller configuration parameters in the {microshift-short} `config.yaml` file. You use these parameters when you configure access logging, TLS, timeouts, route admission, and other ingress options.

.Ingress controller configuration fields definitions table
[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`ingress`
|The `ingress` section of the {microshift-short} `config.yaml` file defines the configurable parameters for the implementation of the {OCP} `IngressController` API. All of the following parameters in this table are subsections in the `ingress` section of the {microshift-short} `config.yaml`.

|`accessLogging`
|This `ingress` subsection describes how client requests are logged. If the `status` field is empty, access logging is disabled. When the status field is set to `Enabled`, access requests are logged as configured with the `accessLogging` parameters and the `accessLogging.destination.type` is automatically set to `Container`.

* When enabled, access logging is part of the `openshift-router` logs. The sos report procedure for {microshift-short} captures logs from this pod.

|`accessLogging.destination`
|A destination for logs. The destination for logs can be a local sidecar container or remote. Default value is null.

|`accessLogging.destination.type`
|The type of destination for logs. Valid values are `Container` or `Syslog`.

* Setting this value to `Container` specifies that logs should go to a sidecar container. When the destination type is set to `Container`, a container called `logs` is automatically created. Using container logs means that logs might be dropped if the rate of logs exceeds the container runtime capacity or the custom logging solution capacity. You must have a custom logging solution that reads logs from this sidecar.

* Setting this value to `Syslog` specifies that logs are sent to a Syslog endpoint. You must configure a custom Syslog instance and specify an endpoint that can receive Syslog messages. You must have a custom Syslog instance. For example, Getting started with kernel logging.

|`accessLogging.destination.container`
|Describes parameters for the `Container` logging destination type. You must configure a custom logging solution that reads logs from this sidecar.

|`accessLogging.destination.container.maxLength`
|Optional configuration. The default value is `1024` bytes. Message length must be at least `480` and not greater than `8192` bytes.

|`accessLogging.destination.syslog`
|Describes parameters for the `Syslog` logging destination type. You must configure a custom Syslog instance with an endpoint that can receive Syslog messages.

|`accessLogging.destination.syslog.address`
|Required configuration when the `Syslog` destination type is set. Valid value is the IP address of the syslog endpoint that receives log messages.

|`accessLogging.destination.syslog.facility`
|Optional configuration when the `Syslog` destination type is set. Specifies the syslog facility of log messages. If this field is empty, the facility is `local1`. Otherwise, the field must specify one of the following valid syslog facilities: `kern`, `user`, `mail`, `daemon`, `auth`, `syslog`, `lpr`, `news`, `uucp`, `cron`, auth2`, `ftp`, `ntp`, `audit`, `alert`, `cron2`, `local0`, `local1`, `local2`, `local3`, `local4`, `local5`, `local6`, or `local7`.

|`accessLogging.destination.syslog.maxLength`
|Optional configuration when the `Syslog` destination type is set. The maximum length of the `Syslog` message. Message length must be at least `480` and not greater than `4096` bytes. If this field is empty, the maximum length is set to the default value of `1024` bytes.

|`accessLogging.destination.syslog.port`
|Required configuration when the `Syslog` destination type is set. The UDP port number of the syslog endpoint that receives log messages. The default value is `0`.

|`httpCaptureCookies`
|Specifies HTTP cookies that you want to capture in access logs. If the `httpCaptureCookies` field is empty, access logs do not capture the cookies. Default value is empty. Configuring `ingress.accessLogging.httpCaptureCookies` automatically enables ingress access logging. For any cookie that you want to capture, you must also set the `matchType` and `maxLength` parameters.

* For example:
+
[source,yam]
----
  httpCaptureCookies:
  - matchType: Exact
    maxLength: 128
    name: MYCOOKIE
----

|`httpCaptureCookies.matchType`
|Specifies whether the field name of the cookie exactly matches the capture cookie setting or is a prefix of the capture cookie setting. Valid values are `Exact` for an exact string match and `Prefix` for a string prefix match.

* If you use the `Exact` setting, you must also specify a name in the `httpCaptureCookies.name` field.
* If you use the `Prefix` setting, you must also specify a prefix in the `httpCaptureCookies.namePrefix` field. For example, the settings of `matchType: Prefix` when the `namePrefix` is "mush" captures a cookie named "mush" or "mushroom" but not one named "room". The first matching cookie is captured.

|`httpCaptureCookies.maxLength`
|Specifies the maximum length of the cookie that is logged, which includes the cookie name, cookie value, and
one-character delimiter. If the log entry exceeds this length, the value is truncated in the log message. The ingress controller might impose a separate bound on the total length of HTTP headers in a request. The minimum value is `1` byte, maximum value is `1024` bytes. The default value is `0`.

|`httpCaptureCookies.name`
|Specifies the exact name used for a cookie name match as set in the `httpCaptureCookies.matchType` parameter. The value must be a valid HTTP cookie name as defined in RFC 6265 section 4.1. The minimum length is `1` byte and the maximum length is `1024` bytes.

|`httpCaptureCookies.namePrefix`
|Specifies the prefix for a cookie name match as set in the `httpCaptureCookies.matchType` parameter. The value must be a valid HTTP cookie name as defined in RFC 6265 section 4.1. The minimum length is `1` byte and the maximum length is `1024` bytes.

|`httpCaptureHeaders`
|Defines the HTTP headers that should be captured in the access logs. This field is a list and allows capturing request and response headers independently. When this field is empty, headers are not captured. This option only applies to plain text HTTP connections and to secure HTTP connections for which the ingress controller terminates encryption: for example, edge-terminated or reencrypt connections. Headers cannot be captured for TLS `passthrough` connections. Configuring the `ingress.accessLogging.httpCaptureHeaders` parameter automatically enables ingress access logging.

|`httpCaptureHeaders.request`
|Specifies which HTTP request headers to capture. When this field is empty, no request headers are captured.

|`httpCaptureHeaders.request.maxLength`
|Specifies a maximum length for the header value. When a header value exceeds this length, the value is truncated in the log message. The minimum required value is `1` byte. The ingress controller might impose a separate bound on the total length of HTTP headers in a request.

|`httpCaptureHeaders.request.name`
|Specifies a header name. The value must be a valid HTTP header name as defined in RFC 2616 section 4.2. If you configure this value, you must specify `maxLength` and `name` values.

|`httpCaptureHeaders.response`
|Specifies which HTTP response headers to capture. If this field is empty, no response headers are captured.

|`httpCaptureHeaders.response.maxLength`
|Specifies a maximum length for the header value. If a header value exceeds this length, the value is truncated in the
log message. The ingress controller might impose a separate bound on the total length of HTTP headers in a request.

|`httpCaptureHeaders.response.name`
|Specifies a header name. The value must be a valid HTTP header name as defined in RFC 2616 section 4.2.

|`httpLogFormat`
|Specifies the format of the log message for an HTTP request. If this field is empty, log messages use the default HTTP log format. For HAProxy default HTTP log format, see the HAProxy documentation.

|`status`
|Specifies whether access is logged or not. Valid values are `Enabled` and `Disabled`. Default value is `Disabled`.

* When you configure either `ingress.accessLogging.httpCaptureHeaders` or
`ingress.accessLogging.httpCaptureCookies`, you must set `ingress.accessLogging.status` to `Enabled`.
* When you set the `ingress.status` field to `Enabled`, the `accessLogging.destination.type` is automatically set to `Container` and the router logs all requests in the `logs` container.
* If you set this value to `Disabled`, the router does not log any requests in the access log.

|`certificateSecret`
|A reference to a `kubernetes.io/tls` type of secret that contains the default certificate that the {microshift-short} ingress controller serves. When routes do not specify their own certificate, the `certificateSecret` parameter is used. All secrets used must contain `tls.key` key file contents and `tls.crt` certificate file contents.

* When the `certificateSecret` parameter is not set, a wildcard certificate is automatically generated and used. The wildcard certificate is valid for the ingress controller default `domain` and its `subdomains`. The generated certificate authority (CA) is automatically integrated with the truststore of the node.

* In-use generated and user-specified certificates are automatically integrated with the {microshift-short} built-in OAuth server.

|`clientTLS`
|Authenticates client access to the node and services. As a result, mutual TLS authentication is enabled. If this parameter is not set, then client TLS is not enabled. You must set the `spec.clientTLS.clientCertificatePolicy` and `spec.clientTLS.clientCA` parameters to use client TLS.

|`clientTLS.AllowedSubjectPatterns`
|Optional subfield that specifies a list of regular expressions that are matched against the distinguished name on a valid client certificate to filter requests. This parameter is useful when you have client authentication. Use this parameter to cause the ingress controller to reject certificates based on the distinguished name. The Perl Compatible Regular Expressions (PCRE) syntax is required. You must set the `spec.clientTLS.clientCertificatePolicy` and `spec.clientTLS.clientCA` parameters to use `clientTLS.AllowedSubjectPatterns`.

[IMPORTANT]
====
When configured, this field must contain a valid expression or the {microshift-short} service fails. At least one pattern must match a client certificate's distinguished name; otherwise, the ingress controller rejects the certificate and denies the connection.
====

|`clientTLS.clientCA`
|Specifies a required config map that is in the `openshift-ingress` namespace. Required to enable client TLS. The config map must contain a certificate authority (CA) bundle named `ca-bundle.pem` or the deployment of the default router fails.

|`clientTLS.clientCA.name`
|The `metadata.name` of the config map referenced in the `clientTLS.clientCA` value.

|`clientTLS.ClientCertificatePolicy`
|`Required` or `Optional` are valid values. Set to `Required` to enable client TLS. The ingress controller only checks client certificates for edge-terminated and re-encrypted TLS routes. The ingress controller cannot check certificates for plain text HTTP or passthrough TLS routes.

|`defaultHTTPVersion`
|Sets the HTTP version for the ingress controller. The default value is `1` for HTTP 1.1. Setting up a load balancer for HTTP 2 and 3 is recommended.

|`forwardedHeaderPolicy`
|Specifies when and how the ingress controller sets the `Forwarded`, `X-Forwarded-For`, `X-Forwarded-Host`, `X-Forwarded-Port`, `X-Forwarded-Proto`, and `X-Forwarded-Proto-Version` HTTP headers. The following values are valid:

* `Append` preserves any existing headers by specifying that the ingress controller appends them. 'Append` is the default value.
* `Replace` removes any existing headers by specifying that the ingress controller sets the headers.
* `IfNone` sets the headers set by specifying that the ingress controller sets the headers if they are not already set.
* `Never` preserves any existing headers by specifying that the ingress controller never sets the headers.

|`httpCompression`
|Defines the policy for HTTP traffic compression.

|`httpCompression.mimeTypes`
|Defines a list of MIME types to which compression should be applied.

* For example, `text/css; charset=utf-8`, `text/html`, `text/*`, `image/svg+xml`, `application/octet-stream`, `X-custom/customsub`, in the, `type/subtype; [;attribute=value]` format.
* Valid `types` are: application, image, message, multipart, text, video, or a custom type prefaced by `X-`. To see the full notation for MIME types and subtypes, see RFC1341 (IETF Datatracker documentation).

|`httpEmptyRequestsPolicy`
|Describes how HTTP connections are handled if the connection times out before a request is received. Allowed values for this field are `Respond` and `Ignore`. The default value is `Respond`. Empty requests typically come from load-balancer health probes or preconnects and can often be safely ignored. However, network errors and port scans can also cause these requests. Therefore, setting this field to `Ignore` can impede detection or diagnosis of network problems and detecting intrusion attempts.

* When the policy is set to `Respond`, the ingress controller sends an HTTP `400` or `408` response, logs the connection if access logging is enabled, and counts the connection in the appropriate metrics.

* When the policy is set to `Ignore`, the `http-ignore-probes` parameter is added to the `HAproxy` process configuration. After this parameter is added, the ingress controller closes the connection without sending a response, then either logs the connection or incrementing metrics.

|`logEmptyRequests`
|Specifies connections for which no request is received and logged. `Log` and `Ignore` are valid values. Empty requests typically come from load-balancer health probes or preconnects and can often be safely ignored. However, network errors and port scans can also cause these requests. Therefore, setting this field to `Ignore` can impede detection or diagnosis of network problems and detecting intrusion attempts. The default value is `Log`.

* Setting this value to `Log` indicates that an event should be logged.
* Setting this value to `Ignore` sets the `dontlognull` option in the `HAproxy` configuration.

|`httpErrorCodePages`
|Describes custom error code pages. To use this setting, you must configure the `httpErrorCodePages.name` parameter.

|`httpErrorCodePages.name`
|Specifies custom error code pages. You can only customize errors for `503` and `404` page codes. To customize error code pages, specify a `ConfigMap` name. The `ConfigMap` object must be in the `openshift-ingress` namespace and contain keys in the `error-page-<error code>.http` format where `<error code>` is an HTTP status code. Each value in the `ConfigMap` must be the full response, including HTTP headers. The default value of this parameter is null.

|`ports`
|Defines default router ports.

|`ports.http`
|Default router http port. Must be in range 1-65535. Default value is `80`.

|`ports.https`
|Default router https port. Must be in range 1-65535. Default value is `443`.

|`routeAdmission`
|Defines a policy for handling new route claims, such as allowing or denying claims across namespaces.

|`routeAdmission.namespaceOwnership`
|Describes how hostname claims across namespaces are handled. The default is `InterNamespaceAllowed`. The following are valid values:

* `Strict` does not allow routes to claim the same hostname across namespaces.
* `InterNamespaceAllowed` allows routes to claim different paths of the same hostname across namespaces.

|`routeAdmission.wildcardPolicy`
|Controls how the ingress controller handles routes with configured wildcard policies. `WildcardsAllowed` and `WildcardsDisallowed` are valid values. Default value is `WildcardsDisallowed`.

* `WildcardPolicyAllowed` means that the ingress controller admits routes with any wildcard policy.

* `WildcardPolicyDisallowed` means that the ingress controller admits only routes with a wildcard policy of `None`.

[IMPORTANT]
====
Changing the wildcard policy from `WildcardsAllowed` to `WildcardsDisallowed` causes admitted routes with a wildcard policy of `subdomain` to stop working. The ingress controller only readmits these routes after they are recreated with a wildcard policy of `None`.
====

|`status`
|Default router status. `Managed` or `Removed` are valid values.

|`tlsSecurityProfile`
|`tlsSecurityProfile` specifies settings for TLS connections for ingress controllers. If not set, the default value is based on the `apiservers.config.openshift.io/cluster` resource. The TLS `1.0` version of an `Old` or `Custom` profile is automatically converted to `1.1` by the ingress controller. `Intermediate` is the default setting.

* The minimum TLS version for ingress controllers is `1.1`. The maximum TLS version is `1.3`.

[NOTE]
====
The `TLSProfile` status shows the ciphers and the minimum TLS version of the configured security profile. Profiles are intent-based and change over time when new ciphers are developed and existing ciphers are found to be insecure. The usable list can be reduced depending on which ciphers are available to a specific process.
====

|`tlsSecurityProfile.custom`
|User-defined TLS security profile. If you configure this parameter and related parameters, use extreme caution.

|`tlsSecurityProfile.custom.ciphers`
|Specifies the cipher algorithms that are negotiated during the TLS handshake. Operators might remove entries their operands do not support.

|`tlsSecurityProfile.custom.minTLSVersion`
|Specifies the minimal version of the TLS protocol that is negotiated during the TLS handshake. For example, to use TLS versions 1.1, 1.2 and 1.3, set the value to `VersionTLS11`. The highest valid value for `minTLSVersion` is `VersionTLS12`.

|`tlsSecurityProfile.intermediate`
|You can use this TLS profile for a majority of services. Intermediate compatibility (recommended).

|`tlsSecurityProfile.old`
|Used for backward compatibility. Old backward compatibility.

|`tlsSecurityProfile.type`
|Valid values are `Intermediate`, `Old`, or `Custom`. The `Modern` value is not supported.

|`tuningOptions`
|Specifies options for tuning the performance of ingress controller pods.

|`tuningOptions.clientFinTimeout`
|Specifies how long the ingress controller holds a connection open while waiting for a client response before the server closes the connection. The default timeout is `1s`.

|`tuningOptions.clientTimeout`
|Specifies how long the ingress controller holds a connection open while waiting for a client response. The default timeout is `30s`.

|`tuningOptions.headerBufferBytes`
|Specifies how much memory is reserved, in bytes, for ingress controller connection sessions. This value must be at least `16384` if HTTP/2 is enabled for the ingress controller. If not set, the default value is `32768` bytes.

[IMPORTANT]
====
Setting this field not recommended because `headerBufferMaxRewriteBytes` parameter values that are too small can break the ingress controller. Conversely, values for `headerBufferMaxRewriteBytes` that are too large could cause the ingress controller to use significantly more memory than necessary.
====

|`tuningOptions.headerBufferMaxRewriteBytes`
|Specifies how much memory should be reserved, in bytes, from `headerBufferBytes` for HTTP header rewriting and appending for ingress controller connection sessions. The minimum value for `headerBufferMaxRewriteBytes` is `4096`. `headerBufferBytes` must be greater than the `headerBufferMaxRewriteBytes` value for incoming HTTP requests. If not set, the default value is `8192` bytes.

[IMPORTANT]
====
Setting this field is not recommended because `headerBufferMaxRewriteBytes` values that are too small can break the ingress controller and `headerBufferMaxRewriteBytes` that are too large could cause the ingress controller to use significantly more memory than necessary.
====

|`tuningOptions.healthCheckInterval`
|Specifies how long the router waits between health checks, set in seconds. The default is `5s`.

|`tuningOptions.maxConnections`
|Specifies the maximum number of simultaneous connections that can be established for each `HAProxy` process. Increasing this value allows each ingress controller pod to handle more connections at the cost of additional system resources. Permitted values are `0`, `-1`, any value within the range `2000` and `2000000`, or the field can be left empty.

* If this field is empty or has the value `0`, the ingress controller uses the default value of `50000`.

* If the field has the value of `-1`, then the `HAProxy` process dynamically computes a maximum value based on the available `ulimits` in the running container. This process results in a large computed value that incurs significant memory usage compared to the current default value of `50000`.

* If the field has a value that is greater than the current operating system limit, the `HAProxy` processes do not start.

* If you choose a discrete value and the router pod is migrated to a new node, it is possible that the new node does not have an identical `ulimit` configured. In such cases, the pod fails to start.

* You can monitor memory usage for router containers with the `container_memory_working_set_bytes{container="router",namespace="openshift-ingress"}` metric.

* You can monitor memory usage of individual `HAProxy` processes in router containers with the `container_memory_working_set_bytes{container="router",namespace="openshift-ingress"}/container_processes{container="router",namespace="openshift-ingress"}` metric.

|`tuningOptions.serverFinTimeout`
|Specifies how long a connection is held open while waiting for the server response to the client that is closing the connection. The default timeout is `1s`.

|`tuningOptions.serverTimeout`
|Specifies how long a connection is held open while waiting for a server response. The default timeout is `30s`.

|`tuningOptions.threadCount`
|Specifies the number of threads to create per HAProxy process. Creating more threads allows each ingress controller pod to handle more connections, at the cost of using more system resources. The HAProxy load balancer supports up to `64` threads. If this field is empty, the ingress controller uses the default value of `4` threads.

[IMPORTANT]
====
Setting this field is not recommended because increasing the number of `HAProxy` threads allows ingress controller pods to use more CPU time under load, and prevent other pods from receiving the CPU resources they need to perform. Reducing the number of threads can cause the ingress controller to perform poorly.
====

|`tuningOptions.tlsInspectDelay`
|Specifies how long the router can hold data to find a matching route. Setting this value too low can cause the router to fall back to the default certificate for edge-terminated, re-encrypted, or passthrough routes, even when using a better-matched certificate. The default inspect delay is `5s`.

|`tuningOptions.tunnelTimeout`
|Specifies how long a tunnel connection, including websockets, remains open while the tunnel is idle. The default timeout is `1h`.

|===

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-ingress-controller.adoc

[id="microshift-ingress-controller-create-cert-secret_{context}"]
= Creating a secret for the ingress controller certificateSecret

[role="_abstract"]
To secure network traffic with your own certificate, you must create a TLS secret and update the configuration file. This process configures a custom default certificate for the {microshift-short} ingress router.

[NOTE]
====
Any in-use certificates automatically integrate with the {microshift-short} built-in OAuth server.
====

To configure application-level certificates for a Kubernetes Ingress object by using the `spec.tls` field, follow the procedure in "Creating a route through an Ingress object".

.Prerequisites

* Root access to the {microshift-short} host.
* Installation of the {oc-first}.
* A decrypted, non-password-protected TLS private key in Privacy-Enhanced Mail (PEM) format.
* A PEM-encoded TLS certificate.
* A valid certificate for the {microshift-short} apps wildcard where the `subjectAltName` extension includes DNS names covering `*.apps.<nodename>.<domain>`.

[NOTE]
====
This procedure only applies to the default ingress router certificate, `ingress.certificateSecret`.
====

.Procedure

. Create a secret that contains the wildcard certificate chain and key:
+
[source,terminal]
----
$ oc create secret tls <secret> \
     --cert=</path/to/cert.crt> \
     --key=</path/to/cert.key> \
     -n openshift-ingress
----
+
** Replace `<secret>` with the name of the secret that contains the certificate chain and private key.
** Replace `</path/to/cert.crt>` with the path to the certificate chain on your local file system.
** Replace `</path/to/cert.key>` with the path to the private key associated with this certificate.
+
[IMPORTANT]
====
The certificate must include the `subjectAltName` extension showing `*.apps.<nodename>.<domain>`.
====

. Update the `certificateSecret` parameter value in the {microshift-short} configuration YAML with the newly created secret.

. Complete any other configurations you require, then start or restart {microshift-short} by running one of the following commands:
+
[source,terminal]
----
$ sudo systemctl start microshift
----
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

[role="_additional-resources"]
.Additional resources

* Creating a route through an Ingress object

// Module included in the following assemblies:
//
// * microshift_configuring/microshift-ingress-controller.adoc

[id="microshift-ingress-controller-config_{context}"]
= Configuring the TLS security profile for the ingress controller

[role="_abstract"]
To configure the TLS security profile for the ingress controller in {microshift-short}, you can add the `spec.tlsSecurityProfile` field to the configuration YAML and set a value for the appropriate profile. To apply the changes, restart the service.

.Prerequisites

* You have root access to the {microshift-short} node.

.Procedure

. Add the `spec.tlsSecurityProfile` field to the {microshift-short} YAML configuration file.
+
[source,yaml]
----
 ...
spec:
  tlsSecurityProfile:
    type: Custom
    custom:
      ciphers:
      - ECDHE-ECDSA-CHACHA20-POLY1305
      - ECDHE-RSA-CHACHA20-POLY1305
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-ECDSA-AES128-GCM-SHA256
      minTLSVersion: VersionTLS11
 ...
----
+
where:

`spec.tlsSecurityProfile.type`:: Specifies the TLS security profile type (`Old`, `Intermediate`, or `Custom`). The default is `Intermediate`.
`spec.tlsSecurityProfile.custom`:: Specifies the appropriate field for the selected type:
** `old: {}`
** `intermediate: {}`
** `custom:`
`spec.tlsSecurityProfile.custom.ciphers`:: Specifies a list of TLS ciphers and minimum accepted TLS version.
+
[WARNING]
====
If you choose a `custom` TLS configuration, use extreme caution. Using self-signed TLS certificates can introduce security risks.
====

. Save the file to apply the changes.

. Restart {microshift-short} by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

[id="additional-resources_microshift-ingress-controller_{context}"]
[role="_additional-resources"]
== Additional resources

* Enabling HTTP/2 Ingress connectivity ({OCP} documentation)
