---
title: "GPO to change this message The person who setup this computer has chosen to block this site"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/449282/gpo-to-change-this-message-the-person-who-setup-th
question_id: 449282
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-edge-edge-development", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
---
# GPO to change this message The person who setup this computer has chosen to block this site

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/449282/gpo-to-change-this-message-the-person-who-setup-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have created a GPO to block URLs in Chrome, Edge and Firefox.  I would like to create a custom message to replace the default one that comes up when a URL is blocked but cannot find a way to do this.  Is there a way to modify this message on Blocked URL's?  

The person who set up this computer has chosen to block this site.  

Try contacting the system admin.  

ERR_BLOCKED_BY_ADMINISTRATOR

## Answer (community) — community member

*upvotes: 1 · updated: 2021-06-28*

I blocked the URL's on purpose I an NOT looking how to get around the blocks.  I am looking for how to customize the message to make it more specific for our company so users know if came from an internal source related to us.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-06-25*

Fortunately, if you get the error in Chrome, the solution is quite simple.  

Go to Start or press CTRL + R,  

Search for Regedit,  

Open Regedit,  

Go to the following directory:  

Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies  

You can also copy and paste the directory in Regedit  

Right click the Google key,  

Click on Delete.  

FIX: ERR_BLOCKED_BY_ADMINISTRATOR for Microsoft Edge Beta  

In Microsoft Edge it’s a different error than in Google Chrome.  

I recently started using the Microsoft Edge Beta version because it ran on Chromium and you could finally create separate user profiles. In the newest stable Microsoft Edge you can also create profiles now.  

After using Edge for a while I suddenly couldn’t open certain URLs anymore.  

reference：https://bwit.blog/fix-err_blocked_by_administrator-in-chromium-browsers/  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 1 · updated: 2021-06-24*

I have both a policy for Edge and for Chrome so it is both of them.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-06-24*

Hi，  

Thank you for posting in our forum.  

I want to confirm some information with you in order to better solve the problem  

Is it Microsoft Edge, or Google Chrome?  

Because this is a different solution. You can tell me which one it is first  

Hope this information can help you  

Best wishes  

Vicky
