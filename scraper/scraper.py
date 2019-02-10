from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
from osisoft.pidevclub.piwebapi.rest import ApiException

import urllib3
import json

path_prefix = "~/hack-davis-osi-bucket/"

urllib3.disable_warnings()

client = PIWebApiClient("https://ucd-pi-iis.ou.ad3.ucdavis.edu/piwebapi", useKerberos=False, verifySsl=False)

buildings = ['Activities and Recreation Center', 'Genome & Biomedical Sciences Facility', 'Giedt Hall', 'Mrak Hall', 'Olson Hall', 'RMI Brewery, Winery, and Food Pilot Facility', 'Shields Library', 'Tercero 2', 'Tercero 3', 'Tercero Dining Commons']
types = ["ChilledWater", "Electricity", "Steam"]
attributes = ["Demand", "Cumulative Use"]

query = "af:\\CEFS\\UCDAVIS\\Buildings\\{0}\\{1}|{2}"
wifi_query = "af:\\REST POSTs to PI\\REST POSTs to PI\\UFL\\UFL\\Wifi Access Points\\ARC|Total_Count"
# fields = "Items.value;Items.timestamp;Items.unitabbr"
start = "*-24h"
query_interval = "10m"

# for b in buildings:
for t in types:
    for a in attributes:
        try:
            df = client.data.get_interpolated_values(query.format(buildings[0], t, a), start_time=start, interval=query_interval)
            unit = df['UnitsAbbreviation'][0]
            df = df[['Value', 'Timestamp']]
            avg = df['Value'].mean()
            data = {}
            # pairs = df.to_dict()
            data['Points'] = [{"x" : timestamp, "y" : value} for timestamp, value in zip(df['Value'], df['Timestamp'])]
            data['Average'] = avg
            data['Units'] = unit

            print(data)

            with open("data/{0}_{1}_{2}.json".format(buildings[0], t, a), "w") as f:
                json.dump(data, f)
                print("Saving: {0} {1} {2}".format(buildings[0], t, a))

        except ApiException:
            print("No Endpoint for: {0} {1} {2}".format(buildings[0], t, a))


wifi_df = client.data.get_interpolated_values(wifi_query, start_time=start, interval=query_interval)
unit = wifi_df['UnitsAbbreviation'][0]
wifi_df = df[['Value', 'Timestamp']]
avg = wifi_df['Value'].mean()
data = {}
data['Points'] = [{"x" : timestamp, "y" : value} for timestamp, value in zip(wifi_df['Value'], wifi_df['Timestamp'])]
data['Average'] = avg
data['Units'] = unit

with open("data/ARC_WiFi_TotalCount.json", "w") as f:
    json.dump(data, f)
    print("Saving: ARC WiFi TotalCount")
