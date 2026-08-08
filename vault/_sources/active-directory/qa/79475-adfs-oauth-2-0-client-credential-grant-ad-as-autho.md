---
title: "ADFS oAuth 2.0 Client Credential Grant, AD as authorizations(scope) store"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/79475/adfs-oauth-2-0-client-credential-grant-ad-as-autho
question_id: 79475
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS oAuth 2.0 Client Credential Grant, AD as authorizations(scope) store

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/79475/adfs-oauth-2-0-client-credential-grant-ad-as-autho (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our scenario could be described this way.  

A back-end webapp service (in linux) uses the OAuth 2.0 Client Credential Flow (CCF) to request a token from ADFS. It passes its client_id and client_secret. Even if the BE service is considered "confidential"(since it uses the CCF to request a token), we know it runs under a service account which is registered into Active Directory.  

The service account is linked to the BE service (the client). In AD, we associate AD groups to the service. Which are application authorizations for the downstream APIs the BE service could call. So instead of using scopes in ADFS we would like to use AD Groups as permissions given to this BE Service.  

We are trying to figure how we tell ADFS to request the attributes associated to this client_id (or service account) in AD so we could transform these attributes into claims. Which will be later added to the requested access token. But ADFS doesn't seems to consider any claim transformations rules since the oAuth flow used here is CCF.  

Notes :   

-  Scopes are working well. But they are local to ADFS. So we are forced to manage authorizations in AD (for human users such as customers and employees) and in ADFS (for processes). Not ideal. One authorization store (AD) vs many authorization store (ADFS instances).   

-  We could use the Authorization Code flow for our BE Service. But we think it's not in the spirit of oAuth to use that flow since our service is not considered "public" (user/human authentication) but "confidential" (server to server).

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-30*

In the context of OAuth 2.0, claims about the client (service account) are generally not part of the standard specification. The Client Credential Flow typically focuses on the client's credentials and does not provide a mechanism for additional claims about the client to be included in the resulting token.
