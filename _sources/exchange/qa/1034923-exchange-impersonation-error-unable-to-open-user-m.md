---
title: "Exchange Impersonation error. Unable to open user mailbox due to impersonation error. Please make sure impersonation is set properly. (11021)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1034923/exchange-impersonation-error-unable-to-open-user-m
question_id: 1034923
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Impersonation error. Unable to open user mailbox due to impersonation error. Please make sure impersonation is set properly. (11021)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1034923/exchange-impersonation-error-unable-to-open-user-m (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to migrate my emails over from Office 365 to Google Workspace. During the migration I get the error: "Exchange Impersonation error. Unable to open user mailbox due to impersonation error. Please make sure impersonation is set properly. (11021)"    

I contacted Google Support and they are saying it is an issue/setting on the GoDaddy/Office 365 side.    

I contacted GoDaddy chat on Friday, they went through some Admin settings with Office 365, then they said they just had to turn SMTP on and it would take up to 24 hours.  On Monday I started the migration again and it still didn't work, the error was the same. I contacted GoDaddy chat once more. The rep gave me their "Migration Team" phone number and said they will do everything for me. I called said number, was on hold for over 2 hours, and finally got a real person. This person didn't quite understand the issue, or the migration, or nearly anything. After spending 30 minutes explaining it to him several times, correcting him several times, and hearing him tell me things that were very untrue I asked if he was the Migration Team. He was not, he was email support, and promised me that Migration Team can not help me because the problem is with Google Workspace.    

Looking for answers online brought me to the response to the same issue answered here », however I am still getting the same error.    

I am really hoping someone can help me with this.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-23*

Did anyone get this resolved? in looking over the docs, it looks like you have to the impersonation role to everyone you are migrating, not just the admin even though it is asking you to assign an admin.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-07-08*

This didn't work for me and i have admin access to my office 365

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-24*

Hey so I did the same thing that you expressed on your response but it gave me this message

Error executing request. You don't have access to create, change, or remove the "NETORGFT5787804.onmicrosoft.com\ApplicationImpersonation-GoogleWorkspace" management role assignment. You must be assigned a delegating role assignment to the management role or its parent in the hierarchy without a scope restriction"
What should I do?
