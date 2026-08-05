---
title: "Exchange Server — pages 2401-2440"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2401-2440
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2401-2440
family: exchange
documentKind: "doc"
abstract: "A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters: The function Func_credit_card finds content that matches the pattern. The checksum passes. <!-- Credit Card Number --> <Entity id=\"50842eb7-edc8-4019-85d"
---

# Exchange Server — pages 2401-2440

<!-- p.2401 -->

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

        The function Func_credit_card finds content that matches the pattern.

        The checksum passes.

  <!-- Credit Card Number -->
  <Entity id="50842eb7-edc8-4019-85dd-5a5c1f2bb085" patternsProximity="300" recommendedConfidence="85">
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_credit_card" />
          <Any minMatches="1">
            <Match idRef="Keyword_cc_verification" />
            <Match idRef="Keyword_cc_name" />
            <Match idRef="Func_expiration_date" />
          </Any>
    </Pattern>
    <Pattern confidenceLevel="65">
          <IdMatch idRef="Func_credit_card" />
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_cc_verification                                                                 Keyword_cc_name

 card verification                                                                       amex
 card identification number                                                              american express
 cvn                                                                                     americanexpress
 cid                                                                                     Visa
 cvc2                                                                                    mastercard
 cvv2                                                                                    master card
 pin block                                                                               mc
 security code                                                                           mastercards
 security number                                                                         master cards
 security no                                                                             diner's Club
 issue number                                                                            diners club
 issue no                                                                                dinersclub
 cryptogramme                                                                            discover card
 numéro de sécurité                                                                      discovercard
 numero de securite                                                                      discover cards
 kreditkartenprüfnummer                                                                  JCB
 kreditkartenprufnummer                                                                  japanese card bureau
 prüfziffer                                                                              carte blanche
 prufziffer                                                                              carteblanche
 sicherheits Kode                                                                        credit card
 sicherheitscode                                                                         cc#
 sicherheitsnummer                                                                       cc#:
 verfalldatum                                                                            expiration date
 codice di verifica                                                                      exp date
 cod. sicurezza                                                                          expiry date
 cod sicurezza                                                                           date d'expiration
 n autorizzazione                                                                        date d'exp
 código                                                                                  date expiration
 codigo                                                                                  bank card
 cod. seg                                                                                bankcard
 cod seg                                                                                 card number
 código de segurança                                                                     card num
 codigo de seguranca                                                                     cardnumber
 codigo de segurança                                                                     cardnumbers
 código de seguranca                                                                     card numbers
 cód. segurança                                                                          creditcard
 cod. seguranca cod. segurança                                                           credit cards
 cód. seguranca                                                                          creditcards
 cód segurança                                                                           ccn
 cod seguranca cod segurança                                                             card holder
 cód seguranca                                                                           cardholder
 número de verificação                                                                   card holders
 numero de verificacao                                                                   cardholders
 ablauf                                                                                  check card
 gültig bis                                                                              checkcard

<!-- p.2402 -->

Keyword_cc_verification   Keyword_cc_name

gültigkeitsdatum          check cards
gultig bis                checkcards
gultigkeitsdatum          debit card
scadenza                  debitcard
data scad                 debit cards
fecha de expiracion       debitcards
fecha de venc             atm card
vencimiento               atmcard
válido hasta              atm cards
valido hasta              atmcards
vto                       enroute
data de expiração         en route
data de expiracao         card type
data em que expira        carte bancaire
validade                  carte de crédit
valor                     carte de credit
vencimento                numéro de carte
Venc                      numero de carte
                          nº de la carte
                          nº de carte
                          kreditkarte
                          karte
                          karteninhaber
                          karteninhabers
                          kreditkarteninhaber
                          kreditkarteninstitut
                          kreditkartentyp
                          eigentümername
                          kartennr
                          kartennummer
                          kreditkartennummer
                          kreditkarten-nummer
                          carta di credito
                          carta credito
                          n. carta
                          n carta
                          nr. carta
                          nr carta
                          numero carta
                          numero della carta
                          numero di carta
                          tarjeta credito
                          tarjeta de credito
                          tarjeta crédito
                          tarjeta de crédito
                          tarjeta de atm
                          tarjeta atm
                          tarjeta debito
                          tarjeta de debito
                          tarjeta débito
                          tarjeta de débito
                          nº de tarjeta
                          no. de tarjeta
                          no de tarjeta
                          numero de tarjeta
                          número de tarjeta
                          tarjeta no
                          tarjetahabiente
                          cartão de crédito
                          cartão de credito
                          cartao de crédito
                          cartao de credito
                          cartão de débito
                          cartao de débito
                          cartão de debito
                          cartao de debito
                          débito automático
                          debito automatico
                          número do cartão
                          numero do cartão
                          número do cartao
                          numero do cartao
                          número de cartão

<!-- p.2403 -->

 Keyword_cc_verification                                                                 Keyword_cc_name

                                                                                         numero de cartão
                                                                                         número de cartao
                                                                                         numero de cartao
                                                                                         nº do cartão
                                                                                         nº do cartao
                                                                                         nº. do cartão
                                                                                         no do cartão
                                                                                         no do cartao
                                                                                         no. do cartão
                                                                                         no. do cartao

Croatia Identity Card Number
Format: Nine digits

Pattern: Nine consecutive digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_croatia_id_card finds content that matches the pattern.

     A keyword from Keyword_croatia_id_card is found.

  <!--Croatia Identity Card Number-->
  <Entity id="ff12f884-c20a-4189-b185-34c8e7258d47" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_croatia_id_card"/>
       <Match idRef="Keyword_croatia_id_card"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_croatia_id_card

 Croatian identity card
 Osobna iskaznica

Croatia Personal Identification (OIB) Number
Format: 10 digits

Pattern: 10 digits:

     Six digits in the form DDMMYY, which are the date of birth

     Four digits where the final digit is a check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_croatia_oib_number finds content that matches the pattern.

     A keyword from Keyword_croatia_oib_number is found.

     The checksum passes.

<!-- p.2404 -->

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The function Func_croatia_oib_number finds content that matches the pattern.

       The checksum passes.

  <!-- Croatia Personal Identification (OIB) Number -->
  <Entity id="31983b6d-db95-4eb2-a630-b44bd091968d" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_croatia_oib_number"/>
       <Match idRef="Keyword_croatia_oib_number"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_croatia_oib_number"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_croatia_oib_number

 Personal Identification Number
 Osobni identifikacijski broj
 OIB

Czech National Identity Card Number
Format: 10 digits containing a forward slash

Pattern: 10 digits:

       Six digits that are the date of birth

       A forward slash

       Four digits where the final digit is a check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The function Func_czech_id_card finds content that matches the pattern.

       A keyword from Keyword_czech_id_card is found.

       The checksum passes.

  <!-- Czech National Identity Card Number -->
  <Entity id="60c0725a-4eb6-455b-9dda-05d8a7396497" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_czech_id_card"/>
       <Match idRef="Keyword_czech_id_card"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_czech_id_card

 Czech national identity card
 Občanský průka

<!-- p.2405 -->

Denmark Personal Identification Number
Format: 10 digits containing a hyphen

