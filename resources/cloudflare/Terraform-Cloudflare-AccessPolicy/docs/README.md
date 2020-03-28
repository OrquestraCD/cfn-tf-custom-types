# Terraform::Cloudflare::AccessPolicy

Provides a Cloudflare Access Policy resource. Access Policies are used
in conjunction with Access Applications to restrict access to a
particular resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::AccessPolicy",
    "Properties" : {
        "<a href="#applicationid" title="ApplicationId">ApplicationId</a>" : <i>String</i>,
        "<a href="#decision" title="Decision">Decision</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#precedence" title="Precedence">Precedence</a>" : <i>Double</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#exclude" title="Exclude">Exclude</a>" : <i>[ <a href="exclude.md">Exclude</a>, ... ]</i>,
        "<a href="#include" title="Include">Include</a>" : <i>[ <a href="include.md">Include</a>, ... ]</i>,
        "<a href="#require" title="Require">Require</a>" : <i>[ <a href="require.md">Require</a>, ... ]</i>,
        "<a href="#azure" title="Azure">Azure</a>" : <i>[ <a href="azure.md">Azure</a>, ... ]</i>,
        "<a href="#github" title="Github">Github</a>" : <i>[ <a href="github.md">Github</a>, ... ]</i>,
        "<a href="#gsuite" title="Gsuite">Gsuite</a>" : <i>[ <a href="gsuite.md">Gsuite</a>, ... ]</i>,
        "<a href="#okta" title="Okta">Okta</a>" : <i>[ <a href="okta.md">Okta</a>, ... ]</i>,
        "<a href="#saml" title="Saml">Saml</a>" : <i>[ <a href="saml.md">Saml</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::AccessPolicy
Properties:
    <a href="#applicationid" title="ApplicationId">ApplicationId</a>: <i>String</i>
    <a href="#decision" title="Decision">Decision</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#precedence" title="Precedence">Precedence</a>: <i>Double</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#exclude" title="Exclude">Exclude</a>: <i>
      - <a href="exclude.md">Exclude</a></i>
    <a href="#include" title="Include">Include</a>: <i>
      - <a href="include.md">Include</a></i>
    <a href="#require" title="Require">Require</a>: <i>
      - <a href="require.md">Require</a></i>
    <a href="#azure" title="Azure">Azure</a>: <i>
      - <a href="azure.md">Azure</a></i>
    <a href="#github" title="Github">Github</a>: <i>
      - <a href="github.md">Github</a></i>
    <a href="#gsuite" title="Gsuite">Gsuite</a>: <i>
      - <a href="gsuite.md">Gsuite</a></i>
    <a href="#okta" title="Okta">Okta</a>: <i>
      - <a href="okta.md">Okta</a></i>
    <a href="#saml" title="Saml">Saml</a>: <i>
      - <a href="saml.md">Saml</a></i>
</pre>

## Properties

#### ApplicationId

The ID of the application the policy is
associated with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Decision

Defines the action Access will take if the policy matches the user.
Allowed values: `allow`, `deny`, `non_identity`, `bypass`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Friendly name of the Access Application.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Precedence

The unique precedence for policies on a single application. Integer.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone to which the access rule should be
added.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclude

_Required_: No

_Type_: List of <a href="exclude.md">Exclude</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Include

_Required_: No

_Type_: List of <a href="include.md">Include</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Require

_Required_: No

_Type_: List of <a href="require.md">Require</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Azure

_Required_: No

_Type_: List of <a href="azure.md">Azure</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Github

_Required_: No

_Type_: List of <a href="github.md">Github</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gsuite

_Required_: No

_Type_: List of <a href="gsuite.md">Gsuite</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Okta

_Required_: No

_Type_: List of <a href="okta.md">Okta</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Saml

_Required_: No

_Type_: List of <a href="saml.md">Saml</a>

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

