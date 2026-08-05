---
title: "Active Directory Multiple Failed Login Attempts by same user"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/587146/active-directory-multiple-failed-login-attempts-by
question_id: 587146
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Active Directory Multiple Failed Login Attempts by same user

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/587146/active-directory-multiple-failed-login-attempts-by (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In my enterprise, a single user logs-in multiple systems ( for example , keep it a count as 5 ). After the password expiry, the user changes the password with the help of IT team and logs-in in one system.  

After this incident, the remaining 4 systems which the user previously logged-in trigger a bad password attempts continuously , like where 5 -10 bad password attempts for each second.  

I can't figure out what is the problem ? How the systems automatically trigger a login attempt ? What should I do to stop such incidents ?

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-10-12*

Hi @Nikil Lepcha       

I'm assuming that the user is logging into windows workstations or servers that are joined to an AD.  The reason I ask is that by default AD will only accept the current password, it doesn't accept n-1, or n-2 passwords.  This functionality only exists for computer accounts and is limited to n and n-1 passwords.  Unless you have additional services installed on the DCs to support this functionality.  Can you share the details of you new lockout policy.    

Are there multiple accounts that are showing this problem or just this one?    

The presents of a user profle on a machine will not cause a logon event, this will only happen if the user has started an RDP session and disconnected the session or left a machine logged on.  Typically in this scenario the logon event happens as the session tries to access resources that were opened while the user was using the session, or mapped drives opened with credentials.    

You can use NetTools to identify which systems are causing the logon and see if there are any sessions still running for the user.    

Gary.    

GAry.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-10-12*

Hi @Nikil Lepcha       

It looks like the user has a previous session still active or a network share or something else that is still using the old password.  Have a look at this article it might help you find where the old credentials are still being used. https://nettools.net/troubleshoot-account-lockouts/    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-12*

Hi,  

If you follow the article it will show you which machines the accounts are getting locked out from, then you can check that machine for a open session.  It doesn't provide the ability to scan machines to find active sessions.  

Gary.
