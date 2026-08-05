---
title: "On Prem Exchange 2019 authentication box pops up sporadically 20 minutes to the hour."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1403910/on-prem-exchange-2019-authentication-box-pops-up-s
question_id: 1403910
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# On Prem Exchange 2019 authentication box pops up sporadically 20 minutes to the hour.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1403910/on-prem-exchange-2019-authentication-box-pops-up-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have recently upgraded from Exchange 2013 to Exchagne 2019 on Prem and we use the M365 client to access our On-Prem Exchange. sporadically 20 minutes to the hour we keep getting a authentication log in box to log in. How to I stop this as we're on Prem. I do have a M365 environment standalone none integrated that we use for apps, OneDrive and Teams only. We do not have AD connect in place nor are we a hybrid environment  I receive 1097 and 1098 event ID's errors and need help to resolve this issue. I've tried several reg fixed and solutions but nothing has helped ID the real issue or fix it. We can't be the only people wiht his issues.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-26*

Hello,

According to your description, we need to gather more information about your case so that we can identify the problem and provide a resolution more effectively:

1.Please screenshot the authentication box, being cautious not to include any of your personal information.

2.Could you please clarify if the 1097 and 1098 event ID's errors you described only shows up when the authentication box pops up and what is the specific situation of the error?

3.When the authentication box pops up, please check the connect status to see what the situation is, as shown in the figure below. The method to view is press and hold the Ctrl key, right-click the Outlook icon in the notification area, and then click connect status.

4.As Andy said, I'd like to know which specific reg fixes you've attempted.

5.If at all feasible, it is recommended that you try to test a different version of Outlook and observe the results.

I would appreciate it if you could collect the above information and give feedback at your earliest convenience.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-10-25*

Typically this is load balancer issue. Are you using one? If so, what is set for session timeouts?

What reg fixes did you try?
