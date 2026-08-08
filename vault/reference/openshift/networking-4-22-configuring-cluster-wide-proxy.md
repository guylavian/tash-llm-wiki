---
title: "Configuring a cluster-wide proxy"
type: reference
domain: openshift
slug: networking-4-22-configuring-cluster-wide-proxy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/configuring-cluster-wide-proxy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring a cluster-wide proxy

[id="configuring-a-cluster-wide-proxy"]
= Configuring a cluster-wide proxy

[role="_abstract"]
If you are using an existing Virtual Private Cloud (VPC), you can configure a cluster-wide proxy during
a OpenShift Container Platform
an OpenShift Container Platform
cluster installation or after the cluster is installed. When you enable a proxy, the core cluster components are denied direct access to the internet, but the proxy does not affect user workloads.

[NOTE]
====
The system proxies only cluster system egress traffic, including calls to the cloud provider API.
====

You can enable a proxy only for OpenShift Container Platform clusters that use the Customer Cloud Subscription (CCS) model.

If you use a cluster-wide proxy, you are responsible for maintaining the availability of the proxy to the cluster. If the proxy becomes unavailable, then it might impact the health and supportability of the cluster.

// Module included in the following assemblies:
//
// * networking/configuring-cluster-wide-proxy.adoc

[id="cluster-wide-proxy-prereqs_{context}"]
= Prerequisites for configuring a cluster-wide proxy

[role="_abstract"]
To configure a cluster-wide proxy, you must meet the following requirements. These requirements are valid when you configure a proxy during installation or postinstallation.

[id="cluster-wide-proxy-general-prereqs_{context}"]
== General requirements

* You are the cluster owner.
* Your account has enough privileges.
* You have an existing Virtual Private Cloud (VPC) for your cluster.
* You have an existing VPC for your cluster.
* You are using the Customer Cloud Subscription (CCS) model for your cluster.
* The proxy can access the VPC for the cluster and the private subnets of the VPC. The proxy must also be accessible from the VPC for the cluster and from the private subnets of the VPC.
* You have added the following endpoints to your VPC endpoint:
** `ec2.<aws_region>.amazonaws.com`
** `elasticloadbalancing.<aws_region>.amazonaws.com`
** `s3.<aws_region>.amazonaws.com`
+
These endpoints are required to complete requests from the nodes to the AWS EC2 API. Because the proxy works at the container level and not at the node level, you must route these requests to the AWS EC2 API through the AWS private network. Adding the public IP address of the EC2 API to your allowlist in your proxy server is not enough.
+
[IMPORTANT]
====
When using a cluster-wide proxy, you must configure the `s3.<aws_region>.amazonaws.com` endpoint as type `Gateway`.
====

[id="cluster-wide-proxy-network-prereqs_{context}"]
== Network requirements

If your proxy re-encrypts egress traffic, you must create exclusions to several domain and port combinations required by OpenShift.

Your proxy must exclude re-encrypting the following OpenShift URLs:

.URLs to exclude from egress traffic re-encryption
[cols="6,1,6",options="header"]
|===
|Address | Protocol/Port | Function
|`observatorium-mst.api.openshift.com`
|https/443
|Required. Used for Managed OpenShift-specific telemetry.

|`sso.redhat.com`
|https/443
|The `console.redhat.com/openshift` site uses authentication from `sso.redhat.com` to download the cluster pull secret and use Red Hat SaaS solutions to ease monitoring of your subscriptions, cluster inventory, and chargeback reporting.
|===

[role="_additional-resources"]
.Additional resources
//ifdef::openshift-rosa[]
//Commenting out the following THREE xrefs because they are breaking the networking and potentially other PRs. Pre- or post-publish HCP pruning task.
//ifdef::openshift-rosa-hcp[]
//* Prerequisites for {hcp-title}
//endif::openshift-rosa-hcp[]
//ifdef::openshift-rosa[]
//* For the installation prerequisites for ROSA clusters that use the AWS Security Token Service (STS), see AWS prerequisites for ROSA with STS.
// This section needs to remain hidden until the HCP migration is completed
// * For the installation prerequisites for ROSA clusters that use the AWS Security Token Service (STS), see AWS prerequisites for ROSA with STS.
//* For the installation prerequisites for ROSA clusters that do not use STS, see AWS prerequisites for ROSA.
//endif::openshift-rosa[]
* Customer Cloud Subscriptions on AWS

