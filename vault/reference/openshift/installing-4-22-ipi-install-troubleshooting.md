---
title: "Troubleshooting the installation"
type: reference
domain: openshift
slug: installing-4-22-ipi-install-troubleshooting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/ipi-install-troubleshooting
version: 4.22
family: installing
documentKind: "Documentation"
---

# Troubleshooting the installation

[id="ipi-install-troubleshooting"]
= Troubleshooting the installation

== Troubleshooting the installation program workflow

Before troubleshooting the installation environment, it is critical to understand the overall flow of the installer-provisioned installation on bare metal. The following diagrams illustrate a troubleshooting flow with a step-by-step breakdown for the environment.

image:flow1.png[Flow-Diagram-1]

_Workflow 1 of 4_ illustrates a troubleshooting workflow when the `install-config.yaml` file has errors or the {op-system-first} images are inaccessible. See  Troubleshooting `install-config.yaml` for troubleshooting suggestions.

image:flow2.png[Flow-Diagram-2]

_Workflow 2 of 4_ illustrates a troubleshooting workflow for  bootstrap VM issues,  bootstrap VMs that cannot boot up the cluster nodes, and   inspecting logs. When installing an OpenShift Container Platform cluster without the `provisioning` network, this workflow does not apply.

image:flow3.png[Flow-Diagram-3]

_Workflow 3 of 4_ illustrates a troubleshooting workflow for cluster nodes that will not PXE boot. If installing using Redfish virtual media, each node must meet minimum firmware requirements for the installation program to deploy the node. See *Firmware requirements for installing with virtual media* in the *Prerequisites* section for additional details.

image:flow4.png[Flow-Diagram-4]

_Workflow 4 of 4_ illustrates a troubleshooting workflow from
 a non-accessible API to a validated installation.

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-install-config_{context}"]

= Troubleshooting `install-config.yaml`

The `install-config.yaml` configuration file represents all of the nodes that are part of the OpenShift Container Platform cluster. The file contains the necessary options consisting of but not limited to `apiVersion`, `baseDomain`, `imageContentSources` and virtual IP addresses. If errors occur early in the deployment of the OpenShift Container Platform cluster, the errors are likely in the `install-config.yaml` configuration file.

.Procedure

. Use the guidelines in YAML-tips.
. Verify the YAML syntax is correct using syntax-check.
. Verify the {op-system-first} QEMU images are properly defined and accessible via the URL provided in the `install-config.yaml`. For example:
+
[source,terminal]
----
$ curl -s -o /dev/null -I -w "%{http_code}\n" http://webserver.example.com:8080/rhcos-44.81.202004250133-0-qemu.<architecture>.qcow2.gz?sha256=7d884b46ee54fe87bbc3893bf2aa99af3b2d31f2e19ab5529c60636fbd0f1ce7
----
+
If the output is `200`, there is a valid response from the webserver storing the bootstrap VM image.

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-bootstrap-vm_{context}"]

= Troubleshooting bootstrap VM issues

The OpenShift Container Platform installation program spawns a bootstrap node virtual machine, which handles provisioning the OpenShift Container Platform cluster nodes.

.Procedure

. About 10 to 15 minutes after triggering the installation program, check to ensure the bootstrap VM is operational using the `virsh` command:
+
[source,terminal]
----
$ sudo virsh list
----
+
[source,terminal]
----
 Id    Name                           State
 --------------------------------------------
 12    openshift-xf6fq-bootstrap      running
----
+
[NOTE]
====
The name of the bootstrap VM is always the cluster name followed by a random set of characters and ending in the word "bootstrap."
====

. If the bootstrap VM is not running after 10-15 minutes, verify `libvirtd` is running on the system by executing the following command:
+
[source,terminal]
----
$ systemctl status libvirtd
----
+
[source,terminal]
----
● libvirtd.service - Virtualization daemon
   Loaded: loaded (/usr/lib/systemd/system/libvirtd.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2020-03-03 21:21:07 UTC; 3 weeks 5 days ago
     Docs: man:libvirtd(8)
           https://libvirt.org
 Main PID: 9850 (libvirtd)
    Tasks: 20 (limit: 32768)
   Memory: 74.8M
   CGroup: /system.slice/libvirtd.service
           ├─ 9850 /usr/sbin/libvirtd
----
+
If the bootstrap VM is operational, log in to it.

. Use the `virsh console` command to find the IP address of the bootstrap VM:
+
[source,terminal]
----
$ sudo virsh console example.com
----
+
[source,terminal]
----
Connected to domain example.com
Escape character is ^]
Red Hat Enterprise Linux CoreOS 43.81.202001142154.0 (Ootpa) 4.3
SSH host key: SHA256:BRWJktXZgQQRY5zjuAV0IKZ4WM7i4TiUyMVanqu9Pqg (ED25519)
SSH host key: SHA256:7+iKGA7VtG5szmk2jB5gl/5EZ+SNcJ3a2g23o0lnIio (ECDSA)
SSH host key: SHA256:DH5VWhvhvagOTaLsYiVNse9ca+ZSW/30OOMed8rIGOc (RSA)
ens3:  fd35:919d:4042:2:c7ed:9a9f:a9ec:7
ens4: 172.22.0.2 fe80::1d05:e52e:be5d:263f
localhost login:
----
+
[IMPORTANT]
====
When deploying an OpenShift Container Platform cluster without the `provisioning` network, you must use a public IP address and not a private IP address like `172.22.0.2`.
====

. After you obtain the IP address, log in to the bootstrap VM using the `ssh` command:
+
[NOTE]
====
In the console output of the previous step, you can use the IPv6 IP address provided by `ens3` or the IPv4 IP provided by `ens4`.
====
+
[source,terminal]
----
$ ssh core@172.22.0.2
----

If you are not successful logging in to the bootstrap VM, you have likely encountered one of the following scenarios:

