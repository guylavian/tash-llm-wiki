---
title: "Network observability DNS resolution analysis"
type: reference
domain: openshift
slug: observability-4-22-network-observability-dns-resolution-analysis
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/network-observability-dns-resolution-analysis
version: 4.22
family: observability
documentKind: "Documentation"
---

# Network observability DNS resolution analysis

[id="network-observability-dns-resolution-analysis_{context}"]
= Network observability DNS resolution analysis

[role="_abstract"]
Learn how DNS resolution analysis uses eBPF-based decoding to identify service discovery issues and follow the steps to enable DNS tracking in the FlowCollector resource to enrich network flow records with domain names.

// Module included in the following assemblies:
//
// * network_observability/network-observability-dns-decoding.adoc

[id="network-observability-dns-resolution-analysis-strategic-benefits_{context}"]
= Strategic benefits of DNS resolution analysis

[role="_abstract"]
Use DNS resolution analysis to differentiate between network transport failures and service discovery issues by enriching eBPF flow records with domain names and status codes.

Standard flow logs only show that traffic occurred on port 53. DNS resolution analysis allows you to complete the following tasks:

* Reduced Mean time to identify (Mtti): Distinguish immediately between a network routing failure and a DNS resolution failure, such as an `NXDOMAIN` error.
* Measure internal service latency: Track the time it takes for CoreDNS to respond to specific internal lookups (e.g., `my-service.namespace.svc.cluster.local`).
* Audit external dependencies: Audit which external APIs or third-party domains your workloads are communicating with without requiring sidecars or manual packet captures.
* Improved security posture: Detect potential data exfiltration or Command and Control (C2) activity by auditing the Fully Qualified Domain Names (FQDNs) queried by internal workloads.

[id="dns-flow-enrichment_{context}"]
== DNS flow enrichment
When this feature is active, the eBPF agent enriches the flow records. This metadata allows you to group and filter traffic by the intent of the connection (the domain) rather than just the source IP.

Enhanced DNS decoding allows the eBPF agent to inspect UDP and TCP DNS traffic on port 53 along with the query names for the DNS request.

// Module included in the following assemblies:
//
// * network_observability/network-observability-dns-decoding.adoc

[id="network-observability-dns-resolution-analysis-configure_{context}"]
= Configure DNS domain tracking for network observability

[role="_abstract"]
Enable DNS tracking in the Network Observability Operator to monitor DNS query names, response codes, and latency for network flows within the cluster.

.Prerequisites

* The Network Observability Operator is installed.
* You have `cluster-admin` privileges.
* You are familiar with the `FlowCollector` custom resource.

.Procedure

. Edit the `FlowCollector` resource by running the following command:
+
[source,terminal]
----
$ oc edit flowcollector cluster
----

. Configure the eBPF agent to enable the DNS tracking feature:
+
[source,yaml]
----
apiVersion: flows.netobserv.io/v1alpha1
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    type: eBPF
    ebpf:
      features:
        - DNSTracking
----
+
where:

`spec.agent.type.ebpf.features`:: Specifies the list of features to enable for the eBPF agent. To enable DNS tracking, add `DNSTracking` to this list.

. Save and exit the editor.

.Verification
. In the OpenShift Container Platform web console, navigate to *Observe* -> *Network Traffic*.
. In the *Traffic Flows* view, click the *Manage columns* icon.
. Ensure that the *DNS Query Name*, *DNS Response Code*, and *DNS Latency* columns are selected.
. Filter the results by setting *Port* to `53`.
. Confirm that the flow table columns are populated with domain names and DNS metadata.

// Module included in the following assemblies:
//
// * network_observability/network-observability-dns-decoding.adoc

[id="network-observability-dns-resolution-analysis-reference_{context}"]
= DNS flow enrichment and analysis reference

[role="_abstract"]
Identify metadata added to network flows, leverage DNS data for network optimization, and understand the performance and storage impacts on the cluster.

The following table describes the metadata fields added to network flows when DNS tracking is enabled.

[NOTE]
====
Query names might be missing or truncated because of compression pointers or cache limitations.
====

.DNS flow metadata
[cols="1,2,1",options="header"]
|===
|Field |Description |Example
|`dns_query_name` |The Fully Qualified Domain Name (FQDN) being queried. |`example.com`
|`dns_response_code` |The status code returned by the DNS server. |`NoError`, `NXDomain`
|`dns_id` |The transaction ID used to match queries with responses. |`45213`
|===

[id="leverage-dns-data-optimization_{context}"]
== Leverage DNS data for network optimization
Use the captured DNS metadata for the following operational outcomes:

* Audit external dependencies: Ensure workloads are not reaching out to unauthorized external APIs or high-risk domains.
* Performance tuning: Monitor `DNS Latency` to identify if `CoreDNS` pods require additional scaling or if upstream DNS providers are lagging.

[id="identify-misconfiguration-errors_{context}"]
== Identify misconfiguration errors
A high frequency of `NXDOMAIN` responses typically indicates service discovery errors in application code or stale environment variables.

`NXDOMAIN` errors can be frequent in Kubernetes because of DNS searches on services and pods. While these results do not necessarily indicate a misconfiguration or broken URL, they can negatively impact performance.

When `NXDOMAIN` errors are returned despite an apparently valid Service or Pod host name, such as `my-svc.my-namespace.svc`, the resolver is likely configured to query DNS for different suffixes. You can optimize this by adding a trailing dot to fully qualified domain names to tell the resolver that the name is unambiguous.

For example, instead of `https://my-svc.my-namespace.svc`, use `https://my-svc.my-namespace.svc.cluster.local.` with a trailing dot.

[id="loki-storage-considerations_{context}"]
== Loki storage considerations

DNS tracking increases the number of labels and the amount of metadata per flow. Ensure that the Loki storage is sized to accommodate the increased log volume.

[role="_additional-resources"]
.Additional resources
* Network flows format reference
* Network Observability Operator runbooks
