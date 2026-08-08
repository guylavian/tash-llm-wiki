---
title: "kubeadm kubeconfig"
type: reference
domain: openshift
slug: reference-kubeadm-kubeconfig
tier: reference
source: https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-kubeconfig
family: reference
documentKind: "doc"
---

# kubeadm kubeconfig

`kubeadm kubeconfig` provides utilities for managing kubeconfig files.

For examples on how to use `kubeadm kubeconfig user` see
[Generating kubeconfig files for additional users](/docs/tasks/administer-cluster/kubeadm/kubeadm-certs#kubeconfig-additional-users).

## kubeadm kubeconfig {#cmd-kubeconfig}

{{< tabs name="tab-kubeconfig" >}}
{{< tab name="overview" include="generated/kubeadm_kubeconfig/_index.md" />}}
{{< /tabs >}}

## kubeadm kubeconfig user {#cmd-kubeconfig-user}

This command can be used to output a kubeconfig file for an additional user.

{{< tabs name="tab-kubeconfig-user" >}}
{{< tab name="user" include="generated/kubeadm_kubeconfig/kubeadm_kubeconfig_user.md" />}}
{{< /tabs >}}
