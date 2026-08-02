---
title: "How to Configure CBA for exchange 2019 on premise??"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196104/how-to-configure-cba-for-exchange-2019-on-premise
question_id: 2196104
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How to Configure CBA for exchange 2019 on premise??

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196104/how-to-configure-cba-for-exchange-2019-on-premise (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

I was setting up CBA for active sync and owa on exchange on premise 2019 following this guide https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/configure-certificate-based-auth?view=exchserver-2019 on my test environment.

Everything went smoothly, but when I Check OWA or ActiveSync virtual directory to require client certificate and connect through browser and prompt to choose user certificate I get error 403 "You don't have the user rights to view this page." Without virtual directory set to requiring client certificate everything works great.

Here is log of 403 in IIS: 2025-01-15 09:15:24 ::1 GET /OWA/auth.owa &encoding=; 443 - ::1 AMProbe/Local/ClientAccess - 403 7 5 19.

For CA I am using AD CA installed on domain controller, and for certificates issuance to user I use copy of user template and autoenrollment. User certificate picture is attached.

Server certificate is generated on offline Linux server CA, and this CA is trusted on domain. I really have no idea what else to do to make CBA work, maybe somebody can give some more suggestions???

![](https://learn-attachment.microsoft.com/api/attachments/cd0396fc-66eb-4bc0-8ca8-fc9bbe3333ed?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-15*

Hello Evald_En,  

Thank you for posting in Microsoft Community forum.  

From the description above, I understand your question is related to Exchange.   

Since there are no engineers dedicated to Exchange in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and type "Exchange" tag and select any tags related to your productions.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
