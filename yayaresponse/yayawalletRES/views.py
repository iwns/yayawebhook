from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import hmac
import hashlib

# Create your views here.
#make request 

@csrf_exempt
def transaction_handler(request):
    if request.method == 'POST':
        print(request.META.get('User-Agent'))
        try:
            payload = json.loads(request.body.decode('utf-8'))
            print(payload)
            yayaSignture = request.META.get('YAYA-SIGNATURE')
            print(header)
            signed_payload = payload['id']+str(payload['amount'])+payload['currency']+str(payload['created_at_time'])+str(payload['timestamp'])+payload['cause']+payload['full_name']+payload['account_name']+payload['invoice_url']

            signature=hmac.new(bytes('secretkey','utf-8'),bytes(signed_payload,'utf-8'),hashlib.sha256)
            print(signature.hexdigest())
            if hmac.compare_digest(signature,yayaSignture):
                id = payload['id']
                amount = payload['amount']
                currency = payload['currency']
                createdTime = payload['created_at_time']
                timestamp = payload['timestamp']
                cause = payload['cause']
                fullname = payload['full_name']
                accountname = payload['account_name']
                invoiceURL = payload['invoice_url']
                print('samesignture')

            return HttpResponse('successfull')#({'status':"success"},status=200)
        except json.JSONDecodeError:
            return HttpResponse('failed')#({'error':"Invalid JSON"},status=400)
        
    return HttpResponse("response")
