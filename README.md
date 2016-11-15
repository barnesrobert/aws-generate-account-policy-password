# aws-generate-account-policy-password

This is an AWS Python tool for generating a random password that complies with the given account's password policy. Random passwords can be generated using the AWS IAM console, but there is currently no API to do this programmatically. This can be useful when programmatically creating IAM users or when provisioning users in CloudFormation.

When using the [console](https://console.aws.amazon.com/iam/home?region=us-east-1#/account_settings), AWS account administrators can create a password policy that meets an organization's password complexity requirements, like setting a minimum length or requiring uppercase letters, numbers, and symbols. 

The password policy can also be viewed using the AWS CLI using the following command:

```
aws iam get-account-password-policy
```

Output:

```
{
    "PasswordPolicy": {
        "AllowUsersToChangePassword": true,
        "RequireLowercaseCharacters": true,
        "RequireUppercaseCharacters": true,
        "MinimumPasswordLength": 8,
        "RequireNumbers": true,
        "RequireSymbols": true,
        "HardExpiry": false,
        "ExpirePasswords": false
    }
}

```

To execute the aws-generate-account-policy-password function, the principal must have at least the following policy:
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:GetAccountPasswordPolicy",
      "Resource": "*"
    }
  ]
}
```
