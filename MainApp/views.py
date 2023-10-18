from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

countries = [
    {
        "country": "Aruba",
        "languages": [
            "Dutch",
            "English",
            "Papiamento",
            "Spanish"
        ]
    },
    {
        "country": "Afghanistan",
        "languages": [
            "Balochi",
            "Dari",
            "Pashto",
            "Turkmenian",
            "Uzbek"
        ]
    },
    {
        "country": "Angola",
        "languages": [
            "Ambo",
            "Chokwe",
            "Kongo",
            "Luchazi",
            "Luimbe-nganguela",
            "Luvale",
            "Mbundu",
            "Nyaneka-nkhumbi",
            "Ovimbundu"
        ]
    },
    {
        "country": "Anguilla",
        "languages": [
            "English"
        ]
    },
    {
        "country": "Albania",
        "languages": [
            "Albaniana",
            "Greek",
            "Macedonian"
        ]
    },
    {
        "country": "Andorra",
        "languages": [
            "Catalan",
            "French",
            "Portuguese",
            "Spanish"
        ]
    },
{
        "country": "Netherlands Antilles",
        "languages": [
            "Dutch",
            "English",
            "Papiamento"
        ]
    },
    {
        "country": "United Arab Emirates",
        "languages": [
            "Arabic",
            "Hindi"
        ]
    },
    {
        "country": "Argentina",
        "languages": [
            "Indian Languages",
            "Italian",
            "Spanish"
        ]
    },
    {
        "country": "Armenia",
        "languages": [
            "Armenian",
            "Azerbaijani"
        ]
    },
    {
        "country": "American Samoa",
        "languages": [
            "English",
            "Samoan",
            "Tongan"
        ]
    },
    {
        "country": "Antigua and Barbuda",
        "languages": [
            "Creole English",
            "English"
        ]
    },
    {
        "country": "Australia",
        "languages": [
            "Arabic",
            "Canton Chinese",
            "English",
            "German",
            "Greek",
            "Italian",
            "Serbo-Croatian",
            "Vietnamese"
        ]
    },
    {
        "country": "Austria",
        "languages": [
            "Czech",
            "German",
            "Hungarian",
            "Polish",
            "Romanian",
            "Serbo-Croatian",
            "Slovene",
            "Turkish"
        ]
    },
    {
        "country": "Azerbaijan",
        "languages": [
            "Armenian",
            "Azerbaijani",
            "Lezgian",
            "Russian"
        ]
    },
    {
        "country": "Burundi",
        "languages": [
            "French",
            "Kirundi",
            "Swahili"
        ]
    },
    {
        "country": "Belgium",
        "languages": [
            "Arabic",
            "Dutch",
            "French",
            "German",
            "Italian",
            "Turkish"
        ]
    },
    {
        "country": "Benin",
        "languages": [
            "Adja",
            "Aizo",
            "Bariba",
            "Fon",
            "Ful",
            "Joruba",
            "Somba"
        ]
    },
    {
        "country": "Burkina Faso",
        "languages": [
            "Busansi",
            "Dagara",
            "Dyula",
            "Ful",
            "Gurma",
            "Mossi"
        ]
    },
    {
        "country": "Bangladesh",
        "languages": [
            "Bengali",
            "Chakma",
            "Garo",
            "Khasi",
            "Marma",
            "Santhali",
            "Tripuri"
        ]
    },
    {
        "country": "Bulgaria",
        "languages": [
            "Bulgariana",
            "Macedonian",
            "Romani",
            "Turkish"
        ]
    },
    {
        "country": "Bahrain",
        "languages": [
            "Arabic",
            "English"
        ]
    },
    {
        "country": "Bahamas",
        "languages": [
            "Creole English",
            "Creole French"
        ]
    },
    {
        "country": "Bosnia and Herzegovina",
        "languages": [
            "Bosnian"
        ]
    },
    {
        "country": "Belarus",
        "languages": [
            "Belorussian",
            "Polish",
            "Russian",
            "Ukrainian"
        ]
    },
    {
        "country": "Belize",
        "languages": [
            "English",
            "Garifuna",
            "Maya Languages",
            "Spanish"
        ]
    },
    {
        "country": "Bermuda",
        "languages": [
            "English"
        ]
    },
    {
        "country": "Bolivia",
        "languages": [
            "Aimar√°",
            "Guaran√≠",
            "Ket¬öua",
            "Spanish"
        ]
    },
    {
        "country": "Brazil",
        "languages": [
            "German",
            "Indian Languages",
            "Italian",
            "Japanese",
            "Portuguese"
        ]
    },
    {
        "country": "Barbados",
        "languages": [
            "Bajan",
            "English"
        ]
    },
    {
        "country": "Brunei",
        "languages": [
            "Chinese",
            "English",
            "Malay",
            "Malay-English"
        ]
    },
    {
        "country": "Bhutan",
        "languages": [
            "Asami",
            "Dzongkha",
            "Nepali"
        ]
    },
    {
        "country": "Botswana",
        "languages": [
            "Khoekhoe",
            "Ndebele",
            "San",
            "Shona",
            "Tswana"
        ]
    },
]

def home(request):
    text = """<h1>"Приветствую"</h1>
              <strong>Автор</strong>: <i>Лебедкин Андрей</i> <br>
              new line
           """
    return HttpResponse(text)


def countries_list(request):
    for i, country in enumerate(countries):

        result = f"""
        <p>{i+1["i+1"]}, {country["country"]}</p>
        """
    return HttpResponse(result)
