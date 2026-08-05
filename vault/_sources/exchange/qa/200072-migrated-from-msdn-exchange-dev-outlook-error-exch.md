---
title: "[Migrated from MSDN Exchange Dev] outlook error exchange must be online or connected after migrate active directory server from 2008 r2 to 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/200072/migrated-from-msdn-exchange-dev-outlook-error-exch
question_id: 200072
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# [Migrated from MSDN Exchange Dev] outlook error exchange must be online or connected after migrate active directory server from 2008 r2 to 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/200072/migrated-from-msdn-exchange-dev-outlook-error-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Note: This case is migrated from MSDN Exchange Server Development forum. Since Exchange Server Development forum mainly discuss issues about Exchange development, and non-developer Exchange has transitioned to Microsoft Q&A for support, we migrated this non-developer question manually to continue the discussion.  

Original Post: https://social.msdn.microsoft.com/Forums/office/en-US/27460162-26ac-4196-8b9a-2eae04d113ed/outlook-error-exchange-must-be-online-or-connected-after-migrate-active-directory-server-from-2008?forum=exchangesvrdevelopment   

hello,  

My problem is my all  users cann't connecte with outlook but can connecte with owa  

infrastructure  

two domain contoller  

exchange server 2013

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-12-16*

What's the detailed version of your Exchange 2013?    

Does the DC with windows server 2008 R2 still exist in the environment?    

Here are some suggestions for you:    

1 > Flush the computer's DNS, then try to create a new Outlook profile to see if user can connect to the mailbox.    

```
ipconfig /flushdns
```

2 > With internal network, we can use the Test E-mail Autoconfiguration to known if Outlook can connect to AD for SCP objects.    

-  Locate the Outlook icon in the notification area, hold the CTRL key, right click the icon, and then click Test E-mail AutoConfiguration.    

-  Enter the user's email address, only choose Use AutoDiscover.     

    

-  View the result on the Log tab.    

You can post the screenshot of the Log page, and don't forget to cover the email address and domain name.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
