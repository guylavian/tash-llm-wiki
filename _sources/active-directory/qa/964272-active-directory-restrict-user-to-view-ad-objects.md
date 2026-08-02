---
title: "Active Directory - Restrict User to view ad objects"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/964272/active-directory-restrict-user-to-view-ad-objects
question_id: 964272
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory - Restrict User to view ad objects

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/964272/active-directory-restrict-user-to-view-ad-objects (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

Is there any option to restrict the standard user to view only the objects which he is part of in Active Directory.    

Currently user is able to view all the objects (read only)    

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2022-08-17*

Hello there,    

You can add all the users in a security group and delegate the permission to restrict their activity.    

Restrict guest access permissions in Azure Active Directory https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/users-restrict-guest-permissions    

Active Directory security groups https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups    

--------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-11*

Have a look at these previous questions, which were trying to achieve same thing.    

https://learn.microsoft.com/en-us/answers/questions/929688/best-practice-to-prevent-active-directory-enumerat.html    

https://learn.microsoft.com/en-us/answers/questions/707421/ad-search-privileged-groups.html    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-11*

Hi @Anonymous       

It’s for a single user, in our case we have 2000 plus users. In this case could you please guide how to restrict.    

Sorry I mentioned Standard User instead of Standards Users in my post.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-11*

Hi @Anonymous       

It’s for a single users, in our case we have 2000 plus users. In this case could you please guide how to restrict.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-08-11*

You can follow along here.    

https://social.technet.microsoft.com/wiki/contents/articles/6130.how-to-hide-objects-in-active-directory-from-specific-users.aspx    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
