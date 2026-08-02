---
title: "exclude users from GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1153618/exclude-users-from-gpo
question_id: 1153618
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# exclude users from GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1153618/exclude-users-from-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All    

i have a user based group policy applied on a Top Level OU, with in this OU i have 50 plus Sub OUs. I have 3000 plus users getting this Group Policy and they are spread across this 50 OUs. i have 10 users i dont want this Group policy to be applied on them. I would like to create an AD group and add these 10 users and how can i make sure this GPO is not applied on this AD group. I dont want any impact on rest of 2990 users. please guide me.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-06*

Hello    

Thank you for your question and reaching out. I can understand you are  having query\issues related  to    

You can Deny using Security filtering or using Deny access to GPO to prevent being appling.    

https://social.technet.microsoft.com/wiki/contents/articles/4617.security-filtering-using-gpmc.aspx     

https://social.technet.microsoft.com/wiki/contents/articles/4606.exclusion-for-a-group-policy-object.aspx    

--If the reply is helpful, please Upvote and Accept as answer--
