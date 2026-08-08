---
title: "Drive Mapping GPO causing slow profile load on citrix VDI machines"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/449939/drive-mapping-gpo-causing-slow-profile-load-on-cit
question_id: 449939
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Drive Mapping GPO causing slow profile load on citrix VDI machines

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/449939/drive-mapping-gpo-causing-slow-profile-load-on-cit (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,  

Please help we are having some issue related to GPO slowness. As per finding one of the drive mapping causing the slow profile loading issue on citrix VDI machines & same GPO is working fine with laptop/desktop user.Once we will deny drive mapping GPO of few user everything works as expected .But we do not have root cause why this is happing only for citrix VDI machine  

Drive mapping policy is coming from parent OU & its user base policy & we have apply one Loopback policy for citrix VDI  

Can anyone advise how to find exact slowness cause of drive mapping policy   

regards

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-26*

Hi, I have recently been facing a similar issue.    

It is possible to audit the culprit GPO using Director (providing you have Windows VDA version 1903 or late installed) :    

Search for the user and click on the left "details" button, you should get a breakdown of the last logon duration.    

    

if you hover over the GPOs section you can select a detailed drilldown of said GPOs :    

    

You should find your culprit.     

In my case the problem was on the driver side of the print spooler. I reinstalled PCL6 latest drivers and that resolved the slow logons.    

Hope it helps !

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-05*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-02*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-29*

Overview of Group Policy Client Service (GPSVC)  

One of the major changes that came with Windows Vista and later operating systems is the new Group Policy Client service. Earlier operating systems used the WinLogon service to apply Group Policy. However, the new Group Policy Client service improves the overall stability of the Group Policy infrastructure and the operating system by isolating it from the WinLogon process.  

The service is responsible for applying settings configured by administrators to computers and users through the Group Policy component. If the service is stopped or disabled, the settings will not be applied, so applications and components will not be manageable through Group Policy. Please keep in mind that, to increased security, users cannot start or stop the Group Policy Client service. In the Services snap-in, the options to start, stop, pause, and resume the Group Policy client are unavailable.  

Finally, any components or applications that depend on the Group Policy component will not be functional if the service is stopped or disabled.  

reference：https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/a-treatise-on-group-policy-troubleshooting-8211-now-with-gpsvc/ba-p/400304  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-25*

The following is a list of Group Policy Settings recommended by Microsoft to lockdown a Remote Desktop Session Host / Citrix Session. These settings should go in the Citrix VDA Non-Admin Users GPO. All settings are located at User Configuration > Policies.    

    

reference：https://www.carlstalhood.com/group-policy-objects-vda-user-settings/    

Hope this information can help you    

Best wishes    

Vicky
