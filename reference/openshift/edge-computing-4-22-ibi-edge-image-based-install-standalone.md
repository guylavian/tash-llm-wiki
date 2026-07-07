---
title: "About image-based deployments for {sno}"
type: reference
domain: openshift
slug: edge-computing-4-22-ibi-edge-image-based-install-standalone
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ibi-edge-image-based-install-standalone
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# About image-based deployments for {sno}

[id="ibi-image-based-install-standalone"]
= About image-based deployments for {sno}

You can manually generate a configuration ISO by using the `openshift-install` program. Attach the configuration ISO to your preinstalled target host to complete the deployment.

// Module included in the following assemblies:
//
// * edge_computing/ibi-edge-image-based-install.adoc

[id="create-standalone-config-iso_{context}"]
= Deploying a {sno} cluster using the openshift-install program

[role="_abstract"]
You can use the `openshift-install` program to configure and deploy a host that you preinstalled with an image-based installation. To configure the target host with site-specific details, you must create the following resources:

* The `install-config.yaml` installation manifest
* The `image-based-config.yaml` manifest

The `openshift-install` program uses these resources to generate a configuration ISO that you attach to the preinstalled target host to complete the deployment.

[NOTE]
====
For more information about the specifications for the `image-based-config.yaml` manifest, see "Reference specifications for the image-based-config.yaml manifest".
====

.Prerequisites

* You preinstalled a host with {sno} using an image-based installation.
* You downloaded the latest version of the `openshift-install` program.
* You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets".

.Procedure

. Create a working directory by running the following:
+
[source,terminal]
----
$ mkdir <working_directory>
----
+
where `<working_directory>` is the name of your working directory, for example `ibi-config-iso-workdir`.

. Create the installation manifest:

.. Create a YAML file that defines the `install-config` manifest, as in the following example:
+
--
[source,yaml]
----
apiVersion: v1
metadata:
  name: sno-cluster-name
baseDomain: host.example.com
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
networking:
  machineNetwork:
  - cidr: 192.168.200.0/24
  #- cidr: fd01::/64
platform:
  none: {}
fips: false
cpuPartitioningMode: "AllNodes"
pullSecret: '{"auths":{"<your_pull_secret>"}}}'
sshKey: 'ssh-rsa <your_ssh_pub_key>'
----
+
For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format in the `machineNetwork` field. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.

[IMPORTANT]
====
If your cluster deployment requires a proxy configuration, you must do the following:

* Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.
* Configure the `machineNetwork` field in your installation manifest.
====
--

.. Save the file in your working directory.

. Optional. Create a configuration template in your working directory by running the following command:
+
[source,terminal]
----
$ openshift-install image-based create config-template --dir ibi-config-iso-workdir/
----
+
Example output:
+
[source,terminal]
----
INFO Config-Template created in: ibi-config-iso-workdir
----
+
The command creates the `image-based-config.yaml` configuration template in your working directory:
+
[source,yaml]
----
#
# Note: This is a sample ImageBasedConfig file showing
# which fields are available to aid you in creating your
# own image-based-config.yaml file.
#
apiVersion: v1beta1
kind: ImageBasedConfig
metadata:
  name: example-image-based-config
additionalNTPSources:
  - 0.rhel.pool.ntp.org
  - 1.rhel.pool.ntp.org
hostname: change-to-hostname
releaseRegistry: quay.io
# networkConfig contains the network configuration for the host in NMState format.
# See https://nmstate.io/examples.html for examples.
networkConfig:
  interfaces:
    - name: eth0
      type: ethernet
      state: up
      mac-address: 00:00:00:00:00:00
      ipv4:
        enabled: true
        address:
          - ip: 192.168.122.2
            prefix-length: 23
        dhcp: false
----

. Edit your configuration file:
+
Example `image-based-config.yaml` file:
+
[source,yaml]
----
#
# Note: This is a sample ImageBasedConfig file showing
# which fields are available to aid you in creating your
# own image-based-config.yaml file.
#
apiVersion: v1beta1
kind: ImageBasedConfig
metadata:
  name: sno-cluster-name
additionalNTPSources:
  - 0.rhel.pool.ntp.org
  - 1.rhel.pool.ntp.org
hostname: host.example.com
releaseRegistry: quay.io
# networkConfig contains the network configuration for the host in NMState format.
# See https://nmstate.io/examples.html for examples.
networkConfig:
    interfaces:
      - name: ens1f0
        type: ethernet
        state: up
        ipv4:
          enabled: true
          dhcp: false
          auto-dns: false
          address:
            - ip: 192.168.200.25
              prefix-length: 24
        ipv6:
          enabled: false
    dns-resolver:
      config:
        server:
          - 192.168.15.47
          - 192.168.15.48
    routes:
      config:
      - destination: 0.0.0.0/0
        metric: 150
        next-hop-address: 192.168.200.254
        next-hop-interface: ens1f0
----

. Create the configuration ISO in your working directory by running the following command:
+
[source,terminal]
----
$ openshift-install image-based create config-image --dir ibi-config-iso-workdir/
----
+
Example output:
+
[source,terminal]
----
INFO Adding NMConnection file <ens1f0.nmconnection>
INFO Consuming Install Config from target directory
INFO Consuming Image-based Config ISO configuration from target directory
INFO Config-Image created in: ibi-config-iso-workdir/auth
----
+
View the output in the working directory:
+
Example output:
+
[source,terminal]
----
ibi-config-iso-workdir/
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
└── imagebasedconfig.iso
----

