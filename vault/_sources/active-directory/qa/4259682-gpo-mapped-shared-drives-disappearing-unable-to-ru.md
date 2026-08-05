---
title: "GPO Mapped Shared Drives Disappearing - Unable to run gpupdate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4259682/gpo-mapped-shared-drives-disappearing-unable-to-ru
question_id: 4259682
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# GPO Mapped Shared Drives Disappearing - Unable to run gpupdate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4259682/gpo-mapped-shared-drives-disappearing-unable-to-ru (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our IT team has noticed a problem with a variety of seemingly related symptoms on several different machines, with multiple different user accounts, each in a different OU for policy.

The initial problem that is obvious is that user's network drives are disappearing when then sign in.  These drives are currently mapped via group policy, but we suspect that the the replace/delete option is not working cleanly and causing things to hang up. I was able to get one error specific to mapping the drives in event viewer indicating the drive was already in use, even though it was not (details at end).  

In addition to the network drives disappearing, or only partially showing up, we have noticed the following related issues.  

-  Can't run programs as admin:  This is the most frustrating, because it prevents you from running diagnostics such as event viewer, or other commands that require elevation.  When you try to sign in as an admin (domain or local), it takes you to the UAC login prompt, but then it waits on a blank screen for about 1 - 2 minutes and then times out.  The exact time might vary.  After about 3 or four attempts, I was finally able to get past this, but then you have to redo it if you want to use a different admin account (attempt logging in several times, wait for it to not do anything for several minutes, try again, etc.)

-  The computer is unable to update Group Policy:  We have tried running "gpupdate /force" on the user's profile when this issue occurs, and it does not do anything.  The command prompt window literally sits there.   The current window I am waiting on has been attempting to run for over 1 hour and 30 minutes and it has not finished, thrown an error, or timed out.  At that point, I closed it out and tried running it again, once again it just sat there, when a successful completion usually takes less than a minute.

-  "Net Use" takes several minutes to run:  I ran it the first time, it took 10 - 15 minutes, finally returned that the shared drive was disconnected.    

Ran it immediately after, took another 10-15 minutes to say it was reconnecting.    

Ran it immediately after that, said it was disconnected again, this time giving immediate results as expected.    

Running again pulled up no shared connections.

-  Slow File Explorer: depending on what point in the process you are at, file explorer will be stuck on the green loading bar after trying to access the shared drives.  This is presumable because something is telling file explorer that the drives are there, but when you run "net use" they are disconnected.  As file explorer tries to connect, it slows down everything else, potentially contributing to some of the other issues.    

You are however able to ping the network drives and navigate to them via file explorer (when it does not freeze), provided that you do not click on the network drive.  One you click on the network drive, it freezes up, sometimes crashing causing very few programs to work when you try to restart explorer.exe

-  Slow Sign off and Restart: Attempts to sign off or restart when these issues are being experienced will cause the computer to hang with the spinning wheel for over 10 - 20 minutes.  wait long enough, and it might do something.  Generally a force shutdown by holding the power button will allow you to power on again.

Known (temporary) fix:  We have been able to temporarily fix the issue by forcing a shutdown, signing in as another user (mostly tested as a domain admin), running a gpupdate, and then signing out.  The gpupdate works, and when the user that was having issues before signs in, all of their shared drives work and there are no issues.... until they sign out or restart their machine, and then it acts up all over again.

Log Name: Application  

Source: Group Policy Drive Maps  

Date: 10/1/2021 2:56:08 PM  

Event ID: 4098  

Task Category: (2)  

Level: Warning  

Keywords: Classic  

User: SYSTEM  

Computer: XXX.XXX  

Description:  

The user 'Z:' preference item in the 'drives - PUBLIC (all users) {XXXXXXXXXXXXXX}' Group Policy Object did not apply because it failed with error code '0x80070055 The local device name is already in use.' This error was suppressed.  

Event Xml:  

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event"&gt;  

<System>  

<Provider Name="Group Policy Drive Maps" />  

<EventID Qualifiers="34305">4098</EventID>  

<Version>0</Version>  

<Level>3</Level>  

<Task>2</Task>  

<Opcode>0</Opcode>  

<Keywords>0x80000000000000</Keywords>  

<TimeCreated SystemTime="2021-10-01T18:56:08.1806002Z" />  

<EventRecordID>6403</EventRecordID>  

<Correlation />  

<Execution ProcessID="0" ThreadID="0" />  

<Channel>Application</Channel>  

<Computer>XXX.XXXXX</Computer>  

<Security UserID="XXXXX" />  

</System>  

<EventData>  

<Data>user</Data>  

<Data>Z:</Data>  

<Data>drives - PUBLIC (all users) {XXXXXXXXXXXXXXXXXXXXXXXXX}</Data>  

<Data>0x80070055 The local device name is already in use.</Data>  

</EventData>  

</Event>

Log Name:      Application 

Source:        Group Policy Drive Maps 

Date:          10/1/2021 3:38:38 PM 

Event ID:      4098 

Task Category: (2) 

Level:         Warning 

Keywords:      Classic 

User:          SYSTEM 

Computer:      XXX,XXX 

Description: The user 'S:' preference item in the 'drives - IT {XXXXXXXXXXXXXXXXXXXX}' Group Policy Object did not apply because it failed with error code '0x80070079 The semaphore timeout period has expired.' This error was suppressed. 

Event Xml: http://schemas.microsoft.com/win/2004/08/events/event">

## Answer (community) — community member

*upvotes: 3 · updated: 2021-10-14*

To update this post, we believe that we have found the fix, and it has nothing to with our group policy or any organizational settings.  This is a windows problem that occurs quite frequently from what I have researched online. The issue appears to be with windows explorer crashing when you attempt to open a network drive.

https://www.thewindowsclub.com/explorer-crashes-accessing-mapped-network-drives

Implementing fix number 6, adding a registry key appears to have resolved the issue for us. While we are still doing some additional testing, I am closing this ticket with this marked as the solution.

"Create a new Value in Windows Registry  

Another method to fix this issue is to create a new Value in Windows Registry. We have listed the instructions for this below. But before you proceed, it is better if you create a backup of Registry so that you can restore it if any problem occurs.  

create new value in Registry  

1] Press Win + R hotkeys to launch the Run command box. Type regedit and click OK. Click Yes if you receive a UAC prompt message.  

2] In the Registry Editor, copy the following path, paste it into its address bar, and hit Enter:  

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider  

3] Make sure that you have selected the NetworkProvider key on the left side. Now, right-click on the right side and go to “New > DWORD (32-bit) Value.” Name this newly created Value RestoreConnection. Now, double-click on it and set its Value Data to zero."

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-04*

I will go ahead and post in the other forum as recommended, but the question is related to how Microsoft drive mapping issues.  I expect that there are also end users who have experienced similar issues trying to map network drives who will also be able to contribute.    

Below is the link to the question in the IT Professionals forum.
https://docs.microsoft.com/en-us/answers/questions/574678/gpo-mapped-shared-drives-disappearing-unable-to-ru.html

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-01*

Hi A.  I'm Greg, 10 years awarded Windows MVP, specializing in Installation, Performance, Troubleshooting and Activation, here to help you.  

Microsoft Community is strictly an end-consumer forum.  As your question concerns an organizational setting, please ask at our sister forums for IT Professionals, Q&A forums here:  https://docs.microsoft.com/th-th/answers/index....

 There are also equally good (and sometimes busier) IT Pro forums here:

https://www.techrepublic.com/forums/

https://www.spiceworks.com/

I hope it helps.
