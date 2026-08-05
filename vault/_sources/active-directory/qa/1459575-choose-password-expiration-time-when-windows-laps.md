---
title: "Choose password expiration time when Windows LAPS store password in Entra ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1459575/choose-password-expiration-time-when-windows-laps
question_id: 1459575
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Choose password expiration time when Windows LAPS store password in Entra ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1459575/choose-password-expiration-time-when-windows-laps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We just begin to migrate from Legacy LAPS to Windows LAPS and we choose to store password on Entra ID.

With LAPS Legacy we could set password expiration time, while with passwords on Entra ID it seems we can just rotate according to our policy. Is there a way to set custom password expiration time?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-12-11*

@Castagnet judicael,Thanks for posting Q&A.

From your description, I know that you want to set custom password expiration time when using Windows LAPS.

Based on my researching, I find that you can custom password expiration time in Intune. You can configure Password Age Days in Endpoint security > Account protection > Windows 10 and later as Platform, Local admin password solution (Windows LAPS) as Profile > Configuration settings.

Hope above information can be helpful.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-12-09*

Hi @Cicindela31  

You can use the following command  :

```
Set-LapsADPasswordExpirationTime -Identity MachineName -WhenEffective (Get-Date -Date "07/04/2024 12:00:00")
```

To get more details about this Powershell command please read the following article:

Set-LapsADPasswordExpirationTime

Please don't forget to accept helpful answer
