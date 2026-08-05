---
title: "How to use this documentation — pages 1281-1320"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p1281-1320
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p1281-1320
family: powershell
documentKind: "doc"
abstract: "When the left operand designates a string the binary * operator creates a new string that contains the one designated by the left operand replicated the number of times designated by the value of the right operand as converted to integer type (§6.4). This operator is left associ"
---

# How to use this documentation — pages 1281-1320

<!-- p.1281 -->

When the left operand designates a string the binary * operator creates a new string
that contains the one designated by the left operand replicated the number of times
designated by the value of the right operand as converted to integer type (§6.4).

This operator is left associative.

Examples:

  PowerShell

  "red" * "3"           # string replicated 3 times
  "red" * 4             # string replicated 4 times
  "red" * 0             # results in an empty string
  "red" * 2.3450D       # string replicated twice
  "red" * 2.7           # string replicated 3 times

7.6.3 Array replication
Description:

When the left operand designates an array the binary * operator creates a new
unconstrained 1-dimensional array that contains the value designated by the left
operand replicated the number of times designated by the value of the right operand as
converted to integer type (§6.4). A replication count of zero results in an array of length
1. If the left operand designates a multidimensional array, it is flattened (§9.12) before
being used.

This operator is left associative.

Examples:

  PowerShell

  $a = [int[]](10,20)                   # [int[]], Length 2*1
  $a * "3"                              # [Object[]], Length 2*3
  $a * 4                                # [Object[]], Length 2*4
  $a * 0                                # [Object[]], Length 2*0
  $a * 2.3450D                          # [Object[]], Length 2*2
  $a * 2.7                              # [Object[]], Length 2*3
  (New-Object 'float[,]' 2,3) * 2       # [Object[]], Length 2*2

7.6.4 Division
Description:

<!-- p.1282 -->

The result of the division operator / is the quotient when the value designated by the
left operand is divided by the value designated by the right operand after the usual
arithmetic conversions (§6.15) have been applied.

If an attempt is made to perform integer or decimal division by zero, an
implementation-defined terminating error is raised.

This operator is left associative.

Examples:

  PowerShell

  10/-10         # int result -1
  12/-10         # double result -1.2
  12/-10D        # decimal result 1.2
  12/10.6        # double result 1.13207547169811
  12/"0xabc"     # double result 0.00436681222707424

If an attempt is made to perform integer or decimal division by zero, a
RuntimeException exception is raised.

7.6.5 Remainder
Description:

The result of the remainder operator % is the remainder when the value designated by
the left operand is divided by the value designated by the right operand after the usual
arithmetic conversions (§6.15) have been applied.

If an attempt is made to perform integer or decimal division by zero, an
implementation-defined terminating error is raised.

Examples:

  PowerShell

  10 % 3             # int result 1
  10.0 % 0.3         # double result 0.1
  10.00D % "0x4"     # decimal result 2.00

If an attempt is made to perform integer or decimal division by zero, a
RuntimeException exception is raised.

<!-- p.1283 -->

7.7 Additive operators
Syntax:

  Syntax

  additive-expression:
      primary-expression + new-lines~opt~ expression
      primary-expression dash new-lines~opt~ expression

  dash: one of
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

7.7.1 Addition
Description:

The result of the addition operator + is the sum of the values designated by the two
operands after the usual arithmetic conversions (§6.15) have been applied.

This operator is left associative.

Examples:

  PowerShell

  12 + -10L          # long result 2
  -10.300D + 12      # decimal result 1.700
  10.6 + 12          # double result 22.6
  12 + "0xabc"       # int result 2760

7.7.2 String concatenation
Description:

When the left operand designates a string the binary + operator creates a new string
that contains the value designated by the left operand followed immediately by the
value(s) designated by the right operand as converted to type string (§6.8).

This operator is left associative.

Examples:

<!-- p.1284 -->

  PowerShell

  "red" + "blue"          # "redblue"
  "red" + "123"           # "red123"
  "red" + 123             # "red123"
  "red" + 123.456e+5      # "red12345600"
  "red" + (20,30,40)      # "red20 30 40"

7.7.3 Array concatenation
Description:

When the left operand designates an array the binary + operator creates a new
unconstrained 1-dimensional array that contains the elements designated by the left
operand followed immediately by the value(s) designated by the right operand.
Multidimensional arrays present in either operand are flattened (§9.12) before being
used.

This operator is left associative.

Examples:

  PowerShell

  $a = [int[]](10,20)                  # [int[]], Length 2
  $a + "red"                           # [Object[]], Length 3
  $a + 12.5,$true                      # [Object[]], Length 4
  $a + (New-Object 'float[,]' 2,3)     # [Object[]], Length 8
  (New-Object 'float[,]' 2,3) + $a     # [Object[]], Length 8

7.7.4 Hashtable concatenation
Description:

When both operands designate Hashtables the binary + operator creates a new
Hashtable that contains the elements designated by the left operand followed
immediately by the elements designated by the right operand.

If the Hashtables contain the same key, an implementation-defined terminating error is
raised.

This operator is left associative.

Examples:

<!-- p.1285 -->

  PowerShell

  $h1 = @{ FirstName = "James"; LastName = "Anderson" }
  $h2 = @{ Dept = "Personnel" }
  $h3 = $h1 + $h2      # new Hashtable, Count = 3

If the Hashtables contain the same key, an exception of type BadOperatorArgument is
raised.

7.7.5 Subtraction
Description:

The result of the subtraction operator - is the difference when the value designated by
the right operand is subtracted from the value designated by the left operand after the
usual arithmetic conversions (§6.15) have been applied. The subtraction operator can be
any one of the dash characters listed in §7.7.

This operator is left associative.

Examples:

  PowerShell

  12 - -10L         # long result 22
  -10.300D - 12     # decimal result -22.300
  10.6 - 12         # double result -1.4
  12 - "0xabc"      # int result -2736

7.8 Comparison operators
Syntax:

  Syntax

  comparison-expression:
      primary-expression comparison-operator new-lines~opt~ expression

  comparison-operator:
      equality-operator
      relational-operator
      containment-operator
      type-operator
      like-operator
      match-operator

<!-- p.1286 -->

Description:

The type of the value designated by the left operand determines how the value
designated by the right operand is converted (§6), if necessary, before the comparison is
done.

Some comparison operators have two variants, one that is case sensitive ( -c<operator> ),
and one that isn't case sensitive ( -i<operator> ). The -<operator> version is equivalent
to -i<operator> . Case sensitivity is meaningful only with comparisons of values of type
string. In non-string comparison contexts, the two variants behave the same.

These operators are left associative.

7.8.1 Equality and relational operators
Syntax:

  Syntax

  equality-operator: one of
      dash eq     dash ceq         dash ieq
      dash ne     dash cne         dash ine

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

  relational-operator: one of
      dash lt     dash clt    dash ilt
      dash le     dash cle    dash ile
      dash gt     dash cgt    dash igt
      dash ge     dash cge    dash ige

