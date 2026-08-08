---
title: "Troubleshooting the Source-to-Image process"
type: reference
domain: openshift
slug: support-4-22-troubleshooting-s2i
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/support/troubleshooting-s2i
version: 4.22
family: support
documentKind: "Documentation"
---

# Troubleshooting the Source-to-Image process

[id="troubleshooting-s2i"]
= Troubleshooting the Source-to-Image process

[role="_abstract"]
A cluster administrator can observe the S2I stages to determine where in the S2I process a failure occurred and gather diagnostic data to resolve Source-to-Image issues.

// Strategies for Source-to-Image troubleshooting
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-s2i.adoc

[id="strategies-for-s2i-troubleshooting_{context}"]
= Strategies for Source-to-Image troubleshooting

[role="_abstract"]
Use Source-to-Image (S2I) to build reproducible, Docker-formatted container images. You can create ready-to-run images by injecting application source code into a container image and assembling a new image. The new image incorporates the base image (the builder) and built source.

.Procedure

. To determine where in the S2I process a failure occurs, you can observe the state of the pods relating to each of the following S2I stages:
+
.. *During the build configuration stage*, a build pod is used to create an application container image from a base image and application source code.
+
.. *During the deployment configuration stage*, a deployment pod is used to deploy application pods from the application container image that was built in the build configuration stage. The deployment pod also deploys other resources such as services and routes. The deployment configuration begins after the build configuration succeeds.
+
.. *After the deployment pod has started the application pods*, application failures can occur within the running application pods. For instance, an application might not behave as expected even though the application pods are in a `Running` state. In this scenario, you can access running application pods to investigate application failures within a pod.

. When troubleshooting S2I issues, follow this strategy:
+
.. Monitor build, deployment, and application pod status.
+
.. Determine the stage of the S2I process where the problem occurred.
+
.. Review logs corresponding to the failed stage.

// Gathering Source-to-Image diagnostic data
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-s2i.adoc

[id="gathering-s2i-diagnostic-data_{context}"]
= Gathering Source-to-Image diagnostic data

[role="_abstract"]
The S2I tool runs a build pod and a deployment pod in sequence. The deployment pod is responsible for deploying the application pods based on the application container image created in the build stage. Watch build, deployment and application pod status to determine where in the S2I process a failure occurs. Then, focus diagnostic data collection accordingly.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Watch the pod status throughout the S2I process to determine at which stage a failure occurs:
+
[source,terminal]
----
$ oc get pods -w
----
+
Use the `-w` flag to monitor pods for changes until you quit the command using `Ctrl+C`.

. Review a failed pod's logs for errors.
+
* *If the build pod fails*, review the build pod's logs:
+
[source,terminal]
----
$ oc logs -f pod/<application_name>-<build_number>-build
----
+
[NOTE]
====
Alternatively, you can review the build configuration's logs using `oc logs -f bc/<application_name>`. The build configuration's logs include the logs from the build pod.
====
+
* *If the deployment pod fails*, review the deployment pod's logs:
+
[source,terminal]
----
$ oc logs -f pod/<application_name>-<build_number>-deploy
----
+
[NOTE]
====
Alternatively, you can review the deployment configuration's logs using `oc logs -f dc/<application_name>`. This outputs logs from the deployment pod until the deployment pod completes successfully. The command outputs logs from the application pods if you run it after the deployment pod has completed. After a deployment pod completes, its logs can still be accessed by running `oc logs -f pod/<application_name>-<build_number>-deploy`.
====
+
* *If an application pod fails, or if an application is not behaving as expected within a running application pod*, review the application pod's logs:
+
[source,terminal]
----
$ oc logs -f pod/<application_name>-<build_number>-<random_string>
----

// Gathering application diagnostic data to investigate application failures
// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-s2i.adoc

[id="gathering-application-diagnostic-data_{context}"]
= Gathering application diagnostic data to investigate application failures

[role="_abstract"]
Application failures can occur within running application pods. In these situations, you can retrieve diagnostic information with these strategies:

