from pytrials.client import ClinicalTrials
import pandas as pd

ct = ClinicalTrials()

def get_full_studies():
    # Get 50 full studies related to Coronavirus and COVID in csv format.
    full_studies = ct.get_full_studies(search_expr="Coronavirus+COVID", max_studies=50)
    # Convert the list of dictionaries to a DataFrame
    full_studies_df = pd.DataFrame.from_records(full_studies[1:], columns=full_studies[0])

    # Save the full studies in a csv file.
    full_studies_df.to_csv("full_studies.csv", index=False)
    print("Full studies saved in full_studies.csv")
    return full_studies

def get_study_fields():
    # Get the NCTId, Condition and Brief title fields from 1000 studies related to Coronavirus and Covid, in csv format.
    corona_fields = ct.get_study_fields(
        search_expr="Coronavirus+COVID",
        fields=["NCT Number", "Conditions", "Study Title"],
        max_studies=1000,
        fmt="csv",
    )
    # Read the csv data in Pandas

    results = pd.DataFrame.from_records(corona_fields[1:], columns=corona_fields[0])

    results.to_csv("corona_fields.csv", index=False)
    print("Corona studies saved in corona_fields.csv")

    return corona_fields


if __name__ == "__main__":
    get_full_studies()
    get_study_fields()