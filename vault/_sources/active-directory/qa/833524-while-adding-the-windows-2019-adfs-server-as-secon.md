---
title: "While adding the Windows 2019 ADFS server as secondary server in existing WS2012R2 adfs farm, the setup fails with error \"MSIS7711:PolicyOperationFault\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/833524/while-adding-the-windows-2019-adfs-server-as-secon
question_id: 833524
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# While adding the Windows 2019 ADFS server as secondary server in existing WS2012R2 adfs farm, the setup fails with error "MSIS7711:PolicyOperationFault"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/833524/while-adding-the-windows-2019-adfs-server-as-secon (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Preparing for ADFS migration from 2012R2 to 2019 I am trying to add a new WS 2019 node to ADFS farm running on WS 2012R2.  

Join command completes with the error: Add-AdfsFarmNode : MSIS7711: PolicyOperationFault  

This error is followed every 5 minutes by events 344:  

```
There was an error doing synchronization. Synchronization of data from the primary federation server to a secondary federation server did not occur. 

Additional data 

Exception details: 
System.ServiceModel.Security.MessageSecurityException: The identity check failed for the outgoing message. The expected identity is 'identity(http://schemas.xmlsoap.org/ws/2005/05/identity/right/possessproperty: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/spn)' for the 'http://adfs02.contoso.com/adfs/services/policystoretransfer' target endpoint.
```

and events 345:  

```
There was a communication error during AD FS configuration database synchronization. Synchronization of data from the primary federation server to a secondary federation server did not occur. 

Additional Data 

Master Name : adfs02.contoso.com 
Endpoint Uri : http://adfs02.contoso.com/adfs/services/policystoretransfer 
Exception details: 
System.ServiceModel.Security.MessageSecurityException: The identity check failed for the outgoing message. The expected identity is 'identity(http://schemas.xmlsoap.org/ws/2005/05/identity/right/possessproperty: http://schemas.xmlsoap.org/ws/2005/05/identity/claims/spn)' for the 'http://adfs02.contoso.com/adfs/services/policystoretransfer' target endpoint.
```

Infra background:  

-  AD: Windows 2012R2  

-  Forest & Domain functional model: Windows Server 2008 R2, prepared for Windows Server 2016  

-  ADFS OS version is Windows 2012R2 (Hyper-v VMs)  

-  ADFS is being implemented for Office 365 SSO plus other apps publishing.  

-  ADFS Plan: 2 ADFS Servers in Corporate LAN & 2 WAP Servers in DMZ. Both servers to be load balanced using HLB.  

Troubleshooting done so far:  

-  Confirmed that both ws2012R2 nodes are syncing without any issue.  

-  Confirmed that test-adfsfarmjoin competed with success  

-  Confirmed that there is a dedicated domain user account with local admin permissions used while installing each server as ser service account.  

-  Confirmed that time & timezone are correct.  

-  Checked that the service account is correctly set with STS domain name.  

-  Checked that DNS names are correct  

-  Disabled Windows firewall.  

-  There is no other FW between ADFS nodes.  

I have run out of ideas what is missing.  

Kindly advise.  

Thank you.  

Regards, Pavel.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-05-09*

And are the IP address you see in the trace matching the actual IP addresses of the servers? Maybe there's an HTTP proxy at the system level and that's messing with the process? You can check this with: `netsh winhttp show proxy`.  

Also, regarding the SPNs, have you checked for duplicated SPNs? Maybe kerberos fails and we fall back to NTLM. In that case other factors such as NTLM hardening or membership to the Protected Users group can interfere.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-05-05*

Are there any other errors? Or maybe failed logons (event 4625) on either the 2019 server or the current primary AD FS server?  

Maybe a network trace might reveal other issues? The transfer is over the port 80. The data is encrypted, but not the SOAP envelop. So maybe the trace will tell us more?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-05-03*

Assuming there's no issues with SPN, I have seen issues when customers have disabled RC4_HMAC_MD5 as an ecnryption type on the new Windows Server 2019 AD FS node.    

To check if you're in this situation, you can check the following parameter on your new server: https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos    

Also, you can enable Kerberos logging on the new server:    

`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\Kerberos\Parameters`    

Registry Value: `LogLevel`    

Value Type: `REG_DWORD`    

Value Data: `0x1`    

This does not require a reboot. If the encryption type is the issue, you should see an error in the System eventlogs when you try to join the farm. Then you can opt to either re-enable RC4_HMAC_MD5 or to enable AES256 on the service account you are using on the farm (if so then let us know here, we'll drive you through the process).
