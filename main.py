import json

import requests


def processPage(from_):
    print(f"Processing page {from_}")
    response = requests.post(
        'https://careers.adobe.com/widgets',
        headers=getHeaders(),
        data=json.dumps(getPayload(from_))
    )
    parsedResponse = response.json()['refineSearch']
    for job in parsedResponse['data']['jobs']:
        for multi_location in job['multi_location_array']:
            print(job['jobId'])
            data = {
                "cityState": job['cityState'],
                "country": job['country'],
                "city": job['city'],
                "mlSkills": ", ".join(job['ml_skills']) if "ml_skills" in job else "",
                "latitude": job['latitude'],
                "type": job['type'],
                "locale": job['locale'],
                "title": job['title'],
                "multiLocationLon": multi_location['latlong']['lon'],
                "multiLocation": multi_location['location'],
                "jobSeqNo": job['jobSeqNo'],
                "postedDate": job['postedDate'],
                "descriptionTeaser": job['descriptionTeaser'],
                "experienceLevel": job['experienceLevel'],
                "dateCreated": job['dateCreated'],
                "state": job['state'],
                "cityStateCountry": job['cityStateCountry'],
                "visibilityType": job['visibilityType'],
                "siteType": job['siteType'],
                "longitude": job['longitude'],
                "address": job['address'],
                "isMultiCategory": job['isMultiCategory'],
                "multiCategory": ", ".join(job['multi_category']),
                "reqId": job['reqId'],
                "jobId": job['jobId'],
                "badge": job['badge'],
                "jobVisibility": ", ".join(job['jobVisibility']),
                "isMultiLocation": job['isMultiLocation'],
                "applyUrl": job['applyUrl'],
                "location": job['location'],
                "category": job['category'],
                "externalApply": job['externalApply'],
            }
            # print(data)


def main():
    response = requests.post(
        'https://careers.adobe.com/widgets',
        headers=getHeaders(),
        data=json.dumps(getPayload(0))
    )
    parsedResponse = response.json()['refineSearch']
    totalHits = parsedResponse['totalHits']
    print(f"Total Hits: {totalHits}")
    for from_ in range(0, totalHits, 100):
        processPage(from_)


def getHeaders():
    return {
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }


def getPayload(from_):
    return {
        "from": from_,
        "size": 100,
        "jobs": True,
        "counts": True,
        "global": True,
        "isSliderEnable": True,
        "clearAll": True,
        "lang": "en_us",
        "deviceType": "desktop",
        "country": "us",
        "ddoKey": "refineSearch",
        "pageType": "category",
        "jdsource": "facets",
    }


if __name__ == '__main__':
    main()
