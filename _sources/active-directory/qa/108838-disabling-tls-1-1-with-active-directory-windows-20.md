---
title: "Disabling TLS 1.1 With Active Directory (Windows 2016)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/108838/disabling-tls-1-1-with-active-directory-windows-20
question_id: 108838
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
---
# Disabling TLS 1.1 With Active Directory (Windows 2016)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/108838/disabling-tls-1-1-with-active-directory-windows-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We already disabled SSL 2.0, 3.0 & TLS 1.0 with DCs. As a security best practice we are planning to disable TLS 1.1 and keep only 1.2 with all DCs. Do we get any guidance in applying this change to all DCs and how this is going to affect other application servers and end users (how can we plan it properly)?   

Thanks in advance

## Answer (community) — community member

*upvotes: 1 · updated: 2020-09-27*

Hi @LMS  ,    

Disabling TLS 1.0 may have an impact if you still use for example:    

-  Older Windows or Linux operating systems    

-  Older printers that may not support TLS higher than 1.0    

I suggest you go through the following articles published by Microsoft:    

Solving the TLS 1.0 problem    

https://www.microsoft.com/security/blog/2019/02/11/solving-the-tls-1-0-problem    

Solving the TLS 1.0 Problem, 2nd Edition      

https://learn.microsoft.com/en-us/security/engineering/solving-tls1-problem    

To disable TLS 1.0 on your Windows Servers, you can refer to the official documentation here:    

https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings#tls-10    

----------    

(If the reply was helpful please don't forget to upvote or accept as answer, thank you)    

Best regards,    

Leon

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-30*

Hi,  

You can use Group preference policy to set registry key if you want disable TLS1.1 on many members servers.  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

Hi,  

According to my knowledge, if it has been disabled, there is no need to test.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-29*

Sorry ... What I'm looking for is to disable TLS 1.1 (I corrected my Q as well). TLS 1.0 is already disabled.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-28*

Hi，@LMS       

Use the following registry keys and their values to enable and disable TLS 1.0.    

 Important    

Disabling TLS 1.0 will break the WAP to AD FS trust. If you disable TLS 1.0 you should enable strong auth for your applications. See Enable Strong Authentication    

Enable TLS 1.0    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server] "Enabled"=dword:00000001    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server] "DisabledByDefault"=dword:00000000    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client] "Enabled"=dword:00000001    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client] "DisabledByDefault"=dword:00000000    

Disable TLS 1.0    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server] "Enabled"=dword:00000000    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server] "DisabledByDefault"=dword:00000001    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client] "Enabled"=dword:00000000    

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client] "DisabledByDefault"=dword:00000001    

Using PowerShell to disable TLS 1.0    

PowerShell    

New-Item 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server' -Force | Out-Null    

```
New-ItemProperty -path 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server' -name 'Enabled' -value '0' -PropertyType 'DWord' -Force | Out-Null  

New-ItemProperty -path 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server' -name 'DisabledByDefault' -value 1 -PropertyType 'DWord' -Force | Out-Null  

New-Item 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client' -Force | Out-Null  

New-ItemProperty -path 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client' -name 'Enabled' -value '0' -PropertyType 'DWord' -Force | Out-Null  

New-ItemProperty -path 'HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client' -name 'DisabledByDefault' -value 1 -PropertyType 'DWord' -Force | Out-Null  
Write-Host 'TLS 1.0 has been disabled.'
```

Hope this information can help you    

Best wishes    

Vicky
