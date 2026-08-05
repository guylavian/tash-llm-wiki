---
title: "Using deployment strategies"
type: reference
domain: openshift
slug: applications-4-22-deployment-strategies
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/applications/deployment-strategies
version: 4.22
family: applications
documentKind: "Documentation"
---

# Using deployment strategies

[id="deployment-strategies"]
= Using deployment strategies

_Deployment strategies_ are used to change or upgrade applications without downtime so that users barely notice a change.

Because users generally access applications through a route handled by a router, deployment strategies can focus on `DeploymentConfig` object features or routing features. Strategies that focus on `DeploymentConfig` object features impact all routes that use the application. Strategies that use router features target individual routes.

Most deployment strategies are supported through the `DeploymentConfig` object, and some additional strategies are supported through router features.

[id="choosing-deployment-strategies"]
== Choosing a deployment strategy

Consider the following when choosing a deployment strategy:

- Long-running connections must be handled gracefully.
- Database conversions can be complex and must be done and rolled back along with the application.
- If the application is a hybrid of microservices and traditional components, downtime might be required to complete the transition.
- You must have the infrastructure to do this.
- If you have a non-isolated test environment, you can break both new and old versions.

A deployment strategy uses readiness checks to determine if a new pod is ready for use. If a readiness check fails, the `DeploymentConfig` object retries to run the pod until it times out. The default timeout is `10m`, a value set in `TimeoutSeconds` in `dc.spec.strategy.*params`.

// Rolling strategies
// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="deployments-rolling-strategy_{context}"]
= Rolling strategy

A rolling deployment slowly replaces instances of the previous version of an application with instances of the new version of the application. The rolling strategy is the default deployment strategy used if no strategy is specified on a `DeploymentConfig` object.

A rolling deployment typically waits for new pods to become `ready` via a readiness check before scaling down the old components. If a significant issue occurs, the rolling deployment can be aborted.

*When to use a rolling deployment:*

- When you want to take no downtime during an application update.
- When your application supports having old code and new code running at the same time.

A rolling deployment means you have both old and new versions of your code running at the same time. This typically requires that your application handle N-1 compatibility.

.Example rolling strategy definition
[source,yaml]
----
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  strategy:
    type: Rolling
    rollingParams:
      updatePeriodSeconds: 1 <1>
      intervalSeconds: 1 <2>
      timeoutSeconds: 120 <3>
      maxSurge: "20%" <4>
      maxUnavailable: "10%" <5>
      pre: {} <6>
     post: {}
----
<1> The time to wait between individual pod updates. If unspecified, this value defaults to `1`.
<2> The time to wait between polling the deployment status after update. If unspecified, this value defaults to `1`.
<3> The time to wait for a scaling event before giving up. Optional; the default is `600`. Here, _giving up_ means automatically rolling back to the previous complete deployment.
<4> `maxSurge` is optional and defaults to `25%` if not specified. See the information below the following procedure.
<5> `maxUnavailable` is optional and defaults to `25%` if not specified. See the information below the following procedure.
<6> `pre` and `post` are both lifecycle hooks.

The rolling strategy:

. Executes any `pre` lifecycle hook.
. Scales up the new replication controller based on the surge count.
. Scales down the old replication controller based on the max unavailable count.
. Repeats this scaling until the new replication controller has reached the desired replica count and the old replication controller has been scaled to zero.
. Executes any `post` lifecycle hook.

[IMPORTANT]
====
When scaling down, the rolling strategy waits for pods to become ready so it can decide whether further scaling would affect availability. If scaled up pods never become ready, the deployment process will eventually time out and result in a deployment failure.
====

The `maxUnavailable` parameter is the maximum number of pods that can be unavailable during the update. The `maxSurge` parameter is the maximum number of pods that can be scheduled above the original number of pods. Both parameters can be set to either a percentage (e.g., `10%`) or an absolute value (e.g., `2`). The default value for both is `25%`.

These parameters allow the deployment to be tuned for availability and speed. For example:

- `maxUnavailable*=0` and `maxSurge*=20%` ensures full capacity is maintained during the update and rapid scale up.
- `maxUnavailable*=10%` and `maxSurge*=0` performs an update using no extra capacity (an in-place update).
- `maxUnavailable*=10%` and `maxSurge*=10%` scales up and down quickly with some potential for capacity loss.

