---
title: "Moving mailbox Error -  Exchange 2013 to Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1241201/moving-mailbox-error-exchange-2013-to-exchange-201
question_id: 1241201
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Moving mailbox Error -  Exchange 2013 to Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1241201/moving-mailbox-error-exchange-2013-to-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I am trying to move mailbox from Exchange 2013 to 2019.
One particular mailbox throws me following error while I tried to move it.
None of the other mailbox has any such issue and worked very well.
Note: At very first, while moving mailbox named "accounts", I had a space issue on Exchange2016 (Destination) and hence I have to cancel the migration of this mailbox. I did it by shell command as well EAC.
But then whenever I try to migrate the same mailbox again, it throws me an error for this mailbox only.

```
[PS] C:\Windows\system32>
New-MoveRequest "accounts" -TargetDatabase "Mailbox Database xxxxxxxx"
Cannot open mailbox /o=xxxxxxx/ou=Exchange Administrative Group
(FYDIBOHF23SPDLT)/cn=Configuration/cn=Servers/cn=EX2/cn=Microsoft System Attendant.
    + CategoryInfo          : NotSpecified: (:) [New-MoveRequest], RemoteTransientException
    + FullyQualifiedErrorId : [Server=MAIL1,RequestId=325262a1-e055-4812-9833-077badb50261,TimeStamp=4/17/2023 5:34:17
    AM] [FailureCategory=Cmdlet-RemoteTransientException] 66F6F8F,Microsoft.Exchange.Management.RecipientTasks.NewMov
  eRequest
    + PSComputerName        : mail1.xxxxxxxxx.local
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-18*

Hi @SenkP ,

-  Please follow the steps below to check if the migration arbitration mailbox is running fine:

-  Run the following cmdlet to find out the database which is hosting the Migration arbitration mailbox:
Get-Mailbox -Arbitration | FL NAME,DATABASE

-  Run the cmdlet below to check the status of the database:
Get-MailboxDatabase -Status | fl name,mounted

-  If the database is dismounted, please mount it back and try again to see the result.
Here is a similar thread for your reference: Error while moving mailbox from 2010 to 2016.

-  Since the issue above is related to the System Attendant mailbox, you can try recreating the migration arbitration mailbox and verify the result again.   Step reference: Re-create the Microsoft Exchange Migration mailbox.     Tip of The Day: System Attendant Mailbox and Exchange 2013.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
