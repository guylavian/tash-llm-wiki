---
title: "Exchange 2010 migration to a newer version and Exchange Management Shell mailbox anchoring"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/289023/exchange-2010-migration-to-a-newer-version-and-exc
question_id: 289023
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2010 migration to a newer version and Exchange Management Shell mailbox anchoring

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/289023/exchange-2010-migration-to-a-newer-version-and-exc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I'm in the process of migrating my Exchange server to a newer version. I'm aware of this EMS (Exchange Management Shell) behavior change: https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-management-shell-and-mailbox-anchoring/ba-p/604653  

and of these workarounds: https://exchangemaster.wordpress.com/2016/01/06/mailbox-anchoring-affecting-new-deployments-upgrades/  

From my understanding that means that, without workarounds, with a fresh install of Exchange, if I run a cmdlet (i.e.: I want to change the SCP attribute to avoid certificate warings in Outlook) in EMS on the new Exchange, simply it won't work. Am i right?  

Those posts was made when Exchange 2013 CU11 and Exchange 2016 CU1 were released. I'm wondering if those "issues" are still present in newer builds.  

My main concern, as above said, is that when a new Exchange version is installed in a AD site, the first thing I must do is to change the default SCP (Service Connection Point) attribute to the one currently used that points to my Exchange 2010 server, to avoid certificate warnings to end users in Outlook. If the above said is still true, I won't be able to change the Service Connection Point created by the new Exchange server in AD in a timely manner since EMS loaded on the new Exchange server will actually point to Exchange 2010. So my users will get those annoying warnings until Exchange admin mailbox will be moved for example and I will then be able to run the cmdlet on the new Exchange.   

In the case, I must change my deployment steps (and time schedule for the deploy) accordingly and I'd like to know it before to start the migration.  

Thank you,  

Francesco B. B.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-25*

Thank you very much, one less concern to worry about :). I read here (https://techcommunity.microsoft.com/t5/exchange-team-blog/remote-powershell-proxying-behavior-in-exchange-2013-cu12-and/ba-p/604504) that from CU12 onward behavior has been reverted but I wanted to be sure.    

Please, consider to remove that behavior change from official Exchange release notes: https://learn.microsoft.com/it-it/exchange/release-notes-for-exchange-2013-exchange-2013-help#exchange-management-shell    

It's quite a while that CU12 has been released :))    

Thank you for the rapid answer AndyDavid!    

Bye,    

Francesco B. B.
