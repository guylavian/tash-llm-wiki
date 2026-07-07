---
title: "Configuring resource quota or requests"
type: reference
domain: openshift
slug: cicd-4-22-configuring-resource-quota
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/configuring-resource-quota
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Configuring resource quota or requests

[id="configuring-resource-quota"]
= Configuring resource quota or requests

[role="_abstract"]
With the Argo CD Custom Resource, you can create, update, and delete resource requests and limits for Argo CD workloads.

// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-resource-quota.adoc

[id="configuring-workloads_{context}"]
= Configuring workloads with resource requests and limits

[role="_abstract"]
You can create Argo CD custom resource workloads with resource requests and limits. This is required when you want to deploy the Argo CD instance in a namespace that is configured with resource quotas.

The following Argo CD instance deploys the Argo CD workloads such as `Application Controller`, `ApplicationSet Controller`, `Dex`, `Redis`,`Repo Server`, and `Server` with resource requests and limits. You can also create the other workloads with resource requirements in the same manner.

[source,yaml]
----
apiVersion: argoproj.io/v1alpha1
kind: ArgoCD
metadata:
  name: example
spec:
  server:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 125m
        memory: 128Mi
    route:
      enabled: true
  applicationSet:
    resources:
      limits:
        cpu: '2'
        memory: 1Gi
      requests:
        cpu: 250m
        memory: 512Mi
  repo:
    resources:
      limits:
        cpu: '1'
        memory: 512Mi
      requests:
        cpu: 250m
        memory: 256Mi
  dex:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 250m
        memory: 128Mi
  redis:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 250m
        memory: 128Mi
  controller:
    resources:
      limits:
        cpu: '2'
        memory: 2Gi
      requests:
        cpu: 250m
        memory: 1Gi
----

// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-resource-quota.adoc

[id="patch-argocd-instance_{context}"]
= Patching Argo CD instance to update the resource requirements

[role="_abstract"]
You can update the resource requirements for all or any of the workloads post installation.

.Procedure
Update the `Application Controller` resource requests of an Argo CD instance in the Argo CD namespace.

[source,terminal]
----
oc -n argocd patch argocd example --type='json' -p='[{"op": "replace", "path": "/spec/controller/resources/requests/cpu", "value":"1"}]'

oc -n argocd patch argocd example --type='json' -p='[{"op": "replace", "path": "/spec/controller/resources/requests/memory", "value":"512Mi"}]'
----

// Module is included in the following assemblies:
//
// * cicd/gitops/configuring-resource-quota.adoc

[id="remove-resource-requirements_{context}"]
= Removing resource requests

[role="_abstract"]
You can also remove resource requirements for all or any of your workloads after installation.

.Procedure
Remove the `Application Controller` resource requests of an Argo CD instance in the Argo CD namespace.

[source,terminal]
----
oc -n argocd patch argocd example --type='json' -p='[{"op": "remove", "path": "/spec/controller/resources/requests/cpu"}]'

oc -n argocd argocd patch argocd example --type='json' -p='[{"op": "remove", "path": "/spec/controller/resources/requests/memory"}]'

----
