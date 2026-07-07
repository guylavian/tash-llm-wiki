---
title: "Tutorial: Updating component routes with custom domains and TLS certificates"
type: reference
domain: openshift
slug: cloud-experts-osd-tutorials-4-22-cloud-experts-osd-update-component-routes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes
version: 4.22
family: cloud_experts_osd_tutorials
documentKind: "Documentation"
---

# Tutorial: Updating component routes with custom domains and TLS certificates

[id="cloud-experts-osd-update-component-routes"]
= Tutorial: Updating component routes with custom domains and TLS certificates

[role="_abstract"]
Change the hostname and Transport Layer Security (TLS) certificate of the web console, OAuth server, and Downloads component routes to use custom domains that align with your organization's branding and security requirements.

[IMPORTANT]
====
Red Hat experts authored this content, but it has not yet been tested on every supported configuration.
====

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes.adoc

[id="cloud-experts-osd-update-component-routes-environment-setup_{context}"]
= Setting up your environment for component route updates

[role="_abstract"]
Log in to your cluster as an admin user and configure environment variables to streamline the component route update workflow.

.Prerequisites
* You have installed {cluster-manager-first} command-line interface (CLI) (`ocm`) version 1.0.5 or higher.
* You have installed `gcloud` CLI.
* You have created an OpenShift Container Platform on {GCP} cluster version 4.14 or higher.
* You have installed {oc-first}.
* You have installed `jq` CLI.
* You have confirmed that you have access to the cluster as a user with the `cluster-admin` role.
* You have installed OpenSSL (for generating the demonstration SSL/TLS certificates).

.Procedure
. Log in to your cluster using an account with `cluster-admin` privileges.
+
. Configure an environment variable for your cluster name:
+
[source,terminal]
----
$ export CLUSTER_NAME=$(oc get infrastructure cluster -o=jsonpath="{.status.infrastructureName}"  | sed 's/-[a-z0-9]\{5\}$//')
$ export CLUSTER_ID=$(oc get clusterversion version -o jsonpath='{.spec.clusterID}')
----

.Verification
* Ensure the environment variable is set correctly:
+
[source,terminal]
----
$ echo "Cluster Name: ${CLUSTER_NAME}"
$ echo "Cluster ID: ${CLUSTER_ID}"
----
+
.Example output
[source,text]
----
Cluster Name: my-osd-cluster
Cluster ID: 12a3b456-78cd-90ef-1234-56789abcdef0
----

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes.adoc

[id="cloud-experts-osd-update-component-routes-find-current-component-routes_{context}"]
= Finding the current component routes

[role="_abstract"]
Find the base hostname of your cluster routes to verify the default component route configuration.

.Procedure
. Verify that you can reach the component routes on their default hostnames. You can find the hostnames by querying the lists of routes in the `openshift-console` and `openshift-authentication` projects.
+
[source,bash]
----
$ oc get routes -n openshift-console
$ oc get routes -n openshift-authentication
----
+
.Example output
[source,text]
----
NAME        HOST/PORT                                                                          PATH       SERVICES    PORT    TERMINATION          WILDCARD
console     console-openshift-console.apps.my-example-cluster-gcp.<cluster_id>.openshiftapps.com    ... 1 more  console    https   reencrypt/Redirect   None
downloads   downloads-openshift-console.apps.my-example-cluster-gcp.<cluster_id>.openshiftapps.com  ... 1 more  downloads  http    edge/Redirect        None
NAME              HOST/PORT                                                             PATH        SERVICES          PORT   TERMINATION            WILDCARD
oauth-openshift   oauth-openshift.apps.my-example-cluster-gcp.<cluster_id>.openshiftapps.com ... 1 more  oauth-openshift   6443   passthrough/Redirect   None
----
+
By running these commands you can see that the default component routes for your cluster are:
+
* `console-openshift-console.apps.my-example-cluster-gcp.<cluster_id>.openshiftapps.com` for Console
* `downloads-openshift-console.apps.my-example-cluster-gcp.<cluster_id>.openshiftapps.com` for Downloads
* `oauth-openshift.apps.my-example-cluster-gcp.<cluster_id>.openshiftapps.com` for OAuth
+
From this output you can see that your base hostname is `<cluster_id>.openshiftapps.com`.
+
. Get the ID of the default ingress by running the following command:
+
[source,bash]
----
$ export INGRESS_ID=$(ocm list ingresses -c ${CLUSTER_NAME} | awk '$4 == "true" {print $1}')
----
+
. Ensure all fields output correctly before moving to the next section:
+
[source,terminal]
----
$ echo "Ingress ID: ${INGRESS_ID}"
----
+
.Example output
[source,text]
----
Ingress ID: r3l6
----

