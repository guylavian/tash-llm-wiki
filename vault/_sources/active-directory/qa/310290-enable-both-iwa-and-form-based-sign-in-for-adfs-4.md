---
title: "Enable both IWA and form based sign-in for ADFS 4.0"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/310290/enable-both-iwa-and-form-based-sign-in-for-adfs-4
question_id: 310290
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Enable both IWA and form based sign-in for ADFS 4.0

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/310290/enable-both-iwa-and-form-based-sign-in-for-adfs-4 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have ADFS 2019 running in Intranet setting. We have enabled both Form-based auth and Integrated Windows Auth. IWA is working fine and accepts the logged in user's credentials from desktop correctly. But now developers are asking if it is possible to have form based auth also available for login with any other accounts (test, admin etc) other than local workstation's logged in user? One solution was to use firefox which rejects the IWA and goes to form sign-in page correctly, but if we want to use Chrome or Edge then there is no choice. I tried directly going to /adfs/ls/FormsSignIn.aspx page, but it gives error. MSIS7065: There are no registered protocol handlers on path /adfs/ls/FormsSignIn.aspx Any other way to bypass IWA and go to form sign-in page?

## Answers

_No answers on this thread._
