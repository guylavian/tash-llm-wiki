---
title: "Deployed Printers via GPO or script are not installing on windows 7"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2736859/deployed-printers-via-gpo-or-script-are-not-instal
question_id: 2736859
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 15
qa_tags: []
---
# Deployed Printers via GPO or script are not installing on windows 7

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2736859/deployed-printers-via-gpo-or-script-are-not-instal (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So let me first say this is NOT a point and print disable fix.  Just needed to get that out of the way - I already had point and print disabled as well as enabled with the FQDN of my print servers listed and both prompts suppressed.  

We are deploying printers in our environment via group policy - we have a mixture of windows 7 pro and windows 10 clients.

I need to state right off the bat that windows 10 clients have no problem getting the printers.

The issue I'm having has to do with the driver installation.  The computers and users being assigned the printer policies get the policy and I see in the application log that the printers could not be installed due to lack of driver.  As I know this is NOT
 the case because we can manually install the printers of course and I have both x86 and 64bit printer drivers on the servers.

Our domain level is at 2008 R2 - but all 3 domain controllers are 2012 R2 - we just upgraded our last 2008 R2 server and haven't done enough testing to upgrade the domain level to 2012 R2.

We had no issues with printers up until recently.  Yes, KB3170455 is installed on the windows 7 computers - but again I have a computer policy (that is being applied) to disable point and print.  I have also tried, as I stated earlier, modifying that same
 policy to enable point and print as well as add in the FQDN of my print servers and supressing the prompts.  

Going back to the client's application event log I see the following error: - Group Policy object did not apply because it failed with error code '0x80070bcb The specified printer driver was not found on the system and needs to be downloaded.' This error
 was suppressed.

I need to stress, again, because I've read everywhere that disabling point and print is the workaround for this - but it's not!  And again, these policies work great on windows 10.  

I have spent days on this issue, I've found nobody that has had this issue - where the driver just won't install so I'm here begging for some help.  And any help is greatly appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2016-09-01*

This question is outside the scope of this site (for consumers) and to be sure you get the best answer it should be asked either on Technet (for IT Pro's) or MSDN (for developers)

http://social.technet.microsoft.com/Forums/en-us/home s/en-US/home

http://social.msdn.microsoft.com/Forum

If you give us a link to the new thread we can point some resources to it