// Module included in the following assemblies:
//
// * networking/configuring-cluster-wide-proxy.adoc

[id="configuring-a-proxy-trust-bundle-responsibilities_{context}"]
= Responsibilities for additional trust bundles

[role="_abstract"]
If you supply an additional trust bundle, you are responsible for the following requirements:

* Ensuring that the contents of the additional trust bundle are valid
* Ensuring that the certificates, including intermediary certificates, contained in the additional trust bundle have not expired
* Tracking the expiry and performing any necessary renewals for certificates contained in the additional trust bundle
* Updating the cluster configuration with the updated additional trust bundle

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-cluster-wide-proxy.adoc

[id="configuring-a-proxy-during-installation_{context}"]
= Configuring a proxy during installation

[role="_abstract"]
You can configure an HTTP or HTTPS proxy when you install an OpenShift Container Platform with Customer Cloud Subscription (CCS) cluster into an existing Virtual Private Cloud (VPC). You can configure the proxy during installation by using {cluster-manager-first}.
You can configure an HTTP or HTTPS proxy when you install a OpenShift Container Platform cluster into an existing Virtual Private Cloud (VPC). You can configure the proxy during installation by using {cluster-manager-first} or the ROSA CLI (`rosa`).

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-cluster-wide-proxy.adoc

[id="configuring-a-proxy-during-installation-ocm_{context}"]
= Configuring a proxy during installation using {cluster-manager}

[role="_abstract"]
If you are installing
an OpenShift Container Platform
a OpenShift Container Platform
cluster into an existing Virtual Private Cloud (VPC), you can use {cluster-manager-first} to enable a cluster-wide HTTP or HTTPS proxy during installation.
You can enable a proxy only for clusters that use the Customer Cloud Subscription (CCS) model.

Before the installation, you must verify that the proxy is accessible from the VPC that you install the cluster into. The proxy must also be accessible from the private subnets of the VPC.

For detailed steps to configure a cluster-wide proxy during installation by using {cluster-manager}, see _Creating a cluster on AWS_ or _Creating a cluster on {gcp-short}_.

For detailed steps to configure a cluster-wide proxy during installation by using {cluster-manager}, see _Creating a cluster with customizations by using OpenShift Cluster Manager_.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-cluster-wide-proxy.adoc

[id="configuring-a-proxy-during-installation-cli_{context}"]
= Configuring a proxy during installation using the CLI

[role="_abstract"]
If you are installing a OpenShift Container Platform cluster into an existing Virtual Private Cloud (VPC), you can use the ROSA CLI (`rosa`) to enable a cluster-wide HTTP or HTTPS proxy during installation.

The following procedure provides details about the ROSA CLI (`rosa`) arguments that you use to configure a cluster-wide proxy during installation.

For general installation steps using the ROSA CLI, see _Creating a cluster with customizations using the CLI_.

.Prerequisites

* You have verified that the proxy is accessible from the VPC that you install the cluster into. The proxy must also be accessible from the private subnets of the VPC.

.Procedure
* Specify a proxy configuration when you create your cluster:
+
[source,terminal]
----
$ rosa create cluster \
 <other_arguments_here> \
 --additional-trust-bundle-file <path_to_ca_bundle_file> \
 --http-proxy http://<username>:<password>@<ip>:<port> \
 --https-proxy https://<username>:<password>@<ip>:<port> \
 --no-proxy example.com
----
+
--

where:

** The `additional-trust-bundle-file`, `http-proxy`, and `https-proxy` arguments are all optional.
** The `additional-trust-bundle-file` argument is a file path pointing to a bundle of PEM-encoded X.509 certificates, which are all concatenated together. The additional-trust-bundle-file argument is required for users who use a TLS-inspecting proxy unless the identity certificate for the proxy is signed by an authority from the {op-system-first} trust bundle. This applies regardless of whether the proxy is transparent or requires explicit configuration using the http-proxy and https-proxy arguments.
** The `http-proxy` and `https-proxy` arguments must point to a valid URL.
** A comma-separated lis of destination domain names, IP addresses, or network CIDRs to exclude proxying.
+
** Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass proxy for all destinations.
** If you scale up workers that are not included in the network defined by the `networking.machineNetwork[].cidr` field from the installation configuration, you must add them to this list to prevent connection issues.
+
** This field is ignored if neither the `httpProxy` nor `httpsProxy` fields are set.
--

