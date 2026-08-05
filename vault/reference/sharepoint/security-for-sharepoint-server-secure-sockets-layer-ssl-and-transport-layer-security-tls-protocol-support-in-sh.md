---
title: "Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol support in SharePoint Server - SharePoint Server"
type: reference
domain: sharepoint
slug: security-for-sharepoint-server-secure-sockets-layer-ssl-and-transport-layer-security-tls-protocol-support-in-sh
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/secure-sockets-layer-ssl-and-transport-layer-security-tls-protocol-support-in-sh
family: security-for-sharepoint-server
documentKind: "reference"
abstract: "This article describes the versions of the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol that SharePoint Server supports."
---

# Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol support in SharePoint Server - SharePoint Server

Note

Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol support in SharePoint Server

# Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocol support in SharePoint Server

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

SharePoint Server supports the following versions of the TLS protocol:

TLS 1.0

TLS 1.1

TLS 1.2

SSL 3.0

Note

SharePoint Server 2016 does not fully support SSL 3.0. This is because SharePoint Server 2016 disables SSL 3.0 connection encryption by default for some, but not all features.

Important

We recommend completely disabling the SSL 3.0 protocol due to its security vulnerability. For additional information on how to completely disable SSL 3.0, see the "Disabled SSL 3.0 in Windows For Server Software" and "Disabled SSL 3.0 in Windows For Client Software" sections in Microsoft Security Advisory 3009008.

For information about how to enable TLS support, see:

Strong Transport Layer Security (TLS) Encryption in SharePoint Server Subscription Edition

Enable TLS 1.1 and TLS 1.2 support in SharePoint Server 2019

Enable TLS 1.1 and TLS 1.2 support in SharePoint Server 2016

Enable TLS and SSL support in SharePoint 2013

SSL and TLS Protocols that can be disabled

## SSL and TLS Protocols that can be disabled

SharePoint Server supports disabling the following versions of the SSL/TLS protocol:

TLS 1.0

TLS 1.1

TLS 1.2

SSL 3.0

Note

At least one of the following TLS protocols must remain enabled: TLS 1.0, TLS 1.1, or TLS 1.2.

See also

## See also

Transport Layer Security (TLS) in SharePoint Server Subscription Edition

Additional resources

## Additional resources

- Last updated on 
		2023-01-19
