---
title: "basic Send As permission not work  Exchange 2019 :-((("
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2242315/basic-send-as-permission-not-work-exchange-2019
question_id: 2242315
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# basic Send As permission not work  Exchange 2019 :-(((

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2242315/basic-send-as-permission-not-work-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I need your help to an issue from à basic fonction, but after one week to work on this, I don't find why a Send As permission not work. (yes one week!)  

In Exchange server 2019 (Hybrid but mailboxes concerned are on premise) I added an user (called "Toto" to understand) who have on premise mailbox, Send As permission to another user on premise mailbox (called Snoopy for the fun too.).  

In Exchange management console, the Send As permission is well allowed for toto in the Snoopy delegation property mailbox.  

But from OWA and Outlook legacy, the Send As not work (permission denied)  

I deleted global address list from cache, redownloaded it, Snoopy show well in the address book,...  

I checked Send As permission in AD object, checked with Powershell and Exchange Shell....  

But still not work after one week.  

I don't know what happen and I 'm pretty lost.  

Thanks you very much for your help

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-04-08*

Hi KG.  

Thanks you for your answer.  

-  Bellow the error returned.  

-  Also the result of Get-ADPermission,  

-  Add-recipientPermission not included from Exchange2019. (onlu used to Exchange online)

Objet :     test send as ju with adress book downloaded

      Date : 26/03/2025 11:34

 

Impossible de contacter le(s) destinataire(s) suivant(s) :

 

      ******@contoso.com le 26/03/2025 11:34

            Nous n’avons pas pu envoyer ce message. Vous n'avez pas l'autorisation d'envoyer le message sous le nom de l'utilisateur spécifié.

 

 

Informations de diagnostic pour les administrateurs :

 

L’erreur est [0x80070005-0x000004dc-0x00000524].

 

En-têtes de réponse d’Exchange :

      request-id : 3cd0ff3f-f4f9-4306-87ae-550047e7a601

      X-ServerApplication : Exchange/15.02.1544.014

      X-FEServer : EXCHserver

      X-BEServer : EXCHserver

      X-CalculatedBETarget : EXCHserver.contoso.com

      X-RequestId : {9BC2656B-C044-458C-919C-F5565797ACC1}:216

      X-ClientInfo : {D34ECDC2-C39C-4B84-B087-89D489611568}:213240021

      X-ElapsedTime : 34

      X-ResponseCode : 0

      X-DiagInfo : EXCHserver

      X-RequestType : Execute

 

Récapitulatif des opérations distantes :

 

      0 : ropSetProps (10) Traitée (1) Terminée (0)

            Résultat de l’opération distante : 0

            Codes de réponse : 0

      1 : ropSetProps (10) Traitée (1) Terminée (0)

            Résultat de l’opération distante : 0

            Codes de réponse : 0

      2 : ropFlushRecipients (14) Traitée (1) Terminée (0)

            Résultat de l’opération distante : 0

            Codes de réponse : 0

      3 : ropSetProps (10) Traitée (1) Terminée (0)

            Résultat de l’opération distante : 0

            Codes de réponse : 0

      4 : ropTransportSend (74) Traitée (1) Terminée (0)

            Résultat de l’opération distante : 0

            Codes de réponse : 1244

 

Exceptions dans la réponse :

 

Index d’opération distante : 4

Associé à l’opération distante : ropTransportSend (74)

Microsoft.Exchange.Data.Storage.SendAsDeniedException: Can't transport send message. ---> Microsoft.Mapi.MapiExceptionSendAsDenied: MapiExceptionSendAsDenied: Unable to transport send message. (hr=0x80070005, ec=1244)

