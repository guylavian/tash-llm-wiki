---
title: "Driver Toolkit"
type: reference
domain: openshift
slug: hardware-enablement-4-22-psap-driver-toolkit
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hardware_enablement/psap-driver-toolkit
version: 4.22
family: hardware_enablement
documentKind: "Documentation"
---

# Driver Toolkit

[id="driver-toolkit"]
= Driver Toolkit

Learn about the Driver Toolkit and how you can use it as a base image for driver containers for enabling special software and hardware devices on OpenShift Container Platform deployments.

// Module included in the following assemblies:
//
// * hardware_enablement/psap-driver-toolkit.adoc

[id="about-driver-toolkit_{context}"]
= About the Driver Toolkit

== Background
The Driver Toolkit is a container image in the OpenShift Container Platform payload used as a base image on which you can build driver containers. The Driver Toolkit image includes the kernel packages commonly required as dependencies to build or install kernel modules, as well as a few tools needed in driver containers. The version of these packages will match the kernel version running on the {op-system-first} nodes in the corresponding OpenShift Container Platform release.

Driver containers are container images used for building and deploying out-of-tree kernel modules and drivers on container operating systems like {op-system}. Kernel modules and drivers are software libraries running with a high level of privilege in the operating system kernel. They extend the kernel functionalities or provide the hardware-specific code required to control new devices. Examples include hardware devices like Field Programmable Gate Arrays (FPGA) or GPUs, and software-defined storage (SDS) solutions, such as Lustre parallel file systems, which require kernel modules on client machines. Driver containers are the first layer of the software stack used to enable these technologies on Kubernetes.

The list of kernel packages in the Driver Toolkit includes the following and their dependencies:

* `kernel-core`
* `kernel-devel`
* `kernel-headers`
* `kernel-modules`
* `kernel-modules-extra`

In addition, the Driver Toolkit also includes the corresponding real-time kernel packages:

* `kernel-rt-core`
* `kernel-rt-devel`
* `kernel-rt-modules`
* `kernel-rt-modules-extra`

The Driver Toolkit also has several tools that are commonly needed to build and install kernel modules, including:

* `elfutils-libelf-devel`
* `kmod`
* `binutilskabi-dw`
* `kernel-abi-whitelists`
* dependencies for the above

== Purpose
Prior to the Driver Toolkit's existence, users would install kernel packages in a pod or build config on OpenShift Container Platform using entitled builds or by installing from the kernel RPMs in the hosts `machine-os-content`. The Driver Toolkit simplifies the process by removing the entitlement step, and avoids the privileged operation of accessing the machine-os-content in a pod. The Driver Toolkit can also be used by partners who have access to pre-released OpenShift Container Platform versions to prebuild driver-containers for their hardware devices for future OpenShift Container Platform releases.

The Driver Toolkit is also used by the Kernel Module Management (KMM), which is currently available as a community Operator in the software catalog. KMM supports out-of-tree and third-party kernel drivers and the support software for the underlying operating system. Users can create modules for KMM to build and deploy a driver container, as well as support software like a device plugin, or metrics. Modules can include a build config to build a driver container-based on the Driver Toolkit, or KMM can deploy a prebuilt driver container.

// Module included in the following assemblies:
//
// * hardware_enablement/psap-driver-toolkit.adoc

[id="pulling-the-driver-toolkit_{context}"]
= Pulling the Driver Toolkit container image

The `driver-toolkit` image is available from the Container images section of the Red Hat Ecosystem Catalog and in the OpenShift Container Platform release payload. The image corresponding to the most recent minor release of OpenShift Container Platform will be tagged with the version number in the catalog. The image URL for a specific release can be found using the `oc adm` CLI command.

[id="pulling-the-driver-toolkit-from-registry"]
== Pulling the Driver Toolkit container image from registry.redhat.io

Instructions for pulling the `driver-toolkit` image from `registry.redhat.io` with `podman` or in OpenShift Container Platform can be found on the Red Hat Ecosystem Catalog.
The driver-toolkit image for the latest minor release are tagged with the minor release version on `registry.redhat.io`, for example: `registry.redhat.io/openshift4/driver-toolkit-rhel8:v`.

