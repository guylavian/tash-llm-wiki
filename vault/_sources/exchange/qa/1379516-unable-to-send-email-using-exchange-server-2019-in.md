---
title: "Unable to send email using exchange server 2019 in home lab"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1379516/unable-to-send-email-using-exchange-server-2019-in
question_id: 1379516
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to send email using exchange server 2019 in home lab

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1379516/unable-to-send-email-using-exchange-server-2019-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have setup exchange server 2019 in home lab.

I created two users.

When I tried to send email from one account to another it just gets stuck in Draft folder, Any idea how can I fix this issue? This is not internet facing all in internal in home lab setup.

Please advise/help!

Thanks.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-02*

Hi @ Haroon Peter,

Is it still stuck in the draft box? Are any DNRs returned?

If not, please refer to the following steps to view them in order:

1. Open Control Panel-Services, find Exchange Transport Service and restart.

2. Run Get-MessageTrackingLogto see the results.

-  In Exchange Toolbox, open the Queue Viewer to check if any messages are stuck and check for Last error.

Maybe you can share the screenshot after removing all privacy information like domain name and email addresses.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
