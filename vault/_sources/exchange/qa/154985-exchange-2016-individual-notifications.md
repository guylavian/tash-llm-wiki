---
title: "Exchange 2016 Individual Notifications"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/154985/exchange-2016-individual-notifications
question_id: 154985
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2016 Individual Notifications

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/154985/exchange-2016-individual-notifications (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

When blocking mobile devices, individual notifications regarding the blocking are sent to the administrator and the user of the new mobile device. How can I customize these notifications?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-10*

First of all, many thanks for the data protection notice. Therefore ichg had already changed all entries on firma.de But I can also enter contoso.com.    

Here are the settings, which unfortunately are not used:

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Sorry, but the text stored there is unfortunately not the text that arrives at the administrator. Here is an example of such a mail, from which I don't know where it comes from:    

Von: Microsoft Outlook    

Gesendet: Donnerstag, 29. Oktober 2020 16:42:02 (UTC+01:00) Amsterdam, Berlin, Bern, Rom, Stockholm, Wien    

An: Kxx, Mxx; Administrator    

Betreff: Das Gerät von Fxx, Pxx (pfrisch) wurde isoliert. Die Synchronisierung mit dem Server über Exchange ActiveSync ist erst wieder möglich, wenn Sie entsprechende Maßnahmen ergriffen haben.    

Der Exchange ActiveSync-Dienst hat das unten aufgeführte Mobiltelefon in Quarantäne verschoben. Die Synchronisierung von Exchange-Inhalten ist erst möglich, wenn Sie entsprechende Maßnahmen ergriffen haben.    

Um eine Aktion für das mobile Gerät auszuführen, wechseln Sie zur folgenden Seite im Exchange Admin Center: https://active.contoso.com/ecp/UsersGroups/EditMobileMailbox.aspx?id=7b861443-e692-470c-8896-04757173ee51&dtm=Isolation    

Informationen zum Gerät, das diesen Hinweis ausgelöst hat:     

Benutzer: pxx@Company portal   .com    

Gerätemodell: iPhone11C2    

Gerätetyp: iPhone    

Geräte-ID: 3IEK5DBJEL4AF295R1944R75S8    

Gerätebetriebssystem: iOS 14.1 18A8395    

Gerätebenutzer-Agent: Apple-iPhone11C2/1801.8395    

Telefonnummer des Geräts:    

Geräte-IMEI:    

Exchange ActiveSync-Version: 16.1    

Angewendete Geräterichtlinie: Default    

Geräterichtlinienstatus: AppliedInFull    

Gerätezugriffsstatus: Quarantined    

Grund für Gerätezugriffsstatus: DeviceRule    

Steuerungsregel für Gerätezugriff: iPhone (DeviceType)    

Um 29.10.2020 16:42:02 an mxx@Company portal   .com,Administrator@Company portal   .com, gesendet.    

First and foremost it is about removing the email address mxx@Company portal   .com because the admin has died!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-09*

Hi @Horst Graner | c-3  ,    

When blocking mobile devices, individual notifications regarding the blocking are sent to the administrator and the user of the new mobile device. How can I customize these notifications?    

As regards to the notifications sent to the administrator, I am afraid it is NOT feasible to customize the text.    

But the notifications sent to users can be customized using the steps shared by Andy, that is, click the Edit button, and you can enter the text you want to include in the message sent to users:    

    

This can also be modified using the powershell script like below:    

```
Set-ActiveSyncOrganizationSettings -UserMailInsert "Your mobile device has been quarantined. Please contact the Help Desk for further assistance."
```

Reference: Set-ActiveSyncOrganizationSettings    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-11-07*

In EAC, go to Mobile and then on the far right, there is an EDIT button. Click on that and scroll down
