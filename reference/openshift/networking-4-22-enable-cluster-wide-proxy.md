---
title: "Configuring the cluster-wide proxy"
type: reference
domain: openshift
slug: networking-4-22-enable-cluster-wide-proxy
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/networking/enable-cluster-wide-proxy
version: 4.22
family: networking
documentKind: "Documentation"
---

# Configuring the cluster-wide proxy

[id="enable-cluster-wide-proxy"]
= Configuring the cluster-wide proxy

[role="_abstract"]
To enable your OpenShift Container Platform cluster to use an HTTP or HTTPS proxy when direct internet access is denied, you can configure cluster-wide proxy settings by modifying the `Proxy` object for existing clusters or by configuring proxy settings in the `install-config.yaml` file for new clusters.

After you enable a cluster-wide egress proxy for your cluster on a supported platform, {op-system-first} populates the `status.noProxy` parameter with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your `install-config.yaml` file that exists on the supported platform.

[NOTE]
====
As a postinstallation task, you can change the `networking.clusterNetwork[].cidr` value, but not the `networking.machineNetwork[].cidr` and the `networking.serviceNetwork[]` values. For more information, see "Configuring the cluster network range".
====

For installations on {aws-first}, {gcp-first}, {azure-first}, and {rh-openstack-first}, the `status.noProxy` parameter is also populated with the instance metadata endpoint, `169.254.169.254`.

.Example of values added to the `status:` segment of a `Proxy` object by {op-system}
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
# ...
networking:
  clusterNetwork:
  - cidr: <ip_address_from_cidr>
    hostPrefix: 23
  network type: OVNKubernetes
  machineNetwork:
  - cidr: <ip_address_from_cidr>
  serviceNetwork:
  - 172.30.0.0/16
# ...
status:
  noProxy:
  - localhost
  - .cluster.local
  - .svc
  - 127.0.0.1
  - <api_server_internal_url>
# ...
----

where:

--
`<ip_address_from_cidr>`:: Specifies IP address blocks from which pod IP addresses are allocated. The default value is `10.128.0.0/14` with a host prefix of `/23`.
`<ip_address_from_cidr>`:: Specifies IP address blocks for machines. The default value is `10.0.0.0/16`.
`<ip_address_from_cidr>`:: Specifies IP address block for services. The default value is `172.30.0.0/16`.
`<api_server_internal_url>`:: You can find the URL of the internal API server by running the `oc get infrastructures.config.openshift.io cluster -o jsonpath='{.status.etcdDiscoveryDomain}'` command.
--

[IMPORTANT]
====
If node IP addresses fall outside the specified `networking.machineNetwork[].cidr` range, you must add the IP addresses to the `noProxy` field. This configuration ensures that traffic between nodes can bypass the proxy.
====

[id="prerequisites_cluster-wide-proxy"]
== Prerequisites

Review the sites that your cluster requires access to and determine whether any of them must bypass the proxy. By default, all cluster system egress traffic is proxied, including calls to the cloud provider API for the cloud that hosts your cluster. The system-wide proxy affects system components only, not user workloads. If necessary, add sites to the `spec.noProxy` parameter of the `Proxy` object to bypass the proxy.

// Enabling the cluster-wide proxy
// Module included in the following assemblies:
//
// * networking/configuring-a-custom-pki.adoc
// * networking/enable-cluster-wide-proxy.adoc

[id="nw-proxy-configure-object_{context}"]
= Enabling the cluster-wide proxy

[role="_abstract"]
To enable the cluster-wide egress proxy for your OpenShift Container Platform cluster, you can modify the `Proxy` object to configure HTTP and HTTPS proxy settings and specify domains that bypass the proxy.

When a cluster is installed or upgraded without the proxy configured, a `Proxy` object is still generated but it has a nil `spec`. For example:

