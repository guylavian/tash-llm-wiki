---
title: "Hybrid Exchange: User created - but mailbox is created in cloud due to script error - how to connect to identity"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/111560/hybrid-exchange-user-created-but-mailbox-is-create
question_id: 111560
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Hybrid Exchange: User created - but mailbox is created in cloud due to script error - how to connect to identity

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/111560/hybrid-exchange-user-created-but-mailbox-is-create (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

i am just curious if this is working. We have hybrid setup and create AD users by script and then enable-remotemailbox.  

But if the script fails the users gets a mailbox created in the cloud without a "hybrid identity" after the next sync and after assigning a license.  

Is there any way to stop this behaviour or how can we connect an existing "cloud mailbox" to an onprem identity?  

Best regards  

Stephan

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-29*

To stop the behavior, do not add a license to a 365 account unless the remote mailbox is created and sycned. The script will need to have some steps in their to catch that when it fails.    

Alternatively, In this scenario, you can still create a remote mailbox after the fact. It will provision it and will link to the on-prem account based on the source anchor.     

https://learn.microsoft.com/en-us/azure/active-directory/hybrid/plan-connect-design-concepts    

After you create the remote mailbox, get the ExchangeGuid of the mailbox in Office 365 following this article:    

https://support.microsoft.com/en-us/help/2956029/migrationpermanentexception-cannot-find-a-recipient-that-has-mailbox-g    

Connect to Exchange Online Powershell:    

```
Get-Mailbox  | Format-List ExchangeGUID
```

Run the following command to set the value of the ExchangeGUID property on the on-premises remote mailbox to the value that you retrieved above    

```
Set-RemoteMailbox  -ExchangeGUID 
```

Force directory synchronization.     

Thats it. You are done!
