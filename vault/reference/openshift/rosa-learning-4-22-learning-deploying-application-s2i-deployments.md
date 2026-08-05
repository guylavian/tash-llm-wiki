---
title: "S2I deployments"
type: reference
domain: openshift
slug: rosa-learning-4-22-learning-deploying-application-s2i-deployments
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rosa_learning/learning-deploying-application-s2i-deployments
version: 4.22
family: rosa_learning
documentKind: "Documentation"
---

# S2I deployments

[id="learning-deploying-application-s2i-deployments"]
= S2I deployments

[role="_abstract"]
You can deploy applications in OpenShift Container Platform by using the integrated Source-to-Image (S2I) builder. Compiling your source code with S2I helps you efficiently build reproducible, Docker-formatted container images.

// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-s2i-deployments.adoc
[id="learning-deploying-application-s2i-deployments-retrieving-login_{context}"]
= Retrieving your login command

[role="_abstract"]
To create your cluster, log in to the {rosa-cli-first}. If you need to authenticate, use a token from {cluster-manager-first}.

.Procedure
. Confirm you are logged in to the {rosa-cli} by running the following command:
+
[source,terminal]
----
rosa whoami
----
+
If you are logged in to the command-line interface, skip to "Creating a new project". If you are not logged in to the command-line interface, continue this procedure.

. If you are not logged in to the {rosa-cli}, in {cluster-manager-url}, click the dropdown arrow next to your name in the upper-right and select *Copy login command*.
+
image::ostoy-cli-login.png[CLI Login]
+
. A new tab opens. Enter your username and password, and select the authentication method.
+
. Click *Display Token*
+
. Copy the command under "Log in with this token".
+
. Log in to the CLI by running the copied command in your terminal.
+
*For example*:
+
[source,terminal]
----
$ oc login --token=RYhFlXXXXXXXXXXXX --server=https://api.osd4-demo.abc1.p1.openshiftapps.com:6443
----
+
*Example output*:
+
[source,terminal]
----
Logged into "https://api.myrosacluster.abcd.p1.openshiftapps.com:6443" as "rosa-user" using the token provided.

You don't have any projects. You can try to create a new project, by running

oc new-project <project name>
----
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-s2i-deployments.adoc
[id="learning-deploying-application-s2i-deployments-create-new-project_{context}"]
= Creating a new project

[role="_abstract"]
You can use the {oc-first} to create a new project within your cluster. To get started with the integrated Source-to-Image (S2I) deployment process, create a new project within your cluster by using the {oc-first}.

.Procedure
* Create a new project from the CLI by running the following command:
+
[source,terminal]
----
$ oc new-project ostoy-s2i
----
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-s2i-deployments.adoc
[id="learning-deploying-application-s2i-deployments-fork-repo_{context}"]
= Fork the OSToy repository

[role="_abstract"]
To trigger automated builds based on changes to the source code, you must fork the OSToy repository and set up a GitHub webhook. The webhook triggers S2I builds when you push code into your GitHub repository.

.Procedure
* To set up the webhook, you must first Create a new fork.
+
[IMPORTANT]
====
Replace `<UserName>` with your own GitHub username for the following URLs in this guide.
====
// Module included in the following assemblies:
//
// * rosa_learning/deploying_application_workshop/learning-deploying-application-s2i-deployments.adoc
[id="learning-deploying-application-s2i-deployments-deploy-to-cluster_{context}"]
= Using S2i to deploy OSToy on your cluster

[role="_abstract"]
To simplify your deployment process, you can deploy OSToy on your cluster by using the Source-to-Image (S2I) builder. This tool saves you time by automatically building a reproducible container image directly from the source binaries.

.Procedure
. Add a secret to {ocp-short}.
+
This example emulates a `.env` file. Files are easily moved directly into an {ocp-short} environment and can even be renamed in the secret.
+
** Run the following command, replacing `<UserName>` with your GitHub username:
+
[source,terminal]
----
$ oc create -f https://raw.githubusercontent.com/<UserName>/ostoy/master/deployment/yaml/secret.yaml
----
+
. Add a ConfigMap to {ocp-short}.
+
This example emulates an HAProxy config file, which is typically used for overriding default configurations in an {ocp-short} application. Files can be renamed in the ConfigMap.
+
** Run the following command, replacing `<UserName>` with your GitHub username:
+
[source,terminal]
----
$ oc create -f https://raw.githubusercontent.com/<UserName>/ostoy/master/deployment/yaml/configmap.yaml
----
+
. Deploy the microservice.
+
You must deploy the microservice to ensure that the service environment variables are available from the UI application.
+
`--context-dir` builds the application defined in the `microservice` directory in the Git repository. The `app` label ensures the user interface (UI) application and microservice are both grouped in the {ocp-short} UI.
+
** Run the following command to create the microservice, replacing `<UserName>` with your GitHub username:
+
[source,terminal]
----
$ oc new-app https://github.com/<UserName>/ostoy \
    --context-dir=microservice \
    --name=ostoy-microservice \
    --labels=app=ostoy