Pattern: 10 digits:

     Six digits in the format DDMMYY, which are the date of birth

     A hyphen

     Four digits where the final digit is a check digit

Checksum: Yes

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_denmark_id finds content that matches the pattern.

     A keyword from Keyword_denmark_id is found.

     The checksum passes.

  <!-- Denmark Personal Identification Number -->
  <Entity id="6c4f2fef-56e1-4c00-8093-88d7a01cf460" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Regex_denmark_id"/>
       <Match idRef="Keyword_denmark_id"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_denmark_id

 Personal Identification Number
 CPR
 Det Centrale Personregister
 Personnummer

Drug Enforcement Agency (DEA) Number
Format: Two letters followed by seven digits

Pattern: Pattern must include all of the following:

     One letter (not case sensitive) from this set of possible letters: abcdefghjklmnprstux, which is a registrant code

     One letter (not case sensitive), which is the first letter of the registrant's last name

     Seven digits, the last of which is the check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_dea_number finds content that matches the pattern.

     The checksum passes.

  <!-- DEA Number -->
  <Entity id="9a5445ad-406e-43eb-8bd7-cac17ab6d0e4" recommendedConfidence="85" patternsProximity="300">

<!-- p.2406 -->

    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_dea_number"/>
    </Pattern>
  </Entity>

Keywords: None

EU Debit Card Number
Format: 16 digits

Pattern: Very complex and robust pattern

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The function Func_eu_debit_card finds content that matches the pattern.

       At least one of the following is true:

          A keyword from Keyword_eu_debit_card is found.

          A keyword from Keyword_card_terms_dict is found.

          A keyword from Keyword_card_security_terms_dict is found.

          A keyword from Keyword_card_expiration_terms_dict is found.

          The function Func_eu_date1 finds a date in the right date format.

          The function Func_eu_date2 finds a date in the right date format.

       The checksum passes.

  <!-- EU Debit Card Number -->
  <Entity id="0e9b3178-9678-47dd-a509-37222ca96b42" patternsProximity="300" recommendedConfidence="85">
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_eu_debit_card" />
          <Any minMatches="1">
            <Match idRef="Keyword_eu_debit_card" />
            <Match idRef="Keyword_card_terms_dict" />
            <Match idRef="Keyword_card_security_terms_dict" />
            <Match idRef="Keyword_card_expiration_terms_dict" />
            <Match idRef="Func_expiration_date" />
            <Match idRef="Func_eu_date" />
            <Match idRef="Func_eu_date1" />
            <Match idRef="Func_eu_date2" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                     ﾉ   Expand table

 Keyword_eu_debit_card           Keyword_card_terms_dict        Keyword_card_security_terms_dict           Keyword_card_expiration_terms_dict

 account number                  acct nbr                       card identification number                 ablauf
 card number                     acct num                       card verification                          data de expiracao
 card no.                        acct no                        cardi la verifica                          data de expiração
 security number                 american express               cid                                        data del exp
 cc#                             americanexpress                cod seg                                    data di exp
                                 americano espresso             cod seguranca                              data di scadenza
                                 amex                           cod segurança                              data em que expira
                                 atm card                       cod sicurezza                              data scad
                                 atm cards                      cod. seg                                   data scadenza
                                 atm kaart                      cod. seguranca                             date de validité

<!-- p.2407 -->

Keyword_eu_debit_card   Keyword_card_terms_dict   Keyword_card_security_terms_dict   Keyword_card_expiration_terms_dict

                        atmcard                   cod. segurança                     datum afloop
                        atmcards                  cod. sicurezza                     datum van exp
                        atmkaart                  codice di sicurezza                de afloop
                        atmkaarten                codice di verifica                 espira
                        bancontact                codigo                             espira
                        bank card                 codigo de seguranca                exp date
                        bankkaart                 codigo de segurança                exp datum
                        card holder               crittogramma                       expiration
                        card holders              cryptogram                         expire
                        card num                  cryptogramme                       expires
                        card number               cv2                                expiry
                        card numbers              cvc                                fecha de expiracion
                        card type                 cvc2                               fecha de venc
                        cardano numerico          cvn                                gultig bis
                        cardholder                cvv                                gultigkeitsdatum
                        cardholders               cvv2                               gültig bis
                        cardnumber                cód seguranca                      gültigkeitsdatum
                        cardnumbers               cód segurança                      la scadenza
                        carta bianca              cód. seguranca                     scadenza
                        carta credito             cód. segurança                     valable
                        carta di credito          código                             validade
                        cartao de credito         código de seguranca                valido hasta
                        cartao de crédito         código de segurança                valor
                        cartao de debito          de kaart controle                  venc
                        cartao de débito          geeft nr uit                       vencimento
                        carte bancaire            issue no                           vencimiento
                        carte blanche             issue number                       verloopt
                        carte bleue               kaartidentificatienummer           vervaldag
                        carte de credit           kreditkartenprufnummer             vervaldatum
                        carte de crédit           kreditkartenprüfnummer             vto
                        carte di credito          kwestieaantal                      válido hasta
                        carteblanche              no. dell'edizione
                        cartão de credito         no. di sicurezza
                        cartão de crédito         numero de securite
                        cartão de debito          numero de verificacao
                        cartão de débito          numero dell'edizione
                        cb                        numero di identificazione della
                        ccn                       scheda
                        check card                numero di sicurezza
                        check cards               numero van veiligheid
                        checkcard                 numéro de sécurité
                        checkcards                nº autorizzazione
                        chequekaart               número de verificação
                        cirrus                    perno il blocco
                        cirrus-edc-maestro        pin block
                        controlekaart             prufziffer
                        controlekaarten           prüfziffer
                        credit card               security code
                        credit cards              security no
                        creditcard                security number
                        creditcards               sicherheits kode
                        debetkaart                sicherheitscode
                        debetkaarten              sicherheitsnummer
                        debit card                speldblok
                        debit cards               veiligheid nr
                        debitcard                 veiligheidsaantal
                        debitcards                veiligheidscode
                        debito automatico         veiligheidsnummer
                        diners club               verfalldatum
                        dinersclub
                        discover
                        discover card
                        discover cards
                        discovercard
                        discovercards
                        débito automático
                        edc
                        eigentümername
                        european debit card
                        hoofdkaart
                        hoofdkaarten
                        in viaggio
                        japanese card bureau

<!-- p.2408 -->

Keyword_eu_debit_card   Keyword_card_terms_dict   Keyword_card_security_terms_dict   Keyword_card_expiration_terms_dict

                        japanse kaartdienst
                        jcb
                        kaart
                        kaart num
                        kaartaantal
                        kaartaantallen
                        kaarthouder
                        kaarthouders
                        karte
                        karteninhaber
                        karteninhabers
                        kartennr
                        kartennummer
                        kreditkarte
                        kreditkarten-nummer
                        kreditkarteninhaber
                        kreditkarteninstitut
                        kreditkartennummer
                        kreditkartentyp
                        maestro
                        master card
                        master cards
                        mastercard
                        mastercards
                        mc
                        mister cash
                        n carta
                        n. carta
                        no de tarjeta
                        no do cartao
                        no do cartão
                        no. de tarjeta
                        no. do cartao
                        no. do cartão
                        nr carta
                        nr. carta
                        numeri di scheda
                        numero carta
                        numero de cartao
                        numero de carte
                        numero de cartão
                        numero de tarjeta
                        numero della carta
                        numero di carta
                        numero di scheda
                        numero do cartao
                        numero do cartão
                        numéro de carte
                        nº carta
                        nº de carte
                        nº de la carte
                        nº de tarjeta
                        nº do cartao
                        nº do cartão
                        nº. do cartão
                        número de cartao
                        número de cartão
                        número de tarjeta
                        número do cartao
                        scheda dell'assegno
                        scheda dell'atmosfera
                        scheda dell'atmosfera
                        scheda della banca
                        scheda di controllo
                        scheda di debito
                        scheda matrice
                        schede dell'atmosfera
                        schede di controllo
                        schede di debito
                        schede matrici
                        scoprono la scheda
                        scoprono le schede
                        solo