[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
spec:
  trustedCA:
    name: ""
status:
----

[NOTE]
====
Only the `Proxy` object named `cluster` is supported, and no additional proxies can be created.
====

A cluster administrator can configure the proxy for OpenShift Container Platform by modifying the `cluster` `Proxy` object.

[WARNING]
====
After you enable the cluster-wide proxy capability for your cluster and you save the `Proxy` object file, the Machine Config Operator (MCO) reboots all nodes in your cluster so that each node can access connections that exist outside of the cluster. You do not need to manually reboot these nodes.
====

.Prerequisites

* You have cluster administrator permissions.
* You installed the OpenShift Container Platform `oc` CLI tool.

.Procedure

. Create a config map that contains any additional CA certificates required for proxying HTTPS connections.
+
[NOTE]
====
You can skip this step if the identity certificate of the proxy is signed by an authority from the {op-system-first} trust bundle.
====
+
.. Create a file called `user-ca-bundle.yaml`, and provide the values of your PEM-encoded certificates:
+
[source,yaml]
----
apiVersion: v1
data:
  ca-bundle.crt: | <1>
    <MY_PEM_ENCODED_CERTS> <2>
kind: ConfigMap
metadata:
  name: user-ca-bundle <3>
  namespace: openshift-config <4>
----
+
where:
+
--
`data.ca-bundle.crt`:: Specifies the data key that must be named `ca-bundle.crt`.
`<MY_PEM_ENCODED_CERTS>`:: Specifies one or more PEM-encoded X.509 certificates used to sign the proxy's identity certificate.
`user-ca-bundle`:: Specifies the config map name that is referenced from the `Proxy` object.
`openshift-config`:: Specifies the namespace that the config map must exist in.
--

.. Create the config map from the `user-ca-bundle.yaml` file by entering the following command:
+
[source,terminal]
----
$ oc create -f user-ca-bundle.yaml
----

. Use the `oc edit` command to modify the `Proxy` object:
+
[source,terminal]
----
$ oc edit proxy/cluster
----

. Configure the necessary fields for the proxy:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
spec:
  httpProxy: http://<username>:<pswd>@<ip>:<port> <1>
  httpsProxy: https://<username>:<pswd>@<ip>:<port> <2>
  noProxy: example.com <3>
  readinessEndpoints:
  - http://www.google.com <4>
  - https://www.google.com
  trustedCA:
    name: user-ca-bundle <5>
----
+
where:
+
--
`httpProxy`:: Specifies the proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.

`httpsProxy`:: Specifies the proxy URL to use for creating HTTPS connections outside the cluster. The URL scheme must be either `http` or `https`. Specify a URL for the proxy that supports the URL scheme. For example, most proxies report an error if they are configured to use `https` but they only support `http`. This failure message may not propagate to the logs and can appear to be a network connection failure instead. If using a proxy that listens for `https` connections from the cluster, you might need to configure the cluster to accept the CAs and certificates that the proxy uses.

`noProxy`:: Specifies a comma-separated list of destination domain names, domains, IP addresses (or other network CIDRs), and port numbers to exclude proxying. Note that Port numbers are only supported when configuring IPv6 addresses. Port numbers are not supported when configuring IPv4 addresses.
+
Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass proxy for all destinations.
+
If your `noproxy` field needs to include a domain address, you must explicitly specify that FQDN, or prefix-matched subdomain, in the `noproxy` field. You cannot use the IP address or CIDR range that encapsulates the domain. This is because the cluster does not wait for DNS to return the IP address before assigning the route connection, and checks explicitly against the request being made.
For example, if you have a CIDR block value, such as `10.0.0.0/24`, for the `noproxy` field and the field attempts to access `\https://10.0.0.11`, the addresses successfully match. However, attempting to access `\https://exampleserver.externaldomain.com`, whose A record entry is `10.0.0.11`, fails. An additional value of `.externaldomain.com` for your `noproxy` field is necessary.
+
If you scale up compute nodes that are not included in the network defined by the `networking.machineNetwork[].cidr` field from the installation configuration, you must add them to this list to prevent connection issues.
+
This field is ignored if neither the `httpProxy` or `httpsProxy` fields are set.

`readinessEndpoints`:: Specifies one or more URLs external to the cluster to use to perform a readiness check before writing the `httpProxy` and `httpsProxy` values to status.

`trustedCA`:: Specifies a reference to the config map in the `openshift-config` namespace that contains additional CA certificates required for proxying HTTPS connections. Note that the config map must already exist before referencing it here. This field is required unless the proxy's identity certificate is signed by an authority from the {op-system} trust bundle.
--

. Save the file to apply the changes.

// Removing the cluster-wide proxy
// Module included in the following assemblies:
//
// * networking/enable-cluster-wide-proxy.adoc

[id="nw-proxy-remove_{context}"]
= Removing the cluster-wide proxy

[role="_abstract"]
The `cluster` Proxy object cannot be deleted. To remove the cluster-wide proxy configuration from your OpenShift Container Platform cluster, you can remove all spec fields from the `Proxy` object by using the `oc edit` command.

.Prerequisites

* Cluster administrator permissions
* OpenShift Container Platform `oc` CLI tool installed

.Procedure

. Use the `oc edit` command to modify the proxy:
+
[source,terminal]
----
$ oc edit proxy/cluster
----

. Remove all `spec` fields from the Proxy object. For example:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
spec: {}
----

. Save the file to apply the changes.

// Verifying the cluster-wide proxy configuration
// Module included in the following assemblies:
//
// * networking/configuring-a-custom-pki.adoc
// * networking/enable-cluster-wide-proxy.adoc

[id="nw-verify-proxy-configuration_{context}"]
= Verifying the cluster-wide proxy configuration

[role="_abstract"]
To verify that your cluster-wide proxy configuration is working correctly in OpenShift Container Platform, you can check the `Proxy` object status, review Machine Config Operator logs, and confirm that system components are routing external requests through the proxy.

.Prerequisites

* You have cluster administrator permissions.
* You have the OpenShift Container Platform `oc` CLI tool installed.

.Procedure

. Check the proxy configuration status using the `oc` command:
+
[source,terminal]
----
$ oc get proxy/cluster -o yaml
----

. Verify the proxy fields in the output to ensure they match your configuration. Specifically, check the `spec.httpProxy`, `spec.httpsProxy`, `spec.noProxy`, and `spec.trustedCA` fields.

. Inspect the status of the `Proxy` object:
+
[source,terminal]
----
$ oc get proxy/cluster -o jsonpath='{.status}'
----
+
.Example output
[source,terminal]
----
{
status:
    httpProxy: http://user:xxx@xxxx:3128
    httpsProxy: http://user:xxx@xxxx:3128
    noProxy: .cluster.local,.svc,10.0.0.0/16,10.128.0.0/14,127.0.0.1,169.254.169.254,172.30.0.0/16,localhost,test.no-proxy.com
}
----

. Check the logs of the Machine Config Operator (MCO) to ensure that the configuration changes were applied successfully:
+
[source,terminal]
----
$ oc logs -n openshift-machine-config-operator $(oc get pods -n openshift-machine-config-operator -l k8s-app=machine-config-operator -o name)
----

. Look for messages that indicate the proxy settings were applied and the nodes were rebooted if necessary.

. Verify that system components are using the proxy by checking the logs of a component that makes external requests, such as the Cluster Version Operator (CVO):
+
[source,terminal]
----
$ oc logs -n openshift-cluster-version $(oc get pods -n openshift-cluster-version -l k8s-app=machine-config-operator -o name)
----

. Look for log entries that show that external requests have been routed through the proxy.

[role="_additional-resources"]
== Additional resources

* Configuring the cluster network range
* Understanding the CA Bundle certificate
* Proxy certificates
* How is the cluster-wide proxy setting applied to OpenShift Container Platform nodes?
