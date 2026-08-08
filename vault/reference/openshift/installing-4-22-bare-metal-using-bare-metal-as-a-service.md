---
title: "Using {bmaas-first}"
type: reference
domain: openshift
slug: installing-4-22-bare-metal-using-bare-metal-as-a-service
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/bare-metal-using-bare-metal-as-a-service
version: 4.22
family: installing
documentKind: "Documentation"
---

# Using {bmaas-first}

[id="bare-metal-using-bare-metal-as-a-service"]
= Using {bmaas-first}

[role="_abstract"]
You can provision and manage bare-metal hosts by using the Metal^3^ API and the Bare Metal Operator (BMO). These hosts, external to the OpenShift Container Platform cluster, can run workloads that might not be suitable for containerization or virtualization, such as legacy applications or applications that require direct hardware access.

{bmaas-first} has the following capabilities:

* Provisioning of bare-metal hosts, including initial configuration.
* Lifecycle management such as power management, firmware updates, and decommissioning by using the BMO.

As standalone systems, these hosts operate independently of the OpenShift Container Platform cluster and support diverse workloads by integrating bare metal resources with containerized and virtualized applications. {bmaas-first} can run other operating systems, but only {op-system-base-full} and CentOS Stream 9 were tested.

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmaas-prerequisites_{context}"]
= Prerequisites for using {bmaas-first}

[role="_abstract"]
{bmaas-first} lets you apply cloud-native management practices to bare-metal infrastructure, enabling automated provisioning and lifecycle management for workloads that require physical hardware. To use {bmaas-first}, complete the following prerequisites:

BareMetalHost Configuration::
All bare-metal hosts must use a Baseboard Management Controller (BMC) configured with the Redfish protocol and virtual media (`redfish-virtualmedia`) driver. Each bare-metal host requires a boot interface with a MAC address configured to receive an IP address lease.

Network Requirements::
A DHCP server, separate from the OpenShift Container Platform and Metal^3^ infrastructure, must be operational on the same Layer 2 network as the bare-metal hosts. The DHCP server must be configured to match the MAC addresses of the boot interfaces on the bare-metal hosts, enabling IP address assignment for communication with Metal^3^ components.

Cluster Privileges::
You must have `cluster-admin` privileges on the OpenShift Container Platform cluster to perform configuration tasks.

Web server with images::
{bmaas-first} does not provide images for deployment on hardware. You must configure a web server with the images and checksums you want to use. The `image` field of the `BareMetalHost` spec references these images during deployment. Ensure that the bare-metal hosts can reach the web server URL. Alternatively, you can access images from an OCI registry as a Technology Preview. This can be done by accessing a public registry such as Quay.io, or by hosting OCI images from the built-in registry in your cluster. The following is an example of images and checksums you might include:

  * `http://example.com/rhel9.qcow2`
  * `http://example.com/rhel9.qcow2.sha512sum`
  * `http://example.com/stream9.qcow2`
  * `http://example.com/stream9.qcow2.sha512sum`
  * `oci://quay.io/example/image:version`

These prerequisites ensure that {bmaas-first} can provision and manage bare-metal hosts effectively.

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmaas-using-the-bmo-to-manage-resources-across-all-namespaces_{context}"]
= Using the Bare Metal Operator to manage resources across all namespaces

[role="_abstract"]
For the Bare Metal Operator (BMO) to manage `BareMetalHost` resources across all namespaces in your OpenShift Container Platform cluster, you must configure the Operator to watch all namespaces. This configuration is important to avoid mixing non-OpenShift Container Platform workloads with other components in the same namespace.

.Prerequisites

* If you are using user-provisioned installation and the Provisioning CR does not exist, you must create it manually. For instructions, see Configuring a provisioning resource to scale user-provisioned clusters. For installer-provisioned installations, the installation program creates the Provisioning custom resource (CR) automatically.

.Procedure

* Patch the provisioning configuration to enable watching all namespaces by running the following command:
+
[source,terminal]
----
$ oc patch provisioning/provisioning-configuration \
  --type merge -p '{"spec": {"watchAllNamespaces": true}}'
----
+
The BMO applies this change automatically.

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmaas-setting-up-a-dedicated-namespace_{context}"]
= Setting up a dedicated namespace

[role="_abstract"]
To prevent accidental interference between {bmaas-first} workloads and the OpenShift Container Platform infrastructure, set up a dedicated namespace. Repeat this procedure for every project where you intend to use {bmaas-first}.

.Prerequisites

* You have configured an identify provider.

.Procedure

. Configure a `bmadmin` user in the identity provider and create a secret in OpenShift:

.. Create the `bmadmin` user in the identity provider. For example, if using the `htpasswd` identity provider, run the following command:
+
[source,terminal]
----
$ htpasswd -c -B -b ./users_htpasswd <username> <password>
----
<username>::
The user name for the identity provider. Replace `<username>` with your preferred user name. This example uses `bmadmin`.
<password>::
The password for the user. Replace `<password>` with a secure password.

