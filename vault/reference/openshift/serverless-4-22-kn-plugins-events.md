---
title: "Knative CLI plugins"
type: reference
domain: openshift
slug: serverless-4-22-kn-plugins-events
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/kn-plugins-events
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Knative CLI plugins

[id="kn-plugins-events"]
= Knative CLI plugins

The Knative (`kn`) CLI supports the use of plugins, which enable you to extend the functionality of your `kn` installation by adding custom commands and other shared commands that are not part of the core distribution. Knative (`kn`) CLI plugins are used in the same way as the main `kn` functionality.

Currently, Red Hat supports the `kn-source-kafka` plugin and the `kn-event` plugin.

// kn event commands
[id="serverless-build-events-kn_{context}"]
= Building events by using the kn-event plugin

You can use the builder-like interface of the `kn event build` command to build an event. You can then send that event at a later time or use it in another context.

.Prerequisites

* You have installed the Knative (`kn`) CLI.

.Procedure

* Build an event:
+
[source,terminal]
----
$ kn event build --field <field-name>=<value> --type <type-name> --id <id> --output <format>
----
where:
** The `--field` flag adds data to the event as a field-value pair. You can use it multiple times.
** The `--type` flag enables you to specify a string that designates the type of the event.
** The `--id` flag specifies the ID of the event.
** You can use the `json` or `yaml` arguments with the `--output` flag to change the output format of the event.
+
All of these flags are optional.
+
.Building a simple event
[source,terminal]
----
$ kn event build -o yaml
----
+
.Resultant event in the YAML format
[source,yaml]
----
data: {}
datacontenttype: application/json
id: 81a402a2-9c29-4c27-b8ed-246a253c9e58
source: kn-event/v0.4.0
specversion: "1.0"
time: "2021-10-15T10:42:57.713226203Z"
type: dev.knative.cli.plugin.event.generic
----
+
.Building a sample transaction event
[source,terminal]
----
$ kn event build \
    --field operation.type=local-wire-transfer \
    --field operation.amount=2345.40 \
    --field operation.from=87656231 \
    --field operation.to=2344121 \
    --field automated=true \
    --field signature='FGzCPLvYWdEgsdpb3qXkaVp7Da0=' \
    --type org.example.bank.bar \
    --id $(head -c 10 < /dev/urandom | base64 -w 0) \
    --output json
----
+
.Resultant event in the JSON format
[source,json]
----
{
  "specversion": "1.0",
  "id": "RjtL8UH66X+UJg==",
  "source": "kn-event/v0.4.0",
  "type": "org.example.bank.bar",
  "datacontenttype": "application/json",
  "time": "2021-10-15T10:43:23.113187943Z",
  "data": {
    "automated": true,
    "operation": {
      "amount": "2345.40",
      "from": 87656231,
      "to": 2344121,
      "type": "local-wire-transfer"
    },
    "signature": "FGzCPLvYWdEgsdpb3qXkaVp7Da0="
  }
}
----
[id="serverless-send-events-kn_{context}"]
= Sending events by using the kn-event plugin

You can use the `kn event send` command to send an event. The events can be sent either to publicly available addresses or to addressable resources inside a cluster, such as Kubernetes services, as well as Knative services, brokers, and channels. The command uses the same builder-like interface as the `kn event build` command.

.Prerequisites

* You have installed the Knative (`kn`) CLI.

.Procedure

* Send an event:
+
[source,terminal]
----
$ kn event send --field <field-name>=<value> --type <type-name> --id <id> --to-url <url> --to <cluster-resource> --namespace <namespace>
----
where:
** The `--field` flag adds data to the event as a field-value pair. You can use it multiple times.
** The `--type` flag enables you to specify a string that designates the type of the event.
** The `--id` flag specifies the ID of the event.
** If you are sending the event to a publicly accessible destination, specify the URL using the `--to-url` flag.
** If you are sending the event to an in-cluster Kubernetes resource, specify the destination using the `--to` flag.
*** Specify the Kubernetes resource using the `<Kind>:<ApiVersion>:<name>` format.
** The `--namespace` flag specifies the namespace. If omitted, the namespace is taken from the current context.
+
All of these flags are optional, except for the destination specification, for which you need to use either `--to-url` or `--to`.
+
The following example shows sending an event to a URL:
+
.Example command
[source,terminal]
----
$ kn event send \
    --field player.id=6354aa60-ddb1-452e-8c13-24893667de20 \
    --field player.game=2345 \
    --field points=456 \
    --type org.example.gaming.foo \
    --to-url http://ce-api.foo.example.com/
----
+
The following example shows sending an event to an in-cluster resource:
+
.Example command
[source,terminal]
----
$ kn event send \
    --type org.example.kn.ping \
    --id $(uuidgen) \
    --field event.type=test \
    --field event.data=98765 \
    --to Service:serving.knative.dev/v1:event-display
----
