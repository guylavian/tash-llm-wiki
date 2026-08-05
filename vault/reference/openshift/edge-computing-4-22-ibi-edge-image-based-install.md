---
title: "About image-based deployments for managed {sno}"
type: reference
domain: openshift
slug: edge-computing-4-22-ibi-edge-image-based-install
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ibi-edge-image-based-install
version: 4.22
family: edge_computing
documentKind: "Documentation"
---

# About image-based deployments for managed {sno}

[id="ibi-edge-image-based-install"]
= About image-based deployments for managed {sno}

When a host preinstalled with {sno} using an image-based installation arrives at a remote site, a technician can easily reconfigure and deploy the host in a matter of minutes.

For clusters with a hub-and-spoke architecture, to complete the deployment of a preinstalled host, you must first define site-specific configuration resources on the hub cluster for each host. These resources contain configuration information such as the properties of the bare-metal host, authentication details, and other deployment and networking information.

The Image Based Install (IBI) Operator creates a configuration ISO from these resources, and then boots the host with the configuration ISO attached. The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the {sno} cluster is ready.

[NOTE]
====
You must create distinct configuration resources for each bare-metal host.
====

See the following high-level steps to deploy a preinstalled host in a cluster with a hub-and-spoke architecture:

. Install the IBI Operator on the hub cluster.
. Create site-specific configuration resources in the hub cluster for each host.
. The IBI Operator creates a configuration ISO from these resources and boots the target host with the configuration ISO attached.
. The host mounts the configuration ISO and runs the reconfiguration process. When the reconfiguration completes, the {sno} cluster is ready.

[NOTE]
====
Alternatively, you can manually deploy a preinstalled host for a cluster without using a hub cluster. You must define an `ImageBasedConfig` resource and an installation manifest, and provide these as inputs to the `openshift-install` installation program. For more information, see "Deploying a {sno} cluster using the `openshift-install` program".
====

[role="_additional-resources"]
.Additional resources

* Deploying a {sno} cluster using the `openshift-install` program

// Module included in the following assemblies:
//
// * edge_computing/ibi-edge-image-based-install.adoc

[id="ibi-install-ibi-operator_{context}"]
= Installing the Image Based Install Operator

[role="_abstract"]
The Image Based Install (IBI) Operator is part of the image-based deployment workflow for preinstalled {sno} on bare-metal hosts.

[NOTE]
====
The IBI Operator is part of the {mce} from MCE version 2.7.
====

.Prerequisites

* You logged in as a user with `cluster-admin` privileges.
* You deployed a {rh-rhacm-first} hub cluster or you deployed the {mce}.
* You reviewed the required versions of software components in the section "Software prerequisites for an image-based installation".

.Procedure

* Set the `enabled` specification to `true` for the `image-based-install-operator` component in the `MultiClusterEngine` resource by running the following command:
+
[source,terminal]
----
$ oc patch multiclusterengines.multicluster.openshift.io multiclusterengine --type json \
--patch '[{"op": "add", "path":"/spec/overrides/components/-", "value": {"name":"image-based-install-operator","enabled": true}}]'
----

.Verification

* Check that the Image Based Install Operator pod is running by running the following command:
+
[source,terminal]
----
$ oc get pods -A | grep image-based
----
+
Example output:
+
[source,terminal]
----
multicluster-engine             image-based-install-operator-57fb8sc423-bxdj8             2/2     Running     0               5m
----

// Module included in the following assemblies:
//
// * edge_computing/ibi-edge-image-based-install.adoc

[id="ibi-create-config-iso_{context}"]
= Deploying a managed {sno} cluster using the IBI Operator

[role="_abstract"]
Create the site-specific configuration resources in the hub cluster to initiate the image-based deployment of a preinstalled host.

When you create these configuration resources in the hub cluster, the Image Based Install (IBI) Operator generates a configuration ISO and attaches it to the target host to begin the site-specific configuration  process. When the configuration process completes, the {sno} cluster is ready.

