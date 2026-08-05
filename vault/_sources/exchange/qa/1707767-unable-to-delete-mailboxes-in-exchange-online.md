---
title: "Unable to delete mailboxes in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1707767/unable-to-delete-mailboxes-in-exchange-online
question_id: 1707767
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Unable to delete mailboxes in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1707767/unable-to-delete-mailboxes-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,

I really need help because we've been struggling this issue for more than 2 months. 

This is happening for the first time. I created an AD User 2 months ago and it created 2 duplicate mailboxes on Exchange Online. I am trying to hide from GAL but it says "Operation failed". I tried to delete the mailbox by using Powershell. But it keeps saying "The operation couldn't be performed because matches multiple entries". I don't know what to do at this point. I also deleted the user from AD completely but that didn't help as well. Mailboxes are still there.

Any solution would be appreciated.

Thank you

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-20*

Hello,

Thank you for posting in Q&A forum.

This issue occurs because there are two or more mailboxes with the same name in Exchange Online.

To delete these duplicate mailboxes, you need to first find their distinguishedName (DN), and then delete them using PowerShell.You can try running a command in PowerShell to solve the issue.

1.Open the Exchange Management Shell (EMS)

2.Run the following command to find mailboxes with the same name:

Get-Mailbox -ResultSize Unlimited | Group-Object -Property UserPrincipalName | Where-Object {$_.Count -gt 1}

This will display all email accounts with the same UserPrincipalName.

3.For each duplicate mailbox, run the following command to get its distinguishedName (DN):

Get-Mailbox -Identity "Mailbox name" | Select-Object -ExpandProperty DistinguishedName

Replace "Mailbox Name" with the actual mailbox name.

4.Delete a mailbox with a specific distinguishedName (DN) using the following command:

Remove-Mailbox -Identity "Mailbox DN" -Confirm: $false

Replace "Mailbox DN" with the actual distinguishedName.

Repeat steps 3 and 4 until all duplicate mailboxes have been deleted.

I hope the information above is helpful.

Best Regards,

Yanhong Liu

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-06-20*

Use the GUID of the mailbox when trying the delete operation.
