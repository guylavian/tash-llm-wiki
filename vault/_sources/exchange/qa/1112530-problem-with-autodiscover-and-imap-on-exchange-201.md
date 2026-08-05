---
title: "Problem with autodiscover and IMAP on exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1112530/problem-with-autodiscover-and-imap-on-exchange-201
question_id: 1112530
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# Problem with autodiscover and IMAP on exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1112530/problem-with-autodiscover-and-imap-on-exchange-201 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

I have a problem with correctly working autodiscover on my exchange servers.    

This is my configuration:    

Domain name(external/internal): contoso.com    

I have an SSL wildcard certificate: *.contoso.com    

External IP addresses:     

-  1.1.1.1,     

-  2.2.2.2    

Exchange Servers:    

-  EXCH19A - 10.0.0.10    

-  EXCH19A - 10.0.0.20    

-  EXCH19B - 10.0.1.10    

-  EXCH19B - 10.0.1.20    

External DNS:     

-  mail.contoso.com > A > 1.1.1.1    

-  mail.contoso.com > A > 2.2.2.2    

-  autodiscover.contoso.com > A > 1.1.1.1    

-  autodiscover.contoso.com > A > 2.2.2.2    

Internal DNS:     

-  mail.contoso.com > 10.0.0.10    

-  mail.contoso.com > 10.0.1.10    

-  autodiscover.contoso.com > 10.0.0.10    

-  autodiscover.contoso.com  > 10.0.1.10    

These servers working in cluster:    

DNS: dag>10.0.0.20\ dag>10.0.1.20    

Here is the result from testconnectivity:    

266284-test-autodiscover.txt     

Here are port redirections on my firewall:    

    

The second problem is with IMAP configuration. IMAP is enabled. Some mailboxes don't synchronize correctly on outlook.     

For example: I see other emails in Outlook with Exchange protocol configuration and other emails in Outlook with IMAP protocol configuration on the same mailbox    

Any suggestions? In the beginning, I would like to repair autodiscover.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-23*

Hi,  

This is probably a problem with one mailbox. I tried it on other devices and there is the same problem.

Now I try to fix the failover cluster of dag.

There was on Exchange servers only one ethernet adapter with two IP addresses.

I add a new eth adapter and configure the second IP from eth1 on eth2.

Now I have:  

EXCH19A:  

ETH1: 10.0.0.10/27  

ETH2: 10.0.0.20/27

EXCH19B:  

ETH1: 10.0.1.10  

ETH2: 10.0.1.20

When I added new eth adapters I see a lot of new ReplicationDagNetwork and I think it's something wrong.  

I would like to change network on 192.168.x.x for replication - is it's gonna be ok?

In ECP/Servers/DAG where is configured witness, there are IP addresses:  

10.0.0.10  

10.0.1.20  

and it's wrong.

In AD I have a computer object colled "DAG01" and in DNS record A has DAG01.contoso.com with IP: 10.0.0.10 and it's wrong

Witness is:  

EXWitness with IP: 10.0.1.60

Now I would like to change DNS record A "DAG01" from 10.0.0.10 to 10.0.1.70.  

Next step when I change DNS I would like to change IP DAG on ECP. I will remove 10.0.0.10 and 10.0.1.20 and add only 10.0.1.70 and it's could be fine, yes?

How to fix EVENT ID 1259?

Cluster network name resource failed registration of one or more associated DNS name(s) because the cluster service failed clean up the existing records corresponding to the network name.

Cluster Network name: 'Claster name'  

DNS Zone: 'contoso.com'

Ensure that cluster name object (CNO) is granted permissions to the Secure DNS Zone.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-07*

Hi,    

I did a few tests on testconnectivity and that looks nice, but on every test, I have the same information about  certificate validation:    

Analyzing the certificate chains for compatibility problems with versions of Windows.    

The test passed with some warnings encountered. Please expand the additional details.    

Additional Details    

The Microsoft Connectivity Analyzer can only validate the certificate chain using the Root Certificate Update functionality from Windows Update. Your certificate may not be trusted on Windows if the "Update Root Certificates" feature isn't enabled.    

Outlook test:    

    

ActiveSync test:    

    

SMTP test:    

    

IMAP test:    

    

I can configure my mailbox on Outlook Mobile via exchange protocol and it's working - send/receive email but I cannot do this on external Outlook.    

I cannot configure the same account via IMAP protocol on Outlook Mobile, Outlook and Thunderbird. Where I use ports 993/465.    

    

Any suggestions?
