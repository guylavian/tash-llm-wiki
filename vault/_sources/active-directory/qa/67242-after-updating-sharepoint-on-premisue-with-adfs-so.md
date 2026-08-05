---
title: "After updating SharePoint On-Premisue with ADFS some users can't work because of old Auth-Cookie (MSIS7042)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/67242/after-updating-sharepoint-on-premisue-with-adfs-so
question_id: 67242
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# After updating SharePoint On-Premisue with ADFS some users can't work because of old Auth-Cookie (MSIS7042)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/67242/after-updating-sharepoint-on-premisue-with-adfs-so (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We already made a few updates from SharePoint 2013 to 2016 or 2019 successfully. When using ADFS-Authentication and preserving the same SiteCollection-URL on the new SharePoint Server, some users may still have an Authentication-Cookie for the URL but they can't work anymore with the new SharePoint until they logout from ADFS and login again (either via Logout-Link https://adfsurl/adfs/ls/?wa=wsignout1.0 or by deleting all Browser-Cookies). The detailed error in ADFS is: `Microsoft.IdentityServer.Web.InvalidRequestException: MSIS7042: The same client browser session has made '6' requests in the last '1' seconds.`  

We never expecience such issues in production since years, but just when updating/moving the SiteCollection to a new SharePoint server. So I think this is not a general configuration-issue but has to do with the actual SharePoint-Server-Upgrade and outdated/obsolete user-cookies.  

What can we do to prevent this issue when performing a SharePoint-Update?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-06-03*

It looks like an existing the FedAuth cookie remains in the Browser for a few days (CookieLifetime default is 5 days). Because of this, no new FedAuth cookie is issued by SharePoint STS.

I didn't find any way to export the STS Signing Certificate ("SharePoint Root Authority"?) with the private key.

Changing the ADFS realm didn't fix this nether.

I found a workaround: Change the FedAuth Cookie name. It will issue a new FedAuth-Cookie, that works side by side. Example in web.config:

```

```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-17*

This issue is more related to lifetime of tokens. You could change the LogonTokenCacheExpirationWindow to be less than the SAML TokenLifetime by the PowerShell command.  

```
$sts = Get-SPSecurityTokenServiceConfig
$sts.LogonTokenCacheExpirationWindow = (New-TimeSpan –minutes 1)
$sts.Update()
iisreset
```

For more detailed information, you could refer to the article below.  

The same client browser session has made '6' requests in the last '11' seconds.
