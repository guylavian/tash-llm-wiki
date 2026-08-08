---
title: "Why is the GAL not updating on Exchange Server 2016?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/412757/why-is-the-gal-not-updating-on-exchange-server-201
question_id: 412757
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Why is the GAL not updating on Exchange Server 2016?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/412757/why-is-the-gal-not-updating-on-exchange-server-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been adding users and mailboxes but the global address list is not updating. The users show up on All Users but not the GAL. When I try to download the default global address list I get an error (0x8004010F): The operation failed. An object cannot be found. I have inherited this Exchange server from a prior tech and am not sure what is wrong.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-28*

Hi @DarthZtech  ,

The users show up on All Users but not the GAL.

Did you check it via Outlok which is running in Exhcange cached mode?  

If this is the case, please follow the steps below and see it the error persists:

1.Open EMS, run the following commands:

```
Get-GlobalAddressList | Update-GlobalAddressList  
Get-OfflineAddressBook | Update-OfflineAddressBook
```

2.Try again in Outlook and check if the updated OAB can be downloaded properly:  

3.If the above doesn't work, it's suggested to try createing a new OAB, assign it to one of the affected user mailboxes, wait for a few hours or creating a new Outlook profile for the user to check the result:

```
New-OfflineAddressBook -Name "Test" -AddressLists "\Default Global Address List"  
Set-Mailbox -Identity user1 -OfflineAddressBook "TEST"
```

If the new OAB works for the user, chances are that the issue is due to the corrupted default OAB used earlier, then you can assign the new OAB to the mailbox databases and then reset IIS for the change to take effect:

```
Get-Mailboxdatabase | Set-MailboxDatabase -OfflineAddressBook "Test”  
Get-MailboxDatabase | Ft Name, *book*  
Set-OfflineAddressBook -Identity "Test" -VirtualDirectories $null -GlobalWebDistributionEnabled $true
```

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
