import requests
import json


def staff():
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
        staff_list = []

        for staff_member in data.get('data', []):
            staff_id = staff_member.get('id')
            staff_name = staff_member.get('name')
            full_staff = staff_id, staff_name
            staff_list.append(full_staff)
        return staff_list
    else:
        print("Ошибка при запросе:", response.status_code)


print(staff())


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
        service_list = []

        for staff_member in data.get('data', []):
            service_id = staff_member.get('id')
            service_name = staff_member.get('booking_title')
            full_info = service_id, service_name
            service_list.append(full_info)
        return service_list
    else:
        print("Ошибка при запросе:", response.status_code)

print(services())


