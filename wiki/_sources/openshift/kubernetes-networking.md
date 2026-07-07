# Kubernetes networking — distilled notes

Source: Kubernetes docs, *Concepts → Services, Load Balancing, and Networking*
(<https://kubernetes.io/docs/concepts/services-networking/>). Paraphrased.

## Service
- A stable virtual endpoint (a `ClusterIP` + DNS name) in front of a changing set of
  pods selected by label. Solves pod-IP churn: clients talk to the Service, kube-proxy
  load-balances to ready pod endpoints.
- Types: **ClusterIP** (internal only, default), **NodePort** (exposes on every node's
  IP at a static port), **LoadBalancer** (provisions an external cloud LB),
  **ExternalName** (CNAME alias).
- Only pods that pass their **readiness probe** are in the Service's endpoint set.

## Ingress vs OpenShift Route
- **Ingress** — Kubernetes API for HTTP/HTTPS routing (host/path rules, TLS) to
  Services; requires an ingress controller to implement it.
- **Route** — OpenShift's older, native external-HTTP object, served by the built-in
  HAProxy-based **Ingress/Router** operator. Routes support edge/passthrough/re-encrypt
  TLS termination. On OCP, an Ingress is reconciled into a Route under the hood.

## NetworkPolicy
- Namespaced, pod-selector-based **allow-list** firewall rules for pod-to-pod and
  pod-to-external traffic (ingress/egress). **Default is allow-all**; the first policy
  selecting a pod flips it to default-deny for that direction. Requires a CNI that
  enforces policy (OpenShift's default **OVN-Kubernetes** does).

## Cluster DNS
- CoreDNS gives every Service a name `*.<namespace>.svc.cluster.local`; pods resolve
  Services by name. Headless Services (StatefulSet) get per-pod DNS records.
