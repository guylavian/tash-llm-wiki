---
title: "Exchange Server — pages 2441-2480"
type: reference
domain: exchange
slug: exchange-exchange-servertoc-p2441-2480
tier: reference
source: https://learn.microsoft.com/en-us/exchange/exchange-servertoc-p2441-2480
family: exchange
documentKind: "doc"
abstract: "Keyword_swift bic number bic code bic # bic# bank identifier code 標準化9362 迅速＃ SWIFTコード SWIFT番号 迅速なルーティング番号 BIC番号 BICコード 銀行識別コードのための国際組織 Organisation internationale de normalisation 9362 rapide # code SWIFT le numéro de swift swift numéro d'acheminement le numéro BIC # BIC code i"
---

# Exchange Server — pages 2441-2480

<!-- p.2441 -->

 Keyword_swift

 bic number
 bic code
 bic #
 bic#
 bank identifier code
 標準化9362
 迅速＃
 SWIFTコード
 SWIFT番号
 迅速なルーティング番号
 BIC番号
 BICコード
 銀行識別コードのための国際組織
 Organisation internationale de normalisation 9362
 rapide #
 code SWIFT
 le numéro de swift
 swift numéro d'acheminement
 le numéro BIC
 # BIC
 code identificateur de banque

Taiwanese ID
Format: One letter (in English) followed by nine digits

Pattern: One letter (in English) followed by nine digits:

     One letter (in English, not case sensitive)

     The digit "1" or "2"

     Eight digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_taiwanese_national_id finds content that matches the pattern.

     A keyword from Keyword_taiwanese_national_id is found.

     The checksum passes.

  <!-- Taiwanese National ID -->
  <Entity id="4C7BFC34-8DD1-421D-8FB7-6C6182C2AF03" patternsProximity="300" recommendedConfidence="85">
        <Pattern confidenceLevel="85">
            <IdMatch idRef="Func_taiwanese_national_id" />
            <Match idRef="Keyword_taiwanese_national_id" />
        </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_taiwanese_national_id

 身份證字號
 身份證
 身份證號碼
 身份證號
 身分證字號
 身分證
 身分證號碼
 身份證號

<!-- p.2442 -->

 Keyword_taiwanese_national_id

 身分證統一編號
 國民身分證統一編號
 簽名
 蓋章
 簽名或蓋章
 簽章

Taiwan Passport Number
Format:

     Biometric passport number: Nine digits

     Non-biometric passport number: Nine digits

Pattern:

     Biometric passport number

           The digit "3"

           Eight digits

     Non-biometric passport number: Nine digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_taiwan_passport finds content that matches the pattern.

     A keyword from Keyword_taiwan_passport is found.

  <!-- Taiwan Passport Number -->
  <Entity id="e7251cb4-4c2c-41df-963e-924eb3dae04a" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Regex_taiwan_passport"/>
       <Match idRef="Keyword_taiwan_passport"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_taiwan_passport

 Taiwan passport number
 Passport number
 Passport no
 Passport Num
 Passport #
 护照
 中華民國護照
 Zhōnghuá Mínguó hùzhào

Taiwan Resident Certificate (ARC/TARC) Number
Format: 10 letters and digits

Pattern: 10 letters and digits:

     Two letters (not case sensitive)

<!-- p.2443 -->

     Eight digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_taiwan_resident_certificate finds content that matches the pattern.

     A keyword from Keyword_taiwan_resident_certificate is found.

  <!-- Taiwan Resident Certificate (ARC/TARC) -->
  <Entity id="48269fec-05ea-46ea-b326-f5623a58c6e9" recommendedConfidence="75" patternsProximity="300">
    <Pattern confidenceLevel="75">
       <IdMatch idRef="Regex_taiwan_resident_certificate"/>
       <Match idRef="Keyword_taiwan_resident_certificate"/>
    </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_taiwan_resident_certificate

 Resident Certificate
 Resident Cert
 Resident Cert.
 Identification card
 Alien Resident Certificate
 ARC
 Taiwan Area Resident Certificate
 TARC
 居留證
 外僑居留證
 台灣地區居留證

U.K. Driver's License Number
Format: Combination of 18 letters and digits in the specified format

Pattern: 18 letters and digits:

     Five letters (not case sensitive) or the digit "9" in place of a letter

     One digit

     Five digits in the date format DDMMY for date of birth

     Two letters (not case sensitive) or the digit "9" in place of a letter

     Five digits

Checksum: Yes

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_uk_drivers_license finds content that matches the pattern.

     A keyword from Keyword_uk_drivers_license is found.

     The checksum passes.

  <!-- U.K. Driver's License Number -->
  <Entity id="f93de4be-d94c-40df-a8be-461738047551" patternsProximity="300" recommendedConfidence="75">

<!-- p.2444 -->

      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_uk_drivers_license" />
          <Match idRef="Keyword_uk_drivers_license" />
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_uk_drivers_license

 DVLA
 light vans
 quad bikes
 motor cars
 125cc
 sidecar
 tricycles
 motorcycles
 photo card licence
 learner drivers
 licence holder
 licence holders
 driving licences
 driving licence
 dual control car

U.K. Electoral Roll Number
Format: Two letters followed by 1-4 digits

Pattern: Two letters (not case sensitive) followed by 1-4 numbers

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

      The regular expression Regex_uk_electoral finds content that matches the pattern.

      A keyword from Keyword_uk_electoral is found.

  <!-- U.K. Electoral Number -->
  <Entity id="a3eea206-dc0c-4f06-9e22-aa1be3059963" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_uk_electoral" />
          <Any minMatches="1">
            <Match idRef="Keyword_uk_electoral" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_uk_electoral

 council nomination
 nomination form
 electoral register
 electoral roll

U.K. National Health Service Number

<!-- p.2445 -->

Format: 10-17 digits separated by spaces

Pattern: 10-17 digits:

     Either 3 or 10 digits

     A space

     Three digits

     A space

     Four digits

Checksum: Yes

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_uk_nhs_number finds content that matches the pattern.

     One of the following is true:

         A keyword from Keyword_uk_nhs_number is found.

         A keyword from Keyword_uk_nhs_number1 is found.

         A keyword from Keyword_uk_nhs_number_dob is found.

     The checksum passes.

  <!-- U.K. NHS Number -->
  <Entity id="3192014e-2a16-44e9-aa69-4b20375c9a78" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_uk_nhs_number" />
          <Any minMatches="1">
            <Match idRef="Keyword_uk_nhs_number" />
            <Match idRef="Keyword_uk_nhs_number1" />
            <Match idRef="Keyword_uk_nhs_number_dob" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                        ﾉ   Expand table

 Keyword_uk_nhs_number                          Keyword_uk_nhs_number1                            Keyword_uk_nhs_number_dob

 national health service                        patient ID                                        GP
 nhs                                            patient identification                            DOB
 health services authority                      patient no                                        D.O.B
 health authority                               patient number                                    Date of Birth
                                                                                                  Birth Date

U.K. National Insurance Number (NINO)
Format: Nine letters and digits, with each pair of letters and digits optionally separated by spaces or dashes

Pattern: Nine letters and digits, with each pair of letters and digits optionally separated by spaces or dashes:

     Two letters (not case sensitive), neither of which can be D, F, I, Q, U, or V. Additionally, the second letter can't be O. The following
     combinations are also not allowed: BG, GB, KN, NK, NT, TN, and ZZ.

     Six digits

     A space or dash (optional)

     Two digits

