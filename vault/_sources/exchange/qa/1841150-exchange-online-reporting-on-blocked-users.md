---
title: "Exchange Online - Reporting on blocked users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1841150/exchange-online-reporting-on-blocked-users
question_id: 1841150
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Online - Reporting on blocked users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1841150/exchange-online-reporting-on-blocked-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There is a feature in Exchange Online which blocks users from being able to send email when they send too many emails in a time period. It usually triggers either when a user sends a load of emails via Mail Merge or when their account gets compromised and it's used to send a load of spam.

You can view which accounts have been blocked from sending either by going to the Restricted Users page in the Defender Security Portal or by running the cmdlet in the Exchange Online EXO PowerShell Module.`Get-BlockedSenderAddress`

The trouble is, these only show the users who are currently blocked. I have been asked by my employer to produce a report on who has been blocked in the last n days. I've looked at the reports in the Defender portal and there isn't one that does exactly that. I'm wondering if this kind of data is kept and if so, how I can extract it?

Thanks in advanced for any help.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-26*

Hi，

Thanks for posting your question in the Microsoft Q&A forum.

You want a report of which users have been blocked in the last N days, here is what I suggest:

Check it in Report > Email & collaboration > Compromised users. You can see the compromised(Suspicious or Restricted) users report in the last 90 days. URL: https://security.microsoft.com/reports/CompromisedUsers

For more information about this: https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/view-email-security-reports?view=o365-worldwide#compromised-users-report

If my answer is helpful to you, please mark it as the answer so that other users can refer to it. Thank you for your support and understanding.