Generally, if you want fast rollouts, use `maxSurge`. If you have to take into account resource quota and can accept partial unavailability, use
`maxUnavailable`.

[WARNING]
====
The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.
====

// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="deployments-canary-deployments_{context}"]
= Canary deployments

All rolling deployments in OpenShift Container Platform are _canary deployments_; a new version (the canary) is tested before all of the old instances are replaced. If the readiness check never succeeds, the canary instance is removed and the `DeploymentConfig` object will be automatically rolled back.

The readiness check is part of the application code and can be as sophisticated as necessary to ensure the new instance is ready to be used. If you must implement more complex checks of the application (such as sending real user workloads to the new instance), consider implementing a custom deployment or using a blue-green deployment strategy.

// Creating rolling deployments
// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="deployments-creating-rolling-deployment_{context}"]
= Creating a rolling deployment

Rolling deployments are the default type in OpenShift Container Platform. You can create a rolling deployment using the CLI.

.Procedure

. Create an application based on the example deployment images found in Quay.io:
+
[source,terminal]
----
$ oc new-app quay.io/openshifttest/deployment-example:latest
----
+
[NOTE]
====
This image does not expose any ports. If you want to expose your applications over an external LoadBalancer service or enable access to the application over the public internet, create a service by using the `oc expose dc/deployment-example --port=<port>` command after completing this procedure.
====

. If you have the router installed, make the application available via a route or use the service IP directly.
+
[source,terminal]
----
$ oc expose svc/deployment-example
----

. Browse to the application at `deployment-example.<project>.<router_domain>` to verify you see the `v1` image.

. Scale the `DeploymentConfig` object up to three replicas:
+
[source,terminal]
----
$ oc scale dc/deployment-example --replicas=3
----

. Trigger a new deployment automatically by tagging a new version of the example as the `latest` tag:
+
[source,terminal]
----
$ oc tag deployment-example:v2 deployment-example:latest
----

. In your browser, refresh the page until you see the `v2` image.

. When using the CLI, the following command shows how many pods are on version 1 and how many are on version 2. In the web console, the pods are progressively added to v2 and removed from v1:
+
[source,terminal]
----
$ oc describe dc deployment-example
----

During the deployment process, the new replication controller is incrementally scaled up. After the new pods are marked as `ready` (by passing their readiness check), the deployment process continues.

If the pods do not become ready, the process aborts, and the deployment rolls back to its previous version.

// Editing a deployment
// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="odc-editing-deployments_{context}"]
= Editing a deployment by using the Developer perspective

You can edit the deployment strategy, image settings, environment variables, and advanced options for your deployment by using the *Developer* perspective.

.Prerequisites

* You are in the *Developer* perspective of the web console.
* You have created an application.

.Procedure

. Navigate to the *Topology* view.
. Click your application to see the *Details* panel.
. In the *Actions* drop-down menu, select *Edit Deployment* to view the *Edit Deployment* page.
. You can edit the following *Advanced options* for your deployment:
.. Optional: You can pause rollouts by clicking *Pause rollouts*, and then selecting the *Pause rollouts for this deployment* checkbox.
+
By pausing rollouts, you can make changes to your application without triggering a rollout. You can resume rollouts at any time.
.. Optional: Click *Scaling* to change the number of instances of your image by modifying the number of *Replicas*.
. Click *Save*.

// Starting a deployment
// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="odc-starting-rolling-deployment_{context}"]
= Starting a rolling deployment using the Developer perspective

You can upgrade an application by starting a rolling deployment.

.Prerequisites

* You are in the *Developer* perspective of the web console.
* You have created an application.

.Procedure

. In the *Topology* view, click the application node to see the *Overview* tab in the side panel. Note that the *Update Strategy* is set to the default *Rolling* strategy.
. In the *Actions* drop-down menu, select *Start Rollout* to start a rolling update. The rolling deployment spins up the new version of the application and then terminates the old one.
+
.Rolling update
image::odc-rolling-update.png[]

[role="_additional-resources"]
.Additional resources
* Creating and deploying applications on OpenShift Container Platform using the *Developer* perspective
* Viewing the applications in your project, verifying their deployment status, and interacting with them in the *Topology* view

