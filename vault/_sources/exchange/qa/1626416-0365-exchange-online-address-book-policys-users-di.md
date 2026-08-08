---
title: "0365/Exchange Online Address Book Policy's Users \"disappearing\" from Address Lists."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1626416/0365-exchange-online-address-book-policys-users-di
question_id: 1626416
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# 0365/Exchange Online Address Book Policy's Users "disappearing" from Address Lists.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1626416/0365-exchange-online-address-book-policys-users-di (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi! I wonder if anyone can cast any insight to address book policies on office365.

So, I've originally set up Custom Address Book polices for schools on 0365. The way I did this was using Groups in on PremAD, then setting those groups as "filters for the GAL / Address List policies". Up until October, this was working as expected.

Around October, there were starting to be reports of people not appearing on the address lists, in Outlook or on o365 - it's eventually made it's way through to me after other have looked at it.  Users have been "tickled" plenty of times.

Basically, the address lists that is shown in 0365/Outlook people have "disappeared" - it's now at the point that there are only 1 or two people in those lists, and I've had to start reverting users back to "no address book policy".

-  The users are still in the AD group.

-  The users are still in the Azure synced AD group (distribution enabled security groups so they appear in Exchange)

-  The address lists are set to with a recipient filter of "The Azure AD Group"

-  When I query the address lists with PowerShell, it seems that the user are "there".

-  But the 0365 and the Outlook Address lists don't show (all) of the users/groups/mailboxes as expected.

Looking further and further into it, there is an attribute that users objects have called AddressListMembership, and where people are being displayed in the ALs, they have as what would be expected, but it seems something might be overwriting that AddressListMembership attribute, with other item config.  This is affecting Users and Distribution Groups in address Lists.

So for an example the two last working staff members i have

{\Default Global Address List, \GAL-SCHOOL, \AL-SCHOOL-All Staff, \All Users…}

Where as another the 55 users not being displayed has

{\Default Global Address List, \All Users, \Offline Global Address List, \All Recipients(VLV)…}

Example code I've used is below to create ...

```
*** Create GAL ***
new-GlobalAddresslist -name "GAL-SCHOOL" -RecipientFilter "MemberOfGroup -eq 'CN=UG-SCHOOL-GAL-All Users and Groups,OU=0365.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=GBRP0000000,DC=PROD,DC=OUTLOOK,DC =COM'"
*** Create OLAB ***
New-OfflineAddressBook -name "OAB-SCHOOL" -AddressLists "GAL-SCHOOL"
*** Create room AL ***
new-addresslist -name "RMAL-SCHOOL-All Rooms" -DisplayName "SCHOOLNAME Rooms" -RecipientFilter "MemberOfGroup -eq 'CN=UG-SCHOOL-RMAL-All Rooms,OU=o365.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=GBRP0000000,DC=PROD,DC=OUTLOOK,DC =COM'"
new-addresslist -name "AL-SCHOOL-All Staff" -DisplayName "SCHOOLNAME All Staff" -RecipientFilter "MemberOfGroup -eq 'CN=UG-SCHOOL-AL-All Staff,OU=o365.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=GBRP0000000,DC=PROD,DC=OUTLOOK,DC =COM'"
new-addresslist -name "AL-SCHOOL-All Groups" -DisplayName "SCHOOLNAME All Groups" -RecipientFilter "MemberOfGroup -eq 'CN=UG-SCHOOL-AL-All Groups,OU=o365.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=GBRP0000000,DC=PROD,DC=OUTLOOK,DC =COM'"
new-addresslist -name "AL-SCHOOL-All Students" -DisplayName "SCHOOLNAME All Students" -RecipientFilter "MemberOfGroup -eq 'CN=UG-SCHOOL-AL-All Students,OU=o365.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=GBRP0000000,DC=PROD,DC=OUTLOOK,DC =COM'"
new-addresslist -name "AL-SCHOOL-All Governors" -DisplayName "SCHOOLNAME All Governors" -RecipientFilter "MemberOfGroup -eq 'CN=UG-SCHOOL-AL-All Governors,OU=o365.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=GBRP0000000,DC=PROD,DC=OUTLOOK,DC =COM'"
SCHOOLNAME Address Book Policy
New-AddressBookPolicy -Name "ABP-SCHOOL-Staff" -AddressLists "AL-SCHOOL-All Staff","AL-SCHOOL-All Students","AL-SCHOOL-All Governors","AL-SCHOOL-All Groups" -OfflineAddressBook "\OAB-SCHOOL" -GlobalAddressList "\GAL-SCHOOL" -RoomList "\RMAL-SCHOOL-All Rooms"
```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-22*

Hi @CT  ,

Run the following command against one of the problematic address list and see if the missing recipients are listed in the output:  

(Note: In Exchange Online, Get-AddressList cmdlet is available only in the Address Lists role, and by default, the role isn't assigned to any role groups. To use this cmdlet, you need to add the Address Lists role to a role group (for example, to the Organization Management role group). For more information, see Add a role to a role group.)  

(Replace "my list" with the name of the address list on your end)

```
$a = get-addresslist "my list" 
Get-recipient -filter $a.recipientfilter
```

If yes, try tickling the object using options provided in the article below and then check if it can make any difference:  

How to view and update address list membership for objects in Exchange Online  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
