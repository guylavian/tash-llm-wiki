---
title: "Unable to create an active directory inside windows server 2016 inside vmware workstation"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1038876/unable-to-create-an-active-directory-inside-window
question_id: 1038876
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["Mvp"]
---
# Unable to create an active directory inside windows server 2016 inside vmware workstation

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1038876/unable-to-create-an-active-directory-inside-window (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am a software developer and i want to test my asp.net core MVC web application to integrate with active directory using LDAP. since i am using Windows 10 home edition so i can not create a test AD inside my windows 10 home edition. so i did the following:-

1) inside my windows 10 home edition >> i installed vmware workstation  

2) download windows server 2016 datacenter iso image.  

3) I install windows server 2016 inside the vmware workstation.

then i enable all those roles and features:-  

the VM got this domain name "WIN-O0DSF1PFVD9" >> I restarted my VM >> but when i tired to configure my VM (mainly prompt this server to domain), i got this error:-

any advice how i can define AD and define LDAP string for this windows server 2016? to test my code?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-10-07*

Might check that the domain controller has a static ip address and that the DC now has own static address listed for DNS and no others such as router or public DNS. Also check the logs for details.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/troubleshooting-domain-controller-deployment    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
