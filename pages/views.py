from django.shortcuts import render
import os
from django.conf import settings


def home(request):
    # -------------------------
    # Menu Sections
    # -------------------------
    menu_sections = [
        {
            "anchor": "Musubi",
            "title": "Musubi",
            "items": [
                {
                    "name": "Classic Spam Musubi",
                    "desc": "a true classic musubi, seasoned rice layered with our teriyaki sauce, fluffy eggs, kewpie mayo topped with the savory spam cooked to crisp with the teriyaki sauce wrapped in nori seaweed with a sprinkle of sesame seeds.",
                    "price": "₱50",
                    "photo": "img/Classic_Musubi.png",
                    "link": "#",
                },
                {
                    "name": "Golden Musubi",
                    "desc": "a golden twist to our classic, our classic spam musubi topped with the creamy and cheesy golden sauce. .",
                    "price": "₱50",
                    "photo": "img/Golden_Musubi.png",
                    "link": "#",
                },
            ],
        },

        {
            "anchor": "Onigiri",
            "title": "Onigiri",
            "items": [
                {
                    "name": "Pastil Onigiri",
                    "desc": "traditional Onigiri with the savory shredded chicken pastil, and creamy kewpie mayo wrapped in nori and topped with sesame seeds. ",
                    "price": "₱25",
                    "photo": "img/Pastil_onigiri.png",
                    "link": "#",
                },
                {
                    "name": "Tuna Onigiri",
                    "desc": "the classic Onigiri filled with tuna and kewpie goodness, wrapped in nori seaweed and sesame seeds. ",
                    "price": "₱25",
                    "photo": "img/Tuna_onigiri.png",
                    "link": "#",
                },
            ],
        },
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
