import pandas as pd
import plotly.express as px
from datetime import datetime

data_urls = {
    "confirmed":
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
    "deaths":
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
    "recovered":
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
}


class CovidDataExplorer:

    def __init__(self, data_urls):
        self.data_urls = data_urls
        self.dataframes = {
            key: self.prepare_data(pd.read_csv(url))
            for key, url in data_urls.items()
        }
        self.selected_data_type = None
        self.country = None
        self.start_date = None
        self.end_date = None

    def prepare_data(self, df):
        #This prepares the datasets by removing unnecessary columns, melting and renaming columns, and converting dates to datetime objects
        df = df.drop(columns=["Province/State", "Lat", "Long"])
        df_melt = df.melt(id_vars=["Country/Region"],
                          var_name="Date",
                          value_name="Cases")
        df_melt.rename(columns={"Country/Region": "Country"}, inplace=True)
        df_melt["Date"] = pd.to_datetime(df_melt["Date"],
                                         format="%m/%d/%y",
                                         errors="coerce")
        return df_melt

    def get_country_input(self):
        #Asks the user to input a country name and returns it. If entered country is invalid, it asks to try again.
        while True:
            self.country = input("Enter your country of choice: ").strip()
            if self.country.lower() == 'exit':
                return None
            country_lower = self.country.lower()
            if any(country_lower in map(str.lower, df["Country"].values)
                   for df in self.dataframes.values()):
                return country_lower
            else:
                print("Invalid country. Please try again.")

    def get_data_type_input(self):
        #Asks the user go input the data type they want to see and if invalid, it asks to try again.
        while True:
            self.selected_data_type = input(
                "Enter the data type of choice (confirmed, deaths, recovered, all): "
            ).strip().lower()
            if self.selected_data_type == 'exit':
                return None
            if self.selected_data_type in self.dataframes or self.selected_data_type == "all":
                return self.selected_data_type
            else:
                print("Invalid data type. Please try again.")

    def get_date_range_input(self):
        #Asks the user to input start and end dates, if invalid, it asks to try again.
        while True:
            start_date = input(
                "Enter the start date (e.g. 01/23/20): ").strip()
            end_date = input("Enter the end date (e.g. 03/09/23): ").strip()

            if start_date.lower() == 'exit' or end_date.lower() == 'exit':
                return None, None

            try:
                start_date = datetime.strptime(start_date, "%m/%d/%y")
                end_date = datetime.strptime(end_date, "%m/%d/%y")

                if end_date < start_date:
                    print(
                        "End date cannot be before start date. Please try again."
                    )
                    continue

                return start_date, end_date
            except ValueError:
                print("Invalid date format. Please try again.")

    def get_filtered_data(self):
        """Filtert die Daten basierend auf den Nutzerangaben."""
        country_lower = self.country.lower()
        filtered_dfs = {
            key: df[df["Country"].str.lower() == country_lower]
            for key, df in self.dataframes.items()
        }

        if self.selected_data_type == "all":
            combined_df = pd.concat([
                filtered_dfs["confirmed"]
                [(filtered_dfs["confirmed"]["Date"] >= self.start_date) &
                 (filtered_dfs["confirmed"]["Date"] <= self.end_date)].assign(
                     Type="Confirmed"), filtered_dfs["deaths"]
                [(filtered_dfs["deaths"]["Date"] >= self.start_date)
                 & (filtered_dfs["deaths"]["Date"] <= self.end_date)].assign(
                     Type="Deaths"), filtered_dfs["recovered"]
                [(filtered_dfs["recovered"]["Date"] >= self.start_date) &
                 (filtered_dfs["recovered"]["Date"] <= self.end_date)].assign(
                     Type="Recovered")
            ])
            return combined_df
        else:
            return filtered_dfs[self.selected_data_type][
                (filtered_dfs[self.selected_data_type]["Date"] >=
                 self.start_date) & (filtered_dfs[self.selected_data_type]
                                     ["Date"] <= self.end_date)]

    def visualize_data(self, result):
        #Visualizes the data
        title_data_type = "Confirmed, Deaths, and Recovered" if 'Type' in result.columns else self.selected_data_type.capitalize(
        )

        fig = px.line(
            result,
            x="Date",
            y="Cases",
            color="Type" if "Type" in result.columns else None,
            title=
            f"COVID-19 {title_data_type} Cases in {result['Country'].iloc[0]}")
        fig.show()

    def run(self):
        #Main function to run the program & welcomr message
        print(
            "Welcome to the COVID-19 Data Explorer!\nWith this tool you can visualize the COVID-19 data across different countries and time periods.\n\n"
            "Please enter a country, time period, and data type (e.g. confirmed, deaths, recovered).\n"
            "(Note: Available dates are:\n1/23/20 - 3/9/23 [MM/DD/YY])\n\nTo exit the explorer, type 'exit'.\n"
        )

        if not self.get_country_input():
            print("Thank you for using the COVID-19 Data Explorer. Goodbye!")
            return

        if not self.get_data_type_input():
            print("Thank you for using the COVID-19 Data Explorer. Goodbye!")
            return

        self.start_date, self.end_date = self.get_date_range_input()
        if self.start_date is None or self.end_date is None:
            print("Thank you for using the COVID-19 Data Explorer. Goodbye!")
            return

        result = self.get_filtered_data()

        if result is not None:
            print("\nChart is loading. Please wait...\n")
            self.visualize_data(result)

#Start the program
if __name__ == "__main__":
    explorer = CovidDataExplorer(data_urls)
    explorer.run()