<!-- p.2409 -->

 Keyword_eu_debit_card           Keyword_card_terms_dict           Keyword_card_security_terms_dict        Keyword_card_expiration_terms_dict

                                 supporti di scheda
                                 supporto di scheda
                                 switch
                                 tarjeta atm
                                 tarjeta credito
                                 tarjeta de atm
                                 tarjeta de credito
                                 tarjeta de debito
                                 tarjeta debito
                                 tarjeta no
                                 tarjetahabiente
                                 tipo della scheda
                                 ufficio giapponese della
                                 scheda
                                 v pay
                                 v-pay
                                 visa
                                 visa plus
                                 visa electron
                                 visto
                                 visum
                                 vpay

Finland National ID
Format: Six digits plus a character indicating a century plus three digits plus a check digit

Pattern: Pattern must include all of the following:

     Six digits in the format DDMMYY, which are a date of birth

     Century marker (either '-', '+' or 'a')

     Three-digit personal identification number

     A digit or letter (case insensitive) which is a check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_finnish_national_id finds content that matches the pattern.

     A keyword from Keyword_finnish_national_id is found.

     The checksum passes.

  <!-- Finnish National ID-->
  <Entity id="338FD995-4CB5-4F87-AD35-79BD1DD926C1" patternsProximity="300" recommendedConfidence="85">
    <Pattern confidenceLevel="85">
            <IdMatch idRef="Func_finnish_national_id" />
            <Match idRef="Keyword_finnish_national_id" />
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                     ﾉ   Expand table

 Keyword_finnish_national_id

 Sosiaaliturvatunnus
 SOTU Henkilötunnus HETU
 Personbeteckning
 Personnummer

<!-- p.2410 -->

Finland Passport Number
Format: Combination of nine letters and digits

Pattern: Combination of nine letters and digits:

     Two letters (not case sensitive)

     Seven digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_finland_passport_number finds content that matches the pattern.

     A keyword from Keyword_finland_passport_number is found.

  <!-- Finland Passport Number -->
  <Entity id="d1685ac3-1d3a-40f8-8198-32ef5669c7a5" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Regex_finland_passport_number"/>
       <Match idRef="Keyword_finland_passport_number"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                 ﾉ   Expand table

 Keyword_finland_passport_number

 Passport
 Passi

France Driver's License Number
Format: 12 digits

Pattern: 12 digits with validation to discount similar patterns such as French telephone numbers

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters::

     The function Func_french_drivers_license finds content that matches the pattern.

     At least one of the following is true:

        A keyword from Keyword_french_drivers_license is found.

        The function Func_eu_date finds a date in the right date format.

  <!-- France Driver's License Number -->
  <Entity id="18e55a36-a01b-4b0f-943d-dc10282a1824" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_french_drivers_license" />
          <Any minMatches="1">
            <Match idRef="Keyword_french_drivers_license" />
            <Match idRef="Func_eu_date" />
          </Any>
    </Pattern>
  </Entity>

<!-- p.2411 -->

Keywords:

                                                                                                                                      ﾉ   Expand table

 Keyword_french_drivers_license

 drivers licence
 drivers license
 driving licence
 driving license
 permis de conduire
 licence number
 license number
 licence numbers
 license numbers

France National ID Card (CNI)
Format: 12 digits

Pattern: 12 digits

Checksum: No

Definition:

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters: The regular expression
Regex_france_cni finds content that matches the pattern.

  <!-- France CNI -->
  <Entity id="f741ac74-1bc0-4665-b69b-f0c7f927c0c4" patternsProximity="300" recommendedConfidence="65">
    <Pattern confidenceLevel="65">
          <IdMatch idRef="Regex_france_cni" />
    </Pattern>
  </Entity>

Keywords: None

France Passport Number
Format: Nine digits and letters

Pattern: Nine digits and letters:

     Two digits

     Two letters (not case sensitive)

     Five digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_fr_passport finds content that matches the pattern.

     A keyword from Keyword_passport is found..

  <!-- France Passport Number -->
  <Entity id="3008b884-8c8c-4cd8-a289-99f34fc7ff5d" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_fr_passport" />
          <Match idRef="Keyword_passport" />

<!-- p.2412 -->

    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_passport

 Passport Number
 Passport No
 Passport #
 Passport#
 PassportID
 Passportno
 passport number
 パスポート
 パスポート番号
 パスポートのNum
 パスポート ＃
 Numéro de passeport
 Passeport n °
 Passeport Non
 Passeport #
 Passeport#
 PasseportNon
 Passeportn °

France Social Security Number (INSEE)
Format: 15 digits

Pattern:

Must match one of two patterns:

     13 digits followed by a space followed by two digits, or

     15 consecutive digits

Checksum: Yes

Definition:

A DLP policy is 95% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_french_insee or Func_fr_insee finds content that matches the pattern.

     A keyword from Keyword_fr_insee is found.

     The checksum passes.

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_french_insee or Func_fr_insee finds content that matches the pattern.

     No keyword from Keyword_fr_insee is found.

     The checksum passes.

  <!-- France INSEE -->
  <Entity id="71f62b97-efe0-4aa1-aa49-e14de253619d" patternsProximity="300" recommendedConfidence="85">
    <Pattern confidenceLevel="95">
          <IdMatch idRef="Func_french_insee" />
          <Match idRef="Func_fr_insee" />
          <Any minMatches="1">
            <Match idRef="Keyword_fr_insee" />
          </Any>
    </Pattern>
    <Pattern confidenceLevel="85">

<!-- p.2413 -->

          <IdMatch idRef="Func_french_insee" />
          <Match idRef="Func_fr_insee" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Keyword_fr_insee" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_fr_insee

 insee
 securité sociale
 securite sociale
 national id
 national identification
 numéro d'identité
 no d'identité
 no. d'identité
 numero d'identite
 no d'identite
 no. d'identite
 social security number
 social security code
 social insurance number
 le numéro d'identification nationale
 d'identité nationale
 numéro de sécurité sociale
 le code de la sécurité sociale
 numéro d'assurance sociale
 numéro de sécu
 code sécu

German Driver's License Number
Format: Combination of 11 digits and letters

Pattern: 11 digits and letters (not case sensitive):

     A digit or letter

     Two digits

     Six digits or letters

     A digit

     A digit or letter

