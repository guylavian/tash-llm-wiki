---
title: "Cannot access exchange url link outside of my network"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196414/cannot-access-exchange-url-link-outside-of-my-netw
question_id: 2196414
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# Cannot access exchange url link outside of my network

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196414/cannot-access-exchange-url-link-outside-of-my-netw (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi

I have my exchange server up an running, I can access my url links mail.xyx-system.com/owa and mail.xyx-system.com/ecp via all the clients on my network, but when i tried to access those links outside of my network "from an different ISP" I'm receiving "DNS_PROBE_FINISHED_NXDOMAIN" I've already set up my Send connector, please help.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-23*

Thanks for your reply!

If you've registered a domain name and correctly configured A records to point to your public IP address, but you still can't access your Exchange server from an external network, then Comcast's blocking of port 25 can really be a problem. Many ISPs restrict certain ports in residential areas to prevent spam and other malicious activities.

Here are some possible solutions and suggestions:  

-  If you can't send mail using port 25, you can consider using a different port, such as 587 (a secure port for sending SMTP mail) or 465 (SMTP SSL port). Make sure that these ports are configured on the Exchange server and that the appropriate port forwarding settings are made on the firewall and router.

-  You can consider using a virtual private network (VPN) to bypass your ISP's throttling. With a VPN, you can encrypt your traffic and route it through other networks, avoiding port throttling from your ISP.

-  Make sure your firewall settings allow external traffic to pass through the port of your choice (such as 587 or 465). Also, make sure that the Exchange server is configured to allow connections through these ports.

If you're still having trouble after trying these solutions, feel free to let me know and I'll do my best to help further!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-22*

Thanks for your replay

I have my domain registered and also configured the A record to my public IP address, but still cannot reached my exchange server from an external network, I was told that comcast blocked port 25 in residential areas, is there any other way that I can bypass that or use a different secured port ?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-18*

Thanks for your reply!  

Yes, if you are using a domain name that has not yet been registered, this does cause you to lose access to the domain name on the external network. An unregistered domain name is not resolved on a public DNS server, so the IP address of the domain name cannot be found by external users.

In your lab environment, you can test unregistered domain names using a local DNS server or by modifying your hosts file, but this only applies to the internal network. If you wish to access the domain name from an external network, you need to make sure that the domain name is registered with the domain registrar and that the DNS records are properly configured.

Here are some suggestions:

Make sure that the domain name you are using is registered with the domain registrar. Only the registered domain name can be resolved on the Internet.

Once the domain name is registered, you need to set up a DNS record in the domain registrar's control panel to make sure that the A record points to the public IP address of your Exchange server.

After the domain name registration and DNS records are configured, you can try accessing your Exchange server from an external network to see if the problem is resolved.

If you have additional questions or need further help, please feel free to let me know!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-02*

Thank you for your reply, I will try those steps in my lab soon, but I have one more question, if the domain is not registered yet would that be a problem, i was just labbing on a test domain but not on the one that I have registered.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-02*

Hello ,  

Thank you for posting in Microsoft Community forum.  

This issue is likely an internal DNS setup issue. To further troubleshoot this issue, please kindly try below steps:  

A "DNS_PROBE_FINISHED_NXDOMAIN" error usually indicates that the domain name cannot be resolved, which can be due to several reasons. Here are some possible solutions and checking steps:

-  Make sure that the DNS records for your domain (e.g. xyx-system.com) are set up correctly. You can use an online tool such as nslookup to check if the DNS resolution of your domain name is working properly.  

Make sure your domain's A record points to the correct IP address.

-  Check your firewall settings to make sure that external traffic can reach the relevant ports of the Exchange server (such as HTTP and HTTPS, usually ports 80 and 443).  

Make sure that requests from external networks are not blocked.

-  If you are using a router, make sure the router's port forwarding settings are correct to forward external requests to  

The internal IP address of the Exchange server.

-  Sometimes, your ISP may cache old DNS records or have other issues. You can try using a different DNS server like Google's 8.8.8.8 or Cloudflare's 1.1.1.1 to see if that fixes the issue.

-  If you use an SSL certificate, make sure that the certificate is properly installed and has not expired. Some browsers may refuse to connect due to SSL issues.

-  Make sure that the Exchange server's external URL is configured correctly. You can check these settings in the Exchange Management Center (ECP).

-  Clear the DNS cache on your computer, you can run the following command in the command prompt:  

ipconfig /flushdns

If you still can't resolve the issue after following the steps above, please provide more details, such as the DNS service provider you are using, the version of the Exchange server, etc., for more in-depth troubleshooting.

I hope the information above is helpful.  

If you have any questions or concerns, please feel free to let us know.  

Regards,  

Jill Zhou
