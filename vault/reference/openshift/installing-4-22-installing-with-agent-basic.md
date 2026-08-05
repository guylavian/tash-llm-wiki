---
title: "Installing a cluster"
type: reference
domain: openshift
slug: installing-4-22-installing-with-agent-basic
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-with-agent-basic
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster

[id="installing-with-agent-basic"]
= Installing a cluster

[role="_abstract"]
You can install a basic OpenShift Container Platform cluster using the Agent-based Installer.

The following procedures deploy a single-node OpenShift Container Platform in a disconnected environment. You can use these procedures as a basis and modify according to your requirements.

For procedures that include optional customizations you can make while using the Agent-based Installer, see "Installing a cluster with customizations".

[id="prerequisites_{context}"]
= Prerequisites for installing a cluster with the Agent-based Installer

[role="_abstract"]
Before beginning your cluster installation, you must complete prerequisite tasks that prepare your environment.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".
* You read "Selecting a cluster installation method and preparing it for users".
* If you use a firewall or proxy, you configured it to allow the sites that your cluster requires access to. For more information, see "Configuring your firewall".

[id="prerequisites_{context}"]
= Prerequisites for preparing PXE assets

[role="_abstract"]
Before beginning to prepare PXE assets, you must complete prerequisite tasks.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".

[role="_additional-resources"]
.Additional resources

* OpenShift Container Platform installation and update
* Selecting a cluster installation method and preparing it for users
* Configuring your firewall

// Downloading the Agent-based Installer
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/prepare-pxe-infra-agent.adoc
// * installing/installing_with_agent_based_installer/installing-using-iscsi.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-retrieve_{context}"]
= Downloading the Agent-based Installer

[role="_abstract"]
Begin the installation process by downloading the Agent-based Installer and the CLI needed for your installation.

.Procedure

. Log in to the {hybrid-console} using your login credentials.

. Navigate to Datacenter.

. Click *Run Agent-based Installer locally*.

. Select the operating system and architecture for the *OpenShift Installer* and *Command line interface*.

. Click *Download Installer* to download and extract the install program.

. Download or copy the pull secret by clicking on *Download pull secret* or *Copy pull secret*.

. Click *Download command-line tools* and place the `openshift-install` binary in a directory that is on your `PATH`.

// Creating the configuration inputs
// Module included in the following assemblies:
//
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-basic-inputs_{context}"]
= Creating the configuration inputs

[role="_abstract"]
Create the configuration files that are used by the installation program to generate the agent image.

.Procedure

. Place the `openshift-install` binary in a directory that is on your PATH.

. Create a directory to store the install configuration by running the following command:
+
[source,terminal]
----
$ mkdir ~/<directory_name>
----

. Create the `install-config.yaml` file by running the following command:
+
--
[source,terminal]
----
$ cat << EOF > ./my-cluster/install-config.yaml
apiVersion: v1
baseDomain: test.example.com
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  replicas: 0
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  replicas: 1
metadata:
  name: sno-cluster
networking:
  clusterNetwork:
  - cidr: fd01::/48
    hostPrefix: 64
  machineNetwork:
  - cidr: fd2e:6f44:5dd8:c956::/120
  networkType: OVNKubernetes
  serviceNetwork:
  - fd02::/112
platform:
  none: {}
pullSecret: '<pull_secret>'
sshKey: '<ssh_pub_key>'
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
EOF
----

where:

`compute.architecture`:: Specifies the system architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.
+
If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command. For more information, see "Verifying the supported architecture for installing an Agent-based Installer cluster".

`metadata.name`:: Specifies your cluster name. This value is required.

`networking.networkingType`:: Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`platform`:: Specifies your platform.
+
[NOTE]
====
For bare metal platforms, host settings made in the platform section of the `install-config.yaml` file are used by default, unless they are overridden by configurations made in the `agent-config.yaml` file.
====
`pullSecret`:: Specifies your pull secret.

`sshKey`:: Specifies your SSH public key.

`additionalTrustBundle`:: Specifies the contents of the certificate file that you used for your mirror registry.
The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry.
You must specify this parameter if you are using a disconnected mirror registry.

