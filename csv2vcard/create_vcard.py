def create_vcard(contact: dict):
    """
    The mappings used below are from https://www.w3.org/TR/vcard-rdf/#Mapping
    """
    vc_begin = "BEGIN:VCARD\n"
    vc_version = "VERSION:3.0\n"
    vc_name = f"N;CHARSET=UTF-8:{contact['Familienname']};{contact['Rufname']};;;\n"
    #vc_title = f"TITLE;CHARSET=UTF-8:{contact['title']}\n"
    #vc_org = f"ORG;CHARSET=UTF-8:{contact['org']}\n"
    vc_phone = f"TEL;TYPE=WORK,VOICE:{contact['Telefonnummer']}\n"
    vc_mobile = f"TEL;TYPE=WORK,CELL:{contact['Handynummer']}\n"
    vc_email = f"EMAIL;TYPE=WORK:{contact['E-Mail']}\n"
    #vc_website = f"URL;TYPE=WORK:{contact['website']}\n"
    #vc_address = f"ADR;TYPE=WORK;CHARSET=UTF-8:{contact['street']};{contact['city']};{contact['p_code']};{contact['country']}\n"
    vc_bday = f"BDAY:{contact['Skript 6']}\n"
    vc_end = "END:VCARD\n"

    vc_filename = f"{contact['Familienname'].lower()}_{contact['Rufname'].lower()}.vcf"
    #vc_output = vc_begin + vc_version + vc_name + vc_title + vc_org + vc_phone + vc_email + vc_website + vc_address + vc_bday + vc_end
    vc_output = vc_begin + vc_version + vc_name + vc_phone + vc_mobile + vc_email + vc_bday + vc_end

    vc_final = {
        "filename" : vc_filename,
        "output" : vc_output,
        "name" : contact['Rufname'] + contact['Familienname'],
    }

    return vc_final
