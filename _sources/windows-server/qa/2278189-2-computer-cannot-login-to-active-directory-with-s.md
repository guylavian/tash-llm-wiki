---
title: "2 computer cannot login to active directory with same user account"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2278189/2-computer-cannot-login-to-active-directory-with-s
question_id: 2278189
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Independent Advisor"]
---
# 2 computer cannot login to active directory with same user account

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2278189/2-computer-cannot-login-to-active-directory-with-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

2 computer cannot login to active directory with same user account

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2025-05-23*

Hello,

```
Thank you for posting the question on Microsoft Windows forum! 

Based on your query of same user account of not being able to login to 2 computers, as specific error message for the failure of login is not provided, we can only suggest to try checking the following steps.
```

1.Check Account Status:

-   Using below Powershell command to check if the account is locked.

-  Get-ADUser -Identity username -Properties LockedOut to check if the LockOut value is True  

2.Check Password & Cached Credentials:

-  Try logging in on one computer first. If successful, attempt logging in on the second device.

-  If the password was recently changed, restart both computers to clear cached credentials.

3.Verify Network & Domain Connectivity:

-  Ensure both computers can ping the domain controller  ping <name of DC><your domain name>

-  Use nslookup <name of DC><your domain name> to check DNS resolution.

-  If one or both computers fail to connect, inspect local firewall settings or network configurations.

4.Check Event Viewer Logs:

-  Open Event Viewer (eventvwr.msc), go to Windows Logs > Security.  

-  Look for failed login attempts (Event IDs 4625 for failed authentication or 4771 for Kerberos issues).

5.Analyze Group Policies:

-  Check if there are any Group Policy restrictions preventing login for that affected user account by using the command gpresult /r.  

-  Review Active Directory Group Policy settings for authentication limitations.

6.Test with a Different User Account:

-  Try logging in on both computers using a different domain account.

-  If a different account works, the issue is likely specific to the original user account.

Hope the above information is helpful!
