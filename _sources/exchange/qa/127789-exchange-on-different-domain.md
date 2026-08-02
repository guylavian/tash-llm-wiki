---
title: "Exchange on Different Domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/127789/exchange-on-different-domain
question_id: 127789
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange on Different Domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/127789/exchange-on-different-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am new to my current organization and one of the items I have been tasked with is to research and prep a migration from Exchange 2010 to O365. I have very little experience with Exchange as this is the first position that has required this level of exposure. I am learning it as I go.   

Here is the scenario: The Exchange server is on a separate domain than the production AD installation. The forest (domain) that was created for the sole purpose of installing the Exchange server itself has a routable address for no apparent reason and is also on its own separate internet connection. This was done by a vendor who I believe was in cahoots with an employee who had an interest in keeping the IT staff out of it. Its political and weird. But apparently, that battle has been won by the IT Coordinator.   

One of the symptoms is that when a new email account is added, it must be done on a network outside of the network that the production domain is on. I did a bit of searching and found that this may be due to the new accounts trying to default to the production domain upon first login, especially considering that the Exchange server and DC is already on its own separate network (internet connection). So the IT staff, for 6 years, have had to put the users pc's on a cell phone hot spot for their initial Outlook login. Pretty strange to me.   

The question is two part: What can be done to remedy this? If it is not remedied before the migration, will the issue persist with a hybrid migration?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-16*

Hi @MShen  ,    

One of the symptoms is that when a new email account is added, it must be done on a network outside of the network that the production domain is on.    

May I know the symptom or error if you attempt to add the new email account inside the production domain?     

Would you please run the "Test E-mail AutoConfiguration" inside and outside the production domain network? This can  so that we can view the difference of autodiscover process in both scenarios:    

-   Launch Outlook, hold down CTRL key, right-click the Outlook icon in the system tray and then select “Test Email Autoconfiguration”.    

    

-  Confirm that your email address is in the address field, uncheck “Use Guessmart” and “secure Guessmart authentication” boxes. Then click the “Test” button.    

-  Once it runs, Check the Log tab.    

-  You can post back the outputs after removing the personal information like email address and domain name involved.    

Furthermore, based on my understanding and research, this could be related to the lack of DNS entries for Autodiscover to the Exchange server. Here are two relevant links for your reference:    

 How do you connect Outlook 2016 in one domain to Exchange in a different domain    

 How to setup Outlook 2013 to connect to an Exchange 2013 account in a different domain    

(Please Note: Since the second web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.)    

As per your concern in hybrid migration, as far as I know, in hybrid environment, mailboxes hosted on Exchange 2010 will still connect to the on-premise Exchange server, so chances are that the issue will persists.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
