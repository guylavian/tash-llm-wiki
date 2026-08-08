---
title: "GPO UNC Hardening with Privacy not working when Hostname contains a hyphen"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/569202/gpo-unc-hardening-with-privacy-not-working-when-ho
question_id: 569202
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO UNC Hardening with Privacy not working when Hostname contains a hyphen

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/569202/gpo-unc-hardening-with-privacy-not-working-when-ho (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We had several Windows Server which contained a hyphen in their Hostname. For example, vm-hostname1   

We enabled UNC Hardening via GPO for all shares on the relevant hosts and want to ensure that Encryption (Privacy) is activated.   

\vm-hostname1.example.domain\* RequireMutualAuthentication=1, RequireIntegrity=1, RequirePrivacy=1  

When we check the SMB session details from the client via Powershell:   

`Get-SmbConnection | Select-Object -Property * `  

SmbInstance           : Default   

ContinuouslyAvailable : False   

Credential            : xxxx\xxxx   

Dialect               : 3.1.1   

Encrypted             : False   

NumOpens              : 1   

Redirected            : False   

Output omitted.....   

We also had some hosts without a hyphen in their hostname. On these Hosts the UNC Hardening with Privacy is working. SMB Session is encrypted.   

After struggling a bit around with the Problem, we located the hyphen in the Hostname. When a hyphen is present in the hostname, the UNC Hardening settings are ignored and encryption is not activated.   

I know Encryption could also be activated global on a server with `Set-SmbServerConfiguration -EncryptData $true`. It seems to be a Bug and the Registry Values are not parsed correct.   

Our prefered way is to enable encryption via UNC Hardening GPO. But it seems to be a bug.   

Any Suggestions?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-12-23*

Sorry for the thread bump, but this post was quite helpful to me and I thought I could help others.    

For anyone else that comes across this post, if you use Wireshark to monitor the traffic you can tell if its Signed or Encrypted.     

The PowerShell command on the client doesn't show the connection is Signed or Encrypted, even if it really is Signed or Encrypted as seen via Wireshark. From what I can gather, it only shows Encrypted or Signed if it's required via a GPO or the Client/Server has it required.    

Get-SmbConnection | FL ServerName,ShareName,Signed,Encrypted    

If within the UNC hardening for a \servername\ or \domainname.com\DFSNamespace and you have RequireMutualAuthentication=1, RequireIntegrity=1 as the hardening value, the SMB messages are signed.     

If the hardening value is "RequireMutualAuthentication=1, RequireIntegrity=1, RequirePrivacy=1" then the SMB messages are Encrypted.     

If the hardening value is nothing or there isn't a server or share entry, it's up to the client and server to negotiate their settings based on their own configuration.    

For determining if signing is being used, after the session setup you will see if the host is doing signing or not by checking if the smb signature blob in the smb header is 0 or not.    

I tested this with and without hyphens in the SMB servername.    

There's also a difference when it comes to Shares versus server name.    

For example, if you have \domainname.com\DFSNamespace set to require Signing (via UNC Hardening), but the underlying DFS target server \servername you have set to require encryption (again via UNC Hardening), it doesn't force encryption for the \domainname.com\DFSNamespace SMB connection.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-28*

Hello Netw0rkDude,  

Thank you for your question.  

We have a topic with a problem similar to yours, I recommend you see the article below:  

https://social.technet.microsoft.com/Forums/en-us/7ff4bafa-a65a-4741-83a2-b9e0cf1e36b3/hardened-unc-path-gpo-question?forum=winserverGP  

If the answer is helpful, please vote positively and accept as an answer.
