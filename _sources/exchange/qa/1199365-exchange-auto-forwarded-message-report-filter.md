---
title: "Exchange Auto forwarded message report filter?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1199365/exchange-auto-forwarded-message-report-filter
question_id: 1199365
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-microsoft-defender-defender-identity", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Auto forwarded message report filter?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1199365/exchange-auto-forwarded-message-report-filter (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
We currently utilise the Auto forwarded message report Auto forwarded message report feature on Exchange (Reports > Mailflow > Auto forward message report).
We are alerted into Defender for any new auto-forward rules set up in our estate which are forwarding to external domains. The function however, comes across as quite crude. For example, the alerts do not contain the actual user(s) who have triggered the alert - they essentially only state that a new user has been detected. 
Our current process of checking who the perpetrator is, is by exporting the list of users who have triggered it in the last 7 days, and manually comparing that with a list of 'approved users' we have stored on our SP to highlight the new unique values.
There is an option to filter the results you get from the last 7 days, and you can 'create new filter'. We've tried this by manually crafting the filter to 'ignore' our approved users, however it's not very dynamic so isn't worth using (I also can't find any documentation on how to fully utilise this [even to the point of deleting old filters] anywhere so any tips are appreciated). 
I'm looking for a better way for this to be managed. Ideally we would like the auto-forward feature to check against a pre-determined list of approved users, before alerting us to potential new forwarders. If the new perpetrator could be included in the alert details, then bonus! However, any ideas on how we can better utilise this function would be great. Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-11*

Hello,
I appreciate my question did include feedback, however it did so to justify my request for assistance. 
I requested any tips/utilisation ideas from other users and how they may manage this type of security issue, so I believe this Q resides in the correct place.
Thanks

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-07*

Hi @ M00nshine,
Welcome to the Microsoft Q&A platform!

Kindly note that this forum mainly focuses on general usage issues and is not the suitable place for feedback.  

If you would like to submit feedback to Microsoft, please consider posting in the Exchange Server · Community (microsoft.com).

Many features of our current products are designed and upgraded based on customers’ feedback. With requirements like this increase, the problem may well be released in the future.   

Thanks for your understanding and support.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread
