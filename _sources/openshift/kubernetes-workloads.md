# Kubernetes workloads — distilled notes

Source: Kubernetes docs, *Concepts → Workloads* (<https://kubernetes.io/docs/concepts/workloads/>).
Paraphrased; load-bearing facts only.

## Pod
- The smallest deployable unit: one or more containers sharing a network namespace
  (one IP/port space) and storage volumes. Containers in a pod are always co-scheduled
  on the same node.
- Pods are **ephemeral and disposable** — you almost never create bare pods directly;
  a workload controller creates and replaces them. A pod's identity (name, IP) does not
  survive rescheduling.

## Workload controllers
- **Deployment** — declarative management of a **stateless** set of replica pods via an
  underlying ReplicaSet. Supports rolling updates and rollback. The default choice for
  stateless apps.
- **ReplicaSet** — keeps a stable set of replica pods running; normally owned by a
  Deployment rather than used directly.
- **StatefulSet** — for **stateful** apps needing stable, unique network identities
  (ordinal pod names `web-0`, `web-1`) and stable per-pod persistent storage. Ordered,
  graceful deployment/scaling.
- **DaemonSet** — ensures **one pod per (matching) node** — used for node-level agents
  (log shippers, CNI, monitoring). New nodes get the pod automatically.
- **Job** — runs pods to **completion** (batch). **CronJob** — runs Jobs on a schedule.

## Health + scheduling levers
- **Probes**: *liveness* (restart the container if it fails), *readiness* (remove the
  pod from Service endpoints until it passes), *startup* (gate the other probes for
  slow-starting apps).
- **Resource requests** drive scheduling (the scheduler places a pod only where the
  request fits) and **limits** cap usage (CPU is throttled; exceeding a memory limit
  gets the container OOM-killed).
- A pod with an unschedulable request stays **Pending**; the Deployment never reaches
  its desired replica count.

## OpenShift note
- OpenShift runs all of the above unchanged (it *is* Kubernetes) and adds
  `DeploymentConfig` (an older OpenShift-native controller with triggers/hooks) — though
  Kubernetes `Deployment` is the recommended default on modern OCP.
