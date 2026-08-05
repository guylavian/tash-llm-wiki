---
title: "Sysadmin Privileges to an Active Directory (AD) Group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1181100/sysadmin-privileges-to-an-active-directory-ad-grou
question_id: 1181100
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["sql-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Sysadmin Privileges to an Active Directory (AD) Group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1181100/sysadmin-privileges-to-an-active-directory-ad-grou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Pretty straightforward, really.

If I add active directory users individually to the SQL Server 2019 Security -> Logins and make the Server Roles as a sysadmin, then I can login with those users and perform all actions.

If I create an active directory group with those same users and the exact same security settings, then those group members can login to the server, but server/database actions are severely limited.  I can't see most database stored procedures or functions, table activity seems to be restricted to SELECTs, etc...  I haven't tried setting any database specific Securables, but that kind of defeats the purpose of assigning sysadmin rights and increases management time.

I will provide any additional information needed.  Thank you for any help.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-02-15*

To add an AD group to sysadmin, you would do:

```
ALTER SERVER ROLE sysadmin ADD MEMBER "DOMAIN\SYSADMINS"
```

If this does not work out for you, it may be that you someone did not the users to the AD group.

You can inspect which security tokens that you have by running

```
SELECT type, usage, name FROM sys.login_token
```

If everything is OK, you should see the name of the AD group as well as "sysadmin" in the name column.
