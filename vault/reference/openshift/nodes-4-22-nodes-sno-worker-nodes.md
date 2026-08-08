---
title: "Adding worker nodes to {sno} clusters"
type: reference
domain: openshift
slug: nodes-4-22-nodes-sno-worker-nodes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/nodes-sno-worker-nodes
version: 4.22
family: nodes
documentKind: "Documentation"
---

# Adding worker nodes to {sno} clusters

[id="nodes-sno-worker-nodes"]
= Adding worker nodes to {sno} clusters

[role="_abstract"]
You can add worker nodes to {sno} clusters in case you need additional capacity in your cluster.

Single-node clusters reduce the host prerequisites for deployment to a single host. This is useful for deployments in constrained environments or at the network edge. However, sometimes you need to add additional capacity to your cluster, for example, in telecommunications and network edge scenarios. In these scenarios, you can add worker nodes to the single-node cluster.

[NOTE]
====
Unlike multi-node clusters, by default all ingress traffic is routed to the single control-plane node, even after adding additional worker nodes.
====

There are several ways that you can add worker nodes to a single-node cluster. You can add worker nodes to a cluster manually, using {cluster-manager-first}, or by using the Assisted Installer REST API directly.

[IMPORTANT]
====
Adding worker nodes does not expand the cluster control plane, and it does not provide high availability to your cluster. For {sno} clusters, high availability is handled by failing over to another site. When adding worker nodes to {sno} clusters, a tested maximum of two worker nodes is recommended. Exceeding the recommended number of worker nodes might result in lower overall performance, including cluster failure.
====

[NOTE]
====
To add worker nodes, you must have access to the {cluster-manager}. This method is not supported when using the Agent-based installer to install a cluster in a disconnected environment.
====

// This is included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

[id="ai-sno-requirements-for-installing-worker-nodes_{context}"]
= Requirements for installing {sno} worker nodes

[role="_abstract"]
You can review the following information to understand the requirements that you must meet before you install a {sno} worker node.

To install a {sno} worker node, you must address the following requirements:

* *Administration host:* You must have a computer to prepare the ISO and to monitor the installation.

* *Production-grade server:* Installing {sno} worker nodes requires a server with sufficient resources to run OpenShift Container Platform services and a production workload.
+
.Minimum resource requirements
[options="header"]
|====

|Profile|vCPU|Memory|Storage

|Minimum|2 vCPU cores|8GB of RAM| 100GB

|====
+
[NOTE]
====
One vCPU is equivalent to one physical core when simultaneous multithreading (SMT), or hyperthreading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio:

(threads per core × cores) × sockets = vCPUs
====
+
The server must have a Baseboard Management Controller (BMC) when booting with virtual media.

* *Networking:* The worker node server must have access to the internet or access to a local registry if it is not connected to a routable network. The worker node server must have a DHCP reservation or a static IP address and be able to access the {sno} cluster Kubernetes API, ingress route, and cluster node domain names. You must configure the DNS to resolve the IP address to each of the following fully qualified domain names (FQDN) for the {sno} cluster:
+
.Required DNS records
[options="header"]
|====

|Usage|FQDN|Description

