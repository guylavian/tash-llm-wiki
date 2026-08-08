---
title: "Exchange 2016 (CU19) New User Address is not visiable in Global Address book"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/345966/exchange-2016-cu19-new-user-address-is-not-visiabl
question_id: 345966
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 (CU19) New User Address is not visiable in Global Address book

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/345966/exchange-2016-cu19-new-user-address-is-not-visiabl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Support  

Created New Mailbox Mail id is not appearing in Global Address book  

When i select All Contacts. it is appearing.  

not   

Even i have updated address book   

get-offlineaddressbook | update-offlineaddressbook  

Update-GlobalAddressList -Identity "Default Global Address List"  

i checked there is no hide from Mailbox feature  

How to fix this?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-04-07*

Hi @Sathishkumar Singh  ,    

Noticed that you've accepted Andy's reply above as Answer, do you mean you've already solved the issue by switching to Exchange Online mode?    

As mentioned by Andy, when you are running Outlook in cached mode, the Global Address Book you see is cached offline and can take hours to update, while the "All Contacts" folder is online and can stay up-to-date. That being said, aside from switching to Online mode or giving it a day, you can also perform a manual download of the offline address book. To do this, follow these steps:    

-  On the ribbon, go to Send/Receive > Send/Receive Groups, and then click Download Address Book.    

    

-  In the Offline Address Book dialog box, make sure that the Download changes since last Send/Receive check box is checked, click OK.    

    

If you would like to learn more about Offline Address Book in Outlook, hopefully you can find the document below helpful:    

Administering the offline address book in Outlook    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
