---
title: "IIS Logs Flooded With 401 EWS Requests from Mac Outlook"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1022693/iis-logs-flooded-with-401-ews-requests-from-mac-ou
question_id: 1022693
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-development-iis"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# IIS Logs Flooded With 401 EWS Requests from Mac Outlook

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1022693/iis-logs-flooded-with-401-ews-requests-from-mac-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi  There:    

  We are running Exchange 2016 in our environment and noticed the IIS logs are growing so fast    

  After Searching the log, we founded lots of request to URL "EWS/Exchange.asmx" and the status code which returned by server is 401    

  All of such log is coming from Mac Outlook users    

  So i just wonder why such client (Mac) send so much（3000/min） 401 request  and how to avoid it ?    

Any help will appreciate~    

Logs are like this:    

2022-09-02 02:43:29 10.7x.xx.2x POST /EWS/Exchange.asmx &CorrelationID=<empty>;&cafeReqId=e7a7da63-88ac-408b-b800-82458bb450b8; 443 - 172.20.1.1 AppleExchangeWebServices/818.0.1 - 401 1 2148074254 5    

by the way , all of these mac outlook users can logon normaly (send / receive emails)

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-28*

hi  Liang. Thanks for your advise    

-  These 401 logs come from different Mac Outlook    

-  Whem these guys change their password , this question  probably come out .     

-   I have no idea how thing will going if i disable the http/2 . Could you give some more information about http/2

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-27*

Hi @延年 侯   ,    

Considering that it's a public forum, I have covered the personal information in your post involved for privacy concern.    

Please be careful to hide your personal information . Thank you!    

----------    

Please have a check whether these codes are from the same computer.     

If these errors come from different Mac users, you could try disabling http/2 in server’s registry to see if the logs continue to be generated.    

```
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\HTTP\Parameters  
EnableHttp2Tls REG_DWORD 0  
EnableHttp2Cleartext REG_DWORD 0
```

Here is a similar thread that discusses this issue in detail: Exchange 2016 - EWS 401 Unauthorized - Apple Mail and Safari Only (microsoft.com)    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-26*

Yep, I see that all the time. I think its just the way the Mac clients work. From what I have seen its normal unfortunately.
