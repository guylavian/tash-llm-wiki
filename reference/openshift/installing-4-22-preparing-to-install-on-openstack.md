---
title: "Preparing to install on OpenStack"
type: reference
domain: openshift
slug: installing-4-22-preparing-to-install-on-openstack
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing/preparing-to-install-on-openstack
version: 4.22
family: installing
documentKind: "Documentation"
---

# Preparing to install on OpenStack

[id="preparing-to-install-on-openstack"]
= Preparing to install on OpenStack

You can install OpenShift Container Platform on {rh-openstack-first}.

[id="preparing-to-install-on-openstack-prerequisites"]
== Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.

[id="choosing-an-method-to-install-ocp-on-openstack"]
== Choosing a method to install OpenShift Container Platform on OpenStack

You can install OpenShift Container Platform on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

See Installation process for more information about installer-provisioned and user-provisioned installation processes.

[id="choosing-an-method-to-install-ocp-on-openstack-installer-provisioned"]
=== Installing a cluster on installer-provisioned infrastructure

You can install a cluster on {rh-openstack-first} infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods:

* **Installing a cluster on OpenStack with customizations**: You can install a customized cluster on {rh-openstack}. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available post-installation.

* **Installing a cluster on OpenStack in a restricted network**: You can install OpenShift Container Platform on {rh-openstack} in a restricted or disconnected network by creating an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

[id="choosing-an-method-to-install-ocp-on-openstack-user-provisioned"]
=== Installing a cluster on user-provisioned infrastructure

You can install a cluster on {rh-openstack} infrastructure that you provision, by using one of the following methods:

* **Installing a cluster on OpenStack on your own infrastructure**: You can install OpenShift Container Platform on user-provisioned {rh-openstack} infrastructure. By using this installation method, you can integrate your cluster with existing infrastructure and modifications. For installations on user-provisioned infrastructure, you must create all {rh-openstack} resources, like Nova servers, Neutron ports, and security groups. You can use the provided Ansible playbooks to assist with the deployment process.

// This is included in the following assemblies:
//
// * installing/installing_openstack/preparing-to-install-on-openstack.adoc

[id="security-osp-validating-certificates_{context}"]
= Scanning {rh-openstack} endpoints for legacy HTTPS certificates

Beginning with OpenShift Container Platform 4.10, HTTPS certificates must contain subject alternative name (SAN) fields. Run the following script to scan each HTTPS endpoint in a {rh-openstack-first} catalog for legacy certificates that only contain the `CommonName` field.

[IMPORTANT]
OpenShift Container Platform does not check the underlying {rh-openstack} infrastructure for legacy certificates prior to installation or updates. Use the provided script to check for these certificates yourself. Failing to update legacy certificates prior to installing or updating a cluster will result in cluster dysfunction.

.Prerequisites

* On the machine where you run the script, have the following software:
** Bash version 4.0 or greater
** `grep`
** OpenStack client
** `jq`
** OpenSSL version 1.1.1l or greater
* Populate the machine with {rh-openstack} credentials for the target cloud.

.Procedure

. Save the following script to your machine:
+
[%collapsible]
====
[source,bash]
----
#!/usr/bin/env bash

set -Eeuo pipefail

declare catalog san
catalog="$(mktemp)"
san="$(mktemp)"
readonly catalog san

declare invalid=0

openstack catalog list --format json --column Name --column Endpoints \
	| jq -r '.[] | .Name as $name | .Endpoints[] | select(.interface=="public") | [$name, .interface, .url] | join(" ")' \
	| sort \
	> "$catalog"

