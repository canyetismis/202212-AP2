import pandas as pd


def normalise_names(dataframe: pd.DataFrame, name_column: str):

    # make letters uppercase
    dataframe[name_column] = dataframe[name_column].str.upper()

    # replace German characters with ASCII letters
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'Ä', 'AE', regex=True)
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'Ö', 'OE', regex=True)
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'Ü', 'UE', regex=True)
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'ẞ', 'SS', regex=True)

    # Handle Separators
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'\sU.\s|\s&\s', ' UND ', regex=True)

    # Remove all punctuation and replace with spaces
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'[^A-Z0-9&]', ' ', regex=True)

    # Replace KG/Kommanditgesellschaft
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'\sK\s?G(\s?|$)|KOMMANDITGESELLSCHAFT', ' KG', regex=True)

    # Replace CO KG
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'\sC\s?O\s?KG(\s?|$)', ' CO KG', regex=True)

    # Replace GMBH and handle GMBHUND
    regex_str = r'\sG\s?M\s?B\s?H(\s|$)|GESELLSCHAFT\s?M\s?B\s?H(\s|$)|GESELLSCHAFT\s?MIT\s?BESCHRAENKTER\s?HAFTUNG(\s|$)'
    dataframe[name_column] = dataframe[name_column].str.replace(
        regex_str, ' GMBH', regex=True)
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'GMBHUND', ' GMBH UND ', regex=True)

    # Replace AG/AKTIENGESELLSCHAFT
    dataframe[name_column] = dataframe[name_column].str.replace(
        '\sA\s?G(\s|$)|AKTIENGESELLSCHAFT', ' AG', regex=True)

    # Replace OHG/OFFENE HANDELSGESELLSCHAFT
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'\sO\s?H\s?G(\s|$)|OFFENE\s?HANDELSGESELLSCHAFT', ' OHG', regex=True)

    # Remove double spaces
    dataframe[name_column] = dataframe[name_column].str.replace(
        r'\s{2}', ' ', regex=True)

    return dataframe[name_column]
