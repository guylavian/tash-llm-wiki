---
title: "Block external access to ECP and OWA while still allowing inbound certificate checks to work."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/337931/block-external-access-to-ecp-and-owa-while-still-a
question_id: 337931
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Block external access to ECP and OWA while still allowing inbound certificate checks to work.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/337931/block-external-access-to-ecp-and-owa-while-still-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need to block external access to ECP and OWA for my Exchange 2016 box.  I have seen the other forums posts about this but my issue is slightly different.  

I thought I could do this at my firewall level by not allowing inbound 443 to my Exchange box.  I have a firewall rule for this and I set the action to disable.  

This definitely works but it ends up causing problems with my 3rd party mail certificate.     

(I dont fully understand this next part so I hope my details are accurate)  

When port 443 traffic is NOT allowed to my inbound mail server then I start having problems with my 3rd party mail certificate.    

Example: I use the digicert mail certificate checker at https://www.digicert.com/help as a test.  When port 443 is forwarded to my mail server then this cert check is successful with no errors.     

When port 443 is NOT forwarded to the mail server then this certificate checker fails.   My firewall vendor states since  we do not have a rule in place that forwards 443 traffic then the firewall offers up  

a different certificate for this checker which causes the failure as the domain names do not match.  

So, if I disable 443 inbound it fixes my goal of blocking ECP and OWA but then causes certificate issues.  

Any suggestions?

## Answers

_No answers on this thread._
