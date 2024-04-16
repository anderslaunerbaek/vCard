from pathlib import Path


def make_vcard(
    full_name: str,
    first_name: str,
    last_name: str,
    company: str,
    title: str,
    phone: int | str,
    address: str,
    email: str,
) -> list[str]:
    return [
        "BEGIN:VCARD",
        "VERSION:2.1",
        f"N:{last_name};{first_name}",
        f"FN:{full_name}",
        f"ORG:{company}",
        # f"TITLE:{title}",
        # f"EMAIL;PREF;INTERNET:{email}",
        f"TEL;HOME;VOICE:{phone}",
        f"ADR;HOME;PREF:;;{address}",
        # f"ADR;HOME;PREF:;;{address_formatted}",
        "REV:1",
        "END:VCARD",
    ]


def write_vcard(filename: Path, vcard: list[str]):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(vcard))
        # f.writelines([l + "\n" for l in vcard])
