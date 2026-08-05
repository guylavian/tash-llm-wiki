---
title: "Understanding networking settings"
type: reference
domain: openshift
slug: microshift-networking-4-22-microshift-networking-settings
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_networking/microshift-networking-settings
version: 4.22
family: microshift_networking
documentKind: "Documentation"
---

# Understanding networking settings

[id="microshift-understanding-networking-settings"]
= Understanding networking settings

[role="_abstract"]
Learn how to apply networking customization and default settings to {microshift-short} deployments. Each node is contained to a single machine and single {microshift-short}, so each deployment requires individual configuration, pods, and settings.

{microshift-short} administrators have several options for exposing applications that run inside a node to external traffic and securing network connections:

* A service such as NodePort

* API resources, such as `Ingress` and `Route`

By default, Kubernetes allocates each pod an internal IP address for applications running within the pod. Pods and their containers can have traffic between them, but clients outside the node do not have direct network access to pods except when exposed with a service such as NodePort.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-config-OVN-K_{context}"]
= Creating an OVN-Kubernetes configuration file

[role="_abstract"]
{microshift-short} uses built-in default OVN-Kubernetes values if an OVN-Kubernetes configuration file is not created. To apply custom OVN-Kubernetes values such as pod `mtu` instead of using built-in defaults, you can copy `ovn.yaml.default` to `/etc/microshift/ovn.yaml` and edit the file.

.Procedure

. To create your `ovn.yaml` file, run the following command:
+
[source, yaml]
----
$ sudo cp /etc/microshift/ovn.yaml.default /etc/microshift/ovn.yaml
----

. To list the contents of the configuration file you created, run the following command:
+
[source, yaml]
----
$ cat /etc/microshift/ovn.yaml
----
+
.Example YAML file with default maximum transmission unit (MTU) value
[source,yaml]
----
mtu: 1400
----

. To customize your configuration, you can change the MTU value. The table that follows provides details:
+
.Supported optional OVN-Kubernetes configurations for {microshift-short}
[cols="5",options="header"]
|===
|Field
|Type
|Default
|Description
|Example

|mtu
|uint32
|auto
|MTU value used for the pods
|1300
|===
+
[IMPORTANT]
====
If you change the `mtu` configuration value in the `ovn.yaml` file, you must restart the host that OpenShift Container Platform is running on to apply the updated setting.
====
+
.Example custom `ovn.yaml` configuration file
[source, yaml]
----
mtu: 1300
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-restart-ovnkube-master_{context}"]
= Restarting the ovnkube-master pod

[role="_abstract"]
To replace the `ovnkube-master` pod with a new instance on {microshift-short}, you can delete the existing pod in the `openshift-ovn-kubernetes` namespace. Confirm that a new pod appears when you list pods in that namespace.

.Prerequisites

* The OpenShift CLI (`oc`) is installed.
* You have root access to the node.
* A node installed on infrastructure configured with the OVN-Kubernetes network plugin.
* The KUBECONFIG environment variable is set.

.Procedure

. Access the remote node by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=$PWD/kubeconfig
----

. Find the name of the `ovnkube-master` pod that you want to restart by running the following command:
+
[source,terminal]
----
$ pod=$(oc get pods -n openshift-ovn-kubernetes | awk -F " " '/ovnkube-master/{print $1}')
----

. Delete the `ovnkube-master` pod by running the following command:
+
[source,terminal]
----
$ oc -n openshift-ovn-kubernetes delete pod $pod
----

. Confirm that a new `ovnkube-master` pod is running by using the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ovn-kubernetes
----
+
The listing of the running pods shows a new `ovnkube-master` pod name and age.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-http-proxy_{context}"]
= Deploying {microshift-short} behind an HTTP or HTTPS proxy

[role="_abstract"]
To add basic anonymity and security measures to your pods, you can deploy {microshift-short} behind an HTTP or HTTPS proxy.

You must configure the host operating system to use the proxy service with all components initiating HTTP or HTTPS requests when deploying {microshift-short} behind a proxy.

