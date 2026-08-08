---
title: "RE : task not working after deploying with gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/860417/re-task-not-working-after-deploying-with-gpo
question_id: 860417
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# RE : task not working after deploying with gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/860417/re-task-not-working-after-deploying-with-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey reader,    

I created a topic 2 days ago on the subject. I forgot to answer to my beacon of light MotoX80.    

Here's the link : task-not-working-after-deploying-with-gpo.html    

So today I went back to it, and here is a quick update :    

I found that there was no point to deploy the task like that. When the system start, it doesn't use an user credential to authentify to my VPN. it uses the PC name.    

I'll give more explanation on what i'm trying to do :    

I want for users to be able to access the vpn before they login to their session. That's the point of the vpn. So i set up an IKEv2 vpn with strongswan. It uses the eap-radius plugin to talk with a radius that uses ntlm_auth with mschap to retrieve passwords from a samba ldap (where i deploy my gpos using RSAT on a windows virtual machine).    

The VPN connection called "Linkso VPN" uses Windows login credential to automatically connect to the VPN.    

It worked great on a client where i manually created a task in the session. The VPN would start at every startup. But now that the computer is joined in the domain and that I have to deploy on every machine, it gets more tricky.    

What i've tried so far was after the indication of MotoX80 :    

I used the script you gave me and found out that it searches at C:\Windows\System32\config\systemprofile\AppData\Roaming\Microsoft\Network\Connections\Pbk\rasphone.pbk    

I didn't mind much because something more interesting happened, the vpn tried to connect without success using what I think is the %USERNAME% of the account System :    

    

What I did since it looks in another directory was to implement in "Start in:" the path to the right rasphone.pbk from the user that is logged on.    

But it makes the task fail with the error 2147942667 that means a permission error or path error. My guess is that it doesn't know where it is since we're not logged in the session...    

Now I don't know where to go from there. I have to deploy with NT AUTHORITY\System for it to appear in the client side, but it uses the wrong username.    

And using a .bat file is the same since it's the System that start the task. I get the same error by opening a .bat file with the task.    

I don't want to put the username and password in the .bat security wise. Also because my higher-ups would not tolerate it.    

I gladly take any help, advice or lead. I would like to thanks again MotoX80 that made me realise so many things I didn't know.    

Have a wonderful day.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-24*

Hey,  

After an hour talking about it, we decided to use a script instead of a task scheduler.  

It's logically impossible for the task to start the VPN connection with the user winlogon before he logins to his session.  

So we are just going to do a task that starts a script at login session to connect the user.  

We talked about some issues like what if we change the password on the LDAP but the user is at home ?  

It's an issue that could be resolved by RDP to their machine when they have an internet access and change it manually.  

Anyway ! Maybe there is a way but i'm just a trainee with 2 weeks left. I understood that improvising, automate the VPN is the hardest part.  

If anyone tried something similar, or had some equivalent to this, please let me know.  

Thanks again MotoX80 for all the answers.  

Have a wonderful week !

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-23*

Hi MotoX80,  

Thanks for the answer. I talked with my tutor and we are going to try things tomorrow. The logon script is a good idea ! That is going to be a lot of gpos now if we put that in place.  

I will update the post tomorrow to tell our heroic tale of how we made this work or come back with hands full of errors.  

Have a fantastic night.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-05-23*

I want for users to be able to access the vpn before they login to their session.   

the VPN connection called "Linkso VPN" uses Windows login credential to automatically connect to the VPN.  

If you don't want to save a password anywhere, then you would have to run the task in the context of the user. But you need a logon event to trigger that.   

Instead of system, can you set it run as Interactive when a user logs on? This creates a task that just displays the username at logon time of any user. Use your bat file instead of the PS command.   

```
SCHTASKS /Create /tn LogonTest  /tr "Powershell.exe -ExecutionPolicy Bypass -command 'whoami.exe;start-sleep 10'" /ru interactive /sc onlogon
```

I don't think that the GUI will let you set a task to run as interactive, so you might have to use "Builtin\Users". Since you have an AD environment, you could also use a logon script.   

to my beacon of light MotoX80.  

Thank you, but I would not go that far. I'm just a retired sysadmin who is trying to keep his brain active answering these questions.
