---
title: "Incorrect DC version shown in Active directory users and computers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/534524/incorrect-dc-version-shown-in-active-directory-use
question_id: 534524
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Incorrect DC version shown in Active directory users and computers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/534524/incorrect-dc-version-shown-in-active-directory-use (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have provisioned a 2 domain controllers on Azure VMs (windows server 2019 marketplace images)  

strange part is, when I open active directory user and computers console, and select "change domain controller" by right clicking on Domain name.  

I see both my DC with online state, but DC version shows windows server 2016 which seems to be strange to me, as it should be showing windows server 2019.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2022-11-28*

Hi All,     

I maybe found myself :)    

On the AD site and services, go on the NTDS Settings properties of one of my server with this strange behaviour, go on attribute editor then the not well updated attribute is msDS-Behaviour-Version    

    

I found this article, at the end they changed manually the attribute    

https://social.technet.microsoft.com/Forums/ie/en-US/91f7e8ab-b96f-4190-a289-801c005873c9/issue-with-msdsbehaviorversion?forum=winserverDS    

In doubt, I also rebooted my 4 RODC and verified the replication went fine.    

Now on Active Directory Domains and trusts, I could now Raise the Domain Functional Level     

I'll force the AD partition replications    

(Get-ADDomainController -Filter *).Name | Foreach-Object {repadmin /syncall $_ (Get-ADDomain).DistinguishedName /e /A | Out-Null}; Start-Sleep 10; Get-ADReplicationPartnerMetadata -Target "$env:userdnsdomain" -Scope Domain | Select-Object Server, LastReplicationSuccess    

Then on the afternoon, I'll raise my Forest Functional Level.    

Hope this resarch could help someone, one day.    

Regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-25*

Hello,    

I've quite the same issue. Can you help me please?    

Small summary of the situation:    

I demoted 4 old 2012R2 and 2008 R2 RODC from my domain and replaced them by 2019 RODC,    

We have now any DC under 2016 in our AD. (Shema version 88 Windows 2019)    

I wanted to raise my domain functional level to 2016 but received the message : The server is unwilling to process the request.     

After searchig a lot on the net I fixed the ADSI Default naming context\lost and found folder. Also on System\DFSRGlobalSettings\Domainsystemvolume\topology, i removed old DC's.    

With Dcdiag /e /test:sysvolcheck /test:advertising, i fixed all the advertising errors (Due to a NTP error and Sysvol check was fine)    

Sysvol is replicating fine and AD 5 partition too.    

But I think I can't raise because of this :    

Get-ADDomainController -Filter *| Select Name,OperatingSystem | Sort-Object name show my os in Windows Server 2016 Datacenter or Windows Server 2019 Datacenter.    

But trying to change domain controller from ADUC or ADDT show them as W2K8 R2    

It mean the information is pointing to a different attribute. How can I update this information please?    

    

PS : Curently Forest and Domain functional level is : Windows Server 2008 R2

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-08-31*

I did a quick test in a test environment (on-prem) with a Windows 2008 R2 domain controller (no updates) and after adding the first 2019 DC, i didn't had any issue with the DC version.  

But i remember having this kind of issue several years ago but i think it was with a Windows 2000 or 2003 DC's... long time ago ;)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-08-31*

Hello @WinTechie       

Please have a look on below Microsoft article to install AD role in 2019    

 and verify its version in AD.    

https://social.technet.microsoft.com/wiki/contents/articles/52765.windows-server-2019-step-by-step-setup-active-directory-environment-using-powershell.aspx    

Thanks,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-08-31*

You may be looking at the functional level which is correct for Server 2019 (2016 functional level)    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels#windows-server-2019    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