All the user-specific workloads or pods with egress traffic, such as accessing cloud services, must be configured to use the proxy. There is no built-in transparent proxying of egress traffic in {microshift-short}.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-rpm-ostree-https_{context}"]
= Using the RPM-OStree HTTP or HTTPS proxy

[role="_abstract"]
To use the HTTP or HTTPS proxy in RPM-OStree, add a `Service` section to the configuration file and set the `http_proxy environment` variable for the `rpm-ostreed` service.

.Procedure

. Add this setting to the `/etc/systemd/system/rpm-ostreed.service.d/00-proxy.conf` file:
+
[source,terminal]
----
[Service]
Environment="http_proxy=http://$PROXY_USER:$PROXY_PASSWORD@$PROXY_SERVER:$PROXY_PORT/"
----

. Next, reload the configuration settings and restart the service to apply your changes.
+
.. Reload the configuration settings by running the following command:
+
[source,terminal]
----
$ sudo systemctl daemon-reload
----
+
.. Restart the `rpm-ostreed` service by running the following command:
+
[source,terminal]
----
$ sudo systemctl restart rpm-ostreed.service
----
//Q: Instructions for how to test that the proxy works by booting the image, verifying that MicroShift starts, and that the application is accessible?

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-CRI-O-container-engine_{context}"]
= Using a proxy in the CRI-O container runtime

[role="_abstract"]
To use an HTTP or HTTPS proxy in CRI-O, you can add a systemd `Service` drop-in file that defines the `HTTP_PROXY`, `HTTPS_PROXY`, and optional `NO_PROXY` environment variables. You can reload systemd, restart `crio`, and restart the {microshift-short} service so the proxy settings apply.

.Procedure

. Create the directory for the configuration file if it does not exist:
+
[source,terminal]
----
$ sudo mkdir /etc/systemd/system/crio.service.d/
----

. Add the following settings to the `/etc/systemd/system/crio.service.d/00-proxy.conf` file:
+
[source,config]
----
[Service]
Environment=NO_PROXY="localhost,127.0.0.1"
Environment=HTTP_PROXY="http://$PROXY_USER:$PROXY_PASSWORD@$PROXY_SERVER:$PROXY_PORT/"
Environment=HTTPS_PROXY="http://$PROXY_USER:$PROXY_PASSWORD@$PROXY_SERVER:$PROXY_PORT/"
----
+
[IMPORTANT]
====
You must define the `Service` section of the configuration file for the environment variables or the proxy settings fail to apply.
====

. Reload the configuration settings:
+
[source,terminal]
----
$ sudo systemctl daemon-reload
----

. Restart the CRI-O service:
+
[source,terminal]
----
$ sudo systemctl restart crio
----

. Restart the {microshift-short} service to apply the settings:
+
[source,terminal]
----
$ sudo systemctl restart microshift
----

.Verification

. Verify that pods are started by running the following command and examining the output:
+
[source,terminal]
----
$ oc get all -A
----

. Verify that {microshift-short} is able to pull container images by running the following command and examining the output:
+
[source,terminal]
----
$ sudo crictl images
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-OVS-snapshot_{context}"]
= Getting a snapshot of OVS interfaces from a running node

[role="_abstract"]
To capture the current state of OVS interface and data from a running {microshift-short} node, you can run `sudo ovs-vsctl` show on the node.

.Procedure

