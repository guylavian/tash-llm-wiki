---
title: "Configuring certificates for {hcp}"
type: reference
domain: openshift
slug: hosted-control-planes-4-22-hcp-certificates
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/hcp-certificates
version: 4.22
family: hosted_control_planes
documentKind: "Documentation"
---

# Configuring certificates for {hcp}

[id="hcp-certificates"]
= Configuring certificates for {hcp}

[role="_abstract"]
To establish secure and encrypted communication between your clients and the hosted control plane, you must configure a server certificate for your hosted cluster. With {hcp}, the steps to configure certificates differ from those of standalone OpenShift Container Platform.

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-certificates.adoc

[id="hcp-custom-cert_{context}"]
= Configuring a custom API server certificate in a hosted cluster

To configure a custom certificate for the API server, specify the certificate details in the `spec.configuration.apiServer` section of your `HostedCluster` configuration.

You can configure a custom certificate during either day-1 or day-2 operations. However, because the service publishing strategy is immutable after you set it during hosted cluster creation, you must know what the hostname is for the Kubernetes API server that you plan to configure.

.Prerequisites

* You created a Kubernetes secret that contains your custom certificate in the management cluster. The secret contains the following keys:

 ** `tls.crt`: The certificate
 ** `tls.key`: The private key

* If your `HostedCluster` configuration includes custom serving certificates via the `spec.configuration.apiServer.servingCerts.namedCertificates` specification, ensure that the Subject Alternative Names (SANs) of the certificate do not conflict with the external API server address. For example, depending on the hostname pattern used in your environment, the address might be in the following format: `api.<cluster-name>.<domain>`.
+
The `HostedCluster` resource automatically includes the external API address in the default Kubernetes API server certificate SANs. If the same hostname is in both the custom certificate and the auto-generated Kubernetes API server certificate, the configuration is rejected to prevent TLS serving ambiguity.
+
This validation applies to all service publishing strategies, including `LoadBalancer` and `NodePort`. The only exception is when you use {aws-first} as the provider with `Private` or `PublicAndPrivate` endpoint access configurations, where the platform manages the SAN conflict.

* The certificate must be valid for the external API endpoint.

* The validity period of the certificate aligns with your cluster's expected life cycle.

.Procedure

. Create a secret with your custom certificate by entering the following command:
+
[source,terminal]
----
$ oc create secret tls sample-hosted-kas-custom-cert \
  --cert=path/to/cert.crt \
  --key=path/to/key.key \
  -n <hosted_cluster_namespace>
----

. Update your `HostedCluster` configuration with the custom certificate details, as shown in the following example:
+
[source,yaml]
----
spec:
  configuration:
    apiServer:
      servingCerts:
        namedCertificates:
        - names: <1>
          - api-custom-cert-sample-hosted.sample-hosted.example.com
          servingCertificate: <2>
            name: sample-hosted-kas-custom-cert
----
<1> The list of DNS names that the certificate is valid for.
<2> The name of the secret that contains the custom certificate.

. Apply the changes to your `HostedCluster` configuration by entering the following command:
+
[source,terminal]
----
$ oc apply -f <hosted_cluster_config>.yaml
----

.Verification

* Check the API server pods to ensure that the new certificate is mounted.

* Test the connection to the API server by using the custom domain name.

* Verify the certificate details in your browser or by using tools such as `openssl`.

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-certificates.adoc

[id="hcp-kube-api-server-cert_{context}"]
= Configuring the Kubernetes API server for a hosted cluster

If you want to customize the Kubernetes API server for your hosted cluster, complete the following steps.

.Prerequisites

* You have a running hosted cluster.

* You have access to modify the `HostedCluster` resource.

* You have a custom DNS domain to use for the Kubernetes API server.
+
** The custom DNS domain must be properly configured and resolvable.
** The DNS domain must have valid TLS certificates configured.
** Network access to the domain must be properly configured in your environment.
** The custom DNS domain must be unique across your hosted clusters.

* You have a configured custom certificate. For more information, see "Configuring a custom API server certificate in a hosted cluster".

.Procedure

. In your provider platform, configure the DNS record so that the `kubeAPIServerDNSName` URL points to the IP address that the Kubernetes API server is being exposed to. The DNS record must be properly configured and resolvable from your cluster.
+
.Example command to configure the DNS record
[source,terminal]
----
$ dig + short kubeAPIServerDNSName
----

. In your `HostedCluster` specification, modify the `kubeAPIServerDNSName` field, as shown in the following example:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_cluster_namespace>
spec:
  configuration:
    apiServer:
      servingCerts:
        namedCertificates:
        - names: <1>
          - api-custom-cert-sample-hosted.sample-hosted.example.com
          servingCertificate: <2>
            name: sample-hosted-kas-custom-cert
  kubeAPIServerDNSName: api-custom-cert-sample-hosted.sample-hosted.example.com <3>