|Kubernetes API|`api.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record. This record must be resolvable by clients external to the cluster.

|Internal API|`api-int.<cluster_name>.<base_domain>`| Add a DNS A/AAAA or CNAME record when creating the ISO manually. This record must be resolvable by nodes within the cluster.

|Ingress route|`*.apps.<cluster_name>.<base_domain>`| Add a wildcard DNS A/AAAA or CNAME record that targets the node. This record must be resolvable by clients external to the cluster.

|====
+
Without persistent IP addresses, communications between the `apiserver` and `etcd` might fail.

// Module included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

[id="sno-adding-worker-nodes-to-sno-clusters_{context}"]
= Adding worker nodes using the Assisted Installer and {cluster-manager}

[role="_abstract"]
You can add worker nodes to {sno} clusters that were created on the {cluster-manager-url} by using the Assisted Installer. This method provides and alternative to using command-line commands.

[IMPORTANT]
====
Adding worker nodes to {sno} clusters is only supported for clusters running OpenShift Container Platform version 4.11 and up.
====

.Prerequisites

* Have access to a {sno} cluster installed using Assisted Installer.
* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.
* Ensure that all the required DNS records exist for the cluster that you are adding the worker node to.

.Procedure

. Log in to the {cluster-manager-url} and click the single-node cluster that you want to add a worker node to.

. Click *Add hosts*, and download the discovery ISO for the new worker node, adding SSH public key and configuring cluster-wide proxy settings as required.

. Boot the target host using the discovery ISO, and wait for the host to be discovered in the console. After the host is discovered, start the installation.

. As the installation proceeds, the installation generates pending certificate signing requests (CSRs) for the worker node. When prompted, approve the pending CSRs to complete the installation.
+
When the worker node is sucessfully installed, it is listed as a worker node in the cluster web console.
+
[IMPORTANT]
====
New worker nodes are encrypted using the same method as the original cluster.
====

// Module included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

[id="ai-adding-worker-nodes-using-the-assisted-installer-api_{context}"]
= Adding worker nodes using the Assisted Installer API

[role="_abstract"]
You can add worker nodes to clusters by writing command-line commands against the Assisted Installer REST API. This method provides an alternative to using the web console.

Before you add worker nodes, you must log in to {cluster-manager} and authenticate against the API. After you authenticate, you can use the Assisted Installer REST API to add the nodes.

// Module included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

[id="ai-authenticating-against-ai-rest-api_{context}"]
= Authenticating against the Assisted Installer REST API

[role="_abstract"]
Before you can use the Assisted Installer REST API, you must authenticate against the API using a JSON web token (JWT) that you generate.

.Prerequisites

* Log in to {cluster-manager} as a user with cluster creation privileges.

* Install `jq`.

.Procedure

. Log in to {cluster-manager} and copy your API token.

. Set the `$OFFLINE_TOKEN` variable using the copied API token by running the following command:
+
[source,terminal]
----
$ export OFFLINE_TOKEN=<copied_api_token>
----

. Set the `$JWT_TOKEN` variable using the previously set `$OFFLINE_TOKEN` variable:
+
[source,terminal]
----
$ export JWT_TOKEN=$(
  curl \
  --silent \
  --header "Accept: application/json" \
  --header "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=refresh_token" \
  --data-urlencode "client_id=cloud-services" \
  --data-urlencode "refresh_token=${OFFLINE_TOKEN}" \
  "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token" \
  | jq --raw-output ".access_token"
)
----
+
[NOTE]
====
The JWT token is valid for 15 minutes only.
====

.Verification

* Optional: Check that you can access the API by running the following command:
+
[source,terminal]
----
$ curl -s https://api.openshift.com/api/assisted-install/v2/component-versions -H "Authorization: Bearer ${JWT_TOKEN}" | jq
----
+
.Example output
[source,yaml]
----
{
    "release_tag": "v2.5.1",
    "versions":
    {
        "assisted-installer": "registry.redhat.io/rhai-tech-preview/assisted-installer-rhel8:v1.0.0-175",
        "assisted-installer-controller": "registry.redhat.io/rhai-tech-preview/assisted-installer-reporter-rhel8:v1.0.0-223",
        "assisted-installer-service": "quay.io/app-sre/assisted-service:ac87f93",
        "discovery-agent": "registry.redhat.io/rhai-tech-preview/assisted-installer-agent-rhel8:v1.0.0-156"
    }
}
----

// Module included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

[id="ai-adding-worker-nodes-to-cluster_{context}"]
= Adding worker nodes using the Assisted Installer REST API

[role="_abstract"]
You can add worker nodes to clusters by writing command-line commands against the Assisted Installer REST API. This method provides an alternative to using the web console.

.Prerequisites

* Install the OpenShift Cluster Manager CLI (`ocm`).

* Log in to {cluster-manager-url} as a user with cluster creation privileges.

* Install `jq`.

* Ensure that all the required DNS records exist for the cluster that you are adding the worker node to.

.Procedure

. Authenticate against the Assisted Installer REST API and generate a JSON web token (JWT) for your session. The generated JWT token is valid for 15 minutes only.

. Set the `$API_URL` variable by running the following command:
+
[source,terminal]
----
$ export API_URL=<api_url>
----
+
Replace `<api_url>` with the Assisted Installer API URL, for example, `https://api.openshift.com`

