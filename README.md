# Iterate and exterminate a AWS Account

AWS Daleks will iterate through resources in a AWS Account in reverse dependency order and optionally exterminate them.

**DISCLAIMER**

This project is not sponsored, affiliated, supported or at all related to neither Amazon nor BBC.

**WARNING**

**Iterating through resources may incur in costs.**

**Extermination is irreversible.**

1- Install SBT:
```
brew install sbt
```

2- Setup credentials
```
aws configure
```
Any other credential in the default credentials chain works: http://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/credentials.html

3- Just fly, don't exterminate (a.k.a dry run): 
```
  sbt run
```

4- EXTERMINATE!
```
  sbt "run exterminate"
```

The following resources are not exterminated:
- IAM Users or Roles with names containing "DO-NOT-DELETE" or starts with a "Lord of The Rings" location (e.g. MordorOverlordRole).
- IAM User used to execute

    Exterminate!
                   /
              ___
      D>=G==='   '.
            |======|
            |======|
        )--/]IIIIII]
           |_______|
           C O O O D
          C O  O  O D
         C  O  O  O  D
         C__O__O__O__D
        [_____________]
