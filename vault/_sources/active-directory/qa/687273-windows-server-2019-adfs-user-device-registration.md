---
title: "Windows Server 2019 - ADFS - User Device Registration - purely on premises"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/687273/windows-server-2019-adfs-user-device-registration
question_id: 687273
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Windows Server 2019 - ADFS - User Device Registration - purely on premises

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/687273/windows-server-2019-adfs-user-device-registration (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It's been quite a challenge getting Windows Hello for Business to work with Windows Server 2019, on premise only.    

I'm struggling very hard with device registration. I followed the guide here to set up an on premise only Windows Hello for Business environment: https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/hello-deployment-cert-trust    

Perhaps I'm totally wrong on how I'm approaching this, but I do assume I must trigger a device registration somehow?    

Yet device registration seems to malfunction. I get errors 304    

```
Automatic registration failed at join phase.   
Exit code: Unknown HResult Error code: 0xcaa1000e   
Server error:    
Tenant type: Federated   
Registration type: fed   
Debug Output:   
joinMode: Join  
drsInstance: ent  
registrationType: fed  
tenantType: Federated  
tenantId: 383a3889-5bc9-47a3-846c-2b70f0b7fe0e  
configLocation: undefined  
errorPhase: auth  
adalCorrelationId: {7C732D89-A151-4E7B-9406-8878EC8AE00B}  
adalLog:  
AdalLog:  HRESULT: 0xcaa1000e  
AdalLog:  HRESULT: 0x2ee6  
AdalLog:  HRESULT: 0x2ee6  
AdalLog:  HRESULT: 0x2ee6  
AdalLog:  HRESULT: 0x4aa90010  
AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuthEnterprise ; HRESULT: 0x0  
AdalLog: AggregatedTokenRequest::AcquireToken- returns false ; HRESULT: 0x0  
AdalLog: AggregatedTokenRequest::AcquireToken- refresh token is not available ; HRESULT: 0x0  
AdalLog: AggregatedTokenRequest::AcquireToken get refresh token info ; HRESULT: 0x0  
AdalLog: Authority validation is completed ; HRESULT: 0x0  
AdalLog: Authority validation is enabled ; HRESULT: 0x0  
AdalLog: Token is not available in the cache ; HRESULT: 0x0  
  
adalResponseCode: 0xcaa1000e
```

 and 305:    

```
Automatic registration failed at authentication phase. Unable to acquire access token.   
Exit code: Unknown HResult Error code: 0x801c0515   
Tenant Name: adfs.xxx.com (this is the actual internal ADFS name)  
Tenant Type: Federated   
Server error:   
AdalMessage: ADALUseWindowsAuthenticationNonHybrid failed,  unable to preform integrated auth  
AdalErrorCode: 0x2ee6  
AdalCorrelationId: {7C732D89-A151-4E7B-9406-8878EC8AE00B}  
AdalLog:  HRESULT: 0x2ee6  
AdalLog:  HRESULT: 0x2ee6  
AdalLog:  HRESULT: 0x2ee6  
AdalLog:  HRESULT: 0x4aa90010  
AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuthEnterprise ; HRESULT: 0x0  
AdalLog: AggregatedTokenRequest::AcquireToken- returns false ; HRESULT: 0x0  
AdalLog: AggregatedTokenRequest::AcquireToken- refresh token is not available ; HRESULT: 0x0  
AdalLog: AggregatedTokenRequest::AcquireToken get refresh token info ; HRESULT: 0x0  
AdalLog: Authority validation is completed ; HRESULT: 0x0  
AdalLog: Authority validation is enabled ; HRESULT: 0x0  
AdalLog: Token is not available in the cache ; HRESULT: 0x0
```

When I try dsregcmd, I see a reference to Microsoft Online - which is NOT what I want    

C:\Windows\system32>dsregcmd /join /debug    

dsregcmd::wmain logging initialized.    

dsregcmd::wmain logging initialized.    

DsrCmdAccountMgr::IsDomainControllerAvailable: DsGetDcName success { domain:xxx.com forest:xxx.com domainController:\jb-support-ad.xxx.com isDcAvailable:true }    

PreJoinChecks Complete.    

preCheckResult: Join    

isPrivateKeyFound: undefined    

isJoined: undefined    

isDcAvailable: YES    

isSystem: YES    

keyProvider: undefined    

keyContainer: undefined    

dsrInstance: undefined    

elapsedSeconds: 0    

resultCode: 0x0    

Automatic device join pre-check tasks completed.    

TenantInfo::Discover: Join Info { TenantType = Federated; AutoJoinEnabled = 1; TenandID = 383a3889-5bc9-47a3-846c-2b70f0b7fe0e; TenantName = adfs.xxx.com }    

GetComputerTokenForADRS: Get token for enterprise DRS    

GetComputerTokenForADRS: Token request authority: "https://login.microsoftonline.com/common"    

AdalLog: Token is not available in the cache ; HRESULT: 0x0    

AdalLog: Authority validation is enabled ; HRESULT: 0x0    

AdalLog: Authority validation is completed ; HRESULT: 0x0    

AdalLog: AggregatedTokenRequest::AcquireToken get refresh token info ; HRESULT: 0x0    

AdalLog: AggregatedTokenRequest::AcquireToken- refresh token is not available ; HRESULT: 0x0    

AdalLog: AggregatedTokenRequest::AcquireToken- returns false ; HRESULT: 0x0    

AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuthEnterprise ; HRESULT: 0x0    

AdalLog:  HRESULT: 0x4aa90010    

AdalLog:  HRESULT: 0x2ee6    

AdalLog:  HRESULT: 0x2ee6    

AdalLog:  HRESULT: 0x2ee6    

LogFatalAuthError: AdalMessage: ADALUseWindowsAuthenticationNonHybrid failed,  unable to preform integrated auth    

AdalErrorCode: 0x2ee6    

AdalCorrelationId: {7C732D89-A151-4E7B-9406-8878EC8AE00B}    

AdalLog:  HRESULT: 0x2ee6    

AdalLog:  HRESULT: 0x2ee6    

AdalLog:  HRESULT: 0x2ee6    

AdalLog:  HRESULT: 0x4aa90010    

AdalLog: AggregatedTokenRequest::UseWindowsIntegratedAuthEnterprise ; HRESULT: 0x0    

AdalLog: AggregatedTokenRequest::AcquireToken- returns false ; HRESULT: 0x0    

AdalLog: AggregatedTokenRequest::AcquireToken- refresh token is not available ; HRESULT: 0x0    

AdalLog: AggregatedTokenRequest::AcquireToken get refresh token info ; HRESULT: 0x0    

AdalLog: Authority validation is completed ; HRESULT: 0x0    

AdalLog: Authority validation is enabled ; HRESULT: 0x0    

AdalLog: Token is not available in the cache ; HRESULT: 0x0    

AdalLog:  HRESULT: 0xcaa1000e    

AutoEnrollAsComputer: Unable to retrieve access token. GetComputerTokenForADRS failed with error 0x801c0515.    

DsrCmdJoinHelper::Join: Federated enterprise DRS join failed with error 0xcaa1000e.    

DSREGCMD_END_STATUS    

             AzureAdJoined : NO  

          EnterpriseJoined : NO  

DeleteFileW returned 0x00000001.    

C:\Windows\system32>    

Any clue what could be wrong, or is there somewhere a decent and not self contradicting guide (for instance, the documentation mentions a local or third party/external MFA adapter is required; but on another page it suddenly claims a  certificate could also be accepted as a form of MFA)?    

Update: resolved, I went through the process of recreating enterpriseregistration.mydomain.org

## Answer (community) — community member

*upvotes: 1 · updated: 2022-01-12*

I went through the process of recreating enterpriseregistration.mydomain.org (CNAME record), which seems to have resolved this issue.

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-01-11*

You should locate the DRS service through the SCP in the configuration partition. Do you know what's in there for you?  

Alternatively, you can create the regitry value `EnterpriseDrsName` (REG-SZ) under `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CDJ` to make the machine point to your AD FS DRS directly.   

Regarding the MFA requirement, yes you can use a certificate, but is that really MFA then? Well it depends how you got your certificate in the first place. If all users get the certificate using auto-enrollement after logging in with their password, then the certificate, although working, is not the way to go.