// Recreate strategies
// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="deployments-recreate-strategy_{context}"]
= Recreate strategy

The recreate strategy has basic rollout behavior and supports lifecycle hooks for injecting code into the deployment process.

.Example recreate strategy definition
[source,yaml]
----
kind: Deployment
apiVersion: apps/v1
metadata:
  name: hello-openshift
# ...
spec:
# ...
  strategy:
    type: Recreate
    recreateParams: <1>
      pre: {} <2>
      mid: {}
      post: {}
----

<1> `recreateParams` are optional.
<2> `pre`, `mid`, and `post` are lifecycle hooks.

The recreate strategy:

. Executes any `pre` lifecycle hook.
. Scales down the previous deployment to zero.
. Executes any `mid` lifecycle hook.
. Scales up the new deployment.
. Executes any `post` lifecycle hook.

[IMPORTANT]
====
During scale up, if the replica count of the deployment is greater than one, the first replica of the deployment will be validated for readiness before fully scaling up the deployment. If the validation of the first replica fails, the deployment will be considered a failure.
====

*When to use a recreate deployment:*

- When you must run migrations or other data transformations before your new code starts.
- When you do not support having new and old versions of your application code running at the same time.
- When you want to use a RWO volume, which is not supported being shared between multiple replicas.

A recreate deployment incurs downtime because, for a brief period, no instances of your application are running. However, your old code and new code do not run at the same time.

// Editing a deployment

// Starting a deployment
// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="odc-starting-recreate-deployment_{context}"]
= Starting a recreate deployment using the Developer perspective

You can switch the deployment strategy from the default rolling update to a recreate update using the *Developer* perspective in the web console.

.Prerequisites
* Ensure that you are in the *Developer* perspective of the web console.
* Ensure that you have created an application using the *Add* view and see it deployed in the *Topology* view.

.Procedure

To switch to a recreate update strategy and to upgrade an application:

. Click your application to see the *Details* panel.
. In the *Actions* drop-down menu, select *Edit Deployment Config* to see the deployment configuration details of the application.
. In the YAML editor, change the `spec.strategy.type` to `Recreate` and click *Save*.
. In the *Topology* view, select the node to see the *Overview* tab in the side panel. The *Update Strategy* is now set to *Recreate*.
. Use the *Actions* drop-down menu to select *Start Rollout* to start an update using the recreate strategy. The recreate strategy first terminates pods for the older version of the application and then spins up pods for the new version.
+
.Recreate update
image::odc-recreate-update.png[]

[role="_additional-resources"]
.Additional resources
* Creating and deploying applications on OpenShift Container Platform using the *Developer* perspective
* Viewing the applications in your project, verifying their deployment status, and interacting with them in the *Topology* view

// Custom strategies
// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="deployments-custom-strategy_{context}"]
= Custom strategy

The custom strategy allows you to provide your own deployment behavior.

.Example custom strategy definition
[source,yaml]
----
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  strategy:
    type: Custom
    customParams:
      image: organization/strategy
      command: [ "command", "arg1" ]
      environment:
        - name: ENV_1
          value: VALUE_1

----

In the above example, the `organization/strategy` container image provides the deployment behavior. The optional `command` array overrides any `CMD` directive specified in the image's `Dockerfile`. The optional environment variables provided are added to the execution environment of the strategy process.

Additionally, OpenShift Container Platform provides the following environment variables to the deployment process:

[cols="4,8",options="header"]
|===
|Environment variable |Description

.^|`OPENSHIFT_DEPLOYMENT_NAME`
|The name of the new deployment, a replication controller.

.^|`OPENSHIFT_DEPLOYMENT_NAMESPACE`
|The name space of the new deployment.
|===

The replica count of the new deployment will initially be zero. The responsibility of the strategy is to make the new deployment active using the
logic that best serves the needs of the user.

Alternatively, use the `customParams` object to inject the custom deployment logic into the existing deployment strategies. Provide a custom shell script logic and call the `openshift-deploy` binary. Users do not have to supply their custom deployer container image; in this case, the default OpenShift Container Platform deployer image is used instead:

[source,yaml]
----
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: example-dc
# ...
spec:
# ...
  strategy:
    type: Rolling
    customParams:
      command:
      - /bin/sh
      - -c
      - |
        set -e
        openshift-deploy --until=50%
        echo Halfway there
        openshift-deploy
        echo Complete
