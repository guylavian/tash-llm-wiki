---
title: "How to Federate ADFS Issued Tokens with Azure AD for Microsoft Graph API Access Using ROPC Flow"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2031999/how-to-federate-adfs-issued-tokens-with-azure-ad-f
question_id: 2031999
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-authenticator", "microsoft-security-ms-graph", "microsoft-security-security-active-directory-federation-services"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to Federate ADFS Issued Tokens with Azure AD for Microsoft Graph API Access Using ROPC Flow

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2031999/how-to-federate-adfs-issued-tokens-with-azure-ad-f (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am working on integrating ADFS-issued tokens with Azure AD to allow access to Microsoft Graph API using the Resource Owner Password Credentials (ROPC) flow (`grant_type=password`). I have set up ADFS as the identity provider, and I can successfully obtain tokens from ADFS. However, when I try to use these tokens to access Microsoft Graph API, I encounter issues with token validation, such as `InvalidAuthenticationToken` or `Invalid audience`.

My goal is to have Azure AD trust the tokens issued by ADFS so that they can be used to authenticate against Microsoft Graph API. Specifically, I am using the ROPC flow to directly obtain a token on behalf of the user, but I am facing challenges with the token being accepted by Azure AD.

Could you provide guidance on how to properly configure federation between ADFS and Azure AD for this purpose? Specifically, I would like to know:

-  What are the necessary steps to establish a federation trust between ADFS and Azure AD when using the ROPC flow?

-  How can I ensure that tokens issued by ADFS using `grant_type=password` are recognized and accepted by Azure AD?

-  Are there any specific configurations required in Azure AD or ADFS to enable this scenario?

-  Can ADFS-issued tokens be directly converted or exchanged for Azure AD tokens to be used with Microsoft Graph API?

Any detailed instructions, documentation, or best practices would be greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-03*

Here is the body of the token I obtained from ADFS

```
{
  "aud": "https://graph.microsoft.com",
  "iss": "http://{adfs-domain}/adfs/services/trust", 
  "iat": 1725346694,
  "nbf": 1725346694,
  "exp": 1725350294,
  "apptype": "Confidential",
  "appid": "{app-id}",
  "authmethod": "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport",
  "auth_time": "2024-09-03T06:58:14.661Z",
  "ver": "1.0"
}
```

When using the Graph API, the following error occurs when using the token  

What should I do?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-09-02*

Hi @DongJin Son  

When accessing the Graph API, you need to exchange SAML tokens issued by ADFS for Microsoft Graph access tokens, and before exchanging tokens, you need to set up ADFS and enable single sign-on to Office365.

For details, refer to this document.

Hope this helps.

If the reply is helpful, please click Accept Answer and kindly upvote it. If you have additional questions about this answer, please click Comment.
