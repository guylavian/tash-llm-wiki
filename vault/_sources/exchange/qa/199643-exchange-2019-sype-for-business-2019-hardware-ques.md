---
title: "Exchange 2019, Sype for Business 2019 hardware questions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199643/exchange-2019-sype-for-business-2019-hardware-ques
question_id: 199643
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-skype-business-platform-windows", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2019, Sype for Business 2019 hardware questions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199643/exchange-2019-sype-for-business-2019-hardware-ques (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

For Exchange 2019, it recommends 128GB RAM?  

I will have roughly 200 mailboxes on a Hyper-V VM.  How much RAM will I actually need?  

I am currently running Exchange 2016 that is using about 15GB RAM.  

For Skype 2019, what non-subscription alternatives are there for voicemail as Exchange 2019 will not have unified messaging?  

For Skype 2019, how high is CPU usage as far as needing 8 cores? My current processor has 4 cores.  This too will be in a Hyper-V VM running with a Skype Edge VM.  

How much RAM does Skype 2019 actually use?  There probably won't be too many user on at one time.  

Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-16*

Hi @Susan Dodds  ,    

For Exchange 2019, it recommends 128GB RAM?    

Yes. The evidence can be found here:    

https://learn.microsoft.com/en-us/exchange/plan-and-deploy/system-requirements?view=exchserver-2019#hardware-requirements-for-exchange-2019    

In fact, Exchange Server storage sizing includes the Exchange Server storage sizing includes estimating the storage space to accommodate databases, content indexes, transaction logs, growth factors, and unexpected overhead growth, so we have no accurate way to calculate it. As a workaround, you can try to use the following link’s calculator to calculate it:    

https://gallery.technet.microsoft.com/office/Exchange-2013-Server-Role-f8a61780    

For more details about Calculator guidance:    

https://exchangeloadbalancer.com/exchange-role-calculator/start/    

For Skype 2019, what non-subscription alternatives are there for voicemail as Exchange 2019 will not have unified messaging?    

Cloud Voicemail is Microsoft’s response to yanking Unified Messaging out of Exchange. For more details about how to configure cloud voicemail service for on-premise users, you can learn it from:    

https://learn.microsoft.com/en-us/skypeforbusiness/hybrid/configure-cloud-voicemail    

For Skype 2019, how high is CPU usage as far as needing 8 cores?    

You can try to download the Skype for Business Server 2015, Stress and Performance Tool. When you have entered all the necessary information, the capacity calculator estimates your requirements. The yellow cells show calculated values for CPU, memory, and bandwidth requirements based on tests performed in Skype for Business Server performance labs.    

https://learn.microsoft.com/en-us/skypeforbusiness/management-tools/capacity-planning-calculator    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