----

This results in following deployment:

[source,terminal]
----
Started deployment #2
--> Scaling up custom-deployment-2 from 0 to 2, scaling down custom-deployment-1 from 2 to 0 (keep 2 pods available, don't exceed 3 pods)
    Scaling custom-deployment-2 up to 1
--> Reached 50% (currently 50%)
Halfway there
--> Scaling up custom-deployment-2 from 1 to 2, scaling down custom-deployment-1 from 2 to 0 (keep 2 pods available, don't exceed 3 pods)
    Scaling custom-deployment-1 down to 1
    Scaling custom-deployment-2 up to 2
    Scaling custom-deployment-1 down to 0
--> Success
Complete
----

If the custom deployment strategy process requires access to the OpenShift Container Platform API or the Kubernetes API the container that executes the strategy can use the service account token available inside the container for authentication.

// Editing a deployment

// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="deployments-lifecycle-hooks_{context}"]
= Lifecycle hooks

The rolling and recreate strategies support _lifecycle hooks_, or deployment hooks, which allow behavior to be injected into the deployment process at predefined points within the strategy:

.Example `pre` lifecycle hook
[source,yaml]
----
pre:
  failurePolicy: Abort
  execNewPod: {} <1>
----
<1> `execNewPod` is a pod-based lifecycle hook.

Every hook has a _failure policy_, which defines the action the strategy should take when a hook failure is encountered:

[cols="2,8"]
|===

.^|`Abort`
|The deployment process will be considered a failure if the hook fails.

.^|`Retry`
|The hook execution should be retried until it succeeds.

.^|`Ignore`
|Any hook failure should be ignored and the deployment should proceed.
|===

Hooks have a type-specific field that describes how to execute the hook. Currently, pod-based hooks are the only supported hook type, specified by the `execNewPod` field.

[id="deployments-lifecycle-hooks-pod-based_{context}"]
== Pod-based lifecycle hook

Pod-based lifecycle hooks execute hook code in a new pod derived from the template in a `DeploymentConfig` object.

The following simplified example deployment uses the rolling strategy. Triggers and some other minor details are omitted for brevity:

[source,yaml]
----
kind: DeploymentConfig
apiVersion: apps.openshift.io/v1
metadata:
  name: frontend
spec:
  template:
    metadata:
      labels:
        name: frontend
    spec:
      containers:
        - name: helloworld
          image: openshift/origin-ruby-sample
  replicas: 5
  selector:
    name: frontend
  strategy:
    type: Rolling
    rollingParams:
      pre:
        failurePolicy: Abort
        execNewPod:
          containerName: helloworld <1>
          command: [ "/usr/bin/command", "arg1", "arg2" ] <2>
          env: <3>
            - name: CUSTOM_VAR1
              value: custom_value1
          volumes:
            - data <4>
----
<1> The `helloworld` name refers to `spec.template.spec.containers[0].name`.
<2> This `command` overrides any `ENTRYPOINT` defined by the `openshift/origin-ruby-sample` image.
<3> `env` is an optional set of environment variables for the hook container.
<4> `volumes` is an optional set of volume references for the hook container.

In this example, the `pre` hook will be executed in a new pod using the `openshift/origin-ruby-sample` image from the `helloworld` container. The hook pod has the following properties:

* The hook command is `/usr/bin/command arg1 arg2`.
* The hook container has the `CUSTOM_VAR1=custom_value1` environment variable.
* The hook failure policy is `Abort`, meaning the deployment process fails if the hook fails.
* The hook pod inherits the `data` volume from the `DeploymentConfig` object pod.

[id="deployments-setting-lifecycle-hooks_{context}"]
== Setting lifecycle hooks
// out of scope for this PR - needs a separate module

You can set lifecycle hooks, or deployment hooks, for a deployment using the CLI.

.Procedure

. Use the `oc set deployment-hook` command to set the type of hook you want: `--pre`, `--mid`, or `--post`. For example, to set a pre-deployment hook:
+
[source,terminal]
----
$ oc set deployment-hook dc/frontend \
    --pre -c helloworld -e CUSTOM_VAR1=custom_value1 \
    --volumes data --failure-policy=abort -- /usr/bin/command arg1 arg2
----
