---
title: "ControllerManagerReleaseLeaderElectionLockOnExit"
type: reference
domain: openshift
slug: reference-controllermanagerreleaseleaderelectionlockonexit
tier: reference
source: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/ControllerManagerReleaseLeaderElectionLockOnExit
family: reference
documentKind: "doc"
---

# ControllerManagerReleaseLeaderElectionLockOnExit

Enables the `kube-controller-manager` to actively release its leader election lock
during leader transitions, rather than waiting for the lock's TTL to expire.
This allows a new leader to be elected more quickly.
