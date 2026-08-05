---
title: "\"NT-Autority\\System\" impersonated or overtaken? GPO-problems."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/95609/nt-autoritysystem-impersonated-or-overtaken-gpo-pr
question_id: 95609
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# "NT-Autority\System" impersonated or overtaken? GPO-problems.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/95609/nt-autoritysystem-impersonated-or-overtaken-gpo-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, was reseaching a GPO-problem on a single W10_1903 PC.  

DNS, DFS and evereything else seemed okay, except from all the GPO-errors in the Event Log.  

But when I from a psexec command prompt, (running "WhoAmI" gives "NT-Autority\System" for sure) ran "dir \<domain.com>\SysVol" I got: "Wrong username or password". Running that several times locked another domain account, whitch is a local administrator on that computer.  

So to me it seems like that other domain account has "taken over" the NT-Autority\System account in some way. Any hints appreciated, thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-18*

Thanks all, but none of the suggested solutions worked. I even tried ro reset Windows. Also searched the whole registry for that account that got locked in case something there had got messed up, bu did not find it at all.  

I ended up with wipe&reinstall, all well with that one now. I hope there are not more of these in our domain, that sympthom seems a bit scary...

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-16*

Hello @Raymond Hellberg  ,

Thank you for posting here.

Based on the description, I did a test in my lab, I got the result successfully.

We can check:

1.Check whether we can logon this computer with any domain account. If no, we may need to disjoin the computer from domain and then rejoin the computer to domain OR reset the secure channel password.

1)Logon this computer with built-in local Administrator.  

2)Open CMD and run as Administrator.  

3)Type Netdom resetpwd /s:target_server /ud:mydomain\domain_admin /pd:* and click Enter.

/s:server is the name of the domain controller to use for setting the machine account password. This is the server where the KDC is running.  

/ud:domain\User is the user account that makes the connection with the domain you specified in the /s parameter. This must be in domain\User format. If this parameter is omitted, the current user account is used.  

/pd:* specifies the password of the user account that is specified in the /ud parameter. Use an asterisk (*) to be prompted for the password.

2.If we access another shared folder on the DC or domain file server, can we access?

3.Check whether only this domain-joined computer has this issue.

4.What is your GPO-errors in the Event Log, what settings we have configured in this GPO.

5.Check what account (local account or domain account) do we use to logon this computer, if we change another account (local account or domain account), check whether the issue persists.

6.Check whether we have a domain account with the same name as this computer.

Best Regards,  

Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-15*

I would put the PC into a workgroup, and then delete it's computer account from the domain. Then check all of the domain controllers to verify that it's account does not exist on any of them. Then re-join it to the domain and put its account in the correct OU.
