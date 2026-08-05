---
title: "IT manager looking for Recommended gpo for school org"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2193287/it-manager-looking-for-recommended-gpo-for-school
question_id: 2193287
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-deploy-group-policy-objects"]
---
# IT manager looking for Recommended gpo for school org

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2193287/it-manager-looking-for-recommended-gpo-for-school (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hey all   

im working as it manager in school   

and i wanna make adjustment and changes here   

we have two types of users here   

pupil ( students )  

teachers   

pupil have the most gpo here   

-  folder redirecting softwares icons from our server  

which making issue beacuse it can take till 30 seconds till dhcp give ip to computer so if the student log to desktop before that   

he wont see icons at all , and he will need to restart his computer  

-  there is a gpo that block windows search bar ( im looking for this gpo but couldnt find it yet , some thing a college did 9 years ago )  

and this gpo with the issue from the folder redirection making it a nightmare   

-  student user only have 1 option of ssid wifi to connect to so they will get their shared folders   

-  shared printer   

-  they cant download stuff , dont have admin privilage   

with those main gpo , ill be glad to get suggestion for gpo to add to adjust / remove from our org   

like i said my main issue are the folder redirect , search bar block , and there is shared printer gpo , but its not like they add new printer using \domainname and add the printer , they still need admin privialge    

thank you

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-23*

Hello Computers1,  

Thank you for your reply.  

You can right click the GPO called pupil2 and select "Save Report".  

Them open the saved report to check if there is any setting related to search function.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-22*

Hello Computers1,  

Thank you for posting in Microsoft Community forum.  

*- folder redirecting softwares icons from our serverwhich making issue beacuse it can take till 30 seconds till dhcp give ip to computer so if the student log to desktop before that he wont see icons at all , and he will need to restart his computer.*A: Did you mean every time student sign in these machines need dhcp give ip? if so, you can assign static IP address to these machines.  

  - ya pretty much , this are laptop computer for student only , the problem with giving them static ip is that we have about 300 computers here for students , so it will be problemtic   - there is a gpo that block windows search bar ( im looking for this gpo but couldnt find it yet , some thing a college did 9 years ago )and this gpo with the issue from the folder redirection making it a nightmare

A: You can try to export the gpresult for different users and compare the result.  

-  i know the problem lay in gpo called pupil2   

the issue is that i coudlnt find any settings that there look like its block the search bar   

i repalyed to your quote question

## Answer (community) — community member

*upvotes: 0 · updated: 2023-11-21*

Hello Computers1,  

Thank you for posting in Microsoft Community forum.  

*- folder redirecting softwares icons from our serverwhich making issue beacuse it can take till 30 seconds till dhcp give ip to computer so if the student log to desktop before that he wont see icons at all , and he will need to restart his computer.*A: Did you mean every time student sign in these machines need dhcp give ip? if so, you can assign static IP address to these machines.  - there is a gpo that block windows search bar ( im looking for this gpo but couldnt find it yet , some thing a college did 9 years ago )and this gpo with the issue from the folder redirection making it a nightmare

A: You can try to export the gpresult for different users and compare the result.  

Sign in the working user.  

For checking User Configurations within gpresult, we can follow steps below.

Logon the machine using normal domain user account.

Create a folder named F1.

Open CMD (do not run as Administrator).

Type gpresult /h C:\F1\gpo.html and click Enter.

Open gpo.html and check gpo setting under "User Details".  

Sign in the non-working user.  

For checking User Configurations within gpresult, we can follow steps below.

Logon the machine using normal domain user account.

Create a folder named F2.

Open CMD (do not run as Administrator).

Type gpresult /h C:\F2\gpo.html and click Enter.

Open gpo.html and check gpo setting under "User Details".

  - they cant download stuff , dont have admin privilage 

A: You can try to share the stuff to the students.

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
