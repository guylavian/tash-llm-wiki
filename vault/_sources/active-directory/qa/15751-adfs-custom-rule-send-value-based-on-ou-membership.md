---
title: "ADFS Custom rule: Send Value based on OU membership"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/15751/adfs-custom-rule-send-value-based-on-ou-membership
question_id: 15751
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# ADFS Custom rule: Send Value based on OU membership

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/15751/adfs-custom-rule-send-value-based-on-ou-membership (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are a community college and I want to make a custom rule in ADFS based on OU membership.  

This rule must send out value 'Employee' or 'Student' based on the OU the account is located in.  

I can't use AD groups because there isn't any group containing all the accounts.  

(Like Active, Future, Alumni etc. they are all separated, not my choice by the way)  

According to this thread: https://social.technet.microsoft.com/Forums/en-US/762a4ab1-1649-442c-91a4-654ee7b3664f/limiting-adfs-20-to-an-org-unit?forum=winserverDS  

I tried:  

eduPersonAffiliation Student  

c:[Type == "http://temp.org/adobjectdn",Value =~ "^.*(OU=Students,OU=OurDomain Users,DC=OurDomain,DC=local)$"] => issue(Type = "eduPersonAffiliation", Value = "Student", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, ValueType = c.ValueType);  

eduPersonAffiliation Employee  

c:[Type == "http://temp.org/adobjectdn",Value =~ "^.*(OU=Employees,OU=OurDomain Users,DC=OurDomain,DC=local)$"] => issue(Type = "eduPersonAffiliation", Value = "Employee", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, ValueType = c.ValueType);  

Do I have to change that temp.org? Or must I define adobjectdn?  

I checked the regex expression and that works.  

I hope anyone can help me, thanks in advance!

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-03-20*

You must define the entire value there, in other words add a claims rule that sets the "http://temp.org/adobjectdn" (what you name it doesn't really matter btw) value of the DN attribute.