[id="pulling-the-driver-toolkit-from-payload"]
== Finding the Driver Toolkit image URL in the payload

.Prerequisites

* You obtained the image {cluster-manager-url-pull}.
* You installed the OpenShift CLI (`oc`).

.Procedure

. Use the `oc adm` command to extract the image URL of the `driver-toolkit` corresponding to a certain release:
+
--
* For an x86 image, the command is as follows:
+
[source,terminal,subs="attributes+"]
----
$ oc adm release info quay.io/openshift-release-dev/ocp-release:.z-x86_64 --image-for=driver-toolkit
----

* For an ARM image, the command is as follows:
+
[source,terminal,subs="attributes+"]
----
$ oc adm release info quay.io/openshift-release-dev/ocp-release:.z-aarch64 --image-for=driver-toolkit
----
--
+
.Example output
[source,terminal]
----
quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:b53883ca2bac5925857148c4a1abc300ced96c222498e3bc134fe7ce3a1dd404
----

. Obtain this image using a valid pull secret, such as the pull secret required to install OpenShift Container Platform:
+
[source,terminal]
----
$ podman pull --authfile=path/to/pullsecret.json quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:<SHA>
----

// Module included in the following assemblies:
//
// * hardware_enablement/psap-driver-toolkit.adoc

[id="using-the-driver-toolkit_{context}"]
= Using the Driver Toolkit

As an example, the Driver Toolkit can be used as the base image for building a very simple kernel module called `simple-kmod`.

[NOTE]
====
The Driver Toolkit includes the necessary dependencies, `openssl`, `mokutil`, and `keyutils`, needed to sign a kernel module. However, in this example, the `simple-kmod` kernel module is not signed and therefore cannot be loaded on systems with `Secure Boot` enabled.
====

[id="create-simple-kmod-image_{context}"]
== Build and run the simple-kmod driver container on a cluster

.Prerequisites

* You have a running OpenShift Container Platform cluster.
* You set the Image Registry Operator state to `Managed` for your cluster.
* You installed the OpenShift CLI (`oc`).
* You are logged into the OpenShift CLI as a user with `cluster-admin` privileges.

.Procedure

Create a namespace. For example:
[source,terminal]
-----
$ oc new-project simple-kmod-demo
-----

. The YAML defines an `ImageStream` for storing the `simple-kmod` driver container image, and a `BuildConfig` for building the container. Save this YAML as `0000-buildconfig.yaml.template`.
+
[source,yaml]
----
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  labels:
    app: simple-kmod-driver-container
  name: simple-kmod-driver-container
  namespace: simple-kmod-demo
spec: {}
---
apiVersion: build.openshift.io/v1
kind: BuildConfig
metadata:
  labels:
    app: simple-kmod-driver-build
  name: simple-kmod-driver-build
  namespace: simple-kmod-demo
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  runPolicy: "Serial"
  triggers:
    - type: "ConfigChange"
    - type: "ImageChange"
  source:
    dockerfile: |
      ARG DTK
      FROM ${DTK} as builder

      ARG KVER

      WORKDIR /build/

      RUN git clone https://github.com/openshift-psap/simple-kmod.git

      WORKDIR /build/simple-kmod

      RUN make all install KVER=${KVER}

      FROM registry.redhat.io/ubi8/ubi-minimal

      ARG KVER

      # Required for installing `modprobe`
      RUN microdnf install kmod

      COPY --from=builder /lib/modules/${KVER}/simple-kmod.ko /lib/modules/${KVER}/
      COPY --from=builder /lib/modules/${KVER}/simple-procfs-kmod.ko /lib/modules/${KVER}/
      RUN depmod ${KVER}
  strategy:
    dockerStrategy:
      buildArgs:
        - name: KMODVER
          value: DEMO
          # $ oc adm release info quay.io/openshift-release-dev/ocp-release:<cluster version>-x86_64 --image-for=driver-toolkit
        - name: DTK
          value: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:34864ccd2f4b6e385705a730864c04a40908e57acede44457a783d739e377cae
        - name: KVER
          value: 4.18.0-372.26.1.el8_6.x86_64
  output:
    to:
      kind: ImageStreamTag
      name: simple-kmod-driver-container:demo
