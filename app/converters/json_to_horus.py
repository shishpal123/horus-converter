import pandas as pd

def convert_json_to_horus(input_path, output_path):
    df = pd.read_json(input_path, orient='index')
    df.drop(['ISO-2-CODE', 'ISO-3-Code'], axis=1, inplace=True)
    df.rename(columns={'Country': 'CountryName', 'ISO-M49': 'CountryNumber'}, inplace=True)
    df.set_index('CountryNumber', inplace=True)
    df.sort_values('CountryName', ascending=False, inplace=True)
    df.to_csv(output_path, index=False)

