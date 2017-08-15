import hvac
from pprint import pprint

def main():
    client = hvac.Client(url='http://10.81.15.28:8200')#, token='c689c11f-f51f-0ebc-d797-20dd239b7fc5')
    client.auth_github('6ebc8f4eb3729b344fa2eca8abe538398de97196')
    assert client.is_authenticated()

    #backends = client.list_auth_backends()
    #pprint(backends)

    client.write('cubbyhole/foo', value='bar')

    print(client.read('cubbyhole/foo'))

    client.delete('cubbyhole/foo')
    #print(client.read('secret/hello'))

if __name__ == '__main__':
    main()