* Review events relating to the application pods.
* Review the logs from the application pods, including application-specific log files that are not collected by the OpenShift Logging framework.
* Test application functionality interactively and run diagnostic tools in an application container.

.Prerequisites

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the cluster as a user with the `dedicated-admin` role.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. List events relating to a specific application pod. The following example retrieves events for an application pod named `my-app-1-akdlg`:
+
[source,terminal]
----
$ oc describe pod/my-app-1-akdlg
----

. Review logs from an application pod:
+
[source,terminal]
----
$ oc logs -f pod/my-app-1-akdlg
----

. Query specific logs within a running application pod. Logs that are sent to stdout are collected by the OpenShift Logging framework and are included in the output of the preceding command. The following query is only required for logs that are not sent to stdout.
+
.. If an application log can be accessed without root privileges within a pod, concatenate the log file as follows:
+
[source,terminal]
----
$ oc exec my-app-1-akdlg -- cat /var/log/my-application.log
----
+
.. If root access is required to view an application log, you can start a debug container with root privileges and then view the log file from within the container. Start the debug container from the project's `DeploymentConfig` object. Pod users typically run with non-root privileges, but running troubleshooting pods with temporary root privileges can be useful during issue investigation:
+
[source,terminal]
----
$ oc debug dc/my-deployment-configuration --as-root -- cat /var/log/my-application.log
----
+
[NOTE]
====
You can access an interactive shell with root access within the debug pod if you run `oc debug dc/<deployment_configuration> --as-root` without appending `-- <command>`.
====

. Test application functionality interactively and run diagnostic tools, in an application container with an interactive shell.
.. Start an interactive shell on the application container:
+
[source,terminal]
----
$ oc exec -it my-app-1-akdlg /bin/bash
----
+
.. Test application functionality interactively from within the shell. For example, you can run the container's entry point command and observe the results. Then, test changes from the command line directly, before updating the source code and rebuilding the application container through the S2I process.
+
.. Run diagnostic binaries available within the container.
+
[NOTE]
====
Root privileges are required to run some diagnostic binaries. In these situations you can start a debug pod with root access, based on a problematic pod's `DeploymentConfig` object, by running `oc debug dc/<deployment_configuration> --as-root`. Then, you can run diagnostic binaries as root from within the debug pod.
====

. If diagnostic binaries are not available within a container, you can run a host's diagnostic binaries within a container's namespace by using `nsenter`. The following example runs `ip ad` within a container's namespace, using the host`s `ip` binary.
// cannot create resource "namespaces" in API group
.. Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`:
+
[source,terminal]
----
$ oc debug node/my-cluster-node
----
+
.. Set `/host` as the root directory within the debug shell. The debug pod mounts the host's root file system in `/host` within the pod. By changing the root directory to `/host`, you can run binaries contained in the host's executable paths:
+
[source,terminal]
----
# chroot /host
----
+
[NOTE]
====
OpenShift Container Platform  cluster nodes running {op-system-first} are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on the target node, `oc` operations will be impacted. In such situations, it is possible to access nodes using `ssh core@<node>.<cluster_name>.<base_domain>` instead.
====
+
.. Determine the target container ID:
+
[source,terminal]
----
# crictl ps
----
+
.. Determine the container's process ID. In this example, the target container ID is `a7fe32346b120`:
+
[source,terminal]
----
# crictl inspect a7fe32346b120 --output yaml | grep 'pid:' | awk '{print $2}'
----
+
.. Run `ip ad` within the container's namespace, using the host's `ip` binary. This example uses `31150` as the container's process ID. The `nsenter` command enters the namespace of a target process and runs a command in its namespace. Because the target process in this example is a container's process ID, the `ip ad` command is run in the container's namespace from the host:
+
[source,terminal]
----
# nsenter -n -t 31150 -- ip ad
----
+
[NOTE]
====
Running a host's diagnostic binaries within a container's namespace is only possible if you are using a privileged container such as a debug node.
====

[role="_additional-resources"]
== Additional resources

* Source-to-Image (S2I) build