Checksum: Yes

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_german_drivers_license finds content that matches the pattern.

     At least one of the following is true:

         A keyword from Keyword_german_drivers_license_number is found.

         A keyword from Keyword_german_drivers_license_collaborative is found.

         A keyword from Keyword_german_drivers_license is found.

     The checksum passes.

<!-- p.2414 -->

  <!-- German Driver's License Number -->
  <Entity id="91da9335-1edb-45b7-a95f-5fe41a16c63c" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_german_drivers_license" />
          <Any minMatches="1">
            <Match idRef="Keyword_german_drivers_license_number" />
            <Match idRef="Keyword_german_drivers_license_collaborative" />
            <Match idRef="Keyword_german_drivers_license" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                         ﾉ   Expand table

 Keyword_german_drivers_license_number        Keyword_german_drivers_license_collaborative       Keyword_german_drivers_license

 Führerschein                                 Nr-Führerschein                                    ausstellungsdatum
 Fuhrerschein                                 Nr-Fuhrerschein                                    ausstellungsort
 Fuehrerschein                                Nr-Fuehrerschein                                   ausstellende behöde
 Führerscheinnummer                           No-Führerschein                                    ausstellende behorde
 Fuhrerscheinnummer                           No-Fuhrerschein                                    ausstellende behoerde
 Fuehrerscheinnummer                          No-Fuehrerschein
 Führerschein-                                N-Führerschein
 Fuhrerschein-                                N-Fuhrerschein
 Fuehrerschein-                               N-Fuehrerschein
 FührerscheinnummerNr                         Nr-Führerschein
 FuhrerscheinnummerNr                         Nr-Fuhrerschein
 FuehrerscheinnummerNr                        Nr-Fuehrerschein
 FührerscheinnummerKlasse                     No-Führerschein
 FuhrerscheinnummerKlasse                     No-Fuhrerschein
 FuehrerscheinnummerKlasse                    No-Fuehrerschein
 Führerschein- Nr                             N-Führerschein
 Fuhrerschein- Nr                             N-Fuhrerschein
 Fuehrerschein- Nr                            N-Fuehrerschein
 Führerschein- Klasse
 Fuhrerschein- Klasse
 Fuehrerschein- Klasse
 FührerscheinnummerNr
 FuhrerscheinnummerNr
 FuehrerscheinnummerNr
 FührerscheinnummerKlasse
 FuhrerscheinnummerKlasse
 FuehrerscheinnummerKlasse
 Führerschein- Nr
 Fuhrerschein- Nr
 Fuehrerschein- Nr
 Führerschein- Klasse
 Fuhrerschein- Klasse
 Fuehrerschein- Klasse
 DL
 DLS
 Driv Lic
 Driv Licen
 Driv License
 Driv Licenses
 Driv Licence
 Driv Licences
 Driv Lic
 Driver Licen
 Driver License
 Driver Licenses
 Driver Licence
 Driver Licences
 Drivers Lic
 Drivers Licen
 Drivers License
 Drivers Licenses
 Drivers Licence
 Drivers Licences
 Driver's Lic
 Driver's Licen
 Driver's License

<!-- p.2415 -->

 Keyword_german_drivers_license_number                Keyword_german_drivers_license_collaborative              Keyword_german_drivers_license

 Driver's Licenses
 Driver's Licence
 Driver's Licences
 Driving Lic
 Driving Licen
 Driving License
 Driving Licenses
 Driving Licence
 Driving Licences

German Identity Card Number
Format:

      Since 1 November 2010: Nine letters and digits

      From 1 April 1987 until 31 October 2010: 10 digits

Pattern:

Since 1 November 2010:

      One letter (not case sensitive)

      Eight digits

From 1 April 1987 until 31 October 2010: 10 digits

Checksum: No

Definition:

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The regular expression Regex_germany_id_card finds content that matches the pattern.

      A keyword from Keyword_germany_id_card is found.

  <!-- Germany Identity Card Number -->
  <Entity id="e577372f-c42e-47a0-9d85-bebed1c237d4" recommendedConfidence="65" patternsProximity="300">
    <Pattern confidenceLevel="65">
       <IdMatch idRef="Regex_germany_id_card"/>
       <Match idRef="Keyword_germany_id_card"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                     ﾉ   Expand table

 Keyword_germany_id_card

 Identity Card
 ID
 Identification
 Personalausweis
 Identifizierungsnummer
 Ausweis
 Identifikation

German Passport Number
Format: 10 digits or letters

Pattern: Pattern must include all of the following:

<!-- p.2416 -->

     First character is a digit or a letter from this set (C, F, G, H, J, K)

     Three digits

     Five digits or letters from this set (C, -H, J-N, P, R, T, V-Z)

     A digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_german_passport finds content that matches the pattern.

     A keyword from any of the five keyword lists is found.

     The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_german_passport_data finds content that matches the pattern.

     A keyword from any of the five keyword lists is found.

     The checksum passes.

  <!-- German Passport Number -->
  <Entity id="2e3da144-d42b-47ed-b123-fbf78604e52c" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_german_passport" />
          <Any minMatches="1">
            <Match idRef="Keyword_german_passport" />
            <Match idRef="Keyword_german_passport_collaborative" />
            <Match idRef="Keyword_german_passport_number" />
            <Match idRef="Keyword_german_passport1" />
            <Match idRef="Keyword_german_passport2" />
          </Any>
    </Pattern>
    <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_german_passport_data" />
          <Any minMatches="1">
            <Match idRef="Keyword_german_passport" />
            <Match idRef="Keyword_german_passport_collaborative" />
            <Match idRef="Keyword_german_passport_number" />
            <Match idRef="Keyword_german_passport1" />
            <Match idRef="Keyword_german_passport2" />
          </Any>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                      ﾉ    Expand table

 Keyword_german_passport       Keyword_german_passport_collaborative           Keyword_german_passport_number   Keyword_german_passport1   Keyword_german_

 reisepass                     geburtsdatum                                    No-Reisepass                     Reisepass-Nr               bnationalit.t
 reisepasse                    ausstellungsdatum                               Nr-Reisepass
 reisepassnummer               ausstellungsort
 passport
 passports

Greece National ID Card
Format: Combination of 7-8 letters and numbers plus a dash

Pattern:

Seven letters and numbers (old format):

<!-- p.2417 -->

     One letter (any letter of the Greek alphabet)

     A dash

     Six digits

Eight letters and numbers (new format):

     Two letters whose uppercase character occurs in both the Greek and Latin alphabets (ABEZHIKMNOPTYX)

     A dash

     Six digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_greece_id_card finds content that matches the pattern.

     A keyword from Keyword_greece_id_card is found.

  <!-- Greece National ID Card -->
  <Entity id="82568215-1da1-46d3-874a-d2294d81b5ac" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Regex_greece_id_card"/>
       <Match idRef="Keyword_greece_id_card"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_greece_id_card

 Greek identity Card
 Tautotita
 Δελτίο αστυνομικής ταυτότητας
 Ταυτότητα

Hong Kong Identity Card (HKID) Number
Format: Combination of 8-9 letters and numbers plus optional parentheses around the final character

Pattern: Combination of 8-9 letters:

     1-2 letters (not case sensitive)

     Six digits

     The final character (any digit or the letter A), which is the check digit and is optionally enclosed in parentheses.