. Import the {sno} cluster by running the following commands:
+
.. Set the `$OPENSHIFT_CLUSTER_ID` variable. Log in to the cluster and run the following command:
+
[source,terminal]
----
$ export OPENSHIFT_CLUSTER_ID=$(oc get clusterversion -o jsonpath='{.items[].spec.clusterID}')
----
+
.. Set the `$CLUSTER_REQUEST` variable that is used to import the cluster:
+
[source,terminal]
----
$ export CLUSTER_REQUEST=$(jq --null-input --arg openshift_cluster_id "$OPENSHIFT_CLUSTER_ID" '{
  "api_vip_dnsname": "<api_vip>",
  "openshift_cluster_id": $openshift_cluster_id,
  "name": "<openshift_cluster_name>"
}')
----
where:

`<api_vip>`:: Specifies the hostname for the cluster's API server. This can be the DNS domain for the API server or the IP address of the single node which the worker node can reach. For example, `api.compute-1.example.com`.
`<openshift_cluster_name>`:: Specifies the plain text name for the cluster. The cluster name should match the cluster name that was set during the Day 1 cluster installation.

.. Import the cluster and set the `$CLUSTER_ID` variable. Run the following command:
+
[source,terminal]
----
$ CLUSTER_ID=$(curl "$API_URL/api/assisted-install/v2/clusters/import" -H "Authorization: Bearer ${JWT_TOKEN}" -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d "$CLUSTER_REQUEST" | tee /dev/stderr | jq -r '.id')
----

. Generate the `InfraEnv` resource for the cluster and set the `$INFRA_ENV_ID` variable by running the following commands:
+
.. Download the {cluster-manager-url-pull}.
+
.. Set the `$INFRA_ENV_REQUEST` variable:
+
[source,terminal]
----
export INFRA_ENV_REQUEST=$(jq --null-input \
    --slurpfile pull_secret <path_to_pull_secret_file> \//
    --arg ssh_pub_key "$(cat <path_to_ssh_pub_key>)" \//
    --arg cluster_id "$CLUSTER_ID" '{
  "name": "<infraenv_name>",
  "pull_secret": $pull_secret[0] | tojson,
  "cluster_id": $cluster_id,
  "ssh_authorized_key": $ssh_pub_key,
  "image_type": "<iso_image_type>"
}')
----
where:

`<path_to_pull_secret_file>`:: Specifies the path to the local file containing the downloaded {cluster-manager-url-pull}.
`<path_to_ssh_pub_key>`:: Specifies the path to the public SSH key required to access the host. If you do not set this value, you cannot access the host while in discovery mode.
`<infraenv_name>`:: Specifies the plain text name for the `InfraEnv` resource.
`<iso_image_type>`:: Specifies the ISO image type, either `full-iso` or `minimal-iso`.

.. Post the `$INFRA_ENV_REQUEST` to the /v2/infra-envs API and set the `$INFRA_ENV_ID` variable:
+
[source,terminal]
----
$ INFRA_ENV_ID=$(curl "$API_URL/api/assisted-install/v2/infra-envs" -H "Authorization: Bearer ${JWT_TOKEN}" -H 'accept: application/json' -H 'Content-Type: application/json' -d "$INFRA_ENV_REQUEST" | tee /dev/stderr | jq -r '.id')
----

. Get the URL of the discovery ISO for the cluster worker node by running the following command:
+
[source,terminal]
----
$ curl -s "$API_URL/api/assisted-install/v2/infra-envs/$INFRA_ENV_ID" -H "Authorization: Bearer ${JWT_TOKEN}" | jq -r '.download_url'
----
+
.Example output
[source,terminal]
----
https://api.openshift.com/api/assisted-images/images/41b91e72-c33e-42ee-b80f-b5c5bbf6431a?arch=x86_64&image_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTYwMjYzNzEsInN1YiI6IjQxYjkxZTcyLWMzM2UtNDJlZS1iODBmLWI1YzViYmY2NDMxYSJ9.1EX_VGaMNejMhrAvVRBS7PDPIQtbOOc8LtG8OukE1a4&type=minimal-iso&version=$VERSION
----

