---
title: "Configuring metrics for core platform monitoring"
type: reference
domain: openshift
slug: observability-4-22-configuring-metrics
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/configuring-metrics
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring metrics for core platform monitoring

[id="configuring-metrics"]
= Configuring metrics for core platform monitoring

Configure the collection of metrics to monitor how cluster components and your own workloads are performing.

You can send ingested metrics to remote systems for long-term storage and add cluster ID labels to the metrics to identify the data coming from different clusters.

[role="_additional-resources"]
.Additional resources

* Understanding metrics

// Configuring remote write storage
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="configuring-remote-write-storage_{context}"]
= Configuring remote write storage

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

You can configure remote write storage to enable Prometheus to send ingested metrics to remote systems for long-term storage. Doing so has no impact on how or for how long Prometheus stores metrics.

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` `ConfigMap` object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.
* You have set up a remote write compatible endpoint (such as Thanos) and know the endpoint URL. See the Prometheus remote endpoints and storage documentation for information about endpoints that are compatible with the remote write feature.
+
[IMPORTANT]
====
Red{nbsp}Hat only provides information for configuring remote write senders and does not offer guidance on configuring receiver endpoints. Customers are responsible for setting up their own endpoints that are remote-write compatible. Issues with endpoint receiver configurations are not included in Red{nbsp}Hat production support.
====
* You have set up authentication credentials in a `Secret` object for the remote write endpoint. You must create the secret in the `{namespace-name}` namespace.
+
[WARNING]
====
To reduce security risks, use HTTPS and authentication to send metrics to an endpoint.
====

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. Add a `remoteWrite:` section under `data/config.yaml/{component}`, as shown in the following example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com" # <1>
        <endpoint_authentication_credentials> # <2>
----
<1> The URL of the remote write endpoint.
<2> The authentication method and credentials for the endpoint.
Currently supported authentication methods are AWS Signature Version 4, authentication using HTTP in an `Authorization` request header, Basic authentication, OAuth 2.0, and TLS client.
See _Supported remote write authentication settings_ for sample configurations of supported authentication methods.

. Add write relabel configuration values after the authentication credentials:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com"
        <endpoint_authentication_credentials>
        writeRelabelConfigs:
        - <your_write_relabel_configs> #<1>
----
<1> Add configuration for metrics that you want to send to the remote endpoint.
+
.Example of forwarding a single metric called `my_metric`
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com"
        writeRelabelConfigs:
        - sourceLabels: [__name__]
          regex: 'my_metric'
          action: keep
----
+
.Example of forwarding metrics called `my_metric_1` and `my_metric_2` in `my_namespace` namespace
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com"
        writeRelabelConfigs:
        - sourceLabels: [__name__,namespace]
          regex: '(my_metric_1|my_metric_2);my_namespace'
          action: keep
----

. Save the file to apply the changes. The new configuration is applied automatically.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* `writeRelabelConfigs`
* `relabel_config` (Prometheus documentation)

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="supported-remote-write-authentication-settings_{context}"]
= Supported remote write authentication settings

You can use different methods to authenticate with a remote write endpoint. Currently supported authentication methods are AWS Signature Version 4, basic authentication, authorization, OAuth 2.0, and TLS client. The following table provides details about supported authentication methods for use with remote write.

[options="header"]
|===

|Authentication method|Config map field|Description

|AWS Signature Version 4|`sigv4`|This method uses AWS Signature Version 4 authentication to sign requests.
You cannot use this method simultaneously with authorization, OAuth 2.0, or Basic authentication.

|Basic authentication|`basicAuth`|Basic authentication sets the authorization header on every remote write request with the configured username and password.

|authorization|`authorization`|Authorization sets the `Authorization` header on every remote write request using the configured token.

|OAuth 2.0|`oauth2`|An OAuth 2.0 configuration uses the client credentials grant type.
Prometheus fetches an access token from `tokenUrl` with the specified client ID and client secret to access the remote write endpoint.
You cannot use this method simultaneously with authorization, AWS Signature Version 4, or Basic authentication.

|TLS client|`tlsConfig`|A TLS client configuration specifies the CA certificate, the client certificate, and the client key file information used to authenticate with the remote write endpoint server using TLS.
The sample configuration assumes that you have already created a CA certificate file, a client certificate file, and a client key file.

|===

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="example-remote-write-authentication-settings_{context}"]
= Example remote write authentication settings

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

The following samples show different authentication settings you can use to connect to a remote write endpoint. Each sample also shows how to configure a corresponding `Secret` object that contains authentication credentials and other relevant settings. Each sample configures authentication for use with
// tag::CPM[]
default platform monitoring
// end::CPM[]
// tag::UWM[]
monitoring for user-defined projects
// end::UWM[]
in the `{namespace-name}` namespace.

[id="remote-write-sample-yaml-aws-sigv4_{context}"]
== Sample YAML for AWS Signature Version 4 authentication

The following shows the settings for a `sigv4` secret named `sigv4-credentials` in the `{namespace-name}` namespace.

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  name: sigv4-credentials
  namespace: {namespace-name}
stringData:
  accessKey: <AWS_access_key> <1>
  secretKey: <AWS_secret_key> <2>
type: Opaque
----
<1> The AWS API access key.
<2> The AWS API secret key.

The following shows sample AWS Signature Version 4 remote write authentication settings that use a `Secret` object named `sigv4-credentials` in the `{namespace-name}` namespace:

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://authorization.example.com/api/write"
        sigv4:
          region: <AWS_region> <1>
          accessKey:
            name: sigv4-credentials <2>
            key: accessKey <3>
          secretKey:
            name: sigv4-credentials <2>
            key: secretKey <4>
          profile: <AWS_profile_name> <5>
          roleArn: <AWS_role_arn> <6>
----
<1> The AWS region.
<2> The name of the `Secret` object containing the AWS API access credentials.
<3> The key that contains the AWS API access key in the specified `Secret` object.
<4> The key that contains the AWS API secret key in the specified `Secret` object.
<5> The name of the AWS profile that is being used to authenticate.
<6> The unique identifier for the Amazon Resource Name (ARN) assigned to your role.

[id="remote-write-sample-yaml-basic-auth_{context}"]
== Sample YAML for Basic authentication

The following shows sample Basic authentication settings for a `Secret` object named `rw-basic-auth` in the `{namespace-name}` namespace:

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  name: rw-basic-auth
  namespace: {namespace-name}
stringData:
  user: <basic_username> <1>
  password: <basic_password> <2>
type: Opaque
----
<1> The username.
<2> The password.

The following sample shows a `basicAuth` remote write configuration that uses a `Secret` object named `rw-basic-auth` in the `{namespace-name}` namespace.
It assumes that you have already set up authentication credentials for the endpoint.

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://basicauth.example.com/api/write"
        basicAuth:
          username:
            name: rw-basic-auth <1>
            key: user <2>
          password:
            name: rw-basic-auth <1>
            key: password <3>
----
<1> The name of the `Secret` object that contains the authentication credentials.
<2> The key that contains the username  in the specified `Secret` object.
<3> The key that contains the password in the specified `Secret` object.

[id="remote-write-sample-yaml-bearer-token_{context}"]
== Sample YAML for authentication with a bearer token using a `Secret` Object

The following shows bearer token settings for a `Secret` object named `rw-bearer-auth` in the `{namespace-name}` namespace:

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  name: rw-bearer-auth
  namespace: {namespace-name}
stringData:
  token: <authentication_token> <1>
type: Opaque
----
<1> The authentication token.

The following shows sample bearer token config map settings that use a `Secret` object named `rw-bearer-auth` in the `{namespace-name}` namespace:

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://authorization.example.com/api/write"
        authorization:
          type: Bearer <1>
          credentials:
            name: rw-bearer-auth <2>
            key: token <3>
----
<1> The authentication type of the request. The default value is `Bearer`.
<2> The name of the `Secret` object that contains the authentication credentials.
<3> The key that contains the authentication token in the specified `Secret` object.

[id="remote-write-sample-yaml-oauth-20_{context}"]
== Sample YAML for OAuth 2.0 authentication

The following shows sample OAuth 2.0 settings for a `Secret` object named `oauth2-credentials` in the `{namespace-name}` namespace:

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  name: oauth2-credentials
  namespace: {namespace-name}
stringData:
  id: <oauth2_id> <1>
  secret: <oauth2_secret> <2>
type: Opaque
----
<1> The Oauth 2.0 ID.
<2> The OAuth 2.0 secret.

The following shows an `oauth2` remote write authentication sample configuration that uses a `Secret` object named `oauth2-credentials` in the `{namespace-name}` namespace:

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://test.example.com/api/write"
        oauth2:
          clientId:
            secret:
              name: oauth2-credentials <1>
              key: id <2>
          clientSecret:
            name: oauth2-credentials <1>
            key: secret <2>
          tokenUrl: https://example.com/oauth2/token <3>
          scopes: <4>
          - <scope_1>
          - <scope_2>
          endpointParams: <5>
            param1: <parameter_1>
            param2: <parameter_2>
----
<1> The name of the corresponding `Secret` object. Note that `ClientId` can alternatively refer to a `ConfigMap` object, although `clientSecret` must refer to a `Secret` object.
<2> The key that contains the OAuth 2.0 credentials in the specified `Secret` object.
<3> The URL used to fetch a token with the specified `clientId` and `clientSecret`.
<4> The OAuth 2.0 scopes for the authorization request. These scopes limit what data the tokens can access.
<5> The OAuth 2.0 authorization request parameters required for the authorization server.

[id="remote-write-sample-yaml-tls_{context}"]
== Sample YAML for TLS client authentication

The following shows sample TLS client settings for a `tls` `Secret` object named `mtls-bundle` in the `{namespace-name}` namespace.

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: Secret
metadata:
  name: mtls-bundle
  namespace: {namespace-name}
data:
  ca.crt: <ca_cert> <1>
  client.crt: <client_cert> <2>
  client.key: <client_key> <3>
type: tls
----
<1> The CA certificate in the Prometheus container with which to validate the server certificate.
<2> The client certificate for authentication with the server.
<3> The client key.

The following sample shows a `tlsConfig` remote write authentication configuration that uses a TLS `Secret` object named `mtls-bundle`.

[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com"
        tlsConfig:
          ca:
            secret:
              name: mtls-bundle <1>
              key: ca.crt <2>
          cert:
            secret:
              name: mtls-bundle <1>
              key: client.crt <3>
          keySecret:
            name: mtls-bundle <1>
            key: client.key <4>
----
<1> The name of the corresponding `Secret` object that contains the TLS authentication credentials. Note that `ca` and `cert` can alternatively refer to a `ConfigMap` object, though `keySecret` must refer to a `Secret` object.
<2> The key in the specified `Secret` object that contains the CA certificate for the endpoint.
<3> The key in the specified `Secret` object that contains the client certificate for the endpoint.
<4> The key in the specified `Secret` object that contains the client key secret.

// Unset the source code block attributes just to be safe.

// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="example-remote-write-queue-configuration_{context}"]
= Example remote write queue configuration

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

You can use the `queueConfig` object for remote write to tune the remote write queue parameters. The following example shows the queue parameters with their default values for
// tag::CPM[]
default platform monitoring
// end::CPM[]
// tag::UWM[]
monitoring for user-defined projects
// end::UWM[]
in the `{namespace-name}` namespace.

.Example configuration of remote write parameters with default values
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com"
        <endpoint_authentication_credentials>
        queueConfig:
          capacity: 10000 #<1>
          minShards: 1 #<2>
          maxShards: 50 #<3>
          maxSamplesPerSend: 2000 #<4>
          batchSendDeadline: 5s #<5>
          minBackoff: 30ms #<6>
          maxBackoff: 5s #<7>
          retryOnRateLimit: false #<8>
          sampleAgeLimit: 0s #<9>
----
<1> The number of samples to buffer per shard before they are dropped from the queue.
<2> The minimum number of shards.
<3> The maximum number of shards.
<4> The maximum number of samples per send.
<5> The maximum time for a sample to wait in buffer.
<6> The initial time to wait before retrying a failed request. The time gets doubled for every retry up to the `maxbackoff` time.
<7> The maximum time to wait before retrying a failed request.
<8> Set this parameter to `true` to retry a request after receiving a 429 status code from the remote write storage.
<9> The samples that are older than the `sampleAgeLimit` limit are dropped from the queue. If the value is undefined or set to `0s`, the parameter is ignored.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Prometheus REST API reference for remote write
* Remote write compatible endpoints (Prometheus documentation)
* Remote write tuning (Prometheus documentation)
* Understanding secrets

// Module included in the following assemblies:
//
// * observability/monitoring/troubleshooting-monitoring-issues.adoc

[id="table-of-remote-write-metrics_{context}"]
= Table of remote write metrics

The following table contains remote write and remote write-adjacent metrics with further description to help solve issues during remote write configuration.

[options="header"]
|===
| Metric | Description
| `prometheus_remote_storage_highest_timestamp_in_seconds` | Shows the newest timestamp that Prometheus stored in the write-ahead log (WAL) for any sample.
| `prometheus_remote_storage_queue_highest_sent_timestamp_seconds` | Shows the newest timestamp that the remote write queue successfully sent.
| `prometheus_remote_storage_samples_retried_total` | The number of samples that remote write failed to send and had to resend to remote storage. A steady high rate for this metric indicates problems with the network or remote storage endpoint.
| `prometheus_remote_storage_shards` | Shows how many shards are currently running for each remote endpoint.
| `prometheus_remote_storage_shards_desired` | Shows the calculated needed number of shards based on the current write throughput and the rate of incoming versus sent samples.
| `prometheus_remote_storage_shards_max` | Shows the maximum number of shards based on the current configuration.
| `prometheus_remote_storage_shards_min` | Shows the minimum number of shards based on the current configuration.
| `prometheus_tsdb_wal_segment_current` | The WAL segment file that Prometheus is currently writing new data to.
| `prometheus_wal_watcher_current_segment` | The WAL segment file that each remote write instance is currently reading from.
|===

//Creating cluster ID labels for metrics for core platform monitoring
// Module included in the following assemblies:
//
// * observability/monitoring/configuring-the-monitoring-stack.adoc

[id="creating-cluster-id-labels-for-metrics_{context}"]
= Creating cluster ID labels for metrics

// Set attributes to distinguish between cluster monitoring example (core platform monitoring - CPM) and user workload monitoring (UWM) examples
// tag::CPM[]
// end::CPM[]
// tag::UWM[]
// end::UWM[]

You can create cluster ID labels for metrics by adding the `write_relabel` settings for remote write storage in the `{configmap-name}` config map in the `{namespace-name}` namespace.

// tag::UWM[]
[NOTE]
====
When Prometheus scrapes user workload targets that expose a `namespace` label, the system stores this label as `exported_namespace`.
This behavior ensures that the final namespace label value is equal to the namespace of the target pod.
You cannot override this default configuration by setting the value of the `honorLabels` field to `true` for `PodMonitor` or `ServiceMonitor` objects.
====
// end::UWM[]

.Prerequisites

// tag::CPM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
// end::CPM[]
// tag::UWM[]
* You have access to the cluster as a user with the `cluster-admin` cluster role, or as a user with the `user-workload-monitoring-config-edit` role in the `openshift-user-workload-monitoring` project.
* A cluster administrator has enabled monitoring for user-defined projects.
* You have access to the cluster as a user with the `dedicated-admin` role.
* The `user-workload-monitoring-config` ConfigMap object exists. This object is created by default when the cluster is created.
// end::UWM[]
* You have installed the {oc-first}.
* You have configured remote write storage.

.Procedure

. Edit the `{configmap-name}` config map in the `{namespace-name}` project:
+
[source,terminal,subs="attributes+"]
----
$ oc -n {namespace-name} edit configmap {configmap-name}
----

. In the `writeRelabelConfigs:` section under `data/config.yaml/{component}/remoteWrite`, add cluster ID relabel configuration values:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com"
        <endpoint_authentication_credentials>
        writeRelabelConfigs: # <1>
          - <relabel_config> # <2>
----
<1> Add a list of write relabel configurations for metrics that you want to send to the remote endpoint.
<2> Substitute the label configuration for the metrics sent to the remote write endpoint.
+
The following sample shows how to forward a metric with the cluster ID label `cluster_id`:
+
[source,yaml,subs="attributes+"]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: {configmap-name}
  namespace: {namespace-name}
data:
  config.yaml: |
    {component}:
      remoteWrite:
      - url: "https://remote-write-endpoint.example.com"
        writeRelabelConfigs:
        - sourceLabels:
          - __tmp_openshift_cluster_id__ # <1>
          targetLabel: cluster_id # <2>
          action: replace # <3>
----
<1> The system initially applies a temporary cluster ID source label named `+++__tmp_openshift_cluster_id__+++`. This temporary label gets replaced by the cluster ID label name that you specify.
<2> Specify the name of the cluster ID label for metrics sent to remote write storage. If you use a label name that already exists for a metric, that value is overwritten with the name of this cluster ID label. For the label name, do not use `+++__tmp_openshift_cluster_id__+++`. The final relabeling step removes labels that use this name.
<3> The `replace` write relabel action replaces the temporary label with the target label for outgoing metrics. This action is the default and is applied if no action is specified.

. Save the file to apply the changes. The new configuration is applied automatically.

// Unset the source code block attributes just to be safe.

[role="_additional-resources"]
.Additional resources

* Adding cluster ID labels to metrics
* Obtaining your cluster ID
