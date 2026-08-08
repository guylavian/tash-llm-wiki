---
title: "Exchange server 2019 - TLS 1.2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1350427/exchange-server-2019-tls-1-2
question_id: 1350427
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange server 2019 - TLS 1.2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1350427/exchange-server-2019-tls-1-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,

This is regarding the Exchange server 2019, I understand Exchange server 2019 will support TLS 1.2 out of the box. In our environment we have few windows 7 machines (We know this is an outdated OS, this will be updated in the near future) which are running some business critical applications. The problem here is, we are unable to connect exchange server 2019 due to TLS compatibility issue between windows 7 and Exchange sever 2019, We found the below fix and we don’t want to apply the below fix for this issue due to internal constraints.

https://support.microsoft.com/en-us/topic/update-to-enable-tls-1-1-and-tls-1-2-as-default-secure-protocols-in-winhttp-in-windows-c4bd73d2-31d7-761e-0178-11268bb10392

I understand TLS 1.0 and TLS 1.1 is not secure, however we would like to understand whether the following things are possible with Exchange server 2019

This is completely an on premises environment and we are not going to have hybrid connectivity with office 365, So is there any way to enable Exchange server 2019 to support TLS 1.0 and TLS 1.1 ? So that windows 7 machines can connect to Exchange server 2019 ?

Is there any way to disable TLS 1.2 in Exchange server 2019  and make Exchange server 2019 to use TLS 1.0 and TLS 1.1 ?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-08-23*

Hi @Nithyanandham Singaravadivelu  

Although the link you provided is lost, I'm guessing you're referring to this: KB3140245

Unfortunately, it seems that the official only mentioned this method. It is recommended to follow the official solution. 

Also, I found the following link, just for reference:

https://www.reddit.com/r/exchangeserver/comments/bezdes/issue_with_windows_7_and_exchange_2019_solved/

https://community.spiceworks.com/topic/2302629-external-windows-7-client-can-t-connect-to-exchange-server

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-08-23*

Yes, it is possible. However, it is not recommended because TLS 1.2 is the most secure version of TLS available.

Please note that disabling TLS 1.2 may cause some clients to be unable to connect to Exchange Server.

Check this article - https://learn.microsoft.com/en-us/exchange/exchange-tls-configuration?view=exchserver-2019
