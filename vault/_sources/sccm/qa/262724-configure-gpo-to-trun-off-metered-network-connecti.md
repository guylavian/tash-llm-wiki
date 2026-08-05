---
title: "Configure GPO to trun off metered network connection on Ethernet (Windows 10)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/262724/configure-gpo-to-trun-off-metered-network-connecti
question_id: 262724
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Configure GPO to trun off metered network connection on Ethernet (Windows 10)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/262724/configure-gpo-to-trun-off-metered-network-connecti (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Technet!  

I deployed MECM Agent (2010) on my company co-workers  

Rarely, I'm failed to setup because MECM Server restrict to access from metered network connections  

  

I know that I can solve this problem by adding ccmsetup parameters : /Allowmetered  

But, I can't modify the deployment policy  

So, we have to turn off metered network connection by GPO  

I tried to find out how to turn off the function in Windows 10 through googling,  

As a result, the GPO template could be checked in WIFI and not in Ethernet.  

In addition, I tried to configure the registry reference policy in the path below, but it didn't work.  

[ HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\DefaultMediaCost ]  

Please help me configure GPO to turn off metered network connections on ethernet.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-19*

Great info.    

A little bit tweaked

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-01*

We see the same issue here (metered network --> MECM Client setup failing).  

Looks like the reg key "HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\DefaultMediaCost" is no longer in use.  

The new place to look at is  

```
"HKLM:SOFTWARE\Microsoft\DusmSvc\Profiles\\*\UserCost"
```

Hence a simple default value won't do the trick.  

You may want to adress this using a PowerShell start up script like:  

```
$nicGuid = (Get-NetAdapter | Where{$_.InterfaceDescription -like "*Ethernet*"}).InterfaceGuid
$regpath = "HKLM:\SOFTWARE\Microsoft\DusmSvc\Profiles\$nicGuid\*"
Set-ItemProperty -Path $regpath -Name UserCost -Value 0
Restart-Service -Name DusmSvc -Force
```

PS: further reading  

https://www.asquaredozen.com/2020/05/22/lockdown-diary-metered-internet-connections-and-broken-configmgr-clients/

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-08*

Hi,  

To narrow down the issue , would you please tell how did you configure the registry reference policy？  

For the registry to turn off metered network connection on Ethernet did you do the following configuration:  

Under HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\DefaultMediaCost  and set the value of the Ethernet to1 ?  

Best Regards,  

Fan