. Use the `ocm edit ingress` command to change the hostname of each service and add a TLS certificate for all of your component routes. This excerpt of the command-line help for the `ocm edit ingress` command shows the relevant parameters:
+
[source,bash]
----
$ ocm edit ingress -h
Edit a cluster ingress for a cluster. Usage:
  ocm edit ingress ID [flags]
  [...]
  --component-routes string                Component routes settings. Available keys [oauth, console, downloads]. For each key a pair of hostname and tlsSecretRef is expected to be supplied. Format should be a comma separate list 'oauth: hostname=example-hostname;tlsSecretRef=example-secret-ref,downloads:...'
----

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes.adoc

[id="cloud-experts-osd-update-component-routes-create-tls-certificates_{context}"]
= Creating TLS certificates for each component route

[role="_abstract"]
Create three self-signed certificates, one for each component route. Trust them on your system so you can open each new hostname in a browser.

[WARNING]
====
Use this flow for learning only, not for production. For live systems, request valid certificates from your certificate authority (CA).
====

[IMPORTANT]
====
Use one certificate per route to prevent issues with HTTP/2 connection coalescing. Wildcard certificates and subject alternative names (SAN) certificates are not supported.
====

This example uses the following custom component routes:

* `console.example.com` for Console
* `downloads.console.example.com` for Downloads
* `oauth.console.example.com` for OAuth

.Procedure
* For each route, run the example `openssl` commands. Set `-subj` to that route's domain name:
+
.Example output:
[source,bash]
----
$ openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout key-console.pem -out cert-console.pem -subj "/CN=console.example.com"
$ openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout key-downloads.pem -out cert-downloads.pem -subj "/CN=downloads.console.example.com"
$ openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout key-oauth.pem -out cert-oauth.pem -subj "/CN=oauth.console.example.com"
----

.Verification

* Check that the `.pem` certificate and key files exist:
+
[source,bash]
----
$ ls -1 *.pem
----
+
.Example output
[source,text]
----
cert-console.pem
cert-downloads.pem
cert-oauth.pem
key-console.pem
key-downloads.pem
key-oauth.pem
----

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes.adoc

[id="cloud-experts-osd-update-component-routes-add-certificates-as-secrets_{context}"]
= Adding the certificates to the cluster as secrets

[role="_abstract"]
Add the Transport Layer Security (TLS) certificates to your cluster as secrets in the `openshift-config` namespace to reference them when updating component routes.

.Procedure
* Create three TLS secrets in the `openshift-config` namespace.
+
These become your secret reference when you update the component routes.
+
[source,bash]
----
$ oc create secret tls console-tls --cert=cert-console.pem --key=key-console.pem -n openshift-config
$ oc create secret tls downloads-tls --cert=cert-downloads.pem --key=key-downloads.pem -n openshift-config
$ oc create secret tls oauth-tls --cert=cert-oauth.pem --key=key-oauth.pem -n openshift-config
----

.Verification

* Verify that the TLS secrets were created:
+
[source,bash]
----
$ oc get secrets -n openshift-config | grep -E 'console-tls|downloads-tls|oauth-tls'
----
+
The output shows the three TLS secrets.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes.adoc

[id="cloud-experts-osd-update-component-routes-find-lb-hostname_{context}"]
= Finding the load balancer IP address

[role="_abstract"]
Find the load balancer internet protocol (IP) address of your cluster to create domain name system (DNS) records for the component route hostnames.

.Procedure
. Retrieve the IP address of the load balancer by running the following command, using the namespace for the load balancer:
+
[source,bash]
----
$ oc get svc -n <namespace>
----
+
The load balancer IP of the load balancer is the `EXTERNAL-IP` associated with the `router-default` service in the `openshift-ingress` namespace.
+
.Example output
[source,bash]
----
$ oc get svc -n openshift-ingress
NAME            TYPE          CLUSTER-IP     EXTERNAL-IP        PORT(S)                     AGE
router-default  LoadBalancer  172.30.237.88  203.0.113.10      80:31175/TCP,443:31554/TCP  76d
----
+
In this example, the load balancer IP is `203.0.113.10`.

