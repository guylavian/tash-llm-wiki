---
title: "Exchange 2019 outlook autodiscover error (0x80070057)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1496943/exchange-2019-outlook-autodiscover-error-0x8007005
question_id: 1496943
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 outlook autodiscover error (0x80070057)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1496943/exchange-2019-outlook-autodiscover-error-0x8007005 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We have 2 exchange server 2019. The url and authentication setting on both servers is the same: 

-  The autodiscoverserviceinternalurl in client access services

-  https://mail.abc.com/autodiscover/autodiscover.xml

-  Different Virtual directory url setting are:

-  internalurl:      https://mail.abc.com/xxxx

-  externalurl:      https://smtp.abc.com/xxxx

  Everything is fine more than 2 years. One day some internal outlook clients have certificate issue suddenly. So, we use "Test Email Autoconfiguration" by outlook icon to test the connection.  We use hostfile to test the connection on 2 servers.  If the outlook connects to ServerA, the autodiscover will go to "https://mail.abc.com", and the test successful. Outlook run no error  But if the outlook connects to ServerB, the autodiscover will go to "https://mail.abc.com" with error code (0x80070057). Then go to "https://smtp.abc.com". So the outlook will prompt certificate error.  The "https://serverB/autodiscover/autodiscover.xml" can access normally in web browser.  Any idea?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-16*

Hi Chong,  

Have you checked whether the certificate on server B is expired or not trusted by the client and may need to be updated or replaced with a new one. OR check the logs on ServerB to see if there are any errors or warnings.  

You can also try the following tools to check for issues.  

Microsoft Remote Connectivity Analyzer  

Kind Regards