Checksum: Yes

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_hong_kong_id_card finds content that matches the pattern.

     A keyword from Keyword_hong_kong_id_card is found.

     The checksum passes.

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_hong_kong_id_card finds content that matches the pattern.

<!-- p.2418 -->

       The checksum passes.

  <!-- Hong Kong Identity Card (HKID) number -->
  <Entity id="e63c28a7-ad29-4c17-a41a-3d2a0b70fd9c" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_hong_kong_id_card"/>
       <Match idRef="Keyword_hong_kong_id_card"/>
    </Pattern>
    <Pattern confidenceLevel="65">
       <IdMatch idRef="Func_hong_kong_id_card"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_hong_kong_id_card

 Hong Kong Identity Card
 HKID
 ID card
 香港身份證
 香港永久性居民身份證

India Permanent Account Number
Format: 10 letters or digits

Pattern: 10 letters or digits:

       Five letters (not case sensitive)

       Four digits

       A letter, which is an alphabetic check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The regular expression Regex_india_permanent_account_number finds content that matches the pattern.

       A keyword from Keyword_india_permanent_account_number is found.

       The checksum passes.

  <!-- India Permanent Account Number -->
  <Entity id="2602bfee-9bb0-47a5-a7a6-2bf3053e2804" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Regex_india_permanent_account_number"/>
       <Match idRef="Keyword_india_permanent_account_number"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_india_permanent_account_number

 Permanent Account Number
 PAN

<!-- p.2419 -->

India Unique Identification (Aadhaar) Number
Format: 12 digits containing optional spaces or dashes

Pattern: 12 digits:

     Four digits

     An optional space or dash

     Four digits

     An optional space or dash

     The final digit, which is the check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_india_aadhaar finds content that matches the pattern.

     A keyword from Keyword_india_aadhar is found.

     The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_india_aadhaar finds content that matches the pattern.

     The checksum passes.

  <!-- India Unique Identification (Aadhaar) number -->
  <Entity id="1ca46b29-76f5-4f46-9383-cfa15e91048f" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_india_aadhaar"/>
       <Match idRef="Keyword_india_aadhar"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_india_aadhaar"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_india_aadhar

 Aadhar
 Aadhaar
 UID
 आधार

Indonesia Identity Card (KTP) Number
Format: 16 digits containing optional periods

Pattern: 16 digits:

     Two-digit province code

     A period (optional)

     Two-digit regency or city code

     Two-digit subdistrict code

<!-- p.2420 -->

       A period (optional)

       Six digits in the format DDMMYY, which are the date of birth

       A period (optional)

       Four digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The regular expression Regex_indonesia_id_card finds content that matches the pattern.

       A keyword from Keyword_indonesia_id_card is found.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters: The regular expression
Regex_indonesia_id_card finds content that matches the pattern.

   <!-- Indonesia Identity Card (KTP) Number -->
   <Entity id="da68fdb0-f383-4981-8c86-82689d3b7d55" recommendedConfidence="85" patternsProximity="300">
     <Pattern confidenceLevel="85">
        <IdMatch idRef="Regex_indonesia_id_card"/>
        <Match idRef="Keyword_indonesia_id_card"/>
     </Pattern>
     <Pattern confidenceLevel="75">
        <IdMatch idRef="Regex_indonesia_id_card"/>
     </Pattern>
   </Entity>

Keywords:

                                                                                                                                                              ﾉ    Expand table

 Keyword_indonesia_id_card

 KTP
 Kartu Tanda Penduduk
 Nomor Induk Kependudukan

International Banking Account Number (IBAN)
Format: Country code (two letters) plus check digits (two digits) plus bban number (up to 30 characters)

Pattern:

Pattern must include all of the following:

       Two-letter country code

       Two check digits (followed by an optional space)

       1-7 groups of four letters or digits (can be separated by spaces)

       1-3 letters or digits

The format for each country is slightly different. The IBAN sensitive information type covers these 60 countries: ad, ae, al, at, az, ba, be, bg, bh, ch,
cr, cy, cz, de, dk, do, ee, es, fi, fo, fr, gb, ge, gi, gl, gr, hr, hu, ie, il, is, it, kw, kz, lb, li, lt, lu, lv, mc, md, me, mk, mr, mt, mu, nl, no, pl, pt, ro, rs, sa, se, si,
sk, sm, tn, tr, vg

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

       The function Func_iban finds content that matches the pattern.

<!-- p.2421 -->

     The checksum passes.

  <Entity id="e7dc4711-11b7-4cb0-b88b-2c394a771f0e" patternsProximity="300" recommendedConfidence="85">
    <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_iban" />
    </Pattern>
  </Entity>

Keywords: None

IP Address
Format: IPv4 or IPv6 address

Pattern:

     IPv4: Complex pattern that accounts for formatted (periods) and unformatted (no periods) versions of the IPv4 addresses.

     IPv6: Complex pattern that accounts for formatted IPv6 numbers (which include colons).

Checksum: No

Definition:

For IPv4, a DLP policy is 95% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_ipv4_address finds content that matches the pattern.

     A keyword from Keyword_ipaddress is found.

For IPv6, a DLP policy is 95% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_ipv6_address finds content that matches the pattern.

     No keyword from Keyword_ipaddress is found.

For IPv4, a DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_ipv4_address finds content that matches the pattern.

     No keyword from Keyword_ipaddress is found.

For IPv6, a DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_ipv6_address finds content that matches the pattern.

     No keyword from Keyword_ipaddress is found.

  <Entity id="1daa4ad5-e2dd-4ca4-a788-54722c09efb2" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="95">
          <IdMatch idRef="Regex_ipv4_address" />
          <Any minMatches="1">
            <Match idRef="Keyword_ipaddress" />
          </Any>
      </Pattern>
      <Pattern confidenceLevel="95">
          <IdMatch idRef="Regex_ipv6_address" />
          <Any minMatches="1">
            <Match idRef="Keyword_ipaddress" />
          </Any>
      </Pattern>
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_ipv4_address" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Keyword_ipaddress" />
          </Any>
      </Pattern>
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Regex_ipv6_address" />
          <Any minMatches="0" maxMatches="0">

<!-- p.2422 -->

            <Match idRef="Keyword_ipaddress" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_ipaddress

 ip address
 internet protocol
 IP-‫כתובת ה‬

Ireland Personal Public Service (PPS) Number
Format:

     New format (1 January 2013 and later): Seven digits followed by two letters

     Old format (31 December 2012 and earlier): Seven digits followed by 1-2 letters

Pattern:

New format (1 January 2013 and later)

     Seven digits

     A letter (not case sensitive) which is an alphabetic check digit

     The letter "A" or "H" (not case sensitive)

Old format (31 December 2012 and earlier)

     Seven digits

     1-2 letters (not case sensitive)

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_ireland_pps finds content that matches the pattern.

     One of the following is true:

           A keyword from Keyword_ireland_pps is found.

           The function Func_eu_date finds a date in the right date format.

     The checksum passes.

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_ireland_pps finds content that matches the pattern.

     The checksum passes.

  <!-- Ireland Personal Public Service (PPS) Number -->
  <Entity id="1cdb674d-c19a-4fcf-9f4b-7f56cc87345a" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_ireland_pps"/>
       <Any minMatches="1">
    <Match idRef="Keyword_ireland_pps"/>
    <Match idRef="Func_eu_date"/>
       </Any>
    </Pattern>
    <Pattern confidenceLevel="65">