* To see a snapshot of OVS interfaces from a running {microshift-short} node, enter the following command:
+
[source,terminal]
----
$ sudo ovs-vsctl show
----
+
.Example OVS interfaces in a running node
[source,terminal]
----
9d9f5ea2-9d9d-4e34-bbd2-dbac154fdc93
    Bridge br-ex
        Port br-ex
            Interface br-ex
                type: internal
        Port patch-br-ex_localhost.localdomain-to-br-int
            Interface patch-br-ex_localhost.localdomain-to-br-int
                type: patch
                options: {peer=patch-br-int-to-br-ex_localhost.localdomain}
    Bridge br-int
        fail_mode: secure
        datapath_type: system
        Port patch-br-int-to-br-ex_localhost.localdomain
            Interface patch-br-int-to-br-ex_localhost.localdomain
                type: patch
                options: {peer=patch-br-ex_localhost.localdomain-to-br-int}
        Port eebee1ce5568761
            Interface eebee1ce5568761
        Port b47b1995ada84f4
            Interface b47b1995ada84f4
        Port "3031f43d67c167f"
            Interface "3031f43d67c167f"
        Port br-int
            Interface br-int
                type: internal
        Port ovn-k8s-mp0
            Interface ovn-k8s-mp0
                type: internal
    ovs_version: "2.17.3"
----
+
where:
+
--
`patch-br-ex_localhost.localdomain-to-br-int`:: Specifies OVS patch ports that connects `br-int`.
`patch-br-int-to-br-ex_localhost.localdomain`:: Specifies OVS patch ports that connects `br-ex`.
`eebee1ce5568761`:: Specifies the pod interface named with the first 15 bits of the pod sandbox ID and is plugged into the `br-int` bridge.
`b47b1995ada84f4`:: Specifies the pod interface named with the first 15 bits of the pod sandbox ID and is plugged into the `br-int` bridge.
`3031f43d67c167f`:: Specifies the pod interface named with the first 15 bits of the pod sandbox ID and is plugged into the `br-int` bridge.
`ovn-k8s-mp0`:: Specifies OVS internal port for hairpin traffic,`ovn-k8s-mp0` is created by the `ovnkube-master` container.
--

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-about-load-balancer-service_{context}"]
= The {microshift-short} LoadBalancer service for workloads

[role="_abstract"]
{microshift-short} has a built-in implementation of network load balancers that you can use for your workloads and applications within the node. You can create a `LoadBalancer` service by configuring a pod to interpret ingress rules and serve as an ingress controller.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-deploying-a-load-balancer_{context}"]
= Deploying a load balancer for an application

[role="_abstract"]
To expose an application through a `LoadBalancer` service that uses the node IP as the external IP in {microshift-short}, you can create a namespace, deploy the example workload, and apply the service manifest.

.Prerequisites

* The {oc-first} is installed.
* You installed a node on an infrastructure configured with the OVN-Kubernetes network plugin.
* The `KUBECONFIG` environment variable is set.

.Procedure

. Verify that your pods are running by entering the following command:
+
[source,terminal]
----
$ oc get pods -A
----
+
.Example output
[source,terminal]
----
NAMESPACE                            NAME                                                     READY   STATUS   RESTARTS  AGE
default                              i-06166fbb376f14a8bus-west-2computeinternal-debug-qtwcr  1/1     Running	   0		   46m
kube-system                          csi-snapshot-controller-5c6586d546-lprv4                 1/1     Running	   0		   51m
openshift-dns                        dns-default-45jl7                                        2/2     Running	   0		   50m
openshift-dns                        node-resolver-7wmzf                                      1/1     Running	   0		   51m
openshift-ingress                    router-default-78b86fbf9d-qvj9s                          1/1     Running 	 0		   51m
openshift-multus                     dhcp-daemon-j7qnf                                        1/1     Running    0		   51m
openshift-multus                     multus-r758z                                             1/1     Running    0		   51m
openshift-operator-lifecycle-manager catalog-operator-85fb86fcb9-t6zm7                        1/1     Running    0		   51m
openshift-operator-lifecycle-manager olm-operator-87656d995-fvz84                             1/1     Running    0		   51m
openshift-ovn-kubernetes             ovnkube-master-5rfhh                                     4/4     Running    0		   51m
openshift-ovn-kubernetes             ovnkube-node-gcnt6                                       1/1     Running    0		   51m
openshift-service-ca                 service-ca-bf5b7c9f8-pn6rk                               1/1     Running    0		   51m
openshift-storage                    topolvm-controller-549f7fbdd5-7vrmv                      5/5     Running    0		   51m
openshift-storage                    topolvm-node-rht2m                                       3/3     Running    0		   50m
----