* You cannot reach the `172.22.0.0/24` network. Verify the network connectivity between the provisioner and the `provisioning` network bridge. This issue might occur if you are using a `provisioning` network.

* You cannot reach the bootstrap VM through the public network. When attempting to SSH via `baremetal` network, verify connectivity on the
`provisioner` host specifically around the `baremetal` network bridge.

* You encountered `Permission denied (publickey,password,keyboard-interactive)`. When attempting to access the bootstrap VM, a `Permission denied` error might occur. Verify that the SSH key for the user attempting to log in to the VM is set within the `install-config.yaml` file.

// Module included in the following assemblies:
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-bootstrap-vm-cannot-boot_{context}"]
= Bootstrap VM cannot boot up the cluster nodes

During the deployment, it is possible for the bootstrap VM to fail to boot the cluster nodes, which prevents the VM from provisioning the nodes with the {op-system} image. This scenario can arise due to:

* A problem with the `install-config.yaml` file.
* Issues with out-of-band network access when using the baremetal network.

To verify the issue, there are three containers related to `ironic`:

* `ironic`
* `ironic-inspector`

.Procedure

. Log in to the bootstrap VM:
+
[source,terminal]
----
$ ssh core@172.22.0.2
----

. To check the container logs, execute the following:
+
[source,terminal]
----
[core@localhost ~]$ sudo podman logs -f <container_name>
----
+
Replace `<container_name>` with one of `ironic` or `ironic-inspector`. If you encounter an issue where the control plane nodes are not booting up from PXE, check the `ironic` pod. The `ironic` pod contains information about the attempt to boot the cluster nodes, because it attempts to log in to the node over IPMI.

.Potential reason
The cluster nodes might be in the `ON` state when deployment started.

.Solution
Power off the OpenShift Container Platform cluster nodes before you begin the
installation over IPMI:

[source,terminal]
----
$ ipmitool -I lanplus -U root -P <password> -H <out_of_band_ip> power off
----

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-bootstrap-vm-inspecting-logs_{context}"]
= Inspecting logs

When experiencing issues downloading or accessing the {op-system} images, first verify that the URL is correct in the `install-config.yaml` configuration file.

.Example of internal webserver hosting {op-system} images
[source,yaml]
----
bootstrapOSImage: http://<ip:port>/rhcos-43.81.202001142154.0-qemu.<architecture>.qcow2.gz?sha256=9d999f55ff1d44f7ed7c106508e5deecd04dc3c06095d34d36bf1cd127837e0c
clusterOSImage: http://<ip:port>/rhcos-43.81.202001142154.0-openstack.<architecture>.qcow2.gz?sha256=a1bda656fa0892f7b936fdc6b6a6086bddaed5dafacedcd7a1e811abb78fe3b0
----

The `coreos-downloader` container downloads resources from a webserver or from the external quay.io registry, whichever the `install-config.yaml` configuration file specifies. Verify that the `coreos-downloader` container is up and running and inspect its logs as needed.

.Procedure

. Log in to the bootstrap VM:
+
[source,terminal]
----
$ ssh core@172.22.0.2
----

. Check the status of the `coreos-downloader` container within the bootstrap VM by running the following command:

+
[source,terminal]
----
[core@localhost ~]$ sudo podman logs -f coreos-downloader
----
+
If the bootstrap VM cannot access the URL to the images, use the `curl` command to verify that the VM can access the images.

. To inspect the `bootkube` logs that indicate if all the containers launched during the deployment phase, execute the following:
+
[source,terminal]
----
[core@localhost ~]$ journalctl -xe
----
+
[source,terminal]
----
[core@localhost ~]$ journalctl -b -f -u bootkube.service
----

. Verify all the pods, including `dnsmasq`, `mariadb`, `httpd`, and `ironic`, are running:
+
[source,terminal]
----
[core@localhost ~]$ sudo podman ps
----

. If there are issues with the pods, check the logs of the containers with issues. To check the logs of the `ironic` service, run the following command:
+
[source,terminal]
----
[core@localhost ~]$ sudo podman logs ironic
----

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="investigating-an-unavailable-kubernetes-api_{context}"]
= Investigating an unavailable Kubernetes API

When the Kubernetes API is unavailable, check the control plane nodes to ensure that they are running the correct components. Also, check the hostname resolution.

.Procedure

.  Ensure that `etcd` is running on each of the control plane nodes by running the following command:
+
[source,terminal]
----
$ sudo crictl logs $(sudo crictl ps --pod=$(sudo crictl pods --name=etcd-member --quiet) --quiet)
----

. If the previous command fails, ensure that Kubelet created the `etcd` pods by running the following command:
+
[source,terminal]
----
$ sudo crictl pods --name=etcd-member
----
+
If there are no pods, investigate `etcd`.

. Check the cluster nodes to ensure they have a fully qualified domain name, and not just `localhost.localdomain`, by using the following command:
+
[source,terminal]
----
$ hostname
----
+
If a hostname is not set, set the correct hostname. For example:
+
[source,terminal]
----
$ sudo hostnamectl set-hostname <hostname>
----

. Ensure that each node has the correct name resolution in the DNS server using the `dig` command:
+
[source,terminal]
----
$ dig api.<cluster_name>.example.com
----
+
[source,terminal]
----
; <<>> DiG 9.11.4-P2-RedHat-9.11.4-26.P2.el8 <<>> api.<cluster_name>.example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 37551
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 1, ADDITIONAL: 2

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 866929d2f8e8563582af23f05ec44203d313e50948d43f60 (good)
;; QUESTION SECTION:
;api.<cluster_name>.example.com. IN A

;; ANSWER SECTION:
api.<cluster_name>.example.com. 10800 IN	A 10.19.13.86

;; AUTHORITY SECTION:
<cluster_name>.example.com. 10800 IN NS	<cluster_name>.example.com.

;; ADDITIONAL SECTION:
<cluster_name>.example.com. 10800 IN A	10.19.14.247

