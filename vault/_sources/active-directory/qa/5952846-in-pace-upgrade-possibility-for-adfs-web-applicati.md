---
title: "In-pace upgrade possibility for ADFS Web application proxy servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5952846/in-pace-upgrade-possibility-for-adfs-web-applicati
question_id: 5952846
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# In-pace upgrade possibility for ADFS Web application proxy servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5952846/in-pace-upgrade-possibility-for-adfs-web-applicati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am writing to know regarding the possibility on in-place upgrade of ADFS Web application proxy servers from Windows 2016 to 2025.  

I can provide the details required, these servers are not domain joined, are in DMZ, no external application URL published on Remote Access console.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-07-21*

Yes. An in-place upgrade path from Windows Server 2016 to Windows Server 2025 is supported for nonclustered systems.

For Web Application Proxy specifically, after the AD FS farm behavior level is updated, Web Application Proxy must be upgraded to the latest level. The documented post-upgrade steps are:

-  Sign in to the Web Application Proxy server and open an elevated PowerShell session.

-  Import the federation certificate and note its thumbprint.

-  Reconfigure WAP by running:

```
$trustcred = Get-Credential -Message ""
   Install-WebApplicationProxy -CertificateThumbprint "" -FederationServiceName "" -FederationServiceTrustCredential $trustcred
```

-  Review connected WAP servers:

```
Get-WebApplicationProxyConfiguration
```

-  If older WAP servers remain, remove them from the connected server list and keep only the upgraded servers:

```
Set-WebApplicationProxyConfiguration -ConnectedServersName "WAPServerName1", "WAPServerName2"
```

-  Upgrade the WAP configuration version:

```
Set-WebApplicationProxyConfiguration -UpgradeConfigurationVersion
```

If building a replacement server instead of upgrading in place is preferred, Web Application Proxy can also be installed and configured fresh by adding the Remote Access role and Web Application Proxy role service, then running the Web Application Proxy Configuration Wizard in the Remote Access Management console.

Because these servers are in a DMZ and not domain joined, the documented WAP configuration model still applies: configuration is done against the AD FS federation service using the federation service name, certificate, and administrator credentials.

References:

-  Plan your Windows Server upgrade

-  Upgrade an existing AD FS farm by using Windows Internal Database

-  Upgrade to AD FS in Windows Server 2016 with SQL Server

-  Upgrading AD RMS to Windows Server 2016
