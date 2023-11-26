import requests
import json
import http.client


def book_staff():
    url = "https://api.alteg.io/api/v1/book_staff/92533"

    payload = json.dumps({
      "success": True,
      "data": [
        {},
        {}
      ],
      "meta": []
    })
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer m4mbf8khn2a4anacm2ej, User 6e82ffb3f03dc939f9abf65bd92292b1',
        'Cookie': '__cf_bm=Eo0hI47mSlO03CR7Ln5oOldIdCwE.4sY1dp1sSU69Vo-1700826951-0-AXj7+NjGBBWmXFNSre1DxUbsH6U+NrChyJ/'
                  '1Fniag3Mn0Jucexs8b1XJWMk12z3lWOcKxkTW5kRir/OpzOGD1B4=;'
                  ' _ga_b1gE8Q=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEXb=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEYQ=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gFbm=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_yeD=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' auth=666ase19j9u8qpdoq8f7cst0elc85f2utm2310dm8ie5bea6l5pv7uh4vqob1kvh'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        staff_list = {}

        for staff_member in data.get('data', []):
            staff_id = staff_member.get('id')
            staff_name = staff_member.get('name')
            staff_list[staff_name] = staff_id
        return staff_list
    else:
        print("Ошибка при запросе:", response.status_code)


def services(category_id):

    url = "https://api.alteg.io/api/v1/company/92533/services"

    payload = json.dumps({
        "success": True,
        "data": [
            {},
            {}
        ],
        "meta": {
            "total_count": 2
        }
    })
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer m4mbf8khn2a4anacm2ej, User 6e82ffb3f03dc939f9abf65bd92292b1',
        'Cookie': '__cf_bm=5ld0uPizVltKwZkLjc3T3FHtzi23V.yXe0fdEntEDpY-1700828138-0-Ae1Y4LOM'
                  'x3oJ9F4SxPZxkWWbI7YveLXIHD6/SpFlVn4JsDnLNJpA756z2Qds/PJvz/unyZqCNaXwzDcwmiw+Fo8=;'
                  ' _ga_b1gE8Q=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEXb=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEYQ=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gFbm=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_yeD=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' auth=666ase19j9u8qpdoq8f7cst0elc85f2utm2310dm8ie5bea6l5pv7uh4vqob1kvh'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        service_list = {}

        for service in data.get('data', []):
            if service.get('category_id') == category_id:
                service_id = service.get('id')
                service_name = service.get('title')
                service_list[service_name] = service_id

        return service_list
    else:
        print("Ошибка при запросе:", response.status_code)


def book_dates(staff_id):
    url = f"https://api.alteg.io/api/v1/book_dates/92533?staff_id={staff_id}"

    payload = json.dumps({
        "success": True,
        "data": {
            "booking_days": {},
            "booking_dates": [],
            "working_days": {},
            "working_dates": []
        },
        "meta": []
    })
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer m4mbf8khn2a4anacm2ej, User 6e82ffb3f03dc939f9abf65bd92292b1',
        'Cookie': '__cf_bm=5ld0uPizVltKwZkLjc3T3FHtzi23V.yXe0fdEntEDpY-1700828138-0-Ae1Y4LOMx3oJ9F4SxPZxkW'
                  'WbI7YveLXIHD6/SpFlVn4JsDnLNJpA756z2Qds/PJvz/unyZqCNaXwzDcwmiw+Fo8=;'
                  ' _ga_b1gE8Q=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEXb=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEYQ=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gFbm=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gFpN=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_yeD=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' auth=666ase19j9u8qpdoq8f7cst0elc85f2utm2310dm8ie5bea6l5pv7uh4vqob1kvh'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        booking_dates = data.get('data', {}).get('booking_dates', [])
        return booking_dates
    else:
        print("Ошибка при запросе:", response.status_code)


def finallys(service_id, staff_id, selected_date, selected_time, name, phone, email):
    conn = http.client.HTTPSConnection("api.alteg.io")
    payload = json.dumps({
        "phone": phone,
        "fullname": name,
        "email": email,
        "appointments": [
            {
              "id": 1,
              "services": [
                service_id
              ],
              "staff_id": staff_id,
              "datetime": f'{selected_date} {selected_time}'
            }
          ]
    })
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer m4mbf8khn2a4anacm2ej, User 6e82ffb3f03dc939f9abf65bd92292b1',
        'Cookie': '__cf_bm=bMg.8lxa22JTb2GBXTFNgq2tLolTL1o_lv7IAh0zi5k-1700829158-0-AWQKAXHYPuNu0R02B7VFt/'
                  'NYE/K6voIr40DzHrvYRhuWPA5oEd1eebC+F7UrM2icKSYVobHrDF2N3T/3QPC1M6s=;'
                  ' _ga_b1gE8Q=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEXb=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gEYQ=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gFbm=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gFpN=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1gFwV=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_yeD=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' auth=666ase19j9u8qpdoq8f7cst0elc85f2utm2310dm8ie5bea6l5pv7uh4vqob1kvh'
    }
    try:
        conn.request("POST", "/api/v1/book_record/92533", payload, headers)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201:
            print("Успешная запись")
            return True
        elif res.status == 422:
            error_message = res.read().decode("utf-8")
            print(f"Ошибка записи. Сообщение об ошибке: {error_message}")
            return False
        else:
            print(f"Ошибка записи. Код состояния: {res.status}")
            return False
    except http.client.HTTPException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return False


def book_time(staff_id, selected_date):
    url = f"https://api.alteg.io/api/v1/book_times/92533/{staff_id}/{selected_date}"

    payload = json.dumps({
        "success": True,
        "data": [],
        "meta": []
    })
    headers = {
        'Accept': 'application/vnd.api.v2+json ',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer m4mbf8khn2a4anacm2ej, User 6e82ffb3f03dc939f9abf65bd92292b1',
        'Cookie': '__cf_bm=GKViXQijTzlJCmZS64vuoZFcmGnn2HSsNNgeHQX8eE4-1701005662-0-AV02qqF7sdUaGIo+Y'
                  'kEuTA/OfWVGVmByAUTWKMvpdFeIEVMz/5db9/grXV4iMBJM02uvaAILZ5K4Xnn8nZ3hkOU=; _ga_b1ho4E=GS1.'
                  '1-2.1664391493.1.1.1664391604.0.0.0; _ga_b1ho4h=GS1.1-2.1664391493.1.1.1664391604.0.0.0;'
                  ' _ga_b1ho6y=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_b1ho7j=GS1.1-2.1664391493.1.1.166'
                  '4391604.0.0.0; _ga_b1hpcG=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_b1hpcT=GS1.1-2.166439'
                  '1493.1.1.1664391604.0.0.0; _ga_b1hpcg=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_b1hpd9=GS1.1'
                  '-2.1664391493.1.1.1664391604.0.0.0; _ga_b1hpdk=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_b1h'
                  'pdy=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_b1hpeg=GS1.1-2.1664391493.1.1.1664391604.0.0.0; '
                  '_ga_b1hprm=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_b1hpss=GS1.1-2.1664391493.1.1.1664391604.'
                  '0.0.0; _ga_yeD=GS1.1-2.1664391493.1.1.1664391604.0.0.0; auth=kio09h8nt3u1d5im4dtoqeae1m904csinc'
                  'upd8uq7i7jijh75r25f7al0kqpf7v6'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        time_list = []
        for staff_member in data.get('data', []):
            work_time = staff_member.get('time')
            work_seance = staff_member.get('seance_length')
            if work_seance >= 3600:
                time_list.append(work_time)
        return time_list
    else:
        print("Ошибка при запросе:", response.status_code)



