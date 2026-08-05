---
title: "Integrating {ServerlessProductShortName} with the cost management service"
type: reference
domain: openshift
slug: serverless-4-22-serverless-cost-management-integration
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-cost-management-integration
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Integrating {ServerlessProductShortName} with the cost management service

[id="serverless-cost-management-integration"]
= Integrating {ServerlessProductShortName} with the cost management service

Cost management is an OpenShift Container Platform service that enables you to better understand and track costs for clouds and containers. It is based on the open source Koku project.

[id="prerequisites_serverless-cost-management-integration"]
== Prerequisites

* You have cluster administrator permissions.

* You have set up cost management and added an OpenShift Container Platform source.

// Module included in the following assemblies:
//
// * /serverless/integrations/serverless-cost-management-integration.adoc

[id="serverless-cost-management-labels_{context}"]
= Using labels for cost management queries

Labels, also known as _tags_ in cost management, can be applied for nodes, namespaces or pods. Each label is a key and value pair. You can use a combination of multiple labels to generate reports. You can access reports about costs by using the Red Hat hybrid console.

Labels are inherited from nodes to namespaces, and from namespaces to pods. However, labels are not overridden if they already exist on a resource. For example, Knative services have a default `app=<revision_name>` label:

.Example Knative service default label
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: example-service
spec:
...
      labels:
        app: <revision_name>
...
----

If you define a label for a namespace, such as `app=my-domain`, the cost management service does not take into account costs coming from a Knative service with the tag `app=<revision_name>` when querying the application using the `app=my-domain` tag. Costs for Knative services that have this tag must be queried under the `app=<revision_name>` tag.

[role="_additional-resources"]
[id="additional-resources_serverless-cost-management-integration"]
== Additional resources
* Configure tagging for your sources
* Use the Cost Explorer to visualize your costs
