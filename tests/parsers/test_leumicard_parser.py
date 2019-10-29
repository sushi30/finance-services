from parsers.leumicard_parser import LeumiCardParser


def test_parse_leumicard():
    with open("../data/leumicard_test_data.xlsx", "rb") as excel_file:
        lcp = LeumiCardParser(excel_file).parse()
    print(lcp.dumps())



