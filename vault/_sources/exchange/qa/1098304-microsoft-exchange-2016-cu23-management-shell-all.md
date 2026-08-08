---
title: "Microsoft Exchange 2016 CU23 - Management Shell & all IIS Sites OWA,ECP WinRM 500 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1098304/microsoft-exchange-2016-cu23-management-shell-all
question_id: 1098304
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange 2016 CU23 - Management Shell & all IIS Sites OWA,ECP WinRM 500 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1098304/microsoft-exchange-2016-cu23-management-shell-all (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

After upgrading Exchange 2016 CU19 to CU23 which completed successfully. Exchange PowerShell no longer works and cannot be connected to. All IIS pages (OWA,ECP)are no longer accessible and throw HTTP error 500 same as PowerShell.    

The Server is in a DAG and was first to be upgraded, all other servers work fine. Using ECP Management Page unable to modify virtual directory of upgraded server with access denied error.    

Although database copy is healthy and replication is ongoing. Only front end services seem to be affected.    

To note I have reviewed the exchange setup logs and everything seem fine. Event viewer does not display any out of the ordinary errors.     

I have run exchange troubleshooter and it was able to connect to the server PowerShell, although launching the exchange management shell does not work.    

All certificates are present and up to date.     

Tried to assign valid certificate to Back End Website in IIS and still no luck.    

Grateful for any ideas or direction to check.    

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2022-11-22*

Hi @Yanick Sauzier  ,

Welcome to our forum.

For the EMS error, please try the following methods:

1.Please first check all Exchange services are running

```
Get-Service | Where {$_.DisplayName -Like "*Exchange*"} | Where {$_.DisplayName -NotLike "*Hyper-V*"} | Format-Table DisplayName, Name, Status
```

2.Check the ExchangeInstallPath: http-error-500-start-ems-emc  

Open Control Panel > System > Advanced system settings > Advanced > Environment Variables > System variables > Check the Value of ExchangeInstallPath

3.Check the WinRM IIS extension.  

Open Server Manager > Add roles and features > Go to Features > Check if the WinRM IIS Extension was installed, if so, uninstall and re-install it, if not, install it.

4.Connect to a remote Exchange server via Windows PowerShell: connect-to-exchange-servers-using-remote-powershell  

If this fixes the EMS error, try removing and recreating the EMS/ECP/OWA virtual directory.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-22*

Make sure all required services are running: Services overview    

At the same time, see if there is any error in the Event Viewer.    

In IIS, the virtual directories(e.g. ECP, OWA, PowerShell etc.) display as "Application", you could click the "View Applications" or click the triangle icon of Default Web Site to see the virtual directories.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-11-21*

Verify that you have an Exchange Server Open Authentication (OAuth) certificate and that it isn't expired.    

See: Can't sign in to Outlook on the web or EAC if Exchange Server OAuth certificate is expired

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2022-11-21*

Hi    

Have seen this happen before after CU updates. Try this:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/owa-stops-working-after-update    

Running Update-Cas.ps1 will recreate your OWA and ECP environments with clean config files.    

Hope this helps,    

Thanks    

Michael Durkan    

-  If the reply was helpful please upvote and/or accept as answer as this helps others in the community with similar questions. Thanks!
