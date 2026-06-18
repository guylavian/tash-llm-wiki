---
title: "Chapter 12. Configuring trusted certificates - Red Hat build of Keycloak 26.4 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-4-keycloak-truststore
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/server_configuration_guide/keycloak-truststore-
guide: server_configuration_guide
version: 26.4
family: rhbk
documentKind: "Documentation"
primary: true
abstract: "Configure the Red Hat build of Keycloak Truststore to communicate through TLS. When Red Hat build of Keycloak communicates with external services or has an incoming connection through TLS, it has to validate the remote certificate in order to ensure it is connecting to a trusted server. This is necessary in order to prevent man-in-the-middle attacks. The certificates of these clients or servers, o…"
---

# Chapter 12. Configuring trusted certificates - Red Hat build of Keycloak 26.4 Server Configuration Guide

Chapter 12. Configuring trusted certificates
Configure the Red Hat build of Keycloak Truststore to communicate through TLS.
When Red Hat build of Keycloak communicates with external services or has an incoming connection through TLS, it has to validate the remote certificate in order to ensure it is connecting to a trusted server. This is necessary in order to prevent man-in-the-middle attacks.
The certificates of these clients or servers, or the CA that signed these certificates, must be put in a truststore. This truststore is then configured for use by Red Hat build of Keycloak.
12.1. Configuring the System Truststore
The existing Java default truststore certs will always be trusted. If you need additional certificates, which will be the case if you have self-signed or internal certificate authorities that are not recognized by the JRE, they can be included in the conf/truststores
directory or subdirectories. The certs may be in PEM files, or PKCS12 files with extension .p12
, .pfx
, or .pkcs12
. If in PKCS12, the certs must be unencrypted - meaning no password is expected.
If you need an alternative path, use the --truststore-paths
option to specify additional files or directories where PEM or PKCS12 files are located. Paths are relative to where you launched Red Hat build of Keycloak, so absolute paths are recommended instead. If a directory is specified, it will be recursively scanned for truststore files.
After all applicable certs are included, the truststore will be used as the system default truststore via the javax.net.ssl
properties, and as the default for internal usage within Red Hat build of Keycloak.
For example:
bin/kc.[sh|bat] start --truststore-paths=/opt/truststore/myTrustStore.pfx,/opt/other-truststore/myOtherTrustStore.pem
It is still possible to directly set your own javax.net.ssl
truststore System properties, but it’s recommended to use the --truststore-paths
instead.
12.2. Hostname Verification Policy
You may refine how hostnames are verified by TLS connections with the tls-hostname-verifier
property.
-
DEFAULT
(the default) allows wildcards in subdomain names (e.g. *.foo.com) to match names with the same number of levels (e.g. a.foo.com, but not a.b.foo.com) - with rules and exclusions for public suffixes based upon https://publicsuffix.org/list/ -
ANY
means that the hostname is not verified - this mode should not be used in production. -
WILDCARD
(deprecated) allows wildcards in subdomain names (e.g. *.foo.com) to match anything, including multiple levels (e.g. a.b.foo.com). Use DEFAULT instead. STRICT
(deprecated) allows wildcards in subdomain names (e.g. *.foo.com) to match names with the same number of levels (e.g. a.foo.com, but not a.b.foo.com) - with some limited exclusions. Use DEFAULT instead.Please note that this setting does not apply to LDAP secure connections, which require strict hostname checking.
12.3. Relevant options
| Value | |
|---|---|
|
STRICT and WILDCARD have been deprecated, use DEFAULT instead. Deprecated values: |
|
|
|
