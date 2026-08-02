---
title: "Why is exchange custom retention policy changing back to previous policy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1839701/why-is-exchange-custom-retention-policy-changing-b
question_id: 1839701
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Why is exchange custom retention policy changing back to previous policy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1839701/why-is-exchange-custom-retention-policy-changing-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I setup a custom retention policy, however after an hour or so, the retention policy is changing back to the previous policy. Any idea why this could happen? I have set the retention policy a few times via Powershell and it keeps reverting back.

-  I should add that the mailbox is currently full which is why I am applying a new policy to make space. Mailbox is currently unusable.

Custom:

```
Name                 RetentionPolicyTagLinks
----                 -----------------------
15 Month Delete      {15 Month Delete - All, Junk Email - 7 Day, Deleted Items - 30 Day}
```

Reverting back to:

```
Name                 RetentionPolicyTagLinks
----                 -----------------------
Company MRM Policy   {1 Year Delete}
```

Tried to manually force policy onto mailbox

```
Powershell>Start-ManagedFolderAssistant -Identity "******@domain.com"
Powershell>
Powershell>
Powershell>
Powershell>Get-MailboxFolderStatistics "******@domain.com" -FolderScope Inbox | Format-Table Name,FolderPath,ItemsInFolder,FolderAndSubfolderSize

Name                 FolderPath            ItemsInFolder FolderAndSubfolderSize
----                 ----------            ------------- ----------------------
Inbox                /Inbox                       177017 84.44 GB (90,667,087,358 bytes)
....
```

Also tried using compliance search + action

```
Powershell>New-ComplianceSearch -Name "Remove older than 15 month messages" -ExchangeLocation "******@domain.com" -ContentMatchQuery "(Received New-ComplianceSearchAction -SearchName "Remove older than 15 month messages" -Purge -PurgeType SoftDelete

Confirm
Are you sure you want to perform this action?
This operation will make message items meeting the criteria of the compliance search "Remove older than 15 month messages" completely inaccessible to users.
 is no automatic method to undo the removal of these message items.
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [?] Help (default is "Y"): A

Name                                      SearchName                          Action RunBy       JobEndTime Status
----                                      ----------                          ------ -----       ---------- ------
Remove older than 15 month messages_Purge Remove older than 15 month messages Purge  adminuser              Starting
```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-25*

Hi, @TomCruise-7376

Thanks for posting your question in the Microsoft Q&A forum.

Could you try to assign the retention policy in EAC and check if this issue continues?

Running Start-ManagedFolderAssistant after you assign the retention policy to users. Then confirm if the issue still persists.

In addition, does this issue occur to all users or the specific user?
