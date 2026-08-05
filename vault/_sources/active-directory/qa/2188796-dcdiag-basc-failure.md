---
title: "dcdiag basc failure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2188796/dcdiag-basc-failure
question_id: 2188796
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# dcdiag basc failure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2188796/dcdiag-basc-failure (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When I run DCDiag /Test:DNS /e /v on our new DC it outputs the following errors.  It only show PASS on itself.

When DCDiag is run from the existing DCs it passes on all except the new one

## Answer (community) — community member

*upvotes: 1 · updated: 2025-02-13*

Hello

-  DNS Configuration on the New DC

Ensure that the new DC is configured correctly with respect to DNS. The new DC should be using a static IP address and should point to itself as the primary DNS server.

Steps to check DNS settings on the new DC:

Open the DNS settings on the new DC:

Right-click on the Network Icon > Open Network & Internet Settings.

Click on Change adapter settings.

Right-click on your network adapter and select Properties.

Select Internet Protocol Version 4 (TCP/IPv4), then click Properties.

In the DNS section, ensure that the Preferred DNS Server is set to the new DC's IP address.

In the Alternate DNS Server, you can enter the old DC's IP address or the DNS server that the network is using.

Flush the DNS cache and re-register the DNS records:  

ipconfig /flushdns  

ipconfig /registerdns

After ensuring the new DC is properly configured to use DNS, rerun DCDiag /Test:DNS on the new DC and check if the issue persists.

-  Check DNS Zones on the New DC

Make sure that the new DC is properly integrated into the existing DNS zones. This includes checking both the Forward Lookup Zones and Reverse Lookup Zones.

Open the DNS Manager on the new DC or an existing DC.

Check the Forward Lookup Zone for the domain to see if the new DC's A records and SRV records (for domain controller services) are properly created.

Check for the reverse lookup zone to ensure the PTR record for the new DC is present.

If the necessary DNS records are missing, you may need to manually create them or re-run the ipconfig /registerdns command.

-  Ensure Proper Replication

If the new DC is not replicating DNS records properly from the other DCs, it might fail to resolve DNS queries correctly.

Run repadmin to check for replication issues:  

repadmin /replsummary

This will give you a summary of any replication issues between DCs. If replication is not happening, resolve the replication issue, which might be related to network connectivity, firewalls, or DNS settings.

-  Check DNS Server Roles

Ensure that the DNS server role is properly installed on the new DC and that the DNS server is running.

Check the DNS service status by running:  

Get-Service -Name DNS

If the service is not running, try to restart it:  

Restart-Service -Name DNS

-  Review DCDiag Errors

Look at the specific errors reported by DCDiag. Some common DNS errors you might encounter include:

"The DNS server is not authoritative for the zone": This could mean that the new DC’s DNS is not properly integrated into the forest or domain.

"DNS Lookup failed": This could indicate that DNS queries are not resolving between the DCs.

Review the exact error messages in the DCDiag output to help pinpoint where the issue lies.

-  Firewall and Network Connectivity

Check whether there are any firewalls blocking DNS traffic or any network connectivity issues between the new DC and the existing DCs.

Ensure that UDP/53 and TCP/53 are open between the DCs for DNS communication.

You can use telnet or PowerShell to test DNS connectivity between the new DC and the others:  

nslookup <old_dc_name_or_ip>

-  Verify Domain Controller SRV Records

You can manually check the _msdcs subdomain and ensure that the SRV records for the domain controllers are correct.

Open DNS Manager, navigate to _msdcs.domain.com (replace with your domain), and verify that the SRV records for all DCs, including the new one, are present.

I hope the above information is helpful to you.

Best regards

Runjie Zhai
