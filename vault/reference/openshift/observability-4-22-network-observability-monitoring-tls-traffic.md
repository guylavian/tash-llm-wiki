---
title: "Monitoring Transport Layer Security traffic"
type: reference
domain: openshift
slug: observability-4-22-network-observability-monitoring-tls-traffic
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/network-observability-monitoring-tls-traffic
version: 4.22
family: observability
documentKind: "Documentation"
---

# Monitoring Transport Layer Security traffic

[id="network-observability-monitoring-tls-traffic"]
= Monitoring Transport Layer Security traffic

[role="_abstract"]
[role="_abstract"]
Monitor TLS traffic to identify insecure protocols, detect security risks, and maintain compliance without decrypting traffic.

// Module included in the following assemblies:
//
// * observability/network_observability/network-observability-monitoring-tls-traffic.adoc

[id="network-observability-tls-monitoring-overview_{context}"]
= Transport Layer Security traffic monitoring

[role="_abstract"]
Transport Layer Security (TLS) traffic monitoring identifies security risks and maintains compliance by analyzing encrypted traffic metadata without decryption.

As a network administrator or security practitioner, you must verify that encrypted traffic uses secure protocols and cipher suites. Monitoring TLS usage identifies security risks, such as workloads that use deprecated TLS versions, and helps maintain compliance with cluster security policies.

[id="tls-monitoring-security-benefits_{context}"]
== Security improvements through metadata analysis

The Network Observability Operator captures TLS metadata from handshake messages without decrypting traffic, providing visibility into encryption protocols while maintaining data privacy. This approach enables the following improvements:

Security risk detection:: Identifies workloads using deprecated TLS versions (1.0, 1.1) or weak cipher suites by capturing TLS version, cipher suite, and group information. You can configure Prometheus alerts to automatically report deprecated TLS configurations.

Compliance auditing:: Audits TLS configurations to meet regulatory requirements through metric aggregation in dashboard charts and overview panels. You can filter flows by TLS fields to isolate specific protocol versions or cipher suites for compliance reporting.

Security posture assessment:: Visualizes encrypted network traffic with lock icons in the topology view and identifies unencrypted communications across your cluster. You can analyze TLS usage patterns to evaluate your overall security posture.

Remediation prioritization:: Targets workloads using deprecated protocols for updates by filtering and analyzing TLS fields to isolate problematic connections requiring immediate attention.

[id="monitoring-tls-traffic-workflow_{context}"]
== TLS traffic monitoring workflow phases

To monitor TLS traffic effectively, complete the following phases:

* Enable the TLS tracking feature in the eBPF agent configuration.
* Analyze TLS traffic details in the *Network Traffic* view.
* Visualize secure connections in the *Topology* view.

// Module included in the following assemblies:
//
// * observability/network_observability/network-observability-monitoring-tls-traffic.adoc

[id="network-observability-enable-tls-tracking_{context}"]
= Enable Transport Layer Security tracking

[role="_abstract"]
Enable Transport Layer Security (TLS) tracking to monitor encryption protocols and identify security risks in the cluster.

[NOTE]
====
TLS fields only appear in flows for connections that perform a TLS handshake after the feature is enabled.
====

.Prerequisites

* The Network Observability Operator is installed.
* The `FlowCollector` custom resource (CR) is configured with `spec.agent.type: eBPF`.
* Access to the cluster with `cluster-admin` privileges.

.Procedure

. Edit the `FlowCollector` CR by running the following command:
+
[source,terminal]
----
$ oc edit flowcollector cluster
----

. Add `TLSTracking` to the `spec.agent.ebpf.features` list:
+
[source,yaml]
----
apiVersion: flows.netobserv.io/v1beta2
kind: FlowCollector
metadata:
  name: cluster
spec:
  agent:
    type: eBPF
    ebpf:
      features:
      - TLSTracking
# ...
----
+
where:
+
`spec.agent.ebpf.features`:: Specifies the list of eBPF agent features to enable. Add `TLSTracking` to this array to enable TLS metadata capture from handshake messages.

. Save and exit your editor.

.Verification

. Confirm that the eBPF agent pods have restarted by running the following command:
+
[source,terminal]
----
$ oc get pods -n netobserv-privileged
----
+
.Example output
[source,terminal]
----
NAME                                    READY   STATUS    RESTARTS   AGE
netobserv-ebpf-agent-abc12              1/1     Running   0          2m
----

. Verify the TLS tracking feature is active by running the following command:
+
[source,terminal]
----
$ oc logs -n netobserv-privileged ds/netobserv-ebpf-agent | grep "EnableTLSTracking"
----
+
.Example output
[source,terminal]
----
EnableTLSTracking:true
----
+
The output confirms that the TLS tracking feature has been initialized in the eBPF agent.