<!-- p.2423 -->

       <IdMatch idRef="Func_ireland_pps"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_ireland_pps

 Personal Public Service Number
 PPS Number
 PPS Num
 PPS No.
 PPS #
 PPS#
 PPSN
 Public Services Card
 Uimhir Phearsanta Seirbhíse Poiblí
 Uimh. PSP
 PSP

Israel Bank Account Number
Format: 13 digits

Pattern:

Formatted:

     Two digits

     A dash

     Three digits

     A dash

     Eight digits

Unformatted: 13 consecutive digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_israel_bank_account_number finds content that matches the pattern.

     A keyword from Keyword_israel_bank_account_number is found.

  <!-- Israel Bank Account Number -->
  <Entity id="7d08b2ff-a0b9-437f-957c-aeddbf9b2b25" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_israel_bank_account_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_israel_bank_account_number" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

<!-- p.2424 -->

 Keyword_israel_bank_account_number

 Bank Account Number
 Bank Account
 Account Number
 ‫מספר חשבון בנק‬

Israel National ID
Format: Nine digits

Pattern: Nine consecutive digits

Checksum: Yes

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_israeli_national_id_number finds content that matches the pattern.

     A keyword from Keyword_Israel_National_ID is found.

     The checksum passes.

  <!-- Israel National ID Number -->
  <Entity id="e05881f5-1db1-418c-89aa-a3ac5c5277ee" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_israeli_national_id_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_Israel_National_ID" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_Israel_National_ID

 ‫מספר זהות‬
 National ID Number

Italy Driver's License Number
Format: A combination of 10 letters and digits

Pattern: A combination of 10 letters and digits:

     One letter (not case sensitive)

     The letter "A" or "V" (not case sensitive)

     Seven letters (not case sensitive), digits, or the underscore character

     One letter (not case sensitive)

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_italy_drivers_license_number finds content that matches the pattern.

     A keyword from Keyword_italy_drivers_license_number is found.

<!-- p.2425 -->

  <!-- Italy Driver's license Number -->
  <Entity id="97d6244f-9157-41bd-8e0c-9d669a5c4d71" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_italy_drivers_license_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_italy_drivers_license_number" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_italy_drivers_license_number

 numero di patente di guida
 patente di guida

Japan Bank Account Number
Format: Seven or eight digits

Pattern:

Bank account number: Seven or eight digits

Bank account branch code:

     Four digits

     A space or dash (optional)

     Three digits

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_jp_bank_account finds content that matches the pattern.

     A keyword from Keyword_jp_bank_account is found.

     One of the following is true:

           The function Func_jp_bank_account_branch_code finds content that matches the pattern.

           A keyword from Keyword_jp_bank_branch_code is found.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_jp_bank_account finds content that matches the pattern.

     A keyword from Keyword_jp_bank_account is found.

  <!-- Japan Bank Account Number -->
  <Entity id="d354f95b-96ee-4b80-80bc-4377312b55bc" patternsProximity="300" recommendedConfidence="75">
    <Version minEngineVersion="15.01.0131.000">
      <Pattern confidenceLevel="85">
            <IdMatch idRef="Func_jp_bank_account" />
            <Match idRef="Keyword_jp_bank_account" />
            <Any minMatches="1">
              <Match idRef="Func_jp_bank_account_branch_code" />
              <Match idRef="Keyword_jp_bank_branch_code" />
            </Any>
        </Pattern>
    </Version>

<!-- p.2426 -->

       <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_jp_bank_account" />
          <Match idRef="Keyword_jp_bank_account" />
      </Pattern>
  </Entity>

Keywords:

                                                                                    ﾉ   Expand table

 Keyword_jp_bank_account                              Keyword_jp_bank_branch_code

 Checking Account Number                              Otemachi
 Checking Account
 Checking Account #
 Checking Acct Number
 Checking Acct #
 Checking Acct No.
 Checking Account No.
 Bank Account Number
 Bank Account
 Bank Account #
 Bank Acct Number
 Bank Acct #
 Bank Acct No.
 Bank Account No.
 Savings Account Number
 Savings Account
 Savings Account #
 Savings Acct Number
 Savings Acct #
 Savings Acct No.
 Savings Account No.
 Debit Account Number
 Debit Account
 Debit Account #
 Debit Acct Number
 Debit Acct #
 Debit Acct No.
 Debit Account No.
 口座番号を当座預金口座の確認
 ＃アカウントの確認、勘定番号の確認
 ＃勘定の確認
 勘定番号の確認
 口座番号の確認
 銀行口座番号
 銀行口座
 銀行口座＃
 銀行の勘定番号
 銀行のacct＃
 銀行の勘定いいえ
 銀行口座番号
 普通預金口座番号
 預金口座
 貯蓄口座＃
 貯蓄勘定の数
 貯蓄勘定＃
 貯蓄勘定番号
 普通預金口座番号
 引き落とし口座番号
 口座番号
 口座番号＃
 デビットのacct番号
 デビット勘定＃
 デビットACCTの番号
 デビット口座番号

Japan Driver's License Number
Format: 12 digits

Pattern: 12 consecutive digits

<!-- p.2427 -->

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_jp_drivers_license_number finds content that matches the pattern.

      A keyword from Keyword_jp_drivers_license_number is found.

  <!-- Japan Driver's License Number -->
  <Entity id="c6011143-d087-451c-8313-7f6d4aed2270" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_jp_drivers_license_number" />
          <Match idRef ="Keyword_jp_drivers_license_number" />
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_jp_drivers_license_number

 driver license
 drivers license
 driver's license
 drivers licenses
 driver's licenses
 driver licenses
 dl#
 dls#
 lic#
 lics#
 運転免許証
 運転免許
 免許証
 免許
 運転免許証番号
 運転免許番号
 免許証番号
 免許番号
 運転免許証ナンバー
 運転免許ナンバー
 免許証ナンバー
 運転免許証No.
 運転免許No.
 免許証No.
 免許No.
 運転免許証#
 運転免許#
 免許証#
 免許#

Japan Passport Number
Format: Two letters followed by seven digits

Pattern: Two letters (not case sensitive) followed by seven digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_jp_passport finds content that matches the pattern.

      A keyword from Keyword_jp_passport is found.

<!-- p.2428 -->

  <!-- Japan Passport Number -->
  <Entity id="75177310-1a09-4613-bf6d-833aae3743f8" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_jp_passport" />
          <Match idRef="Keyword_jp_passport" />
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_jp_passport

 パスポート
 パスポート番号
 パスポートのNum
 パスポート＃

Japan Resident Registration Number
Format: 11 digits

Pattern: 11 consecutive digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_jp_resident_registration_number finds content that matches the pattern.

     A keyword from Keyword_jp_resident_registration_number is found.

  <!-- Japan Resident Registration Number -->
  <Entity id="01c1209b-6389-4faf-a5f8-3f7e13899652" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_jp_resident_registration_number" />
          <Match idRef ="Keyword_jp_resident_registration_number" />
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_jp_resident_registration_number

 Resident Registration Number
 Resident Register Number
 Residents Basic Registry Number
 Resident Registration No.
 Resident Register No.
 Residents Basic Registry No.
 Basic Resident Register No.
 住民登録番号、登録番号をレジデント
 住民基本登録番号、登録番号
 住民基本レジストリ番号を常駐
 登録番号を常駐住民基本台帳登録番号

