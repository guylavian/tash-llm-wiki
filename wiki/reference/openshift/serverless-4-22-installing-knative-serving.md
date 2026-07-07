---
title: "Installing Knative Serving"
type: reference
domain: openshift
slug: serverless-4-22-installing-knative-serving
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/installing-knative-serving
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Installing Knative Serving

[id="installing-knative-serving"]
= Installing Knative Serving

Installing Knative Serving allows you to create Knative services and functions on your cluster. It also allows you to use additional functionality such as autoscaling and networking options for your applications.

After you install the {ServerlessOperatorName}, you can install Knative Serving by using the default settings, or configure more advanced settings in the `KnativeServing` custom resource (CR). For more information about configuration options for the `KnativeServing` CR, see Global configuration.

[IMPORTANT]
====
If you want to use {DTProductName} with {ServerlessProductName}, you must install and configure {DTProductName} before you install Knative Serving.
====

// Module included in the following assemblies:
//
//  * serverless/install/installing-knative-serving.adoc

[id="serverless-install-serving-web-console_{context}"]
= Installing Knative Serving by using the web console

After you install the {ServerlessOperatorName}, install Knative Serving by using the OpenShift Container Platform web console. You can install Knative Serving by using the default settings or configure more advanced settings in the `KnativeServing` custom resource (CR).

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* You have logged in to the OpenShift Container Platform web console.
* You have installed the {ServerlessOperatorName}.

.Procedure

. In the *Administrator* perspective of the OpenShift Container Platform web console, navigate to *Ecosystem* -> *Installed Operators*.

. Check that the *Project* dropdown at the top of the page is set to *Project: knative-serving*.

. Click *Knative Serving* in the list of *Provided APIs* for the {ServerlessOperatorName} to go to the *Knative Serving* tab.

. Click *Create Knative Serving*.

. In the *Create Knative Serving* page, you can install Knative Serving using the default settings by clicking *Create*.
+
You can also modify settings for the Knative Serving installation by editing the `KnativeServing` object using either the form provided, or by editing the YAML.

* Using the form is recommended for simpler configurations that do not require full control of `KnativeServing` object creation.

* Editing the YAML is recommended for more complex configurations that require full control of `KnativeServing` object creation. You can access the YAML by clicking the *edit YAML* link in the top right of the *Create Knative Serving* page.
+
After you complete the form, or have finished modifying the YAML, click *Create*.
+
[NOTE]
====
For more information about configuration options for the KnativeServing custom resource definition, see the documentation on _Advanced installation configuration options_.
====

. After you have installed Knative Serving, the `KnativeServing` object is created, and you are automatically directed to the *Knative Serving* tab. You will see the `knative-serving` custom resource in the list of resources.

.Verification

. Click on `knative-serving` custom resource in the *Knative Serving* tab.

. You will be automatically directed to the *Knative Serving Overview* page.
+
image::serving-overview.png[Installed Operators page]

. Scroll down to look at the list of *Conditions*.

. You should see a list of conditions with a status of *True*, as shown in the example image.
+
image::serving-conditions-true.png[Conditions]
+
[NOTE]
====
It may take a few seconds for the Knative Serving resources to be created. You can check their status in the *Resources* tab.
====

. If the conditions have a status of *Unknown* or *False*, wait a few moments and then check again after you have confirmed that the resources have been created.
// Module included in the following assemblies:
//
// * /serverless/install/installing-knative-serving.adoc

[id="serverless-install-serving-yaml_{context}"]
= Installing Knative Serving by using YAML

After you install the {ServerlessOperatorName}, you can install Knative Serving by using the default settings, or configure more advanced settings in the `KnativeServing` custom resource (CR). You can use the following procedure to install Knative Serving by using YAML files and the `oc` CLI.

.Prerequisites

* You have access to an OpenShift Container Platform account with cluster administrator access.

* You have access to an OpenShift Container Platform account with cluster administrator or dedicated administrator access.

* You have installed the {ServerlessOperatorName}.
* Install the OpenShift CLI (`oc`).

.Procedure

. Create a file named `serving.yaml` and copy the following example YAML into it:
+
[source,yaml]
----
apiVersion: operator.knative.dev/v1beta1
kind: KnativeServing
metadata:
    name: knative-serving
    namespace: knative-serving
----
. Apply the `serving.yaml` file:
+
[source,terminal]
----
$ oc apply -f serving.yaml
----

.Verification

. To verify the installation is complete, enter the following command:
+
[source,terminal]
----
$ oc get knativeserving.operator.knative.dev/knative-serving -n knative-serving --template='{{range .status.conditions}}{{printf "%s=%s\n" .type .status}}{{end}}'
----
+
.Example output
[source,terminal]
----
DependenciesInstalled=True
DeploymentsAvailable=True
InstallSucceeded=True
Ready=True
----
+
[NOTE]
====
It may take a few seconds for the Knative Serving resources to be created.
====
+
If the conditions have a status of `Unknown` or `False`, wait a few moments and then check again after you have confirmed that the resources have been created.

. Check that the Knative Serving resources have been created:
+
[source,terminal]
----
$ oc get pods -n knative-serving
----
+
.Example output
[source,terminal]
----
NAME                                                        READY   STATUS      RESTARTS   AGE
activator-67ddf8c9d7-p7rm5                                  2/2     Running     0          4m
activator-67ddf8c9d7-q84fz                                  2/2     Running     0          4m
autoscaler-5d87bc6dbf-6nqc6                                 2/2     Running     0          3m59s
autoscaler-5d87bc6dbf-h64rl                                 2/2     Running     0          3m59s
autoscaler-hpa-77f85f5cc4-lrts7                             2/2     Running     0          3m57s
autoscaler-hpa-77f85f5cc4-zx7hl                             2/2     Running     0          3m56s
controller-5cfc7cb8db-nlccl                                 2/2     Running     0          3m50s
controller-5cfc7cb8db-rmv7r                                 2/2     Running     0          3m18s
domain-mapping-86d84bb6b4-r746m                             2/2     Running     0          3m58s
domain-mapping-86d84bb6b4-v7nh8                             2/2     Running     0          3m58s
domainmapping-webhook-769d679d45-bkcnj                      2/2     Running     0          3m58s
domainmapping-webhook-769d679d45-fff68                      2/2     Running     0          3m58s
storage-version-migration-serving-serving-0.26.0--1-6qlkb   0/1     Completed   0          3m56s
webhook-5fb774f8d8-6bqrt                                    2/2     Running     0          3m57s
webhook-5fb774f8d8-b8lt5                                    2/2     Running     0          3m57s
----

. Check that the necessary networking components have been installed to the automatically created `knative-serving-ingress` namespace:
+
[source,terminal]
----
$ oc get pods -n knative-serving-ingress
----
+
.Example output
[source,terminal]
----
NAME                                      READY   STATUS    RESTARTS   AGE
net-kourier-controller-7d4b6c5d95-62mkf   1/1     Running   0          76s
net-kourier-controller-7d4b6c5d95-qmgm2   1/1     Running   0          76s
3scale-kourier-gateway-6688b49568-987qz   1/1     Running   0          75s
3scale-kourier-gateway-6688b49568-b5tnp   1/1     Running   0          75s
----

[id="next-steps_installing-knative-serving"]
== Next steps

* If you want to use Knative event-driven architecture you can install Knative Eventing.
