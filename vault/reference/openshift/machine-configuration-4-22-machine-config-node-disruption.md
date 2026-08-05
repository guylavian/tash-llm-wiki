---
title: "Using node disruption policies to minimize disruption from machine config changes"
type: reference
domain: openshift
slug: machine-configuration-4-22-machine-config-node-disruption
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_configuration/machine-config-node-disruption
version: 4.22
family: machine_configuration
documentKind: "Documentation"
---

# Using node disruption policies to minimize disruption from machine config changes

[id="machine-config-node-disruption_{context}"]
= Using node disruption policies to minimize disruption from machine config changes

By default, when you make certain changes to the fields in a `MachineConfig` object, the Machine Config Operator (MCO) drains and reboots the nodes associated with that machine config. However, you can create a _node disruption policy_ that defines a set of changes to some Ignition config objects that would require little or no disruption to your workloads.

[NOTE]
====
Node disruption policies are not supported for on-cluster custom layered images.
====

A node disruption policy allows you to define the configuration changes that cause a disruption to your cluster, and which changes do not. This allows you to reduce node downtime when making small machine configuration changes in your cluster. To configure the policy, you modify the `MachineConfiguration` object, which is in the `openshift-machine-config-operator` namespace. See the example node disruption policies in the `MachineConfiguration` objects that follow.

[NOTE]
====
There are machine configuration changes that always require a reboot, regardless of any node disruption policies. For more information, see _About the Machine Config Operator_.
====

After you create the node disruption policy, the MCO validates the policy to search for potential issues in the file, such as problems with formatting. The MCO then merges the policy with the cluster defaults and populates the `status.nodeDisruptionPolicyStatus` fields in the machine config with the actions to be performed upon future changes to the machine config. The configurations in your policy always overwrite the cluster defaults.

[IMPORTANT]
====
The MCO does not validate whether a change can be successfully applied by your node disruption policy. Therefore, you are responsible to ensure the accuracy of your node disruption policies.
====

For example, you can configure a node disruption policy so that sudo configurations do not require a node drain and reboot. Or, you can configure your cluster so that updates to `sshd` are applied with only a reload of that one service.

You can control the behavior of the MCO when making the changes to the following Ignition configuration objects:

// I used this wording for the objects to match the previous section in the assembly: file:///home/mburke/openshift-docs/_preview/openshift-enterprise/mco-node-disruption-policy/post_installation_configuration/machine-configuration-tasks.html#what-can-you-change-with-machine-configs.
* *configuration files*: You add to or update the files in the `/var` or `/etc` directory. You can configure a policy for a specific file anywhere in the directory or for a path to a specific directory. For a path, a change or addition to any file in that directory triggers the policy.
+
[NOTE]
====
If a file is included in more than one policy, only the policy with the best match to that file is applied.

For example, if you have a policy for the `/etc/` directory and a policy for the `/etc/pki/` directory, a change to the `/etc/pki/tls/certs/ca-bundle.crt` file would apply the `etc/pki` policy.
====

* *systemd units*: You create and set the status of a systemd service or modify a systemd service.
* *users and groups*: You change SSH keys in the `passwd` section postinstallation.
* *ICSP*, *ITMS*, *IDMS* objects: You can remove mirroring rules from an `ImageContentSourcePolicy` (ICSP), `ImageTagMirrorSet` (ITMS), and `ImageDigestMirrorSet` (IDMS) object.

// Module included in the following assemblies:
//
// * machine_configuration/machine-config-node-disruption_machine-configs-configure.adoc

[id="machine-config-node-disruption-example_{context}"]
= Example node disruption policies

The following example `MachineConfiguration` objects contain a node disruption policy.

[TIP]
====
A `MachineConfiguration` object and a `MachineConfig` object are different objects. A `MachineConfiguration` object is a singleton object in the MCO namespace that contains configuration parameters for the MCO operator. A `MachineConfig` object defines changes that are applied to a machine config pool.
====

The following example `MachineConfiguration` object shows no user defined policies. The default node disruption policy values are shown in the `status` stanza.

.Default node disruption policy
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
  logLevel: Normal
  managementState: Managed
  operatorLogLevel: Normal
status:
  nodeDisruptionPolicyStatus:
    clusterPolicies:
      files:
      - actions:
        - type: None
        path: /etc/mco/internal-registry-pull-secret.json
      - actions:
        - type: None
        path: /var/lib/kubelet/config.json
      - actions:
        - reload:
            serviceName: crio.service
          type: Reload
        path: /etc/machine-config-daemon/no-reboot/containers-gpg.pub
      - actions:
        - reload:
            serviceName: crio.service
          type: Reload
        path: /etc/containers/policy.json
      - actions:
        - type: Special
        path: /etc/containers/registries.conf
      - actions:
        - reload:
            serviceName: crio.service
          type: Reload
        path: /etc/containers/registries.d
      - actions:
        - type: None
        path: /etc/nmstate/openshift
      - actions:
        - restart:
            serviceName: coreos-update-ca-trust.service
          type: Restart
        - restart:
            serviceName: crio.service
          type: Restart
        path: /etc/pki/ca-trust/source/anchors/openshift-config-user-ca-bundle.crt
      sshkey:
        actions:
        - type: None
  observedGeneration: 9
