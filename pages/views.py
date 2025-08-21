from django.shortcuts import render

def home(request):
    menu_sections = [
        {
            "anchor": "signatures",
            "title": "Signatures",
            "items": [
                {"name": "Kimchi Sinigang", "desc": "Tamarind-kimchi broth, grilled pork belly, kangkong, siling haba."},
                {"name": "Gochu Adobo", "desc": "Chicken adobo with gochujang glaze, garlic chips, soft egg."},
                {"name": "Bibim-Pancit", "desc": "Stir-fried miki bihon with bibimbap veggies, sesame, calamansi."},
                {"name": "Samgyup Sisig", "desc": "Crispy pork sisig with ssamjang, nori, and pickled onions."},
            ],
        },
        {
            "anchor": "rawbar",
            "title": "Raw Bar",
            "items": [
                {"name": "Tuna Kilawin Yukhoe", "desc": "Calamansi-soy cure, sesame, pear, egg yolk."},
                {"name": "Salmon Kinilaw Gimbap Bites", "desc": "Nori rice squares, coconut-vinegar cured salmon, chili."},
            ],
        },
        {
            "anchor": "ricebowls",
            "title": "Rice Bowls",
            "items": [
                {"name": "Longga Kimbap Bowl", "desc": "Garlic rice, seared longganisa, rolled egg, nori, achara."},
                {"name": "Beef Tapsilog Bulgogi", "desc": "Sweet soy bulgogi, fried egg, atchara, scallion."},
            ],
        },
        {
            "anchor": "grill",
            "title": "Robata & Grill",
            "items": [
                {"name": "Inasal Dak Galbi", "desc": "Lemongrass chicken, chili paste, coconut glaze."},
                {"name": "Liempo Galbi", "desc": "Charred pork belly, kalbi marinade, sesame-calamansi dip."},
            ],
        },
        {
            "anchor": "drinks",
            "title": "Drinks",
            "items": [
                {"name": "Calamansi-Yuja Ade", "desc": "Sparkling yuja with calamansi"},
                {"name": "Barako-Milk Iced Latte", "desc": "Batangas barako + Korean milk foam"},
            ],
        },
    ]
    hours = [
        ("Sunday", "11:00 AM – 10:00 PM"),
        ("Monday", "12:00 NN – 10:00 PM"),
        ("Tuesday", "12:00 NN – 10:00 PM"),
        ("Wednesday", "12:00 NN – 10:00 PM"),
        ("Thursday", "12:00 NN – 10:00 PM"),
        ("Friday", "11:00 AM – 11:00 PM"),
        ("Saturday", "11:00 AM – 11:00 PM"),
    ]
    return render(request, "index.html", {"menu_sections": menu_sections, "hours": hours})