Description:

There are two equality operators: equality ( -eq ) and inequality ( -ne ); and four relational
operators: less-than ( -lt ), less-than-or-equal-to ( -le ), greater-than ( -gt ), and greater-
than-or-equal-to ( -ge ). Each of these has two variants (§7.8).

For two strings to compare equal, they must have the same length and contents, and
letter case, if appropriate.

If the value designated by the left operand is not a collection, the result has type bool .
Otherwise, the result is a possibly empty unconstrained 1-dimensional array containing

<!-- p.1287 -->

the elements of the collection that test True when compared to the value designated by
the right operand.

Examples:

  PowerShell

  10 -eq "010"                # True, int comparison
  "010" -eq 10                # False, string comparison
  "RED" -eq "Red"             # True, case-insensitive comparison
  "RED" -ceq "Red"            # False, case-sensitive comparison
  "ab" -lt "abc"              # True

  10,20,30,20,10 -ne 20       # 10,30,10, Length 3
  10,20,30,20,10 -eq 40       # Length 0
  10,20,30,20,10 -ne 40       # 10,20,30,20,10, Length 5
  10,20,30,20,10 -gt 25       # 30, Length 1
  0,1,30 -ne $true            # 0,30, Length 2
  0,"00" -eq "0"              # 0 (int), Length 1

7.8.2 Containment operators
Syntax:

  Syntax

  containment-operator: one of
      dash contains       dash ccontains               dash icontains
      dash notcontains    dash cnotcontains            dash inotcontains
      dash in             dash cin                     dash iin
      dash notin          dash cnotin                  dash inotin

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

There are four containment operators: contains ( -contains ), does-not-contain ( -
notcontains ), in ( -in ) and not-in ( -notin ). Each of these has two variants (§7.8).

The containment operators return a result of type bool that indicates whether a value
occurs (or does not occur) at least once in the elements of an array. With -contains and
-notcontains , the value is designated by the right operand and the array is designated

<!-- p.1288 -->

by the left operand. With -in and -notin , the operands are reversed. The value is
designated by the left operand and the array is designated by the right operand.

For the purposes of these operators, if the array operand has a scalar value, the scalar
value is treated as an array of one element.

Examples:

  PowerShell

  10,20,30,20,10 -contains 20         # True
  10,20,30,20,10 -contains 42.9       # False
  10,20,30 -contains "10"             # True
  "10",20,30 -contains 10             # True
  "010",20,30 -contains 10            # False
  10,20,30,20,10 -notcontains 15      # True
  "Red",20,30 -ccontains "RED"        # False

7.8.3 Type testing and conversion operators
Syntax:

  Syntax

  type-operator: one of
      dash is
      dash as

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The type operator -is tests whether the value designated by the left operand has the
type, or is derived from a type that has the type, designated by the right operand. The
right operand must designate a type or a value that can be converted to a type (such as
a string that names a type). The type of the result is bool . The type operator -isnot
returns the logical negation of the corresponding -is form.

The type operator -as attempts to convert the value designated by the left operand to
the type designated by the right operand. The right operand must designate a type or a
value that can be converted to a type (such as a string that names a type). If the

<!-- p.1289 -->

conversion fails, $null is returned; otherwise, the converted value is returned and the
return type of that result is the runtime type of the converted value.

Examples:

  PowerShell

  $a = 10               # value 10 has type int
  $a -is [int]          # True

  $t = [int]
  $a -isnot $t       # False
  $a -is "int"       # True
  $a -isnot [double] # True

  $x = [int[]](10,20)
  $x -is [int[]]     # True

  $a = "abcd"           # string is derived from object
  $a -is [Object]       # True

  $x = [double]
  foreach ($t in [int],$x,[decimal],"string") {
      $b = (10.60D -as $t) * 2 # results in int 22, double 21.2
  }                             # decimal 21.20, and string "10.6010.60"

7.8.4 Pattern matching and text manipulation operators

7.8.4.1 The -like and -notlike operators

Syntax:

  Syntax

  like-operator: one of
      dash like       dash clike           dash ilike
      dash notlike    dash cnotlike        dash inotlike

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

If the left operand does not designate a collection, the result has type bool . Otherwise,
the result is a possibly empty unconstrained 1-dimensional array containing the

<!-- p.1290 -->

elements of the collection that test True when compared to the value designated by the
right operand. The right operand may designate a string that contains wildcard
expressions (§3.15). These operators have two variants (§7.8).

Examples:

  PowerShell

  "Hello" -like "h*"                        # True, starts with h
  "Hello" -clike "h*"                       # False, does not start with lowercase
  h
  "Hello" -like "*l*"                       # True, has an l in it somewhere
  "Hello" -like "??l"                       # False, no length match

  "-abc" -like "[-xz]*"                     # True, - is not a range separator
  "#$%\^&" -notlike "*[A-Za-z]"             # True, does not end with alphabetic
  character
  "He" -like "h[aeiou]?*"                   # False, need at least 3 characters
  "When" -like "*[?]"                       # False, ? is not a wildcard character
  "When?" -like "*[?]"                      # True, ? is not a wildcard character

  "abc","abbcde","abcgh" -like "abc*"       # object[2], values
  "abc" and "abcgh"

7.8.4.2 The -match and -notmatch operators

Syntax:

  Syntax

  match-operator: one of
      dash match      dash cmatch          dash imatch
      dash notmatch   dash cnotmatch       dash inotmatch

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

If the left operand does not designate a collection, the result has type bool and if that
result is $true , the elements of the Hashtable $Matches are set to the strings that match
(or do-not-match) the value designated by the right operand. Otherwise, the result is a
possibly empty unconstrained 1-dimensional array containing the elements of the
collection that test True when compared to the value designated by the right operand,

<!-- p.1291 -->

and $Matches is not set. The right operand may designate a string that contains regular
expressions (§3.16), in which case, it is referred to as a pattern. These operators have two
variants (§7.8).

These operators support submatches (§7.8.4.6).

Examples:

  PowerShell

  "Hello" -match ".l"                           # True, $Matches key/value is 0/"el"
  "Hello" -match '\^h.*o$'                      # True, $Matches key/value is
  0/"Hello"
  "Hello" -cmatch '\^h.*o$'                     # False, $Matches not set
  "abc\^ef" -match ".\\\^e"                     # True, $Matches key/value is
  0/"c\^e"

  "abc" -notmatch "[A-Za-z]"                    # False
  "abc" -match "[\^A-Za-z]"                     # False
  "He" -match "h[aeiou]."                       # False, need at least 3 characters
  "abc","abbcde","abcgh" -match "abc.*"         # Length is 2, values "abc", "abcgh"

