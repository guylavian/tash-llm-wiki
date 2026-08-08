---
title: "ADSS Security references obsolete Exchange admin accounts"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/164698/adss-security-references-obsolete-exchange-admin-a
question_id: 164698
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# ADSS Security references obsolete Exchange admin accounts

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/164698/adss-security-references-obsolete-exchange-admin-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon, all!  

I have been tasked with validating and cleaning up a customer's ADSS structure. One of the things I've found is that there are some orphaned SIDs that refer back to an obsolete Exchange installation and transporting Exchange information between sites. I don't have info on how on-prem Exchange was decommissioned; I do know that's a nice area to injure yourself. My preference in the past has been to decommission all but one on-prem server, shut that one down, but leave all the AD-Exchange stuff to make managing O365 a little easier.  

Question is - would archiving and deleting those entries be a bad thing for ADSS?   

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-17*

Hi @Gregg Hughes   ,    

Do you mean Active Directory Site and Service by ADSS? If not, would you mind describing in detail what you are referring to.    

Is your environment hybrid deployment now? If so, when directory synchronization is enabled for a tenant and a user is synchronized from on-premises, most of the attributes cannot be managed from Exchange Online and must be managed from on-premises. So if you still need the local Active Directory and Exchange information, you cannot disable all local Exchange servers.    

For more information you could refer to:How and when to decommission your on-premises Exchange servers in a hybrid deployment    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
