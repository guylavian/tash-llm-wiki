---
title: "Uninstalling a cluster on {rh-openstack} from your own infrastructure"
type: reference
domain: openshift
slug: installing-4-22-uninstalling-openstack-user
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/uninstalling-openstack-user
version: 4.22
family: installing
documentKind: "Documentation"
---

# Uninstalling a cluster on {rh-openstack} from your own infrastructure

[id="uninstalling-openstack-user"]
= Uninstalling a cluster on {rh-openstack} from your own infrastructure

You can remove a cluster that you deployed to {rh-openstack-first} on user-provisioned infrastructure.

// include::modules/installation-uninstall-clouds.adoc[leveloffset=+1]
// Module included in the following assemblies:
// * installing/installing_openstack/installing-openstack-installer-user.adoc
// * installing/installing_openstack/uninstalling-openstack-user.adoc
//
//YOU MUST SET AN IFEVAL FOR EACH NEW MODULE

[id="installation-osp-downloading-modules_{context}"]
= Downloading playbook dependencies

The Ansible playbooks that simplify the installation process on user-provisioned infrastructure require several ansible collections and Python modules. On the machine where you will run the installation program, add the {rh-openstack-first} repositories and then install the packages.

The following dependencies are required:

* Python modules:
** `openstackclient`
** `openstacksdk`
** `netaddr`
** `pip`
* Ansible collections:
** `ansible-collections-openstack`, which installs Ansible Core
** `ansible-collection-community-general`
** `ansible-collection-ansible-netcommon`

The Ansible playbooks that simplify the removal process on user-provisioned
infrastructure require several Python modules. On the machine where you will run the process,
add the modules' repositories and then download them.

[NOTE]
These instructions assume that you are using {op-system-base-full} 8.

.Prerequisites

* Python 3 is installed on your machine.

.Procedure

. On a command line, add the repositories:

.. Register with Red Hat Subscription Manager:
+
[source,terminal]
----
$ sudo subscription-manager register # If not done already
----

.. Pull the latest subscription data:
+
[source,terminal]
----
$ sudo subscription-manager attach --pool=$YOUR_POOLID # If not done already
----

.. Disable the current repositories:
+
[source,terminal]
----
$ sudo subscription-manager repos --disable=* # If not done already
----

.. Add the required repositories:
+
[source,terminal]
----
$ sudo subscription-manager repos \
  --enable=rhel-9-for-x86_64-appstream-rpms \
  --enable=rhel-9-for-x86_64-baseos-rpms \
  --enable=openstack-17.1-for-rhel-9-x86_64-rpms
----

. Install the modules:
+
[source,terminal]
----
$ sudo dnf install ansible-collection-ansible-netcommon \
    ansible-collection-community-general \
    ansible-collections-openstack \
    python3-netaddr \
    python3-openstackclient \
    python3-openstacksdk \
    python3-pip
----

. Install the modules:
+
[source,terminal]
----
$ sudo yum install python3-openstackclient ansible python3-openstacksdk
----

. Ensure that the `python` command points to `python3`:
+
[source,terminal]
----
$ sudo alternatives --set python /usr/bin/python3
----

// Module included in the following assemblies:
//
// * installing/installing_openstack/uninstalling-openstack-user.adoc

[id="installation-uninstall-infra_{context}"]
= Removing a cluster from {rh-openstack} that uses your own infrastructure

You can remove an OpenShift Container Platform cluster on {rh-openstack-first} that uses your own infrastructure. To complete the removal process quickly, run several Ansible playbooks.

.Prerequisites

* Python 3 is installed on your machine.
* You downloaded the modules in "Downloading playbook dependencies."
* You have the playbooks that you used to install the cluster.
* You modified the playbooks that are prefixed with `down-` to reflect any changes that you made to their corresponding installation playbooks. For example, changes to the `bootstrap.yaml` file are reflected in the `down-bootstrap.yaml` file.
* All of the playbooks are in a common directory.

.Procedure

. On a command line, run the playbooks that you downloaded:
+
[source,terminal]
----
$ ansible-playbook -i inventory.yaml  \
	down-bootstrap.yaml      \
	down-control-plane.yaml  \
	down-compute-nodes.yaml  \
	down-load-balancers.yaml \
	down-network.yaml        \
	down-security-groups.yaml
----

. Remove any DNS record changes you made for the OpenShift Container Platform installation.

OpenShift Container Platform is removed from your infrastructure.
