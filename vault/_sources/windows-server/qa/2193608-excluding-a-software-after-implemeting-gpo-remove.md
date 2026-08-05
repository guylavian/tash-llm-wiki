---
title: "Excluding a software after implemeting GPO remove admins rights"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193608/excluding-a-software-after-implemeting-gpo-remove
question_id: 2193608
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-po"]
---
# Excluding a software after implemeting GPO remove admins rights

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193608/excluding-a-software-after-implemeting-gpo-remove (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Microsoft community :)

Recently I implemented GPO which removes local admin rights in my organization

One specific user is trying to run payed software which requiers local admin rights ( so saying the software engeneers )

The issue is that I cant exclude his PC from this policy because of organizational ISO

Please help

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-02*

Hello QmarkIT,  

Thank you for posting on the Microsoft Community Forum.

Temporarily grant local administrator privileges to this specific user so that they can run paid software that requires this privilege.

You can use the "Restricted Groups" or "Local Users and Groups" GPO settings to implement temporary permission changes.

Or "Right click" ->"Run as administrator" and enter the administrator credentials.

This is an explanatory article about group policy restricted groups: Description of group policy restricted groups - Windows Server | Microsoft Learn

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,

Daisy Zhou
