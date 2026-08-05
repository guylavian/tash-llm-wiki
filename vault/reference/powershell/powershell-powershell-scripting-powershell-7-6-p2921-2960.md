---
title: "How to use this documentation — pages 2921-2960"
type: reference
domain: powershell
slug: powershell-powershell-scripting-powershell-7-6-p2921-2960
tier: reference
source: https://learn.microsoft.com/en-us/powershell/scripting/powershell-scripting-powershell-7-6-p2921-2960
family: powershell
documentKind: "doc"
abstract: "Extended Type System Overview PowerShell uses its PSObject object to extend the types of objects in two ways. First, the PSObject object provides a way to show different views of specific object types. This is referred to as showing an adapted view of an object. Second, the PSOb"
---

# How to use this documentation — pages 2921-2960

<!-- p.2921 -->

Extended Type System Overview
PowerShell uses its PSObject object to extend the types of objects in two ways. First, the
PSObject object provides a way to show different views of specific object types. This is referred
to as showing an adapted view of an object. Second, the PSObject object provides a way to
add members to existing object. Together, by wrapping an existing object, referred to as the
base object, the PSObject object provides an extended type system (ETS) that script and
cmdlet developers can use to manipulate .NET objects within the shell.

Cmdlet and Script Development Issues
ETS resolves two fundamental issues:

First, some .NET Objects do not have the necessary default behavior for acting as the data
between cmdlets.

     Some .NET objects are "meta" objects (for example: WMI Objects, ADO objects, and XML
     objects) whose members describe the data they contain. However, in a scripting
     environment it is the contained data that is most interesting, not the description of the
     contained data. ETS resolves this issue by introducing the notion of Adapters that adapt
     the underlying .NET object to have the expected default semantics.
     Some .NET Object members are inconsistently named, provide an insufficient set of public
     members, or provide insufficient capability. ETS resolves this issue by introducing the
     ability to extend the .NET object with additional members.

Second, the PowerShell scripting language is typeless in that a variable does not need to be
declared of a particular type. That is, the variables a script developer creates are by nature
typeless. However, the PowerShell system is "type-driven" in that it depends on having a type
name to operate against for basic operations such as outputting results or sorting.

Therefore a script developer must have the ability to state the type of one of their variables and
build up their own set of dynamically typed "objects" that contain properties and methods and
can participate in the type-driven system. ETS solves this problem by providing a common
object for the scripting language that has the ability to state its type dynamically and to add
members dynamically.

Fundamentally, ETS resolves the issue mentioned previously by providing the PSObject object,
which acts as the basis of all object access from the scripting language and provides a standard

<!-- p.2922 -->

abstraction for the cmdlet developer.

Cmdlet Developers
For the cmdlet developers, ETS provides the following support:

     The abstractions to work against objects in a generic way using the PSObject object. ETS
     also provides the ability to drill past these abstractions if required.
     The mechanisms to create a default behavior for formatting, sorting, serialization, and
     other system manipulations of their object type using a well-known set of extended
     members.
     The means to operate against any object using the same semantics as the script language
     using a LanguagePrimitives object.
     The means to dynamically "type" a hash table so that the rest of the system can operate
     against it effectively.

Script Developers
For the script developers, ETS provides the following support:

     The ability to reference any underlying object type using the same syntax ( $a.x ).
     The ability to access beyond the abstraction provided by the PSObject object (such as
     accessing only adapted members, or accessing the base object itself).
     The ability to define well-known members that control the formatting, sorting,
     serialization, and other manipulations of an object instance or type.
     The means to name an object as a specific type and thus control the inheritance of its
     type-based members.
     The ability to add, remove, and modify extended members.
     The ability to manipulate the PSObject object itself if required.

The PSObject class
The PSObject object is the basis of all object access from the scripting language and provides a
standard abstraction for the cmdlet developer. It contains a base-object (a .NET object) and any
instance members (members, specifically extended members, that are present on a particular
object instance while not necessarily on other objects of the same type). Depending on the
type of the base-object, the PSObject object might also provide implicit and explicit access to
adapted members as well as any type-based extended members.

<!-- p.2923 -->

The PSObject object provides the following mechanisms:

     The ability to construct a PSObject with or without a base-object.
     The ability to access of all members of each constructed PSObject object through a
     common lookup algorithm and the ability to override that algorithm when required.
     The ability to get and set the type-names of the constructed PSObject objects so that
     scripts and cmdlets can reference similar PSObject objects by the same type-name,
     regardless of the type of their base-object.

How to Construct a PSObject
The following list describes ways to create a PSObject object:

     Calling the PSObject .#ctor constructor creates a new PSObject object with a base-object
     of PSCustomObject. A base-object of this type indicates that the PSObject object has no
     meaningful base-object. However, a PSObject object with this type of base-object does
     provide a property bag that cmdlet developers can find helpful by adding extended-
     members.

Developers can also specify the object type-name, which allows this object to share its
extended-members with other PSObject objects of the same type-name.

     Calling the PSObject .#ctor(System.Object) constructor creates a new PSObject object
     with a base-object of type System.Object.

     In this case, the type-name for the created object is a collection of the derivation
     hierarchy of the base-object. For example, the type-name for the PSObject that contains
     a ProcessInfo base-object would include the following names:
        System.Diagnostics.Process
        System.ComponentModel.Component
        System.MarshalByRefObject
        System.Object

     Calling the PSObject .AsPSObject(System.Object) method creates a new PSObject object
     based on a supplied object.

     If the supplied object is of type System.Object, the supplied object is used as the base-
     object for the new PSObject object. If the supplied object is already a PSObject object,
     the supplied object is returned as is.

Base, adapted, and extended members

<!-- p.2924 -->

Conceptually, ETS uses the following terms to show the relationship between the original
members of the base-object and those members added by PowerShell. For more information
about the specific types of members that are used by the PSObject object, see PSObject class.

Base-object members

If the base-object is specified when constructing the PSObject objects, then the members of
the base-object are made available through the Members property.

Adapted members

When a base-object is a meta-object, one that contains data in a generic fashion whose
properties "describe" their contained data, ETS adapts those objects to a view that allows for
direct access to the data through adapted members of the PSObject object. Adapted members
and base-object members are accessed through the Members property.

