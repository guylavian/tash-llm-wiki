---
title: "Tutorial: Updating component routes with custom domains and TLS certificates"
type: reference
domain: openshift
slug: cloud-experts-tutorials-4-22-cloud-experts-update-component-routes
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/cloud_experts_tutorials/cloud-experts-update-component-routes
version: 4.22
family: cloud_experts_tutorials
documentKind: "Documentation"
---

# Tutorial: Updating component routes with custom domains and TLS certificates

[id="cloud-experts-update-component-routes"]
= Tutorial: Updating component routes with custom domains and TLS certificates

[role="_abstract"]
This guide demonstrates how to modify the hostname and TLS certificate of the Web console, OAuth server, and Downloads component routes in OpenShift Container Platform version 4.14 and above.{fn-supported-versions}

The changes that we make to the component routes{fn-term-component-routes} in this guide are described in greater detail in the customizing the internal OAuth server URL, console route, and download route OpenShift Container Platform documentation.

[id="prerequisites_{context}"]
== Prerequisites
* {rosa-cli} (`rosa`) version 1.2.37 or higher
* AWS CLI (`aws`)
* A OpenShift Container Platform cluster version 4.14 or higher
+
[NOTE]
====
{rosa-title} is not supported at this time.
====
+
* {oc-first}
* `jq` CLI
* Access to the cluster as a user with the `cluster-admin` role.
* OpenSSL (for generating the demonstration SSL/TLS certificates)

// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-environment-setup_{context}"]
= Setting up your environment

[role="_abstract"]
You can use environment variables to ensure consistency across the commands within this lab.

.Procedure
. Log in to your cluster using an account with `cluster-admin` privileges.
+
. Configure an environment variable for your cluster name:
+
[source,terminal]
----
$ export CLUSTER_NAME=$(oc get infrastructure cluster -o=jsonpath="{.status.infrastructureName}"  | sed 's/-[a-z0-9]\{5\}$//')
----

. Ensure all fields output correctly before moving to the next section:
+
[source,terminal]
----
$ echo "Cluster: ${CLUSTER_NAME}"
----
+
.Example output
[source,text]
----
Cluster: my-rosa-cluster
----
// Module included in the following assemblies:
//
// * cloud_experts_osd_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-find-current-component-routes_{context}"]
= Find the current routes

[role="_abstract"]
You need to use the {oc-first} tool to find the base hostname of your cluster routes.

.Procedure
. Verify that you can reach the component routes on their default hostnames.
+
You can find the hostnames by querying the lists of routes in the `openshift-console` and `openshift-authentication` projects.
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
console     console-openshift-console.apps.my-example-cluster-aws.z9a9.p1.openshiftapps.com    ... 1 more  console    https   reencrypt/Redirect   None
downloads   downloads-openshift-console.apps.my-example-cluster-aws.z9a9.p1.openshiftapps.com  ... 1 more  downloads  http    edge/Redirect        None
NAME              HOST/PORT                                                             PATH        SERVICES          PORT   TERMINATION            WILDCARD
oauth-openshift   oauth-openshift.apps.my-example-cluster-aws.z9a9.p1.openshiftapps.com ... 1 more  oauth-openshift   6443   passthrough/Redirect   None
----
+
From this output you can see that our base hostname is `z9a9.p1.openshiftapps.com`.
+
. Get the ID of the default ingress by running the following command:
+
[source,bash]
----
$ export INGRESS_ID=$(rosa list ingress -c ${CLUSTER_NAME} -o json | jq -r '.[] | select(.default == true) | .id')
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
+
By running these commands you can see that the default component routes for our cluster are:
+
* `console-openshift-console.apps.my-example-cluster-aws.z9a9.p1.openshiftapps.com` for Console
* `downloads-openshift-console.apps.my-example-cluster-aws.z9a9.p1.openshiftapps.com` for Downloads
* `oauth-openshift.apps.my-example-cluster-aws.z9a9.p1.openshiftapps.com` for OAuth
+
We can use the `rosa edit ingress` command to change the hostname of each service and add a TLS certificate for all of our component routes. The relevant parameters are shown in this excerpt of the command-line help for the `rosa edit ingress` command:
+
[source,bash]
----
$ rosa edit ingress -h
Edit a cluster ingress for a cluster. Usage:
  rosa edit ingress ID [flags]
  [...]
  --component-routes string                Component routes settings. Available keys [oauth, console, downloads]. For each key a pair of hostname and tlsSecretRef is expected to be supplied. Format should be a comma separate list 'oauth: hostname=example-hostname;tlsSecretRef=example-secret-ref,downloads:...'
----
+
For this example, we'll use the following custom component routes:
+
* `console.my-new-domain.dev` for Console
* `downloads.my-new-domain.dev` for Downloads
* `oauth.my-new-domain.dev` for OAuth
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-create-tls-certificates_{context}"]
= Create a valid TLS certificate for each component route

[role="_abstract"]
In this section, we create three separate self-signed certificate key pairs and then trust them to verify that we can access our new component routes using a real web browser.

[WARNING]
====
This is for demonstration purposes only, and is not recommended as a solution for production workloads. Consult your certificate authority to understand how to create certificates with similar attributes for your production workloads.
====

