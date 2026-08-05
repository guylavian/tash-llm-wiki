---
title: "Exchange Online MX Record *.mail.protection.outlook.com security default and hardening best practice?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1014810/exchange-online-mx-record-*-mail-protection-outloo
question_id: 1014810
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# Exchange Online MX Record *.mail.protection.outlook.com security default and hardening best practice?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1014810/exchange-online-mx-record-*-mail-protection-outloo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

People,    

I need some guidance and explanation for the Exchange Online MX record email relay.    

My company is using EOP, hence the MX record is like the below:    

```
company-com.mail.protection.outlook.com  
domain1-com.mail.protection.outlook.com  
domain2-net.mail.protection.outlook.com  
...
```

When I am at the internet cafe and on the outside network, I can perform send email relay to *@mathieu.company  .com, *@domain1.com and domain2.net from random.address@whatever  .com using simple scripting and any method which can take SMTP anonymously.    

All of the inbound email relays using the above MX records are successful and NOT quarantined nor rejected.    

Is this the default behaviour or something must be done to secure this loophole?    

I look forward to your reply.

## Answers

_No answers on this thread._
