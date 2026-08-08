---
title: "Domain controller with DNS trying to register with external DNS/IP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197671/domain-controller-with-dns-trying-to-register-with
question_id: 2197671
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: []
---
# Domain controller with DNS trying to register with external DNS/IP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197671/domain-controller-with-dns-trying-to-register-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a domain controller that has the DNS role installed too. Since yesterday (after demoting an older DC) I have noticed odd entries in the system log relating to DNS. This is now a single domain controller in the domain. DNS settings for the server are set to its own internal IP address for primary and 127.0.0.1 for its secondary. The error is seen pretty much every hour at the same time.

The dynamic registration of the DNS record 'ae3061c9-ba2b-457d-9a0d-ff8e0c23fd75._msdcs.*****#######.net. 600 IN CNAME #########.net.' failed on the following DNS server:

DNS server IP address: 129.211.176.209

Returned Response Code (RCODE): 0

Returned Status Code: 9502

For computers and users to locate this domain controller, this record must be registered in DNS.

USER ACTION

Determine what might have caused this failure, resolve the problem, and initiate registration of the DNS records by the domain controller. To determine what might have caused this failure, run DCDiag.exe. To learn more about DCDiag.exe, see Help and Support Center. To initiate registration of the DNS records by this domain controller, run 'nltest.exe /dsregdns' from the command prompt on the domain controller or restart Net Logon service.

Or, you can manually add this record to DNS, but it is not recommended.

ADDITIONAL DATA

Error Value: Bad DNS packet.

I have tried flushing DNS, registering and then restarting the netlogon service. Forwarders are setup to go to google DNS servers.

The IP address of the DNS server in the error changes each time but its the same addresses in a rotation. I cannot see why it is trying to register with an external IP address. I found that our internal domain name is registered by someone ie a website. The IP addresses that my DC/DNS server is trying to register with look to be name servers associated with this external domain. Why is it not referencing the internal domain for this? Any assistance would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-25*

Hi ED,

Thank you for your detailed update and for trying the steps I previously suggested. Based on your feedback, it seems like the issue may indeed be related to the domain name conflict, but there are some additional steps we can take to address this.

-  Check DNS Zone Settings:

-  Ensure that the DNS zones are correctly configured on your domain controller.

-  Open DNS Manager and expand the Forward Lookup Zones.

-  Verify that the records in `_msdcs.<yourdomain>` and `<yourdomain>` zones are correct and do not contain any references to external IP addresses.

-  Verify Dynamic Update Settings:

-  Ensure that dynamic updates are allowed for your DNS zones.

-  In DNS Manager, right-click on your DNS zone (e.g., `<yourdomain>`) and select Properties.

-  Under the General tab, ensure that `Dynamic updates` is set to `Secure only`.

-  Check for Stale or Incorrect Records:

-  Remove any stale or incorrect records that may be causing the registration attempts to external DNS.

-  Look specifically for any CNAME or A records that may be pointing to external addresses.

-  Run DCDiag with Specific Tests:

-  Run DCDiag with specific DNS-related tests to identify more detailed issues.        cmdCopy codedcdiag /test:DNS /v /s:<YourDomainControllerName>

-  Review Event Logs:

-  Review the event logs on your domain controller for any additional details or recurring errors.

-  Open Event Viewer and navigate to `Applications and Services Logs > Microsoft > Windows > DNS-Server` and `Directory Service` logs for detailed information.

-  Review Netlogon Logs:

-  Netlogon logs can provide additional details on the registration process.

-  Enable Netlogon logging by running the following command:        cmdCopy codenltest /DBFlag:0x2080FFFF

-  Check the Netlogon.log file located at `C:\Windows\debug\netlogon.log` for detailed logs.

-  Check Forwarding Zones and Root Hints:

-  Verify the settings for forwarding zones and root hints in DNS Manager.

-  Ensure that they are set correctly and not pointing to any unexpected external DNS servers.

Given that your internal domain name conflicts with an external domain name, consider the following:

