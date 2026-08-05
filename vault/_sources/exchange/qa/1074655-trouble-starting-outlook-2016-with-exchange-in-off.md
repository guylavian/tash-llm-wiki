---
title: "Trouble starting Outlook 2016 with Exchange in offline lab"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1074655/trouble-starting-outlook-2016-with-exchange-in-off
question_id: 1074655
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Trouble starting Outlook 2016 with Exchange in offline lab

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1074655/trouble-starting-outlook-2016-with-exchange-in-off (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, I am testing a Hyper-V 2019 server that runs 3 virtual machines. These virtual machines have no access to LAN, they use an internal Hyper-V switch so the VM's can only communicatie with each other.  These virtual machines are clones of a real world and fully functional environment.  At the client office, everything works great. This test setup is offsite and we don't want to give it access to internet etc, it's just for testing purposes.    

1 exchange server, 1 domain controller/file server, 1 RDS server with Outlook 2016.     

The domain works fine in the offline setup, credentials work, no error messages in the logs, users can log on, webmail works.    

The only problem I'm trying to figure out is the fact that I cannot get Outlook to start.    

The setup is a bit unique but this is sort of the setup we have (and works great in real life)    

mailserver hostname = exchange.contoso.com      internal LAN IP   192.168.10.2  (dns entry in local domain DNS)    

mailserver hostname = exchange.contoso.com     external IP   185.125.xxx.xxx      (dns entry at domain hosting)    

client uses a SRV record to locate exchange autodiscover  -->     _autodiscover._tcp.customerdomain.com      10 1 443  exchange.contoso.com    

This causes Outlook to use the SRV record to point autodiscover to the exchange server and use the exchange server certificate because the client email domain is different from the mailserver, the mailserver hosts multiple domains but they all use the exchange certificate that way.    

Because this SRV record is usually added in the domain hosting of these email domains, they cannot be accessed in the test setup due to no internet.    

So we have added this SRV record in the local DNS of our own offline domain (created a zone for customerdomain.com, and created the SRV record). We can verify the record works if we test it using nslookup     

When starting Outlook we get the following message (not my screenshots but the exact same message):     

    

    

I would assume that if you have all the right records in your DNS that Outlook should be able to start. Webmail works fine, all exchange services are started, no errors in the event logs anywhere.    

Do you guys know if I would be missing something simple that would prevent Outlook from starting without having access to the internet? Any record I am forgetting here?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2022-11-04*

Hi @Caspar - ABO   ，    

Is the computer with the Outlook client joined to the domain?    

For using DNS, the client locates the Autodiscover service on the Internet by using the primary SMTP domain address from the user's email address.    

Please use a domain-joined computer to connect to Exchange by searching for the SCP object in AD.    

Here is an article about Autodiscover for your reference:Autodiscover service in Exchange Server | Microsoft Learn    

    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
