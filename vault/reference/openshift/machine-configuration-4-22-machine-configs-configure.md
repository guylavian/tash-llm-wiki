---
title: "Using machine config objects to configure nodes"
type: reference
domain: openshift
slug: machine-configuration-4-22-machine-configs-configure
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/machine-configs-configure
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Using machine config objects to configure nodes

[id="machine-configs-configure"]
= Using machine config objects to configure nodes

[role="_abstract"]
You can use the tasks in this section to create `MachineConfig` objects that modify files, systemd unit files, and other operating system features running on OpenShift Container Platform nodes. This allows you to perform such tasks such as disabling chronyd, adding kernel arguments, enabling multipathing, and adding {op-system} extensions.

For more ideas on working with machine configs, see content related to updating SSH authorized keys, verifying image signatures, enabling SCTP, and configuring iSCSI initiatornames for OpenShift Container Platform.

OpenShift Container Platform supports Ignition specification version 3.5. You should base all new machine configs you create going forward on Ignition specification version 3.5. If you are upgrading your OpenShift Container Platform cluster, any existing machine configs with a previous Ignition specification will be translated automatically to specification version 3.5.

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called _configuration drift_. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated. For more information on configuration drift, see Understanding configuration drift detection.

[TIP]
====
Use the following "Configuring chrony time service" procedure as a model for how to go about adding other configuration files to OpenShift Container Platform nodes.
====

// Module included in the following assemblies:
//
// * installing/install_config/installing-customizing.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * machine_configuration/machine-configs-configure.adoc

[id="installation-special-config-chrony_{context}"]
= Configuring chrony time service

[role="_abstract"]
You
set the time server and related settings used by the chrony time service (`chronyd`)
by modifying the contents of the `chrony.conf` file and passing those contents
to your nodes as a machine config.

.Procedure

. Create a Butane config including the contents of the `chrony.conf` file. For example, to configure chrony on worker nodes, create a `99-worker-chrony.bu` file.
+
[NOTE]
====
====
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 99-worker-chrony
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  files:
  - path: /etc/chrony.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        pool 0.rhel.pool.ntp.org iburst
        driftfile /var/lib/chrony/drift
        makestep 1.0 3
        rtcsync
        logdir /var/log/chrony
----
+
--
* `name: 99-worker-chrony` - Specify a name for the machine config file. On control plane nodes, substitute `master` for `worker`.
* `machineconfiguration.openshift.io/role: worker` - On control plane nodes, substitute `master` for `worker`.
* `mode: 0644` - Specify an octal value mode for the `mode` field in the machine config file. After creating the file and applying the changes, the `mode` is converted to a decimal value. You can check the YAML file with the command `oc get mc <mc-name> -o yaml`.
* `pool 0.rhel.pool.ntp.org iburst` - Specify any valid, reachable time source, such as the one provided by your DHCP server.
--

+
[NOTE]
====
For all-machine to all-machine communication, the Network Time Protocol (NTP) on UDP is port `123`. If an external NTP time server is configured, you must open UDP port `123`.
====

. Use Butane to generate a `MachineConfig` object file, `99-worker-chrony.yaml`, containing the configuration to be delivered to the nodes:
+
[source,terminal]
----
$ butane 99-worker-chrony.bu -o 99-worker-chrony.yaml
----

. Apply the configurations in one of two ways:
+
* If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
+
* If the cluster is already running, apply the file:
+
[source,terminal]
----
$ oc apply -f ./99-worker-chrony.yaml
----

For more information on chrony best practices, see the following resources:

* https://access.redhat.com/solutions/3073261[Configuring chrony]
* https://access.redhat.com/solutions/778603[Best practices for NTP]
* https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/troubleshooting_guide/basic-chrony-NTP-troubleshooting_diag#basic-chrony-NTP-troubleshooting_diag[Basic chrony NTP troubleshooting]

// Module included in the following assemblies:
//
// * networking/using-ptp.adoc

[id="cnf-disable-chronyd_{context}"]
= Disabling the chrony time service

You can disable the chrony time service (`chronyd`) for nodes with a specific role by using a `MachineConfig` custom resource (CR).

.Prerequisites

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

.Procedure

. Create the `MachineConfig` CR that disables `chronyd` for the specified node role.

.. Save the following YAML in the `disable-chronyd.yaml` file:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: <node_role> <1>
  name: disable-chronyd
