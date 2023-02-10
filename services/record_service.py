import os
import json
from models import GLOBALS
from services.redis_service import RedisService
from helpers.streamlit_helpers import streamlit_session_helper as session_helper, streamlit_helper as sh
from helpers.http_helpers import http_helper
from datetime import datetime, date
import json

cache_service = RedisService()


def SendHelpCall(params):
    http_helper.send_request(os.getenv("API_BASE_URL"), method="POST", body_params=params)


def RefreshCallData():
    redis_service = RedisService()
    available_call_data = redis_service.Get(GLOBALS.CALLER_DATA_CACHE_KEY)
    params = {}
    if available_call_data is not None:
        cached_call_data_list = json.loads(available_call_data)
        most_up_to_date_date = cached_call_data_list[0].zaman
        params = {"guncel_zaman": most_up_to_date_date}

        up_to_date_call_data = http_helper.send_request(os.getenv("API_BASE_ENDPOINT"), method="GET",
                                                        query_params=params)

        up_to_date_call_data = up_to_date_call_data + cached_call_data_list
    else:
        up_to_date_call_data = http_helper.send_request(os.getenv("API_BASE_ENDPOINT"), method="GET",
                                                        query_params=params)

    redis_service.Set(GLOBALS.CALLER_DATA_CACHE_KEY, json.dumps(up_to_date_call_data))


def FilterCallData(province, district, needs, name, notes, start_date, end_date):
    params = __CreateCallParamDict(province, district, name, needs, notes, start_date, end_date)

    call_data_response = http_helper.send_request(os.getenv("API_BASE_ENDPOINT"), method="GET", query_params=params)


def CreateCallRecord(payload):
    response = None
    if ValidateCallDataPayload(payload):
        url = os.getenv("API_BASE_ENDPOINT") + os.getenv("CREATE_CALL_DATA_ENDPOINT")
        response = http_helper.send_request(url, method="POST",
                                            body_params=payload)

    return response


def CreateHelperRecord(payload):
    response = None
    # print(payload)
    if ValidateHelperDataPayload(payload):
        url = os.getenv("API_BASE_ENDPOINT") + os.getenv("CREATE_HELPER_MAP_DATA_ENDPOINT")
        response = http_helper.send_request(url, method="POST",
                                            body_params=payload)

    return response


def ValidateCallDataPayload(payload):
    if payload is None or len(payload) == 0 or payload["il"] == "" or payload["ilce"] == "" or \
            payload["adres"] == "" or payload["lat"] == "" or payload["lon"] == "" or payload["isim"] == "":
        return False

    if len(payload["gereksinimler"]) == 0:
        payload["gereksinimler"] = ["Diğer"]

    payload["zaman"] = str(datetime.now())

    return True


def GetFullCallRecords():  # fulldataya bak ?
    all_call_record_result = cache_service.Get(GLOBALS.CALLER_DATA_CACHE_KEY)
    if all_call_record_result is not None:
        return json.loads(all_call_record_result)

    url = os.getenv("API_BASE_ENDPOINT") + os.getenv("API_GET_CALL_MAP_DATA_ENDPOINT")
    all_call_record_result = http_helper.send_request(url, method="POST")
    all_call_record_result = all_call_record_result.json()["detail"]
    cache_service.Set(GLOBALS.CALLER_DATA_CACHE_KEY, json.dumps(all_call_record_result))

    return all_call_record_result


def GetFullHelperRecords():
    all_helper_record_result = cache_service.Get(GLOBALS.HELPER_DATA_CACHE_KEY)
    if all_helper_record_result is not None:
        return json.loads(all_helper_record_result)

    url = os.getenv("API_BASE_ENDPOINT") + os.getenv("API_GET_HELPER_MAP_DATA_ENDPOINT")
    all_helper_record_result = http_helper.send_request(url, method="POST")
    all_helper_record_result = all_helper_record_result.json()["detail"]
    cache_service.Set(GLOBALS.HELPER_DATA_CACHE_KEY, json.dumps(all_helper_record_result))

    return all_helper_record_result


