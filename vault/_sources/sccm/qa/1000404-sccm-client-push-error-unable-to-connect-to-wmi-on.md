---
title: "SCCM Client push error - ---> Unable to connect to WMI on remote machine, error = 0x80070005."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1000404/sccm-client-push-error-unable-to-connect-to-wmi-on
question_id: 1000404
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# SCCM Client push error - ---> Unable to connect to WMI on remote machine, error = 0x80070005.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1000404/sccm-client-push-error-unable-to-connect-to-wmi-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear experts,     

A small number of our client machines running Win 10 pro education 2004 or later, they are facing the client issue with error logs. I checked that WMI is consistent in client machine, server side can access client machine via \machinename\admin$, firewall disabled on client machine, all to no avail.    

Any idea we can check elsewhere?    

```
---> Trying the 'best-shot' account which worked for previous CCRs (index = 0x0)	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Attempting to connect to administrative share '\\DELL3620-01.test.edu.cn\admin$' using account 'test\CM_CPI'	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> The 'best-shot' account has now succeeded 14 times and failed 0 times.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Connected to administrative share on machine DELL3620-01.test.edu.cn using account 'test\CM_CPI'	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Trying the 'best-shot' account which worked for previous CCRs (index = 0x0)	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Attempting to make IPC connection to share 	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Searching for SMSClientInstall.* under '\\DELL3620-01.test.edu.cn\admin$\'	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Unable to connect to remote machine "DELL3620-01.test.edu.cn" using Kerberos with alternate account, error - 0x80070005.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
--> NTLM fallback is enabled, remote machine "DELL3620-01.test.edu.cn" is continuing with client push.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Unable to connect to WMI on remote machine "DELL3620-01.test.edu.cn", error = 0x80070005.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Unable to connect to remote machine "DELL3620-01" using Kerberos with machine account, error - 0x80070005.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
--> NTLM fallback is enabled, remote machine "DELL3620-01" is continuing with client push.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Unable to connect to WMI on remote machine "DELL3620-01", error = 0x80070005.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
---> Deleting SMS Client Install Lock File '\\DELL3620-01.test.edu.cn\admin$\SMSClientInstall.GTN'	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
Execute query exec [sp_CP_SetLastErrorCode] 2097152456, -2147024891	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
Stored request "2097152456", machine name "DELL3620-01", in queue "Retry".	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
Execute query exec [sp_CP_SetPushRequestMachineStatus] 2097152456, 2	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
Execute query exec [sp_CP_SetLatest] 2097152456, N'09/09/2022 06:07:21', 142	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
<======End request: "2097152456", machine name: "DELL3620-01".	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:07:21	14036 (0x36D4)  
CCR count in queue "Retry" is 1.	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:09:09	2624 (0x0A40)  
Sleeping for 661 seconds...	SMS_CLIENT_CONFIG_MANAGER	09/09/2022 14:09:09	2624 (0x0A40)
```

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-09-12*

Hi,    

1,A similar thread here for your reference. The workaround is to revert to May 2022 Cumulative Update.    

I have this error in SCCM------ Unable to connect to remote machine "LAPTO-01" using Kerberos with machine account, error - 0x80070005    

2,We can try to see if the manual installation works. If yes, maybe something is blocked between the server and client. Please check below options:    

a,Add the File and Printer Sharing and Windows Management Instrumentation (WMI) as exceptions to the Windows Firewall.    

b,Make sure that there are no DNS issues    

c,Firewall is not blocking the SMB traffic    

d,Make sure the RPC port 135 and the Dynamic port range is opened in any firewall between the client and the server including the windows firewall.    

3,You can try to add the following registry key on the server to disable the hardening changes, refer to KB5004442    

Path : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Ole\AppCompat    

Value Name: "RequireIntegrityActivationAuthenticationLevel"    

Type: dword    

Value Data: default = 0x00000000    

Thanks for your time.    

Best regards,    

Simon    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
