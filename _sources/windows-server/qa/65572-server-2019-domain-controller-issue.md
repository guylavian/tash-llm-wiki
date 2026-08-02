---
title: "Server 2019 domain controller issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/65572/server-2019-domain-controller-issue
question_id: 65572
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Server 2019 domain controller issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/65572/server-2019-domain-controller-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi     

We have newly promoted server 2019 as a domain controller. post successful configuration we are getting a file by name: DNS settings and Type:msDNS-ServerSettings    

    

I have never seen this earlier. please clarify what is this file and is it by design or do we need to delete it or is it safe to ignore it.    

Thanks    

Sunny

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-01*

Can this file be deleted of dc has been demoted?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-13*

Just to check if the above reply could be of help, if yes, you may mark useful reply as answer, if not, welcome to feedback.  

Best regards,  

Sylvia

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-12*

Looks like this one may be a key master, nothing to worry about.      

https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dnsp/24e513b0-0b67-4cbe-b149-f287f3acf6fd      

--please don't forget to Accept as answer if the reply is helpful--