7.8.4.3 The -replace operator
Syntax:

  Syntax

  binary-replace-operator: one of
      dash replace    dash creplace          dash ireplace

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The -replace operator allows text replacement in one or more strings designated by
the left operand using the values designated by the right operand. This operator has
two variants (§7.8). The right operand has one of the following forms:

      The string to be located, which may contain regular expressions (§3.16). In this
      case, the replacement string is implicitly "".
      An array of 2 objects containing the string to be located, followed by the
      replacement string.

<!-- p.1292 -->

If the left operand designates a string, the result has type string. If the left operand
designates a 1-dimensional array of string, the result is an unconstrained 1-dimensional
array, whose length is the same as for left operand's array, containing the input strings
after replacement has completed.

This operator supports submatches (§7.8.4.6).

Examples:

  PowerShell

  "Analogous","an apple" -replace "a","*"              # "*n*logous","*n *pple"
  "Analogous" -creplace "[aeiou]","?"                  # "An?l?g??s"
  "Analogous","an apple" -replace '\^a',"%%A"          # "%%Analogous","%%An apple"
  "Analogous" -replace "[aeiou]",'$&$&'                # "AAnaaloogoouus"

7.8.4.4 The binary -join operator
Syntax:

  Syntax

  binary-join-operator: one of
      dash join

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The binary -join operator produces a string that is the concatenation of the value of
one or more objects designated by the left operand after having been converted to
string (§6.7), if necessary. The string designated by the right operand is used to separate
the (possibly empty) values in the resulting string.

The left operand can be a scalar value or a collection.

Examples:

  PowerShell

  (10, 20, 30) -join "\|"         # result is "10\|20\|30"
  12345 -join ","                 # result is "12345", no separator needed

<!-- p.1293 -->

  ($null,$null) -join "<->"       # result is "<->", two zero-length values

7.8.4.5 The binary -split operator
Syntax:

  Syntax

  binary-split-operator: one of
      dash split      dash csplit            dash isplit

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The binary -split operator splits one or more strings designated by the left operand,
returning their subparts in a constrained 1-dimensional array of string. This operator has
two variants (§7.8). The left operand can designate a scalar value or an array of strings.
The right operand has one of the following forms:

      A delimiter string
      An array of 2 objects containing a delimiter string followed by a numeric split count
      An array of 3 objects containing a delimiter string, a numeric split count, and an
      options string
      A script block
      An array of 2 objects containing a script block followed by a numeric split count

The delimiter string may contain regular expressions (§3.16). It is used to locate subparts
with the input strings. The delimiter is not included in the resulting strings. If the left
operand designates an empty string, that results in an empty string element. If the
delimiter string is an empty string, it is found at every character position in the input
strings.

By default, all subparts of the input strings are placed into the result as separate
elements; however, the split count can be used to modify this behavior. If that count is
negative, zero, or greater than or equal to the number of subparts in an input string,
each subpart goes into a separate element. If that count is less than the number of
subparts in the input string, there are count elements in the result, with the final element
containing all of the subparts beyond the first count - 1 subparts.

<!-- p.1294 -->

An options string contains zero or more option names with each adjacent pair separated
by a comma. Leading, trailing, and embedded whitespace is ignored. Option names may
be in any order and are case-sensitive.

If an options string contains the option name SimpleMatch, it may also contain the
option name IgnoreCase. If an options string contains the option name RegexMatch or
it does not contain either RegexMatch or SimpleMatch, it may contain any option name
except SimpleMatch. However, it must not contain both Multiline and Singleline.

