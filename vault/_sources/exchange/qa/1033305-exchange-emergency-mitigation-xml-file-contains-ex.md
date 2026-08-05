---
title: "Exchange Emergency Mitigation / XML-File contains expired Certificates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1033305/exchange-emergency-mitigation-xml-file-contains-ex
question_id: 1033305
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Emergency Mitigation / XML-File contains expired Certificates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1033305/exchange-emergency-mitigation-xml-file-contains-ex (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Is there another certificate expired for the Exchange Mitigation Service?  The last successful event in the event log was on 8/31/2022.  Since that date I'm getting an error: "The remote certificate is invalid according to the validation procedure." and "The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel."

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-04*

@Chris Rendall      

Here is a blog introduced about this function: New security feature in September 2021 Cumulative Update for Exchange Server    

    

As said in the article that AndyDavid provided, ensure that your Exchange servers can communicate with the Internet to validate the certificate chain.    

If you don't want to use this function, you could follow above blog to disable this function:    

```
Set-OrganizationConfig -MitigationsEnabled $false
```

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
