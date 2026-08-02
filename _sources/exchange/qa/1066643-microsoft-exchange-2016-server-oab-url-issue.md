---
title: "Microsoft Exchange 2016 Server - OAB URL issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1066643/microsoft-exchange-2016-server-oab-url-issue
question_id: 1066643
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange 2016 Server - OAB URL issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1066643/microsoft-exchange-2016-server-oab-url-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

We found an issue in our client OAB URL, the default URL is randomly changed by itself like this capture below:    

    

The impact of this issue is on every Outlook user it will automatically ask to re-login and the Autodiscover will be detected as a Trojan on our client Antivirus:    

    

Our temporary solution is changing the affected URL on OAB to our client's default URL, and sometimes we need to restart our client Node (mailbox server) which was affected, then the URL returns to normal.    

This repeatedly happens at random, please tell us if there's a permanent solution for this issue.    

Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-31*

Hi @Support Eranyacloud  ,    

What is your Exchange server version?    

It looks like your server has been attacked.    

First, it is recommended to remove and rebuild the OAB virtual directory:    

To delete an existing OAB virtual directory:    

```
Remove-OabVirtualDirectory -Identity "EX01-2016\OAB (Default Web Site)" -Confirm:$false -Force
```

To rebuild the OAB virtual directory:    

```
New-OabVirtualDirectory -Server "EX01-2016" -InternalUrl "https://mail.exoip.com/OAB" -ExternalUrl "https://mail.exoip.com/OAB"
```

Second, if your Exchange version is not up to date, some vulnerabilities in Exchange can cause attacks on your server, so it is recommended that you upgrade to the latest SU and then verify whether the issue still occurs.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-28*

Sure you the server is not compromised?    

Have you applied the lasest CU plus SU plus the needed mitigations?    

https://techcommunity.microsoft.com/t5/exchange-team-blog/customer-guidance-for-reported-zero-day-vulnerabilities-in/bc-p/3651277#M34558    

https://techcommunity.microsoft.com/t5/exchange-team-blog/released-october-2022-exchange-server-security-updates/ba-p/3646263
