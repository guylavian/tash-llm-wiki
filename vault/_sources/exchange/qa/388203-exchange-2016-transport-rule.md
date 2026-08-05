---
title: "Exchange 2016 Transport Rule"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/388203/exchange-2016-transport-rule
question_id: 388203
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 Transport Rule

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/388203/exchange-2016-transport-rule (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Tech Community,  

I have Exchange 2016 CU 19 running on Windows 2012 R2. I have created an Transport Rule which rejects message "Reject the message with the enhanced status code" to any external sender trying to send to a particular internal recipient. The rule works the message is not delivered to internal recipient however the NDR is not delivered to external sender.  

I have checked the NDR setting for external domain and it is enabled:  

Get-RemoteDomain "Default" | fl NdrEnabled   

NDREnabled : True  

Can you please advise.  

Thank you  

b.l

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-05-11*

Dear ZhengqiLou,    

Thank you for you reply, my rule is exactly as yours, please find attached. I trayed in reverse for outbound email and it works as expected, however for inbound the external recipient is not getting any rejection message.    

    

Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2021-05-10*

Hi @Bujar Lushta   ,    

I've tried the transport rule and it worked as expected, the rule is:    

    

And the code is:    

    

Please first verify the rule you're in using, also make sure it's not reject by other rules. And them check the code and error text with:    

```
Get-TransportRule "RuleName" | FL *Reject*
```

Besides, you could try test the NDR by changing the rule's condition, like rejecting messages send from inside organization users to specific user. And please check if you could send emails to the external sender.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-14*

Hi ZhengqiLou-MSFT,  

Thank you for your reply.  

I tested the rule with outlook.com and gmail.com as well, I didn't receive any rejection message. It seems the problem is some ware else.  

b.l
