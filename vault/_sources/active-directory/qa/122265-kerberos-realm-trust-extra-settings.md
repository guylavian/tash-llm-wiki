---
title: "Kerberos Realm Trust: Extra settings"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/122265/kerberos-realm-trust-extra-settings
question_id: 122265
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Kerberos Realm Trust: Extra settings

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/122265/kerberos-realm-trust-extra-settings (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Kerberos Realm Trust is one of the available trusts in AD Domains and Trusts. So I proceed "as usual" by adding this trust with Wizard:    

    

This can also be done from command line: netdom trust /add /realm .... . Netdom has also some extra commands about kerberos (/kerberos /EnableTgtDelegation etc):    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc835085(v=ws.11)    

My question is this: Because this one is with non windows machine- what else has to be setup? Firewall? What about commands like ksetup/ktpass even kadmin?    

Ksetup    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh240190(v=ws.11)    

Ktpass    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc753771(v=ws.11)    

kadmin [-O|-N] [-r realm] [-p principal] [-q query] [[-c cache_name]|[-k [-t keytab]]|-n] [-w password] [-s admin_server[:port]]    

kadmin.local [-r realm] [-p principal] [-q query] [-d dbname] [-e enc:salt ...] [-m] [-x db_args]    

Thanks for clear answer!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-10-12*

Hello @InfoTechdude  ,

Thank you for posting here.

We can try the following steps on DC in Windows domain.

1.Before setting up any trust, we should create secondary zone or set up conditional forwarders to make two realms can find each other on DC in Windows domain and DC in non-Windows domain.

Create secondary zone or set up conditional forwarders based on the steps in the link below.  

https://social.technet.microsoft.com/Forums/windowsserver/en-US/9e501d72-5457-421a-b81b-3a1f83ac7b0e/setup-of-trust-relationship-between-2-domains?forum=winservergen

2.Create a Realm Trust through UI or netdom truat command on DC in Windows domain.

Create a Realm Trust  

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754706(v=ws.11)

3.We should make some AD (including trust) Port Requirements below listening.

For AD (including trust) Port Requirements, we can refer to the links below.  

Active Directory and Active Directory Domain Services Port Requirements  

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd772723(v=ws.10)?redirectedfrom=MSDN

Active Directory Replication over Firewalls  

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727063(v=technet.10)?redirectedfrom=MSDN

For the two commands, if we want to set some settings to support Kerberos realms (Ksetup) and support Kerberos authentication (Ktpass), we can use them if needed.

Best Regards，  

Daisy Zhou
