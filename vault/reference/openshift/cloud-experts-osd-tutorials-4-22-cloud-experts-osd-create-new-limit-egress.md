---
title: "Tutorial: Limit egress with Google Cloud Next Generation Firewall"
type: reference
domain: openshift
slug: cloud-experts-osd-tutorials-4-22-cloud-experts-osd-create-new-limit-egress
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_osd_tutorials/cloud-experts-osd-create-new-limit-egress
version: 4.22
family: cloud_experts_osd_tutorials
documentKind: "Documentation"
---

# Tutorial: Limit egress with Google Cloud Next Generation Firewall

[id="cloud-experts-osd-limit-egress-ngfw"]
= Tutorial: Limit egress with Google Cloud Next Generation Firewall

[role="_abstract"]
Implement egress restrictions for OpenShift Container Platform on {GCP} by using Next Generation Firewall (NGFW), which allows fully qualified domain name (FQDN)-based firewall rules required for OpenShift Container Platform external endpoints.

[IMPORTANT]
====
This content is authored by Red{nbsp}Hat experts but has not yet been tested on every supported configuration.
====

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-setup-environ_{context}"]
= Setting up your environment

[role="_abstract"]
Set environment variables so each command in this tutorial uses the same values for OpenShift Container Platform on {GCP} with your firewall rules.

.Prerequisites
* You have the {GCP} command-line interface (CLI) (`gcloud`) installed.
* You are logged into the {GCP} CLI and have selected the {GCP} project where you plan to deploy OpenShift Container Platform.
* You have the minimum necessary permissions in {GCP}, including:
** `Compute Network Admin`
** `Domain Name System (DNS) Administrator`
* You enabled the required {GCP} services:
** `networksecurity.googleapis.com`
** `networkservices.googleapis.com`
** `servicenetworking.googleapis.com`
+
You can enable these services by running the following commands:
+
[source,terminal]
----
$ gcloud services enable networksecurity.googleapis.com
$ gcloud services enable networkservices.googleapis.com
$ gcloud services enable servicenetworking.googleapis.com
----

.Procedure
* Run this command to set the environment variables:
+
[source,terminal]
----
$ export project_id=$(gcloud config list --format="value(core.project)")
$ export region=us-east1
$ export prefix=osd-ngfw
$ export service_cidr="172.30.0.0/16"
$ export machine_cidr="10.0.0.0/22"
$ export pod_cidr="10.128.0.0/14"
----
+
This example sets the region to `us-east1` and the name prefix to `osd-ngfw`. The service and pod networks use the default Classless Inter-Domain Routing (CIDR) ranges in the export list. You add subnet ranges later in this tutorial. The machine CIDR must fit inside those subnet ranges. Change the exports to match your project.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-create-subnets_{context}"]
= Creating the VPC and subnets

[role="_abstract"]
Create the Virtual Private Cloud (VPC) and subnets required for deploying {GCP} Next Generation Firewall (NGFW) with OpenShift Container Platform.

.Procedure
. Create the VPC by running the following command:
+
[source,terminal]
----
$ gcloud compute networks create ${prefix}-vpc --subnet-mode=custom
----
+
. Create the worker subnets by running the following command:
+
[source,terminal]
----
$ gcloud compute networks subnets create ${prefix}-worker \
    --range=10.0.2.0/23 \
    --network=${prefix}-vpc \
    --region=${region} \
    --enable-private-ip-google-access
----
+
. Create the control plane subnets by running the following command:
+
[source,terminal]
----
$ gcloud compute networks subnets create ${prefix}-control-plane \
    --range=10.0.0.0/25 \
    --network=${prefix}-vpc \
    --region=${region} \
    --enable-private-ip-google-access
----
+
. Create the Private Service Connect (PSC) subnets by running the following command:
+
[source,terminal]
----
$ gcloud compute networks subnets create ${prefix}-psc \
    --network=${prefix}-vpc \
    --region=${region} \
    --stack-type=IPV4_ONLY \
    --range=10.0.0.128/29 \
    --purpose=PRIVATE_SERVICE_CONNECT

