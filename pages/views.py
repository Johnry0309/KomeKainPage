from django.shortcuts import render

def home(request):
    menu_sections = [
        {
            "anchor": "signatures",
            "title": "Signatures",
            "items": [
                {
                    "name": "Kimchi Sinigang",
                    "desc": "Tamarind-kimchi broth, grilled pork belly, kangkong, siling haba.",
                    "price": "₱320",
                    "photo": "img/kimchi-sinigang.jpg",
                    "link": "#",  # later link to order/details
                },
                {
                    "name": "Gochu Adobo",
                    "desc": "Chicken adobo with gochujang glaze, garlic chips, soft egg.",
                    "price": "₱280",
                    "photo": "img/gochu-adobo.jpg",
                    "link": "#",
                },
                {
                    "name": "Bibim-Pancit",
                    "desc": "Stir-fried miki bihon with bibimbap veggies, sesame, calamansi.",
                    "price": "₱250",
                    "photo": "img/bibim-pancit.jpg",
                    "link": "#",
                },
                {
                    "name": "Samgyup Sisig",
                    "desc": "Crispy pork sisig with ssamjang, nori, and pickled onions.",
                    "price": "₱300",
                    "photo": "img/samgyup-sisig.jpg",
                    "link": "#",
                },
            ],
        },
        # repeat for rawbar, ricebowls, grill, drinks...
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

    return render(
        request,
        "index.html",
        {"menu_sections": menu_sections, "hours": hours}
    )
