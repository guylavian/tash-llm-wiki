---
title: "Apply GPO only if application is not installed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2195105/apply-gpo-only-if-application-is-not-installed
question_id: 2195105
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# Apply GPO only if application is not installed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2195105/apply-gpo-only-if-application-is-not-installed (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,

I have a GPO which disables Defender. I wish to apply this GPO only if it doesn't find a specific application. How can I check for the presence of the application and skip applying the GPO if it is not found?

Thanks for your assitance!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-28*

Hello Jeffrey Pascone1,

If you want to check whether a specific application exists before applying the GPO, you can create a script to perform this check and configure the script as a startup script in the GPO. If the script detects the presence of a specific application, it skips applying the GPO; if not, it applies the GPO.

But unfortunately we do not provide scripts here. You can try writing script files as needed, or search the Internet for similar scripts. In the script, you may need to indicate the name and path of the application.

Thank you for your understanding. I hope the information above is helpful.

Best Regards,

Yanhong Liu

If the Answer is helpful, please click "Accept Answer" and upvote it.
