---
title: "exchange send to different smart host by \"sender domain\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/190261/exchange-send-to-different-smart-host-by-sender-do
question_id: 190261
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# exchange send to different smart host by "sender domain"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/190261/exchange-send-to-different-smart-host-by-sender-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

halo,  

I wondering can I send to different smart host depending on the sender domain?  

I have 2 exchange servers and all in the same site. ad we got 2 domain name a.com and b.com  

I want the email send from A.com will via smart A  (or boardband A).  

email from B.com will go to smart host B (or boardband B).  

can I ?   

PS: since all the exchange servers in the same site, we can't use the "send connector scope" option the control the mail flow.   

thx

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-09*

tons of thanks! I am clear the whole picture now, I will report to my boss and let him make the decision.  

 thanks again

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-08*

hey Ashok,    

thanks for your reply, do you remember couple weeks ago you answered a question about send connector :)    

https://learn.microsoft.com/en-us/answers/questions/151065/question-about-exchange-send-connector.html    

according to that, if I separate the domain in 2 AD site, a.com put in site A subnet, and B.com put in Site B.    

and all the users using ******@a.com put on the mailbox DB which located in server A. same to B.    

and I create 2 scoped send connector.     

Can that able to achieve the my purpose?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-08*

Hi,  

To my knowledge, there is no option to configure sender based routing in Exchange. However, it can be achieved by using 3rd party Transport agents or custom agents.  

https://jaapwesselius.com/2018/04/19/source-based-routing-in-exchange/  

https://support.appriver.com/kb/a1074/setting-up-sender-based-routing-for-exchange-2013-2016.aspx  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.  

If the above suggestion helps, please click on Accept Answer and upvote it.