. Create a namespace by running the following commands:
+
[source,terminal]
----
$ NAMESPACE=_<nginx_lb_test>_
----
+
* Replace _<nginx_lb_test>_ with the application namespace that you want to create.
+
[source,terminal]
----
$ oc create ns $NAMESPACE
----
+
The following example deploys three replicas of the test `nginx` application in the created namespace:
+
[source,terminal]
----
oc apply -n $NAMESPACE -f - <<EOF
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx
data:
  headers.conf: |
    add_header X-Server-IP  \$server_addr always;
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: quay.io/packit/nginx-unprivileged
        imagePullPolicy: Always
        name: nginx
        ports:
        - containerPort: 8080
        volumeMounts:
        - name: nginx-configs
          subPath: headers.conf
          mountPath: /etc/nginx/conf.d/headers.conf
        securityContext:
          allowPrivilegeEscalation: false
          seccompProfile:
            type: RuntimeDefault
          capabilities:
            drop: ["ALL"]
          runAsNonRoot: true
      volumes:
        - name: nginx-configs
          configMap:
            name: nginx
            items:
              - key: headers.conf
                path: headers.conf
EOF
----

. You can verify that the three sample replicas started successfully by running the following command:
+
[source,terminal]
----
$ oc get pods -n $NAMESPACE
----

. Create a `LoadBalancer` service for the `nginx` test application by running the following command:
+
[source,terminal]
----
oc create -n $NAMESPACE -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  ports:
  - port: 81
    targetPort: 8080
  selector:
    app: nginx
  type: LoadBalancer
EOF
----
+
[NOTE]
====
You must ensure that the `port` parameter is a host port that is not occupied by other `LoadBalancer` services or {microshift-short} components.
====

. Verify that the service file exists, that the external IP address is properly assigned, and that the external IP is identical to the node IP by running the following command:
+
[source,terminal]
----
$ oc get svc -n $NAMESPACE
----
+
.Example output
[source,terminal]
----
NAME    TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
nginx   LoadBalancer   10.43.183.104   192.168.1.241   81:32434/TCP   2m
----

.Verification

The following command forms five connections to the example `nginx` application by using the external IP address of the `LoadBalancer` service configuration. The result of the command is a list of those server IP addresses.

* Verify that the load balancer sends requests to all the running applications by running the following command:
+
[source,terminal]
----
EXTERNAL_IP=192.168.1.241
seq 5 | xargs -Iz curl -s -I http://$EXTERNAL_IP:81 | grep X-Server-IP
----
+
The output of the previous command contains different IP addresses if the `LoadBalancer` service is successfully distributing the traffic to the applications, for example:
+
.Example output
[source,terminal]
----
X-Server-IP: 10.42.0.41
X-Server-IP: 10.42.0.41
X-Server-IP: 10.42.0.43
X-Server-IP: 10.42.0.41
X-Server-IP: 10.42.0.43
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-blocking-nodeport-access_{context}"]
= Blocking external access to the NodePort service on a specific host interface

[role="_abstract"]
OVN-Kubernetes does not restrict the host interface where a `NodePort` service can be accessed from
outside a OpenShift Container Platform node. To block the `NodePort` service on a specific host interface and restrict external access, you can insert a _drop_ rule for the port and IP on a OpenShift Container Platform node.

.Prerequisites

* You must have an account with root privileges.

.Procedure

. Change the `NODEPORT` variable to the host port number assigned to your Kubernetes NodePort service by running the following command:
+
[source,terminal]
----
# export NODEPORT=30700
----

. Change the `INTERFACE_IP` value to the IP address from the host interface that you want to block. For example:
+
[source,terminal]
----
# export INTERFACE_IP=192.168.150.33
----

. Insert a new rule in the `nat` table PREROUTING chain to drop all packets that match the destination port and IP address. For example:
+
[source,terminal]
----
$ sudo nft -a insert rule ip nat PREROUTING tcp dport $NODEPORT ip daddr $INTERFACE_IP drop
----

