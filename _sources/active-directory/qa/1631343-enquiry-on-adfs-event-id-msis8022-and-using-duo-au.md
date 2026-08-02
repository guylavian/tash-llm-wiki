---
title: "Enquiry on ADFS event ID MSIS8022 and Using DUO Authenticator for primary authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1631343/enquiry-on-adfs-event-id-msis8022-and-using-duo-au
question_id: 1631343
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Enquiry on ADFS event ID MSIS8022 and Using DUO Authenticator for primary authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1631343/enquiry-on-adfs-event-id-msis8022-and-using-duo-au (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

We are trying to use DUO Authenticator for primary authentication as we would try using it to replace traditional form based authentication (Passwordless). We have tried testing it with our Shibboleth service provider through SAML2 protocol.

However, during the testing, we found the below error happen when we are using an invalid user (i.e. not exist in AD). Is it a bug or any way to avoid this error?

The ADFS event ID is MSIS8022. 

Thanks a lot.

Regards,  

Patrick

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-28*

The problem seems happen on Service Provider (SP) initialized URL only.

No problem if it's Identity Provider (IDP) initialized.

e.g. https://sts.contoso.com/adfs/ls/idpinitiatedsignon.aspx
