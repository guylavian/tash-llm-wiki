---
title: "Unable to Unlock Active Directory Account - Tried Resetting Password"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2199356/unable-to-unlock-active-directory-account-tried-re
question_id: 2199356
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-user-logon-profiles"]
---
# Unable to Unlock Active Directory Account - Tried Resetting Password

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2199356/unable-to-unlock-active-directory-account-tried-re (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm encountering an issue with a user account in Active Directory that I can't seem to unlock. Despite repeated attempts to unlock the account, it remains locked. I’ve also tried resetting the user’s password, but the account still stays locked. Has anyone else experienced a similar issue, or does anyone have a potential solution to this problem? Any help would be appreciated!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-09-04*

Hello Houman Alavehzadeh1,

Thank you for posting in the Microsoft Community Forums.

 First of all, please refer to the following steps for account lockout troubleshooting:

-  First of all, you can check and enable the following logon audit on all DCs, so that we can easily check the protocols and client hostnames or IP addresses that failed to authenticate in the future. 	

It is recommended to enable the following audit policy on all domain controllers: 	

GPO: Default Domain Controller 	

Traditional Audit Policies: Computer Configuration\Windows settings 	Computer Configuration\Windows settings\security settings\local policies\audit policy 	

Audit Account Logon Events - Failure 	

Audit Account Management - Success and Failure 	

Audit Logon Events - Failure   	

Or use the advanced audit policy (advanced audit policy overrides the traditional audit policy by default).          

Computer Configuration\Windows settings\security settings\Advanced Audit Policy Configuration         

Logon/Logoff.         

Audit Account Lockout - Failure         

Audit Logon - Failure          

Audit Account Lockout - Failure Audit Logon - Failure         

Audit Kerberos Authentication Service - Failure         

Audit Credential Validation - Failure           

Account Management.         

Audit User Account Management - Success and Failure           

We can open CMD with administrator privileges on the domain controller and run the following command to force the policy to be refreshed and to check that the relevant audits are turned on.         

gpupdate /force         

auditpol /get /category:*

-  After the account has been locked out, determine on which domain control the account is locked out: 	

a. Note that the account will only be locked on one domain, and then the lockout will be replicated to other domains as an emergency. 	

b. On any domain machine, download and install lockoutstatus.exe: http://www.microsoft.com/downloads/en/details.aspx?familyid=D1A5ED1D-CD55-4829-A189- 99515B0E90F7&displaylang=en 	

c. You can refer to the document: “How to use the LockoutStatus.exe Tool” in http://technet.microsoft.com/en-us/library/cc738772(WS.10). aspx 	

d. Double click the tool, click File -> select target, enter the username and domain information, then click OK. (Here the username is the locked AD account) You can see all the DCs in the domain where the users are being sent incorrect passwords to authenticate. 	  	  	

If you find the case of wrong password verification on both PDC and normal DC, it means that the wrong password verification may be done on normal domain control and then sent to PDC for confirmation. In this case, we need the security log of the ordinary domain control.

-  Then go to the corresponding dc to check the security logs, 4740 (account lockout), 4771 (Kerberos authentication), 4776 (NTLM authentication) and other logs to analyze, can be filtered by the syntax: [System[(EventID=4771 or EventID=4776 or EventID=4740)]] and *[EventData[Data and (Data='user account')]]	First find the point in time of the account lockout in the 4740 event log in the security log on the DC, and then look at a couple of 4771 or 4776 event logs near the 4740 log (that contain the user's account name with an error code of 0X18 or 0xc000006a).	If it is Event 4771, it means that the user was using the kerberos authentication protocol, we need to refer to the following steps to troubleshooting:

-  check the “Client Address” in the 4771 event log to get the source IP address, if the address belongs to another domain controller, please log in to the domain controller to check the 4771 event logs near the same time period to get the IP address of the client in question.

-  After getting the IP address of the client, we can login to the client to check:

-  Check the credentials management to see if there are any old credentials of the cached users.

-  Check to see if the user's old credentials have been cached.

-  Check to see if the user's old credentials are cached. Check to see if the user's wrong password is used to mount a network drive.

-  Check to see if any other third-party programs are caching the user's wrong password.

If you can't locate what process is causing the problem, you can turn on audit logon event failure audit log on the computer to see if the 4625 log can locate what process is causing the problem.	Through the 4776 event log, we can get the Source workstation address, login to the computer to refer to the previous steps to check:

```
- Check the credentials management to see if there are any old credentials cached for the user.

- Check to see if the user's old credentials are cached. Check to see if the user has mounted the disk with the wrong password.

- Check to see if the user's old credentials have been cached. Check to see if the user's old credentials have been cached.

- Check if any other third-party programs have cached the user's wrong password.
```

Best regards

Neuvi
