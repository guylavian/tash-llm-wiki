---
title: "Authenticate an EWS WCF service by using OAuth and refresh access token"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/312604/authenticate-an-ews-wcf-service-by-using-oauth-and
question_id: 312604
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["developer-technologies-dotnet-other-l1", "office-exchange-office-exchange-server-development"]
---
# Authenticate an EWS WCF service by using OAuth and refresh access token

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/312604/authenticate-an-ews-wcf-service-by-using-oauth-and (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I am trying to call Exchange web services (EWS) end points from my WCF service using OAuth authentication.     

I have registered the app on Azure portal and able to generate and authenticate it using access token.     

My question is about how I can refresh the token in WCF service. It seems access token has an hour validity.     

```
//Code to generate access token  
// Using Microsoft.Identity.Client 4.22.0  
//Get a token with app-only auth  
var cca = ConfidentialClientApplicationBuilder  
    .Create(ConfigurationManager.AppSettings["appId"])  
    .WithClientSecret(ConfigurationManager.AppSettings["clientSecret"])  
    .WithTenantId(ConfigurationManager.AppSettings["tenantId"])  
    .Build();  
  
// The permission scope required for EWS access  
var ewsScopes = new string[] { "https://outlook.office365.com/.default" };  
  
//Make the token request  
var authResult = await cca.AcquireTokenForClient(ewsScopes).ExecuteAsync();
```

Followed below link for this.    

https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-authenticate-an-ews-application-by-using-oauth    

Thanks

## Answers

_No answers on this thread._