Extended members

In addition to the members made available from the base-object or those adapted members
created by PowerShell, a PSObject may also define extended members that extend the original
base-object with additional information that is useful in the scripting environment.

For example, all the core cmdlets provided by PowerShell, such as the Get-Content and Set-
Content cmdlets, take a Path parameter. To ensure that these cmdlets, and others, can work
against objects of different types, a Path member can be added to those objects so that they
all state their information in a common way. This extended Path member ensures that the
cmdlets can work against all those types even though there base class might not have a Path
member.

Extended members, adapted members, and base-object members are all accessed through the
Members property.

 Last updated on 05/20/2025

<!-- p.2925 -->

Extended Type System class members
ETS refers to a number of different kinds of members whose types are defined by the
PSMemberTypes enumeration. These member types include properties, methods, members,
and member sets that are each defined by their own CLR type. For example, a NoteProperty is
defined by its own PSNoteProperty type. These individual CLR types have both their own
unique properties and common properties that are inherited from the PSMemberInfo class.

The PSMemberInfo class
The PSMemberInfo class serves as a base class for all ETS member types. This class provides
the following base properties to all member CLR types.

     Name property: The name of the member. This name can be defined by the base-object
     or defined by PowerShell when adapted members or extended members are exposed.
     Value property: The value returned from the particular member. Each member type
     defines how it handles its member value.
     TypeNameOfValue property: This is the name of the CLR type of the value that is
     returned by the Value property.

Accessing members
Collections of members can be accessed through the Members, Methods, and Properties
properties of the PSObject object.

ETS properties
ETS properties are members that can be treated as a property. Essentially, they can appear on
the left-hand side of an expression. They include alias properties, code properties, PowerShell
properties, note properties, and script properties. For more information about these types of
properties, see ETS properties.

ETS methods
ETS methods are members that can take arguments, may return results, and cannot appear on
the left-hand side of an expression. They include code methods, PowerShell methods, and
script methods. For more information about these types of methods, see ETS methods.

<!-- p.2926 -->

Last updated on 05/20/2025

<!-- p.2927 -->

ETS member sets
Member sets allow you to partition the members of the PSObject object into two subsets so
that the members of the subsets can be referenced together by their subset name. The two
types of subsets include property sets and member sets. For example of how PowerShell uses
member sets, there is a specific property set named DefaultDisplayPropertySet that is used to
determine, at runtime, which properties to display for a given PSObject object.

Property Sets
Property sets can include any number of properties of a PSObject type. In general, a property
set can be used whenever a collection of properties (of the same type) is needed. The property
set is created by calling the
PSPropertySet(System.String,System.Collections.Generic.IEnumerable{System.String})

constructor with the name of the property set and the names of the referenced properties. The
created PSPropertySet object can then be used as an alias that points to the properties in the
set. The PSPropertySet class has the following properties and methods.

     IsInstance property: Gets a Boolean value that indicates the source of the property.
     MemberType property: Gets the type of properties in the property set.
     Name property: Gets the name of the property set.
     ReferencedPropertyNames property: Gets the names of the properties in the property
     set.
     TypeNameOfValue property: Gets a PropertySet enumeration constant that defines this
     set as a property set.
     Value property: Gets or sets the PSPropertySet object.
      PSPropertySet.Copy method: Makes an exact copy of the PSPropertySet object.

      PSMemberSet.ToString method: Converts the PSPropertySet object to a string.

Member Sets
Member sets can include any number of extended members of any type. The member set is
created by calling the
PSMemberSet(System.String,System.Collections.Generic.IEnumerable{System.Management.Automa

tion.PSMemberInfo}) constructor with the name of the member set and the names of the

referenced members. The created PSPropertySet object can then be used as an alias that

<!-- p.2928 -->

points to the members in the set. The PSMemberSet class has the following properties and
methods.

     IsInstance property: Gets a Boolean value that indicates the source of the member.
     Members property: Gets all the members of the member set.
     MemberType property: Gets a MemberSet enumeration constant that defines this set as
     a member set.
     Methods property: Gets the methods included in the member set.
     Properties property: Gets the properties included in the member set.
     TypeNameOfValue property: Gets a MemberSet enumeration constant that defines this
     set as a member set.
     Value property: Gets the PSMemberSet object.
     PSMemberSet.Copy method: Makes an exact copy of the PSMemberSet object.

     PSMemberSet.ToString method: Converts the PSMemberSet object to a string.

Last updated on 05/20/2025

<!-- p.2929 -->

ETS properties
Properties are members that can be treated as a property. Essentially, they can appear on the
left-hand side of an expression. The properties that are available include alias, code, note, and
script properties.

Alias Property
An alias property is a property that references another property that the PSObject object
contains. It is used primarily to rename the referenced property. However, it may also be used
to convert the referenced property's value to another type. With respect to ETS, this type of
property is always an extended-member and is defined by the PSAliasProperty class. The class
includes the following properties.

     ConversionType property: The CLR type used to convert the referenced member's value.
     IsGettable property: Indicates whether the value of the referenced property can be
     retrieved. This property is dynamically determined by examining the IsGettable property
     of the referenced property.
     IsSettable property: Indicates whether the value of the referenced property can be set.
     This property is dynamically determined by examining the IsSettable property of the
     referenced property.
     MemberType property: An AliasProperty enumeration constant that defines this property
     as an alias property.
     ReferencedMemberName property: The name of the referenced property that this alias
     refers to.
     TypeNameOfValue property: The full name of the CLR type of the referenced property's
     value.
     Value property: The value of the referenced property.

Code Property
A code property is a property that is a getter and setter that is defined in a CLR language. In
order for a code property to become available, a developer must write the property in some
CLR language, compile, and ship the resultant assembly. This assembly must be available in the
runspace where the code property is desired. With respect to ETS, this type of property is

<!-- p.2930 -->

