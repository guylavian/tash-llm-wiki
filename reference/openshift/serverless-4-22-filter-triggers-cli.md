---
title: "Filtering triggers from the command line"
type: reference
domain: openshift
slug: serverless-4-22-filter-triggers-cli
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/filter-triggers-cli
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Filtering triggers from the command line

[id="filter-triggers-cli"]
= Filtering triggers from the command line

Using the Knative (`kn`) CLI to filter events by using triggers provides a streamlined and intuitive user interface. You can use the `kn trigger create` command, along with the appropriate flags, to filter events by using triggers.

// Module included in the following assemblies:
//
// * /serverless/eventing/triggers/filter-triggers-cli.adoc

[id="kn-trigger-filtering_{context}"]
= Filtering events with triggers by using the Knative CLI
// should be a procedure module but out of scope for this PR

In the following trigger example, only events with the attribute `type: dev.knative.samples.helloworld` are sent to the event sink:

[source,terminal]
----
$ kn trigger create <trigger_name> --broker <broker_name> --filter type=dev.knative.samples.helloworld --sink ksvc:<service_name>
----

You can also filter events by using multiple attributes. The following example shows how to filter events using the type, source, and extension attributes:

[source,terminal]
----
$ kn trigger create <trigger_name> --broker <broker_name> --sink ksvc:<service_name> \
--filter type=dev.knative.samples.helloworld \
--filter source=dev.knative.samples/helloworldsource \
--filter myextension=my-extension-value
----