. Attach the `imagebasedconfig.iso` to the preinstalled host using your preferred method and restart the host to complete the configuration process and deploy the cluster.

.Verification
When the configuration process completes on the host, access the cluster to verify its status.

. Export the `kubeconfig` environment variable to your kubeconfig file by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=ibi-config-iso-workdir/auth/kubeconfig
----

. Verify that the cluster is responding by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
+
Example output:
+
[source,terminal]
----
NAME                                         STATUS   ROLES                  AGE     VERSION
node/sno-cluster-name.host.example.com       Ready    control-plane,master   5h15m   v1.35.4
----

[role="_additional-resources"]
.Additional resources

* Using image pull secrets

* Reference specifications for the `image-based-installation-config.yaml` manifest

// Module included in the following assemblies:
//
// * edge_computing/ibi-image-based-install.adoc

[id="ibi-installer-configuration-config_{context}"]
= Reference specifications for the image-based-config.yaml manifest

[role="_abstract"]
The following content describes the specifications for the `image-based-config.yaml` manifest.

The `openshift-install` program uses the `image-based-config.yaml` manifest to create a site-specific configuration ISO for image-based deployments of {sno}.

.Required specifications
[options="header"]
[cols="2a,1a,4a"]
|====
|Specification|Type|Description
|`hostname`|`string`|Define the name of the node for the {sno} cluster.

|====

.Optional specifications
[options="header"]
[cols="2a,1a,4a"]
|====
|Specification|Type|Description

|`networkConfig`|`string`|Specifies networking configurations for the host, for example:
[source,yaml]
----
networkConfig:
    interfaces:
      - name: ens1f0
        type: ethernet
        state: up
        ...
----
If you require static networking, you must install the `nmstatectl` library on the host that creates the live installation ISO. For further information about defining network configurations by using `nmstate`, see nmstate.io.
[IMPORTANT]
====
The name of the interface must match the actual NIC name as shown in the operating system.
====

|`additionalNTPSources`|`string`| Specifies a list of NTP sources for all cluster hosts. These NTP sources are added to any existing NTP sources in the cluster. You can use the hostname or IP address for the NTP source.

|`releaseRegistry`|`string`| Specifies the container image registry that you used for the release image of the seed cluster.

|`nodeLabels` |`map[string]string`| Specifies custom node labels for the {sno} node, for example:
[source,yaml]
----
nodeLabels:
  node-role.kubernetes.io/edge: true
  environment: production
----

|====

// Module included in the following assemblies:
//
// * edge_computing/ibi-edge-image-based-install.adoc

[id="ibi-extra-manifest-standalone_{context}"]
= Configuring resources for extra manifests

[role="_abstract"]
You can optionally define additional resources in an image-based deployment for {sno} clusters.

Create the additional resources in an `extra-manifests` folder in the same working directory that has the `install-config.yaml` and `image-based-config.yaml` manifests.

[NOTE]
====
Filenames for additional resources in the `extra-manifests` directory must not exceed 30 characters. Longer filenames might cause deployment failures.
====

The following example shows how to create a resource in the `extra-manifests` folder of your working directory to add an single-root I/O virtualization (SR-IOV) network to the deployment.

[NOTE]
====
If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.
====

.Prerequisites

* You created a working directory with the `install-config.yaml` and `image-based-config.yaml` manifests

.Procedure

. Go to your working directory and create the `extra-manifests` folder by running the following command:
+
[source,terminal]
----
$ mkdir extra-manifests
----

. Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources in the `extra-manifests` folder:

.. Create a YAML file that defines the resources, as shown in the following example:
+
[NOTE]
====
If the cluster nodes include Intel vRAN Boost (VRB1 or VRB2) hardware, you can include a `SriovVrbClusterConfig` resource in the extra manifests to configure the hardware.
====
+
[source,yaml]
----
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: "example-sriov-node-policy"
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames: [ens1f0]
  nodeSelector:
    node-role.kubernetes.io/master: ""
  mtu: 1500
  numVfs: 8
  priority: 99
  resourceName: example-sriov-node-policy
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: "example-sriov-network"
  namespace: openshift-sriov-network-operator
spec:
  ipam: |-
    {
    }
  linkState: auto
  networkNamespace: sriov-namespace
  resourceName: example-sriov-node-policy
  spoofChk: "on"
  trust: "off"
---
apiVersion: sriovvrb.intel.com/v1
kind: SriovVrbClusterConfig
metadata:
  name: config
  namespace: vran-acceleration-operators
spec:
  priority: 1
  nodeSelector:
    kubernetes.io/hostname: worker-node
  acceleratorSelector:
    pciAddress: 0000:07:00.0
  drainSkip: true
  physicalFunction:
    pfDriver: vfio-pci
    vfDriver: vfio-pci
    vfAmount: 2
    bbDevConfig:
      vrb2:
        pfMode: false
        numVfBundles: 2
        maxQueueSize: 1024
        downlink4G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 0
        uplink4G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 0
        downlink5G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 4
        uplink5G:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 4
        qfft:
          aqDepthLog2: 4
          numAqsPerGroups: 16
          numQueueGroups: 4
        qmld:
          aqDepthLog2: 4
          numAqsPerGroups: 64
          numQueueGroups: 4
----

.Verification

* When you create the configuration ISO, you can view the reference to the extra manifests in the `.openshift_install_state.json` file in your working directory:
+
[source,json]
----
 "*configimage.ExtraManifests": {
        "FileList": [
            {
                "Filename": "extra-manifests/sriov-extra-manifest.yaml",
                "Data": "YXBFDFFD..."
            }
        ]
    }
----
