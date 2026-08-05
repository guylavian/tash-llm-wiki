---
title: "Unable to add secondary ADFS server to the existing farm ADFS error: Failed to register SSL bindings for Device Registration Service: An item with the same key has already been added"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/183001/unable-to-add-secondary-adfs-server-to-the-existin
question_id: 183001
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Unable to add secondary ADFS server to the existing farm ADFS error: Failed to register SSL bindings for Device Registration Service: An item with the same key has already been added

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/183001/unable-to-add-secondary-adfs-server-to-the-existin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,    

I'm configuring Windows Server 2016 Active Passive ADFS server, the primary ADFS server ADFS01-VM has been set up fine using the steps in https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/install-the-ad-fs-role-service    

The SSL SAN certificate *.domain.com has been imported with no issue on the primary server.    

However, moving on to the secondary server called ADFS02-VM the error showing like below screenshot:    

Screenshot URL: https://i.imgur.com/oiyLsC1.png    

    

I have also executed the steps described in https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-support-for-alternate-hostname-binding-for-certificate-authentication    

Under the Primary DFS server ADFS01-VM PowerShell ISE as Administrator:    

```
Set-AdfsAlternateTlsClientBinding -Member ADFS02-VM.DOMAIN.com -Thumbprint 'B6DA73B83A759DEE37F975668266FE92B4E5F788'
```

This is the error message:    

```
Set-AdfsAlternateTlsClientBinding :   
PS0317: One or more of AD FS servers returned errors during execution of command 'Set-AdfsAlternateTlsClientBinding'.   
Error information:   
PS0316: AD FS Server: 'localhost', Error: 'The specified SSL certificate with thumbprint 'B6DA73B83A759DEE37F975668266FE92B4E5F788' does not meet the requirements for configuring alternate Tls Client binding. For more information see http://go.microsoft.com/fwlink/?LinkId=613586.'.  
PS0316: AD FS Server: 'ADFS02-VM.DOMAIN.com', Error: 'The specified SSL certificate with thumbprint 'B6DA73B83A759DEE37F975668266FE92B4E5F788' does not meet the requirements for configuring alternate Tls Client binding. For more information see http://go.microsoft.com/fwlink/?LinkId=613586.'.  
At line:1 char:1  
+ Set-AdfsAlternateTlsClientBinding -Member ADFS02-VM.DOMAIN.com -Th ...  
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
    + CategoryInfo          : NotSpecified: (:) [Set-AdfsAlternateTlsClientBinding], RemoteException  
    + FullyQualifiedErrorId : RuntimeException,Microsoft.IdentityServer.Management.Commands.SetAlternateTlsClientBinding
```

Your help would be greatly appreciated.

## Answers

_No answers on this thread._