----
+
These examples use the subnet ranges of 10.0.2.0/23 for the worker subnet, 10.0.0.0/25 for the control plane subnet, and 10.0.0.128/29 for the PSC subnet. Modify the parameters to meet your needs. Ensure the parameter values are contained within the machine CIDR you set earlier in this tutorial.

.Verification

* Verify the VPC and subnets were created by running the following command:
+
[source,terminal]
----
$ gcloud compute networks subnets list --network=${prefix}-vpc
----
+
The output shows the three subnets you created with their internet protocol (IP) ranges and regions.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-deploy-policy_{context}"]
= Deploying a global firewall policy

[role="_abstract"]
Create a global network firewall policy. Attach it to your VPC so you can control traffic that leaves your OpenShift Container Platform cluster.

.Procedure
. Run this command to create a global network firewall policy:
+
[source,terminal]
----
$ gcloud compute network-firewall-policies create \
    ${prefix} \
    --description "OpenShift Dedicated Egress Firewall" \
    --global
----
+
. Run this command to attach the new policy to the VPC you created earlier:
+
[source,terminal]
----
$ gcloud compute network-firewall-policies associations create \
      --name ${prefix}-vpc-association \
      --firewall-policy ${prefix} \
      --network ${prefix}-vpc \
      --global-firewall-policy

----

.Verification

* Run this command to check that the policy exists and is attached to your VPC:
+
[source,terminal]
----
$ gcloud compute network-firewall-policies describe ${prefix} --global
----
+
The output lists the policy and its link to your VPC.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-create-a-cloud-router_{context}"]
= Creating a Cloud Router and Cloud network address translation

[role="_abstract"]
Create a Cloud Router and Cloud network address translation (NAT). Private VMs can use the internet while their private IP addresses stay hidden.

.Procedure
. Reserve an IP address for Cloud NAT by running the following command:
+
[source,terminal]
----
$ gcloud compute addresses create ${prefix}-${region}-cloudnatip \
    --region=${region}
----
+
. Create a Cloud Router by running the following command:
+
[source,terminal]
----
$ gcloud compute routers create ${prefix}-router \
    --region=${region} \
    --network=${prefix}-vpc
----
+
. Create a Cloud NAT by running the following command:
+
[source,terminal]
----
$ gcloud compute routers nats create ${prefix}-cloudnat-${region} \
    --router=${prefix}-router --router-region ${region} \
    --nat-all-subnet-ip-ranges \
    --nat-external-ip-pool=${prefix}-${region}-cloudnatip
----

.Verification

* Check that the Cloud Router and NAT gateway exist by running the following command:
+
[source,terminal]
----
$ gcloud compute routers describe ${prefix}-router --region=${region}
----
+
The output lists the router and the NAT gateway you created.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-create-private-dns_{context}"]
= Creating private Domain Name System records for private Google access

[role="_abstract"]
Create a private Domain Name System (DNS) zone to route Google application programming interface (API) traffic through the internal network of Google for faster and more secure connections.

.Procedure
. Create a private DNS zone for the googleapis.com domain by running the following command:
+
[source,terminal]
----
$ gcloud dns managed-zones create ${prefix}-googleapis \
    --visibility=private \
    --networks=https://www.googleapis.com/compute/v1/projects/${project_id}/global/networks/${prefix}-vpc \
    --description="Private Google Access" \
    --dns-name=googleapis.com
----
+
. Begin a record set transaction by running the following command:
+
[source,terminal]
----
$ gcloud dns record-sets transaction start \
    --zone=${prefix}-googleapis
----
+
. Stage the DNS records for Google APIs under the googleapis.com domain by running the following commands:
+
[source,terminal]
----
$ gcloud dns record-sets transaction add --name="*.googleapis.com." \
    --type=CNAME restricted.googleapis.com. \
    --zone=${prefix}-googleapis \
    --ttl=300
