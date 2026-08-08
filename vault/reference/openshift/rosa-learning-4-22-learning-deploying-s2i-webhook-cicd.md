---
title: "Using Source-to-Image (S2I) webhooks for automated deployment"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-deploying-s2i-webhook-cicd
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-deploying-s2i-webhook-cicd
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# Using Source-to-Image (S2I) webhooks for automated deployment

[id="learning-deploying-s2i-webhook-cicd"]
= Using Source-to-Image (S2I) webhooks for automated deployment

[role="_abstract"]
Automatically trigger a build and deploy any time you change the source code by using a webhook. For more information about this process, see Triggering Builds.

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-s2i-webhook-cicd.adoc
[id="learning-deploying-s2i-webhook-cicd-configuration_{context}"]
= Configuring your automated deployment

[role="_abstract"]
Configure a GitHub webhook to set up automated deployments for your OSToy application. Using this webhook saves you time by automatically triggering a new build every time you update your source code.

.Procedure
. Obtain the GitHub webhook trigger secret by running the following command:
+
[source,terminal]
----
$ oc get bc/ostoy-microservice -o=jsonpath='{.spec.triggers..github.secret}'
----
+
*For example*:
+
[source,terminal]
----
`o_3x9M1qoI2Wj_cz1WiK`
----
+
[IMPORTANT]
====
You need to use this secret in a later step in this process.
====

. Obtain the GitHub webhook trigger URL from the OSToy's buildconfig by running the following command:
+
[source,terminal]
----
$ oc describe bc/ostoy-microservice
----
+
*For example*:
+
[source,terminal]
----
[...]
Webhook GitHub:
	URL:	https://api.demo1234.openshift.com:443/apis/build.openshift.io/v1/namespaces/ostoy-s2i/buildconfigs/ostoy/webhooks/<secret>/github
[...]
----

. In the GitHub webhook URL, replace the `<secret>` text with the secret you retrieved. Your URL will resemble the following example output:
+
*For example*:
+
[source,text]
----
https://api.demo1234.openshift.com:443/apis/build.openshift.io/v1/namespaces/ostoy-s2i/buildconfigs/ostoy-microservice/webhooks/o_3x9M1qoI2Wj_czR1WiK/github
----

. Set up the webhook URL in GitHub repository.
.. In your repository, click *Settings > Webhooks > Add webhook*.
+
image::ostoy-webhook.png[Add Webhook]
+
.. Paste the GitHub webhook URL with the `Secret` included in the "Payload URL" field.
.. Change the "Content type" to `application/json`.
.. Click the *Add webhook* button.
+
image::ostoy-webhookfinish.png[Finish Add Webhook]
+
You should see a message from GitHub stating that your webhook was successfully configured. Now, whenever you push a change to your GitHub repository, a new build automatically starts, and upon a successful build, a new deployment starts.

. Make a change in the source code. Any changes automatically trigger a build and deployment. In this example, the colors that denote the status of your OSToy app are randomly selected. To test the configuration, change the box to display grayscale.
+
.. Go to the source code in your repository https://github.com/<username>/ostoy/blob/master/microservice/app.js.
.. Edit the file.
.. Comment out line 8 (containing `let randomColor = getRandomColor();`).
.. Uncomment line 9 (containing `let randomColor = getRandomGrayScaleColor();`).
+

[source,javascript,highlight='2-3']
----
7   app.get('/', function(request, response) {
8   //let randomColor = getRandomColor(); // <-- comment this
9   let randomColor = getRandomGrayScaleColor(); // <-- uncomment this
10
11  response.writeHead(200, {'Content-Type': 'application/json'});
----
+
.. Enter a message for the update, such as "changed box to grayscale colors".
.. Click *Commit* at the bottom to commit the changes to the main branch.

. In your cluster's web UI, click *Builds > Builds* to determine the status of the build. After this build is completed, the deployment begins. You can also check the status by running `oc status` in your terminal.
+
image::ostoy-builddone.png[Build Run]

. After the deployment has finished, return to the OSToy application in your browser. Access the *Networking* menu item on the left. The box color is now limited to grayscale colors only.
+
image::ostoy-gray.png[Gray]
