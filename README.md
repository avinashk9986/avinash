# avinash

# REST API

## what is this?

```
Simple api example using flask. a flask api object contains one or more functionalities (GET, POST, Delete). It perform below tasks :-
a. Allows users to submit/post messages
b. Lists received messages
c. Retrieves a specific message on demand, and determines if it is a palindrome.
d. Allows users to delete specific messages

```

## install

```
yum install python
pip install boto3
python createinstance.py
ssh -i key.ppk ec2-user@public-ip

```

## run

```
python application.py

```

## Sample output

```
[root@ip-172-31-17-216 ~]# curl -X POST http://54.146.17.200:5005/message/avi1
{
    "message": "avi1"
}


[root@ip-172-31-17-216 ~]# curl -X GET http://54.146.17.200:5005/list
[
    {
        "message": "avinash"
    },
    {
        "message": "alok"
    },
    {
        "message": "vivek"
    }
]
[root@ip-172-31-17-216 ~]# curl -X GET http://54.146.17.200:5005/message/avinash
"{'message': 'avinash'}  string isn't a palindrome "

[root@ip-172-31-17-216 ~]# curl -X DELETE http://54.146.17.200:5005/message/avi1
"avi1 is deleted."

```
