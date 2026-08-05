---
title: "Do not allow Exchange Online calendar details to be shared with external users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1251377/do-not-allow-exchange-online-calendar-details-to-b
question_id: 1251377
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 2
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Do not allow Exchange Online calendar details to be shared with external users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1251377/do-not-allow-exchange-online-calendar-details-to-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This recommendation in the Security Score calculations, on the Microsoft 365 Defender dashboard, does not appear to be accurate.  We allow sharing from free/busy times only -- NOT DETAILS.
However, it is still withholding the Secure Score points and flagging this suggestion.
Anyone else seeing this?
Do not allow Exchange Online calendar details to be shared with external users
General
Implementation
 Action plan

Allowed individual sharing, but limited to free/busy times.
 Description

Users should not be allowed to share the full details of their calendars with external users.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2024-09-24*

The location at which Microsoft recommends implementing this action seems to be inaccurate. The correct location is in the admin.microsoft.com center and then clicking Settings > Org Settings. In the services area you will select Calendar and proceed to untick "Let users share their calendars with people outside of your organization who Office 365 or Exchange."

## Answer (community) — community member

*upvotes: 1 · updated: 2023-04-24*

@Xuyan Ding - MSFT  Thank you for responding to my question.  I understand your response.
I am not trying to get too picky, but the Security Score warning says sharing "details".   I am only sharing free/busy times, not "details".  If MS determine sharing free/busy times is also a risk it would be appropriate to re-word the Security Score measurement so it does not limit to details (but ALL calendar sharing).
If sharing free/busy times only is secure, then the criteria for the Secure Score should be altered to not regress points when only free/busy times are shared.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-24*

Hi @ADM-Griffin2, Jay ,  

If you have calendars that are shared with external users, this advice is expected behavior and is intended to remind you that an Individual sharing policy is being applied by your organization.

For security purposes, administrators can sometimes choose to disable a user's sharing policy to prevent external access to the calendar.
You can try to untick all the policies in Individual Sharing and look again at the recommended actions in Microsoft Secure Score, it will not show the suggestions in the picture above.
Note that it may take up to 24 hours for scores to update.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
