---
title: "Using the Network Observability CLI"
type: reference
domain: openshift
slug: observability-4-22-netobserv-cli-using
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/observability/netobserv-cli-using
version: 4.22
family: observability
documentKind: "Documentation"
---

# Using the Network Observability CLI

[id="netobserv-cli-using"]
= Using the Network Observability CLI

[role="_abstract"]
The Network Observability CLI filters and visualizes network flow and packet telemetry directly within the terminal. The tool exports captured data as JSON, database files, or Packet Capture (PCAP) files for seamless integration with third-party analysis utilities.

//Module included in the following assemblies:
//
// observability/network_observability/netobserv_cli/netobserv-cli-using.adoc

[id="network-observability-cli-capturing-flows_{context}"]
= Capturing flows

[role="_abstract"]
Capture network flows and apply filters based on resources or zones directly in the CLI. This helps you solve complex use cases, such as visualizing the Round-Trip Time (RTT) between two different zones.

Table visualization in the CLI provides viewing and flow search capabilities.

.Prerequisites
* Install the {oc-first}.
* Install the Network Observability CLI (`oc netobserv`) plugin.

.Procedure
. Capture flows with filters enabled by running the following command:
+
[source,terminal]
----
$ oc netobserv flows --enable_filter=true --action=Accept --cidr=0.0.0.0/0 --protocol=TCP --port=49051
----
. Add filters to the `live table filter` prompt in the terminal to further refine the incoming flows. For example:
+
[source,terminal]
----
live table filter: [SrcK8S_Zone:us-west-1b] press enter to match multiple regular expressions at once
----
. Use the *PageUp* and *PageDown* keys to toggle between *None*, *Resource*, *Zone*, *Host*, *Owner* and *all of the above*.
. To stop capturing, press kbd:[Ctrl+C]. The data that was captured is written to two separate files in an `./output` directory located in the same path used to install the CLI.
. View the captured data in the `./output/flow/<capture_date_time>.json` JSON file, which contains JSON arrays of the captured data.
+
.Example JSON file
[source,json]
----
{
  "AgentIP": "10.0.1.76",
  "Bytes": 561,
  "DnsErrno": 0,
  "Dscp": 20,
  "DstAddr": "f904:ece9:ba63:6ac7:8018:1e5:7130:0",
  "DstMac": "0A:58:0A:80:00:37",
  "DstPort": 9999,
  "Duplicate": false,
  "Etype": 2048,
  "Flags": 16,
  "FlowDirection": 0,
  "IfDirection": 0,
  "Interface": "ens5",
  "K8S_FlowLayer": "infra",
  "Packets": 1,
  "Proto": 6,
  "SrcAddr": "3e06:6c10:6440:2:a80:37:b756:270f",
  "SrcMac": "0A:58:0A:80:00:01",
  "SrcPort": 46934,
  "TimeFlowEndMs": 1709741962111,
  "TimeFlowRttNs": 121000,
  "TimeFlowStartMs": 1709741962111,
  "TimeReceived": 1709741964
}
----
. You can use SQLite to inspect the `./output/flow/<capture_date_time>.db` database file. For example:
.. Open the file by running the following command:
+
[source,terminal]
----
$ sqlite3 ./output/flow/<capture_date_time>.db
----

.. Query the data by running a SQLite `SELECT` statement, for example:
+
[source,terminal]
----
sqlite> SELECT DnsLatencyMs, DnsFlagsResponseCode, DnsId, DstAddr, DstPort, Interface, Proto, SrcAddr, SrcPort, Bytes, Packets FROM flow WHERE DnsLatencyMs >10 LIMIT 10;
----
+
.Example output
[source,terminal]
----
12|NoError|58747|10.128.0.63|57856||17|172.30.0.10|53|284|1
11|NoError|20486|10.128.0.52|56575||17|169.254.169.254|53|225|1
11|NoError|59544|10.128.0.103|51089||17|172.30.0.10|53|307|1
13|NoError|32519|10.128.0.52|55241||17|169.254.169.254|53|254|1
12|NoError|32519|10.0.0.3|55241||17|169.254.169.254|53|254|1
15|NoError|57673|10.128.0.19|59051||17|172.30.0.10|53|313|1
13|NoError|35652|10.0.0.3|46532||17|169.254.169.254|53|183|1
32|NoError|37326|10.0.0.3|52718||17|169.254.169.254|53|169|1
14|NoError|14530|10.0.0.3|58203||17|169.254.169.254|53|246|1
15|NoError|40548|10.0.0.3|45933||17|169.254.169.254|53|174|1
----
//Module included in the following assemblies:
//
// observability/network_observability/netobserv_cli/netobserv-cli-using.adoc

[id="network-observability-cli-capturing-packets_{context}"]
= Capturing packets

[role="_abstract"]
Use the Network Observability CLI to capture network packets. You can apply filters and refine them live in the terminal for accurate, real-time debugging.

.Prerequisites
* Install the {oc-first}.
* Install the Network Observability CLI (`oc netobserv`) plugin.

.Procedure
. Run the packet capture with filters enabled:
+
[source,terminal]
----
$ oc netobserv packets --action=Accept --cidr=0.0.0.0/0 --protocol=TCP --port=49051
----
. Add filters to the `live table filter` prompt in the terminal to refine the incoming packets. An example filter is as follows:
+
[source,terminal]
----
live table filter: [SrcK8S_Zone:us-west-1b] press enter to match multiple regular expressions at once
----
. Use the *PageUp* and *PageDown* keys to toggle between *None*, *Resource*, *Zone*, *Host*, *Owner* and *all of the above*.
. To stop capturing, press kbd:[Ctrl+C].
. View the captured data, which is written to a single file in an `./output/pcap` directory located in the same path that was used to install the CLI:
.. The `./output/pcap/<capture_date_time>.pcap` file can be opened with Wireshark.
// Module included in the following assemblies:
//
// * observability/network_observability/netobserv_cli/netobserv-cli-using.adoc

[id="network-observability-cli-capturing-metrics_{context}"]
= Capturing metrics

[role="_abstract"]
Generate on-demand network observability dashboards in Prometheus using a service monitor. This allows you to quickly view and analyze network metrics.

.Prerequisites
* Install the {oc-first}.
* Install the Network Observability CLI (`oc netobserv`) plugin.

.Procedure
. Capture metrics with filters enabled by running the following command:
+
.Example output
[source,terminal]
----
$ oc netobserv metrics --enable_filter=true --cidr=0.0.0.0/0 --protocol=TCP --port=49051
----
. Open the link provided in the terminal to view the *NetObserv / On-Demand* dashboard:
+
.Example URL
[source,terminal]
----
https://console-openshift-console.apps.rosa...openshiftapps.com/monitoring/dashboards/netobserv-cli
----
+
[NOTE]
====
Features that are not enabled present as empty graphs.
====
// Module included in the following assemblies:

// * observability/network_observability/netobserv_cli/netobserv-cli-install.adoc

[id="network-observability-cli-uninstall_{context}"]
= Cleaning the Network Observability CLI

[role="_abstract"]
Use `oc netobserv cleanup` to manually remove all components installed by the Network Observability CLI from your cluster. While the client runs this command automatically after a capture, you may need to run it manually if you face connectivity issues.

.Procedure
* Run the following command:
+
[source,terminal]
----
$ oc netobserv cleanup
----

[role=_additional_resources]
.Additional resources
* Network Observability CLI reference