`imageContentSources`:: Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository.
You must specify this parameter if you are using a disconnected mirror registry.
+
[IMPORTANT]
====
* When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
* When using the `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
* The `ImageContentSourcePolicy` resource is deprecated.
====
--

. Create the `agent-config.yaml` file by running the following command:
+
[source,terminal]
----
$ cat > agent-config.yaml << EOF
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: sno-cluster
rendezvousIP: fd2e:6f44:5dd8:c956::50
EOF
----
+
where:

`rendezvousIP`:: Specifies the IP address used to determine which node performs the bootstrapping process as well as running the `assisted-service` component.
You must provide the rendezvous IP address when you do not specify at least one host IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided host `networkConfig` parameter.

// Creating and booting the agent image
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-boot_{context}"]
= Creating and booting the agent image

[role="_abstract"]
After you have prepared the configuration inputs for your installation, create the ISO image and boot it on your machines.

.Prerequisites

* If you plan to boot the agent image from a USB drive, you have installed the `syslinux` package.

.Procedure

. Create the agent image by running the following command:
+
[source,terminal]
----
$ openshift-install --dir <install_directory> agent create image
----
+
[NOTE]
====
{op-system-first} supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the agent ISO image, with a default `/etc/multipath.conf` configuration.
====

. If you plan to boot the ISO image from a USB drive, add a master boot record to the image by running the following command:
+
[source,terminal]
----
$ isohybrid --uefi <agent_iso_image>
----
+
.Example command
[source,terminal]
----
$ isohybrid --uefi agent.x86_64.iso
----

. Boot the `agent.x86_64.iso`, `agent.aarch64.iso`, or `agent.s390x.iso` image on the bare-metal machines.

// Verifying that the current installation host can pull release images
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-tui_{context}"]
= Verifying that the current installation host can pull release images

[role="_abstract"]
After you boot the agent image and network services are made available to the host, the agent console application performs a pull check to verify that the current host can retrieve release images.

If the primary pull check passes, you can quit the application to continue with the installation. If the pull check fails, the application performs additional checks, as seen in the `Additional checks` section of the TUI, to help you troubleshoot the problem. A failure for any of the additional checks is not necessarily critical as long as the primary pull check succeeds.

If there are host network configuration issues that might cause an installation to fail, you can use the console application to make adjustments to your network configurations.

[IMPORTANT]
====
If the agent console application detects host network configuration issues, the installation workflow will be halted until the user manually stops the console application and signals the intention to proceed.
====

.Procedure

. Wait for the agent console application to check whether or not the configured release image can be pulled from a registry.

. If the agent console application states that the installer connectivity checks have passed, wait for the prompt to time out to continue with the installation.
+
[NOTE]
====
You can still choose to view or change network configuration settings even if the connectivity checks have passed.

However, if you choose to interact with the agent console application rather than letting it time out, you must manually quit the TUI to proceed with the installation.
====

. If the agent console application checks have failed, which is indicated by a red icon beside the `Release image URL` pull check, use the following steps to reconfigure the host's network settings:

.. Read the `Check Errors` section of the TUI.
This section displays error messages specific to the failed checks.
+
image::agent-tui-home.png[The home screen of the agent console application  displaying check errors, indicating a failed check]

.. Select *Configure network* to launch the NetworkManager TUI.

.. Select *Edit a connection* and select the connection you want to reconfigure.

.. Edit the configuration and select *OK* to save your changes.

.. Select *Back* to return to the main screen of the NetworkManager TUI.

.. Select *Activate a Connection*.

.. Select the reconfigured network to deactivate it.

.. Select the reconfigured network again to reactivate it.

.. Select *Back* and then select *Quit* to return to the agent console application.

.. Wait at least five seconds for the continuous network checks to restart using the new network configuration.

.. If the `Release image URL` pull check succeeds and displays a green icon beside the URL, select *Quit* to exit the agent console application and continue with the installation.

// Tracking and verifying installation progress
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-verify_{context}"]
= Tracking and verifying installation progress

[role=_abstract]
After the installation has started, you can track installation progress and verify a successful installation.

.Prerequisites

* You have configured a DNS record for the Kubernetes API server.

.Procedure

. Optional: To know when the bootstrap host (rendezvous host) reboots, run the following command:
+
--
[source,terminal]
----
$ ./openshift-install --dir <install_directory> agent wait-for bootstrap-complete \
    --log-level=info
----

where:

`--dir`:: specifies the path to the directory where the agent ISO was generated.

`--log-level`:: Specifies the level of installation details. Valid values are `info`, `warn`, `debug`, and `error`.
--
+
.Example output
[source,terminal]
----
...................................................................
...................................................................
INFO Bootstrap configMap status is complete
INFO cluster bootstrap is complete
----
+
The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines.

. Track the progress and verify successful installation by running the following command:
+
[source,terminal]
----
$ openshift-install --dir <install_directory> agent wait-for install-complete <1>
----
+
Replace `<install_directory>` with the path to the directory where the agent ISO was generated.
+
.Example output
[source,terminal]
----
...................................................................
...................................................................
INFO Cluster is installed
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run
INFO     export KUBECONFIG=/home/core/installer/auth/kubeconfig
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.sno-cluster.test.example.com
----

+
[NOTE]
====
If you are using the optional method of {ztp} manifests, you can configure IP address endpoints for cluster nodes through the `AgentClusterInstall.yaml` file in three ways:

* IPv4
* IPv6
* IPv4 and IPv6 in parallel (dual-stack)

IPv6 is supported only on bare metal platforms.
====
+
.Example of dual-stack networking
[source,yaml,subs="attributes+"]
----
apiVIP: 192.168.11.3
ingressVIP: 192.168.11.4
clusterDeploymentRef:
  name: mycluster
imageSetRef:
  name: openshift-
networking:
  clusterNetwork:
  - cidr: 172.21.0.0/16
    hostPrefix: 23
  - cidr: fd02::/48
    hostPrefix: 64
  machineNetwork:
  - cidr: 192.168.11.0/16
  - cidr: 2001:DB8::/32
  serviceNetwork:
  - 172.22.0.0/16
  - fd03::/112
  networkType: OVNKubernetes
----

// Gathering log data from a failed Agent-based installation
// Module included in the following assemblies:
//
// * installing/installing-with-agent-based-installer/installing-with-agent-based-installer.adoc
// * installing/installing_with_agent_based_installer/installing-with-agent-basic.adoc

[id="installing-ocp-agent-gather-log_{context}"]
= Gathering log data from a failed Agent-based installation

[role="_abstract"]
If you encounter a failed Agent-based installation, you can gather log data to provide for a support case.

.Prerequisites

* You have configured a DNS record for the Kubernetes API server.

.Procedure

. Run the following command and collect the output:
+
[source,terminal]
----
$ ./openshift-install --dir <installation_directory> agent wait-for bootstrap-complete --log-level=debug
----
+
.Example error message
[source,terminal]
----
...
ERROR Bootstrap failed to complete: : bootstrap process timed out: context deadline exceeded
----

. If the output from the previous command indicates a failure, or if the bootstrap is not progressing, run the following command to connect to the rendezvous host and collect the output:
+
[source,terminal]
----
$ ssh core@<node-ip> agent-gather -O >agent-gather.tar.xz
----
+
[NOTE]
====
Red{nbsp}Hat Support can diagnose most issues using the data gathered from the rendezvous host, but if some hosts are not able to register, gathering this data from every host might be helpful.
====

. If the bootstrap completes and the cluster nodes reboot, run the following command and collect the output:
+
[source,terminal]
----
$ ./openshift-install --dir <install_directory> agent wait-for install-complete --log-level=debug
----

. If the output from the previous command indicates a failure, perform the following steps:

.. Export the `kubeconfig` file to your environment by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<install_directory>/auth/kubeconfig
----

.. Gather information for debugging by running the following command:
+
[source,terminal]
----
$ oc adm must-gather
----

.. Create a compressed file from the `must-gather` directory that was just created in your working directory by running the following command:
+
[source,terminal]
----
$ tar cvaf must-gather.tar.gz <must_gather_directory>
----

. Excluding the `/auth` subdirectory, attach the installation directory used during the deployment to your support case on the Red{nbsp}Hat Customer Portal.

. Attach all other data gathered from this procedure to your support case.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Installing a cluster with customizations
