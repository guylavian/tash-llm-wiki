---
title: "Windows Hello for Business with ADFS - Certificate - Hybrid Joined - Device Provisioning is failing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/591928/windows-hello-for-business-with-adfs-certificate-h
question_id: 591928
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 8
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# Windows Hello for Business with ADFS - Certificate - Hybrid Joined - Device Provisioning is failing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/591928/windows-hello-for-business-with-adfs-certificate-h (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

User Device Registration  

Event ID 360  

Windows Hello for Business provisioning will not be launched.   

Device is AAD joined ( AADJ or DJ++ ): Yes   

User has logged on with AAD credentials: Yes   

Windows Hello for Business policy is enabled: Yes   

Windows Hello for Business post-logon provisioning is enabled: Yes   

Local computer meets Windows hello for business hardware requirements: Yes   

User is not connected to the machine via Remote Desktop: Yes   

User certificate for on premise auth policy is enabled: Yes   

Machine is governed by enrollment authority policy.   

Cloud trust for on premise auth policy is enabled: No   

User account has Cloud TGT: Not Tested   

See https://go.microsoft.com/fwlink/?linkid=832647 for more details.  

Event ID 362  

Windows Hello for Business provisioning will not be launched.   

Device is AAD joined ( AADJ or DJ++ ): Yes   

User has logged on with AAD credentials: Yes   

Windows Hello for Business policy is enabled: Yes   

Windows Hello for Business post-logon provisioning is enabled: Yes   

Local computer meets Windows hello for business hardware requirements: Yes   

User is not connected to the machine via Remote Desktop: Yes   

User certificate for on premise auth policy is enabled: Yes   

Enterprise user logon certificate enrollment endpoint is ready: Yes   

Enterprise user logon certificate template is : Yes   

User has successfully authenticated to the enterprise STS: No   

Certificate enrollment method: enrollment authority   

See https://go.microsoft.com/fwlink/?linkid=832647 for more details.  

AAD Errors  

*Error: 0xCAA5001C Token broker operation failed.  

Operation name: GetTokenSilently, Error: -895418359 (0xcaa10009), Description: The value specified for 'clientId' must be non-empty.  

Logged at WebAccountProcessor.cpp, line: 652, method: AAD::Core::WebAccountProcessor::ReportOperationError.  

Enterprise STS Logon failure. Status: 0xC000006D Correlation ID: 12D0E4F1-7F17-4087-B7D4-026E58338C8E  

OAuth response error: invalid_grant  

Error description: MSIS9682: Received invalid OAuth JWT Bearer request. The certificate used to sign JWT Bearer request is not from a registered device with a Transport key.  

CorrelationID:   

Http request status: 400. Method: POST Endpoint Uri: https://fs.xxxx.xxx/adfs/oauth2/token/ Correlation ID: 12D0E4F1-7F17-4087-B7D4-026E58338C8E*  

dsregcmd  

+----------------------------------------------------------------------+  

| Device State                                                         |  

+----------------------------------------------------------------------+  

```
AzureAdJoined : YES
      EnterpriseJoined : NO
          DomainJoined : YES
            DomainName : xxxxx
           Device Name : MyPC.xxxx.com
```

+----------------------------------------------------------------------+  

| Device Details                                                       |  

+----------------------------------------------------------------------+  

```
DeviceAuthStatus : SUCCESS
```

+----------------------------------------------------------------------+  

| User State                                                           |  

+----------------------------------------------------------------------+  

```
NgcSet : NO
       WorkplaceJoined : NO
         WamDefaultSet : YES
   WamDefaultAuthority : organizations
          WamDefaultId : https://login.microsoft.com
        WamDefaultGUID : {B16898C6-A148-4967-9171-64D755DA8520} (AzureAd)
```

+----------------------------------------------------------------------+  

| SSO State                                                            |  

+----------------------------------------------------------------------+  

```
AzureAdPrt : YES
  AzureAdPrtUpdateTime : 2021-10-15 11:54:04.000 UTC
  AzureAdPrtExpiryTime : 2021-10-29 11:54:03.000 UTC
   AzureAdPrtAuthority : https://login.microsoftonline.com/baaf30d9-bdd3-4de1-815f-59e774096377
         EnterprisePrt : NO
EnterprisePrtAuthority : https://fs.xxxx.xxx:443/adfs
```

+----------------------------------------------------------------------+  

| Diagnostic Data                                                      |  

+----------------------------------------------------------------------+  

```
AadRecoveryEnabled : NO
Executing Account Name : ***\*******
           KeySignTest : PASSED
```

+----------------------------------------------------------------------+  

| Ngc Prerequisite Check                                               |  

+----------------------------------------------------------------------+  

```
IsDeviceJoined : YES
         IsUserAzureAD : YES
         PolicyEnabled : YES
      PostLogonEnabled : YES
        DeviceEligible : YES
    SessionIsNotRemote : YES
        CertEnrollment : enrollment authority
      AdfsRefreshToken : NO
         AdfsRaIsReady : YES
LogonCertTemplateReady : YES ( StateReady )
          PreReqResult : WillNotProvision
```

It have run through every article I can think of and I am stuck at this point.  

My device is writing back to AD and is in Azure AD.  I have re-registered, confirmed the 'ugs' entry in ADFS and so on.  I just don't know where to go from here.  I have run back and forth so many times I am starting to lose track of my changes.  Any help would be great.  

I have read that I may need an NDES Server to allow for SSO but I am not sure I need to go this route at the moment. I would like to get this working first.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-11-12*

I am experiencing the same with `dsregcmd /status`, can this be related and did you find a solution?

-  https://learn.microsoft.com/en-us/troubleshoot/windows-client/user-profiles-and-logon/event-1098-error-0xcaa5001c

```
+----------------------------------------------------------------------+
| SSO State                                                            |
+----------------------------------------------------------------------+
                AzureAdPrt : YES
      AzureAdPrtUpdateTime : [Date] UTC
      AzureAdPrtExpiryTime : [Date] UTC
       AzureAdPrtAuthority : https://login.microsoftonline.com/[TenantId]
             EnterprisePrt : NO
    EnterprisePrtAuthority :
     AcquirePrtDiagnostics : PRESENT
      Previous Prt Attempt : [Date] UTC
            Attempt Status : 0xc000006d
             User Identity : [UserPrincipalName]
           Credential Type : Password
            Correlation ID : [GUID]
              Endpoint URI : https://[ADFS-Server]/adfs/oauth2/token/
               HTTP Method : POST
                HTTP Error : 0x0
               HTTP status : 400
         Server Error Code : invalid_grant
  Server Error Description : MSIS9682: Received invalid OAuth JWT Bearer request. The certificate used to sign JWT Bearer request is not from a registered device with a Transport key.
                 OnPremTgt : NO
                  CloudTgt : YES
         KerbTopLevelNames : .windows.net,.windows.net:1433,.windows.net:3342,.azure.net,.azure.net:1433,.azure.net:3342
x
```
