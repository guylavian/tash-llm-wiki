---
title: "Configuring a private cluster"
type: reference
domain: openshift
slug: post-installation-configuration-4-22-configuring-private-cluster
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/post_installation_configuration/configuring-private-cluster
version: 4.22
family: post_installation_configuration
documentKind: "Documentation"
---

# Configuring a private cluster

[id="configuring-private-cluster"]
= Configuring a private cluster

After you install an OpenShift Container Platform version  cluster, you can set some of its core components to be private.

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

[id="private-clusters-about_{context}"]
= About private clusters

By default, OpenShift Container Platform is provisioned using publicly-accessible DNS and endpoints. You can set the DNS, Ingress Controller, and API server to private after you deploy your private cluster.

[id="private-clusters-about-dns_{context}"]
== DNS

If you install OpenShift Container Platform on installer-provisioned infrastructure, the installation program creates records in a pre-existing public zone and, where possible, creates a private zone for the cluster's own DNS resolution. In both the public zone and the private zone, the installation program or cluster creates DNS entries for `*.apps`, for the `Ingress` object, and `api`, for the API server.

The `*.apps` records in the public and private zone are identical, so when you delete the public zone, the private zone seamlessly provides all DNS resolution for the cluster.

[id="private-clusters-about-ingress-controller_{context}"]
== Ingress Controller
Because the default `Ingress` object is created as public, the load balancer is internet-facing and in the public subnets.

The Ingress Operator generates a default certificate for an Ingress Controller to serve as a placeholder until you configure a custom default certificate. Do not use Operator-generated default certificates in production clusters. The Ingress Operator does not rotate its own signing certificate or the default certificates that it generates. Operator-generated default certificates are intended as placeholders for custom default certificates that you configure.

[id="private-clusters-about-api-server_{context}"]
== API server

By default, the installation program creates appropriate network load balancers for the API server to use for both internal and external traffic.

On Amazon Web Services (AWS), separate public and private load balancers are created. The load balancers are identical except that an additional port is available on the internal one for use within the cluster. Although the installation program automatically creates or destroys the load balancer based on API server requirements, the cluster does not manage or maintain them. As long as you preserve the cluster's access to the API server, you can manually modify or move the load balancers. For the public load balancer, port 6443 is open and the health check is configured for HTTPS against the `/readyz` path.

On {gcp-full}, a single load balancer is created to manage both internal and external API traffic, so you do not need to modify the load balancer.

On Microsoft Azure, both public and private load balancers are created. However, because of limitations in current implementation, you just retain both load balancers in a private cluster.

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

[id="private-clusters-setting-dns-private_{context}"]
= Configuring DNS records to be published in a private zone

For all OpenShift Container Platform clusters, whether public or private, DNS records are published in a public zone by default.

You can remove the public zone from the cluster DNS configuration to avoid exposing DNS records to the public. You might want to avoid exposing sensitive information, such as internal domain names, internal IP addresses, or the number of clusters at an organization, or you might simply have no need to publish records publicly. If all the clients that should be able to connect to services within the cluster use a private DNS service that has the DNS records from the private zone, then there is no need to have a public DNS record for the cluster.

After you deploy a cluster, you can modify its DNS to use only a private zone by modifying the `DNS` custom resource (CR).
Modifying the `DNS` CR in this way means that any DNS records that are subsequently created are not published to public DNS servers, which keeps knowledge of the DNS records isolated to internal users. This can be done when you configure the cluster to be private, or if you never want DNS records to be publicly resolvable.

Alternatively, even in a private cluster, you might keep the public zone for DNS records because it allows clients to resolve DNS names for applications running on that cluster. For example, an organization can have machines that connect to the public internet and then establish VPN connections for certain private IP ranges in order to connect to private IP addresses. The DNS lookups from these machines use the public DNS to determine the private addresses of those services, and then connect to the private addresses over the VPN.

.Procedure

. Review the `DNS` CR for your cluster by running the following command and observing the output:
+
[source,terminal]
----
$ oc get dnses.config.openshift.io/cluster -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: DNS
metadata:
  creationTimestamp: "2019-10-25T18:27:09Z"
  generation: 2
  name: cluster
  resourceVersion: "37966"
  selfLink: /apis/config.openshift.io/v1/dnses/cluster
  uid: 0e714746-f755-11f9-9cb1-02ff55d8f976
