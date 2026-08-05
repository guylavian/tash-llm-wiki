---
title: "After promoting new domain controller. cannot no longer log into it, unless in directory recovery mode."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2196066/after-promoting-new-domain-controller-cannot-no-lo
question_id: 2196066
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 11
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# After promoting new domain controller. cannot no longer log into it, unless in directory recovery mode.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2196066/after-promoting-new-domain-controller-cannot-no-lo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have replicated this issue on multiple new server using both Windows server 2019 and 2022. Before promotion no issue logging in on domain, but after promotion it fails and no useful errors are logged.

After recent Windows updates, we seem to be having issues with our Windows Server 2016 domain controllers. After recent updates were installed, on server restarts we are unable to log into domain controllers normally (nothing happens when hitting enter after typing credentials, no error) We are able to start the server with the network card disabled and then log in (sometimes). Once logged in we are able to re-enable the network card and resume normal function.

To address this issue we were just going to build new domain controllers to replace the existing ones. However when promoting the new server to domain controllers we run into the authentication issue again. The promotion process appears to complete with error. We can see the new domain controllers in active directory and no errors are given during the promotion process.

Server can be joined to the domain without any problem. This issue seems to only affect domain controllers specifically. Once promoted to domain controller we cannot authenticate on the server anymore and need to use directory recovery mode to log in and demote the server.

Please help!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-24*

I had a similar issue in azure. Removing the Azure AD based Windows Login extension that was there prior allowed me to log in with the domain\administrator account.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-20*

on an azure-vm domain controller: add Azure Virtual Machine Extension 'InstallOpenSSH'

-  Connect using SSH to an Azure VM running Windows - Azure Virtual Machines | Microsoft Learn

ssh to server with admin creds, switch to 'powershell' and run this command (#uninstalling-azure-arc-setup)

-  Disable-WindowsOptionalFeature -Online -FeatureName AzureArcSetup

after restart, rdp works as expected :-)

## Answer (community) — community member

*upvotes: 0 · updated: 2024-05-07*

Hi,  

Any idea how to recover from this issue when all the DCs have this issue that same time and we can't get remote/console and PowerShell access to servers?  

we have 2 DC on win 2022 and both face this problem (first this happen on secondary server) and today it happens on main DC.

Regards

Salehi

## Answer (community) — community member

*upvotes: 0 · updated: 2024-04-02*

Hi Avi,

We've had this exact same issue, and it took me quite a while before I figured out what was happening.

I found out that if you promote a Windows Server 2022 system without the 'Azure Arc Setup' feature installed, everything completes without issues, but after the mandatory reboot we were unable to log in on the newly created DC in any way (not via RDP or on the console).  

Installing the Azure Arc Setup feature after having promoted the system doesn't seem to solve the issue.

I demoted the system using server manager from another DC, installed this feature, promoted it back to DC, and everything was fine after that.

I haven't checked with Server 2019 but I wouldn't be surprised if it's the same issue.

I'm starting to get more and more annoyed with Microsoft wanting all systems to be Internet connected, while there are very good reasons not to want that....

I hope this information solves your issue.

Regards,

Dennis

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-18*

Hi Avi Markowitz,

Thank you for posting in the Microsoft Community Forum.

It sounds like you're encountering persistent authentication issues after promoting new servers to domain controllers, specifically on Windows Server 2019 and 2022, and experiencing difficulties even after joining the domain without any problem. Here are some steps you can take to troubleshoot and potentially resolve this issue: 

-  **Review Windows Updates**: Since the issue seems to have started after recent Windows updates, review the updates that were installed on both the domain controllers and the newly promoted servers. Look for any updates that might be related to authentication, networking, or domain services. Consider rolling back these updates to see if it resolves the issue. 

-  **Check Group Policy Settings**: Ensure that there are no conflicting or misconfigured Group Policy settings that could be affecting authentication on the domain controllers. Pay special attention to policies related to security settings, network settings, and domain controller configuration. 

-  **Verify DNS Configuration**: Double-check the DNS settings on both the domain controllers and the newly promoted servers. Ensure that they are pointing to the correct DNS servers and that DNS resolution is working properly. Check for any DNS issues that might be preventing proper domain controller authentication. 

-  **Examine Active Directory Replication**: Verify that Active Directory replication is functioning correctly between all domain controllers in your environment. Use tools like Repadmin or Active Directory Sites and Services to check for any replication errors or issues. 

-  **Review Event Logs**: Look for any relevant error or warning messages in the event logs on both the domain controllers and the newly promoted servers. Pay attention to events related to authentication, domain services, and networking. 

-  **Check System Time Synchronization**: Ensure that the system time is synchronized across all domain controllers and member servers. Time discrepancies can cause authentication issues in Active Directory environments. 

-  **Test Authentication with Different Accounts**: Try logging in to the affected servers using different domain accounts, including administrative accounts and regular user accounts, to see if the issue is account-specific or affecting all authentication attempts. 

-  **Consider Firewall and Antivirus Settings**: Review the firewall and antivirus settings on both the domain controllers and the newly promoted servers. Ensure that there are no rules or policies blocking necessary network traffic or interfering with domain authentication processes. 

By carefully reviewing these areas and performing targeted troubleshooting steps, you should be able to identify and resolve the authentication issues you're experiencing with your domain controllers and newly promoted servers.

Best regards

Neuvi Jiang
