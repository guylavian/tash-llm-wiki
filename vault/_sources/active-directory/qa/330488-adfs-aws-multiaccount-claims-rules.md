---
title: "ADFS AWS Multiaccount Claims Rules"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/330488/adfs-aws-multiaccount-claims-rules
question_id: 330488
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS AWS Multiaccount Claims Rules

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/330488/adfs-aws-multiaccount-claims-rules (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to figure out a way to use ADF S to authenticate and assume roles in an AWS multiaccount environment using a BI application and JDBC as the frontend components which authenticate to AD and AD FS.  

We've set this up to work with one hardcoded AWS account. We have AD FS setup to pull an AD attribute which matches the name of an AWS-based role, then it's passed to a claim that looks like this:  

c:[Type == "http://temp/variable"]  

 => issue(Type = "https://aws.amazon.com/SAML/Attributes/Role", Value = "arn:aws:iam::111111111111:saml-provider/rdms-adfs,arn:aws:iam::111111111111:role/" + c.Value);  

Our environment has Dev, Test, and Prod installations of the BI app and JDBC connectors. We'd like the to be able to use one AD FS instance, and then grab an STS token in corresponding Dev, Test, and Prod AWS accounts.  

Is it possible for this to be done? Could the BI app/JDBC connector pass a value to ADFS to include in a claim, or can AD FS use an if/then statement based on the source requesting authentication?  

I am running AD FS on Windows Server 2012 R2.  

Thank you

## Answers

_No answers on this thread._