spec:
  baseDomain: <base_domain>
  privateZone:
    tags:
      Name: <infrastructure_id>-int
      kubernetes.io/cluster/<infrastructure_id>: owned
  publicZone:
    id: Z2XXXXXXXXXXA4
status: {}
----
+
Note that the `spec` section contains both a private and a public zone.

. Patch the `DNS` CR to remove the public zone by running the following command:
+
[source,terminal]
----
$ oc patch dnses.config.openshift.io/cluster --type=merge --patch='{"spec": {"publicZone": null}}'
----
+
.Example output
[source,yaml]
----
dns.config.openshift.io/cluster patched
----
+
The Ingress Operator consults the `DNS` CR definition when it creates DNS records for `IngressController` objects. If only private zones are specified, only private records are created.
+
[IMPORTANT]
====
Existing DNS records are not modified when you remove the public zone. You must manually delete previously published public DNS records if you no longer want them to be published publicly.
====

.Verification

* Review the `DNS` CR for your cluster and confirm that the public zone was removed, by running the following command and observing the output:
+
[source,terminal]
----
$ oc get dnses.config.openshift.io/cluster -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: DNS
metadata:
  creationTimestamp: "2019-10-25T18:27:09Z"
  generation: 2
  name: cluster
  resourceVersion: "37966"
  selfLink: /apis/config.openshift.io/v1/dnses/cluster
  uid: 0e714746-f755-11f9-9cb1-02ff55d8f976
spec:
  baseDomain: <base_domain>
  privateZone:
    tags:
      Name: <infrastructure_id>-int
      kubernetes.io/cluster/<infrastructure_id>-wfpg4: owned
status: {}
----

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

[id="private-clusters-setting-ingress-private_{context}"]
= Setting the Ingress Controller to private

After you deploy a cluster, you can modify its Ingress Controller to use only a private zone.

.Procedure

. Modify the default Ingress Controller to use only an internal endpoint:
+
[source,terminal]
----
$ oc replace --force --wait --filename - <<EOF
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: default
spec:
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: Internal
EOF
----
+
.Example output
[source,terminal]
----
ingresscontroller.operator.openshift.io "default" deleted
ingresscontroller.operator.openshift.io/default replaced
----
+
The public DNS entry is removed, and the private zone entry is updated.

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-supported-features-aws.adoc

[id="private-clusters-setting-api-private-aws_{context}"]
= Restricting the API server to private for an {aws-full} cluster

[role="_abstract"]
If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers.
To implement this API server restriction, use the {aws-first} console and {oc-first} to delete the external load balancer components.

[IMPORTANT]
====
The {oc-first} steps that remove the external load balancers require the Machine API.
For clusters that cannot use the Machine API, you must manually remove the external load balancers.

Clusters with the infrastructure platform type `none` cannot use the Machine API.
To view the platform type for your cluster, run the following command:

[source,terminal]
----
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
----
====

.Prerequisites

* You have installed an OpenShift Container Platform cluster on {aws-short}.
* You have access to the {aws-short} console as a user with administrator privileges.
* You have access to the {oc-first} as a user with administrator privileges.

.Procedure

. Log in to the {aws-short} console as a user with administrator privileges.

. Delete the external load balancer.
+
[NOTE]
====
The API DNS entry in the private zone already points to the internal load balancer, which uses an identical configuration, so you do not need to modify the internal load balancer.
====

. Delete the `api.<cluster_name>.<domain_name>` DNS entry in the public zone.
+
where `<cluster_name>` is the name of the cluster and `<domain_name>` is the base domain for the cluster.

. To remove the external load balancers, log in to the {oc-first} as a user with administrator privileges.

** If your cluster uses a control plane machine set, remove the external load balancers by editing the `ControlPlaneMachineSet` custom resource (CR).
+
--
. Edit the `ControlPlaneMachineSet` CR by running the following command:
+
[source,terminal]
----
$ oc edit controlplanemachineset.machine.openshift.io cluster \
  -n openshift-machine-api
----

. Remove the external load balancers by deleting the corresponding lines in the control plane machine set custom resource (CR).
+
In the `spec.template.spec.providerSpec.value.loadBalancers` section of the CR, the `name` value for the external load balancer ends in `-ext`.
Delete the line with the external load balancer `name` value and the line with the external load balancer `type` value that accompanies it.
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            loadBalancers:
            - name: <cluster_id>-ext
              type: network
            - name: <cluster_id>-int
              type: network
