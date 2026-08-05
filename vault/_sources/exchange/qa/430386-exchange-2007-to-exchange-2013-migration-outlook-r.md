---
title: "Exchange 2007 to Exchange 2013 Migration & Outlook reconfiguration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430386/exchange-2007-to-exchange-2013-migration-outlook-r
question_id: 430386
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2007 to Exchange 2013 Migration & Outlook reconfiguration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430386/exchange-2007-to-exchange-2013-migration-outlook-r (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello!  

Planning for Exchange 2007 to Exchange 2013 Migration. clients as as below:-  

outlook 2007  

outlook 2010  

outlook 2013  

Please confirm whether outlook will require manual reconfiguration after mailbox movement to exchange 2013 servers.  

Cheers  

Priya

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-06-10*

Possibly. No one can really tell you that, but any move from Exchange 2007 to Exchange 2013, I would expect to have to recreate some Outlook profiles.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-11*

Hi @Priya Jayaraman  ,    

Please confirm whether outlook will require manual reconfiguration after mailbox movement to exchange 2013 servers.    

I’m afraid that this might not be able to accurately predict. According to my experience, some users can indeed continue to use their email account in Outlook desktop client without any manual reconfiguration after migration, while others might encounter issues like Outlook cannot connect to the new mail server and need to create and use a new Outlook profile. To avoid problems as much as possible, it would be better to recreate Outlook profiles and re-configure your email accounts after migration.    

By the way, considering that you are planning for Exchange 2007 to Exchange 2013 migration, the guidance provided by the Exchange Deployment Assistant should be able to help, hope it could help make these works easier.     

And about Outlook desktop clients, considering that Outlook 2007 and Outlook 2010 has reached their ends of support, for better user experience, you could try some newer versions of Outlook desktop client like Outlook 365 and Outlook 2019 like the supported clients list says:    

    

Hope these could help.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
