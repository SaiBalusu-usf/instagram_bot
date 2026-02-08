import random

class SmartHashtags:
    def __init__(self):
        self.categories = {
            "portrait": [
                "#portraitphotography", "#portraitmood", "#portraitpage", "#portraitglam",
                "#portrait_vision", "#portrait_perfection", "#moodyports", "#makeportraits",
                "#faceobsessed", "#portraitstream", "#portrait_shots", "#pursuitofportraits"
            ],
            "landscape": [
                "#landscapephotography", "#landscapelovers", "#landscapehunter", "#landscape_captures",
                "#naturephotography", "#naturelovers", "#earthpix", "#visualsofearth",
                "#agameoftones", "#artofvisuals", "#roamtheplanet", "#beautifuldestinations"
            ],
            "street": [
                "#streetphotography", "#streetclassics", "#streetleaks", "#streetlife",
                "#urbanphotography", "#citykillerz", "#urbanromantix", "#streetshared",
                "#streetmobs", "#streetframe", "#capturestreets", "#life_is_street"
            ],
            "bnw": [
                "#bnwphotography", "#bnw_captures", "#bnw_planet", "#bnw_society",
                "#monochrome", "#blackandwhitephotography", "#bnw_life", "#bnw_greatshots",
                "#bnw_rose", "#bnw_demand", "#noir", "#fineart_photobw"
            ],
            "general": [
                "#photography", "#photooftheday", "#picoftheday", "#photographer",
                "#photo", "#instagood", "#love", "#art", "#beautiful"
            ]
        }

    def get_hashtags(self, category="general", count=15):
        """
        Returns a string of random hashtags from the specified category.
        Mixes in a few general tags for reach.
        """
        category = category.lower()
        if category not in self.categories:
            print(f"Category '{category}' not found. Using 'general'.")
            category = "general"

        specific_tags = self.categories[category]
        general_tags = self.categories["general"]

        # Mix: 70% specific, 30% general
        num_specific = int(count * 0.7)
        num_general = count - num_specific

        selected_specific = random.sample(specific_tags, min(num_specific, len(specific_tags)))
        selected_general = random.sample(general_tags, min(num_general, len(general_tags)))

        return " ".join(selected_specific + selected_general)

    def list_categories(self):
        return list(self.categories.keys())
