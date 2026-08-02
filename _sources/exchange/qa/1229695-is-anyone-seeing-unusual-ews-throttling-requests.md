---
title: "Is anyone seeing unusual EWS throttling requests ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1229695/is-anyone-seeing-unusual-ews-throttling-requests
question_id: 1229695
fetched: 2026-07-25
answer_count: 10
has_accepted_answer: false
upvotes: 4
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-development"]
answer_author_roles: ["Q&A User"]
---
# Is anyone seeing unusual EWS throttling requests ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1229695/is-anyone-seeing-unusual-ews-throttling-requests (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On April 6, sometime after midnight, it appears that Exchange Online made a change that effects the EWS throttling policies. 
As of 9am CST today, we have 275 tenants with this problem.  

The error looks like this:
 [You have exceeded the available concurrent connections for your account.  Try again once your other requests have completed.]
ErrorDetails; Key=[Policy], Value=[MaxConcurrency]
ErrorDetails; Key=[MaxConcurrencyLimit], Value=[27]
ErrorDetails; Key=[ErrorMessage], Value=[This operation exceeds the throttling budget for policy part 'MaxConcurrency', policy value '27',  Budget type: 'Ews'.  Suggested backoff time 0 ms.]

At this phase of processing., our SaaS platform has only a single thread (no concurrency) and our backoff time is ten minutes.
We made the request to remove throttling policies for 90 days on our own tenant.  The support request suggested that we wait 15 minutes for the policy to be updated.
We waited 24 hours and the same error appears.  
Microsoft support has not been so helpful.
Microsoft Case 35934803

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-14*

We do have the same problem since April 13th. Sucking...

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-14*

Hi, we can confirm the same error affecting one of our customers. They are unable to connect to EWS services. 
This operation exceeds the throttling budget for policy part 'MaxConcurrency', policy value '27',  Budget type: 'Ews'.  Suggested backoff time 0 ms.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-14*

Same here since Tuesday, MS told me...we didn't make any changes....problem must be on your side....
`[EwsResponse]`

```

```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-14*

Hi,
The same problem happened a couple days ago at several our customers.
It happens on EWS request <m:GetFolder> with <t:DistinguishedFolderId> = publicfoldersroot
Office365 server returns
<e:ResponseCode>ErrorServerBusy</e:ResponseCode>
<e:Message>The server cannot service this request right now. Try again later.</e:Message>
<t:MessageXml>
<t:Value Name="Policy">MaxConcurrency</t:Value>
<t:Value Name="MaxConcurrencyLimit">27</t:Value>
<t:Value Name="ErrorMessage">This operation exceeds the throttling budget for policy part 'MaxConcurrency', policy value '27',  Budget type: 'Ews'.  Suggested backoff time 0 ms.</t:Value>
</t:MessageXml>
Although the same request <m:GetFolder> with <t:DistinguishedFolderId> = msgfolderroot works OK.
Please help to resolve this problem because our customers can't access their PublicFolders in Office365 Outlook

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-14*

The error you are getting is not related to the "MaxConcurrentConnection" but due to exceeding the value for "EWSMaxSubscriptions". 
Reference: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/ews-throttling-in-exchange
Increase the value of EWSMaxSubscriptions on your exchange server and try.
