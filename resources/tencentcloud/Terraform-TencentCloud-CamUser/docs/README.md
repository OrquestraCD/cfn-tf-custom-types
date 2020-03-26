# Terraform::TencentCloud::CamUser

Provides a resource to create a CAM user.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::CamUser",
    "Properties" : {
        "<a href="#consolelogin" title="ConsoleLogin">ConsoleLogin</a>" : <i>Boolean</i>,
        "<a href="#countrycode" title="CountryCode">CountryCode</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#needresetpassword" title="NeedResetPassword">NeedResetPassword</a>" : <i>Boolean</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#phonenum" title="PhoneNum">PhoneNum</a>" : <i>String</i>,
        "<a href="#remark" title="Remark">Remark</a>" : <i>String</i>,
        "<a href="#useapi" title="UseApi">UseApi</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::CamUser
Properties:
    <a href="#consolelogin" title="ConsoleLogin">ConsoleLogin</a>: <i>Boolean</i>
    <a href="#countrycode" title="CountryCode">CountryCode</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#needresetpassword" title="NeedResetPassword">NeedResetPassword</a>: <i>Boolean</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#phonenum" title="PhoneNum">PhoneNum</a>: <i>String</i>
    <a href="#remark" title="Remark">Remark</a>: <i>String</i>
    <a href="#useapi" title="UseApi">UseApi</a>: <i>Boolean</i>
</pre>

## Properties

#### ConsoleLogin

Indicate whether the CAM user can login or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CountryCode

Country code of the phone num, like '86'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

Email of the CAM user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of CAM user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeedResetPassword

Indicate whether the CAM user will reset the password the next time he/her logs in.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of the CAM user. The password should be set with 8 characters or more and contains uppercase small letters, numbers, and special characters. Only valid when console_login set true. If not set and the value of console_login is true, a random password is automatically generated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhoneNum

Phone num of the CAM user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remark

Remark of the CAM user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseApi

Indicate whether to generate a secret key or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### SecretId

Returns the <code>SecretId</code> value.

#### SecretKey

Returns the <code>SecretKey</code> value.

#### Uid

Returns the <code>Uid</code> value.

#### Uin

Returns the <code>Uin</code> value.

