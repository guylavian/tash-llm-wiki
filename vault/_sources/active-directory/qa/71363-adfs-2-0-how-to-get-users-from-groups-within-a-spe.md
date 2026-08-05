---
title: "ADFS 2.0 - how to get users from groups within a specific OU"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/71363/adfs-2-0-how-to-get-users-from-groups-within-a-spe
question_id: 71363
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS 2.0 - how to get users from groups within a specific OU

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/71363/adfs-2-0-how-to-get-users-from-groups-within-a-spe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Thanks in advance for anyone who can assist on this issue.    

Am running ADFS 2.0 on Win2008R2 SP1 and encountered some problems.  The purpose is to get the users in the different groups inside the specific OU and rely it to a 3rd party app. So what I did was:    

a. Added a rule under "Acceptance Transform Rules"  in "Claims Provider Trusts". Using "distinguishedname" under LDAP Attribute and "ht tp://myserver/claims/DistinguishedName" as the outgoing claim type.    

Should this rule be on the top or below of the rule order?     

Is the use of distinguishedname correct here?    

b. Then under the "Relying Party Trusts" ==> "Issurance Authorization Rules", I add this custom claim rule.    

    

Is this custom rule claim correct? Cos I am getting the error "The status code of the Response was not Success, was Responder -> urn:oasis:names:tc:SAML:2.0:status:RequestDenied".    

I am not versed with ADFS but i am pretty sure the custom rule claim is not getting the correct response. Can anyone help to advise on this?    

Many thank in advance!    

Tan

## Answers

_No answers on this thread._
