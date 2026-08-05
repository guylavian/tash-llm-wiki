---
title: "Configuring log forwarding"
type: reference
domain: openshift
slug: observability-4-22-log6x-clf-6-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/log6x-clf-6.2
version: 4.22
family: observability
documentKind: "Documentation"
---

# Configuring log forwarding

[id="log6x-clf-6-2"]
= Configuring log forwarding

The `ClusterLogForwarder` (CLF) allows users to configure forwarding of logs to various destinations. It provides a flexible way to select log messages from different sources, send them through a pipeline that can transform or filter them, and forward them to one or more outputs.

.Key Functions of the ClusterLogForwarder
* Selects log messages using inputs
* Forwards logs to external destinations using outputs
* Filters, transforms, and drops log messages using filters
* Defines log forwarding pipelines connecting inputs, filters and outputs

// Module included in the following assemblies:
//
// observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-collection-setup_{context}"]
= Setting up log collection

This release of Cluster Logging requires administrators to explicitly grant log collection permissions to the service account associated with *ClusterLogForwarder*. This was not required in previous releases for the legacy logging scenario consisting of a *ClusterLogging* and, optionally, a *ClusterLogForwarder.logging.openshift.io* resource.

The {clo} provides `collect-audit-logs`, `collect-application-logs`, and `collect-infrastructure-logs` cluster roles, which enable the collector to collect audit logs, application logs, and infrastructure logs respectively.

Setup log collection by binding the required cluster roles to your service account.

== Legacy service accounts
To use the existing legacy service account `logcollector`, create the following *ClusterRoleBinding*:

[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-application-logs system:serviceaccount:openshift-logging:logcollector
----

[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-infrastructure-logs system:serviceaccount:openshift-logging:logcollector
----

Additionally, create the following *ClusterRoleBinding* if collecting audit logs:

[source,terminal]
----
$ oc adm policy add-cluster-role-to-user collect-audit-logs system:serviceaccount:openshift-logging:logcollector
----

== Creating service accounts
.Prerequisites

* The {clo} is installed in the `openshift-logging` namespace.
* You have administrator permissions.

.Procedure

. Create a service account for the collector. If you want to write logs to storage that requires a token for authentication, you must include a token in the service account.

. Bind the appropriate cluster roles to the service account:
+
.Example binding command
[source,terminal]
----
$ oc adm policy add-cluster-role-to-user <cluster_role_name> system:serviceaccount:<namespace_name>:<service_account_name>
----

=== Cluster Role Binding for your Service Account
The role_binding.yaml file binds the ClusterLogging operator's ClusterRole to a specific ServiceAccount, allowing it to manage Kubernetes resources cluster-wide.

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: manager-rolebinding
roleRef:                                           <1>
  apiGroup: rbac.authorization.k8s.io              <2>
  kind: ClusterRole                                <3>
  name: cluster-logging-operator                   <4>
subjects:                                          <5>
  - kind: ServiceAccount                           <6>
    name: cluster-logging-operator                 <7>
    namespace: openshift-logging                   <8>
----
<1> roleRef: References the ClusterRole to which the binding applies.
<2> apiGroup: Indicates the RBAC API group, specifying that the ClusterRole is part of Kubernetes' RBAC system.
<3> kind: Specifies that the referenced role is a ClusterRole, which applies cluster-wide.
<4> name: The name of the ClusterRole being bound to the ServiceAccount, here cluster-logging-operator.
<5> subjects: Defines the entities (users or service accounts) that are being granted the permissions from the ClusterRole.
<6> kind: Specifies that the subject is a ServiceAccount.
<7> Name: The name of the ServiceAccount being granted the permissions.
<8> namespace: Indicates the namespace where the ServiceAccount is located.

=== Writing application logs
The write-application-logs-clusterrole.yaml file defines a ClusterRole that grants permissions to write application logs to the Loki logging application.

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-logging-write-application-logs
rules:                                              <1>
  - apiGroups:                                      <2>
      - loki.grafana.com                            <3>
    resources:                                      <4>
      - application                                 <5>
    resourceNames:                                  <6>
      - logs                                        <7>
    verbs:                                          <8>
      - create                                      <9>
----
<1> rules: Specifies the permissions granted by this ClusterRole.
<2> apiGroups: Refers to the API group loki.grafana.com, which relates to the Loki logging system.
<3> loki.grafana.com: The API group for managing Loki-related resources.
<4> resources: The resource type that the ClusterRole grants permission to interact with.
<5> application: Refers to the application resources within the Loki logging system.
<6> resourceNames: Specifies the names of resources that this role can manage.
<7> logs: Refers to the log resources that can be created.
<8> verbs: The actions allowed on the resources.
<9> create: Grants permission to create new logs in the Loki system.

=== Writing audit logs
The write-audit-logs-clusterrole.yaml file defines a ClusterRole that grants permissions to create audit logs in the Loki logging system.
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-logging-write-audit-logs
rules:                                              <1>
  - apiGroups:                                      <2>
      - loki.grafana.com                            <3>
    resources:                                      <4>
      - audit                                       <5>
    resourceNames:                                  <6>
      - logs                                        <7>
    verbs:                                          <8>
      - create                                      <9>
----
<1> rules: Defines the permissions granted by this ClusterRole.
<2> apiGroups: Specifies the API group loki.grafana.com.
<3> loki.grafana.com: The API group responsible for Loki logging resources.
<4> resources: Refers to the resource type this role manages, in this case, audit.
<5> audit: Specifies that the role manages audit logs within Loki.
<6> resourceNames: Defines the specific resources that the role can access.
<7> logs: Refers to the logs that can be managed under this role.
<8> verbs: The actions allowed on the resources.
<9> create: Grants permission to create new audit logs.

=== Writing infrastructure logs
The write-infrastructure-logs-clusterrole.yaml file defines a ClusterRole that grants permission to create infrastructure logs in the Loki logging system.

.Sample YAML
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-logging-write-infrastructure-logs
rules:                                              <1>
  - apiGroups:                                      <2>
      - loki.grafana.com                            <3>
    resources:                                      <4>
      - infrastructure                              <5>
    resourceNames:                                  <6>
      - logs                                        <7>
    verbs:                                          <8>
      - create                                      <9>
----
<1> rules: Specifies the permissions this ClusterRole grants.
<2> apiGroups: Specifies the API group for Loki-related resources.
<3> loki.grafana.com: The API group managing the Loki logging system.
<4> resources: Defines the resource type that this role can interact with.
<5> infrastructure: Refers to infrastructure-related resources that this role manages.
<6> resourceNames: Specifies the names of resources this role can manage.
<7> logs: Refers to the log resources related to infrastructure.
<8> verbs: The actions permitted by this role.
<9> create: Grants permission to create infrastructure logs in the Loki system.

=== ClusterLogForwarder editor role
The clusterlogforwarder-editor-role.yaml file defines a ClusterRole that allows users to manage ClusterLogForwarders in OpenShift.

[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: clusterlogforwarder-editor-role
rules:                                              <1>
  - apiGroups:                                      <2>
      - observability.openshift.io                  <3>
    resources:                                      <4>
      - clusterlogforwarders                        <5>
    verbs:                                          <6>
      - create                                      <7>
      - delete                                      <8>
      - get                                         <9>
      - list                                        <10>
      - patch                                       <11>
      - update                                      <12>
      - watch                                       <13>
----
<1> rules: Specifies the permissions this ClusterRole grants.
<2> apiGroups: Refers to the OpenShift-specific API group
<3> obervability.openshift.io: The API group for managing observability resources, like logging.
<4> resources: Specifies the resources this role can manage.
<5> clusterlogforwarders: Refers to the log forwarding resources in OpenShift.
<6> verbs: Specifies the actions allowed on the ClusterLogForwarders.
<7> create: Grants permission to create new ClusterLogForwarders.
<8> delete: Grants permission to delete existing ClusterLogForwarders.
<9> get: Grants permission to retrieve information about specific ClusterLogForwarders.
<10> list: Allows listing all ClusterLogForwarders.
<11> patch: Grants permission to partially modify ClusterLogForwarders.
<12> update: Grants permission to update existing ClusterLogForwarders.
<13> watch: Grants permission to monitor changes to ClusterLogForwarders.

[id="modifying-log-level_6-2_{context}"]
== Modifying log level in collector

To modify the log level in the collector, you can set the `observability.openshift.io/log-level` annotation to `trace`, `debug`, `info`, `warn`, `error`, and `off`.

.Example log level annotation
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: collector
  annotations:
    observability.openshift.io/log-level: debug
# ...
----

[id="managing-the-operator_6-2_{context}"]
== Managing the Operator

The `ClusterLogForwarder` resource has a `managementState` field that controls whether the operator actively manages its resources or leaves them Unmanaged:

Managed:: (default) The operator will drive the logging resources to match the desired state in the CLF spec.

Unmanaged:: The operator will not take any action related to the logging components.

This allows administrators to temporarily pause log forwarding by setting `managementState` to `Unmanaged`.

[id="clf-structure_6-2_{context}"]
== Structure of the ClusterLogForwarder

The CLF has a `spec` section that contains the following key components:

Inputs:: Select log messages to be forwarded. Built-in input types `application`, `infrastructure` and `audit` forward logs from different parts of the cluster. You can also define custom inputs.

Outputs:: Define destinations to forward logs to. Each output has a unique name and type-specific configuration.

Pipelines:: Define the path logs take from inputs, through filters, to outputs. Pipelines have a unique name and consist of a list of input, output and filter names.

Filters:: Transform or drop log messages in the pipeline. Users can define filters that match certain log fields and drop or modify the messages. Filters are applied in the order specified in the pipeline.

[id="clf-inputs_6-2_{context}"]
=== Inputs

Inputs are configured in an array under `spec.inputs`. There are three built-in input types:

application:: Selects logs from all application containers, excluding those in infrastructure namespaces.

infrastructure:: Selects logs from nodes and from infrastructure components running in the following namespaces:
** `default`
** `kube`
** `openshift`
** Containing the `kube-` or `openshift-` prefix

audit:: Selects logs from the OpenShift API server audit logs, Kubernetes API server audit logs, ovn audit logs, and node audit logs from auditd.

Users can define custom inputs of type `application` that select logs from specific namespaces or using pod labels.

[id="clf-outputs_6-2_{context}"]
=== Outputs

Outputs are configured in an array under `spec.outputs`. Each output must have a unique name and a type. Supported types are:

azureMonitor:: Forwards logs to Azure Monitor.
cloudwatch:: Forwards logs to AWS CloudWatch.
elasticsearch:: Forwards logs to an external Elasticsearch instance.
googleCloudLogging:: Forwards logs to {gcp-full} Logging.
http:: Forwards logs to a generic HTTP endpoint.
kafka:: Forwards logs to a Kafka broker.
loki:: Forwards logs to a Loki logging backend.
lokistack:: Forwards logs to the logging supported combination of Loki and web proxy with {Product-Title} authentication integration. LokiStack's proxy uses {Product-Title} authentication to enforce multi-tenancy
otlp:: Forwards logs using the OpenTelemetry Protocol.
splunk:: Forwards logs to Splunk.
syslog:: Forwards logs to an external syslog server.

Each output type has its own configuration fields.

// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-configuring-otlp-output_{context}"]
= Configuring OTLP output

Cluster administrators can use the OpenTelemetry Protocol (OTLP) output to collect and forward logs to OTLP receivers. The OTLP output uses the specification defined by the https://opentelemetry.io/docs/specs/otlp/[OpenTelemetry Observability framework] to send data over HTTP with JSON encoding.

.Procedure

* Create or edit a `ClusterLogForwarder` custom resource (CR) to enable forwarding using OTLP by adding the following annotation:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  annotations:
    observability.openshift.io/tech-preview-otlp-output: "enabled" # <1>
  name: clf-otlp
spec:
  serviceAccount:
    name: <service_account_name>
  outputs:
  - name: otlp
    type: otlp
    otlp:
      tuning:
        compression: gzip
        deliveryMode: AtLeastOnce
        maxRetryDuration: 20
        maxWrite: 10M
        minRetryDuration: 5
      url: <otlp_url> # <2>
  pipelines:
  - inputRefs:
    - application
    - infrastructure
    - audit
    name: otlp-logs
    outputRefs:
    - otlp
----
<1> Use this annotation to enable the OpenTelemetry Protocol (OTLP) output, which is a Technology Preview feature.
<2> This URL must be absolute and is a placeholder for the OTLP endpoint where logs are sent.

[NOTE]
====
The OTLP output uses the OpenTelemetry data model, which is different from the ViaQ data model that is used by other output types. It adheres to the OTLP using https://opentelemetry.io/docs/specs/semconv/[OpenTelemetry Semantic Conventions] defined by the OpenTelemetry Observability framework.
====

[id="clf-pipelines_6-2_{context}"]
=== Pipelines

Pipelines are configured in an array under `spec.pipelines`. Each pipeline must have a unique name and consists of:

inputRefs:: Names of inputs whose logs should be forwarded to this pipeline.
outputRefs:: Names of outputs to send logs to.
filterRefs:: (optional) Names of filters to apply.

The order of filterRefs matters, as they are applied sequentially. Earlier filters can drop messages that will not be processed by later filters.

[id="clf-filters_6-2_{context}"]
=== Filters

Filters are configured in an array under `spec.filters`. They can match incoming log messages based on the value of structured fields and modify or drop them.

Administrators can configure the following types of filters:

// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-multiline-except_{context}"]
= Enabling multi-line exception detection

Enables multi-line error detection of container logs.

[WARNING]
====
Enabling this feature could have performance implications and may require additional computing resources or alternate logging solutions.
====

Log parsers often incorrectly identify separate lines of the same exception as separate exceptions. This leads to extra log entries and an incomplete or inaccurate view of the traced information.

.Example java exception
[source,java]
----
java.lang.NullPointerException: Cannot invoke "String.toString()" because "<param1>" is null
    at testjava.Main.handle(Main.java:47)
    at testjava.Main.printMe(Main.java:19)
    at testjava.Main.main(Main.java:10)
----

* To enable logging to detect multi-line exceptions and reassemble them into a single log entry, ensure that the `ClusterLogForwarder` Custom Resource (CR) contains a `detectMultilineErrors` field under the `.spec.filters`.

.Example ClusterLogForwarder CR
[source,yaml]
----
apiVersion: "observability.openshift.io/v1"
kind: ClusterLogForwarder
metadata:
  name: <log_forwarder_name>
  namespace: <log_forwarder_namespace>
spec:
  serviceAccount:
    name: <service_account_name>
  filters:
  - name: <name>
    type: detectMultilineException
  pipelines:
    - inputRefs:
        - <input-name>
      name: <pipeline-name>
      filterRefs:
        - <filter-name>
      outputRefs:
        - <output-name>
----

== Details
When log messages appear as a consecutive sequence forming an exception stack trace, they are combined into a single, unified log record. The first log message's content is replaced with the concatenated content of all the message fields in the sequence.

The collector supports the following languages:

* Java
* JS
* Ruby
* Python
* Golang
* PHP
* Dart
// Module included in the following assemblies:
//
// * observability/logging/logging-6.2/log6x-clf-6.2.adoc

[id="logging-http-forward-6-2_{context}"]
= Forwarding logs over HTTP

To enable forwarding logs over HTTP, specify `http` as the output type in the `ClusterLogForwarder` custom resource (CR).

.Procedure

* Create or edit the `ClusterLogForwarder` CR using the template below:
+
.Example ClusterLogForwarder CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: <log_forwarder_name>
  namespace: <log_forwarder_namespace>
spec:
  managementState: Managed
  outputs:
  - name: <output_name>
    type: http
    http:
      headers:  # <1>
          h1: v1
          h2: v2
      authentication:
        username:
          key: username
          secretName: <http_auth_secret>
        password:
          key: password
          secretName: <http_auth_secret>
      timeout: 300
      proxyURL: <proxy_url> # <2>
      url: <url> # <3>
    tls:
      insecureSkipVerify: # <4>
      ca:
        key: <ca_certificate>
        secretName: <secret_name> # <5>
  pipelines:
    - inputRefs:
        - application
      name: pipe1
      outputRefs:
        - <output_name>  # <6>
  serviceAccount:
    name: <service_account_name> # <7>
----
<1> Additional headers to send with the log record.
<2> Optional: URL of the HTTP/HTTPS proxy that should be used to forward logs over http or https from this output. This setting overrides any default proxy settings for the cluster or the node.
<3> Destination address for logs.
<4> Values are either `true` or `false`.
<5> Secret name for destination credentials.
<6> This value should be the same as the output name.
<7> The name of your service account.
// Module included in the following assemblies:
//
// * observability/logging/logging-6.2/log6x-clf-6.2.adoc

[id="cluster-logging-collector-log-forward-syslog-6x_{context}"]
= Forwarding logs using the syslog protocol

You can use the syslog RFC3164 or RFC5424 protocol to send a copy of your logs to an external log aggregator that is configured to accept the protocol instead of, or in addition to, the default Elasticsearch log store. You are responsible for configuring the external log aggregator, such as a syslog server, to receive the logs from OpenShift Container Platform.

To configure log forwarding using the syslog protocol, you must create a `ClusterLogForwarder` custom resource (CR) with one or more outputs to the syslog servers, and pipelines that use those outputs. The syslog output can use a UDP, TCP, or TLS connection.

.Prerequisites

* You must have a logging server that is configured to receive the logging data using the specified protocol or format.

.Procedure

. Create or edit a YAML file that defines the `ClusterLogForwarder` CR object:
+
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: collector
spec:
  managementState: Managed
  outputs:
  - name: rsyslog-east # <1>
    syslog:
      appName: <app_name> # <2>
      enrichment: KubernetesMinimal
      facility: <facility_value> # <3>
      msgId: <message_ID> # <4>
      payloadKey: <record_field> # <5>
      procId: <process_ID> # <6>
      rfc: <RFC3164_or_RFC5424> # <7>
      severity: informational # <8>
      tuning:
        deliveryMode: <AtLeastOnce_or_AtMostOnce> # <9>
      url: <url> # <10>
    tls: # <11>
      ca:
        key: ca-bundle.crt
        secretName: syslog-secret
    type: syslog
  pipelines:
  - inputRefs: # <12>
    - application
    name: syslog-east # <13>
    outputRefs:
    - rsyslog-east
  serviceAccount: # <14>
    name: logcollector
----
<1> Specify a name for the output.
<2> Optional: Specify the value for the `APP-NAME` part of the syslog message header. The value must conform with The Syslog Protocol. The value can be a combination of static and dynamic values consisting of field paths followed by `||`, and then followed by another field path or a static value. The maximum length of the final values is truncated to 48 characters. You must encase a dynamic value curly brackets and the value must be followed with a static fallback value separated with `||`. Static values can only contain alphanumeric characters along with dashes, underscores, dots and forward slashes. Example value: <value1>-{.<value2>||"none"}.
<3> Optional: Specify the value for `Facility` part of the syslog-msg header.
<4> Optional: Specify the value for `MSGID` part of the syslog-msg header. The value can be a combination of static and dynamic values consisting of field paths followed by `||`, and then followed by another field path or a static value. The maximum length of the final values is truncated to 32 characters. You must encase a dynamic value curly brackets and the value must be followed with a static fallback value separated with `||`. Static values can only contain alphanumeric characters along with dashes, underscores, dots and forward slashes. Example value: <value1>-{.<value2>||"none"}.
<5> Optional: Specify the record field to use as the payload. The `payloadKey` value must be a single field path encased in single curly brackets `{}`. Example: {.<value>}.
<6> Optional: Specify the value for the `PROCID` part of the syslog message header. The value must conform with The Syslog Protocol. The value can be a combination of static and dynamic values consisting of field paths followed by `||`, and then followed by another field path or a static value. The maximum length of the final values is truncated to 48 characters. You must encase a dynamic value curly brackets and the value must be followed with a static fallback value separated with `||`. Static values can only contain alphanumeric characters along with dashes, underscores, dots and forward slashes. Example value: <value1>-{.<value2>||"none"}.
<7> Optional: Set the RFC that the generated messages conform to. The value can be `RFC3164` or `RFC5424`.
<8> Optional: Set the severity level for the message. For more information, see The Syslog Protocol.
<9> Optional: Set the delivery mode for log forwarding. The value can be either `AtLeastOnce`, or `AtMostOnce`.
<10> Specify the absolute URL with a scheme. Valid schemes are: `tcp`, `tls`, and `udp`. For example: `tls://syslog-receiver.example.com:6514`.
<11> Specify the settings for controlling options of the transport layer security (TLS) client connections.
<12> Specify which log types to forward by using the pipeline: `application,` `infrastructure`, or `audit`.
<13> Specify a name for the pipeline.
<14> The name of your service account.

. Create the CR object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

[id="cluster-logging-collector-log-forward-examples-syslog-log-source_{context}"]
== Adding log source information to the message output

You can add `namespace_name`, `pod_name`, and `container_name` elements to the `message` field of the record by adding the `enrichment` field to your `ClusterLogForwarder` custom resource (CR).

[source,yaml]
----
# ...
  spec:
    outputs:
    - name: syslogout
      syslog:
        enrichment: KubernetesMinimal
        facility: user
        payloadKey: message
        rfc: RFC3164
        severity: debug
      type: syslog
      url: tls://syslog-receiver.example.com:6514
    pipelines:
    - inputRefs:
      - application
      name: test-app
      outputRefs:
      - syslogout
# ...
----

[NOTE]
====
This configuration is compatible with both RFC3164 and RFC5424.
====

.Example syslog message output with `enrichment: None`
[source, text]
----
 2025-03-03T11:48:01+00:00  example-worker-x  syslogsyslogserverd846bb9b: {...}
----

.Example syslog message output with `enrichment: KubernetesMinimal`

[source, text]
----
2025-03-03T11:48:01+00:00  example-worker-x  syslogsyslogserverd846bb9b: namespace_name=cakephp-project container_name=mysql pod_name=mysql-1-wr96h,message: {...}
----
// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-content-filter-drop-records_{context}"]
= Configuring content filters to drop unwanted log records

When the `drop` filter is configured, the log collector evaluates log streams according to the filters before forwarding. The collector drops unwanted log records that match the specified configuration.

.Procedure

. Add a configuration for a filter to the `filters` spec in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to drop log records based on regular expressions:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  filters:
  - name: <filter_name>
    type: drop # <1>
    drop: # <2>
    - test: # <3>
      - field: .kubernetes.labels."foo-bar/baz" # <4>
        matches: .+ # <5>
      - field: .kubernetes.pod_name
        notMatches: "my-pod" # <6>
  pipelines:
  - name: <pipeline_name> # <7>
    filterRefs: ["<filter_name>"]
# ...
----
<1> Specifies the type of filter. The `drop` filter drops log records that match the filter configuration.
<2> Specifies configuration options for applying the `drop` filter.
<3> Specifies the configuration for tests that are used to evaluate whether a log record is dropped.
** If all the conditions specified for a test are true, the test passes and the log record is dropped.
** When multiple tests are specified for the `drop` filter configuration, if any of the tests pass, the record is dropped.
** If there is an error evaluating a condition, for example, the field is missing from the log record being evaluated, that condition evaluates to false.
<4> Specifies a dot-delimited field path, which is a path to a field in the log record. The path can contain alpha-numeric characters and underscores (`a-zA-Z0-9_`), for example, `.kubernetes.namespace_name`. If segments contain characters outside of this range, the segment must be in quotes, for example, `.kubernetes.labels."foo.bar-bar/baz"`. You can include multiple field paths in a single `test` configuration, but they must all evaluate to true for the test to pass and the `drop` filter to be applied.
<5> Specifies a regular expression. If log records match this regular expression, they are dropped. You can set either the `matches` or `notMatches` condition for a single `field` path, but not both.
<6> Specifies a regular expression. If log records do not match this regular expression, they are dropped. You can set either the `matches` or `notMatches` condition for a single `field` path, but not both.
<7> Specifies the pipeline that the `drop` filter is applied to.

. Apply the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----

.Additional examples

The following additional example shows how you can configure the `drop` filter to only keep higher priority log records:

[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  filters:
  - name: important
    type: drop
    drop:
    - test:
      - field: .message
        notMatches: "(?i)critical|error"
      - field: .level
        matches: "info|warning"
# ...
----

In addition to including multiple field paths in a single `test` configuration, you can also include additional tests that are treated as _OR_ checks. In the following example, records are dropped if either `test` configuration evaluates to true. However, for the second `test` configuration, both field specs must be true for it to be evaluated to true:

[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  filters:
  - name: important
    type: drop
    drop:
    - test:
      - field: .kubernetes.namespace_name
        matches: "^open"
    - test:
      - field: .log_type
        matches: "application"
      - field: .kubernetes.pod_name
        notMatches: "my-pod"
# ...
----
// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-audit-filtering_{context}"]
= Overview of API audit filter
OpenShift API servers generate audit events for each API call, detailing the request, response, and the identity of the requester, leading to large volumes of data. The API Audit filter uses rules to enable the exclusion of non-essential events and the reduction of event size, facilitating a more manageable audit trail. Rules are checked in order, and checking stops at the first match. The amount of data that is included in an event is determined by the value of the `level` field:

* `None`: The event is dropped.
* `Metadata`: Audit metadata is included, request and response bodies are removed.
* `Request`: Audit metadata and the request body are included, the response body is removed.
* `RequestResponse`: All data is included: metadata, request body and response body. The response body can be very large. For example, `oc get pods -A` generates a response body containing the YAML description of every pod in the cluster.

The `ClusterLogForwarder` custom resource (CR) uses the same format as the standard Kubernetes audit policy, while providing the following additional functions:

Wildcards:: Names of users, groups, namespaces, and resources can have a leading or trailing `\*` asterisk character. For example, the namespace `openshift-\*` matches `openshift-apiserver` or `openshift-authentication`. Resource `\*/status` matches `Pod/status` or `Deployment/status`.

Default Rules:: Events that do not match any rule in the policy are filtered as follows:
* Read-only system events such as `get`, `list`, and `watch` are dropped.
* Service account write events that occur within the same namespace as the service account are dropped.
* All other events are forwarded, subject to any configured rate limits.

To disable these defaults, either end your rules list with a rule that has only a `level` field or add an empty rule.

Omit Response Codes:: A list of integer status codes to omit. You can drop events based on the HTTP status code in the response by using the `OmitResponseCodes` field, which lists HTTP status codes for which no events are created. The default value is `[404, 409, 422, 429]`. If the value is an empty list, `[]`, then no status codes are omitted.

The `ClusterLogForwarder` CR audit policy acts in addition to the OpenShift Container Platform audit policy. The `ClusterLogForwarder` CR audit filter changes what the log collector forwards and provides the ability to filter by verb, user, group, namespace, or resource. You can create multiple filters to send different summaries of the same audit stream to different places. For example, you can send a detailed stream to the local cluster log store and a less detailed stream to a remote site.

[NOTE]
====
You must have a cluster role `collect-audit-logs` to collect the audit logs. The following example provided is intended to illustrate the range of rules possible in an audit policy and is not a recommended configuration.
====

.Example audit policy
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: <log_forwarder_name>
  namespace: <log_forwarder_namespace>
spec:
  serviceAccount:
    name: <service_account_name>
  pipelines:
    - name: my-pipeline
      inputRefs: audit # <1>
      filterRefs: my-policy # <2>
  filters:
    - name: my-policy
      type: kubeAPIAudit
      kubeAPIAudit:
        # Don't generate audit events for all requests in RequestReceived stage.
        omitStages:
          - "RequestReceived"

        rules:
          # Log pod changes at RequestResponse level
          - level: RequestResponse
            resources:
            - group: ""
              resources: ["pods"]

          # Log "pods/log", "pods/status" at Metadata level
          - level: Metadata
            resources:
            - group: ""
              resources: ["pods/log", "pods/status"]

          # Don't log requests to a configmap called "controller-leader"
          - level: None
            resources:
            - group: ""
              resources: ["configmaps"]
              resourceNames: ["controller-leader"]

          # Don't log watch requests by the "system:kube-proxy" on endpoints or services
          - level: None
            users: ["system:kube-proxy"]
            verbs: ["watch"]
            resources:
            - group: "" # core API group
              resources: ["endpoints", "services"]

          # Don't log authenticated requests to certain non-resource URL paths.
          - level: None
            userGroups: ["system:authenticated"]
            nonResourceURLs:
            - "/api*" # Wildcard matching.
            - "/version"

          # Log the request body of configmap changes in kube-system.
          - level: Request
            resources:
            - group: "" # core API group
              resources: ["configmaps"]
            # This rule only applies to resources in the "kube-system" namespace.
            # The empty string "" can be used to select non-namespaced resources.
            namespaces: ["kube-system"]

          # Log configmap and secret changes in all other namespaces at the Metadata level.
          - level: Metadata
            resources:
            - group: "" # core API group
              resources: ["secrets", "configmaps"]

          # Log all other resources in core and extensions at the Request level.
          - level: Request
            resources:
            - group: "" # core API group
            - group: "extensions" # Version of group should NOT be included.

          # A catch-all rule to log all other requests at the Metadata level.
          - level: Metadata
----
<1> The log types that are collected. The value for this field can be `audit` for audit logs, `application` for application logs, `infrastructure` for infrastructure logs, or a named input that has been defined for your application.
<2> The name of your audit policy.
// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-input-spec-filter-labels-expressions_{context}"]
= Filtering application logs at input by including the label expressions or a matching label key and values

You can include the application logs based on the label expressions or a matching label key and its values by using the `input` selector.

.Procedure

. Add a configuration for a filter to the `input` spec in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to include logs based on label expressions or matched label key/values:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  inputs:
    - name: mylogs
      application:
        selector:
          matchExpressions:
          - key: env # <1>
            operator: In # <2>
            values: ["prod", "qa"] # <3>
          - key: zone
            operator: NotIn
            values: ["east", "west"]
          matchLabels: # <4>
            app: one
            name: app1
      type: application
# ...
----
<1> Specifies the label key to match.
<2> Specifies the operator. Valid values include: `In`, `NotIn`, `Exists`, and `DoesNotExist`.
<3> Specifies an array of string values. If the `operator` value is either `Exists` or `DoesNotExist`, the value array must be empty.
<4> Specifies an exact key or value mapping.

. Apply the `ClusterLogForwarder` CR by running the following command:

+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-content-filter-prune-records_{context}"]
= Configuring content filters to prune log records

When the `prune` filter is configured, the log collector evaluates log streams according to the filters before forwarding. The collector prunes log records by removing low value fields such as pod annotations.

.Procedure

. Add a configuration for a filter to the `prune` spec in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to prune log records based on field paths:
+
[IMPORTANT]
====
If both are specified, records are pruned based on the `notIn` array first, which takes precedence over the `in` array. After records have been pruned by using the `notIn` array, they are then pruned by using the `in` array.
====
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
metadata:
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  filters:
  - name: <filter_name>
    type: prune # <1>
    prune: # <2>
      in: [.kubernetes.annotations, .kubernetes.namespace_id] # <3>
      notIn: [.kubernetes,.log_type,.message,."@timestamp"] # <4>
  pipelines:
  - name: <pipeline_name> # <5>
    filterRefs: ["<filter_name>"]
# ...
----
<1> Specify the type of filter. The `prune` filter prunes log records by configured fields.
<2> Specify configuration options for applying the `prune` filter. The `in` and `notIn` fields are specified as arrays of dot-delimited field paths, which are paths to fields in log records. These paths can contain alpha-numeric characters and underscores (`a-zA-Z0-9_`), for example, `.kubernetes.namespace_name`. If segments contain characters outside of this range, the segment must be in quotes, for example, `.kubernetes.labels."foo.bar-bar/baz"`.
<3> Optional: Any fields that are specified in this array are removed from the log record.
<4> Optional: Any fields that are not specified in this array are removed from the log record.
<5> Specify the pipeline that the `prune` filter is applied to.
+
[NOTE]
====
The filters exempts the `log_type`, `.log_source`, and `.message` fields.
====

. Apply the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-input-spec-filter-audit-infrastructure_{context}"]
= Filtering the audit and infrastructure log inputs by source

You can define the list of `audit` and `infrastructure` sources to collect the logs by using the `input` selector.

.Procedure

. Add a configuration to define the `audit` and `infrastructure` sources in the `ClusterLogForwarder` CR.

+
The following example shows how to configure the `ClusterLogForwarder` CR to define `audit` and `infrastructure` sources:
+
.Example `ClusterLogForwarder` CR
+
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  inputs:
    - name: mylogs1
      type: infrastructure
      infrastructure:
        sources: # <1>
          - node
    - name: mylogs2
      type: audit
      audit:
        sources: # <2>
          - kubeAPI
          - openshiftAPI
          - ovn
# ...
----
<1> Specifies the list of infrastructure sources to collect. The valid sources include:
** `node`: Journal log from the node
** `container`: Logs from the workloads deployed in the namespaces
<2> Specifies the list of audit sources to collect. The valid sources include:
** `kubeAPI`: Logs from the Kubernetes API servers
** `openshiftAPI`: Logs from the OpenShift API servers
** `auditd`: Logs from a node auditd service
** `ovn`: Logs from an open virtual network service

. Apply the `ClusterLogForwarder` CR by running the following command:

+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-clf.adoc

[id="log6x-input-spec-filter-namespace-container_{context}"]
= Filtering application logs at input by including or excluding the namespace or container name

You can include or exclude the application logs based on the namespace and container name by using the `input` selector.

.Procedure

. Add a configuration to include or exclude the namespace and container names in the `ClusterLogForwarder` CR.
+
The following example shows how to configure the `ClusterLogForwarder` CR to include or exclude namespaces and container names:
+
.Example `ClusterLogForwarder` CR
[source,yaml]
----
apiVersion: observability.openshift.io/v1
kind: ClusterLogForwarder
# ...
spec:
  serviceAccount:
    name: <service_account_name>
  inputs:
    - name: mylogs
      application:
        includes:
          - namespace: "my-project" # <1>
            container: "my-container" # <2>
        excludes:
          - container: "other-container*" # <3>
            namespace: "other-namespace" # <4>
      type: application
# ...
----
<1> Specifies that the logs are only collected from these namespaces.
<2> Specifies that the logs are only collected from these containers.
<3> Specifies the pattern of namespaces to ignore when collecting the logs.
<4> Specifies the set of containers to ignore when collecting the logs.
+
[NOTE]
====
The `excludes` field takes precedence over the `includes` field.
====
+
. Apply the `ClusterLogForwarder` CR by running the following command:
+
[source,terminal]
----
$ oc apply -f <filename>.yaml
----