spec:
  config:
    ignition:
      version: 3.5.0
    systemd:
      units:
        - contents: |
            [Unit]
            Description=NTP client/server
            Documentation=man:chronyd(8) man:chrony.conf(5)
            After=ntpdate.service sntp.service ntpd.service
            Conflicts=ntpd.service systemd-timesyncd.service
            ConditionCapability=CAP_SYS_TIME
            [Service]
            Type=forking
            PIDFile=/run/chrony/chronyd.pid
            EnvironmentFile=-/etc/sysconfig/chronyd
            ExecStart=/usr/sbin/chronyd $OPTIONS
            ExecStartPost=/usr/libexec/chrony-helper update-daemon
            PrivateTmp=yes
            ProtectHome=yes
            ProtectSystem=full
            [Install]
            WantedBy=multi-user.target
          enabled: false
          name: "chronyd.service"
        - name: "kubelet-dependencies.target"
          contents: |
            [Unit]
            Description=Dependencies necessary to run kubelet
            Documentation=https://github.com/openshift/machine-config-operator/
            Requires=basic.target network-online.target
            Wants=NetworkManager-wait-online.service crio-wipe.service
            Wants=rpc-statd.service
----
<1> Node role where you want to disable `chronyd`, for example, `master`.

.. Create the `MachineConfig` CR by running the following command:
+
[source,terminal]
----
$ oc create -f disable-chronyd.yaml
----

// Module included in the following assemblies:
//
// * nodes/nodes-nodes-managing.adoc
// * machine_configuration/machine-configs-configure.adoc

[id="nodes-nodes-kernel-arguments_{context}"]
= Adding kernel arguments to nodes

[role="_abstract"]
In some special cases, you can add kernel arguments to a set of nodes in your cluster to customize the kernel behavior to meet specific needs you might have.

You should add kernel arguments with caution and a clear understanding of the implications of the arguments you set.

[WARNING]
====
Improper use of kernel arguments can result in your systems becoming unbootable.
====

Examples of kernel arguments you could set include:

* **nosmt**: Disables symmetric multithreading (SMT) in the kernel. Multithreading allows multiple logical threads for each CPU. You could consider `nosmt` in multi-tenant environments to reduce risks from potential cross-thread attacks. By disabling SMT, you essentially choose security over performance.

* **enforcing=0**: Configures Security Enhanced Linux (SELinux) to run in permissive mode. In permissive mode, the system acts as if SELinux is enforcing the loaded security policy, including labeling objects and emitting access denial entries in the logs, but it does not actually deny any operations. While not supported for production systems, permissive mode can be helpful for debugging.
+
[WARNING]
====
Disabling SELinux on {op-system} in production is not supported. After SELinux has been disabled on a node, it must be re-provisioned before re-inclusion in a production cluster.
====

See Kernel.org kernel parameters for a list and descriptions of kernel arguments.

In the following procedure, you create a `MachineConfig` object that identifies:

* A set of machines to which you want to add the kernel argument. In this case, machines with a worker role.
* Kernel arguments that are appended to the end of the existing kernel arguments.
* A label that indicates where in the list of machine configs the change is applied.

.Prerequisites

* You have `cluster-admin` privileges.
* Your cluster is running.

.Procedure

. List existing `MachineConfig` objects for your OpenShift Container Platform cluster to determine how to
label your machine config:
+
[source,terminal]
----
$ oc get MachineConfig
----
+
.Example output
[source,terminal]
----
NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
00-master                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
00-worker                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-master-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-master-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-worker-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-worker-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-master-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-master-ssh                                                                                 3.2.0             40m
99-worker-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-worker-ssh                                                                                 3.2.0             40m
rendered-master-23e785de7587df95a4b517e0647e5ab7   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
rendered-worker-5d596d9293ca3ea80c896a1191735bb1   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
----

. Create a `MachineConfig` object file that identifies the kernel argument (for example, `05-worker-kernelarg-selinuxpermissive.yaml`)
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 05-worker-kernelarg-selinuxpermissive
spec:
  kernelArguments:
    - enforcing=0
----
+
where:
+
`machineconfiguration.openshift.io/role`:: Specifies a label to apply changes to specific nodes.
`name`:: Specifies a name to identify where it fits among the machine configs (05) and what it does (adds a kernel argument to configure SELinux permissive mode).
`kernelArguments`:: Specifies the exact kernel argument as `enforcing=0`.

. Create the new machine config:
+
[source,terminal]
----
$ oc create -f 05-worker-kernelarg-selinuxpermissive.yaml
----

