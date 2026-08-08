---
title: "Troubleshooting issues in {gitops-title}"
type: reference
domain: openshift
slug: cicd-4-22-troubleshooting-issues-in-gitops
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cicd/troubleshooting-issues-in-GitOps
version: 4.22
family: cicd
documentKind: "Documentation"
---

# Troubleshooting issues in {gitops-title}

[id="troubleshooting-issues-in-GitOps"]

= Troubleshooting issues in {gitops-title}

When working with {gitops-title}, you might face issues related to performance, monitoring, configuration, and other aspects. This section helps you to understand those issues and provide solutions to resolve them.

[id="auto-reboot-during-argo-cd-sync-with-machine-configurations"]
= Issue: Auto-reboot during Argo CD sync with machine configurations

In the Red Hat OpenShift Container Platform, nodes are updated automatically through the Red Hat OpenShift Machine Config Operator (MCO). A Machine Config Operator (MCO) is a custom resource that is used by the cluster to manage the complete life cycle of its nodes.

When an MCO resource is created or updated in a cluster, the MCO picks up the update, performs the necessary changes to the selected nodes, and restarts the nodes gracefully by cordoning, draining, and rebooting those nodes. It handles everything from the kernel to the kubelet.

However, interactions between the MCO and the GitOps workflow can introduce major performance issues and other undesired behaviors. This section shows how to make the MCO and the Argo CD GitOps orchestration tool work well together.

[id="performance-challenges-in-machine-configurations-and-argo-cd"]
= Solution: Enhance performance in machine configurations and Argo CD

When you are using a Machine Config Operator as part of a GitOps workflow, the following sequence can produce suboptimal performance:

* Argo CD starts an automated sync job after a commit to the Git repository that contains application resources.

* If Argo CD notices a new or an updated machine configuration while the sync operation is in process, MCO picks up the change to the machine configuration and starts rebooting the nodes to apply the change.

* If a rebooting node in the cluster contains the Argo CD application controller, the application controller terminates, and the application sync is aborted.

As the MCO reboots the nodes in sequential order, and the Argo CD workloads can be rescheduled on each reboot, it can take some time for the sync to be completed. This results in an undefined behavior until the MCO has rebooted all nodes affected by the machine configurations within the sync.

[role="_additional-resources"]
[id="additional-resources_troubleshooting-issues-in-GitOps"]
== Additional resources
* Preventing nodes from auto-rebooting during Argo CD sync with machine configs
