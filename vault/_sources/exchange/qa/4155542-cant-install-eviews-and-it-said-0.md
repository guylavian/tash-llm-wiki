---
title: "Can't install eviews and it said 0*80040702"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4155542/cant-install-eviews-and-it-said-0*80040702
question_id: 4155542
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 10
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Can't install eviews and it said 0*80040702

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4155542/cant-install-eviews-and-it-said-0*80040702 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Everytime when I opened the install program, it will load like it's run normally, but then, it will give me two error alert. And I can ensure that the install program is complete because I download it for many times both in Official website and another websites. And their MD5 are same. I tried nearly all the eviews edition, but they all have this problem. 

 

One is: 

one or more installer files are missing! Unable to proceed with install. 

 

And another is:  

Error number: 0*80040702 

Description: Failed to load DLL: install 

Setup will be terminate

And I will see that:

## Answer (community) — Independent Advisor

*upvotes: 1 · updated: 2023-05-15*

Hi,

I'm Sumit, here to answer your query at the Microsoft Community.

as an HRESULT: Severity: FAILURE (1), FACILITY_ITF (0x4), Code 0x702

for hex 0x702 / decimal 1794

  ERROR_REDIRECTOR_HAS_OPEN_HANDLES                              winerror.h

The redirector is in use and cannot be unloaded.

2 matches found for "80040702"

Try  installing in a clean boot state which should hopefully work.

Press the Windows key + R to open the Run dialog box.

Type “msconfig” (without quotes) and press Enter.

In the System Configuration window, select the Services tab.

Check the box next to “Hide all Microsoft services”. Ensure you do it carefully, and not disable all Microsoft services.

Click on “Disable all”.

Select the Startup tab and click on “Open Task Manager”.

In the Task Manager window, select each startup item and click on “Disable”.

Close Task Manager and click on OK in the System Configuration window.

Restart your computer.

Hope that helps, and rely on us for any further inquiries. All the best.
