import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/SIRREG001/c4bb5f8e2bcccc1a8eeb95ca7f576b8f/raw/7fa59fb47d47872c2f01132dbb3bcbe500c8361c/udochukwu-reginald-linkedin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_key = os.environ.get("PROXYCURL_API_KEY")
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'linkedin_profile_url': linkedin_profile_url,
            'use_cache': 'if-recent'

        }
        response = requests.get(
            api_endpoint,
            params=params,
            headers=headers,
            timeout=10
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certification"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/udochukwu-reginald-971938225/", mock=True
        )
    )
