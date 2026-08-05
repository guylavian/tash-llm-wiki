---
title: "EWS Streaming Notification subscription disconnected/exceeding max limit with O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1032393/ews-streaming-notification-subscription-disconnect
question_id: 1032393
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# EWS Streaming Notification subscription disconnected/exceeding max limit with O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1032393/ews-streaming-notification-subscription-disconnect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we are using EWS Streaming notification for more than a year and suddenly previous week we notice two issues with the streaming notification on the meeting room.    

-  The streaming notification is disconnected within 2 seconds after open and some times the acknowledgment is not sent out to the client.    

-  The streaming subscription exceeding the max limit for the account -> we are pretty sure that there are no additional client running.    

LOG:    

 warn: Fail to start streaming subscription <"room email id>">. Ex: You have exceeded the available subscriptions for your account.  Remove unnecessary subscriptions and try your request again. ServiceResponseException {    

  message: 'You have exceeded the available subscriptions for your account.  Remove unnecessary subscriptions and try your request again.',    

  InnerException: null,    

  response:    

   SubscribeResponse {    

     errorDetails:  

      DictionaryWithStringKey {  

        keys: [Array],  

        keysToObjs: [Object],  

        objects: [Object],  

        keyPicker: [Function] },  

     errorProperties: [],  

     subscription: StreamingSubscription { service: [Object], id: null, watermark: null },  

     result: 2,  

     errorCode: 103,  

     errorMessage: 'You have exceeded the available subscriptions for your account.  Remove unnecessary subscriptions and try your request again.' } }

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-06*

FYR, we have "Run diagnostics" in the "How can we help?" section by increasing the throttling and still the streaming notification subscription connection is fail.    

Are the Meeting room Mailboxes in Office365 or are they OnPrem, you can't change the throttling setting in Office365 but you can modify them onPrem by changing the web.Config file.    

Have you implemented all the headers as outlined in https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-maintain-affinity-between-group-of-subscriptions-and-mailbox-server this is important at scale and could be the reason you seeing issue eg if you haven't set the X-AnchorMailbox setting especially.     

-  To know the reason for the ews streaming notification subscription fail.    

For OnPrem mailboxes the best way would be to look at the ewsLogs on the CAS server they will tell you budget usage etc, in the cloud you can't get that information so that when you need to log a case with the requestid etc    

-  To Understand the limit on the streaming notification subscription connections and data.    

If you are impersonating correctly then it should be 20 subscriptions per mailbox, if mailboxes are in the cloud then using the client credentials flow rather then service accounts is a better idea https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow    

-  Advice on the design part to cater for throttling on single service account basis. The requirement is to have ~100 meetings rooms and ~1000 users impersonated by the service account.    

If your doing impersonation correctly then it shouldn't be a problem there a plenty of Apps out there that scale larger than that, if it is targeting Exchange Online only then using the Microsoft Graph and Webhooks maybe a better long term solution.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

Thanks @Glen Scales  ,    

We are using Impersonation and the streaming notification subscriptions are within 8 meeting rooms. The system was running fine since 11+ months and since previous week we are noticing the above mention issues.     

The impersonation account license type is "Exchange Online (Plan 1)" -> I presume there is no quota or limit wrt account type?    

For "1. The streaming notification is disconnected within 2 seconds after open and some times the acknowledgment is not sent out to the client." issue related, the response from the ews is "error: undefined, errCode=undefined".

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-04*

Are you using Impersonation in your code or delegate access, you can have up to 20 subscriptions by default and the way they are counted varies depending on if you using Delegate Access or Impersonation.  Audit logs can help identify what is access the mailbox https://learn.microsoft.com/en-us/exchange/security-and-compliance/exchange-auditing-reports/view-administrator-audit-log something like a Teams Meeting Room Device or Meeting Room display etc could cause this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-04*

Thanks @ joyceshen-MSFT.
