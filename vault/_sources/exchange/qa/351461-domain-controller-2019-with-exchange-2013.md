---
title: "Domain Controller 2019 with Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/351461/domain-controller-2019-with-exchange-2013
question_id: 351461
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain Controller 2019 with Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/351461/domain-controller-2019-with-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Forum,   

I inherited a network that the DC where upgraded to a mix of Windows 2019 and Windows 2016.   

Domain level and Forest level are set to Windows 2016.  

I was tasked with the upgrade of Exchange 2013 to Exchange 2019.   

During the pre-requirement checks I notice that Exchange 2013 does not support Domain controllers 2019.  

However in the current environment it is already running.   

Now my questions is, is it safe to introduce the Exchange 2019 to the network seeing that the Domain Controllers are already a mix of 2019 and 2016?  

What other alternatives do I have for this upgrade?  

Thank you in advance for your feedback

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-26*

Dear All,   

Thank you for your feedback.  

What I will do is replicate the scenario in a test lab. Then introduce the Exchange 2019 is simulate a migration.   

It that goes well I will do the same into he production environment.   

Thank you again for you input.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-12*

Hi @Sherlon Martina   ,    

Yes the Exchange 2013 will not support Windows server 2019 as the domain controller, but you still have 2016 mixed.    

    

I think the question is the schema master, that refers to the first Windows server you've installed.    

    

But as you said, it is running, so I think you could go on migrating.    

Oh you can export the mailboxes to pst files to backup, and you can follow the deploy assistant to do the migration.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
