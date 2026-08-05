---
title: "[Migrated from MSDN Exchange Dev] Out of Office Uniform Template"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/134628/migrated-from-msdn-exchange-dev-out-of-office-unif
question_id: 134628
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev] Out of Office Uniform Template

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/134628/migrated-from-msdn-exchange-dev-out-of-office-unif (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on Exchange developer questions and the TechNet Exchange forums for Non-developer Exchange has been locked down and transitioned to Microsoft Q&A for support, we manually migrated this one to Microsoft Q&A platform to continue the discussion.  

[MSDN thread link]  Out of Office Uniform Template  

[Original post]  

Dear Team  

I have a requirement to set the Out of Office Template for all users within company.Can i enable the belwo template in outlook for all users and they can just select date and time and modify the relevant content. I am using Exchange Server 2016 in hybrid mode with office 365. Is below possible in anyway like GPO or Exchange powershell  

Automatic out of office reply:  

Thank you for your email. I am out of office from dd/mm/yyyy to dd/mm/yyyy. I may not have regular access to my emails. Therefore, for urgent matters please contact the following colleague(s):" 1. (Name) (Function / Department) at (email Address) 2. (Name) (Function / Department) at (email Address) 3. (Name) (Function / Department) at (email Address)

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-22*

Hi,  

To the best of my knowledge, I am afraid it's not feasible to set the Out of Office template globally for all users via either GPO or Exchange powershell.   

That being said, personally I would suggest considering sharing the template to all users via email and training them to set the Out-of-Office by themselves.   

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
