---
title: "[Migrated from MSDN Exchange Dev] Installed Exchange 2019, broke outlook for domain joined machines"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/155961/migrated-from-msdn-exchange-dev-installed-exchange
question_id: 155961
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# [Migrated from MSDN Exchange Dev] Installed Exchange 2019, broke outlook for domain joined machines

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/155961/migrated-from-msdn-exchange-dev-installed-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Origin link: https://social.msdn.microsoft.com/Forums/office/en-US/b6e1b992-4a1a-4ba1-80bd-896e4a5f7f3f/installed-exchange-2019-broke-outlook-for-domain-joined-machines?forum=exchangesvrdevelopment  

My External and Internal URLs all point to an external domain name with an SSL certificate.  

Exchange 2013 has been working great and is on the latest CU  

It was using RPC/Proxy for Outlook  

he external FQDN points to a Exchange 2013 server  

The Exchange 2013 server FQDN points to is running on Azure, as is the new Exchange 2019 server  

We have an Exchange 2013 server running in our NOC inside the domain synced to the external servers via a VPN  

Our internal DNS had a forward for autodiscover.domain.com and the fqdn of the server which points domain machines to the internal server.  

Removing the internal DNS so it points to external server fixed nothing.  

Finally it was time to upgrade  

I Installed Server 2019, followed guides to prepare for Exchange 2019  

Exchange 2019 installs smoothly (hurray)  

Suddenly Outlook Clients inside our domain are prompting for credentials and worse wont except the proper login/password  

Outlook clients outside the domain work perfectly and now show to be using MAPI over HTTP instead of RPC  

Mobile Devices still working perfectly  

Outlook Webmail works perfectly (we use UPN for logins)  

My guess was the MAPI over HTTP instead of RPC doesn't work for domain joined PCs.  

Checked group policy and did find outlooks were set to use NTLM only, changed that to NTLM/Kerberos as someone in another post said is required for MAPI over HTTP, did gpupdate /force, logged out/in same result  

Yes I have removed all saved credentials, even tried a clean domain joined PC first time login  

When Outlook runs for the first time to auto configure my mailbox it prompts for credentials, which it doesnt accept.  

Used PowerShell command to test MAPI over HTTP, all servers pass (exchange 2013 and 2019 alike)  

User PowerShell command to test RPC, all fail now  

My conclusion is something is making the domain joined PCs want to use RPC, which is now broken.  

When testing autodiscover outsidedomain returns everything perfect  

When testing autodiscover inside domain it prompts for password and wont take, but if I cancel password prompt it then returns autodiscover info fine  

I cant believe no one else installing Exchange 2019 had this happen but so many google searches and I cant find someone saying this problem. Several complain external devices cant connect to the new server, but this is domain joined machines.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Which version of Outlook are you using?    

If you create a new user mailbox and configure Outlook for him, will he be asked for password?    

Run the following command to check the url and authentification you set:    

    Get-MapiVirtualDirectory | FL Identity,URL,Auth  

Was the server 2013 decommissioned now?    

Run a test on https://testconnectivity.microsoft.com/tests/Ola/input please.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
