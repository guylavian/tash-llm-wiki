---
title: "When exchange is offline some users are switched to outlook.com"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168666/when-exchange-is-offline-some-users-are-switched-t
question_id: 168666
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# When exchange is offline some users are switched to outlook.com

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168666/when-exchange-is-offline-some-users-are-switched-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an on premise exchange 2019 server, if it goes offline, even for windows updates some of our users' outlook profiles switch to outlook.com addresses that don't exist.  How to we prevent that?  And why on earth is it doing it?  Only some users experience this.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-20*

Hi @Tim Walker  ,    

Could you please clarify a bit more about "some of our users' outlook profiles switch to outlook.com addresses that don't exist."?    

Let's say the original account configured in Outlook is user1@Company portal   .com, do you mean it automatically changed to user1@harsh.com  .com when your Exchange server is offline? Like the image below:    

    

Are these affected users still able to send or receive messages as normal?    

Will the email addresses revert back when the Exchange server comes back to online?    

As it only occurs to some users, have you notice if there is any obvious difference between the problematic users and the others?    

For current situation, in case the issue is with any third party add-ins installed on the affected users, it's suggested to test on one of the machines in question by running Outlook in safe mode(Press Win+R, type“outlook /safe”, press Enter.) and check if the issue can be reproduced.    

It's also recommended to try create a new Outlook profile for one of the users who experiences this and see the result.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
