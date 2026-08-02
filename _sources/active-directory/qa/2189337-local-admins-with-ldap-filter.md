---
title: "Local Admins with LDAP Filter"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2189337/local-admins-with-ldap-filter
question_id: 2189337
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Local Admins with LDAP Filter

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2189337/local-admins-with-ldap-filter (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Folks,

Im working in a new environment and its about deploying different local administrator groups to Computers, as Sites or IP Ranges arent an good option in our scenario I tried to tie it to the location attribute inside the computer object and filter in the GPP, so what did I do.

(&(objectCategory=computer)(objectClass=Computer)(location=MyLocation1*)

this maps a administrator group that is specified to hold administrators from "mylocation1"

(&(objectCategory=computer)(objectClass=Computer)(location=MyLocation2*)

this maps a administrator group that is specified to hold administrators from "mylocation2"

on my testcomputer, the location attribute inside of its Active Directory Account  is "MyLocation1 east"

But even without the wildcards in the filter both GPPs are "matched and processed" on my client

the bindung and attribute i leave default.

Problem is: BOTH gpps are processed and àpplied. So i have 2 administrator groups that are getting added to the computer. 

What is it that I am missing?

Cheers 

Andreas

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-04*

Hello Andreas Ernst,

Thank you for posting in Microsoft Community forum.

Here you can see the detailed description of the LDAP filter.

https://forsenergy.com/en-us/gpmc/html/0d8d3ad2-8fcd-406a-8a13-1619d67f4a30.htm

Preference Item-Level Targeting Using the GPMC | Microsoft Learn

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