. Save this value for later, as you need it to configure DNS records for your new component route hostnames.
. Create an A record in your DNS settings, pointing the domain to the IP address of the load balancer for router-default.

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes.adoc

[id="cloud-experts-osd-update-component-routes-tls-using-ocm-cli_{context}"]
= Updating the component routes and TLS certificates

[role="_abstract"]
Use the {cluster-manager-first} CLI to apply your custom hostnames and TLS certificates to the component routes.

.Procedure
. Use the `ocm edit ingress` command to update your default ingress route with the new base domain and the secret reference associated with it, and update the hostnames for each component route.
+
[source,bash]
----
$ ocm edit ingress -c ${CLUSTER_NAME} ${INGRESS_ID} --component-routes 'console: hostname=console.my-new-domain.dev;tlsSecretRef=console-tls,downloads: hostname=downloads.my-new-domain.dev;tlsSecretRef=downloads-tls,oauth: hostname=oauth.my-new-domain.dev;tlsSecretRef=oauth-tls'
----
+
[NOTE]
====
You can also edit only a subset of the component routes by leaving the component routes you do not want to change set to an empty string. For example, if you only want to change the Console and OAuth server hostnames and TLS certificates, you would run the following command:
[source,bash]
----
$ ocm edit ingress -c ${CLUSTER_NAME} ${INGRESS_ID} --component-routes 'console: hostname=console.my-new-domain.dev;tlsSecretRef=console-tls,downloads: hostname="";tlsSecretRef="", oauth: hostname=oauth.my-new-domain.dev;tlsSecretRef=oauth-tls'
----
====
+
. Run the `ocm list ingress` command to verify your changes:
+
[source,bash]
----
$ ocm list ingress -c ${CLUSTER_NAME} -ojson | jq ".[] | select(.id == \"${INGRESS_ID}\") | .component_routes"
----
+
.Example output
[source,text]
----
{
  "console": {
    "kind": "ComponentRoute",
    "hostname": "console.my-new-domain.dev",
    "tls_secret_ref": "console-tls"
  },
  "downloads": {
    "kind": "ComponentRoute",
    "hostname": "downloads.my-new-domain.dev",
    "tls_secret_ref": "downloads-tls"
  },
  "oauth": {
    "kind": "ComponentRoute",
    "hostname": "oauth.my-new-domain.dev",
    "tls_secret_ref": "oauth-tls"
  }
}
----

// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-osd-update-component-routes.adoc

[id="cloud-experts-osd-update-component-routes-reset-component-routes-to-default_{context}"]
= Resetting routes to defaults

[role="_abstract"]
Reset the routes, use default hostnames, and remove custom TLS certs.

.Procedure
* Reset your routes by running the following command:
+
[source,bash]
----
$ ocm edit ingress -c ${CLUSTER_NAME} ${INGRESS_ID} --component-routes 'console: hostname="";tlsSecretRef="",downloads: hostname="";tlsSecretRef="", oauth: hostname="";tlsSecretRef=""'
----

.Verification
* Check that hostnames and TLS cert refs use defaults:
+
[source,bash]
----
$ ocm get /api/clusters_mgmt/v1/clusters/${CLUSTER_ID}/ingresses/${INGRESS_ID} | jq .component_routes
----
+
.Example output
[source,bash]
----
{
  "console": {
    "hostname": "console.my-new-domain.dev",
    "tls_secret_ref": "console-tls"
  },
  "downloads": {
    "hostname": "downloads.my-new-domain.dev",
    "tls_secret_ref": "downloads-tls"
  },
  "oauth": {
    "hostname": "oauth.my-new-domain.dev",
    "tls_secret_ref": "oauth-tls"
  }
}
----
+
The output shows empty `hostname` and `tls_secret_ref` for each route.

[role="_additional-resources"]
[id="additional-resources_{context}"]
== Additional resources

* Customizing the internal OAuth server URL
* Creating secrets
* Customizing the console route
* Customizing the download route
* OpenSSL req command documentation
* Ingress controller configuration parameters
