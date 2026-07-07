---
title: "Configuring your firewall"
type: reference
domain: openshift
slug: installing-4-22-configuring-firewall
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/configuring-firewall
version: 4.22
family: installing
documentKind: "Documentation"
---

# Configuring your firewall

[id="configuring-firewall"]
= Configuring your firewall

If you use a firewall, you must configure your firewall's allowlist to ensure OpenShift Container Platform has access to the URLs it requires to pull container images and access Red Hat services.
Additional URLs are required for features such as Telemetry, {red-hat-lightspeed}, cloud provider integrations, or certain build strategies.

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc
// * installing/installing-oci-agent-based-installer.adoc

[id="configuring-firewall_{context}"]
= Configuring your firewall for OpenShift Container Platform

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires. When using a firewall, make additional configurations to the firewall so that OpenShift Container Platform can access the sites that it requires to function.

There are no special configuration considerations for services running on only controller nodes compared to compute nodes.

For a disconnected environment, you must mirror content from both Red{nbsp}Hat and Oracle. This environment requires that you create firewall rules to expose your firewall to specific ports and registries.

[NOTE]
====
If your environment has a dedicated load balancer in front of your OpenShift Container Platform cluster, review the allowlists between your firewall and load balancer to prevent unwanted network restrictions to your cluster.
====

.Procedure

. Allowlist the following container registry URLs for cluster installation and upgrades:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`registry.redhat.io`
|443
|Provides core container images

|`access.redhat.com`
|443
|Hosts a signature store that a container client requires for verifying images pulled from `registry.access.redhat.com`. In a firewall environment, ensure that this resource is on the allowlist.

|`registry.access.redhat.com`
|443
|Hosts all the container images that are stored on the Red Hat Ecosystem Catalog, including core container images.

|`quay.io`
|443
|Provides core container images

|`cdn.quay.io`
|443
|Provides core container images

|`cdn01.quay.io`
|443
|Provides core container images

|`cdn02.quay.io`
|443
|Provides core container images

|`cdn03.quay.io`
|443
|Provides core container images

|`cdn04.quay.io`
|443
|Provides core container images

|`cdn05.quay.io`
|443
|Provides core container images

|`cdn06.quay.io`
|443
|Provides core container images

|`icr.io`
|443
|Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks.

|`cp.icr.io`
|443
|Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks.
|===
+
* You can use the wildcard `*.quay.io` instead of `cdn.quay.io` and `cdn0[1-6].quay.io` in your allowlist.
* You can use the wildcard `*.access.redhat.com` to simplify the configuration and ensure that all subdomains, including `registry.access.redhat.com`, are allowed.
* When adding a site such as `quay.io` to your allowlist, do not add a wildcard entry such as `*.quay.io` to your denylist. In most cases, image registries use a content delivery network (CDN) to serve images. If a firewall blocks access, image downloads are denied when the initial download request redirects to a hostname such as `cdn01.quay.io`.

. Allowlist the following URLs to enable cluster access, authentication, and updates:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`*.apps.<cluster_name>.<base_domain>`
|443
|Allowlist these URLs to enable cluster access, authentication, and updates.

|`api.openshift.com`
|443
|API endpoint for cluster tokens and update checks.

|`console.redhat.com`
|443
|Authentication service for cluster tokens.

|`sso.redhat.com`
|443
|The `https://console.redhat.com` site uses authentication from `sso.redhat.com`
|===
+
For egress traffic, Operators require route access to perform health checks to establish a connection for reaching endpoints. The authentication and web console Operators connect to two routes to verify functionality. Cluster administrators who do not want to allow `*.apps.<cluster_name>.<base_domain>`, must allow the following routes:
+
* `oauth-openshift.apps.<cluster_name>.<base_domain>`
* `canary-openshift-ingress-canary.apps.<cluster_name>.<base_domain>`
* `console-openshift-console.apps.<cluster_name>.<base_domain>`, or the hostname
that is specified in the `spec.route.hostname` field of the
`consoles.operator/cluster` object if the field is not empty.

