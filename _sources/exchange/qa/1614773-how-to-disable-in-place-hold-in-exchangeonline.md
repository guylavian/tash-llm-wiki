---
title: "How to disable In-Place Hold in ExchangeOnline?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1614773/how-to-disable-in-place-hold-in-exchangeonline
question_id: 1614773
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-purview", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# How to disable In-Place Hold in ExchangeOnline?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1614773/how-to-disable-in-place-hold-in-exchangeonline (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have Archive Online turned on few Exchange mailboxes. I want to disable one of them but I can't. When I try to do this by UI I have a meaning-nothing error:  

So I tried doing it via PowerShell and this fortunately gives me an actual error:  

So my question is - how to disable InPlaceHold? Using UI and using PowerShell.   

Microsoft documentation is outdated - it refers to this feature in EAC in which it is retired, so documentation is useless.   

https://learn.microsoft.com/en-us/exchange/security-and-compliance/create-or-remove-in-place-holds

I run a PowerShell to check some ids of those InPlace-Holds but I couldn't find any PowerShell that works to actually delete it.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-05-10*

Hello,  

Finally, I resolved this problem with help from Microsoft consultant. I couldn't get rid off ComplianceTagHoldApplied set to True. They changed this parameter from "their side".

I was told that the problem is know by Microsoft and they are working to fix it.

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2024-03-13*

You could use Invoke-HoldRemovalAction in Security & Compliance PowerShell:

Invoke-HoldRemovalAction (ExchangePowerShell) | Microsoft Learn

Invoke-HoldRemovalAction -Action RemoveHold -ExchangeLocation ******@contoso.onmicrosoft.com -HoldId "UniHecbf89df-74fc-444a-a2dc-c0756c7d3503"  -force

 

I have test in my M365, it works fine.

 

Or you could Use the GUID to identify the hold:

$CaseHold = Get-CaseHoldPolicy <hold GUID without prefix>

Get-ComplianceCase $CaseHold.CaseId | FL Name

The second command displays the name of the eDiscovery case the hold is associated with. And you could modify/remove it in Microsoft Purview directly.

How to identify the hold on an Exchange Online mailbox | Microsoft Learn

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-28*

Great to know that the issue has already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer : )  

Issue Symptom:

How to disable In-Place Hold in ExchangeOnline?

Can not disable the mailbox with "-mbx" hold**.** His mailbox is excluded from organization hold, because it has prefix "-mbx".

Resolution:

The problem is that one account have ComplianceTagHoldApplied set to True and I can't get rid of that and this is causing the problem. When accounts I want to disable didn't have it set to True I can exclude them for policies and disable archive w/o problems.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-03-13*

Those seem to be holds corresponding to Retention policies in the Compliance center, simply exclude the mailbox therein: https://learn.microsoft.com/en-us/purview/create-retention-policies?tabs=other-retention
