---
title: "EWS Managed API Authentication with Exchange on-premise (NTLM)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2142168/ews-managed-api-authentication-with-exchange-on-pr
question_id: 2142168
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
---
# EWS Managed API Authentication with Exchange on-premise (NTLM)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2142168/ews-managed-api-authentication-with-exchange-on-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

Could you please guide me on how to use NTLM authentication for the Microsoft EWS API services with Exchange Server On-Premises? According to the documentation https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/authentication-and-ews-in-exchange, On-Premise Exchange installations should use NTLM authentication. I have tried using the MSAL library for authentication, but if I am not mistaken, this is used for OAuth2, so it is not suitable for this case. My question is the following, if I am using NTLM does this mean the user will input their username & password in clear format and I will use NetworkCredential to authenticate him/her using the EWS Managed API library? Will the credentials be passed securely this way? This means that no cloud Identity provider is used as in OAuth2.

```
service.Credentials = new NetworkCredential("username", "password", "domain");
```

Could you please let me know if this is the correct approach please? In my case I do not want to use the Exchange on cloud or any cloud service like the identity provider for OAuth2. What is also the difference of NetworkCredential and WebCredentials? Now, this is what I am using, but is appropriate only for OAuth2 which is only available on cloud Exchange Server, and it is not what I need:

```
ExchangeService ewsService = new ExchangeService();
ewsService.UseDefaultCredentials = true;
ewsService.Url = new Uri("https://outlook.office365.com/EWS/Exchange.asmx");
ewsService.Credentials = new OAuthCredentials(accessToken);
```

Could you please also confirm whether using OAuth requires and is mandatory to register your application on the Azure portal? Because we need to avoid using the cloud in all cases, as per our requirements.

Also as a side question, how am I supposed to determine what is the ewsService.URL for my On premise exchange server?

Many thanks,

## Answers

_No answers on this thread._
