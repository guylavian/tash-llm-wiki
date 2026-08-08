---
title: "Skype for Business 2019 - Exchange server 2016 Integration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/168377/skype-for-business-2019-exchange-server-2016-integ
question_id: 168377
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-skype-business-platform-windows", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Skype for Business 2019 - Exchange server 2016 Integration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/168377/skype-for-business-2019-exchange-server-2016-integ (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

While attempting to integrate a Skype For Business Server 2019 with an Exchange Server 2016, I am receiving the following error message :

The command I entered is:  

New-CsPartnerApplication -Identity Exchange -ApplicationTrustLevel Full -MetadataUrl "https://autodiscover.mydomain.com/autodiscover/metadata/json/1"

Error:  

New-CsPartnerApplication : Cannot bind parameter 'MetadatUrl' to the target. Exception setting "MetadataUrl": "The metadata document could not be downloaded from the URL in the MetadataUrl parameter or downloaded data is not a valid metadata document, error: The underlying connection was closed: Could not establish trust relationship for the SSL/TLS secure channel."  

-  ... MetadataUrl "https://autodiscover.mydomain.com/autodiscover/metadata/jso ...  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : WriteError: (:) [New-CsPartnerApplication], ParameterBindingException  

-  FullyQualifiedErrorId : ParameterBindingFailed,Microsoft.Rtc.Management.Internal.NewPartnerApplicationCmdlet

The following error is displayed in skype for business management shell

Kindly help us to solve the issue

Regards,  

Navinkumar S

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-11-20*

@Navin Kumar  ,    

It seems to be a certificate issue on the Exchange server. Try to delete the old certificate and then restart IIS. For more details, please read Kismet’s reply in this link.    

Besides, Jeff Schertz’s blog also gives detailed steps for integration between Exchange and Skype for business. You can refer to this link: https://blog.schertz.name/2015/09/exchange-and-skype-for-business-integration/.     

Note: Microsoft is providing this information as a convenience to you. The sites are not controlled by Microsoft. Microsoft cannot make any representations regarding the quality, safety, or suitability of any software or information found there. Please make sure that you completely understand the risk before retrieving any suggestions from the above link.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
