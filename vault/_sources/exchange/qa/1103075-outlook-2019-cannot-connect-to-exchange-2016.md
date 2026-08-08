---
title: "outlook 2019 cannot connect to exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1103075/outlook-2019-cannot-connect-to-exchange-2016
question_id: 1103075
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# outlook 2019 cannot connect to exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1103075/outlook-2019-cannot-connect-to-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

i have exchange server 2016 cu 22 and it was working vey well without any problem then i made the mitigation steps as it mentioned in the link    

https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/    

i can't login through outlook 2016,2019  then i remove all the steps and update my exchange with the latest update of 8/11/2022 but the problem still the  same

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-25*

Hi @Samuel Sefeen  ,    

Welcome to our forum.    

How did you remove the mitigation?    

If an admin removes a mitigation but does not block it, the EM service will reapply the mitigation when it performs its hourly check for new mitigations.    

You can run the following command to block the mitigation, then manually removing it.     

```
Set-ExchangeServer -Identity  -MitigationsBlocked @("M1")
```

If this error persists, it is recommended that you temporarily disable EM service.    

```
Set-OrganizationConfig -MitigationsEnabled $false
```

For more information about the Exchange Emergency Mitigation (EM) service, please refer to exchange-emergency-mitigation-service    

Besides, the mitigations are no longer recommended, and you can simply install the November 8, 2022 update.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
