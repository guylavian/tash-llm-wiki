---
title: "News and Interests Breaks Everytime and Doesn't Show Weather Without Me Clicking On It!!!"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3902729/news-and-interests-breaks-everytime-and-doesnt-sho
question_id: 3902729
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# News and Interests Breaks Everytime and Doesn't Show Weather Without Me Clicking On It!!!

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3902729/news-and-interests-breaks-everytime-and-doesnt-sho (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

News and interests, even after booting the PC turns into a folder icon, and it even completely disappear sometimes. I need to click on it to make it load! And it works even when it disappears when I click on it.

It is so annoying! The whole point of having it is to having a real-time updates, without need to touch it! If I wanted to click on it I would google weather as well!!!

When it turns into a folder icon:
https://imgur.com/a/pmxdl2B

And when it completely disappears:
https://imgur.com/a/HpbLjP4

Normally when I hover over my mouse on it it has a flashing effect, like it disappears and reappears delayedly. But sometimes it stucks in the disappeared effect.

## Answer (community) — community member

*upvotes: 0 · updated: 2025-03-01*

Hi letumexordo

Welcome to Microsoft Community.

  

Based on your description, I understand that you've noticed that News and Interests turns into a folder icon when you start your computer, and sometimes disappears altogether and must be clicked on before it will load, and sometimes even after clicking on it. I understand very well how you feel!

  

Thank you very much for the pictures so I can get a better understanding of your situation.

  

Typically, problems occurring with News and Interests can be due to some of the following reasons.

-  The icon cache or service that the widget relies on (e.g. WebExperienceHost) may be corrupt.

-  the taskbar functionality is managed by explorer.exe, which if it is running abnormally can cause problems with the icon display.

-  There may be some cases where some system files are corrupted or missing.

-  Third party software interference, security software or system optimization tools may limit the background service of the widget.

-  The user account we are currently using may be damaged or lost causing the problem.

etc.

  

I will give you some suggestions and options to hopefully solve your problem or find out what is causing it! However, this is the first time I've replied to this question, so please understand and provide more information in your reply (pictures would be great!). Thank you very much!

  

Option 1: Let's start with the simpler option.

-  Let's try restarting Windows Explorer first to see if the problem still exists.

Open Task Manager by pressing Ctrl+Shift+Esc -> find “Windows Explorer” -> right-click and select “Restart”.

  

-  We tried to manually reset the news and interests function.

Right-click on the taskbar -> disable “News and Interests” -> wait for 10 seconds -> re-enable the feature.

  

Option 2: We try to manually clear the icon cache and reset it.

  

Click on “Windows Logo Key” to open the search bar -> Type “cmd” in the search bar and open it with administrator privileges -> Please enter the following commands

  

```
taskkill /IM explorer.exe /F

DEL /A:H "%localappdata%\IconCache.db"

start explorer.exe
```

  

The system will automatically create a new cache after restarting your computer.

  

Option 3: Consider widgets or news and interest-related features related to Windows Web Experience.

  

So let's try uninstalling UWP via PowerShell and reinstalling it via Microsoft Store to see if the problem persists.

  

-  Uninstall UWP via Windows PowerShell.

  

```
Get-AppxPackage *Microsoft.WindowsWebExperience* | Remove-AppxPackage
```

  

-  Reinstall via Microsoft Store.

The link is: Windows Web Experience Pack - Microsoft Apps

  

-  Restart the computer and see if the problem still exists.

  

Option 4: There may be cases where some system files are corrupted or missing causing the problem.

  

At this point we try to completely repair the system in two ways to at least ensure that the problem is not due to system corruption.

  

-  Scan and repair the system from the command line.

Click on “Windows Logo Key” to open the search bar -> Type “cmd” in the search bar and open it with administrator privileges -> Please enter the following commands

  

```
DISM /Online /Cleanup-Image /ScanHealth

DISM /Online /Cleanup-Image /CheckHealth

DISM /Online /Cleanup-Image /RestoreHealth

SFC /Scannow
```

  

Please note: The above commands need to be repeated 5~6 times to ensure the completeness of the scan!

  

-  Please try non-destructive repair.

The steps are as follows

(1) First download the Media Creation Tool for Windows 10 via the following link. (Media Creation Tool)

The link is: Download Windows 10

  

Once the download is complete open it and select the ISO file.

  

(2) After downloading the ISO file, double click to open and run “setup.exe”.

  

(3) Under the “Install Windows 10” page, select “Change how the installer downloads updates”.

  

(4) Under the “Get Updates, Drivers, and Optional Features” screen, select “Not Now”.

  

(5) Follow the instructions to continue.

Please note: If prompted for a key, the downloaded ISO image file does not match the current system version.

  

(6) Under the Select what to keep screen, make sure you select “Keep personal files and applications” so that the contents of your computer will not be affected or lost.

  

(7) Start the non-destructive repair.

  

Option 5: If you have recently received a system update push, we can try to update your system. Sometimes the update process can help us to fix some potential problems with the system.

  

“WIN + i” Open Settings -> ‘Update & Security’ -> ”Check for updates”

  

Option 6: We need to manually check and ensure that widget related services are enabled.

  

“WIN + R” to open ‘Run’ -> type ‘services.msc’ and open it -> find the ‘Web Experience Host’ service -> right-click to set it to ‘Automatic’ and start the service

  

Option 7: Please try to clean boot your computer.

  

Since clean boot uses only a limited set of files and drivers, it can help us to effectively troubleshoot the possibility of problems caused by third-party applications, driver conflicts, etc.

  

You can refer to Clean Boot for more information: How to perform a clean boot in Windows - Microsoft Support

  

After clean boot, please slide down the webpage after opening the link and find “How to determine what is causing the problem after you do a clean boot” This is a dichotomy that helps us pinpoint the service that is causing the problem and disable it.

  

Disclaimer: A “clean boot” starts Windows with a minimal set of drivers and startup programs. It helps to determine whether a background service is interfering with your game or program and to isolate the cause of a problem. 

These steps of "clean boot" might look complicated at first glance. However, to avoid any trouble for you, please follow them in order and step-by step so that it will help you get back on track.

  

Option 8: Sometimes the problem may occur due to corruption or loss of the user account profile we are currently using.

  

Let's try creating a new local administrator account from the command line and logging in to see if the problem persists.

  

Click “Windows Logo Key” to open the search bar -> Type “cmd” in the search bar and open it with administrator privileges -> Please enter the following command

```
net user USERNAME PASSWORD /add

net localgroup administrators USERNAME /add
```

  

Please note: USERNAME PASSWORD can be replaced with your preferred account name and password, if you don't need a password you can leave out the PASSWORD.

I sincerely hope that the above information and programs will help you! Please feel free to contact me (Photos related to the question would be great!).

I look forward to hearing back from you. 

Best Regards

Arthur Sheng | Microsoft Community Support Specialist

Not blaming you at all, just wanna express my frustration with Windows. I don't understand how after all those years Microsoft can't manage to make things work perfectly? Though we don't experience all those blue screen errors from XP to Windows 7 days, it's still annoying that Microsoft is incompetent on making things work properly and stably. Why they just don't force this widget's background process and block any other program that limits the background service of the widget? 

Option 1: Restarting Windows Explorer does not solve the issue. But the News and interests widget were not there, it was in that "disappeared" status and restarting Windows Explorer did make it turn into the folder icon instead of showing weather. 

-  It didn't work. After I did turn it off, then turn it on after waiting for 10 seconds, folder icon appeared again, and while I was typing this, it did disappear completely, then popped up again as folder icon. 

Well, I'm only doing it to help you see where the problem is, such solution is unacceptable. I don't want to do anything just so the widget functions properly. It is Microsoft's job to make their OS and anything related to it function properly. 

Option 2: Restarted the PC, still folder is there, no weather info at all. 

Option 3: Though you haven't stated that I should type this on cmd, I did get I am supposed to put that code there. And I get this error message: 

"'Get-AppxPackage' is not recognized as an internal or external command,  

operable program or batch file." 

Hey, btw after 3th scan completed, I did past something else, some text. Didn't press on Enter, would it interfere the process? 

Now I can't even scan further, it gave an error message and the error message still pops after restarting and running cmd as administrator. 

The error message is that: 

"C:\WINDOWS\system32>DISM /Online /Cleanup-Image /ScanHealthDISM /Online /Cleanup-Image /CheckHealthDISM /Online /Cleanup-Image /RestoreHealthSFC /Scannow  

Error: 87  

The Online option has been duplicated on the command-line.  

Remove the duplicate option and try the command again.  

The DISM log file can be found at C:\WINDOWS\Logs\DISM\dism.log  

C:\WINDOWS\system32> "

Okay, it did give the same error after I shutdown the PC instead of restart, accidentally. So I thought maybe restarting would do it because restarting has a different effect compared to shutdown, I believe. And it works again. Just wanted to keep it here as an additional detail.

I've done this 6 times from the scratch.

Well, since there are so many text, I'll just upload a screenshot of it. After the first scan, I've got these codes

"/SCANNOW        Scans integrity of all protected system files and repairs files with

```
problems when possible.
```

/VERIFYONLY     Scans integrity of all protected system files. No repair operation is

```
performed.
```

/SCANFILE       Scans integrity of the referenced file, repairs file if problems are

```
identified. Specify full path
```

/VERIFYFILE     Verifies the integrity of the file with full path .  No repair

```
operation is performed.
```

/OFFBOOTDIR     For offline repair, specify the location of the offline boot directory

/OFFWINDIR      For offline repair, specify the location of the offline windows directory

/OFFLOGFILE     For offline repair, optionally enable logging by specifying a log file path"

However, it is not the whole text, I've just copy pasted to give you an idea which part it is.

And on third try, I got the last part.

https://imgur.com/lKh5sER

Well, I have downloaded Media Creation Tool. And when I double click on it, I see Accept then 2 options pop up:

-  Upgrade this PC now

-  Create installation media (USB flash drive, DVD, or ISO file) for another PC.

Not such an option like “Install Windows 10” or “Change how the installer downloads updates”. So I chose "Upgrade this PC now" option hoping it'll give me the options you've listed.

Well, it asks me to install Windows 10. And, I don't want to do this, I don't trust that it will not break things. So I pass that step.

Option 5: No updates available. The system is up to date.

Option 6: No ‘Web Experience Host’ is available. It simply does not exist in the list. So it seems it is what the issue is caused by. I've double checked.

Option 7: Sorry, it's a big no no. Just to make sure a goddamn feature function properly I'm not gonna do this process, disable, enable, reboot. It's not my responsibility to fix the mess Microsoft is created. They are supposed to features run seamless.

Option 8: I'd better not mess with administrator accounts, sometimes it causes all your desktop gone! I lose my notepads I've created once because of this!!

## Answer (community) — community member

*upvotes: 0 · updated: 2025-02-28*

Hi letumexordo

Welcome to Microsoft Community.

Based on your description, I understand that you've noticed that News and Interests turns into a folder icon when you start your computer, and sometimes disappears altogether and must be clicked on before it will load, and sometimes even after clicking on it. I understand very well how you feel!

Thank you very much for the pictures so I can get a better understanding of your situation.

Typically, problems occurring with News and Interests can be due to some of the following reasons.

-  The icon cache or service that the widget relies on (e.g. WebExperienceHost) may be corrupt.

-  the taskbar functionality is managed by explorer.exe, which if it is running abnormally can cause problems with the icon display.

-  There may be some cases where some system files are corrupted or missing.

-  Third party software interference, security software or system optimization tools may limit the background service of the widget.

-  The user account we are currently using may be damaged or lost causing the problem.

etc.

I will give you some suggestions and options to hopefully solve your problem or find out what is causing it! However, this is the first time I've replied to this question, so please understand and provide more information in your reply (pictures would be great!). Thank you very much!

Option 1: Let's start with the simpler option.

-  Let's try restarting Windows Explorer first to see if the problem still exists.

Open Task Manager by pressing Ctrl+Shift+Esc -> find “Windows Explorer” -> right-click and select “Restart”.

-  We tried to manually reset the news and interests function.

Right-click on the taskbar -> disable “News and Interests” -> wait for 10 seconds -> re-enable the feature.

Option 2: We try to manually clear the icon cache and reset it.

Click on “Windows Logo Key” to open the search bar -> Type “cmd” in the search bar and open it with administrator privileges -> Please enter the following commands

```
taskkill /IM explorer.exe /F

DEL /A:H "%localappdata%\IconCache.db"

start explorer.exe
```

The system will automatically create a new cache after restarting your computer.

Option 3: Consider widgets or news and interest-related features related to Windows Web Experience.

So let's try uninstalling UWP via PowerShell and reinstalling it via Microsoft Store to see if the problem persists.

-  Uninstall UWP via Windows PowerShell.    Get-AppxPackage Microsoft.WindowsWebExperience | Remove-AppxPackage

-  Reinstall via Microsoft Store.

The link is: Windows Web Experience Pack - Microsoft Apps

-  Restart the computer and see if the problem still exists.

Option 4: There may be cases where some system files are corrupted or missing causing the problem.

At this point we try to completely repair the system in two ways to at least ensure that the problem is not due to system corruption.

-  Scan and repair the system from the command line.

Click on “Windows Logo Key” to open the search bar -> Type “cmd” in the search bar and open it with administrator privileges -> Please enter the following commands

```
DISM /Online /Cleanup-Image /ScanHealth

DISM /Online /Cleanup-Image /CheckHealth

DISM /Online /Cleanup-Image /RestoreHealth

SFC /Scannow
```

Please note: The above commands need to be repeated 5~6 times to ensure the completeness of the scan!

-  Please try non-destructive repair.

The steps are as follows

(1) First download the Media Creation Tool for Windows 10 via the following link. (Media Creation Tool)

The link is: Download Windows 10

Once the download is complete open it and select the ISO file.

(2) After downloading the ISO file, double click to open and run “setup.exe”.

(3) Under the “Install Windows 10” page, select “Change how the installer downloads updates”.

(4) Under the “Get Updates, Drivers, and Optional Features” screen, select “Not Now”.

(5) Follow the instructions to continue.

Please note: If prompted for a key, the downloaded ISO image file does not match the current system version.

(6) Under the Select what to keep screen, make sure you select “Keep personal files and applications” so that the contents of your computer will not be affected or lost.

(7) Start the non-destructive repair.

Option 5: If you have recently received a system update push, we can try to update your system. Sometimes the update process can help us to fix some potential problems with the system.

“WIN + i” Open Settings -> ‘Update & Security’ -> ”Check for updates”

Option 6: We need to manually check and ensure that widget related services are enabled.

“WIN + R” to open ‘Run’ -> type ‘services.msc’ and open it -> find the ‘Web Experience Host’ service -> right-click to set it to ‘Automatic’ and start the service

Option 7: Please try to clean boot your computer.

Since clean boot uses only a limited set of files and drivers, it can help us to effectively troubleshoot the possibility of problems caused by third-party applications, driver conflicts, etc.

You can refer to Clean Boot for more information: How to perform a clean boot in Windows - Microsoft Support

After clean boot, please slide down the webpage after opening the link and find “How to determine what is causing the problem after you do a clean boot” This is a dichotomy that helps us pinpoint the service that is causing the problem and disable it.

Disclaimer: A “clean boot” starts Windows with a minimal set of drivers and startup programs. It helps to determine whether a background service is interfering with your game or program and to isolate the cause of a problem. 

These steps of "clean boot" might look complicated at first glance. However, to avoid any trouble for you, please follow them in order and step-by step so that it will help you get back on track.

Option 8: Sometimes the problem may occur due to corruption or loss of the user account profile we are currently using.

Let's try creating a new local administrator account from the command line and logging in to see if the problem persists.

Click “Windows Logo Key” to open the search bar -> Type “cmd” in the search bar and open it with administrator privileges -> Please enter the following command

```
net user USERNAME PASSWORD /add

net localgroup administrators USERNAME /add
```

Please note: USERNAME PASSWORD can be replaced with your preferred account name and password, if you don't need a password you can leave out the PASSWORD.

I sincerely hope that the above information and programs will help you! Please feel free to contact me (Photos related to the question would be great!).

I look forward to hearing back from you. 

Best Regards

Arthur Sheng | Microsoft Community Support Specialist
