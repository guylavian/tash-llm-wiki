---
title: "Active Directory - RDP Users Users Cannot Reset Own Password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1520759/active-directory-rdp-users-users-cannot-reset-own
question_id: 1520759
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-remote-desktop-terminal-services", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory - RDP Users Users Cannot Reset Own Password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1520759/active-directory-rdp-users-users-cannot-reset-own (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We host cloud environments for our customers that they access via RDP (using RD Gateway with SSL - not Terminal Services).
The environment in question is running at Server 2012 R2 functional level.There are technically 2 domain controllers running (one is 2012 R2, the other 2016).

The 2016 Domain Controller exists to support Azure AD Connect (and synchronization has been working perfectly - password sync is one-way, Active Directory to Office 365) and is effectively a clone of the original 2012 R2 domain controller except it is running a newer OS version (I.E. DNS, DHCP, Group Policy, etc. have all replicated properly and are up to date on both devices).

I have also confirmed that the clock time on each device is correct and there is not a massive difference between one of the DCs and the device I'm using to test.

In order to facilitate my testing - password age has temporarily been set to 0 days 

Here are the issues I'm encountering (and not entirely sure how to resolve it):

-  If user is set to "Have user set to reset password at next login" - RDP fails at the initial login point with simple "The login attempt failed" message at the bottom of the Remote Desktop connection window. No window is opened or connection established to the remote machine.

-  If the "Reset Password at next login" box is then unchecked (after the failed attempt) all subsequent login attempts succeed and login takes place normally

-  If "Reset Password at next login" is not set and the user logs in normally, THEN the user tries to utilize the CTRL+ALT+END shortcut to access the "Reset Password" functions, any password that the user attempts to enter fails with the message "The password does not meet complexity requirements". This has been tested with MUTLIPLE passwords that fulfill both the length and complexity requirements.

-  Conversely, setting the password directly on the domain controller succeeds without issue

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-02*

Not 100% this is applicable to RDS gateway but in RDP its a security question, you can disable CredSSP on the server side, but since that lowers the security on all RDP connections to that server it is not recommended. To do it you de-select the “Allow connections only from computers running Remote Desktop with Network Level Authentication (recommended)” on the servers system properties. The client also have a setting for it but i think you have to disable it by editing an .rdp file (save as on the rdp profile) then edit the value related to CredSSP 😀 however this is not recommended. But hope the information helps, if you want a more step-by-step guide try searching for "disable CredSSP for RDP" or "disable Network level authentication for RDP"
