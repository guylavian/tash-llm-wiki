---
title: "Upgrade Hybrid Exchange Server 2016 to Hybrid Exchange Server 2019 and Certificate Questions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1250797/upgrade-hybrid-exchange-server-2016-to-hybrid-exch
question_id: 1250797
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Upgrade Hybrid Exchange Server 2016 to Hybrid Exchange Server 2019 and Certificate Questions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1250797/upgrade-hybrid-exchange-server-2016-to-hybrid-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So we are currently running a Hybrid Exchange Server 2012 and need to install a new guest virtual server with Hybrid Exchange Server 2019. I have done a bunch of reading and it seems the more I read, the more I get confused. We are an Office 365 customer. No Mailboxes on site (All mail is in Exchange Online). We do not use OWA or anything similar.  

So Question #1 - Certificates - Do I need a 3rd Party Verified Certificate from GoDaddy and if so, what do I need to ask for?  

Question # 2 I have downloaded the .ISO file for Exchange 2019, do I do a full install on the new server and then run the Hybrid Configuration Wizard?  

Question # 3 will running the install from the .ISO take care of Extending my schema? Our current DCs are Server 2012 R2 and the Functional level of our Domain and Forrest is set to 2016 R2.  

Question #4 - Licensing - I read in one place the I have to buy a Microsoft License for Exchange Hybrid install, and in another I read that I do not have to pay for the Hybrid Exchange License?  

Thank you in advance for any guidance.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2023-04-21*

Hi @Brian Chernish  ,

Question #1 - Certificates - Do I need a 3rd Party Verified Certificate from GoDaddy and if so, what do I need to ask for?

Yes. According to this article, a 3rd-party certificate is required for the external-facing Exchange hybrid server or servers. Since you are already in the Exchange 2016 hybrid, you can just reuse the certificate in Exchange 2016. For detailed steps, you can generate a step-by-step guidance for upgrading to Exchange 2019 from Exchange 2016 using the Deployment Assistant tool and check the instructions in the "Configure Exchange certificates" part. 

Question # 2 I have downloaded the .ISO file for Exchange 2019, do I do a full install on the new server and then run the Hybrid Configuration Wizard?

Yes. 

Question # 3 will running the install from the .ISO take care of Extending my schema? Our current DCs are Server 2012 R2 and the Functional level of our Domain and Forrest is set to 2016 R2.

Yes, you can let the Exchange Setup wizard to take care of extending schema and preparing AD and domains supposing you don't have a large AD deployment. See this link. The OS version of your current DCs and your current functional level can meet the requirements for Exchange 2019 as well as per this table.

Question #4 - Licensing - I read in one place the I have to buy a Microsoft License for Exchange Hybrid install, and in another I read that I do not have to pay for the Hybrid Exchange License?

It's now for free for Exchange 2019. See this link.  

It's also mentioned in the following blog:  

Released: 2022 H1 Cumulative Updates for Exchange Server  

Hope the information above can be helpful. By the way, as we usually focus on only one question in one thread, should you need further assistance, it'd be best if you can focus on one question in this thread and start new posts for the others. Thanks for your understanding.  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
