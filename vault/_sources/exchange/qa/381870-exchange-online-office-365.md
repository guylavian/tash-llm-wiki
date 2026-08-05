---
title: "Exchange Online + Office 365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/381870/exchange-online-office-365
question_id: 381870
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Online + Office 365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/381870/exchange-online-office-365 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

one of my cutomers has rented exchange online with O365. He has Problems with his email accounts.     

He has configured those mail accounts on many different systems.     

3 PCs and a few mobile devices.     

Its 3 PCs with 3 mailboxes and 3 Phones/iPads. Each of them has all three mailboxes configured     

Now Outlook on some clients can not access the mailbox and displays a waring that the connection could not be established.     

I assume that MS has a hardcoded connection limit inside their exchange?    

I can not get a hold of support by telefon...     

So how do i fix this now?      

Update:     

This is one of the messages i get trying to sync the mailbox:    

    

If i try to open the mailbox within outlook i get a message that the mailbox can not be opened becuase there is no premission to open it     

 Sometimes this works tho ...     

I'll collect another screenshot of this when i speak with my customer    

thx

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-05*

Hi thx for the answers i'll speak to the customer and get more details.   

Its not the software aka. outlook that can't be opened its a mailbox within outlook that can not be accessed.  

Outlook runs just fine with only one mailbox installed but if i add the other two it behaves strangely  

Outlook is also licensed correctly   

Those are full exchange mailboxes and he added them in the accounts tabs. Login is fine even owa works fine too  

He added all three mailboxes on every device he owns so it's maybe 9 or 10 devices that are accessing all of these mailboxes simultaneously.  

I read that exchange online has a hardcoded connection limit of arround 27-30? and each device needs at least 2 connections per mailbox. In this case he would have 19-20 connections open simultaneusly   

thx

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-05*

Hi @BR0KK   ,  

Did you try to log in to the mailbox in OWA?  

All clients have problems logging in? Or is it only the Outlook client on the PC has this problem?

1.What kind of license does the user use? Each license has different restrictions. Such as, if you using the Office for home, you could install Office on all your devices and sign in to Office on five devices at the same time. If you using the office for business, you could install and sign in to Office on 5 PCs or Macs, 5 tablets, and 5 phones.

2.According to research on the error message, this error is more like Outlook client related. Please try to create a new Outlook profile.You could following the steps in the article provided by AlexC-8264.

3.Please make sure that outlook client upgrade to the lastest version.

In addtion, currently in Microsoft Q&A we only support English. So in order to better solve this issue, please provide English version for the error information provided later. Thanks for your understanding.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-04*

Hi BR0KK,    

Have you already found this KBA and tested?    

Error 0x8004010F when you try to send or receive email in Outlook 2010 or Outlook 2013    

https://learn.microsoft.com/en-us/outlook/troubleshoot/synchronization/error-0x8004010f-when-sending-or-receiving-emails

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-04*

you have to narrow down the problem a bit more. The given information is way to general for anyone to be able to help you.  

when you talk about exchange online with 365 i would assume you have a standard M365 E3 Licence, If that's the case you may use Office simultaneously on 5 devices (3 PCS and "a few" phones is more or less than 3 phones?)   

more infos here https://support.microsoft.com/en-us/office/how-sign-in-works-in-microsoft-365-1d646e83-1585-4278-8daf-d4a2cc0905e0#:~:text=With%20Microsoft%20365%2C%20you%20can,Macs%2C%20tablets%2C%20and%20phones.
