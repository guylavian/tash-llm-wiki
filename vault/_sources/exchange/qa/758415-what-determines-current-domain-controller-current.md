---
title: "What determines Current Domain Controller, Current Global Catalog and CurrentConfigDomainController?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/758415/what-determines-current-domain-controller-current
question_id: 758415
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# What determines Current Domain Controller, Current Global Catalog and CurrentConfigDomainController?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/758415/what-determines-current-domain-controller-current (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I run; Get-ExchangeServer -Identity mailserver -status | Fl current  

This command returns current DC, GC and ConfigDC.  In EMC, Server Configuration, "Modify Configuration Domain Controller....." it is chosen "Use a default domain controller."  What is a default DC?  Where is it indicated which DC(s) are default?  

How does it choose a GC or a ConfigDC?  What, really, is a configDC anyway?  

None of this seems to come from the DNS IPs used by the NIC.    

How do I change any of this to test getting rid of old DCs?

## Answer (community) — community member

*upvotes: 1 · updated: 2022-03-04*

Just an FYI; set-exchangeserver -Identity exchange -StaticExcludedDomainControllers asf-dc1.domain.local  Did work.  It did create a Key, in Default, not beneath it.  Within Default ExcludedDCs REG_MULTI_SZ = dc3.domain.local  

Thanks for everything.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-03*

Well, I will say that 2080 does show 5 DCs; 3 new and 2 old.   They all are Cs and Ds and 3 (two new) are Gs.  So, that said, I think I'm okay.  Doing a lot of reading and help from this forum got me to a comfortable place....I hope.  You'll never forget when your Exchange server loses contact with AD.  No EMC, no Exchange shell...nothing.  The registry is all you have.  Do you know if command  "set-exchangeserver <Exch Server> -StaticExcludedDomainControllers" creates a registry entry so I can recover from disaster?  

Thanks again, big help.
