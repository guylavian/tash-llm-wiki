---
title: "GPO policies"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/66849/gpo-policies
question_id: 66849
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# GPO policies

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/66849/gpo-policies (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there,  

I have an Windows server with ADDS ,DNS and GPO services.  

An workstation is member of the Domain.  

I configured 3 GPO's : 1 dont acces pc settings, 2, deployment google chrome and 3 lockscreen and desktop wallpaper.  

GPO 1 works fine on the workstation but 2 and 3 not. On the workstation I only see on the desktop an black background and lockscreen image the standard from microsoft.  

On the windows server I configure GPO 2 and 3 but only GPO 3 works..  

Hopefully its enough info, please need some help

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-17*

Hi,    

You are welcome. Thank you so much for your feedback.    

To check the computer configuration on the servers, we have to run as administrator to open CMD. Hope we could have a recheck.    

As for the deployment of google chrome, there will be computer configuration and user configuration. If it is computer configuration, the GPO will be linked to the OU with computer accounts. And the deployment method is assigned.     

    

If it is user configuration, the GPO will be linked to the OU with user accounts. The deployment method could be published or assigned. If it is published, it will not install automatically when the user logs on to the computer. If we want it installed automatically, we could choose assigned deployment method. Besides, under the Deployment tab, choose "Install this application at logon".    

    

    

According to our description, the GPOs work fine on our DC server, but not working on our workstation. May I know what the workstation is, member server or client? If it is client, what the version is?     

Since the GPOs work on the DC server, there will be no problem with the configurations. Then to check whether it is applied or not on the workstation, we could run gpresult /h to check the result report as mentioned before.    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-08-15*

Hi,  

GPOs for Computer configuration are not listed in the reports but User Configuration does.  

To display the GPO settings for computer configuration , you have to launch gpresult command with a local administrator account on member machine.  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-15*

Hi Hannah and thanks for the detailed explain.  

GPOs for Computer configuration are not listed in the reports but User Configuration does.  

The thing is when I switch GPO for google chrome from Computer to User configuration then it works, but users have to install it by hand.  

I want it installed automatically.  

It is weird because the GPO's for wallpaper, lock screen image and deploy  google chrome only works on my DC server..  

I have applied more GPOS based on computer and user config on my workstations and they working fine..  

For me right know I just want only the 3 GPO desktop wallpaper, lock screen image and deploy google chrome to work..

## Answer (community) — community member

*upvotes: 0 · updated: 2020-08-14*

Hello,  

Thank you so much for posting here.  

To troubleshoot the issue, we could check the following points:  

1, As per the three GPOs, there are computer configuration and user configuration. For User Configuration section, our Group Policy object must be linked to an OU with users objects. Then the users in this OU will apply the user setting within this GPO object. While for Computer Configuration, the GPO must be linked to an OU with computer objects.   

We could kindly have a check whether they are correctly configured.  

2, After the configuration, if we want GPO settings to refresh, we can run gpupdate /force command.  

For several special GPO settings, such as folder redirection, drive map, Software Installation, Disk Quota, we must restart the machines or sign out and sign in the user account to refresh these GPO settings.  

3, To check if the specific settings get applied or not, we could run “gpresult /h” to get a detailed group policy result report.  

If it is computer configuration,   

-  Logon one client with the Administrator account.  

-  Open CMD, run as administrator.  

-  Type gpresult /h C:\report.html and click Enter.  

-  Open report file to check the policies under Computer Details.  

If it is user configuration,   

-  Logon one client with domain user account who is within the OU linked by the GPO.  

-  Create a new folder in C drive named Folder.  

-  Open CMD, type gpresult /h C:\Folder\report.html and click Enter.  

-  Open report file to check the policies under User Details.  

For any question, please feel free to contact us.  

Best regards,  

Hannah Xiong
