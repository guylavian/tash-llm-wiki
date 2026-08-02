---
title: "Transitioning Exchange 2007 SP1"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/234068/transitioning-exchange-2007-sp1
question_id: 234068
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Transitioning Exchange 2007 SP1

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/234068/transitioning-exchange-2007-sp1 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently acquired an old company where we have 3 Windows 2003 Domain Controllers where AD +Exchange 2007 SP1 is installed on the same server.  I would like to perform transition to Windows 2008 R2, which is fairly easy.   

The Windows 2003 domain Functional Level is Windows 2003  

Forest Functional Level is Windows 2000.  

I have read the below article with regards to Exchange 2007 SP1 against Windows 2008 R2 Active Directory.  

https://techcommunity.microsoft.com/t5/exchange-team-blog/exchange-server-2007-supportability-matrix/ba-p/598981  

Exchange Server 2007 is not supported on Windows Server 2008 R2. However, Exchange 2007 SP1 RU9 and SP2 are supported against Windows Server 2008 R2 Active Directory servers. In addition, Exchange 2007 SP1 RU9 and SP2 are supported in Active Directory environments whose domain/forest functional levels have been raised to Windows Server 2008 R2.  

If I am not wrong the above lines quoted in bold lines means that I can use the same forest functional Levels and Domain Level as it is and also later If I am upgrading it to Windows 200R2 (Functional Level and Domain Level) it will work.  

Thanks

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-01-18*

A couple of things:     

 You need to get those to 2007 SP3 plus the latest UC if possible first if you want to eventually migrate to Exchange 2013 - then to Exchange 2016/2019.    

Personally I would build new servers.  Since 2007 is out of support, there is no public , official way to get those latest service packs and UCs,  So unless you have those available to you, you are stuck.    

https://learn.microsoft.com/en-us/exchange/upgrade-from-exchange-2007-to-exchange-2013-exchange-2013-help#coexistence-of-exchange-2013-and-earlier-versions-of-exchange-server    

As far as the current FFL/DFL, I read it the same way, it should hopefully work for you now and if you upgrade the 2007 servers, but you are in completely unsupported territory, so no one at Microsoft can help you if something goes sideways.    

You may want to also consider third party software and simply export the existing mailboxes out and import them back into upgraded servers     

Or use the built-in export powershell in 2007:    

https://techcommunity.microsoft.com/t5/exchange-team-blog/how-to-export-and-import-mailboxes-to-pst-files-in-exchange-2007/ba-p/594262    

-  or use exmerge which probably worked on 2007 : https://www.microsoft.com/en-us/download/details.aspx?id=2743    

Alternatively, just give them new mailboxes on a supported system and not attempt to upgrade.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Thanks Andy let me see how I can solve the issue and revert back to the forums if  more advice needed
