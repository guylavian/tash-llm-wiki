---
title: "Exchange 2019 Hybrid Configuration wizard timeout error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1687837/exchange-2019-hybrid-configuration-wizard-timeout
question_id: 1687837
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Hybrid Configuration wizard timeout error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1687837/exchange-2019-hybrid-configuration-wizard-timeout (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to setup hybrid Exchange between my Exchange 2019 server and Microsoft. I'm using the Exchange server for a grand total of two email addresses (different domains), both to the same AD user (me). I'm migrating one domain to make sure everything works, then will add the second domain. My Exchange server is sitting behind NAT with appropriate DNS entries to my Cisco router and it works as expected by itself. I am using Let's Encrypt certificates but am on a residential internet service, so Spamhaus flags me as inappropriate, which means a lot of my emails don't get delivered. My hope is that once the hybrid setup is complete that issue will go away since the MX records will point to MS servers. I've gone through the configuration without issue until I run the hybrid configuration wizard, which fails in the verify stage with this error:

2024.05.25 03:28:53.295 ERROR 10349 [Client=UX, Page=HybridConnectorInstall, Thread=19] The connection to the server '<GUID>.resource.mailboxmigration.his.msappproxy.net' could not be completed., The call to '<GUID>.resource.mailboxmigration.his.msappproxy.net/EWS/mrsproxy.svc' timed out. 

Nothing seem amiss, except the MSAPProxy times out. I assume there is something on my end it doesn't like, so just ignores me. :( Has anyone got ideas on where I go from here?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-05-27*

Hi @Bill Seymour,

Thank you for posting to Microsoft Community.

Based on your description, I understand you got an error in “Validating Hybrid Agent” page.

I suggest you could try the following to troubleshoot.

-  Check whether TLS 1.2 is enabled.

-  Please disabled and enabled MRS option and then restarted IIS to take the action effective.

-  Enable basic authentication on Web Services Virtual Directory by the following command:  Set-WebServicesVirtualDirectory -Identity "Server\EWS (default Web site)" –BasicAuthenticaition $true

-  Check proxy and firewall settings and ensure your firewall settings to allow connections from O365. You can refer to Microsoft 365 URLs and IP address ranges - Microsoft 365 Enterprise | Microsoft Learn for more information.

-  You could refer to the requirements part of The Microsoft Hybrid Agent Public Preview - Microsoft Community Hub to make sure it is configured correctly.

Also, please check if Exchange Server Extended Protection was turned on, try to turn Extended Protection OFF in IIS (EWS) to see if it works. You could refer to Exchange Server support for Windows Extended Protection | Microsoft Learn for more information.

Hope it helps and if there are anything else you need help, please feel free to contact me.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-05-27*

The error message indicates a timeout when trying to connect to '<GUID>.resource.mailboxmigration.his.msappproxy.net'.

Here are a few troubleshooting steps you can try:

-  Ensure that there are no network issues preventing your Exchange server.

-  Check if no firewall rules or network configurations blocking the connection.

-  Double-check your DNS settings to ensure that the Exchange server can resolve the hostname '<GUID>.resource.mailboxmigration.his.msappproxy.net' correctly.  

-  Verify that your Let's Encrypt certificate is properly configured and trusted by all parties involved.
