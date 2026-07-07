---
title: "Executing remote commands in an {product-title} container"
type: reference
domain: openshift
slug: nodes-4-22-nodes-containers-remote-commands
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-containers-remote-commands
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Executing remote commands in an {product-title} container

[id="nodes-containers-remote-commands"]
= Executing remote commands in an OpenShift Container Platform container

[role="_abstract"]
You can use the `oc exec` command to execute remote commands in OpenShift Container Platform containers from your local machine.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * nodes/nodes-containers-remote-commands.adoc

[id="nodes-containers-remote-commands-about_{context}"]
= Executing remote commands in containers

[role="_abstract"]
You can use the {oc-first} to execute remote commands in OpenShift Container Platform containers. By running commands in a container, you can perform troubleshooting, inspect logs, run scripts, and other tasks.

.Procedure

* Use a command similar to the following to run a command in a container:
+
[source,terminal]
----
$ oc exec <pod> [-c <container>] -- <command> [<arg_1> ... <arg_n>]
----
+
For example:
+
[source,terminal]
----
$ oc exec mypod date
----
+
.Example output
[source,terminal]
----
Thu Apr  9 02:21:53 UTC 2015
----
+
[IMPORTANT]
====
For security purposes, the
`oc exec` command does not work when accessing privileged containers except when
the command is executed by a `cluster-admin` user.
====

// Module included in the following assemblies:
//
// * nodes/nodes-containers-remote-commands.adoc

[id="nodes-containers-remote-commands-protocol_{context}"]
= Protocol for initiating a remote command from a client

[role="_abstract"]
A client resource in your cluster can initiate the execution of a remote command in a container by issuing a request to the Kubernetes API server.

The following example is the format for a typical request to a Kubernetes API server:

[source,terminal]
----
/proxy/nodes/<node_name>/exec/<namespace>/<pod>/<container>?command=<command>
----
where:

--
`<node_name>`:: Specifies the FQDN of the node.
`<namespace>`:: Specifies the project of the target pod.
`<pod>`:: Specifies the name of the target pod.
`<container>`:: Specifies the name of the target container.
`<command>`:: Specifies the desired command to be executed.
--

.Example request
[source,terminal]
----
/proxy/nodes/node123.openshift.com/exec/myns/mypod/mycontainer?command=date
----

Additionally, the client can add parameters to the request to indicate any of the following conditions:

* The client should send input to the remote container's command (stdin).
* The client's terminal is a TTY.
* The remote container's command should send output from stdout to the client.
* The remote container's command should send output from stderr to the client.

After sending an `exec` request to the API server, the client upgrades the
connection to one that supports multiplexed streams; the current implementation
uses *HTTP/2*.

The client creates one stream each for stdin, stdout, and stderr. To distinguish
among the streams, the client sets the `streamType` header on the stream to one
of `stdin`, `stdout`, or `stderr`.

The client closes all streams, the upgraded connection, and the underlying
connection when it is finished with the remote command execution request.
