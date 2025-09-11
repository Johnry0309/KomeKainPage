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
                    "desc": "A Hawaiian favorite — seasoned rice layered with fluffy egg, drizzled with our signature sauce, topped with savory Spam, and wrapped in crisp nori with a sprinkle of sesame seeds.",
                    "price": "₱50",
                    "photo": "img/Classic_Musubi.png",
                    "link": "#",
                },
                {
                    "name": "Golden Musubi",
                    "desc": "A crispy twist on the classic — golden pan-seared Spam on rice with egg, sesame seeds, and our rich house sauce, all wrapped in roasted seaweed.",
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
                    "desc": "A Filipino-inspired onigiri filled with savory shredded chicken pastil, wrapped in nori, and paired with seasoned rice for a hearty bite.",
                    "price": "₱25",
                    "photo": "img/Pastil_onigiri.png",
                    "link": "#",
                },
                {
                    "name": "Tuna Onigiri",
                    "desc": "Classic Japanese rice ball stuffed with a creamy tuna filling, wrapped in nori for the perfect light snack.",
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
