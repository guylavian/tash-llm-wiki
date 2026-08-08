---
title: "Screensaver GPO not working properly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2197044/screensaver-gpo-not-working-properly
question_id: 2197044
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directo"]
---
# Screensaver GPO not working properly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2197044/screensaver-gpo-not-working-properly (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

```
I have a GPO for screensaver to run after 30 minutes of system idle. Buts its not running the specified time and hope you advice to troubleshoot screensaver policy.
```

Thanks & Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-25*

Hello Yakub Pangat_AIMS,  

Thank you for posting in Microsoft Community forum.  

1.What specific GPO setting related to ScreenSaver did you configure?  

2.Did you configure screen saver within GPO "User Configuration\Administrative Templates\Control Panel\Personalization\Enable screen saver"?  

3.Based on the description "I have a GPO for screensaver to run after 30 minutes of system idle.", did you configure 30 minutes within GPO "User Configuration\Administrative Templates\Control Panel\Personalization\Screen saver timeout"?  

4.Based on "But its not running the specified time", do you know what the actual time is instead of 30 minutes?  

I assume your device is in one domain and you sign in using domain user account.  

Maybe there are other GPO setting related to ScreenSaver applying to the user or the computer, you can try to check by exporting gpresult file.  

You can search the key word related to "ScreenSaver" or "Screen" or "Saver" or "minutes" or "seconds"  

For checking Computer Configurations within gpresult, you can follow steps below.  

Logon this machine using administrator account.

Open CMD (run as Administrator).

Type gpresult /h C:\gpo.html and click Enter.

Open gpo.html and check gpo setting under "Computer Details".

For checking User Configurations within gpresult, you can follow steps below.

Logon the machine using normal domain user account (the user account you sing in now).

Create a folder named F1.

Open CMD (do not run as Administrator).

Type gpresult /h C:\F1\gpo.html and click Enter.

Open gpo.html and check gpo setting under "User Details".

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
