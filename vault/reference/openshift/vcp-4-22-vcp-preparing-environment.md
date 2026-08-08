---
title: "Preparing the environment for virtualized control planes"
type: reference
domain: openshift
slug: vcp-4-22-vcp-preparing-environment
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/vcp/vcp-preparing-environment
version: 4.22
family: vcp
documentKind: "Documentation"
---

# Preparing the environment for virtualized control planes

[id="vcp-preparing-environment"]
= Preparing the environment for virtualized control planes

[role="_abstract"]
Prepare your hosting cluster environment before deploying a virtualized control plane cluster.
This includes installing and configuring KubeVirt Redfish and creating the control plane VMs.

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-kubevirt-redfish.adoc
// * vcp/vcp-preparing-environment.adoc

[id="proc_virt-installing-kubevirt-redfish_{context}"]
= Install KubeVirt Redfish

[role="_abstract"]
Install KubeVirt Redfish on your {VirtProductName} cluster by applying a series of custom resources (CRs).
These CRs create the namespace, permissions, configuration, and deployment required to expose VMs through the Redfish API.

.Prerequisites

* You have a OpenShift Container Platform cluster with {VirtProductName} installed.
* You installed the OpenShift CLI (`oc`).
* You logged in to OpenShift Container Platform as a user with `cluster-admin` privileges.

.Procedure

. Create the `Namespace` CR for KubeVirt Redfish by creating a YAML file with content such as the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  name: kubevirt-redfish
  labels:
    app.kubernetes.io/name: kubevirt-redfish
----

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f namespace.yaml
----

. Create the `ServiceAccount` CR by creating a YAML file with content such as the following example:
+
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: kubevirt-redfish
  namespace: kubevirt-redfish
  labels:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: rbac
----

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f serviceaccount.yaml
----

. Create the `ClusterRole` CR with required permissions by creating a YAML file with content such as the following example:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kubevirt-redfish-role
  labels:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: rbac