# ...
----
<1> The list of DNS names that the certificate is valid for. The names listed in this field cannot be the same as the names specified in the `spec.servicePublishingStrategy.*hostname` field.
<2> The name of the secret that contains the custom certificate.
<3> This field accepts a URI that will be used as the API server endpoint.

. Apply the configuration by entering the following command:
+
[source,terminal]
----
$ oc -f <hosted_cluster_spec>.yaml
----
+
After the configuration is applied, the HyperShift Operator generates a new `kubeconfig` secret that points to your custom DNS domain.

. Retrieve the `kubeconfig` secret by using the CLI or the console.
+
.. To retrieve the secret by using the CLI, enter the following command:
+
[source,terminal]
----
$ kubectl get secret <hosted_cluster_name>-custom-admin-kubeconfig \
  -n <cluster_namespace> \
  -o jsonpath='{.data.kubeconfig}' | base64 -d
----

+
.. To retrieve the secret by using the console, go to your hosted cluster and click **Download Kubeconfig**.
+
[NOTE]
====
You cannot consume the new `kubeconfig` secret by using the **show login command** option in the console.
====

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-certificates.adoc

[id="hcp-oauth-server-cert-about_{context}"]
= OAuth server certificates for {hcp}

[role="_abstract"]
In {hcp}, the OAuth server shares its serving certificate configuration with the Kubernetes API server. To configure a custom serving certificate for the OAuth server, you modify the `spec.configuration.apiServer` section in the `HostedCluster` resource.

[IMPORTANT]
====
This configuration method deviates from the standard OpenShift Container Platform behavior. In OpenShift Container Platform, OAuth certificates are configured separately through the `componentRoute` properties of the Ingress Operator. In {hcp}, the `namedCertificates` configuration in the API server settings applies to both the Kubernetes API server and the OAuth server.
====

In {hcp}, the Control Plane Operator reads serving certificates through the shared `GetNamedCertificates()` function. Certificates are not configured in an OAuth-specific section of the `HostedCluster` resource. In addition, OAuth server certificates are not provided through an OAuth custom resource definition (CRD) configuration. Instead, {hcp} automatically injects the selected certificates into the OAuth server deployment.

.OAuth certificate differences between OpenShift Container Platform and {hcp}
[cols="3",options="header"]
|===
|Area |OpenShift Container Platform |{hcp}

|Certificate source
|Ingress Operator generates and maps certificates through component routes
|OAuth uses `apiServer.servingCerts.namedCertificates` settings

|Certificate selection
|Based on ingress-managed routes
|Based on host name match in `namedCertificates` property

|User responsibility
|No need to manually provide OAuth certificates
|User must supply certificates if custom behavior is needed

|Code path
|Ingress Operator manages the OAuth route
|Control Plane Operator manages the OAuth server container runtime arguments
|===

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-certificates.adoc

[id="hcp-oauth-server-cert_{context}"]
= Configuring OAuth server certificates for a hosted cluster

[role="_abstract"]
If you want to use certificates from a trusted certificate authority (CA) to access a hosted cluster, you can configure OAuth server certificates.

.Prerequisites

* You have a running hosted cluster.

* You have `cluster-admin` access to the management cluster.

* You have access to modify the `HostedCluster` resource.

* You have a TLS secret that contains your signed certificate and private key in the hosted cluster namespace with the following keys:
+
** `tls.crt`
** `tls.key`

.Procedure

. Identify your hosted cluster namespace:

.. Export the namespace where your hosted cluster is running by entering the following command:
+
[source,terminal]
----
$ export HC_NAMESPACE=<hosted_cluster_namespace>
----

.. Export the hosted cluster name by entering the following command:
+
[source,terminal]
----
$ export CLUSTER_NAME=<hosted_cluster_name>
----

. Generate a quick test certificate by entering the following command:
+
[source,terminal]
----
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key \
  -out tls.crt \
  -subj "/CN=openshift-oauth" \
  -addext "subjectAltName=DNS:oauth-${HC_NAMESPACE}-${CLUSTER_NAME}.api-custom-cert-sample-hosted.sample-hosted.example.com"
----
+
The `api-custom-cert-sample-hosted.sample-hosted.example.com` value is used in the command and throughout the rest of this procedure as an example.
+
[NOTE]
====
This example uses a placeholder hostname. After you discover your OAuth route later in this procedure, you must regenerate this certificate with the correct hostname before you edit the `HostedCluster` resource.
====

. Confirm that the file exists by entering the following command:
+
[source,terminal]
----
$ ls tls.crt tls.key
----

. If you have not already created the TLS secret in the hosted cluster namespace, create the secret by entering the following command:
+
[source,terminal]
----
$ oc create secret tls my-oauth-cert-secret \
  --cert=path/to/tls.crt \
  --key=path/to/tls.key \
  -n $HC_NAMESPACE
