---
title: "Node access with kubeconfig files"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-node-access-kubeconfig
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-node-access-kubeconfig
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Node access with kubeconfig files

[id="microshift-node-access-kubeconfig"]
= Node access with kubeconfig files

[role="_abstract"]
`Kubeconfig` files supply node details, IP addresses, and authentication so that CLI tools can communicate with the API server of a node. You can use them for local access, remote access, generating additional files, and opening firewall access when needed.

// Module included in the following assemblies:
//
// * microshift/microshift_configuring/microshift-node-access-kubeconfig.adoc

[id="kubeconfig-files-overview_{context}"]
= Kubeconfig files for configuring node access

[role="_abstract"]
The two categories of `kubeconfig` files used in {microshift-short} are local access and remote access. Each time {microshift-short} starts, it generates a set of `kubeconfig` files for accessing the API server. These files are created in the `/var/lib/microshift/resources/kubeadmin/` directory by using existing configuration information.

Each access type requires a different authentication certificate signed by different Certificate Authorities (CAs). The generation of multiple `kubeconfig` files accommodates this need.

You can use the appropriate `kubeconfig` file for the access type needed in each case to provide authentication details. The contents of {microshift-short} `kubeconfig` files are determined by either default built-in values or a `config.yaml` file.

[NOTE]
====
A `kubeconfig` file must exist for the cluster to be accessible. The values are applied from built-in default values or a customized `config.yaml` file.
====

.Example contents of the kubeconfig files
[source,terminal]
----
/var/lib/microshift/resources/kubeadmin/
├── kubeconfig
├── alt-name-1
│   └── kubeconfig
├── 1.2.3.4
│   └── kubeconfig
└── microshift-rhel9
    └── kubeconfig
----

where:

`kubeconfig`:: Specifies the local hostname. The main IP address of the host is always the default.
`alt-name-1`:: Specifies the subject alternative name for the API server certificate.
`1.2.3.4`:: Specifies the DNS name.
`microshift-rhel9`:: Specifies the {microshift-short} hostname.

// Module included in the following assemblies:
//
// * microshift/microshift_configuring/microshift-node-access-kubeconfig.adoc

[id="microshift-kubeconfig-local-access_{context}"]
= Local access kubeconfig file

[role="_abstract"]
The local access `kubeconfig` file in OpenShift Container Platform is written to `/var/lib/microshift/resources/kubeadmin/kubeconfig`. This `kubeconfig` file provides access to the API server by using `localhost`. Use this file when you connect to the node locally.

.Example contents of `kubeconfig` for local access
[source,yaml]
----
clusters:
- cluster:
    certificate-authority-data: <base64_encoded_CA>
    server: https://localhost:6443
----

The `localhost` `kubeconfig` file can only be used from a client connecting to the API server from the same host. The certificates in the file do not work for remote connections.

// Module included in the following assemblies:
//
// microshift_install_rpm/microshift-install-rpm.adoc
// microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree.adoc
// microshift_configuring/microshift-node-access-kubeconfig.adoc

[id="accessing-microshift-node-locally_{context}"]
= Accessing the {microshift-short} node locally

[role="_abstract"]
Use the following procedure to access the {microshift-short} node locally by using a `kubeconfig` file.

.Prerequisites

* You installed the {oc-first}.

.Procedure

. Optional: to create a `~/.kube/` folder if your {op-system-base-full} machine does not have one, run the following command:
+
[source,terminal]
----
$ mkdir -p ~/.kube/
----

. Copy the generated local access `kubeconfig` file to the `~/.kube/` directory by running the following command:
+
[source,terminal]
----
$ sudo cat /var/lib/microshift/resources/kubeadmin/kubeconfig > ~/.kube/config
----

. Update the permissions on your `~/.kube/config` file by running the following command:
+
[source,terminal]
----
$ chmod go-r ~/.kube/config
----

.Verification

* Verify that {microshift-short} is running by entering the following command:
+
--
--

