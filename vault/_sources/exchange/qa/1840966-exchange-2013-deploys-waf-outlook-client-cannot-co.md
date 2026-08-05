---
title: "Exchange 2013 deploys WAF, Outlook client cannot connect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1840966/exchange-2013-deploys-waf-outlook-client-cannot-co
question_id: 1840966
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 deploys WAF, Outlook client cannot connect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1840966/exchange-2013-deploys-waf-outlook-client-cannot-co (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Exchange 2013 deploys WAF, Outlook client cannot connect，other clients are ok.error:RPC server unavailable

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-26*

Hi,

Welcome to the Microsoft Q&A forum!

The "RPC server unavailable" error can stem from a variety of causes, including network configuration, firewall settings, or RPC service issues.

Ensure the RPC proxy component on the Exchange server is properly configured. You can verify this in the Exchange Management Shell with the following commands:

```
Get-OutlookAnywhere 
Get-ClientAccessServer | fl
```

Ensure the "Microsoft Exchange RPC Client Access" service is running on the Exchange 2013 server. - You can restart the service to see if it resolves the issue: 

```
Restart-Service MSExchangeRPC
```

RPC over HTTP, which was not supported by WAF 2.2.0.0-12waf and earlier. So, you can check this also.

More details you can refer to:https://www.sonicwall.com/support/knowledge-base/waf-common-configurations-for-securing-owa-activesync-and-outlook-anywhere-to-access-exchange-mailbox/181218235648455/

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.
