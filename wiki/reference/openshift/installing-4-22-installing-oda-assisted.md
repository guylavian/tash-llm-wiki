---
title: "Installing a cluster on {oda} by using the Assisted Installer"
type: reference
domain: openshift
slug: installing-4-22-installing-oda-assisted
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/installing-oda-assisted
version: 4.22
family: installing
documentKind: "Documentation"
---

# Installing a cluster on {oda} by using the Assisted Installer

[id="installing-oda-assisted-installer"]
= Installing a cluster on {oda} by using the Assisted Installer

[role="_abstract"]
You can use the {ai-full} to install a cluster on {oda-first}.

[id="ai-oda-env_{context}"]
= Preparing the {oda} environment

[role="_abstract"]
Before you can deploy an OpenShift Container Platform cluster on {oda-first}, you must prepare the {oda-short} environment.

.Prerequisites

* You have reviewed the requirements and additional prerequisites described in section 1 of the Red{nbsp}Hat OpenShift Container Platform on {oda} Deployment Guide (Oracle documentation).

.Procedure

. Complete the pre-deployment tasks as described in section 2 of the "Red{nbsp}Hat OpenShift Container Platform on {oda} Deployment Guide".

. Complete the final environment preparations as described in sections 3.1 and 3.2 of the "Red{nbsp}Hat OpenShift Container Platform on {oda} Deployment Guide".

[id="abi-oda-discovery-iso_{context}"]
= Beginning the cluster installation and generating the Discovery ISO

[role="_abstract"]
Begin installing the OpenShift Container Platform cluster in the {oda-first} environment by using the {hybrid-console}.

.Procedure

. Log in to the {hybrid-console}.

. On the *Cluster List* page, click *Create cluster*.

. Click the *Datacenter* tab.

. Under *Assisted Installer*, click *Create cluster*.

. Configure your cluster on the *Cluster details* page:

.. Enter a name for the cluster in the *Cluster name* field.

.. Enter a base domain for the cluster in the *Base domain* field.
All subdomains for the cluster will use this base domain.
+
[NOTE]
====
The base domain must be a valid DNS name.
You must not have a wildcard domain set up for the base domain.
====

.. Select a version from the *OpenShift version* dropdown list.
By default, the dropdown list displays the latest version.

.. Optional: In the *Number of control plane nodes* field, select the number of control plane nodes for your installation from the dropdown menu.
The default value is `3`.

.. Optional: Select the *Include custom manifests* checkbox if you want to upload custom manifests to further configure your cluster.
This option adds an additional page for custom manifests that you use later in the configuration process.
+
[IMPORTANT]
====
If you have already added custom manifests, clearing the *Include custom manifests* checkbox automatically deletes them all.
You must confirm the deletion.
====

.. Click *Next* to continue.
Once you proceed to the next page, you cannot go back to change any of these cluster details.

. Choose additional Operators to install on the *Operators* page:

.. If you want to install an Operator bundle, select an option in the *Bundles* section.

.. If you want to install only some Operators, select the individual Operators from the *Single Operators* section.

.. Click *Next* to continue.

. Upload an SSH public key and generate the Discovery ISO:

.. Click the *Add Hosts* button in the *Host Discovery* page.

.. Upload an SSH public key in the *SSH public key* section so that you can connect to the cluster nodes as the `core` user.
If you do not already have an SSH public key, see "Generating a key pair for cluster node SSH access" for more information.

.. Select *Show proxy settings*.

.. Enter values for the *HTTP proxy URL*, *HTTPS URL proxy*, and *No proxy domains* fields.

.. Click *Generate Discovery ISO*.

. Copy the command from the *Command to download the ISO* field and run the command as a root user in the {oda-short} environment.
+
.Example command
[source,terminal]
----
# wget -O discovery_image_example.iso 'https://api.openshift.com/api/assisted-images/bytoken/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Njg0Mjc3MDIsInN1YiI6ImNhMzZjZWU1LTQ3ZWEtNDc0Ny05OTg5LTVhZTYyMmMzMjZlNSJ9.jl-HvaxBR-WX73vpxO-Fy65bmY-RE5iL6AqL0wbWCmE/4.20/x86_64/minimal.iso'
----

[role="_additional-resources"]
.Additional resources

* Generating a key pair for cluster node SSH access

[id="abi-oda-create-nodes_{context}"]
= Creating nodes in the {oda} environment

[role="_abstract"]
After generating and downloading the Discovery ISO to your {oda-first} environment, create control plane nodes and worker nodes in the environment.

.Procedure

. Run the script to create control plane nodes as described in section 3.4 of the Red{nbsp}Hat OpenShift Container Platform on {oda} Deployment Guide (Oracle documentation).

. Run the script to create worker nodes as described in section 3.5 of the "Red{nbsp}Hat OpenShift Container Platform on {oda} Deployment Guide".

. Update the MAC address for each node as described in section 3.6 of the "Red{nbsp}Hat OpenShift Container Platform on {oda} Deployment Guide".

[id="abi-oda-start-install_{context}"]
= Completing host discovery and starting cluster installation

[role="_abstract"]
After preparing control plane and worker nodes in the {oda-first} environment, complete host discovery and initiate the cluster installation.

As you create hosts using the provided scripts, the hosts begin to appear in the table of the **Host Discovery** page, where you can configure the hosts as needed.

.Procedure

. Go to the **Host Discovery** page.

. Assign host roles in the **Host Inventory** table:

.. In the **Role** column of the table, expand the **Auto-Assign** arrow for the host.

.. Assign the host with either a **Control Plane node** or a **Worker** role.

.. Repeat this process for each host in the table.

. Click **Next**.

. On the *Storage* page, verify storage details and configure host storage as needed.

. Click **Next**.

. Configure networking details on the **Networking** page:

.. Select **User-Managed Networking** as the **Network Management** type.

.. Select **Host SSH Public Key for troubleshooting after installation** to connect to hosts using a public SSH key for troubleshooting after installation.

. Click **Next**.

. Validate cluster details on the **Review and create** page.

. Click **Install cluster** to begin the installation.

. Monitor installation progress and wait for all nodes to reach a `Ready` state.

[id="abi-oda-complete-install_{context}"]
= Completing the installation

[role="_abstract"]
After the cluster is installed and initialized, the {ai-full} indicates that the installation is finished. The {ai-full} provides the console URL, the `kubeadmin` username and password, and the `kubeconfig` file.

.Prerequisites

* You have installed the {oc-first}.

.Procedure

. Make a copy of the `kubeadmin` username and password.

. Download the `kubeconfig` file and copy it to the auth directory under your working directory by running the following commands:
+
[source,terminal]
----
$ mkdir -p <working_directory>/auth
----
+
[source,terminal]
----
$ cp kubeconfig <working_directory>/auth
----
+
[NOTE]
====
The `kubeconfig` file is available for download for 20 days after completing the installation.
====

. Add the `kubeconfig` file to your environment by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=<working_directory>/auth/kubeconfig
----

. Log in with the {oc-first} by running the following command:
+
[source,terminal]
----
$ oc login -u kubeadmin -p <password>
----
+
Replace `<password>` with the password of the `kubeadmin` user.

. Click the web console URL or click **Launch OpenShift Console** to open the console.

. Enter the `kubeadmin` username and password. Follow the instructions in the OpenShift Container Platform console to configure an identity provider and configure alert receivers.
