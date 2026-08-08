---
title: "Messages dropped from on-prem Exchange to Office 365 when on-prem IP is blacklisted"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/258713/messages-dropped-from-on-prem-exchange-to-office-3
question_id: 258713
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Messages dropped from on-prem Exchange to Office 365 when on-prem IP is blacklisted

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/258713/messages-dropped-from-on-prem-exchange-to-office-3 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a hybrid Exchange setup where the on-prem Exchange is on a connection with dynamic IP. The ISP did an upgrade and I got a new IP address which was blacklisted. The result was that the on-prem server receives the email, which results in the sender being satisfied the mail is sent and received. However, when the local server tries to forward the email to Office365 the email is dropped and I can see the status FAIL in the message tracking log. The end result is that the email will never arrive in the recipients mailbox and the sender will not resend.  

Is there a way to avoid this behavior? Is there some way to tell Office 365 to accept incoming emails from my on-prem server, even if the IP is blacklisted?  

Or, as an alternative, is there a way to let these messages stay in the queue on the on-prem server until the IP issue is fixed and Office 365 will accept them? Right now they are dropped at once, never to be seen again.  

PS! I know all the reasons why I shouldn't use dynamic IP and hybrid, but that is not part of the question.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-17*

"PS! I know all the reasons why I shouldn't use dynamic IP and hybrid, but that is not part of the question."  

Sometimes the answers are not technical... If you know you are doing something the wrong way, and it's causing you grief, isn't it easier to just do it the right way?  

Aside from many RBL's blocking dynamic public address pools, you need reverse PTRs and other features not available with dynamic IP's for headache free SMTP transmission.   

-Miguel Fra  

https://www.falconitservices.com

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-04*

Ok, well, if you are using a dynamic IP, then you are stuck  :)  

I know its not part of what you are asking, but ---really it is. Using a Dynamic IP simply is not something that should be used for this architecture.
