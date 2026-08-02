---
title: "Connecting powershell to exchange sign in window does not load"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1360700/connecting-powershell-to-exchange-sign-in-window-d
question_id: 1360700
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator"]
---
# Connecting powershell to exchange sign in window does not load

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1360700/connecting-powershell-to-exchange-sign-in-window-d (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all,

I am trying to connect to Exchange via Powershell and am able to load the Exchange Online module but when I try to connect using 'Connect-ExchangeOnline -UserPrincipalName ******@mydomain.com' I get a pop-up window with nothing loaded into it. My colleague is able to log in fine at this point and as far as we are aware, we have the same setup/permissions. Is there anything that might be preventing the page from loading? I feel like it will end up being something small and obvious. 

Here is what the pop-up window looks like:

Thank you,

Rob

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-07*

Hi @Rob Ward,

My colleague is able to log in fine at this point and as far as we are aware, we have the same setup/permissions.

If you login your account on your colleague's device, would the issue persist?

If this issue only happens on your device, to me it may probably be a network issue.

Please have a check if you have proxy or VPN enabled, or there are firewalls which are blocking the requests.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-06*

Hello there,

Might be permission issues.After you connect, the cmdlets and parameters that you have or don't have access to is controlled by role-based access control (RBAC)

In Exchange Online, the permissions that you grant to administrators and users are based on management roles. A management role defines the set of tasks that an administrator or user can perform. For example, a management role called Mail Recipients defines the tasks that someone can perform on a set of mailboxes, contacts, and distribution groups. https://learn.microsoft.com/en-us/exchange/permissions-exo/permissions-exo

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–