Here is the set of option names:

                                                                                 ﾉ     Expand table

 Option                    Description

 CultureInvariant          Ignores cultural differences in language when evaluating the delimiter.

 ExplicitCapture           Ignores non-named match groups so that only explicit capture groups
                           are returned in the result list.

 IgnoreCase                Force case-insensitive matching, even if -csplit is used.

 IgnorePatternWhitespace   Ignores unescaped whitespace and comments marked with the
                           number sign ( # ).

 Multiline                 This mode recognizes the start and end of lines and strings. The
                           default mode is Singleline.

 RegexMatch                Use regular expression matching to evaluate the delimiter. This is the
                           default.

 SimpleMatch               Use simple string comparison when evaluating the delimiter.

 Singleline                This mode recognizes only the start and end of strings. It is the
                           default mode.

The script block (§7.1.8) specifies the rules for determining the delimiter, and must
evaluate to type bool.

Examples:

  PowerShell

  "one,forty two,," -split ","                       # 5 strings: "one" "forty two" ""
  ""

  "abc","de" -split ""                               # 9 strings: "" "a" "b" "c" "" ""
  "d" "e" ""

<!-- p.1295 -->

  "ab,cd","1,5,7,8" -split ",", 2                  # 4 strings: "ab" "cd" "1" "5,7,8"

  "10X20x30" -csplit "X", 0, "SimpleMatch"         # 2 strings: "10" "20x30"

  "analogous" -split "[AEIOU]", 0, "RegexMatch, IgnoreCase"
                                            # 6 strings: "" "n" "l" "g" "" "s"

  "analogous" -split { $_ -eq "a" -or $_ -eq "o" }, 4
                                            # 4 strings: "" "n" "l" "gous"

7.8.4.6 Submatches
The pattern being matched by -match , -notmatch , and -replace may contain subparts
(called submatches) delimited by parentheses. Consider the following example:

"red" -match "red"

The result is $true and key 0 of $Matches contains "red", that part of the string
designated by the left operand that exactly matched the pattern designated by the right
operand.

In the following example, the whole pattern is a submatch:

"red" -match "(red)"

As before, key 0 contains "red"; however, key 1 also contains "red", which is that part of
the string designated by the left operand that exactly matched the submatch.

Consider the following, more complex, pattern:

"red" -match "((r)e)(d)"

This pattern allows submatches of "re", "r", "d", or "red".

Again, key 0 contains "red". Key 1 contains "re", key 2 contains "r", and key 3 contains
"d". The key/value pairs are in matching order from left-to-right in the pattern, with
longer string matches preceding shorter ones.

In the case of -replace , the replacement text can access the submatches via names of
the form $n , where the first match is $1 , the second is $3 , and so on. For example,

  PowerShell

  "Monday morning" -replace '(Monday|Tuesday)
  (morning|afternoon|evening)','the $2 of $1'

<!-- p.1296 -->

The resulting string is "the morning of Monday".

Instead of having keys in $Matches be zero-based indexes, submatches can be named
using the form ?<*name*> . For example, "((r)e)(d)" can be written with three named
submatches, m1 , m2 , and m3 , as follows: "(?<m1>(?<m2>r)e)(?<m3>d)" .

7.8.5 Shift operators
Syntax:

  Syntax

  shift-operator: one of
      dash shl
      dash shr

  dash:
      - (U+002D)
      EnDash character (U+2013)
      EmDash character (U+2014)
      Horizontal bar character (U+2015)

Description:

The shift left ( -shl ) operator and shift right ( -shr ) operator convert the value designed
by the left operand to an integer type and the value designated by the right operand to
int, if necessary, using the usual arithmetic conversions (§6.15).

The shift left operator shifts the left operand left by a number of bits computed as
described below. The low-order empty bit positions are set to zero.

The shift right operator shifts the left operand right by a number of bits computed as
described below. The low-order bits of the left operand are discarded, the remaining
bits shifted right. When the left operand is a signed value, the high-order empty bit
positions are set to zero if the left operand is non-negative and set to one if the left
operand is negative. When the left operand is an unsigned value, the high-order empty
bit positions are set to zero.

When the left operand has type int, the shift count is given by the low-order five bits of
the right operand. When the right operand has type long, the shift count is given by the
low-order six bits of the right operand.

Examples:

  PowerShell

<!-- p.1297 -->

  0x0408 -shl 1                  # int with value 0x0810
  0x0408 -shr 3                  # int with value 0x0081
  0x100000000 -shr 0xfff81       # long with value 0x80000000

7.9 Bitwise operators
Syntax:

  Syntax

  bitwise-expression:
      unary-expression -band new-lines~opt~ unary-expression
      unary-expression -bor new-lines~opt~ unary-expression
      unary-expression -bxor new-lines~opt~ unary-expression

Description:

The bitwise AND operator -band , the bitwise OR operator -bor , and the bitwise XOR
operator -bxor convert the values designated by their operands to integer types, if
necessary, using the usual arithmetic conversions (§6.15). After conversion, if both values
have type int that is the type of the result. Otherwise, if both values have type long, that
is the type of the result. If one value has type int and the other has type long, the type
of the result is long. Otherwise, the expression is ill formed. The result is the bitwise
AND, bitwise OR, or bitwise XOR, respectively, of the possibly converted operand values.

These operators are left associative. They are commutative if neither operand contains a
side effect.

Examples:

  PowerShell

  0x0F0F -band 0xFE        # int with value 0xE
  0x0F0F -band 0xFEL       # long with value 0xE
  0x0F0F -band 14.6        # long with value 0xF

  0x0F0F -bor 0xFE         # int with value 0xFFF
  0x0F0F -bor 0xFEL        # long with value 0xFFF
  0x0F0F -bor 14.40D       # long with value 0xF0F

  0x0F0F -bxor 0xFE        # int with value 0xFF1
  0x0F0F -bxor 0xFEL       # long with value 0xFF1
  0x0F0F -bxor 14.40D      # long with value 0xF01
  0x0F0F -bxor 14.6        # long with value 0xF00

<!-- p.1298 -->

7.10 Logical operators
Syntax:

  Syntax

  logical-expression:
      unary-expression -and new-lines~opt~ unary-expression
      unary-expression -or new-lines~opt~ unary-expression
      unary-expression -xor new-lines~opt~ unary-expression

Description:

The logical AND operator -and converts the values designated by its operands to bool ,
if necessary (§6.2). The result is the logical AND of the possibly converted operand
values, and has type bool . If the left operand evaluates to False the right operand is not
evaluated.

The logical OR operator -or converts the values designated by its operands to bool , if
necessary (§6.2). The result is the logical OR of the possibly converted operand values,
and has type bool . If the left operand evaluates to True the right operand is not
evaluated.

The logical XOR operator -xor converts the values designated by its operands to bool
(§6.2). The result is the logical XOR of the possibly converted operand values, and has
type bool .

These operators are left associative.

Examples:

  PowerShell

  $j = 10
  $k = 20
  ($j -gt 5) -and (++$k -lt 15)         # True -and False -> False
  ($j -gt 5) -and ($k -le 21)           # True -and True -> True
  ($j++ -gt 5) -and ($j -le 10)         # True -and False -> False
  ($j -eq 5) -and (++$k -gt 15)         # False -and True -> False

  $j = 10
  $k = 20
  ($j++ -gt 5) -or (++$k -lt 15)        # True -or False -> True
  ($j -eq 10) -or ($k -gt 15)           # False -or True -> True
  ($j -eq 10) -or (++$k -le 20)         # False -or False -> False

  $j = 10

<!-- p.1299 -->

  $k = 20
  ($j++ -gt 5) -xor (++$k -lt 15) # True -xor False -> True
  ($j -eq 10) -xor ($k -gt 15)    # False -xor True -> True
  ($j -gt 10) -xor (++$k -le 25) # True -xor True -> False

7.11 Assignment operators
Syntax:

  Syntax

  assignment-expression:
      expression assignment-operator statement

  assignment-operator: *one of
      =   dash =   +=   *=   /=         %=

Description:

An assignment operator stores a value in the writable location designated by expression.
For a discussion of assignment-operator = see §7.11.1. For a discussion of all other
assignment operators see §7.11.2.

An assignment expression has the value designated by expression after the assignment
has taken place; however, that assignment expression does not itself designate a
writable location. If expression is type-constrained (§5.3), the type used in that constraint
is the type of the result; otherwise, the type of the result is the type after the usual
arithmetic conversions (§6.15) have been applied.

This operator is right associative.

7.11.1 Simple assignment
Description:

In simple assignment ( = ), the value designated by statement replaces the value stored in
the writable location designated by expression. However, if expression designates a non-
existent key in a Hashtable, that key is added to the Hashtable with an associated value
of the value designated by statement.

As shown by the grammar, expression may designate a comma-separated list of writable
locations. This is known as multiple assignment. statement designates a list of one or
more comma-separated values. The commas in either operand list are part of the
multiple-assignment syntax and do not represent the binary comma operator. Values are

<!-- p.1300 -->

taken from the list designated by statement, in lexical order, and stored in the
corresponding writable location designated by expression. If the list designated by
statement has fewer values than there are expression writable locations, the excess
locations take on the value $null . If the list designated by statement has more values
than there are expression writable locations, all but the right-most expression location
take on the corresponding statement value and the right-most expression location
becomes an unconstrained 1-dimensional array with all the remaining statement values
as elements.

For statements that have values (§8.1.2), statement can be a statement.

Examples:

  PowerShell

  $a = 20; $b = $a + 12L                  # $b has type long, value 22
  $hypot = [Math]::Sqrt(3*3 + 4*4)        # type double, value 5
  $a = $b = $c = 10.20D                   # all have type decimal, value 10.20
  $a = (10,20,30),(1,2)                   # type [Object[]], Length 2
  [int]$x = 10.6                          # type int, value 11
  [long]$x = "0xabc"                      # type long, value 0xabc
  $a = [float]                            # value type literal [float]
  $i,$j,$k = 10,"red",$true               # $i is 10, $j is "red", $k is True
  $i,$j = 10,"red",$true                  # $i is 10, $j is [Object[]], Length 2
  $i,$j = (10,"red"),$true                # $i is [Object[]], Length 2, $j is True
  $i,$j,$k = 10                           # $i is 10, $j is $null, $k is $null

  $h = @{}
  [int] $h.Lower, [int] $h.Upper = -split "10 100"

  $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
  $h1.Dept = "Finance"               # adds element Finance
  $h1["City"] = "New York"           # adds element City

  [int]$Variable:v = 123.456         # v takes on the value 123
  ${E:output.txt} = "a"              # write text to the given file
  $Env:MyPath = "X:\data\file.txt"   # define the environment variable
  $Function:F = { param ($a, $b) "Hello there, $a, $b" }
  F 10 "red"                         # define and invoke a function
  function Demo { "Hi there from inside Demo" }
  $Alias:A = "Demo"                  # create alias for function Demo
  A                                  # invoke function Demo via the alias

7.11.2 Compound assignment
Description:

<!-- p.1301 -->

A compound assignment has the form E1 op= E2 , and is equivalent to the simple
assignment expression E1 = E1 op (E2) except that in the compound assignment case
the expression E1 is evaluated only once. If expression is type-constrained (§5.3), the
type used in that constraint is the type of the result; otherwise, the type of the result is
determined by op. For *= , see §7.6.1, §7.6.2, §7.6.3; for /= , see §7.6.4; for %= , see §7.6.5;
for += , see §7.7.1, §7.7.2, §7.7.3; for -= , see §7.7.5.

  ７ Note

  An operand designating an unconstrained value of numeric type may have its type
  changed by an assignment operator when the result is stored.

Examples:

  PowerShell

  $a = 1234; $a *= (3 + 2)         # type is int, value is 1234 * (3 + 2)
  $b = 10,20,30                    # $b[1] has type int, value 20
  $b[1] /= 6                       # $b[1] has type double, value 3.33...

  $i = 0
  $b = 10,20,30
  $b[++$i] += 2                    # side effect evaluated only once

  [int]$Variable:v = 10            # v takes on the value 10
  $Variable:v -= 3                 # 3 is subtracted from v

  ${E:output.txt} = "a"            # write text to the given file
  ${E:output.txt} += "b"           # append text to the file giving ab
  ${E:output.txt} *= 4             # replicate ab 4 times giving abababab

7.12 Redirection operators
Syntax:

  Syntax

  pipeline:
      expression redirections~opt~ pipeline-tail~opt~
      command verbatim-command-argument~opt~ pipeline-tail~opt~

  redirections:
      redirection
      redirections redirection

  redirection:

<!-- p.1302 -->

         merging-redirection-operator
         file-redirection-operator redirected-file-name

     redirected-file-name:
         command-argument
         primary-expression

     file-redirection-operator: one of
         >   >>   2>   2>>   3>   3>>        4>     4>>
         5> 5>> 6>     6>>   >    >>         <

     merging-redirection-operator: one of
         >&1   2>&1   3>&1   4>&1   5>&1          6>&1
         >&2   1>&2   3>&2   4>&2   5>&2          6>&2

Description:

The redirection operator > takes the standard output from the pipeline and redirects it
to the location designated by redirected-file-name, overwriting that location's current
contents.

The redirection operator >> takes the standard output from the pipeline and redirects it
to the location designated by redirected-file-name, appending to that location's current
contents, if any. If that location does not exist, it is created.

The redirection operator with the form n> takes the output of stream n from the
pipeline and redirects it to the location designated by redirected-file-name, overwriting
that location's current contents.

The redirection operator with the form n>> takes the output of stream n from the
pipeline and redirects it to the location designated by redirected-file-name, appending
to that location's current contents, if any. If that location does not exist, it is created.

The redirection operator with the form m>&n writes output from stream m to the same
location as stream n.

The following are the valid streams:

                                                                              ﾉ   Expand table

 Stream     Description

 1          Standard output stream

 2          Error output stream

 3          Warning output stream

<!-- p.1303 -->

 Stream       Description

 4            Verbose output stream

 5            Debug output stream

 *            Standard output, error output, warning output, verbose output, and debug output
              streams

The redirection operators 1>&2 , 6> , 6>> and < are reserved for future use.

If on output the value of redirected-file-name is $null , the output is discarded.

Ordinarily, the value of an expression containing a top-level side effect is not written to
the pipeline unless that expression is enclosed in a pair of parentheses. However, if such
an expression is the left operand of an operator that redirects standard output, the value
is written.

Examples:

     PowerShell

     $i = 200                             # pipeline gets nothing
     $i                                   # pipeline gets result
     $i > output1.txt                     # result redirected to named file
     ++$i >> output1.txt                  # result appended to named file
     type file1.txt 2> error1.txt         # error output redirected to named file
     type file2.txt 2>> error1.txt        # error output appended to named file
     dir -Verbose 4> verbose1.txt         # verbose output redirected to named file

     # Send all output to output2.txt
     dir -Verbose -Debug -WarningAction Continue *> output2.txt

     # error output redirected to named file, verbose output redirected
     # to the same location as error output
     dir -Verbose 4>&2 2> error2.txt

<!-- p.1304 -->

8. Statements

Editorial note

  ） Important

  The Windows PowerShell Language Specification 3.0 was published in December 2012 and
  is based on Windows PowerShell 3.0. This specification does not reflect the current state
  of PowerShell. There is no plan to update this documentation to reflect the current state.
  This documentation is presented here for historical reference.

  The specification document is available as a Microsoft Word document from the Microsoft
  Download Center at: https://www.microsoft.com/download/details.aspx?id=36389
  That Word document has been converted for presentation here on Microsoft Learn.
  During conversion, some editorial changes have been made to accommodate formatting
  for the Docs platform. Some typos and minor errors have been corrected.

8.1 Statement blocks and lists
Syntax:

   Tip

  The ~opt~ notation in the syntax definitions indicates that the lexical entity is optional in
  the syntax.

 Syntax

 statement-block:
     new-lines~opt~ { statement-list~opt~ new-lines~opt~ }

 statement-list:
     statement
     statement-list statement

 statement:
     if-statement
     label~opt~ labeled-statement
     function-statement

<!-- p.1305 -->

      flow-control-statement statement-terminator
      trap-statement
      try-statement
      data-statement
      inlinescript-statement
      parallel-statement
      sequence-statement
      pipeline statement-terminator

 statement-terminator:
     ;
     new-line-character

Description:

A statement specifies some sort of action that is to be performed. Unless indicated otherwise
within this clause, statements are executed in lexical order.

A statement-block allows a set of statements to be grouped into a single syntactic unit.

8.1.1 Labeled statements
Syntax:

 Syntax

 labeled-statement:
     switch-statement
     foreach-statement
     for-statement
     while-statement
     do-statement

Description:

An iteration statement (§8.4) or a switch statement (§8.6) may optionally be preceded
immediately by one statement label, label. A statement label is used as the optional target of a
break (§8.5.1) or continue (§8.5.2) statement. However, a label does not alter the flow of
control.

White space is not permitted between the colon ( : ) and the token that follows it.

Examples:

 PowerShell

<!-- p.1306 -->

 :go_here while ($j -le 100) {
     # ...
 }

 :labelA
 for ($i = 1; $i -le 5; ++$i) {
     :labelB
     for ($j = 1; $j -le 3; ++$j) {
         :labelC
         for ($k = 1; $k -le 2; ++$k) {
             # ...
         }
     }
 }

8.1.2 Statement values
The value of a statement is the cumulative set of values that it writes to the pipeline. If the
statement writes a single scalar value, that is the value of the statement. If the statement writes
multiple values, the value of the statement is that set of values stored in elements of an
unconstrained 1-dimensional array, in the order in which they were written. Consider the
following example:

$v = for ($i = 10; $i -le 5; ++$i) { }

There are no iterations of the loop and nothing is written to the pipeline. The value of the
statement is $null .

$v = for ($i = 1; $i -le 5; ++$i) { }

Although the loop iterates five times nothing is written to the pipeline. The value of the
statement is $null.

$v = for ($i = 1; $i -le 5; ++$i) { $i }

The loop iterates five times each time writing to the pipeline the int value $i . The value of the
statement is object[] of Length 5.

$v = for ($i = 1; $i -le 5; ) { ++$i }

Although the loop iterates five times nothing is written to the pipeline. The value of the
statement is $null .

$v = for ($i = 1; $i -le 5; ) { (++$i) }

<!-- p.1307 -->

The loop iterates five times with each value being written to the pipeline. The value of the
statement is object[] of Length 5.

$i = 1; $v = while ($i++ -lt 2) { $i }

The loop iterates once. The value of the statement is the int with value 2.

Here are some other examples:

 PowerShell

 # if $count is not currently defined then define it with int value 10
 $count = if ($count -eq $null) { 10 } else { $count }

 $i = 1
 $v = while ($i -le 5) {
     $i                       # $i is written to the pipeline
     if ($i -band 1) {

          "odd"               # conditionally written to the pipeline

      }

      ++$i                    # not written to the pipeline

 }
 # $v is object[], Length 8, value 1,"odd",2,3,"odd",4,5,"odd"

8.2 Pipeline statements
Syntax:

 Syntax

 pipeline:
     assignment-expression
     expression redirections~opt~ pipeline-tail~opt~
     command verbatim-command-argument~opt~ pipeline-tail~opt~

 assignment-expression:
     expression assignment-operator statement

 pipeline-tail:
     | new-lines~opt~ command
     | new-lines~opt~ command pipeline-tail

 command:
     command-name command-elements~opt~
     command-invocation-operator command-module~opt~ command-name-expr command-

<!-- p.1308 -->

 elements~opt~

 command-invocation-operator: one of
     &   .

 command-module:
     primary-expression

 command-name:
     generic-token
     generic-token-with-subexpr

 generic-token-with-subexpr:
     No whitespace is allowed between ) and command-name.
     generic-token-with-subexpr-start statement-list~opt~ )

 command-namecommand-name-expr:
     command-name

 primary-expressioncommand-elements:
     command-element
     command-elements command-element

 command-element:
     command-parameter
     command-argument
     redirection

 command-argument:
     command-name-expr

 verbatim-command-argument:
     --% verbatim-command-argument-chars

