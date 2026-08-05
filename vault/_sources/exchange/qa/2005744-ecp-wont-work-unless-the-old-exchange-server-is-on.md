---
title: "ECP won't work unless the old Exchange server is on."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2005744/ecp-wont-work-unless-the-old-exchange-server-is-on
question_id: 2005744
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# ECP won't work unless the old Exchange server is on.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2005744/ecp-wont-work-unless-the-old-exchange-server-is-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

All Exchange servers listed are Exchange 2019. 

Long story short, I have a single server environment.

Box A became unusable after a windows update made it so Microsoft Filtering Management Service would not start. No error besides it failed to start.

This caused me to throw together Box B in a hurry. Luckily, migration still works so I can save the mailboxes. 

However, when I switch my internal DNS (autodiscover and word.contoso.com) to the new box or disconnect Box A from the network, the ECP becomes unavailable on Box A, Box B, and any computer trying to access the ECP until I turn DNS back to Box A or put Box A back on the network.

I have it so internal and external URL's are the same. The URL's are the same on each box. This has worked going from 2013 to 2016 to 2019. 

What am I missing?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-28*

Hi, 

Did you check if the arbitration mailboxes were moved from Exchange 2016 to 2019? The ECP will not work until they are moved to the Exchange 2019.

https://www.alitajran.com/move-arbitration-mailboxes-in-exchange-server/

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-08-26*

Hi @Susan Dodds,

Welcome to the Microsoft Q&A platform!

It sounds like you are dealing with a complex issue involving your Exchange 2019 servers and DNS configurations. Here are a few steps you can take to troubleshoot and resolve the issue:

-  Ensure that the DNS records for autodiscover and the mail domain are correctly pointing to Box B. Check both internal and external DNS settings.

-  Verify the internal and external URLs configured for the Exchange services on Box B. You can do this using the following PowerShell commands on Box B:

```
Get-ExchangeServer | fl AutoDiscoverServiceInternalUri Get-WebServicesVirtualDirectory | fl InternalUrl,ExternalUrl Get-OwaVirtualDirectory | fl InternalUrl,ExternalUrl Get-EcpVirtualDirectory | fl InternalUrl,ExternalUrl
```

   Ensure that the URLs are correctly set to the new Box B server's address.

-  Check the health of relevant services on Box B. Ensure that all necessary Exchange services are running:

```
Get-Service | Where-Object {$_.DisplayName -like "*exchange*"} | Select-Object DisplayName, Status
```

-  Ensure that the SSL certificates are properly configured on Box B. If the certificates are not correctly installed, the ECP might fail to load.

-  Verify the Outlook Anywhere settings and ensure they are set correctly for Box B:

```
Get-OutlookAnywhere | fl ExternalHostname, InternalHostname
```

-  Reset the ECP virtual directory on Box B if necessary. Sometimes, resetting the virtual directory can resolve issues with accessibility:

```
Remove-EcpVirtualDirectory -Identity "ServerName\ecp (Default Web Site)" New-EcpVirtualDirectory -Server "ServerName"
```

-  If you have a DAG setup or any form of mailbox replication, ensure that the databases are properly mounted and replicated on Box B.

-  Use the Exchange Remote Connectivity Analyzer (https://testconnectivity.microsoft.com/) to test the connectivity to Box B. This can help identify any issues with autodiscover or other services.

-  Double-check the network configuration and firewall settings to ensure there are no blocks or issues preventing proper communication with Box B.

Taking these steps should help you identify and resolve the issue with accessing the ECP on Box B after changing the DNS records.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang
