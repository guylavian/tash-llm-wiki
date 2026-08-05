---
title: "How to pass token while calling EWS endpoint using proxy generated classes (ExchangeServicePortTypeClient) not through EWSManagedAPI RRS feed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/180611/how-to-pass-token-while-calling-ews-endpoint-using
question_id: 180611
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# How to pass token while calling EWS endpoint using proxy generated classes (ExchangeServicePortTypeClient) not through EWSManagedAPI RRS feed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/180611/how-to-pass-token-while-calling-ews-endpoint-using (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I am having a console application which uses Exchange Web Services OnPrem using proxy generated classes like below  

var client = new ExchangeServicePortTypeClient("EndPointConfigName", ".XXXXXasmx");  

It works fine. Now I want to do the same for Exchange Online but with that it's OAuth authentication and requires token to pass.  

I am generating token using registered application id, tenant id and certificate however, not sure how exactly I can add it with "ExchangeServicePortTypeClient" object.  

I see ExchangeServicePortTypeClient.ClientCredentials.IssuedToken but not getting how exactly I can do.  

Due to that I am getting exception "The HTTP request is unauthorized with client authentication scheme 'Negotiate'. The authentication header received from the server was 'Basic Realm=""'".  

Can you please suggest how I can achieve this ?   

Please note I am able to do this using EWSManagedAPI as well as Service call using "HttpWebRequest" [passing token like getFolderRequest.Headers.Add("Authorization", "Bearer " + accessToken);]  

However, my requirement is to do using proxy generated classes.  

Thanks,

## Answers

_No answers on this thread._
