---
title: "User CSP MDM and Kerberos (updated 2/21/24 21:47CST)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4066777/user-csp-mdm-and-kerberos-updated-2-21-24-21-47cst
question_id: 4066777
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# User CSP MDM and Kerberos (updated 2/21/24 21:47CST)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4066777/user-csp-mdm-and-kerberos-updated-2-21-24-21-47cst (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been subject to "sophisticated" cyber issues since 2022.  There is a reason but I do not fall into the political, a journalist, in the government, etc... yet even Apple has informed me they can do no more.

I have struggled just to get this far reaching community assistance.  

Verizon tells me they do not assist with 'hacking'.  Apple tells me to seek assistance via 3rd Party Security Software. 

It is quite complicated and has been impossible to find assistance.  No one will even confirm that I have always been speaking with any 'real' representative; except when I went to the Apple store.

I have reason to believe and I do feel 100% that my devices have been compromised via MDM and kerberos.  

It is complicated.  

It began with my OneDrive being compromised (due to information in it), leading to my Azure account, Verizon, Amazon, Apple, Google, etc... my entire life.  

I am not here to discuss Azure.  That is now a moderately separate issue that I am working on.

That is all some background information that may be useful.

I have already tried everything I think is possible to someone without professional resources.  

That applies to accounts, multiple devices, operating systems, learning code, networking, software, hardware, and more.  Please just ask me if I have tried "?"

I am a very dedicated learner.

When I create passwords I am even careful about which characters, letters and numbers I start/end with and the way I combine them- just to make it more difficult to 'accidentally' execute in a script.  Yes, that is extreme.  I doubt someone is doing that, but that is an example of how sophisticated and persistent this has been.

I have a voluminous amount of information but I am trying to keep my posts specific.

Recently I found the following in my Windows 10 Home registry:

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Kerberos\AllowForestSearchOrder]  

"admxMetadataDevice"=hex: 

[I am excluding the actual decimal]

"Behavior"=dword:00000060  

"mergealgorithm"=dword:00000003  

"policytype"=dword:00000001  

"RegKeyPathRedirect"="Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters"  

"RegValueNameRedirect"="UseForestSearch"

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Kerberos\KerberosClientSupportsClaimsCompoundArmor]  

"admxMetadataDevice"=hex:

[I am excluding the actual decimal]  

"Behavior"=dword:00000060  

"mergealgorithm"=dword:00000003  

"policytype"=dword:00000001  

"RegKeyPathRedirect"="Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters"  

"RegValueNameRedirect"="EnableCbacAndArmor"

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Kerberos\RequireKerberosArmoring]  

"admxMetadataDevice"=hex:

[I am excluding the actual decimal]  

"Behavior"=dword:00000060  

"mergealgorithm"=dword:00000003  

"policytype"=dword:00000001  

"RegKeyPathRedirect"="Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters"  

"RegValueNameRedirect"="RequireFast"

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Kerberos\RequireStrictKDCValidation]  

"admxMetadataDevice"=hex:

[I am excluding the actual decimal]  

"Behavior"=dword:00000060  

"mergealgorithm"=dword:00000003  

"policytype"=dword:00000001  

"RegKeyPathRedirect"="Software\Microsoft\Windows\CurrentVersion\Policies\System\Kerberos\Parameters"  

"RegValueNameRedirect"="KdcValidation"

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Kerberos\SetMaximumContextTokenSize]  

"admxMetadataDevice"=hex:

[I am excluding the actual decimal]  

"Behavior"=dword:00000060  

"mergealgorithm"=dword:00000003  

"policytype"=dword:00000001  

"RegKeyPathRedirect"="System\CurrentControlSet\Control\Lsa\Kerberos\Parameters"  

"RegValueNameRedirect"="EnableMaxTokenSize"

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Kerberos\UPNNameHints]  

"Behavior"=dword:00000220  

"mergealgorithm"=dword:00000003  

"policytype"=dword:00000001  

"RegKeyPathRedirect"="System\CurrentControlSet\Control\Lsa\Kerberos\Parameters"  

"RegValueNameRedirect"="UPNNameHints"  

"value"=""

I also found:

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Provisioning\ServerConfig\com.vzwdmserver\CustomAlertConfiguration]  

"AlertData"="Y2hlY2tDb25maWd1cmF0aW9u"  

"AlertDataType"=dword:00000006  

"AlertSourceUri"="./Device/CheckConfiguration"  

"AlertType"="org.openmobilealliance.dm.firmwareupdate.userrequest"

Asking for insight is most likely more helpful than trying to learn every single thing on my own.

**I would just at least like to know if the above is something to explore, or is it 'normal'.

I was definitely not involved in creating an "AlertType" via '"userrequest" for \ServerConfig.vzwdmserver\CustomAlertConfiguration

Additionally, if the only feedback I receive from anyone is to seek third party security then I need a job with a third party security team.

I cannot rest

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-20*

Hi, Fire Ant1

```
You're welcome, I just hope you can get the answers you've been looking for from Microsoft Learn.
```

Best Regards   

Martin | Microsoft Community Support Specialist

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-15*

Thank You!

I need to know who and how I can best communicate with.

Due to the situation it has been difficult to be able to communicate.

Many of my waking moments are spent on Microsoft Learn and I love having that resource.  I appreciate your encouragement to reach out and ask questions.

I have the information from your reply.

I only wanted to reply with my gratitude before I delete this post. 

I appreciate your assistance.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-12*

Hi, Fire Ant1

Welcome to the Microsoft Community.  

```
I do understand your security concerns. Based on the registry values you provided, there is no way to prove that the computer was compromised, so I suggest you use Windows Defender or a third-party tool to do a full scan to see if you can find any anomalies. 

For Microsoft accounts, I would suggest that you try using Microsoft Authenticator to secure the account. For registry or security related advice questions, it's more suitable for publishing on Microsoft Learn, you can click on "Ask a question", there are experts who can provide more professional solutions in that place.

Here is a [link](https://learn.microsoft.com/en-us/answers/ "learn.microsoft.com") to the forum where you can raise specific scenarios and share your idea to help solve the problem.

Thank you for your understanding!
```

Best Regards    

Martin | Microsoft Community Support Specialist
