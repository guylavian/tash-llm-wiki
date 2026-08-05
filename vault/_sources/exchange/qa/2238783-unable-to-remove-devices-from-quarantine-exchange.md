---
title: "Unable to remove devices from quarantine (Exchange)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2238783/unable-to-remove-devices-from-quarantine-exchange
question_id: 2238783
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to remove devices from quarantine (Exchange)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2238783/unable-to-remove-devices-from-quarantine-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

Please i need your help on this issue.

We are Unable to remove devices from quarantine (Exchange).

Unable to allow quarantined devices.  I select, press Allow, they stay on the list.  Have tried different browsers and Powershell commands.  The devices remain blocked.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2025-03-25*

Thanks for posting your question in the Microsoft Q&A forum.

Sometimes, the ActiveSyncAllowedDeviceIDs and ActiveSyncBlockedDeviceIDs parameters are not cleared properly. You can manually set these parameters to $null using PowerShell:

```
Set-CASMailbox -Identity  -ActiveSyncAllowedDeviceIDs $null -ActiveSyncBlockedDeviceIDs $null
```

** Please don't forget to close up the thread here by upvoting and accept it as an answer if it is helpful **

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-26*

Hi @James James,  

Welcome to the Microsoft Q&A platform!  

You can also try using Remote Wipe, which deletes all user data from the mobile device the next time the device receives data from Microsoft Exchange server.

```
Clear-MobileDevice -Identity  -NotificationEmailAddresses "admin@example.com"
```

https://learn.microsoft.com/en-us/powershell/module/exchange/clear-mobiledevice?view=exchange-ps

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
