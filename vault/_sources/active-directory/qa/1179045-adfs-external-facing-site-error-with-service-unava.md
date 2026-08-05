---
title: "ADFS external facing site error with 'Service Unavailable  HTTP Error 503. The service is unavailable.'"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1179045/adfs-external-facing-site-error-with-service-unava
question_id: 1179045
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS external facing site error with 'Service Unavailable  HTTP Error 503. The service is unavailable.'

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1179045/adfs-external-facing-site-error-with-service-unava (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,   

We have 2 AD FS (2016) servers, and 2 WAP servers (2016) and recently renewed SSL certificate for ADFS. During the same time, ADFS service account password expired and we updated that as well.   

SSL renewal steps:   

Installed the cert with private key on all servers (2x ADFS & 2x WAPs).  

Re-established the trust between ADFS and WAPs. Operations Status on WAP: Web Application Proxy, AD FS Proxy, Web Application Proxy Core are all Green and status shows Working.   

But when I try to log in to Office from external network, the AD FS signing page shows the below error. Am I missing something here?  

Service Unavailable

***HTTP Error 503. The service is unavailable.  

Any help would be appreciated!  

TIA

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-31*

If anyone is still having issues with this, I would check the following:

HTTP Error 503. The Service is unavailable

Cause #1: Invalid base address entered in the SAML login redirection page field.

Solution #1: Make sure your base addresses match your application and ADFS. For example, if ADFS was assigned `https://sso.contosso.com/` your application should reflect the same address, `https://sso.contosso.com/`.

Cause #2: The ADFS services are not running.

Solution #2: Check your service account has up-to-date credentials and start or restart your ADFS services.

Cause #3: Not pointing to the correct resource endpoint, specifically `/ls`.

Solution#3: Make sure your address is also pointing to the correct resources, `/adfs/ls`.
