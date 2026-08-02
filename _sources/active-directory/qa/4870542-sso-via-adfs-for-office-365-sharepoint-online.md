---
title: "SSO via ADFS for Office 365 (SharePoint Online)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4870542/sso-via-adfs-for-office-365-sharepoint-online
question_id: 4870542
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
---
# SSO via ADFS for Office 365 (SharePoint Online)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4870542/sso-via-adfs-for-office-365-sharepoint-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I try to configure SSO via ADFS for Office 365 and my virtual machine (Windows Server 2012 R2) with AD DC. ADFS is installed on my VM. My VM is located behind the router and i have done port forwarding to my
 VM, particularly 80, 443, 5985 ports.

I have successfully installed latest updates for Windows Server 2012 R2 and individual updates for ADFS (particularly KB3018886, KB3020773, KB3025078, KB3033917, KB3035025, KB3052122).

I have created additional UPN suffix on my AD.

I use the following script for my goal.

```
clear-host

$ErrorActionPreference = "Stop"

$adfsServerAddress = "example.com"
$domainName = "example.com"

$cred = Get-Credential -Message "Enter a Global Administrator account from Office 365"

Write-Host "Connecting to Microsoft Online Services with the credential" -foreground Green
Connect-MsolService -Credential $cred

Enable-PSRemoting -Force

Write-Host "Setting of the MSOL ADFS Context server to the ADFS server" -foreground Green
Set-MsolADFSContext -Computer $adfsServerAddress -logfile c:\log.txt

Write-Host "Converting of the domain to a federated domain" -foreground Green
Convert-MsolDomainToFederated -DomainName $domainName

Write-Host "Verifying federation" -foreground Green
Get-MsolFederationProperty -DomainName $domainName
```

In my case UPN suffix, $adfsServerAddress and $domainName are identical. Script is being run on my VM.

Script fails on cmdlet Set-MsolADFSContext. Error message is

```
Set-MsolADFSContext : The connection to example.com Active Directory
Federation Services 2.0 server failed due to invalid credentials.
At C:\Users\Administrator\Desktop\Office 365 ADFS configuration.ps1:16 char:1
+ Set-MsolADFSContext -Computer $adfsServerAddress -logfile c:\log.txt
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [Set-MsolADFSContext], Fed
   erationException
    + FullyQualifiedErrorId : ConnectionToGenevaServerFailed,Microsoft.Online.
   Identity.Federation.Powershell.ContextCredentialsCommand
```

I have the following log.

