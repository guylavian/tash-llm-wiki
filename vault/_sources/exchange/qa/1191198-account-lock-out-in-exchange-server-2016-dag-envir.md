---
title: "Account lock out in Exchange server 2016 DAG environment with AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1191198/account-lock-out-in-exchange-server-2016-dag-envir
question_id: 1191198
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Account lock out in Exchange server 2016 DAG environment with AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1191198/account-lock-out-in-exchange-server-2016-dag-envir (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Tracing account lock out by event viewer shows that IP source is Exchange server or domain controller. Tracking done by event 4740. Accounts are continuously being locked out how can we trouble shoot this further I used Microsoft Account lockout tool but it has very limited information about source IP

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-20*

Hello there,

I'd recommend going into your IIS logs and finding the timestamp of that event to locate the IP address. Check to make sure Pop3 / IMAP hasn't been enabled in exchange, for an old phone or such.

A lot of the lockouts will be cached credentials in windows in credential manager. You can try to remove the local Windows credentials and see if the problem persists.

Copy the below line

rundll32.exe keymgr.dll,KRShowKeyMgr

Windows Key+R > CTRL+V to paste the above-copied line and Enter

Here you can delete the stored passwords

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-03-20*

Hello @azhar Nasim

Thank you for using Q & A forum.

This event ID will contain the source computer of the lockout. 

Refer to the below link solution already provided.

Using PowerShell to Find the Source of Account Lockouts

-  Open the Group Policy Management console. This can be from the domain controller or any computer that has the RSAT tools installed.

-  Modify the Default Domain Controllers Policy

If this answers your query, do click `Accept Answer` and Up-Vote for the same. And, if you have any further query do let us know.
