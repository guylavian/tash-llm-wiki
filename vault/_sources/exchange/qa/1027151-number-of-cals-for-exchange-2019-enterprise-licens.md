---
title: "Number of CAL's for Exchange 2019 Enterprise license - how to find out?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1027151/number-of-cals-for-exchange-2019-enterprise-licens
question_id: 1027151
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Number of CAL's for Exchange 2019 Enterprise license - how to find out?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1027151/number-of-cals-for-exchange-2019-enterprise-licens (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello! Need some help with Exchange licenses - I have Enterprise key for Exchange 2019 but how do I know about number of available CAL's for this license? Is there any Exchange Management Shell command for this? We need at least 100 CAL's for our small company :-) Thank you for help.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-29*

Hi @Evgeny Shupik   ,    

Yes . As Andy said, you don't need to install any CALs.    

You can refer to the command in the following link if you want to check how many users are using  Enterprise CALs:    

FAQ: Licensing Microsoft Exchange Server 2019/2016 | Windows OS Hub (woshub.com)    

NOTE: Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-28*

Yea, you dont install CALs or check via powershell, you have to simply ensure the licenses you have purchased match the amount you need:    

https://www.reddit.com/r/exchangeserver/comments/n1dd7f/exchange_server_2019_cals_install/

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-28*

But how can I be sure I have all necessary number of client licences? I didn't catch - should I activate it using Shell to see available number of CAL's?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-09-28*

see the answer here:    

https://learn.microsoft.com/en-us/answers/questions/534650/exchange-2019-cals.html
