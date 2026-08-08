---
title: "problem to activate certificate template on AD CS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1441797/problem-to-activate-certificate-template-on-ad-cs
question_id: 1441797
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# problem to activate certificate template on AD CS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1441797/problem-to-activate-certificate-template-on-ad-cs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

i  have installed  Active Directory Certificate Services on server with windows 2019  OS to use for radius server.

i have setup the enterprise CA and seems to work fine, but i have this issue.

I have duplicated a computer template, changed some settings and saved without. When i try to add the model for activation i can't see this template on the list.

I don't understand why, the template is replicated on all domain controllers.

what I see is that the version and schema are different from the standard template. for example the duplicate template has schema 4 and version 100.5

what could be the problem? my AD domain and forest level is 2008 R2

thanks

Andrea

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-28*

Hello andrea1981,  

Thank you for posting in Q&A forum.  

Based on the description "When i try to add the model for activation i can't see this template on the list.", what did you mean "add the model for activation"? Did you mean you cannot issue certificate template?    

Or did you mean you cannot see the certificate template when you enroll certificate?  

If so, you can check the permissions on certificate template->Security tab, make sure the machine/ or machine group has read and enroll permission.

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
