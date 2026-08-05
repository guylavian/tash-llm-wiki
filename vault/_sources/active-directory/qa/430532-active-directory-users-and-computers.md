---
title: "Active Directory Users and Computers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/430532/active-directory-users-and-computers
question_id: 430532
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Users and Computers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/430532/active-directory-users-and-computers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I just installed additional DC on Windows Server 2012 to replicate with the first DC, but  when I open Active Directory Users and Computers on the newly installed DC, unfortunately t shows 1st domain controller users, computers, distribution groups etc. (Active Directory Users and Computers [DC1.abc.local)  

While it should show its own users, computers, distribution groups etc. (Active Directory Users and Computers [DC2.abc.local)  

Any possible solution plz.  

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-21*

Hi,  

Just checking in to see if the information provided was helpful.   

Please let us know if you would like further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-16*

Hi，  

Thank you for waiting and replying  

Run the following commands to see if there are any errors  

Dcdiag /v >c:\dcdiag1.log  

Repadmin /showrepl >C:\repl.txt  

Repadmin /showreps *  

You can check whether there is a problem with the new DC. If there is an error, share the screenshot with us. Don’t put all the logs up. We don’t support analyzing these logs.  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-11*

Hi,  

Thank you for posting in our forum.  

So where is the problem now? Has the problem with the domain controller been resolved?  

What kind of help do I need?  

Best wishes  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-10*

Hi @Yousuf Shahzad  ,    

Have you made sure that your Active Directory Users and Computers (ADUC) is connected to your "local server", that is your DC2.abc.local?    

You can try changing your Domain Controller in the ADUC console as shown in the screenshot below:    

    

----------    

(If the reply was helpful please don't forget to upvote and/or accept as answer, thank you)    

Best regards,    

Leon
