---
title: "Screensaver and Hibernate / Shutdown GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/691514/screensaver-and-hibernate-shutdown-gpo
question_id: 691514
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
---
# Screensaver and Hibernate / Shutdown GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/691514/screensaver-and-hibernate-shutdown-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have one GPO that sets the Screensaver at 5 minutes along with locking the laptops.    

We're trying to setup another GPP which hibernates the laptop after, let's say, idle session for 3 hours.     

When I set the hibernate to anything more than 5 minutes, it does not takes effect. But when I set it to less than or equal to 5 minutes, it works, and the laptop hibernates when left idle for 5 minutes.    

Will the playing of screensaver remove the idleness of the laptop to let it hibernate / shutdown?    

Much appreciated.    

This is the policy for screensaver.    

    

and this is the policy for hibernate

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-13*

Hi there,    

Before jumping to troubleshooting the GPO you can try disabling and re-enabling the hibernation. Once this is done try charging the GPO for 180 minutes and see if this is applied successfully.    

-At the command prompt, type powercfg.exe /hibernate off and then press Enter.    

-Type exit, and then press Enter to close the Command Prompt window.    

-At the command prompt, type powercfg.exe /hibernate on, and then press Enter.    

-Type exit, and then press Enter to close the Command Prompt window.    

How to disable and re-enable hibernation on a computer that is running Windows    

https://learn.microsoft.com/en-US/troubleshoot/windows-client/deployment/disable-and-re-enable-hibernation    

Here is a thread as well which discusses the same issue and you can try out some troubleshooting steps from this and see if that helps you to sort the Issue.    

https://social.technet.microsoft.com/Forums/Lync/en-US/ca376a19-7b4e-4e2b-8996-1885234f7c0f/after-exactly-3-hours-in-sleep-laptop-shutsdown-or-hibernates?forum=w8itprogeneral    

---------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
