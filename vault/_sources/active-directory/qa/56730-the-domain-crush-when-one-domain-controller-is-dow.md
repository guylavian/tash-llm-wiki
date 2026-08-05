---
title: "The domain crush when one Domain Controller is down"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56730/the-domain-crush-when-one-domain-controller-is-dow
question_id: 56730
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# The domain crush when one Domain Controller is down

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56730/the-domain-crush-when-one-domain-controller-is-dow (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have two different forests (each forest one domain). And I have three domain controller in that domain, but when I disconnect one domain controller, also the original domain controller that create that domain. The domain is totally crash, no matter I use "Active Directory Users and Computers", netdom query /fsmo. All will prompt "The Specified Domain Either Does Not Exist or Could Not Be Contacted".  

But I checked the domain in another forest, and I think that the domain does not have that problem. What is the problem?  

Thanks for your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-12*

Hi,  

   

Just want to confirm the current situations.  

   

Please feel free to let us know if you need further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-04*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-01*

Hi @Hau Kit Wong       

From an elevated command prompt, can you run "dcdiag"    

More than likely, you will have errors there that you will need to investigate but if you post the output here in a format that we can easily read we can have a look too.    

Please also send us the output of "netdom query fsmo"    

Thank you in advance,    

Didier    

--I hope this helps. Please Accept it as an answer and "Up-Vote" the answer or message(s) that helped you so that it can help others in the community looking for help on similar topics

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-08-01*

The domain is totally crash  

Not sure what this means but I'd check the remaining domain controller and problem members both have the static ip address of an active healthy domain controller listed for DNS and no others such as router or public DNS  

--please don't forget to Accept as answer if the reply is helpful--
