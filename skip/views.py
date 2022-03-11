from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from skip.src.client.skip import crud
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from skip.src.client.skip import ttypes
# Create your views here.


def index(request):
    return render(request, "web.html")

def insert(request):
    data = request.GET
    key = data.get('key')
    value = data.get('value')
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = crud.Client(protocol)
    transport.open()
    flag = client.insert_element(key, value)
    transport.close()
    if flag == 1:
        return JsonResponse({
            'result': "insert [" + key + "," + value +"], success!",
        })
    else:
        return JsonResponse({
            'result': "key " + key + " already exist!",
        })


def delete(request):
    data = request.GET
    key = data.get('key')
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = crud.Client(protocol)
    transport.open()
    flag = client.delete_element(key)
    transport.close()

    if flag == 1:
        return JsonResponse({
            'result': "delete key " + key + " success!",
        })
    else:
        return JsonResponse({
            'result': "key "+ key + " not found!",
        })



def search(request):
    data = request.GET
    key = data.get('key')
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = crud.Client(protocol)
    transport.open()
    r = client.search_element(key)
    transport.close()
    return JsonResponse({
            'result': r.msg,
        })