----
+
[source,terminal]
----
$ gcloud dns record-sets transaction add 199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7 \
    --name=restricted.googleapis.com. \
    --type=A \
    --zone=${prefix}-googleapis \
    --ttl=300

----
+
. Apply the staged record set transaction you started above by running the following command:
+
[source,terminal]
----
$ gcloud dns record-sets transaction execute \
    --zone=$prefix-googleapis
----

.Verification

* Verify the private DNS zone and records were created by running the following command:
+
[source,terminal]
----
$ gcloud dns record-sets list --zone=${prefix}-googleapis
----
+
The output shows the DNS zone with CNAME and A records for googleapis.com.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-create-firewall-rules_{context}"]
= Creating the firewall rules

[role="_abstract"]
Create firewall rules for egress to private IP ranges and to the OpenShift Container Platform domains listed in this procedure. Egress to other external destinations does not match these rules and is not permitted.

.Procedure
. Create a blanket allow rule for private IP (Request for Comments (RFC) 1918) address space by running the following command:
+
[source,terminal]
----
$ gcloud compute network-firewall-policies rules create 500 \
    --description "Allow egress to private IP ranges" \
    --action=allow \
    --firewall-policy=${prefix} \
    --global-firewall-policy \
    --direction=EGRESS \
    --layer4-configs all \
    --dest-ip-ranges=10.0.0.0/8,172.16.0.0/12,192.168.0.0/16

----
+
. Create an allow rule for HTTPS (tcp/443) domains required for OpenShift Container Platform by running the following command:
+
[NOTE]
====
If you receive an error "Cannot have rules with the same priorities", the rule already exists. You can verify it with:

[source,bash]
----
$ gcloud compute network-firewall-policies rules describe 500 --firewall-policy=${prefix} --global-firewall-policy
$ gcloud compute network-firewall-policies rules describe 600 --firewall-policy=${prefix} --global-firewall-policy
----

To re-create the rules, first delete them:

[source,bash]
----
$ gcloud compute network-firewall-policies rules delete 500 --firewall-policy=${prefix} --global-firewall-policy
$ gcloud compute network-firewall-policies rules delete 600 --firewall-policy=${prefix} --global-firewall-policy
----
====
+
[source,terminal]
----
$ gcloud compute network-firewall-policies rules create 600 \
    --description "Allow egress to OpenShift Dedicated required domains (tcp/443)" \
    --action=allow \
    --firewall-policy=${prefix} \
    --global-firewall-policy \
    --direction=EGRESS \
    --layer4-configs tcp:443 \
    --dest-fqdns accounts.google.com,pull.q1w2.quay.rhcloud.com,http-inputs-osdsecuritylogs.splunkcloud.com,nosnch.in,api.deadmanssnitch.com,events.pagerduty.com,api.pagerduty.com,api.openshift.com,mirror.openshift.com,observatorium.api.openshift.com,observatorium-mst.api.openshift.com,console.redhat.com,infogw.api.openshift.com,api.access.redhat.com,cert-api.access.redhat.com,catalog.redhat.com,sso.redhat.com,registry.connect.redhat.com,registry.access.redhat.com,cdn01.quay.io,cdn02.quay.io,cdn03.quay.io,cdn04.quay.io,cdn05.quay.io,cdn06.quay.io,cdn.quay.io,quay.io,registry.redhat.io,quayio-production-s3.s3.amazonaws.com

----
+
[IMPORTANT]
====
The firewall blocks any traffic if you did not create any matching rules. To allow access to other resources, such as internal networks or other external endpoints, create additional rules with a priority of less than 1000. For more information on how to create firewall rules, see the _Additional resources_.
====

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-create-osd-gcp-cluster_{context}"]
= Cluster creation

[role="_abstract"]
Your OpenShift Container Platform cluster on {GCP} uses the VPC, subnets, and firewall rules from this tutorial.

For detailed instructions on creating a cluster, see Creating a cluster on {GCP}.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-delete-osd-gcp-cluster_{context}"]
= Cluster deletion

[role="_abstract"]
When you delete your cluster on {GCP}, also clean up the network setup from this guide to prevent ongoing charges.

