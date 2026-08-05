---
title: "Exchange Online connectors"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1435504/exchange-online-connectors
question_id: 1435504
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online connectors

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1435504/exchange-online-connectors (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After some clarification how the inbound connectors in EXO work.  In the tenant I am looking at there are several inbound connectors, including one from an on-prem relay.

One of them (the main filter service) the setting is "Reject messages if they don't come from this IP"

I am trying to test direct submission from another source but it gets rejected, presumably because of that setting. But I am unclear the processing order of these connectors, they still work even though one of them explicity says reject if not from this IP?  

I am trying to test direct submission because we are planning on removing this 3rd party filter and use only Defender for spam analysis, but currently, I can't bypass the existing MX record by submitting directly to  

company-com-au.protection.outlook.com

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-23*

Hi @Bob Pants  ,

Welcome to our Q&A forum!

The processing order of connectors is based on the corresponding priority parameter value in PowerShell or the order listed on the Mail flow > Rules page in Exchange Admin Center. Each rule also offers the option of stopping processing more rules when the rule is matched.

Regarding your specific issue, it’s possible that the connector with the “Reject messages if they don’t come from this IP” setting has a higher priority than the other connectors, which is why your direct submission from another source is getting rejected. You can try changing the priority of the connectors to see if that resolves the issue.

https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/use-connectors-to-configure-mail-flow

Please feel free to let us know if there are any other questions.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
