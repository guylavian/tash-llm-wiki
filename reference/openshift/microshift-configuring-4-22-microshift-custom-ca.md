---
title: "Configuring custom certificate authorities"
type: reference
domain: openshift
slug: microshift-configuring-4-22-microshift-custom-ca
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_configuring/microshift-custom-ca
version: 4.22
family: microshift_configuring
documentKind: "Documentation"
---

# Configuring custom certificate authorities

[id="microshift-custom-ca"]
= Configuring custom certificate authorities

[role="_abstract"]
You can allow and encrypt connections with external clients by replacing the {microshift-short} default API server certificate with a custom server certificate issued by a certificate authority (CA).

// Module included in the following assemblies:
//
// * microshift_security_compliance/microshift-custom-ca.adoc

[id="microshift-custom-cas_{context}"]
= Using custom certificate authorities for the {microshift-short} API server

[role="_abstract"]
To enable external clients to verify the {microshift-short} API server and maintain encrypted connections, you can replace the default internal certificate with a custom server certificate issued by a trusted certificate authority (CA).

By default, clients outside of the node cannot verify the {microshift-short}-issued API server certificate. You must update the configuration file with the certificate location and relevant domain names to ensure secure access across your network.

The following steps illustrate the workflow for customizing the API server certificate configuration in {microshift-short}:

. Copy the certificates and keys to the preferred directory in the host operating system. Ensure that the files are accessible only with root access.

. Update the {microshift-short} configuration for each custom CA by specifying the certificate names and new fully qualified domain name (FQDN) in the {microshift-short} `/etc/microshift/config.yaml` configuration file.
+
Each certificate configuration can contain the following values:

* The certificate file location is a required value.
* A single common name containing the API server DNS and IP address or IP address range.
+
--
[TIP]
====
In most cases, {microshift-short} generates a new `kubeconfig` file for your custom CA that includes the IP address or range that you specify. The exception is when you specify wildcards for the IP address. In this case, {microshift-short} generates a `kubeconfig` file with the public IP address of the server. To use wildcards, you must update the `kubeconfig` file with your specific details.
====
--
* Multiple Subject Alternative Names (SANs) containing the API server DNS and IP addresses or a wildcard certificate.
* You can list additional DNS names for each certificate.

. After the {microshift-short} service restarts, you must copy the generated `kubeconfig` files to the client.

. Configure additional CAs on the client system. For example, you can update CA bundles in the {op-system-base-full} truststore.
+
[IMPORTANT]
====
Custom server certificates must be validated against CA data configured in the trust root of the host operating system. For more information, read the following documentation:

* The system-wide truststore
====

. The certificates and keys are read from the specified file location on the host. You can test and validate configuration from the client.

* If any validation fails, {microshift-short} skips the custom configuration and uses the default certificate to start. The priority is to continue the service uninterrupted. {microshift-short} logs errors when the service starts. Common errors include expired certificates, missing files, or wrong IP addresses.

. External server certificates are not automatically renewed. You must manually rotate your external certificates.

// Module included in the following assemblies:
//
// * microshift_security_compliance/microshift-custom-ca.adoc

[id="microshift-custom-cas-configuring_{context}"]
= Configuring custom certificate authorities

[role="_abstract"]
To configure externally generated certificates and domain names by using custom certificate authorities (CAs), add them to the {microshift-short} `/etc/microshift/config.yaml` configuration file. You must also configure the host operating system trust root.

[NOTE]
====
Externally generated `kubeconfig` files are created in the `/var/lib/microshift/resources/kubeadmin/<hostname>/kubeconfig` directory. If you need to use `localhost` in addition to externally generated configurations, retain the original `kubeconfig` file in its default location. The `localhost` `kubeconfig` file uses the self-signed certificate authority.
====

.Prerequisites

* The {oc-first} is installed.
* You have root access to the node.
* The certificate authority has issued the custom certificates.
* A {microshift-short} `/etc/microshift/config.yaml` configuration file exists.

.Procedure

. Copy the custom certificates you want to add to the trust root of the {microshift-short} host. Ensure that the
certificate and private keys are only accessible to {microshift-short}.