[NOTE]
====
For more information about the configuration resources that you must configure in the hub cluster, see "Cluster configuration resources for deploying a preinstalled host".
====

.Prerequisites

* You preinstalled a host with {sno} using an image-based installation.
* You logged in as a user with `cluster-admin` privileges.
* You deployed a {rh-rhacm-first} hub cluster or you deployed the multicluster engine for Kubernetes operator (MCE).
* You installed the IBI Operator on the hub cluster.
* You created a pull secret to authenticate pull requests. For more information, see "Using image pull secrets".

.Procedure

. Create the `ibi-ns` namespace by running the following command:
+
[source,terminal]
----
$ oc create namespace ibi-ns
----

. Create the `Secret` resource for your image registry:

.. Create a YAML file that defines the `Secret` resource for your image registry:
+
Example `secret-image-registry.yaml` file:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: ibi-image-pull-secret
  namespace: ibi-ns
stringData:
  .dockerconfigjson: <base64_docker_auth_code>
type: kubernetes.io/dockerconfigjson
----
+
where:
+
`<base64_docker_auth_code>`:: Specifies base64-encoded credential details. See the "Additional resources" section for more information about using image pull secrets.

.. Create the `Secret` resource for your image registry by running the following command:
+
[source,terminal]
----
$ oc create -f secret-image-registry.yaml
----

. Optional: Configure static networking for the host:

.. Create a `Secret` resource containing the static network configuration in `nmstate` format:
+
Example `host-network-config-secret.yaml` file:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
 name: <network_secret_name>
 namespace: ibi-ns
type: Opaque
stringData:
 nmstate: |
  interfaces:
    - name: <interface_name>
      type: ethernet
      state: up
      ipv4:
        enabled: true
        address:
          - ip: 192.168.200.25
            prefix-length: 24
        dhcp: false
      ipv6:
        enabled: false
  dns-resolver:
    config:
      server:
        - <dns_server_1>
        - 192.168.15.48
  routes:
    config:
      - destination: 0.0.0.0/0
        metric: 150
        next-hop-address: 192.168.200.254
        next-hop-interface: <interface_name>
        table-id: 254
----
+
where:
+
`<network_secret_name>`:: Specifies the name for the `Secret` resource, for example `host-network-config-secret`.
`nmstate`:: Specifies the static network configuration in `nmstate` format.
`<interface_name>`:: Specifies the name of the interface on the host, for example `ens1f0`. The name of the interface must match the actual NIC name as shown in the operating system. To use your MAC address for NIC matching, set the `identifier` field to `mac-address`.
`dhcp: false`:: Specifies that DHCP is disabled to ensure `nmstate` assigns the static IP address to the interface.
`<dns_server_1>`:: Specifies one or more DNS servers that the system will use to resolve domain names, for example `192.168.15.47`.
`config`:: Specifies the default route through the `ens1f0` interface to the next hop IP address `192.168.200.254`.

. Create the `BareMetalHost` and `Secret` resources:

.. Create a YAML file that defines the `BareMetalHost` and `Secret` resources:
+
Example `ibi-bmh.yaml` file:
+
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: <baremetalhost_name>
  namespace: ibi-ns
spec:
  online: <online_status>
  bootMACAddress: <boot_mac_address>
  bmc:
    address: <bmc_address>
    credentialsName: <bmh_secret_name>
  preprovisioningNetworkDataName: <network_secret_name>
  automatedCleaningMode: disabled
  externallyProvisioned: true
---
apiVersion: v1
kind: Secret
metadata:
  name: <bmh_secret_name>
  namespace: ibi-ns
type: Opaque
data:
  username: <username>
  password: <password>