----
+
.Example output
[source,terminal]
----
secret/my-oauth-cert-secret created
----
+
[NOTE]
====
Although the OAuth server runs in the hosted control plane namespace, the serving certificate must exist in the hosted cluster namespace. Secrets that are created in the hosted control plane namespace are not picked up.
====

. Discover the correct OAuth route:

.. Use the management cluster `kubconfig` file to enter the following command:
+
[source,terminal]
----
$ oc get routes -n ${HC_NAMESPACE}-${CLUSTER_NAME}
----

.. If the route name is `oauth`, confirm it by entering the following command:
+
[source,terminal]
----
$ oc get route oauth -n ${HC_NAMESPACE}-${CLUSTER_NAME} -o yaml
----

.. Prepare to extract the OAuth route host by entering the following command:
+
[source,terminal]
----
OAUTH_HOST=$(oc get route oauth \
  -n ${HC_NAMESPACE}-${CLUSTER_NAME} \
  -o jsonpath='{.spec.host}')
----

.. Extract the OAuth route host by entering the following command:
+
[source,terminal]
----
$ echo "${OAUTH_HOST}"
----
+
.Example output
[source,terminal]
----
oauth-${HC_NAMESPACE}-${CLUSTER_NAME}.api-custom-cert-sample-hosted.sample-hosted.example.com
----

. Edit the `HostedCluster` resource:

.. Open the `HostedCluster` resource for editing by entering the following command:
+
[source,terminal]
----
$ oc edit hostedcluster $CLUSTER_NAME -n $HC_NAMESPACE
----

.. In the resource, configure the named certificates by adding the `servingCerts.namedCertificates` stanza to the `spec.configuration.apiServer` section:
+
[source,yaml]
----
apiVersion: hypershift.openshift.io/v1beta1
kind: HostedCluster
metadata:
  name: <hosted_cluster_name>
  namespace: <hosted_cluster_namespace>
spec:
  configuration:
    apiServer:
      audit:
        profile: Default
      servingCerts:
        namedCertificates:
        - names:
          - api-custom-cert-sample-hosted.sample-hosted.example.com
          servingCertificate:
            name: my-oauth-cert-secret
# ...
----
+
where:

`spec.configuration.apiServer.servingCerts.namedCertificates.names`:: Specifies the actual host name of your OAuth route.
`spec.configuration.apiServer.servingCerts.servingCertificate.name`:: Specifies the name of your TLS secret. This secret must exist in the hosted cluster namespace.

.. Save and apply the changes. The Control Plane Operator reconciles the changes, the configuration propagates to the control plane, and the OAuth server begins serving the new certificate.
+
[IMPORTANT]
====
No separate OAuth certificate configuration field exists for a hosted cluster.
====

.Verification

* Verify the certificate being served by the route by entering the following command:
+
[source,terminal]
----
$ echo | openssl s_client \
  -connect "${OAUTH_HOST}:443" \
  -servername "${OAUTH_HOST}" \
  2>/dev/null \
  | openssl x509 -noout -subject -issuer -ext subjectAltName
----
+
.Example output
[source,terminal]
----
subject=CN=openshift-oauth
issuer=CN=openshift-oauth
X509v3 Subject Alternative Name:
    DNS:oauth-${HC_NAMESPACE}-${CLUSTER_NAME}.api-custom-cert-sample-hosted.sample-hosted.example.com
----
+
The output shows that the OAuth route is serving the custom certificate and the certificate comes from the `my-oauth-cert-secret` secret.

// Module included in the following assemblies:
//
// * hosted-control-planes/hcp-certificates.adoc

[id="hcp-ts-custom-dns_{context}"]
= Troubleshooting accessing a hosted cluster by using a custom DNS

If you encounter issues when you access a hosted cluster by using a custom DNS, complete the following steps.

.Procedure

. Verify that the DNS record is properly configured and resolved.

. Check that the TLS certificates for the custom domain are valid, verifying that the SAN is correct for your domain, by entering the following command:
+
[source,terminal]
----
$ oc get secret \
  -n clusters <serving_certificate_name> \
  -o jsonpath='{.data.tls\.crt}' | base64 \
  -d |openssl x509 -text -noout -
----

. Ensure that network connectivity to the custom domain is working.

. In the `HostedCluster` resource, verify that the status shows the correct custom `kubeconfig` information, as shown in the following example:
+
.Example `HostedCluster` status
[source,yaml]
----
status:
  customKubeconfig:
    name: sample-hosted-custom-admin-kubeconfig
----

. Check the `kube-apiserver` logs in the `HostedControlPlane` namespace by entering the following command:
+
[source,terminal]
----
$ oc logs -n <hosted_control_plane_namespace> \
  -l app=kube-apiserver -f -c kube-apiserver
----

//include::modules/hcp-ingress-cert.adoc[leveloffset=+1]
