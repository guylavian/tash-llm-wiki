---
title: "Why aren't all members of an Active Directory group being added to my Teams channel when I apply the AD group?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4436719/why-arent-all-members-of-an-active-directory-group
question_id: 4436719
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-teams-teams-business-teams-channels-manage-team-channel"]
---
# Why aren't all members of an Active Directory group being added to my Teams channel when I apply the AD group?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4436719/why-arent-all-members-of-an-active-directory-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Teams group set up specifically to communicate with all members of an AD group that currently has ~1,500 members. As I currently understand it, I need to manually re-apply the AD Group regularly via the 'Add member' function, as don't believe you can automate updates. Although not ideal, this works OK.  

Although Teams is temperamental when I apply the AD group (it will say 'There were some errors' maybe 4 or 5 times), it allows me to 'Try again' each time and will complete successfully.   

The issue I'm having is that over 100 of the members of the AD group are not being added when I apply it and there doesn't seem to be any logical pattern or explanation for the people not being added. For example, they aren't just the newest members of the AD group, don't have name changes and all appear to be permanent 'normal' current employee profiles who use Teams. I can also still add people who were not added via the AD group process individually to the Team, so don't believe it's a problem with certain people or profiles.  

Has anyone else experienced this or know what the cause might be please? We're currently at 1,381 members in the Team, so don't seem to have hit any limit on numbers yet. Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2025-02-21*

Hello David Rodriguez Rivas,

Good morning!   

Thank you for publishing in Microsoft Community. We are happy to help you.

Based on your description we understand that when you try to add an Active Directory (AD) group with around 1,500 members to a Microsoft Teams group, over 100 members are not being added. This happens despite multiple attempts and without any clear pattern or explanation. The problem persists even though these members are regular employees who use Teams and can be added individually without issues.

In order to identify the problem for a better understanding of the situation, I can ask the following questions. Thank you very much for your cooperation and time.

1-Please are you trying to add an on-prem AD group to a active team ? If yes ! 

So far what i know "Nesting" groups is not yet supported for Team. You can "add" a group as member via the Teams client, but that simply takes the current membership of the group. Instead, you can use Teams with Dynamic membership rules, as detailed here:

 https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/groups-dynamic-membership.

Configure dynamic membership groups with the memberOf attribute in the Azure portal - Microsoft Entra ID | Microsoft Learn

In all cases, the group must be synced to Azure AD, you cannot use purely on-prem one.

Please note that : it seems you are in hybrid environment, since from our side we are in pure cloud and we can reproduce the issue from our end, it is advice to post the issue in our dedicate team channel via Microsoft Exchange Hybrid Management - Microsoft Q&A or you can create support ticket , so our agent can reproduce the issue in same environment and provide the correct solution. You can refer to this article to check the way how to raise a ticket. Ways to contact support for business products - Admin help. (if you are not admin you need to contact your admin or IT department)     

2-Please if you are in pure cloud environment let me know ? however if you are hybrid the best way to troubleshooting the issue is to contact the dedicated team as mention it above. 

We look forward to your reply.  We will continue to assist you based on the information you provide. I sincerely appreciate your patience and cooperation.  

Sincerely   

Eben Ezer Tres | Microsoft Community Moderator

## Answer (community) — community member

*upvotes: 0 · updated: 2025-03-12*

Apologies for the delay and thanks very much for your response. We do have a hybrid set-up and the group is synced to Azure AD. Our MS Teams experts raised a ticket with Microsoft recently, as this does appear to be an issue without an obvious cause (at the moment) other than starting to be a large group to add each time it's applied (although still well under the limit of ~3,500).   

We've been advised to do some further testing (by setting up a new Team and applying the same group) to see if we can capture some logs to share as part of the analysis of the problem. Will update here if we find a cause/solution.