. Check the machine configs to see that the new one was added:
+
[source,terminal]
----
$ oc get MachineConfig
----
+
.Example output
[source,terminal]
----
NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
00-master                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
00-worker                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-master-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-master-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-worker-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-worker-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
05-worker-kernelarg-selinuxpermissive                                                         3.5.0             105s
99-master-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-master-ssh                                                                                 3.2.0             40m
99-worker-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-worker-ssh                                                                                 3.2.0             40m
rendered-master-23e785de7587df95a4b517e0647e5ab7   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
rendered-worker-5d596d9293ca3ea80c896a1191735bb1   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
----

. Check the nodes:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                           STATUS                     ROLES    AGE   VERSION
ip-10-0-136-161.ec2.internal   Ready                      worker   28m   v1.35.4
ip-10-0-136-243.ec2.internal   Ready                      master   34m   v1.35.4
ip-10-0-141-105.ec2.internal   Ready,SchedulingDisabled   worker   28m   v1.35.4
ip-10-0-142-249.ec2.internal   Ready                      master   34m   v1.35.4
ip-10-0-153-11.ec2.internal    Ready                      worker   28m   v1.35.4
ip-10-0-153-150.ec2.internal   Ready                      master   34m   v1.35.4
----
+
You can see that scheduling on each worker node is disabled as the change is being applied.

. Check that the kernel argument worked by going to one of the worker nodes and listing
the kernel command-line arguments (in `/proc/cmdline` on the host):
+
[source,terminal]
----
$ oc debug node/ip-10-0-141-105.ec2.internal
----
+
.Example output
[source,terminal]
----
Starting pod/ip-10-0-141-105ec2internal-debug ...
To use host binaries, run `chroot /host`

sh-4.2# cat /host/proc/cmdline
BOOT_IMAGE=/ostree/rhcos-... console=tty0 console=ttyS0,115200n8
rootflags=defaults,prjquota rw root=UUID=fd0... ostree=/ostree/boot.0/rhcos/16...
coreos.oem.id=qemu coreos.oem.id=ec2 ignition.platform.id=ec2 enforcing=0

sh-4.2# exit
----
+
You should see the `enforcing=0` argument added to the other kernel arguments.

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-configure.adoc

[id="rhcos-enabling-multipath-day-2_{context}"]
= Enabling multipathing with kernel arguments on {op-system}

[IMPORTANT]
====
Enabling multipathing during installation is supported and recommended for nodes provisioned in OpenShift Container Platform. In setups where any I/O to non-optimized paths results in I/O system errors, you must enable multipathing at installation time. For more information about enabling multipathing during installation time, see "Enabling multipathing post installation" in the _Installing on bare metal_ documentation.
====

{op-system-first} supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Postinstallation support is available by activating multipathing via the machine config.

[IMPORTANT]
====
On {ibm-z-name} and {ibm-linuxone-name}, you can enable multipathing only if you configured your cluster for it during installation. For more information, see "Installing {op-system} and starting the OpenShift Container Platform bootstrap process" in _Installing a cluster with z/VM on {ibm-z-name} and {ibm-linuxone-name}_.
====
// Add xref once it's allowed.

[IMPORTANT]
====
When an OpenShift Container Platform cluster is installed or configured as a postinstallation activity on a single VIOS host with "vSCSI" storage on {ibm-power-name} with multipath configured, the CoreOS nodes with multipath enabled fail to boot. This behavior is expected, as only one path is available to the node.
====

.Prerequisites
* You have a running OpenShift Container Platform cluster.
* You are logged in to the cluster as a user with administrative privileges.
* You have confirmed that the disk is enabled for multipathing. Multipathing is only supported on hosts that are connected to a SAN via an HBA adapter.

.Procedure

. To enable multipathing postinstallation on control plane nodes:

* Create a machine config file, such as `99-master-kargs-mpath.yaml`, that instructs the cluster to add the `master` label and that identifies the multipath kernel argument, for example:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: "master"
  name: 99-master-kargs-mpath
spec:
  kernelArguments:
    - 'rd.multipath=default'
    - 'root=/dev/disk/by-label/dm-mpath-root'
----

. To enable multipathing postinstallation on worker nodes:

* Create a machine config file, such as `99-worker-kargs-mpath.yaml`, that instructs the cluster to add the `worker` label and that identifies the multipath kernel argument, for example:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: "worker"
  name: 99-worker-kargs-mpath
spec:
  kernelArguments:
    - 'rd.multipath=default'
    - 'root=/dev/disk/by-label/dm-mpath-root'
----

. Create the new machine config by using either the master or worker YAML file you previously created:
+
[source,terminal]
----
$ oc create -f ./99-worker-kargs-mpath.yaml
----

