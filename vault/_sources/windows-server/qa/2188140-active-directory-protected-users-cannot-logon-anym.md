---
title: "Active Directory - Protected Users cannot logon anymore with SamAccountName after forest and domain functional level update"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188140/active-directory-protected-users-cannot-logon-anym
question_id: 2188140
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory - Protected Users cannot logon anymore with SamAccountName after forest and domain functional level update

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188140/active-directory-protected-users-cannot-logon-anym (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We recently raised our forest and domain functional levels (single domain forest) from Windows 2012R2 to Windows 2016

Since then, all the accounts present in Protected users group cannot logon anymore using the pre-Windows 2000 logon name (the "old" fashioned %Domain%%SamAccountName% login). 

When we try to login via RDP we get following message:.

 “A user account restriction (for example, a time-of-day restriction) is preventing you from logging on. For assistance, contact your system administrator or technical support.”

When we try to login on vCenter, Linux or web-based application, we get a wrong user/password error message.

Logging locally on a server is however possible.

Also, we have no problem when connecting using the UPN login.

Pushing further investigation, we found events 100 in the log Applications and Services Logs\Microsoft\Windows\Authentication\ProtectedUsersFailures-DomainControllers with following message:

 "NTLM authentication failed because the account was a member of the Protected User group"

Error code 0xC000006E

It seems that when using the pre-Windows 2000 logon Kerberos will not be used.

We reversed the functional level of forest and domain to Windows 2012R2 but this did not solve the problem.

This is a blocking issue for us because by corporate policy all privileged accounts need to be in Protected User group. Unfortunately some of those accounts are used from applications that will connect with the SamAccountName.

Could you please help us with this problem?

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-09*

Hi Jean-Mi Jac,

Have a nice day！

Protected User accounts that authenticate to a domain running Windows Server 2012 R2 or later are unable to do the following:

-  Authenticate with NTLM authentication.

-  Use DES or RC4 encryption types in Kerberos pre-authentication.

-  Delegate with unconstrained or constrained delegation.

-  Renew Kerberos TGTs beyond their initial four-hour lifetime.

The Protected Users group applies non-configurable settings to TGT expiration for every member account. Normally, the domain controller sets the TGT lifetime and renewal based on the following two domain policies:

-  Maximum lifetime for user ticket

-  Maximum lifetime for user ticket renewal

Protected Users Security Group | Microsoft Learn

Best regards

Neuvi

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-07*

Hi Neuvi,

Thanks for your answer.

I did all those checks but it unfortunately won't help. Problem is not on one particular account but on all accounts in Protected User group.

Permissions are correctly set as accounts can connect using their UPN, problem comes only when pre-Windows 2000 login is used.

Basically our problem is that since the functional level was raised the accounts can't use anymore Kerberos to login when using the old way, falling back to (forbidden) NTLM. Would like to find the root cause of this behavior and how we can correct this.

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-07*

Hi Jean-Mi Jac,

Thank you for posting in the Microsoft Community Forums.

-  Check the security policy

Account lockout policy: Ensure that no user accounts have been locked out due to too many failed login attempts.

Password policy: Check that the password policy has been updated and that the user is aware of the requirements of the new password policy (e.g., password complexity, length, history, etc.).

-  Verify account status

In the AD User and Computer Management tool, check that the account status of the protected user is enabled.

Check if the account is disabled or has other security restrictions.

-  Compatibility check

OS and AD versions: Ensure that all domain controllers and client OS versions are compatible with the Lin and Domain functional level.

Applications and scripts: Check if there are any applications or scripts that rely on older versions of SamAccountName login that need to be updated.

-  Check account privileges

Verify that protected users have sufficient privileges to access the resources they need.

Check if there are any group policies or security settings that restrict a user's login privileges.

-  Review event logs

Review the security event logs on the domain controller for error codes and details related to the failed logon.

Analyze the logs to determine if there are any other potential security issues or configuration errors.

-  Verify login names

Ensure that the user is using the correct SamAccountName when attempting to log on.

If the user has changed to logging in using the UPN (User Principal Name), verify that they are aware of this change.

-  Rollback or reapply updates

If the problem occurs after updating the forest and domain feature levels, consider rolling back to the previous version to test if it resolves the problem.

If rollback is not possible or does not resolve the issue, reapply the update and double-check all relevant settings.

Best regards

Neuvi Jiang
