---
title: "Active Directory Recovery succeeds but not able to view the AD Users and computers on Windows Server 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2185984/active-directory-recovery-succeeds-but-not-able-to
question_id: 2185984
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory Recovery succeeds but not able to view the AD Users and computers on Windows Server 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2185984/active-directory-recovery-succeeds-but-not-able-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Steps followed to create Active Directory - 

-  Installed the Active Directory Domain Service from Server roles and features. 

-  Promoted the Server to Domain Controller 

-  Created a forest with the name DEV.local and did not configure any DNS. 

-  Installed Windows Server backup tool 

-  Configured full system backup to network share which included the system state. 

After the backup was completed, I reset the machine to test the Windows Server Backup recovery flow to recover the AD- 

Steps followed to recover- 

-  Logged in to the administrator account 

-  Installed Windows server backup feature. 

-  Booted the OS into safe mode with Active directory repair enabled. 

-  Created a disk partition on the machine and moved the backup from network share to local disk. 

-  From the Windows server backup tool, selected the backup for recovery. 

-  Selected System state and enabled Authoritative restore in the menu. 

The restore operation was successful and rebooted the machine. After the reboot, I got the console pop-up with the message restore completed successfully. 

I exited from safe mode and logged in with the domain user, the login was successful but got a pop-up with the message "You've been Signed in with a Temporary Profile" 

To resolve this, From the registry, I deleted all the entries with .bak under HKLM\SOFTWARE\MICROSOFT\WINDOWS NT\CURRENT VERSION\PROFILE LIST and rebooted the system. With this, the Temporary profile issue was resolved. 

After reboot, I tried to open the Active Directory domain computers and users but it fails with the following message pop-up - 

Naming information cannot be located because:

The specified domain either does not exist or could not be contacted.

Contact your system administrator to verify that your domain is properly configured and is currently online.

I am also unable to create new users under this domain.

Kindly suggest what steps am I missing during AD setup, backup, or recovery to help resolve this issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-13*

Hello Manikanta_VH,  

Greetings!  

I am sorry I am not familiar with bare metal recovery. How did you perform bare metal recovery?  

Even with steps that you mentioned if I do a system state restore in DRSM I get blue screen after restore is completed.

A: You can do such test in another VM and check the result. All the steps I mentioned should be OK, because I did such test in my lab successfully.  

Backup and restore Domain Controller using built-in Windows backup role.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-12*

Hey Daisy,

I want to do bare metal recovery and I getting the error as mentioned above reply.

Even with steps that you mentioned if I do a system state restore in DRSM I get blue screen after restore is completed.

When I am doing bare metal recovery, the machine is able to detect the image but not able to restore it.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-12*

Hello Manikanta_VH,  

Good day!  

Enter DSRM: Start->Administrative Tools->System Configuration->Boot tab->Boot options->Safe boot->Active Directory repair->click OK->In the System Configuration->click Restart.   

```
-or-
```

Start or restart the DC, press F8 to enter the safe mode and then select “Directory Services Restore Mode”. 

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-03-08*

Hi Daisy,

As mentioned I followed the steps and created AD with DNS configured and took a full system backup. I created a separate volume to store this image on the machine. Now when I try to do system image recovery by booting into advanced boot options I get the following error.

How do I fix this?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-28*

Hello Manikanta_VH,  

Thank you for posting on the Microsoft Community Forum.

This information usually indicates that the attempted domain name or domain controller cannot be resolved or contacted. This may be due to DNS setup issues, network connectivity issues, or domain controller service status issues.  

As I understand, you have set up one forest with single domain with only one Domain Controller, am I right?  

1.Before you add the AD DS role and promote it as Domain Controller, you should set the static IP address as the IP address and set this IP address of this machine itself (or 127.0.0.1) as the Preferred DNS.  

2.You should set the DC as the DNS server (I mean you install DNS role on this machine). Also, check the GC option during promotion.

3.You can first check if your network connection is normal.  

4.Check if the IP address is pointing the DNS server correctly. Run ipconfig /all to check.  

5.If DNS resolution is normal, and if the network port is open (usually because the UDP 389 port is not open).  

6.After the DC is promote successfully, please check the health of the Domain Controller by running Dcdiag /v on it and check the result.  

7.If DC is healthy, you can install Windows server backup role and back up it.  

8.After back up it, you can restore it.  

 Note:  

1.If you back up the full server, you restore the full server.  

2.If you back up the system state, you restore the system state.  

3.Select location for system state recovery: Original location with the option “Perform an authoritative restore of Active Directory files”. By default, we do not select this check box “Perform an authoritative restore of Active Directory files”.  

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,  

Daisy Zhou
