---
title: "Set Firefox default browser by gpo for citrix session"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/791635/set-firefox-default-browser-by-gpo-for-citrix-sess
question_id: 791635
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Set Firefox default browser by gpo for citrix session

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/791635/set-firefox-default-browser-by-gpo-for-citrix-sess (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

HI all,  

I tried to set up the firefox default browser using gpo. I achived it to all devices using Computer Configuration > Policies > Administrative Template > Windows Components > File Explorer and xml file however it doesnt work for user who use citrix sessnion.  

Please advise.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-05*

Hi @Anonymous       

Please try the following:    

The Group Policy Management console lets you create and manage Group Policy Objects (GPO) for your domain. These GPOs control the policies that are applied to all your domain-linked computers. After you create the GPO, you use security filtering to apply it to the computers in your domain.    

In the following example, you create a GPO (Set Firefox as default browser) and apply it to computers in the firefoxforwork.com domain.    

Open the Group Policy Management Console. Go to Start > All programs > Administrative Tools > Group Policy Management.    

In the navigation pane, go to Group Policy Management > Domains.    

In the navigation pane, right-click on the firefoxforwork.com domain, and click Create a GPO in this domain, and Link it here...    

Type the name of the new GPO (in our example, the name is Set Firefox as default browser) and click OK.    

In the navigation pane, go to Group Policy Management > Domains > firefoxforwork.com > Group Policy Objects and select Set Firefox as default browser.    

In the Security Filtering pane, click Add.    

In the Select User, Computer, or Group window, type the name of the object you want to add, click Check Names (to verify the name you entered), and click OK. You can type Domain Computers to add all workstations and servers joined to this domain (as in the example below) or you can specify a different group of computers.    

The GPO now applies to all domain-linked computers.    

-------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-04-04*

to clarify situation. It looks like this. I'm logged on the server where this gpo is applied and gpo is working correctly, the citrix session is run when I open the folder and it direct me to file server. Where I open any file from file server (via this citrix session )with html or htm extenssion it ask me what browser do I want to use despite its set up by gpo. On file server there is no gpo applied.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2022-03-29*

Hi,  

Check if the GPO linked to the correct OU.  

You can also check on the GPO report applied on Citrix session to verify which GPO settings and filters are already applied:  

```
gpresult /H  C:\temp\gpresult.html
```

Please don't forget to mark helpful reply as answer
