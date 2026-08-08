---
title: "Add second mailbox to existing exchange outlook profile via GPO (on-prem)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1289834/add-second-mailbox-to-existing-exchange-outlook-pr
question_id: 1289834
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# Add second mailbox to existing exchange outlook profile via GPO (on-prem)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1289834/add-second-mailbox-to-existing-exchange-outlook-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear guys,

hope everything is fine.

Need your expertise for the above question.

Background:  

All users have a default Outlook profile which is deployed using "ZeroConfigExchange" via GPP. Now we need to add a second mailbox to the same profile because we want to use the calendar reminder feature for the second mailbox (which is obviously not possible with the auto mapped mailbox). As far as I know, the reminder function works only with mailboxes configured in the outlook profile.

Unfortunately I have no idea how to set a second mailbox in an existing profile via GPO (we would like to avoid a manual setup). An online search could not help me either.

I hope someone can help

Thank you so much!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-24*

Hi @TomD,

To my knowledge it is not possible to archive this with ZeroConfigExchange, as this feature only creates an Outlook profile with the corresponding mailbox (email address) of the user account in Active Directory.

Thus there is no method to specify a secondary mailbox to be added to the profile.

To me you may have to have users manually add the secondary mailbox as automapping does not work in this case.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