----
+
where:
+
`<baremetalhost_name>`:: Specifies the name for the `BareMetalHost` resource, for example `ibi-bmh`.
`<online_status>`:: Specifies if the host should be online, for example `false`.
`<boot_mac_address>`:: Specifies the host boot MAC address, for example `00:a5:12:55:62:64`.
`<bmc_address>`:: Specifies the BMC address, for example `redfish-virtualmedia+http://192.168.111.1:8000/redfish/v1/Systems/8a5babac-94d0-4c20-b282-50dc3a0a32b5`. You can only use bare-metal host drivers that support virtual media networking booting, for example redfish-virtualmedia and idrac-virtualmedia.
`<bmh_secret_name>`:: Specifies the name of the bare-metal host `Secret` resource, for example `ibi-bmh-bmc-secret`.
`<network_secret_name>`:: (Optional) Specifies the name of the `Secret` resource containing the static network configuration for the host, for example `host-network-config-secret`.
`automatedCleaningMode: disabled`:: Specifies that automated cleaning is disabled to prevent the provisioning service from deleting all preinstallation artifacts, such as the seed image, during disk inspection.
`externallyProvisioned: true`:: Specifies that the host is externally provisioned to enable it to boot from the preinstalled disk, instead of the configuration ISO.
`<username>`:: Specifies the username for BMC authentication.
`<password>`:: Specifies the password for BMC authentication.

.. Create the `BareMetalHost` and `Secret` resources by running the following command:
+
[source,terminal]
----
$ oc create -f ibi-bmh.yaml
----

. Create the `ClusterImageSet` resource:

.. Create a YAML file that defines the `ClusterImageSet` resource:
+
Example `ibi-cluster-image-set.yaml` file:
+
[source,yaml]
----
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  name: <clusterimageset_name>
spec:
  releaseImage: <release_image>
----
+
where:
+
`<clusterimageset_name>`:: Specifies the name for the `ClusterImageSet` resource, for example `ibi-img-version-arch`.
`<release_image>`:: Specifies the address for the release image to use for the deployment, for example `ibi.example.com:path/to/release/images:version-arch`. If you use a different image registry compared to the image registry used during seed image generation, ensure that the OpenShift Container Platform version for the release image remains the same.

.. Create the `ClusterImageSet` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f ibi-cluster-image-set.yaml
----

. Create the `ImageClusterInstall` resource:

.. Create a YAML file that defines the `ImageClusterInstall` resource:
+
Example `ibi-image-cluster-install.yaml` file:
+
[source,yaml]
----
apiVersion: extensions.hive.openshift.io/v1alpha1
kind: ImageClusterInstall
metadata:
  name: <imageclusterinstall_name>
  namespace: ibi-ns
spec:
  bareMetalHostRef:
    name: <baremetalhost_name>
    namespace: ibi-ns
  clusterDeploymentRef:
    name: <clusterdeployment_name>
  hostname: <cluster_hostname>
  imageSetRef:
    name: <clusterimageset_name>
  machineNetworks:
  - cidr: 10.0.0.0/24
  #- cidr: fd01::/64
  proxy:
    httpProxy: "http://proxy.example.com:8080"
    #httpsProxy: "http://proxy.example.com:8080"
    #noProxy: "no_proxy.example.com"
----
+
where:
+
`<imageclusterinstall_name>`:: Specifies the name for the `ImageClusterInstall` resource, for example `ibi-image-install`.
`<baremetalhost_name>`:: Specifies the `BareMetalHost` resource that you want to target for the image-based installation, for example `ibi-bmh`.
`<clusterdeployment_name>`:: Specifies the name of the `ClusterDeployment` resource that you want to use for the image-based installation of the target host, for example `ibi-cluster-deployment`.
`<cluster_hostname>`:: Specifies the hostname for the cluster, for example `ibi-host`.
`<clusterimageset_name>`:: Specifies the name of the `ClusterImageSet` resource you used to define the container release images to use for deployment, for example `ibi-img-version-arch`.
`machineNetworks`:: Specifies the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.
`proxy`:: (Optional) Specifies a proxy to use for the cluster deployment.
+
[IMPORTANT]
====
If your cluster deployment requires a proxy configuration, you must do the following:

* Create a seed image from a seed cluster featuring a proxy configuration. The proxy configurations do not have to match.
* Configure the `machineNetwork` field in your installation manifest.
====