# ...
----

. Save your changes and exit the object specification.
+
When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.
For more information, see "Updating the control plane configuration".
--

** If your cluster does not use a control plane machine set, you must delete the external load balancers from each control plane machine.

... List the cluster machines by running the following command:
+
[source,terminal]
----
$ oc get machine -n openshift-machine-api
----
+
.Example output
[source,text]
----
NAME                                        STATE     TYPE        REGION      ZONE         AGE
<cluster_id>-master-0                       running   m4.xlarge   us-east-1   us-east-1a   17m
<cluster_id>-master-1                       running   m4.xlarge   us-east-1   us-east-1b   17m
<cluster_id>-master-2                       running   m4.xlarge   us-east-1   us-east-1a   17m
<cluster_id>-worker-us-east-1a-<zone_tag>   running   m4.xlarge   us-east-1   us-east-1a   15m
<cluster_id>-worker-us-east-1a-<zone_tag>   running   m4.xlarge   us-east-1   us-east-1a   15m
<cluster_id>-worker-us-east-1b-<zone_tag>   running   m4.xlarge   us-east-1   us-east-1b   15m
----
+
The control plane machines contain the `master` string in their names.

... Remove the external load balancer from each control plane machine:

.... Edit a control plane machine object to by running the following command:
+
[source,terminal]
----
$ oc edit machines -n openshift-machine-api <control_plane_machine_name>
----
+
where `<control_plane_machine_name>` is the name of the control plane machine object to modify.

.... Remove the lines that describe the external load balancer.
+
In the `spec.providerSpec.value.loadBalancers` section of the CR, the `name` value for the external load balancer ends in `-ext`.
Delete the line with the external load balancer `name` value and the the line with the external load balancer `type` value that accompanies it.
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  name: <control_plane_machine_name>
  namespace: openshift-machine-api
spec:
  providerSpec:
    value:
      loadBalancers:
      - name: <cluster_id>-ext
        type: network
      - name: <cluster_id>-int
        type: network
# ...
----

.... Save your changes and exit the object specification.

.... Repeat this process for each control plane machine.

[role="_additional-resources"]
.Additional resources
* Updating the control plane configuration

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc
// * machine_management/control_plane_machine_management/cpmso_provider_configurations/cpmso-supported-features-azure.adoc

[id="private-clusters-setting-api-private-azure_{context}"]
= Restricting the API server to private for an {azure-full} cluster

[role="_abstract"]
If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers.
To implement this API server restriction, use the {azure-first} console to delete the external load balancer component.

.Prerequisites

* You have installed an OpenShift Container Platform cluster on {azure-short}.
* You have access to the {azure-short} console as a user with administrator privileges.

.Procedure

. Log in to the {azure-short} console as a user with administrator privileges.

. Delete the following resources:

** The `api-v4` rule for the public load balancer.

** The `frontendIPConfiguration` parameter that is associated with the `api-v4` rule for the public load balancer.

** The public IP address that is specified in the `frontendIPConfiguration` parameter.

. Configure the Ingress Controller endpoint publishing scope to `Internal`.
For more information, see "Configuring the Ingress Controller endpoint publishing scope to Internal".

. Delete the `api.<cluster_name>` DNS entry in the public zone.

+
where `<cluster_name>` is the name of the cluster.

[role="_additional-resources"]
.Additional resources
* Configuring the Ingress Controller endpoint publishing scope to Internal

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

[id="registry-configuring-private-storage-endpoint-azure_{context}"]
= Configuring a private storage endpoint on Azure

You can leverage the Image Registry Operator to use private endpoints on Azure, which enables seamless configuration of private storage accounts when OpenShift Container Platform is deployed on private Azure clusters. This allows you to deploy the image registry without exposing public-facing storage endpoints.

[IMPORTANT]
====
Do not configure a private storage endpoint on {azure-first} Red{nbsp}Hat OpenShift (ARO), because the endpoint can put your {azure-first} Red{nbsp}Hat OpenShift cluster in an unrecoverable state.
====

You can configure the Image Registry Operator to use private storage endpoints on Azure in one of two ways:

