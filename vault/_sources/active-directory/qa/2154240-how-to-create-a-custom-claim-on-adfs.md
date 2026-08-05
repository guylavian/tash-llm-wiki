---
title: "How to create a custom claim on ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2154240/how-to-create-a-custom-claim-on-adfs
question_id: 2154240
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# How to create a custom claim on ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2154240/how-to-create-a-custom-claim-on-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I would like to create a custom rule with ADFS using two attributes in order to combine them like this

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]

=> add(store = "Active Directory", types = ("claims:temp/givenname","claims:temp/sn"), query = ";givenname,sn;{0}", param = c.Value);

 

c1:[Type == "claims:temp/givenname"] && c2:[Type == "claims:temp/sn"]

=> issue(Type = "urn:oid: urn**:oid:**0.9.2342.19200300.100.1.3", Value =  c1.Value  + "." + c2.Value + "@test.com");

I understood I must create two custom rules, one for each rule above

I would like to know if there is something wrong with these two rules ?

thanks in advance

Regards

Louis

## Answers

_No answers on this thread._