;; Query time: 0 msec
;; SERVER: 10.19.14.247#53(10.19.14.247)
;; WHEN: Tue May 19 20:30:59 UTC 2020
;; MSG SIZE  rcvd: 140
----
+
The output in the foregoing example indicates that the appropriate IP address for the `api.<cluster_name>.example.com` VIP is `10.19.13.86`. This IP address should reside on the `baremetal` network.

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="troubleshooting-failure-to-initialize-the-cluster_{context}"]
= Troubleshooting a failure to initialize the cluster

The installation program uses the Cluster Version Operator to create all the components of an OpenShift Container Platform cluster. When the installation program fails to initialize the cluster, you can retrieve the most important information from the `ClusterVersion` and `ClusterOperator` objects.

.Procedure

. Inspect the `ClusterVersion` object by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get clusterversion -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: ClusterVersion
metadata:
  creationTimestamp: 2019-02-27T22:24:21Z
  generation: 1
  name: version
  resourceVersion: "19927"
  selfLink: /apis/config.openshift.io/v1/clusterversions/version
  uid: 6e0f4cf8-3ade-11e9-9034-0a923b47ded4
spec:
  channel: stable-4.1
  clusterID: 5ec312f9-f729-429d-a454-61d4906896ca
status:
  availableUpdates: null
  conditions:
  - lastTransitionTime: 2019-02-27T22:50:30Z
    message: Done applying 4.1.1
    status: "True"
    type: Available
  - lastTransitionTime: 2019-02-27T22:50:30Z
    status: "False"
    type: Failing
  - lastTransitionTime: 2019-02-27T22:50:30Z
    message: Cluster version is 4.1.1
    status: "False"
    type: Progressing
  - lastTransitionTime: 2019-02-27T22:24:31Z
    message: 'Unable to retrieve available updates: unknown version 4.1.1
    reason: RemoteFailed
    status: "False"
    type: RetrievedUpdates
  desired:
    image: registry.svc.ci.openshift.org/openshift/origin-release@sha256:91e6f754975963e7db1a9958075eb609ad226968623939d262d1cf45e9dbc39a
    version: 4.1.1
  history:
  - completionTime: 2019-02-27T22:50:30Z
    image: registry.svc.ci.openshift.org/openshift/origin-release@sha256:91e6f754975963e7db1a9958075eb609ad226968623939d262d1cf45e9dbc39a
    startedTime: 2019-02-27T22:24:31Z
    state: Completed
    version: 4.1.1
  observedGeneration: 1
  versionHash: Wa7as_ik1qE=
----

. View the conditions by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get clusterversion version \
     -o=jsonpath='{range .status.conditions[*]}{.type}{" "}{.status}{" "}{.message}{"\n"}{end}'
----
+
Some of most important conditions include `Failing`, `Available` and `Progressing`.
+
.Example output
[source,terminal]
----
Available True Done applying 4.1.1
Failing False
Progressing False Cluster version is 4.0.0-0.alpha-2019-02-26-194020
RetrievedUpdates False Unable to retrieve available updates: unknown version 4.1.1
----

. Inspect the `ClusterOperator` object by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get clusteroperator
----
+
The command returns the status of the cluster Operators.
+
.Example output
[source,terminal]
----
NAME                                  VERSION   AVAILABLE   PROGRESSING   FAILING   SINCE
cluster-baremetal-operator                      True        False         False     17m
cluster-autoscaler                              True        False         False     17m
cluster-storage-operator                        True        False         False     10m
console                                         True        False         False     7m21s
dns                                             True        False         False     31m
image-registry                                  True        False         False     9m58s
ingress                                         True        False         False     10m
kube-apiserver                                  True        False         False     28m
kube-controller-manager                         True        False         False     21m
kube-scheduler                                  True        False         False     25m
machine-api                                     True        False         False     17m
machine-config                                  True        False         False     17m
marketplace-operator                            True        False         False     10m
monitoring                                      True        False         False     8m23s
network                                         True        False         False     13m
node-tuning                                     True        False         False     11m
openshift-apiserver                             True        False         False     15m
openshift-authentication                        True        False         False     20m
openshift-cloud-credential-operator             True        False         False     18m
openshift-controller-manager                    True        False         False     10m
openshift-samples                               True        False         False     8m42s
operator-lifecycle-manager                      True        False         False     17m
service-ca                                      True        False         False     30m
----

. Inspect individual cluster Operators by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get clusteroperator <operator> -oyaml <1>
----
<1> Replace `<operator>` with the name of a cluster Operator. This command is useful for identifying why an cluster Operator has not achieved the `Available` state or is in the `Failed` state.
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: ClusterOperator
metadata:
  creationTimestamp: 2019-02-27T22:47:04Z
  generation: 1
  name: monitoring
  resourceVersion: "24677"
  selfLink: /apis/config.openshift.io/v1/clusteroperators/monitoring
  uid: 9a6a5ef9-3ae1-11e9-bad4-0a97b6ba9358
spec: {}
status:
  conditions:
  - lastTransitionTime: 2019-02-27T22:49:10Z
    message: Successfully rolled out the stack.
    status: "True"
    type: Available
  - lastTransitionTime: 2019-02-27T22:49:10Z
    status: "False"
    type: Progressing
  - lastTransitionTime: 2019-02-27T22:49:10Z
    status: "False"
    type: Failing
  extension: null
  relatedObjects: null
  version: ""
----

. To get the cluster Operator's status condition, run the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get clusteroperator <operator> \
     -o=jsonpath='{range .status.conditions[*]}{.type}{" "}{.status}{" "}{.message}{"\n"}{end}'
----
+
Replace `<operator>` with the name of one of the operators above.
+
.Example output
[source,terminal]
----
Available True Successfully rolled out the stack
Progressing False
Failing False
----

