---
title: "Exchange Online - Route Email by Sender Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/364791/exchange-online-route-email-by-sender-domain
question_id: 364791
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Online - Route Email by Sender Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/364791/exchange-online-route-email-by-sender-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,  

We use a 3rd party cloud hosted email protection system that we use for our Exchange 2013 user base.  We just setup hybrid with Exchange Online and would like to start moving a set of our users to Exchange Online.  

The user base on Exchange 2013 uses domain.com while the user base located on Exchange Online uses a child domain of my.domain.com.  

Both domains are setup in O365 Admin Center.  

I have the following rule created but it seems like the "The sender's domain is..." setting includes both domain.com AND my.domain.com.  This caused ALL Exchange Online email to route out through our 3rd party cloud hosted email protection system.  

Then I added an Exception of "sender's address domain portion belong to": 'my.domain.com'.  

Name: Route domain.com to 3rd party cloud hosted email protection system  

If the message:  

sender's address domain portion belongs to any of these domains: 'domain.com'  

Take the following actions:  

Route the message using the connector named 'Outbound to 3rd Party Host Email Protection System'.  

Except if the message:  

Is sent to 'Inside the organization'  

or sender's address domain portion belongs to any of these domains: 'my.domain.com'  

This seems to work for the most part but the issue is if anyone with a my.domain.com account has forwarding enabled (which is alot), AND someone from the domain.com sends and email to them it will route out through our 3rd party email protection system.    

Is there a better way to create a rule to route Exchange Online users with domain.com outbound through our hosted email protect system AND have our child domain users of my.domain.com route out via O365?  

Thanks for any input!  

Ian...

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-27*

Have a look at RouteBySender tool.
