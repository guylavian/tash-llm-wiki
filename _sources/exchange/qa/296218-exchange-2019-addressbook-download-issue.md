---
title: "Exchange 2019 Addressbook download issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/296218/exchange-2019-addressbook-download-issue
question_id: 296218
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2019 Addressbook download issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/296218/exchange-2019-addressbook-download-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,   

I have exchange 2019 server and outlook 2019 one of the user tried downloading address book it is giving error "task email address reported error (0x8004010F): The operation failed. The object cannot be found. All other users its working fine.Can you help   

Thanks Rajith

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-08*

Thanks Ashok and ZhengqiLou, I got solution this was conflicting with other outlook profile, I deleted all outlook profiles and deleted all outlook data files and all files in  c:\users\usernameAppData\Local\Microsoft\Outlook.Then its started working. Thank you..

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-03*

Hi @Rajith Minni   ,    

Try running the Test Email Autoconfiguration in users outlook profile and check if Autodiscover is working fine and OAB URL is populated. Since its for one user, try creating a new outlook profile from client side and from server end, try moving it to another database.    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
