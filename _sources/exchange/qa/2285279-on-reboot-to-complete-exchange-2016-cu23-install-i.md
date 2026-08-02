---
title: "On reboot to complete Exchange 2016 CU23 install, it failed on step 7, PushNotification already exists."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2285279/on-reboot-to-complete-exchange-2016-cu23-install-i
question_id: 2285279
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# On reboot to complete Exchange 2016 CU23 install, it failed on step 7, PushNotification already exists.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2285279/on-reboot-to-complete-exchange-2016-cu23-install-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I tried installing Exchange 2016 CU23, on Server 2016 Standard. It went thru all the prerequisites checks fine, and asked to reboot to complete the installation. But upon reboot, at step 7 the following error occurs:

Error:

The following error was generated when "$error.Clear(); 

```
New-PushNotificationsVirtualDirectory -Role Mailbox -OAuthAuthentication:$RoleIsDatacenter -DomainController $RoleDomainController;

    " was run: "System.ArgumentException: The AD configuration for virtual directory 'PushNotifications' already exists in 'CN=PushNotifications (Exchange Back End),CN=HTTP,CN=Protocols,CN=EPO,CN=Servers,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups,CN=EBC,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=MIDIS-TTO,DC=local', please remove this AD configuration manually.
```

Parameter name: VirtualDirectoryName

   at Microsoft.Exchange.Configuration.Tasks.Task.ThrowError(Exception exception, ErrorCategory errorCategory, Object target, String helpUrl)

   at Microsoft.Exchange.Management.SystemConfigurationTasks.NewExchangeVirtualDirectory`1.InternalValidate()

   at Microsoft.Exchange.Configuration.Tasks.Task.<ProcessRecord>b__91_1()

   at Microsoft.Exchange.Configuration.Tasks.Task.InvokeRetryableFunc(String funcName, Action func, Boolean terminatePipelineIfFailed)".

I have tried restarting the relevant exchange services, disabling antivirus to no avail. On attempting to uninstall, so as to reinstall. But when I try this it detects an incomplete previous installation and tries to complete the previous installation, to again fail at the same step with the same error. Assistance would be greatly appreciated.

NigelS

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-18*

Hi @Nigel Sampath

Thank you for posting your question in the Microsoft Q&A forum.   

Based on your inquiry, we understand that you have received an annocunment relevant to PushNotifications when installing Exchange 2016 CU23. We will be glad to assist you in this part. 

According to the error code display, Its saying in  'PushNotifications' already exists in 'CN=PushNotifications (Exchange Back End) and you need to delete it manually . Could you please remove that with ADSI Edit (Be careful not to delete anything else and then re-run setup). 

If you need further assistance, please let us know.   

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".       

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
