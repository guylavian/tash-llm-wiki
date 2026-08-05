---
title: "How to fix \"Invoke-IpamGpoProvisioning : Exception calling GetCurrentDomain with 0 argument(s): Current security context is not associated with an Active Directory domain or forest\" in Windows server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1395249/how-to-fix-invoke-ipamgpoprovisioning-exception-ca
question_id: 1395249
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# How to fix "Invoke-IpamGpoProvisioning : Exception calling GetCurrentDomain with 0 argument(s): Current security context is not associated with an Active Directory domain or forest" in Windows server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1395249/how-to-fix-invoke-ipamgpoprovisioning-exception-ca (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am implementing IPAM server for school project.

I have it installed on a VM and needed to provision it:

I run this command:

Invoke-IpamGpoProvisioning -Domain <DomainName> -IpamServerFqdn <ServerFQDN> -GpoPrefixName <GPOName> -DelegatedGpoUser Administrator

After running the above command, it generated the error message.

I will be grateful if someone can point my attention to what I am getting wrong.

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-22*

Hi  

Usually when you have above error, i want to believe you are logged in to the IPAM server with a Local user, 

you need to log in to the server machine or Ipam server using a Domain User( that exist in the DC you are trying to access).

although you can make the Local user to be a domain user which ever works for you.

once logged in using a Domain user, try this cmdlet again and it will work just fine.
