---
title: "Set custom port for ADFS Proxy (Web Application Proxy) on Windows 2012 R2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/53091/set-custom-port-for-adfs-proxy-web-application-pro
question_id: 53091
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Set custom port for ADFS Proxy (Web Application Proxy) on Windows 2012 R2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/53091/set-custom-port-for-adfs-proxy-web-application-pro (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi;  

I am configuring a AD FS Proxy (WAP) on Windows 2012 R2 server, the default https port is 443 and I want to use port 8443 instead of port 443 for the https traffic coming in from my 3rd party hosted cloud system.  My understand that I need to issue Set-ADFSProxyProperties -HttpsPort to change but when I issue this command, I got "The term 'Set-ADFSProxyProperties' is not recognized as the name of a cmdlet..."  

This is a AD FS Proxy server, so I do not install the complete ADFS.  What can I do to install the PowerShell cmdlets for me to complete the following execution.  

Get-ADFSProxyProperties  

Set-ADFSProxyProperties  

I had run the following command to add the NuGet package onto my ADFS Proxy server but not working for those command above.  

Install-PackageProvider -Name NuGet -RequiredVersion 2.8.5.208 -Force  

Import-PackageProvider -Name NuGet -RequiredVersion 2.8.5.208  

How can I list if "Get-ADFSProxyProperties" cmdlet and "Set-ADFSProxyProperties" cmdlet is available in my PowerShell?  

Thanks!

## Answers

_No answers on this thread._
