---
title: "Remote PowerShell between LAN and DMZ/Exchange Edge Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2128353/remote-powershell-between-lan-and-dmz-exchange-edg
question_id: 2128353
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Remote PowerShell between LAN and DMZ/Exchange Edge Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2128353/remote-powershell-between-lan-and-dmz-exchange-edg (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi!

I'm trying to configure a dashboard to get regular updates on the health of our Exchange Servers. Now I've run into a roadblock:

I want to connect from a local server, where our dashboard system is running to our Exchange Edge Servers via Remote PowerShell, but I can't seem to be able to connect. I've activated remote PowerShell on the Edge Servers and tested WinRM, to make sure that we get passed the firewall, but then I get the following errors, depending on how I try to connect:

`$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http://<ServerName>/PowerShell/ -Authentication Kerberos -Credential $UserCredential`` `

`New-PSSession : [app370300] Connecting to remote server <ServerName> failed with the following error message : WinRM cannot process the request. The following error with errorcode 0x80090311 occurred while using Kerberos authentication: There are currently no logon servers available to service the logon request.`` `

`Possible causes are:`` `

`-The user name or password specified are invalid.`` `

`-Kerberos is used when no authentication method and no user name are specified.`` `

`-Kerberos accepts domain user names, but not local user names.`` `

`-The Service Principal Name (SPN) for the remote computer name and port does not exist.`` `

`-The client and remote computers are in different domains and there is no trust between the two domains. After checking for the above issues, try the following:`` `

`-Check the Event Viewer for events related to authentication.`` `

`-Change the authentication method; add the destination computer to the WinRM TrustedHosts configuration setting or use HTTPS transport.`` `

`Note that computers in the TrustedHosts list might not be authenticated.`` `` `

`-For more information about WinRM configuration, run the following command: winrm help config. For more`` ``information, see the about_Remote_Troubleshooting Help topic.`` `

`At line:1 char:12`` ``+ $Session = New-PSSession -ConfigurationName Microsoft.Exchange -Conne ...`` ``+            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`` ``   + CategoryInfo          : OpenError: (System.Manageme....RemoteRunspace:RemoteRunspace) [New-PSSession], PSRemotin`` ``  gTransportException + FullyQualifiedErrorId : AuthenticationFailed,PSSessionOpenFailed`

This error, I can understand. Exchange Online doesn't use IIS, so there is no URL to connect to, but then I tried Enter-PSSession and got this error:

`Enter-PSSession -ComputerName <ServerName> -Credential $UserCredential`` `

`Enter-PSSession : Connecting to remote server <ServerName> failed with the following error message : WinRM cannot process the request. The following error with errorcode 0x80090311 occurred while using Kerberos authentication: There are`` ``currently no logon servers available to service the logon request.`` `

`Possible causes are:`` `

`-The user name or password specified are invalid.`` `

`-Kerberos is used when no authentication method and no user name are specified.`` `

`-Kerberos accepts domain user names, but not local user names.`` `

`-The Service Principal Name (SPN) for the remote computer name and port does not exist.`` `

`-The client and remote computers are in different domains and there is no trust between the two domains.`` ``After checking for the above issues, try the following:`` `

`-Check the Event Viewer for events related to authentication.`` `

`-Change the authentication method; add the destination computer to the WinRM TrustedHosts configuration setting or`` ``use HTTPS transport.`` `

`Note that computers in the TrustedHosts list might not be authenticated.`` `` `

` -For more information about WinRM configuration, run the following command: winrm help config. For more information, see the about_Remote_Troubleshooting Help topic.`` ``At line:1 char:1`` ``+ Enter-PSSession -ComputerName <ServerName> -Credential $UserCredential`` ``+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`` ``   + CategoryInfo          : InvalidArgument: (<ServerName:String) [Enter-PSSession], PSRemotingTransportException`` ``   + FullyQualifiedErrorId : CreateRemoteRunspaceFailed`

I also tried adding -Authentication Negotiate, but the result was the same. :(

Does anyone here have experience in connecting Remote PowerShell to Exchange Edge Servers? I would be greatful for any and all input.

Best Regards,

Gerrit Deike (System Engineer Exchange)

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-10*

Hi @Gerrit Deike  ,

Welcome to the Microsoft Q&A platform!

Based on your description, you are experiencing some common issues related to remote PowerShell connections to Exchange Edge Servers. Let's troubleshoot this issue step by step:

-  Make sure that the username and password you are using are correct and have the necessary permissions.

-  Verify that Kerberos authentication is configured correctly. Kerberos requires that both the client and server are in the same domain or that there is a trust relationship between the domains.

-  Make sure that the SPN for the remote computer name and port exists. You can use the setspn command to check and set the SPN.

-  Make sure that WinRM is configured correctly on both the client and server. You can run winrm quickconfig on both machines to set the necessary settings.

If the target computer is not in the same domain, add it to the WinRM TrustedHosts list. Use the following command:

```
Set-Item WSMan:\localhost\Client\TrustedHosts -Value ""
```

If using HTTPS, make sure that the SSL certificate is configured correctly and trusted.

-  Verify that the firewall settings allow traffic on the necessary ports (the default value for HTTP is 5985 and the default value for HTTPS is 5986).

Make sure there are no network issues preventing communication between the client and server.

-  If Kerberos does not work, try using Basic or NTLM authentication. Note that Basic authentication requires HTTPS to be secure:

```
$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri http:///PowerShell/ -Authentication Basic -Credential $UserCredential
```

-  Make sure that remote PowerShell is enabled and configured correctly on the Exchange Edge server. You can enable it with the following command:

```
Enable-PSRemoting -Force
```

Please feel free to contact me for any updates. And if this helps, don't forget to mark it as an answer.

Best,

Jake Zhang
