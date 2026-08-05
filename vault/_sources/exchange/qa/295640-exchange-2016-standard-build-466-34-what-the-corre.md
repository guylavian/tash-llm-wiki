---
title: "Exchange 2016 Standard ‎(Build 466.34)‎ | What the correct way to deal with an expired certificate (Self signed)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/295640/exchange-2016-standard-build-466-34-what-the-corre
question_id: 295640
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Standard ‎(Build 466.34)‎ | What the correct way to deal with an expired certificate (Self signed)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/295640/exchange-2016-standard-build-466-34-what-the-corre (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

We are running an Exchange 2016 Standard server (Version 15.1 ‎(Build 466.34)‎).    

The following Self-Signed Certificate recently expired:  

Microsoft Exchange Server Auth Certificate  

Self-signed certificate  

Issuer: CN=Microsoft Exchange Server Auth Certificate  

Status  

Invalid  

Expires on: 2/25/2021  

Expires on:Renew  

Assigned to services  

SMTP  

We do have a separate, valid cert that handles IIS & SMTP:  

Microsoft Exchange  

Self-signed certificate  

Issuer: CN=RBS-MAIL  

Status  

Valid  

Expires on: 8/16/2021  

Expires on:Renew  

Assigned to services  

IIS, SMTP  

What is the appropriate action to take?  Should it simply be renewed?    

There is currently no impact, but I want to ensure I do this correctly.  

Thanks in advance.  

Regards,  

Rudy

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-03-02*

Hi.  

yes renew both and its easy :)   

For the first: Microsoft Exchange Server Auth Certificate  

https://supertechman.com.au/how-to-renew-an-expired-microsoft-exchange-server-auth-certificate/  

for the "Microsoft Exchange" cert, follow the steps on my blog:  

https://ehloergosum.com/2020/01/25/renewing-that-pesky-microsoft-exchange-certificate/

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-18*

Hi @Rudolf Amarlapudi  ，    

Before we go on, would you please verify if this is still a self-signed certificate as stated earlier in your original post? As from the screenshot you shared above, it seems to me that it's more likely to be a certificated issued by certification authority(From the Issuer field in the second image). You can run the command below and check the value of the IsSelfSigned field:    

```
Get-Exchangecertificate DEE4C09E56600048BA9606E15B7F25F159C8CECA | fl
```

If you have confirmed that it's a self-signed cert (IsSelfSigned: True), please refer to the steps in the link below to renew the certificate:    

Renew an Exchange self-signed certificate    

If it's not a self-signed cert, you would need to create a certificate renewal request, and then send the request to the CA. The CA then sends you the actual certificate file that you need to install on the Exchange server.     

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-03*

Hi @Rudolf Amarlapudi  ,

From your description, now you only need to renew the expired "Microsoft Exchange Server Auth Certificate". You can follow the first link shared by Andy for the renew procedure or refer to the steps below which are virtually identical:

1.Click the Renew button in EAC.  

2.Double click the "Microsoft Exchange Server Auth Certificate", go to the General tab, scroll down and find the new thumbprint, take a note of it for later commands.  

3. Put the required information for the next command into variable:

(replace the "NewCertificateThumbprint" with the thumbprint in step2 )

```
$thumb = "NewCertificateThumbprint"  
$date = get-date
```

4.Run the command below to add the new certificate:

```
Set-AuthConfig -NewCertificateThumbprint $thumb -NewCertificateEffectiveDate $date
```

You will get a warning that the new effective date is not 48 hours in the future, but we're OK with that so you can just ignore it.

5.Publish the certificate to all servers using the following command:

```
Set-AuthConfig -PublishCertificate
```

6.Then you can remove the old expired certificate from the configuration:

```
Set-AuthConfig -ClearPreviousCertificate
```

7.Run an IISReset for the change to take effect.

Here's one more link for your reference:  

Expired Microsoft Exchange Server Auth Certificate  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
