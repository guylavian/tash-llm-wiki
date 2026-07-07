---
title: "Creating a Windows machine set on vSphere"
type: reference
domain: openshift
slug: windows-containers-4-22-creating-windows-machineset-vsphere
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/windows_containers/creating-windows-machineset-vsphere
version: 4.22
family: windows_containers
documentKind: "Documentation"
---

# Creating a Windows machine set on vSphere

[id="creating-windows-machineset-vsphere"]
= Creating a Windows machine set on vSphere

[role="_abstract"]
You can create a Windows `MachineSet` object to serve a specific purpose in your OpenShift Container Platform cluster on {vmw-first}. For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines.

== Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.
* You must prepare your vSphere environment for Windows container workloads by creating the vSphere Windows VM golden image. See "Creating the vSphere Windows VM golden image" in this section.
* You must enable communication with the internal API server for the WMCO. See "Enabling communication with the internal API server for the WMCO on vSphere" in this section.

// Module included in the following assemblies:
//
// * machine_management/index.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-osp.adoc
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-aws.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-azure.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-gcp.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-nutanix.adoc

[id="machine-api-overview_{context}"]
= Machine API overview

[role="_abstract"]
The Machine API performs all node host provisioning management actions after the cluster installation finishes. Because of this system, OpenShift Container Platform offers an elastic, dynamic provisioning method on top of public or private cloud infrastructure.

The Machine API is a combination of primary resources that are based on the upstream Cluster API project and custom OpenShift Container Platform resources.

The two primary resources are:

Machines:: A fundamental unit that describes the host for a node. A machine has a `providerSpec` specification, which describes the types of compute nodes that are offered for different cloud platforms. For example, a machine type for a compute node might define a specific machine type and required metadata.

Machine sets:: `MachineSet` resources are groups of compute machines. Compute machine sets are to compute machines as replica sets are to pods. If you need more compute machines or must scale them down, you change the `replicas` field on the `MachineSet` resource to meet your compute need.
+
[WARNING]
====
Control plane machines cannot be managed by compute machine sets.

Control plane machine sets provide management capabilities for supported control plane machines that are similar to what compute machine sets provide for compute machines.

For more information, see “Managing control plane machines".
====

The following custom resources add more capabilities to your cluster:

Machine autoscaler:: The `MachineAutoscaler` resource automatically scales compute machines in a cloud. You can set the minimum and maximum scaling boundaries for nodes in a specified compute machine set, and the machine autoscaler maintains that range of nodes.
+
The `MachineAutoscaler` object takes effect after a `ClusterAutoscaler` object exists. Both `ClusterAutoscaler` and `MachineAutoscaler` resources are made available by the `ClusterAutoscalerOperator` object.

Cluster autoscaler:: This resource is based on the upstream cluster autoscaler project. In the OpenShift Container Platform implementation, it is integrated with the Machine API by extending the compute machine set API. You can use the cluster autoscaler to manage your cluster in the following ways:
+
* Set cluster-wide scaling limits for resources such as cores, nodes, memory, and GPU
* Set the priority so that the cluster prioritizes pods and new nodes are not brought online for less important pods
* Set the scaling policy so that you can scale up nodes but not scale them down

Machine health check:: The `MachineHealthCheck` resource detects when a machine is unhealthy, deletes it, and, on supported platforms, makes a new machine.

// Should this paragraph still be in here in 2022? Or at least should it be rephrased to avoid comparing to 3.11?
In OpenShift Container Platform version 3.11, you could not roll out a multi-zone architecture easily because the cluster did not manage machine provisioning. Beginning with OpenShift Container Platform version 4.1, this process is easier. Each compute machine set is scoped to a single zone, so the installation program sends out compute machine sets across availability zones on your behalf. And then because your compute is dynamic, and in the face of a zone failure, you always have a zone for when you must rebalance your machines. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability. The autoscaler provides best-effort balancing over the life of a cluster.

// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc

[id="creating-the-vsphere-windows-vm-golden-image_{context}"]
= Creating the vSphere Windows VM golden image