.. Create a secret in the `openshift-config` namespace to store the identity provider configuration by running the following command:
+
[source,terminal]
----
$ oc create secret generic <identity_provider_arguments> -n openshift-config
----
+
For example, when using the `htpasswd` identity provider, run the following command:
+
[source,terminal]
----
$ oc create secret generic htpass-secret --from-file=htpasswd=users_htpasswd -n openshift-config
----
<identity_provider_arguments>::
The arguments specific to the identity provider secret. Replace `<identity_provider_arguments>` with the appropriate arguments for your identity provider.

. Configure OAuth to use the identity provider:

.. Edit the OAuth resource by running the following command:
+
[source,terminal]
----
$ oc edit oauth cluster
----
+
The editor opens and displays the Oauth resource.

.. Add the identity provider configuration to the `spec.identityProviders` list:
+
.Identity provider configuration examples
[options="header"]
|====
|Type|Example
| htpasswd
a|[source,yaml]
----
# ...
- name: my_bmaas_provider
  mappingMethod: claim
  type: htpasswd
  htpasswd:
    fileData:
      name: <secret>
# ...
----
| LDAP
a|[source,yaml]
----
# ...
- name: my_bmaas_provider
  mappingMethod: claim
  type: ldap
  ldap:
    attributes:
      id:
      - dn
      email:
      - mail
      name:
      - cn
      preferredUsername:
      - uid
# ...
----
| GitHub
a|[source,yaml]
----
# ...
- name: my_bmaas_provider
  mappingMethod: claim
  type: GitHub
    github:
      ca:
        name: ca-config-map
      clientID: {...}
      clientSecret:
        name: github-secret
      hostname: ...
      organizations:
      - myorganization1
      - myorganization2
      teams:
      - myorganization1/team-a
      - myorganization2/team-b
# ...
----
|====
+
For more information about identify providers, see Authentication and authorization.

.. Save and exit the editor.

. Create a `bmadmin` user by running the following command:
+
[source,terminal]
----
$ oc create user <username>
----
<username>::
The user name. Replace `<username>` with your username. The following examples use `bmadmin` as the username.

. Create a dedicated `bmaas` namespace for {bmaas-first} hosts by running the following command:
+
[source,terminal]
----
$ oc new-project <namespace>
----
`<namespace>`::
Replace <namespace> with the namespace name that you want to use. This example uses `bmaas`.

. Assign the `edit` role to the `bmadmin` user in the `bmaas` namespace by running the following command:
+
[source,terminal]
----
$ oc adm policy add-role-to-user edit <username> -n bmaas
----

. Clone the `baremetal-operator` repository to obtain the role-based access control (RBAC) role definitions by running the following command:
+
[source,terminal,subs="attributes"]
----
$ git clone -b release- https://github.com/openshift/baremetal-operator.git
----

. For each role you want to add, apply the appropriate RBAC role YAML file from the repository by running the following command:
+
[source,terminal]
----
$ oc apply -f baremetal-operator/config/base/rbac/<role_filename>.yaml
----

. Assign the custom RBAC roles to the `bmadmin` user in the `bmaas` namespace by running the following command:
+
[source,terminal]
----
$ oc adm policy add-role-to-user <role_name> bmadmin -n bmaas
----

. Login as the `bmadmin` user by running the following command:
+
[source,terminal]
----
$ oc login <api_server_url>:6443
----
`<api_server_url>`::
The URL to the Kubernetes API.

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmo-creating-a-bmc-secret_{context}"]
= Creating a BMC secret

[role="_abstract"]
To deploy a bare-metal host, you must create a secret to access the baseboard management controller (BMC). This means you can remotely provision or manage the physical hardware.

.Procedure

. Create a BMC secret file by running the following command:
+
[source,terminal]
----
$ vim bmaas-<name>-bmc-secret.yaml
----
+
Replace `<name>` with the name of the bare-metal host.

. Edit the secret:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: bmaas-<name>-bmc-secret
  namespace: bmaas
type: Opaque
data:
  username: <base64_of_uid>
  password: <base64_of_pwd>
----
+
<base64_of_uid>::
Replace `<base64_of_uid>` with the BMC user name as a Base64-encoded string.
<base64_of_pwd>::
Replace `<base64_of_pwd>` with the BMC password as a Base64-encoded string.

. Apply the BMC secret by running the following command:
+
[source,terminal]
----
$ oc apply -f bmaas-<name>-bmc-secret.yaml
----

[role="_additional-resources"]
.Additional resources

* About BMC addressing

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmo-creating-a-bare-metal-host-resource_{context}"]
= Creating a bare-metal host resource

[role="_abstract"]
To deploy a bare-metal host, you must create a `BareMetalHost` resource.

.Procedure

. Create a `BareMetalHost` custom resource (CR) file by running the following command:
+
[source,terminal]
----
$ vim bmaas-<name>-bmh.yaml
----
+
<name>::
    Replace `<name>` with the name of the bare-metal host.

. Edit the CR:
+
[source,yaml]
----
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: bmaas-<name>
  namespace:  bmaas
spec:
  online: true
  bootMACAddress: <mac_addr>
  bmc:
    address: redfish-virtualmedia+<address>/redfish/v1/Systems/System.Embedded.1
    credentialsName: bmaas-<num>-bmc-secret