Japan Social Insurance Number (SIN)
Format: 7-12 digits

<!-- p.2429 -->

Pattern: 7-12 digits:

     Four digits

     A hyphen (optional)

     Six digits

     OR

     7-12 consecutive digits

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_jp_sin finds content that matches the pattern.

     A keyword from Keyword_jp_sin is found.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_jp_sin_pre_1997 finds content that matches the pattern.

     A keyword from Keyword_jp_sin is found.

  <!-- Japan Social Insurance Number -->
  <Entity id="c840e719-0896-45bb-84fd-1ed5c95e45ff" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_jp_sin" />
          <Match idRef="Keyword_jp_sin" />
      </Pattern>
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_jp_sin_pre_1997" />
          <Match idRef="Keyword_jp_sin" />
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_jp_sin

 Social Insurance No.
 Social Insurance Num
 Social Insurance Number
 社会保険のテンキー
 社会保険番号

Malaysia ID Card Number
Format: 12 digits containing optional hyphens

Pattern: 12 digits:

     Six digits in the format YYMMDD, which are the date of birth

     A dash (optional)

     Two-letter place-of-birth code

     A dash (optional)

     Three random digits

     One-digit gender code

<!-- p.2430 -->

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_malaysia_id_card_number finds content that matches the pattern.

     A keyword from Keyword_malaysia_id_card_number is found.

  <!-- Malaysia ID Card Number -->
  </Entity>
        <Entity id="7f0e921c-9677-435b-aba2-bb8f1013c749" patternsProximity="300" recommendedConfidence="85">
          <Pattern confidenceLevel="85">
              <IdMatch idRef="Regex_malaysia_id_card_number" />
              <Match idRef="Keyword_malaysia_id_card_number" />
          </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_malaysia_id_card_number

 MyKad
 Identity Card
 ID Card
 Identification Card
 Digital Application Card
 Kad Akuan Diri
 Kad Aplikasi Digital

Netherlands Citizen's Service (BSN) Number
Format: 8-9 digits containing optional spaces

Pattern: 8-9 digits:

     Three digits

     A space (optional)

     Three digits

     A space (optional)

     2-3 digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_netherlands_bsn finds content that matches the pattern.

     A keyword from Keyword_netherlands_bsn is found.

     The function Func_eu_date finds a date in the right date format.

     The checksum passes.

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_netherlands_bsn finds content that matches the pattern.

     The checksum passes.

<!-- p.2431 -->

  <!-- Netherlands Citizen's Service (BSN) Number -->
  <Entity id="c5f54253-ef7e-44f6-a578-440ed67e946d" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_netherlands_bsn"/>
       <Match idRef="Keyword_netherlands_bsn"/>
       <Match idRef="Func_eu_date"/>
    </Pattern>
    <Pattern confidenceLevel="65">
       <IdMatch idRef="Func_netherlands_bsn"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_netherlands_bsn

 Citizen service number
 BSN
 Burgerservicenummer
 Sofinummer
 Persoonsgebonden nummer
 Persoonsnummer

New Zealand Ministry of Health Number
Format: Three letters, a space (optional), and four digits

Pattern: Three letters (not case sensitive) a space (optional) four digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_new_zealand_ministry_of_health_number finds content that matches the pattern.

     A keyword from Keyword_nz_terms is found.

     The checksum passes.

  <!-- New Zealand Health Number -->
  <Entity id="2b71c1c8-d14e-4430-82dc-fd1ed6bf05c7" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_new_zealand_ministry_of_health_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_nz_terms" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_nz_terms

 NHI
 New Zealand
 Health
 treatment

Norway Identification Number
Format: 11 digits

<!-- p.2432 -->

Pattern: 11 digits:

     Six digits in the format DDMMYY that are the date of birth

     Three-digit individual number

     Two check digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_norway_id_number finds content that matches the pattern.

     A keyword from Keyword_norway_id_number is found.

     The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_norway_id_numbe finds content that matches the pattern.

     The checksum passes.

  <!-- Norway Identification Number -->
  <Entity id="d4c8a798-e9f2-4bd3-9652-500d24080fc3" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_norway_id_number"/>
       <Match idRef="Keyword_norway_id_number"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_norway_id_number"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_norway_id_number

 Personal identification number
 Norwegian ID Number
 ID Number
 Identification
 Personnummer
 Fødselsnummer

Philippines Unified Multi-Purpose ID Number
Format: 12 digits separated by hyphens

Pattern: 12 digits:

     Four digits

     A hyphen

     Seven digits

     A hyphen

     One digit

Checksum: No

Definition:

<!-- p.2433 -->

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_philippines_unified_id finds content that matches the pattern.

     A keyword from Keyword_philippines_id is found.

  <!-- Philippines Unified Multi-Purpose ID number -->
  <Entity id="019b39dd-8c25-4765-91a3-d9c6baf3c3b3" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Regex_philippines_unified_id"/>
       <Match idRef="Keyword_philippines_id"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_philippines_id

 Unified Multi-Purpose ID
 UMID
 Identity Card
 Pinag-isang Multi-Layunin ID

Poland Identity Card
Format: Three letters and six digits

Pattern: Three letters (not case sensitive) followed by six digits

Checksum: Yes

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_polish_national_id finds content that matches the pattern.

     A keyword from Keyword_polish_national_id_passport_number is found.

     The checksum passes.

  <!-- Poland Identity Card-->
  <Entity id="25E64989-ED5D-40CA-A939-6C14183BB7BF" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
            <IdMatch idRef="Func_polish_national_id" />
            <Match idRef="Keyword_polish_national_id_passport_number" />
        </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_polish_national_id_passport_number

 Nazwa i nr dowodu tożsamości
 Dowód Tożsamości
 dow. os.

Poland National ID (PESEL)
Format: 11 digits

<!-- p.2434 -->

Pattern: 11 consecutive digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_pesel_identification_number finds content that matches the pattern.

     A keyword from Keyword_pesel_identification_number is found.

     The checksum passes.

  <!-- Poland National ID (PESEL) -->
  <Entity id="E3AAF206-4297-412F-9E06-BA8487E22456" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
            <IdMatch idRef="Func_pesel_identification_number" />
            <Match idRef="Keyword_pesel_identification_number" />
        </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_pesel_identification_number

 Nr PESEL
 PESEL

Poland Passport
Format: Two letters and seven digits

Pattern: Two letters (not case sensitive) followed by seven digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_polish_passport_number finds content that matches the pattern.

     A keyword from Keyword_polish_national_id_passport_number is found.

     The checksum passes.

  <!-- Poland Passport Number -->
  <Entity id="03937FB5-D2B6-4487-B61F-0F8BFF7C3517" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
             <IdMatch idRef="Func_polish_passport_number" />
             <Match idRef="Keyword_polish_national_id_passport_number" />
        </Pattern>
  </Entity>
  </Version>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_polish_national_id_passport_number

 Nazwa i nr dowodu tożsamości
 Dowód Tożsamości
 dow. os.

