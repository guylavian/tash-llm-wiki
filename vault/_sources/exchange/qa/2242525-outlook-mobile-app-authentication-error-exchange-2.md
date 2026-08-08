---
title: "Outlook Mobile App authentication error Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2242525/outlook-mobile-app-authentication-error-exchange-2
question_id: 2242525
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Outlook Mobile App authentication error Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2242525/outlook-mobile-app-authentication-error-exchange-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On premise Exchange 2019. Self-signed certificate.

I had to renew my self-signed certificate.

The old self-signed certificate originated from an Exchange 2016 server. This certificate worked ok on my Exchange 2019 server. I had to make a new Exchange 2019 server due to reasons and it continued to use the old self-signed certificate but I am not sure if new Outlook app accounts were created in the few months between the new server going into service and the new certificate being created on the new server.

However, the new certificate broke adding accounts to mobile Outlook apps.

Existing accounts in Outlook apps were grandfathered in and continue to work fine.

Is this entirely because of the self-signed certificate or is there something else that I can try?

The old Exchange 2019 server is still not fully decommissioned but is usually powered off. Powering it back on does not fix the issue.

Is there a setting on my new Exchange 2019 server I need to check? 

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-10*

The issue you're experiencing with mobile Outlook apps failing to add new accounts (while existing ones continue to work) is likely related to certificate trust and authentication configuration on your new Exchange 2019 server. Here are the key things to check and potential solutions:

1. Certificate Issues (Most Likely Cause)

-  Self-signed certificates are not trusted by mobile devices by default

-  Even if you installed the certificate on the devices, some mobile email clients (especially Outlook for iOS/Android) may still reject it

-  Solutions:

-  Obtain a publicly trusted certificate from a CA (DigiCert, GoDaddy, Let's Encrypt, etc.)

-  Ensure the certificate includes all necessary SANs (autodiscover.domain.com, mail.domain.com, etc.)

-  If you must use self-signed, ensure it's properly installed on all mobile devices

2. Autodiscover Configuration

-  Verify your Autodiscover service is properly configured on the new server

-  Check with the Microsoft Remote Connectivity Analyzer: https://testconnectivity.microsoft.com

-  Ensure DNS records point to the new server (especially autodiscover.domain.com)

3. Authentication Settings

-  Mobile Outlook uses Modern Authentication (OAuth 2.0) by default

-  Verify Modern Authentication is enabled:

```
Get-OrganizationConfig | fl OAuth*
```

  (Should show OAuth2ClientProfileEnabled as True)

4. Virtual Directory URLs

-  Check your internal/external URLs match your certificate:

```
Get-WebServicesVirtualDirectory | fl InternalUrl,ExternalUrl

  Get-OABVirtualDirectory | fl InternalUrl,ExternalUrl

  Get-ActiveSyncVirtualDirectory | fl InternalUrl,ExternalUrl

  Get-ECPVirtualDirectory | fl InternalUrl,ExternalUrl
```

5. Old Server Artifacts

-  Even powered off, if the old server's records still exist in AD, it could cause issues

-  Run `Get-ExchangeServer` to verify only your new server appears as valid

Immediate Workaround:

If you need a temporary fix before getting a proper certificate, you can try:

-  On the mobile device, try adding the account manually (skip Autodiscover)

-  Use the Outlook app's "Advanced Settings" to accept the untrusted certificate

-  For testing, you could temporarily enable Basic Authentication (not recommended long-term)

The most reliable solution is to obtain a proper certificate from a trusted CA. Self-signed certificates will continue to cause problems with mobile clients, especially newer versions of Outlook for iOS/Android.

If my above response helps, you may share your vote so more users can find useful information on your case url

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-01*

Hi,@Susan Dodds

Thanks for posting your question in the Microsoft Q&A forum.

Based on your description, it appears that your new Exchange 2019 server is not binding the certificates correctly.

Are you using a self-signed certificate? As I understand it, self-signed certificates are automatically created when you deploy Exchange2019. You can refer to this link for details:https://learn.microsoft.com/en-us/exchange/architecture/client-access/certificates?view=exchserver-2016#certificates-in-exchange

If you want to use mobile Outlook to sign in to Exchange2019, it is recommended that you use an on-premises CA certificate as a minimum.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
