---
title: "Renew ssl certificate Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/357365/renew-ssl-certificate-exchange-2013
question_id: 357365
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Renew ssl certificate Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/357365/renew-ssl-certificate-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Recently we renewed our ssl certificate from Sectigo on two hybrid exchange server 2013 servers, all went well then had to open a ticket with Microsoft due to breaking EAC and not getting the ssl to be recognized. We followed the below steps but then MS had us Bind the ssl to 'Default web site' as well as binding the "Microsoft Exchange" ssl to the 'Exchange backend' in IIS. I'm just seeing if anyone has a step by step that goes throughout the entire process instead of just relying on EAC console.

How to Renew SSL Certificate for 2013 Step by Step

1) Creating a new CSR (Certificate signing request)  

Open EAC or Exchange Admin Center Web page.  

Navigate to Servers section.  

Click on Certificates Option.  

Select Server Name.  

Click on Certificate you need to renew.  

Click on Renew option.  

Save the new CSR request to your desired UNC path.  

Submit the CSR request to generate a new certificate with your 3rd party Certificate vendor.  

Download the new certificate.

2) Installing new certificate  

Open EAC or Exchange Admin Center Web page.  

Navigate to Servers section.  

Click on Certificates Option.  

Select Server Name.  

Now Select Certificate with status "Pending Request".  

Right-hand side, click on the complete option.  

Now enter the UNC path for new downloaded Certificate.

3) Assign New Certificate to Services like IIS, SMTP, IMAP or POP  

Open EAC or Exchange Admin Center Web page.  

Navigate to Servers section.  

Click on Certificates Option.  

Select Server Name.  

Select the new certificate.  

Click on Edit Icon.  

Click on Services option.  

Click on the Services checkbox you want to assign and save.  

Certificate renew completed for the single server.

Note: If you have more than one Exchange server. Move to Step 4.

4) Exporting Certificate from First Exchange Server in the same Org.  

Export certificate from the server you first renewed or installed.  

Open EAC or Exchange Admin Center Web page.  

Navigate to Servers section.  

Click on Certificates Option.  

Select First Server Name.  

Select the new certificate you want to export.  

Click on “…” or more icon and select Export Exchange Certificate.  

Enter the UNC path, where you want to export the new certificate.  

Provide the password and follow rest of the steps.

5) Importing Certificate on Other Exchange Servers in the same Org.  

Open EAC or Exchange Admin Center Web page.  

Navigate to the Servers section.  

Click on the Certificates Option.  

Click on “…” or more icon.  

Click Import Exchange Certificate  

Enter the UNC path for the exported certificate you did in step 4 above.  

Enter the password you gave in step 4 above.  

Now click on "+" icon and add your other Exchange 2013 servers.  

Follow Wizard and finish the import process.

6) Assign Services on other Exchange servers.

No where does it state you have to bind your ssl in iis on each exchange node. Then run these commands from Exchange powershell mgmt:  

$newcertificate=get-Exchangecertificate -Thumbprint "yournewsslthumbprint"  

Set-ReceiveConnector "Servername\Default Frontend Servername" -TlsCertificateName "<I>$($newcertificate.Issuer)<S>$($newcertificate.Subject)"

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-15*

Hi @Crod   ,    

What's your means that "it doesn't bind the cert"?    

According to the steps you provided, these are the correct procedures for renew the certificate in Exchange.    

After we renew the certificate in Exchange server, the certificate bound in the default site and the back end site in IIS may change. The steps provided by Microsoft are correct, we could manually change the binding certificate in IIS. Bind the SSL certificate you requested to "Default web site" and the "Microsoft Exchange" self-signed certificate to Exchange Back End site.    

In addition, there are two related articles that may help you: Renew a Certificate in Exchange and Import & Export SSL Certificates in Exchange Server 2016, you need to import the new certificate to the remaining servers except the first server.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

Yep and we did that but what gets me is it doesn't bind the cert. So if you have an article that goes over this additional process that would be most helpful.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-04-14*

Step 5 is all about importing the certificate from first exchange server to the remaining servers.
