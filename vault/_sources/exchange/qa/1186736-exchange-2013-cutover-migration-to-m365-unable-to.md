---
title: "Exchange 2013 Cutover Migration to M365 - unable to create migration endpoint in M365, .local AD domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1186736/exchange-2013-cutover-migration-to-m365-unable-to
question_id: 1186736
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 Cutover Migration to M365 - unable to create migration endpoint in M365, .local AD domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1186736/exchange-2013-cutover-migration-to-m365-unable-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

- 

-  On-prem Exchange 2013 CU23 + all patches, on Server 2012 R2

-  On-prem Windows domain is company.local, Exchange server hostname is srv.company.local

-  Public/external domain is company.com. The server has a valid wildcard cert for *.company.com. External DNS is configured so the server can be reached at mail.company.com on port 443

-  All Exchange virtual directory external URLs are configured to point to mail.company.com as the FQDN

Trying to create a migration endpoint in M365 for a cutover migration fails with a message "Error creating endpoint. We weren't able to connect to the remote server. Please verify the migration endpoint settings are correct...". It suggests using the Exchange Remote Connectivity Analyzer (ExRCA). That has interesting results. Testing done against "Exchange Server...Outlook Connectivity" option (as cutover migration appears to require Outlook Anywhere):

ExRCA using default AutoDiscover: connectivity test failed:

-  Testing RPC over HTTP connectivity to server srv.company.local

-  Host srv.company.com couldn't be resolved in DNS InfoDomainNonexistent

This is somewhat expected, because AutoDiscover.xml points in many places to srv.company.local.

ExRCA using manually specified server settings: Connectivity test successful with warnings:

-  RPC proxy server: mail.company.com

-  Exchange server: srv.company.local

-  Mutual authentication principal name: <blank>

-  RPC proxy authentication method: Ntlm

The warnings were about validating the cert using Root Certificate Update functionality from Windows Update, and testing the MAPI Referral Service on the Exchange Server (not sure if this is needed for a cutover migration (?))

When trying to create the migration endpoint in M365, it looks up server information based on the test mailbox address, presumably using AutoDiscover to start. This is not auto-filled, it comes up blank. However, there's the opportunity to enter the same Exchange server hostname and RPC proxy server hostname as in the ExRCA test. The same mailbox and AD user credentials were used for the endpoint and in ExRCA.

One thing I tested was enabling the MRSProxy in the EWS virtual directory. This made no difference to the inability to create the migration endpoint. I'm not sure if this needs to be enabled for a cutover migration, it seems to be related to mailbox move functions (correct me if I'm wrong).

Conceptually the simplest solution is to get autodiscover.xml to return mail.company.com instead of srv.company.local but I have zero idea how to do that - it may be generated (?)

Alternately, if there's some other setting needed on-prem to get the M365 migration endpoint to be accepted, that would be great.

Thanks for taking the time to go through all this.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-15*

Thanks for your suggestions. It turns out this is a bug/inconsistency in the web-based Exchange Admin Center.

Our on-prem server passes migration endpoint availability testing:

-  In Exchange Remote Connectivity Analyzer (ExRCA) https://testconnectivity.microsoft.com/tests/o365

-  In Exchange Online PowerShell (ExOPS) using the Test-MigrationServerAvailability cmdlet

However, trying to create a new migration endpoint as part of creating a new migration batch in the web UI fails, even when using the exact same parameters as the successful tests above.

For now, the workaround is to use ExOPS and the New-MigrationEndpoint cmdlet. This allows an endpoint to be created with the proper parameters. Then, when creating a new migration batch in the web UI, this pre-existing endpoint can be selected rather than creating a new one on the fly, thus sidestepping the web UI issue.

I've been working on this in parallel with M365 Exchange Online migration support and they've validated my findings. The support ticket is 35029447 if either of you can access it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-13*

Please describe in detail which test you have performed using the RCA. Select Exchange Server -> Microsoft Office Outlook Connectivity Tests -> Outlook Autodiscover to run the test.

Besides, please refer to Perform a cutover migration of email to Office 365 and make sure you have done everything under the Prepare for a cutover migration section.

And if the Autodiscover is OK and all those preparations are done, but the issue persists, I suspect network factors could be the cause. If you have any firewall settings, please try temporarily bypassing it at an off-work hour to see if the issue is gone.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-03-07*

Hi @ Al Doman ，

Error creating endpoint. We weren't able to connect to the remote server. Please verify the migration endpoint settings are correct.

For this error, please follow these steps to verify that the configuration is correct:

1. Make sure that the RPC proxy server is correctly set up to use specific ports to communicate with Outlook Anywhere and that the on-premises domain controllers are listening on port 6004.

2. Make sure that the RPC proxy server is correctly set up to use specific ports to communicate with Outlook Anywhere and that the on-premises domain controllers are listening on port 6004.

-  Verify Outlook Anywhere connectivity to the on-premises Exchange server. 

```
$pscred=Get-Credential

Test-MigrationServerAvailability -Credentials $pscred -ExchangeOutlookAnywhere -ExchangeServer  -RPCProxyServer  -Authentication Basic -EmailAddress 
```

Please refer to this link for more information：We weren't able to connect to the remote server error - Exchange | Microsoft Learn

 

If you are still unable to create an endpoint after performing the above steps, can you post a screenshot of the ExRCA test after anonymizing your personal information for us further research and troubleshooting?

Thank you for your patience and understanding~

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
