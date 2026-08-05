---
title: "GPOs Not Applied / AD Group Issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/120736/gpos-not-applied-ad-group-issue
question_id: 120736
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPOs Not Applied / AD Group Issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/120736/gpos-not-applied-ad-group-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Multiple computers (W10 Pro/Ent, WS2019, WS2012) had issues applying several GPOs that had been working correctly for months.  The error was Filtering:  Not Applied (Unknown Reason).    

The GPOs fixed themselves automatically (reapplied) on subsequent background gpupdates without any changes made to AD or GP.    

The only GPOs affected have custom security group added to the Security Filtering section of the GPO (see image below).    

Other GPOs with default Authenticated Users OR GPOs with only explicitly defined computers (without Authenticated Users) in Security Filtering were unaffected.    

Example of GPO with issue:    

    

What I observed on an affected computer:    

    

Issues occurred on the day where the following two changes occurred:    

-  Both DCs (WS2019, we only have 2) updated with KB4570333 and rebooted.  Ample time allowed in between reboots for syncing.    

-  Security groups changed scopes from Domain Local to Universal to Global    

Issues appeared on computers within the next several background gpupdates across our domain on multiple devices between 1 to 12 hours later (sometimes with multiple background gpupdates before GPOs were unapplied).  Missing GPOs were pulled from both domain controllers.    

No replication or obvious errors in DC event logs from that day.  GPOs and group membership for security groups wasn't changed.  GPOs stopped applying/reapplied automatically on computers without any reboots.    

It's almost as if the computers could not see themselves as members of the security groups anymore during a background gpupdate, for some unknown reason.  And then they suddenly saw themselves as members again, for some unknown reason, and reapplied the GPOs.    

Can anyone provide any insight into this behavior?  Can anyone confirm that this should NOT be happening?  Would the group scope changes cause this, and if so, is there any documentation to support this?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-14*

Hello @Anonymous  ,    

Thank you so much for your time and support.    

I did the test in my lab. I configured a GPO with security Filtering. Deleted the Authenticated User group and added my security group with computer accounts. At first, it is domain local group and the GPO is applied without any problems. Then I changed the group scope to universal and the GPO is still applied without any problems. Then continue to change the group scope to Global and the GPO could also be applied successfully. So from my test, there is no need to restart the machines to take effect after changing the group scope.     

Besides, I also tried to restart the machine, and the GPO is still be applied without any problems. So it is hard to say what changes caused this issue. As mentioned before, since the GPO is not applied now, we could enable GPSVC debug logging to further troubleshoot. We could run the following command to refresh the group policy and reproduce the issue:    

gpupdate /force    

Hope the information is helpful. For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

@Anonymous   thanks for the reply.  A few notes:    

-  The computers stopped applying the GPOs without a reboot.  This means that the computers did not refresh their kerberos tickets and thus didn't recalculate which GPOs they should apply.  Additionally, there were no membership changes (only scope changes).  That's what makes this problem so bizarre.    

-  I don't believe that removing the Authenticated Users group will cause any problems if another custom security group is used correctly.  At least, MS claims that there shouldn't be issues (see Strategy 3): https://techcommunity.microsoft.com/t5/core-infrastructure-and-security/who-broke-my-user-gpos/ba-p/258781    

I'm open to any documentation from MS that explicitly states that the method I've used for Security Filtering (with Authenticated Users removed) will cause issues.    

Thank you for the instructions on enabling this, which, if I could reproduce it, would be very helpful.  Unfortunately, I haven't been able to reproduce the issue where GPOs stop applying.  If I'm able to reproduce it, I'll definitely update this post.    

To me, this looks like either some strange bug due to one or both of the known changes made or possibly another unknown change that happened.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-12*

Hi @Anonymous  ,

You are welcome. Thank you so much for your kindly reply.

Since there is no change to the GPOs themselves, only the security group scopes changed, we need to restart the computers to refresh the membership change. Then check whether the GPOs could be applied or not.

Besides, we noticed that we deleted the Authenticated User and added the Firewall Servers group in the Security Filtering. If possible, we could try to add the Authenticated User back and only give it Read permission. As we know, to delete the Authenticated User might cause some problems.

It is suggested that we could enable GPSVC debug logging to further troubleshoot. 

1.On problematic machine, create the “usermode” folder under “**%windir%\debug**” directory. 

2.Create the following registry keys:   

   

Under HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion    

Create a new Key “Diagnostics” there;   

   

3.Then create a new value “GPSvcDebugLevel” under the key “Diagnostics”:   

   

Entry: GPSvcDebugLevel   

Type: REG_DWORD   

Value data: 30002 (Hexadecimal)   

   

At this point, use the GPSVC analysis blog to get further:  

https://learn.microsoft.com/en-us/archive/blogs/askds/a-treatise-on-group-policy-troubleshootingnow-with-gpsvc-log-analysis

Please note: Due to forum rules and security considerations, we do not analyze logs here. 

For any question, please feel free to contact us.

Best regards,  

Hannah Xiong

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-09*

Hi @Anonymous   Thank you for the reply.    

-  GPOs contain computer settings only    

-  GPOs are linked to the correct OUs that contain the target computers  (and these computers are also in the custom security group).  So for example, in my image, the Windows Servers OU contains a target server which is also a member of the Firewall Servers group.    

-  Only computers are in the custom security group.  No users present.  Group membership hasn't been edited in months.    

-  Correct, the error I linked in the post is from gpresult.  There were few other "errors" I could find in any event log.  I did observe the GPOs stop being applied in the event log, and then being reapplied.  This shouldn't happen, but this behavior didn't necessarily trigger additional error messages.    

-  I have verified the Read and Apply permissions on the GPOs.  I even went into SYSVOL and checked the permissions on the directories for the GPOs in question.  I also checked the SYSVOL permissions at the time of the issue (DC backups).  No permission issues on the GPOs themselves.    

These GPOs have been working for months, so we know that the GPOs/OUs/Security Filtering is all configured correctly.  The GPOs themselves were not changed, only the security group's scopes.    

It seems as if changing these scopes from Domain Local > Universal > Global caused some sort of bug that rippled through AD and caused the GPOs to become filtered out.  That's my best guess, at least.    

@Anonymous   I understand we may never understand a root cause of the behavior we experienced.  Can you confirm that this behavior is unexpected/not supposed to have happened with the changes I described?    

Thank you kindly!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-09*

Hello,    

Thank you so much for posting here.    

To further narrow down the issue, we would like to get more detailed information. Would you please help to collect the following information:     

1: The not applied GPOs are under Computer Configuration, right?     

2: If these GPOs are under Computer Configuration, are they linked to the OU with computer objects?    

For Security Filtering, this Group Policy now applies to only users or computers that are a member of the security group. However you still need to remember that the user and/or computer should be part of the site/domain/OU to which this Group Policy Object is linked.    

3: The not applied GPOs have custom security group added to the Security Filtering. Are users or computers added to this custom security group?    

4: Where did we see error message? From gpresult?     

5: We could have a check whether this security group has the Read and Apply Group Policy permission. Since we changed the security group scope, we could check whether the Read and Apply permission still exists.    

For any question, please feel free to contact us.     

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