always an extended-member and is defined by the PSCodeProperty class. The class includes
the following properties.

     GetterCodeReference property: The method used to get the value of the code property.
     IsGettable property: Indicates whether the value of the code property can be retrieved,
     that the SetterCodeReference property: The method used to set the value of the code
     property.
     IsSettable property: Indicates whether the value of the code property can be set, that the
     SetterCodeReference property is not null.
     MemberType property: A CodeProperty enumeration constant that defines this property
     as a code property.
     SetterCodeReference property: The method used to get the value of the code property.
     TypeNameOfValue property: The CLR type of the code property value that is returned by
     the properties get operation.
     Value property: The value of the code property. When this property is retrieved, the getter
     code in the GetterCodeReference property is invoked, passing the current PSObject
     object and returning the value returned by the invocation. When this property is set, the
     setter code in the SetterCodeReference property is invoked, passing the current
     PSObject object as the first argument and the object used to set the value as the second
     argument.

Note Property
A Note property is a property that has a name/value pairing. With respect to ETS, this type of
property is always an extended-member and is defined by the PSNoteProperty class. The class
includes the following properties.

     IsGettable property: Indicates whether the value of the note property can be retrieved.
     IsSettable property: Indicates whether the value of the note property can be set.
     MemberType property: A NoteProperty enumeration constant that defines this property
     as a note property.
     TypeNameOfValue property: The fully-qualified type name of the object returned by the
     note property's get operation.
     Value: The value of the note property.

PowerShell property

<!-- p.2931 -->

A PowerShell property is a property defined on the base object or a property that is made
available through an adapter. It can refer to both CLR fields as well as CLR properties. With
respect to ETS, this type of property can be either a base-member or an adapter-member and
is defined by the PSProperty class. The class includes the following properties.

      IsGettable property: Indicates whether the value of the base or adapted property can be
      retrieved.
      IsSettable property: Indicates whether the value of the base or adapted property can be
      set.
      MemberType property: A Property enumeration constant that defines this property as a
      PowerShell property.
      TypeNameOfValue property: The fully-qualified name of the property value type. For
      example, for a property whose value is a string, its property value type is System.String.
      Value property: The value of the property. If the get or set operation is called on a
      property that does not support that operation, a GetValueException or
      SetValueException exception is thrown

PowerShell Script property
A Script property is a property that has getter and setter scripts. With respect to ETS, this type
of property is always an extended-member and is defined by the PSScriptProperty class. The
class includes the following properties.

      GetterScript property: The script used to retrieve the script property value.
      IsGettable property: Indicates whether the GetterScript property exposes a script block.
      IsSettable property: Indicates whether the SetterScript property exposes a script block.
      MemberType property: A ScriptProperty enumeration constant that identifies this
      property as a script property.
      SetterScript property: The script used to set the script property value.
      TypeNameOfValue property: The fully-qualified type name of the object returned by the
      getter script. In this case System.Object is always returned.
      Value property: The value of the script property. A get invokes the getter script and
      returns the value provided. A set invokes the setter script.

 Last updated on 05/20/2025

<!-- p.2932 -->

ETS class methods
ETS methods are members that can take arguments, may return results, and cannot appear on
the left-hand side of an expression. The methods that are available within ETS include code,
Windows PowerShell, and script methods.

  ７ Note

  From scripts, methods are accessed using the same syntax as other members with the
  addition of parenthesis at the end of the method name.

Code Methods
A code method is an extended member that is defined in a CLR language. It provides similar
functionality to a method defined on a base object; however, a code method may be added
dynamically to an PSObject object. In order for a code method to become available, a
developer must write the property in some CLR language, compile, and ship the resultant
assembly. This assembly must be available in the runspace where the code method is desired.
Be aware that a code method implementation must be thread safe. Access to these methods is
done through PSCodeMethod objects that provides the following public methods and
properties.

     PSCodeMethod.Copy method: Makes an exact copy of the PSCodeMethod object.

     PSCodeMethod.Invoke(System.Object[]) method: Invokes the underlying code method.

     PSCodeMethod.ToString method: Converts the PSCodeMethod object to a string.

     PSCodeMethod.CodeReference property: Gets the underlying method that the code method

     is based on.
     PSMemberInfo.IsInstance property: Gets a Boolean value that indicates the source of the
     member.
     PSCodeMethod.MemberType property: Gets an PSMemberTypes.CodeMethod
     enumeration constant that identifies this method as a code method.
     PSMemberInfo.Name property: Gets the name of the underlying code method.
     PSCodeMethod.OverloadDefinitions property: Gets a definition of all the overloads of
     the underlying code method.
     PSCodeMethod.TypeNameOfValue property: Gets the full name of the code method.
     PSMemberInfo.Value property: Gets the PSCodeMethod object.

<!-- p.2933 -->

Windows PowerShell Methods
A PowerShell method is a CLR method defined on the base object or is made accessible
through an adapter. Access to these methods is done through PSMethod objects that provides
the following public methods and properties.

     PSMethod.Copy method: Makes an exact copy of the PSMethod object.

     PSMethod.Invoke(System.Object[]) method: Invokes the underlying method.

     PSMethod.ToString method: Converts the PSMethod object to a string.

     PSMemberInfo.IsInstance property: Gets a Boolean value that indicates the source of the
     member.
     PSMethod.MemberType property: Gets an PSMemberTypes.Method enumeration
     constant that identifies this method as a PowerShell method.
     PSMemberInfo.Name property: Gets the name of the underlying method.
     PSMethod.OverloadDefinitions property: Gets the definitions of all the overloads of the
     underlying method.
     PSMethod.TypeNameOfValue property: Gets the ETS type of this method.
     PSMemberInfo.Value property: Gets the PSMethod object.

Script Methods
A script method is an extended member that is defined in the PowerShell language. It provides
similar functionality to a method defined on a base object; however, a script method may be
added dynamically to an PSObject object. Access to these methods is done through
PSScriptMethod objects that provides the following public methods and properties.

     PSScriptMethod.Copy method: Makes an exact copy of the PSScriptMethod object.

     PSScriptMethod.Invoke(System.Object[]) method: Invokes the underlying script method.

     PSScriptMethod.ToString method: Converts the PSScriptMethod object to a string.

     PSMemberInfo.IsInstance property: Gets a Boolean value that indicates the source of the
     member.
     PSScriptMethod.MemberType property: Gets a PSMemberTypes.ScriptMethod
     enumeration constant that identifies this method as a script method.
     PSMemberInfo.Name property: Gets the name of the underlying code method.
     PSScriptMethod.OverloadDefinitions property: Gets the definitions of all the overloads
     of the underlying script method.
     PSScriptMethod.TypeNameOfValue property: Gets the ETS type of this method.
     PSScriptMethod.Script property: Gets the script used to invoke the method.

