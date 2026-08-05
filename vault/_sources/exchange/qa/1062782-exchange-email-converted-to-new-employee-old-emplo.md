---
title: "Exchange Email converted to new employee, old employee still recieving emails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1062782/exchange-email-converted-to-new-employee-old-emplo
question_id: 1062782
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Email converted to new employee, old employee still recieving emails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1062782/exchange-email-converted-to-new-employee-old-emplo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am a one man business so I manage my own emails through Exchange.  I have a previous employee who I no longer need to have an email address.  I have a new employee, so I just changed the details on the old email account to the new employees information and it works fine for the new employee.    

Problem is, the old employee is still getting those emails on their iPhone (not on their PC) even though the account on the iPhone has been deleted.    

I cannot find any settings that are still showing the old employees information anywhere.    

How can I stop the old employee from getting the new employees email?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-26*

Hi @Joseph Winslow      

According to my research, this seems to be an expected behavior. You could consider using the methods below to wipe the old device:    

In the EAC, navigate to Recipients > Mailboxes.    

Select the user, mailbox features > and under Mobile Devices, choose View details.    

On the Mobile Device Details page, select the lost mobile device, and then select Wipe Data (or Account Only Remote Wipe Device if desired).    

Select Save.    

A related thread here discussed the similar question for your reference: Exchange mobile devices still getting email after password reset    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