. Check the machine configs to see that the new one was added:
+
[source,terminal]
----
$ oc get MachineConfig
----
+
.Example output
[source,terminal]
----
NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
00-master                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
00-worker                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-master-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-master-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-worker-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
01-worker-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-master-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-master-ssh                                                                                 3.2.0             40m
99-worker-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
99-worker-kargs-mpath                              52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             105s
99-worker-ssh                                                                                 3.2.0             40m
rendered-master-23e785de7587df95a4b517e0647e5ab7   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
rendered-worker-5d596d9293ca3ea80c896a1191735bb1   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
----

. Check the nodes:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                           STATUS                     ROLES    AGE   VERSION
ip-10-0-136-161.ec2.internal   Ready                      worker   28m   v1.35.4
ip-10-0-136-243.ec2.internal   Ready                      master   34m   v1.35.4
ip-10-0-141-105.ec2.internal   Ready,SchedulingDisabled   worker   28m   v1.35.4
ip-10-0-142-249.ec2.internal   Ready                      master   34m   v1.35.4
ip-10-0-153-11.ec2.internal    Ready                      worker   28m   v1.35.4
ip-10-0-153-150.ec2.internal   Ready                      master   34m   v1.35.4
----
+
You can see that scheduling on each worker node is disabled as the change is being applied.

. Check that the kernel argument worked by going to one of the worker nodes and listing
the kernel command-line arguments (in `/proc/cmdline` on the host):
+
[source,terminal]
----
$ oc debug node/ip-10-0-141-105.ec2.internal
----
+
.Example output
[source,terminal]
----
Starting pod/ip-10-0-141-105ec2internal-debug ...
To use host binaries, run `chroot /host`

sh-4.2# cat /host/proc/cmdline
...
rd.multipath=default root=/dev/disk/by-label/dm-mpath-root
...

sh-4.2# exit
----
+
You should see the added kernel arguments.

// Module included in the following assemblies:
//
// * nodes/nodes/nodes-nodes-managing.adoc
// * machine_configuration/machine-configs-configure.adoc

[id="nodes-nodes-rtkernel-arguments_{context}"]
= Adding a real-time kernel to nodes

[role="_abstract"]
If your OpenShift Container Platform workloads require real-time operating system characteristics, you can switch your machines to the Linux real-time kernel. Switching to the real-time kernel provides a higher degree of determinism for your OpenShift Container Platform workloads.

Even though Linux is not a real-time operating system, the Linux real-time
kernel includes a preemptive scheduler that provides the operating system with real-time characteristics. For OpenShift Container Platform,  you can make the switch to real-time kernel by using a `MachineConfig` object.

Although making the change is as simple as changing a machine config `kernelType` setting to `realtime`, there are a few other considerations before making the change:

* Currently, real-time kernel is supported only on worker nodes, and only for radio access network (RAN) use.
* The following procedure is fully supported with bare metal installations that use systems that are certified for Red Hat Enterprise Linux for Real Time 8.
* Real-time support in OpenShift Container Platform is limited to specific subscriptions.
* The following procedure is also supported for use with {gcp-full}.

.Prerequisites
* Have a running OpenShift Container Platform cluster (version 4.4 or later).
* Log in to the cluster as a user with administrative privileges.

.Procedure

. Create a machine config for the real-time kernel: Create a YAML file (for example, `99-worker-realtime.yaml`) that contains a `MachineConfig`
object for the `realtime` kernel type. This example tells the cluster to use a real-time kernel for all worker nodes:
+
[source,terminal]
----
$ cat << EOF > 99-worker-realtime.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: "worker"
  name: 99-worker-realtime
spec:
  kernelType: realtime
EOF
----

. Add the machine config to the cluster. Type the following to add the machine config to the cluster:
+
[source,terminal]
----
$ oc create -f 99-worker-realtime.yaml
----

. Check the real-time kernel: Once each impacted node reboots, log in to the cluster and run the following commands to make sure that the real-time kernel has replaced the regular kernel for the set of nodes you configured:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                                        STATUS  ROLES    AGE   VERSION
ip-10-0-143-147.us-east-2.compute.internal  Ready   worker   103m  v1.35.4
ip-10-0-146-92.us-east-2.compute.internal   Ready   worker   101m  v1.35.4
ip-10-0-169-2.us-east-2.compute.internal    Ready   worker   102m  v1.35.4
----
+
[source,terminal]
----
$ oc debug node/ip-10-0-143-147.us-east-2.compute.internal
----
+
.Example output
[source,terminal]
----
Starting pod/ip-10-0-143-147us-east-2computeinternal-debug ...
To use host binaries, run `chroot /host`