<!-- p.2435 -->

Portugal Citizen Card Number
Format: Eight digits

Pattern: Eight digits

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_portugal_citizen_card finds content that matches the pattern.

     A keyword from Keyword_portugal_citizen_card is found.

  <!-- Portugal Citizen Card Number -->
  <Entity id="91a7ece2-add4-4986-9a15-c84544d81ecd" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Regex_portugal_citizen_card"/>
       <Match idRef="Keyword_portugal_citizen_card"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_portugal_citizen_card

 Citizen Card
 National ID Card
 CC
 Cartão de Cidadão
 Bilhete de Identidade

Saudi Arabia National ID
Format: 10 digits

Pattern: 10 consecutive digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_saudi_arabia_national_id finds content that matches the pattern.

     A keyword from Keyword_saudi_arabia_national_id is found.

  <!-- Saudi Arabia National ID -->
  <Entity id="8c5a0ba8-404a-41a3-8871-746aa21ee6c0" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_saudi_arabia_national_id" />
          <Any minMatches="1">
            <Match idRef="Keyword_saudi_arabia_national_id" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

<!-- p.2436 -->

 Keyword_saudi_arabia_national_id

 Identification Card
 I card number
 ID number
 ‫الوطنية الهوية بطاقة رقم‬

Singapore National Registration Identity Card (NRIC) Number
Format: Nine letters and digits

Pattern: Nine letters and digits:

     The letter "F", "G", "S", or "T" (not case sensitive)

     Seven digits

     An alphabetic check digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_singapore_nric finds content that matches the pattern.

     A keyword from Keyword_singapore_nric is found.

     The checksum passes.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_singapore_nric finds content that matches the pattern.

     The checksum passes.

  <!-- Singapore National Registration Identity Card (NRIC) Number -->
  <Entity id="cead390a-dd83-4856-9751-fb6dc98c34da" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Regex_singapore_nric"/>
       <Match idRef="Keyword_singapore_nric"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Regex_singapore_nric"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_singapore_nric

 National Registration Identity Card
 Identity Card Number
 NRIC
 IC
 Foreign Identification Number
 FIN
 身份证
 身份證

South Africa Identification Number
Format: 13 digits that may contain spaces

Pattern: 13 digits:

<!-- p.2437 -->

      Six digits in the format YYMMDD, which are the date of birth

      Four digits

      A single-digit citizenship indicator

      The digit "8" or "9"

      One digit that is a checksum digit

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_south_africa_identification_number finds content that matches the pattern.

      A keyword from Keyword_south_africa_identification_number is found.

      The checksum passes.

  <!-- South Africa Identification Number -->
  <Entity id="e2adf7cb-8ea6-4048-a2ed-d89eb65f2780" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_south_africa_identification_number"/>
       <Match idRef="Keyword_south_africa_identification_number"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_south_africa_identification_number

 Identity card
 ID
 Identification

South Korea Resident Registration Number
Format: 13 digits containing a hyphen

Pattern: 13 digits:

      Six digits in the format YYMMDD that are the date of birth

      A hyphen

      One digit determined by the century and gender

      Four-digit region-of-birth code

      One digit used to differentiate people for whom the preceding numbers are identical

      A check digit.

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The function Func_south_korea_resident_number finds content that matches the pattern.

      A keyword from Keyword_south_korea_resident_number is found.

      The checksum passes.

<!-- p.2438 -->

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_south_korea_resident_number finds content that matches the pattern.

     The checksum passes.

  <!-- South Korea Resident Registration Number -->
  <Entity id="5b802e18-ba80-44c4-bc83-bf2ad36ae36a" recommendedConfidence="85" patternsProximity="300">
    <Pattern confidenceLevel="85">
       <IdMatch idRef="Func_south_korea_resident_number"/>
       <Match idRef="Keyword_south_korea_resident_number"/>
    </Pattern>
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Func_south_korea_resident_number"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_south_korea_resident_number

 National ID card
 Citizen's Registration Number
 Jumin deungnok beonho
 RRN
 주민등록번호

Spain Social Security Number (SSN)
Format: 11-12 digits

Pattern: 11-12 digits:

     Two digits

     A forward slash (optional)

     7-8 digits

     A forward slash (optional)

     Two digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_spanish_social_security_number finds content that matches the pattern.

     The checksum passes.

  <!-- Spain SSN -->
  <Entity id="5df987c0-8eae-4bce-ace7-b316347f3070" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_spanish_social_security_number" />
      </Pattern>
  </Entity>

Keywords: None

Sweden National ID

<!-- p.2439 -->

Format: 10 or 12 digits and an optional delimiter

Pattern: 10 or 12 digits and an optional delimiter:

     2-4 digits (optional)

     Six digits in date format YYMMDD

     Delimiter of "-" or "+" (optional), plus

     Four digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_swedish_national_identifier finds content that matches the pattern.

     The checksum passes.

  <!-- Sweden National ID -->
  <Entity id="f69aaf40-79be-4fac-8f05-fd1910d272c8" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_swedish_national_identifier" />
      </Pattern>
  </Entity>

Keywords: None

Sweden Passport Number
Format: Eight digits

Pattern: Eight consecutive digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_sweden_passport_number finds content that matches the pattern.

     One of the following is true:

        A keyword from Keyword_passport is found.

        A keyword from Keyword_sweden_passport is found.

  <!-- Sweden Passport Number -->
  <Entity id="ba4e7456-55a9-4d89-9140-c33673553526" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_sweden_passport_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_passport" />
            <Match idRef="Keyword_sweden_passport" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

<!-- p.2440 -->

 Keyword_sweden_passport                                                              Keyword_passport

 visa requirements                                                                    Passport Number
 Alien Registration Card                                                              Passport No
 Schengen visas                                                                       Passport #
 Schengen visa                                                                        Passport#
 Visa Processing                                                                      PassportID
 Visa Type                                                                            Passportno
 Single Entry                                                                         passport number
 Multiple Entry                                                                       パスポート
 G3 Processing Fees                                                                   パスポート番号
                                                                                      パスポートのNum
                                                                                      パスポート＃
                                                                                      Numéro de passeport
                                                                                      Passeport n °
                                                                                      Passeport Non
                                                                                      Passeport #
                                                                                      Passeport#
                                                                                      PasseportNon
                                                                                      Passeportn °

SWIFT Code
Format: Four letters followed by 5-31 letters or digits

Pattern: Four letters followed by 5-31 letters or digits:

     Four-letter bank code (not case sensitive)

     An optional space

     4-28 letters or digits (the Basic Bank Account Number (BBAN))

     An optional space

     1-3 letters or digits (remainder of the BBAN)

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_swift finds content that matches the pattern.

     A keyword from Keyword_swift is found.

  <Entity id="cb2ab58c-9cb8-4c81-baf8-a4e106791df4" patternsProximity="300" recommendedConfidence="75">
  <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_swift" />
          <Match idRef="Keyword_swift" />
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_swift

 international organization for standardization 9362
 iso 9362
 iso9362
 swift#
 swift code
 swift number
 swiftroutingnumber
 swift code
 swift number #
 swift routing number
