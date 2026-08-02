---
title: "Primary Domain Controller Domain Passwords are not asking for change password (Windows 2012)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/597486/primary-domain-controller-domain-passwords-are-not
question_id: 597486
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Primary Domain Controller Domain Passwords are not asking for change password (Windows 2012)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/597486/primary-domain-controller-domain-passwords-are-not (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All    

My Current Infra    

1-Primary Domain Controller    

1-Secondary Domain Controller + File Server    

2-RODC    

-  UK-RODC    

-  Dubai-RODC (Powered Off) No more Office    

2 Child Domain    

1 Exchange Server 2016 (CU21)    

DB01    

DB02    

Child Domain Users are getting a report when i run above the script. But Primary Domain Controllers Domain Users not get reports of their password expired.    

When i checked there is no changes on Grain fine password .This is strange what could be cause password reminders are not asking for users.    

Note :- there is no tick option password never expire has been set. every 62 Days password expire should notified. since March 2021 , We having this issue. really strange    

    

Can you advise what command to check that issue?    

Get-ADUser -filter {Enabled -eq $True -and PasswordNeverExpires -eq $False} –Properties "DisplayName", "msDS-UserPasswordExpiryTimeComputed" |Select-Object -Property "Displayname",@{Name="ExpiryDate";Expression={[datetime]::FromFileTime($_."msDS-UserPasswordExpiryTimeComputed")}} | Export-Csv C:\YYYY-MM-DD_Client_AD_Users.csv

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-21*

Any feedback about this issue?
