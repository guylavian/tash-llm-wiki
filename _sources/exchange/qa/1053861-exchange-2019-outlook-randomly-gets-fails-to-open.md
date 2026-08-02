---
title: "Exchange 2019 Outlook Randomly gets Fails to open, or opens but can't access all mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1053861/exchange-2019-outlook-randomly-gets-fails-to-open
question_id: 1053861
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 Outlook Randomly gets Fails to open, or opens but can't access all mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1053861/exchange-2019-outlook-randomly-gets-fails-to-open (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Running Server: Exchange 2019 on Windows 2019, Client: Win10 Office Latest Version.    

Issue: Outlook in 1 of 2x ways.    

-  Fails to open completely with error: "Cannot start Microsoft Outlook. Cannot open The outlook Window. The Set of folders cannot be opened. the information store could not be opened."    

-  Opens, but not all mailboxes are accessible, with Error:     

either Fails to open, or when it does open not all mailboxes are accessible. (Seemingly Randomly when it works and doesn't work)    

Can happen within Minuets: Open: Fail, 1 min later, Open: Worked, Close, 1 min Later, Open: Fail/or part open    

3 of our Users have this issue.    

All of them have access to 10+ Mailboxes (FullAccess)    

It has been happening more frequently in the past 1-2 Months.    

Error will occur 5-9 times out of 10, other times outlook will open.    

However, sometimes not all Mailboxes are accessable.    

Happens on any computer that user is logged into.    

Also created NEW test account & granted the same mailbox access & same issue eventually occurred.    

That is, Outlook opened fine the first few times, but then errored.    

When Opening Outlook it fails and this error comes on:    

"Cannot start Microsoft Outlook. Cannot open The outlook Window. The Set of folders cannot be opened. the information store could not be opened."    

Outlook Connection Status:    

FULLY WORKING:    

    

Partial Working:    

    

Complete FAIL:

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-20*

Hi @Mr Scaffold Domain Administrator  ,    

Welcome to our forum.    

Through My Search, there is a throttling policy for each client access protocol in Exchange. If users attempt to make more concurrent requests than their policy allows, the new connection attempt fails. However, the existing connections remain valid.     

You can create a new throttling policy and modify the value of the RCAMaxConcurrency parameter, then assign it to the user. For example：    

To create a new throttling policy:    

```
New-ThrottlingPolicy -Name "throttling-policy" -RCAMAXConcurrency: 100
```

Assign to user:    

```
Set-Mailbox -Identity tonysmith -ThrottlingPolicy "throttling-policy"
```

For more details, please refer to:     

new-throttlingpolicy    

change-user-throttling-settings-for-specific-users-exchange-2013-help    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
