---
title: "Chapter 1. Introduction to Red Hat Single Sign-On for OpenShift - Red Hat Single Sign-On 7.6 Red Hat Single Sign-On for OpenShift"
type: reference
domain: keycloak
slug: rhsso-7-6-introduction-to-red-hat-single-sign-on-for-openshift
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/red_hat_single_sign-on_for_openshift/introduction_to_red_hat_single_sign_on_for_openshift
version: 7.6
family: rhsso
documentKind: "Documentation"
abstract: "1.1. What is Red Hat Single Sign-On? Red Hat Single Sign-On is an integrated sign-on solution available as a Red Hat JBoss Middleware for OpenShift containerized image. The Red Hat Single Sign-On for OpenShift image provides an authentication server for users to centrally log in, log out, register, and manage user accounts for web applications, mobile applications, and RESTful web services. Red Ha…"
---

# Chapter 1. Introduction to Red Hat Single Sign-On for OpenShift - Red Hat Single Sign-On 7.6 Red Hat Single Sign-On for OpenShift

Chapter 1. Introduction to Red Hat Single Sign-On for OpenShift
1.1. What is Red Hat Single Sign-On?
Red Hat Single Sign-On is an integrated sign-on solution available as a Red Hat JBoss Middleware for OpenShift containerized image. The Red Hat Single Sign-On for OpenShift image provides an authentication server for users to centrally log in, log out, register, and manage user accounts for web applications, mobile applications, and RESTful web services.
Red Hat Single Sign-On for OpenShift is available on the following platforms: x86_64, IBM Z, and IBM Power Systems.
1.2. Comparison: Red Hat Single Sign-On for OpenShift Image versus Red Hat Single Sign-On
The Red Hat Single Sign-On for OpenShift image version number 7.6.12 is based on Red Hat Single Sign-On 7.6.12. There are some important differences in functionality between the Red Hat Single Sign-On for OpenShift image and Red Hat Single Sign-On that should be considered:
The Red Hat Single Sign-On for OpenShift image includes all of the functionality of Red Hat Single Sign-On. In addition, the Red Hat Single Sign-On-enabled JBoss EAP image automatically handles OpenID Connect or SAML client registration and configuration for .war deployments that contain <auth-method>KEYCLOAK</auth-method> or <auth-method>KEYCLOAK-SAML</auth-method> in their respective web.xml files.
1.3. Templates for use with this software
Red Hat offers multiple OpenShift application templates using the Red Hat Single Sign-On for OpenShift image version number 7.6.12. These templates define the resources needed to develop Red Hat Single Sign-On 7.6.12 server based deployment. The templates can mainly be split into two categories: passthrough templates and reencryption templates. Some other miscellaneous templates also exist.
1.3.1. Passthrough templates
These templates require that HTTPS, JGroups keystores, and a truststore for the Red Hat Single Sign-On server exist beforehand. They secure the TLS communication using passthrough TLS termination.
- sso76-ocp3-https, sso76-ocp4-https: Red Hat Single Sign-On 7.6.12 backed by internal H2 database on the same pod.
- sso76-ocp3-postgresql, sso76-ocp4-postgresql: Red Hat Single Sign-On 7.6.12 backed by ephemeral PostgreSQL database on a separate pod.
- sso76-ocp3-postgresql-persistent, sso76-ocp4-postgresql-persistent: Red Hat Single Sign-On 7.6.12 backed by persistent PostgreSQL database on a separate pod.
Templates for using Red Hat Single Sign-On with MySQL / MariaDB databases have been removed and are not available since Red Hat Single Sign-On version 7.4.
1.3.2. Re-encryption templates
Separate re-encryption templates exist for OpenShift 3.x and for OpenShift 4.x
1.3.2.1. OpenShift 3.x
The OpenShift 3.x templates use the service-ca.crt CA bundle file as part of the Service Serving Certificate Secrets to generate TLS certificates and keys for serving secure content. The Red Hat Single Sign-On truststore is also created automatically, containing the /var/run/secrets/kubernetes.io/serviceaccount/service-ca.crt
CA certificate file, which is used to sign the certificate for the HTTPS keystore.
The truststore for the Red Hat Single Sign-On server is pre-populated with the all known, trusted CA certificate files found in the Java system path. These templates secure the TLS communication using re-encryption TLS termination. The JGroups cluster traffic is authenticated using the AUTH
protocol and encrypted using the ASYM_ENCRYPT
protocol.
- sso76-ocp3-x509-https: Red Hat Single Sign-On 7.6.12 with auto-generated HTTPS keystore and Red Hat Single Sign-On truststore, backed by internal H2 database.
- sso76-ocp3-x509-postgresql-persistent: Red Hat Single Sign-On 7.6.12 with auto-generated HTTPS keystore and Red Hat Single Sign-On truststore, backed by persistent PostgreSQL database.
1.3.2.2. OpenShift 4.x
The OpenShift 4.x templates use the internal service serving x509 certificate secrets to automatically create the HTTPS keystore used for serving secure content. These templates use a new service CA bundle that contains the service.beta.openshift.io/inject-cabundle=true
ConfigMap definition.
The truststore for the Red Hat Single Sign-On server is pre-populated with the all known, trusted CA certificate files found in the Java system path. These templates secure the TLS communication using re-encryption TLS termination. The JGroups cluster traffic is authenticated using the AUTH
protocol and encrypted using the ASYM_ENCRYPT
protocol.
-
sso76-ocp4-x509-https: Red Hat Single Sign-On 7.6.12 with auto-generated HTTPS keystore and Red Hat Single Sign-On truststore, backed by internal H2 database. The
ASYM_ENCRYPT
JGroups protocol is used for encryption of cluster traffic. -
sso76-ocp4-x509-postgresql-persistent: Red Hat Single Sign-On 7.6.12 with auto-generated HTTPS keystore and Red Hat Single Sign-On truststore, backed by persistent PostgreSQL database. The
ASYM_ENCRYPT
JGroups protocol is used for encryption of cluster traffic.
1.3.3. Other templates
Other templates that integrate with Red Hat Single Sign-On are also available:
- eap64-sso-s2i: Red Hat Single Sign-On-enabled Red Hat JBoss Enterprise Application Platform 6.4.
- eap71-sso-s2i: Red Hat Single Sign-On-enabled Red Hat JBoss Enterprise Application Platform 7.1.
- datavirt63-secure-s2i: Red Hat Single Sign-On-enabled Red Hat JBoss Data Virtualization 6.3.
These templates contain environment variables specific to Red Hat Single Sign-On that enable automatic Red Hat Single Sign-On client registration when deployed.
1.4. Version compatibility and support
For details about OpenShift image version compatibility, see the Supported Configurations page.
The Red Hat Single Sign-On for OpenShift image versions between 7.0 and 7.5 are deprecated and they will no longer receive updates of image and application templates.
To deploy new applications, use the 7.6 version of the Red Hat Single Sign-On for OpenShift image along with the application templates specific to this image version.
