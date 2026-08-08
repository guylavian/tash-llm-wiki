---
title: "Understanding Red Hat OpenShift Kubernetes Cluster Federation"
type: reference
domain: openshift
slug: kubefed-4-22-understanding-kubefed
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/kubefed/understanding-kubefed
version: 4.22
family: kubefed
documentKind: "Documentation"
---

# Understanding Red Hat OpenShift Kubernetes Cluster Federation

[id="understanding-kubefed"]
= Understanding Red Hat OpenShift Kubernetes Cluster Federation

{KubeFedProductName} is based on the open source Kubernetes Cluster Federation (KubeFed) project.
It enables coordinated and centrally managed configuration for multiple clusters in a federated OpenShift Container Platform deployment through a single API interface.

Federating application resources using {KubeFedProductShortName} allows applications deployed on a cluster in a federated deployment to be continuously reconciled with the desired state.

{KubeFedProductName} provides components which are designed as simple building blocks and can be used to address more advanced use cases, such as disaster recovery and applications across multi-geo deployments.
