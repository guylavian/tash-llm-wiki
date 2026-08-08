---
title: "[Migrated from MSDN Exchange Dev]Upgrade Exchange SP1 to CU23"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218924/migrated-from-msdn-exchange-dev-upgrade-exchange-s
question_id: 218924
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# [Migrated from MSDN Exchange Dev]Upgrade Exchange SP1 to CU23

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218924/migrated-from-msdn-exchange-dev-upgrade-exchange-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/cff27038-62e1-40e9-80ca-c7acb13ebe59/upgrade-exchange-sp1-to-cu23?forum=exchangesvrdevelopment  

I have exchange server 2013 sp1, i need to upgrade it to CU23. Can i do it directly or i have to do intermediate upgrade first.  

Exchange OS: 2012r2  

AD OS: 2012r2  

Forest\ domain function levels: 2008  

I need also to install exchange 2019 cu9 "coexistent" for awhile and migrate all mailboxes to exchange 2019. should i upgrade current forest\ domain function levels or it gonna work.  

for exchange 2019 cu9, what IE or chrome version should i use (install or update to latest version)  

Thank You

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-05*

Hi IICO2022,    

Based on my knowledge, you need to install .Net Framework 4.8 or 4.7.2 to support the Exchange 2013 CU23.    

And note that only .Net Framework 4.8 could support Exchange 2019 CU9.    

should i upgrade current forest\ domain function levels or it gonna work.    

You should raise the forest function level to Windows Server 2012 R2 to support Exchange 2019.    

    

for exchange 2019 cu9, what IE or chrome version should i use (install or update to latest version)    

You can use the latest version Microsoft Edge, and you can check other browsers in these articles.    

Browsers that support OWA : Web browsers supported for use with the premium version of Outlook Web App or Outlook on the web    

And browsers that support EAC: Exchange Admin Center Supported browsers    

Note that Exchange 2019 Mailbox/Edge Transport roles could only be installed on Windows server 2019.    

     

I think this article would be helpful: Exchange Server 2019 system requirements, Exchange Server supportability matrix.    

And Exchange Deployment Assistant could help you in upgrading.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
