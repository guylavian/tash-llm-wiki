---
title: "Sysvol replication error 6408 on server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/896101/sysvol-replication-error-6408-on-server-2019
question_id: 896101
fetched: 2026-07-25
answer_count: 14
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Sysvol replication error 6408 on server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/896101/sysvol-replication-error-6408-on-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I keep getting an error 6408 on my domain controllers.  I have tried multiple ways of disabling the file replication services and forcing it to replicate through authoritative and non-authoritative means. when I have everything disabled and I run repadmin it comes back with no errors but as soon as I start the service back up I get error 6408 again.    

ERROR:    

The DFS Replication service failed to initialize replicated folder C:\Windows\SYSVOL because the service detected that one of its private folders overlaps with an existing replicated folder. This is an unsupported configuration.     

Additional Information:     

Overlapped Folder 1: C:\Windows\SYSVOL\staging areas\morrismfg.local     

Replicated Folder 1: C:\Windows\SYSVOL     

Replicated Folder 1 Name: SYSVOL Share     

Replicated Folder 1 ID: 43B28239-B9C8-46C4-8708-78E4DB6E3A17     

Replication Group 1 Name: Domain System Volume     

Replication Group 1 ID: 9AC17A3E-FD82-4BCC-B2E8-037A6FD4A0B0     

Member1 ID: 330F0D83-6AB5-4EFB-882A-CB62A80DF17A     

Overlapped Folder 2: C:\Windows\SYSVOL     

Replicated Folder 2: C:\Windows\SYSVOL     

Replicated Folder 2 Name: SYSVOL Share     

Replicated Folder 2 ID: 43B28239-B9C8-46C4-8708-78E4DB6E3A17     

Replication Group 2 Name: Domain System Volume     

Replication Group 2 ID: 9AC17A3E-FD82-4BCC-B2E8-037A6FD4A0B0     

Member2 ID: 330F0D83-6AB5-4EFB-882A-CB62A80DF17A

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-21*

I quote myself "I have tried multiple ways of disabling the file replication services    

The File Replication service (FRS) cannot be used with server 2019. You might try removing the 2019 server to clean things up.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-21*

I quote myself "I have tried multiple ways of disabling the file replication services and forcing it to replicate through authoritative and non-authoritative means.".  That link just leads to a page with everything that is on practically every page I have went to other then deleting the dfsr folder. The problem is, I don't have one to delete. It is still using the old folder but the migration is complete in it's mind so it won't rebuild the dfsr. I do all of that, I have done hundreds of google searches the last week and tried every page that I can find. Nothing tells me how to actually open the hood and get in there and fix things myself, it's all through commands that give me total success until the very end when I fire things back up. Every test that is said to run all comes back as successful but when I restart everything I get the 6408 error.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-20*

Ok, well you didn't say what actions triggered the problem or when it started. You could try this method.    

https://gist.github.com/RavuAlHemio/00e51d3ea64731be9d43b01eda18734f    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-20*

I have tried going through that but things don't come out the way they should and that page really doesn't address it so I am here. The domains started out on 2003, they have been updated to 2008 to 2008 R2 to 2019. Both domain and forest level have been set to 2016. If I check the migration status it tells me that it is "Eliminated" but net share still reports the SYSVOL folder.    

C:\Users\administrator.MORRISMFG0>Dfsrmig /getmigrationstate    

All domain controllers have migrated successfully to the Global state ('Eliminated').    

Migration has reached a consistent state on all domain controllers.    

Succeeded.    

C:\Users\administrator.MORRISMFG0>NET SHARE    

Share name   Resource                        Remark    

-------------------------------------------------------------------------------    

C$           C:\                             Default share    

IPC$                                         Remote IPC    

ADMIN$       C:\Windows                      Remote Admin    

MORRIS-REPO  C:\REPO    

NETLOGON     C:\Windows\SYSVOL\sysvol\morrismfg.local\SCRIPTS

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-20*

have tried multiple ways of disabling the file replication services    

In case its a typo; Server 2019 cannot use FRS for replication. The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR    

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