[role="_additional-resources"]
.Additional resources

//Commenting out the following xref because it's breaking the networking and potentially other PRs because it was renamed and the file no longer exists. Pre- or post-publish HCP pruning task.
//ifdef::openshift-rosa-hcp[]
//* Creating a {hcp-title} cluster
//endif::openshift-rosa-hcp[]
* Creating a cluster with customizations by using OpenShift Cluster Manager
* Creating a cluster with customizations using the CLI
* Creating a cluster on AWS
* Creating a cluster on {gcp-short} with Workload Identity Federation authentication

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-cluster-wide-proxy.adoc

[id="configuring-a-proxy-after-installation_{context}"]
= Configuring a proxy after installation

[role="_abstract"]
You can configure an HTTP or HTTPS proxy after you install an OpenShift Container Platform with Customer Cloud Subscription (CCS) cluster into an existing Virtual Private Cloud (VPC). You can configure the proxy after installation by using {cluster-manager-first}.
You can configure an HTTP or HTTPS proxy after you install a OpenShift Container Platform cluster into an existing Virtual Private Cloud (VPC). You can configure the proxy after installation by using {cluster-manager-first} or the ROSA CLI (`rosa`).

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-cluster-wide-proxy.adoc

[id="configuring-a-proxy-after-installation-ocm_{context}"]
= Configuring a proxy after installation using {cluster-manager}

[role="_abstract"]
You can use {cluster-manager-first} to add a cluster-wide proxy configuration to an existing OpenShift Container Platform cluster in a Virtual Private Cloud (VPC).
You can enable a proxy only for clusters that use the Customer Cloud Subscription (CCS) model.

You can also use {cluster-manager} to update an existing cluster-wide proxy configuration. For example, you might need to update the network address for the proxy or replace the additional trust bundle if any of the certificate authorities for the proxy expire.

[IMPORTANT]
====
The cluster applies the proxy configuration to the control plane and compute nodes. While applying the configuration, each cluster node is temporarily placed in an unschedulable state and drained of its workloads. The process restarts each node.
====

.Prerequisites

* You have an OpenShift Container Platform cluster.
* You have an OpenShift Container Platform cluster that uses the Customer Cloud Subscription (CCS) model.
* You deploy your cluster in a VPC.

.Procedure

. Navigate to {cluster-manager-url} and select your cluster.

. Under the *Virtual Private Cloud (VPC)* section on the *Networking* page, click *Edit cluster-wide proxy*.

. On the *Edit cluster-wide proxy* page, give your proxy configuration details:
.. Enter a value in at least one of the following fields:
*** Specify a valid *HTTP proxy URL*.
*** Specify a valid *HTTPS proxy URL*.
*** In the *Additional trust bundle* field, give a Privacy Enhanced Mail (PEM) encoded X.509 certificate bundle.
+
If you are replacing an existing trust bundle file, select *Replace file* to view the field. The system adds the bundle to the trusted certificate store for the cluster nodes. You must use an additional trust bundle file if you use a TLS-inspecting proxy unless an authority from the {op-system-first} trust bundle signs the identity certificate for the proxy. This requirement applies regardless of whether the proxy is transparent or requires explicit configuration by using the `http-proxy` and `https-proxy` arguments.

.. Click *Confirm*.

.Verification

* Under the *Virtual Private Cloud (VPC)* section on the *Networking* page, verify that the proxy configuration for your cluster is as expected.

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-cluster-wide-proxy.adoc

[id="configuring-a-proxy-after-installation-cli_{context}"]
= Configuring a proxy after installation using the CLI

[role="_abstract"]
You can use the ROSA CLI (`rosa`) to add a cluster-wide proxy configuration to an existing ROSA cluster in a Virtual Private Cloud (VPC).

You can also use `rosa` to update an existing cluster-wide proxy configuration. For example, you might need to update the network address for the proxy or replace the additional trust bundle if any of the certificate authorities for the proxy expire.

