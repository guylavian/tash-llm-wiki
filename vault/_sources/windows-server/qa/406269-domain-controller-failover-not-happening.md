---
title: "Domain controller failover not happening"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/406269/domain-controller-failover-not-happening
question_id: 406269
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain controller failover not happening

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/406269/domain-controller-failover-not-happening (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have multiple domain controllers on a single network. All DCs are running Windows Server 2012 Standard. When I shutdown the "primary" domain controller, and try to logon to another server (tesing failover), I get the following results:

Connecting to dc2, I get:  

estimating connection quality  

welcome  

applying user settings  

please wait for the local session manager

Then it logs me into the session. However, each of these messages take a long time to come up, and when I run nslookup on this machine, I get:  

dns request timed out  

default server: unknown  

Address: <ip address of primary dc (which is turned off)>

Trying to log on to another server, I get:  

after Welcome screen:  

There are currently no logon servers available to service the logon request.

I have the DNS ip addresses for Preferred and Alternate DNS Servers for each machine set to the ip addresses of the "primary" dc and dc2.

I am including a genericized dcdiag capture for dc2 below. I ran this command from the "primary" dc:

C:\Windows\system32> dcdiag /test:dns /v /s:dc2.domain.local /DnsDynamicUpdate

Directory Server Diagnosis

Performing initial setup:  

* Connecting to directory service on server dc2.domain.local.  

* Identified AD Forest.  

Collecting AD specific global data  

* Collecting site info.  

Calling ldap_search_init_page(hld,CN=Sites,CN=Configuration,DC=domain,DC=local,LDAP_SCOPE_SUBTREE,(objectCategory=ntDSSiteSettings),.......  

The previous call succeeded  

Iterating through the sites  

Looking at base site object: CN=NTDS Site Settings,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domain,DC=local  

Getting ISTG and options for the site  

* Identifying all servers.  

Calling ldap_search_init_page(hld,CN=Sites,CN=Configuration,DC=domain,DC=local,LDAP_SCOPE_SUBTREE,(objectClass=ntDSDsa),.......  

The previous call succeeded....  

The previous call succeeded  

Iterating through the list of servers  

Getting information for the server CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domain,DC=local  

objectGuid obtained  

InvocationID obtained  

dnsHostname obtained  

site info obtained  

All the info for the server collected  

Getting information for the server CN=NTDS Settings,CN=dc2,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domain,DC=local  

objectGuid obtained  

InvocationID obtained  

dnsHostname obtained  

site info obtained  

All the info for the server collected  

Getting information for the server CN=NTDS Settings,CN=dc3,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=domain,DC=local  

objectGuid obtained  

InvocationID obtained  

dnsHostname obtained  

site info obtained  

Server is an RODC  

All the info for the server collected  

* Identifying all NC cross-refs.  

* Found 3 DC(s). Testing 1 of them.  

Done gathering initial info.

Doing initial required tests

Testing server: Default-First-Site-Name\dc2  

Starting test: Connectivity  

* Active Directory LDAP Services Check  

Determining IP4 connectivity  

* Active Directory RPC Services Check  

......................... dc2 passed test Connectivity

Doing primary tests

Testing server: Default-First-Site-Name\dc2  

Test omitted by user request: Advertising  

Test omitted by user request: CheckSecurityError  

Test omitted by user request: CutoffServers  

Test omitted by user request: FrsEvent  

Test omitted by user request: DFSREvent  

Test omitted by user request: SysVolCheck  

Test omitted by user request: KccEvent  

Test omitted by user request: KnowsOfRoleHolders  

Test omitted by user request: MachineAccount  

Test omitted by user request: NCSecDesc  

Test omitted by user request: NetLogons  

Test omitted by user request: ObjectsReplicated  

Test omitted by user request: OutboundSecureChannels  

Test omitted by user request: Replications  

Test omitted by user request: RidManager  

Test omitted by user request: Services  

Test omitted by user request: SystemLog  

Test omitted by user request: Topology  

Test omitted by user request: VerifyEnterpriseReferences  

Test omitted by user request: VerifyReferences  

Test omitted by user request: VerifyReplicas

```
Starting test: DNS

     DNS Tests are running and not hung. Please wait a few minutes...
     See DNS test in enterprise tests section for results
     ......................... dc2 passed test DNS
```

Running partition tests on : ForestDnsZones  

Test omitted by user request: CheckSDRefDom  

Test omitted by user request: CrossRefValidation

Running partition tests on : DomainDnsZones  

Test omitted by user request: CheckSDRefDom  

Test omitted by user request: CrossRefValidation

Running partition tests on : Schema  

Test omitted by user request: CheckSDRefDom  

Test omitted by user request: CrossRefValidation

Running partition tests on : Configuration  

Test omitted by user request: CheckSDRefDom  

Test omitted by user request: CrossRefValidation

Running partition tests on : domain  

Test omitted by user request: CheckSDRefDom  

Test omitted by user request: CrossRefValidation

Running enterprise tests on : domain.local  

Starting test: DNS  

Test results for domain controllers:

```
DC: dc2.domain.local
        Domain: domain.local

           TEST: Authentication (Auth)
              Authentication test: Successfully completed

           TEST: Basic (Basc)
              The OS
              Microsoft Windows Server 2012 Standard (Service Pack level: 0.0)
              is supported.
              NETLOGON service is running
              kdc service is running
              DNSCACHE service is running
              DNS service is running
              DC is a DNS server
              Network adapters information:
              Adapter
              [00000011] Broadcom BCM5709C NetXtreme II GigE (NDIS VBD Client):

                 MAC address is dc2_mac_address
                 IP Address is static
                 IP address: dc2_ip_address
                 DNS servers:
                    dc_ip_address (DC) [Valid]
                    dc2_ip_address (dc2) [Valid]
              The A host record(s) for this DC was found
              The SOA record for the Active Directory zone was found
              The Active Directory zone on this DC/DNS server was found primary
              Root zone on this DC/DNS server was not found

           TEST: Dynamic update (Dyn)
              Test record dcdiag-test-record added successfully in zone domain.local
              Test record dcdiag-test-record deleted successfully in zone domain.local

     Summary of test results for DNS servers used by the above domain
     controllers:

        DNS server: dc_ip_address (DC)
           All tests passed on this DNS server
           Name resolution is functional._ldap._tcp SRV record for the forest root domain is registered

        DNS server: dc2_ip_address (dc2)
           All tests passed on this DNS server
           Name resolution is functional._ldap._tcp SRV record for the forest root domain is registered

     Summary of DNS test results:

                                        Auth Basc Forw Del  Dyn  RReg Ext
        _________________________________________________________________
        Domain: domain.local
           dc2                          PASS PASS n/a  n/a  PASS n/a  n/a

     ......................... domain.local passed test DNS
  Test omitted by user request: LocatorCheck
  Test omitted by user request: Intersite
```

C:\Windows\system32>

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-26*

Hello @ck  ,    

Thank you for your update.    

Here is my test in my lab.    

I have three DCs: PDC, BDC and RODC.    

PDC: vchzho720vm   192.168.2.53    

BDC: vchzho0280vm 192.168.2.61    

RODC:vchhzo367vm  192.168.2.58    

    

Here are DNS settings on three DCs.    

    

When PDC running:    

    

    

    

When PDC shut down:    

    

1-I sign out the domain admin on BDC and sign in again with the same domain Admin on BDC, it took about 60 seconds.    

2-When BDC is running and I sign in with domain admin on BDC, then I sign out the domain admin on RODC and sign in again with the same domain Admin on RODC, it took about 60 seconds.    

3-When BDC is running and no account logs on BDC (not shut down), then I sign out the domain admin on RODC and sign in again with the same domain Admin on RODC, it took about 60 seconds.    

4-When BDC is shut down, then I sign out the domain admin on RODC and sign in again with the same domain Admin on RODC, it took about 60 seconds.    

For the issue:     

Trying to log on to another server, I get:    

after Welcome screen:    

There are currently no logon servers available to service the logon request.    

I think maybe the passwords are not replicated to RODC, and there is no DC to authenticated.    

For more information, please refer to link below.    

Understanding “Read Only Domain Controller” authentication    

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/understanding-8220-read-only-domain-controller-8221/ba-p/395031    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-25*

Hello @ck  ,    

Thank you for your update.    

1-I mean whether you install and configure DNS role on all three DCs?    

3. Not sure what you're asking .. dc is the SOA and dc and dc2 have NS records in DNS. All three dc's have CNAME records in DNS.    

2-How did you set DNS on all three DCs?    

For example:    

On dc (primary DC)    

Preferred DNS server: IP address of primary DC    

Alternative DNS server: IP address of dc2    

OR    

Preferred DNS server: IP address of dc2    

Alternative DNS server: IP address of primary DC    

On dc2    

Preferred DNS server: IP address of primary DC    

Alternative DNS server: IP address of dc2    

OR    

Preferred DNS server: IP address of dc2    

Alternative DNS server: IP address of primary DC    

On RODC bu     

Preferred DNS server: IP address of primary DC    

Alternative DNS server: IP address of dc2    

OR    

Preferred DNS server: IP address of dc2    

Alternative DNS server: IP address of primary DC    

3-Did you mean you log on RODC (bu)?     

Trying to log on to another server, I get:    

after Welcome screen:    

There are currently no logon servers available to service the logon request.    

Then I will do a test in my lab.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-24*

Hello @ck  ,

Thank you for posting here.

To better understand our question, please confirm the following information at your convenience.

1.Is your AD forest single forest with single domain?

2.If your AD forest is single forest with single domain, how many DCs in your domain?

3.Are all the DCs in your domain DNS server?

4.How many sites do you have?

5.Based on the description:  

When I shutdown the "primary" domain controller, and try to logon to another server (tesing failover), I get the following results" and "Trying to log on to another server, I get", do you mean you logon the Domain Controllers or member server?

6.Based on "Then it logs me into the session. However, each of these messages take a long time to come up, and when I run nslookup on this machine, I get:  

dns request timed out  

default server: unknown  

Address: <ip address of primary dc (which is turned off)>

How did you run nslookup command? Did you run nslookup + ip address of primary dc?

7.Based on the description "I have the DNS ip addresses for Preferred and Alternate DNS Servers for each machine set to the ip addresses of the "primary" dc and dc2.", do you mean you have the same DNS set on all DCs, member servers, workstations and clients?

Also, please check if you keep PDC start and running, if the two issues you mentioned in the post are OK?

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