def GetCallRecords(province=None, district=None, name=None, needs=None, notes=None, phone=None, start_date=None,
                   end_date=None):
    params = __CreateCallParamDict(province, district, name, needs, notes, phone, start_date, end_date)
    if len(params) == 0:
        return json.loads(GetFullCallRecords())
    # print(params)
    url = os.getenv("API_BASE_ENDPOINT") + os.getenv("API_GET_CALL_MAP_DATA_ENDPOINT")
    call_record_result = http_helper.send_request(url, method="POST", body_params=params)
    call_record_result = call_record_result.json()["detail"]

    return call_record_result


def GetHelperRecords(province=None, district=None, name=None, needs=None, notes=None, phone=None, start_date=None,
                     end_date=None):
    params = __CreateHelperParamDict(province, district, name, needs, notes, phone, start_date, end_date)
    if len(params) == 0:
        return json.loads(GetFullHelperRecords())
    # print(params)
    url = os.getenv("API_BASE_ENDPOINT") + os.getenv("API_GET_HELPER_MAP_DATA_ENDPOINT")
    # print(url)
    call_record_result = http_helper.send_request(url, method="POST", body_params=params)
    call_record_result = call_record_result.json()["detail"]
    # print(call_record_result)

    return call_record_result


def FillCallRecordString(last_records):
    last_records_list = []

    for rec in last_records:
        gereksinimler = ""
        if "gereksinimler" in rec:
            gereksinimler = f"İhtiyaç: {rec['gereksinimler']}"
        else:
            gereksinimler = f"Servis: {rec['servis']}"

        tarih_str = ""
        if "zaman" in rec:
            tarih_str = f"Tarih: {rec['zaman']}   |"

        last_records_list.append(f"""
                {tarih_str}   İl: {rec["il"]}   |   İlçe: {rec["ilce"]}

İsim: {rec["isim"]}

Adres: {rec["adres"]}

{gereksinimler}

İletişim Bilgisi: {rec["telefon"]}

Notlar: {rec["notlar"]}
            """)
    return last_records_list


def GetRawLocationDataForMap(province=None, district=None, name=None, needs=None, notes=None, start_date=None,
                             end_date=None):
    call_record_result = None
    if session_helper.get_session('second_page_selected_option') == "caller":
        call_record_result = GetCallRecords(province, district, name, needs, notes, start_date, end_date)
    else:
        call_record_result = GetHelperRecords(province, district, name, needs, notes, start_date, end_date)
    return call_record_result


def GetLatLongsForMap(province=None, district=None, name=None, needs=None, notes=None, start_date=None, end_date=None):
    call_record_result = GetRawLocationDataForMap(province, district, name, needs, notes, start_date, end_date)
    return [[res["lat"], res["lon"]] for res in call_record_result]

def __CreateCallParamDict(province, district, name, needs, notes, phone, start_date, end_date):
    return {"il": province, "ilce": district, "gereksinimler": needs, "notlar": notes, "telefon": phone,
            "baslangic_zaman": start_date,
            "bitis_zaman": end_date, "isim": name}


def ValidateHelperDataPayload(payload):
    if payload is None or len(payload) == 0 or payload["il"] == "" or payload["ilce"] == "" or \
            payload["adres"] == "" or payload["lat"] == "" or payload["lon"] == "" or payload["isim"] == "":
        return False

    if len(payload["servis"]) == 0:
        payload["servis"] = ["Diğer"]

    return True


def __CreateHelperParamDict(province, district, name, needs, notes, phone, start_date, end_date):
    return {"il": province, "ilce": district, "servis": needs, "notlar": notes, "telefon": phone,
            "baslangic_zaman": start_date,
            "bitis_zaman": end_date, "isim": name}