* By configuring the Image Registry Operator to discover the VNet and subnet names

* With user-provided Azure Virtual Network (VNet) and subnet names

[id="limitations-configuring-private-storage-endpoint-azure"]
== Limitations for configuring a private storage endpoint on Azure

The following limitations apply when configuring a private storage endpoint on Azure:

* When configuring the Image Registry Operator to use a private storage endpoint, public network access to the storage account is disabled. Consequently, pulling images from the registry outside of OpenShift Container Platform only works by setting `disableRedirect: true` in the registry Operator configuration. With redirect enabled, the registry redirects the client to pull images directly from the storage account, which will no longer work due to disabled public network access. For more information, see "Disabling redirect when using a private storage endpoint on Azure".

* This operation cannot be undone by the Image Registry Operator.

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

[id="configuring-private-storage-endpoint-azure-vnet-subnet-iro-discovery_{context}"]
= Configuring a private storage endpoint on Azure by enabling the Image Registry Operator to discover VNet and subnet names

The following procedure shows you how to set up a private storage endpoint on Azure by configuring the Image Registry Operator to discover VNet and subnet names.

.Prerequisites

* You have configured the image registry to run on Azure.
* Your network has been set up using the Installer Provisioned Infrastructure installation method.
+
For users with a custom network setup, see "Configuring a private storage endpoint on Azure with user-provided VNet and subnet names".

.Procedure

. Edit the Image Registry Operator `config` object and set `networkAccess.type` to `Internal`:
+
[source,terminal]
----
$ oc edit configs.imageregistry/cluster
----
+
[source,terminal]
----
# ...
spec:
  # ...
   storage:
      azure:
        # ...
        networkAccess:
          type: Internal
# ...
----

. Optional: Enter the following command to confirm that the Operator has completed provisioning. This might take a few minutes.
+
[source,terminal]
----
$ oc get configs.imageregistry/cluster -o=jsonpath="{.spec.storage.azure.privateEndpointName}" -w
----

. Optional: If the registry is exposed by a route, and you are configuring your storage account to be private, you must disable redirect if you want pulls external to the cluster to continue to work. Enter the following command to disable redirect on the Image Operator configuration:
+
[source,terminal]
----
$ oc patch configs.imageregistry cluster --type=merge -p '{"spec":{"disableRedirect": true}}'
----
+
[NOTE]
====
When redirect is enabled,  pulling images from outside of the cluster will not work.
====

.Verification

. Fetch the registry service name by running the following command:
+
[source,terminal]
----
$ oc get imagestream -n openshift
----
+
.Example output
+
[source,terminal]
----
NAME   IMAGE REPOSITORY                                                 TAGS     UPDATED
cli    image-registry.openshift-image-registry.svc:5000/openshift/cli   latest   8 hours ago
...
----

. Enter debug mode by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Run the suggested `chroot` command. For example:
+
[source,terminal]
----
$ chroot /host
----

. Enter the following command to log in to your container registry:
+
[source,terminal]
----
$ podman login --tls-verify=false -u unused -p $(oc whoami -t) image-registry.openshift-image-registry.svc:5000
----
+
.Example output
+
[source,terminal]
----
Login Succeeded!
----

. Enter the following command to verify that you can pull an image from the registry:
+
[source,terminal]
----
$ podman pull --tls-verify=false image-registry.openshift-image-registry.svc:5000/openshift/tools
----
+
.Example output
+
[source,terminal]
----
Trying to pull image-registry.openshift-image-registry.svc:5000/openshift/tools/openshift/tools...
Getting image source signatures
Copying blob 6b245f040973 done
Copying config 22667f5368 done
Writing manifest to image destination
Storing signatures
22667f53682a2920948d19c7133ab1c9c3f745805c14125859d20cede07f11f9
----

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

[id="configuring-private-storage-endpoint-azure-user-provided-vnet-subnet_{context}"]
= Configuring a private storage endpoint on Azure with user-provided VNet and subnet names

Use the following procedure to configure a storage account that has public network access disabled and is exposed behind a private storage endpoint on Azure.

.Prerequisites

* You have configured the image registry to run on Azure.
* You must know the VNet and subnet names used for your Azure environment.
* If your network was configured in a separate resource group in Azure, you must also know its name.

.Procedure