-  Short-term Workaround:

-  Ensure that your internal DNS is authoritative for your internal domain and is correctly resolving all internal requests.

-  Continue to use forwarders to trusted external DNS servers (e.g., Google DNS) for any external queries.

-  Long-term Solution:

-  Consider renaming the internal domain to avoid conflicts with the external domain. This is a complex process and should be carefully planned and tested.

-  Microsoft provides a guide on Active Directory Domain Rename (https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-rename-domain) which can be a reference if you decide to take this step.

The DNS registration attempts to external IP addresses are likely due to the domain name conflict and configuration changes after demoting the old DC/DNS server. Please follow the additional steps provided to further diagnose and resolve the issue.

Thank you for your patience and cooperation. If the issue persists, please provide any additional logs or details, and we will continue to investigate further.

Best regards,

Rosy  

Forum Support Team

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

Hi,

Thank you for your reply.

I have tried steps 1, 2, 3 and 5.  DCDIAG lists the errors in the event log as posted as above, and refers to nltest which I have tried.  DNS is already set to itself and loopback address. Forwarders already set to Google. I restarted the netlogon service after the dns flush and register.

Step 4 appears to be the issue BUT the old DC/DNS server never had this error and there has been this conflict for year, our internal domain has always been named this along with the external domain being registered.  It was only when I demoted the old DC/DNS server and changed the DNS settings to itself (was Primary: old DC, secondary: self before).  However, there is no reference to use external DNS anywhere on this DC/DNS server so why would resolve the internal domain to the external one?  If I do a nslookup for the domain, it always returns the internal address, never the external domain.

thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

Hi ED, 

Thank you for providing detailed information about the DNS registration issue on your domain controller. Based on the details you shared, it seems that the DNS server is attempting to register DNS records with external IP addresses. Here are some steps to help resolve this issue: 

Step 1: Run DCDiag and NLTest Commands 

Run DCDiag 

DCDiag is a diagnostic tool that can help identify and resolve issues with Active Directory. Please run the following command to check the status of the domain controller: 

-  Open Command Prompt as Administrator. 

-  Enter the following command and press Enter:     dcdiag /v /c /d /e /s:<YourDomainControllerName> 

   Review any errors or warnings in the output and address them as indicated. 

Run NLTest 

NLTest can help check and register DNS records. Please run the following command: 

-  Open Command Prompt as Administrator. 

-  Enter the following command and press Enter: 

```
nltest /dsregdns
```

  

Step 2: Check DNS Settings 

Verify DNS Server Configuration 

-  Open DNS Manager. 

-  Ensure your domain controller is set to use its own internal IP address as the primary DNS server (e.g., 192.168.x.x) and 127.0.0.1 as the secondary DNS server. 

 Clear and Re-register DNS Records 

-  Open Command Prompt as Administrator. 

-  Enter the following command to clear the DNS cache:     ipconfig /flushdns 

  

-  Enter the following command to force DNS records re-registration: 

```
ipconfig /registerdns
```

 

 Step 3: Check and Configure DNS Forwarders 

Verify DNS Forwarders 

-  Open DNS Manager. 

-  Right-click your DNS server name and select **Properties**. 

-  Navigate to the **Forwarders** tab and ensure the forwarders are set to trusted DNS servers (e.g., Google DNS: 8.8.8.8 and 8.8.4.4). 

 Step 4: Check Domain Name Configuration 

 Verify Domain Name Conflict 

-  Ensure your internal domain name does not conflict with any external domain names. If you find that the internal domain name is the same as an external domain, consider changing the internal domain name to avoid conflicts. 

 Step 5: Check Netlogon Service 

Restart Netlogon Service 

-  Open Command Prompt as Administrator. 

-  Enter the following commands to restart the Netlogon service: 

```
net stop netlogon 

net start netlogon
```

Please try these steps and let me know the results. Thank you for your patience and cooperation. 

Best regards, 

Rosy
