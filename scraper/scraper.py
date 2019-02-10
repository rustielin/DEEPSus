from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
from osisoft.pidevclub.piwebapi.rest import ApiException
from urllib3 import disable_warnings

disable_warnings()

client = PIWebApiClient("https://ucd-pi-iis.ou.ad3.ucdavis.edu/piwebapi", useKerberos=False, verifySsl=False)

buildings = ['Activities and Recreation Center', 'Genome & Biomedical Sciences Facility', 'Giedt Hall', 'Mrak Hall', 'Olson Hall', 'RMI Brewery, Winery, and Food Pilot Facility', 'Shields Library', 'Tercero 2', 'Tercero 3', 'Tercero Dining Commons']
types = ["ChilledWater", "Electricity", "Steam"]
attributes = ["MonthlyUsage", "Demand"]

query = "af:\\CEFS\\UCDAVIS\\Buildings\\{0}\\{1}|{2}"
wifi_query = "af:\\REST POSTs to PI\\REST POSTs to PI\\UFL\\UFL\\Wifi Access Points\\ARC|Total_Count"

for b in buildings:
    for t in types:
        for a in attributes:
            try:
                df = client.data.get_interpolated_values(query.format(b, t, a), start_time="*-1m", interval="5s")
                df.to_csv("data/{0}_{1}_{2}".format(b, t, a))
                print("Saving: {0} {1} {2}".format(b, t, a))
            except ApiException:
                print("No Endpoint for: {0} {1} {2}".format(b, t, a))


wifi_df = client.data.get_interpolated_values(wifi_query, start_time="*-1m", interval="5s")
wifi_df.to_csv("data/ARC_WiFi_TotalCount")
print("Saving: ARC WiFi TotalCount")