while read -r name interface url; do
	# Ignore HTTP
	if [[ ${url#"http://"} != "$url" ]]; then
		continue
	fi

	# Remove the schema from the URL
	noschema=${url#"https://"}

	# If the schema was not HTTPS, error
	if [[ "$noschema" == "$url" ]]; then
		echo "ERROR (unknown schema): $name $interface $url"
		exit 2
	fi

	# Remove the path and only keep host and port
	noschema="${noschema%%/*}"
	host="${noschema%%:*}"
	port="${noschema##*:}"

	# Add the port if was implicit
	if [[ "$port" == "$host" ]]; then
		port='443'
	fi

	# Get the SAN fields
	openssl s_client -showcerts -servername "$host" -connect "$host:$port" </dev/null 2>/dev/null \
		| openssl x509 -noout -ext subjectAltName \
		> "$san"

	# openssl returns the empty string if no SAN is found.
	# If a SAN is found, openssl is expected to return something like:
	#
	#    X509v3 Subject Alternative Name:
	#        DNS:standalone, DNS:osp1, IP Address:192.168.2.1, IP Address:10.254.1.2
	if [[ "$(grep -c "Subject Alternative Name" "$san" || true)" -gt 0 ]]; then
		echo "PASS: $name $interface $url"
	else
		invalid=$((invalid+1))
		echo "INVALID: $name $interface $url"
	fi
done < "$catalog"

# clean up temporary files
rm "$catalog" "$san"

if [[ $invalid -gt 0 ]]; then
	echo "${invalid} legacy certificates were detected. Update your certificates to include a SAN field."
	exit 1
else
	echo "All HTTPS certificates for this cloud are valid."
fi
----
====

. Run the script.

. Replace any certificates that the script reports as `INVALID` with certificates that contain SAN fields.

[IMPORTANT]
====
You must replace all legacy HTTPS certificates before you install OpenShift Container Platform 4.10 or update a cluster to that version. Legacy certificates will be rejected with the following message:

[source,txt]
----
x509: certificate relies on legacy Common Name field, use SANs instead
----
====

// This is included in the following assemblies:
//
// * installing/installing_openstack/preparing-to-install-on-openstack.adoc

[id="security-osp-validating-certificates-manually_{context}"]
= Scanning {rh-openstack} endpoints for legacy HTTPS certificates manually

Beginning with OpenShift Container Platform 4.10, HTTPS certificates must contain subject alternative name (SAN) fields. If you do not have access to the prerequisite tools that are listed in "Scanning {rh-openstack} endpoints for legacy HTTPS certificates", perform the following steps to scan each HTTPS endpoint in a {rh-openstack-first} catalog for legacy certificates that only contain the `CommonName` field.

[IMPORTANT]
====
OpenShift Container Platform does not check the underlying {rh-openstack} infrastructure for legacy certificates prior to installation or updates. Use the following steps to check for these certificates yourself. Failing to update legacy certificates prior to installing or updating a cluster will result in cluster dysfunction.
====

.Procedure

. On a command line, run the following command to view the URL of {rh-openstack} public endpoints:
+
[source,terminal]
----
$ openstack catalog list
----
+
Record the URL for each HTTPS endpoint that the command returns.
. For each public endpoint, note the host and the port.
+
[TIP]
====
Determine the host of an endpoint by removing the scheme, the port, and the path.
====

. For each endpoint, run the following commands to extract the SAN field of the certificate:
.. Set a `host` variable:
+
[source,terminal]
----
$ host=<host_name>
----
.. Set a `port` variable:
+
[source,terminal]
----
$ port=<port_number>
----
+
If the URL of the endpoint does not have a port, use the value `443`.
.. Retrieve the SAN field of the certificate:
+
[source,terminal]
----
$ openssl s_client -showcerts -servername "$host" -connect "$host:$port" </dev/null 2>/dev/null \
    | openssl x509 -noout -ext subjectAltName
----
+
.Example output
[source,terminal]
----
X509v3 Subject Alternative Name:
    DNS:your.host.example.net
----
+
For each endpoint, look for output that resembles the previous example. If there is no output for an endpoint, the certificate of that endpoint is invalid and must be re-issued.

[IMPORTANT]
====
You must replace all legacy HTTPS certificates before you install OpenShift Container Platform 4.10 or update a cluster to that version. Legacy certificates are rejected with the following message:

[source,txt]
----
x509: certificate relies on legacy Common Name field, use SANs instead
----
====