[role="_abstract"]
You must prepare your vSphere environment for Windows container workloads by creating the vSphere Windows VM golden image.

.Prerequisites

* You have created a private/public key pair, which is used to configure key-based authentication in the OpenSSH server. The private key must be configured in the Windows Machine Config Operator (WMCO) namespace so that the WMCO can communicate with the Windows VM.
+
--
--
+
See the "Configuring a secret for the Windows Machine Config Operator" section for more details.

[NOTE]
====
You must use Microsoft PowerShell commands in several cases when creating your Windows VM. PowerShell commands in this guide are distinguished by the `PS C:\>` prefix.
====

.Procedure

.  Select a compatible Windows Server version. Currently, the Windows Machine Config Operator (WMCO) stable version supports the following versions:
+
--
* Windows Server 2025 Long-Term Servicing Channel
* Windows Server 2022 Long-Term Servicing Channel with the OS-level container networking patch KB5012637, Microsoft Windows documentation.
--

. Create a new VM in the vSphere client using the VM golden image with a compatible Windows Server version. For more information about compatible versions, see the "Windows Machine Config Operator prerequisites" section of the "Red Hat OpenShift support for Windows Containers release notes."
+
[IMPORTANT]
====
The virtual hardware version for your VM must meet the infrastructure requirements for OpenShift Container Platform. For more information, see the "VMware vSphere infrastructure requirements" section in the OpenShift Container Platform documentation. Also, you can refer to VMware's documentation on virtual machine hardware versions.
====

. Install and configure VMware Tools version 11.0.6 or greater on the Windows VM. See the VMware Tools documentation for more information.

. After installing VMware Tools on the Windows VM, verify the following:

.. The `C:\ProgramData\VMware\VMware Tools\tools.conf` file exists with the following entry:
+
[source,ini]
----
exclude-nics=
----
+
If the `tools.conf` file does not exist, create it with the `exclude-nics` option uncommented and set as an empty value.
+
This entry ensures the cloned vNIC generated on the Windows VM by the hybrid-overlay is not ignored.

.. The Windows VM has a valid IP address in vCenter:
+
[source,terminal]
----
C:\> ipconfig
----

.. The VMTools Windows service is running:
+
[source,posh]
----
PS C:\> Get-Service -Name VMTools | Select Status, StartType
----

. Install and configure the OpenSSH Server on the Windows VM. See Microsoft's documentation on installing OpenSSH for more details.

. Set up SSH access for an administrative user. See Microsoft's documentation on the Administrative user to do this.
+
[IMPORTANT]
====
The public key used in the instructions must correspond to the private key you create later in the WMCO namespace that holds your secret. See the "Configuring a secret for the Windows Machine Config Operator" section for more details.
====

. You must create a new firewall rule in the Windows VM that allows incoming connections for container logs. Run the following PowerShell command to create the firewall rule on TCP port 10250:
+
[source,posh]
----
PS C:\> New-NetFirewallRule -DisplayName "ContainerLogsPort" -LocalPort 10250 -Enabled True -Direction Inbound -Protocol TCP -Action Allow -EdgeTraversalPolicy Allow
----

. Clone the Windows VM so it is a reusable image. Follow the VMware documentation on how to clone an existing virtual machine for more details.

. In the cloned Windows VM, run the Windows Sysprep tool:
+
[source,terminal]
----
C:\> C:\Windows\System32\Sysprep\sysprep.exe /generalize /oobe /shutdown /unattend:<path_to_unattend.xml>
----
+
Replace `<path_to_unattend.xml>` with the path to your `unattend.xml` file.
+
[NOTE]
====
There is a limit on how many times you can run the `sysprep` command on a Windows image. Consult Microsoft's documentation for more information.
====
+
An example `unattend.xml` is provided, which maintains all the changes needed for the WMCO. You must modify this example; it cannot be used directly.
+
.Example `unattend.xml`
[source,xml]
----
<?xml version="1.0" encoding="UTF-8"?>
<unattend xmlns="urn:schemas-microsoft-com:unattend">
   <settings pass="specialize">
      <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
         <InputLocale>0409:00000409</InputLocale>
         <SystemLocale>en-US</SystemLocale>
         <UILanguage>en-US</UILanguage>
         <UILanguageFallback>en-US</UILanguageFallback>
         <UserLocale>en-US</UserLocale>
      </component>
      <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Security-SPP-UX" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
         <SkipAutoActivation>true</SkipAutoActivation>
      </component>
      <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-SQMApi" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
         <CEIPEnabled>0</CEIPEnabled>
      </component>
      <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
         <ComputerName>winhost</ComputerName>
      </component>
   </settings>
   <settings pass="oobeSystem">
      <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
         <AutoLogon>
            <Enabled>false</Enabled>
         </AutoLogon>
         <OOBE>
            <HideEULAPage>true</HideEULAPage>
            <HideLocalAccountScreen>true</HideLocalAccountScreen>
            <HideOEMRegistrationScreen>true</HideOEMRegistrationScreen>
            <HideOnlineAccountScreens>true</HideOnlineAccountScreens>
            <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
            <NetworkLocation>Work</NetworkLocation>
            <ProtectYourPC>1</ProtectYourPC>
            <SkipMachineOOBE>true</SkipMachineOOBE>
            <SkipUserOOBE>true</SkipUserOOBE>
         </OOBE>
         <RegisteredOrganization>Organization</RegisteredOrganization>
         <RegisteredOwner>Owner</RegisteredOwner>
         <DisableAutoDaylightTimeSet>false</DisableAutoDaylightTimeSet>
         <TimeZone>Eastern Standard Time</TimeZone>
         <UserAccounts>
            <AdministratorPassword>
               <Value>MyPassword</Value>
               <PlainText>true</PlainText>
            </AdministratorPassword>
         </UserAccounts>
      </component>
   </settings>
</unattend>
----
+
where:

`<ComputerName>`:: Replace the `winhost` placeholder with a computer name, which must follow the Kubernetes' names specification. These specifications also apply to Guest OS customization performed on the resulting template while creating new VMs. For more information, see "Object Names and IDs specification (Kubernetes documentation)" in the _Additional resources_ section.
`<AutoLogon>.<Enabled>`:: When `false`, automatic logon is disabled to avoid the security issue of leaving an open terminal with Administrator privileges at boot. This is the default value and must not be changed.
`<UserAccounts>.<AdministratorPassword>.<Value>`:: Replace the `MyPassword` placeholder with the password for the Administrator account. This prevents the built-in Administrator account from having a blank password by default. Follow Microsoft's best practices for choosing a password. For more information on Microsoft's best practices, see "Password must meet complexity requirements (Microsoft documentation)" in the _Additional resources_ section.
+
After the Sysprep tool has completed, the Windows VM will power off. You must not use or power on this VM anymore.

. Convert the Windows VM to a template in vCenter. For more information, see "vSphere Virtual Machine Administration (vSphere documentation)" in the _Additional resources_ section.

// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc

[id="enabling-internal-api-server-vsphere_{context}"]
= Enabling communication with the internal API server for the WMCO on vSphere

[role="_abstract"]
You must enable communication with the internal API server so that your Windows virtual machine (VM) can download the Ignition config files, and the kubelet on the configured VM can only communicate with the internal API server.

The Windows Machine Config Operator (WMCO) can download the Ignition config files from the internal API server endpoint only after communication with the server is enabled.

.Prerequisites

* You have installed a cluster on vSphere.

.Procedure

* Add a new DNS entry for `api-int.<cluster_name>.<base_domain>` that points to the external API server URL `api.<cluster_name>.<base_domain>`. This can be a CNAME or an additional A record.
+
[NOTE]
====
The external API endpoint was already created as part of the initial cluster installation on vSphere.
====

// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc

[id="windows-machineset-vsphere_{context}"]
= Sample YAML for a Windows MachineSet object on vSphere