<!-- p.2446 -->

     A space or dash (optional)

     Two digits

     A space or dash (optional)

     Two digits

     One letter that can be A, B, C, D; or one space.

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_uk_nino finds content that matches the pattern.

     A keyword from Keyword_uk_nino is found.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_uk_nino finds content that matches the pattern.

     No keyword from Keyword_uk_nino is found.

  <!-- U.K. NINO -->
  <Entity id="16c07343-c26f-49d2-a987-3daf717e94cc" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_uk_nino" />
          <Any minMatches="1">
            <Match idRef="Keyword_uk_nino" />
          </Any>
      </Pattern>
       <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_uk_nino" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Keyword_uk_nino" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

 Keyword_uk_nino

 national insurance number
 national insurance contributions
 protection act
 insurance
 social security number
 insurance application
 medical application
 social insurance
 medical attention
 social security
 great britain
 insurance

U.S. / U.K. Passport Number
Format: Nine digits

Pattern: Nine consecutive digits

Checksum: No

Definition:

<!-- p.2447 -->

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_usa_uk_passport finds content that matches the pattern.

     A keyword from Keyword_passport is found.

  <Entity id="178ec42a-18b4-47cc-85c7-d62c92fd67f8" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_usa_uk_passport" />
          <Match idRef="Keyword_passport" />
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
 パスポート＃
 Numéro de passeport
 Passeport n °
 Passeport Non
 Passeport #
 Passeport#
 PasseportNon
 Passeportn °

U.S. Bank Account Number
Format: 4-17 digits

Pattern: 4-17 consecutive digits

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The regular expression Regex_usa_bank_account_number finds content that matches the pattern.

     A keyword from Keyword_usa_Bank_Account is found.

  <!-- U.S. Bank Account Number -->
  <Entity id="a2ce32a8-f935-4bb6-8e96-2a5157672e2c" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Regex_usa_bank_account_number" />
          <Match idRef="Keyword_usa_Bank_Account" />
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                ﾉ   Expand table

<!-- p.2448 -->

 Keyword_usa_Bank_Account

 Checking Account Number
 Checking Account
 Checking Account #
 Checking Acct Number
 Checking Acct #
 Checking Acct No.
 Checking Account No.
 Bank Account Number
 Bank Account #
 Bank Acct Number
 Bank Acct #
 Bank Acct No.
 Bank Account No.
 Savings Account Number
 Savings Account.
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

U.S. Driver's License Number
Format: Depends on the state

Pattern: Depends on the state -- for example, New York:

     Nine digits formatted like ddd ddd ddd will match

     Nine digits like ddddddddd will not match.

Checksum: No

Definition:

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_new_york_drivers_license_number finds content that matches the pattern.

     A keyword from Keyword_[state_name]_drivers_license_name is found.

     A keyword from Keyword_us_drivers_license is found.

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_new_york_drivers_license_number finds content that matches the pattern.

     A keyword from Keyword_[state_name]_drivers_license_name is found.

     A keyword from Keyword_us_drivers_license_abbreviations is found.

     No keyword from Keyword_us_drivers_license is found.

  <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_new_york_drivers_license_number" />
          <Match idRef="Keyword_new_york_drivers_license_name" />
          <Match idRef="Keyword_us_drivers_license" />
      </Pattern>
      <Pattern confidenceLevel="65">
          <IdMatch idRef="Func_new_york_drivers_license_number" />
          <Match idRef="Keyword_new_york_drivers_license_name" />
          <Match idRef="Keyword_us_drivers_license_abbreviations" />

<!-- p.2449 -->

            <Any minMatches="0" maxMatches="0">
              <Match idRef="Keyword_us_drivers_license" />
            </Any>
        </Pattern>

Keywords:

                                                                                                                         ﾉ   Expand table

 Keyword_us_drivers_license_abbreviations          Keyword_us_drivers_license   Keyword_[state_name]_drivers_license_name

 DL                                                DriverLic                    State abbreviation (for example, "NY")
 DLS                                               DriverLics                   State name (for example, "New York")
 CDL                                               DriverLicense
 CDLS                                              DriverLicenses
 ID                                                Driver Lic
 IDs                                               Driver Lics
 DL#                                               Driver License
 DLS#                                              Driver Licenses
 CDL#                                              DriversLic
 CDLS#                                             DriversLics
 ID#                                               DriversLicense
 IDs#                                              DriversLicenses
 ID number                                         Drivers Lic
 ID numbers                                        Drivers Lics
 LIC                                               Drivers License
 LIC#                                              Drivers Licenses
                                                   Driver'Lic
                                                   Driver'Lics
                                                   Driver'License
                                                   Driver'Licenses
                                                   Driver' Lic
                                                   Driver' Lics
                                                   Driver' License
                                                   Driver' Licenses
                                                   Driver'sLic
                                                   Driver'sLics
                                                   Driver'sLicense
                                                   Driver'sLicenses
                                                   Driver's Lic
                                                   Driver's Lics
                                                   Driver's License
                                                   Driver's Licenses
                                                   identification number
                                                   identification numbers
                                                   identification #
                                                   ID card
                                                   ID cards
                                                   identification card
                                                   identification cards
                                                   DriverLic#
                                                   DriverLics#
                                                   DriverLicense#
                                                   DriverLicenses#
                                                   Driver Lic#
                                                   Driver Lics#
                                                   Driver License#
                                                   Driver Licenses#
                                                   DriversLic#
                                                   DriversLics#
                                                   DriversLicense#
                                                   DriversLicenses#
                                                   Drivers Lic#
                                                   Drivers Lics#
                                                   Drivers License#
                                                   Drivers Licenses#
                                                   Driver'Lic#
                                                   Driver'Lics#
                                                   Driver'License#
                                                   Driver'Licenses#
                                                   Driver' Lic#
                                                   Driver' Lics#
                                                   Driver' License#
                                                   Driver' Licenses#

<!-- p.2450 -->

 Keyword_us_drivers_license_abbreviations                Keyword_us_drivers_license           Keyword_[state_name]_drivers_license_name

                                                         Driver'sLic#
                                                         Driver'sLics#
                                                         Driver'sLicense#
                                                         Driver'sLicenses#
                                                         Driver's Lic#
                                                         Driver's Lics#
                                                         Driver's License#
                                                         Driver's Licenses#
                                                         ID card#
                                                         ID cards#
                                                         identification card#
                                                         identification cards#

U.S. Individual Taxpayer Identification Number (ITIN)
Format: Nine digits that start with a "9" and contain a "7" or "8" as the fourth digit, optionally formatted with spaces or dashes

Pattern:

Formatted:

     The digit "9"

     Two digits

     A space or dash

     A "7" or "8"

     A digit

     A space, or dash

     Four digits

Unformatted:

     The digit "9"

     Two digits

     A "7" or "8"

     Five digits

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_formatted_itin finds content that matches the pattern.

     At least one of the following is true:

           A keyword from Keyword_itin is found.

           The function Func_us_address finds an address in the right date format.

           The function Func_us_date finds a date in the right date format.

           A keyword from Keyword_itin_collaborative is found.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_unformatted_itin finds content that matches the pattern.

     At least one of the following is true:

           A keyword from Keyword_itin_collaborative is found.

