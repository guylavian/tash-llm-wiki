---
title: "Exchange 2019 outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1630912/exchange-2019-outlook
question_id: 1630912
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1630912/exchange-2019-outlook (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have exchange 2019 I'm using outlook 2019 client, why groups which I'm part are not listed in the outlook and OWA ?   

I'm trying to add profile photo for the distribution group to which I'm the Owner, I want to find solution for this.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-03-25*

Hi Nandan NK,

According to your problem description, I suggest you can follow the following steps for troubleshooting:

-  Ensure that Cached Exchange Mode is enabled in the Outlook client. If it is disabled, try enabling it and restarting Outlook.

-  Sometimes, a corrupt configuration file can cause problems. You can create a new profile in Outlook and configure it with an account that can view groups. Check if the groups are shown in the new profile.

-  If you are in a mixed environment (a mix of local Exchange and Exchange Online), make sure you synchronize the group settings correctly. Sometimes, by default, groups created through Microsoft Teams may not show up in Outlook.

If the problem is still not resolved, feel free to comment to me and I'll be happy to help!