----

. Substitute the correct driver toolkit image for the OpenShift Container Platform version you are running in place of “DRIVER_TOOLKIT_IMAGE” with the following commands.
+
[source,terminal]
----
$ OCP_VERSION=$(oc get clusterversion/version -ojsonpath={.status.desired.version})
----
+
[source,terminal]
----
$ DRIVER_TOOLKIT_IMAGE=$(oc adm release info $OCP_VERSION --image-for=driver-toolkit)
----
+
[source,terminal]
----
$ sed "s#DRIVER_TOOLKIT_IMAGE#${DRIVER_TOOLKIT_IMAGE}#" 0000-buildconfig.yaml.template > 0000-buildconfig.yaml
----

. Create the image stream and build config with
+
[source,terminal]
----
$ oc create -f 0000-buildconfig.yaml
----

. After the builder pod completes successfully, deploy the driver container image as a `DaemonSet`.

.. The driver container must run with the privileged security context in order to load the kernel modules on the host. The following YAML file contains the RBAC rules and the `DaemonSet` for running the driver container. Save this YAML as `1000-drivercontainer.yaml`.
+
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: simple-kmod-driver-container
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: simple-kmod-driver-container
rules:
- apiGroups:
  - security.openshift.io
  resources:
  - securitycontextconstraints
  verbs:
  - use
  resourceNames:
  - privileged
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: simple-kmod-driver-container
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: simple-kmod-driver-container
subjects:
- kind: ServiceAccount
  name: simple-kmod-driver-container
userNames:
- system:serviceaccount:simple-kmod-demo:simple-kmod-driver-container
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: simple-kmod-driver-container
spec:
  selector:
    matchLabels:
      app: simple-kmod-driver-container
  template:
    metadata:
      labels:
        app: simple-kmod-driver-container
    spec:
      serviceAccount: simple-kmod-driver-container
      serviceAccountName: simple-kmod-driver-container
      containers:
      - image: image-registry.openshift-image-registry.svc:5000/simple-kmod-demo/simple-kmod-driver-container:demo
        name: simple-kmod-driver-container
        imagePullPolicy: Always
        command: [sleep, infinity]
        lifecycle:
          postStart:
            exec:
              command: ["modprobe", "-v", "-a" , "simple-kmod", "simple-procfs-kmod"]
          preStop:
            exec:
              command: ["modprobe", "-r", "-a" , "simple-kmod", "simple-procfs-kmod"]
        securityContext:
          privileged: true
      nodeSelector:
        node-role.kubernetes.io/worker: ""
----

.. Create the RBAC rules and daemon set:
+
[source,terminal]
----
$ oc create -f 1000-drivercontainer.yaml
----

. After the pods are running on the worker nodes, verify that the `simple_kmod` kernel module is loaded successfully on the host machines with `lsmod`.

.. Verify that the pods are running:
+
[source,terminal]
----
$ oc get pod -n simple-kmod-demo
----
+
.Example output
[source,terminal]
----
NAME                                 READY   STATUS      RESTARTS   AGE
simple-kmod-driver-build-1-build     0/1     Completed   0          6m
simple-kmod-driver-container-b22fd   1/1     Running     0          40s
simple-kmod-driver-container-jz9vn   1/1     Running     0          40s
simple-kmod-driver-container-p45cc   1/1     Running     0          40s
----

.. Execute the `lsmod` command in the driver container pod:
+
[source,terminal]
----
$ oc exec -it pod/simple-kmod-driver-container-p45cc -- lsmod | grep simple
----
+
.Example output
[source,terminal]
----
simple_procfs_kmod     16384  0
simple_kmod            16384  0
----

[role="_additional-resources"]
[id="additional-resources_driver-toolkkit-id"]
== Additional resources

* For more information about configuring registry storage for your cluster, see Image Registry Operator in OpenShift Container Platform.
