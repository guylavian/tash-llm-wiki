---
title: "Active Directory service account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/257615/active-directory-service-account
question_id: 257615
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Active Directory service account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/257615/active-directory-service-account (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

there are a couple of accounts like cluster, Rep, Scheduler in Active directory ( win server 2016). how can I find out if they are being used for any services?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-04*

Hello @el ma  ,    

Thank you for posting here.    

We can try to run the command on every machine that may run these service accounts, then check if we can find all the service account you want.    

Or we can check if we can see event ID 4771 (Kerberos authentication) for accounts like cluster, Rep, Scheduler or event ID 4776  (NTLM authentication)  for accounts like cluster, Rep, Scheduleron DCs security logs.    

For Kerberos authentication, both authentication success and authentication failure is the same event ID 4771, but the information is not the same.    

For NTLM authentication, both authentication success and authentication failure is the same event ID 4776, but the information is not the same.    

Hope the information above is helpful.    

Best Regards,    

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-03*

I already ran the command but I only see these two StartNames for different Services:  

StartName               : LocalSystem  

StartName               : NT AUTHORITY\LocalService

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-02-03*

You could list them and have a look.  

https://devblogs.microsoft.com/scripting/the-scripting-wife-uses-powershell-to-find-service-accounts/  

--please don't forget to Accept as answer if the reply is helpful--
