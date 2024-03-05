import requests
import pandas as pd
from datetime import datetime, timedelta

def get_wikipedia_revisions(url_titles, rv_start="", rv_end=""):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "revisions",
        "titles": url_titles,
        "rvprop": "timestamp|user|comment|tags|size|parsedcomment",
        "rvslots": "main",
        "formatversion": "2",
        "format": "json",
        "rvlimit": 500,
        "rvend": rv_end,
        "rvstart": rv_start
    }

    with requests.Session() as session:
        try:
            response = session.get(url=base_url, params=params)
            response.raise_for_status() 
            data = response.json()
            pages = data.get("query", {}).get("pages", [])
            if pages:
                revisions = pages[0].get("revisions", [])
                return revisions
        except requests.RequestException as e:
            print(f"Error in get_wikipedia_revisions for {url_titles}: {e}")
    return None

def generate_graph(day):
    df = pd.read_csv('events_data.csv')
    url_list = ["Perovskite_solar_cell", "Solar_cell", "Semiconductor"]
    all_event_revision_counts = {url: {} for url in url_list}

    for url in url_list:
        try:
            for index, row in df.iterrows():
                event_date_str = row['Event date']
                event_name = row['Event name']
                event_description = row['Event description']
                event_date = datetime.strptime(event_date_str, '%B %d, %Y')
                window_end = event_date + timedelta(days=day)
                # print("event_date:", event_date)
                # print("window_end:", window_end)
                revisions = get_wikipedia_revisions(url, window_end.strftime('%Y-%m-%d %H:%M:%S'), event_date.strftime('%Y-%m-%d %H:%M:%S'))
                revision_info_list = [{'timestamp': revision['timestamp'], 'comment': revision.get('parsedcomment', '')} for revision in revisions] if revisions else [] 
                all_event_revision_counts[url][str(event_date)] = revision_info_list
        except Exception as e:
            print(f"Error in generate_graph for {url}: {e}")

    # print(all_event_revision_counts)
    return all_event_revision_counts