. Allowlist the following registry URLs that host related artifacts for cluster installation and upgrades, such as installation content, release images, and client tools:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`mirror.openshift.com`
|443
|Required to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator needs only a single functioning source.

|`quayio-production-s3.s3.amazonaws.com`
|443
|Required to access Quay image content in AWS.

// |`registry.access.redhat.com`
// |443
// |Required for `odo` CLI.

|`rhcos.mirror.openshift.com`
|443
|Required to download {op-system-first} images.

|`storage.googleapis.com/openshift-release`
|443
|A source of release image signatures, although the Cluster Version Operator needs only a single functioning source.
|===

. Set your firewall's allowlist to include any site that provides resources for a language or framework that your builds require.

. If you do not disable Telemetry, you must grant access to the following URLs to access Telemetry and {red-hat-lightspeed}:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`cert-api.access.redhat.com`
|443
|Required for Telemetry

|`api.access.redhat.com`
|443
|Required for Telemetry

|`infogw.api.openshift.com`
|443
|Required for Telemetry

|`console.redhat.com`
|443
|Required for Telemetry and for `insights-operator`
|===

. Set your firewall's allowlist to include the following registry URLs:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`api.openshift.com`
|443
|Required both for your cluster token and to check if updates are available for the cluster.

|`rhcos.mirror.openshift.com`
|443
|Required to download {op-system-first} images.
|===

. Set your firewall's allowlist to include the following external URLs. Each repository URL hosts {oci} containers. Consider mirroring images to as few repositories as possible to reduce any performance issues.
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`k8s.gcr.io`
|port
|A Kubernetes registry that hosts container images for a community-based image registry. This image registry is hosted on a custom Google Container Registry (GCR) domain.

|`ghcr.io`
|port
|A GitHub image registry where you can store and manage Open Container Initiative images. Requires an access token to publish, install, and delete private, internal, and public packages.

|`storage.googleapis.com`
|443
|A source of release image signatures, although the Cluster Version Operator needs only a single functioning source.

|`registry.k8s.io`
|port
|Replaces the `k8s.gcr.io` image registry because the `k8s.gcr.io` image registry does not support other platforms and vendors.
|===

. If you use {alibaba}, {aws-first}, {azure-first}, or {gcp-first} to host your cluster, you must grant access to the URLs that offer the cloud provider API and DNS for that cloud:
+
[cols="2a,8a,2a,8a",options="header"]
|===
|Cloud |URL | Port |Function

|Alibaba
|`*.aliyuncs.com`
|443
|Required to access Alibaba Cloud services and resources. Review the Alibaba endpoints_config.go file to find the exact endpoints to allow for the regions that you use.

.17+|AWS
|`aws.amazon.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.amazonaws.com`

Alternatively, if you choose to not use a wildcard for AWS APIs, you must include the following URLs in your allowlist:
|443
|Required to access AWS services and resources. Review the AWS Service Endpoints in the AWS documentation to find the exact endpoints to allow for the regions that you use.

|`ec2.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`events.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`iam.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`route53.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.s3.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.s3.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`*.s3.dualstack.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`sts.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`sts.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`tagging.us-east-1.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment. This endpoint is always `us-east-1`, regardless of the region the cluster is deployed in.

