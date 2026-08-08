---
title: "Installation of Exchange 2016 CU19 for the current Exchange security patch"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/314842/installation-of-exchange-2016-cu19-for-the-current
question_id: 314842
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Installation of Exchange 2016 CU19 for the current Exchange security patch

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/314842/installation-of-exchange-2016-cu19-for-the-current (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a question related to the current Exchange vulnerabilities: I run an Exchange server 2016 with CU15. Since the installation of the security patch required a more recent CU, I tried to install CU19 but the system threw a "System.UnauthorizedAccessException” at step 16 of 18 which is “Mailbox role: client access front end service”.  I already tried to reinstall CU19 but it does not seem to be possible. Since CU19 was not successfully installed, I still cannot install the security patch.  

Since a few days, there is also a security patch for CU15 available. However, the system detects CU19 so I am also unable to install this patch.    

Is there any option to repair CU19 or how would you suggest proceeding?  The ultima ratio would be to fully reinstall the entire Exchange server but cannot imagine that is the most efficient way.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-16*

Hi,  

Did you run prepare AD steps before the setup?  

Does the DC that your server connects to have FSMO roles?  

Is the account you log in a member of schema admins, domain admins and exchange organization management?  

Run the following command and check if any components are inactive:

```
Get-ServerComponentState –Identity 
```

Check the Exchange setup log if the update fails again.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Thank you for the quick reply. I directly disconnected the servers’ internet connection on Wednesday a week ago when the vulnerabilities have first been published. This was not a problem since the server has not been used as a productive system. So it is not compromised.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-15*

I suspect your server may already be compromised.    

https://msrc-blog.microsoft.com/2021/03/02/multiple-security-updates-released-for-exchange-server/    

Run through this doc and use the Safety Scanner as well:    

https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/#scan-log    

https://learn.microsoft.com/en-us/windows/security/threat-protection/intelligence/safety-scanner-download    

If so, a rebuild may be necessary regardless.     

You can use the RecoverServer switch    

https://learn.microsoft.com/en-us/exchange/high-availability/disaster-recovery/recover-exchange-servers?view=exchserver-2019
