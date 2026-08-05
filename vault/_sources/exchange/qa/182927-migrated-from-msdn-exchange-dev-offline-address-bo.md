---
title: "[Migrated from MSDN Exchange Dev]Offline address book is not working"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/182927/migrated-from-msdn-exchange-dev-offline-address-bo
question_id: 182927
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev]Offline address book is not working

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/182927/migrated-from-msdn-exchange-dev-offline-address-bo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note] This thread was originally posted on MSDN. As the MSDN Exchange Dev forum mainly focuses on developing issues and the TechNet Exchange forums for general questions have been locked down, we manually migrated this one to Microsoft Q&A platform to continue the troubleshooting.

Dear All,

My Offline address book is not working after Migration from Exchange server 2013 to 2016 recently,

getting the below error while trying to download Offline Address Book

Task 's*****l@*****.com' reported error (0x8004010F) : 'The operation failed. An object cannot be found.'

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-02*

Hi,  

Only one user have this issue or all users have?  

Please check the related settings of OAB according to the following settings:  

1.Please run the following command to update the offline address book and try to download again.

```
Get-OfflineAddressBook | Update-OfflineAddressBook
```

2.Please hold down the ctrl key and right-click the small Outlook icon, click "Test email auto configuration" to check whether the Autodiscover service is running normally.  

  

3.Please run the following command to check the settings of OAB virtual directory:

```
Get-OabVirtualDirectory | fl name, *URL*
```

4.Please run the following command to check the setting of OAB:

```
Get-OfflineAddressBook | fl
```

5.Please run the following command to make sure the organization mailbox is exist:

```
Get-Mailbox -Arbitration | where {$_.PersistedCapabilities -like “*OAB*”} | ft Name, Servername, Database
```

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
