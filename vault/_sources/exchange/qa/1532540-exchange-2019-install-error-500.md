---
title: "Exchange 2019 install Error 500"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1532540/exchange-2019-install-error-500
question_id: 1532540
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange 2019 install Error 500

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1532540/exchange-2019-install-error-500 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am testing in lab adding exchange 2019 to an existing exchange 2013 environment.  

After setup of Exchange I get error 500.    

After install the ECP worked.  

I have updated URLs and Certificate and rebooted. 
After reboot I cannot login to ECP as localhost or the URL given.  

WHAT IS GOING ON WITH ERROR 500????   IT KEEPS HAPPENING!!!!!
How do I even debug this?  I see no errors.  It just is dead.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-02-14*

I think there was an issue with access to the admin mailbox.  Once I moved it to the new server I could login to the new ecp.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-15*

Hi @ComputerHabit  ,

I think there was an issue with access to the admin mailbox. Once I moved it to the new server I could login to the new ecp.

Great to know that you've managed to fix the issue by moving the admin mailbox to the new server and thanks for the share!  

Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )    

[Exchange 2019 install Error 500]  

Issue symptom:  

"I am testing in lab adding exchange 2019 to an existing exchange 2013 environment.  

After setup of Exchange I get error 500.  

After install the ECP worked.  

I have updated URLs and Certificate and rebooted. After reboot I cannot login to ECP as localhost or the URL given."  

Solution:  

"I think there was an issue with access to the admin mailbox. Once I moved it to the new server I could login to the new ecp."
