---
title: "Domain controller with DNS trying to register with external DNS/IP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1692475/domain-controller-with-dns-trying-to-register-with
question_id: 1692475
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Domain controller with DNS trying to register with external DNS/IP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1692475/domain-controller-with-dns-trying-to-register-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a domain controller that has the DNS role installed too.  Since yesterday (after demoting an older DC) I have noticed odd entries in the system log relating to DNS.  This is now a single domain controller in the domain.  DNS settings for the server are set to its own internal IP address for primary and 127.0.0.1 for its secondary. The error is seen pretty much every hour at the same time.

The dynamic registration of the DNS record 'ae3061c9-ba2b-457d-9a0d-ff8e0c23fd75._msdcs.*****#######.net. 600 IN CNAME #########.net.' failed on the following DNS server:  

DNS server IP address: 129.211.176.209 

Returned Response Code (RCODE): 0 

Returned Status Code: 9502  

For computers and users to locate this domain controller, this record must be registered in DNS.  

USER ACTION  

Determine what might have caused this failure, resolve the problem, and initiate registration of the DNS records by the domain controller. To determine what might have caused this failure, run DCDiag.exe. To learn more about DCDiag.exe, see Help and Support Center. To initiate registration of the DNS records by this domain  controller, run 'nltest.exe /dsregdns' from the command prompt on the domain controller or restart Net Logon service. 

  Or, you can manually add this record to DNS, but it is not recommended.  

ADDITIONAL DATA 

Error Value: Bad DNS packet.

I have tried flushing DNS, registering and then restarting the netlogon service.  Forwarders are setup to go to google DNS servers.

The IP address of the DNS server in the error changes each time but its the same addresses in a rotation.  I note they are always located in China.  I cannot see why it is trying to register with an external IP address.  Any assistance would be appreciated.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-06-11*

Hello,

 

Thank you for posting in Q&A forum.

To further troubleshoot this issue, please kindly follow below steps:

1.Please kindly run CMD command

ipconfig /all

to check perferred DNS setting

2.Run CMD command

nslookup domain

and check if this name resolution succeeds

3.Go to DNS console and check if there's any DNS forwarder configured

4.Capture a network trace by network monitor or wireshark and reproduce this issue. Filter "DNS" and related DNS Server IP address and check if there's any insight inside.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.