<!-- p.2934 -->

     PSMemberInfo.Value property: Gets the PSScriptMethod object.

Last updated on 05/20/2025

<!-- p.2935 -->

ETS type converters
ETS uses two basic types of type converters when a call is made to the
LanguagePrimitives.ConvertTo(System.Object, System.Type) method. When this method is

called, PowerShell attempts to perform the type conversion using its standard PowerShell
language converters or a custom converter. If PowerShell cannot perform the conversion, it
throws an PSInvalidCastException exception.

Standard Windows PowerShell Language
Converters
These standard conversions are checked before any custom conversions and cannot be
overridden. The following table lists the type conversions performed by PowerShell when the
ConvertTo(System.Object, System.Type) method is called. Be aware that references to the

valueToConvert and resultType parameters refer to parameters of the
ConvertTo(System.Object,System.Type) method.

                                                                                    ﾉ     Expand table

 From               To             Returns
 (valueToConvert)   (resultType)

 Null               String         ""

 Null               Char           '\0'

 Null               Numeric        0 of the type specified in the resultType parameter.

 Null               Boolean        Results of call to the IsTrue(System.Object)(Null) method.

 Null               PSObject       New object of type PSObject.

 Null               Non-value-     Null.
                    type

 Null               Nullable<T>    Null.

 Derived Class      Base class     valueToConvert

 Anything           Void           AutomationNull.Value

 Anything           String         Calls ToString mechanism.

<!-- p.2936 -->

 From                To             Returns
 (valueToConvert)    (resultType)

 Anything            Boolean        IsTrue(System.Object) (valueToConvert)

 Anything            PSObject       Results of call to the AsPSObject(System.Object) (valueToConvert)
                                    method.

 Anything            Xml            Converts valueToConvert to string, then calls XMLDocument
                     Document       constructor.

 Array               Array          Attempts to convert each element of the array.

 Singleton           Array          Array[0] equals valueToConvert that is converted to the element
                                    type of the array.

 IDictionary         Hash table     Results of call to Hashtable(valueToConvert).

 String              Char[]         valueToConvert.ToCharArray

 String              RegEx          Results of call to Regx(valueToConvert) .

 String              Type           Returns the appropriate type using the valueToConvert parameter
                                    to search RunspaceConfiguration.Assemblies.

 String              Numeric        If valueToConvert is "", returns 0 of the resultType. Otherwise the
                                    culture "culture invariant" is used to produce a numeric value.

 Integer             System.Enum    Converts the integer to the constant if the integer is defined by the
                                    enumeration. If the integer is not defined an
                                    PSInvalidCastException exception is thrown.

Custom conversions
If PowerShell cannot convert the type using a standard PowerShell language converter, it then
checks for custom converters. PowerShell looks for several types of custom converters in the
order described in this section. Be aware that references to the valueToConvert and resultType
parameters refer to parameters of the ConvertTo(System.Object, System.Type) method. If a
custom converter throws an exception, then no further attempt is made to convert the object
and that exception is wrapped in a PSInvalidCastException exception which is then thrown.

PowerShell type converter
PowerShell type converters are used to convert a single type or a family of types, such as all
types that derive from the System.Enum class. To create a PowerShell type converter you must

<!-- p.2937 -->

implement an PSTypeConverter class and associate that implementation with the target class.
There are two ways of associating the PowerShell type converter with its target class.

     Through the type configuration file
     By applying the TypeConverterAttribute attribute to the target class

PowerShell type converters, derived from the PSTypeConverter abstract class, provide methods
for converting an object to a specific type or from a specific type. If the valueToConvert
parameter contains an object that has a PowerShell Type converter associated with it,
PowerShell calls the PSTypeConverter.ConvertTo(System.Object,
System.Type,System.IFormatProvider, System.Boolean) method of the associated converter to

convert the object to the type specified by the resultType parameter. If the resultType
parameter references a type that has a PowerShell type converter associated with it, PowerShell
calls the PSTypeConverter.ConvertFrom(System.Object,System.Type, System.IFormatProvider,
System.Boolean) method of the associated converter to convert the object from the type

specified by the resultType parameter.

System type converter
System type converters are used to convert a specific target class. This type of converter cannot
be used to convert a family of classes. To create an system type converter you must implement
an TypeConverter class and associate that implementation with the target class. There are two
ways of associating the system type converter with its target class.

     Through the type configuration file
     By applying the TypeConverterAttribute attribute to the target class

Parse converter
If the valueToConvert parameter is a string, and the object type of the resultType parameter
has a Parse method, then the Parse method is called to convert the string.

Constructor converter
If the object type of the resultType parameter has a constructor that has a single parameter
that is the same type as the object of the valueToConvert parameter, then this constructor is
called.

Implicit cast operator converter

<!-- p.2938 -->

If the valueToConvert parameter has an implicit cast operator that converts to resultType, then
its cast operator is called. If the resultType parameter has an implicit cast operator that
converts from valueToConvert, then its cast operator is called.

Explicit cast operator converter
If the valueToConvert parameter has an explicit cast operator that converts to resultType, then
its cast operator is called. If the resultType parameter has an explicit cast operator that
converts from valueToConvert, then its cast operator is called.

 Last updated on 05/20/2025

<!-- p.2939 -->

Errors and exceptions in the Extended Type
System
Errors can occur in ETS during the initialization of type data and when accessing a member of
an PSObject object or using one of the utility classes such as LanguagePrimitives.

Runtime errors
With one exception, when casting, all exceptions thrown from ETS during runtime are either an
ExtendedTypeSystemException exception or an exception derived from the
ExtendedTypeSystemException class. This allows script developers to trap these exceptions
using the trap statement in their script.

Errors getting member values
All errors that occur when getting the value of an ETS member (property, method, or
parameterized property) cause a GetValueException or GetValueInvocationException
exception to be thrown. When ETS recognizes that an error occurred a GetValueException
exception is thrown. When the underlying getter of a referenced member recognizes that an
error occurred, a GetValueInvocationException exception is thrown that may or may not
include the inner exception that caused the get invocation error.

