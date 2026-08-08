---
title: "Kerberos encryption AES128 CTS HMAC and AES128 HMAC"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1112704/kerberos-encryption-aes128-cts-hmac-and-aes128-hma
question_id: 1112704
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Kerberos encryption AES128 CTS HMAC and AES128 HMAC

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1112704/kerberos-encryption-aes128-cts-hmac-and-aes128-hma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

We are hardening our server 2019 and we are using cis-cat (cisecurity.org) GPO recommendations. The "Network Security: Configure Encryption types allowed for Kerberos" setting started causing problems after October 2022. We have it set for Aes128, aes256, and future encryption and originally this wasn't causing issues. Now the problem that I am experiencing is with remote desktop not able to connect, also gpupdate /force gives out an error, rsop.msc works but gives an error as well. Here is what I tried that I know fixed the problem until the machine is restarted again.    

If I leave the domain, restart, delete the computer object, recreate the computer object, join the domain and restart, everything seems to work fine. Until I have to restart the system again and I am back at square one.     

Now if I enable rc4 , aes128, aes256 the remote desktop doesn't brake but I believe this is defaulting to rc4 and not using aes128 or aes256. Also I don't want to turn on Rc4.    

Here are some of the errors that the server experiences when we have the network security key set to AES128_HMAC, AES256_HMAC, and future encryption    

This error happened after trying to add remote desktop services again after we re joined the machine to the domain.    

```
The post installation configuration did not complete. Could not create the  
> Windows Management Instrumentation Windows Firewall exception on  
> server2.LAB.WN.EDU. Could not create the Windows Management  
> Instrumentation Windows Firewall exception on  
> server2.LAB.WN.EDU.  
> System.Management.Automation.Remoting.PSRemotingTransportException:  
> Connecting to remote server server2.LAB.WN.EDU failed with  
> the following error message : WinRM cannot process the request. The  
> following error with errorcode 0x80090342 occurred while using Kerberos  
> authentication: An unknown security error occurred.  
>  Possible causes are:  
>   -The user name or password specified are invalid.  
>   -Kerberos is used when no authentication method and no user name are  
> specified.  
>   -Kerberos accepts domain user names, but not local user names.  
>   -The Service Principal Name (SPN) for the remote computer name and port  
> does not exist.  
>   -The client and remote computers are in different domains and there is  
> no trust between the two domains.  
>  After checking for the above issues, try the following:  
>   -Check the Event Viewer for events related to authentication.  
>   -Change the authentication method; add the destination computer to the  
> WinRM TrustedHosts configuration setting or use HTTPS transport.  
>  Note that computers in the TrustedHosts list might not be authenticated.  
>    -For more information about WinRM configuration, run the following  
> command: winrm help config. For more information, see the  
> about_Remote_Troubleshooting Help topic.  
>    at  
> Microsoft.RemoteDesktopServices.Management.Cmdlets.CommonUtils.ExecutePowerShellScriptShowError(String  
> serverName, String script, Object argumentList)  
>    at  
> Microsoft.RemoteDesktopServices.Management.Cmdlets.CommonUtils.OpenFirewallPort(String  
> serverName)
```

ID40790:    

```
> The Security System has detected a downgrade attempt when contacting the  
> 3-part SPN  
  
  
 ldap/camp.id.wn.edu/******@ID.WN.EDU  
  
  
 with error code "The encryption type requested is not supported by the KDC.  
>  (0xc00002fd)". Authentication was denied.
```

ID10154:    

```
> The WinRM service failed to create the following SPNs: WSMAN/  
> server2.lab.wn.edu; WSMAN/server2.  
  
  
 Additional Data  
>  The error received was 5: %%5.  
  
  
 User Action  
>  The SPNs can be created by an administrator using setspn.exe utility.
```

Firewall has been disabled just in case.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-27*

You are not the only person. Any chance anyone else has found a solution? 

External link to Reddit with a similar issue but it isn't speaking about computer accounts, only user accounts: https://www.reddit.com/r/sysadmin/comments/sjop64/anyone_else_being_hit_with_lsasrv_event_id_40970/?scrlybrkr=38ad0813 

On the computer account front, does changing the local password in AD, force an update to newer encryption types? external link

https://ss64.com/ps/reset-computermachinepassword.html

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-18*

Did you find  a solution for this

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-14*

Anyone else having this problem or am  I the only one who has had this issue?
