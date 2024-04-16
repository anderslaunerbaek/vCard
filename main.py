from pathlib import Path

import pandas as pd
from src.vcard import make_vcard, write_vcard

DIRECTORY = Path(__file__).resolve().parent


def load_data(filename: Path) -> pd.DataFrame:
    df = pd.read_csv(filename, sep=";").drop(["Hjemmenr.", "Arbejdstelefon"], axis=1)
    df.Adresse = df.Adresse.apply(
        lambda x: x.replace(
            ", 5762 Vester Skerninge", ";Vester Skerninge;;5762;Danmark"
        )
    )
    df.Adresse = df.Adresse.apply(
        lambda x: x.replace(", 5700 Svendborg", ";Svendborg;;5700;Danmark")
    )
    df.Adresse = df.Adresse.apply(
        lambda x: x.replace(", 5771 Stenstrup", ";Stenstrup;;5771;Danmark")
    )
    return df


def main():
    df = load_data(DIRECTORY / "data.csv")
    output_dir = DIRECTORY / "vCards"
    for i, x in df.iterrows():
        vcard = make_vcard(
            x["Kontaktperson"],
            x["Kontaktperson"].split(" ")[0],
            x["Kontaktperson"].split(" ")[-1],
            x["Elever"],
            "",
            x["Mobiltelefon"],
            x["Adresse"],
            "",
        )
        write_vcard(f"{output_dir}/{i}.vcf", vcard)


if __name__ == "__main__":
    main()
