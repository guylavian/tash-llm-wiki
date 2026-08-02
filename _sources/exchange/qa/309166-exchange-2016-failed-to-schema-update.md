---
title: "Exchange 2016 failed to schema update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/309166/exchange-2016-failed-to-schema-update
question_id: 309166
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 failed to schema update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/309166/exchange-2016-failed-to-schema-update (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,    

Our exchange 2016 is cu9 which install in child domain, and will patch to cu19. When we run the "prepareschema"  in root domain's Schema master DC, it show below error:    

    

-  We checked the account is member of "Schema Admin", "Enterprise Admin", "Domain Admin" and "Organization Management".    

-  The forest functional level and domain functional level is 2016    

-  Tried to create another admin account with required permission also have the same error.    

-  Tried to run the "prepareschema" in other server which in the same AD site    

-  All DC restarted and replication is good    

Any idea?    

Thanks    

Chong

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-17*

Hi @Joyce Shen - MSFT       

I double check the prerequisites and my environment should meet the requirement. The Exchange log don't have more detail, I can see the same error message as the capture screen and many "Active Directory operation failed on . The supplied credential for 'domain\admin' is invalid." error. But the account should be member of "Schema Admin", "Enterprise Admin", "Domain Admin" and "Organization Management".    

I didn't try to run the prepareAD command, as the prepareSchema command not work. I know run prepareAD will include prepareSchema also. But have any different with run the prepareSchema first?    

Thanks    

Chong

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-12*

Hi @Anonymous      

Please check the ExchangeSetup log to see more related information. Make sure you have meet all the prerequisites list in the official document here: Exchange Server prerequisites    

In addition, have you tried running the prepare AD command manually? Prepare Active Directory and domains for Exchange Server    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-11*

-  Sounds like an DNS related issue so I would start by validating the Exchange Server DNS settings are correct  

-  The other action to consider would be to do an AD Health check  

-  I would also check the local groups to ensurer there are no abandoned/orphaned entries, i.e. they will show as a GUID vs a username   

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
