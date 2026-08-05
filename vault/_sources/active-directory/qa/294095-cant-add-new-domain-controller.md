---
title: "Cant add new Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/294095/cant-add-new-domain-controller
question_id: 294095
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Cant add new Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/294095/cant-add-new-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello all and thanks in advance for any help. (sorry if i dont format something properly, first time posting here)  

I am trying to migrate a clients domain from a server running 2008R2 to and server running 2019.  

their domain is ad.clientdomain.com according to the 2008 DC  

the first issue happens when i try to add the new 2019 server to the domain. i go to add the domain and type in ad.clientdomain.com and i get the below error.  

```
Note: This information is intended for a network administrator.  If you are not your network's administrator, notify the administrator that you received this information, which has been recorded in the file C:\Windows\debug\dcdiag.txt.
The following error occurred when DNS was queried for the service location (SRV) resource record used to locate an Active Directory Domain Controller (AD DC) for domain "ad.clientdomain.com":
The error was: "DNS name does not exist."
(error code 0x0000232B RCODE_NAME_ERROR)
The query was for the SRV record for _ldap._tcp.dc._msdcs.ad.clientdomain.com
Common causes of this error include the following:
- The DNS SRV records required to locate a AD DC for the domain are not registered in DNS. These records are registered with a DNS server automatically when a AD DC is added to a domain. They are updated by the AD DC at set intervals. This computer is configured to use DNS servers with the following IP addresses:
192.168.254.2
- One or more of the following zones do not include delegation to its child zone:
ad.clientdomain.com
clientdomain.com
com
. (the root zone)
```

i can get around this by changing the domain name that i am trying to join from ad.clientdomain.com to clientdomain. but, after it joins i can this error  

```
changing the promary domain DNS name of this computer to "" failed. the name will remain "ad.clientdomain.com".

the specified domain either does not exist or could not be contected.
```

after it reboots and i try to promote it to a DC it says it cannot contact to domain controller  

I have the old DC set as the DNS server on the new server  

let me know if more info is needed.   

thanks again for any help!  

-Josiah

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

Just checked, the Domain controller does have itself listed as the only DNS server.  

ran ipconfig /flushdns, ipconfig /registerdns, restarted the netlogon services, then re ran the dcdiag /v and got the same resaults

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-03-04*

I'd check the domain controller has own static ip address listed for DNS and no others such as router or public DNS. Then do ipconfig /flushdns, ipconfig /registerdns, restart the netlogon service, then check results.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

I ran DCDIAG /v and got this in the output  

```
Doing initial required tests

   Testing server: Default-First-Site-Name\CLIENTSERVER
      Starting test: Connectivity
         * Active Directory LDAP Services Check
         The host 2e660063-3e0a-4ba7-9737-726faa6cd755._msdcs.ad.clientdomain.com
         could not be resolved to an IP address. Check the DNS server, DHCP,
         server name, etc.
         Got error while checking LDAP and RPC connectivity. Please check your
         firewall settings.
         ......................... CLIENTRSERVER failed test Connectivity
```

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-04*

Hello and thank you for the reply.  

-  only 1 domain  

-  only 1 DC on the 1 domain  

-  windows server 2008 R2  

-  yes?  

-  domain function level is 2008  

-  looks like that registry subkey exists but is set to 0. so I guess I am using FRS.  

I will be trying to follow the steps you gave me this afternoon will post results  

thank you

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-02*

Hello @Josiah brainard  ,

Thank you for posting here.

Please confirm the following information at your convenience:  

1.How many Domains do you have in your AD domain?  

2.How many DCs in each domain if you have multiple domains?  

3.What are the operating system of all DCs?  

4.Are all DCs in your domain also DNS servers?

As I understand:  

The minimum requirement to add a Windows Server 2019 Domain Controller is a Windows Server 2008 functional level. The domain also has to use DFS-R as the engine to replicate SYSVOL.

5.What is the forest/domain functional level? Should be at least Windows Server 2008 functional level.  

6.What is the SYSVOL replication engine? FRS or DFSR? Should be DFSR.

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\DFSR\Parameters\SysVols\Migrating Sysvols\LocalState registry subkey. If this registry subkey exists and its value is set to 3 (ELIMINATED), DFSR is being used. If the subkey does not exist, or if it has a different value, FRS is being used.

For your request, you want to add a server 2019 to the existing domain, we can set one IP address of active DC/DNS server as its Preferred DNS.

Then try to join this server 2019 to domain and provide one domain credential.

After adding the server 2019 to domain, then check the information before we promoting server 2019 as DC.

Before we do any change in existing AD domain environment, we had better do:  

1.Check if AD environment is healthy. Check all DCs in this domain is working fine by running Dcdiag /v. Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum.  

forest/domain functional level should be at least Windows Server 2008 functional level  

2.SYSVOL replication should be DFSR.  

3.Back up all domain controllers.  

4.Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC.  

5.Check we can update gpupdate /force on each DC successfully.

Based on the description "after it reboots and i try to promote it to a DC it says it cannot contact to domain controller", which DC do you specify when you select replication partner?

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
