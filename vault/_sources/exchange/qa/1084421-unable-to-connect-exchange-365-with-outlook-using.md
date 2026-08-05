---
title: "unable to connect exchange 365 with outlook using ONLINE mode. Can connect in cached mode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1084421/unable-to-connect-exchange-365-with-outlook-using
question_id: 1084421
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
---
# unable to connect exchange 365 with outlook using ONLINE mode. Can connect in cached mode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1084421/unable-to-connect-exchange-365-with-outlook-using (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

was working until today,    

Getting error now of     

Cannot start outlook. cannot open outlook window. the set of folders cannot be opened. The information store cannot be opened.    

works fine if I turn on cached mode.     

no matter what machine on or off network, new profile/ reset nave pane/ none of the suggestions help.    

users mailbox is around 18gig with a premium 365 account. has about 100 folders in mailbox.    

trying to find out if there is some sort of Limit for outlook in online mode.    

any ideas would be most welcomed.  ( needs to be in online mode due to Remote desktop FYI. cannot be configured for cache mode for this user)    

Latest version of office 365 installed

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-16*

Hi @David A. Wenzel      

The Error,  “Cannot start Outlook. cannot open outlook window. the set of folders cannot be opened. The information store cannot be opened” generally occurs when the Outlook data file is corrupted. For the OST file, remove it or rename that OST file for the backup and Let’s start Outlook again. The new OST file will automatically replace the corrupted file.      

drive:\Users\user\AppData\Local\Microsoft\Outlook.     

For the PST file, you can use the scanPST.exe (Inbox repair tool) to repair the corrupt PST file.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-11*

Hi @David A. Wenzel   ,    

You could try the following methods:    

-  Repair Outlook Data Files (.pst and .ost)    

-  Open Outlook in safe mode and disable all add-ins. If Outlook works well in safe mode, then this issue is caused by add-ins.     

To open Outlook in safe mode, right-click the Start button > click Run > type Outlook.exe /safe, and click OK.     

-  You could Try guided support    

You could refer to the following steps for details:    

https://support.microsoft.com/en-us/office/i-can-t-start-microsoft-outlook-or-receive-the-error-cannot-start-microsoft-outlook-cannot-open-the-outlook-window-d1f69da6-b333-4650-97bf-4d77bd7abb85    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
