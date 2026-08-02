---
title: "Microsoft Exchange 2019 Hybrid - Cannot send email after two days setup (Azure VM)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1243409/microsoft-exchange-2019-hybrid-cannot-send-email-a
question_id: 1243409
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Microsoft Exchange 2019 Hybrid - Cannot send email after two days setup (Azure VM)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1243409/microsoft-exchange-2019-hybrid-cannot-send-email-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,
I have 2 VMs in Azure with no Enterprise Agreement.
One for Active Directory and one for Exchange Server.
&. I have M365 Organization with E3 & E5 subscription for my users.
based on Microsoft's post, my subscription have the port blocked to send emails.
that is why I setup 3rd party SMTP relay, in this case, I want to use M365 SMTP to send emails.
The first day, all users in my organizationn are able to send emails.
The next day and the rest, only the user that being the connector can send the email.
Can you please tell me why?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-18*

Hello there,
Exchange Online will grey list and back off connections it hasn't seen before in some cases. Especially if they are "spammy" in nature. Usually, after that initial back off period or when a contact is placed to Microsoft, EOP will allow these and they will go through. 
If this is something that just started occurring, then you can removing and re-adding the send/receive connector. 
This also occurs if the domain that's set up in the hybrid deployment isn't set as an internal relay domain in Microsoft 365. To fix this issue, set up the domain as an internal relay domain
https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/on-premises-users-not-getting-emails-from-microsoft-365

Hope this resolves your Query !!
--If the reply is helpful, please Upvote and Accept it as an answer--
