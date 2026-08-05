---
title: "ADFS Custom Primary Authenticator triggers MSIS8022 when user input invalid username"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1624835/adfs-custom-primary-authenticator-triggers-msis802
question_id: 1624835
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS Custom Primary Authenticator triggers MSIS8022 when user input invalid username

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1624835/adfs-custom-primary-authenticator-triggers-msis802 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are developing a custom authenticator for ADFS 2019 and intend to make it work as primary authentication method in Paginated theme.

We found that when user input an invalid upn as username and choose our custom authenticator, an error message "Incorrect user ID or password" will be displayed. This is not desirable as it will allow adversaries to brute force our list of valid usernames.

We tried to set the RequiresIdentity property in the metadata of our authenticator to False. And the result is the same.

In addition, we found that the following error event is logged when user select our authenticator:

Exception details: 

Microsoft.IdentityServer.Service.AccountPolicy.ADAccountLookupException: MSIS8022: Unable to find the specified user account.

   at Microsoft.IdentityServer.Service.LocalAccountStores.ActiveDirectory.ActiveDirectoryCpTrustStore.GetUserClaimsIdentity(String identifier)

   at Microsoft.IdentityServer.Web.Authentication.External.ExternalAuthenticationHandler.GetUnauthenticatedSSOToken(ProtocolContext context, String username)

   at Microsoft.IdentityServer.Web.Authentication.External.ExternalAuthenticationHandler.Process(ProtocolContext context)

   at Microsoft.IdentityServer.Web.Authentication.AuthenticationOptionsHandler.Process(ProtocolContext context)

   at Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)

Any way to make it work like the out-of-the-box password authenticator? That is, even if user input a wrong username, allow user to continue the challenge, but let the authenticator logic to decide what to do.

Thanks very much!

## Answers

_No answers on this thread._
