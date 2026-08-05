---
title: "Private key management for SSL certificates - SharePoint Server"
type: reference
domain: sharepoint
slug: administration-private-key-management-for-ssl-certificates
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/administration/private-key-management-for-ssl-certificates
family: administration
documentKind: "article"
abstract: "Learn how SSL certificate implements private key management."
---

# Private key management for SSL certificates - SharePoint Server

Note

Private key management for SSL certificates

# Private key management for SSL certificates

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

To better support least privileges scenarios and minimize the permissions given to certificate private keys, SharePoint Server Subscription Edition Version 23H1 applies more granular and sophisticated permission management for these private keys. The permissions are based on the certificate assignments and are dynamically updated when the certificate assignments change.

For example, if a certificate is assigned to perform client certificate authentication to a Simple Mail Transfer Protocol (SMTP) server, SharePoint ensures that the process that’s connecting to the SMTP server has the necessary permissions to use the private key of that certificate. If a certificate is no longer assigned to perform client certificate authentication to an SMTP server, SharePoint removes permissions for that process so it no longer has access to the private key of that certificate.

The following API has been added
*Microsoft.SharePoint.Administration.CertificateManagement.SPServerCertificate* class to allow third-party integration with this functionality.

Additional resources

## Additional resources

- Last updated on 
		2023-11-01
