---
title: "Exchange Zero Day mitigation crashed outlook for all users."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1038697/exchange-zero-day-mitigation-crashed-outlook-for-a
question_id: 1038697
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Zero Day mitigation crashed outlook for all users.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1038697/exchange-zero-day-mitigation-crashed-outlook-for-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We implemented the first mitigation recommended by Microsoft on 9/30, but today when we attempted to implement the updated recommendation from 10/5 to decode the URL parameter in the IIS Rewrite rule it caused all outlook clients to crash - mail was still being received to the Exchange server but no users could connect to their mailbox.    

Environment is Windows Server 2016 with a Microsoft Exchange cluster running on premise, no hybrid cloud services.    

We performed the implementation steps manually as described in this blog post by Microsoft: https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/#     

Has anyone implement the modified Exchange mitigations recommended by Microsoft yesterday without causing an impact to end users - how?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-25*

I also had an issue on one environment but it was with autodiscover. I was unable to use autodiscover for a new useraccount. As soon as I removed the rewrite ((?=.*autodiscover)(?=.*powershell) variant) and tried again, outlook was able to find settings and configured itself. Afterwards I reinstalled the rewrite using the EOMTv2.ps1

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-07*

@indeliblelibel       

I tested it in my lab there doesn't exist such issue with it. Did you try to reconfigure Outlook profile for one of them, whether could reconfigure Outlook profile successfully?    

Could you provide screenshots about the rule that you created? We could double check about it for you.    

From the picture below, we can know it is used to filter PowerShell related request which will not effect the using of Outlook client.    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-06*

Ok, I havent heard of any issues with the rules when the Mitigation Service is downloading them. Not sure if you have a typo or some other setting that is causing an issue.    

I would consider opening a change , enabling the Mitigation Service and letting it apply the rule instead if you cant get it to work.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-06*

I assume this is Exchange 2016? Why are you setting this rule manually? I would let the Exchange Emergency Mitigation Service update the rule automatically.
