---
title: "ADFS 3.0 Logout - allow two SAML Logout Endpoints"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/74462/adfs-3-0-logout-allow-two-saml-logout-endpoints
question_id: 74462
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 3.0 Logout - allow two SAML Logout Endpoints

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/74462/adfs-3-0-logout-allow-two-saml-logout-endpoints (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,   

I have searched low and high for a solution but could not find a definitive answer if my problem can be solved. Even just knowing that it cannot be solved would be extremely helpful.  

We have a single identity service that has two DNS names assigned to it, and want to enable federation to a ADFS 3.0 RP. Requests to our identity service can come to either domain. The federated login is successful for all requests, independent of the domain, however, the logout callback from the ADFS 3.0 RP would always go to the first (default) configured SAML Logout Endpoint, irrespective from which domain the request came from. This creates downstream issues with cookies from our identity service being handled on the wrong domain, when the logout request did not come from the default domain.  

I have tried using wreply to tell the RP which logout endpoint it should call, but the parameter got ignored.   

I have found various suggestions in forums and blogs that say that two logout URLs are effectively not possible with ADFS 3.0 but no definite answer.   

If anybody has had this scenario working, it would be great to know.   

Kind Regards,  

Florian

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-25*

Ensure that you are accounting for time zone differences between Outlook and Google Calendar. Both events should be in the same time zone, or you may need to convert the time appropriately during the mapping.
