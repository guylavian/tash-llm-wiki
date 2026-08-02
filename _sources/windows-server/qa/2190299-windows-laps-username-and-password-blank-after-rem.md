---
title: "Windows Laps Username and password blank after removing and readding computer to domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190299/windows-laps-username-and-password-blank-after-rem
question_id: 2190299
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Windows Laps Username and password blank after removing and readding computer to domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190299/windows-laps-username-and-password-blank-after-rem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am currently testing Window  Laps to role out to the entire domain. I am currently testing with 6 devices. I created a group that has access to view and change the password through powershell and active directory users and computers on their local machines. Everything is working appeared to be working correctly during our testing until one test. I removed a device from the domain to test if it would be able to use the last password which worked as expected. I re added the device to the domain , ran gpupdate and this is where it gets weird. If the users try to view the password via PowerShell or ADUC on their local machine the Laps Local admin account and password are blank. However if you log into a domain control and go to the device you can see both of those. 

I have forced gpupdate on my own personal laptop and still not able to see the laps local admin account and password. This is concerning as only the Infrastructure administrators are able to access the Domain Controllers. The Technicians need to be able to access via there local machines.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-21*

Hello Michael_542,

Good day!  

If the users try to view the password via PowerShell or ADUC on their local machine the Laps Local admin account and password are blank. However if you log into a domain control and go to the device you can see both of those.  

A: Do you mean the same user signs in domain controller, hs/she can see the LAPS, but the same user signs in their own machine, he/she can not see the LAPS, am I right? If so, you can try to open PowerShell or ADUC as Administrator to see if it helps.

Does the same problem occurs on other machines? I mean if you remove another test machine from domain and readd it to domain, does the same problem occurs?  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-20*

-  yes the policy is being applied correctly to the device. 

-  My Understanding Windows Laps is now built into the devices and does not need an client. Microsoft Laps needed the Client. 

-  Users have the permissions to view the admin account and password as the other 5 test devices are working fine. Just not this one device that was removed from the Domain and readded.

-  No errors regarding this.

Once again the device Laps password can be seen if you are logged into the domain controller but just not from a tech Laptop. Just this one device is causing issues

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-20*

Hello Michael_542,

Thank you for posting in Microsoft Community forum.

Based on the information you have provided, you can check：

-  Check the Group Policy settings on the affected devices to ensure that the LAPS settings are being applied correctly. 

-  Verify that the LAPS client is installed and configured correctly on the affected devices. 

-  Ensure that the users have the necessary permissions to view the LAPS password on their local machines. 

-  Check the event logs on the affected devices for any errors or warnings related to LAPS.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