[IMPORTANT]
====
To prevent issues with HTTP/2 connection coalescing, you must use a separate individual certificate for each endpoint. Using a wildcard or SAN certificate is not supported.
====

.Procedure
. Generate a certificate for each component route, taking care to set our certificate's subject (`-subj`) to the custom domain of the component route we want to use:
+
*Example*:
+
[source,bash]
----
$ openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout key-console.pem -out cert-console.pem -subj "/CN=console.my-new-domain.dev"
$ openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout key-downloads.pem -out cert-downloads.pem -subj "/CN=downloads.my-new-domain.dev"
$ openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout key-oauth.pem -out cert-oauth.pem -subj "/CN=oauth.my-new-domain.dev"
----
+
This generates three pairs of `.pem` files, `key-<component>.pem` and `cert-<component>.pem`.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-add-certificates-as-secrets_{context}"]
= Add the certificates to the cluster as secrets

[role="_abstract"]
You can use the {oc-first} tool to add the certificates to your created cluster as secrets.

.Procedure
. Create three TLS secrets in the `openshift-config` namespace.
+
These become your secret reference when you update the component routes later in this guide.
+
[source,bash]
----
$ oc create secret tls console-tls --cert=cert-console.pem --key=key-console.pem -n openshift-config
$ oc create secret tls downloads-tls --cert=cert-downloads.pem --key=key-downloads.pem -n openshift-config
$ oc create secret tls oauth-tls --cert=cert-oauth.pem --key=key-oauth.pem -n openshift-config
----
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-find-lb-hostname_{context}"]
= Find the hostname of the load balancer in your cluster

[role="_abstract"]
When you create a cluster, the service creates a load balancer and generates a hostname for that load balancer. We need to know the load balancer hostname in order to create DNS records for our cluster. You can find the hostname by using the {oc-first} tool.

.Procedure
* Run the following command against the `openshift-ingress` namespace.
+
[source,bash]
----
$ oc get svc -n openshift-ingress
NAME            TYPE          CLUSTER-IP     EXTERNAL-IP                                             PORT(S)                     AGE
router-default  LoadBalancer  172.30.237.88  a234gsr3242rsfsfs-1342r624.us-east-1.elb.amazonaws.com  80:31175/TCP,443:31554/TCP  76d
----
+
The hostname of the load balancer is the `EXTERNAL-IP` associated with the `router-default` service in the `openshift-ingress` namespace. In our case, the hostname is `a234gsr3242rsfsfs-1342r624.us-east-1.elb.amazonaws.com`.
+
Save this value for later, as we will need it to configure DNS records for our new component route hostnames.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-add-component-routes-to-dns_{context}"]
= Add component route DNS records to your hosting provider

[role="_abstract"]
In your hosting provider, add DNS records that map the `CNAME` of your new component route hostnames to the load balancer hostname we found in the previous step.

//.Need an image for this
//image::[Picture goes here]
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-tls-using-rosa-cli_{context}"]
= Update the component routes and TLS secret using the {rosa-cli}

[role="_abstract"]
When your DNS records have been updated, you can use the {rosa-cli} to change the component routes.

.Procedure
. Use the `rosa edit ingress` command to update your default ingress route with the new base domain and the secret reference associated with it, taking care to update the hostnames for each component route.
+
[source,bash]
----
$ rosa edit ingress -c ${CLUSTER_NAME} ${INGRESS_ID} --component-routes 'console: hostname=console.my-new-domain.dev;tlsSecretRef=console-tls,downloads: hostname=downloads.my-new-domain.dev;tlsSecretRef=downloads-tls,oauth: hostname=oauth.my-new-domain.dev;tlsSecretRef=oauth-tls'
----
+
[NOTE]
====
You can also edit only a subset of the component routes by leaving the component routes you do not want to change set to an empty string. For example, if you only want to change the Console and OAuth server hostnames and TLS certificates, you would run the following command:
[source,bash]
----
$ rosa edit ingress -c ${CLUSTER_NAME} ${INGRESS_ID} --component-routes 'console: hostname=console.my-new-domain.dev;tlsSecretRef=console-tls,downloads: hostname="";tlsSecretRef="", oauth: hostname=oauth.my-new-domain.dev;tlsSecretRef=oauth-tls'
----
====
+
. Run the `rosa list ingress` command to verify that your changes were successfully made:
+
[source,bash]
----
$ rosa list ingress -c ${CLUSTER_NAME} -ojson | jq ".[] | select(.id == \"${INGRESS_ID}\") | .component_routes"
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
+
. Add your certificate to the truststore on your local system, then confirm that you can access your components at their new routes using your local web browser.
// Module included in the following assemblies:
//
// * cloud_experts_tutorials/cloud-experts-update-component-routes.adoc

[id="cloud-experts-update-component-routes-reset-component-routes-to-default_{context}"]
= Reset the component routes to the default using the {rosa-cli}

[role="_abstract"]
You can use the {oc-first} tool to reset the component routes to the default configuration.

.Procedure
* Run the following command to reset your component routes:
+
[source,bash]
----
$ rosa edit ingress -c ${CLUSTER_NAME} ${INGRESS_ID} --component-routes 'console: hostname="";tlsSecretRef="",downloads: hostname="";tlsSecretRef="", oauth: hostname="";tlsSecretRef=""'
----
