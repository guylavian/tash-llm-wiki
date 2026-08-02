---
title: "Having an issue starting ADFS 4 service not running...HELP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1288462/having-an-issue-starting-adfs-4-service-not-runnin
question_id: 1288462
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Having an issue starting ADFS 4 service not running...HELP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1288462/having-an-issue-starting-adfs-4-service-not-runnin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

```
I'm just trying to go on a brainstorm if we're missing something on troubleshooting the ADFS 4 issue or any similar experience that HQ faced and how it was solved.

Affected - Users that are trying to authenticate to ADFS server via Office 365 services and or users that renews their passwords.

ADFS Issues
ADFS Management - Triggers error Admin0017 when it trying to connect to WID but cannot because, It can't start the service.
Services - Triggers an error 1064 when you try to restart the service, account uses GMSA.
WID and WID VSS Writer - Are running and can be restarted without an error.
Event logs - Triggers a constant Event ID 102 and 381 with 381 pointing to a thumbprint "049FFDsdxxxxxxxxxxx1" that is non-existent.

Steps taken. 
1. Check, Update and verified thumbprint chains and remove old ones and remove and re-added again 
2. Check GMSA permission, right not its full perm.
3. Check, Verified and Re added SPN to reference to adfs domain 
4. Check the Microsoft.IdentityServer.Servicehost.exe.config and edited line to AdfsConfigurationV4;Integrated Security=False" - no change either and still throws back the 1064 and Admin0017 (reverted to original config already) 
5. Followed Microsoft suggestions and other forums suggestion

To no avail were still looping on the same issue that we cant start ADFS service. You're input are very much appreciated, Thank you!
```

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2023-05-20*

Hello @Stephen Almarez !

maybe you already followed this but let me suggest a re try with careful attention on each step

https://blog.rmilne.ca/2016/12/06/change-ad-fs-2012-r2-service-account-password/

-  Stop AD FS service on all AD FS servers in the farm

-  Change the AD password for the service account

-  Ensure AD has replicated ( In fact wait 5-15 minutes)

-  Change the AD FS service password on each AD FS server

-  Start AD FS service on each server in the AD FS farm

-  Test

Stop AD FS Service On All AD FS Servers in The Farm

Stop the AD FS service on all AD FS servers.   Use which means you prefer to do this, this could be either the services applet or PowerShell.  In the below example PowerShell is used locally on the server.

Change the AD Password For the Service Account

Follow your documented process to change the assigned password for the AD FS service account.  This should be then stored so that it is in compliance with your internal security policies and practices.

Ensure AD Has Replicated

It is possible that your AD FS farm is deployed in multiple datacentres to provide site resilience.  This may mean that there are additional considerations for AD replication latency to the additional sites.  Ensure that AD has successfully replicated the changed service account password so that the updated password is available to all AD FS servers in the farm.

One potential method is the Active Directory Replication Status Tool.

Change the AD FS Service Password on Each AD FS Server

Now that AD has replicated to all of the locations which contain AD FS servers, we can update the password stored on each AD FS server.

In the example below we are using the services.msc applet, though there are many other ways to do this.  Choose your weapon!

After opening the properties for the AD FS service, select the Log On tab.  Enter the new password, confirm it and then click apply to save the change.

Start AD FS Service on Each Server in the Farm

All AD FS servers have had their service account updated, and we can now start the services on the servers.  In PowerShell we could use:

Start-Service adfssrv

Ensure that the service starts, and no issues are reported in the event logs.

Also ensure that Web Application Proxy (WAP) servers are running without issues, and their event logs are also clean.

 I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-30*

Dear All, sorry for the late reply, we ended up reinstalling the ADFS role, overwritten the WID, then resync WAP and AADC. and thank you for your input and suggestions, its valuable.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-05-20*

Thank you for the quick replies, on numbers.

-  Time synchronization: Check if the time is correctly synchronized across all your servers. Kerberos authentication, which is used by ADFS, can fail if the time is not correctly synchronized. - We have checked this already and seems are clocks are syn.     2. & 3.   GMSA: Verify the GMSA password hasn't expired. This can sometimes cause problems with service start-up.

```
- We did change the the password on the service account and then tried starting the service but not successful
```

-  We have remove expired and reregistered the valid certificates, 

-  make sure that the ADFS service has read access to the private key of the service communications certificate. (SOS) - not sure on this one but from certutil, managed key, we can sevice account has read access and we even modified to full.

-  We haven't done this since the ADFS is a stand-alone service and not sure where to point to anew WID or is there a  way to reset WID?

Are you using AD Connect? - Yep were using

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/adfs-2-service-fails-to-start - did all this except for the SQL step since we don't use it.

Once again, thank you.

Best Regards,

Stephen

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-05-20*

Hello @Stephen Almarez  !

Welcome to Microsoft QnA!

I understand you are under an emergency situation with ADFS troubleshooting

Since you have been through many links , i can only suggest the following

The errors are pointing to Certificate issues 

1.       Time synchronization: Check if the time is correctly synchronized across all your servers. Kerberos authentication, which is used by ADFS, can fail if the time is not correctly synchronized.

2.       GMSA: Verify the GMSA password hasn't expired. This can sometimes cause problems with service start-up.

3.       Verify that the ADFS service account (if it's not using the GMSA) has the necessary permissions on the ADFS databases.

4.       Encryption Certificate: An ADFS service can refuse to start if the encryption certificate is not valid. Double check your certificates, and make sure that the ADFS service has read access to the private key of the service communications certificate. (SOS)

5.       Corrupted WID Database: There could be a possibility of a corrupted WID database. If possible, test this by pointing ADFS to a different WID database and see if that resolves the issue.

Did this happened after some changes ? I suspect an expired Certificate OR corrupt Database

Are you using AD Connect ? 

I suppose you have seen this already , buy i anyway i add also :

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/adfs-2-service-fails-to-start

Post you feedback on these suggestions and we are here to help !

I hope this helps!

Kindly mark the answer as Accepted and Upvote in case it helped!

Regards
