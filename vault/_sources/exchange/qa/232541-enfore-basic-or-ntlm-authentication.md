---
title: "Enfore Basic or NTLM authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/232541/enfore-basic-or-ntlm-authentication
question_id: 232541
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-identity-manager", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Enfore Basic or NTLM authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/232541/enfore-basic-or-ntlm-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We have Exchange 2016 and ADFS and the clients is outlook 2016  

We enabled hybrid moderen authentication and it is enabled for all users now.  

I need to enforce all internal users to use basic or Ntlm authentication when the connected to exchange 2016 and the modern authentication will be applied on External user.  

Please send me your suggestions

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-18*

Hi @yasser Mohamed AbdelMoneim   ,    

Based on my knowledge, in Exchange 2016 or later, MAPI over HTTP is enabled by default at the organization level, and we cannot configure separately internal and external authentication for MAPI virtual directory. We only could enable Basic or other authentication by Set-MAPIVirtualDirectory with IISAuthenticationMethods parameter. But this will change both internal and external authentication methods.     

In addition, according to the Microsoft official article, Microsoft recommend that you always have the virtual directory configured for OAuth.    

There is a similar cased you could refer to: How to set MAPI/HTTP internal and external authentication differently    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
