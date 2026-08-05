---
title: "Microsoft Exchange Wide Mail Signature"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1572890/microsoft-exchange-wide-mail-signature
question_id: 1572890
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange Wide Mail Signature

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1572890/microsoft-exchange-wide-mail-signature (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,
I am trying to create a wide email signature for my organization. We use Microsoft 365 Online and i am trying to set it up from Exchange admin center>Mail Flow >Rules and i created a signature rule which works however the dynamic attributes such as Display Name, Job title, Phone number and description are not working.
I a using the following attributes on my inline html:   

Here is my html signature code:

```

 
                
                    
                
                
                 %{displayname}%
                    

                    %{title}%                     
%{mobile}%%{mail}%

  www.apeirondata.com
                    
                    

  
                      
                            
                        
                    
```

Here is how it displays:
Am i doing it anything wrong?
Thanks.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2024-02-23*

Your formatting seems off, those variables should be enclosed in double %% and no brackets. See https://learn.microsoft.com/en-us/exchange/security-and-compliance/mail-flow-rules/disclaimers-signatures-footers-or-headers#use-the-new-eac-to-add-a-disclaimer-or-other-email-header-or-footer

```
%%DisplayName%%
```

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-28*

Like Vasil already mentioned, placeholders are off.
The easiest way to get this done is use an email signature generator - this one is free to use and can automatically create a signature's HTML code with the right placeholders included. All you have to do is paste it to a mail flow rule.
