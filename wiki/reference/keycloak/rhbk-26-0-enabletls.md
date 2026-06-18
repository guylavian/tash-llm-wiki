---
title: "Chapter 6. Configuring TLS - Red Hat build of Keycloak 26.0 Server Configuration Guide"
type: reference
domain: keycloak
slug: rhbk-26-0-enabletls
tier: reference
source: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_configuration_guide/enabletls-
guide: server_configuration_guide
version: 26.0
family: rhbk
documentKind: "Documentation"
---

# Chapter 6. Configuring TLS - Red Hat build of Keycloak 26.0 Server Configuration Guide

Chapter 6. Configuring TLS
Transport Layer Security (short: TLS) is crucial to exchange data over a secured channel. For production environments, you should never expose Red Hat build of Keycloak endpoints through HTTP, as sensitive data is at the core of what Red Hat build of Keycloak exchanges with other applications. In this chapter, you will learn how to configure Red Hat build of Keycloak to use HTTPS/TLS.
Red Hat build of Keycloak can be configured to load the required certificate infrastructure using files in PEM format or from a Java Keystore. When both alternatives are configured, the PEM files takes precedence over the Java Keystores.
6.1. Providing certificates in PEM format
When you use a pair of matching certificate and private key files in PEM format, you configure Red Hat build of Keycloak to use them by running the following command:
bin/kc.[sh|bat] start --https-certificate-file=/path/to/certfile.pem --https-certificate-key-file=/path/to/keyfile.pem
Red Hat build of Keycloak creates a keystore out of these files in memory and uses this keystore afterwards.
6.2. Providing a Java Keystore
When no keystore file is explicitly configured, but http-enabled
is set to false, Red Hat build of Keycloak looks for a conf/server.keystore
file.
As an alternative, you can use an existing keystore by running the following command:
bin/kc.[sh|bat] start --https-key-store-file=/path/to/existing-keystore-file
6.2.1. Setting the Keystore password
You can set a secure password for your keystore using the https-key-store-password
option:
bin/kc.[sh|bat] start --https-key-store-password=<value>
If no password is set, the default password password
is used.
6.2.1.1. Securing credentials
Avoid setting a password in plaintext by using the CLI or adding it to conf/keycloak.conf
file. Instead use good practices such as using a vault / mounted secret. For more detail, see Using a vault and Configuring Red Hat build of Keycloak for production.
6.3. Configuring TLS protocols
By default, Red Hat build of Keycloak does not enable deprecated TLS protocols. If your client supports only deprecated protocols, consider upgrading the client. However, as a temporary work-around, you can enable deprecated protocols by running the following command:
bin/kc.[sh|bat] start --https-protocols=<protocol>[,<protocol>]
To also allow TLSv1.2, use a command such as the following: kc.sh start --https-protocols=TLSv1.3,TLSv1.2
.
6.4. Switching the HTTPS port
Red Hat build of Keycloak listens for HTTPS traffic on port 8443
. To change this port, use the following command:
bin/kc.[sh|bat] start --https-port=<port>
6.5. Certificate and Key Reloading
By default Red Hat build of Keycloak will reload the certificates, keys, and keystores specified in https-*
options every hour. For environments where your server keys may need frequent rotation, this allows that to happen without a server restart. You may override the default via the https-certificates-reload-period
option. Interval on which to reload key store, trust store, and certificate files referenced by https-*
options. The value may be a java.time.Duration value, an integer number of seconds, or an integer followed by one of the time units [ms
, h
, m
, s
, d
]. Must be greater than 30 seconds. Use -1
to disable.
6.6. Relevant options
| Value | |
|---|---|
|
|
|
|
| |
|
| |
|
| (default) |
|
| |
|
| |
|
| (default) |
|
| |
|
| (default) |
|
| (default) |
|
| |
|
| |
|
| |
|
| (default) |
