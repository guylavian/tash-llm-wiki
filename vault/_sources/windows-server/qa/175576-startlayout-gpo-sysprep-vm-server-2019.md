---
title: "StartLayout GPO - Sysprep - VM Server 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/175576/startlayout-gpo-sysprep-vm-server-2019
question_id: 175576
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# StartLayout GPO - Sysprep - VM Server 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/175576/startlayout-gpo-sysprep-vm-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I have created a Windows Server 2019 VM (want to use it as a template) in which I have enabled the start layout GPO locally on the VM (have tried both computer and user variants). The taskbar layout is set as I want it on this VM.  

However when I clone and then sysprep the VM (using an unattend.xml file with copy profile) I find that although the GPO is enabled and the tiles in the start menu are locked, the taskbar pins are not set and the default icons are shown!!??  

Is this a known issue? Please help!  

Thankyou.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-27*

Hi,  

The cloned image might be the problem. You could try with image downloaded from MS official, then follow steps in below link to customize and sysprep:  

https://www.joseespitia.com/2016/06/27/customized-a-windows-10-start-layout/  

Hope this helps and please help to accept as Answer if the response is useful.  

Thanks,  

Jenny

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-26*

-  I have created a Windows server 2019 VM in which I have enabled the startlayout GPO.  

-  Startlayout is added before sysprep but the taskbar config is not applied after sysprep is finished. The startlayout policy is enabled pointing to the correct XML file after Sysprep.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-26*

Hi,  

1.using an unattend.xml file with copy profile  

Did you mean that you are using the StartLayout.xml which was exported from the VM(you've customized before)?

2.However when I clone and then sysprep the VM  

Per my knowledge, Clone is not officially supported since it might have some problems. The normal methods to keep customized startlay out is to add the .xml file before sysprep.

Reference link:  

https://www.joseespitia.com/2016/06/27/customized-a-windows-10-start-layout/  

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.

 

Hope this helps and please help to accept as Answer if the response is useful.

Thanks,  

Jenny
