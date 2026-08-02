---
title: "Active Directory - Why change the owner of an object?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/817599/active-directory-why-change-the-owner-of-an-object
question_id: 817599
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Active Directory - Why change the owner of an object?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/817599/active-directory-why-change-the-owner-of-an-object (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When we click on the 'Advanced' button (Properties -> Security -> Advanced), there's an option that allows us to change who the object's owner is. I have two questions regarding this:    

1. Who is an object's 'owner'? My search results say that an object's owner has FULL CONTROL of the object.  I tried testing it - I have a user object called User1. I checked if the Domain Admins group (default owner) had full control of it- and it did. Then I changed the owner to User2. I refreshed everything and then checked if User2 had full control of User1 (also tried 'Effective Access') but it did not. The Domain Admins group still had Full Control of the object. So what exactly is the owner and why do the permissions not change to give the new owner full control?    

2. Why would we want to change the owner? If the Domain Admins group has default ownership of user objects, why would we want to change the Owner? Could you please give me a few example instances where changing an object's owner would be necessary?    

Thank you.    

@Gary Reynolds     I'm taking the liberty of tagging you here because you answered my other question so beautifully. Please help? Thank you :)

## Answers

_No answers on this thread._
