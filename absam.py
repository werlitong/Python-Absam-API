import requests
import time
import sys


#usage:
#absam.exe "AccessToken" "SecretToken" "cloudid" "(suspend|unsuspend)"

url = 'https://api.absam.io/v1/cloud-server'
try:
    AccessToken = sys.argv[1]
    SecretToken = sys.argv[2]
    cloudid = sys.argv[3]
    action = sys.argv[4]
except:
    print("At least one argument not provided")
    sys.exit(1)

def suspend():
    endpoint = url + '/suspend'
    headers = {'access-token': AccessToken,'secret-access-token': SecretToken}
    body = {'id': cloudid}
    response = requests.post(endpoint,data=body,headers=headers)
    data = response.json()
    print(data)
    print("this screen will close in {} seconds".format(3))
    time.sleep(3)
    sys.exit(0)
    
def unsuspend():
    endpoint = url + '/unsuspend'
    headers = {'access-token': AccessToken,'secret-access-token': SecretToken}
    body = {'id': cloudid}
    response = requests.post(endpoint,data=body,headers=headers)
    data = response.json()
    print(data)
    print("this screen will close in {} seconds".format(3))
    time.sleep(3)
    sys.exit(0)

def main():
    if (action == "suspend"):
        suspend()
    elif (action == "unsuspend"):
        unsuspend()

if __name__ == '__main__':
    main()