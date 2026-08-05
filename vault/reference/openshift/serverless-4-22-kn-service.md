---
title: "kn service commands"
type: reference
domain: openshift
slug: serverless-4-22-kn-service
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/kn-service
version: 4.22
family: serverless
documentKind: "Documentation"
---

# kn service commands

[id="kn-service"]
= kn service commands

You can use the following commands to create and manage Knative services.

// Module included in the following assemblies:
//
// * serverless/develop/serverless-applications.adoc
// * serverless/reference/kn-serving-ref.adoc

[id="creating-serverless-apps-kn_{context}"]
= Creating serverless applications by using the Knative CLI

Using the Knative (`kn`) CLI to create serverless applications provides a more streamlined and intuitive user interface over modifying YAML files directly. You can use the `kn service create` command to create a basic serverless application.

.Prerequisites

* {ServerlessOperatorName} and Knative Serving are installed on your cluster.
* You have installed the Knative (`kn`) CLI.
* You have created a project or have access to a project with the appropriate roles and permissions to create applications and other workloads in OpenShift Container Platform.

.Procedure

* Create a Knative service:
+
[source,terminal]
----
$ kn service create <service-name> --image <image> --tag <tag-value>
----
+
Where:
+
** `--image` is the URI of the image for the application.
** `--tag` is an optional flag that can be used to add a tag to the initial revision that is created with the service.
+
.Example command
[source,terminal]
----
$ kn service create event-display \
    --image quay.io/openshift-knative/knative-eventing-sources-event-display:latest
----
+
.Example output
[source,terminal]
----
Creating service 'event-display' in namespace 'default':

  0.271s The Route is still working to reflect the latest desired specification.
  0.580s Configuration "event-display" is waiting for a Revision to become ready.
  3.857s ...
  3.861s Ingress has not yet been reconciled.
  4.270s Ready to serve.

Service 'event-display' created with latest revision 'event-display-bxshg-1' and URL:
http://event-display-default.apps-crc.testing
----
// Module included in the following assemblies:
//
// * serverless/reference/kn-serving-ref.adoc

[id="kn-service-update_{context}"]
= Updating serverless applications by using the Knative CLI

You can use the `kn service update` command for interactive sessions on the command line as you build up a service incrementally. In contrast to the `kn service apply` command, when using the `kn service update` command you only have to specify the changes that you want to update, rather than the full configuration for the Knative service.

.Example commands

* Update a service by adding a new environment variable:
+
[source,terminal]
----
$ kn service update <service_name> --env <key>=<value>
----

* Update a service by adding a new port:
+
[source,terminal]
----
$ kn service update <service_name> --port 80
----

* Update a service by adding new request and limit parameters:
+
[source,terminal]
----
$ kn service update <service_name> --request cpu=500m --limit memory=1024Mi --limit cpu=1000m
----

* Assign the `latest` tag to a revision:
+
[source,terminal]
----
$ kn service update <service_name> --tag <revision_name>=latest
----

* Update a tag from `testing` to `staging` for the latest `READY` revision of a service:
+
[source,terminal]
----
$ kn service update <service_name> --untag testing --tag @latest=staging
----

* Add the `test` tag to a revision that receives 10% of traffic, and send the rest of the traffic to the latest `READY` revision of a service:
+
[source,terminal]
----
$ kn service update <service_name> --tag <revision_name>=test --traffic test=10,@latest=90
----
// Module included in the following assemblies:
//
// * serverless/reference/kn-serving-ref.adoc

[id="kn-service-apply_{context}"]
= Applying service declarations

You can declaratively configure a Knative service by using the `kn service apply` command. If the service does not exist it is created, otherwise the existing service is updated with the options that have been changed.

The `kn service apply` command is especially useful for shell scripts or in a continuous integration pipeline, where users typically want to fully specify the state of the service in a single command to declare the target state.

When using `kn service apply` you must provide the full configuration for the Knative service. This is different from the `kn service update` command, which only requires you to specify in the command the options that you want to update.

.Example commands

* Create a service:
+
[source,terminal]
----
$ kn service apply <service_name> --image <image>
----

* Add an environment variable to a service:
+
[source,terminal]
----
$ kn service apply <service_name> --image <image> --env <key>=<value>
----

* Read the service declaration from a JSON or YAML file:
+
[source,terminal]
----
$ kn service apply <service_name> -f <filename>
----
// Module included in the following assemblies:
//
// * serverless/reference/kn-serving-ref.adoc

[id="kn-service-describe_{context}"]
= Describing serverless applications by using the Knative CLI

You can describe a Knative service by using the `kn service describe` command.

.Example commands

* Describe a service:
+
[source,terminal]
----
$ kn service describe --verbose <service_name>
----
+
The `--verbose` flag is optional but can be included to provide a more detailed description. The difference between a regular and verbose output is shown in the following examples:
+
.Example output without `--verbose` flag
[source,terminal]
----
Name:       hello
Namespace:  default
Age:        2m
URL:        http://hello-default.apps.ocp.example.com

Revisions:
  100%  @latest (hello-00001) [1] (2m)
        Image:  docker.io/openshift/hello-openshift (pinned to aaea76)

Conditions:
  OK TYPE                   AGE REASON
  ++ Ready                   1m
  ++ ConfigurationsReady     1m
  ++ RoutesReady             1m
----
+
.Example output with `--verbose` flag
[source,terminal]
----
Name:         hello
Namespace:    default
Annotations:  serving.knative.dev/creator=system:admin
              serving.knative.dev/lastModifier=system:admin
Age:          3m
URL:          http://hello-default.apps.ocp.example.com
Cluster:      http://hello.default.svc.cluster.local

Revisions:
  100%  @latest (hello-00001) [1] (3m)
        Image:  docker.io/openshift/hello-openshift (pinned to aaea76)
        Env:    RESPONSE=Hello Serverless!

Conditions:
  OK TYPE                   AGE REASON
  ++ Ready                   3m
  ++ ConfigurationsReady     3m
  ++ RoutesReady             3m
----

* Describe a service in YAML format:
+
[source,terminal]
----
$ kn service describe <service_name> -o yaml
----

* Describe a service in JSON format:
+
[source,terminal]
----
$ kn service describe <service_name> -o json
----

* Print the service URL only:
+
[source,terminal]
----
$ kn service describe <service_name> -o url
----