. To retrieve the list of objects owned by the cluster Operator, execute the following command:
+
[source,terminal]
----
oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get clusteroperator kube-apiserver \
   -o=jsonpath='{.status.relatedObjects}'
----
+
.Example output
[source,javascript]
----
[map[resource:kubeapiservers group:operator.openshift.io name:cluster] map[group: name:openshift-config resource:namespaces] map[group: name:openshift-config-managed resource:namespaces] map[group: name:openshift-kube-apiserver-operator resource:namespaces] map[group: name:openshift-kube-apiserver resource:namespaces]]
----

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="troubleshooting-failure-to-fetch-the-console-url_{context}"]
= Troubleshooting a failure to fetch the console URL

The installation program retrieves the URL for the OpenShift Container Platform console by using `[route][route-object]` within the `openshift-console` namespace. If the installation program fails the retrieve the URL for the console, use the following procedure.

.Procedure

. Check if the console router is in the `Available` or `Failing` state by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get clusteroperator console -oyaml
----
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: ClusterOperator
metadata:
  creationTimestamp: 2019-02-27T22:46:57Z
  generation: 1
  name: console
  resourceVersion: "19682"
  selfLink: /apis/config.openshift.io/v1/clusteroperators/console
  uid: 960364aa-3ae1-11e9-bad4-0a97b6ba9358
spec: {}
status:
  conditions:
  - lastTransitionTime: 2019-02-27T22:46:58Z
    status: "False"
    type: Failing
  - lastTransitionTime: 2019-02-27T22:50:12Z
    status: "False"
    type: Progressing
  - lastTransitionTime: 2019-02-27T22:50:12Z
    status: "True"
    type: Available
  - lastTransitionTime: 2019-02-27T22:46:57Z
    status: "True"
    type: Upgradeable
  extension: null
  relatedObjects:
  - group: operator.openshift.io
    name: cluster
    resource: consoles
  - group: config.openshift.io
    name: cluster
    resource: consoles
  - group: oauth.openshift.io
    name: console
    resource: oauthclients
  - group: ""
    name: openshift-console-operator
    resource: namespaces
  - group: ""
    name: openshift-console
    resource: namespaces
  versions: null
----

. Manually retrieve the console URL by executing the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get route console -n openshift-console \
     -o=jsonpath='{.spec.host}' console-openshift-console.apps.adahiya-1.devcluster.openshift.com
----

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="troubleshooting-failure-to-add-the-ingress-certificate-to-kubeconfig_{context}"]
= Troubleshooting a failure to add the ingress certificate to kubeconfig

The installation program adds the default ingress certificate to the list of trusted client certificate authorities in `${INSTALL_DIR}/auth/kubeconfig`. If the installation program fails to add the ingress certificate to the `kubeconfig` file, you can retrieve the certificate from the cluster and add it.

.Procedure

. Retrieve the certificate from the cluster using the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig get configmaps default-ingress-cert \
     -n openshift-config-managed -o=jsonpath='{.data.ca-bundle\.crt}'
----
+
[source,terminal]
----
-----BEGIN CERTIFICATE-----
MIIC/TCCAeWgAwIBAgIBATANBgkqhkiG9w0BAQsFADAuMSwwKgYDVQQDDCNjbHVz
dGVyLWluZ3Jlc3Mtb3BlcmF0b3JAMTU1MTMwNzU4OTAeFw0xOTAyMjcyMjQ2Mjha
Fw0yMTAyMjYyMjQ2MjlaMC4xLDAqBgNVBAMMI2NsdXN0ZXItaW5ncmVzcy1vcGVy
YXRvckAxNTUxMzA3NTg5MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA
uCA4fQ+2YXoXSUL4h/mcvJfrgpBfKBW5hfB8NcgXeCYiQPnCKblH1sEQnI3VC5Pk
2OfNCF3PUlfm4i8CHC95a7nCkRjmJNg1gVrWCvS/ohLgnO0BvszSiRLxIpuo3C4S
EVqqvxValHcbdAXWgZLQoYZXV7RMz8yZjl5CfhDaaItyBFj3GtIJkXgUwp/5sUfI
LDXW8MM6AXfuG+kweLdLCMm3g8WLLfLBLvVBKB+4IhIH7ll0buOz04RKhnYN+Ebw
tcvFi55vwuUCWMnGhWHGEQ8sWm/wLnNlOwsUz7S1/sW8nj87GFHzgkaVM9EOnoNI
gKhMBK9ItNzjrP6dgiKBCQIDAQABoyYwJDAOBgNVHQ8BAf8EBAMCAqQwEgYDVR0T
AQH/BAgwBgEB/wIBADANBgkqhkiG9w0BAQsFAAOCAQEAq+vi0sFKudaZ9aUQMMha
CeWx9CZvZBblnAWT/61UdpZKpFi4eJ2d33lGcfKwHOi2NP/iSKQBebfG0iNLVVPz
vwLbSG1i9R9GLdAbnHpPT9UG6fLaDIoKpnKiBfGENfxeiq5vTln2bAgivxrVlyiq
+MdDXFAWb6V4u2xh6RChI7akNsS3oU9PZ9YOs5e8vJp2YAEphht05X0swA+X8V8T
C278FFifpo0h3Q0Dbv8Rfn4UpBEtN4KkLeS+JeT+0o2XOsFZp7Uhr9yFIodRsnNo
H/Uwmab28ocNrGNiEVaVH6eTTQeeZuOdoQzUbClElpVmkrNGY0M42K0PvOQ/e7+y
AQ==
-----END CERTIFICATE-----
----

. Add the certificate to the `client-certificate-authority-data` field in the `${INSTALL_DIR}/auth/kubeconfig` file.

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="troubleshooting-ssh-access-to-cluster-nodes_{context}"]
= Troubleshooting SSH access to cluster nodes

