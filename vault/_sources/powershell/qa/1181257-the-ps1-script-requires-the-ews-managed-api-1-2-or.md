---
title: "the .ps1 script requires the EWS Managed API 1.2 or later.  but where to find it and hopw to install?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181257/the-ps1-script-requires-the-ews-managed-api-1-2-or
question_id: 1181257
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# the .ps1 script requires the EWS Managed API 1.2 or later.  but where to find it and hopw to install?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181257/the-ps1-script-requires-the-ews-managed-api-1-2-or (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

I have a .ps1 script that I would like to use to get some info from my 365 tenant.

The script returns me this error:

This script requires the EWS Managed API 1.2 or later.
Please download and install the current version of the EWS Managed API from
http://go.microsoft.com/fwlink/?LinkId=255472

but no page at that link.

the statement that gets me this error, I guess, is this:

```
Get-ReadStatus -EmailAddress $MailboxName -Credential $credentials  -MessageID $MessageID -startdate 01/01/2023 -enddate 03/01/2023
```

What do I have to do?

thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-16*

sorted!!!!

it was a permissione issue!

I created an Azure App Registration with following API permissions

```
Directory.Read.All

Mail.ReadBasic.All
```

and it worked!!!!

many thanks!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-16*

That API has been replaced by Microsoft Graph.

You can find the EWS API here: https://github.com/OfficeDev/ews-managed-api but it's a dead-end bit of software.