Errors setting member values
All errors that occur when setting the value of an ETS property cause a SetValueException or
SetValueInvocationException exception to be thrown. When ETS recognizes that an error
occurred a SetValueException exception is thrown. When the underlying setter of a referenced
property recognizes that an error occurred, a SetValueInvocationException exception is
thrown that may or may not include the inner exception that caused the set invocation error.

Errors invoking a method
All errors that occur when invoking an ETS method cause a MethodException or
MethodInvocationException exception to be thrown. When ETS recognizes that an error
occurred a MethodException exception is thrown. When the referenced method recognizes

<!-- p.2940 -->

that an error occurred, a MethodInvocationException exception is thrown that may or may not
include the inner exception that caused the invocation error.

Casting errors
When an invalid cast is attempted, an PSInvalidCastException is thrown. Because this
exception derives from System.InvalidCastException, it is not able to be directly trapped from
script. Be aware that the entity attempting the cast would need to wrap
PSInvalidCastException in an PSRuntimeException for this to be trappable by scripts. If an
attempt is made to set the value of an PSPropertySet, PSMemberSet, PSMethodInfo, or a
member of the ReadOnlyPSMemberInfoCollection`1, a NotSupportedException is thrown.

Common runtime errors
Any other common runtime errors that occur are of type ExtendedTypeSystemException
exception with no additional specific exception types.

Initialization errors
Errors may occur when initializing types.ps1xml . Typically, these errors are displayed when the
PowerShell runtime starts. However, they can also be displayed when a module is loaded.

 Last updated on 05/20/2025

<!-- p.2941 -->

The Monad Manifesto
07/07/2025

Jeffrey Snover, the inventor of PowerShell, wrote the Monad Manifesto to explain his vision for
PowerShell and how it would change the way we manage systems. You can read more about
why he wrote it in his Monad Manifesto      blog post.

In that post, he explained how hard it was to communicate the vision for PowerShell to widely
distributed development teams. The development teams didn't understand the vision. Writing
the Manifesto forced him to be clear about what problem was being addressed, the core
principles of the design, how to address the issue, who would benefit from it, and why.

Use the following link to download a copy of the Manifesto.

     Monad Manifesto      .

This document is historically significant to PowerShell. It's a version of the original Monad
Manifesto, which articulated the long-term vision and initiated the development effort that
became PowerShell. PowerShell has delivered on many of the elements described in this
document.

<!-- p.2942 -->

Contributing to PowerShell documentation
Thank you for your support of PowerShell!

The Contributor's Guide is a collection of articles that describe the tools and processes we use
to create documentation at Microsoft. Some of these guides cover information common to any
documentation set published to learn.microsoft.com . Other guides are specific to how we
write documentation for PowerShell.

The common articles are available in our centralized Contributor's Guide. The PowerShell-
specific guides are available here.

Ways to contribute
There are two ways to contribute. Both contributions are valuable to us.

     Filing issues helps us identify problems and gaps in our documentation. Sometimes the
     issues are difficult to resolve, requiring more investigation and research. The issue process
     allows us to have a conversation about the problem and develop a satisfactory resolution.

     Submitting a pull request to add or change content is a more involved process. The
     following information outlines the tools, processes, and standards for submitting content
     to the documentation.

Prepare to make a contribution
Contributing to the documentation requires a GitHub account. Use the following checklist to
install and configure the tools you need to make contributions.

   1. Sign up for GitHub
   2. Install Git and Markdown tools
   3. Install the Docs Authoring Pack
   4. Install Posh-Git   - not required but recommended
   5. Set up a local Git repository
   6. Review Git and GitHub fundamentals

Get started writing docs

<!-- p.2943 -->

There are two ways to contribute changes to the documentation:

   1. Quick edits to existing docs - Minor corrections, fixing typos, or small additions
   2. Full GitHub workflow for docs - large changes, multiple versions, adding or changing
     images, or contributing new articles

Also, read the Writing essentials section of the centralized Contributor's Guide. Another
excellent resource is the Microsoft Writing Style Guide.

Minor corrections or clarifications to documentation and code examples in public repositories
are covered by the learn.microsoft.com Terms of Use.

Use the full GitHub workflow when you're making significant changes. If you're not an
employee of Microsoft, our PR validation system adds a comment to the pull request asking
you to sign the online Contribution Licensing Agreement (CLA)      . You must complete this step
before we can review or accept your pull request. Signing the CLA is only required the first time
you submit a PR in the repository. You might be asked to sign the CLA for each time you
contribute to a new repository.

Code of conduct
All repositories that publish to Microsoft Learn adhere to the Microsoft Open Source Code of
Conduct    or the .NET Foundation Code of Conduct . For more information, see the Code of
Conduct FAQ     .

Next steps
The following articles cover information specific to PowerShell documentation. Where there's
overlap with the guidance in the centralized Contributor's Guide, we call out how those rules
differ for the PowerShell content.

Review the following documents:

     Get started writing docs
     Markdown best practices
     PowerShell-Docs style guide
     How to file an issue
     Submitting a pull request

Additional resources

<!-- p.2944 -->

     Editorial checklist
     How we manage issues
     How we manage pull requests

Last updated on 11/20/2025

<!-- p.2945 -->

Get started contributing to PowerShell
documentation
This article is an overview of how to get started as a contributor to the PowerShell
documentation.

PowerShell-Docs structure
There are three categories of content in the PowerShell-Docs       repository:

     reference content
     conceptual content
     metadata and configuration files

Reference content
The reference content is the PowerShell cmdlet reference for the cmdlets that ship in
PowerShell. The cmdlet reference     is collected in versioned folders (like 5.1, 7.4, 7.5, and 7.6),
which contain the reference for the modules that ship with PowerShell. This content is also
used to create the help information displayed by the Get-Help cmdlet.

Conceptual content
The conceptual documentation       isn't organized by version. All articles are displayed for every
version of PowerShell.

  ７ Note

  Anytime a conceptual article is added, removed, or renamed, the TOC must be updated.
  Any deleted or renamed files must be redirected.

Metadata files
This project contains several types of metadata files. The metadata files control the behavior of
our build tools and the publishing system. Only PowerShell-Docs maintainers and approved
contributors are allowed to change these files. If you think that a meta file should be changed,
open an issue to discuss the needed changes.

<!-- p.2946 -->

Meta files in the root of the repository

         .* - configuration files in the root of the repository

         *.md - Project documentation in the root of the repository

         *.yml - Project documentation in the root of the repository

         .devcontainer/* - devcontainer configuration files

         .github/**/* - GitHub templates, actions, and other meta files

         .vscode/**/* - VS Code extension configurations

         assets/* - contains downloadable files linked in the documentation

         redir/* - contain redirection mapping files

         tests/* - test tools used by the build system

         tools/* - other tools used by the build system

Meta files in the documentation set

         reference/**/*.json - docset configuration files

         reference/**/*.yml - TOC and other structured content files

         reference/bread/* - breadcrumb navigation configuration

         reference/includes/* - markdown include files

         reference/mapping/* - version mapping configuration

         reference/**/media/** - image files used in documentation

         reference/module/* - Module Browser page configuration

Creating new articles
A GitHub issue must be created for any new document you want to contribute. Check for
existing issues to make sure you're not duplicating efforts. Assigned issues are considered to
be in progress . If you wish to collaborate on an issue, contact the person assigned to the
issue.

Similar to the PowerShell RFC process        , create an issue before you write the content. The issue
ensures you don't waste time and effort on work that gets rejected by the PowerShell-Docs
team. The issue allows us to consult with you on the scope of the content and where it fits in
the PowerShell documentation. All articles must be included in the Table of Contents (TOC). The
proposed TOC location should be included in the issue discussion.

  ７ Note

<!-- p.2947 -->

  The publishing system autogenerates the TOC for reference content. You don't have to
  update the TOC.

Updating existing articles
Where applicable, cmdlet reference articles are duplicated across all versions of PowerShell
maintained in this repository. When reporting an issue about a cmdlet reference or an About_
article, list the versions of the article that have the problem.

Apply the appropriate change to each version of the file.

Localized content
The PowerShell documentation is written in English and translated into 17 other languages. The
English content is stored in the GitHub repository named MicrosoftDocs/PowerShell-Docs .
Issues found in the translated content should be submitted to this repository.

All translations start from the English content first. We use both human and machine
translation.

                                                                                         ﾉ   Expand table

 Translation method        Languages

 Human translation         de-DE, es-ES, fr-FR, it-IT, ja-JP, ko-KR, pt-BR, ru-RU, zh-CN, zh-TW

 Machine translation       cs-CZ, hu-HU, nl-NL, pl-PL, pt-PT, sv-SE, tr-TR

The content translated by machine translation might not always result in correct word choices
and grammar. If you find an error in translation for any language, rather than in the technical
details of the article, open an issue explaining why you think the translation is wrong.

Some translation issues can be fixed by changing the English source files. However, some
issues can require updates to our internal translation system. For those cases, we must submit
the issue to our internal localization team for review and response.

Next steps
There are two common ways of submitting changes in GitHub. Both methods are described in
the central Contributor's Guide:

<!-- p.2948 -->

   1. You can make quick edits to existing documents in the GitHub web interface.
   2. Use the full GitHub workflow for adding new articles, updating multiple files, or other
      large changes.

Before starting any changes, you should create a fork of the PowerShell-Docs repository. The
changes should be made in a working branch in your copy of the PowerShell-Docs. If you're
using the quick edit method in GitHub, these steps are handled for you. If you're using the full
GitHub workflow, you must be set up to work locally.

Both methods end with the creation of a Pull Request (PR). For more information and best
practices, see Submitting a pull request.

 Last updated on 11/20/2025

<!-- p.2949 -->

Contribute using GitHub Codespaces
Article • 03/30/2025

GitHub has a feature called Codespaces        that you can use to contribute to the
PowerShell documentation without having to install or configure any software locally.
When you use a codespace, you get the same authoring tools the team uses for writing
and editing.

You can use a codespace in your browser, making your contributions in VS Code hosted
over the internet. If you have VS Code installed locally, you can connect to the
codespace there too.

Available tools
When you use a codespace to contribute to the PowerShell documentation, your editor
has these tools already available for you:

      Markdownlint       for checking your Markdown syntax.
      cSpell    for checking your spelling.
      Vale     for checking your prose.
      The Learn Authoring Pack       for inserting platform-specific syntax, previewing your
      contribution, and more.
      The Reflow Markdown         extension for wrapping your Markdown as needed,
      making reading and editing easier.
      The Table Formatter      extension for making your tables more readable without
      having to manually align columns.
      The change-case       extension for converting the casing of your headings and
      prose.
      The GitLens      extension for reviewing historical file changes.
      The PowerShell      extension for interacting authoring PowerShell examples.
      The Gremlins tracker for Visual Studio Code       for finding problematic characters in
      your Markdown.

Cost
GitHub Codespaces can be used for free up to 120 core-hours per month. The monthly
usage is calculated across all your repositories, not just documentation.

For more information about pricing, see About billing for GitHub Codespaces .

<!-- p.2950 -->

   Tip

  If you're comfortable using containers and Docker, you can get the same
  experience by using the devcontainer defined for the PowerShell documentation
  repositories. There's no cost associated with using devcontainers. For more
  information, see the Dev Containers tutorial .

Creating your GitHub Codespace
To create your GitHub Codespace for contributing to PowerShell documentation, follow
these steps:

   1. Open https://github.com/codespaces           in your browser.
   2. Select the "New codespace" button in the top right of the page.
   3. In the "Create a new codespace" page, select the "Select a repository" button and
     type the name of the repository you want to contribute to, like
     MicrosoftDocs/PowerShell-Docs .

   4. Leave all other settings as their default.
   5. Select the "Create codespace" button.

After following these steps, GitHub creates a new codespace for that repository and sets
it up for you. When the codespace is ready, the page refreshes and shows the web
editor UI for the codespace. The UI is based on VS Code and works the same way.

Opening your GitHub Codespace
To open your GitHub Codespace in the browser, follow these steps:

   1. Open https://github.com/codespaces           in your browser.
   2. The page lists your Codespaces. Find the created codespace for the repository you
     want to contribute to and select it.

After you select your codespace, GitHub opens it in the same window. From here, you're
ready to contribute.

To open your GitHub Codespace in VS Code, follow the steps in Using GitHub
Codespaces in Visual Studio Code      .

Authoring in your GitHub Codespace

<!-- p.2951 -->

Once you have your GitHub Codespace open in your browser or VS Code, contributing
to the documentation follows the same process.

The rest of this article describes a selection of tasks you can do in your GitHub
Codespace while writing or editing your contribution.

Extract a reference link
When you want to turn an inline link, like [some text](destination.md) , into a reference
link like [some text][01] , select the link destination in the editor. Then you can either:

   1. Right-click on the link destination and select "Refactor..." in the context menu.
   2. Press Ctrl + Shift + R .

Either action raises the refactoring context menu. To replace the (destination.md) in the
link with [def] , select Extract to link definition in the context menu. You can rename
the definition by typing a name in.

For the PowerShell documentation, we use two-digit numerical reference link definitions,
like [01] or [31] . Only use reference link definitions in about articles and conceptual
documentation. Don't use reference link definitions in cmdlet reference documentation.

Fix prose style violations
When you review an article in your codespace, Vale automatically checks the article
when you first open it and every time you save it. If Vale finds any style violations, it
highlights them in the document with colored squiggles.

Hover over a violation to see more information about it.

To open a web page that explains the rule, select the rule's name in the hover
information. To open the rule and review its implementation, select the rule's filename
(ending in .yml ).

If the rule supports a quick fix, you can select "Quick Fix..." in the hover information for
the violation and apply one of the suggested fixes by selecting it from the context
menu. You can also press Ctrl + . when your cursor is on a highlighted problem to
apply a quick fix if the rule supports it.

If the rule doesn't support quick fixes, read the rule's message and fix it if you can. If
you're not sure how to fix it, the editors can make a suggestion when reviewing your PR.

Fix syntax problems

<!-- p.2952 -->

When you review an article in your codespace, Markdownlint automatically checks the
article when you open it and as you type. If Markdownlint finds any syntax problems, it
highlights them in the document with colored squiggles.

Hover over a violation to see more information about it. To open a web page that
explains the rule, select the rule's ID in the hover information.

If the rule supports a quick fix, you can select "Quick Fix..." in the hover information for
the violation and apply one of the suggested fixes by selecting it from the context
menu. You can also press Ctrl + . when your cursor is on a highlighted problem to
apply a quick fix if the rule supports it.

If the rule doesn't support quick fixes, read the rule's message and fix it if you can. If
you're not sure how to fix it, the editors can make a suggestion when reviewing your PR.

You can also apply fixes to all syntax violations in an article. To do so, open the
command palette and type Fix all supported markdownlint violations in the
document . As you type, the command palette filters the available commands. Select the

"Fix all supported markdownlint violations in the document" command. When you do,
Markdownlint updates the document to resolve any violations it has a quick fix for.

Format a table
To format a Markdown table, place your cursor in or on the table in your Markdown.
Open the Command Palette and search for the Table: Format Current command. When
you select that command, it updates the Markdown for your table to align and pad the
table for improved readability.

It converts a table defined like this:

  markdown

  | foo | bar | baz |
  |:--:|:--|-:|
  | a | b | c |

Into this:

  markdown

  | foo | bar | baz |
  | :---: | :--- | ---: |
  |   a   | b    |    c |

<!-- p.2953 -->

Insert an alert
The documentation uses alerts to make information more notable to a reader.

To insert an alert, you can, open the Command Palette and search for the Learn: Alert
command. When you select that command, it opens a context menu. Select the alert
type you want to add. When you do, the command inserts the alert's Markdown at your
cursor in the document.

Make a heading use sentence casing
To convert a heading's casing, highlight the heading's text except for the leading #
symbols, which set the heading level. When you have the text highlighted, open the
Command Palette and search for the Change case sentence command. When you select
that command, it converts the casing of the highlighted text.

You can also use the casing commands for any text in the document.

Open the Command Palette
You can use VS Code's Command Palette       to run many helpful commands.

To open the Command Palette in the UI, select "View" in the top menu bar. Then select
"Command Palette..." in the context menu.

To open the Command Palette with your keyboard, press the key combination for your
operating system:

     Windows and Linux: Ctrl + Shift + P
     macOS: Cmd + Shift + P

Preview your contribution
To preview your contribution, open the Command Palette and search for the Markdown:
Open Preview command. When you select that command, VS Code opens a preview of

the active document. The preview's style matches the Learn platform.

  ７ Note

  Site-relative and cross-reference links don't work in the preview.

<!-- p.2954 -->

Reflow your content
To limit the line lengths for a paragraph in a document, place your cursor on the
paragraph. Then open the Command Palette and search for the Reflow Markdown
command. When you select the command, it updates the current paragraph's line
lengths to the configured length. For our repositories, that length is 99 characters.

When using this command for block quotes, make sure the paragraph in the block
quote you're reflowing is surrounded by blank lines. Otherwise, the command reflows
every paragraph together.

  Ｕ Caution

  Don't use this command when editing about articles. The lines in those documents
  must not be longer than 80 characters. There's currently no way for a repository to
  configure different line lengths by folder or filename, so reflow doesn't work for
  about article documents.

Review all problems in a document
To review all syntax and style rule violations in a document, open the Problems View.

To open the Problems View in the UI, select "View" in the top menu bar. Then select
"Problems" in the context menu.

To open the Problems View with your keyboard, press the key combination for your
operating system:

     Windows and Linux: Ctrl + Shift + M
     macOS: Cmd + Shift + M

The Problems View displays all errors, warnings, and suggestions for the open
document. Select a problem to scroll to it in the document.

You can filter the problems by type or text matching.

Updating the ms.date metadata
To update the ms.date metadata for an article, open the Command Palette and search
for the Learn: Update "ms.date" Metadata Value command. When you select the
command, it updates the metadata to the current date.

<!-- p.2955 -->

Additional resources
The tasks and commands described in this article don't cover everything you can do
with VS Code or the installed extensions.

For more information on using VS Code, see these articles:

     Visual Studio Code Tips and Tricks
     Basic Editing
     Using Git source control in VS Code
     Markdown and Visual Studio Code

For more information about the installed extensions, see their documentation:

     change-case
     GitLens
     Gremlins tracker for Visual Studio Code
     Learn Authoring Pack
     markdownlint
     Reflow Markdown
     Table Formatter

<!-- p.2956 -->

Markdown best practices
Article • 04/29/2025

This article provides specific guidance for using Markdown in our documentation. It isn't a
tutorial for Markdown. If you need a tutorial for Markdown, see this Markdown cheatsheet          .

The build pipeline that builds our documentation uses markdig        to process the Markdown
documents. Markdig parses the documents based on the rules of the latest CommonMark
specification. OPS follows the CommonMark specification and adds some extensions for
platform-specific features, such as tables and alerts.

The CommonMark specification is stricter about the construction of some Markdown elements.
Pay close attention to the details provided in this document.

We use the markdownlint       extension in VS Code to enforce our style and formatting rules.
This extension is installed as part of the Learn Authoring Pack.

Blank lines, spaces, and tabs
Blank lines also signal the end of a block in Markdown.

      Put a single blank between Markdown blocks of different types; for example, between a
      paragraph and a list or header.
      Don't use more than one blank line. Multiple blank lines render as a single blank line in
      HTML, therefore the extra blank lines are unnecessary.
      Don't use put multiple consecutive blank lines in a code block, consecutive blank lines
      break the code block.

Spacing is significant in Markdown.

      Remove extra spaces at the end of lines. Trailing spaces can change how Markdown
      renders.
      Always use spaces instead of tabs (hard tabs).

Titles and headings
Use ATX headings       only ( # style, as opposed to = or - style headers).

      Use sentence case - only proper nouns and the first letter of a title or header should be
      capitalized
      Include a single space between the # and the first letter of the heading
      Surround headings with single blank line

<!-- p.2957 -->

        Don't use more than one H1 per document
           It should be the first header
           It should match the title of the article
        Increment header levels by one - don't skip levels
        Limit depth to H3 or H4
        Avoid using bold or other markup in headers

Limit line length to 100 characters
For conceptual articles and cmdlet reference, limit lines to 100 characters. For about_ articles,
limit the line length to 79 characters. Limiting the line length improves the readability of git
diffs and history. It also makes it easier for other writers to make contributions.

Use the Reflow Markdown          extension in VS Code to reflow paragraphs to fit the prescribed
line length.

Some content types can't be easily reflowed. For example, the code inside of code blocks can
also be difficult to reflow, depending on the content and the code language. You can't reflow a
table. In these cases, use your best judgment to keep the content as close to the 100-character
limit as possible.

Emphasis
For emphasis, Markdown supports bold and italics. Markdown allows you to use either * or _
to mark the emphasis. However, to be consistent and show intent:

        Use ** for bold
        Use _ for italics

Following this pattern makes it easier for others to understand the intent of the markup when
there's a mix of bold and italics in a document.

Lists
If your list has multiple sentences or paragraphs, consider using a sublevel header rather than a
list.

Surround lists with a single blank line.

Unordered lists

<!-- p.2958 -->

     Don't end list items with a period unless they contain multiple sentences.
     Use the hyphen character ( - ) for list item bullets to avoid confusion with emphasis
     markup that uses the asterisk ( * ).
     To include a paragraph or other elements under a bullet item, insert a line break and align
     indentation with the first character after the bullet.

For example:

  Markdown

  This is a list that contains child elements under a bullet item.

  - First bullet item

     Sentence explaining the first bullet.

     - Child bullet item

       Sentence explaining the child bullet.

  - Second bullet item
  - Third bullet item

This is a list that contains child elements under a bullet item.

     First bullet item

     Sentence explaining the first bullet.

        Child bullet item

        Sentence explaining the child bullet.

     Second bullet item

     Third bullet item

Ordered lists
     All items in a numbered list should use the number 1. rather than incrementing each
     item.
        Markdown rendering increments the value automatically.
        This makes reordering items easier and standardizes the indentation of subordinate
        content.
     To include a paragraph or other elements under a numbered item, align indentation with
     the first character after the item number.

<!-- p.2959 -->

For example:

  Markdown

  1. For the first element, insert a single space after the `1`. Long sentences
  should be wrapped to
     the next line and must line up with the first character after the numbered list
  marker.

     To include a second element, insert a line break after the first and align
  indentations. The
     indentation of the second element must line up with the first character after
  the numbered list
     marker.

  1. The next numbered item starts here.

The resulting Markdown is rendered as follows:

   1. For the first element, insert a single space after the 1 . Long sentences should be wrapped
     to the next line and must line up with the first character after the numbered list marker.

     To include a second element, insert a line break after the first and align indentations. The
     indentation of the second element must line up with the first character after the
     numbered list marker.

   2. The next numbered item starts here.

Images
The syntax to include an image is:

  Markdown

  ![[alt text]](<folderPath>)

  Example:
  ![Introduction](./media/overview/Introduction.png)

Where alt text is a brief description of the image and <folderPath> is a relative path to the
image.

     Alternate text is required to support screen readers for the visually impaired.
     Images should be stored in a media/<article-name> folder within the folder containing
     the article.

<!-- p.2960 -->

        Create a folder that matches the filename of your article under the media folder. Copy
        the images for that article to that new folder.
     Don't share images between articles.
        If an image is used by multiple articles, each folder must have a copy of that image.
        This prevents a change to an image in one article from affecting another article.

The following image file types are supported: *.png , *.gif , *.jpeg , *.jpg , *.svg

Markdown extension - Alert boxes
The Learn Authoring Pack contains tools that support features unique to our publishing system.
Alerts are a Markdown extension to create blockquotes that render with colors and icons
highlighting the significance of the content. The following alert types are supported:

  Markdown

  > [!NOTE]
  > Information the user should notice even if skimming.

  > [!TIP]
  > Optional information to help a user be more successful.

  > [!IMPORTANT]
  > Essential information required for user success.

  > [!CAUTION]
  > Negative potential consequences of an action.

  > [!WARNING]
  > Dangerous certain consequences of an action.

These alerts look like this on Microsoft Learn:

Note block

  ７ Note

  Information the user should notice even if skimming.

Tip block

   Tip

  Optional information to help a user be more successful.