----
+
*Example output*:
+
[source,terminal]
----
--> Creating resources with label app=ostoy ...
    imagestream.image.openshift.io "ostoy-microservice" created
    buildconfig.build.openshift.io "ostoy-microservice" created
    deployment.apps "ostoy-microservice" created
    service "ostoy-microservice" created
--> Success
    Build scheduled, use 'oc logs -f buildconfig/ostoy-microservice' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose service/ostoy-microservice'
    Run 'oc status' to view your app.
----
+
. Check the status of the microservice.
** Check that the microservice was created and is running correctly by running the following command:
+
[source,terminal]
----
$ oc status
----
+
*For example*:
+
[source,terminal]
----
In project ostoy-s2i on server https://api.myrosacluster.g14t.p1.openshiftapps.com:6443

svc/ostoy-microservice - 172.30.47.74:8080
  dc/ostoy-microservice deploys istag/ostoy-microservice:latest <-
    bc/ostoy-microservice source builds https://github.com/UserName/ostoy on openshift/nodejs:14-ubi8
    deployment #1 deployed 34 seconds ago - 1 pod
----
+
Wait until you see that the microservice was successfully deployed. You can also check this through the web UI.
+
. Deploy the front end UI.
+
The application relies on several environment variables to define external settings.
+
** Attach the secret and ConfigMap and create a PersistentVolume by running the following command:
+
[source,terminal]
----
$ oc new-app https://github.com/<UserName>/ostoy \
    --env=MICROSERVICE_NAME=OSTOY_MICROSERVICE
----
+
*For example*:
+
[source,terminal]
----
--> Creating resources ...
    imagestream.image.openshift.io "ostoy" created
    buildconfig.build.openshift.io "ostoy" created
    deployment.apps "ostoy" created
    service "ostoy" created
--> Success
    Build scheduled, use 'oc logs -f buildconfig/ostoy' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose service/ostoy'
    Run 'oc status' to view your app.
----
+
. Update the deployment by running the following command:
+
[source,terminal]
----
$ oc patch deployment ostoy --type=json -p \
    '[{"op": "replace", "path": "/spec/strategy/type", "value": "Recreate"}, {"op": "remove", "path": "/spec/strategy/rollingUpdate"}]'
----
+
. Set a liveness probe.
+
Create a liveness probe to ensure the pod restarts if something is wrong in the application.
+
** Run the following command:
+
[source,terminal]
----
$ oc set probe deployment ostoy --liveness --get-url=http://:8080/health
----
+
. Attach the secret, ConfigMap, and persistent volume to the deployment.
+
.. Run the following command to attach your secret:
+
[source,terminal]
----
$ oc set volume deployment ostoy --add \
    --secret-name=ostoy-secret \
    --mount-path=/var/secret
----
+
.. Run the following command to attach your ConfigMap:
+
[source,terminal]
----
$ oc set volume deployment ostoy --add \
    --configmap-name=ostoy-config \
    -m /var/config
----
+
.. Run the following command to create and attach your persistent volume:
+
[source,terminal]
----
$ oc set volume deployment ostoy --add \
    --type=pvc \
    --claim-size=1G \
    -m /var/demo_files
----
+
. Expose the UI application as an {ocp-short} Route.

** Run the following command to deploy the application as an HTTPS application that uses the included TLS wildcard certificates:
+
[source,terminal]
----
$ oc create route edge --service=ostoy --insecure-policy=Redirect
----
+
. Browse to your application with the following methods:
** Run the following command to open a web browser with your OSToy application:
+
[source,terminal]
----
$ python -m webbrowser "$(oc get route ostoy -o template --template='https://{{.spec.host}}')"
----
+
** Run the following command to get the route for the application and copy and paste the route into your browser:
+
[source,terminal]
----
$ oc get route
----

[role="_additional-resources"]
== Additional resources

* Glossary of common terms for {OCP}
