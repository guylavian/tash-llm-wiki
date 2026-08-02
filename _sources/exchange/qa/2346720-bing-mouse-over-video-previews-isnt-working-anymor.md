---
title: "bing mouse over video previews isn't working anymore please can someone explain how to fix this or explain why it's changed"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2346720/bing-mouse-over-video-previews-isnt-working-anymor
question_id: 2346720
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 3
qa_tags: []
---
# bing mouse over video previews isn't working anymore please can someone explain how to fix this or explain why it's changed

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2346720/bing-mouse-over-video-previews-isnt-working-anymor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

bing mouse over video previews isn't working anymore 

please can someone explain how to fix this or explain

why it's changed I'am using Win11Home And Edge 

not sure if an update changed things or if i did but there are

no error messages that is trying to load as if it's not a feature anymore

I can't find any Option to turn it back on or info about if that feature was just removed 

recently hope this can be fixed was very helpful

It's now May 31,2024

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-01*

Hello, Mustafa Muhammad. 

Welcome to Microsoft Community.

Thank you for your description of the problem.

You are experiencing an issue where the video preview feature is not working in Microsoft Edge browser, do you mean: when you move your mouse over the video tab or cover, the video will no longer play in the small window preview?

What I need to check with you in this case is whether you are not able to preview the video in a small window in all video sites, or is this only happening in some specific sites?

I note that you are using Windows 11 Home Edition, in which we can try to troubleshoot the effect at the software level using Clean Start:

Perform a clean boot

The method is as follows

-  Tap Windows+R and type msconfig

-  Open System Configuration and select General tab - Selective Startup.

-  Remove the checkbox of Load startup items.

-  Go to the Services tab - click Hide all Microsoft services in the lower left corner, and then click Disable all.

-  Click OK and restart your computer. (Be sure to select Hide all Microsoft services first and then click Disable all, otherwise it may cause unforeseen problems such as not being able to access the system.)

See if the problem still recurs.

Disclaimer: Clean boot is a way to start Windows with a minimal set of drivers and startup programs so that you can determine if background programs are interfering with your games or programs and help you figure out the cause of the problem. It will help you get back on track.

We can also try to repair the system if there exists some corruption and loss of system files that caused this to happen:

-  Search for CMD, find the command prompt, and choose to run in administrator mode.

-  Enter the following commands one by one, make sure to execute the next command after the previous one is completed.

DISM /Online /Cleanup-Image /ScanHealth

DISM /Online /Cleanup-Image /CheckHealth

DISM /Online /Cleanup-Image /RestoreHealth

SFC /Scannow

-  After the scanning is completed, you can check the scanning information to see if the problem has been detected and fixed.

If the above methods do not work, you can try to update your Microsoft Edge browser and Windows system as follows:

Update Microsoft Edge browser.

-  Open Microsoft Edge browser.

-  Click the “...” menu in the upper right corner of the browser and select “Help”. menu in the upper right corner of the browser and select “Help and Feedback”.

-  Select “About Microsoft Edge”.

-  If there are updates available, you will be automatically checked for them and prompted to update.

-  Follow the prompts to complete the Edge browser update.

To update Windows 11:

-  Open Windows Settings and click on “Update and Security”.

-  Select the “Windows Update” tab.

-  Click the “Check for Updates” button and the system will automatically check for available Windows updates.

-  If an update is available, click the “Download and Install” button.

-  Wait for the update to finish downloading and install automatically.

-  Restart your computer to complete the update.

Please make sure your computer is fully powered on and your internet connection is stable during the update process. After the update is complete, please try using the video preview feature of Microsoft Edge again to see if the problem is solved.

If the problem is still not solved after the update, using the Beta version of Microsoft Edge to solve the problem of video preview function failure is also a good choice. Here are some specific steps and suggestions:

-  Download Microsoft Edge Beta version.

   - Open the official website of Microsoft Edge:  Get to Know Microsoft Edge

   - Find the download link for “Microsoft Edge Beta” and click on download.

   - Wait for the download to complete and install the Beta version of Edge.

-  Update Edge Beta.

   - Open the Edge Beta browser and go to the “Settings” menu.

   - Select the “About Microsoft Edge” option.

   - If there is an update available, you will be automatically prompted to update.

   - Follow the prompts to complete the Edge Beta update.

-  Check the video preview feature.

   - Try out the video preview feature in the Edge Beta browser.

   - See if the feature has been fixed or improved.

-  Cautions: Edge Beta versions may include video previews.

   - Edge Beta version may contain some unstable features and bugs, please pay attention to backup important data when using it.

   - If the Beta version does not solve the problem, you can always switch back to the full version of Edge.

The above is the information I can provide for you; I hope it can help you.

Thank you for your support of Microsoft products, we look forward to your feedback.

Best Regards.

Leo.L - Microsoft Community Support Specialist