[role="_abstract"]
You can define a Windows `MachineSet` object running on {vmw-first} by creating a YAML file similar to the following example, which the Windows Machine Config Operator (WMCO) can react upon.

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <windows_machine_set_name>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: vsphereprovider.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          diskGiB: 128
          kind: VSphereMachineProviderSpec
          memoryMiB: 16384
          network:
            devices:
            - networkName: "<vm_network_name>"
          numCPUs: 4
          numCoresPerSocket: 1
          snapshot: ""
          template: <windows_vm_template_name>
          userDataSecret:
            name: windows-user-data
          workspace:
             datacenter: <vcenter_data_center_name>
             datastore: <vcenter_datastore_name>
             folder: <vcenter_vm_folder_path>
             resourcePool: <vsphere_resource_pool>
             server: <vcenter_server_ip>
----
where:

`metadata.labels`:: For the `machine.openshift.io/cluster-api-cluster` label, replace `<infrastructure_id>` with the infrastructure ID. You can obtain the infrastructure ID by running the following command: Specify the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
`metadata.name`:: Replace the infrastructure ID, worker label, and zone.
`spec.selector.matchLabels`:: Replace the parameters for the following labels:
* `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
* `machine.openshift.io/cluster-api-machineset`. Specify the Windows compute machine set name. The compute machine set name cannot be more than 9 characters long, due to the way machine names are generated in vSphere.
`spec.template.metadata.labels`:: Replace the parameters for the following labels:
* `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
* `machine.openshift.io/cluster-api-machineset`. Specify the Windows compute machine set name. The compute machine set name cannot be more than 9 characters long, due to the way machine names are generated in vSphere.
* `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.
`spec.template.spec.metadata.labels`::  When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.
`spec.template.spec.providerSpec`:: Specify the following parameters:
* `value.diskGiB`. Specifies the size of the vSphere Virtual Machine Disk (VMDK).
+
[NOTE]
====
This parameter does not set the size of the Windows partition. You can resize the Windows partition by using the `unattend.xml` file or by creating the vSphere Windows virtual machine (VM) golden image with the required disk size.
====
* `value.network.devices.networkName`. Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other Linux compute machines reside in the cluster.
* `value.template`. Specifies the full path of the Windows vSphere VM template to use, such as `golden-images/windows-server-template`. The name must be unique.
+
[IMPORTANT]
====
Do not specify the original VM template. The VM template must remain off and must be cloned for new Windows machines. Starting the VM template configures the VM template as a VM on the platform, which prevents it from being used as a template that compute machine sets can apply configurations to.
====
+
* `value.userDataSecret.name`. The `windows-user-data` is created by the WMCO when the first Windows machine is configured. After that, the `windows-user-data` is available for all subsequent compute machine sets to consume.
* `value.workspace.datacenter`. Specifies the vCenter data center to deploy the compute machine set on.
* `value.workspace.datastore`. Specifies the vCenter datastore to deploy the compute machine set on.
* `value.workspace.folder`. Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.
* `value.workspace.resourcePool`. Specifies the vSphere resource pool for your Windows VMs. This parameter is optional.
* `value.workspace.server`. Specifies the vCenter server IP or fully qualified domain name. This parameter is optional.

// Module included in the following assemblies:
//
// * machine_management/creating-infrastructure-machinesets.adoc
// * machine_management/creating_machinesets/creating-machineset-aws.adoc
// * machine_management/creating_machinesets/creating-machineset-azure.adoc
// * machine_management/creating_machinesets/creating-machineset-azure-stack-hub.adoc
// * machine_management/creating_machinesets/creating-machineset-gcp.adoc
// * machine_management/creating_machinesets/creating-machineset-osp.adoc
// * machine_management/creating_machinesets/creating-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-aws.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-azure.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-vsphere.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-gcp.adoc
// * post_installation_configuration/cluster-tasks.adoc
// * installing/installing_aws/aws-compute-edge-zone-tasks.adoc
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-nutanix.adoc

[id="machineset-creating_{context}"]
= Creating a compute machine set

[role="_abstract"]
To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

[NOTE]
====
Clusters that are installed with user-provisioned infrastructure have a different networking stack than clusters with infrastructure that is provisioned by the installation program. As a result of this difference, automatic load balancer management is unsupported on clusters that have user-provisioned infrastructure. For these clusters, a compute machine set can only create `worker` and `infra` type machines.
====

.Prerequisites

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* Have the necessary permissions to deploy VMs in your vCenter instance and have the required access to the datastore specified.
* If your cluster uses user-provisioned infrastructure, you have satisfied the specific Machine API requirements for that configuration.
* Create an availability set in which to deploy Azure Stack Hub compute machines.
* In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the OpenSSH server v0.0.1.0 installed.

.Procedure

. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.
+
Ensure that you set the `<clusterID>` and `<role>` parameter values.
Ensure that you set the `<availabilitySet>`, `<clusterID>`, and `<role>` parameter values.

. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

.. To list the compute machine sets in your cluster, run the following command:
+
[source,terminal]
----
$ oc get machinesets -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
----

.. To view values of a specific compute machine set custom resource (CR), run the following command:
+
[source,terminal]
----
$ oc get machineset <machineset_name> \
  -n openshift-machine-api -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-<role>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
    spec:
      providerSpec:
        ...
----
+
where:

`metadata.labels.machine.openshift.io/cluster-api-cluster`:: Specifies the cluster infrastructure ID.
`metadata.labels.name`:: Specifies a default node label.
+
[NOTE]
====
For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.
====
`spec.template.metadata.spec.providerSpec`:: Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
.. If you are creating a compute machine set for a cluster that has user-provisioned infrastructure, note the following important values:
+
.Example vSphere `providerSpec` values
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
...
template:
  ...
  spec:
    providerSpec:
      value:
        apiVersion: machine.openshift.io/v1beta1
        credentialsSecret:
          name: vsphere-cloud-credentials
        dataDisks:
        - name: <disk_name>
          provisioningMode: <mode>
          sizeGiB: 10
        diskGiB: 120
        kind: VSphereMachineProviderSpec
        memoryMiB: 16384
        network:
          devices:
            - networkName: "<vm_network_name>"
        numCPUs: 4
        numCoresPerSocket: 4
        snapshot: ""
        template: <vm_template_name>
        userDataSecret:
          name: worker-user-data
        workspace:
          datacenter: <vcenter_data_center_name>
          datastore: <vcenter_datastore_name>
          folder: <vcenter_vm_folder_path>
          resourcepool: <vsphere_resource_pool>
          server: <vcenter_server_address>
----
+
where:

`vsphere-cloud-credentials`:: Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required vCenter credentials.
`<disk_name>`:: Specifies the collection of data disk definitions. For more information, see "Configuring data disks by using machine sets".
`<vm_template_name>`:: Specifies the name of the {op-system} VM template for your cluster that was created during installation.
`worker-user-data`:: Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required Ignition configuration credentials.
`<vcenter_server_address>`:: Specifies the IP address or fully qualified domain name (FQDN) of the vCenter server.

. Create a `MachineSet` CR by running the following command:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----

. If you need compute machine sets in other availability zones, repeat this process to create more compute machine sets.

.Verification

* View the list of compute machine sets by running the following command:
+
[source,terminal]
----
$ oc get machineset -n openshift-machine-api
----
+
.Example output
[source,terminal]
----
NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
agl030519-vplxk-edge-us-east-1-nyc-1a      1         1         1       1           11m
agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d          0         0                             55m
agl030519-vplxk-worker-us-east-1e          0         0                             55m
agl030519-vplxk-worker-us-east-1f          0         0                             55m
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-infra-us-east-1a    1         1         1       1           11m
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
----
+
When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

* Optional: To check nodes that were created by the edge machine, run the following command:
+
[source,terminal]
----
$ oc get nodes -l node-role.kubernetes.io/edge
----
+
.Example output
[source,terminal]
----
NAME                           STATUS   ROLES         AGE    VERSION
ip-10-0-207-188.ec2.internal   Ready    edge,worker   172m   v1.25.2+d2e245f
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Configuring a secret for the Windows Machine Config Operator
* VMware vSphere infrastructure requirements
* Overview of machine management
* Object Names and IDs specification (Kubernetes documentation)
* Password must meet complexity requirements (Microsoft documentation)
* vSphere Virtual Machine Administration (vSphere documentation)