For added security, you cannot SSH into the cluster from outside the cluster by default. However, you can access control plane and worker nodes from the provisioner node. If you cannot SSH into the cluster nodes from the provisioner node, the nodes might be waiting on the bootstrap VM. The control plane nodes retrieve their boot configuration from the bootstrap VM, and they cannot boot successfully if they do not retrieve the boot configuration.

.Procedure

. If you have physical access to the nodes, check their console output to determine if they have successfully booted. If the nodes are still retrieving their boot configuration, there might be problems with the bootstrap VM .

. Ensure you have configured the `sshKey: '<ssh_pub_key>'` setting in the `install-config.yaml` file, where `<ssh_pub_key>` is the public key of the `kni` user on the provisioner node.

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-cluster-nodes-will-not-pxe_{context}"]

= Cluster nodes will not PXE boot

When OpenShift Container Platform cluster nodes will not PXE boot, execute the following checks on the cluster nodes that will not PXE boot. This procedure does not apply when installing an OpenShift Container Platform cluster without the `provisioning` network.

.Procedure

. Check the network connectivity to the `provisioning` network.

. Ensure PXE is enabled on the NIC for the `provisioning` network and PXE is disabled for all other NICs.

. Verify that the `install-config.yaml` configuration file includes the `rootDeviceHints` parameter and boot MAC address for the NIC connected to the `provisioning` network. For example:
+
.control plane node settings
+
----
bootMACAddress: 24:6E:96:1B:96:90 # MAC of bootable provisioning NIC
----
+
.Worker node settings
+
----
bootMACAddress: 24:6E:96:1B:96:90 # MAC of bootable provisioning NIC
----

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="installing-creates-no-worker-nodes_{context}"]
= Installing creates no worker nodes

The installation program does not provision worker nodes directly. Instead, the Machine API Operator scales nodes up and down on supported platforms. If worker nodes are not created after 15 to 20 minutes, depending on the speed of the cluster's internet connection, investigate the Machine API Operator.

.Procedure

. Check the Machine API Operator by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig \
   --namespace=openshift-machine-api get deployments
----
+
If `${INSTALL_DIR}` is not set in your environment, replace the value with the name of the installation directory.
+
.Example output
[source,terminal]
----
NAME                          READY   UP-TO-DATE   AVAILABLE   AGE
cluster-autoscaler-operator   1/1     1            1           86m
cluster-baremetal-operator    1/1     1            1           86m
machine-api-controllers       1/1     1            1           85m
machine-api-operator          1/1     1            1           86m
----

. Check the machine controller logs by running the following command:
+
[source,terminal]
----
$ oc --kubeconfig=${INSTALL_DIR}/auth/kubeconfig \
     --namespace=openshift-machine-api logs deployments/machine-api-controllers \
     --container=machine-controller
----

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="troubleshooting-the-cluster-network-operator_{context}"]
= Troubleshooting the Cluster Network Operator

The Cluster Network Operator is responsible for deploying the networking components. It runs early in the installation process, after the control plane nodes have come up but before the installation program removes the bootstrap control plane. Issues with this Operator might indicate installation program issues.

.Procedure

. Ensure the network configuration exists by running the following command:
+
[source,terminal]
----
$ oc get network -o yaml cluster
----
+
If it does not exist, the installation program did not create it. To find out why, run the following command:
+
[source,terminal]
----
$ openshift-install create manifests
----
+
Review the manifests to determine why the installation program did not create the network configuration.

. Ensure the network is running by entering the following command:
+
[source,terminal]
----
$ oc get po -n openshift-network-operator
----

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="unable-to-discover-new-bare-metal-hosts-using-the-bmc_{context}"]
= Unable to discover new bare metal hosts using the BMC

In some cases, the installation program will not be able to discover the new bare metal hosts and issue an error, because it cannot mount the remote virtual media share.

For example:

[source,terminal]
----
ProvisioningError 51s metal3-baremetal-controller Image provisioning failed: Deploy step deploy.deploy failed with BadRequestError: HTTP POST
https://<bmc_address>/redfish/v1/Managers/iDRAC.Embedded.1/VirtualMedia/CD/Actions/VirtualMedia.InsertMedia
returned code 400.
Base.1.8.GeneralError: A general error has occurred. See ExtendedInfo for more information
Extended information: [
  {
    "Message": "Unable to mount remote share https://<ironic_address>/redfish/boot-<uuid>.iso.",
    "MessageArgs": [
      "https://<ironic_address>/redfish/boot-<uuid>.iso"
    ],
    "MessageArgs@odata.count": 1,
    "MessageId": "IDRAC.2.5.RAC0720",
    "RelatedProperties": [
      "#/Image"
    ],
    "RelatedProperties@odata.count": 1,
    "Resolution": "Retry the operation.",
    "Severity": "Informational"
  }
].
----

In this situation, if you are using virtual media with an unknown certificate authority, you can configure your baseboard management controller (BMC) remote file share settings to trust an unknown certificate authority to avoid this error.

[NOTE]
====
This resolution was tested on OpenShift Container Platform 4.11 with Dell iDRAC 9 and firmware version 5.10.50.
====

// This module is included in the following assemblies:
//
// installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="worker-nodes-cannot-join-the-cluster_{context}"]
= Troubleshooting worker nodes that cannot join the cluster

Installer-provisioned clusters deploy with a DNS server that includes a DNS entry for the `api-int.<cluster_name>.<base_domain>` URL. If the nodes within the cluster use an external or upstream DNS server to resolve the `api-int.<cluster_name>.<base_domain>` URL and there is no such entry, worker nodes might fail to join the cluster. Ensure that all nodes in the cluster can resolve the domain name.

.Procedure

. Add a DNS A/AAAA or CNAME record to internally identify the API load balancer. For example, when using dnsmasq, modify the `dnsmasq.conf` configuration file:
+
[source,terminal,options="nowrap",role="white-space-pre"]
----
$ sudo nano /etc/dnsmasq.conf
----
+
[source,terminal,options="nowrap",role="white-space-pre"]
----
address=/api-int.<cluster_name>.<base_domain>/<IP_address>
address=/api-int.mycluster.example.com/192.168.1.10
address=/api-int.mycluster.example.com/2001:0db8:85a3:0000:0000:8a2e:0370:7334
----

