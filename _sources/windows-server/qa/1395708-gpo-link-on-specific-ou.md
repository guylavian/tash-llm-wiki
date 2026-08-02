---
title: "GPO Link on specific OU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1395708/gpo-link-on-specific-ou
question_id: 1395708
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO Link on specific OU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1395708/gpo-link-on-specific-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I created a GPO and I I would that the admin group which have permissions on it can link it on specific OU and prevent to link on the others.

Do you have any method please?

By advance Thank you.

Mohamed SAKHO

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-02*

Hello

To link a Group Policy Object (GPO) to a specific Organizational Unit (OU) and prevent it from being linked to others, you can follow these steps:

Create the GPO: If you haven’t already, create the GPO that you want to link.

Link the GPO to the Specific OU: Navigate to the desired OU in the Group Policy Management Console. Right-click on this OU and select “Link an Existing GPO”. In the “Select GPO” dialog under Group Policy Objects, select the GPO you want to link and click OK.

Set Permissions: To prevent others from linking this GPO to other OUs, you need to set permissions on the GPO. In the Group Policy Management Console, navigate to the GPO, right-click on it and select “Delegate”. In the Delegation tab, click on “Add” to add the admin group. In the permissions box, select “Deny” for the “Link GPO” permission. This will prevent members of this group from linking the GPO to other OUs.

Please note that only users with appropriate permissions can create and manage GPOs. Also, changes made to GPOs can affect all users and computers in the domain, so it’s important to plan and test changes carefully.
