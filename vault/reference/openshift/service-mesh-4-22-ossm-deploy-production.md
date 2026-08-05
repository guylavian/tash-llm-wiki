---
title: "Configuring Service Mesh for production"
type: reference
domain: openshift
slug: service-mesh-4-22-ossm-deploy-production
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/service_mesh/ossm-deploy-production
version: 4.22
family: service_mesh
documentKind: "Documentation"
---

# Configuring Service Mesh for production

[id="ossm-production"]
= Configuring Service Mesh for production

When you are ready to move from a basic installation to production, you must configure your control plane, tracing, and security certificates to meet production requirements.

.Prerequisites

* Install and configure {SMProductName}.
* Test your configuration in a staging environment.

// Module included in the following assemblies:
//
// * service_mesh/v2x/ossm-deploy-production.adoc

[id="ossm-smcp-prod_{context}"]
= Configuring your ServiceMeshControlPlane resource for production

If you have installed a basic `ServiceMeshControlPlane` resource to test {SMProductShortName}, you must configure it to production specification before you use {SMProductName} in production.

You cannot change the `metadata.name` field of an existing `ServiceMeshControlPlane` resource. For production deployments, you must customize the default template.

.Procedure

. Configure the {JaegerShortName} for production.
+
.. Edit the `ServiceMeshControlPlane` resource to use the `production` deployment strategy, by setting `spec.addons.jaeger.install.storage.type` to `Elasticsearch` and specify additional configuration options under `install`. You can create and configure your Jaeger instance and set `spec.addons.jaeger.name` to the name of the Jaeger instance.
+
.Default Jaeger parameters including Elasticsearch
[source,yaml, subs="attributes,verbatim"]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  version: v{MaistraVersion}
  tracing:
    sampling: 100
    type: Jaeger
  addons:
    jaeger:
      name: MyJaeger
      install:
        storage:
          type: Elasticsearch
        ingress:
          enabled: true
  runtime:
    components:
      tracing.jaeger.elasticsearch: # only supports resources and image name
        container:
          resources: {}
----

.. Configure the sampling rate for production. For more information, see the Performance and scalability section.

. Ensure your security certificates are production ready by installing security certificates from an external certificate authority. For more information, see the Security section.

.Verification

. Enter the following command to verify that the `ServiceMeshControlPlane` resource updated properly. In this example, `basic` is the name of the `ServiceMeshControlPlane` resource.
+
[source,terminal]
----
$ oc get smcp basic -o yaml
----

[id="additional-resources_ossm-production"]
[role="_additional-resources"]
== Additional resources

* For more information about tuning {SMProductShortName} for performance, see Performance and scalability.
