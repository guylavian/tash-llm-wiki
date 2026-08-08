---
title: "ADFS Custom Rule with MultiValue schacPersonalUniqueCode"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1019335/adfs-custom-rule-with-multivalue-schacpersonaluniq
question_id: 1019335
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS Custom Rule with MultiValue schacPersonalUniqueCode

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1019335/adfs-custom-rule-with-multivalue-schacpersonaluniq (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone    

I need to add a Claim Rule with MultiValue schacPersonalUniqueCode in ADFS, so far i can add one value but i need to add a second value that use the same Type in the same rule. How can i do it?     

I have this code now:    

c:[Type == "urn:mace:dir:attribute-def:employeeNumber"]    

 => issue(Type = "urn:schac:attribute-def:schacPersonalUniqueCode", Value = "urn:schac:personalUniqueCode:nl:local:Mycompany:studentid:" + c.Value);    

And i need to add the a second value with: "urn:schac:personalUniqueCode:nl:local:Mycompany:employeeid:"     

Thanks Gents/Ladies

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-10-01*

I am not sure I understand the ask...    

I don't understand the logic behind the claims you have so I'll use the generic claims. Let's say you have the following claims:    

-  Claim1    

-  Claim2    

-  Claim3    

You would like to set Claim3 as a multi value claim with the values of Claim1 and Claim2. You would do the following:    

`c:[Type == "Claim1"]     => issue(Type = "Claim3", Value = c.Value);`    

and     

`c:[Type == "Claim2"]     => issue(Type = "Claim3", Value = c.Value);`    

You issue the claim Claim3 twice so it is now "multi value". Does this help?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-30*

Hi Everyone.    

Can someone take a look to this pls? :)    

Kind Regrds
