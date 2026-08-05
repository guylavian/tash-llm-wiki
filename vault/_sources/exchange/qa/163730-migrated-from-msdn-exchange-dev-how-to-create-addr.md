---
title: "[Migrated from MSDN Exchange Dev] How to create address list for each OU and make it visible only to users in that OU only??!!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/163730/migrated-from-msdn-exchange-dev-how-to-create-addr
question_id: 163730
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] How to create address list for each OU and make it visible only to users in that OU only??!!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/163730/migrated-from-msdn-exchange-dev-how-to-create-addr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/532ee849-347d-4f67-ae04-41e2b1b1b495/how-to-create-address-list-for-each-ou-and-make-it-visible-only-to-users-in-that-ou-only?forum=exchangesvrdevelopment&prof=required  

Dears,  

Hope everything is ok.  

I need to create multiple address lists for some departmental OUs and I need the users to see only their perspective address list content. (In other words the users can see only their belonging address list in the address book so all other information are hidden)  

Thanks  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-16*

Which version of Exchange are you using?  

This is for Exchange 2013 or later:  

(if you are using Exchange 2010, you should create GAL and address list via powershell with "-recipientcontainer", if you are using Exchange 2007 or earlier, the parameter "-recipientcontainer" does not work thus you get error in first step)

1.Create an address list contains users in a specific OU.  

Navigate to Organization > Address lists, and then click Add Icon.  

Type a name, choose 'All Recipient types'  

Click Add a rule, choose recipient container, and choose that specific OU.  

Click Save to create this address list.  

In the details pane, click Update.

2.Create a new GAL with none users and update GAL. We can only modify the GAL via command.  

New-GlobalAddressList NewGAL  

Update-GlobalAddressList NewGAL

3.Create a Offline address book, type the name of address created in step1.  

New-OfflineAddressBook -Name "New" -AddressLists "\Address list name"

4.Create a room list or you can use the default room list (I suggest to use the default one, if you don't have restriction to room mailbox for users in that OU)

5.The last step is to create the address book policy. All steps above are for this address book policy because an address book policy contains at least one GAL, one OAB, one address list, one room list.  

New-AddressBookPolicy PolicyName -AddressLists "\Address list name in step1" -OfflineAddressBook NewOAB -GlobalAd  

dressList NewGAL -RoomList "\all rooms"

6.Then assign this address book policy to users in that OU via EAC or EWS. It's easy to use command

Get-Mailbox -OrganizationalUnit "OU name" | Set-Mailbox -AddressBookPolicy "PolicyName"

Reference link: https://social.technet.microsoft.com/Forums/lync/en-US/25467d5d-2baa-4587-893a-6750e0802257/assigning-an-address-book-to-an-organizational-unit-in-exchange-2013?forum=exchangesvrgeneral

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
