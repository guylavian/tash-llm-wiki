---
title: "Reset machine password of a domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/512045/reset-machine-password-of-a-domain-controller
question_id: 512045
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Reset machine password of a domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/512045/reset-machine-password-of-a-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

On my secondary DC I'm seeing the event NETLOGON 3210  

This computer could not authenticate with \DC.network.local, a Windows domain controller for domain Network, and therefore this computer might deny logon requests. This inability to authenticate might be caused by another computer on the same network using the same name or the password for this computer account is not recognized. If this message appears again, contact your system administrator.  

It doesn't appear to be causing any issues but it's something that I'm sure needs to be addresses. I've seen various articles around the topic but none that are quite the issue I have. The closest I can find is: http://blog.cpolydorou.net/2019/02/domain-controller-machine-password-reset.html   

I've never reset the machine password of a DC before so a bit apprehensive to follow along.  Thoughts anyone?  

Many thanks  

Edit: I should also add, this DC runs ADsync and has been happily operating for at least 2 years. I've only recently discovered the event so no idea of when it started. Earliest log was 2 months ago.

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-08-18*

Sounds good, you're welcome.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-18*

Thanks DSPatrick,  

Sorry I didn't get notified of your replies. I've run the commands you've mentioned and the DC does fail, but the repair doesn't work. I was hoping to avoid demoting as it runs our ADSync. I think the easy answer is the normal windows way of doing a clean install. I'll transfer everything over and bomb the DC in question.  

Appreciate you time. Thanks

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-14*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-12*

Try;    

`Test-ComputerSecureChannel`  

or    

`Test-ComputerSecureChannel -Repair`  

or    

The simplest solution may be to move roles off, demote, reboot, promo the problematic one again.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
