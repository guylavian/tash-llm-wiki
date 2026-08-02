---
title: "ADFS claim rules help"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/549888/adfs-claim-rules-help
question_id: 549888
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS claim rules help

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/549888/adfs-claim-rules-help (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I am trying to configure a monitoring software called "Zabbix" to use our ADFS system for SSO. However I am having trouble getting it to work and I believe it comes down to missing or incorrect claim rules.     

This is how I have it set up on Zabbix:    

    

However, I keep getting the error, The parameter "UPN" is missing from the user attributes.    

I have also tried uid and samaccountname instead of UPN but I receive the same error for those (with uid or samaccountname replacing UPN in the error)    

Do I need to create a claim rule to get rid of this error and if so, what is the proper syntax?    

Thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-15*

I was able to get it to work. It turns out I needed to translate the LDAP claims with this rule:    

    

When I added "samaccountname" in the username attribute field above, I was able to sign in with SAML.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-09-14*

Do I need to create a claim rule to get rid of this error ...  

You might. But they (the SP) should tell you what to send.  

You need to know if you need a NameID. If so, in what format.  

Then you need to know what claims you need to send. You need the exact claim type. For example, for UPN, you can send a claim that is exactly "UPN" with the user principal name of the user.
