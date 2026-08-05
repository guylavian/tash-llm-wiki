---
title: "Exchange 2016 cu22 upgrade to CU23 Failed on Mailbox Role - Cannot find Arbitration Mailbox"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1345184/exchange-2016-cu22-upgrade-to-cu23-failed-on-mailb
question_id: 1345184
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 cu22 upgrade to CU23 Failed on Mailbox Role - Cannot find Arbitration Mailbox

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1345184/exchange-2016-cu22-upgrade-to-cu23-failed-on-mailb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to update our Exchange 2016 CU22 to CU23.  Everything was going fine, Mailbox role: mailbox service failed.  Trying to read the exchangesetup.log I'm finding Cannot find arbitration mailbox with name-$name.   Trying to google solutions.  One possible solution says to recreate arbitration mailbox, but commands such as : get-mailboxdatabase | format-Table Name, Guid returns : The Term Get-Mailboxdatabase is not recognized.  

We currently are running a Hybrid, and all users are already on O365, and before this update everything was fine except local server was on CU22.   I could be reading this entire log file incorrectly, here is a snip of the log that I believe helps to assist in the error . 

08/13/2023 03:40:40.0097] [2] Preparing to output objects. The maximum size of the result set is "1".

[08/13/2023 03:40:40.0098] [2] Ending processing Get-User

[08/13/2023 03:40:40.0098] [2] Beginning processing Write-ExchangeSetupLog

[08/13/2023 03:40:40.0100] [2] Cannot find arbitration mailbox with name=SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}.

[08/13/2023 03:40:40.0100] [2] Ending processing Write-ExchangeSetupLog

[08/13/2023 03:40:40.0101] [1] The following 1 error(s) occurred during task execution:

One article I read suggested installing the ExchangeOnlineManagement module, then I should have access to the commands I'm trying to run, but I'm not sure if I'm going to make matters worse.  

Suggestions or assistance in this issue would greatly be appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-08-16*

According to error messages, you may need to recreate Arbitration Mailboxes.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-08-14*

Hi @DonS ,

Thanks for posting in our Q&A forum.

From Exchange 2016 CU8 and later, there are seven arbitration mailboxes. According to the error messages, it seems related to cannot find the SystemMailbox{bb558c35-97f1-4cb9-8ff7-d53741dc928c}.

You can try the following steps to fix this issue. 

1.Use the below cmdlet to check if there is the specific missing arbitration mailboxes in our Exchange organization.

```
Set-ADServerSettings -ViewEntireForest $true; Get-Mailbox -Arbitration | Format-Table Name, ServerName, Database, AdminDisplayVersion
```

2.Check Exchange arbitration mailboxes in Active Directory Users and Computers. If it is not present there, then try to recreate the object. https://www.alitajran.com/recreate-arbitration-mailboxes-in-exchange-server/

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
