---
title: "PS Script to Get Members of a DL group in Exchange Online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2154032/ps-script-to-get-members-of-a-dl-group-in-exchange
question_id: 2154032
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# PS Script to Get Members of a DL group in Exchange Online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2154032/ps-script-to-get-members-of-a-dl-group-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to get the list of DL groups user is member of in O365. I'm using below PS Script but I'm getting the error message.

$user = "******@rheem.com" $dlGroups =Get-DistributionGroup | Get-DistributionGroupMember | Where-Object {$_.PrimarySmtpAddress -eq $userEmail}

foreach($dl in $dlGroups){ Write-Output $dl #Remove-DistributionGroupMember -Identity $dl.Identity -Member $user

}

error:

Write-ErrorMessage : ||The operation couldn't be performed because 'Bus Training School' matches multiple entries.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-02-06*

The error occurs because multiple groups have the same name. In such cases, you need to use a unique property, such as the primary SMTP address, to identify the group. You can use the below script:

```
Connect-ExchangeOnline
$UserEmail = 
Get-DistributionGroup -ResultSize Unlimited | Where-Object { 
    (Get-DistributionGroupMember -Identity $_.PrimarySmtpAddress -ResultSize Unlimited).PrimarySmtpAddress -contains $UserEmail 
} | Select Name, PrimarySmtpAddress
```

Replace the <MemberEmail> with a respective user.

The above script will retrieve all DLs a user is memberof. If you want to find for multiple users, you can use the script available here: https://o365reports.com/2022/04/19/list-all-the-distribution-groups-a-user-is-member-of-using-powershell/