For detailed instructions on deleting a cluster, see Deleting an OpenShift Dedicated cluster on {GCP}.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-limit-egress-ngfw.adoc

[id="cloud-experts-osd-limit-egress-ngfw-clean-resources_{context}"]
= Cleaning up resources

[role="_abstract"]
Delete the {GCP} networking infrastructure after deleting your cluster to prevent ongoing charges. The cluster deletion does not automatically remove virtual private cloud (VPC) networks, subnets, firewall policies, or domain name system (DNS) zones.

.Procedure
. Authenticate by running the following command:
+
[source,terminal]
----
$ gcloud init
----
+
. Log in to your {GCP} account by running the following command:
+
[source,terminal]
----
$ gcloud auth application-default login
----
+
. Log in to the {cluster-manager} CLI tool by running the following command:
+
[source,terminal]
----
$ ocm login --use-auth-code
----
+
You can now clean up the resources you created as part of this tutorial. To respect resource dependencies, delete them in the reverse order of their creation.

. Delete the association of the firewall policy with the VPC by running the following command:
+
[source,terminal]
----
$ gcloud compute network-firewall-policies associations delete \
      --name network-${prefix}-vpc \
      --firewall-policy=${prefix} \
      --global-firewall-policy \
      --project=${project_id}
----
+
. Delete the global network firewall policy by running the following command:
+
[source,terminal]
----
$ gcloud compute network-firewall-policies delete ${prefix} --global --project=${project_id}
----
+
. List and delete all user-defined DNS records from the Private DNS zone:
+
[source,terminal]
----
$ gcloud dns record-sets list \
    --project=${project_id} \
    --zone=${prefix}-googleapis \
    --filter="type!=NS AND type!=SOA" \
    --format="value(name,type)" | while read name type; do
  gcloud dns record-sets delete "$name" \
    --project=${project_id} \
    --zone=${prefix}-googleapis \
    --type="$type"
done
----
+
. Delete the Private DNS Zone by running the following command:
+
[source,terminal]
----
$ gcloud dns managed-zones delete ${prefix}-googleapis --project=${project_id}
----
+
. Delete the Cloud NAT gateway:
+
[source,terminal]
----
$ gcloud compute routers nats delete ${prefix}-cloudnat-${region} \
    --router=${prefix}-router \
    --router-region=${region} \
    --project=${project_id}
----
+
. Delete the Cloud Router by running the following command:
+
[source,terminal]
----
$ gcloud compute routers delete ${prefix}-router --region=${region} --project=${project_id}
----
+
. Delete the reserved IP address by running the following command:
+
[source,terminal]
+
----
$ gcloud compute addresses delete ${prefix}-${region}-cloudnatip --region=${region} --project=${project_id}
----
+
. Delete the worker subnet by running the following command:
+
[source,terminal]
+
----
$ gcloud compute networks subnets delete ${prefix}-worker --region=${region} --project=${project_id}
----
+
. Delete the control plane subnet by running the following command:
+
[source,terminal]
+
----
$ gcloud compute networks subnets delete ${prefix}-control-plane --region=${region} --project=${project_id}
----
+
. Delete the Private Service Connect (PSC) subnet by running the following command:
+
[source,terminal]
----
$ gcloud compute networks subnets delete ${prefix}-psc --region=${region} --project=${project_id}
----
+
. Delete the VPC by running the following command:
+
[source,terminal]
----
$ gcloud compute networks delete ${prefix}-vpc --project=${project_id}
----

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Regions and zones ({GCP})
* Create and manage VPC networks ({GCP})
* Subnets overview ({GCP})
* Firewall overview ({GCP})
* Use global network firewall policies and rules ({GCP})
* Cloud NAT overview ({GCP})
* Cloud Router overview ({GCP})
* Configure Private Google Access ({GCP})
* DNS zones overview ({GCP})
* VPC firewall rules overview ({GCP})
* Firewall prerequisites for {GCP}
* Use global network firewall policies and rules
* `gcloud` command-line tool reference ({GCP})
