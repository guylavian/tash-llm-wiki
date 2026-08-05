---
title: "Domain Controller that is also Entra Sync Server permanently offline - How to reconnect On-premises AD to Azure / Entra"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199068/domain-controller-that-is-also-entra-sync-server-p
question_id: 2199068
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Domain Controller that is also Entra Sync Server permanently offline - How to reconnect On-premises AD to Azure / Entra

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199068/domain-controller-that-is-also-entra-sync-server-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are a small business, and have two Active Directory Domain Controllers, both running Windows Server 2022

[PENTAGRAM-1]

[PENTAGRAM-2]

PENTAGRAM-1 is the Primary Domain Controller. It also has Entra Connect installed and syncing to our Azure/Entra Tenant with SSO enabled, and password writeback enabled. Sync method is Password Hash Sync.

The hard disk failed permanently. We do not have an image backup as we have just started setting up our infrastructure.

We have promoted PENTAGRAM-2 to the primary domain controller, but are now unable to setup and install Entra Connect to resume syncing between our On-premises AD and M365 / Entra.

We continue to get the error "An error occurred executing Configure AAD Sync Task: An Error Occurred While Sending The Request"

Error Log: trace-20240729-190859.log (PasteBin Link)

How do I re-connect my on-premises AD DS to Entra?

So far I have deleted the local ADDS account created by the previous sync client on PENTAGRAM-1 but I still run into the same issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-30*

Hello nggamingna-eric,  

Thank you for posting in Microsoft Community forum.  

From the description above, I understand your question is related to Azure or Microsoft Entra.   

Since there are no engineers dedicated to Azure or Microsoft Entra in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and type "Azure" tag and "Microsoft Entra ID" and select any tags related to your productions.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
