---
title: "Monitoring application health by using health checks"
type: reference
domain: openshift
slug: applications-4-22-application-health
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/application-health
version: 4.22
family: applications
documentKind: "Documentation"
---

# Monitoring application health by using health checks

[id="application-health"]
= Monitoring application health by using health checks

In software systems, components can become unhealthy due to transient issues such as temporary connectivity loss, configuration errors, or problems with external dependencies. OpenShift Container Platform applications have a number of options to detect and handle unhealthy containers.

// The following include statements pull in the module files that comprise
// the assembly. Include any combination of concept, procedure, or reference
// modules required to cover the user story. You can also include other
// assemblies.

// Module included in the following assemblies:
//
// * applications/application-health.adoc

[id="application-health-about_{context}"]
= Understanding health checks

A health check periodically performs diagnostics on a
running container using any combination of the readiness, liveness, and startup health checks.

You can include one or more probes in the specification for the pod that contains the container which you want to perform the health checks.

[NOTE]
====
If you want to add or edit health checks in an existing pod, you must edit the pod `DeploymentConfig` object or use the web console. You cannot use the CLI to add or edit health checks for an existing pod.
====

Readiness probe::
A _readiness probe_ determines if a container is ready to accept service requests. If
the readiness probe fails for a container, the kubelet removes the pod from the list of available service endpoints.
+
After a failure, the probe continues to examine the pod. If the pod becomes available, the kubelet adds the pod to the list of available service endpoints.

Liveness health check::
A _liveness probe_ determines if a container is still
running. If the liveness probe fails due to a condition such as a deadlock, the kubelet kills the container. The pod then
responds based on its restart policy.
+
For example, a liveness probe on a pod with a `restartPolicy` of `Always` or `OnFailure`
kills and restarts the container.

Startup probe::
A _startup probe_ indicates whether the application within a container is started. All other probes are disabled until the startup succeeds. If the startup probe does not succeed within a specified time period, the kubelet kills the container, and the container is subject to the pod `restartPolicy`.
+
Some applications can require additional startup time on their first initialization. You can use a startup probe with a liveness or readiness probe to delay that probe long enough to handle lengthy start-up time using the `failureThreshold` and `periodSeconds` parameters.
+
For example, you can add a startup probe, with a `failureThreshold` of 30 failures and a `periodSeconds` of 10 seconds (30 * 10s = 300s) for a maximum of 5 minutes, to a liveness probe. After the startup probe succeeds the first time, the liveness probe takes over.

You can configure liveness, readiness, and startup probes with any of the following types of tests:

* HTTP `GET`: When using an HTTP `GET` test, the test determines the healthiness of the container by using a web hook. The test is successful if the HTTP response code is between `200` and `399`.
+
You can use an HTTP `GET` test with applications that return HTTP status codes when completely initialized.

* Container Command: When using a container command test, the probe executes a command inside the container. The probe is successful if the test exits with a `0` status.

* TCP socket: When using a TCP socket test, the probe attempts to open a socket to the container. The container is only
considered healthy if the probe can establish a connection. You can use a TCP socket test with applications that do not start listening until
initialization is complete.

You can configure several fields to control the behavior of a probe:

* `initialDelaySeconds`: The time, in seconds, after the container starts before the probe can be scheduled. The default is 0.
* `periodSeconds`: The delay, in seconds, between performing probes. The default is `10`. This value must be greater than `timeoutSeconds`.
* `timeoutSeconds`: The number of seconds of inactivity after which the probe times out and the container is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.
* `successThreshold`: The number of times that the probe must report success after a failure to reset the container status to successful. The value must be `1` for a liveness probe. The default is `1`.
* `failureThreshold`: The number of times that the probe is allowed to fail. The default is 3. After the specified attempts:
** for a liveness probe, the container is restarted
** for a readiness probe, the pod is marked `Unready`
** for a startup probe, the container is killed and is subject to the pod's `restartPolicy`

[id="application-health-examples"]
== Example probes

The following are samples of different probes as they would appear in an object specification.

.Sample readiness probe with a container command readiness probe in a pod spec
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app <1>
    args:
    image: registry.k8s.io/goproxy:0.1 <2>
    readinessProbe: <3>
      exec: <4>
        command: <5>
        - cat
        - /tmp/healthy
# ...
----

<1> The container name.
<2> The container image to deploy.
<3> A readiness probe.
<4> A container command test.
<5> The commands to execute on the container.

