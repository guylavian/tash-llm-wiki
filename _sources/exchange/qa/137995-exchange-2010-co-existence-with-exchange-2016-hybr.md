---
title: "Exchange 2010 Co Existence with Exchange 2016 Hybrid - Public Folder Migration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/137995/exchange-2010-co-existence-with-exchange-2016-hybr
question_id: 137995
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange 2010 Co Existence with Exchange 2016 Hybrid - Public Folder Migration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/137995/exchange-2010-co-existence-with-exchange-2016-hybr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am deploying Exchange 2016 into an Exchange 2010 environment with the intention of migrating the Exchange 2010 mailboxes to Office 365.  Due to Exchange 2010 EOL I am installing classic Hybrid on Exchange 2016.  Exchange 2010 also hosts Public Folders.  From my research it seems that the MRS proxy has to be on the server that hosts the public folders in order to migrate them.  So is my only real option to migrate the public folders to Exchange 2016 and then migrate them to Office 365?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-31*

Hi All, knowing this environment has exchange 2010 & 2016 with hybrid exchange online through excahnge 2016, is it works for calendar sharing and Global address list  between exchange 2010 mailbox n exchange online mailbox ?

thanks

Novih

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-13*

Hi @Andy David - MVP   & @Lydia Zhou - MSFT  !    

I have a Exchange 2016 Coexistence Environment with Exchange 2010 so the namespace (OWA, OA, Autodiscover) point to Exchange 2016. The PFs are hosted in Exchange 2010.    

His recommendations are to have 2 migration endpoints: one for public folder migration, and other, for mailbox migration. But in Exchange 2016 Coexistence Environment with Exchange 2010, I need to have the same ExternalHostName in Outlook Anywhere for both Exchange 2010 and Exchange 2016 for coex working. I am right?    

I ask you this because I read the article https://www.enowsoftware.com/solutions-engine/migration-of-legacy-public-folder-to-modern-public-folder-in-exchange-online and see that it use 2 different names and I don't know if that is possible. Also, the autodiscover record should point to the Exchange On-Premise server with the most updated version.    

Could you help me?    

Thanks!!

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-10-26*

@jpcapone       

Agree with AndyDavid, and the provided articles are very helpful. We can migrate legacy public folders from Exchange 2010, and make sure Outlook Anywhere is enabled on your Exchange 2010.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
