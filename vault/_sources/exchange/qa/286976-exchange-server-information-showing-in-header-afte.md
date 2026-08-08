---
title: "Exchange server information showing in header after removing the ms-Exch-Send-Headers-Routing in the send connector"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/286976/exchange-server-information-showing-in-header-afte
question_id: 286976
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange server information showing in header after removing the ms-Exch-Send-Headers-Routing in the send connector

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/286976/exchange-server-information-showing-in-header-afte (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

In the send connectors, removing the 'ms-Exch-Send-Headers-Routing' extended rights for NT AUTHORITY\ANONYMOUS LOGON still gives the exchange server information in HELO.    

Please see the attached.    

Though hostname shows as unknown and Exchange server is showing in HELO.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-10*

Have a look at this tool: HeaderRewriter for Microsoft Exchange 2013/2016/2019.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-25*

You can compare the header result with an old message header result that ms-Exch-Send-Headers-Routing has not been removed on connector.    

Removing ms-Exch-Send-Headers-Routing will hide your internal ip address and internal host name from the header, you can see the whole testing process in this blog: https://www.alitajran.com/remove-message-header-in-exchange-server/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-24*

That's expected.  Removing that permission "Controls the preservation of RECEIVED headers in messages. If this permission isn't granted, all received headers are removed from messages." When you send the message externally, that last hop is not your org receiving it, its the recipient's org.    

https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/send-connectors?view=exchserver-2019    

The header stamp showing the receiving connection between the Exchange Server and a receiving external server is not something you can control.    

You can also clear the FQDN on the send connector, but I wouldnt do that. It should match a subject name on a certificate bound to SMTP and you could get mail rejected that you sending.
