---
title: "SSL certificates are about to expire - SharePoint Server"
type: reference
domain: sharepoint
slug: technical-reference-ssl-certificates-expire
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/technical-reference/ssl-certificates-expire
family: technical-reference
documentKind: "troubleshooting"
abstract: "Learn how to replace the SSL certificates that are about to expire."
---

# SSL certificates are about to expire - SharePoint Server

Note

SSL certificates are about to expire

# SSL certificates are about to expire

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

**Rule Name:** SSL certificates are about to expire.

**Summary:** SSL certificates currently in use in the farm will expire within the certificate expiration warning threshold (15 days by default). Once an SSL certificate expires, it's no longer valid to secure the resource. Users will receive error messages from their web browsers and client applications when accessing web sites that use expired SSL certificates.

**Cause:** SSL certificates currently in use in the farm are about to expire.

**Resolution: Renew or replace these certificates to ensure uninterrupted access to these resources. You can renew or replace these certificates from the Certificate Management page in Central Administration.**

Additional resources

## Additional resources

- Last updated on 
		2023-04-27
