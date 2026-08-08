---
title: "Exchange hybrid agent not installing (Exch 2016 on prem)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1571376/exchange-hybrid-agent-not-installing-exch-2016-on
question_id: 1571376
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange hybrid agent not installing (Exch 2016 on prem)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1571376/exchange-hybrid-agent-not-installing-exch-2016-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Many moons ago we migrated our users, groups, public folders to Exchange Online but are still hybrid, I believe this is required because our on-prem AD is still the global.
So now we have an issue where we have an old distribution group that was migrated, so exchange online see is as administered by the on-prem exchange server.  However we've been asked to add a user to it that was created in Exchange Online.  We can't add the user through Exchange Online because on-prem controls the group, but on-prem doesn't see the user because it was created in Exchange Online.
Couple questions.  1) Can we completely migrate to Exchange Online with AD still being on-premise so we are no longer hybrid in Exchange Online?  2) If not, will installing the Hybrid agent via the wizard help with sync'ing between the two (we had one but decommissioned it when the migration was complete)?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-23*

Hi @Daniel Kaliel,

-  Can we completely migrate to Exchange Online with AD still being on-premise so we are no longer hybrid in Exchange Online?

If you have on-premises AD and will continue to create users in on-premises AD then sync them to cloud and enable mailboxes for them in the future, to keep you in a supported situation you may need Exchange hybrid deployment for management purpose.

Otherwise you may have trouble with managing the Exchange mailbox attributes in on-premises AD.

For more details please refer to this link:

Why you may not want to decommission Exchange servers from on-premises

-  If not, will installing the Hybrid agent via the wizard help with sync'ing between the two (we had one but decommissioned it when the migration was complete)?

Sorry I do not quite understand what do you mean by syncing between the two.

If you install a new Exchange server, download and re-run Hybrid Configuration Wizard, it will simply update the configuration in the hybrid deployment for you.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
