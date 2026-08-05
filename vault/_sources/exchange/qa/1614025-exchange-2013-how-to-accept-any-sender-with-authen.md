---
title: "Exchange 2013: How to accept any sender with authenticated relay connector?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1614025/exchange-2013-how-to-accept-any-sender-with-authen
question_id: 1614025
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013: How to accept any sender with authenticated relay connector?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1614025/exchange-2013-how-to-accept-any-sender-with-authen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an Exchange 2013 server on-premise which has to be kept up for a little while longer until fully having phased out some old mailboxes. Until recently we used an external Mail Gateway with it but now it handles spam filtering and spoofing protection on its own. The thing is: Since Sender ID is turned on, it cannot be used as an anonymous relay by our internal ERP host to send out mails any longer. That's because the ERP uses external sender addresses which of course don't pass SPF checking when being sent from an internal host inside the local network. Now, I thought of two viable options here:

-   Excluding SMTP connections from the local ERP host from being Sender ID checked. Unfortunately, I haven't found any way to do so. The only option I found is to exempt the sender domains from Sender ID checks but that would also facilitate spoofing of those domains.

-  Switching from anonymous to authenticated relay. Then, Sender ID would not be checked. Problem is: I cannot get it to allow arbitrary sender addresses. The connector always responds with 

5.7.1 Client does not have permissions to send as this sender

That is despite setting the same ExtendedRights to the respective user that are set to NT AUTHORITY\ANONYMOUS LOGON which are

ms-Exch-SMTP-Accept-Any-Sender
ms-Exch-SMTP-Accept-Any-Recipient
ms-Exch-SMTP-Accept-Authoritative-Domain-Sender
ms-Exch-Accept-Headers-Routing
ms-Exch-SMTP-Submit
ms-Exch-Store-Create-Named-Properties
ms-Exch-Create-Public-Folder

Additionally, I added the external sender address to the user's proxyAddresses property like so:

SMTP:******@external-domain.com

Still, it won't let me do it. However, it works using a Domain Admin account and then there is also the fact that it works anonymously with the permissions of NT AUTHORITY\ANONYMOUS LOGON (which is not an option because then would be Sender ID checking).

What additional settings/permissions are required for a user to be able to send mails using any sender address?

In case it is not possible to send mail using any sender address as authenticated user, is there any way to bypass Sender ID for SMTP sessions originating from a specific host which is on the same local network as the Exchange Server?

Edit: I could add an SPF record allowing the ERP host's IP address for every external sender domain to the domain's local DNS server to get around the Sender ID problem when using an anonymous relay. But that seems kind of messy and I'd like to avoid it.

## Answer (community) — community member

*upvotes: 1 · updated: 2024-03-12*

Found it:

It was necessary to set "Externally secured (for example, with IPSec)" as Authentication and "Exchange Servers" as Permission group for the connector. Sender ID will then not be checked by this connector using it either anonymously or authenticated.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-12*

Hi @SAMFS,

If you cannot send anonymously as ERP host, would it be possible to create an account for the ERP host on Exchange, then authenticate and send as that account to bypass Gateway check?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