sh-4.4# uname -a
Linux <worker_node> 4.18.0-147.3.1.rt24.96.el8_1.x86_64 #1 SMP PREEMPT RT
        Wed Nov 27 18:29:55 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
----
+
The kernel name contains `rt` and text “PREEMPT RT” indicates that this is a real-time kernel.

. To go back to the regular kernel, delete the `MachineConfig` object:
+
[source,terminal]
----
$ oc delete -f 99-worker-realtime.yaml
----

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-configure.adoc

[id="machineconfig-modify-journald_{context}"]
= Configuring journald settings

If you need to configure settings for the `journald` service on OpenShift Container Platform nodes, you can do that by modifying the appropriate configuration file and passing the file to the appropriate pool of nodes as a machine config.

This procedure describes how to modify `journald` rate limiting settings in the `/etc/systemd/journald.conf` file and apply them to worker nodes. See the `journald.conf` man page for information on how to use that file.

.Prerequisites
* Have a running OpenShift Container Platform cluster.
* Log in to the cluster as a user with administrative privileges.

.Procedure

. Create a Butane config file, `40-worker-custom-journald.bu`, that includes an `/etc/systemd/journald.conf` file with the required settings.
+
[NOTE]
====
====
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 40-worker-custom-journald
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  files:
  - path: /etc/systemd/journald.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        # Disable rate limiting
        RateLimitInterval=1s
        RateLimitBurst=10000
        Storage=volatile
        Compress=no
        MaxRetentionSec=30s
----

. Use Butane to generate a `MachineConfig` object file, `40-worker-custom-journald.yaml`, containing the configuration to be delivered to the worker nodes:
+
[source,terminal]
----
$ butane 40-worker-custom-journald.bu -o 40-worker-custom-journald.yaml
----

. Apply the machine config to the pool:
+
[source,terminal]
----
$ oc apply -f 40-worker-custom-journald.yaml
----

. Check that the new machine config is applied and that the nodes are not in a degraded state. It might take a few minutes. The worker pool will show the updates in progress, as each node successfully has the new machine config applied:
+
[source,terminal]
----
$ oc get machineconfigpool
----
+
.Example output
[source,terminal]
----
NAME   CONFIG             UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE
master rendered-master-35 True    False    False    3            3                 3                   0                    34m
worker rendered-worker-d8 False   True     False    3            1                 1                   0                    34m
----

. To check that the change was applied, you can log in to a worker node:
+
[source,terminal]
----
$ oc get node | grep worker
----
+
.Example output
[source,terminal]
----
ip-10-0-0-1.us-east-2.compute.internal   Ready    worker   39m   v0.0.0-master+$Format:%h$
----
+
[source,terminal]
----
$ oc debug node/ip-10-0-0-1.us-east-2.compute.internal
----
+
.Example output
[source,terminal]
----
Starting pod/ip-10-0-141-142us-east-2computeinternal-debug ...
...
sh-4.2# chroot /host
sh-4.4# cat /etc/systemd/journald.conf
# Disable rate limiting
RateLimitInterval=1s
RateLimitBurst=10000
Storage=volatile
Compress=no
MaxRetentionSec=30s
sh-4.4# exit
----

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-configure.adoc

[id="rhcos-add-extensions_{context}"]

= Adding extensions to {op-system}

{op-system} is a minimal container-oriented RHEL operating system, designed to provide a common set of capabilities to OpenShift Container Platform clusters across all platforms. Although adding software packages to {op-system} systems is generally discouraged, the MCO provides an `extensions` feature you can use to add a minimal set of features to {op-system} nodes.

Currently, the following extensions are available:

* **usbguard**: The `usbguard` extension protects {op-system} systems from attacks by intrusive USB devices. For more information, see USBGuard for details.

* **kerberos**: The `kerberos` extension provides a mechanism that allows both users and machines to identify themselves to the network to receive defined, limited access to the areas and services that an administrator has configured. For more information, see Using Kerberos for details, including how to set up a Kerberos client and mount a Kerberized NFS share.

* **sandboxed-containers**: The `sandboxed-containers` extension contains RPMs for Kata, QEMU, and its dependencies. For more information, see https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/latest[OpenShift Sandboxed Containers].

* **ipsec**: The `ipsec` extension contains RPMs for libreswan and NetworkManager-libreswan.

* **wasm**: The `wasm` extension enables Developer Preview functionality in OpenShift Container Platform for users who want to use WASM-supported workloads.

