---
title: "Exchange hybrid setup Free/Busy for multidomain not working."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/238096/exchange-hybrid-setup-free-busy-for-multidomain-no
question_id: 238096
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Exchange hybrid setup Free/Busy for multidomain not working.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/238096/exchange-hybrid-setup-free-busy-for-multidomain-no (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,     

We have a multi domain (22 domains) AD e Exchange 2013 setup. we have successfully created the endpoints for the hybrid setup and performed the on boarding of some of the test mailboxes successfully (On-premises to Exchange online). We have a dedicated Exchange 2016 server with the hybrid setup.    

All 22 domains are validated successfully on Office365- using SRV record on the public DNS.     

The issue is :  Free/busy option is not working between domains.         

    

TO start with, we have enabled the federation trust between the domain1 and the domain2 by registering the txt value (Key) provided by the by the wizard and still no result.    

do you have any suggestions ?    

Thank you    

--    

Jerry

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

Hi @jerry verghese george      

According to your information above, you have a hybrid environment with 22 domains. You have configured federation trust between on-premise domain1 and domain2,     

however freebusy between these two on-premise domains still not work. Are the users still located on-premise now? Correct me if I have any misunderstanding about your question.    

Did you configure any sharing policy in your organization? Please check if you have setup all steps right list in the offcial document: Configure federated sharing    

You could refer to this link to get more information about this process as well: Exchange 2013/2016: Calendar Sharing between 2 Orgs    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
