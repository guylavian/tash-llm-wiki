---
title: "ADFS - Append String to End of Attribute Passed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/22834/adfs-append-string-to-end-of-attribute-passed
question_id: 22834
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS - Append String to End of Attribute Passed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/22834/adfs-append-string-to-end-of-attribute-passed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,  

I'm dealing with a challenge with the value passed by ADFS to an application in a particular attribute.  

Here is what he have for the value passed in the Claim Rule:  

c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 => issue(store = "Active Directory", types = ("User.username"), query = ";userPrincipalName;{0}", param = c.Value);  

I need the value of the "User.username" attribute passed to the application during sign-on to have ".stage" appended to the end. How do I accomplish this?  

I thought changing "c.Value" to "c.Value + '.stage'" might work in param, but I think that didn't work.

## Answers

_No answers on this thread._