* **sysstat**: Adding the `sysstat` extension provides additional performance monitoring for OpenShift Container Platform nodes, including the system activity reporter (`sar`) command for collecting and reporting information.

* **kernel-devel**: The `kernel-devel` extension provides kernel headers and makefiles sufficient to build modules against the kernel package.

The following procedure describes how to use a machine config to add one or more extensions to your {op-system} nodes.

.Prerequisites
* Have a running OpenShift Container Platform cluster (version 4.6 or later).
* Log in to the cluster as a user with administrative privileges.

.Procedure

. Create a machine config for extensions: Create a YAML file (for example, `80-extensions.yaml`) that contains a `MachineConfig` `extensions` object. This example tells the cluster to add the `usbguard` extension.
+
[source,terminal]
----
$ cat << EOF > 80-extensions.yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 80-worker-extensions
spec:
  config:
    ignition:
      version: 3.5.0
  extensions:
    - usbguard
EOF
----

. Add the machine config to the cluster. Type the following to add the machine config to the cluster:
+
[source,terminal]
----
$ oc create -f 80-extensions.yaml
----
+
This sets all worker nodes to have rpm packages for `usbguard` installed.

. Check that the extensions were applied:
+
[source,terminal]
----
$ oc get machineconfig 80-worker-extensions
----
+
.Example output
+
[source,terminal]
----
NAME                 GENERATEDBYCONTROLLER IGNITIONVERSION AGE
80-worker-extensions                       3.5.0           57s
----

. Check that the new machine config is now applied and that the nodes are not in a degraded state. It may take a few minutes. The worker pool will show the updates in progress, as each machine successfully has the new machine config applied:
+
[source,terminal]
----
$ oc get machineconfigpool
----
+
.Example output
+
[source,terminal]
----
NAME   CONFIG             UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE
master rendered-master-35 True    False    False    3            3                 3                   0                    34m
worker rendered-worker-d8 False   True     False    3            1                 1                   0                    34m
----

. Check the extensions. To check that the extension was applied, run:
+
[source,terminal]
----
$ oc get node | grep worker
----
+
.Example output
+
[source,terminal]
----
NAME                                        STATUS  ROLES    AGE   VERSION
ip-10-0-169-2.us-east-2.compute.internal    Ready   worker   102m  v1.35.4
----
+
[source,terminal]
----
$ oc debug node/ip-10-0-169-2.us-east-2.compute.internal
----
+
.Example output
+
[source,terminal]
----
...
To use host binaries, run `chroot /host`
sh-4.4# chroot /host
sh-4.4# rpm -q usbguard
usbguard-0.7.4-4.el8.x86_64.rpm
----

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-configure.adoc

[id="rhcos-load-firmware-blobs_{context}"]
= Loading custom firmware blobs in the machine config manifest

Because the default location for firmware blobs in `/usr/lib` is read-only, you can locate a custom firmware blob by updating the search path. This enables you to load local firmware blobs in the machine config manifest when the blobs are not managed by {op-system}.

.Procedure

. Create a Butane config file, `98-worker-firmware-blob.bu`, that updates the search path so that it is root-owned and writable to local storage. The following example places the custom blob file from your local workstation onto nodes under `/var/lib/firmware`.
+
[NOTE]
====
====
+
.Butane config file for custom firmware blob
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 98-worker-firmware-blob
storage:
  files:
  - path: /var/lib/firmware/<package_name> <1>
    contents:
      local: <package_name> <2>
    mode: 0644 <3>
openshift:
  kernel_arguments:
    - 'firmware_class.path=/var/lib/firmware' <4>
----
+
<1> Sets the path on the node where the firmware package is copied to.
<2> Specifies a file with contents that are read from a local file directory on the system running Butane. The path of the local file is relative to a `files-dir` directory, which must be specified by using the `--files-dir` option with Butane in the following step.
<3> Sets the permissions for the file on the {op-system} node. It is recommended to set `0644` permissions.
<4> The `firmware_class.path` parameter customizes the kernel search path of where to look for the custom firmware blob that was copied from your local workstation onto the root file system of the node. This example uses `/var/lib/firmware` as the customized path.

. Run Butane to generate a `MachineConfig` object file that uses a copy of the firmware blob on your local workstation named `98-worker-firmware-blob.yaml`. The firmware blob contains the configuration to be delivered to the nodes. The following example uses the `--files-dir` option to specify the directory on your workstation where the local file or files are located:
+
[source,terminal]
----
$ butane 98-worker-firmware-blob.bu -o 98-worker-firmware-blob.yaml --files-dir <directory_including_package_name>
----
. Apply the configurations to the nodes in one of two ways:
+
* If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
+
* If the cluster is already running, apply the file:
+
[source,terminal]
----
$ oc apply -f 98-worker-firmware-blob.yaml
----
+
A `MachineConfig` object YAML file is created for you to finish configuring your machines.
+
. Save the Butane config in case you need to update the `MachineConfig` object in the future.

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-configure.adoc