Description:

redirections is discussed in §7.12; assignment-expression is discussed in §7.11; and the
command-invocation-operator dot ( . ) is discussed in §3.5.5. For a discussion of argument-to-
parameter mapping in command invocations, see §8.14.

The first command in a pipeline is an expression or a command invocation. Typically, a
command invocation begins with a command-name, which is usually a bare identifier.
command-elements represents the argument list to the command. A newline or n unescaped
semicolon terminates a pipeline.

A command invocation consists of the command's name followed by zero or more arguments.
The rules governing arguments are as follows:

<!-- p.1309 -->

     An argument that is not an expression, but which contains arbitrary text without
     unescaped white space, is treated as though it were double quoted. Letter case is
     preserved.

     Variable substitution and sub-expression expansion (§2.3.5.2) takes place inside
     expandable-string-literals and expandable-here-string-literals.

     Text inside quotes allows leading, trailing, and embedded white space to be included in
     the argument's value. [Note: The presence of whitespace in a quoted argument does not
     turn a single argument into multiple arguments. end note]

     Putting parentheses around an argument causes that expression to be evaluated with the
     result being passed instead of the text of the original expression.

     To pass an argument that looks like a [switch] parameter (§2.3.4) but is not intended as
     such, enclose that argument in quotes.

     When specifying an argument that matches a parameter having the [switch] type
     constraint (§8.10.5), the presence of the argument name on its own causes that parameter
     to be set to $true . However, the parameter's value can be set explicitly by appending a
     suffix to the argument. For example, given a type constrained parameter p, an argument
     of -p:$true sets p to True, while -p:$false sets p to False.

     An argument of -- indicates that all arguments following it are to be passed in their
     actual form as though double quotes were placed around them.

     An argument of --% indicates that all arguments following it are to be passed with
     minimal parsing and processing. This argument is called the verbatim parameter.
     Arguments after the verbatim parameter are not PowerShell expressions even if they are
     syntactically valid PowerShell expressions.