[IMPORTANT]
====
The cluster applies the proxy configuration to the control plane and compute nodes. While applying the configuration, each cluster node is temporarily placed in an unschedulable state and drained of its workloads. The process restarts each node.
====

.Prerequisites

* You have installed and configured the latest ROSA (`rosa`) and OpenShift (`oc`) command-line interfaces (CLIs) on your installation host.
* You have deployed your OpenShift Container Platform cluster in a VPC.

.Procedure

* Edit the cluster configuration to add or update the cluster-wide proxy details:
+
[source,terminal]
----
$ rosa edit cluster \
 --cluster $CLUSTER_NAME \
 --additional-trust-bundle-file <path_to_ca_bundle_file> \
 --http-proxy http://<username>:<password>@<ip>:<port> \
 --https-proxy https://<username>:<password>@<ip>:<port> \
  --no-proxy example.com
----
+
--

where:

** The `additional-trust-bundle-file`, `http-proxy`, and `https-proxy` arguments are all optional.
** The `additional-trust-bundle-file` argument is a file path pointing to a bundle of PEM-encoded X.509 certificates, which are all concatenated together. The additional-trust-bundle-file argument is a file path pointing to a bundle of PEM-encoded X.509 certificates, which are all concatenated together. The additional-trust-bundle-file argument is required for users who use a TLS-inspecting proxy unless the identity certificate for the proxy is signed by an authority from the {op-system-first} trust bundle. This applies regardless of whether the proxy is transparent or requires explicit configuration using the `http-proxy` and `https-proxy` arguments.
+
[IMPORTANT]
====
Do not attempt to change the proxy or additional trust bundle configuration on the cluster directly. Any changes must be applied by using the ROSA CLI (`rosa`) or {cluster-manager-first}. Any changes made directly to managed resources on the cluster are reverted automatically.
====
** The `http-proxy` and `https-proxy` arguments must point to a valid URL.
** A comma-separated list of destination domain names, IP addresses, or network CIDRs to exclude proxying.
+
** Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass proxy for all destinations.
+
** If you scale up workers that are not included in the network defined by the `networking.machineNetwork[].cidr` field from the installation configuration, you must add them to this list to prevent connection issues.
+
** This field is ignored if neither the `httpProxy` nor `httpsProxy` fields are set.
--

.Verification

. List the status of the machine config pools and verify that they are updated:
+
[source,terminal]
----
$ oc get machineconfigpools
----
+
.Example output
[source,terminal]
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-d9a03f612a432095dcde6dcf44597d90   True      False      False      3              3                   3                     0                      31h
worker   rendered-worker-f6827a4efe21e155c25c21b43c46f65e   True      False      False      6              6                   6                     0                      31h
----

. Display the proxy configuration for your cluster and verify that the details are as expected:
+
[source,terminal]
----
$ oc get proxy cluster -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: config.openshift.io/v1
kind: Proxy
spec:
  httpProxy: http://proxy.host.domain:<port>
  httpsProxy: https://proxy.host.domain:<port>
  <...more...>
status:
  httpProxy: http://proxy.host.domain:<port>
  httpsProxy: https://proxy.host.domain:<port>
  <...more...>
----

// Module included in the following assemblies:
//
// * networking/ovn_kubernetes_network_provider/configuring-cluster-wide-proxy.adoc

[id="removing-cluster-wide-proxy_{context}"]
= Removing a cluster-wide proxy

[role="_abstract"]
You can remove your cluster-wide proxy by using the ROSA CLI. After removing the cluster, you should also remove any trust bundles that you added to the cluster.

// Module included in the following assemblies:
//
// * networking/enable-cluster-wide-proxy.adoc

[id="nw-rosa-proxy-remove-cli_{context}"]
= Removing the cluster-wide proxy using CLI

[role="_abstract"]
You must use the ROSA CLI, `rosa`, to remove the proxy's address from your cluster.

.Prerequisites

* You must have cluster administrator privileges.
* You have installed the ROSA CLI (`rosa`).

.Procedure