[id="core-user-password_{context}"]
= Changing the core user password for node access

By default, {op-system-first} creates a user named `core` on the nodes in your cluster. You can use the `core` user to access the node through a cloud provider serial console or a bare metal baseboard controller manager (BMC). This can be helpful, for example, if a node is down and you cannot access that node by using SSH or the `oc debug node` command. However, by default, there is no password for this user, so you cannot log in without creating one.

You can create a password for the `core` user by using a machine config. The Machine Config Operator (MCO) assigns the password and injects the password into the `/etc/shadow` file, allowing you to log in with the `core` user. The MCO does not examine the password hash. As such, the MCO cannot report if there is a problem with the password.

[NOTE]
====
* The password works only through a cloud provider serial console or a BMC. It does not work with SSH.

* If you have a machine config that includes an `/etc/shadow` file or a systemd unit that sets a password, it takes precedence over the password hash.
====

You can change the password, if needed, by editing the machine config you used to create the password. Also, you can remove the password by deleting the machine config. Deleting the machine config does not remove the user account.

.Procedure
. Using a tool that is supported by your operating system, create a hashed password. For example, create a hashed password using `mkpasswd` by running the following command:
+
[source,terminal]
----
$ mkpasswd -m SHA-512 testpass
----
+
.Example output
[source,terminal]
----
$ $6$CBZwA6s6AVFOtiZe$aUKDWpthhJEyR3nnhM02NM1sKCpHn9XN.NPrJNQ3HYewioaorpwL3mKGLxvW0AOb4pJxqoqP4nFX77y0p00.8.
----
. Create a machine config file that contains the `core` username and the hashed password:
+
[source,terminal]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: set-core-user-password
spec:
  config:
    ignition:
      version: 3.5.0
    passwd:
      users:
      - name: core <1>
        passwordHash: <password> <2>
----
<1> This must be `core`.
<2> The hashed password to use with the `core` account.

. Create the machine config by running the following command:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
The nodes do not reboot and should become available in a few moments. You can use the `oc get mcp` to watch for the machine config pools to be updated, as shown in the following example:
+
----
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-d686a3ffc8fdec47280afec446fce8dd   True      False      False      3              3                   3                     0                      64m
worker   rendered-worker-4605605a5b1f9de1d061e9d350f251e5   False     True       False      3              0                   0                     0                      64m
----

.Verification

. After the nodes return to the `UPDATED=True` state, start a debug session for a node by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Set `/host` as the root directory within the debug shell by running the following command:
+
[source,terminal]
----
sh-4.4# chroot /host
----

. Check the contents of the `/etc/shadow` file:
+
.Example output
[source,terminal]
----
...
core:$6$2sE/010goDuRSxxv$o18K52wor.wIwZp:19418:0:99999:7:::
...
----
+
The hashed password is assigned to the `core` user.

// Module included in the following assemblies:
//
// * machine_configuration/machine-configs-configure.adoc

[id="machine-config-install-time-configs_{context}"]
= Overriding storage or partition setup

[role="_abstract"]
You can use a `MachineConfig` object to change the disk partition schema, file systems, and RAID configurations that were established during the cluster installation. This allows you to make specific configuration changes that are different from the initial cluster state.

If you specified storage and partition configuration upon cluster installation by using a Butane config, Ignition config, or machine config, those configurations become defaults within your cluster. If you create new nodes, those nodes automatically use those default configurations.

You cannot change these components directly. By default, the Machine Config Operator (MCO) reviews changes in `MachineConfig` objects for specific fields and blocks some changes for security reasons. However, you can override this restriction for disk partition schema, file systems, and RAID configurations by adding the `irreconcilableValidationOverrides` parameter to the `MachineConfiguration` object. Then, you can create a new machine config to make the necessary changes for new nodes.

[NOTE]
====
Configuration changes made through this process apply to new nodes only.
====

For example, you might want to override your default storage configuration to add new hardware that uses a different storage partitioning schema or storage file system to your cluster. In this case, you can modify the storage configuration for any new nodes in your cluster.

Or, if you used Ignition to modify the storage configuration as a post-installation task, your cluster might be reporting an `irreconcilableChanges` status in the `MachineConfigNode` object status fields. This messaging can alert you to these differences, so that you can determine if you want new hardware with the new configurations.