. Add a DNS PTR record to internally identify the API load balancer. For example, when using dnsmasq, modify the `dnsmasq.conf` configuration file:
+
[source,terminal,options="nowrap",role="white-space-pre"]
----
$ sudo nano /etc/dnsmasq.conf
----
+
[source,terminal,options="nowrap",role="white-space-pre"]
----
ptr-record=<IP_address>.in-addr.arpa,api-int.<cluster_name>.<base_domain>
ptr-record=10.1.168.192.in-addr.arpa,api-int.mycluster.example.com
----

. Restart the DNS server. For example, when using dnsmasq, execute the following command:
+
[source,terminal,subs="+quotes",options="nowrap",role="white-space-pre"]
----
$ sudo systemctl restart dnsmasq
----

These records must be resolvable from all the nodes within the cluster.

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-cleaning-up-previous-installations_{context}"]
= Cleaning up previous installations

In case of an earlier failed deployment, remove the artifacts from the failed attempt before trying to deploy OpenShift Container Platform again.

.Procedure

. Power off all bare-metal nodes before installing the OpenShift Container Platform cluster by using the following command:
+
[source,terminal]
----
$ ipmitool -I lanplus -U <user> -P <password> -H <management_server_ip> power off
----

. Remove all old bootstrap resources if any remain from an earlier deployment attempt by using the following script:
+
[source,bash]
----
for i in $(sudo virsh list | tail -n +3 | grep bootstrap | awk {'print $2'});
do
  sudo virsh destroy $i;
  sudo virsh undefine $i;
  sudo virsh vol-delete $i --pool $i;
  sudo virsh vol-delete $i.ign --pool $i;
  sudo virsh pool-destroy $i;
  sudo virsh pool-undefine $i;
done
----

. Delete the artifacts that the earlier installation generated by using the following command:
+
[source,terminal]
----
$ cd ; /bin/rm -rf auth/ bootstrap.ign master.ign worker.ign metadata.json \
.openshift_install.log .openshift_install_state.json
----

. Re-create the OpenShift Container Platform manifests by using the following command:
+
[source,terminal]
----
$ ./openshift-baremetal-install --dir ~/clusterconfigs create manifests
----

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-registry-issues_{context}"]

= Issues with creating the registry

When creating a disconnected registry, you might encounter a "User Not Authorized" error when attempting to mirror the registry. This error might occur if you fail to append the new authentication to the existing `pull-secret.txt` file.

.Procedure

. Check to ensure authentication is successful:
+
[source,terminal]
----
$ /usr/local/bin/oc adm release mirror \
  -a pull-secret-update.json
  --from=$UPSTREAM_REPO \
  --to-release-image=$LOCAL_REG/$LOCAL_REPO:${VERSION} \
  --to=$LOCAL_REG/$LOCAL_REPO
----
+
[NOTE]
====
Example output of the variables used to mirror the install images:

[source,terminal]
----
UPSTREAM_REPO=${RELEASE_IMAGE}
LOCAL_REG=<registry_FQDN>:<registry_port>
LOCAL_REPO='ocp4/openshift4'
----

The values of `RELEASE_IMAGE` and `VERSION` were set during the **Retrieving OpenShift Installer** step of the **Setting up the environment for an OpenShift installation** section.
====

. After mirroring the registry, confirm that you can access it in your
disconnected environment:
+
[source,terminal]
----
$ curl -k -u <user>:<password> https://registry.example.com:<registry_port>/v2/_catalog
{"repositories":["<Repo_Name>"]}
----

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-misc-issues_{context}"]

= Miscellaneous issues

== Addressing the `runtime network not ready` error

After the deployment of a cluster you might receive the following error:

----
`runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: Missing CNI default network`
----

The Cluster Network Operator is responsible for deploying the networking components in response to a special object created by the installation program. It runs very early in the installation process, after the control plane (master) nodes have come up, but before the bootstrap control plane has been torn down. It can be indicative of more subtle installation program issues, such as long delays in bringing up control plane (master) nodes or issues with `apiserver` communication.

.Procedure

. Inspect the pods in the `openshift-network-operator` namespace:
+
[source,terminal]
----
$ oc get all -n openshift-network-operator
----
+
[source,terminal]
----
NAME                                    READY STATUS            RESTARTS   AGE
pod/network-operator-69dfd7b577-bg89v   0/1   ContainerCreating 0          149m
----

. On the `provisioner` node, determine that the network configuration exists:
+
[source,terminal]
----
$ kubectl get network.config.openshift.io cluster -oyaml
----
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  serviceNetwork:
  - 172.30.0.0/16
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
----
+
If it does not exist, the installation program did not create it. To determine why the installation program did not create it, execute the following:
+
[source,terminal]
----
$ openshift-install create manifests
----

. Check that the `network-operator` is running:
+
[source,terminal]
----
$ kubectl -n openshift-network-operator get pods
----

. Retrieve the logs:
+
[source,terminal]
----
$ kubectl -n openshift-network-operator logs -l "name=network-operator"
----
+
On high availability clusters with three or more control plane nodes, the Operator will perform leader election and all other Operators will sleep. For additional details, see https://github.com/openshift/installer/blob/master/docs/user/troubleshooting.md[Troubleshooting].

== Addressing the "No disk found with matching rootDeviceHints" error message

After you deploy a cluster, you might receive the following error message:

[source,text]
----
No disk found with matching rootDeviceHints
----

To address the `No disk found with matching rootDeviceHints` error message, a temporary workaround is to change the `rootDeviceHints` to `minSizeGigabytes: 300`.

After you change the `rootDeviceHints` settings, boot the CoreOS and then verify the disk information by using the following command:

