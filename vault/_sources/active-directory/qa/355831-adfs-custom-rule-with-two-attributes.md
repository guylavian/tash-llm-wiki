---
title: "ADFS Custom Rule with Two Attributes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/355831/adfs-custom-rule-with-two-attributes
question_id: 355831
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Custom Rule with Two Attributes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/355831/adfs-custom-rule-with-two-attributes (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are configuring ADFS (on Server 2012 R2) to support multiple AWS accounts. We plan to leverage an LDAP attribute to determine the user's role, and a second attribute to specify the AWS account number the user should be authenticated to.  

We have this working with the user's role populated in an LDAP attribute, but the AWS account number is hardcoded in the claim right now, so we're looking for some guidance getting that put into a claim correctly.  

Here is what we are trying:  

Get Attributes Claim Rule (Rule template: Send claims using a custom rule)  

c1:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 => add(store = "Active Directory", types = ("http://temp/variable"), query = ";ad-attribute1;{0}", param = c.Value1);  

c2:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]  

 => add(store = "Active Directory", types = ("http://temp/variable"), query = ";ad-attribute2;{0}", param = c.Value2);  

AWS Role (Rule template: Send claims using a custom rule)  

c:[Type == "http://temp/variable"]  

 => issue(Type = "https://aws.amazon.com/SAML/Attributes/Role", Value = "arn:aws:iam::" + c.Value2 ":saml-provider/our-adfs,arn:aws:iam::" + c.Value2 ":role/" + c.Value1);  

The value we are trying to achieve will be structured like this:  

arn:aws:iam::111111111111:saml-provider/our-adfs,arn:aws:iam::111111111111:role/rolename

## Answers

_No answers on this thread._