----

The default node disruption policy does not contain a policy for changes to the `/etc/containers/registries.conf.d` file. This is because both OpenShift Container Platform and {op-system-base-full} use the `registries.conf.d` file to specify aliases for image short names. It is recommended that you always pull an image by its fully-qualified name. This is particularly important with public registries, because the image might not deploy if the public registry requires authentication. You can create a user-defined policy to use with the `/etc/containers/registries.conf.d` file, if you need to use image short names.

In the following example, when changes are made to the SSH keys, the MCO drains the cluster nodes, reloads the `crio.service`, reloads the systemd configuration, and restarts the `crio-service`.

.Example node disruption policy for an SSH key change
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    sshkey:
      actions:
      - type: Drain
      - reload:
          serviceName: crio.service
        type: Reload
      - type: DaemonReload
      - restart:
          serviceName: crio.service
        type: Restart
# ...
----

In the following example, when changes are made to the `/etc/chrony.conf` file, the MCO restarts the `chronyd.service` on the cluster nodes. If files are added to or modified in the `/var/run` directory, the MCO applies the changes with no further action.

.Example node disruption policy for a configuration file change
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    files:
    - actions:
      - restart:
          serviceName: chronyd.service
        type: Restart
      path: /etc/chrony.conf
    - actions:
      - type: None
      path: /var/run
----

In the following example, when changes are made to the `auditd.service`	systemd unit, the MCO drains the cluster nodes, reloads the `crio.service`, reloads the systemd manager configuration, and restarts the `crio.service`.

.Example node disruption policy for a systemd unit change
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    units:
      - name: auditd.service
        actions:
          - type: Drain
          - type: Reload
            reload:
              serviceName: crio.service
          - type: DaemonReload
          - type: Restart
            restart:
              serviceName: crio.service
----

In the following example, when changes are made to the `registries.conf` file, such as by editing an `ImageContentSourcePolicy` (ICSP) object, the MCO does not drain or reboot the nodes and applies the changes with no further action.

.Example node disruption policy for a registries.conf file change
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    files:
      - actions:
        - type: None
        path: /etc/containers/registries.conf
----

// Module included in the following assemblies:
//
// * machine_configuration/machine-config-node-disruption_machine-configs-configure.adoc

[id="machine-config-node-disruption-config_{context}"]
= Configuring node restart behaviors upon machine config changes

You can create a node disruption policy to define the machine configuration changes that cause a disruption to your cluster, and which changes do not.

You can control how your nodes respond to changes in the files in the `/var` or `/etc` directory, the systemd units, the SSH keys, and the `registries.conf` file.

.Procedure

. Edit the `machineconfigurations.operator.openshift.io` object to define the node disruption policy:
+
[source,terminal]
----
$ oc edit MachineConfiguration cluster -n openshift-machine-config-operator
----

. Add a node disruption policy similar to the following:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy: <1>
    files: # <2>
    - actions: # <3>
      - restart: # <4>
          serviceName: chronyd.service # <5>
        type: Restart
      path: /etc/chrony.conf # <6>
    sshkey: # <7>
      actions:
      - type: Drain
      - reload:
          serviceName: crio.service
        type: Reload
      - type: DaemonReload
      - restart:
          serviceName: crio.service
        type: Restart
    units: # <8>
    - actions:
      - type: Drain
      - reload:
          serviceName: crio.service
        type: Reload
      - type: DaemonReload
      - restart:
          serviceName: crio.service
        type: Restart
      name: test.service
----
<1> Specifies the node disruption policy.
<2> Specifies a list of machine config file definitions and actions to take to changes on those paths. This list supports a maximum of 50 entries.
<3> Specifies the series of actions to be executed upon changes to the specified files. Actions are applied in the order that they are set in this list. This list supports a maximum of 10 entries.
<4> Specifies that the listed service is to be reloaded upon changes to the specified files.
<5> Specifies the full name of the service to be acted upon.
<6> Specifies the location of a file that is managed by a machine config. The actions in the policy apply when changes are made to the file in `path`.
<7> Specifies a list of service names and actions to take upon changes to the SSH keys in the cluster.
<8> Specifies a list of systemd unit names and actions to take upon changes to those units.

.Verification

* View the `MachineConfiguration` object file that you created:
+
----
$ oc get MachineConfiguration/cluster -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: cluster
# ...
status:
  nodeDisruptionPolicyStatus: <1>
    clusterPolicies:
      files:
# ...
      - actions:
        - restart:
            serviceName: chronyd.service
          type: Restart
        path: /etc/chrony.conf
      sshkey:
        actions:
        - type: Drain
        - reload:
            serviceName: crio.service
          type: Reload
        - type: DaemonReload
        - restart:
            serviceName: crio.service
          type: Restart
      units:
      - actions:
        - type: Drain
        - reload:
            serviceName: crio.service
          type: Reload
        - type: DaemonReload
        - restart:
            serviceName: crio.service
          type: Restart
        name: test.se
# ...
----
<1> Specifies the current cluster-validated policies.