<!-- p.2451 -->

         The function Func_us_address finds an address in the right date format.

         The function Func_us_date finds a date in the right date format.

  <!-- U.S. Individual Taxpayer Identification Number (ITIN) -->
  <Entity id="e55e2a32-f92d-4985-a35d-a0b269eb687b" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_formatted_itin" />
          <Any minMatches="1">
            <Match idRef="Keyword_itin" />
            <Match idRef="Func_us_address" />
            <Match idRef="Func_us_date" />
            <Match idRef="Keyword_itin_collaborative" />
          </Any>
      </Pattern>
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_unformatted_itin" />
          <Match idRef="Keyword_itin" />
          <Any minMatches="1">
            <Match idRef="Keyword_itin_collaborative" />
            <Match idRef="Func_us_address" />
            <Match idRef="Func_us_date" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                                                                                 ﾉ   Expand table

 Keyword_itin                                                  Keyword_itin_collaborative

 taxpayer                                                      License
 tax ID                                                        DL
 tax identification                                            DOB
 itin                                                          Birthdate
 ssn                                                           Birthday
 tin                                                           Date of Birth
 social security
 tax payer
 itins
 taxid
 individual taxpayer

U.S. Social Security Number (SSN)
Format: Nine digits, which may be in a formatted or unformatted pattern

  ７ Note

  If issued before mid-2011, an SSN has strong formatting where certain parts of the number must fall within certain ranges to be valid (but
  there's no checksum).

Pattern: Four functions look for SSNs in four different patterns:

      Func_ssn finds SSNs with pre-2011 strong formatting that are formatted with dashes or spaces (ddd-dd-dddd OR ddd dd dddd)

      Func_unformatted_ssn finds SSNs with pre-2011 strong formatting that are unformatted as nine consecutive digits (ddddddddd)

      Func_randomized_formatted_ssn finds post-2011 SSNs that are formatted with dashes or spaces (ddd-dd-dddd OR ddd dd dddd)

      Func_randomized_unformatted_ssn finds post-2011 SSNs that are unformatted as nine consecutive digits (ddddddddd)

Checksum: No

Definition:

A DLP policy is 85% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

<!-- p.2452 -->

     The function Func_ssn finds content that matches the pattern.

     At least one of the following is true:

        A keyword from Keyword_ssn is found.

        The function Func_us_date finds a date in the right date format.

        The function Func_us_address finds an address in the right date format.

A DLP policy is 75% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_unformatted_ssn finds content that matches the pattern.

     A keyword from Keyword_ssn is found.

     At least one of the following is true:

        The function Func_us_date finds a date in the right date format.

        The function Func_us_address finds an address in the right date format.

A DLP policy is 65% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_randomized_formatted_ssn finds content that matches the pattern.

     The function Func_ssn does not find content that matches the pattern.

     At least one of the following is true:

        A keyword from Keyword_ssn is found.

        The function Func_us_date finds a date in the right date format.

        The function Func_us_address finds an address in the right date format.

A DLP policy is 55% confident that it's detected this type of sensitive information if, within a proximity of 300 characters:

     The function Func_randomized_unformatted_ssn finds content that matches the pattern.

     A keyword from Keyword_ssn is found.

     The function Func_unformatted_ssn does not find content that matches the pattern.

     At least one of the following is true:

        The function Func_us_date finds a date in the right date format.

        The function Func_us_address finds an address in the right date format.

  <!-- U.S. Social Security Number (SSN) -->
  <Entity id="a44669fe-0d48-453d-a9b1-2cc83f2cba77" patternsProximity="300" recommendedConfidence="75">
      <Pattern confidenceLevel="85">
          <IdMatch idRef="Func_ssn" />
          <Any minMatches="1">
            <Match idRef="Keyword_ssn" />
            <Match idRef="Func_us_date" />
            <Match idRef="Func_us_address" />
          </Any>
      </Pattern>
      <Pattern confidenceLevel="75">
          <IdMatch idRef="Func_unformatted_ssn" />
          <Match idRef="Keyword_ssn" />
          <Any minMatches="1">
            <Match idRef="Func_us_date" />
            <Match idRef="Func_us_address" />
          </Any>
      </Pattern>
      <Pattern confidenceLevel="65">
          <IdMatch idRef="Func_randomized_formatted_ssn" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Func_ssn" />
          </Any>

<!-- p.2453 -->

          <Any minMatches="1">
            <Match idRef="Keyword_ssn" />
            <Match idRef="Func_us_date" />
            <Match idRef="Func_us_address" />
          </Any>
      </Pattern>
      <Pattern confidenceLevel="55">
          <IdMatch idRef="Func_randomized_unformatted_ssn" />
          <Match idRef="Keyword_ssn" />
          <Any minMatches="0" maxMatches="0">
            <Match idRef="Func_unformatted_ssn" />
          </Any>
          <Any minMatches="1">
            <Match idRef="Func_us_date" />
            <Match idRef="Func_us_address" />
          </Any>
      </Pattern>
  </Entity>

Keywords:

                                                                ﾉ   Expand table

 Keyword_ssn

 Social Security
 Social Security#
 Soc Sec
 SSN
 SSNS
 SSN#
 SS#
 SSID

<!-- p.2454 -->

Information Rights Management in
Exchange Server
Article • 05/09/2025

Every day, people use email to exchange sensitive information, such as confidential information
or reports. Because email is accessible from just about anywhere, mailboxes have transformed
into repositories that contain large amounts of potentially sensitive information. As a result,
information leakage can be a serious threat to organizations. To help prevent information
leakage, Exchange Server includes Information Rights Management (IRM) features, which
provide persistent online and offline protection for email messages and attachments. These
IRM features are basically unchanged from Exchange 2013.

What is information leakage?
Information leakage is the disclosure of sensitive information to unauthorized users.
Information leakage can be costly for an organization, and can have a wide-ranging impact on
the organization's business, employees, customers, and partners. To avoid violating any
applicable regulations, organizations need to protect themselves against accidental or
intentional information leakage.

These are some consequences that can result from information leakage:

      Financial damage: The organization might incur a loss of business, fines, or adverse
      media coverage.

      Damage to image and credibility: Leaked email messages can potentially be a source of
      embarrassment for the sender and the organization.

      Loss of competitive advantage: This is one of the most serious consequences. The
      disclosure of strategic business or merger and acquisition plans can lead to losses in
      revenue or market capitalization for the organization. Other threats to competitive
      advantage include the loss of research information, analytical data, and other intellectual
      property.

Traditional solutions to information leakage
Although traditional solutions to information leakage may protect the initial access to data,
they often don't provide constant protection. This table describes some traditional solutions to
information leakage.

<!-- p.2455 -->

                                                                                         ﾉ   Expand table

 Solution     Description                                      Limitations

 Transport    TLS is an Internet standard protocol that's      TLS only protects the SMTP session
 Layer        used to encrypt network communications. In       between two SMTP hosts. In other words,
 Security     a messaging environment, TLS is used to          TLS protects information in motion, and it
 (TLS)        encrypt server/server and client/server          doesn't provide protection at the
              communications.                                  message-level or for information at rest.
              By default, Exchange uses TLS for all internal   Unless the messages are encrypted using
              message transfers. Opportunistic TLS is also     another method, messages in sender and
              enabled by default for SMTP sessions with        recipient mailboxes remain unprotected.
              external hosts (TLS encryption is tried first,   For email sent outside the organization,
              but if it isn't available, unencrypted           you can require TLS only for the first hop.
              communication is allowed). You can also          After a remote SMTP host receives the
              configure domain security to enforce mutual      message, it can relay it to another SMTP
              TLS with external organizations.                 host over an unencrypted session.

                                                               Because TLS is a transport layer
                                                               technology that's used in mail flow, it can't
                                                               provide control over what the recipient
                                                               does with the message.

 Message      Users can use technologies such as S/MIME        Users decide whether a message gets
 encryption   to encrypt messages.                             encrypted.
                                                               There are additional costs of a public key
                                                               infrastructure (PKI) deployment, with the
                                                               accompanying overhead of certificate
                                                               management for users and protection of
                                                               private keys.

                                                               After a message is decrypted, there's no
                                                               control over what the recipient can do
                                                               with the information. Decrypted
                                                               information can be copied, printed, or
                                                               forwarded. By default, saved attachments
                                                               aren't protected.

                                                               Messaging servers can't open and inspect
                                                               messages that are encrypted by S/MIME.
                                                               Therefore, the messaging servers can't
                                                               enforce messaging policies, scan
                                                               messages for viruses, or take other actions
                                                               that require access to the content in
                                                               messages.

Finally, traditional solutions often lack enforcement tools that apply uniform messaging policies
to prevent information leakage. For example, a user marks a message with Company
Confidential and Do Not Forward. After the message is delivered to the recipient, the sender

<!-- p.2456 -->

or the organization no longer has control over the message. The recipient can willfully or
accidentally forward the message (using features such as automatic forwarding rules) to
external email accounts, which subjects your organization to substantial information leakage
risks.

IRM in Exchange
IRM in Exchange helps prevent information leakage by offering these features:

         Prevent an authorized recipient of IRM-protected content from forwarding, modifying,
         printing, faxing, saving, or cutting and pasting the content.

         Protect supported attachment file formats with the same level of protection as the
         message.

         Support expiration of IRM-protected messages and attachments so they can no longer be
         viewed after the specified period.

         Prevent IRM-protected content from being copied using the Snipping Tool inWindows.

However, IRM in Exchange can't prevent the disclosure of information by using these methods:

         Third-party screen capture programs.

         Photographing IRM-protected content that's displayed on the screen.

         Users remembering or manually transcribing the information.

IRM uses Active Directory Rights Management Services (AD RMS), an information protection
technology in Windows Server that uses extensible rights markup language (XrML)-based
certificates and licenses to certify computers and users, and to protect content. When a
document or message is protected using AD RMS, an XrML license containing the rights that
authorized users have to the content is attached. To access IRM-protected content, AD RMS-
enabled applications must procure a use license for the authorized user from the AD RMS
server. Office applications, such as Word, Excel, PowerPoint and Outlook are RMS-enabled and
can be used to create and consume protected content.

  ７ Note

  The Exchange Prelicense Agent attaches a use license to messages that are protected by
  the AD RMS server in your organization. For more information, see the Prelicensing
  section later in this topic.

<!-- p.2457 -->

To learn more about Active Directory Rights Management Services, see Active Directory Rights
Management Services.

Active Directory Rights Management Services rights policy
templates
AD RMS servers provide a Web service that's used to enumerate and acquire the XrML-based
rights policy templates that you use to apply IRM protection to messages. By applying the
appropriate rights policy template, you can control whether a recipient is allowed to reply to,
reply to all, forward, extract information from, save, or print the message.

By default, Exchange ships with the Do Not Forward template. When this template is applied
to a message, only the recipients addressed in the message can decrypt the message. The
recipients can't forward the message, copy content from the message, or print the message.
You can create additional RMS templates on the AD RMS servers in your organization to meet
your requirements.

For more information about rights policy templates, see AD RMS Policy Template
Considerations.

For more information about creating AD RMS rights policy templates, see AD RMS Rights
Policy Templates Deployment Step-by-Step Guide.

Apply IRM protection to messages
By default, an Exchange organization is enabled for IRM, but to apply IRM protection to
messages, you need to use one or more of these methods:

     Manually by users in Outlook: Users can IRM-protect messages in Outlook by using the
     AD RMS rights policy templates that are available to them. This process uses the IRM
     functionality in Outlook, not Exchange. For more information about using IRM in Outlook,
     see Introduction to using IRM for email messages      .

     Manually by users in Outlook on the web: When an administrator enables IRM in
     Outlook on the web (formerly known as Outlook Web App), users can IRM-protect
     messages that they send, and view IRM-protected messages that they receive. For more
     information about IRM in Outlook on the web, see Understanding IRM in Outlook Web
     App.

     Manually by users in Exchange ActiveSync: When an administrator enables IRM in
     Exchange ActiveSync users can view, reply to, forward, and create IRM-protected

<!-- p.2458 -->

     messages on ActiveSync devices. For more information, see Understanding Information
     Rights Management in Exchange ActiveSync.

     Automatically in Outlook: Administrators can create Outlook protection rules to
     automatically IRM-protect messages. Outlook protection rules are automatically deployed
     to Outlook clients, and IRM-protection is applied by Outlook when the user is composing
     a message. For more information, see Outlook Protection Rules.

     Automatically on Mailbox servers: Administrators can create mail flow rules (also known
     as transport rules) to automatically IRM-protect messages that match specified
     conditions. For more information, see Understanding Transport Protection Rules.

        ７ Note

        IRM protection isn't applied again to messages that are already IRM-protected. For
        example, if a user IRM-protects a message in Outlook or Outlook on the web, a
        transport protection rule won't apply IRM protection to the same message.

Scenarios for IRM protection
This table describes the scenarios for sending messages, and whether IRM protection is
available.

                                                                                      ﾉ   Expand table

 Scenario                         Is sending IRM-   Requirements
                                  Protected
                                  messages
                                  supported?

 Sending messages within the      Yes               For the requirements, see the IRM requirements
 same on-premises Exchange                          section later in this topic.
 organization

 Sending messages between         Yes               For the requirements, see Configuring AD RMS to
 different Active Directory                         Integrate with Exchange Server 2010 Across Multiple
 forests in an on-premises                          Forests.
 organization.

 Sending messages between         Yes               For more information, see IRM in Exchange hybrid
 an on-premises Exchange                            deployments.
 organization and a Microsoft
 365 or Office 365 organization
 in a hybrid deployment.

<!-- p.2459 -->

 Scenario                       Is sending IRM-   Requirements
                                Protected
                                messages
                                supported?

 Sending messages to external   No                Exchange doesn't include a solution for sending
 recipients                                       IRM-protected messages to external recipients in
                                                  non-federated organizations. To create a federated
                                                  trust between two Active Directory forests by using
                                                  Active Directory Federation Services (AD FS), see
                                                  Understanding AD RMS Trust Policies.

Decrypt IRM-protected messages to enforce
messaging policies
To enforce messaging policies and for regulatory compliance, Exchange needs access to the
content of encrypted messages. To meet eDiscovery requirements due to litigation, regulatory
audits, or internal investigations, a designated auditor must also be able to search encrypted
messages. To help with these tasks, Exchange includes the following decryption features:

     Transport decryption: Allows access to message content by the transport agents that are
     installed on Exchange servers. For more information, see Understanding Transport
     Decryption.

     Journal report decryption: Allows standard or premium journaling to save a clear-text
     copy of IRM-protected messages in journal reports. For more information, see Enable
     journal report decryption.

     IRM decryption for Exchange Search: Allows Exchange Search to index content in IRM-
     protected messages. When a discovery manager performs an In-Place eDiscovery search,
     IRM-protected messages that have been indexed are returned in the search results. For
     more information, see Configure IRM for Exchange Search and In-Place eDiscovery.

To enable these decryption features, you need to add the Federation mailbox (a system
mailbox that's created by Exchange), to the Super Users group on the AD RMS server. For
instructions, see Add the Federation Mailbox to the AD RMS Super Users Group.

Prelicensing
To allow authorized users to view IRM-protected messages and attachments, Exchange
automatically attaches a prelicense to protected messages. This prevents the client from
making repeated trips to the AD RMS server to retrieve a use license, and enables offline

<!-- p.2460 -->

viewing of IRM-protected messages. Prelicensing also allows users to view IRM-protected
messages in Outlook on the web. When you enable IRM features, prelicensing is enabled by
default.

IRM agents
IRM features use the built-in transport agents that exist in the Transport service on Mailbox
servers. Most of the built-in transport agents are invisible and unmanageable by the transport
agent management cmdlets in the Exchange Management Shell (*-TransportAgent).

The built-in transport agents that are associated with IRM are described in this table:

                                                                                  ﾉ   Expand table

 Agent name         Manageable?   SMTP or categorizer      Description
                                  event

 Journal Report     No            OnCategorizedMessage     Provides a clear-text copy of the IRM-
 Decryption                                                protected messages that are attached to
 Agent                                                     journal reports.

 Prelicense Agent   No            OnRoutedMessage          Attaches a prelicense to IRM-protected
                                                           messages.

 RMS Decryption     No            OnSubmittedMessage,      Decrypts IRM-protected messages to
 Agent                                                     allow access to the message content by
                                                           transport agents.

 RMS Encryption     No            OnRoutedMessage          Applies IRM protection to messages
 Agent                                                     flagged by the transport agent and re-
                                                           encrypts transport decrypted messages.

 RMS Protocol       No            OnEndOfData              Decrypts IRM-protected messages to
 Decryption                                                allow access to the message content by
 Agent                                                     transport agents.

 Transport Rule     Yes           OnRoutedMessage          Flags messages that match the conditions
 Agent                                                     in a transport protection rule to be IRM-
                                                           protected by the RMS Encryption agent.

For more information about transport agents, see Transport Agents in Exchange Server.

IRM requirements
By default, an Exchange organization is enabled for IRM. To actually implement IRM in your
Exchange Server organization, your deployment must meet the requirements that are

<!-- p.2461 -->

described in this table.

                                                                                         ﾉ   Expand table

 Server       Requirements

 AD RMS       AD RMS cluster is the term that's used for any AD RMS deployment, including a single AD
 cluster      RMS server. AD RMS is a Web service, so you don't need to set up a Windows Server
              failover cluster. For high availability and load-balancing, you can deploy multiple AD RMS
              servers in the cluster and use network load balancing (NLB).

              Service connection point: AD RMS-aware applications like Exchange use the service
              connection point that's registered in Active Directory to discover an AD RMS cluster and
              URLs. There's only one service connection point for AD RMS in an Active Directory forest.
              You can register the service connection point during AD RMS Setup, or after setup is
              complete.

              Permissions: Read and Execute permissions to the AD RMS server certification pipeline (the
               ServerCertification.asmx file at \inetpub\wwwroot\_wmcs\certification\ ) must be
              assigned to these security principals:

                    The Exchange Servers group or individual Exchange servers.
                    The AD RMS Service group on AD RMS servers.
                    For details, see Set Permissions on the AD RMS Server Certification Pipeline.

              AD RMS super users: To enable transport decryption, journal report decryption, IRM in
              Outlook on the web, and IRM decryption for Exchange Search, you need to add the
              Federation mailbox to the Super Users group on the AD RMS server. For details, see Add
              the Federation Mailbox to the AD RMS Super Users Group.

 Exchange     Exchange 2010 or later is required.
              In a production environment, installing AD RMS and Exchange on the same server isn't
              supported.

 Outlook      AD RMS templates for protecting messages are available in Outlook 2007 or later.
              Outlook protection rules in Exchange require Outlook 2010 or later.

 Exchange     IRM is available on mobile applications and devices that support Exchange ActiveSync
 ActiveSync   protocol version 14.1 or later, and the included RightsManagementInformation tag (both
              introduced in Exchange 2010 Service Pack 1). Users with supported devices can use
              ActiveSync to view, reply to, forward, and create IRM-protected messages without
              connecting to a computer to activate the device for IRM. For more information, see
              Understanding Information Rights Management in Exchange ActiveSync.

Exchange IRM features support Office file formats. You can extend IRM protection to other file
formats by deploying custom protectors. For more information about custom protectors,
search for Information Protection and Control Partners on the Microsoft solution providers
page.

<!-- p.2462 -->

Configure and test IRM
You use the Exchange Management Shell to configure IRM features in Exchange. For
procedures, see Managing Rights Protection.

After you install and configure a Mailbox server, you can use the Test-IRMConfiguration
cmdlet to perform end-to-end tests of your IRM deployment. The cmdlet performs these tests:

     Inspects IRM configuration for your Exchange organization.

     Checks the AD RMS server for version and hotfix information.

     Verifies whether an Exchange server can be activated for RMS by retrieving a Rights
     Account Certificate (RAC) and client licensor certificate.

     Acquires AD RMS rights policy templates from the AD RMS server.

     Verifies that the specified sender can send IRM-protected messages.

     Retrieves a Super User use license for the specified recipient.

     Acquires a prelicense for the specified recipient.

For more information, see Test-IRMConfiguration.

Extend Rights Management with the Rights
Management connector
The Azure Rights Management connector (RMS connector) is an optional application that
enhances data protection for your Exchange server by employing the cloud-based Azure Rights
Management (Azure RMS) service. Once you install the RMS connector, it provides continuous
data protection during the lifetime of the information. And, because these services are
customizable, you can define the level of protection that you need. For example, you can limit
email message access to specific users, or set view-only rights for certain messages.

To learn more about the RMS connector and how to install it, see Deploying the Azure Rights
Management connector.

<!-- p.2463 -->

Journaling in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016     2019        Subscription Edition

Journaling in Exchange Server can help your organization respond to legal, regulatory, and
organizational compliance requirements by recording all or targeted email messages.
Journaling in Exchange Server is basically unchanged from Exchange Server 2010.

Exchange provides the following journaling options:

      Standard journaling: Journal all messages that are sent to and received by mailboxes on a
      specific mailbox database. To journal all messages in your organization, you need to
      configure journaling on all mailbox databases on all Exchange servers.

      Premium journaling: Use journal rules to journal messages based on recipients (all
      recipients or specified recipients), and scope (internal messages, external messages, or all
      messages). Premium journaling requires Exchange Enterprise client access licenses (CALs).
      For more information about CALs, see Exchange licensing FAQs       .

To configure journaling, see Journaling procedures in Exchange Server.

When you plan for messaging retention and compliance, it's important to understand
journaling, and how journaling fits in your organization's compliance policies.

Why journaling is important
First, it's important to understand the difference between journaling and archiving when it
comes to email messages:

      Journaling refers to recording email communications as part of the organization's email
      retention strategy.

      Archiving refers to removing email messages from their native location (for example, a
      user's mailbox), and storing them elsewhere.

Many organizations need to maintain records of the email communication that occurs as
employees perform their daily business tasks. You can use Exchange journaling as a tool in your
email retention or archival strategy.

Although a regulation may not specifically require journaling, Exchange journaling can help
your organization achieve compliance with the regulation. For example, corporate officers in
some financial sectors can be held liable for claims that are made by their employees to
customers. Designated compliance managers can use journaling to collect and regularly review

<!-- p.2464 -->

the email messages that are sent by employees to customers as part of their greater employee-
to-customer communications review. The compliance managers can report their approval to
the corporate officer, and the corporate officer can then report compliance to the regulating
body.

The following list shows some of the more well-known U.S. and international regulations where
Exchange journaling may help form part of your compliance strategies:

     Sarbanes-Oxley Act of 2002 (SOX)

     Security Exchange Commission Rule 17a-4 (SEC Rule 17 A-4)

     National Association of Securities Dealers 3010 & 3110 (NASD 3010 & 3110)

     Gramm-Leach-Bliley Act (Financial Modernization Act)

     Financial Institution Privacy Protection Act of 2001

     Financial Institution Privacy Protection Act of 2003

     Health Insurance Portability and Accountability Act of 1996 (HIPAA)

     Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept
     and Obstruct Terrorism Act of 2001 (Patriot Act)

     European Union Data Protection Directive (EUDPD)

     Japan's Personal Information Protection Act

Journaling agent
The Journaling agent is the built-in Exchange transport agent that processes messages as they
flow through the Transport service on Mailbox servers. The journaling configuration settings
are stored in Active Directory, and are read by the Journaling agent. The Journaling agent is
registered on the OnSubmittedMessage and OnRoutedMessage categorizer events in the
transport pipeline. For more information about the transport pipeline, see Mail flow and the
transport pipeline.

Note that built-in transport agents like the Journaling agent are invisible and unmanageable by
the transport agent management cmdlets (*-TransportAgent).

Journal reports

<!-- p.2465 -->

A journal report is the message that's recorded by journaling. The journal report contains the
original message as an unaltered file attachment. The body of the journal report contains
summary information from the original message (for example, the sender's email address,
message subject, Message-ID, and recipient email addresses). This type of journaling is known
as envelope journaling, and is the only journaling method that's supported by Exchange.

Journal reports and IRM-protected messages
You need to consider the effects of IRM-protected messages on journal reports. Third-party
archiving systems that don't have built-in RMS support can't decrypt the IRM-protected
messages in journal reports, which negatively affects the search and discovery of content in
journaled messages. In Exchange, you can configure journal report decryption to save a clear-
text copy of the message in the journal report. For more information, see Enable journal report
decryption.

Journal rules
The basic components of a journal rule are:

        Journal recipient: Who you want to journal.

        Journal rule scope: What you want to journal.

        Journaling mailbox: Where you want to store the journaled messages.

Journal recipient
The journal recipient specifies who you want to journal. Messages that are sent to or received
by the journal recipient are journaled (the direction doesn't matter). You can configure a
journal rule to journal messages for all senders and recipients in the Exchange organization, or
you can limit a journal rule to an Exchange mailbox, group, mail user, or mail contact. If you
specify a distribution group, you enable journaling for the members of the distribution group
(not for the group itself).

By targeting specific recipients or groups of recipients, you can configure a journaling
environment that helps you meet your organization's regulatory and legal requirements, while
minimizing the storage and other costs that are associated with retaining large amounts of
data.

Journal recipients that are enabled for Unified Messaging in Exchange
2016

<!-- p.2466 -->

By default, if your Exchange 2016 organization uses Unified Messaging (UM) to consolidate the
email, voice mail, and fax infrastructure, Exchange is configured to journal voice mail
notification and missed call notification messages. You can disable journaling for these types of
messages, but messages that contain UM-generated faxes are always journaled.

To disable journaling for voice mail and missed call notifications, see Enable or disable
journaling for voice mail and missed call notifications.

  ７ Note

  Unified Messaging is not available in Exchange 2019.

Journal rule scope
After you define who you want to journal, you need to define the scope of the messages to
journal. The available scopes are:

     Internal messages only: The source or destination of the message is inside your Exchange
     organization.

     External messages only: The source or destination of the message is outside your
     Exchange organization.

     All messages: The source or destination of the message doesn't matter. Note that a
     journal rule with this scope could potentially journal messages that were already
     journaled by other rules with internal only or external only scopes.

Journaling mailbox
The journaling mailbox is where the journaled messages are delivered. How you configure the
journaling mailbox depends on your organization's policies, regulatory requirements, and legal
requirements. For example, you may be able to configure one journaling mailbox for all journal
rules in your organization, or you may be required to use different journaling mailboxes for
different journal rules.

Notes:

     Journaling mailboxes contain sensitive information, so you need to secure access to them.
     Messages in the journaling mailbox may be part of legal proceedings or subject to
     regulatory requirements. We recommend that you create and enforce clearly-defined
     policies that indicate who has access to a journaling mailbox. Speak with your legal

<!-- p.2467 -->

     representatives to verify that your journaling solution complies with all the laws and
     regulations that apply to your organization.

     A Microsoft 365 or Office 365 mailbox can't be used as a journaling mailbox. If you're
     running a hybrid deployment between on-premises Exchange and Microsoft 365 or Office
     365, you can designate on-premises journaling mailboxes for your Microsoft 365 or Office
     365 and on-premises organizations. You can also deliver journaled messages to an on-
     premises email archiving system or a third-party email archiving service.

     Journaling mailboxes need to accept messages that are at least as large as the maximum
     message size that's available in your organization. Be sure to account for any custom
     maximum message sizes that you've configured on individual mailboxes. For more
     information, see Configure message size limits for a mailbox.

     We recommend that you configure the journaling mailbox to only accept messages from
     the Microsoft Exchange recipient (the only sender of journal reports). Note that you can
     only do this in the Exchange Management Shell. For more information, see Configure
     message delivery restrictions for a mailbox.

     We recommend that you disable the storage quota limits for the journaling mailbox. For
     more information, see Configure storage quotas for a mailbox.

Alternate journaling mailbox

Like other messages, undeliverable journal reports are queued, and delivery is periodically
retried until the message expires (the default value is two days, and is configured by the
MessageExpirationTimeout parameter on the Set-TransportService cmdlet). Unlike other
messages, expired journal reports can't be returned to the sender in a non-delivery report (also
known as an NDR or bounce message), because the sender is the Microsoft Exchange recipient.
Expired journal reports can't be recovered.

If you don't want undeliverable journal reports to queue and eventually expire, you can specify
an alternate journaling mailbox that accepts the NDRs for all undeliverable journal reports
when any journaling mailbox is unavailable (one alternate journaling mailbox for all journaling
mailboxes in your organization). The original journal report is an attachment in the NDR. When
the journaling mailbox becomes available again, you can use the Resend this message feature
in Outlook on the NDRs in the alternate journaling mailbox to send the unaltered delivery
reports to the journaling mailbox.

Before you configure an alternate journaling mailbox, contact your legal representatives. Laws
or regulations that apply to your organization may prohibit all journaled messages from being
stored in the same mailbox.

<!-- p.2468 -->

When you configure an alternate journaling mailbox, you should use the same criteria that you
used when you configured the journaling mailbox.

Notes:

     If the alternate journaling mailbox also becomes unavailable and rejects the NDRs for
     undeliverable journal reports, the original journal reports are lost and can't be recovered.

     You should treat the alternate journaling mailbox as a special dedicated mailbox. Journal
     rules, Inbox rules, and mail flow rules (also known as transport rules) that involve the
     alternate journaling mailbox are ignored.

Journal rule replication
Because journal rules are stored in Active Directory, they're read and applied by the Transport
service on all Mailbox servers in the organization. When you create, modify, or remove a
journal rule, the change is replicated between the domain controllers in your organization. This
allows Exchange to provide a consistent set of journal rules across the organization.

Notes:

     Replication between domain controllers depends on factors that aren't controlled by
     Exchange (for example, the number of Active Directory sites, and the speed of network
     links). Therefore, you need to consider replication delays when you implement journal
     rules in your organization. For more information about Active Directory replication, see
     Introduction to Active Directory Replication and Topology Management Using Windows
     PowerShell.

     Each Mailbox server caches expanded distribution groups to avoid repeated Active
     Directory queries to determine a group's membership. By default, entries in the expanded
     groups cache expire every four hours. Therefore, changes to the group's membership
     can't be applied to journal rules until the expanded groups cache is updated. To force an
     immediate update of the cache on a Mailbox server, restart the Microsoft Exchange
     Transport service. You need to restart the service on each Mailbox server where you want
     to forcibly update the cache.

Troubleshooting
Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange Server        .
If you're having trouble with the alternate journaling mailbox, see KB2829319     .

<!-- p.2469 -->

Journaling procedures in Exchange Server
Article • 04/30/2025

APPLIES TO:        2016    2019         Subscription Edition

Journaling in Exchange Server records inbound and outbound email messages. For more
information, see Journaling in Exchange Server.

This topic shows you how to configure standard journaling (journal messages for all mailboxes
on a mailbox database) and premium journaling (use journal rules to specify the recipients that
are journaled). Some configuration settings are available in the Exchange admin center (EAC),
while others are only available in the Exchange Management Shell.

What do you need to know before you begin?
      Estimated time to complete each procedure: 5 minutes.

      You need to be assigned permissions before you can perform this procedure(s). For more
      information on permissions that you need, see the "Journaling" entry in Messaging policy
      and compliance permissions in Exchange Server.

      To learn how to open the Exchange Management Shell in your on-premises Exchange
      organization, see Open the Exchange Management Shell.

      For information about keyboard shortcuts that may apply to the procedures in this topic,
      see Keyboard shortcuts in the Exchange admin center.

   Tip

  Having problems? Ask for help in the Exchange forums. Visit the forums at: Exchange
  Server , Exchange Online, or Exchange Online Protection . If you're having trouble
  with the JournalingReportDNRTo mailbox, see Transport and Mailbox Rules in Exchange
  Online don't work as expected     .

Procedures for standard journaling
Standard journaling records all messages that are sent to and received by all mailboxes on the
specified mailbox database. You enable journaling by specifying the journaling mailbox for the
database (the mailbox that stores the journaled messages). To disable journaling for the
database, clear the value for the journaling mailbox on the mailbox database. For more
information about the journaling mailbox, see Journaling mailbox.

<!-- p.2470 -->

 Ｕ Caution

 Disabling journaling on a mailbox database may result in your organization being out of
 compliance with any applicable messaging retention policies.

Use the EAC to enable or disable journaling on mailbox
databases
 1. In the EAC, go to Servers > Databases.

 2. Select the mailbox database, and then select Edit (   ).

 3. In the mailbox database properties window that opens, select the Maintenance tab, and
   then perform one of the following procedures:

         Enable journaling: Select Browse next to the Journal recipient field. In the resulting
         dialog box, select the mailbox where you want to store the journaled messages, and
         then select OK.

         Disable journaling: Select Remove X next to the value in the Journal recipient field.

 4. When you're finished, select Save.

<!-- p.2471 -->

Use the Exchange Management Shell to enable or disable
journaling on mailbox databases
To enable journaling on a mailbox database, use the following syntax:

  Set-MailboxDatabase -Identity <MailboxDatabaseIdentity> -JournalRecipient
  <JournalMailboxIdentity>

The following example enables journaling on the mailbox database named Sales Database, and
configures the mailbox named Sales Database Journal Mailbox as the journaling mailbox that
stores the journaled messages.

  Set-MailboxDatabase -Identity "Sales Database" -JournalRecipient "Sales Database
  Journal Mailbox"

To disable journaling on a mailbox database, use the following syntax:

  Set-MailboxDatabase -Identity <MailboxDatabaseIdentity> -JournalRecipient $null

The following example disables journaling on the mailbox database named Sales Database.

  Set-MailboxDatabase -Identity "Sales Database" -JournalRecipient $null

The following example disables journaling on all mailbox databases in the Exchange
organization.

  Get-MailboxDatabase | Set-MailboxDatabase -JournalRecipient $null

How do you know this worked?
To verify that you've successfully enabled or disabled journaling on a mailbox database, use
any of the following procedures:

<!-- p.2472 -->

     In the EAC, go to Servers > Databases > select the database > Edit (     ) > Maintenance,
     and verify whether the Journal recipient field is populated (journaling is enabled), or
     empty (journaling is disabled).

     In the Exchange Management Shell, run the following command to verify the value of the
     JournalRecipient property on all mailbox databases in your organization:

        Get-MailboxDatabase | Format-Table -Auto Name,JournalRecipient

     Send a message to a mailbox on the database, open the journaling mailbox in Outlook or
     Outlook Web App (formerly known as Outlook on the web), and verify whether the
     journaled message (journal report) has or hasn't been delivered to the journaling mailbox.

Procedures for premium journaling
Premium journaling uses journal rules to record messages based on recipients (all recipients or
specified recipients) and scope (internal messages, external messages, or all messages).
Premium journaling requires Exchange Enterprise client access licenses (CALs). For more
information about CALs, see Exchange licensing FAQs     .

Create journal rules
The basic components of a journal rule are:

     Journal recipient: Who you want to journal. You can specify all messages, or messages
     received by or sent by specific recipients (including members of distribution groups).

     Journal rule scope: What you want to journal - internal messages only, external messages
     only, or internal and external messages.

     Journaling mailbox: Where you want to store the journaled messages.

Use the EAC to create journal rules

   1. In the EAC, go to Compliance management > Journal rules, and then select Add (           ).

   2. In New journal rule window that opens, configure the following settings:

          Send journal reports to: Type the alias or email address of the journaling mailbox
          where the journaled messages (journal reports) will be delivered.

<!-- p.2473 -->

          Name: Type a unique, descriptive name for the journal rule.

          If the message is sent to or received from: Specify the journal recipient (whom you
          want to journal). Click the drop-down arrow and select either of the following
          values:

             A specific user or group: In the dialog box that opens, select one recipient, and
             then select OK when you're finished.

             [Apply to all messages]

          Journal the following messages: Specify the scope of the journal rule. Click the
          drop-down arrow and select one of the available values:

             All messages

             Internal messages only

             External messages only

   3. When you're finished, select Save.

Use the Exchange Management Shell to create journal rules

To create journal rules in the Exchange Management Shell, use the following syntax:

<!-- p.2474 -->

  New-JournalRule -Name <RuleName> -JournalEmailAddress <JournalMailboxIdentity> [-
  Recipient <JournalRecipientEmailAddress>] [-Scope <Global | Internal | External>]
  [-Enabled <$true | $false>]

You can use the following settings to create a journal rule named Regulation 123:

      Journal recipient: The user Connie Mayr, whose email address is cmayr@contoso.com.

      Journal rule scope: Internal and external messages (We didn't use the Scope parameter,
      and the default value is Global .).

      Journaling mailbox: The mailbox named Journal Mailbox.

Use these settings in the following example:

  New-JournalRule -Name "Regulation 123" -JournalEmailAddress "Journal Mailbox" -
  Recipient cmayr@contoso.com

The journal rule is enabled (We didn't use the Enabled parameter, and the default value is
$true .).

Note: To create a journal rule that applies to all recipients, don't use the Recipient parameter.

For detailed syntax and parameter information, see New-JournalRule.

How do you know this worked?
To verify that you've successfully created a journal rule, use any of the following procedures:

      In the EAC, go to Compliance management > Journal rules and verify that the new
      journal rule you created is listed.

      In the Exchange Management Shell, run the following command to verify that the new
      journal rule is listed:

            Get-JournalRule | Format-Table -Auto
            Name,Recipient,JournalEmailAddress,Scope,Enabled

      Send a message to a recipient that's in the scope of the journal rule, open the journaling
      mailbox in Outlook or Outlook Web App, and verify that the journaled message (journal

<!-- p.2475 -->

     report) is delivered to the journaling mailbox.

Enable or disable journal rules
By default, when you create a journal rule in the EAC or the Exchange Management Shell, the
rule is enabled. You can only use the Exchange Management Shell to create a journal rule that's
disabled (The Enabled parameter value is $false in the New-JournalRule command.).

After you create a journal rule, you can use the EAC or the Exchange Management Shell to
disable or enable the rule.

  ） Important

  When a journal rule is disabled, any messages that would have normally been journaled
  by the rule aren't journaled. Verify that you don't compromise the regulatory or
  compliance requirements of your organization by disabling a journaling rule.

Use the EAC to enable or disable journal rules
   1. In the EAC, go to Compliance management > Journal rules.

   2. In the list view, select the journal rule and in the On column, clear the checkbox to disable
     the rule, and select the checkbox to enable the rule.

Use the Exchange Management Shell to enable or disable journal rules

To enable or disable journal rules in the Exchange Management Shell, use the following syntax:

  <Disable-JournalRule | Enable-JournalRule> -Identity <JournalRuleIdentity>

The following example disables the journal rule named Contoso Legal.

  Disable-JournalRule -Identity "Contoso Legal"

The following example enables the journal rule named Contoso Legal.

<!-- p.2476 -->

  Enable-JournalRule -Identity "Contoso Legal"

How do you know this worked?
To verify that you've successfully enabled or disabled a journal rule, use any of the following
procedures:

     In the EAC, go to Compliance management > Journal rules, and verify the status of the
     checkbox in the On column for the rule.

     In the Exchange Management Shell, run the following command to verify the value of the
     Enabled property on all journal rules:

        Get-JournalRule | Format-Table -Auto Name,Enabled

     Send a message to a recipient that's in the scope of the journal rule, open the journaling
     mailbox in Outlook or Outlook Web App, and verify whether the journaled message
     (journal report) has or hasn't been delivered to the journaling mailbox.

Modify journal rules
No additional settings are available when you modify a journal rule. The available settings are
the same that were available when you created the rule:

     EAC: Go to Compliance management > Journal rules, and then select Edit (         ). The
     available settings are the same as when you created the rule. For more information, see
     the Use the EAC to create journal rules section.

     Exchange Management Shell: The syntax to modify a journal rule is:

        Set-JournalRule -Identity <JournalRuleIdentity> [-Name <RuleName>] [-
        JournalEmailAddress <JournalMailboxIdentity>] [-Recipient
        <JournalRecipientEmailAddress | $null>] [-Scope <Global | Internal |
        External>]

     You can't use the Set-Journal cmdlet to enable or disable the rule (there's no Enabled
     parameter). To enable or disable the rule, you use the Enable-JournalRule and Disable-
     JournalRule cmdlets as described in the Enable or disable journal rules section.

<!-- p.2477 -->

     For detailed syntax and parameter information, see Set-JournalRule.

Remove journal rules

Use the EAC to remove journal rules

   1. In the EAC, go to Compliance management > Journal rules.

   2. In the list view, select the rule or rules that you want to remove, and then select Delete (
     ).

Use the Exchange Management Shell to remove journal rules
To remove journal rules in the Exchange Management Shell, use the following syntax:

  Remove-JournalRule -Identity <JournalRuleIdentity>

The following example removes the journal rule named Brokerage Journal Rule.

  Remove-JournalRule "Brokerage Journal Rule"

For detailed syntax and parameter information, see Remove-JournalRule.

How do you know this worked?
To verify that you've successfully removed a journal rule, use any of the following procedures:

     In the EAC, go to Compliance management > Journal rules and verify that the rule you
     removed is no longer listed.

     In the Exchange Management Shell, run the following command to verify that the rule
     you removed is no longer listed:

          Get-JournalRule | Format-Table -Auto Name

<!-- p.2478 -->

     Send a message to a recipient that was in the scope of the deleted journal rule, open the
     journaling mailbox in Outlook or Outlook Web App, and verify that the journaled
     message (journal report) isn't delivered to the journaling mailbox.

Enable or disable journaling for voicemail and missed call
notifications
By default, premium journaling will journal voicemail notification and missed call notification
messages that are generated by Unified Messaging (UM) in Exchange 2016. However, you can
disable journaling for these types of messages. Even if you disable journaling for UM
notification messages, messages containing faxes that were generated by the UM service are
always journaled.

  ７ Note

  Unified Messaging isn't available in Exchange 2019.

You can only change this setting in the Exchange Management Shell.

To disable journaling for voicemail and missed call notifications, run the following command:

  Set-TransportConfig -VoicemailJournalingEnabled $false

To enable journaling for voicemail and missed call notifications, run the following command:

  Set-TransportConfig -VoicemailJournalingEnabled $true

How do you know this worked?

To verify that you've successfully enabled or disabled journaling for voicemail and missed call
notifications, run the following command to verify the value of the
VoicemailJournalingEnabled property:

  Get-TransportConfig | Format-List VoicemailJournalingEnabled

<!-- p.2479 -->

Specify the alternate journaling mailbox
For premium journaling, you can specify an alternate journaling mailbox that accepts non-
delivery reports (also known as NDRs or bounce messages) for all undeliverable journal reports
when any journaling mailbox is unavailable (one alternate journaling mailbox for all journaling
mailboxes in your organization). For more information, see Alternate journaling mailbox.

  Ｕ Caution

  If the alternate journaling mailbox also becomes unavailable and rejects the NDRs for
  undeliverable journal reports, the original journal reports are lost and can't be retrieved.

Use the EAC to specify the alternate journaling mailbox

   1. In the EAC, go to Compliance management > Journal rules.

   2. Select Select address next to Send undeliverable journal reports to.

   3. In the NDRs for undeliverable journal reports window that opens, select Browse, select
     the mailbox in the dialog box that appears, select OK, and then select Save.

  ７ Note

  To remove the functionality of the alternate journaling mailbox, select the email address
  next to Send undeliverable journal reports to. In the NDRs for undeliverable journal
  reports window that opens, select Remove X next to the email address, and then select
  Save.

Use the Exchange Management Shell to specify an alternate journaling
mailbox

To specify the alternate journaling mailbox in the Exchange Management Shell, use the
following syntax:

  PowerShell

  Set-TransportConfig -JournalingReportNdrTo <MailboxEmailAddress>

The following example specifies the mailbox that has the email address
altjournalingmbx@contoso.com as the alternate journaling mailbox.

<!-- p.2480 -->

  PowerShell

  Set-TransportConfig -JournalingReportNdrTo altjournalingmbx@contoso.com

  ） Important

  The default value for the JournalingReportNdrTo property is $null. Once it has been set
  to a mailbox email address, it can be set to an alternate address, that is, to another email
  address, but can never be reverted to $null.

How do you know this worked?
To verify that you've successfully specified an alternate journaling mailbox, use any of the
following procedures:

     In the EAC, go to Compliance management > Journal rules and verify the value of Send
     undeliverable journal reports to.

     In the Exchange Management Shell, run the following command to verify the value of the
     JournalingReportNdrTo property:

        Get-TransportConfig | Format-List JournalingReportNdrTo

Enable journal report decryption
Journal report decryption allows premium journaling to save a clear-text copy of IRM-
protected messages in journal reports (along with the original IRM-protected message). If the
message contains any attachments that were protected by the Active Directory Rights
Management Services (AD RMS) cluster in your organization, the attachments are also
decrypted.

To enable journal report decryption, perform the following steps:

   1. Configure the AD RMS super users group. For instructions, see Add the Federation
     Mailbox to the AD RMS Super Users Group.

   2. Run the following command in the Exchange Management Shell:
