---
title: "LDAPS configuration works fine intermittently"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1696538/ldaps-configuration-works-fine-intermittently
question_id: 1696538
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
---
# LDAPS configuration works fine intermittently

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1696538/ldaps-configuration-works-fine-intermittently (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

we are facing a strange problem with LDAPS configuration.

Servers involved:

-  A server: Application Server

-  B server: Domain Controller

On A server there is an application developed in PHP. The application is connecting to AD on B server with LDAP protocol and is working fine.

When we change the configuration in LDAPS, it works well intermittently: sometimes it works fine, sometimes it gives an issue.

We performed a Wireshark capture during LDAPS connections and we saw an error "Unknown CA" given by the A server when it receives the certificate from Domain Controller. We checked that the certificate used by the DC is the same both when it works and when it doesn't work.

We haven't noticed any network or infrastructure problems, and the DC serves about 500,000 LDAPS connections per day (all other LDAPS configurations work fine), so I think we can rule out a problem on the DC.

Does anyone have an idea what the problem might be?

Thank you in advance.

Best regards,

Emanuele

## Answers

_No answers on this thread._
