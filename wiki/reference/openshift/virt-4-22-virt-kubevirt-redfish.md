---
title: "Configuring KubeVirt Redfish for VM management"
type: reference
domain: openshift
slug: virt-4-22-virt-kubevirt-redfish
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virt/virt-kubevirt-redfish
version: 4.22
family: virt
documentKind: "Documentation"
---

# Configuring KubeVirt Redfish for VM management

[id="virt-kubevirt-redfish"]
= Configuring KubeVirt Redfish for VM management

[role="_abstract"]
KubeVirt Redfish exposes {VirtProductName} virtual machines (VMs) through a Redfish-compatible API.
This enables external tools and orchestration systems to manage VM power states, query inventory, and attach virtual media using the industry-standard Redfish protocol.

Use KubeVirt Redfish when you need programmatic control over VMs using Redfish, such as deploying virtualized control planes or automating VM lifecycle management.

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-kubevirt-redfish.adoc

[id="con_virt-about-kubevirt-redfish_{context}"]
= About KubeVirt Redfish

[role="_abstract"]
KubeVirt Redfish is a Redfish-compatible API that exposes virtual machines (VMs) managed by {VirtProductName} on OpenShift Container Platform.
You can use the same Redfish automation patterns you use for physical baseboard management controllers (BMCs) to manage VM power and inventory.
The primary use case is deploying virtualized control plane clusters, where the control plane nodes run as VMs on an existing {VirtProductName} cluster.

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-kubevirt-redfish.adoc

[id="con_virt-kubevirt-redfish-architecture_{context}"]
= KubeVirt Redfish architecture

[role="_abstract"]
KubeVirt Redfish is deployed on the hosting cluster as a Deployment resource and is exposed using Service and Route resources. KubeVirt Redfish connects to the cluster API to list and control the KubeVirt VMs you expose through configuration.

Requests arrive at the KubeVirt Redfish endpoint, which is exposed as an OpenShift Container Platform Route. KubeVirt Redfish then translates supported Redfish operations into KubeVirt API calls to manage VM power state, inventory, and virtual media.

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-kubevirt-redfish.adoc

[id="con_virt-kubevirt-redfish-vs-bmc_{context}"]
= How KubeVirt Redfish differs from physical BMC Redfish

[role="_abstract"]
Redfish is commonly used with physical baseboard management controllers (BMCs) for bare metal deployments, where it manages hardware power state, boot configuration, and provisioning.

KubeVirt Redfish is different in some of the following ways:

* It targets VMs managed by {VirtProductName}, not physical servers.
* It runs as a service on your cluster, not on hardware BMCs.
* You can use it for virtualized control plane deployments where physical BMC Redfish supports bare metal deployments.

The two are complementary and can be used together in environments with mixed physical and virtual nodes.

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

// Commented out - detailed parameter reference may be added back later
// include::modules/ref_virt-kubevirt-redfish-configuration-parameters.adoc[leveloffset=+1]

// Module included in the following assemblies:
//
// * virt/post_installation_configuration/virt-kubevirt-redfish.adoc

[id="ref_virt-kubevirt-redfish-api-endpoints_{context}"]
= Supported Redfish API endpoints

[role="_abstract"]
KubeVirt Redfish implements a subset of the Redfish standard for managing virtual machines.
The following table lists the supported API endpoints.

Access these endpoints using the full URL format `\https://<route_hostname>/<endpoint_path>`, where `<route_hostname>` is the KubeVirt Redfish Route hostname.

[NOTE]
====
In endpoint paths, `{system_id}` refers to the VM identifier.
With the `enhanced` system ID convention, this is `<namespace>.<vm-name>`.
With the `legacy` convention, this is `<vm-name>` only.
====

.Supported Redfish API endpoints
[cols="1,2,3",options="header"]
|===
|Method |Endpoint |Description

|GET
|`/redfish/v1/`
|Service root. Returns available resource collections.

|GET
|`/redfish/v1/Systems`
|List all VMs exposed as Redfish systems.

|GET
|`/redfish/v1/Systems/{system_id}`
|Get details for a specific VM, including power state and boot settings.

|POST
|`/redfish/v1/Systems/{system_id}/Actions/ComputerSystem.Reset`
|Power operations. Supported `ResetType` values: `On`, `ForceOff`, `GracefulShutdown`.

|GET
|`/redfish/v1/Systems/{system_id}/VirtualMedia/Cd`
|Get VirtualMedia status for the VM's virtual CD drive.

|POST
|`/redfish/v1/Systems/{system_id}/VirtualMedia/Cd/Actions/VirtualMedia.InsertMedia`
|Attach an ISO image to the VM. Requires `Image` URL parameter.

|POST
|`/redfish/v1/Systems/{system_id}/VirtualMedia/Cd/Actions/VirtualMedia.EjectMedia`
|Detach the ISO image from the VM.

|PATCH
|`/redfish/v1/Systems/{system_id}`
|Modify boot settings. Set `Boot.BootSourceOverrideTarget` (`Cd`, `Hdd`, `Pxe`) and `Boot.BootSourceOverrideEnabled` (`Once`, `Continuous`, `Disabled`).
|===

// Commented out - troubleshooting section may be added back later
// include::modules/proc_virt-troubleshooting-kubevirt-redfish.adoc[leveloffset=+1]

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* BMC addressing for installer-provisioned infrastructure
* Deploying far edge sites with ZTP
* Redfish standard (DMTF)
