---
title: "OTLP data ingestion in Loki"
type: reference
domain: openshift
slug: observability-4-22-log6x-configuring-lokistack-otlp-6-2
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/log6x-configuring-lokistack-otlp-6.2
version: 4.22
family: observability
documentKind: "Documentation"
---

# OTLP data ingestion in Loki

[id="log6x-configuring-lokistack-otlp-6-2"]
= OTLP data ingestion in Loki

You can use an API endpoint by using the OpenTelemetry Protocol (OTLP) with Logging. As OTLP is a standardized format not specifically designed for Loki, OTLP requires an additional Loki configuration to map data format of OpenTelemetry to data model of Loki. OTLP lacks concepts such as _stream labels_ or _structured metadata_. Instead, OTLP provides metadata about log entries as *attributes*, grouped into the following three categories:

* Resource
* Scope
* Log

You can set metadata for multiple entries simultaneously or individually as needed.

// Module included in the following assemblies:
//
// * observability/logging/logging-6.0/log6x-configuring-lokistack-otlp.adoc

[id="log6x-configuring-lokistack-otlp-data-ingestion_{context}"]
= Configuring LokiStack for OTLP data ingestion

To configure a `LokiStack` custom resource (CR) for OTLP ingestion, follow these steps:

.Prerequisites

* Ensure that your Loki setup supports structured metadata, introduced in schema version 13 to enable OTLP log ingestion.

.Procedure

. Set the schema version:
+
** When creating a new `LokiStack` CR, set `version: v13` in the storage schema configuration.
+
[NOTE]
====
For existing configurations, add a new schema entry with `version: v13` and an `effectiveDate` in the future. For more information on updating schema versions, see Upgrading Schemas (Grafana documentation).
====

. Configure the storage schema as follows:
+
.Example configure storage schema
[source,yaml]
----
# ...
spec:
  storage:
    schemas:
    - version: v13
      effectiveDate: 2024-10-25
----
+
Once the `effectiveDate` has passed, the v13 schema takes effect, enabling your `LokiStack` to store structured metadata.

[id="attribute-mapping_{context}"]
== Attribute mapping

When you set the {loki-op} to the `openshift-logging` mode, {loki-op} automatically applies a default set of attribute mappings. These mappings align specific OTLP attributes with stream labels and structured metadata of Loki.

For typical setups, these default mappings are sufficient. However, you might need to customize attribute mapping in the following cases:

* Using a custom collector: If your setup includes a custom collector that generates additional attributes that you do not want to store, consider customizing the mapping to ensure these attributes are dropped by Loki.
* Adjusting attribute detail levels: If the default attribute set is more detailed than necessary, you can reduce it to essential attributes only. This can avoid excessive data storage and streamline the {logging} process.

[id="custom-attribute-mapping-for-openshift_{context}"]
=== Custom attribute mapping for OpenShift

When using the {loki-op} in `openshift-logging` mode, attribute mapping follow OpenShift default values, but you can configure custom mappings to adjust default values.
In the `openshift-logging` mode, you can configure custom attribute mappings globally for all tenants or for individual tenants as needed. When you define custom mappings, they are appended to the OpenShift default values. If you do not need default labels, you can disable them in the tenant configuration.

[NOTE]
====
A major difference between the {loki-op} and Loki lies in inheritance handling. Loki copies only `default_resource_attributes_as_index_labels` to tenants by default, while the {loki-op} applies the entire global configuration to each tenant in the `openshift-logging` mode.
====

Within `LokiStack`, attribute mapping configuration is managed through the `limits` setting. See the following example `LokiStack` configuration:

[source,yaml]
----
# ...
spec:
  limits:
    global:
      otlp: {} # <1>
    tenants:
      application: # <2>
        otlp: {}
----
<1> Defines global OTLP attribute configuration.
<2> Defines the OTLP attribute configuration for the `application` tenant within the `openshift-logging` mode. You can also configure `infrastructure` and `audit` tenants in addition to `application` tenants.

[NOTE]
====
You can use both global and per-tenant OTLP configurations for mapping attributes to stream labels.
====

Stream labels derive only from resource-level attributes, which the `LokiStack` resource structure reflects. See the following `LokiStack` example configuration:

[source,yaml]
----
spec:
  limits:
    global:
      otlp:
        streamLabels:
          resourceAttributes:
          - name: "k8s.namespace.name"
          - name: "k8s.pod.name"
          - name: "k8s.container.name"
----

You can drop attributes of type resource, scope, or log from the log entry.

[source,yaml]
----
# ...
spec:
  limits:
    global:
      otlp:
        streamLabels:
# ...
        drop:
          resourceAttributes:
          - name: "process.command_line"
          - name: "k8s\\.pod\\.labels\\..+"
            regex: true
          scopeAttributes:
          - name: "service.name"
          logAttributes:
          - name: "http.route"
----

You can use regular expressions by setting `regex: true` to apply a configuration for attributes with similar names.

[IMPORTANT]
====
Avoid using regular expressions for stream labels, as this can increase data volume.
====

Attributes that are not explicitly set as stream labels or dropped from the entry are saved as structured metadata by default.

[id="customizing-openshift-defaults_{context}"]
=== Customizing OpenShift defaults

In the `openshift-logging` mode, certain attributes are required and cannot be removed from the configuration due to their role in OpenShift functions. Other attributes, labeled *recommended*, might be dropped if performance is impacted. For information about the attributes, see OpenTelemetry data model attributes.

When using the `openshift-logging` mode without custom attributes, you can achieve immediate compatibility with OpenShift tools. If additional attributes are needed as stream labels or some attributes need to be droped, use custom configuration. Custom configurations can merge with default configurations.

[id="removing-recommended-attributes_{context}"]
=== Removing recommended attributes

To reduce default attributes in the `openshift-logging` mode, disable recommended attributes:

[source,yaml]
----
# ...
spec:
  tenants:
    mode: openshift-logging
    openshift:
      otlp:
        disableRecommendedAttributes: true # <1>
----
<1> Set `disableRecommendedAttributes: true` to remove recommended attributes, which limits default attributes to the required attributes or stream labels.
+
[NOTE]
====
This setting might negatively impact query performance, as it removes default stream labels. You must pair this option with a custom attribute configuration to retain attributes essential for queries.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources
* Loki labels (Grafana documentation)
* Structured metadata (Grafana documentation)
* OpenTelemetry data model
* OpenTelemetry attribute (OpenTelemetry documentation)