----
+
<mac_addr>::
    Replace `<mac_addr>` with the MAC address of the first NIC on the bare-metal host.
<address>::
    Replace `<address>` with IP address or FQDN of the host.

. Apply the CR by running the following command:
+
[source,terminal]
----
$ oc apply -f bmaas-<name>-bmh.yaml
----

.Verification

* Check the `BareMetalHost` state by running the following command:
+
[source,terminal]
----
$ oc get baremetalhost -n bmaas
----
+
The state progresses from *registering*, to *inspecting*, and finally to *available*.

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmo-configuring-users-for-bmaas-hosts_{context}"]
= Configuring users for {bmaas-first} hosts

[role="_abstract"]
Configure bare-metal host users and add them to a Kubernetes secret. Then, create and apply the secret to customize the host. With configured users you can access or manage the bare-metal host after it is provisioned.

.Procedure

. Create a file named `<hostname>-user-data.yaml`, where `<hostname>` is the name of the bare-metal host, with the following content:
+
[source,yaml]
----
users:
  - name: <name>
    sudo: [<sudo_config>]
    ssh_authorized_keys:
      - <key_type>
      <key>
    shell: <shell_path>
    groups: [<groups>]
    lock_passwd: true|false
----
`users.name`::
The user name.
`users.sudo`::
The sudo configuration for the user.
`users.ssh_authorized_keys.<key_type>`::
The SSH key type.
`users.ssh_authorized_keys.<key>`::
The public SSH key to use when accessing this host as the `<name>` user.
`users.shell`::
The shell to use when accessing the host.
`users.groups`::
The groups the user belongs to.
`users.lock_passwd`::
Whether the user password is locked. If `true`, the user cannot log in by using the password, but can still use SSH.

+
.Example user
[source,yaml]
----
users:
  - name: sysadmin
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
    ssh_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc2E... sysadmin@workstation.example.com
    shell: /bin/bash
    groups: [adm, sudo]
    lock_passwd: true
----

. Create a secret from the `<hostname>-user-data.yaml` file by running the following command:
+
[source,terminal]
----
$ oc create secret generic <hostname>-user-data \
  --from-file=userData=<hostname>-user-data.yaml -n bmaas
----
`<hostname>`::
  The name of the bare-metal host.

. Configure the `BareMetalHost` to use the `<hostname>-user-data.yaml` file by running the following command:
+
[source,terminal]
----
$ oc patch baremetalhost <hostname> -n bmaas \
     --type merge -p '{"spec":{"userData":{"name":"<hostname>-user-data"}}}'
----
`<hostname>`::
  The name of the bare-metal host.

//include::modules/bmo-configuring-ignition-userdata.adoc[leveloffset=+1]

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmo-configuring-the-networkdata-parameter-in-the-bmo-cr_{context}"]
= Configuring the networkData parameter in the BareMetalHost resource

[role="_abstract"]
The `networkData` field in the `BareMetalHost` custom resource (CR) allows you to control the network configuration of the bare-metal host at creation time. For most operating systems, this is achieved using a configuration file encapsulated in a Kubernetes secret. Then, the `cloud-init` service uses it to customize services.

.Procedure

. Create a file named `network-data.yaml` with the following content:
+
[source,yaml]
----
links:
  - id: <interface_id>
    type: phy
    ethernet_mac_address: <mac_address>
networks:
  - id: <interface_id>
    source,terminal
----
$ oc create secret generic <hostname>-network-data \
  --from-file=networkData=network-data.yaml -n bmaas
----
+
`<hostname>`::
The hostname of the bare-metal host.

. Configure the `BareMetalHost` to use the `networkData` file by running the following command:
+
[source,terminal]
----
$ oc patch baremetalhost <hostname> -n bmaas \
  --type merge -p '{"spec":{"networkData":{"name":"<hostname>-network-data"}}}'
----

// This module is included in the following assemblies:
//
// * installing/installing_bare_metal/bare-metal-using-bare-metal-as-a-service.adoc

[id="bmo-deploying-an-image-to-the-bare-metal-host_{context}"]
= Deploying an image to the bare-metal host

[role="_abstract"]
To deploy the image to the host, update the `image` field in the `spec` section of the `BareMetalHost` resource. Once you update the `image` field, provisioning begins immediately. Deploying an image transforms bare hardware into a functional system
ready to run your workloads, in an automated and repeatable way.

.Procedure

* Update the `image` field in the `BareMetalHost` CR by running the following command:
+
[source,terminal]
----
$ oc patch baremetalhost <hostname> \
  --type merge -p '{"spec": {"image": {"url": "<image_url>", "checksum": "<checksum_url>", "checksumType": "auto"}}}'
----
+
`<hostname>`::
The name of your `BareMetalHost` resource.
`<image_url>`::
The URL of the image to deploy. You can access images using the HTTP and OCI protocols. Accessing images using the OCI protocol is available as a Technology Preview.
`<checksum_url>`::
The URL of the checksum file for the image.