If the command type is Application, the parameter --% is not passed to the command. The
arguments after --% have any environment variables (strings surrounded by % ) expanded. For
example:

 PowerShell

 echoargs.exe --% "%path%" # %path% is replaced with the value $Env:path

The order of evaluation of arguments is unspecified.

<!-- p.1310 -->

For information about parameter binding see §8.14. For information about name lookup see
§3.8.

Once argument processing has been completed, the command is invoked. If the invoked
command terminates normally (§8.5.4), control reverts to the point in the script or function
immediately following the command invocation. For a description of the behavior on abnormal
termination see break (§8.5.1), continue (§8.5.2), throw (§8.5.3), exit (§8.5.5), try (§8.7), and
trap (§8.8).

Ordinarily, a command is invoked by using its name followed by any arguments. However, the
command-invocation operator, &, can be used. If the command name contains unescaped
white space, it must be quoted and invoked with this operator. As a script block has no name,
it too must be invoked with this operator. For example, the following invocations of a
command call Get-Factorial are equivalent:

  PowerShell

  Get-Factorial 5
  & Get-Factorial 5
  & "Get-Factorial" 5

Direct and indirect recursive function calls are permitted. For example,

  PowerShell

  function Get-Power([int]$x, [int]$y) {
      if ($y -gt 0) { return $x * (Get-Power $x (--$y)) }
      else { return 1 }
  }

