---
title: "Customize Exchange 2013 mailbox size warning message"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2810385/customize-exchange-2013-mailbox-size-warning-messa
question_id: 2810385
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Customize Exchange 2013 mailbox size warning message

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2810385/customize-exchange-2013-mailbox-size-warning-messa (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We ran the following command to change the default Exchange 2013 mailbox size warning message.

New-SystemMessage -QuotaMessageType WarningMailbox -Language en -Text "Your mailbox has exceeded the warning limit specified by your email administrator. Please reduce the size of your mailbox."

If we run the Get-SystemMessage we the updated message in the list.

But when the email is sent each night we get the default message.

Your mailbox is becoming too large. The current size is 1027 MB.

Please reduce your mailbox size by deleting items you don't need from your mailbox and emptying your Deleted Items folder.

I'm not sure what step we are missing.

Any help would be greatly appreciated.

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2018-05-09*

Hi,

Your question is outside the scope of this Community.

I suggest that you repost your Question in the TechNet Exchange Forums.

https://social.technet.microsoft.com/Forums/exchange/en-us/home?category=exchangeserver

And/or here:

https://social.technet.microsoft.com/Forums/exchange/en-US/home?forum=exchangesvrgeneral

TechNet Server Forums. 

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

Or MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
