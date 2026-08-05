---
title: "Domain Controller Stuck (AD)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/698034/domain-controller-stuck-ad
question_id: 698034
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller Stuck (AD)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/698034/domain-controller-stuck-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

Its my first time here and I apologies if this is not the corret forum to post this issue.    

I am experiencing some strange problem. My onpremises domain controller does not respond after a period.    

For example, I reboot it right now and everything works fine but after, Id say, 5 days, I cant open any windows or task or whatever.    

And after a long long time after clicked to open DHCP, e.g., it returns the windows below:    

    

An important point is that all the services are running as expected, that is, dhcp is providing IP, users are authenticating through active directory, DNS resolves names etc.    

Anyone can help me?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-18*

Hi there,    

The on-premises network connection (OPNC) periodically checks your environment to make sure that all requirements are met and are in a healthy state. If any check fails, you'll see error messages in the Microsoft Endpoint Manager admin center.    

If provisioning fails, make sure that:    

-The sync period configuration on Azure AD is set appropriately. Speak with your identity team to make sure that your directory is syncing fast enough.    

-Your Azure AD is active and healthy.    

-Azure AD Connect is running correctly and there are no issues with the sync server.    

-You manually perform an Add-Computer into the OU provided for Cloud PCs. Time how long it takes for that computer object to appear in Azure AD.    

Troubleshoot on-premises network connections    

https://learn.microsoft.com/en-us/windows-365/enterprise/troubleshoot-on-premises-network-connection    

----------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-17*

Simplest solution may be to stand up a new one for replacement.    

I'd use dcdiag / repadmin tools to verify health `correcting all errors found` before starting `any` operations. Then stand up the new one, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
