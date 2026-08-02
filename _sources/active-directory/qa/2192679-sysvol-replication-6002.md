---
title: "sysvol replication 6002"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192679/sysvol-replication-6002
question_id: 2192679
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# sysvol replication 6002

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192679/sysvol-replication-6002 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

sysvol replication 6002

Greetings - 

Ran into a bit of an issue while doing some overzealous troubleshooting of DFS. I have somehow deleted the Domain System Volume replication in DFS Management.

I am now encountering the follow error message in Event Viewer:

Error   DFSR    6002    None

The DFS Replication service detected invalid msDFSR-Subscriber object data while polling for configuration information.  

Additional Information:  

Object DN: CN=Domain System Volume,CN=DFSR-LocalSettings,CN=XXXXXXX,OU=Domain Controllers,DC=XXXXXXX,DC=local  

Attribute Name: msDFSR-MemberReference  

Domain Controller: XXXXXX.local  

Polling Cycle: 60 minutes

The sysvol appears to be still intact;

C:\Users\administrator.xxxxxxx>DCDIAG /Test:sysvolcheck  

Directory Server Diagnosis  

Performing initial setup:  

   Trying to find home server...  

   Home Server = xxxxxxx  

   * Identified AD Forest.  

   Done gathering initial info.  

Doing initial required tests  

   Testing server: xxxxxxx\xxxxxxx  

      Starting test: Connectivity  

         ......................... xxxxxxx passed test Connectivity  

Doing primary tests  

   Testing server: xxxxxxx\xxxxxxx  

      Starting test: SysVolCheck  

         ......................... xxxxxxx passed test SysVolCheck  

   Running partition tests on : ForestDnsZones  

   Running partition tests on : DomainDnsZones  

   Running partition tests on : Schema  

   Running partition tests on : Configuration  

   Running partition tests on : xxxxxxx  

   Running enterprise tests on : xxxxxxx.local

I have followed the steps located on these sites without success.

https://community.spiceworks.com/topic/2463191-error-6002-dfsr#:~:text=The%20DFS%20Replication%20service%20detected,while%20polling%20for%20configuration%20information.

https://www.experts-exchange.com/questions/29164999/Missing-Expected-Value-SYSVOL-Sync-fail.html

https://www.experts-exchange.com/dashboard/#/questions/29164999

Here are the results of  DCDIAG /c /v /e /q

C:\Users\administrator.xxxxxx>DCDIAG /c /v /e /q  

         [xxxxxx] No security related replication errors were found on this DC!  To target the connection to a  

         specific source DC use /ReplSource:<DC>.  

         There are warning or error events within the last 24 hours after the SYSVOL has been shared.  Failing SYSVOL  

         replication problems may cause Group Policy problems.  

         ......................... xxxxxxx failed test DFSREvent  

         ** Did not run Outbound Secure Channels test because /testdomain: was not entered  

         The following problems were found while verifying various important DN references.  Note, that  these problems  

         can be reported because of latency in replication.  So follow up to resolve the following problems, only if  

         the same problem is reported on all DCs for a given domain or if  the problem persists after replication has  

         had reasonable time to replicate changes.  

            [1] Problem: Missing Expected Value  

             Base Object: CN=xxxxxxx,OU=Domain Controllers,DC=xxxxxxx,DC=local  

             Base Object Description: "DC Account Object"  

             Value Object Attribute Name: msDFSR-ComputerReferenceBL  

             Value Object Description: "SYSVOL FRS Member Object"  

             Recommended Action: See Knowledge Base Article: Q312862  

            LDAP Error 0x5e (94) - No result present in message.  

         ......................... xxxxxxx failed test VerifyEnterpriseReferences  

         Some objects relating to the DC xxxxxxx have problems:  

            [1] Problem: Missing Expected Value  

             Base Object:  

            CN=NTDS Settings,CN=xxxxxxx,CN=xxxxxxx,CN=xxxxxxx,CN=Sites,CN=Configuration,DC=xxxxxxx,DC=local  

             Base Object Description: "DSA Object"  

             Value Object Attribute Name: serverReferenceBL  

             Value Object Description: "SYSVOL FRS Member Object"  

             Recommended Action: See Knowledge Base Article: Q312862  

            [1] Problem: Missing Expected Value  

             Base Object: CN=xxxxxxx,OU=Domain Controllers,DC=xxxxxxx,DC=local  

             Base Object Description: "DC Account Object"  

             Value Object Attribute Name: msDFSR-ComputerReferenceBL  

             Value Object Description: "SYSVOL FRS Member Object"  

             Recommended Action: See Knowledge Base Article: Q312862  

         ......................... xxxxxxx failed test VerifyReferences

The referenced KB Q312862 did not get me very far.

I have also tried to restore the sysvol from ldp.exe
Expanding base 'CN=Domain System Volume\0ADEL:5a33d907-f6c9-4006-8b1d-03d40ed79f23,CN=Deleted Objects,DC=XXXXXXX,DC=local'...

Getting 1 entries:

Dn: CN=Domain System Volume\0ADEL:5a33d907-f6c9-4006-8b1d-03d40ed79f23,CN=Deleted Objects,DC=XXXXXXX,DC=local

cn: Domain System Volume

DEL:5a33d907-f6c9-4006-8b1d-03d40ed79f23; 

distinguishedName: CN=Domain System Volume\0ADEL:5a33d907-f6c9-4006-8b1d-03d40ed79f23,CN=Deleted Objects,DC=XXXXXXX,DC=local; 

instanceType: 0x4 = ( WRITE ); 

isDeleted: TRUE; 

isRecycled: TRUE; 

