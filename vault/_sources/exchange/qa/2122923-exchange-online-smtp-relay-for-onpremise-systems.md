---
title: "Exchange Online - SMTP Relay for Onpremise Systems"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2122923/exchange-online-smtp-relay-for-onpremise-systems
question_id: 2122923
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online - SMTP Relay for Onpremise Systems

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2122923/exchange-online-smtp-relay-for-onpremise-systems (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone, Since Microsoft has announced that it will soon deactivate the legacy SMTP protocol (including SMTP authentication), I am faced with the question of how on-premise systems can continue to send emails. Specifically, the situation is as follows: An on-premise server uses an IIS SMTP relay that currently works with SMTP authentication. This method will no longer work after the legacy SMTP protocol is deactivated. I have heard of Azure Communication Services, which supports OAuth, but this is not compatible with old systems that do not support OAuth. My question: What solution does Microsoft recommend for on-premise systems that still need to send emails via a relay when SMTP auth is no longer available? Is there an alternative that is both secure and suitable for older systems? Thank you in advance for your support!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-27*

Hi Xintao Qiao,

many thanks for your Reply.

so the only secure ways would be option 3 or 4.

In conclusion, either we use the Hybrid setup (relay over onprem Exchange) or we use OAuth if possible. Is there anything planed for Environments who dont support OAuth if no Onprem Exchange is available as SMTP is soon decommissioned? I Guess the Option 1 with the Exchange Connector is not the best choice as it doesnt need any authentication.

Best Regards

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-26*

Hi, @SQIT  

With the imminent retirement of legacy SMTP protocols, including SMTP authentication, you will need to look for alternative ways to enable your on-premises systems to continue sending email securely. Here are some suggestions that may help:

-  You can configure your local system to use Office 365's SMTP trunk. This method allows you to send emails without using SMTP authentication.

-  For clients that still require legacy SMTP, you can opt in to Exchange Online endpoints to support legacy TLS clients that use SMTP AUTH.

-  If you have a hybrid setup of on-premises and cloud environments, you can take advantage of a hybrid configuration where email is routed through an on-premises Exchange server and then relayed by it to Office 365.

-  If you have any systems that can be updated or configured to use OAuth2, this should be your top consideration for modern and secure email communications.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