.. Create the `ImageClusterInstall` resource by running the following command:
+
[source,terminal]
----
$ oc create -f ibi-image-cluster-install.yaml
----

. Create the `ClusterDeployment` resource:

.. Create a YAML file that defines the `ClusterDeployment` resource:
+
Example `ibi-cluster-deployment.yaml` file:
+
[source,yaml]
----
apiVersion: hive.openshift.io/v1
kind: ClusterDeployment
metadata:
  name: <clusterdeployment_name>
  namespace: <namespace>
spec:
  baseDomain: <base_domain>
  clusterInstallRef:
    group: extensions.hive.openshift.io
    kind: ImageClusterInstall
    name: <imageclusterinstall_name>
    version: v1alpha1
  clusterName: <cluster_name>
  platform:
    none: {}
  pullSecretRef:
    name: <pull_secret_name>
----
+
where:
+
`<clusterdeployment_name>`:: Specifies the name for the `ClusterDeployment` resource, for example `ibi-cluster-deployment`.
`<namespace>`:: Specifies the namespace for the `ClusterDeployment` resource, for example `ibi-ns`.
`<base_domain>`:: Specifies the base domain that the cluster should belong to, for example `example.com`.
`<imageclusterinstall_name>`:: Specifies the name of the `ImageClusterInstall` in which you defined the container images to use for the image-based installation of the target host, for example `ibi-image-install`.
`<cluster_name>`:: Specifies a name for the cluster, for example `ibi-cluster`.
`<pull_secret_name>`:: Specifies the secret to use for pulling images from your image registry, for example `ibi-image-pull-secret`.

.. Create the `ClusterDeployment` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f ibi-cluster-deployment.yaml
----

. Create the `ManagedCluster` resource:

.. Create a YAML file that defines the `ManagedCluster` resource:
+
Example `ibi-managed.yaml` file:
+
[source,yaml]
----
apiVersion: cluster.open-cluster-management.io/v1
kind: ManagedCluster
metadata:
  name: <managedcluster_name>
spec:
  hubAcceptsClient: <hub_accepts_client>
----
+
where:
+
`<managedcluster_name>`:: Specifies the name for the `ManagedCluster` resource, for example `sno-ibi`.
`<hub_accepts_client>`:: Specifies whether {rh-rhacm} manages the cluster. Set to `true` to enable management.

.. Create the `ManagedCluster` resource by running the following command:
+
[source,terminal]
----
$ oc apply -f ibi-managed.yaml
----

.Verification

. Check the status of the `ImageClusterInstall` in the hub cluster to monitor the progress of the target host installation by running the following command:
+
[source,terminal]
----
$ oc get imageclusterinstall
----
+
Example output:
+
[source,terminal]
----
NAME       REQUIREMENTSMET           COMPLETED                     BAREMETALHOSTREF
target-0   HostValidationSucceeded   ClusterInstallationSucceeded  ibi-bmh
----
+
[WARNING]
====
If the `ImageClusterInstall` resource is deleted, the IBI Operator reattaches the `BareMetalHost` resource and reboots the machine.
====

. When the installation completes, you can retrieve the `kubeconfig` secret to log in to the managed cluster by running the following command:
+
[source,terminal]
----
$ oc extract secret/<cluster_name>-admin-kubeconfig -n <cluster_namespace>  --to - > <directory>/<cluster_name>-kubeconfig
----
+
where:
+
`<cluster_name>`:: Specifies the name of the cluster.
`<cluster_namespace>`:: Specifies the namespace of the cluster.
`<directory>`:: Specifies the directory in which to create the file.

[role="_additional-resources"]
.Additional resources

* Using image pull secrets

* Cluster configuration resources for deploying a preinstalled host

// Module included in the following assemblies:
//
// * edge_computing/ibi-edge-image-based-install.adoc

[id="ibi-managed-cluster-config-resources_{context}"]
= Cluster configuration resources for deploying a preinstalled host

