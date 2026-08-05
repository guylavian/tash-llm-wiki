---
title: "Exchange Active sync"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1017332/exchange-active-sync
question_id: 1017332
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange Active sync

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1017332/exchange-active-sync (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello    

I have Exchange 2019 and i want a policy to deny some users to access Activesync by their mobiles from outlook native applications.    

Thanks

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-22*

Did you go through with these articles?    

https://learn.microsoft.com/en-us/exchange/create-or-modify-a-mobile-device-mailbox-policy-exchange-2013-help?redirectedfrom=MSDN    

https://msexchangeguru.com/2017/10/26/exchange-2016-mobile-device/

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-22*

Hi     

You can use Allow/Block/Quarantine list function to accomplish your requirement. You can use EAC and follow the below steps to complete the configuration:    

- 	Log on EAC    

- 	Click “mobile” then choose “mobile device access” and click “+” below “Device Access Rules”    

- 	Click “browse” to choose “All families” of the ”Device family”, then choose “Quarantine - Let me decide to block or allow later”, last click “save”.    

- 	After the next time the user want to log on the Outlook application on mobile, it is need your approval. To the users you do not want them to log on ,you can reject them to log on.    

For more information about “Allow/Block/Quarantine list” ,you can reference this Microsoft Blog:588930    

If this Answer is helpful, please click "Accept Answer" to upvote it. If you have extra questions about this answer, please click "Comment" and I will come to your aid.