.Sample container command startup probe and liveness probe with container command tests in a pod spec
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app <1>
    args:
    image: registry.k8s.io/goproxy:0.1 <2>
    livenessProbe: <3>
      httpGet: <4>
        scheme: HTTPS <5>
        path: /healthz
        port: 8080 <6>
        httpHeaders:
        - name: X-Custom-Header
          value: Awesome
    startupProbe: <7>
      httpGet: <8>
        path: /healthz
        port: 8080 <9>
      failureThreshold: 30 <10>
      periodSeconds: 10 <11>
# ...
----

<1> The container name.
<2> Specify the container image to deploy.
<3> A liveness probe.
<4> An HTTP `GET` test.
<5> The internet scheme: `HTTP` or `HTTPS`. The default value is `HTTP`.
<6> The port on which the container is listening.
<7> A startup probe.
<8> An HTTP `GET` test.
<9> The port on which the container is listening.
<10> The number of times to try the probe after a failure.
<11> The number of seconds to perform the probe.

.Sample liveness probe with a container command test that uses a timeout in a pod spec
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
# ...
spec:
  containers:
  - name: goproxy-app <1>
    args:
    image: registry.k8s.io/goproxy:0.1 <2>
    livenessProbe: <3>
      exec: <4>
        command: <5>
        - /bin/bash
        - '-c'
        - timeout 60 /opt/eap/bin/livenessProbe.sh
      periodSeconds: 10 <6>
      successThreshold: 1 <7>
      failureThreshold: 3 <8>
# ...
----

<1> The container name.
<2> Specify the container image to deploy.
<3> The liveness probe.
<4> The type of probe, here a container command probe.
<5> The command line to execute inside the container.
<6> How often in seconds to perform the probe.
<7> The number of consecutive successes needed to show success after a failure.
<8> The number of times to try the probe after a failure.

.Sample readiness probe and liveness probe with a TCP socket test in a deployment
[source,yaml]
----
kind: Deployment
apiVersion: apps/v1
metadata:
  labels:
    test: health-check
  name: my-application
spec:
# ...
  template:
    spec:
      containers:
        - resources: {}
          readinessProbe: <1>
            tcpSocket:
              port: 8080
            timeoutSeconds: 1
            periodSeconds: 10
            successThreshold: 1
            failureThreshold: 3
          terminationMessagePath: /dev/termination-log
          name: ruby-ex
          livenessProbe: <2>
            tcpSocket:
              port: 8080
            initialDelaySeconds: 15
            timeoutSeconds: 1
            periodSeconds: 10
            successThreshold: 1
            failureThreshold: 3
# ...
----
<1> The readiness probe.
<2> The liveness probe.

// Module included in the following assemblies:
//
// * applications/application-health.adoc

[id="application-health-configuring_{context}"]
= Configuring health checks using the CLI

To configure readiness, liveness, and startup probes, add one or more probes to the specification for the pod that contains the container which you want to perform the health checks

[NOTE]
====
If you want to add or edit health checks in an existing pod, you must edit the pod `DeploymentConfig` object or use the web console. You cannot use the CLI to add or edit health checks for an existing pod.
====

.Procedure

To add probes for a container:

. Create a `Pod` object to add one or more probes:
+
[source,yaml]
----
apiVersion: v1
kind: Pod
metadata:
  labels:
    test: health-check
  name: my-application
spec:
  containers:
  - name: my-container <1>
    args:
    image: registry.k8s.io/goproxy:0.1 <2>
    livenessProbe: <3>
      tcpSocket:  <4>
        port: 8080 <5>
      initialDelaySeconds: 15 <6>
      periodSeconds: 20 <7>
      timeoutSeconds: 10 <8>
    readinessProbe: <9>
      httpGet: <10>
        host: my-host <11>
        scheme: HTTPS <12>
        path: /healthz
        port: 8080 <13>
    startupProbe: <14>
      exec: <15>
        command: <16>
        - cat
        - /tmp/healthy
      failureThreshold: 30 <17>
      periodSeconds: 20 <18>
      timeoutSeconds: 10 <19>