```
8/28/2015 3:47:38 AM    Command Set-MsolADFSContext invoked.
8/28/2015 3:47:38 AM    Creating ADFS Server PS session.
8/28/2015 3:47:38 AM    ContextCredentialsCommand:CreatePowerShellSessionToGenevaServer: Invoked.
8/28/2015 3:47:38 AM    Creating PS session to 'example.com' ADFS server
8/28/2015 3:47:38 AM    Connect using current logged-on user creds.
8/28/2015 3:47:38 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:47:38 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:47:38 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:47:39 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:47:39 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:47:39 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:47:39 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:47:39 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
8/28/2015 3:47:40 AM    Going to sleep mode for 1000 milliseconds before reattempt - 2
8/28/2015 3:47:41 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:47:41 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:47:41 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:47:42 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:47:42 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:47:42 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:47:42 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:47:42 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
8/28/2015 3:47:42 AM    Going to sleep mode for 2000 milliseconds before reattempt - 3
8/28/2015 3:47:44 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:47:44 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:47:44 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:47:45 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:47:45 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:47:45 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:47:45 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:47:45 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
8/28/2015 3:47:45 AM    Failure after too many retry attempts...
8/28/2015 3:47:45 AM    Wrong credentials to ADFS Server connection, attempt #'1'
8/28/2015 3:47:45 AM    Prompting the user for 'example.com' ADFS Server creds.
8/28/2015 3:47:45 AM    ContextCredentialsCommand:GetServerCredentials: Invoked.
8/28/2015 3:47:55 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:47:55 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:47:55 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:47:56 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:47:56 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:47:56 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:47:56 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:47:56 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
8/28/2015 3:47:56 AM    Going to sleep mode for 1000 milliseconds before reattempt - 2
8/28/2015 3:47:57 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:47:57 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:47:57 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:47:58 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:47:58 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:47:58 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:47:58 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:47:58 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
8/28/2015 3:47:58 AM    Going to sleep mode for 2000 milliseconds before reattempt - 3
8/28/2015 3:48:00 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:48:00 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:48:00 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:48:01 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:48:01 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:48:01 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:48:01 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:48:01 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
8/28/2015 3:48:01 AM    Failure after too many retry attempts...
8/28/2015 3:48:01 AM    Wrong credentials to ADFS Server connection, attempt #'2'
8/28/2015 3:48:01 AM    Prompting the user for 'example.com' ADFS Server creds.
8/28/2015 3:48:01 AM    ContextCredentialsCommand:GetServerCredentials: Invoked.
8/28/2015 3:48:17 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:48:17 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:48:17 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:48:18 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:48:18 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:48:18 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:48:18 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:48:18 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
8/28/2015 3:48:18 AM    Going to sleep mode for 1000 milliseconds before reattempt - 2
8/28/2015 3:48:19 AM    Runspace Connection info: Scheme:http Port:5985, AuthenticationType:Default Uri:example.com AppName:wsman, Shell:http://schemas.microsoft.com/powershell/Microsoft.PowerShell
8/28/2015 3:48:19 AM    Connection Uri: http://example.com:5985/wsman/
8/28/2015 3:48:19 AM    Opening runspace to 'http://example.com:5985/wsman/'
8/28/2015 3:48:20 AM    System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at System.Management.Automation.Runspaces.Internal.RunspacePoolInternal.EndOpen(IAsyncResult asyncResult)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
8/28/2015 3:48:20 AM    fullyQualifiedErrorId: System.Management.Automation.Remoting.PSRemotingDataStructureException
8/28/2015 3:48:20 AM    Command failed: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException: Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.ParseAndThrowErrorRecord(ErrorRecord errorRecord, String overRideErrorId)
   at Microsoft.Online.Identity.Federation.Powershell.PowerShellSession.VerifyAndReconnectRunSpacePool()
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.OpenToGenevaServer(PSCredential serverCredential)
   at Microsoft.Online.Identity.Federation.Powershell.ContextCredentialsCommand.<>c__DisplayClass2.b__0()
   at Microsoft.Online.Identity.Federation.Powershell.Utility.InvokeOperationWithRetry(Action operation, Type exceptionType, String errorId, Int32 retryCount, Int32 retryWaitTimeInMilliseconds)
8/28/2015 3:48:20 AM    Retry errorId: ConnectionToGenevaServerFailed
8/28/2015 3:48:20 AM    Retry exception: Microsoft.Online.Identity.Federation.Powershell.IdentityFederationException
...
8/28/2015 3:48:23 AM    Failure after too many retry attempts...
8/28/2015 3:48:23 AM    Wrong credentials to ADFS Server connection, attempt #'3'
```

As we can see we have the same error on all attempts

```
Connecting to remote server example.com failed with the following error message : The client cannot connect to the destination specified in the request. Verify that the service on the destination is running and is accepting requests. Consult the logs and documentation for the WS-Management service running on the destination, most commonly IIS or WinRM. If the destination is the WinRM service, run the following command on the destination to analyze and configure the WinRM service: "winrm quickconfig". For more information, see the about_Remote_Troubleshooting Help topic.
```

I have tried to execute "winrm quickconfig" and got following:

```
WinRM service is already running on this machine.
WinRM is already set up for remote management on this computer.
```

I get the same on "Enable-PSRemoting -Force" command.

In execution process of Set-MsolADFSContext it requests credentials for example.com two times. I input a valid credentials.

In event viewer i have records like

```
A logon was attempted using explicit credentials.

Subject:
    Security ID:        WMDOMAIN\Administrator
    Account Name:       Administrator
    Account Domain:     WMDOMAIN
    Logon ID:       0x10EF8F6
    Logon GUID:     {59d6d6bb-ed3f-ef6b-d744-b8a45aa4fa64}

Account Whose Credentials Were Used:
    Account Name:       administrator
    Account Domain:     WMDOMAIN
    Logon GUID:     {00000000-0000-0000-0000-000000000000}

Target Server:
    Target Server Name: example.com
    Additional Information: HTTP/example.com

Process Information:
    Process ID:     0x2208
    Process Name:       C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe

Network Information:
    Network Address:    -
    Port:           -

This event is generated when a process attempts to log on an account by explicitly specifying that account’s credentials.  This most commonly occurs in batch-type configurations such as scheduled tasks, or when using the RUNAS command.
```

I have no ideas what can be done else. Please, help.

## Answer (community) — community member

*upvotes: 0 · updated: 2015-08-29*

Hi Vladimir,  

Thank you for posting your query in Microsoft Community.  

Since the issue is related SharePoint, I kindly request you to post this query in the following TechNet forum for better suggestions.  

http://social.technet.microsoft.com/Forums/en-US/home?forum=sharepointgeneral

If you have any other queries related to Office products, feel free to reply and I'll be happy to further assist you.  

Thank you.
