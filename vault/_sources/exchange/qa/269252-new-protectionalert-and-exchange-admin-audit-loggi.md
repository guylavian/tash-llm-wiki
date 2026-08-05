---
title: "New-ProtectionAlert and Exchange Admin Audit Logging"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/269252/new-protectionalert-and-exchange-admin-audit-loggi
question_id: 269252
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# New-ProtectionAlert and Exchange Admin Audit Logging

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/269252/new-protectionalert-and-exchange-admin-audit-loggi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to solve a problem for the following scenario.    

I need to be able to alert when all of my users except administrators issue a Set-DistributionGroup command.  Since the M365 Protection alert policies don't include that as an operation/activity to alert on I have tried setting my own operation via PowerShell using:    

New-ProtectionAlert -Name "SetDL"  -Operation Set-DistributionGroup -ThreatType Activity -Category Others -AggregationType None -Filter "Activity.UserId -ne 'admin1@keyman  .com' -or 'admin2@keyman  .com'" -NotifyUser alertuser@keyman  .com    

The filter is based on the OPath syntax and filterable properties listed here    

The good news is that this does indeed create an alert when a user runs the Set-DistributionGroup command.  The bad news is that the filter doesn't work so I'm also alerted when admin1@keyman  .com or admin2@keyman  .com runs the command which I'm trying to avoid.    

Has anyone run into this scenario and managed to get the filter properties to work for this type of operation? Or have a different approach to tackling this?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-12*

Hi, @Jay Scovill       

Instead of -or, would you try with -and and see if it works for you?    

```
New-ProtectionAlert -Name "SetDL" -Operation Set-DistributionGroup -ThreatType Activity -Category Others -AggregationType None -Filter "Activity.UserId -ne '******@domain.com' -and Activity.UserId -ne '******@domain.com'" -NotifyUser ******@domain.com
```

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-11*

Your filter seems off, you can try something like this instead:  

```
-Filter "Activity.UserId -ne '******@domain.com' -or Activity.UserId -ne '******@domain.com'"
```
