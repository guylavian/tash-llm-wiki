---
title: "AD CS: Deploying Cross-forest Certificate Enrollment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56711/ad-cs-deploying-cross-forest-certificate-enrollmen
question_id: 56711
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# AD CS: Deploying Cross-forest Certificate Enrollment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56711/ad-cs-deploying-cross-forest-certificate-enrollmen (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

With reference to the article https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff955845(v=ws.10) can somebody please clarify if I already have a Enterprise CA in an Account Forest can I establish a 'Cross Forest Enrollment' with a Resource Forest and maintain the Enterprise CA in the Account Forest or do I have to consolidate this Account Forest CA into the Resource Forest?        

The reason I am asking is because we have  a small user base in Account Forest and want to integrate these into an AOVPN solution in the Resource Forest.         

Thanks in advance for any advise/help.    

Rich

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-08-03*

Hi,    

Based on my research, from the management, both the methods you mentioned can be considered.     

Since you have only a small user base in Account Forest,for easier management, you can consolidate this Account Forest CA into the Resource Forest .    

Not familiar with the AOVPN solution, you may combine various factors and choose an appropriate method.    

Following link for your refrence:    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff955842(v=ws.10)?redirectedfrom=MSDN    

Fan
