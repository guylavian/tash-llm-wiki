---
title: "ADFS Extranet logon Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3256603/adfs-extranet-logon-issue
question_id: 3256603
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# ADFS Extranet logon Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3256603/adfs-extranet-logon-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a single ADFS server setup in my domain to provide SSO for our internal applications and (internally) this is working very well.

The issue is when we try to access one of these applications from outside the domain.

I was expecting ADFS to present its own login page but what we see is just the grey dialog window asking for a user id and password for the ADFS server.  These credentials are never accepted and after 3 attempts the dialog window is not shown again.

I think the ADFS server is seeing these (non domain) requests as intranet requests rather than extranet

The reason I say this is because I if I remove the windows authentication from the ADFS intranet authentication methods and set it to be forms then I see the ADFS login page in my (non domain) browser. Set it back to windows authentication or windows authentication
 and forms and the grey dialog window is displayed.

Any help/pointers would be most appreciated

Thanks

Ian

## Answer (community) — community member

*upvotes: 0 · updated: 2019-11-19*

Your question is beyond the scope of these Forums

This Community is mainly for home users and their computer problems, not business systems.

Kindly post your question in the TechNet Server Forums.

http://social.technet.microsoft.com/Forums/windowsserver/en-US/home?category=windowsserver

TechNet Forums: 

https://social.technet.microsoft.com/Forums/en-US/home

MSDN Forums:

https://social.msdn.microsoft.com/Forums/en-US/home

Cheers.
