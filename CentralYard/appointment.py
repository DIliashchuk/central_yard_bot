import requests
import json
import http.client


def book_staff():
    url = "https://api.alteg.io/api/v1/book_staff/777559"

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
      'Authorization': 'Bearer kmhut9umky73276yryjt, User 5efa5ab2f2474930209f9392c78a3dab',
      'Cookie': '__cf_bm=NJFDriHP.FkxsIVI2ocWV3l9iF124QWz69vNU2ZvbCg-1700492464-0-AbTgX3FM9c4aQSQL2l+Apfgxv4'
                'iZOS0mIJYiJCisQIdHqTUpO1z3ztTkhP5RqRFF/RSxFmo1+EYDbDlej6LqC/w=; _ga_b1ff3p=GS1.1-2.1664391493.1.1.'
                '1664391604.0.0.0; _ga_b1ffHf=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_dqrr=GS1.1-2.1664391493.1.1.'
                '1664391604.0.0.0; auth=kio09h8nt3u1d5im4dtoqeae1m904csincupd8uq7i7jijh75r25f7al0kqpf7v6'
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


def services():

    url = "https://api.alteg.io/api/v1/company/777559/services"

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
        'Authorization': 'Bearer kmhut9umky73276yryjt, User 5efa5ab2f2474930209f9392c78a3dab',
        'Cookie': '__cf_bm=oy43Sz80c4M0y.8v7jMuFbklXIZ4DYOrPJQHlcbS1fE-1700493967-0-ASgfzgiWWyru8+tKv5ut'
                  '837+qIuZKloz7in0L0cxJ4Va3FDEwCO9Iuxwjdm3EqNimTTPKoe2sPIYosDwpbXhgrk=; _ga_b1ff3p=GS1.1-2.'
                  '1664391493.1.1.1664391604.0.0.0; _ga_b1fgkd=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_dqrr=GS1.'
                  '1-2.1664391493.1.1.1664391604.0.0.0; auth=kio09h8nt3u1d5im4dtoqeae1m904csincupd8uq7i7'
                  'jijh75r25f7al0kqpf7v6'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        service_list = {}

        for staff_member in data.get('data', []):
            service_id = staff_member.get('id')
            service_name = staff_member.get('booking_title')
            service_list[service_name] = service_id
        return service_list
    else:
        print("Ошибка при запросе:", response.status_code)


def book_dates(staff_id):
    url = f"https://api.alteg.io/api/v1/book_dates/777559?staff_id={staff_id}"

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
        'Authorization': 'Bearer kmhut9umky73276yryjt, User 5efa5ab2f2474930209f9392c78a3dab',
        'Cookie': '__cf_bm=al1Mz8EUz9y4Z2WtaRueiqNKdvjU1Xdt.iKMmW7fkyk-1700568479-0-AZWOJx3Jn7Hz3glyRMNp7OmB1'
                  'mWSm0vcgMt/Xt9VoaXXTRKcYVPbUh/G1YjTrxkvuWY7sTElZykmQsBiOcC09CU=; _ga_b1fzH1=GS1.1-2.1664391493.'
                  '1.1.1664391604.0.0.0; _ga_dqrr=GS1.1-2.1664391493.1.1.1664391604.0.0.0; auth=kio09h8nt3u1d5im4'
                  'dtoqeae1m904csincupd8uq7i7jijh75r25f7al0kqpf7v6'
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        booking_dates = data.get('data', {}).get('booking_dates', [])
        return booking_dates
    else:
        print("Ошибка при запросе:", response.status_code)


def book_times(date):

    url = f"https://api.alteg.io/api/v1/book_times/777559/2219665/{date}"

    payload = json.dumps({
      "success": True,
      "data": [
        {},
        {},
        {},
        {},
        {}
      ],
      "meta": []
    })
    headers = {
      'Accept': 'application/vnd.api.v2+json',
      'Content-Type': 'application/json',
      'Authorization': 'Bearer kmhut9umky73276yryjt, User 5efa5ab2f2474930209f9392c78a3dab',
      'Cookie': '__cf_bm=WwI80tCHxMoP4ncjE3Ie9INcc.VtVDPSPRg.X7v6Kk4-1700562213-0-ASqa9wi1dsB4tfsi4i'
                'RIMQDMzNaALOyfBbA9+/s8KR9+lRdeYAY++oJfhKxr22aErTnszNK4mE/AzB2qJhFnSts=; _ga_b1fx49=GS1.1-2.'
                '1664391493.1.1.1664391604.0.0.0; _ga_b1fx5h=GS1.1-2.1664391493.1.1.1664391604.0.0.0; _ga_dqrr=GS1.'
                '1-2.1664391493.1.1.1664391604.0.0.0; auth=kio09h8nt3u1d5im4dtoqeae1m904csincupd8uq7i7jijh75r'
                '25f7al0kqpf7v6'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        book_list = {}

        for book_time in data.get('data', []):
            booking_time = book_time.get('time')
            book_datetime = book_time.get('datetime')
            book_list[booking_time] = book_datetime
        return book_list
    else:
        print("Ошибка при запросе:", response.status_code)

    print(response.text)


def finallys(service_id, staff_id, full_time_info):
    conn = http.client.HTTPSConnection("api.alteg.io")
    payload = json.dumps({
        "phone": "+380657628742",
        "fullname": "Ihor Myshkin",
        "email": "lalalend@gigbyte.das",
        "appointments": [
            {
              "id": 1,
              "services": [
                service_id
              ],
              "staff_id": staff_id,
              "datetime": full_time_info
            }
          ]
    })
    headers = {
        'Accept': 'application/vnd.api.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer kmhut9umky73276yryjt, User 5efa5ab2f2474930209f9392c78a3dab',
        'Cookie': 'auth=kio09h8nt3u1d5im4dtoqeae1m904csincupd8uq7i7jijh75r25f7al0kqpf7v6'
    }
    try:
        conn.request("POST", "/api/v1/book_record/777559", payload, headers)
        res = conn.getresponse()
        if res.status == 200 or res.status == 201:
            print("Успешная запись")
        elif res.status == 422:
            error_message = res.read().decode("utf-8")
            print(f"Ошибка записи. Сообщение об ошибке: {error_message}")
        else:
            print(f"Ошибка записи. Код состояния: {res.status}")
    except http.client.HTTPException as e:
        print(f"Ошибка при выполнении запроса: {e}")