.Prerequisites

* You enabled the required Technology Preview features for your cluster by adding the `TechPreviewNoUpgrade` feature set to the `FeatureGate` CR named `cluster`. For information about enabling Feature Gates, see _Enabling features using feature gates_.
+
[WARNING]
====
Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them. Do not enable this feature set on production clusters.
====

.Procedure

. Edit the `MachineConfiguration` object by using the following command:
+
[source,terminal]
----
$ oc edit machineconfiguration
----

. Add the `irreconcilableValidationOverrides` stanza to the `MachineConfiguration` object.
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
# ...
spec:
  irreconcilableValidationOverrides:
    storage:
    - Disks
    - Raid
    - FileSystems
# ...
----
where:
+
--
`spec.irreconcilableValidationOverrides.storage.Disks`:: Allows you to modify the installed storage disk configuration to be used with new nodes. This field is optional.

`spec.irreconcilableValidationOverrides.storage.Raid`:: Allows you to modify the installed RAID configuration to be used with new nodes. This field is optional.

`spec.irreconcilableValidationOverrides.storage.FileSystems`:: Allows you to modify the installed file system configuration to be used with new nodes. This field is optional.
--

. Create a YAML file for a `MachineConfig` object with the changes that you need, similar to the following:
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: extra-disks
spec:
  config:
    ignition:
      version: "3.5.0"
    storage:
      disks:
      - device: "/dev/sdb"
        wipeTable: true
        partitions:
        - label: raid.1.1
          number: 1
          sizeMiB: 1024
          startMiB: 0
      - device: "/dev/sdc"
        wipeTable: true
        partitions:
        - label: raid.1.2
          number: 1
          sizeMiB: 1024
          startMiB: 0
      raid:
      - devices:
        - "/dev/disk/by-partlabel/raid.1.1"
        - "/dev/disk/by-partlabel/raid.1.2"
        level: stripe
        name: data
      filesystems:
      - device: "/dev/md/data"
        path: "/var/lib/data"
        format: ext4
        label: DATA
----
where:

`spec.config.storage.disks`:: Specifies changes to the installed storage disk configuration in Ignition format. This field is optional.

`spec.config.storage.raid`:: Specifies changes to the installed RAID configuration in Ignition format. This field is optional.

`spec.config.storage.filesystems`:: Specifies changes to the installed file system configuration in Ignition format. This field is optional.

. Create the `MachineConfig` object by using a command similar to the following:
+
[source,terminal]
----
$ oc create -f <file_name>.yaml
----
+
When you create a new node from a machine set with the associated label, the new configurations are applied to the node.

Hide for the GA release. Need to verify the verification.
.Verification

. View the changes in the created machine set by using a command similar to the following:
+
[source,terminal]
----
$ oc edit mc
----
+
[source,yaml]
----
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  name: rendered-worker-b640f52876a9bf7fe636fee0a0164ae1
# ...
spec
  config
# ...
    storage:
      disks:
      - device: /dev/sdb
        partitions:
        - label: raid.1.1
          number: 1
          sizeMiB: 1024
          startMiB: 0
        wipeTable: true
      - device: /dev/sdc
        partitions:
        - label: raid.1.2
          number: 1
          sizeMiB: 1024
          startMiB: 0
        wipeTable: true
     files:
# ...
      filesystems:
      - device: /dev/md/data
        format: ext4
        label: DATA
        path: /var/lib/data
      raid:
      - devices:
        - /dev/disk/by-partlabel/raid.1.1
        - /dev/disk/by-partlabel/raid.1.2
        level: stripe
        name: data
# ...
----

. Open an `oc debug` session to a node by running a command similar to the following:
+
[source,terminal]
----
$ oc debug node/<node_name>
----
+
. Set `/host` as the root directory within the debug shell by running the following command:
+
[source,terminal]
----
sh-5.1# chroot /host
----
+
. Ensure the raid exists and that the file system can be mounted by using commands similar to the following:
+
[source,terminal]
----
sh-5.1# mount /dev/md/data /var/lib/data
----
+
[source,terminal]
----
sh-5.1# mdadm --detail --scan
----
+
.Example output
[source,terminal]
----
ARRAY /dev/md/data metadata=1.2 UUID=9989eb57:2fa9774c:b57cc2cc:70ac303e
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Creating machine configs with Butane
* Enabling multipathing with kernel arguments on RHCOS
* Creating machine configs with Butane
* Enabling features using feature gates