. Edit the Image Registry Operator `config` object and configure the private endpoint using your VNet and subnet names:
+
[source,terminal]
----
$ oc edit configs.imageregistry/cluster
----
+
[source,terminal]
----
# ...
spec:
  # ...
   storage:
      azure:
        # ...
        networkAccess:
          type: Internal
          internal:
            subnetName: <subnet_name>
            vnetName: <vnet_name>
            networkResourceGroupName: <network_resource_group_name>
# ...
----

. Optional: Enter the following command to confirm that the Operator has completed provisioning. This might take a few minutes.
+
[source,terminal]
----
$ oc get configs.imageregistry/cluster -o=jsonpath="{.spec.storage.azure.privateEndpointName}" -w
----
+
[NOTE]
====
When redirect is enabled, pulling images from outside of the cluster will not work.
====

.Verification

. Fetch the registry service name by running the following command:
+
[source,terminal]
----
$ oc get imagestream -n openshift
----
+
.Example output
+
[source,terminal]
----
NAME   IMAGE REPOSITORY                                                 TAGS     UPDATED
cli    image-registry.openshift-image-registry.svc:5000/openshift/cli   latest   8 hours ago
...
----

. Enter debug mode by running the following command:
+
[source,terminal]
----
$ oc debug node/<node_name>
----

. Run the suggested `chroot` command. For example:
+
[source,terminal]
----
$ chroot /host
----

. Enter the following command to log in to your container registry:
+
[source,terminal]
----
$ podman login --tls-verify=false -u unused -p $(oc whoami -t) image-registry.openshift-image-registry.svc:5000
----
+
.Example output
+
[source,terminal]
----
Login Succeeded!
----

. Enter the following command to verify that you can pull an image from the registry:
+
[source,terminal]
----
$ podman pull --tls-verify=false image-registry.openshift-image-registry.svc:5000/openshift/tools
----
+
.Example output
+
[source,terminal]
----
Trying to pull image-registry.openshift-image-registry.svc:5000/openshift/tools/openshift/tools...
Getting image source signatures
Copying blob 6b245f040973 done
Copying config 22667f5368 done
Writing manifest to image destination
Storing signatures
22667f53682a2920948d19c7133ab1c9c3f745805c14125859d20cede07f11f9
----

// Module included in the following assemblies:
//
// * post_installation_configuration/configuring-private-cluster.adoc

[id="disabling-redirect-private-storage-endpoint-azure_{context}"]
= Optional: Disabling redirect when using a private storage endpoint on Azure

By default, redirect is enabled when using the image registry. Redirect allows off-loading of traffic from the registry pods into the object storage, which makes pull faster. When redirect is enabled and the storage account is private, users from outside of the cluster are unable to pull images from the registry.

In some cases, users might want to disable redirect so that users from outside of the cluster can pull images from the registry.

Use the following procedure to disable redirect.

.Prerequisites

* You have configured the image registry to run on Azure.
* You have configured a route.

.Procedure

* Enter the following command to disable redirect on the image
registry configuration:
+
[source,terminal]
----
$ oc patch configs.imageregistry cluster --type=merge -p '{"spec":{"disableRedirect": true}}'
----

.Verification

. Fetch the registry service name by running the following command:
+
[source,terminal]
----
$ oc get imagestream -n openshift
----
+
.Example output
+
[source,terminal]
----
NAME   IMAGE REPOSITORY                                           TAGS     UPDATED
cli    default-route-openshift-image-registry.<cluster_dns>/cli   latest   8 hours ago
...
----

. Enter the following command to log in to your container registry:
+
[source,terminal]
----
$ podman login --tls-verify=false -u unused -p $(oc whoami -t) default-route-openshift-image-registry.<cluster_dns>
----
+
.Example output
+
[source,terminal]
----
Login Succeeded!
----

. Enter the following command to verify that you can pull an image from the registry:
+
[source,terminal]
----
$ podman pull --tls-verify=false default-route-openshift-image-registry.<cluster_dns>
/openshift/tools
----
+
.Example output
+
[source,terminal]
----
Trying to pull default-route-openshift-image-registry.<cluster_dns>/openshift/tools...
Getting image source signatures
Copying blob 6b245f040973 done
Copying config 22667f5368 done
Writing manifest to image destination
Storing signatures
22667f53682a2920948d19c7133ab1c9c3f745805c14125859d20cede07f11f9
----
