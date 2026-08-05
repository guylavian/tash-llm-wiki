---
title: OpenShift / Kubernetes — Workloads
type: topic
domain: openshift
slug: openshift-workloads
summary: "The spine of the workloads area — which controller (Deployment, StatefulSet, DaemonSet, Job/CronJob) fits which shape of app, how rollout strategies and probes govern availability during change, how requests/limits drive scheduling, and where OpenShift's legacy DeploymentConfig and its own deployment strategies (Rolling/Recreate/Custom) diverge from upstream Kubernetes."
sources:
  - kb:deployment
  - kb:statefulset
  - kb:daemonset
  - kb:job
  - kb:cron-jobs
  - kb:horizontal-pod-autoscale
  - kb:configure-liveness-readiness-startup-probes
  - kb:manage-resources-containers
  - kb:what-deployments-are
  - kb:deployment-strategies
  - kb:managing-deployment-processes
provenance_extracted: 9
provenance_inferred: 3
provenance_ambiguous: 0
tags: [workloads, concept]
status: draft
updated: 2026-07-02
graph_community: "OpenShift / Kubernetes — Implementation Review (Evaluation-Lens MOC)"
---

# OpenShift / Kubernetes — Workloads

**Every running thing on the cluster is a [[kubernetes-pod]]; the workloads area is about which controller creates and manages those Pods, and the two levers (probes, requests/limits) that decide their health and placement.**

## Choosing a controller

| Shape of app | Controller | Why |
|---|---|---|
| Stateless, interchangeable replicas | [[kubernetes-deployment]] | Declarative rollout via ReplicaSets; the default choice |
| Needs stable per-Pod identity/storage | [[kubernetes-statefulset]] | Stable ordinal, network name, PVC that survives rescheduling |
| One Pod per node (agents, log/metrics collectors) | [[kubernetes-daemonset]] | Automatically added/removed as nodes join/leave; no `.spec.replicas` |
| Run-to-completion / batch work | Job | Retries Pods until a target number succeed; `completions`/`parallelism`/`backoffLimit` control shape |
| Scheduled batch work | CronJob | Creates a Job on a cron schedule (`.spec.schedule`); `startingDeadlineSeconds` bounds how late a missed run may start |

A Job with `completions` and `parallelism` both unset runs one Pod to completion (non-parallel); leaving only `completions` unset and setting `parallelism` makes it a work-queue Job. `backoffLimit` (default counted retries) bounds how many times a failing Pod is retried before the Job is marked failed. A CronJob is, structurally, one line of a crontab — it creates ordinary Jobs on the given schedule and inherits all of Job's semantics.

## Rollout strategy (Kubernetes-native Deployment)
`.spec.strategy.type` is `RollingUpdate` (default) or `Recreate`:
- **RollingUpdate** — scales the new ReplicaSet up and the old one down together, bounded by `maxUnavailable` (default 25% — how far below `replicas` the Deployment may drop) and `maxSurge` (default 25% — how far above `replicas` it may temporarily rise).
- **Recreate** — kills all old Pods before creating new ones; simpler, but causes a full availability gap.

`kubectl rollout undo deployment/<name>` (optionally `--to-revision=N`) is the standard rollback when a rollout leaves the app unstable/crash-looping.

## Probes and placement
- Health during rollout and steady state is governed by [[liveness-readiness-startup-probes]] — liveness restarts, readiness gates traffic without restarting, startup delays both for slow boots.
- Placement is driven by [[resource-requests-limits]] — the scheduler places Pods by their **requests**; **limits** cap actual usage and decide the failure mode (CPU throttled, memory OOM-killed).
- Scaling replica count to demand is [[horizontal-pod-autoscaler]]'s job — it targets Deployments/StatefulSets, not DaemonSets (whose count tracks node count, not load).

## OpenShift-specific: DeploymentConfig and its strategies
OpenShift ships a second, older deployment object, `DeploymentConfig`, built on `ReplicationController` (the predecessor of `ReplicaSet`) rather than on `ReplicaSet`. **Use the Kubernetes-native `Deployment` for new workloads unless a `DeploymentConfig`-only feature is required** — `DeploymentConfig` is the legacy path, still supported but not the default.

`DeploymentConfig` supports a broader, OpenShift-only strategy set (`.spec.strategy`):
- **Rolling** (default for `DeploymentConfig`) — same idea as Kubernetes RollingUpdate, replacing old Pods with new gradually; readiness checks gate progress and the deployment times out (default `10m`) if a new Pod never becomes ready.
- **Recreate** — terminates all old Pods, then starts the new ones; supports lifecycle hooks for injecting code (e.g. `pre`/`mid`/`post` hooks) into the deployment process.
- **Custom** — you supply your own deployment behavior/controller image.
- Blue-green style cutover is mentioned as an alternative pattern for apps needing more sophisticated readiness checks than the built-in rolling strategy provides (inferred: the source note names it in passing as a "consider instead" option, not as a fourth formal `DeploymentConfig` strategy type — treat it as an application-level pattern layered on Routes/Services, not a `.spec.strategy.type` value).

`DeploymentConfig` objects also support **triggers** the Kubernetes `Deployment` object doesn't have natively: a **config change trigger** (new rollout on Pod-template change — added by default if no triggers are specified) and an **image change trigger** (new rollout when a watched [[image-streams|ImageStreamTag]] gets a new image) — the mechanism that ties [[openshift-builds-and-images]] to automatic redeploys.

## See also
- [[kubernetes-pod]] · [[kubernetes-deployment]] · [[kubernetes-statefulset]] · [[kubernetes-daemonset]] · [[liveness-readiness-startup-probes]] · [[resource-requests-limits]] · [[horizontal-pod-autoscaler]]
- [[openshift-builds-and-images]] · [[openshift-overview]] · [[openshift-implementation-review]]

## Sources
<!-- crosslink:begin (generated by crosslink.py — do not edit) -->
- [[concepts-deployment|Deployments]]
- [[concepts-statefulset|StatefulSets]]
- [[concepts-daemonset|DaemonSet]]
- [[concepts-job|Jobs]]
- [[concepts-cron-jobs|CronJob]]
- [[concepts-horizontal-pod-autoscale|Horizontal Pod Autoscaling]]
- [[tasks-configure-liveness-readiness-startup-probes|Configure Liveness, Readiness and Startup Probes]]
- [[concepts-manage-resources-containers|Resource Management for Pods and Containers]]
- [[applications-4-22-what-deployments-are|Understanding deployments]]
- [[applications-4-22-deployment-strategies|Using deployment strategies]]
- [[applications-4-22-managing-deployment-processes|Managing deployment processes]]
<!-- crosslink:end -->
