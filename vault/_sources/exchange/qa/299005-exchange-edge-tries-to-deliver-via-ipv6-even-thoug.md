---
title: "Exchange EDGE tries to deliver via IPv6 even though it is disabled"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/299005/exchange-edge-tries-to-deliver-via-ipv6-even-thoug
question_id: 299005
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange EDGE tries to deliver via IPv6 even though it is disabled

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/299005/exchange-edge-tries-to-deliver-via-ipv6-even-thoug (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have on-premise Exchange deployment with EDGE server delivering email. The IPv6 has been disabled all along via Registry key. More and more local small companies are implementing IPv6 addressing and for some reason my EDGE server is trying o connect via IPv6 and can't, email goes to queue and sits there. If I tried to Retry email from the queue it get delivered via IPv4. Why is this happening?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-07*

Yes, it is set to use MX record.  

SourceIPAddress              : 0.0.0.0

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-05*

Hi @Mr Mind   ,    

Have you checked the settings on the Connectors of Edge?     

Also are you using the MX record or Smart host to route?     

You can use the following command to check the IPAddress in using by your Edge send connector.    

```
Get-SendConnector -Identity "EdgeSendConnectorName" | FL Name,SourceIPAddress
```

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
