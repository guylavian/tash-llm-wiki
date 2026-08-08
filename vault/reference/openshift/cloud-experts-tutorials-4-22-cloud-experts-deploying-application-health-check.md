---
title: "Tutorial: Health Check"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-deploying-application-health-check
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-deploying-application-health-check
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Health Check

[id="cloud-experts-deploying-application-health-check"]
= Tutorial: Health Check

[role="_abstract"]
You can see how Kubernetes responds to pod failure by intentionally crashing your pod and making it unresponsive to the Kubernetes liveness probes.

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-health-check.adoc

[id="cloud-experts-deploying-application-health-check-prep_{context}"]
= Preparing your desktop

[role="_abstract"]
You can set up your desktop to make this tutorial easier to follow.

.Procedure
. Split your desktop screen between the OpenShift web console and the OSToy application web console so that you can see the results of your actions immediately.
+
image::5-ostoy-splitscreen.png[Splitscreen desktop with the OSToy application and the web console]
+
If you cannot split your screen, open the OSToy application web console in another tab so you can quickly switch to the OpenShift web console after activating the features in the application.

. From the OpenShift web console, select *Workloads > Deployments > ostoy-frontend* to view the OSToy deployment.
+
image::5-ostoy-deployview.png[The web console deployments page]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-health-check.adoc

[id="cloud-experts-deploying-application-health-manipulate-pods_{context}"]
= Manipulating your pods

[role="_abstract"]
You can crash and revive your pods to see how the application reports these statuses.

.Procedure
. From the OSToy application web console, click *Home* in the left menu, and enter a message in the *Crash Pod* box, for example, `This is goodbye!`.

. Click *Crash Pod*.
+
image::5-ostoy-crashpod.png[OSToy crash pod selection]
+
The pod crashes and Kubernetes should restart the pod.
+
image::5-ostoy-crashmsg.png[OSToy pod crash message]

. You can now revive your pod from the OpenShift web console, quickly switch to the *Deployments* screen. You will see that the pod turns yellow, meaning it is down. It should quickly revive and turn blue. The revival process happens quickly so you might miss it.
+
image::5-ostoy-podcrash.gif[Deployment details page]

.Verification
. From the web console, click  *Pods > ostoy-frontend-xxxxxxx-xxxx* to change to the pods screen.
+
image::5-ostoy-events.png[Pod overview page]

. Click the *Events* sub-tab and verify that the container crashed and restarted.
+
image::5-ostoy-podevents.png[Pod events list]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-deploying-application/cloud-experts-deploying-application-health-check.adoc

[id="cloud-experts-deploying-application-health-app-malfunction_{context}"]
= Making the application malfunction

[role="_abstract"]
You can force the application that you deployed to malfunction to see how failures show up.

.Procedure
* From the OSToy application, click *Toggle Health* in the *Toggle Health Status* tile. Watch *Current Health* switch to *I'm not feeling all that well*.
+
image::5-ostoy-togglehealth.png[OSToy toggle health tile]

.Verification

After the previous step, the application stops responding with a `200 HTTP code`. After 3 consecutive failures, Kubernetes will stop the pod and restart it. From the web console, switch back to the pod events page and you will see that the liveness probe failed and the pod restarted.

The following image shows an example of what you should see on your pod events page.

image::5-ostoy-podevents2.png[Pod events list]

*A.* The pod has three consecutive failures.
*B.* Kubernetes stops the pod.
*C.* Kubernetes restarts the pod.