|`ec2.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`elasticloadbalancing.<aws_region>.amazonaws.com`
|443
|Used to install and manage clusters in an AWS environment.

|`servicequotas.<aws_region>.amazonaws.com`
|443
|Required. Used to confirm quotas for deploying the service.

|`tagging.<aws_region>.amazonaws.com`
|443
|Allows the assignment of metadata about AWS resources in the form of tags.

|`*.cloudfront.net`
|443
|Used to provide access to CloudFront. If you use the AWS Security Token Service (STS) and the private S3 bucket, you must provide access to CloudFront.

.2+|GCP
|`*.googleapis.com`
|443
|Required to access {gcp-short} services and resources. Review Cloud Endpoints in the {gcp-short} documentation to find the endpoints to allow for your APIs.

|`accounts.google.com`
|443
| Required to access your {gcp-short} account.

.3+|Microsoft Azure
|`management.azure.com`
|443
|Required to access Microsoft Azure services and resources. Review the Microsoft Azure REST API reference in the Microsoft Azure documentation to find the endpoints to allow for your APIs.

|`*.blob.core.windows.net`
|443
|Required to download Ignition files.

|`login.microsoftonline.com`
|443
|Required to access Microsoft Azure services and resources. Review the Azure REST API reference in the Microsoft Azure documentation to find the endpoints to allow for your APIs.

|===

. Allowlist the following URL for optional third-party content:
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`registry.connect.redhat.com`
|443
|Required for all third-party images and certified operators.
|===

. If you use a default Red Hat Network Time Protocol (NTP) server, allow the following URLs. NTP operates on User Datagram Protocol (UDP) port 123, so this port must be opened on the firewall.
+
[cols="3,2,4",options="header"]
|===
|URL | Port | Function

|`1.rhel.pool.ntp.org`
|123
|Provides NTP services for time synchronization.

|`2.rhel.pool.ntp.org`
|123
|Provides NTP services for time synchronization.

|`3.rhel.pool.ntp.org`
|123
|Provides NTP services for time synchronization.
|===

[NOTE]
====
If you do not use a default Red Hat NTP server, verify the NTP server for your platform and allow it in your firewall.
====

[role="_additional-resources"]
.Additional resources

* OpenID Connect requirements for AWS STS

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="network-flow-matrix_{context}"]
= OpenShift Container Platform network flow matrix

The following network flow matrixes describe the ingress flows to OpenShift Container Platform services for the following environments:

* OpenShift Container Platform on bare metal
* {sno-caps} with other platforms
* OpenShift Container Platform on {aws-first}
* {sno-caps} on {aws-short}

[NOTE]
====
You can use the `commatrix` plugin for the `oc` command to generate local network flow data for your cluster. For more information see "Generating ingress network flow data using the `commatrix` plugin".
====

Use the information in the appropriate network flow matrix to help you manage ingress traffic for your specific environment. You can restrict ingress traffic to essential flows to improve network security.

Additionally, consider the following dynamic port ranges when managing ingress traffic for both bare metal and cloud environments:

* `9000-9999`: Reserved for internal OpenShift Container Platform components. Do not assign user workloads or services to ports in this range.
* `30000-32767`: Kubernetes `NodePort` service ports. These ports are required only if you expose services by using the `NodePort` service type. If `NodePort` services are not used, you can block this port range.

To view or download the complete raw CSV content for an environment, see the following resources:

* OpenShift Container Platform on bare metal

* {sno-caps} with other platforms

* OpenShift Container Platform on {aws-short}

* {sno-caps} on {aws-short}

[NOTE]
====
The network flow matrixes describe ingress traffic flows for a base OpenShift Container Platform or {sno} installation. The matrixes do not apply for {hcp}, Red{nbsp}Hat build of MicroShift, or standalone clusters.
====

[id="network-flow-matrix-common_{context}"]
== Base network flows

The following matrixes describe the base ingress flows to OpenShift Container Platform services.

[NOTE]
====
For base ingress flows to {sno} clusters, see the _Control plane node base flows_ matrix only.
====

[id="network-flow-matrix-control_{context}"]
.Control plane node base flows
[%header,format=csv]
|===

|===

[id="network-flow-matrix-worker_{context}"]
.Worker node base flows
[%header,format=csv]
|===

|===

[id="network-flow-matrix-bm_{context}"]
== Additional network flows for OpenShift Container Platform on bare metal

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on bare metal.

.OpenShift Container Platform on bare metal
[%header,format=csv]
|===

|===

[id="network-flow-matrix-sno_{context}"]
== Additional network flows for {sno} with other platforms

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to {sno} configured with `platform: none` in the installation manifest.

.{sno-caps} with other platforms
[%header,format=csv]
|===

|===

[id="network-flow-matrix-aws_{context}"]
== Additional network flows for OpenShift Container Platform on {aws-short}

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on {aws-short}.

.OpenShift Container Platform on AWS
[%header,format=csv]
|===

|===

[id="network-flow-matrix-aws-sno_{context}"]
== Additional network flows for {sno} on {aws-short}

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to {sno} on {aws-short}.

.{sno-caps} on AWS
[%header,format=csv]
|===

|===

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="network-commatrix-plugin-intro_{context}"]
= Ingress network flow management with the commatrix plugin

[role="_abstract"]
Use the `commatrix` plugin for the `oc` command to analyze ingress network traffic and generate firewall rules for live clusters.

For ingress network analysis, the plugin reads the services deployed in a target cluster and generates a communication matrix of expected ingress flows. You can export the data in formats such as CSV, JSON, or YAML for audits, documentation, or configuring external firewalls.

For firewall configuration, the plugin generates `nftables` rules in Butane format that restrict ingress traffic to only the flows required by your cluster. The plugin also generates a `NodeDisruptionPolicy` patch to apply updates without triggering node reboots.

The plugin relies on `EndpointSlice` resources for port discovery. However, some ports on your cluster nodes might be open without a corresponding service or `EndpointSlice`, such as host-level services, monitoring agents, or third-party software. Use the `--host-open-ports` flag to discover actual listening ports on your nodes and merge them into the generated firewall rules. This ensures the rules capture all known open ports, not just those defined in `EndpointSlice` resources.

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="network-commatrix-plugin-install_{context}"]
= Installing the commatrix plugin

[role="_abstract"]
You can install the `commatrix` plugin from the Red Hat Ecosystem Catalog.

[NOTE]
====
You can also install the `commatrix` plugin by using Krew. For more information, see "{cli-manager} overview".
====

.Prerequisites
* You installed the OpenShift CLI (`oc`).
* You installed Podman.

.Procedure

. Log in to the Red Hat Ecosystem Catalog registry by running the following command and entering your credentials:
+
[source,bash]
----
$ podman login registry.redhat.io
----

. Extract the `commatrix` binary from the plugin image by running the following commands:
+
[source,bash]
----
$ podman create --name oc-commatrix registry.redhat.io/openshift-kni/commatrix:v4.22
$ podman cp oc-commatrix:/oc-commatrix .
$ podman rm oc-commatrix
----

. Move the extracted binary to a directory in your system `PATH`, such as `/usr/local/bin/`, by running the following command:
+
[source,bash]
----
sudo mv oc-commatrix /usr/local/bin/
----

.Verification

* Run the following command to verify that the plugin is available locally:
+
[source,bash]
----
$ oc commatrix
----
+
[source,bash]
----
Generate an up-to-date communication flows matrix for all ingress flows of openshift (multi-node and single-node in OpenShift) and Operators.

 Optionally, generate a host open ports matrix and the difference with the communication matrix.

 For additional details, please refer to the communication matrix documentation(https://github.com/openshift-kni/commatrix/blob/main/README.md).

Usage:
  commatrix [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  generate    Generate an up-to-date communication flows matrix for all ingress flows.
  help        Help about any command

Flags:
  -h, --help   help for commatrix

Use "commatrix [command] --help" for more information about a command.
----

[role="_additional-resources"]
.Additional resources
* {cli-manager} overview

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="network-commatrix-plugin-generate_{context}"]
= Generate ingress network flow data using the `commatrix` plugin

[role="_abstract"]
Use the `commatrix` plugin for the `oc` command to generate ingress network flow data from your cluster and identify any differences between open ports on the host and expected ingress flows for your environment.

The plugin generates ingress flows to OpenShift Container Platform services for the following environments:

* OpenShift Container Platform on bare metal
* {sno-caps} with other platforms
* OpenShift Container Platform on {aws-first}
* {sno-caps} on {aws-short}

.Prerequisites
* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.
* You installed Podman.
* You installed the `commatrix` plugin.

.Procedure

. Generate network flow data by running the following command:
+
[source,bash]
----
$ oc commatrix generate
----
+
[NOTE]
====
By default, the plugin generates the network flow data in CSV format in a `communication-matrix` directory in your current working directory.
====

.Verification

* View the generated network flow data in the `communication-matrix` directory by running the following command:
+
[source,bash]
----
$ cat communication-matrix/communication-matrix.csv
----
+
[source,bash]
----
Direction,Protocol,Port,Namespace,Service,Pod,Container,Node Role,Optional
Ingress,TCP,4194,kube-system,kubelet,konnectivity-agent,,,false
Ingress,TCP,9100,openshift-monitoring,node-exporter,node-exporter,kube-rbac-proxy,,false
Ingress,TCP,9103,openshift-ovn-kubernetes,ovn-kubernetes-node,ovnkube-node,kube-rbac-proxy-node,,false

...
----

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="commatrix-restricting-ingress-traffic_{context}"]
= Ingress traffic configuration with the commatrix plugin

[role="_abstract"]
You can use the `commatrix` plugin to generate `nftables` rules that configure the firewall on cluster nodes to permit only the ingress traffic defined in the communication matrix.

`nftables` is the packet filtering framework in the Linux kernel that replaces `iptables`.
OpenShift Container Platform cluster nodes running {op-system-first} use `nftables` for packet filtering.
The `commatrix` plugin generates `nftables` rules and packages them as `MachineConfig` resources that the Machine Config Operator applies to your nodes.

When you generate firewall rules with the `commatrix` plugin in Butane format, the plugin also generates a `NodeDisruptionPolicy` patch.
This patch enables the Machine Config Operator to apply `nftables` rule updates without triggering a full node reboot, minimizing disruption to running workloads.

[IMPORTANT]
====
When operators or components are installed, enabled, uninstalled, or disabled, you must regenerate the firewall rules to reflect the new configuration. Failure to regenerate and apply firewall rules in this scenario might have the following consequences:

* Unnecessary ports might remain open, which increases the attack surface of your cluster.

* Services might fail to function correctly if required ports remain blocked by outdated firewall rules.
====

[role="_additional-resources"]
.Additional resources
* Minimizing node disruption with MachineConfig changes
* Custom nftables firewall rules in OpenShift

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="commatrix-generate-butane_{context}"]
= Generate nftables firewall rules in Butane format

[role="_abstract"]
You can generate `nftables` firewall rules in Butane format by using the `commatrix` plugin.
The generated Butane configs contain `nftables` rules that allow the ingress flows defined in the communication matrix and block all other ingress flows.

[WARNING]
====
Errors in `nftables` rules can block legitimate traffic and isolate nodes from the cluster.
Review all generated rules before applying them.
====

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.
* You installed Podman.
* You installed the `commatrix` plugin.
* You installed the `butane` CLI.
* For custom node groups, you need an existing machine config pool that you can target using node label selectors.

.Procedure

. Generate firewall rules in Butane format by running the following command:
+
[source,terminal]
----
$ oc commatrix generate --format butane
----
+
By default, the plugin writes the output files to the `communication-matrix` directory in your current working directory.
+
The plugin generates one Butane config file per node pool, named `butane-<pool_name>.yaml`, and a `node-disruption-policy.yaml` patch file, for example:
+
[source,terminal]
----
communication-matrix/
├── butane-master.yaml
├── butane-worker.yaml
└── node-disruption-policy.yaml
----
+
. Review the generated Butane config files by running the following command:
+
[source,terminal]
----
$ cat communication-matrix/butane-<pool_name>.yaml
----
+
See the following example of the `butane-master.yaml` file.
+
[NOTE]
====
You can adjust the generated firewall rules in your YAML file to suit your network environment.
====
+
[source,yaml]
----
variant: openshift
version: 4.22.0
metadata:
  name: 98-nftables-commatrix-master
  labels:
    machineconfiguration.openshift.io/role: master
systemd:
  units:
    - name: "nftables.service"
      enabled: true
      contents: |
        # ... systemd unit configuration ...
storage:
  files:
    - path: /etc/sysconfig/nftables.conf
      mode: 0600
      overwrite: true
      contents:
        inline: |
          table inet openshift_filter {
              chain OPENSHIFT {
                  type filter hook input priority 1; policy accept;

                  # Allow loopback traffic
                  iif lo accept

                  # Allow established and related traffic
                  ct state established,related accept

                  # Allow ICMP on ipv4
                  ip protocol icmp accept
                  ip6 nexthdr ipv6-icmp accept

                  # Allow specific TCP and UDP ports
                  tcp dport { 22, 6443, 9100, 10250, 30000-60999 } accept
                  udp dport { 6081, 30000-60999 } accept

                  # Drop broadcast traffic with rate-limited logging
                  ip daddr 255.255.255.255 jump { limit rate 1/minute log prefix "firewall "; drop; }

                  # Rate-limited logging and default drop
                  jump { limit rate 1/minute log prefix "firewall "; drop; }
              }
          }
----
+
. Review the generated `NodeDisruptionPolicy` patch by running the following command:
+
[source,terminal]
----
$ cat communication-matrix/node-disruption-policy.yaml
----

. Check whether your cluster already defines `NodeDisruptionPolicy` entries by running the following command:
+
[source,terminal]
----
$ oc get -o yaml machineconfiguration cluster
----

. Apply the `NodeDisruptionPolicy` patch:
+
.. If the `MachineConfiguration` resource does not define any `nodeDisruptionPolicy` entries, run the following command:
+
[source,terminal]
----
$ oc patch machineconfiguration cluster --type=merge --patch-file=communication-matrix/node-disruption-policy.yaml
----
+
.. If the `MachineConfiguration` resource already contains `nodeDisruptionPolicy` entries, manually add the entries from `node-disruption-policy.yaml` to the existing `.spec.nodeDisruptionPolicy.units` and `.spec.nodeDisruptionPolicy.files` lists by running the following command:
+
[source,terminal]
----
$ oc edit machineconfiguration cluster
----

. Convert each Butane config to a `MachineConfig` resource by running the following command:
+
[source,terminal]
----
$ butane --strict -o mc-<pool_name>.yaml communication-matrix/butane-<pool_name>.yaml
----
+
* `<pool_name>` is the name of the target node pool.

. Apply the `MachineConfig` resources by running the following command for each node pool:
+
[IMPORTANT]
====
You must apply the `NodeDisruptionPolicy` patch before applying `MachineConfig` resources.
If you apply `MachineConfig` resources without the `NodeDisruptionPolicy` in place, the Machine Config Operator triggers a full node reboot.
====
+
[source,terminal]
----
$ oc apply -f mc-<pool_name>.yaml
----
+
The plugin generates `MachineConfig` resources with the naming pattern `98-nftables-commatrix-<pool_name>`.

.Verification

. Open a debug shell on a target node by running the following commands:
+
[source,terminal]
----
$ oc debug node/<node_name>
sh-5.1# chroot /host
----
+
* `<node_name>` is the name of a cluster node.
* `chroot /host` accesses the host filesystem.
+
. Verify that the `nftables` rules are active on a node by running the following command:
+
[source,terminal]
----
sh-5.1# nft list ruleset
----
+
[source,terminal]
----
...
table inet openshift_filter {
	chain OPENSHIFT {
		type filter hook input priority filter + 1; policy accept;
		iif "lo" accept
		ct state established,related accept
		ip protocol icmp accept
		ip6 nexthdr ipv6-icmp accept
		tcp dport { 22, 111, 2379-2380, 6080, 6443, 9001, 9099-9100, 9103-9105, 9107-9108, 9192, 9258, 9443, 9637, 9978-9980, 10250, 10256-10259, 17697, 22623-22624, 30000-60999 } accept
		udp dport { 111, 6081, 30000-60999 } accept
		ip daddr 255.255.255.255 jump {
			limit rate 1/minute burst 5 packets log prefix "firewall "
			drop
		}
		jump {
			limit rate 1/minute burst 5 packets log prefix "firewall "
			drop
		}
	}
}
...
----
+
. Verify that denied traffic is logged with rate limiting by checking the node journal:
+
[source,terminal]
----
$ oc debug node/<node_name> -- chroot /host journalctl -k --grep firewall
----
+
Denied packets are logged, but log entries are rate-limited to one per minute with an initial burst of five entries.

[role="_additional-resources"]
.Additional resources
* Installing Butane

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="commatrix-revert-nftables_{context}"]
= Revert nftables firewall rules generated by the commatrix plugin

[role="_abstract"]
If you need to remove the `nftables` firewall rules from your cluster nodes, delete the `MachineConfig` resources, and then clean up the `NodeDisruptionPolicy` entries.

.Prerequisites

* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.
* You applied `nftables` firewall rules generated by the `commatrix` plugin.

.Procedure

. Identify the `MachineConfig` resources created by the `commatrix` plugin by running the following command:
+
[source,terminal]
----
$ oc get machineconfig | grep nftables
----

. Delete the `MachineConfig` resource for each node pool by running the following command:
+
[source,terminal]
----
$ oc delete machineconfig 98-nftables-commatrix-<pool_name>
----

. Wait for all `MachineConfigPool` resources to return to the `UPDATED` state:
+
[source,terminal]
----
$ oc get mcp
----
+
.Example output showing pools in `UPDATED` state
[source,terminal]
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6   True      False      False      1              1                   1                     0                      160d
worker   rendered-worker-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6   True      False      False      0              0                   0                     0                      160d
----

. Open a debug shell on a target node by running the following commands:
+
[source,terminal]
----
$ oc debug node/<node_name>
sh-5.1# chroot /host
----
+
* `<node_name>` is the name of a cluster node.
* `chroot /host` accesses the host filesystem.

. Verify that the custom `nftables` rules were removed by running the following command:
+
[source,terminal]
----
sh-5.1# nft list ruleset 2>&1 | grep -q openshift_filter || echo "Custom rules removed"
----

. Remove the related `nftables` rules from the `NodeDisruptionPolicy` entries by editing the `MachineConfiguration` resource:
+
[source,terminal]
----
$ oc edit machineconfiguration cluster
----
+
Remove the `nftables.service` entry from `.spec.nodeDisruptionPolicy.units` and the `/etc/sysconfig/nftables.conf` entry from `.spec.nodeDisruptionPolicy.files`.

// Module included in the following assemblies:
//
// * installing/install_config/configuring-firewall.adoc

[id="commatrix-plugin-reference_{context}"]
= Reference flags for the `commatrix` plugin

[role="_abstract"]
The following table describes the flags for the `commatrix` plugin.

[cols="2,1,3", options="header"]
|===
|Flag |Type |Description

|`--customEntriesFormat` |string |Define the format of a custom entries file. The plugin appends the entries in this file to the generated data. Supported values are `json`, `yaml`, or `csv`.

|`--customEntriesPath` |string |Define the file path to a custom entries file. The plugin appends the entries in this file to the generated data.

|`--debug` |boolean |Enable verbose logging for debugging. The default value is `false`.

|`--destDir` |string |Define the directory for output files. The default value is `communication-matrix`.

|`--custom-node-group` |string |Assign nodes matching a label selector to a custom group for separate firewall rule generation. Specify in `<group_name>=<label_selector>` format. You can specify this flag multiple times to define multiple custom groups. This flag applies only to `nft`, `butane`, and `mc` output formats. A `MachineConfigPool` custom group matching the custom group name must exist before you apply the generated `MachineConfig` resources.

|`--format` |string |Define the output format. Supported values are `json`, `yaml`, `csv`, `nft`, `butane`, or `mc`. The `butane` format generates Butane YAML configs containing nftables firewall rules. The `mc` format generates `MachineConfig` custom resources containing nftables firewall rules. The default value is `csv`.

|`--host-open-ports` |boolean |Generate the expected communication data for the cluster environment. Identify the actual open ports on the cluster node to compare the difference between the expected open ports and the actual open ports. You can view the differences in the generated `matrix-diff-ss` file in the destination directory. For `nft`, `butane`, and `mc` formats, host open ports are merged into the communication matrix instead of generating a separate diff file.

|`-h` |boolean |Display the plugin help information.
|===
