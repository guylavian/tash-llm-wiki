---
title: "Exchange 2019 CU15 On-Prem + ADFS: Outlook for iOS/Android ActiveSync fails with OAuth/MFA"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5927610/exchange-2019-cu15-on-prem-adfs-outlook-for-ios-an
question_id: 5927610
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Exchange 2019 CU15 On-Prem + ADFS: Outlook for iOS/Android ActiveSync fails with OAuth/MFA

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5927610/exchange-2019-cu15-on-prem-adfs-outlook-for-ios-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey !

I'm deep into an ADFS integration project for a pure on-premises Exchange 2019 CU15 environment and have hit a wall with ActiveSync and mobile devices. I'm hoping someone here has either a silver bullet or can confirm my suspicion that this is an architectural dead-end.

I have Exchange 2019 CU15 servers with DAG and right now ADFS configured for Modern Auth with Exchange according to this article: https://learn.microsoft.com/en-us/exchange/plan-and-deploy/post-installation-tasks/enable-modern-auth-in-exchange-server-on-premises

Also I created policies which are blocking Legacy Auth ActiveSync, but arent blocking Modern Auth ActiveSync.

This problem is only seen with ActiveSync with Outlook for iOS, Outlook for Android, Gmail (Android), but Gmail (IOS) and the stock iOS Mail app connect successfully. They trigger the ADFS login page, handle the MFA challenge, and sync without issues.

Android (Gmail app, Nine, Aqua Mail and etc) always fails to connect with 401 code (Unauthorized response)

My Diagnosis:

It seems the Android clients are unable to initiate or handle the OAuth 2.0 flow via ADFS for ActiveSync. The server, as seen in the connectivity test, is still offering Basic auth as the primary method for ActiveSync connections, which our strict policies correctly block. This creates a loop where the client doesn't know how to proceed to OAuth.

I understand that Hybrid Modern Authentication (HMA) with Microsoft 365 would solve this, but that's not an option for us. We need to keep everything on-prem.

Is it true that in a pure on-premises environment without HMA, Outlook for Android (and other Android clients) simply cannot use OAuth for ActiveSync?

Has anyone successfully made this work in a pure on-premises 2019 environment? If so, what was the missing piece?

Thanks in advance for any help you can offer!

## Answers

_No answers on this thread._
