---
title: "Exchange Issue with Autodiscover and external mail communication RRS feed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202257/exchange-issue-with-autodiscover-and-external-mail
question_id: 202257
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange Issue with Autodiscover and external mail communication RRS feed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202257/exchange-issue-with-autodiscover-and-external-mail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I've got a problem with the initial configuration of an Exchange Server 2016. Sending/receiving internal emails works but not to/from the oudside. I tested the inbound SMTP mail flow with testconnectivity.microsoft.com which presents the following error message:    

"Testing TCP port 25 on host mx0.DOMAIN.TLD to ensure it's listening and open.    

The specified port is either blocked, not listening, or not producing the expected response."    

According to "netstat -a", a service is listening on port 25 on the mail server. However, this is not the case for the firewall server. Since all the network communication is routed through the firewall server, I guess no SMTP communication is possible between the mail server and outside. Can you confirm the analysis so far? How can I tell a service to listen on port 25 on the firewall, too? The respective firewall port is already opened.    

Can this be caused by an Autodiscover issue? When I test the Exchange ActiveSync with testconnectivity.microsoft.com it returns the following four error messages that I am also not able to solve:    

"The Microsoft Connectivity Analyzer is attempting to retrieve an XML Autodiscover response from URL https://DOMAIN.TLD:443/Autodiscover/Autodiscover.xml for user MAIL@keyman  .TLD    

The Microsoft Connectivity Analyzer failed to obtain an Autodiscover XML response.    

Additional Details    

A Web exception occurred because an HTTP 404 - 404 response was received from Unknown.    

[...]"    

Furthermore, it returns again similar port problems as described before:    

"Testing TCP port 443 on host autodiscover.DOMAIN:TLD to ensure it's listening and open.    

The specified port is either blocked, not listening, or not producing the expected response.    

Additional DetailsA network error occurred while communicating with the remote host."    

and    

"Testing TCP port 80 on host autodiscover.DOMAIN.TLD to ensure it's listening and open.    

The specified port is either blocked, not listening, or not producing the expected response.    

Additional Details    

A network error occurred while communicating with the remote host."    

Besides that, it presents a certificate warning:    

Analyzing the certificate chains for compatibility problems with versions of Windows.    

The test passed with some warnings encountered. Please expand the additional details.    

Additional Details    

The Microsoft Connectivity Analyzer can only validate the certificate chain using the Root Certificate Update functionality from Windows Update.     

Your certificate may not be trusted on Windows if the "Update Root Certificates" feature isn't enabled.    

Thanks a lot for any hint to solve the problem!

## Answer (community) — Microsoft Moderator

*upvotes: 1 · updated: 2020-12-18*

Hi,    

Have you configured port forwarding to Exchange server on your firewall server?    

To receive external mails and have the autodiscover and OWA to work, you need to forward incoming traffic to port 25, 80 and 443 on your firewall server to your Exchange server.    

For more information,please refer to:    

Network ports for clients and mail flow in Exchange    

The document lists the inbound and outbound ports needed.    

To send mails to external recipients,you need to setup a send connector to send to the internet.    

Here is also a Microsoft document on this topic:    

Create a Send connector in Exchange Server to send mail to the internet    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-15*

I have also tested with https://mxtoolbox.com whether the issue is related to the configuration of the DNS records. The result: the domain name correctly refers to the firewall server, the domain is not blacklisted, but the tool “failed to connect to SMTP host”. This seems to be strongly related to the problem that I cannot receive (but send emails).  Could this be caused by a configuration issue of Autodiscover or which service/function/component would you suggest having a closer look at?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

Thanks for your feedback. However, I already had added DOMAIN.TLD as an accepted domain, and I already had configured the email address policy.  

But I noted another issue that might be of interest. The tool testconnectivity.microsoft.com tested two different URLs with regard to Autodiscover. Do I really have to provide both of them (which seems not to be the case at the moment)?  

•	http://DOMAIN.TLD/Autodiscover/Autodiscover.xml  

•	http://Autodiscover.DOMAIN.TLD/Autodiscover/Autodiscover.xml  

Besides that, coming back to the port issue: for testing purposes, I have set up a thunderbird mail client on the server with an external email account. The result: I could send/receive emails using SMTP. Therefore, port 25 is not blocked as indicated by the error message I have shown you in the beginning:  

"Testing TCP port 25 on host mx0.DOMAIN.TLD to ensure it's listening and open. The specified port is either blocked, not listening, or not producing the expected response."  

I also double-checked again that a service is listening on port 25 (and on the other e-mail ports) on the firewall server.  

From my perspective, this looks like a DNS issue (and not like a firewall conflict with the Global/Local Group Policy Manage, the Network Policy Manager, or with another internal Windows component. Do you agree?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-05*

Thank you for proactively coming back to me! Unfortunately, the problem is not solved yet. Let me structure the status quo by the potential issues that might be responsible for the problem:  

DNS entries:  

I already had  added similar entries to the forward lookup zone of the internal DNS as you suggested:  

-  A CNAME record for autodiscover.DOMAIN.TLD referring to mailserver.DOMAIN.TLD;  

-  But the A record for mailserver.DOMAIN.TLD does refer to the mail server’s IP address and not to the IP address of the firewall server (as the internet-facing server). How could the mail server be contacted by using a domain name otherwise? Maybe, I got the idea wrong.  

Would an SRV record for autodiscover.DOMAIN.TLD referring to mailserver.DOMAIN.TLD also makes sense?  

Exchange certificate:  

A certificate is installed on the Exchange server containing entries for autodiscover.DOMAIN.TLD and mailserver.DOMAIN.TLD. Please note that TLD refers to the internal domain name (the same in the previous section) – the TLD of the mail domain is different. As described before, the DNS entries for the mail domain is in a public DNS (configured in the admin web interface of our domain-hosting provider).  

Mismatch between internal FQDN and the TLD of the mail domain:  

In the meanwhile, I also found sources saying that it is not necessarily a problem to have two mismatching domains. However, I’m still not entirely sure yet if special configurations are needed in this case.  

Issue with ports:  

Besides that, I could still imagine that the root cause lies at the port level since even open ports are shown as blocked from the outside. I already performed a port scan on the firewall server. The result is that all ports are presented as closed although 1) the respective e-mail ports are explicitly opened in the firewall and 2) services are listening on these ports (due to the port forwarding to the email server). Although all ports are shown as closed to the outside, I can connect to the firewall server via VPN and then connect to all servers via Remote Desktop. I also tried to temporarily deactivate the firewall - without success.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

Thanks for your answer.

The port forwarding is now configured for the respective ports (from the firewall server to the Exchange server). Now, I can see that services are listening on these ports on the firewall server and not only on the Exchange server as before.

When testing the Exchange ActiveSync two errors still occur:

- 

-  error message: "Attempting to send an Autodiscover POST request to potential Autodiscover URLs. Autodiscover settings weren't obtained when the Autodiscover POST request was sent. Test Steps: The Microsoft Connectivity Analyzer is attempting to retrieve an XML Autodiscover response from URL https://DOMAIN.TLD:443/Autodiscover/Autodiscover.xml for user MAIL@keyman  .TLD The Microsoft Connectivity Analyzer failed to obtain an Autodiscover XML response. Additional Details: A Web exception occurred because an HTTP 404 - 404 response was received from Unknown.“

- 

-  error message: „Testing TCP port 443 on host autodiscover.DOMAIN.TLD to ensure it's listening and open. The specified port is either blocked, not listening, or not producing the expected response.“
