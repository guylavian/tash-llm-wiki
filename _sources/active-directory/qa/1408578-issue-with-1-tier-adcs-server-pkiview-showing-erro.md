---
title: "Issue with 1 tier ADCS server PKIView showing errors Unable To Download"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1408578/issue-with-1-tier-adcs-server-pkiview-showing-erro
question_id: 1408578
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
---
# Issue with 1 tier ADCS server PKIView showing errors Unable To Download

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1408578/issue-with-1-tier-adcs-server-pkiview-showing-erro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good Day, me and our team inherited an AD and AD CS environment that was not looked after properly. We are looking to retire this AD CS but we are still using it for 802.1x Radius Auth with Wifi.

AD CS was discovered to be running on an old DC. The AD CS environment was backed up and restored to a new server which had a different hostname and I believe this was done properly as the CA still reference the old hostname along with the new one. Then the root cert needed to be renewed and it was with the existing pair. 

We are currently seeing an issue with PKIView in regards to 1 CDP location and two DeltaCRL locations. All three of the ones showing error say Unable to Download. All items here are pointing to .crl files except for the AIA location. The URL's that the three items below with errors are all reachable from domain machines and are http paths to the ADCS server which is also running IIS. Again currently this server is a single tier domain server.

Here are the "unable to download" urls. Is it possible to fix this? Currently I think the biggest negative of this situation would be the machines are not turning in their expired or superceded certs which I can understand is a security issue

http://hostname.ourdomain.com/CertEnroll/CA.crl  is CDP Location #1 and Delta CRL Location #1

[http://hostname.ourdomain.com/CertEnroll/CA+.crl] is Delta CRL Location #2 (also error)

Can we correct these bad CDP and Delta CRL issues

## Answers

_No answers on this thread._
