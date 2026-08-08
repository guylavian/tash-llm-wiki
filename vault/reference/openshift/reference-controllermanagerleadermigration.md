---
title: "ControllerManagerLeaderMigration"
type: reference
domain: openshift
slug: reference-controllermanagerleadermigration
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ControllerManagerLeaderMigration
family: reference
documentKind: "doc"
---

# ControllerManagerLeaderMigration

Enables Leader Migration for
[kube-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#initial-leader-migration-configuration) and
[cloud-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#deploy-cloud-controller-manager)
which allows a cluster operator to live migrate
controllers from the kube-controller-manager into an external controller-manager
(e.g. the cloud-controller-manager) in an HA cluster without downtime.
