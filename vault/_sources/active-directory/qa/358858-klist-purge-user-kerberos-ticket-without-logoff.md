---
title: "Klist: Purge User Kerberos Ticket without Logoff"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/358858/klist-purge-user-kerberos-ticket-without-logoff
question_id: 358858
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Klist: Purge User Kerberos Ticket without Logoff

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/358858/klist-purge-user-kerberos-ticket-without-logoff (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, having added my test account into the AD group having rights to access shared folder I am still not able to access it from file explorer without logging off/logging on (Windows Server 2016):  

klist purge  

runas /user:DOMAIN\testacc "cmd.exe"  

I see that Kerberos ticket has been updated (klist tgt) and whoami /groups confirms test account is member of AD group but still I always get an error that I do not have permission to access shared folder from file explorer. Logging off/logging on is something I would like to avoid definitely.  

Any help on this would be appreciated - thank you in advance!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-16*

I tried and experienced what I wrote initially.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-16*

Hello @Bojan Zivkovic  ,    

Thank you for your update.    

I am not sure the method you provided will work or not, but you can try.    

If it does not work, I think logging off/logging on is inevitable.    

Best Regards,    

Daisy Zhou

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-04-16*

So this http://woshub.com/how-to-refresh-ad-groups-membership-without-user-logoff/ won't ever work meaning logging off/logging on is inevitable?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-16*

Hello @Bojan Zivkovic  ,    

Thank you for posting here.    

We can see one domain user on one domain client wants to access \server\shared folder to read a file. The process follows this sequence (the user has already logged on, and the user has requested and received a ticket for the workstation):    

    

Then for a user session that originally logged in normally, the user's access token only includes the permissions that the user had when logging in.    

Winlogon creates a window station and several desktop objects for the user, attaches the user's access token, and starts the shell process the user will use to interact with the computer. The user's access token is subsequently inherited by any application process that the user starts during the logon session.    

When the user logs out, the credential cache is refreshed, and all service tickets and all session keys are destroyed.    

If the user is allowed to change the permissions of the shared folder (the original user did not have permission to the shared folder, now the user is given the permission one the shared folder), log off the user, and log in to the client with the user’s account again.    

Only the new permissions are included in the user's access token in user's new logon session, and then the user can access the shared folder.    

For more information we can refer to link below.    

How the Kerberos Version 5 Authentication Protocol Works    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc772815(v=ws.10)?redirectedfrom=MSDN    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou
