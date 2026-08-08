---
title: "tracking read status of email messages in exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1664535/tracking-read-status-of-email-messages-in-exchange
question_id: 1664535
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# tracking read status of email messages in exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1664535/tracking-read-status-of-email-messages-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Currently our organization uses an exchange hybrid cloud model.

We want to track read status of email messages of a specific sender in the system. We tested using a user in the oprem to send to users in the online exchange, however I used the Get-MessageTrace command. -Sender mail@xyz -MessageSubject "abc" -Start (Get-Date).AddHours(-48) -EventId RECEIVE | Select MessageID to get the ID of user mail@xyz but the returned result is none. While it is also the address mail@xyz sent to mails in oprem, we can still use the above command to get the user's MessageID. Please help me regarding this case

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-13*

Hi @Anonymous  

Thank you for your answer, I find it very practical for me

If you need those details on a per-message basis, you could refer EWS Powershell Script to find the ‘True’ Read Status of an email message | Microsoft Learn to get it from a EWS based script. -> However, when I access the Get-ReadStatus.ps1 scripts, I cannot download them

Is there any way you can help me?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-09*

The Get-MessageTrace will not give you the read status of a message, in fact no cmdlet within Exchange Online will, now that they removed Search-Mailbox. You will have to use an EWS or Graph API based solution, for example the Get-MgUserMessage cmdlet:

```
Connect-MgGraph -Scopes Mail.Read
Get-MgUserMessage -UserId ******@domain.com -Filter {sender/emailAddress/address eq 'm365dev@microsoft.com'} -Top 5 | select Subject,IsRead
```
