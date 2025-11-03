import base64

encoded_string = "KRUGKUDFOJZWS43UMVXGGZKPMZGWK3LPOJ4UIYLMNE"

decoded_bytes = base64.b32decode(encoded_string)

decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
decoded_string
