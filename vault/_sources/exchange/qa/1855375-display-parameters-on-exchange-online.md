---
title: "Display parameters on Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1855375/display-parameters-on-exchange-online
question_id: 1855375
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Display parameters on Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1855375/display-parameters-on-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have migrated from Exchange 2016 to Exchange Online.

In the mailbox view in EAC for both 2016 and Online you can Add/remove columns to customize your view. However it seems to be limited in Exchange Online compared to that in 2016.

In our local AD we use a number of CustomAttributes for our users which are synced to AAD/Exchange, and in 2016 those can be chosen as columns to be displayed, also it's possible to display the HiddenFromAddressListsEnabled property. In Exchange Online however I can't choose those columns. But if I double click a mailbox/user in Exchange Online I can directly see the checkbox for the HiddenFromAddressListsEnabled property and clicking on More options... I can see that the CustomAttributes are visible to Exchange.

I've tried with both the old and the new EAC view for Exchange Online and neither of them allows me to choose those columns to display.

With Powershell and the cmdlet I can get the mailboxes matching the desired criteria, but the new not seem to expose these attributes.`Get-MailboxGet-EXOMailbox does`

`Get-Mailbox -ResultSize Unlimited | Where-Object -FilterScript {$_.HiddenFromAddressListsEnabled -eq 'True'}`

`Get-Mailbox -ResultSize Unlimited | Where-Object -FilterScript {$_.CustomAttribute7 -eq 'Staff'}`

The best would be to be able to display these columns so our support-staff can sort on them if they need to.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-08-05*

Yea, you arent going to get alot of flexibility here with that. powershell is the only way to surface alot of that