rules:
  - apiGroups: ["kubevirt.io"]
    resources: ["virtualmachines", "virtualmachineinstances"]
    verbs: ["get", "list", "watch", "update", "patch"]
  - apiGroups: ["kubevirt.io"]
    resources: ["virtualmachines/status", "virtualmachineinstances/status"]
    verbs: ["get", "list", "watch", "patch"]
  - apiGroups: ["kubevirt.io"]
    resources: ["virtualmachines/restart", "virtualmachines/start", "virtualmachines/stop"]
    verbs: ["create"]
  - apiGroups: ["subresources.kubevirt.io"]
    resources: ["virtualmachineinstances/pause", "virtualmachineinstances/unpause"]
    verbs: ["create", "update"]
  - apiGroups: [""]
    resources: ["pods", "services", "configmaps", "secrets"]
    verbs: ["get", "list", "watch", "create", "update", "delete"]
  - apiGroups: [""]
    resources: ["namespaces"]
    verbs: ["get", "list"]
  - apiGroups: ["cdi.kubevirt.io"]
    resources: ["datavolumes", "volumeimportsources"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims"]
    verbs: ["get", "list", "create", "update", "patch", "delete", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get", "list"]
----

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f clusterrole.yaml
----

. Create the `ClusterRoleBinding` CR by creating a YAML file with content such as the following example:
+
[source,yaml]
----
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubevirt-redfish-binding
  labels:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: rbac
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kubevirt-redfish-role
subjects:
  - kind: ServiceAccount
    name: kubevirt-redfish
    namespace: kubevirt-redfish
----

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f clusterrolebinding.yaml
----

. Create the `Secret` CR containing the configuration by creating a YAML file with content such as the following example.
Edit the `config.yaml` section to match your environment:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: kubevirt-redfish-secret
  namespace: kubevirt-redfish
  labels:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: config
type: Opaque
stringData:
  config.yaml: |
    server:
      host: "0.0.0.0"
      port: 8443
      tls:
        enabled: false
    system_id_convention: "enhanced"
    chassis:
      - name: "<chassis_name>"
        namespace: "<vm_namespace>"
        service_account: "kubevirt-redfish"
        vm_selector:
          labels:
            redfish-enabled: "true"
    authentication:
      users:
        - username: "admin"
          password: "<password>"
          chassis: ["<chassis_name>"]
    datavolume:
      storage_class: "<storage_class>"
      storage_size: "3Gi"
----
+
where:

* `system_id_convention` specifies the format for Redfish system IDs. The recommended setting is `enhanced` to use `<namespace>.<vm-name>` format. The `legacy` setting uses `<vm-name>` only.
* `chassis` specifies the namespaces where VMs are deployed. Replace `<chassis_name>` with a name for this chassis configuration and `<vm_namespace>` with the namespace containing your VMs. The `vm_selector` labels identify which VMs in the namespace are exposed through Redfish. Only VMs with matching labels are visible. You can configure multiple chassis entries to expose different subsets of VMs in the same namespace, each with different authentication users.
* `authentication` specifies the username and password required to access the Redfish API. These credentials enable full management control over exposed VMs, independently of any OpenShift Container Platform privileges. Replace `<password>` with a secure password.
* `datavolume` specifies storage for VirtualMedia operations. Replace `<storage_class>` with a storage class available on your cluster, such as `lvms-vg1` or `ocs-storagecluster-ceph-rbd-virtualization`. For more information about storage options, see _Storage requirements_ in "Prerequisites for virtualized control planes".

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f secret.yaml
----
+
[WARNING]
====
The credentials defined in this `Secret` CR enable full management control over the VMs exposed through KubeVirt Redfish, independently of any OpenShift Container Platform privileges.
====

. Create the `Deployment` CR by creating a YAML file with content such as the following example:
+
[source,yaml,subs="attributes+"]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kubevirt-redfish
  namespace: kubevirt-redfish
  labels:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: server
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: kubevirt-redfish
      app.kubernetes.io/component: server
  template:
    metadata:
      labels:
        app.kubernetes.io/name: kubevirt-redfish
        app.kubernetes.io/component: server
    spec:
      serviceAccountName: kubevirt-redfish
      securityContext:
        runAsNonRoot: true
      containers:
        - name: kubevirt-redfish
          image: registry.redhat.io/container-native-virtualization/kubevirt-redfish-rhel9:v
          imagePullPolicy: Always
          ports:
            - name: http
              containerPort: 8443
              protocol: TCP
          env:
            - name: CONFIG_PATH
              value: "/app/config/config.yaml"
            - name: LOG_LEVEL
              value: "info"
          resources:
            requests:
              memory: "512Mi"
              cpu: "100m"
            limits:
              memory: "2Gi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /redfish/v1/
              port: 8443
              scheme: HTTP
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /redfish/v1/
              port: 8443
              scheme: HTTP
            initialDelaySeconds: 5
            periodSeconds: 5
          securityContext:
            runAsNonRoot: true
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL
          volumeMounts:
            - name: config-volume
              mountPath: /app/config
              readOnly: true
      volumes:
        - name: config-volume
          secret:
            secretName: kubevirt-redfish-secret
----
where:
+
* The `image` field specifies the KubeVirt Redfish container image.

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f deployment.yaml
----

. Create the `Service` CR by creating a YAML file with content such as the following example:
+
[source,yaml]
----
apiVersion: v1
kind: Service
metadata:
  name: kubevirt-redfish
  namespace: kubevirt-redfish
  labels:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: server
spec:
  type: ClusterIP
  ports:
    - name: http
      port: 8443
      targetPort: 8443
      protocol: TCP
  selector:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: server
----

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f service.yaml
----

. Create the `Route` CR to expose the Redfish API externally by creating a YAML file with content such as the following example:
+
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: kubevirt-redfish
  namespace: kubevirt-redfish
  labels:
    app.kubernetes.io/name: kubevirt-redfish
    app.kubernetes.io/component: server
spec:
  port:
    targetPort: http
  to:
    kind: Service
    name: kubevirt-redfish
    weight: 100
  tls:
    termination: edge
    insecureEdgeTerminationPolicy: Redirect
----

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f route.yaml
----

.Verification

. Verify that the pods are running by running the following command:
+
[source,terminal]
----
$ oc get pods -n kubevirt-redfish
----
+
.Example output
[source,terminal]
----
NAME                                READY   STATUS    RESTARTS   AGE
kubevirt-redfish-587cd94988-xthml   1/1     Running   0          2m
----

. Get the route hostname by running the following command:
+
[source,terminal]
----
$ oc get route kubevirt-redfish -n kubevirt-redfish -o jsonpath='{.spec.host}'
----

. Test the Redfish endpoint by running the following command:
+
[source,terminal]
----
$ curl -sk -u "admin:<password>" https://<route_hostname>/redfish/v1/
----
+
A successful response returns JSON with the Redfish service root:
+
[source,json]
----
{
  "@odata.id": "/redfish/v1",
  "@odata.type": "#ServiceRoot.v1_0_0.ServiceRoot",
  "Id": "RootService",
  "Name": "Root Service",
  "Systems": {
    "@odata.id": "/redfish/v1/Systems"
  }
}
----

// Module included in the following assemblies:
//
// * vcp/vcp-preparing-environment.adoc

[id="proc_virt-creating-vcp-vms_{context}"]
= Create control plane VMs

[role="_abstract"]
Create VMs on the hosting cluster that will become the control plane nodes for your virtualized control plane cluster.

.Prerequisites

* KubeVirt Redfish is installed and configured on the hosting cluster.
* The hosting cluster has a network configured to provide Layer 2 connectivity between VMs.

.Procedure

. Enable the `RebootPolicy` feature gate on the hosting cluster by running the following command:
+
[source,terminal]
----
$ oc annotate --overwrite -n openshift-cnv hyperconverged kubevirt-hyperconverged \
    kubevirt.kubevirt.io/jsonpatch='[{"op":"add","path":"/spec/configuration/developerConfiguration/featureGates/-","value":"RebootPolicy"}]'
----
+
[NOTE]
====
The `RebootPolicy` feature gate enables the `rebootPolicy` field in `VirtualMachine` specifications.
This configuration is required when using KubeVirt Redfish for cluster installation.
The feature gate is enabled through an annotation on the `HyperConverged` resource, which propagates the configuration to the underlying `KubeVirt` CR.
====

. Enable the `declarativeHotplugVolumes` feature gate on the hosting cluster by running the following command:
+
[source,terminal]
----
$ oc patch hyperconverged kubevirt-hyperconverged -n openshift-cnv \
    --type merge \
    -p '{"spec": {"featureGates": {"declarativeHotplugVolumes": true}}}'
----
+
[NOTE]
====
The `declarativeHotplugVolumes` feature gate enables KubeVirt Redfish to dynamically attach boot media to VMs through the Redfish API.
This configuration is required when using KubeVirt Redfish for cluster installation.
====

. Create a `VirtualMachine` CR for each control plane node by creating a YAML file with content such as the following example:
+
[source,yaml]
----
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: master-0
  namespace: <vm_namespace>
  labels:
    redfish-enabled: "true"
spec:
  runStrategy: Halted
  template:
    metadata:
      labels:
        redfish-enabled: "true"
    spec:
      domain:
        rebootPolicy: Terminate
        cpu:
          cores: 8
        memory:
          guest: 16Gi
        devices:
          disks:
            - name: rootdisk
              disk:
                bus: virtio
            - name: cloudinitdisk
              disk:
                bus: virtio
          interfaces:
            - name: default
              bridge: {}
      networks:
        - name: default
          multus:
            networkName: <network_attachment_definition>
      volumes:
        - name: rootdisk
          dataVolume:
            name: master-0-disk
        - name: cloudinitdisk
          cloudInitNoCloud:
            userData: |
              #cloud-config
              hostname: master-0
              user: core
----
+
where:
+
* `<vm_namespace>` specifies the namespace for the VMs. Must match the namespace specified in the KubeVirt Redfish chassis configuration.
* `redfish-enabled: "true"` specifies the label that must match the `vm_selector` labels in the KubeVirt Redfish configuration so the VM is exposed through the Redfish API.
* `runStrategy: Halted` specifies that VMs must be powered off initially. The installation powers them on by using the Redfish API.
* `rebootPolicy: Terminate` specifies the reboot behavior required for Redfish API boot override operations. Ensures the VM terminates cleanly when boot media changes.
* `cores: 8` and `guest: 16Gi` specify the minimum recommended resources for control plane nodes.
* `<network_attachment_definition>` specifies the name of a `NetworkAttachmentDefinition` configured on your hosting cluster. All control plane VMs must share the same L2 network segment. Common options include localnet, Linux bridge, or OVN Layer 2 networks.
+
[IMPORTANT]
====
For production deployments, configure anti-affinity rules to ensure control plane VMs are distributed across different physical nodes.
This prevents a single node failure from affecting multiple control plane VMs simultaneously.
Add pod anti-affinity rules or topology spread constraints to the VM specification based on your environment requirements.
====

. Apply the resource by running the following command:
+
[source,terminal]
----
$ oc apply -f master-0.yaml
----

If required, create further VMs for `master-1` and `master-2`, for example.

.Verification

* Verify that the VMs are created and powered off by running the following command:
+
[source,terminal]
----
$ oc get vm -n <vm_namespace>
----
+
* `vm_namespace` is the namespace of the VMs.
+
.Example output
[source,terminal]
----
NAME       AGE   STATUS    READY
master-0   1m    Stopped   False
master-1   1m    Stopped   False
master-2   1m    Stopped   False
----

* Verify that KubeVirt Redfish can discover the VMs by querying the Redfish API:
+
[source,terminal]
----
$ curl -sk -u "<username>:<password>" \
    https://<kubevirt_redfish_route>/redfish/v1/Systems
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Recommended resources for topologies
* Connecting a virtual machine to a secondary localnet user-defined network