----
<1> Specify the container name.
<2> Specify the container image to deploy.
<3> Optional: Create a Liveness probe.
<4> Specify a test to perform, here a TCP Socket test.
<5> Specify the port on which the container is listening.
<6> Specify the time, in seconds, after the container starts before the probe can be scheduled.
<7> Specify the number of seconds to perform the probe. The default is `10`. This value must be greater than `timeoutSeconds`.
<8> Specify the number of seconds of inactivity after which the probe is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.
<9> Optional: Create a Readiness probe.
<10> Specify the type of test to perform, here an HTTP test.
<11> Specify a host IP address. When `host` is not defined, the `PodIP` is used.
<12> Specify `HTTP` or `HTTPS`. When `scheme` is not defined, the `HTTP` scheme is used.
<13> Specify the port on which the container is listening.
<14> Optional: Create a Startup probe.
<15> Specify the type of test to perform, here an Container Execution probe.
<16> Specify the commands to execute on the container.
<17> Specify the number of times to try the probe after a failure.
<18> Specify the number of seconds to perform the probe. The default is `10`. This value must be greater than `timeoutSeconds`.
<19> Specify the number of seconds of inactivity after which the probe is assumed to have failed. The default is `1`. This value must be lower than `periodSeconds`.
+
[NOTE]
====
If the `initialDelaySeconds` value is lower than the `periodSeconds` value, the first Readiness probe occurs at some point between the two periods due to an issue with timers.

The `timeoutSeconds` value must be lower than the `periodSeconds` value.
====

. Create the `Pod` object:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----

. Verify the state of the health check pod:
+
[source,terminal]
----
$ oc describe pod my-application
----
+
.Example output
[source,terminal]
----
Events:
  Type    Reason     Age   From                                  Message
  ----    ------     ----  ----                                  -------
  Normal  Scheduled  9s    default-scheduler                     Successfully assigned openshift-logging/liveness-exec to ip-10-0-143-40.ec2.internal
  Normal  Pulling    2s    kubelet, ip-10-0-143-40.ec2.internal  pulling image "registry.k8s.io/liveness"
  Normal  Pulled     1s    kubelet, ip-10-0-143-40.ec2.internal  Successfully pulled image "registry.k8s.io/liveness"
  Normal  Created    1s    kubelet, ip-10-0-143-40.ec2.internal  Created container
  Normal  Started    1s    kubelet, ip-10-0-143-40.ec2.internal  Started container
----
+
The following is the output of a failed probe that restarted a container:
+
.Sample Liveness check output with unhealthy container
[source,terminal]
----
$ oc describe pod pod1
----
+
.Example output
[source,terminal]
----
....