[role="_abstract"]
To complete a deployment for a preinstalled host at a remote site, you must configure the following site-specifc cluster configuration resources in the hub cluster for each bare-metal host.

.Cluster configuration resources reference
[cols="1,3", options="header"]
|===

| Resource | Description

|`Namespace`
|Namespace for the managed {sno} cluster.

|`BareMetalHost`
|Describes the physical host and its properties, such as the provisioning and hardware configuration.

|`Secret` for the bare-metal host
|Credentials for the host BMC.

|`Secret` for the bare-metal host static network configuration
|Optional: Describes static network configuration for the target host.

|`Secret` for the image registry
|Credentials for the image registry. The secret for the image registry must be of type `kubernetes.io/dockerconfigjson`.

|`ImageClusterInstall`
|References the bare-metal host, deployment, and image set resources.

|`ClusterImageSet`
|Describes the release images to use for the cluster.

|`ClusterDeployment`
|Describes networking, authentication, and platform-specific settings.

|`ManagedCluster`
|Describes cluster details to enable {rh-rhacm-first} to register and manage.

|`ConfigMap`
|Optional: Describes additional configurations for the cluster deployment, such as adding a bundle of trusted certificates for the host to ensure trusted communications for cluster services.

|===

// Module included in the following assemblies:
//
// * edge_computing/ibi-edge-image-based-install.adoc

[id="ibi-image-cluster-install-api-spec_{context}"]
= ImageClusterInstall resource API specifications

[role="_abstract"]
The following content describes the API specifications for the `ImageClusterInstall` resource. This resource is the endpoint for the Image Based Install Operator.

.Required specifications
[options="header"]
[cols="2a,1a,4a"]
|====
|Specification|Type|Description

|`imageSetRef`|`string`| Specify the name of the `ClusterImageSet` resource that defines the release images for the deployment.

|`hostname`|`string`| Specify the hostname for the cluster.

|`sshKey`|`string`| Specify your SSH key to provide SSH access to the target host.

|====

.Optional specifications
[options="header"]
[cols="2a,1a,4a"]
|====
|Specification|Type|Description

|`clusterDeploymentRef`|`string`| Specify the name of the `ClusterDeployment` resource that you want to use for the image-based installation of the target host.

|`clusterMetadata`|`string`| After the deployment completes, this specification is automatically populated with metadata information about the cluster, including the `cluster-admin` kubeconfig credentials for logging in to the cluster.

|`imageDigestSources`|`string`|Specifies the sources or repositories for the release-image content, for example:
[source,yaml]
----
imageDigestSources:
  - mirrors:
      - "registry.example.com:5000/ocp4/openshift4"
    source: "quay.io/openshift-release-dev/ocp-release"
----

|`extraManifestsRefs`|`string`| Specify a `ConfigMap` resource containing additional manifests to be applied to the target cluster.

|`bareMetalHostRef`|`string`| Specify the `bareMetalHost` resource to use for the cluster deployment

|`machineNetworks`|`string`| Specify the public Classless Inter-Domain Routing (CIDR) of the external network. For dual-stack networking, you can specify both IPv4 and IPv6 CIDRs using a list format. The first CIDR in the list is the primary address family and must match the primary address family of the seed cluster.

|`proxy`|`string`|Specifies proxy settings for the cluster, for example:
[source,yaml]

----
proxy:
  httpProxy: "http://proxy.example.com:8080"
  httpsProxy: "http://proxy.example.com:8080"
  noProxy: "no_proxy.example.com"
----

|`caBundleRef`|`string`| Specify a `ConfigMap` resource containing the new bundle of trusted certificates for the host.

|====

// Module included in the following assemblies:
//
// * edge_computing/ibi-edge-image-based-install.adoc

[id="ibi-extra-manifests-configmap_{context}"]
= ConfigMap resources for extra manifests

[role="_abstract"]
You can optionally create a `ConfigMap` resource to define additional manifests in an image-based deployment for managed {sno} clusters.