. List the new rule by running the following command:
+
[source,terminal]
----
$ sudo nft -a list chain ip nat PREROUTING
table ip nat {
	chain PREROUTING { # handle 1
		type nat hook prerouting priority dstnat; policy accept;
		tcp dport 30700 ip daddr 192.168.150.33 drop # handle 134
		counter packets 108 bytes 18074 jump OVN-KUBE-ETP # handle 116
		counter packets 108 bytes 18074 jump OVN-KUBE-EXTERNALIP # handle 114
		counter packets 108 bytes 18074 jump OVN-KUBE-NODEPORT # handle 112
	}
}
----
+
[NOTE]
====
Note the `handle` number of the newly added rule. You need to remove the `handle` number in the following step.
====

. Remove the custom rule with the following sample command:
+
[source,terminal]
----
$ sudo nft -a delete rule ip nat PREROUTING handle 134
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-mDNS_{context}"]
= The multicast DNS protocol

[role="_abstract"]
To allow name resolution and service discovery within a Local Area Network (LAN) using multicast exposed on the `5353/UDP` port, you can use the multicast DNS protocol (mDNS).

{microshift-short} includes an embedded mDNS server for deployment scenarios in which the authoritative DNS server cannot be reconfigured to point clients to services on {microshift-short}. The embedded DNS server allows `.local` domains exposed by {microshift-short} to be discovered by other elements on the LAN.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking.adoc

[id="microshift-exposed-audit-ports_{context}"]
= Auditing exposed network ports

[role="_abstract"]
On {microshift-short}, the host port can be opened by a workload in the following cases. You can check logs to view the network services.

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking-settings.adoc

[id="microshift-exposed-audit-ports-hostnetwork_{context}"]
= hostNetwork

[role="_abstract"]
When a pod is configured with the `hostNetwork:true` setting, the pod is running in the host network namespace. This configuration can independently open host ports. {microshift-short} component logs cannot be used to track this case, the ports are subject to firewalld rules. If the port opens in firewalld, you can view the port opening in the firewalld debug log.

.Prerequisites

* You have root user access to your build host.

.Procedure

. Optional: You can check that the `hostNetwork:true` parameter is set in your ovnkube-node pod by using the following example command:
+
[source,terminal]
----
$ sudo oc get pod -n openshift-ovn-kubernetes <ovnkube-node-pod-name> -o json | jq -r '.spec.hostNetwork' true
----

. Enable debug in the firewalld log by running the following command:
+
[source,terminal]
----
$ sudo vi /etc/sysconfig/firewalld
FIREWALLD_ARGS=--debug=10
----

. Restart the firewalld service:
+
[source,terminal]
----
$ sudo systemctl restart firewalld.service
----

. To verify that the debug option was added properly, run the following command:
+
[source,terminal]
----
$ sudo systemd-cgls -u firewalld.service
----
+
The firewalld debug log is stored in the `/var/log/firewalld` path.
+
.Example logs for when the port open rule is added
[source,terminal]
----
2023-06-28 10:46:37 DEBUG1: config.getZoneByName('public')
2023-06-28 10:46:37 DEBUG1: config.zone.7.addPort('8080', 'tcp')
2023-06-28 10:46:37 DEBUG1: config.zone.7.getSettings()
2023-06-28 10:46:37 DEBUG1: config.zone.7.update('...')
2023-06-28 10:46:37 DEBUG1: config.zone.7.Updated('public')
----
+
.Example logs for when the port open rule is removed
[source,terminal]
----
2023-06-28 10:47:57 DEBUG1: config.getZoneByName('public')
2023-06-28 10:47:57 DEBUG2: config.zone.7.Introspect()
2023-06-28 10:47:57 DEBUG1: config.zone.7.removePort('8080', 'tcp')
2023-06-28 10:47:57 DEBUG1: config.zone.7.getSettings()
2023-06-28 10:47:57 DEBUG1: config.zone.7.update('...')
2023-06-28 10:47:57 DEBUG1: config.zone.7.Updated('public')
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking-settings.adoc

