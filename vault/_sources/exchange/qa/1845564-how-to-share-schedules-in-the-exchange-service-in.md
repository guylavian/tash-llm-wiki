---
title: "How to share schedules in the exchange service in the XML mode?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1845564/how-to-share-schedules-in-the-exchange-service-in
question_id: 1845564
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to share schedules in the exchange service in the XML mode?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1845564/how-to-share-schedules-in-the-exchange-service-in (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

How to share schedules in the exchange service in the XML mode?We tried the updateFolder method, but the error says that an internal server error has occurred. Operation failed.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-30*

Hi @two mows,

Welcome to the Microsoft Q&A platform!

There can be multiple steps and methods involved when sharing a plan in an exchange service in XML mode. Based on the information you provided, an internal server error was encountered using the `updateFolder` method, which could be due to various reasons. Here are some possible solutions and checkpoints:

-  Ensure that the account used to invoke the `updateFolder` method has sufficient privileges to perform the operation. Try using an administrator account to perform the operation.

-  Ensure that the XML structure sent is correct and conforms to the specification. An incorrect XML structure may cause the server to fail to parse the request correctly.

-  Check the log files of the Exchange Services server for more detailed error messages. These logs usually contain more debugging information to help locate the problem.

-  Ensure that the incoming paths and parameters are correct. For example, verify that the folder path exists, that the destination folder is correct, and so on.

-  Sometimes it is useful to try other similar methods or interfaces to see if they accomplish the same task. For example, try the `createFolder` method to create a folder, and then use the `getFolder` and `setFolderPermissions` methods to change the permissions.

Assuming you are using Exchange Web Services (EWS) to share a calendar folder, here is a complete example showing how to share a specific calendar folder and assign permissions.

```
                 ******@archermind.com  false false false true false None None FullDetails Reviewer           
```

In this example:

-  FolderId: Replace with the ID of your destination folder.

-  PrimarySmtpAddress: Replaced with the SMTP address of the user you need to share the folder with.

-  other fields like `CanCreateItems`, `CanCreateSubFolders`, `IsFolderOwner`, etc. are configured according to your needs.

Please feel free to contact me if you have any queries.

Best,

Jake Zhang

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-29*

```

     
       
     
     
       
         
           
             
             
               
                 
                 
                   
                     
                       
                         
                           ******@archermind.com
                         
                         false
                         false
                         false
                         true
                         false
                         None
                         None
                         FullDetails
                         Reviewer
                       
                     
                   
                 
               
             
           
         
       
     
   
```
