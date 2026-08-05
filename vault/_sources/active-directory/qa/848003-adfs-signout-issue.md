---
title: "ADFS Signout Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/848003/adfs-signout-issue
question_id: 848003
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Signout Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/848003/adfs-signout-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I experience the following issue when trying to logout from several relying parties in ADFS:  

-  First logon to a SAML application, this gives me a SamlSession cookie  

-  Second logon to a WS-Fed application  

-  Logout of the WS-Fed application  

Then I get the ADFS error page and in the network trace, I do see that the signout request sent to ADFS is sent correctly, but on the request the SamlSession cookie is provided.   

In the network trace I then see ADFS sends me to the logout page I have configured for the SAML application.  

How can I achieve to just do a logout from the requested WS-Fed relying party?

## Answers

_No answers on this thread._
