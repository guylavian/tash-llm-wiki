---
title: "ADFS SAML Assertions"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/96303/adfs-saml-assertions
question_id: 96303
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS SAML Assertions

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/96303/adfs-saml-assertions (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've setup an AD FS server on Windows Server 2012 R2. I've gotten claims rules to work so that a user can logon to AD FS and then assume a role in AWS based on AD group membership and a mapping between the group and a role. This method is documented well, but now we need to change it.  

We're setting up an application that will authenticate to AD FS and it will pass users preferred IAM role, which we're storing in the AD userParameters attribute. AD FS will go fetch a temporary token from AWS. I'm not sure how to setup claims rules for this approach. Can anyone point me in the right direction?  

Thanks

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-09-16*

If what you need is simply to take the value of the userParameters for the user and send it to the relying party, you can use the Claim Issuance Rule wizard. Pick "Send LDAP attributes as Claims" in the drop down menu and enter the following:    

    

The "userParameters" is not in the drop down list, but you can just write it directly. And you can pick whatever claim type for the outgoing claim. Here is used "claim:/userParameters" just as an example.