Examples:

  PowerShell

  New-Object 'int[,]' 3,2
  New-Object -ArgumentList 3,2 -TypeName 'int[,]'

  dir E:\PowerShell\Scripts\*statement*.ps1 | ForEach-Object {$_.Length}

  dir E:\PowerShell\Scripts\*.ps1 |
      Select-String -List "catch" |
      Format-Table Path, LineNumber -AutoSize

8.3 The if statement

<!-- p.1311 -->

Syntax:

  Syntax

  if-statement:
      if new-lines~opt~ ( new-lines~opt~ pipeline new-lines~opt~ ) statement-block
          elseif-clauses~opt~ else-clause~opt~

  elseif-clauses:
      elseif-clause
      elseif-clauses elseif-clause

  elseif-clause:
      new-lines~opt~ elseif new-lines~opt~ ( new-lines~opt~ pipeline new-lines~opt~ )
  statement-block

  else-clause:
      new-lines~opt~ else statement-block

Description:

The pipeline controlling expressions must have type bool or be implicitly convertible to that
type. The else-clause is optional. There may be zero or more elseif-clauses.

If the top-level pipeline tests True, then its statement-block is executed and execution of the
statement terminates. Otherwise, if an elseif-clause is present, if its pipeline tests True, then its
statement-block is executed and execution of the statement terminates. Otherwise, if an else-
clause is present, its statement-block is executed.

Examples:

  PowerShell

  $grade = 92
  if ($grade -ge 90) { "Grade A" }
  elseif ($grade -ge 80) { "Grade B" }
  elseif ($grade -ge 70) { "Grade C" }
  elseif ($grade -ge 60) { "Grade D" }
  else { "Grade F" }

8.4 Iteration statements
8.4.1 The while statement
Syntax:

<!-- p.1312 -->

 Syntax

 while-statement:
     while new-lines~opt~ ( new-lines~opt~ while-condition new-lines~opt~ )
 statement-block

 while-condition:
     new-lines~opt~ pipeline

Description:

The controlling expression while-condition must have type bool or be implicitly convertible to
that type. The loop body, which consists of statement-block, is executed repeatedly until the
controlling expression tests False. The controlling expression is evaluated before each
execution of the loop body.

Examples:

 PowerShell

 $i = 1
 while ($i -le 5) {                           # loop 5 times
     "{0,1}`t{1,2}" -f $i, ($i*$i)
     ++$i
 }

8.4.2 The do statement
Syntax:

 Syntax

 do-statement:
     do statement-block new-lines~opt~ while new-lines~opt~ ( while-condition new-
 lines~opt~ )
     do statement-block new-lines~opt~ until new-lines~opt~ ( while-condition new-
 lines~opt~ )

 while-condition:
     new-lines~opt~ pipeline

Description:

The controlling expression while-condition must have type bool or be implicitly convertible to
that type. In the while form, the loop body, which consists of statement-block, is executed
repeatedly while the controlling expression tests True. In the until form, the loop body is

<!-- p.1313 -->

executed repeatedly until the controlling expression tests True. The controlling expression is
evaluated after each execution of the loop body.

Examples:

 PowerShell

 $i = 1
 do {
     "{0,1}`t{1,2}" -f $i, ($i * $i)
 }
 while (++$i -le 5)                  # loop 5 times

 $i = 1
 do {
     "{0,1}`t{1,2}" -f $i, ($i * $i)
 }
 until (++$i -gt 5)                  # loop 5 times

8.4.3 The for statement
Syntax:

 Syntax

 for-statement:
     for new-lines~opt~ (
         new-lines~opt~ for-initializer~opt~ statement-terminator
         new-lines~opt~ for-condition~opt~ statement-terminator
         new-lines~opt~ for-iterator~opt~
         new-lines~opt~ ) statement-block

      for new-lines~opt~ (
          new-lines~opt~ for-initializer~opt~ statement-terminator
          new-lines~opt~ for-condition~opt~
          new-lines~opt~ ) statement-block

      for new-lines~opt~ (
          new-lines~opt~ for-initializer~opt~
          new-lines~opt~ ) statement-block

 for-initializer:
     pipeline

 for-condition:
     pipeline

 for-iterator:
     pipeline

<!-- p.1314 -->

Description:

The controlling expression for-condition must have type bool or be implicitly convertible to that
type. The loop body, which consists of statement-block, is executed repeatedly while the
controlling expression tests True. The controlling expression is evaluated before each execution
of the loop body.

Expression for-initializer is evaluated before the first evaluation of the controlling expression.
Expression for-initializer is evaluated for its side effects only; any value it produces is discarded
and is not written to the pipeline.

Expression for-iterator is evaluated after each execution of the loop body. Expression for-
iterator is evaluated for its side effects only; any value it produces is discarded and is not
written to the pipeline.

If expression for-condition is omitted, the controlling expression tests True.

Examples:

 PowerShell

 for ($i = 5; $i -ge 1; --$i) { # loop 5 times
     "{0,1}`t{1,2}" -f $i, ($i * $i)
 }

 $i = 5
 for (; $i -ge 1; ) { # equivalent behavior
     "{0,1}`t{1,2}" -f $i, ($i * $i)
     --$i
 }

8.4.4 The foreach statement
Syntax:

 Syntax

 foreach-statement:
     foreach new-lines~opt~ foreach-parameter~opt~ new-lines~opt~
         ( new-lines~opt~ variable new-lines~opt~ *in* new-lines~opt~ pipeline
         new-lines~opt~ ) statement-block

 foreach-parameter:
     -parallel

<!-- p.1315 -->

Description:

The loop body, which consists of statement-block, is executed for each element designated by
the variable variable in the collection designated by pipeline. The scope of variable is not
limited to the foreach statement. As such, it retains its final value after the loop body has
finished executing. If pipeline designates a scalar (excluding the value $null) instead of a
collection, that scalar is treated as a collection of one element. If pipeline designates the value
$null , pipeline is treated as a collection of zero elements.

If the foreach-parameter -parallel is specified, the behavior is implementation defined.

The foreach-parameter ‑parallel is only allowed in a workflow (§8.10.2).

Every foreach statement has its own enumerator, $foreach (§2.3.2.2, §4.5.16), which exists only
while that loop is executing.

The objects produced by pipeline are collected before statement-block begins to execute.
However, with the ForEach-Object cmdlet, statement-block is executed on each object as it is
produced.

Examples:

 PowerShell

 $a = 10, 53, 16, -43
 foreach ($e in $a) {
     ...
 }
 $e # the int value -43

 foreach ($e in -5..5) {
     ...
 }

 foreach ($t in [byte], [int], [long]) {
     $t::MaxValue # get static property
 }

 foreach ($f in Get-ChildItem *.txt) {
     ...
 }

 $h1 = @{ FirstName = "James"; LastName = "Anderson"; IDNum = 123 }
 foreach ($e in $h1.Keys) {
     "Key is " + $e + ", Value is " + $h1[$e]
 }