. For each custom CA that you need, add an `apiServer` section called `namedCertificates` to the `/etc/microshift/config.yaml` {microshift-short} configuration file by using the following example:
+
[source,yaml]
----
apiServer:
  namedCertificates:
   - certPath: ~/certs/api_fqdn_1.crt
     keyPath:  ~/certs/api_fqdn_1.key
   - certPath: ~/certs/api_fqdn_2.crt
     keyPath:  ~/certs/api_fqdn_2.key
     names:
     - api_fqdn_1
     - *.apps.external.com
----
+
where:

`apiServer.namedCertificates.certPath`:: Add the full path to the certificate.
`apiServer.namedCertificates.keyPath`:: Add the full path to the certificate key.
`apiServer.namedCertificates.names`:: Optional. Add a list of explicit DNS names. Leading wildcards are allowed. If no names are listed, the implicit names are extracted from the certificates.

. Restart the {microshift-short} to apply the certificates by running the following command:
+
[source,terminal]
----
$ systemctl microshift restart
----

. Wait a few minutes for the system to restart and apply the custom server. New `kubeconfig` files are generated in the `/var/lib/microshift/resources/kubeadmin/` directory.

. Copy the `kubeconfig` files to the client. If you specified wildcards for the IP address, update the `kubeconfig` to remove the public IP address of the server and replace that IP address with the specific wildcard range you want to use.

. From the client, use the following steps:

.. Specify the `kubeconfig` to use by running the following command:
+
[source,terminal]
----
$ export KUBECONFIG=~/custom-kubeconfigs/kubeconfig
----
+
Use the location of the copied `kubeconfig` file as the path.

.. Check that the certificates are applied by using the following command:
+
[source,terminal]
----
$ oc --certificate-authority ~/certs/ca.ca get node
----
+
.Example output
[source,terminal]
----
oc get node
NAME                             STATUS   ROLES                         AGE   VERSION
dhcp-1-235-195.arm.example.com   Ready    control-plane,master,worker   76m   v1.35.4
----

.. Add the new CA file to the $KUBECONFIG environment variable by running the following command:
+
[source,terminal]
----
$ oc config set clusters.microshift.certificate-authority /tmp/certificate-authority-data-new.crt
----

.. Verify that the new `kubeconfig` file contains the new CA by running the following command:
+
[source,terminal]
----
$ oc config view --flatten
----
+
.Example externally generated `kubeconfig` file
[source,yaml]
----
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /tmp/certificate-authority-data-new.crt
    server: https://api.ci-ln-k0gim2b-76ef8.aws-2.ci.openshift.org:6443
  name: ci-ln-k0gim2b-76ef8
contexts:
- context:
    cluster: ci-ln-k0gim2b-76ef8
    user:
  name:
current-context:
kind: Config
preferences: {}
----
+
where:

`clusters.cluster.certificate-authority`:: The `certificate-authority-data` section is not present in externally generated `kubeconfig` files. It is added with the `oc config set` command used previously.

.. Verify the `subject` and `issuer` of your customized API server certificate authority by running the following command:
+
[source,terminal]
----
$ curl --cacert /tmp/caCert.pem https://${fqdn_name}:6443/healthz -v
----
+
.Example output
----
Server certificate:
  subject: CN=kas-test-cert_server
  start date: Mar 12 11:39:46 2024 GMT
  expire date: Mar 12 11:39:46 2025 GMT
  subjectAltName: host "dhcp-1-235-3.arm.eng.rdu2.redhat.com" matched cert's "dhcp-1-235-3.arm.eng.rdu2.redhat.com"
  issuer: CN=kas-test-cert_ca
  SSL certificate verify ok.
----
+
[IMPORTANT]
====
Either replace the `certificate-authority-data` in the generated `kubeconfig` file with the new `rootCA` or add the `certificate-authority-data` to the trust root of the operating system. Do not use both methods.
====

.. Configure additional CAs in the trust root of the operating system. For example, in the RHEL Client truststore on the client system. The system-wide truststore.
** Updating the certificate bundle with the configuration that contains the CA is recommended.
** If you do not want to configure your certificate bundles, you can alternately use the `oc login localhost:8443 --certificate-authority=/path/to/cert.crt` command, but this method is not preferred.

