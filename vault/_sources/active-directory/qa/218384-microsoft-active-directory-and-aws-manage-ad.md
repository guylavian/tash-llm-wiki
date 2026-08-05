---
title: "Microsoft Active Directory and AWS Manage AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218384/microsoft-active-directory-and-aws-manage-ad
question_id: 218384
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Microsoft Active Directory and AWS Manage AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218384/microsoft-active-directory-and-aws-manage-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we currently have On MS Perm Active Directory (XXX.xyz), recently we configure Manage AD in AWS (AWS.XXX.XYZ) and set up the Trust between On Perm AD and Manage AD in AWS, users from On Perm AD are successfully able to log on using the On Perm AD domain (XXX.xyz) and credential to the resource on AWS. My question is " is this possible if I build a Windows EC2 Instance in AWS  and join it to AD in AWS (AWS.XXX.XYZ), this New EC2 instance join AWS.XXX.XYZ domain but fall under computer object under on perm AD (XXX.xyz) so that all the GPO from XXX.xyz domain are applied to this new object??  

not sure if this could be possible or not, kindly help.  

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-11*

Thank you so much Daisy, i have open up a case with AWS support, will work with them, and provide the update once the issue is resolved.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-05*

Hello @Shaikh Hussain  ,    

Thank you for posting here.    

I am sorry, I don't know much about AWS.     

But based on "is this possible if I build a Windows EC2 Instance in AWS and join it to AD in AWS (AWS.XXX.XYZ), this New EC2 instance join AWS.XXX.XYZ domain but fall under computer object under on perm AD (XXX.xyz)", I do not know how to make one object (New EC2 instance) in AWS.XXX.XYZ domain and on perm AD (XXX.xyz) at the same time.    

In my opinion, if one Windows machine (server or client) is in on perm AD (XXX.xyz), so that the GPO from XXX.xyz domain can be applied to this object.    

Best Regards,    

Daisy Zhou