Diagnostic context:

    ......

    Lid: 52176   ClientVersion: 15.2.1544.14

    Lid: 50032   ServerVersion: 15.2.1544.6014

    Lid: 35180 

    Lid: 23226   --- ROP Parse Start ---

    Lid: 27962   ROP: ropDeletePropsNoReplicate [122]

    Lid: 27962   ROP: ropSetProps [10]

    Lid: 27962   ROP: ropFlushRecipients [14]

    Lid: 31418   --- ROP Parse Done ---

    Lid: 55847   EMSMDBPOOL.EcPoolSessionDoRpc called [length=204]

    Lid: 43559   EMSMDBPOOL.EcPoolSessionDoRpc returned [ec=0x0][length=400][latency=0]

    Lid: 52176   ClientVersion: 15.2.1544.14

    Lid: 50032   ServerVersion: 15.2.1544.6014

    Lid: 35180 

    Lid: 23226   --- ROP Parse Start ---

    Lid: 27962   ROP: ropSetProps [10]

    Lid: 27962   ROP: ropTransportSend [74]

    Lid: 17082   ROP Error: 0x4DC    

    Lid: 44949 

    Lid: 21921   StoreEc: 0x4DC    

    Lid: 27962   ROP: ropExtendedError [250]

    Lid: 1494    ---- Remote Context Beg ----

    Lid: 37692 

    Lid: 44092 

    Lid: 41232 

    Lid: 60208 

    Lid: 37136 

    Lid: 34608 

    Lid: 55056 

    Lid: 42768 

    Lid: 56112 

    Lid: 52807 

    Lid: 33016   StoreEc: 0x4DC    

    Lid: 40748   qdwParam: 0xB01000000000001

    Lid: 57132   qdwParam: 0x0              

    Lid: 63016   dwParam: 0x4A

    Lid: 39640   StoreEc: 0x4DC    

    Lid: 45434   Guid: ffcdc076-d676-48f5-bde6-b91f3b96fc21

    Lid: 10786   dwParam: 0x0        Msg: 15.02.1544.014:EXCHserver:b146b0b3-78ea-4447-aada-76ba3d40e4a9

    Lid: 1750    ---- Remote Context End ----

    Lid: 31418   --- ROP Parse Done ---

    Lid: 22753 

    Lid: 21817   ROP Failure: 0x4DC    

    Lid: 59285 

    Lid: 46997   StoreEc: 0x4DC    

   at Microsoft.Mapi.MapiExceptionHelper.InternalThrowIfErrorOrWarning(String message, Int32 hresult, Boolean allowWarnings, Int32 ec, DiagnosticContext diagCtx, Exception innerException)

   at Microsoft.Mapi.MapiExceptionHelper.ThrowIfError(String message, Int32 hresult, IExInterface iUnknown, Exception innerException)

   at Microsoft.Mapi.MapiMessage.TransportSendMessage(PropValue[]& propsToReturn)

   at Microsoft.Exchange.Data.Storage.MapiAccessor.TransportSendMessage(MapiMessage mapiMessage, PropValue[]& mapiPropValues)

   --- End of inner exception stack trace ---

   at Microsoft.Exchange.Data.Storage.MapiAccessor.TransportSendMessage(MapiMessage mapiMessage, PropValue[]& mapiPropValues)

   at Microsoft.Exchange.Data.Storage.CoreItem.TransportSend(PropertyDefinition[]& propertyDefinitions, Object[]& propertyValues)

   at Microsoft.Exchange.RpcClientAccess.Handler.Message.TransportSend()

   at Microsoft.Exchange.RpcClientAccess.Handler.RopHandler.<>c__DisplayClass153_0.<TransportSend>b__0()

   at Microsoft.Exchange.RpcClientAccess.Handler.ExceptionTranslator.TryExecuteCatchAndTranslateExceptions[TResult]

 

 

Échec de Transport-Send : échec de l’énumération(25), HResult(0x00000000), EC(1244).

Échec de Transport-Send : échec de l’énumération(22), HResult(0x00000000), EC(1244).

Échec de Submit-Message : ID de message(5), échec d’énumération(13), HResult(0x80070005), EC(1244).

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-04-01*

Hi @Darkmoutch，

Thank you for posting your question in the Microsoft Q&A forum.

Based on your description, you are experiencing an issue where user Toto is unable to send emails as Snoopy via OWA/Outlook in an Exchange 2019 Hybrid environment, despite having the “Send As” permission configured.

In order to pinpoint the root cause of the issue, I would like to understand the following key information:

-  Can you provide a complete error message or screenshot of the failed “Send As” attempt? This will help us identify the exact type of error.

-  Have you tried assigning the same permission to another user? Did you get the same error? This test will help determine if the problem is user-specific or a global configuration issue.

Based on the information available, the following troubleshooting steps are recommended: 

-  I don't know if you have used the following commands to check permissions. If not, you can try the following commands, paying special attention to whether the output contains the SendAs permission item.

Get-ADPermission -Identity "Snoopy" -User "Toto" | Format-List Deny,ExtendedRights

-  Although you are using EAC to add user permissions, it is recommended that you use the following command to add them:

Add-RecipientPermission -Identity "Snoopy" -Trustee "Toto" -AccessRights SendAs

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.
