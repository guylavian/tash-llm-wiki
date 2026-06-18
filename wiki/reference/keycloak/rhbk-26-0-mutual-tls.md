---
title: "Chapter 13. Configuring trusted certificates for mTLS - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-mutual-tls
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/mutual-tls-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 13. Configuring trusted certificates for mTLS - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 13. Configuring trusted certificates for mTLS
In order to properly validate client certificates and enable certain authentication methods like two-way TLS or mTLS, you can set a trust store with all the certificates (and certificate chain) the server should be trusting. There are number of capabilities that rely on this trust store to properly authenticate clients using certificates such as Mutual TLS and X.509 Authentication.
13.1. Enabling mTLS
Authentication using mTLS is disabled by default. To enable mTLS certificate handling when Red Hat build of Keycloak is the server and needs to validate certificates from requests made to Red Hat build of Keycloak endpoints, put the appropriate certificates in a truststore and use the following command to enable mTLS:
bin/kc.[sh|bat] start --https-client-auth=<none|request|required>
Using the value required
sets up Red Hat build of Keycloak to always ask for certificates and fail if no certificate is provided in a request. By setting the value to request
, Red Hat build of Keycloak will also accept requests without a certificate and only validate the correctness of a certificate if it exists.
The mTLS configuration and the truststore is shared by all Realms. It is not possible to configure different truststores for different Realms.
Management interface properties are inherited from the main HTTP server, including mTLS settings. It means when mTLS is set, it is also enabled for the management interface. To override the behavior, use the https-management-client-auth
property.
13.2. Using a dedicated truststore for mTLS
By default, Red Hat build of Keycloak uses the System Truststore to validate certificates. See Configuring trusted certificates for details.
If you need to use a dedicated truststore for mTLS, you can configure the location of this truststore by running the following command:
bin/kc.[sh|bat] start --https-trust-store-file=/path/to/file --https-trust-store-password=<value>
13.3. Additional resources
13.3.1. Using mTLS for outgoing HTTP requests
Be aware that this is the basic certificate configuration for mTLS use cases where Red Hat build of Keycloak acts as server. When Red Hat build of Keycloak acts as client instead, e.g. when Red Hat build of Keycloak tries to get a token from a token endpoint of a brokered identity provider that is secured by mTLS, you need to set up the HttpClient to provide the right certificates in the keystore for the outgoing request. To configure mTLS in these scenarios, see Configuring outgoing HTTP requests.
13.3.2. Configuring X.509 Authentication
For more information on how to configure X.509 Authentication, see X.509 Client Certificate User Authentication section.
13.4. Relevant options
| Value | |
|---|---|
| 🛠
|
|
|
| |
|
| |
|
| |
| 🛠
|
|
