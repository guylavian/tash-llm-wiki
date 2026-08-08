---
title: "User managment by \"user type\" on active directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/294851/user-managment-by-user-type-on-active-directory
question_id: 294851
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# User managment by "user type" on active directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/294851/user-managment-by-user-type-on-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I have two type of users in my AD.  

1-real users  

2-users that create for bunch of people and we call it "share user"  

How can separate these users? is it possible to set object category type for this aim?  

e.g. I have 10+K user and all of them locate on CN=users  

every time I integrate other application with my AD fetch all users!  

FYI: I don't want to create another CN because of two CN increase complexity of management.   

Any idea?  

Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-03*

Hi,  

Actually, put different users for different purpose to different OUs is a good way to management.  

One OU will not increase complexity of management.  

Not quite sure how did you integrate other application users, if you don't want to create OUs, you may considered to put them into different security groups or use the attribute to mark the difference.  

Best Regards,
