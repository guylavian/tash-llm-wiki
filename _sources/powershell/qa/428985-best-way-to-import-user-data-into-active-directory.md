---
title: "Best way to import user data into Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/428985/best-way-to-import-user-data-into-active-directory
question_id: 428985
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
---
# Best way to import user data into Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/428985/best-way-to-import-user-data-into-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm tasked with getting user data into AD and updating existing users in AD with changes.  

The user data itself can be pulled from a SQL query, perhaps periodically/repeatedly.  

Trouble is there's a management perception that I must write code (C#, .Net) that does this, perhaps some console app that gets runs once a day or something.  

But as I read about AD it seems nobody does this, they write powershell scripts etc  

So is this really a job for the Infrastructure team and not the Development team?  

I'm a very experienced .Net developer but very little experience or knowledge of AD or ADFS, which brings me to my next question, but I'll hold off on that for now.  

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Hi,

Thanks for your patience!

Based on your description, I agree with what you two have discussed in this blog and I think adopting PowerShell script should be a right choice. And based on your missions, I think a customized script should be more appropriate, while writing customized scripts isout of Microsoft's scope. In this case, I may suggest you to look for scripts in Github.com. Besides, you can keep this nlog open to the public, so that people who experienced a similar issue with yours can get to help you.

Thanks for your understanding and support! And I would appreciate it if you could help me Accept Answer to support my work. When you Accept Answer, your blog will be automatically put on top of our forum, letting others who have a similar issue with yours to get to your blog more quickly.

Have a nice day! : )

BR,  

Joan

If the Answer is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-10*

Oh, I'd definitely advocate using PowerShell as the language of choice for something like this.  

Does "upsert" mean "update and\or insert"? I haven't heard that term before. :-)  

-  "Regularly": use a scheduled task  

-  "Urgently": HR knows when they onboard someone. The database should have the information. I'd say "see #1". Name changes should fall within this scope. If they're in the database and not in the AD then they should be added to the AD.  

-  I haven't used ADFS since I retire seven years ago. I can't count myself as any kind of authority on that product. However, other data can be kept in the AD, either in an existing property, an existing property designed to hold ad hoc data (e.g. extension attributes), of you can extend the AD schema for customized (and appropriately named and constrained data) use within your organization.  

The only exception I see to #1 would be the CEO insisting his nephew be given a corporate identity and privileges immediately. How often does that happen?  

I used to work in a mid-sized multi-national company. They had a multi-domain forest, tens of thousands of employees. Layers of management that never seemed to communicate very well, etc. I've written the program you're asking about (in Perl) and dealt with the problems.  

Whatever the outcome, make sure the people that you work for, and the people above them, etc. all agree on the what and how and who. It won't be any different to any other project, but it may adversely affect the operation of the company if things go awry because the AD is central to an awful lot of stuff that's buried in software.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

Also articles like this seem to say the same thing.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

@Rich Matheisen       

Hello Rich,    

Forgot to mention, this is all currently on prem.    

Interesting questions, the Dev team primarily work in C# and JavaScript with a smattering of legacy VB for some older ASP.NET stuff and of course we write SQL often.    

The Inf team I know less about, they certainly don't work with any of the above languages, they do not use Visual Studio and they do write PowerShell scripts I think.    

We - Dev - Maintain code that we author, it becomes our responsibility once released, this includes bug fixing, enhancements etc.    

There are three broad problems at the root of the work assigned to me:    

-  Be able to regularly (daily, twice daily, whatever) upsert user data that currently sits inside our database into AD.    

-  (Less urgently, phase 2 so to speak), be able to upsert a user in a more real-time manner - if a user's name for example gets changed, have AD updated right away or as close to.    

-  Start to upsert additional user data with a view to having our ADFS provide richer information in the form of claims data.    

My brief research and your reply, seem to tell me that this (with the exception of 2.) does not require the design, development and testing of a new console app or Windows Service to actually do the upsert, it seems that power shell scripts can be written or tools like MIM etc leveraged to do this out of the box.    

Writing a .Net app that does this strikes me as a bad idea because the detail we'd need to write the code requires a sound understanding of the .Net libraries for AD and testing this becomes complex because it involves both Dev and Inf to closely work together and could lead to bugs etc that impact the overall quality of the AD system.    

I cannot see any reason for anyone to write .Net code to do this, AD already has most of our users in it already, these get into the system in various ways and writing code to do that would mean we have to write code that mirrors these other ways, Dev currently play no role in getting user info into AD and once we start to do that we have a whole new area of risk.    

Let me know if you share this view, I want to reach out later to a few people and state that this is my advice based on research and experts that I have discussed it with, because I hardly know anything about AD or ADFS I cannot state an opinion until I've dug down like this.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-09*

Does it make a difference to the development team what language they code in?  

Does the Infrastructure team write any other code (or code of any complexity)?  

Who's going to maintain the code that goes into production?  

You can run PowerShell scripts from the PowerShell shell, of you can run it as a scheduled task with no input from a human (which is probably what is required).