[source,terminal]
----
$ udevadm info /dev/sda
----

If you are using DL360 Gen 10 servers, be aware that they have an SD-card slot that might be assigned the `/dev/sda` device name. If no SD card is present in the server, it can cause conflicts. Ensure that the SD card slot is disabled in the server's BIOS settings.

If the `minSizeGigabytes` workaround is not fulfilling the requirements, you might need to revert `rootDeviceHints` back to `/dev/sda`. This change allows ironic images to boot successfully.

An alternative approach to fixing this problem is by using the serial ID of the disk. However, be aware that finding the serial ID can be challenging and might make the configuration file less readable. If you choose this path, ensure that you gather the serial ID using the previously documented command and incorporate it into your configuration.

== Cluster nodes not getting the correct IPv6 address over DHCP

If the cluster nodes are not getting the correct IPv6 address over DHCP, check the following:

. Ensure the reserved IPv6 addresses reside outside the DHCP range.

. In the IP address reservation on the DHCP server, ensure the reservation specifies the correct DHCP Unique Identifier (DUID). For example:
+
[source,terminal]
----
# This is a dnsmasq dhcp reservation, 'id:00:03:00:01' is the client id and '18:db:f2:8c:d5:9f' is the MAC Address for the NIC
id:00:03:00:01:18:db:f2:8c:d5:9f,openshift-master-1,[2620:52:0:1302::6]
----

. Ensure that route announcements are working.

. Ensure that the DHCP server is listening on the required interfaces serving the IP address ranges.

== Cluster nodes not getting the correct hostname over DHCP

During IPv6 deployment, cluster nodes must get their hostname over DHCP. Sometimes the `NetworkManager` does not assign the hostname immediately. A control plane (master) node might report an error such as:

----
Failed Units: 2
  NetworkManager-wait-online.service
  nodeip-configuration.service
----

This error indicates that the cluster node likely booted without first receiving a hostname from the DHCP server, which causes `kubelet` to boot
with a `localhost.localdomain` hostname. To address the error, force the node to renew the hostname.

.Procedure

. Retrieve the `hostname`:
+
[source,terminal]
----
[core@master-X ~]$ hostname
----
+
If the hostname is `localhost`, proceed with the following steps.
+
[NOTE]
====
Where `X` is the control plane node number.
====

. Force the cluster node to renew the DHCP lease:
+
[source,terminal]
----
[core@master-X ~]$ sudo nmcli con up "<bare_metal_nic>"
----
+
Replace `<bare_metal_nic>` with the wired connection corresponding to the `baremetal` network.

. Check `hostname` again:
+
[source,terminal]
----
[core@master-X ~]$ hostname
----

. If the hostname is still `localhost.localdomain`, restart `NetworkManager`:
+
[source,terminal]
----
[core@master-X ~]$ sudo systemctl restart NetworkManager
----

. If the hostname is still `localhost.localdomain`, wait a few minutes and check again. If the hostname remains  `localhost.localdomain`, repeat the previous steps.

. Restart the `nodeip-configuration` service:
+
[source,terminal]
----
[core@master-X ~]$ sudo systemctl restart nodeip-configuration.service
----
+
This service will reconfigure the `kubelet` service with the correct hostname references.

. Reload the unit files definition since the kubelet changed in the previous step:
+
[source,terminal]
----
[core@master-X ~]$ sudo systemctl daemon-reload
----

. Restart the `kubelet` service:
+
[source,terminal]
----
[core@master-X ~]$ sudo systemctl restart kubelet.service
----

. Ensure `kubelet` booted with the correct hostname:
+
[source,terminal]
----
[core@master-X ~]$ sudo journalctl -fu kubelet.service
----

If the cluster node is not getting the correct hostname over DHCP after the cluster is up and running, such as during a reboot, the cluster will have a pending `csr`. **Do not** approve a `csr`, or other issues might arise.

.Addressing a `csr`

. Get CSRs on the cluster:
+
[source,terminal]
----
$ oc get csr
----

. Verify if a pending `csr` contains `Subject Name: localhost.localdomain`:
+
[source,terminal]
----
$ oc get csr <pending_csr> -o jsonpath='{.spec.request}' | base64 --decode | openssl req -noout -text
----

. Remove any `csr` that contains `Subject Name: localhost.localdomain`:
+
[source,terminal]
----
$ oc delete csr <wrong_csr>
----

== Routes do not reach endpoints

During the installation process, it is possible to encounter a Virtual Router Redundancy Protocol (VRRP) conflict. This conflict might occur if a previously used OpenShift Container Platform node that was once part of a cluster deployment using a specific cluster name is still running but not part of the current OpenShift Container Platform cluster deployment using that same cluster name. For example, a cluster was deployed using the cluster name `openshift`, deploying three control plane (master) nodes and three worker nodes. Later, a separate install uses the same cluster name `openshift`, but this redeployment only installed three control plane (master) nodes, leaving the three worker nodes from a previous deployment in an `ON` state. This might cause a Virtual Router Identifier (VRID) conflict and a VRRP conflict.

. Get the route:
+
[source,terminal]
----
$ oc get route oauth-openshift
----

. Check the service endpoint:
+
[source,terminal]
----
$ oc get svc oauth-openshift
----
+
[source,terminal]
----
NAME              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
oauth-openshift   ClusterIP   172.30.19.162   <none>        443/TCP   59m
----