. Download the ISO:
+
[source,terminal]
----
$ curl -L -s '<iso_url>' --output rhcos-live-minimal.iso
----
+
Replace `<iso_url>` with the URL for the ISO from the previous step.

. Boot the new worker host from the downloaded `rhcos-live-minimal.iso`.

. Get the list of hosts in the cluster that are _not_ installed. Keep running the following command until the new host shows up:
+
[source,terminal]
----
$ curl -s "$API_URL/api/assisted-install/v2/clusters/$CLUSTER_ID" -H "Authorization: Bearer ${JWT_TOKEN}" | jq -r '.hosts[] | select(.status != "installed").id'
----
+
.Example output
[source,terminal]
----
2294ba03-c264-4f11-ac08-2f1bb2f8c296
----

. Set the `$HOST_ID` variable for the new worker node, for example:
+
[source,terminal]
----
$ HOST_ID=<host_id>
----
+
Replace `<host_id>` with the host ID from the previous step.

. Check that the host is ready to install by running the following command:
+
[NOTE]
====
Ensure that you copy the entire command including the complete `jq` expression.
====
+
[source,terminal]
----
$ curl -s $API_URL/api/assisted-install/v2/clusters/$CLUSTER_ID -H "Authorization: Bearer ${JWT_TOKEN}" | jq '
def host_name($host):
    if (.suggested_hostname // "") == "" then
        if (.inventory // "") == "" then
            "Unknown hostname, please wait"
        else
            .inventory | fromjson | .hostname
        end
    else
        .suggested_hostname
    end;

def is_notable($validation):
    ["failure", "pending", "error"] | any(. == $validation.status);

def notable_validations($validations_info):
    [
        $validations_info // "{}"
        | fromjson
        | to_entries[].value[]
        | select(is_notable(.))
    ];

{
    "Hosts validations": {
        "Hosts": [
            .hosts[]
            | select(.status != "installed")
            | {
                "id": .id,
                "name": host_name(.),
                "status": .status,
                "notable_validations": notable_validations(.validations_info)
            }
        ]
    },
    "Cluster validations info": {
        "notable_validations": notable_validations(.validations_info)
    }
}
' -r
----
+
.Example output
[source,terminal]
----
{
  "Hosts validations": {
    "Hosts": [
      {
        "id": "97ec378c-3568-460c-bc22-df54534ff08f",
        "name": "localhost.localdomain",
        "status": "insufficient",
        "notable_validations": [
          {
            "id": "ntp-synced",
            "status": "failure",
            "message": "Host couldn't synchronize with any NTP server"
          },
          {
            "id": "api-domain-name-resolved-correctly",
            "status": "error",
            "message": "Parse error for domain name resolutions result"
          },
          {
            "id": "api-int-domain-name-resolved-correctly",
            "status": "error",
            "message": "Parse error for domain name resolutions result"
          },
          {
            "id": "apps-domain-name-resolved-correctly",
            "status": "error",
            "message": "Parse error for domain name resolutions result"
          }
        ]
      }
    ]
  },
  "Cluster validations info": {
    "notable_validations": []
  }
}
----

. When the previous command shows that the host is ready, start the installation using the /v2/infra-envs/{infra_env_id}/hosts/{host_id}/actions/install API by running the following command:
+
[source,terminal]
----
$ curl -X POST -s "$API_URL/api/assisted-install/v2/infra-envs/$INFRA_ENV_ID/hosts/$HOST_ID/actions/install"  -H "Authorization: Bearer ${JWT_TOKEN}"
----

. As the installation proceeds, the installation generates pending certificate signing requests (CSRs) for the worker node.
+
[IMPORTANT]
====
You must approve the CSRs to complete the installation.
====
+
Keep running the following API call to monitor the cluster installation:
+
[source,terminal]
----
$ curl -s "$API_URL/api/assisted-install/v2/clusters/$CLUSTER_ID" -H "Authorization: Bearer ${JWT_TOKEN}" | jq '{
    "Cluster day-2 hosts":
        [
            .hosts[]
            | select(.status != "installed")
            | {id, requested_hostname, status, status_info, progress, status_updated_at, updated_at, infra_env_id, cluster_id, created_at}
        ]
}'
----
+
.Example output
[source,terminal]
----
{
  "Cluster day-2 hosts": [
    {
      "id": "a1c52dde-3432-4f59-b2ae-0a530c851480",
      "requested_hostname": "control-plane-1",
      "status": "added-to-existing-cluster",
      "status_info": "Host has rebooted and no further updates will be posted. Please check console for progress and to possibly approve pending CSRs",
      "progress": {
        "current_stage": "Done",
        "installation_percentage": 100,
        "stage_started_at": "2022-07-08T10:56:20.476Z",
        "stage_updated_at": "2022-07-08T10:56:20.476Z"
      },
      "status_updated_at": "2022-07-08T10:56:20.476Z",
      "updated_at": "2022-07-08T10:57:15.306369Z",
      "infra_env_id": "b74ec0c3-d5b5-4717-a866-5b6854791bd3",
      "cluster_id": "8f721322-419d-4eed-aa5b-61b50ea586ae",
      "created_at": "2022-07-06T22:54:57.161614Z"
    }
  ]
}
----

. Optional: Run the following command to see all the events for the cluster:
+
[source,terminal]
----
$ curl -s "$API_URL/api/assisted-install/v2/events?cluster_id=$CLUSTER_ID" -H "Authorization: Bearer ${JWT_TOKEN}" | jq -c '.[] | {severity, message, event_time, host_id}'
----
+
.Example output
[source,terminal]
----
{"severity":"info","message":"Host compute-0: updated status from insufficient to known (Host is ready to be installed)","event_time":"2022-07-08T11:21:46.346Z","host_id":"9d7b3b44-1125-4ad0-9b14-76550087b445"}
{"severity":"info","message":"Host compute-0: updated status from known to installing (Installation is in progress)","event_time":"2022-07-08T11:28:28.647Z","host_id":"9d7b3b44-1125-4ad0-9b14-76550087b445"}
{"severity":"info","message":"Host compute-0: updated status from installing to installing-in-progress (Starting installation)","event_time":"2022-07-08T11:28:52.068Z","host_id":"9d7b3b44-1125-4ad0-9b14-76550087b445"}
{"severity":"info","message":"Uploaded logs for host compute-0 cluster 8f721322-419d-4eed-aa5b-61b50ea586ae","event_time":"2022-07-08T11:29:47.802Z","host_id":"9d7b3b44-1125-4ad0-9b14-76550087b445"}
{"severity":"info","message":"Host compute-0: updated status from installing-in-progress to added-to-existing-cluster (Host has rebooted and no further updates will be posted. Please check console for progress and to possibly approve pending CSRs)","event_time":"2022-07-08T11:29:48.259Z","host_id":"9d7b3b44-1125-4ad0-9b14-76550087b445"}
{"severity":"info","message":"Host: compute-0, reached installation stage Rebooting","event_time":"2022-07-08T11:29:48.261Z","host_id":"9d7b3b44-1125-4ad0-9b14-76550087b445"}
----

. Log in to the cluster and approve the pending CSRs to complete the installation.

.Verification

* Check that the new worker node was successfully added to the cluster with a status of `Ready`:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                           STATUS   ROLES           AGE   VERSION
control-plane-1.example.com    Ready    master,worker   56m   v1.35.4
compute-1.example.com          Ready    worker          11m   v1.35.4
----

// Module included in the following assemblies:
//
// * nodes/nodes/nodes-sno-worker-nodes.adoc

[id="sno-adding-worker-nodes-to-single-node-clusters-manually_{context}"]
= Adding worker nodes to {sno} clusters manually

[role="_abstract"]
You can add a worker node to a {sno} cluster manually by booting the worker node from {op-system-first} ISO and by using the cluster `worker.ign` file to join the new worker node to the cluster.

.Prerequisites

* Install a {sno} cluster on bare metal.

* Install the OpenShift CLI (`oc`).

* Log in as a user with `cluster-admin` privileges.

* Ensure that all the required DNS records exist for the cluster that you are adding the worker node to.

.Procedure

. Set the OpenShift Container Platform version:
+
[source,terminal]
----
$ OCP_VERSION=<ocp_version>
----
+
Replace `<ocp_version>` with the current version, for example, `latest-`

. Set the host architecture:
+
[source,terminal]
----
$ ARCH=<architecture>
----
+
Replace `<architecture>` with the target host architecture, for example, `aarch64` or `x86_64`.

. Get the `worker.ign` data from the running single-node cluster by running the following command:
+
[source,terminal]
----
$ oc extract -n openshift-machine-api secret/worker-user-data-managed --keys=userData --to=- > worker.ign
----

. Host the `worker.ign` file on a web server accessible from your network.

. Download the OpenShift Container Platform installer and make it available for use by running the following commands:
+
[source,terminal]
----
$ curl -k https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$OCP_VERSION/openshift-install-linux.tar.gz > openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ tar zxvf openshift-install-linux.tar.gz
----
+
[source,terminal]
----
$ chmod +x openshift-install
----

. Retrieve the {op-system} ISO URL:
+
[source,terminal]
----
$ ISO_URL=$(./openshift-install coreos print-stream-json | grep location | grep $ARCH | grep iso | cut -d\" -f4)
----

. Download the {op-system} ISO:
+
[source,terminal]
----
$ curl -L $ISO_URL -o rhcos-live.iso
----

. Use the {op-system} ISO and the hosted `worker.ign` file to install the worker node:

.. Boot the target host with the {op-system} ISO and your preferred method of installation.

.. When the target host has booted from the {op-system} ISO, open a console on the target host.

.. If your local network does not have DHCP enabled, you need to create an ignition file with the new hostname and configure the worker node static IP address before running the {op-system} installation. Perform the following steps:

... Configure the worker host network connection with a static IP. Run the following command on the target host console:
+
[source,terminal]
----
$ nmcli con mod <network_interface> ipv4.method manual /
ipv4.addresses <static_ip> ipv4.gateway <network_gateway> ipv4.dns <dns_server> /
802-3-ethernet.mtu 9000
----
+
where:
+
--
<static_ip>:: Specifies the host static IP address and CIDR, for example, `10.1.101.50/24`.
<network_gateway>:: Specifies the network gateway, for example, `10.1.101.1`.
--

... Activate the modified network interface:
+
[source,terminal]
----
$ nmcli con up <network_interface>
----

... Create a new ignition file `new-worker.ign` that includes a reference to the original `worker.ign` and an additional instruction that the `coreos-installer` program uses to populate the `/etc/hostname` file on the new worker host. For example:
+
[source,json]
----
{
  "ignition":{
    "version":"3.2.0",
    "config":{
      "merge":[
        {
          "source":"<hosted_worker_ign_file>"
        }
      ]
    }
  },
  "storage":{
    "files":[
      {
        "path":"/etc/hostname",
        "contents":{
          "source":"data:,<new_fqdn>"
        },
        "mode":420,
        "overwrite":true,
        "path":"/etc/hostname"
      }
    ]
  }
}
----
where:
+
`<hosted_worker_ign_file>`:: Specifies the locally accessible URL for the original `worker.ign` file. For example, `http://webserver.example.com/worker.ign`.
`<new_fqdn>`:: Specifies the new FQDN that you set for the worker node. For example, `new-worker.example.com`.

... Host the `new-worker.ign` file on a web server accessible from your network.

... Run the following `coreos-installer` command, passing in the `ignition-url` and hard disk details:
+
[source,terminal]
----
$ sudo coreos-installer install --copy-network /
--ignition-url=<new_worker_ign_file> <hard_disk> --insecure-ignition
----
+
where:
+
--
<new_worker_ign_file>:: Specifies the locally accessible URL for the hosted `new-worker.ign` file, for example, `http://webserver.example.com/new-worker.ign`.
<hard_disk>:: Specifies the hard disk where you install {op-system}, for example, `/dev/sda`.
--

.. For networks that have DHCP enabled, you do not need to set a static IP. Run the following `coreos-installer` command from the target host console to install the system:
+
[source,terminal]
----
$ coreos-installer install --ignition-url=<hosted_worker_ign_file> <hard_disk>
----

.. To manually enable DHCP, apply the following `NMStateConfig` CR to the {sno} cluster:
+
[source,yaml]
----
apiVersion: agent-install.openshift.io/v1
kind: NMStateConfig
metadata:
  name: nmstateconfig-dhcp
  namespace: example-sno
  labels:
    nmstate_config_cluster_name: <nmstate_config_cluster_label>
spec:
  config:
    interfaces:
      - name: eth0
        type: ethernet
        state: up
        ipv4:
          enabled: true
          dhcp: true
        ipv6:
          enabled: false
  interfaces:
    - name: "eth0"
      macAddress: "AA:BB:CC:DD:EE:11"
----
+
[IMPORTANT]
====
The `NMStateConfig` CR is required for successful deployment of worker nodes with static IP addresses and for adding a worker node with a dynamic IP address if the {sno} was deployed with a static IP address. The cluster network DHCP does not automatically set these network settings for the new worker node.
====

. As the installation proceeds, the installation generates pending certificate signing requests (CSRs) for the worker node. When prompted, approve the pending CSRs to complete the installation.

. When the installation is complete, reboot the host. The host joins the cluster as a new worker node.

.Verification

* Check that the new worker node was successfully added to the cluster with a status of `Ready`:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME                           STATUS   ROLES           AGE   VERSION
control-plane-1.example.com    Ready    master,worker   56m   v1.35.4
compute-1.example.com          Ready    worker          11m   v1.35.4
----

// Module included in the following assemblies:
//
// * installing/installing_aws/installing-aws-user-infra.adoc
// * installing/installing_azure/installing-azure-user-infra.adoc
// * installing/installing_azure_stack_hub/installing-azure-stack-hub-user-infra.adoc
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-gcp-restricted-networks.adoc
// * installing/installing_bare_metal/upi/installing-bare-metal.adoc
// * installing/installing_aws/installing-restricted-networks-aws.adoc
// * installing/installing_bare_metal/upi/installing-restricted-networks-bare-metal.adoc
// * installing/installing_vsphere/installing-restricted-networks-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere.adoc
// * installing/installing_vsphere/installing-vsphere-network-customizations.adoc
// * machine_management/adding-rhel-compute.adoc
// * machine_management/more-rhel-compute.adoc
// * machine_management/user_provisioned/adding-aws-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-bare-metal-compute-user-infra.adoc
// * machine_management/user_provisioned/adding-vsphere-compute-user-infra.adoc
// * post_installation_configuration/node-tasks.adoc
// * installing/installing_ibm_z/installing-ibm-z.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z.adoc
// * installing/installing_ibm_z/installing-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-kvm.adoc
// * installing/installing_ibm_z/installing-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-z-lpar.adoc
// * installing/installing_ibm_z/installing-ibm-power.adoc
// * installing/installing_ibm_z/installing-restricted-networks-ibm-power.adoc
// * installing/installing_azure/installing-restricted-networks-azure-user-provisioned.adoc
// * post_installation_configuration/configuring-multi-arch-compute-machines/creating-multi-arch-compute-nodes-ibm-power.adoc

[id="installation-approve-csrs_{context}"]
= Approving the certificate signing requests for your machines

[role="_abstract"]
When you add machines to a cluster, two pending certificate signing requests (CSRs) are generated for each machine that you added. You must confirm that these CSRs are approved or, if necessary, approve them yourself. The client requests must be approved first, followed by the server requests.

.Prerequisites

* You added machines to your cluster.

.Procedure

. Confirm that the cluster recognizes the machines:
+
[source,terminal]
----
$ oc get nodes
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  63m  v1.35.4
master-1  Ready     master  63m  v1.35.4
master-2  Ready     master  64m  v1.35.4
----
+
The output lists all of the machines that you created.
+
[NOTE]
====
The preceding output might not include the compute nodes, also known as worker nodes, until some CSRs are approved.
====

. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
...
----
+
In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
[source,terminal]
----
$ oc get csr
----
+
[source,terminal]
.Example output
----
NAME        AGE   REQUESTOR                                   CONDITION
csr-mddf5   20m   system:node:master-01.example.com   Approved,Issued
csr-z5rln   16m   system:node:worker-21.example.com   Approved,Issued
----

. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:
+
[NOTE]
====
You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates will rotate, and more than two certificates will be present for each node. You must approve all of these certificates. After the client CSR is approved, the Kubelet creates a secondary CSR for the serving certificate, which requires manual approval. Then, subsequent serving certificate renewal requests are automatically approved by the `machine-approver` if the Kubelet requests a new certificate with identical parameters.
====
+
[NOTE]
====
For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If a request is not approved, then the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because a serving certificate is required when the API server connects to the kubelet. Any operation that contacts the Kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the CSR was submitted by the `node-bootstrapper` service account in the `system:node` or `system:admin` groups, and confirm the identity of the node.
====
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
----
+
[NOTE]
====
Some Operators might not become available until some CSRs are approved.
Each node submits two CSRs, so you may need to run the command to approve CSRs multiple times.
====

. Now that your client requests are approved, you must review the server requests for each machine that you added to the cluster:
+
[source,terminal]
----
$ oc get csr
----
+
.Example output
[source,terminal]
----
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
...
----

. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:
+
** To approve them individually, run the following command for each valid CSR:
+
[source,terminal]
----
$ oc adm certificate approve <csr_name>
----
+
where:
+
`<csr_name>`:: Specifies the name of a CSR from the list of current CSRs.
+
** To approve all pending CSRs, run the following command:
+
[source,terminal]
----
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
----

. After all client and server CSRs have been approved, the machines have the `Ready` status. Verify this by running the following command:
+
[source,terminal]
----
$ oc get nodes
----
[source,terminal]
----
$ oc get nodes -o wide
----
+
.Example output
[source,terminal]
----
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  73m  v1.35.4
master-1  Ready     master  73m  v1.35.4
master-2  Ready     master  74m  v1.35.4
worker-0  Ready     worker  11m  v1.35.4
worker-1  Ready     worker  11m  v1.35.4
----
.Example output
[source,terminal]
----
NAME               STATUS   ROLES                  AGE   VERSION   INTERNAL-IP      EXTERNAL-IP   OS-IMAGE                                                       KERNEL-VERSION                  CONTAINER-RUNTIME
worker-0-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.21   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-ppc64le   Ready    worker                 42d   v1.35.4   192.168.200.20   <none>        Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.ppc64le   cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-0-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.38      10.248.0.38   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-1-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.39      10.248.0.39   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
master-2-x86       Ready    control-plane,master   75d   v1.35.4   10.248.0.40      10.248.0.40   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-0-x86       Ready    worker                 75d   v1.35.4   10.248.0.43      10.248.0.43   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
worker-1-x86       Ready    worker                 75d   v1.35.4   10.248.0.44      10.248.0.44   Red Hat Enterprise Linux CoreOS 415.92.202309261919-0 (Plow)   5.14.0-284.34.1.el9_2.x86_64    cri-o://1.35.4-3.rhaos4.15.gitb36169e.el9
----
+
[NOTE]
====
It can take a few minutes after approval of the server CSRs for the machines to transition to the `Ready` status.
====

[role="_additional-resources"]
[id="additional-resources_{context}"]
.Additional resources

* Minimum resource requirements for cluster installation

* Recommended practices for scaling the cluster

* Creating a bootable ISO image on a USB drive

* Booting from an ISO image served over HTTP using the Redfish API

* Deleting nodes from a cluster

* User-provisioned DNS requirements

* Approving the certificate signing requests for your machines