[id="microshift-exposed-audit-ports-hostport_{context}"]
= hostPort

[role="_abstract"]
To access host port open and close activity for workloads that use `hostPort` on {microshift-short}, you can run `journalctl -u crio` and filter for lines that contain `local port`.

.Procedure

* You can access the logs by running the following command:
+
[source,terminal]
----
$ journalctl -u crio | grep "local port"
----
+
.Example CRI-O logs when the host port is opened
[source,terminal]
----
$ Jun 25 16:27:37 rhel92 crio[77216]: time="2023-06-25 16:27:37.033003098+08:00" level=info msg="Opened local port tcp:443"
----
+
.Example CRI-O logs when the host port is closed
[source,terminal]
----
$ Jun 25 16:24:11 rhel92 crio[77216]: time="2023-06-25 16:24:11.342088450+08:00" level=info msg="Closing host port tcp:443"
----

// Module included in the following assemblies:
//
// * microshift_networking/microshift-networking-settings.adoc

[id="microshift-exposed-audit-ports-loadbalancer_{context}"]
= NodePort and LoadBalancer services

[role="_abstract"]
OVN-Kubernetes opens host ports for `NodePort` and `LoadBalancer` service types. These services add iptables rules that take the ingress traffic from the host port and forwards it to the node IP address.

Logs for the `NodePort` and `LoadBalancer` services are
presented in the following examples.

.Procedure

. To access the name of your `ovnkube-master` pods, run the following command:
+
[source,terminal]
----
$ oc get pods -n openshift-ovn-kubernetes | awk '/ovnkube-master/{print $1}'
----
+
.Example `ovnkube-master` pod name
[source,terminal]
----
ovnkube-master-n2shv
----

. You can access the `NodePort` and `LoadBalancer` services logs using your `ovnkube-master` pod and running the following example command:
+
[source,terminal]
----
$ oc logs -n openshift-ovn-kubernetes <ovnkube_master_podname> ovnkube-master | grep -E "OVN-KUBE-NODEPORT|OVN-KUBE-EXTERNALIP"
----
+
.Example `NodePort` service logs in the `ovnkube-master` container of the `ovnkube-master` pod when a host port is open
[source,terminal]
----
$ I0625 09:07:00.992980 2118395 iptables.go:27] Adding rule in table: nat, chain: OVN-KUBE-NODEPORT with args: "-p TCP -m addrtype --dst-type LOCAL --dport 32718 -j DNAT --to-destination 10.96.178.142:8081" for protocol: 0
----
+
.Example `NodePort` service logs in the `ovnkube-master` container of the `ovnkube-master` pod when a host port is closed
[source,terminal]
----
$ Deleting rule in table: nat, chain: OVN-KUBE-NODEPORT with args: "-p TCP -m addrtype --dst-type LOCAL --dport 32718 -j DNAT --to-destination 10.96.178.142:8081" for protocol: 0
----
+
.Example `LoadBalancer` service logs in the `ovnkube-master` container of the `ovnkube-master` pod when a host port is open
[source,terminal]
----
$ I0625 09:34:10.406067  128902 iptables.go:27] Adding rule in table: nat, chain: OVN-KUBE-EXTERNALIP with args: "-p TCP -d 172.16.47.129 --dport 8081 -j DNAT --to-destination 10.43.114.94:8081" for protocol: 0
----
+
.Example `LoadBalancer` service logs in the `ovnkube-master` container of the `ovnkube-master` pod when a host port is closed
[source,terminal]
----
$ I0625 09:37:00.976953  128902 iptables.go:63] Deleting rule in table: nat, chain: OVN-KUBE-EXTERNALIP with args: "-p TCP -d 172.16.47.129 --dport 8081 -j DNAT --to-destination 10.43.114.94:8081" for protocol: 0
----
