---
title: "SCCM/MEM 2203 Client Push Failing, Kerberos, 0x80004005"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/965723/sccm-mem-2203-client-push-failing-kerberos-0x80004
question_id: 965723
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM/MEM 2203 Client Push Failing, Kerberos, 0x80004005

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/965723/sccm-mem-2203-client-push-failing-kerberos-0x80004 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a client PC that I cannot push install SCCM on.  This is a test case PC before a wider deployment.  The error is 0x80004005.  Kerberos is required, NTLM is not allowed on this domain.  The only suggestions I can find for a scenario similar to mine is to enable NTLM.  I can't do that, so I need to get Kerberos working, if that's the issue.    

Notes:    

-  The log files show successful kerberos connection to both ADMIN$ and IPC$.  Only later in the log does it indicate it failed right after searching for SMSClientInstall.    

-  There are no logs generated on the client.  It never pushes the installer to the client.    

-  Systems with the agent manually installed are working fine.  This appears to only be a client push issue.    

Here is the relevant log portion.    

```
======>Begin Processing request: "2097152019", machine name: "TESTPC1"  $$  
Execute query exec [sp_IsMPAvailable] N'AVH'~  $$  
---> Trying the 'best-shot' account which worked for previous CCRs (index = 0x0)~  $$  
---> Attempting to connect to administrative share '\\TESTPC1\admin$' using account 'TESTDOMAIN\sccmDeploy'~  $$  
---> SspiEncodeStringsAsAuthIdentity succeeded!~  $$  
---> SspiExcludePackage succeeded!~  $$  
---> SspiMarshalAuthIdentity succeeded!~  $$  
---> NetUseAdd succeeded!~  $$  
---> The 'best-shot' account has now succeeded 7 times and failed 0 times.  $$  
---> Connected to administrative share on machine TESTPC1 using account 'TESTDOMAIN\sccmDeploy'~  $$  
---> Trying the 'best-shot' account which worked for previous CCRs (index = 0x0)~  $$  
---> Attempting to make IPC connection to share  with Kerberos authentication ~  $$  
---> SspiEncodeStringsAsAuthIdentity succeeded for IPC$ authentication!~  $$  
---> SspiExcludePackage succeeded for IPC$ authentication!~  $$  
---> SspiMarshalAuthIdentity succeeded for IPC$ authentication!~  $$  
---> NetUseAdd succeeded for IPC$ authentication!~  $$  
---> Searching for SMSClientInstall.* under '\\TESTPC1\admin$\'~  $$  
---> Unable to connect to remote machine "TESTPC1" using Kerberos with alternate account, error - 0x80004005.  $$  
--> NTLM fallback is not enabled, remote machine "TESTPC1" is not continuing with client push.  $$  
---> Unable to connect to remote machine "TESTPC1.TESTDOMAIN.com" using Kerberos with machine account, error - 0x80070005.  $$  
--> NTLM fallback is not enabled, remote machine "TESTPC1.TESTDOMAIN.com" is not continuing with client push.  $$  
---> Unable to connect to remote machine "TESTPC1" using Kerberos with machine account, error - 0x80070005.  $$  
--> NTLM fallback is not enabled, remote machine "TESTPC1" is not continuing with client push.  $$  
---> Deleting SMS Client Install Lock File '\\TESTPC1\admin$\SMSClientInstall.AVH'~  $$  
Execute query exec [sp_CP_SetLastErrorCode] 2097152019, -2147024891~  $$  
Stored request "2097152019", machine name "TESTPC1", in queue "Retry".  $$  
Execute query exec [sp_CP_SetPushRequestMachineStatus] 2097152019, 2~  $$  
Execute query exec [sp_CP_SetLatest] 2097152019, N'08/12/2022 15:06:09', 93~  $$  

```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-08-16*

Hi,    

1,A similar thread here for your reference. The workaround is to revert to May 2022 Cumulative Update.    

Unable to connect to remote machine "LAPTO-01" using Kerberos with machine account, error - 0x80070005    

2,As the manual installation works, it's firstly recommended to add at least one client push installation account under Administration > Site Configuration > Site > Settings > Client Installation Settings > Client Push Installation to have a try. This account must be a member of the local Administrators group on the target client computers    

3,Maybe something is blocked between the server and client. Please check below options:    

a,Add the File and Printer Sharing and Windows Management Instrumentation (WMI) as exceptions to the Windows Firewall.    

b,Make sure that there are no DNS issues    

c,Firewall is not blocking the SMB traffic    

d,Make sure the RPC port 135 and the Dynamic port range is opened in any firewall between the client and the server including the windows firewall.    

Refer to: Troubleshooting SCCM ..Part I (Client Push Installation )    

Hope it helps. Thanks for your effort and time.    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
