# Kubernetes storage — distilled notes

Source: Kubernetes docs, *Concepts → Storage* (<https://kubernetes.io/docs/concepts/storage/>).
Paraphrased.

## The PV / PVC split
- **PersistentVolume (PV)** — a cluster-scoped piece of storage (provisioned by an admin
  or dynamically). Has a lifecycle independent of any pod.
- **PersistentVolumeClaim (PVC)** — a namespaced *request* for storage (size + access
  mode). A pod mounts a PVC; the PVC binds to a PV that satisfies it.
- **Access modes**: `ReadWriteOnce` (RWO — one node), `ReadOnlyMany` (ROX),
  `ReadWriteMany` (RWX — many nodes, needs a file/shared backend), `ReadWriteOncePod`
  (exactly one pod).

## StorageClass + dynamic provisioning
- A **StorageClass** names a provisioner (a CSI driver) and parameters. A PVC that
  references a StorageClass triggers **dynamic provisioning** — the PV is created on
  demand, no pre-provisioning.
- The **default StorageClass** is used when a PVC omits `storageClassName`. A PVC with no
  matching class/PV stays **Pending** (a common "pod stuck in Pending/ContainerCreating"
  root cause).
- **reclaimPolicy**: `Delete` (default for dynamic — deleting the PVC deletes the volume)
  vs `Retain` (keep the volume for manual recovery).

## CSI
- The **Container Storage Interface** is the standard plugin model; storage vendors ship
  CSI drivers. In-tree volume plugins are deprecated/migrated to CSI.

## OpenShift note
- OCP ships CSI drivers/operators per platform (e.g. AWS EBS, vSphere, ODF) and sets a
  default StorageClass. `volumeBindingMode: WaitForFirstConsumer` delays binding until a
  pod is scheduled so the volume lands in the pod's zone.
