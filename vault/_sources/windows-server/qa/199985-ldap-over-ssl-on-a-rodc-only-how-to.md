---
title: "LDAP over SSL on a RODC only (how to)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/199985/ldap-over-ssl-on-a-rodc-only-how-to
question_id: 199985
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# LDAP over SSL on a RODC only (how to)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/199985/ldap-over-ssl-on-a-rodc-only-how-to (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

I have a "basic" question.   

Customer has 2x RODC in a separated environment, which is direct connected to the On_Prem domain controllers (all 2016)  

Firewall ports are configured and open.  

The RODC setup was done without any issues.  

Now he wants to enable only on these 2 RODCs LDAP over SSL.  

I have searched for an document, where the setup is described, but I didn't find anything matching the environment. Except, when I install the CA direct on the DCs itself (then it seems, that LDAP/S is active immediately)  

But here the CA is separated somewhere in the On-Premise network.  

How do I request / install an certificate to enable LDAP/S? And which certificate template?  

Like this article here?  

https://www.miniorange.com/guide-to-setup-ldaps-on-windows-server  

Would be great, if someone could kick me into the correct direction  

Best,  

Lutz

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-28*

Its again me  

It is working now  

The problem was the RODC....he doenst want to replicate  

Reverse DNS settings  

no he can...I can see the template, use it, export the cert and bind it to the AD service  

Best,  

Lutz

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-28*

Hello @Lutz Rahe  ,    

Thank you for your update.    

Would you please check the permissions under the Security tab of this certificate you mentioned?    

Check if you have given the Domain Controllers group read and enroll permission.    

    

If so, after I checked, you can give the RODC account Read and Enroll permissions explicitly.    

Because Domain Controllers group has no RODC in it by default.    

    

If anything is unclear, please feel free to let us know.    

Best Regards,    

Daisy Zhou

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-28*

Hi Daisy  

Just a short question  

To try - I have setup a small environment with a DC, a rootCA and a RODC in a different subnet  

I have made a new certificate template (based on the Kerberos Template) in my CA, and said "publish in Active Directory). After that I said new certificate template to issue......so I can see my new template in the CA console  

But when I'm trying to request this from my RODC, I only can see the "standard" templates (Directory Email, Domain Controller, Domain Controller Authentication, Kerberos Authentication), but not my new template  

I have restarted the DC, the CA, the RODC.....nothing. Waiting now for more than 1h  

???????  

Best  

Lutz  

btw: When I am requestiong a certificate from my DC, then I can see the new template. From my RODC I cannot  

Now Im totally confsed....both I have logged in with the same account

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-16*

Hi Daisy  

Thank you for your answer.  

I hve just checked the links, the 2.nd I already have seen. But not used, cause here the CA was installed on the DC itself.  

This scenario is not matching.  

The 1st one looks interesting. I will go through it. When I have questions, I will let you know (and if its working, Ill mark your answer as working solution  

Best,  

Lutz