// Module included in the following assemblies:
//
// * observability/network_observability/network-observability-monitoring-tls-traffic.adoc

[id="network-observability-analyze-tls-traffic_{context}"]
= Analyze Transport Layer Security traffic data

[role="_abstract"]
View and filter Transport Layer Security (TLS) metadata to identify deprecated configurations and verify encryption compliance in the cluster.

.Prerequisites

* The Network Observability Operator is installed.
* TLS tracking is enabled in the `FlowCollector` custom resource (CR).
* Access to the OpenShift Container Platform web console.

.Procedure

. Navigate to *Observe* -> *Network Traffic* in the OpenShift Container Platform web console and click the *Traffic flows* tab.
+
[NOTE]
====
The *TLS Version* column is enabled by default. If the default TLS version column is not visible after enabling TLS tracking, click *Restore default columns* in *Manage columns* to refresh the table.
====

. Add TLS-specific columns to the traffic table:
.. Click *Manage columns*.
.. Select the *TLS Cipher Suite*, *TLS Group*, and *TLS Types* checkboxes.
.. Click *Save*.

. Filter traffic by message type to view complete TLS metadata:
.. In the filter bar, select *TLS Types* and choose *ServerHello* from the dropdown menu.
+
`ServerHello` messages contain negotiated TLS metadata such as cipher suite and cryptographic group information.

. Filter traffic by TLS version to identify deprecated configurations:
.. In the filter bar, select *TLS Version*.
.. Select the versions you want to review:
* *1.0*: Deprecated
* *1.1*: Deprecated
* *1.2*: Legacy
* *1.3*: Current standard
+
To identify all deprecated connections, filter for TLS versions 1.0 and 1.1.

. Analyze TLS metrics in the overview panel:
.. Click the *Overview* tab.
.. Review the default TLS panels, which include *TLS usage (network flows per second)* and *TLS per version (network flows per second)*.
.. Optional: To view additional TLS metrics, click *Manage panels* to select and display additional panels, such as *TLS per group (network flows per second)* or *TLS per cipher suite (network flows per second)*.

. Identify secure connections in the *Topology* view:
.. Click the *Topology* tab.
+
Connections secured with TLS are marked with a lock icon. The color of the lock icon indicates the security level:
+
* *Red*: Deprecated TLS versions (1.0 or 1.1)
* *Yellow*: Legacy configurations (TLS 1.2)
* *Green*: Secure connections (TLS 1.3)
* *Blue*: Post-Quantum Cryptography (PQC) compliant
+
Select a connection node to view its specific TLS version and cipher suite details.

. View TLS metrics in the Network Observability dashboard:
.. Navigate to *Observe* -> *Dashboards*.
.. Search for *NetObserv* and review the available metrics:
* *TLS Traffic*: Displays overall TLS traffic metrics.
* *Flows rate per TLS version*: Displays traffic trends by TLS version over time.
* *Flows rate per TLS group*: Displays traffic by TLS group over time.

// Module included in the following assemblies:
//
// * observability/network_observability/network-observability-monitoring-tls-traffic.adoc

[id="tls-tracking-fields_{context}"]
= Transport Layer Security tracking fields reference

[role="_abstract"]
Transport Layer Security (TLS) metadata fields track and define encryption protocols, protocol versions, and cipher suite data to help you analyze secure network flows.

.TLS tracking fields
[cols="1,2,2,2",options="header"]
|===
|Field |Description |Possible values |Availability

|*TLS Version*
|Negotiated TLS protocol version.
a|* `1.0`: Deprecated
* `1.1`: Deprecated
* `1.2`: Secure
* `1.3`: Current standard
a|`ClientHello`, `ServerHello`

`ClientHello` displays the version requested by the client. `ServerHello` displays the negotiated version selected by the server.

|*TLS Cipher Suite*
|Cryptographic algorithm suite negotiated between the client and server.
a|Examples:

* `TLS_AES_256_GCM_SHA384`
* `TLS_CHACHA20_POLY1305_SHA256`
a|`ServerHello` only

Displays as `n/a` in `ClientHello` messages.

|*TLS Group*
|Elliptic curve used for key exchange.
a|Examples:

* `X25519`: Recommended for TLS 1.3
* `secp256r1` (P-256)
a|`ServerHello` (TLS 1.3 only)

Displays as `n/a` in `ClientHello` messages and TLS 1.2 connections.

|*TLS Types*
|Type of TLS handshake message captured.
a|* `ClientHello`: Initial client request
* `ServerHello`: Server response
|All TLS flows
|===