After you create the `ConfigMap` resource, reference it in the `ImageClusterInstall` resource. During deployment, the IBI Operator includes the extra manifests in the deployment.

[id="ibi-create-extra-manifest-configmap_{context}"]
== Creating a ConfigMap resource to add extra manifests in an image-based deployment

You can use a `ConfigMap` resource to add extra manifests to the image-based deployment for {sno} clusters.

The following example adds an single-root I/O virtualization (SR-IOV) network to the deployment.

[NOTE]
====
Filenames for extra manifests must not exceed 30 characters. Longer filenames might cause deployment failures.
====

Before you begin, ensure that:

* You preinstalled a host with {sno} using an image-based installation.
* You logged in as a user with `cluster-admin` privileges.

To create the `ConfigMap` resource, complete the following steps:

. Create the `SriovNetworkNodePolicy` and `SriovNetwork` resources:

.. Create a YAML file that defines the resources, as in the following example:
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
----

.. Create the `ConfigMap` resource by running the following command:
+
[source,terminal]
----
$ oc create configmap sr-iov-extra-manifest --from-file=sriov-extra-manifest.yaml -n <namespace>
----
+
where:
+
`<namespace>`:: Specifies the namespace that has the `ImageClusterInstall` resource, for example `ibi-ns`.
+
Example output:
+
[source,terminal]
----
configmap/sr-iov-extra-manifest created
----
+
[NOTE]
====
If you add more than one extra manifest, and the manifests must be applied in a specific order, you must prefix the filenames of the manifests with numbers that represent the required order. For example, `00-namespace.yaml`, `01-sriov-extra-manifest.yaml`, and so on.
====

. Reference the `ConfigMap` resource in the `spec.extraManifestsRefs` field of the `ImageClusterInstall` resource:
+
[source,yaml]
----
#...
  spec:
    extraManifestsRefs:
    - name: sr-iov-extra-manifest
#...
----

[id="ibi-create-ca-extra-manifest-configmap_{context}"]
== Creating a ConfigMap resource to add a CA bundle in an image-based deployment

You can use a `ConfigMap` resource to add a certificate authority (CA) bundle to the host to ensure trusted communications for cluster services.

After you create the `ConfigMap` resource, reference it in the `spec.caBundleRef` field of the `ImageClusterInstall` resource.

Before you begin, ensure that:

* You preinstalled a host with {sno} using an image-based installation.
* You logged in as a user with `cluster-admin` privileges.

To create the CA bundle `ConfigMap` resource, complete the following steps:

. Create a CA bundle file called `tls-ca-bundle.pem`, as in the following example:
+
[source,text]
----
-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJAKmjYKJbIyz3MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
...Custom CA certificate bundle...
4WPl0Qb27Sb1xZyAsy1ww6MYb98EovazUSfjYr2EVF6ThcAPu4/sMxUV7He2J6Jd
cA8SMRwpUbz3LXY=
-----END CERTIFICATE-----
----

. Create the `ConfigMap` object by running the following command:
+
[source,terminal]
----
$ oc create configmap custom-ca --from-file=tls-ca-bundle.pem -n ibi-ns
----
+
where:
+
`custom-ca`:: Specifies the name for the `ConfigMap` resource.
`tls-ca-bundle.pem`:: Specifies the key for the `data` entry in the `ConfigMap` resource. You must include a `data` entry with the `tls-ca-bundle.pem` key.
`ibi-ns`:: Specifies the namespace that has the `ImageClusterInstall` resource.
+
Example output:
+
[source,terminal]
----
configmap/custom-ca created
----

. Reference the `ConfigMap` resource in the `spec.caBundleRef` field of the `ImageClusterInstall` resource:
+
[source,yaml]
----
#...
  spec:
    caBundleRef:
      name: custom-ca
#...
----

[role="_additional-resources"]
.Additional resources

* About the BareMetalHost resource

* Using image pull secrets

* Reference specifications for the image-based-config.yaml manifest