. Attempt to reach the service from a control plane (master) node:
+
[source,terminal]
----
[core@master0 ~]$ curl -k https://172.30.19.162
----
+
[source,terminal]
----
{
  "kind": "Status",
  "apiVersion": "v1",
  "metadata": {
  },
  "status": "Failure",
  "message": "forbidden: User \"system:anonymous\" cannot get path \"/\"",
  "reason": "Forbidden",
  "details": {
  },
  "code": 403
----

. Identify the `authentication-operator` errors from the `provisioner` node:
+
[source,terminal]
----
$ oc logs deployment/authentication-operator -n openshift-authentication-operator
----
+
[source,terminal]
----
Event(v1.ObjectReference{Kind:"Deployment", Namespace:"openshift-authentication-operator", Name:"authentication-operator", UID:"225c5bd5-b368-439b-9155-5fd3c0459d98", APIVersion:"apps/v1", ResourceVersion:"", FieldPath:""}): type: 'Normal' reason: 'OperatorStatusChanged' Status for clusteroperator/authentication changed: Degraded message changed from "IngressStateEndpointsDegraded: All 2 endpoints for oauth-server are reporting"
----

.Solution

. Ensure that the cluster name for every deployment is unique, ensuring no conflict.

. Turn off all the rogue nodes which are not part of the cluster deployment that are using the same cluster name. Otherwise, the authentication pod of the  OpenShift Container Platform cluster might never start successfully.

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-failed-ignition-during-firstboot_{context}"]

= Failed Ignition during Firstboot

During the Firstboot, the Ignition configuration may fail.

.Procedure

. Connect to the node where the Ignition configuration failed:
+
[source,terminal]
----
Failed Units: 1
  machine-config-daemon-firstboot.service
----

. Restart the `machine-config-daemon-firstboot` service:
+
[source,terminal]
----
[core@worker-X ~]$ sudo systemctl restart machine-config-daemon-firstboot.service
----

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-ntp-out-of-sync_{context}"]

= NTP out of sync

The deployment of OpenShift Container Platform clusters depends on NTP synchronized clocks among the cluster nodes. Without synchronized clocks, the deployment may fail due to clock drift if the time difference is greater than two seconds.

.Procedure

. Check for differences in the `AGE` of the cluster nodes. For example:
+
[source,terminal]
----
$ oc get nodes
----
+
[source,terminal]
----
NAME                         STATUS   ROLES    AGE   VERSION
master-0.cloud.example.com   Ready    master   145m   v1.35.4
master-1.cloud.example.com   Ready    master   135m   v1.35.4
master-2.cloud.example.com   Ready    master   145m   v1.35.4
worker-2.cloud.example.com   Ready    worker   100m   v1.35.4
----

. Check for inconsistent timing delays due to clock drift. For example:
+
[source,terminal]
----
$ oc get bmh -n openshift-machine-api
----
+
[source,terminal]
----
master-1   error registering master-1  ipmi://<out_of_band_ip>
----
+
[source,terminal]
----
$ sudo timedatectl
----
+
[source,terminal]
----
               Local time: Tue 2020-03-10 18:20:02 UTC
           Universal time: Tue 2020-03-10 18:20:02 UTC
                 RTC time: Tue 2020-03-10 18:36:53
                Time zone: UTC (UTC, +0000)
System clock synchronized: no
              NTP service: active
          RTC in local TZ: no
----

.Addressing clock drift in existing clusters

. Create a Butane config file including the contents of the `chrony.conf` file to be delivered to the nodes. In the following example, create `99-master-chrony.bu` to add the file to the control plane nodes. You can modify the file for worker nodes or repeat this procedure for the worker role.
+
[NOTE]
====
See "Creating machine configs with Butane" for information about Butane.
====
+
[source,yaml,subs="attributes+"]
----
variant: openshift
version: .0
metadata:
  name: 99-master-chrony
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  files:
  - path: /etc/chrony.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        server <NTP_server> iburst <1>
        stratumweight 0
        driftfile /var/lib/chrony/drift
        rtcsync
        makestep 10 3
        bindcmdaddress 127.0.0.1
        bindcmdaddress ::1
        keyfile /etc/chrony.keys
        commandkey 1
        generatecommandkey
        noclientlog
        logchange 0.5
        logdir /var/log/chrony
----
<1> Replace `<NTP_server>` with the IP address of the NTP server.

. Use Butane to generate a `MachineConfig` object file, `99-master-chrony.yaml`, containing the configuration to be delivered to the nodes:
+
[source,terminal]
----
$ butane 99-master-chrony.bu -o 99-master-chrony.yaml
----
. Apply the `MachineConfig` object file:
+
[source,terminal]
----
$ oc apply -f 99-master-chrony.yaml
----

. Ensure the `System clock synchronized` value is **yes**:
+
[source,terminal]
----
$ sudo timedatectl
----
+
[source,terminal]
----
               Local time: Tue 2020-03-10 19:10:02 UTC
           Universal time: Tue 2020-03-10 19:10:02 UTC
                 RTC time: Tue 2020-03-10 19:36:53
                Time zone: UTC (UTC, +0000)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
----
+
To setup clock synchronization prior to deployment, generate the manifest files and add this file to the `openshift` directory. For example:
+
[source,terminal]
----
$ cp chrony-masters.yaml ~/clusterconfigs/openshift/99_masters-chrony-configuration.yaml
----
+
Then, continue to create the cluster.

// Module included in the following assemblies:
//
//installing/installing_bare_metal/ipi/ipi-install-troubleshooting.adoc

[id="ipi-install-troubleshooting-reviewing-the-installation_{context}"]

= Reviewing the installation

After installation, ensure the installation program deployed the nodes and pods successfully.

.Procedure

. When the OpenShift Container Platform cluster nodes are installed appropriately, the following `Ready` state is seen within the `STATUS` column:
+
[source,terminal]
----
$ oc get nodes
----
+
[source,terminal]
----
NAME                   STATUS   ROLES           AGE  VERSION
master-0.example.com   Ready    master,worker   4h   v1.35.4
master-1.example.com   Ready    master,worker   4h   v1.35.4
master-2.example.com   Ready    master,worker   4h   v1.35.4
----

. Confirm the installation program deployed all pods successfully. The following command
removes any pods that are still running or have completed as part of the output.
+
[source,terminal]
----
$ oc get pods --all-namespaces | grep -iv running | grep -iv complete
----