lastKnownParent: CN=DFSR-LocalSettings,CN=SERVER1,OU=Domain Controllers,DC=XXXXXXX,DC=local; 

name: Domain System Volume

DEL:5a33d907-f6c9-4006-8b1d-03d40ed79f23; 

objectClass (2): top; msDFSR-Subscriber; 

objectGUID: 5a33d907-f6c9-4006-8b1d-03d40ed79f23; 

uSNChanged: 148340; 

uSNCreated: 16398; 

whenChanged: 11/14/2023 11:35:15 AM Eastern Standard Time; 

whenCreated: 9/5/2023 4:00:39 PM Eastern Standard Time;

However from what I've dug up on other forums  - the isRecycled: TRUE attribute might be the nail in the coffin.

***Call Modify... 

ldap_modify_ext_s(ld, 'CN=Domain System Volume\0ADEL:5a33d907-f6c9-4006-8b1d-03d40ed79f23,CN=Deleted Objects,DC=xxxxxxx,DC=local',[2] attrs, SvrCtrls, ClntCtrls); 

Error: Modify: Object Class Violation. <65> 

Server error: 0000207C: UpdErr: DSID-03151CEB, problem 6002 (OBJ_CLASS_VIOLATION), data 0 

Error 0x207C A required attribute is missing.

I have a feeling that, short of demoting and promoting the server, I'm up the creek. Did I happen to mention that it is the only DC in the domain, which consists of just that DC and no other servers.

Any thoughts/input would be greatly appreciated. Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-28*

Hello Matt B_5446,  

Thank you for your reply.

In the Modify window, try to do these steps and check:

– On text box Edit Entry Attribute: type isDeleted then select the Delete radio button from Operation then click Enter the isDeleted attribute will appear on Entry List box.

– On the text box Edit Entry Attribute: type distinguishedName

– On the text box Values: type CN=123,CN=RRAS,CN=Services,CN=Configuration,DC=a,DC=local (example) continue select Replace radio button under Operation then click Enter

– Check Extended check box on left bottom corner then click Run.  

  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-27*

Greetings,

Yes I am able to see CN=Deleted Objects,DC=XX,DC=XX.

When I attempt to modify the need object(s) by deleting the isDeleted attribute and changing the  distinguishedName to reflect its last known path - CN=Domain System Volume,CN=DFSR-GlobalSettings,CN=System,DC=XXXXXXX,DC=local - I receive this error message

***Call Modify...

ldap_modify_ext_s(ld, 'CN=Domain System Volume\0ADEL:3a427844-d513-40ab-95ce-02cb8626a344,CN=Deleted Objects,DC=SparkleBuggy,DC=local',[2] attrs, SvrCtrls, ClntCtrls);

Error: Modify: Object Class Violation. <65>

Server error: 0000207C: UpdErr: DSID-03151CEB, problem 6002 (OBJ_CLASS_VIOLATION), data 0

Error 0x207C A required attribute is missing.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-27*

Hello Matt B_5446,  

Thank you for your reply.  

Can you see CN=Deleted Objects via LDP.exe?  

Check as below:  

1.Logon as Administrative privileges (Domain Admin) Windows AD DC. 

2.On Windows Start Button type Run type ldp.exe. 

3.On Ldp click Connection menu select Connect… 

4.In the Connect box type your full AD server name then click OK.  

5.Again, click the Connection menu and select Bind. Select Bind as currently logged on user (that have administrative priledge) then click OK.  

6.Click Options menu then select Controls. From the Load Predefined list select Return deleted objects then click OK.  

7.Click the View menu and select Tree view. Select BaseDN: DC=XX,DC=XX then click OK.   

8.CAn you see CN=Deleted Objects,DC=XX,DC=XX?  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-24*

Hello Matt B_5446,  

Thank you for posting in Microsoft Community forum.  

As I understand, you have only one Domain Controller in the domain.  

Please check if you can see the CN=SYSVOL Subscription below on the DC (domain partition)?  

  

And check if you can see the two attribute below on the DC (Schema partition)?

![Image](https://learn-attachment.microsoft.com/api/attachments/f5a4e021-69e6-4f6c-a0aa-1a1821b14c84?platform=QnA"https://learn-attachment.microsoft.com/api/attachments/b9ba5579-0f80-4b7d-992c-d6949102cb65?platform=QnA" title="filestore.community.support.microsoft.com" rel="ugc nofollow">  

Method two:  

Have you had a recent DC full backup or system state backup? If so, you can restore this DC.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

Greetings Daisy - Thank you for your reply.

I am not seeing the CN=SYSVOL Subscription on the DC, in fact, it appears that CN=Domain System Volume is not present either.

The CN=ms-DFSR-ComputerReference and CN=ms-DFSR-ComputerReferenceBL are available.

It appears that the recycling bin was not enabled on this DC

And if I have read correctly, it I enable it now, anything that was deleted is no longer recoverable?

Alas, There are no recent DC full backup or system state backups.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-23*

Hello Matt B_5446,  

Thank you for posting in Microsoft Community forum.  

As I understand, you have only one Domain Controller in the domain.  

Please check if you can see the CN=SYSVOL Subscription below on the DC (domain partition)?  

  

And check if you can see the two attribute below on the DC (Schema partition)?

  

If no, you can try to restore the object you deleted via two methods:  

Method one:  

Please check if you have enabled Recycle Bin before， open ADAC (Active Directory Administrative Center) and check if "Enable Recycle Bin" is grey out, if it is grey out, this means it is enabled. You can restore the deleted objects from recycle bin.   

  

Method two:  

Have you had a recent DC full backup or system state backup? If so, you can restore this DC.  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
