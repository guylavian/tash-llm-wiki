---
title: "Windows Server 2019 Standard - Active Directory Domain Services"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/490998/windows-server-2019-standard-active-directory-doma
question_id: 490998
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Windows Server 2019 Standard - Active Directory Domain Services

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/490998/windows-server-2019-standard-active-directory-doma (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Installed Active Directory Domain Service on Windows Server 2019 Standard and ran into a problem.  

After installation, when I open network and internet settings through the Settings application, then I click change card options, I get the following message:  

Error: Windows cannot access the specified device, path or file. You may not have the appropriate permission to access the item.  

The error points to the path C:\Windows\system32\control.exe and I cannot access the settings of the network adapters from the Settings item. However, when I want to run the Control Panel outside of Settings, it turns on normally.  

I also get the same error when in Settings I enter Time and language in the Language submenu for the path C:\Windows\system32\ SystemSettingsAdminFlows.exe, and this application does not start at all, because it is only in the settings and it is not in Control panel. I checked the same error in several other Settings.  

To be sure, I did a double AD installation to rule out other factors. My question is, should it be that this service deactivates these settings for me or is there a bug causing me this?   

Zainstalowałem usługę domeny Active Directory w Windows Server 2019 Standard i natrafiłem na problem.  

Po instalacji, kiedy otwieram ustawienia sieci i Internetu przez aplikację Ustawienia, później klikam zmień opcje karty otrzymuję poniższy komunikat:  

Błąd: System Windows nie może uzyskać dostępu do określonego urządzenia, ścieżki lub pliku. Możesz nie dysponować odpowiednimi zezwoleniami na uzyskanie dostępu do elementu.  

Błąd wskazuje na ścieżkę C:\Windows\system32\control.exe i z pozycji Ustawień nie mogę przejść do ustawień kart sieciowych. Natomiast kiedy chcę uruchomić Panel sterowania poza Ustawieniami to się normalnie włącza.  

Ten sam błąd otrzymuję również kiedy w Ustawieniach wejdę w Czas i język w podmenu Język dla ścieżki C:\Windows\system32\SystemSettingsAdminFlows.exe, no i tej aplikacji nie idzie uruchomić w ogóle, gdyż jest tylko w ustawieniach a nie ma jej w Panelu sterowania. Sprawdzałem jeszcze w kilku innych Ustawieniach ten sam błąd.  

Dla pewności przeprowadziłem dwukrotną instalację usługi AD, aby wykluczyć inne czynniki. Moje pytanie brzmi, czy tak powinno być, że ta usługa dezaktywuje mi te ustawienia, czy w czymś tkwi błąd, który mi to powoduje?

## Answer (community) — community member [Mvp]

*upvotes: 2 · updated: 2021-07-27*

My question is, should it be that this service deactivates these settings for me or is there a bug causing me this?  

No, not normal, something sounds broken. Existing domain or new domain? Make sure to patch fully before adding roles.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 1 · updated: 2021-07-27*

New or existing domain? Might also try adjusting UAC down.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 1 · updated: 2021-07-27*

No problem before installation and after uninstalling AD DS, all updates are ready. I did this on the new DELL R540 server with the operating system installed. I reinstalled it, but the situation happened again. I remove AD DS the problem disappears.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-07-27*

As @Anonymous    said, it's not normal.  Do you have the same issue before installing ADDS role ?    

Does the installation is a fresh install of from a Windows image ?
