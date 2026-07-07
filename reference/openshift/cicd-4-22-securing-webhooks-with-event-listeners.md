---
title: "Securing webhooks with event listeners"
type: reference
domain: openshift
slug: cicd-4-22-securing-webhooks-with-event-listeners
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/securing-webhooks-with-event-listeners
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Securing webhooks with event listeners

[id="securing-webhooks-with-event-listeners"]
= Securing webhooks with event listeners

As an administrator, you can secure webhooks with event listeners. After creating a namespace, you enable HTTPS for the `Eventlistener` resource by adding the `operator.tekton.dev/enable-annotation=enabled` label to the namespace. Then, you create a `Trigger` resource and a secured route using the re-encrypted TLS termination.

Triggers in {pipelines-title} support insecure HTTP and secure HTTPS connections to the `Eventlistener` resource. HTTPS secures connections within and outside the cluster.

{pipelines-title} runs a `tekton-operator-proxy-webhook` pod that watches for the labels in the namespace. When you add the label to the namespace, the webhook sets the `service.beta.openshift.io/serving-cert-secret-name=<secret_name>` annotation on the `EventListener` object. This, in turn, creates secrets and the required certificates.

[source,terminal,subs="attributes+"]
----
service.beta.openshift.io/serving-cert-secret-name=<secret_name>
----

In addition, you can mount the created secret into the `Eventlistener` pod to secure the request.

[id='op-providing-secure-connection_{context}']
= Providing secure connection with OpenShift routes

To create a route with the re-encrypted TLS termination, run:

[source,terminal,subs="attributes+"]
----
$ oc create route reencrypt --service=<svc-name> --cert=tls.crt --key=tls.key --ca-cert=ca.crt --hostname=<hostname>
----

Alternatively, you can create a re-encrypted TLS termination YAML file to create a secure route.

.Example re-encrypt TLS termination YAML to create a secure route
[source,yaml,subs="attributes+"]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: route-passthrough-secured  <1>
spec:
  host: <hostname>
  to:
    kind: Service
    name: frontend <1>
  tls:
    termination: reencrypt <2>
    key: [as in edge termination]
    certificate: [as in edge termination]
    caCertificate: [as in edge termination]
    destinationCACertificate: |- <3>
      -----BEGIN CERTIFICATE-----
      [...]
      -----END CERTIFICATE-----
----
<1> The name of the object, which is limited to only 63 characters.
<2> The termination field is set to `reencrypt`. This is the only required TLS field.
<3> This is required for re-encryption. The `destinationCACertificate` field specifies a CA certificate to validate the endpoint certificate, thus securing the connection from the router to the destination pods. You can omit this field in either of the following scenarios:
* The service uses a service signing certificate.
* The administrator specifies a default CA certificate for the router, and the service has a certificate signed by that CA.

You can run the `oc create route reencrypt --help` command to display more options.

[id='op-sample-eventlistener-resource_{context}']
= Creating a sample EventListener resource using a secure HTTPS connection

This section uses the pipelines-tutorial example to demonstrate creation of a sample EventListener resource using a secure HTTPS connection.

.Procedure

. Create the `TriggerBinding` resource from the YAML file available in the pipelines-tutorial repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/master/03_triggers/01_binding.yaml
----

. Create the `TriggerTemplate` resource from the YAML file available in the pipelines-tutorial repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/master/03_triggers/02_template.yaml
----

. Create the `Trigger` resource directly from the pipelines-tutorial repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/master/03_triggers/03_trigger.yaml
----

. Create an `EventListener` resource using a secure HTTPS connection:
.. Add a label to enable the secure HTTPS connection to the `Eventlistener` resource:
+
[source,terminal,subs="attributes+"]
----
$ oc label namespace <ns-name> operator.tekton.dev/enable-annotation=enabled
----

.. Create the `EventListener` resource from the YAML file available in the pipelines-tutorial repository:
+
[source,terminal,subs="attributes+"]
----
$ oc create -f https://raw.githubusercontent.com/openshift/pipelines-tutorial/master/03_triggers/04_event_listener.yaml
----

.. Create a route with the re-encrypted TLS termination:
+
[source,terminal,subs="attributes+"]
----
$ oc create route reencrypt --service=<svc-name> --cert=tls.crt --key=tls.key --ca-cert=ca.crt --hostname=<hostname>
----