// Module included in the following assemblies:
//
// * microshift/microshift_configuring/microshift-node-access-kubeconfig.adoc

[id="remote-access-con_{context}"]
= Remote access kubeconfig files

[role="_abstract"]
{microshift-short} generates a default `kubeconfig` file that enables external clients to connect securely to the API server. The configuration uses the node hostname and certificate validation based on Subject Alternative Name (SAN) entries.

When a {microshift-short} node connects to the API server from an external source, a certificate with all alternative names listed in the SAN field is used for validation. {microshift-short} generates a default `kubeconfig` for external access by using the hostname value. The defaults are set in the `<node.hostnameOverride>`, `<node.nodeIP>`, and `api.<dns.baseDomain>` parameter values of the default `kubeconfig` file.

The `/var/lib/microshift/resources/kubeadmin/<hostname>/kubeconfig` file uses the hostname of the machine, or `node.hostnameOverride` if that option is set, to reach the API server. The CA in the `kubeconfig` file can validate certificates when the API server is accessed externally.

.Example contents of a default `kubeconfig` file for remote access
[source,yaml]
----
clusters:
- cluster:
    certificate-authority-data: <base64 CA>
    server: https://microshift-rhel9:6443
----

//line space was not showing on PV1 preview, so added extra blank line
[id="remote-access-customization_{context}"]
== Remote access customization

Multiple remote access `kubeconfig` file values can be generated for accessing the node with different IP addresses or host names. An additional `kubeconfig` file generates for each entry in the `apiServer.subjectAltNames` parameter. You can copy remote access `kubeconfig` files from the host during times of IP connectivity and then use them to access the API server from other workstations.

// Module included in the following assemblies:
//
// * microshift/microshift_configuring/microshift-node-access-kubeconfig.adoc

[id="microshift-kubeconfig-generating-additional-files_{context}"]
= Generating additional kubeconfig files for remote access

[role="_abstract"]
To support more host names or IP addresses for remote access than the default file provides, you can generate additional `kubeconfig` files in {microshift-short}. Add the entries to `apiServer.subjectAltNames` in `config.yaml` and restart the service to create the files.

[IMPORTANT]
====
You must restart {microshift-short} for configuration changes to be implemented.
====

.Prerequisites

* You have created a `config.yaml` file for {microshift-short}.

.Procedure

. Optional: You can show the contents of the `config.yaml`. Run the following command:
+
[source,terminal]
----
$ cat /etc/microshift/config.yaml
----

. Optional: You can show the contents of the remote-access `kubeconfig` file. Run the following command:
+
[source,terminal]
----
$ cat /var/lib/microshift/resources/kubeadmin/<hostname>/kubeconfig
----
+
[IMPORTANT]
====
Additional remote access `kubeconfig` files must include one of the server names listed in the OpenShift Container Platform `config.yaml` file. Additional `kubeconfig` files must also use the same CA for validation.
====

. To generate additional `kubeconfig` files for additional DNS names SANs or external IP addresses, add the entries you need to the `apiServer.subjectAltNames` field. In the following example, the DNS name used is `alt-name-1` and the IP address is `1.2.3.4`.
+
.Example `config.yaml` with additional authentication values
[source,yaml]
----
dns:
  baseDomain: example.com
node:
  hostnameOverride: "microshift-rhel9"
  nodeIP: 10.0.0.1
apiServer:
  subjectAltNames:
  - alt-name-1
  - 1.2.3.4
----
+
where:

`microshift-rhel9`:: Specifies the hostname of the node.
`alt-name-1`:: Specifies the DNS name.
`1.2.3.4`:: Specifies the IP address or range.

. Restart {microshift-short} to apply configuration changes and auto-generate the `kubeconfig` files you need by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

. To check the contents of additional remote-access `kubeconfig` files, insert the name or IP address as listed in the `config.yaml` into the `cat` command. For example, `alt-name-1` is used in the following example command:
+
[source,terminal]
----
$ cat /var/lib/microshift/resources/kubeadmin/alt-name-1/kubeconfig
----

