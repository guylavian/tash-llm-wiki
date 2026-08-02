---
title: "Exchange Server OWA Login success and failure log parameter"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1304376/exchange-server-owa-login-success-and-failure-log
question_id: 1304376
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Server OWA Login success and failure log parameter

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1304376/exchange-server-owa-login-success-and-failure-log (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

How do we identify which exchange owa indicate successful login and failure?

Actually needs to integrate with SIEM solutions and cannot able to identify which exchange owa url indicate success login and failure.

If there is any documentation from microsoft or suggest please help.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2024-04-23*

When a user clicks login in the login and password form, a POST request is sent to https://<owa_server_name>/owa/auth.owa in response, the server sends a 302 redirect and a location header that contains the link.   

The link has a reason parameter that can take the value reason=2, indicating that the login/password was unsuccessful. By default, iis does not log this header, so you need to add this logging. This can be done through:  

And further:  

  

Then in splunk this can be found using the following SPL:  

index=your_iis_index cs_uri_stem="/owa/auth.owa" response_location_h="reason=2"*  

SPL will return all attempted failed inputs.*   

To get successful inputs, combine:  

index=your_iis_index cs_uri_stem="/owa/auth.owa" response_location_h!="reason=2"

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-14*

Hi@ Binod Maharjan,

In Exchange Server, you can check the IIS logs(C:\inetpub\logs\LogFiles\W3SVC1) for entries that succeeded or failed the OWA response.

The sc-status field should contain 200, which indicates a successful HTTP response.

The sc-status field should contain a value other than 200 to indicate that an error occurred in the HTTP response.

 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
