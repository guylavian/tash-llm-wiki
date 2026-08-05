---
title: "Exchange 2010 to 2016 migration steps"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/188847/exchange-2010-to-2016-migration-steps
question_id: 188847
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2010 to 2016 migration steps

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/188847/exchange-2010-to-2016-migration-steps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

i need Exchange 2010 to 2016 migration steps     

current Exchange version is below

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-08*

Hi @Sabir Shibley  ,    

Happy to see that you've got useful information from Andy's reply : )     

To add to the links shared by Andy, I'd like to mention that before introducing Exchange 2016 into the existing environment, please make sure that the following co-existence requirements are met:    

• All the Exchange 2010 servers have been updated to at least SP3 with Update Rollup 11 installed. You can download the latest Update Rollup 30 for SP3 from Update Rollup 30 For Exchange 2010 SP3 (KB4536989).    

• In Exchange 2016, the minimum support Forest Functional Level and Domain Functional Level is Windows 2008 or above. So please ensure your environment is ready for this.    

• The Outlook clients are upgraded to Outlook 2010 or above on Windows and Outlook 2011 or higher on the Mac.    

Besides, for the detailed step-by-step guidance, apart from Andy's link and the Exchange Deployment Assistant tool he mentioned, hopefully you can also find the document below helpful:    

Rapid Migration from Exchange 2010 to Exchange 2016    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