. Choose the `kubeconfig` file to use that contains the SAN or IP address you want to use to connect your node. In this example, the `kubeconfig` containing `alt-name-1` in the `clusters.cluster.server` field is the correct file.
+
.Example contents of an additional `kubeconfig` file
[source,yaml]
----
clusters:
- cluster:
    certificate-authority-data: <base64 CA>
    server: https://alt-name-1:6443
----
+
** The `/var/lib/microshift/resources/kubeadmin/alt-name-1/kubeconfig` file values are from the `apiServer.subjectAltNames` configuration values.
+
[NOTE]
====
All parameters are included as common names (CN) and subject alternative names (SAN) in the external serving certificates for the API server.
====

// Module included in the following assemblies:
//
// microshift_install_rpm/microshift-install-rpm.adoc
// microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree.adoc
// microshift_configuring/microshift-node-access-kubeconfig.adoc

[id="microshift-accessing-node-open-firewall_{context}"]
= Opening the firewall for remote access to the {microshift-short} node

[role="_abstract"]
You must open the firewall before a workstation user can access the {microshift-short} node remotely.

For this procedure, `user@microshift` is the user on the {microshift-short} host machine and is responsible for setting up that machine so that it can be accessed by a remote user on a separate workstation.

.Prerequisites

* You installed the {oc-first}.
* Your account has cluster administration privileges.

.Procedure

* As `user@microshift` on the {microshift-short} host, open the firewall port for the Kubernetes API server (`6443/tcp`) by running the following command:
+
[source,terminal]
----
[user@microshift]$ sudo firewall-cmd --permanent --zone=public --add-port=6443/tcp && sudo firewall-cmd --reload
----

.Verification

* As `user@microshift`, verify that {microshift-short} is running by entering the following command:
+
--
--

// Module included in the following assemblies:
//
// microshift_install_rpm/microshift-install-rpm.adoc
// microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree.adoc
// microshift_configuring/microshift-access-node-kubeconfig.adoc

[id="accessing-microshift-node-remotely_{context}"]
= Accessing the {microshift-short} node remotely

[role="_abstract"]
Access the {microshift-short} service from a remote location by using a `kubeconfig` file.

The `user@workstation` login is used to access the host machine remotely. The `<user>` value in the procedure is the name of the user that `user@workstation` logs in with to the {microshift-short} host.

.Prerequisites

* You installed the {oc-first}.
* The `user@microshift` has opened the firewall from the local host.
* You generated additional `kubeconfig` files.

.Procedure

. As `user@workstation`, create a `~/.kube/` folder if your {op-system-base-full} machine does not have one by running the following command:
+
[source,terminal]
----
[user@workstation]$ mkdir -p ~/.kube/
----

. As `user@workstation`, set a variable for the hostname of your {microshift-short} host by running the following command:
+
[source,terminal,subs="+quotes"]
----
[user@workstation]$ MICROSHIFT_MACHINE=_<microshift_hostname>_
----
+
Replace the value, _<{microshift-short}_hostname>_, with the either the name or the IP address of the host running {microshift}.

. As `user@workstation`, copy the generated `kubeconfig` file that has the hostname or IP address you want to connect to from the {op-system-base} machine running {microshift-short} to your local machine by running the following command:
+
[source,terminal,subs="+quotes"]
----
[user@workstation]$ ssh _<user>_@$MICROSHIFT_MACHINE "sudo cat /var/lib/microshift/resources/kubeadmin/$MICROSHIFT_MACHINE/kubeconfig" > ~/.kube/config #
----
+
Replace _<user>_ with your SSH login credentials.

. As `user@workstation`, update the permissions on your `~/.kube/config` file by running the following command:
+
[source,terminal]
----
$ chmod go-r ~/.kube/config
----

.Verification

* As `user@workstation`, verify that {microshift-short} is running by entering the following command:
+
--
--
