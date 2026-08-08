---
title: "Unable logon to Domain Controller after reboot"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/106459/unable-logon-to-domain-controller-after-reboot
question_id: 106459
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable logon to Domain Controller after reboot

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/106459/unable-logon-to-domain-controller-after-reboot (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, in a large AD environment we have same issues reported on the page below:    

https://social.technet.microsoft.com/Forums/en-US/912d062b-3168-4782-a128-604223fd0636/unable-to-log-into-domain-controller-after-reboot?forum=ws2016    

Often when I reboot domain controller on branch office I'm not be able to logon, with the same issue:     

System is restarted using the restart option in Windows.  Server appears to start normally.  Press CTRL-ALT-DEL to get a login prompt.  User is administrator (or any other domain admin account), enter password and hit enter or click the arrow.  The cursor is moved back to the beginning of the password field and the previously entered password remains.    

This issue seems start happens after we raise the domain functionality level from 2003 to 2008 R2. Note: PDC is still on 2008 R2    

After that no way to logon on DC's, only after many and many reboot server accepts credentials. Same issue if I try to isolate domain controller from network.    

New domain controllers are also affects by this problem, immediatly after promotion still not be able to connect    

Same errors in the event viewer reported on the thread.    

We are working around this issue from many days, time is correct on every DC's.    

Thanks in advance for the help to resolve this issue.    

Enrico Z.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-23*

Hi Enrico,  

did you find a solution?  

I have a similar problem with DC with OS 2016.  

I think, something is wrong with our previous domain controllers (2008 or 2003).

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-25*

Hello @Anonymous  ,

Thank you for reply

1.Based on "Often when I reboot domain controller on branch office I'm not be able to logon, with the same issue", do you mean when reboot any one DC in the forest, this DC will have such issue? No, all 2012 R2 DC's are affects. 2008 R2 seems ok.

2.Or only reboot this specific DC, this DC will have such issue? No, all DC's 2012 R2 have this issue

3.Based on "New domain controllers are also affects by this problem, immediatly after promotion still not be able to connect", do you mean the issue is replicated between all the DCs in the forest? ****Yes.** For testing purpose we promoted a fresh new 2012 R2 server to DC, after first reboot logon is "hang", instead a fresh new DC 2008 R2 works without any issue **

We notice that AD replicate correctly on all DC's, also when DC's are in this strange "stall mode".  

Keep in mind that this issue is observed immediatly time after we demote all 2003 DC's and raise forest/domain functional level to 2008 R2  

The condition in which the domain controllers are after the reboot is strange, some services do not start (for example MSDTC) if you type the password, at logon screen, and press enter it does not work, even if you press the arrow next to the password field it does not work.  

If you reboot the DC 10-20 or 30 times it may be that the services start and accept the credentials. the only condition in which you can logon is safe mode. When the DC starts correctly and you restart "Active Directory Domain Services" the services do not restart, you have to restart the DC and start again.  

When the DC is in "stalled mode" you can remotely manage the event viewer but not the services or the registry

Check if AD environment is healthy. Check whether all DCs in this domain is working fine by running Dcdiag /v on each DC. We checking log as suggest by @Fabian  . file is attached28290-dcdiag-full.txt

Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum on each DC. Replication works fine

Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC. Up and running on all DC's

Check we can update gpupdate /force on each DC successfully. Update is successfully

Regards.

Enrico

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-25*

Hello @Enrico Zocca  ,

Thank you for posting here.

1.Based on "Often when I reboot domain controller on branch office I'm not be able to logon, with the same issue", do you mean when reboot any one DC in the forest, this DC will have such issue?

2.Or only reboot this specific DC, this DC will have such issue?

3.Based on "New domain controllers are also affects by this problem, immediatly after promotion still not be able to connect", do you mean the issue is replicated between all the DCs in the forest?

Meanwhile, check the information below:

-   Check if AD environment is healthy. Check whether all DCs in this domain is working fine by running Dcdiag /v on each DC.

-   Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum on each DC.

-   Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC.

-   Check we can update gpupdate /force on each DC successfully.

Best Regards,  

Daisy Zhou

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-25*

Hello @Enrico Zocca  ,

Thank you for posting here.

1.Based on "Often when I reboot domain controller on branch office I'm not be able to logon, with the same issue", do you mean when reboot any one DC in the forest, this DC will have such issue?

2.Or only reboot this specific DC, this DC will have such issue?

3.Based on "New domain controllers are also affects by this problem, immediatly after promotion still not be able to connect", do you mean the issue is replicated between all the DCs in the forest?

Meanwhile, check the information below:

-   Check if AD environment is healthy. Check whether all DCs in this domain is working fine by running Dcdiag /v on each DC.

-   Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum on each DC.

-   Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC.

-   Check we can update gpupdate /force on each DC successfully.

Best Regards,  

Daisy Zhou

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-25*

Hello @Enrico Zocca  ,

Thank you for posting here.

1.Based on "Often when I reboot domain controller on branch office I'm not be able to logon, with the same issue", do you mean when reboot any one DC in the forest, this DC will have such issue?

2.Or only reboot this specific DC, this DC will have such issue?

3.Based on "New domain controllers are also affects by this problem, immediatly after promotion still not be able to connect", do you mean the issue is replicated between all the DCs in the forest?

Meanwhile, check the information below:

-   Check if AD environment is healthy. Check whether all DCs in this domain is working fine by running Dcdiag /v on each DC.

-   Check if AD replication works properly by running repadmin /showrepl and repadmin /replsum on each DC.

-   Check both SYSVOL folder and Netlogon folder are shared by running net share on each DC.

-   Check we can update gpupdate /force on each DC successfully.

Best Regards,  

Daisy Zhou
