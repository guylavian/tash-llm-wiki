---
title: "How long are certificates available in ADCS Web Enrollment page after issued"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/646241/how-long-are-certificates-available-in-adcs-web-en
question_id: 646241
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# How long are certificates available in ADCS Web Enrollment page after issued

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/646241/how-long-are-certificates-available-in-adcs-web-en (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a windows 2008 enterprise ADCS server with web enrollment. I want to know/configure how long do issued certificates last on the page before a user has to submit another request.  

This is different from certdat.inc's "nPendingTimoutDays" since this controls pending requests, not already issued certificates.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-02*

Hi there,    

By default, the lifetime of a certificate that is issued by a Stand-alone Certificate Authority CA is one year. After one year, the certificate expires and is not trusted for use. There may be situations when you have to override the default expiration date for certificates that are issued by an intermediate or an issuing CA.    

Here is a link as well to dig more information regarding the certificate validity https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/change-certificates-expiration-date    

--------------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
