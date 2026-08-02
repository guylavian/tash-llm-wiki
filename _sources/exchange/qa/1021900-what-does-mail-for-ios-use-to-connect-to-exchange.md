---
title: "what does mail for IOS use to connect to Exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1021900/what-does-mail-for-ios-use-to-connect-to-exchange
question_id: 1021900
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# what does mail for IOS use to connect to Exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1021900/what-does-mail-for-ios-use-to-connect-to-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

dear experts,    

I tried to restrict OWA conection from external network  via IP and domain restriction function in OWA directory in IIS. After I set it, I can't configure mail account in IOS mail

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-27*

Hi @xhope   ,    

As far as I know ,IOS mail is connected to the Exchange server via Exchange Activesync .    

Have you tried adding the IP address of this IOS device to your IP limits to see if you can configure the account?    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-25*

Hi @xhope  ,    

Have you tried to restore domain restriction to the state where it was before?
