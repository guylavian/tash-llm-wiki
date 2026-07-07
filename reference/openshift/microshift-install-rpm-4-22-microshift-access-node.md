---
title: "Accessing the {microshift-short} node with oc"
type: reference
domain: openshift
slug: microshift-install-rpm-4-22-microshift-access-node
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_install_rpm/microshift-access-node
version: 4.22
family: microshift_install_rpm
documentKind: "Documentation"
---

# Accessing the {microshift-short} node with oc

[id="microshift-access-node"]
= Accessing the {microshift-short} node with oc

[role="_abstract"]
Access a {microshift-short} node with the {oc-first}.

// Module included in the following assemblies:
//
// microshift_install_rpm/microshift-install-rpm.adoc
// microshift_install_rpm_ostree/microshift-embed-in-rpm-ostree.adoc

[id="accessing-microshift-node_{context}"]
= How to access the {microshift-short} node

[role="_abstract"]
Access the {microshift-short} service by using the {oc-first}.

* You can access the node from either the same machine running the {microshift-short} service or from a remote location.
* You can use this access to observe and administer workloads.
* When using the following steps, choose the `kubeconfig` file that has the hostname or IP address you want to connect to and place it in the relevant directory.

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

[id="additional-resources_microshift-access-node"]
[role="_additional-resources"]
== Additional resources

* Installing the OpenShift CLI tool
* Node access with kubeconfig files