<!-- p.1316 -->

8.5 Flow control statements
Syntax:

 Syntax

 flow-control-statement:
     break label-expression~opt~
     continue label-expression~opt~
     throw pipeline~opt~
     return pipeline~opt~
     exit pipeline~opt~

 label-expression:
     simple-name
     unary-expression

Description:

A flow-control statement causes an unconditional transfer of control to some other location.

8.5.1 The break statement
Description:

A break statement with a label-expression is referred to as a labeled break statement. A break
statement without a label-expression is referred to as an unlabeled break statement.

Outside a trap statement, an unlabeled break statement directly within an iteration statement
(§8.4) terminates execution of that smallest enclosing iteration statement. An unlabeled break
statement directly within a switch statement (§8.6) terminates pattern matching for the current
switch's switch-condition. See (§8.8) for details of using break from within a trap statement.

An iteration statement or a switch statement may optionally be preceded immediately by one
statement label (§8.1.1).Such a statement label may be used as the target of a labeled break
statement, in which case, that statement terminates execution of the targeted enclosing
iteration statement.

A labeled break need not be resolved in any local scope; the search for a matching label may
continue up the calling stack even across script and function-call boundaries. If no matching
label is found, the current command invocation is terminated.

The name of the label designated by label-expression need not have a constant value.

<!-- p.1317 -->

If label-expression is a unary-expression, it is converted to a string.

Examples:

 PowerShell

 $i = 1
 while ($true) { # infinite loop
     if ($i * $i -gt 100) {
         break # break out of current while loop
     }
     ++$i
 }

 $lab = "go_here"
 :go_here
 for ($i = 1; ; ++$i) {
     if ($i * $i -gt 50) {
         break $lab # use a string value as target
     }
 }

 :labelA
 for ($i = 1; $i -le 2; $i++) {

      :labelB
      for ($j = 1; $j -le 2; $j++) {

            :labelC
            for ($k = 1; $k -le 3; $k++) {
                if (...) { break labelA }
            }
      }
 }

8.5.2 The continue statement
Description:

A continue statement with a label-expression is referred to as a labeled continue statement. A
continue statement without a label-expression is referred to as an unlabeled continue statement.

The use of continue from within a trap statement is discussed in §8.8.

An unlabeled continue statement within a loop terminates execution of the current loop and
transfers control to the closing brace of the smallest enclosing iteration statement (§8.4). An
unlabeled continue statement within a switch terminates execution of the current switch
iteration and transfers control to the smallest enclosing switch 's switch-condition (§8.6).

<!-- p.1318 -->

An iteration statement or a switch statement (§8.6) may optionally be preceded immediately
by one statement label (§8.1.1). Such a statement label may be used as the target of an
enclosed labeled continue statement, in which case, that statement terminates execution of
the current loop or switch iteration, and transfers control to the targeted enclosing iteration or
switch statement label.

A labeled continue need not be resolved in any local scope; the search for a matching label
may continue up the calling stack even across script and function-call boundaries. If no
matching label is found, the current command invocation is terminated.

The name of the label designated by label-expression need not have a constant value.

If label-expression is a unary-expression, it is converted to a string.

Examples:

 PowerShell

 $i = 1
 while (...) {
     ...
     if (...) {
         continue # start next iteration of current loop
     }
     ...
 }

 $lab = "go_here"
 :go_here
 for (...; ...; ...) {
     if (...) {
         continue $lab # start next iteration of labeled loop
     }
 }

 :labelA
 for ($i = 1; $i -le 2; $i++) {

      :labelB
      for ($j = 1; $j -le 2; $j++) {

            :labelC
            for ($k = 1; $k -le 3; $k++) {
                if (...) { continue labelB }
            }
      }
 }

<!-- p.1319 -->

8.5.3 The throw statement
Description:

An exception is a way of handling a system- or application-level error condition. The throw
statement raises an exception. (See §8.7 for a discussion of exception handling.)

If pipeline is omitted and the throw statement is not in a catch-clause, the behavior is
implementation defined. If pipeline is present and the throw statement is in a catch-clause, the
exception that was caught by that catch-clause is re-thrown after any finally-clause associated
with the catch-clause is executed.

If pipeline is present, the type of the exception thrown is implementation defined.

When an exception is thrown, control is transferred to the first catch clause in an enclosing try
statement that can handle the exception. The location at which the exception is thrown initially
is called the throw point. Once an exception is thrown the steps described in §8.7 are followed
repeatedly until a catch clause that matches the exception is found or none can be found.

Examples:

 PowerShell

 throw
 throw 100
 throw "No such record in file"

If pipeline is omitted and the throw statement is not from within a catch-clause, the text
"ScriptHalted" is written to the pipeline, and the type of the exception raised is
System.Management.Automation.RuntimeException .

If pipeline is present, the exception raised is wrapped in an object of type
System.Management.Automation.RuntimeException , which includes information about the

exception as a System.Management.Automation.ErrorRecord object (accessible via $_ ).

Example 1: throw 123 results in an exception of type RuntimeException. From within the catch
block, $_.TargetObject contains the object wrapped inside, in this case, a System.Int32 with
value 123.

Example 2: throw "xxx" results in an exception of type RuntimeException. From within the
catch block, $_.TargetObject contains the object wrapped inside, in this case, a System.String
with value "xxx".

<!-- p.1320 -->

Example 3: throw 10,20 results in an exception of type RuntimeException. From within the
catch block, $_.TargetObject contains the object wrapped inside, in this case, a
System.Object[] , an unconstrained array of two elements with the System .Int32` values 10 and

20.

8.5.4 The return statement
Description:

The return statement writes to the pipeline the value(s) designated by pipeline, if any, and
returns control to the function or script's caller. A function or script may have zero or more
return statements.

If execution reaches the closing brace of a function an implied return without pipeline is
assumed.

The return statement is a bit of "syntactic sugar" to allow programmers to express themselves
as they can in other languages; however, the value returned from a function or script is actually
all of the values written to the pipeline by that function or script plus any value(s) specified by
pipeline. If only a scalar value is written to the pipeline, its type is the type of the value
returned; otherwise, the return type is an unconstrained 1-dimensional array containing all the
values written to the pipeline.

Examples:

  PowerShell

  function Get-Factorial ($v) {
      if ($v -eq 1) {
          return 1 # return is not optional
      }

      return $v * (Get-Factorial ($v - 1)) # return is optional
  }

The caller to Get-Factorial gets back an int .

  PowerShell

  function Test {
      "text1" # "text1" is written to the pipeline
      # ...
      "text2" # "text2" is written to the pipeline
      # ...
