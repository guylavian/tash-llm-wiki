---
title: "Geeting server reference in Exchange online"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/341365/geeting-server-reference-in-exchange-online
question_id: 341365
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Geeting server reference in Exchange online

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/341365/geeting-server-reference-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi    

I am just starting out with OAuth authentication for Exchange online. I have tried below code from here  to get reference to exchange service;    

```
Dim pcaOptions = New PublicClientApplicationOptions With {  
        .ClientId = "00000000-0000-0000-0000-000000000000",  
        .TenantId = "00000000-0000-0000-0000-000000000000"  
        }  
  
        Dim pca = PublicClientApplicationBuilder.CreateWithApplicationOptions(pcaOptions).Build()  
        Dim ewsScopes = New String() {"https://outlook.office365.com/EWS.AccessAsUser.All"}  
  
        Dim authResult = pca.AcquireTokenInteractive(ewsScopes).ExecuteAsync()  
        Dim ewsClient = New ExchangeService()  
          
        ewsClient.Url = New Uri("https://outlook.office365.com/EWS/Exchange.asmx")  
        ewsClient.Credentials = New OAuthCredentials(authResult.Result.AccessToken)
```

My code was getting stuck indefinitely at;    

```
Dim authResult = pca.AcquireTokenInteractive(ewsScopes).ExecuteAsync()
```

I changed it to below and it went ahead.    

```
Dim authResult = pca.AcquireTokenInteractive(ewsScopes).**WithUseEmbeddedWebView(True)**.ExecuteAsync()
```

Now it is indefinitely stuck at;    

```
ewsClient.Credentials = New OAuthCredentials(authResult.Result.AccessToken)
```

What am I doing wrong and how can I get the exchange service reference?    

Thanks    

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-06*

AcquireTokenInteractive should pop up an dialog (or embedded/system browser) where the authentication will take place (or a consent will popup if you app hasn't been consented to). Are you seeing the browser auth happening ? what client are you using ?