Events:
  Type     Reason          Age                From                                               Message
  ----     ------          ----               ----                                               -------
  Normal   Scheduled       <unknown>                                                             Successfully assigned aaa/liveness-http to ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj
  Normal   AddedInterface  47s                multus                                             Add eth0 [10.129.2.11/23]
  Normal   Pulled          46s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 773.406244ms
  Normal   Pulled          28s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 233.328564ms
  Normal   Created         10s (x3 over 46s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Created container liveness
  Normal   Started         10s (x3 over 46s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Started container liveness
  Warning  Unhealthy       10s (x6 over 34s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Liveness probe failed: HTTP probe failed with statuscode: 500
  Normal   Killing         10s (x2 over 28s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Container liveness failed liveness probe, will be restarted
  Normal   Pulling         10s (x3 over 47s)  kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Pulling image "registry.k8s.io/liveness"
  Normal   Pulled          10s                kubelet, ci-ln-37hz77b-f76d1-wdpjv-worker-b-snzrj  Successfully pulled image "registry.k8s.io/liveness" in 244.116568ms
----

// Module included in the following assemblies:
//
// * applications/application-health

[id="odc-monitoring-application-health-using-developer-perspective_{context}"]
= Monitoring application health using the Developer perspective

You can use the *Developer* perspective to add three types of health probes to your container to ensure that your application is healthy:

* Use the Readiness probe to check if the container is ready to handle requests.
* Use the Liveness probe to check if the container is running.
* Use the Startup probe to check if the application within the container has started.

You can add health checks either while creating and deploying an application, or after you have deployed an application.

// cannot add health checks in web console
// Module included in the following assemblies:
//
// applications/application-health

[id="odc-adding-health-checks_{context}"]
= Adding health checks using the Developer perspective

[role="_abstract"]
You can use the *Topology* view to add health checks to your deployed application.

.Prerequisites
* You have switched to the *Developer* perspective in the web console.
* You have created and deployed an application on OpenShift Container Platform using the *Developer* perspective.

.Procedure
. In the *Topology* view, click the application node to see the side panel. If the container does not have health checks added, a *Health Checks* notification is displayed with a link to add health checks.
. In the displayed notification, click the *Add Health Checks* link.
. Alternatively, you can also click the *Actions* list and select *Add Health Checks*. Note that if the container already has health checks, you will see the *Edit Health Checks* option instead of the add option.
. In the *Add Health Checks* form, if you have deployed multiple containers, use the *Container* list to ensure that the appropriate container is selected.
. Click the required health probe links to add them to the container. Default data for the health checks is pre-populated. You can add the probes with the default data or further customize the values and then add them. For example, to add a Readiness probe that checks if your container is ready to handle requests:
.. Click *Add Readiness Probe*, to see a form containing the parameters for the probe.
.. Click the *Type* list to select the request type you want to add. For example, in this case, select *Container Command* to select the command that will be executed inside the container.
.. In the *Command* field, add an argument `cat`, similarly, you can add multiple arguments for the check, for example, add another argument `/tmp/healthy`.
.. Retain or modify the default values for the other parameters as required.
+
[NOTE]
====
The `Timeout` value must be lower than the `Period` value. The `Timeout` default value is `1`. The `Period` default value is `10`.
====
.. Click the checkmark at the bottom of the form. The *Readiness Probe Added* message is displayed.

. Click *Add* to add the health check. You are redirected to the *Topology* view and the container is restarted.
. In the side panel, verify that the probes have been added by clicking on the deployed pod under the *Pods* section.
. In the *Pod Details* page, click the listed container in the *Containers* section.
. In the *Container Details* page, verify that the Readiness probe - *Exec Command* `cat` `/tmp/healthy` has been added to the container.

// Module included in the following assemblies:
//
// applications/application-health

[id="odc-editing-health-checks"]
= Editing health checks using the Developer perspective

You can use the *Topology* view to edit health checks added to your application, modify them, or add more health checks.

.Prerequisites
* You have switched to the *Developer* perspective in the web console.
* You have created and deployed an application on OpenShift Container Platform using the *Developer* perspective.
* You have added health checks to your application.

.Procedure
. In the *Topology* view, right-click your application and select *Edit Health Checks*. Alternatively, in the side panel, click the *Actions* drop-down list and select *Edit Health Checks*.
. In the *Edit Health Checks* page:

* To remove a previously added health probe, click the *Remove* icon adjoining it.
* To edit the parameters of an existing probe:
+
.. Click the *Edit Probe* link next to a previously added probe to see the parameters for the probe.
.. Modify the parameters as required, and click the check mark to save your changes.
+
* To add a new health probe, in addition to existing health checks, click the add probe links. For example, to add a Liveness probe that checks if your container is running:
+
.. Click *Add Liveness Probe*, to see a form containing the parameters for the probe.
.. Edit the probe parameters as required.
+
[NOTE]
====
The `Timeout` value must be lower than the `Period` value. The `Timeout` default value is `1`. The `Period` default value is `10`.
====
.. Click the check mark at the bottom of the form. The *Liveness Probe Added* message is displayed.

. Click *Save* to save your modifications and add the additional probes to your container. You are redirected to the *Topology* view.
. In the side panel, verify that the probes have been added by clicking on the deployed pod under the *Pods* section.
. In the *Pod Details* page, click the listed container in the *Containers* section.
. In the *Container Details* page, verify that the Liveness probe - `HTTP Get 10.129.4.65:8080/` has been added to the container, in addition to the earlier existing probes.

// Module included in the following assemblies:
//
// applications/application-health

[id="odc-monitoring-health-checks"]
= Monitoring health check failures using the Developer perspective

In case an application health check fails, you can use the *Topology* view to monitor these health check violations.

.Prerequisites
* You have switched to the *Developer* perspective in the web console.
* You have created and deployed an application on OpenShift Container Platform using the *Developer* perspective.
* You have added health checks to your application.

.Procedure
. In the *Topology* view, click on the application node to see the side panel.
. Click the *Observe* tab to see the health check failures in the *Events (Warning)* section.
. Click the down arrow adjoining *Events (Warning)* to see the details of the health check failure.

[role="_additional-resources"]
.Additional resources
* For details on switching to the *Developer* perspective in the web console, see About the *Developer* perspective.
* For details on adding health checks while creating and deploying an application, see *Advanced Options* in the Creating applications using the Developer perspective section.