// Module included in the following assemblies:
//
// * microshift_security_compliance/microshift-custom-ca.adoc

[id="microshift-custom-ca-reserved-name-values_{context}"]
= Custom certificates reserved name values

[role="_abstract"]
Certificate problems cause {microshift-short} to ignore certificates dynamically and log an error. Problems can be caused by:

* The certificate files do not exist on the disk or are not readable.
* The certificate is not parsable.
* The certificate overrides the internal certificates IP addresses or DNS names in a `SubjectAlternativeNames` (SAN) field. Do not use a reserved name when configuring SANs.

.Reserved Names values
[cols="<,<,<",options="header",]
|===
|Address |Type |Comment
|`localhost` |DNS |
|`127.0.0.1` |IP Address |
|`10.42.0.0` |IP Address |Node Network
|`10.43.0.0/16,10.44.0.0/16` |IP Address |Service Network
|169.254.169.2/29 |IP Address |br-ex Network
|`kubernetes.default.svc` |DNS |
|`openshift.default.svc` |DNS |
|`svc.cluster.local` |DNS |
|===

// Module included in the following assemblies:
//
// * microshift_security_compliance/microshift-custom-ca.adoc

[id="microshift-custom-ca-troubleshootin_{context}"]
= Troubleshooting custom certificates

[role="_abstract"]
To troubleshoot the implementation of custom certificates, you can take the following steps.

.Procedure

. From {microshift-short}, ensure that the certificate is served by the `kube-apiserver` and verify that the certificate path is appended to the `--tls-sni-cert-key` FLAG by running the following command:
+
[source,terminal]
----
$ journalctl -u microshift -b0 | grep tls-sni-cert-key
----
+
.Example output
[source,terminal]
----
Jan 24 14:53:00 localhost.localdomain microshift[45313]: kube-apiserver I0124 14:53:00.649099   45313 flags.go:64] FLAG: --tls-sni-cert-key="[/home/eslutsky/dev/certs/server.crt,/home/eslutsky/dev/certs/server.key;/var/lib/microshift/certs/kube-apiserver-external-signer/kube-external-serving/server.crt,/var/lib/microshift/certs/kube-apiserver-external-signer/kube-external-serving/server.key;/var/lib/microshift/certs/kube-apiserver-localhost-signer/kube-apiserver-localhost-serving/server.crt,/var/lib/microshift/certs/kube-apiserver-localhost-signer/kube-apiserver-localhost-serving/server.key;/var/lib/microshift/certs/kube-apiserver-service-network-signer/kube-apiserver-service-network-serving/server.crt,/var/lib/microshift/certs/kube-apiserver-service-network-signer/kube-apiserver-service-network-serving/server.key
----

. From the client, ensure that the `kube-apiserver` is serving the correct certificate by running the following command:
+
[source,terminal]
----
$ openssl s_client -connect <SNI_ADDRESS>:6443 -showcerts | openssl x509 -text -noout -in - | grep -C 1 "Alternative\|CN"
----

// Module included in the following assemblies:
//
// * microshift_security_compliance/microshift-custom-ca.adoc

[id="microshift-custom-ca-certificates-cleaning_{context}"]
= Cleaning up and recreating the custom certificates

[role="_abstract"]
You can stop the {microshift-short} service, clean up the custom certificates, and re-create the custom certificates, to ensure that your system uses the most recent certificate data.

.Procedure

. Stop the {microshift-short} services and clean up the custom certificates by running the following command:
+
[source,terminal]
----
$ sudo microshift-cleanup-data --cert
----
+
.Example output
[source,terminal]
----
Stopping MicroShift services
Removing MicroShift certificates
MicroShift service was stopped
Cleanup succeeded
----

. Restart the {microshift-short} services to recreate the custom certificates by running the following command:
+
[source,terminal]
----
$ sudo systemctl start microshift
----

[id="Additional-resources_microshift-custom-ca_{context}"]
[role="_additional-resources"]
== Additional resources

* OpenShift: Add an API server named certificate

* RHEL: Creating and managing TLS keys and certificates

* The system-wide truststore

* OpenShift CLI Reference: oc login
