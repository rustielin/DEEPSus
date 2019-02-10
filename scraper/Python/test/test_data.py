# coding: utf-8

"""
	Copyright 2017 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	  <http://www.apache.org/licenses/LICENSE-2.0>

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""

import unittest
from osisoft.pidevclub.piwebapi.models import PIAnalysis, PIItemsStreamValues, PIStreamValues, PITimedValue
from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
from osisoft.pidevclub.piwebapi.rest import ApiException


class TestData(unittest.TestCase):
    def getPIWebApiClient(self):
        """
            TODO: The PI Web API client must provide a user name and password when using “basic” authentication
            Store passwords outside of the code in a hardware TPM, trusted service (credential manager) or in a protected file.
            Code to return the user name and password is not shown here.
        """
        return PIWebApiClient("https://devdata.osisoft.com/piwebapi", False, "webapiuser", "!try3.14webapi!", True)


    def test_data_convertPathToWebId(self):
        client = self.getPIWebApiClient()
        webId = client.data.convert_path_to_web_id("pi:\\PISRV1\sinusoid")
        print(webId)
        pass

    def test_data_convertPathToWebIds(self):
        client = self.getPIWebApiClient()
        paths = []
        paths.append("pi:\\PISRV1\sinusoid")
        paths.append("pi:\\PISRV1\sinusoidu")
        paths.append("pi:\\PISRV1\cdt158")
        webIds = client.data.convert_paths_to_web_ids(paths)
        print(webIds)
        pass

    def test_data_recorded(self):
        client = self.getPIWebApiClient()

        df1 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", start_time="*-1d", end_time="*")
        df1b = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", start_time="*-1d", end_time="*", selected_fields="items.value;items.timestamp")
        df1b = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", start_time="*-1d", end_time="*", selected_fields="items.good;items.questionable;items.substituted")
        df2 = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoidu", start_time="*-10d", end_time="*")
        df3 = client.data.get_recorded_values("pi:\\\\PISRV1\\cdt158", start_time="*-10d", end_time="*-9d")
        df4 = client.data.get_recorded_values("af:\\\\PISRV1\\Universities\\UC Davis\\Buildings\\Academic Surge Building\\Electricity|AnnualUsage", start_time="*-10d", end_time="*-9d")

        df5 = client.data.get_interpolated_values("pi:\\PISRV1\\sinusoid", start_time="*-1d", end_time="*", interval="1h")
        df5b = client.data.get_interpolated_values("pi:\\PISRV1\\sinusoid", start_time="*-1d", end_time="*", interval="1h", selected_fields="items.value;items.timestamp")
        df6 = client.data.get_interpolated_values("pi:\\PISRV1\\sinusoidu", start_time="*-1d", end_time="*", interval="2h")
        df7 = client.data.get_interpolated_values("pi:\\PISRV1\\cdt158",None, "*", None, None, "3h", None, "*-1d", None, None, None)
        df8 = client.data.get_interpolated_values("af:\\\\PISRV1\\Universities\\UC Davis\\Buildings\\Academic Surge Building\\Electricity|AnnualUsage", None, "*", None, None, "3h", None, "*-20d", None, None, None)



        df9 = client.data.get_plot_values("pi:\\\\PISRV1\\sinusoid", end_time="*", intervals=15, start_time= "*-1d")
        df9b = client.data.get_plot_values("pi:\\\\PISRV1\\sinusoid", None, "*", 15, "items.value;items.timestamp", "*-1d", None)
        df10 = client.data.get_plot_values("pi:\\\\PISRV1\\sinusoidu", None, "*", 10, None, "*-3d", None)
        df11 = client.data.get_plot_values("pi:\\\\PISRV1\\cdt158", None, "*", 20, None, "*-2d", None)
        df12 = client.data.get_plot_values("af:\\\\PISRV1\\Universities\\UC Davis\\Buildings\\Academic Surge Building\\Electricity|AnnualUsage", None, "*", 20, None, "*-40d", None)
        pass

    def test_data_summary(self):
        client = self.getPIWebApiClient()
        df1 = client.data.get_summary_values("pi:\\\\PISRV1\\sinusoid", start_time="*-1d", end_time="*",
                                             summary_type=['Average'], summary_duration='1h')
        df2 = client.data.get_summary_values("pi:\\\\PISRV1\\sinusoid", start_time="*-1d", end_time="*",
                                             summary_type=['Average', 'Total'], summary_duration='1h')
        pass

    def test_getExceptionError(self):
        client = self.getPIWebApiClient()
        paths=["pi:\\\\PISRV1\\sinusoid", "pi:\\\\PISRV1\\sinusoidu", "pi:\\\\PISRV1\\cdt158"]


        try:
            df1b = client.data.get_recorded_values("pi:\\\\PISRV1\\sinusoid", None, None, "*", None, None, None,"a", "*-1d", None)
        except Exception as e:
            if (e.args[0]!='The returned data is Null or None'):
                raise Exception('Unexpected exception')

        try:
            dfs1c = client.data.get_multiple_recorded_values(paths, None, "*", None, None, None, "value;timestamp",None, None,"*-1d", None, None)
        except Exception as e:
            if (e.args[0]!='The returned data is Null or None'):
                raise Exception('Unexpected exception')

        try:
            dfs1c = client.data.get_multiple_recorded_values(paths, None, "*", None, None, None, "a", None, None, "*-1d", None, None)
        except Exception as e:
            if (e.args[0]!='The returned data is Null or None'):
                raise Exception('Unexpected exception')

        try:
            dfs1d = client.data.get_multiple_recorded_values(paths, None, "*", None, None, None, "items.value;items.timestamp",None, None, "*-1d", None, None)
        except Exception as e:
            if (e.args[0] != 'Some items are Null or None.'):
                raise Exception('Unexpected exception')
        pass

        try:
            dfs2b = client.data.get_multiple_interpolated_values(paths, "*", None, None, "1h", "items.value;items.timestamp", None, None, "*-5d", None, None, None, None)
        except Exception as e:
            if (e.args[0] != 'Some items are Null or None.'):
                raise Exception('Unexpected exception')

        try:
            dfs2b = client.data.get_multiple_interpolated_values(paths, "*", None, None, "1h", "a", None, None, "*-5d", None, None, None, None)
        except Exception as e:
            if (e.args[0] != 'The returned data is Null or None'):
                raise Exception('Unexpected exception')

        try:
            dfs2b = client.data.get_multiple_interpolated_values(paths, "*", None, None, "1h","value;timestamp", None, None, "*-5d", None, None, None, None)
        except Exception as e:
            if (e.args[0] != 'The returned data is Null or None'):
                raise Exception('Unexpected exception')



    def test_data_multiple_recorded(self):
        client = self.getPIWebApiClient()
        paths = ["pi:\\\\PISRV1\\sinusoid", "pi:\\\\PISRV1\\sinusoidu", "pi:\\\\PISRV1\\cdt158"]

        dfs1 = client.data.get_multiple_recorded_values(paths, start_time="*-1d", end_time= "*")
        dfs2 = client.data.get_multiple_interpolated_values(paths, start_time="*-1d", end_time="*", interval="1h")
        dfs3 = client.data.get_multiple_plot_values(paths,  start_time="*-1d", end_time="*", intervals="14")

        dfs1b = client.data.get_multiple_recorded_values(paths, start_time="*-1d", end_time="*",
                                                     selected_fields="items.items.value;items.items.timestamp")
        dfs2b = client.data.get_multiple_interpolated_values(paths, start_time="*-1d", end_time="*", interval="1h",
                                                     selected_fields="items.items.value;items.items.timestamp")
        dfs3b = client.data.get_multiple_plot_values(paths,  start_time="*-1d", end_time="*", intervals="14",
                                                     selected_fields="items.items.value;items.items.timestamp")

        dfs1 = client.data.get_multiple_recorded_values(paths, None, "*", None, None, None, None, None, None, "*-1d", None, None)
        dfs2 = client.data.get_multiple_interpolated_values(paths, "*", None, None, "1d", None, None, None, "*-5d", None, None, None, None)
        dfs3 = client.data.get_multiple_plot_values(paths, "*", 14, None, None, None, "*-1d", None, None)

        dfs1b = client.data.get_multiple_recorded_values(paths, None, "*", None, None, None, "items.items.value;items.items.timestamp",None, None, "*-1d", None, None)
        dfs2b = client.data.get_multiple_interpolated_values(paths, "*", None, None, "1h", "items.items.value;items.items.timestamp", None, None,"*-5d", None, None, None, None)
        dfs3b = client.data.get_multiple_plot_values(paths, "*", 10, "items.items.value;items.items.timestamp", None, None, "*-1d", None, None)
        pass


if __name__ == '__main__':
    unittest.main()
