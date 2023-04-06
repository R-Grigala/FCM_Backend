import json
import requests

def send_notification(registration_ids, message_title, message_desc):
    fcm_api = "AAAA8ILaOzc:APA91bFRapskgwOn3YgPI--eXo63jJalU5rd8FJbDOu3b0O5r1SyqyHnDZnOtPgp4_tf5T50MwGT90s-Y_0ozVW5uuR6Df4D9aF1ucu4jjpjlBihZO-4YI9xMCzDWzHMVQrwq25huxkt"
    fcm_api2 = "AAAAY_kXJbY:APA91bFyN8qNkgG-Es_SaENqkdTxZ5v4g4D2E2s6hAQi05wkDhQBDFnviCyciWJJtFXlfCoZNW_pFGsAQYJwFfzQeYPf6wsC07STEkJ6aOkaM3WPcwFe99IR5jeLMouvfIrTFptNFN54" 
    url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        "Content-Type":"application/json",
        "Authorization": 'key=' + fcm_api2
    }

    payload = {
        "registration_ids" : registration_ids,
        "priority" : "high",
        "notification" : {
            "body": message_desc,
            "title" : message_title,
            "image" : "",
            "icon" : ""
        }
    }

    result = requests.post(url, data=json.dumps(payload), headers=headers)
    print(result.json())


registratin_ids2 = ['ezT9dNbGRUWRr9j2NrpaPs:APA91bGx2JJZ1o2KbMntRBVAoc5d6X0HEESkuiHYOln3wlfcnxAguMmMIqL_kPCArVoQ-V1Pd4e5a2src3YX0Ppt2nSDNxXdby6FpV6lTosip3f2d68ev-Bv6aomCVbDm9Yl7bDNgbqn']
registratin_ids = ['d4BY7MyVTyqqNHbUXrJo_E:APA91bF8MNbmeh-onVWzmOBQCtuWXpI-Jbh10tL6y6fi-qu4sIIOev_rbpYdAwIFmEeD5vLPwjCuK2KfXPlrKMNJTW30TUG6dZ_O4iYwsbvvw_PqmMFhRmiUGQlbR6UCcCFd4oqo64m-']
message_desc = "Test Test"
message_title = "Test Test"
send_notification(registration_ids=registratin_ids2, message_title='Test Test', message_desc='Test Test')