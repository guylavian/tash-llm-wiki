---
title: "Server 2019 GPO for domain to disable Win11 upgrade"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/712884/server-2019-gpo-for-domain-to-disable-win11-upgrad
question_id: 712884
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Server 2019 GPO for domain to disable Win11 upgrade

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/712884/server-2019-gpo-for-domain-to-disable-win11-upgrad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm running Server 2019 and do not see the option in GPO editor to push the option to stay on a specific version to the client machines.  

I checked User and Computer Configuration > Policies > Admin Templates > Windows Components > Windows Update (and WU for Business) and don't see the option that's referenced on so many sites.  How do I get it updated to enable an option to stop people from upgrading to Windows 11?  

It doesn't make sense to login to 30 machines to manually change the registry.  We have a domain with 3 DC's, 2 DFS servers, 2 RDP boxes, and multiple various other servers and workstations.  What would I need to change?    

Thank you for your help.

## Answer (community) — community member

*upvotes: 2 · updated: 2022-01-27*

I figured it out!  

So, edit the registry on your Windows 11 machine. Install the Windows RSAT tools for Group Policy Management. Launch regedit and create a new Key and then DWORD value: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Group Policy, EnableLocalStoreOverride = 1, reboot.  

Launch Group Policy Management, edit the Default Domain policy or the one you've created just for this. Navigate to Computer Configuration > Policies > Admin Templates > Windows Components > Windows Update > Manage updates offered from Windows Update. Double click "Select the target Feature Update version", set to enabled, put "Windows 10" in the first box and "21H2" in the second.  

Note, later in the year you might need to change from 21H2 to the newer Windows 10 release when those updates are being rolled out.

## Answer (community) — Q&A User [Mvp]

*upvotes: 1 · updated: 2022-02-04*

You don't need to do all of what Gabriel did. Simply load the Windows 11 GPO ADMX Templates into your central store and you'll have the options.  

See the bottom section titled appropriately on:  

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-3-windows-as-a-service-waas-and-group-policy-administrative-templates/

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-15*

Thank you for the described steps and screen shots above. But at first this still did not work for a DC in Windows Server 2019.  

I downloaded the admx for both Win10 and Win11 to Windows Server 2019  

I ran the MSI.   

It extracted/placed the files into C:\Program Files (x86)\Microsoft Group Policy\ under a folder with the policy name  

I copied those files and folders to a new folder in central store under \PolicyDefinitions-Win1021h1  

(and also to a new folder \PolicyDefinitions-Win11-21h1 for that set)  

I run gpupdate /force  

I open Group Policy Manager  

I edit the Default Domain Policy object.   

I browse down to Computer Configuration > Policies > Admin Templates > Windows Components > Windows Update >Windows Update for Business  

There was NO entry "Select the target feature update version" under that key.   

The admx files have to be copied into the existing "PolicyDefinitions" folder, over-writing whatever previous ones you have in there (back them up first!). And do it by selecting the files, and copy/paste. Do not over-write the entire folder (such as en-us) because you could be wiping out files you need - not every admx update contains all the same files. It may have 212, but your en-us folder might have 221. Those other 10 extra files you have may still be very important to you, so don't destroy them by just overwriting the folder itself. Same thing for the base folder of PolicyDefinitions - copy/paste the files. You likely have other ones in there you do not want to lose.. so don't rename/delete the PolicyDefinitions folder itself.   

Then run gpupdate and then open the GP editor and the setting should appear.   

But this approach by Microsoft is still stupid.  It should not be so broken, and should not require such extra manual processes. This should be delivered to servers as an automatic update that provides a one-click setting to push into GPO's to disable access for end users to run major version upgrades. Sys Admins need time to test, test, and test again before such major things can roll out. To just give it to all end users in corporate networks by default is outrageously dangerous.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-01-27*

Where are you looking?    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
