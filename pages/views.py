from django.shortcuts import render
import os
from django.conf import settings


def home(request):
    # -------------------------
    # Menu Sections
    # -------------------------
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
                    "link": "#",
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
        # Add more sections...
    ]

    # -------------------------
    # Operating Hours
    # -------------------------
    hours = [
        ("Sunday", "11:00 AM – 10:00 PM"),
        ("Monday", "12:00 NN – 10:00 PM"),
        ("Tuesday", "12:00 NN – 10:00 PM"),
        ("Wednesday", "12:00 NN – 10:00 PM"),
        ("Thursday", "12:00 NN – 10:00 PM"),
        ("Friday", "11:00 AM – 11:00 PM"),
        ("Saturday", "11:00 AM – 11:00 PM"),
    ]

    # -------------------------
    # Carousel Images (auto-load from static/images)
    # -------------------------
    image_dir = os.path.join(settings.STATICFILES_DIRS[0], "images")
    carousel_images = [
        "images/" + f for f in os.listdir(image_dir) 
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp"))
    ]

    # -------------------------
    # Render everything to template
    # -------------------------
    return render(
        request,
        "index.html",
        {
            "menu_sections": menu_sections,
            "hours": hours,
            "carousel_images": carousel_images,
        },
    )
