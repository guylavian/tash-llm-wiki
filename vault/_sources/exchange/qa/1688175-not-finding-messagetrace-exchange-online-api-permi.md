---
title: "Not finding MessageTrace Exchange Online API permision"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1688175/not-finding-messagetrace-exchange-online-api-permi
question_id: 1688175
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Not finding MessageTrace Exchange Online API permision

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1688175/not-finding-messagetrace-exchange-online-api-permi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Under Splunk Addon for Microsoft 365, i'am trying to input the Message trace of Exchange Online.  

My Azure application and permissions are well setup for all others inputs, but i got an issue with this input.

The endpoint i'am trying to access is : https://reports.office365.com/ecp/reportingwebservice/reporting.svc/MessageTrace

The result is a 403 error  (forbiden).  

Looking into all the api permissions, i cannot find the right one.  

I have granted permissions for my application on :  

(API) Office 365 Exchange Online  

Exchange.Manage  

Exchange.ManageAsApp  

ReportingWebService.Read  

ReportingWebService.Read.All  

Anyone knows which permission should i add to be able to get the message trace report?  

Thank you!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-05-28*

The permissions are sufficient, but you have not provided any details on how you authenticate your app. You might have to assign an admin role in addition to the permissions granted, something like a Global reader should do.
