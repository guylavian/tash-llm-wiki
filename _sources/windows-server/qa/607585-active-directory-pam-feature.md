---
title: "Active Directory PAM feature"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/607585/active-directory-pam-feature
question_id: 607585
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory PAM feature

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/607585/active-directory-pam-feature (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I want to utilize Active Directory PAM feature to allow standard users of our company's Veeam team to be local administrators on Veeam servers only for certain period of time (will create GUI Tool based on PowerShell for submitting/approving PAM request).  

However, due to nature of Kerberos token I guess they will keep local admin rights on their servers they are already logged on to even after their group membership expires (practically only after logging off they will "lose" local admin rights). Am I right and if answer is yes how to "forcibly" strip them from having local admin rights when TTL of their group membership expires (they will be members of AD group that is member of local admin group on all their servers - that AD group will be empty until they submit PAM request via GUI Tool).  

Thank you in advance.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-08*

Here I am more worried about them still having local admin rights on servers because Kerberos ticket still has them as members of AD group despite the fact that AD group membership expired (TTL).

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-29*

Hello @Bojan Zivkovic  ,

Thank you for your question and reaching out.

Group membership forms part of the user's Kerberos token as far as I'm aware. This can only be generated on login which is why you must have users to logout and back in again for the new group memberships to take effect.

Filesystem permissions apply at the moment you hit "Apply". I would do as you say and join users to the group, wait a day, and then remove the individual user permissions.

The reason your users will need to log out and back in again is because the security token for that group membership on the user object doesn't exist yet. Basically, you're right; you'll need to have your users log out to get this security token. The best method is to add them, then wait until you're confident they've gone through this process.

But...if you can initiate re-authentication manually, This typically means you need to re-login. LSASS only hands this token out when the user authenticates, which is usually only at logon but you can do something like C:\> runas /user:YouProgram.exe a".

Or as a workaround that avoids the hassle of login logoff.

-   Open Command Prompt Kill

-   Kill explorer.exe process (It will only kill the windows explorer. All your other applications are safe). ( You can do it remotely using psexec from Sysinternals )

-   In the command prompt type the following command: runas /user:DOMAIN\ explorer.exe

You will be prompted to enter your password. Enter your password.

--If the reply is helpful, please Upvote and Accept as answer--
