---
title: "ADFS Claim to convert values to lower case"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/28216/adfs-claim-to-convert-values-to-lower-case
question_id: 28216
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Claim to convert values to lower case

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/28216/adfs-claim-to-convert-values-to-lower-case (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!  

We are currently using this claim rule but we need to change the attribute mail to lower case  

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 => issue(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",   

 "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname",   

 "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname",   

 "http://schemas.xmlsoap.org/claims/Group"),   

 query = ";mail,givenName,sn,tokenGroups;{0}", param = c.Value);  

I found this article   

https://social.technet.microsoft.com/Forums/windowsserver/en-US/109a226d-b9c5-47b4-98ab-2d9e6446b1e4/adfs-claim-to-convert-user-id-to-uppercase?forum=ADFS  

But I don't understand how to apply this to our current claim rule?   

Regards ET  

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 => add(store = "Active Directory", types = ("temp_email"), query = ";mail;{0}", param = c.Value);  

c:[Type == "temp_email"]  

 => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", Value = RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(RegExReplace(c.Value, "a", "A"), "b", "B"), "c", "C"), "d", "D"), "e", "E"), "f", "F"), "g", "G"), "h", "H"), "i", "I"), "j", "J"), "k", "K"), "l", "L"), "m", "M"), "n", "N"), "o", "O"), "p", "P"), "q", "Q"), "r", "R"), "s", "S"), "t", "T"), "u", "U"), "v", "V"), "w", "W"), "x", "X"), "y", "Y"), "z", "Z"));

## Answer (community) — community member

*upvotes: 0 · updated: 2020-05-20*

3_claims c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"] => issue(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname", "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname", "http://schemas.xmlsoap.org/claims/Group"), query = ";givenName,sn,tokenGroups;{0}", param = c.Value);
