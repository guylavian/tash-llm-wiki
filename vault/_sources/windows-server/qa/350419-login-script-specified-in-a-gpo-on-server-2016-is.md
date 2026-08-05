---
title: "login script specified in a GPO on server 2016 is not running right on a win10 client"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/350419/login-script-specified-in-a-gpo-on-server-2016-is
question_id: 350419
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# login script specified in a GPO on server 2016 is not running right on a win10 client

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/350419/login-script-specified-in-a-gpo-on-server-2016-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Forum,   

the setup:   

-Thank you in advance yet again for helping with the banes of computing.  

-I have a lab setup with one pc running microsoft server 2016 that is a domain controller and another pc running win10 professional.  

-They are both connected with cat 6 cables to the same netgear soho router / switch / wifi device (a netgear n750).  

-I am doing this to get good at doing this again (eg, the last time i did this was with server 2003).  

the problem:   

-I am trying to get a simple login script to run (the script is just a text file that is saved as a batch file with net use commands in it to map network drives) when the win10 pc logs into the server .  

-I am trying to run the login script from a gpo.  

-The win10 pc can log into the domain, and it seems the gpo was processed (eg, gpresult says that the gpo was processed (eg, there are no errors mentioned in gpresult)), but i do not get the results i expected.  

-there is a pause statement in the login script, so i expected to get the login process to pause and make me press a key to continue....this did not happen  

-also, i expected to get the drive letter i am trying to map (which is Y:) to be available from the windows file explorer....this did not happen either  

-also, and i unfortunately do not understand this part at all..., I found that if i open a dos prompt and i try to map Y: with a net use command it says the drive letter is already in use?!  

-so then i found i could just navigate to the Y: drive in the dos prompt and see its contents normally.  

-then, i found that i can use the GUI map a network drive option in windows file explorer to map a Y: drive to a different folder than what the dos prompt has.  

-so, instead of getting what i expected, the Y: drive in the dos prompt is pointing to one folder on the server, and its possible to point the Y: drive in the file explorer to another folder on the server.  

-regarding the gpo settings:   

the batch file is called ls-y1.bat  

these are its contents :  

net use y: \server2\y-1  

pause  

rem the end  

-note: server2 is the name of the win2016 server, y-1 is the name of the folder i am trying to share  

-i have tried this with the y-1 folder itself being shared as "y-1", and without the y-1 folder itself being shared at all  

-also, for the whole time the c: drive of the server itself is currently shared, too  

-the computer object for the win10 pc is in an ou i created on the server  

-the user account i am logging in with from the win10 pc is in another ou i created on the server  

-i created a gpo that has only one setting, this login script setting, and it is linked to the ou the user object is in  

-this is its location in the gpo manager:   

group policy management editor, user configuration, policies, windows settings, scripts (logon/logoff), logon  

-in the logon settings, i selected add, then browse, and a browse window opened to this location:   

C:\Windows\SYSVOL\sysvol\d2.local\Policies{773467F8-58E8-4D00-8E61-FBC1A552A614}\User\Scripts\Logon  

-note: i confirmed the number in the {}'s matches the GPO i'm using  

-also, i placed the batch file in this folder so its path and name is   

C:\Windows\SYSVOL\sysvol\d2.local\Policies{773467F8-58E8-4D00-8E61-FBC1A552A614}\User\Scripts\Logon\ls-y1.bat  

-also, i have restarted the win10 pc with each part/stage/change  

the question:   

-can anyone help me with this?  

-i recall when using server 2003, there was a folder called something like "%systemroot%\System32\Repl\Imports\Scripts" that i had to put the script in, but i did not find that folder on the win2016 server  

-i manually created this folder, and i put the login script in it, and i edited the gpo to point to the new location, and i am about to try to log in again with the win10 pc, but the win10 is taking a very long time to run its latest update (i honestly thought i set it to not update today...but it is updating for a long time anyway, and it may not matter anyway, and i did not want to wait to post this question...if that changes anything i will update this post...)

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-22*

-more detail (i hope this is helpful):   

-just to see if there was a difference, i copied the script file to the client pc (i made the path the same as it is on the server, and i updated the path in the gpo to say "C: _alab\script\xls-y1.bat ")  

-then when i restarted the client pc and logged in again, and ran gpresult, the "logon scripts" section said the script ran, but the timestamp was way off from what time is really is?!...i dont know why that happened...  

your question ....why not use the GPP to map the drive  

-i tried this, and it worked! ...so thank you for that  

but...my main goal is to be able to run batch files (and ultimately other script files) from gpos  

if you can offer any more help, i would be very grateful  

-michael

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-09*

update:   

-the windows 10 pc finished updating, and i logged into the domain again, and i dont have the y drive in the dos prompt or in the file explorer, so moving the login script file to the repl\imports\scripts folder i made apparently did not help  

-i ran gpupdate /user mike2 /v (mike2 is the name of the user i am logging in with from the win10 pc)  

-in the section: user settings, applied group policy objects: the gpo is listed (the GPO name is "unknown-ls-y1")  

-but in the section: user settings, rsop for user, logon scripts: it has this line "LastExecuted: this script has not yet been run"
