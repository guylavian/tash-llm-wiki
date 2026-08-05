---
title: "OpenID Connect 1.0 authentication - SharePoint Server"
type: reference
domain: sharepoint
slug: security-for-sharepoint-server-oidc-1-0-authentication
tier: reference
source: https://learn.microsoft.com/en-us/sharepoint/security-for-sharepoint-server/oidc-1-0-authentication
family: security-for-sharepoint-server
documentKind: "article"
abstract: "Learn how to set up OIDC authentication in SharePoint Server."
---

# OpenID Connect 1.0 authentication - SharePoint Server

Note

OpenID Connect 1.0 authentication

# OpenID Connect 1.0 authentication

**APPLIES TO:** 2013 2016 2019 Subscription Edition SharePoint in Microsoft 365

OpenID Connect (OIDC) 1.0 is a modern authentication protocol that seamlessly integrates applications and devices with identity and authentication management solutions to keep pace with the evolving security and compliance needs of your organization.

In SharePoint 2019 and prior versions, SharePoint Server supported three types of authentication methods:

- Windows authentication (New Technology LAN Manager (NTLM), Kerberos, etc.)

- Forms-based authentication

- Security Assertion Markup Language (SAML) 1.1-based authentication

OIDC 1.0 authentication protocol only supports SharePoint Server Subscription Edition. With this capability, you can set up an OIDC-enabled `SPTrustedIdentityTokenIssuer` that works with a remote identity provider to enable OIDC authentication.

The OIDC 1.0 authentication protocol integrates with SharePoint Certificate Management to manage the nonce (number used once) cookie certification. The nonce cookie certificate ensures that OIDC authentication tokens are secure.

Prior to OIDC 1.0 authentication integration with SharePoint Certificate Management, the administrators used the Certificate snap-in in Windows to check the status of the nonce certificate. In a multi-server farm, the administrators needed to manually export certificates, import certificates, and grant permissions on each server individually. When administrators enable OIDC for a new web application using a new application pool account, the administrators had to remember to grant permissions for the account.

Farm administrators can use the following command to establish or replace the nonce certificate at the farm level. This command can be used regardless of the fact if it's being done during the initial configuration or during replacement of an existing nonce certificate.

```
# Use one of the commands to acquire the nonce cookie certificate if it's already imported:
$nonceCert = Get-SPCertificate -DisplayName <the certificate name>
$nonceCert = Get-SPCertificate -Thumbprint <thumbprint>

# Update
$farm = Get-SPFarm 
$farm.UpdateNonceCertificate($nonceCert, $true)
```

You can set up OIDC authentication in SharePoint Server with either of these options:

Microsoft Entra ID. For more information, see Set up OIDC authentication in SharePoint Server with Microsoft Entra ID.

Active Directory Federation Services (AD FS). For more information, see Set up OIDC authentication in SharePoint Server with Active Directory Federation Services (AD FS).

Additional resources

## Additional resources

- Last updated on 
		2024-03-12
