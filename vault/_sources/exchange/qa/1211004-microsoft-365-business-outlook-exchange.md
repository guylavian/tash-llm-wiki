---
title: "Microsoft 365 business 版本Outlook配置本地Exchange邮箱后个人日程安排可见，会议室日程不可见。"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1211004/microsoft-365-business-outlook-exchange
question_id: 1211004
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# Microsoft 365 business 版本Outlook配置本地Exchange邮箱后个人日程安排可见，会议室日程不可见。

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1211004/microsoft-365-business-outlook-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Microsoft 365 business 版本Outlook配置本地Exchange邮箱后个人日程安排可见，会议室日程不可见。

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-11*

Hi @李璕旸 ,  

Since our forum mainly provides technical support in English, in order to avoid misunderstanding, it is recommended that you post in English. Thank you for your understanding.  

According to machine translation, your question is as follows: Microsoft 365 business version Outlook is visible for personal schedule and not for meeting room schedule after configuring local Exchange mailbox.  

   

Let me confirm with you first, have you entered the room mailbox to view the calendar through the room's account which has been delegated to?

-  If you didn't add the event in OWA, add it and see if it appears in Outlook after a few minutes.

-  If you can view rooms in OWA, please check out this post for Outlook desktop client setup. Try turning off the Shared Calendar Improvements option to see if that helps.

-  If both have this problem, please check the room mailbox to see if a delegate is set up to accept or decline booking requests.     If it's not set to auto-accept, the person who is having permission to that room mailbox manually has to accept the meetings.

You can change the book delegates section of room mailbox to Auto-Accept from the EAC or via a PowerShell command to determine if the issue is due to the delegate not accepting the meeting.

```
Set-MailboxCalendarSettings “RoomMailbox” -AutomateProcessing:AutoAccept
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
