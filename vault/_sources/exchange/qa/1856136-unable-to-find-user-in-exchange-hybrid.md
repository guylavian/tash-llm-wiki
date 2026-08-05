---
title: "Unable to find user in Exchange hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1856136/unable-to-find-user-in-exchange-hybrid
question_id: 1856136
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Unable to find user in Exchange hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1856136/unable-to-find-user-in-exchange-hybrid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have a single user that was not created correctly in Exchange on-prem. This is causing issues with SMTP mail not routing/failing to deliver to the o365 email.

In our environment, users are created in Exchange on-prem as an "Office 365" mailbox, which then creates the account in Active Directory, and Office 365.

For this user it looks like the user was created in Active Directory First, then the AD Sync synced the account to Office 365. A mail user has been created in exchange on prem, but this doesn't look like it's the solution as all other accounts on prem are "Office 365".

Is there a way to fix the missing "Office 365" account in exchange on prem?

attempted to add

```
PS] C:\Windows\system32>Set-RemoteMailbox $USER -ExchangeGuid $GUIDHERE
The operation couldn't be performed because object '$USER' couldn't be found on 'AD1.DOMAIN.LOCAL'.
    + CategoryInfo          : NotSpecified: (:) [Set-RemoteMailbox], ManagementObjectNotFoundException
    + FullyQualifiedErrorId : [Server=EXCHANGE1,RequestId=c45a6d57-2c60-43d1-a36d-67bbbccc8bcf,TimeStamp=5/19/2020
   10:19:41 PM] [FailureCategory=Cmdlet-ManagementObjectNotFoundException] 1082ECE3,Microsoft.Exchange.Management.Rec
  ipientTasks.SetRemoteMailbox
    + PSComputerName        : EXCHANGE1.DOMAIN.LOCAL
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-08-07*

You need to correctly create the mailbox in Exchange so that it can sync properly with Office 365.

1.       Open EAC and remove the incorrect mail user

2.       Open EMS, convert existing AD user to office 365

3.       In Windows Powershell, run command to force directory sync

4.       Check mailbox is created through EAC

5.       Verify that email flow working properly