* Use the `rosa edit` command to change the proxy. You must pass empty strings to the `--http-proxy` and `--https-proxy` arguments to clear the proxy from the cluster:
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_name> --http-proxy "" --https-proxy ""
----
+
[NOTE]
====
While your proxy might only use one of the proxy arguments, the system ignores the empty fields, so passing empty strings to both the `--http-proxy` and `--https-proxy` arguments does not cause any issues.
====
+
*Example output*
+
[source,yaml]
----
I: Updated cluster <cluster_name>
----

.Verification

* You can verify that you removed the proxy from the cluster by using the `rosa describe` command:
+
[source,yaml]
----
$ rosa describe cluster -c <cluster_name>
----
+
Before removal, the proxy IP displays in a proxy section:
+
[source,yaml,subs="attributes+"]
----
Name:                       <cluster_name>
ID:                         <cluster_internal_id>
External ID:                <cluster_external_id>
OpenShift Version:          .0
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_account_id>
API URL:                    <api_url>
Console URL:                <console_url>
Region:                     us-east-1
Multi-AZ:                   false
Nodes:
 - Control plane:           3
 - Infra:                   2
 - Compute:                 2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             <host_prefix>
Proxy:
 - HTTPProxy:               <proxy_url>
Additional trust bundle:    REDACTED
----
+
After removing the proxy, the proxy section is removed:
+
[source,yaml,subs="attributes+"]
----
Name:                       <cluster_name>
ID:                         <cluster_internal_id>
External ID:                <cluster_external_id>
OpenShift Version:          .0
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_account_id>
API URL:                    <api_url>
Console URL:                <console_url>
Region:                     us-east-1
Multi-AZ:                   false
Nodes:
 - Control plane:           3
 - Infra:                   2
 - Compute:                 2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             <host_prefix>
Additional trust bundle:    REDACTED
----

// Module included in the following assemblies:
//
// * builds/setting-up-trusted-ca

[id="configmap-removing-ca_{context}"]
= Removing certificate authorities on a OpenShift Container Platform cluster

[role="_abstract"]
You can remove certificate authorities (CA) from your cluster with the ROSA CLI, `rosa`.

.Prerequisites

* You must have cluster administrator privileges.
* You have installed the ROSA CLI (`rosa`).
* Your cluster has certificate authorities added.

.Procedure

* Use the `rosa edit` command to change the CA trust bundle. You must pass empty strings to the `--additional-trust-bundle-file` argument to clear the trust bundle from the cluster:
+
[source,terminal]
----
$ rosa edit cluster -c <cluster_name> --additional-trust-bundle-file ""
----
+
*Example output*
+
[source,yaml]
----
I: Updated cluster <cluster_name>
----

.Verification

* To verify that you removed the trust bundle from the cluster, use the `rosa describe` command:
+
[source,yaml]
----
$ rosa describe cluster -c <cluster_name>
----
+
Before removal, the Additional trust bundle section is displayed, redacting its value for security purposes:
+
[source,yaml,subs="attributes+"]
----
Name:                       <cluster_name>
ID:                         <cluster_internal_id>
External ID:                <cluster_external_id>
OpenShift Version:          .0
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_account_id>
API URL:                    <api_url>
Console URL:                <console_url>
Region:                     us-east-1
Multi-AZ:                   false
Nodes:
 - Control plane:           3
 - Infra:                   2
 - Compute:                 2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             <host_prefix>
Proxy:
 - HTTPProxy:               <proxy_url>
Additional trust bundle:    REDACTED
----
+
After you remove the proxy, the Additional trust bundle section no longer displays:
+
[source,yaml,subs="attributes+"]
----
Name:                       <cluster_name>
ID:                         <cluster_internal_id>
External ID:                <cluster_external_id>
OpenShift Version:          .0
Channel Group:              stable
DNS:                        <dns>
AWS Account:                <aws_account_id>
API URL:                    <api_url>
Console URL:                <console_url>
Region:                     us-east-1
Multi-AZ:                   false
Nodes:
 - Control plane:           3
 - Infra:                   2
 - Compute:                 2
Network:
 - Type:                    OVNKubernetes
 - Service CIDR:            <service_cidr>
 - Machine CIDR:            <machine_cidr>
 - Pod CIDR:                <pod_cidr>
 - Host Prefix:             <host_prefix>
Proxy:
 - HTTPProxy:               <proxy_url>
----
