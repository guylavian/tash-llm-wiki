---
title: "Health check"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-deploying-application-health-check
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-deploying-application-health-check
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Health check

[id="learning-deploying-application-health-check"]
= Health check

[role="_abstract"]
You can see how Kubernetes responds to pod failure by purposely crashing your pod and making it unresponsive to Kubernetes liveness probes. Observing this failure allows you to verify how the cluster automatically handles recovery.

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-health-check.adoc
[id="learning-deploying-application-health-check-prepare_{context}"]
= Preparing your desktop

[role="_abstract"]
To prepare your desktop for the health check procedures, access your OSToy application from {cluster-manager-url}.

.Procedure
* From the {ocp-short} web console, select *Workloads > Deployments > ostoy-frontend* to view the OSToy deployment.
+
image::5-ostoy-deployview.png[The web console deployments page]
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-health-check.adoc
[id="learning-deploying-application-health-check-crash-pod_{context}"]
= Crashing the pod

[role="_abstract"]
To test the failure states for your application, you can force the pod to crash. Observing this crash demonstrates how the system handles unexpected terminations and initiates recovery.

.Procedure
. From the OSToy application web console, click *Home* in the left menu, and enter a message in the *Crash Pod* box, for example, `This is goodbye!`.

. Click *Crash Pod*.
+
image::5-ostoy-crashpod.png[OSToy crash pod selection]
+
The pod crashes and Kubernetes restarts the pod.
+
image::5-ostoy-crashmsg.png[OSToy pod crash message]
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-health-check.adoc
[id="learning-deploying-application-health-check-view-pod_{context}"]
= Viewing the revived pod

[role="_abstract"]
You can check the status of your revived pod within {cluster-manager-url}. Check the status to see how quickly the system revives the pod and recovers from unexpected failures.

.Procedure
* From the {ocp-short} web console, quickly switch to the *Deployments* screen. You will see that the pod turns yellow, which means it is down. It should quickly revive and turn blue. The revival process happens quickly.
+
image::5-ostoy-podcrash.gif[Deployment details page]

.Verification

. From the web console, click  *Pods > ostoy-frontend-xxxxxxx-xxxx* to change to the pods screen.
+
image::5-ostoy-events.png[Pod overview page]

. Click the *Events* subtab, and verify that the container crashed and restarted.
+
image::5-ostoy-podevents.png[Pod events list]
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-health-check.adoc
[id="learning-deploying-application-health-check-forced-malfunction_{context}"]
= Making the application malfunction

[role="_abstract"]
You can test your application's failure responses by purposefully causing the application to malfunction. By causing this failure, you can observe how your system handles unexpected errors and verify that it recovers correctly.

.Procedure

* From the OSToy application, click *Toggle Health* in the *Toggle Health Status* tile. Watch *Current Health* switch to *I'm not feeling all that well*.
+
image::5-ostoy-togglehealth.png[OSToy toggle health tile]

.Verification

After you make the application malfunction, the application stops responding with a `200 HTTP code`. After 3 consecutive failures, Kubernetes stops the pod and restarts it.

* From the web console, switch back to the pod events page to see that the liveness probe failed and the pod restarted.

The following image shows an example of what you will see on your pod events page.

image::5-ostoy-podevents2.png[Pod events list]

*A.* The pod has three consecutive failures.

*B.* Kubernetes stops the pod.

*C.* Kubernetes restarts the pod.
