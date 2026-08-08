---
title: "On-prem exchange server & domain server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187736/on-prem-exchange-server-domain-server
question_id: 2187736
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# On-prem exchange server & domain server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187736/on-prem-exchange-server-domain-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello 

We have exchange 2019 and domain controller installed on separate windows 2019 servers where exchange server ip is 192.168.10.10 and the ip of DC is 192.168.10.20 and the portfarwading is configured properly 

Domain name is registered by domain registrar and public ip is associated with it the public ip is ex 180.180.180.180 the domain (example.com) is available in whois database 

Now we want to host the domain in our windows server and configure all required DNS records for mail send and receive

The question is how to configure dns server to act as public DNS server and be able to send and receive mails from all domains 

Note : there is no public dns manager for creating DNS record we must create all required record in our windows server 

Thanks in advance for helping and providing detailed information 

Sorry for my bad English

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-12*

Hi Team ,

We have setup Exchange server in lab .

-  DC and Exchange.

-  We have purchased the domain and updated in go daddy.( A records and MX records highlighted below) .

-  The ip 37.131.107.204 is static ip in the router and we have added port forwarding from our router to exchange server on port 25 and 587, 110

-  We have created send connector and we are waiting for the DNS records to be populated. (Now we get socket error while sending email in the logs).

-  We would like to know anything that we are missing apart from the above setup. please let us know.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-26*

Hi,

Thanks for update.

Then please past the step, instead to create an MX record and set the MX record's value to the FQDN of your Exchange server (e.g., mail.example.com) and assign it a priority value (e.g., 10).

And refer to PTR Record: Yes, it also matters. Optionally, This is important for email deliverability and spam prevention --- create a PTR (Pointer) record mapping your public IP address (e.g., 180.180.180.180) to the FQDN of your mail server (e.g., mail.example.com).

Then it might work to receive or transfer the mails in domain.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-24*

Thank you so much Karlie Weng

In the step 3 :

@ not accepting in the name field

And What about the ptr record

## Answer (community) — community member

*upvotes: 0 · updated: 2024-01-23*

Hi,

To configure your Windows Server as a public DNS server and set up the required DNS records for sending and receiving emails, you can follow these steps:

-  Install the DNS Server role on your Windows Server:

Open Server Manager.

Click on "Add roles and features."

Select the appropriate server and click "Next."

Choose the "DNS Server" role and proceed with the installation.

-  Configure the DNS Server:

Open the DNS Manager.

Right-click on your server name and select "Properties."

In the "Interfaces" tab, ensure that the server is listening on the correct IP address (192.168.10.20).

In the "Forwarders" tab, add the IP addresses of reliable external DNS servers provided by your ISP or other trusted sources.

Click "OK" to save the changes.

-  Create DNS records for your domain:

In the DNS Manager, expand your server name and then the "Forward Lookup Zones" folder.

Right-click on your domain name (example.com) and select "New Host (A or AAAA)."

Enter "@" in the "Name" field and the public IP address of your Exchange server (180.180.180.180) in the "IP address" field. This creates an A record for your domain.

Create additional DNS records as needed, such as MX records for email routing, SPF records for email authentication, and any other required records.

-  Configure MX records for email routing:

Right-click on your domain name (example.com) in the DNS Manager and select "New Mail Exchanger (MX)."

Leave the "Mail server" field blank (or enter a dot ".") to indicate the domain itself.

Set the "Preference" value (priority) to determine the order of mail server preference (lower value means higher priority).

Enter the fully qualified domain name (FQDN) of your Exchange server (e.g., mail.example.com) in the "Fully qualified domain name (FQDN) of the mail server" field.

Click "OK" to save the MX record.

-  Configure SPF records for email authentication:

Right-click on your domain name (example.com) in the DNS Manager and select "New Text (TXT)."

Enter the SPF record value, which specifies the authorized email servers for your domain. For example:

v=spf1 mx -all

This record allows the MX servers listed in your MX records to send email on behalf of your domain.

Click "OK" to save the SPF record.

-  Test your DNS configuration:

Use external DNS lookup tools or online services to verify that your DNS records are correctly propagated and resolving to the expected IP addresses.

Test email sending and receiving to ensure that your Exchange server can send and receive emails from other domains.

Remember to regularly monitor and maintain your DNS server to ensure its reliability and security. Additionally, consider implementing security measures such as firewall rules and DNSSEC to protect your DNS infrastructure.

Feel free to engage if there's any need.

Best Regards,

Karlie Weng
