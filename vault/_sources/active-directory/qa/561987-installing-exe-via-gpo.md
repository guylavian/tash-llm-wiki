---
title: "installing exe via gpo"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/561987/installing-exe-via-gpo
question_id: 561987
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# installing exe via gpo

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/561987/installing-exe-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

How do I deploy exe via gpo? I am trying to install Python but they only do EXEs now!  

Help!

## Answer (community) — community member

*upvotes: 1 · updated: 2021-09-23*

Hello @AB123  ,

The most common way would be to create a logon script that verifies the installation (installed/not installed).

The GPO would be:  

Computer Configuration > Policies > Windows Settings > Scripts (Startup/Shutdown).

You will need to save a script in a DFS share accessible for the clients (such as Netlogon, or other if configured) and store a BAT script.

Examples of the script:

IF EXIST "c:\myapp - Installed.txt" GOTO END

\servername\sharename\<path>\installfilename.exe  

echo "Myapplication is installed on this computer" > "c:\myapp - Installed.txt"  

goto END

:END

Basically it checks if a TXT file is already created, if yes: it finishes, if not: proceeds with install and then write the file. You may need to check the install parameters of your app for things like /passive or /silent to run on background without user interaction.

Hope this helps in your case,

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-09-22*

Hi @AB123       

You can install exe's via active directory GPO.    

Refer below link it is explained step-by-step.    

https://community.spiceworks.com/how_to/160869-how-to-install-exe-with-group-policy    

If the Answer is helpful, please click `Accept Answer` and up-vote, so that it can help others in the community looking for help on similar topics.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-22*

Hi @Anonymous   @SUNOJ KUMAR YELURU       

I have tried to use : https://www.exemsi.com/ to convert python 3.5.2 exe into a msi but no luck! Any ideas on what I am doing wrong or if there is a better way to do it

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-22*

You cannot deploy ".exe" through GPO.  It has to be .msi.  

You need to convert the .exe to .msi first and then you will be able to install the .msi  

hth

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-22*

Hi @SUNOJ KUMAR YELURU       

Is there not a way without using a MSI converter to deploy exes?
