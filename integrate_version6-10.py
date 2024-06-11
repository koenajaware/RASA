# %%
import re

# %% [markdown]
# Catering Packages

# %%
class DesiDeluxeOrder:
    def __init__(self):
        self.quantity = 0 
        self.bases = []
        self.protein_or_vegetables = []
        self.sauces = []
        self.veggies = []
        self.toppings = []
        self.chutneys = []

def extract_desi_deluxe_details(text):
    desi_deluxe_pattern = r"(\d+) The Desi Deluxe @ \$[\d.]+ View more details Bases: ([\w\s]+) Bases: ([\w\s]+)? Bases: ([\w\s]+)? Bases: ([\w\s]+)? Protein Or Vegetables: ([\w\s]+) Protein Or Vegetables: ([\w\s]+) Protein Or Vegetables: ([\w\s]+) Protein Or Vegetables: ([\w\s]+) Sauces: ([\w\s]+) Sauces: ([\w\s]+) Sauces: ([\w\s]+) Sauces: ([\w\s]+) Veggies: ([\w\s]+) Veggies: ([\w\s]+) Veggies: ([\w\s]+) Veggies: ([\w\s]+) Toppings: ([\w\s]+) Toppings: ([\w\s]+) Toppings: ([\w\s]+) Toppings: ([\w\s]+) Chutneys: ([\w\s]+) Chutneys: ([\w\s]+) Chutneys: ([\w\s]+) Chutneys: ([\w\s]+) \$[\d,]+"
    desi_deluxe_occurrences = re.findall(desi_deluxe_pattern, text)
    
    extracted_orders = []
    for occurrence in desi_deluxe_occurrences:
        order = DesiDeluxeOrder()
        order.quantity = int(occurrence[0])
        order.bases = [base.strip() for base in occurrence[1:5] if base.strip()]
        order.protein_or_vegetables = [pov.strip() for pov in occurrence[5:9] if pov.strip()]
        order.sauces = [sauce.strip() for sauce in occurrence[9:13] if sauce.strip()]
        order.veggies = [veggie.strip() for veggie in occurrence[13:17] if veggie.strip()]
        order.toppings = [topping.strip() for topping in occurrence[17:21] if topping.strip()]
        order.chutneys = [chutney.strip() for chutney in occurrence[21:25] if chutney.strip()]
        
        extracted_orders.append(order)

    return extracted_orders

# %%
class TheClassicOrder:
    def __init__(self):
        self.quantity = 0 
        self.bases = []
        self.protein_or_vegetables = []
        self.sauces = []
        self.veggies = []
        self.toppings = []
        self.chutneys = []

def extract_the_classic_details(text):
    classic_pattern = r"(\d+) The Classic @ \$[\d.]+ View more details Bases: ([\w\s]+) Bases: ([\w\s]+)? Bases: ([\w\s]+)? Protein Or Vegetables: ([\w\s]+) Protein Or Vegetables: ([\w\s]+) Protein Or Vegetables: ([\w\s]+) Sauces: ([\w\s]+) Sauces: ([\w\s]+) Sauces: ([\w\s]+) Veggies: ([\w\s]+) Veggies: ([\w\s]+) Veggies: ([\w\s]+) Toppings: ([\w\s]+) Toppings: ([\w\s]+) Toppings: ([\w\s]+) Chutneys: ([\w\s]+) Chutneys: ([\w\s]+) Chutneys: ([\w\s]+) \$[\d,]+"
    classic_occurrences = re.findall(classic_pattern, text)
    
    extracted_orders = []
    for occurrence in classic_occurrences:
        order = TheClassicOrder()
        order.quantity = int(occurrence[0])
        order.bases = [base.strip() for base in occurrence[1:4] if base.strip()]
        order.protein_or_vegetables = [pov.strip() for pov in occurrence[4:7] if pov.strip()]
        order.sauces = [sauce.strip() for sauce in occurrence[7:10] if sauce.strip()]
        order.veggies = [veggie.strip() for veggie in occurrence[10:13] if veggie.strip()]
        order.toppings = [topping.strip() for topping in occurrence[13:16] if topping.strip()]
        order.chutneys = [chutney.strip() for chutney in occurrence[16:19] if chutney.strip()]
        
        extracted_orders.append(order)

    return extracted_orders

# %%
class PartyPackOrder:
    def __init__(self):
        self.quantity = 0 
        self.bases = []
        self.protein_or_vegetables = []
        self.sauces = []
        self.veggies = []
        self.toppings = []
        self.chutneys = []

def extract_party_pack_details(text):
    party_pack_pattern = r"(\d+) The Party Pack @ \$[\d.]+ View more details Bases: ([\w\s]+) Bases: ([\w\s]+)? Protein Or Vegetables: ([\w\s]+) Protein Or Vegetables: ([\w\s]+) Sauces: ([\w\s]+) Sauces: ([\w\s]+) Veggies: ([\w\s]+) Veggies: ([\w\s]+) Toppings: ([\w\s]+) Toppings: ([\w\s]+) Chutneys: ([\w\s]+) Chutneys: ([\w\s]+) \$[\d,]+"
    party_pack_occurrences = re.findall(party_pack_pattern, text)
    
    extracted_orders = []
    for occurrence in party_pack_occurrences:
        order = PartyPackOrder()
        order.quantity = int(occurrence[0])
        order.bases = [base.strip() for base in occurrence[1:3] if base.strip()]
        order.protein_or_vegetables = [pov.strip() for pov in occurrence[3:5] if pov.strip()]
        order.sauces = [sauce.strip() for sauce in occurrence[5:7] if sauce.strip()]
        order.veggies = [veggie.strip() for veggie in occurrence[7:9] if veggie.strip()]
        order.toppings = [topping.strip() for topping in occurrence[9:11] if topping.strip()]
        order.chutneys = [chutney.strip() for chutney in occurrence[11:13] if chutney.strip()]
        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Individually Packaged Bowls

# %%
class TikkaChanceOnMeBowlOrder:
    def __init__(self):
        self.quantity = 0

def extract_tikka_chance_on_me_bowl_details(text):
    tikka_chance_on_me_bowl_pattern = r"(\d+) Tikka Chance On Me Bowl @"
    tikka_chance_on_me_bowl_occurrences = re.findall(tikka_chance_on_me_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in tikka_chance_on_me_bowl_occurrences:
        order = TikkaChanceOnMeBowlOrder()
        order.quantity = int(occurrence[0])        
        extracted_orders.append(order)

    return extracted_orders

# %%
class AlooNeedIsLoveBowlOrder:
    def __init__(self):
        self.quantity = 0

def extract_aloo_need_is_love_bowl_details(text):
    aloo_need_is_love_bowl_pattern = r"(\d+) Aloo Need Is Love Bowl @"
    aloo_need_is_love_bowl_occurrences = re.findall(aloo_need_is_love_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in aloo_need_is_love_bowl_occurrences:
        order = AlooNeedIsLoveBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class OpenSesameBowlOrder:
    def __init__(self):
        self.quantity = 0

def extract_open_sesame_bowl_details(text):
    open_sesame_bowl_pattern = r"(\d+) Open Sesame Bowl @"
    open_sesame_bowl_occurrences = re.findall(open_sesame_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in open_sesame_bowl_occurrences:
        order = OpenSesameBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class HomeCookingBowlOrder:
    def __init__(self):
        self.quantity = 0

def extract_home_cooking_bowl_details(text):
    home_cooking_bowl_pattern = r"(\d+) Home Cooking Bowl @"
    home_cooking_bowl_occurrences = re.findall(home_cooking_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in home_cooking_bowl_occurrences:
        order = HomeCookingBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class HarvestChickenBowlOrder:
    def __init__(self):
        self.quantity = 0

def extract_harvest_chicken_bowl_details(text):
    harvest_chicken_bowl_pattern = r"(\d+) Harvest Chicken Bowl @"
    harvest_chicken_bowl_occurrences = re.findall(harvest_chicken_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in harvest_chicken_bowl_occurrences:
        order = HarvestChickenBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class VibesAndVeggieBowlOrder:
    def __init__(self):
        self.quantity = 0

def extract_vibes_and_veggie_bowl_details(text):
    vibes_and_veggie_bowl_pattern = r"(\d+) Vibes & Veggies Bowl @"
    vibes_and_veggie_bowl_occurrences = re.findall(vibes_and_veggie_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in vibes_and_veggie_bowl_occurrences:
        order = VibesAndVeggieBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class ChickenTikkaAndAvocadoSaladBowlOrder:
    def __init__(self):
        self.quantity = 0
        
def extract_chicken_tikka_and_avocado_salad_bowl_details(text):
    chicken_tikka_and_avocado_salad_bowl_pattern = r"(\d+) Chicken Tikka & Avocado Salad Bowl @"
    chicken_tikka_and_avocado_salad_bowl_occurrences = re.findall(chicken_tikka_and_avocado_salad_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in chicken_tikka_and_avocado_salad_bowl_occurrences:
        order = ChickenTikkaAndAvocadoSaladBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class SpicyChiliChickenBowlOrder:
    def __init__(self):
        self.quantity = 0
        
def extract_spicy_chili_chicken_bowl_details(text):
    spicy_chili_chicken_bowl_pattern = r"(\d+) Spicy Chili Chicken Bowl @"
    spicy_chili_chicken_bowl_occurrences = re.findall(spicy_chili_chicken_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in spicy_chili_chicken_bowl_occurrences:
        order = SpicyChiliChickenBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class TandooriPaneerBowlOrder:
    def __init__(self):
        self.quantity = 0

def extract_tandoori_paneer_bowl_details(text):
    tandoori_paneer_bowl_pattern = r"(\d+) Tandoori Paneer Bowl @"
    tandoori_paneer_bowl_occurrences = re.findall(tandoori_paneer_bowl_pattern, text)
    
    extracted_orders = []
    for occurrence in tandoori_paneer_bowl_occurrences:
        order = TandooriPaneerBowlOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Sides

# %%
class NaanBasketOrder:
    def __init__(self):
        self.quantity = 0
        self.size = ""
        self.type = ""

def extract_naan_basket_details(text):
    naan_basket_pattern = r"(\d+) Naan Basket @ \$[\d.]+ Size: (\w+) View more details Please ServeAdd: (Garlic Naan|Naan|Combo of Naan)"
    naan_basket_occurrences = re.findall(naan_basket_pattern, text)
    
    extracted_orders = []
    for occurrence in naan_basket_occurrences:
        order = NaanBasketOrder()
        order.quantity = int(occurrence[0])
        order.size = occurrence[1]
        order.type = occurrence[2]
        
        extracted_orders.append(order)

    return extracted_orders

# %%
class SamosaTrayOrder:
    def __init__(self):
        self.quantity = 0
        self.size = 10

def extract_samosa_tray_details(text):
    samosa_tray_pattern = r"(\d+) Samosa Tray @ \$[\d.]+(?: Size: (\w+))?"
    samosa_tray_occurrences = re.findall(samosa_tray_pattern, text)
    
    extracted_orders = []
    for occurrence in samosa_tray_occurrences:
        order = SamosaTrayOrder()
        order.quantity = int(occurrence[0])
        order.size = int(occurrence[1]) if occurrence[1] else 10
        
        extracted_orders.append(order)

    return extracted_orders

# %%
class CucumberRaitaOrder:
    def __init__(self):
        self.quantity = 0
        
def extract_cucumber_raita_details(text):
    cucumber_raita_pattern = r"(\d+) Cucumber Raita @"
    cucumber_raita_occurrences = re.findall(cucumber_raita_pattern, text)
    
    extracted_orders = []
    for occurrence in cucumber_raita_occurrences:
        order = CucumberRaitaOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class LentilChipsOrder:
    def __init__(self):
        self.quantity = 0
        
def extract_lentil_chips_order(text):
    lentil_chips_pattern = r"(\d+) Lentil Chips @"
    lentil_chips_occurrences = re.findall(lentil_chips_pattern, text)
    
    extracted_orders = []
    for occurrence in lentil_chips_occurrences:
        order = LentilChipsOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Desserts

# %%
class ChaiChocolateChipCookieBasketOrder:
    def __init__(self):
        self.quantity = 0
        self.size = 10

def extract_chai__chocolate_chip_cookie_basket_details(text):
    chai__chocolate_chip_cookie_basket_pattern = r"(\d+) Chai Chocolate Chip Cookie Basket @ \$[\d.]+(?: Size: (\w+))?"
    chai__chocolate_chip_cookie_basket_occurrences = re.findall(chai__chocolate_chip_cookie_basket_pattern, text)
    
    extracted_orders = []
    for occurrence in chai__chocolate_chip_cookie_basket_occurrences:
        order = ChaiChocolateChipCookieBasketOrder()
        order.quantity = int(occurrence[0])
        order.size = int(occurrence[1]) if occurrence[1] else 10
        
        extracted_orders.append(order)

    return extracted_orders

# %%
class IndianYogurtOrder:
    def __init__(self):
        self.quantity = 0
        
def extract_indian_yogurt_details(text):
    indian_yogurt_pattern = r"(\d+) Indian Yogurt @"
    indian_yogurt_occurrences = re.findall(indian_yogurt_pattern, text)
    
    extracted_orders = []
    for occurrence in indian_yogurt_occurrences:
        order = IndianYogurtOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Additional Bases

# %%
class BasmatiRiceOrder:
    def __init__(self):
        self.quantity = 0
        
def extract_basmati_rice_details(text):
    basmati_rice_pattern = r"(\d+) Basmati Rice @"
    basmati_rice_occurrences = re.findall(basmati_rice_pattern, text)
    
    extracted_orders = []
    for occurrence in basmati_rice_occurrences:
        order = BasmatiRiceOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class LemonTurmericRiceOrder:
    def __init__(self):
        self.quantity = 0
    
def extract_lemon_turmeric_rice_details(text):
    lemon_turmeric_rice_pattern = r"(\d+) Lemon Turmeric Rice @"
    lemon_turmeric_rice_occurrences = re.findall(lemon_turmeric_rice_pattern, text)
    
    extracted_orders = []
    for occurrence in lemon_turmeric_rice_occurrences:
        order = LemonTurmericRiceOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class SouthIndianRiceNoodlesOrder:
    def __init__(self):
        self.quantity = 0
    
def extract_south_indian_rice_noodles_details(text):
    south_indian_rice_noodles_pattern = r"(\d+) South Indian Rice Noodles @"
    south_indian_rice_noodles_occurrences = re.findall(south_indian_rice_noodles_pattern, text)
    
    extracted_orders = []
    for occurrence in south_indian_rice_noodles_occurrences:
        order = SouthIndianRiceNoodlesOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class SupergrainsOrder:
    def __init__(self):
        self.quantity = 0
    
def extract_supergrains_details(text):
    supergrains_pattern = r"(\d+) Supergrains @"
    supergrains_occurrences = re.findall(supergrains_pattern, text)
    
    extracted_orders = []
    for occurrence in supergrains_occurrences:
        order = SupergrainsOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Additional Mains

# %%
class ChickenTikkaOrder:
    def __init__(self):
        self.quantity = 0
    
def extract_chicken_tikka_details(text):
    chicken_tikka_pattern = r"(\d+) Chicken Tikka @"
    chicken_tikka_occurrences = re.findall(chicken_tikka_pattern, text)
    
    extracted_orders = []
    for occurrence in chicken_tikka_occurrences:
        order = ChickenTikkaOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class HarvestVegetablesOrder:
    def __init__(self):
        self.quantity = 0
    
def extract_harvest_vegtables_details(text):
    harvest_vegetables_pattern = r"(\d+) Harvest Vegetables @"
    harvest_vegetables_occurrences = re.findall(harvest_vegetables_pattern, text)
    
    extracted_orders = []
    for occurrence in harvest_vegetables_occurrences:
        order = HarvestVegetablesOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class SweetPotatoTikkiOrder:
    def __init__(self):
        self.quantity = 0

def extract_sweet_potato_tikki_details(text):
    sweet_potato_tikki_pattern = r"(\d+) Sweet Potato Tikki @"
    sweet_potato_tikki_occurrences = re.findall(sweet_potato_tikki_pattern, text)
    
    extracted_orders = []
    for occurrence in sweet_potato_tikki_occurrences:
        order = SweetPotatoTikkiOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class LambKebabOrder:
    def __init__(self):
        self.quantity = 0

def extract_lamb_kebab_details(text):
    lamb_kebab_pattern = r"(\d+) Lamb Kebab Meatballs @"
    lamb_kebab_occurrences = re.findall(lamb_kebab_pattern, text)
    
    extracted_orders = []
    for occurrence in lamb_kebab_occurrences:
        order = LambKebabOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class TurmericGingerShrimpOrder:
    def __init__(self):
        self.quantity = 0

def extract_turmeric_ginger_shrimp_details(text):
    turmeric_ginger_shrimp_pattern = r"(\d+) Turmeric Ginger Shrimp @"
    turmeric_ginger_shrimp_occurrences = re.findall(turmeric_ginger_shrimp_pattern, text)
    
    extracted_orders = []
    for occurrence in turmeric_ginger_shrimp_occurrences:
        order = TurmericGingerShrimpOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class TandooriPaneerOrder:
    def __init__(self):
        self.quantity = 0

def extract_tandoori_paneer_details(text):
    tandoori_paneer_pattern = r"(\d+) Tandoori Paneer @"
    tandoori_paneer_occurrences = re.findall(tandoori_paneer_pattern, text)
    
    extracted_orders = []
    for occurrence in tandoori_paneer_occurrences:
        order = TandooriPaneerOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class SpicyChilliChickenOrder:
    def __init__(self):
        self.quantity = 0

def extract_spicy_chilli_chicken_details(text):
    spicy_chili_chicken_pattern = r"(\d+) Spicy Chili Chicken @"
    spicy_chili_chicken_occurrences = re.findall(spicy_chili_chicken_pattern, text)
    
    extracted_orders = []
    for occurrence in spicy_chili_chicken_occurrences:
        order = SpicyChilliChickenOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Additional Sauces

# %%
class TomatoGarlicSauceOrder:
    def __init__(self):
        self.quantity = 0

def extract_tomato_garlic_sauce_details(text):
    tomato_garlic_sauce_pattern = r"(\d+) Tomato Garlic Sauce @"
    tomato_garlic_sauce_occurrences = re.findall(tomato_garlic_sauce_pattern, text)
    
    extracted_orders = []
    for occurrence in tomato_garlic_sauce_occurrences:
        order = TomatoGarlicSauceOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class TamarindChiliSauceOrder:
    def __init__(self):
        self.quantity = 0

def extract_tamarind_chili_sauce_details(text):
    tamarind_chili_sauce_pattern = r"(\d+) Tamarind Chili Sauce @"
    tamarind_chili_sauce_occurrences = re.findall(tamarind_chili_sauce_pattern, text)
    
    extracted_orders = []
    for occurrence in tamarind_chili_sauce_occurrences:
        order = TamarindChiliSauceOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class CoconutGingerSauceOrder:
    def __init__(self):
        self.quantity = 0

def extract_coconut_ginger_sauce_details(text):
    coconut_ginger_sauce_pattern = r"(\d+) Coconut Ginger Sauce @"
    coconut_ginger_sauce_occurrences = re.findall(coconut_ginger_sauce_pattern, text)
    
    extracted_orders = []
    for occurrence in coconut_ginger_sauce_occurrences:
        order = CoconutGingerSauceOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class PeanutSesameSauceOrder:
    def __init__(self):
        self.quantity = 0

def extract_peanut_sesame_sauce_details(text):
    peanut_sesame_sauce_pattern = r"(\d+) Peanut Sesame Sauce @"
    peanut_sesame_sauce_occurrences = re.findall(peanut_sesame_sauce_pattern, text)
    
    extracted_orders = []
    for occurrence in peanut_sesame_sauce_occurrences:
        order = PeanutSesameSauceOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Additional Veggies

# %%
class SpicedChickpeasOrder:
    def __init__(self):
        self.quantity = 0

def extract_spiced_chickpeas_details(text):
    spiced_chickpeas_pattern = r"(\d+) Spiced Chickpeas @"
    spiced_chickpeas_occurrences = re.findall(spiced_chickpeas_pattern, text)
    
    extracted_orders = []
    for occurrence in spiced_chickpeas_occurrences:
        order = SpicedChickpeasOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class TossedGreenBeansOrder:
    def __init__(self):
        self.quantity = 0

def extract_tossed_green_beans_details(text):
    tossed_green_beans_pattern = r"(\d+) Tossed Green Beans @"
    tossed_green_beans_occurrences = re.findall(tossed_green_beans_pattern, text)
    
    extracted_orders = []
    for occurrence in tossed_green_beans_occurrences:
        order = TossedGreenBeansOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class SauteedSpinachOrder:
    def __init__(self):
        self.quantity = 0

def extract_sauteed_spinach_details(text):
    sauteed_spinach_pattern = r"(\d+) Sautéed Spinach @"
    sauteed_spinachs_occurrences = re.findall(sauteed_spinach_pattern, text)
    
    extracted_orders = []
    for occurrence in sauteed_spinachs_occurrences:
        order = SauteedSpinachOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class CharredEggplantOrder:
    def __init__(self):
        self.quantity = 0

def extract_charred_eggplant_details(text):
    charred_eggplant_pattern = r"(\d+) Charred Eggplant @"
    charred_eggplant_occurrences = re.findall(charred_eggplant_pattern, text)
    
    extracted_orders = []
    for occurrence in charred_eggplant_occurrences:
        order = CharredEggplantOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Beverages

# %%
class LaCroixSparklingWaterOrder:
    def __init__(self):
        self.quantity = 0
        self.flavor = "Most Popular"

def extract_la_croix_sparkling_water_details(text):
    la_croix_sparkling_water_pattern = r"(\d+) LaCroix Sparkling Water @ \$[\d.]+(?: View more details Flavor: (Lime|Grapefruit|Most Popular))?"
    la_croix_sparkling_water_occurrences = re.findall(la_croix_sparkling_water_pattern, text)
    
    extracted_orders = []
    for occurrence in la_croix_sparkling_water_occurrences:
        order = LaCroixSparklingWaterOrder()
        order.quantity = int(occurrence[0])
        order.flavor = occurrence[1] if occurrence[1] else "Most Popular"
        
        extracted_orders.append(order)

    return extracted_orders

# %%
class RAINWaterOrder:
    def __init__(self):
        self.quantity = 0

def extract_RAIN_Water_details(text):
    rain_water_pattern = r"(\d+) RAIN Water @"
    rain_water_occurrences = re.findall(rain_water_pattern, text)
    
    extracted_orders = []
    for occurrence in rain_water_occurrences:
        order = RAINWaterOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class MangoLassiOrder:
    def __init__(self):
        self.quantity = 0

def extract_mango_lassi_details(text):
    mango_lassi_pattern = r"(\d+) Mango Lassi @"
    mango_lassi_occurrences = re.findall(mango_lassi_pattern, text)
    
    extracted_orders = []
    for occurrence in mango_lassi_occurrences:
        order = MangoLassiOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %%
class WildKombuchaOrder:
    def __init__(self):
        self.quantity = 0
        self.flavor = "Most Popular"

def extract_wild_kombucha_details(text):
    wild_kombucha_pattern = r"(\d+) Wild Kombucha @ \$[\d.]+(?: View more details Flavor: (Ginger|Mango Peach|Most Popular))?"
    wild_kombucha_occurrences = re.findall(wild_kombucha_pattern, text)
    
    extracted_orders = []
    for occurrence in wild_kombucha_occurrences:
        order = WildKombuchaOrder()
        order.quantity = int(occurrence[0])
        order.flavor = occurrence[1] if occurrence[1] else "Most Popular"
        
        extracted_orders.append(order)

    return extracted_orders

# %%
class MintYerbaMateOrder:
    def __init__(self):
        self.quantity = 0

def extract_mint_yerba_mate_detail(text):
    mint_yerba_mate_pattern = r"(\d+) Icaro Spearmint Yerba Mate @"
    mint_yerba_mate_occurrences = re.findall(mint_yerba_mate_pattern, text)
    
    extracted_orders = []
    for occurrence in mint_yerba_mate_occurrences:
        order = MintYerbaMateOrder()
        order.quantity = int(occurrence)        
        extracted_orders.append(order)

    return extracted_orders

# %% [markdown]
# Utensils

# %%
class Utensils:
    def __init(self):
        self.quantity = 0 

def extract_utensils_detail(text):
    utensils_pattern = r"(\d+) Utensils @"
    utensils_occurences = re.findall(utensils_pattern, text)

    extracted_orders = []
    for occurence in utensils_occurences:
        order = Utensils()
        order.quantity = int(occurence)
        extracted_orders.append(order)
    
    return extracted_orders

# %%
def calculate_and_print(category, item_name, original, amount, uom="oz-wt", container="", utensil=""):
        # only do this if the item is in the order 
        if amount != 0:
            # create data set for it
            data = [[category, item_name, round(original, 2) ,"recipe"
                     , round(amount, 2), uom, round(amount/16, 2), "lbs", container, utensil]]

            # open file for this order and all orders 
            #f = open(order, "a")
            # f2 = open("total_order.txt", "a")

            def print_table(data):
                for row in data:
                    # print all data to output, write it to this order file and write to all order file 
                    print("{:<10} {:<35} {:<10} {:<10} {:<10} {:<6} {:<10} {:<6} {:<10} {:<10}".format(*row))
                    #f.write("{:<10} {:<25} {:<10} {:<6} {:<10} {:<6} {:<10} {:<10}\n".format(*row))
                    # f2.write("{:<10} {:<25} {:<10} {:<6} {:<10} {:<6} {:<10} {:<10}\n".format(*row))

            # print our table and close files 
            print_table(data)
            #print()
            #f.close()
            # f2.close()

# %% [markdown]
# Parsing

# %%
while True:
    order = ""
    input_text = input("Enter your order (press Enter to finish): ")
    if not input_text:
        break
    order += input_text
    
    lamb_kebab_re = r"Protein Or Vegetables: (\d+) x Lamb Kebab Meatballs @ \$2\.64"
    simplified_lamb_kebab_re = "Protein Or Vegetables: Lamb Kebab"

    spicy_chili_chicken_re = r"Protein Or Vegetables: (\d+) x Spicy Chili Chicken @ \$1\.50"
    simplified_spicy_chili_chicken_re = "Protein Or Vegetables: Spicy Chili Chicken"

    tandoori_paneer_re = r"Protein Or Vegetables: (\d+) x Tandoori Paneer @ \$1\.20"
    simplified_tandoori_paneer_re = "Protein Or Vegetables: Tandoori Paneer"

    shrimp_re = r"Protein Or Vegetables: (\d+) x Shrimp @ \$3\.24"
    simplified_shrimp_re = "Protein Or Vegetables: Turmeric Garlic Shrimp"

    turmeric_garlic_shrimp_re = r"Protein Or Vegetables: (\d+) x Turmeric Garlic Shrimp @ \$3\.24"
    simplified_turmeric_garlic_shrimp_re = "Protein Or Vegetables: Turmeric Garlic Shrimp"

    sauteed_spinach_re = r"Veggies: Sautéed Spinach"
    simplified_sauteed_spinach_re = "Veggies: Sautéed Spinach"

    avocado_re = r"Toppings: (\d+) x Avocado @ \$2\.50"
    simplified_avocado_re = "Toppings: Avocado"

    garlic_naan_re = r"Please ServeAdd: (\d+) x Garlic Naan @ \$2\.00"
    simplified_garlic_naan_re = "Please ServeAdd: Garlic Naan"

    combo_naan_re = r"Please ServeAdd: (\d+) x Combo of Naan @ \$2\.00"
    simplified_combo_naan_re = "Please ServeAdd: Combo of Naan"

    #special_instructions_re = r"Special Instructions: .* $"
    #simplified_special_instructions_re = ""

    special_instructions_re = r"Special Instructions:.*?\$"

    if re.search(lamb_kebab_re, order):
        order = re.sub(lamb_kebab_re, simplified_lamb_kebab_re, order)
    if re.search(spicy_chili_chicken_re, order):
        order = re.sub(spicy_chili_chicken_re, simplified_spicy_chili_chicken_re, order)
    if re.search(tandoori_paneer_re, order):
        order = re.sub(tandoori_paneer_re, simplified_tandoori_paneer_re, order)
    if re.search(turmeric_garlic_shrimp_re, order):
        order = re.sub(turmeric_garlic_shrimp_re, simplified_turmeric_garlic_shrimp_re, order)
    if re.search(shrimp_re, order):
        order = re.sub(shrimp_re, simplified_shrimp_re, order)
    if re.search(sauteed_spinach_re, order):
        order = re.sub(sauteed_spinach_re, simplified_sauteed_spinach_re, order)
    if re.search(avocado_re, order):
        order = re.sub(avocado_re, simplified_avocado_re, order)
    if re.search(garlic_naan_re, order):
        order = re.sub(garlic_naan_re, simplified_garlic_naan_re, order)
    if re.search(combo_naan_re, order):
        order = re.sub(combo_naan_re, simplified_combo_naan_re, order)
    #if re.search(special_instructions_re, orders):
        #orders = re.sub(special_instructions_re, simplified_special_instructions_re, orders)
    if re.search(special_instructions_re, order):
        order = re.sub(special_instructions_re, "$", order)
        
    with open("orders.txt", "w") as file:
        file.write(order)


    totalBasmatiRice = 0 
    totalLemonTurmericRice = 0 
    totalSupergrains = 0
    totalSouthIndianRiceNoodles = 0 
    totalSpinach = 0 
    totalSexyGreens = 0 
    totalRomaine = 0 
    totalArugula = 0 

    totalChickenTikka = 0 
    totalLambKebab = 0 
    totalTurmericGingerShrimp = 0 
    totalSpicyChiliChicken = 0 
    totalSweetPotatoTikki = 0 
    totalHarvestVegetables = 0 
    totalTandooriPaneer = 0

    totalTomato_garlic = 0
    totalPeanute_sesame = 0
    totalTamarind_chili = 0
    totalCoconut_ginger = 0

    totalCharred_egglant = 0
    totalSpiced_chickpeas = 0
    totalTossed_green_beans = 0
    totalSauteed_spinach = 0

    totalCucumber_cubes = 0
    totalMasala_beets = 0
    totalPickled_onions = 0
    totalPickled_radishes = 0
    totalMango_salsa = 0
    totalCilantro = 0
    totalKachumber_salad = 0
    totalCarrot_slaw = 0
    totalIndian_street_corn = 0
    totalPumpkin_seeds = 0
    totalRoasted_lentils = 0
    totalTamarind_coconut_powder = 0
    totalAvocado = 0

    totalMint_cilantro_chutney = 0
    totalToasted_cumin_yogurt = 0
    totalMango_coconut_yogurt = 0
    totalTamarind_ginger_chutney = 0
    totalCoriander_chili = 0
    totalHouse_vinaigrette = 0
    totalKokum_vinaigrette = 0

    totalTomato = 0
    totalCranberry = 0  
    totalChickpeaNoodle = 0

    totalLentilChips = 0


    #The Desi Deluxe

    desideluxe_details = extract_desi_deluxe_details(order)
    for item in desideluxe_details:

        basmati_rice = 0
        lemon_turmeric_rice = 0
        supergrains = 0
        south_indian_rice_noodles = 0
        spinach = 0
        sexygreens = 0
        romaine = 0
        arugula = 0

        chicken_tikka = 0
        lamb_kebab = 0
        turmeric_ginger_shrimp = 0
        spicy_chili_chicken = 0
        sweet_potato_tikki = 0
        harvest_vegetables = 0
        tandoori_paneer = 0

        tomato_garlic = 0
        peanute_sesame = 0
        tamarind_chili = 0
        coconut_ginger = 0

        charred_egglant = 0
        spiced_chickpeas = 0
        tossed_green_beans = 0
        sauteed_spinach = 0

        cucumber_cubes = 0
        masala_beets = 0
        pickled_onions = 0
        pickled_radishes = 0
        mango_salsa = 0
        cilantro = 0
        kachumber_salad = 0
        carrot_slaw = 0
        indian_street_corn = 0
        pumpkin_seeds = 0
        roasted_lentils = 0
        tamarind_coconut_powder = 0
        avocado = 0

        mint_cilantro_chutney = 0
        toasted_cumin_yogurt = 0
        mango_coconut_yogurt = 0
        tamarind_ginger_chutney = 0
        coriander_chili = 0
        house_vinaigrette = 0
        kokum_vinaigrette = 0

        tomato = 0
        cranberry = 0 

        print("The Desi Deluxe")
        print("Quantity:", item.quantity)
        print("Bases:", item.bases)
        print("Protein Or Vegetables:", item.protein_or_vegetables)
        print("Sauces:", item.sauces)
        print("Veggies:", item.veggies)
        print("Toppings:", item.toppings)
        print("Chutneys:", item.chutneys)
        print()

        quantity = item.quantity

        bases = item.bases
        for base in bases:
            if "Basmati Rice" in base:
                basmati_rice += quantity
            if "Lemon Turmeric Rice" in base:
                lemon_turmeric_rice += quantity
            if "Supergrains" in base:
                supergrains += quantity
            if "South Indian Rice Noodles" in base:
                south_indian_rice_noodles += quantity
            if "Spinach" in base:
                spinach += quantity
            if "Sexygreens" in base:
                sexygreens += quantity
            if "Romaine" in base:
                romaine += quantity
            if "Arugula" in base:
                arugula += quantity

        protein_veggies = item.protein_or_vegetables
        for protein in protein_veggies:
            if "Chicken Tikka" in protein:
                chicken_tikka += quantity
            if "Lamb Kebab" in protein:
                lamb_kebab += quantity
            if "Turmeric Ginger Shrimp" in protein:
                turmeric_ginger_shrimp += quantity
            if "Spicy Chili Chicken" in protein:
                spicy_chili_chicken += quantity
            if "Sweet Potato Tikki" in protein:
                sweet_potato_tikki += quantity
            if "Harvest Vegetables" in protein:
                harvest_vegetables += quantity
            if "Tandoori Paneer" in protein:
                tandoori_paneer += quantity
        
        sauces = item.sauces
        for sauce in sauces:
            if "Coconut Ginger" in sauce:
                coconut_ginger += quantity
            if "Peanut Sesame" in sauce:
                peanute_sesame += quantity
            if "Tamarind Chili" in sauce:
                tamarind_chili += quantity
            if "Tomato Garlic" in sauce:
                tomato_garlic += quantity

        veggies = item.veggies
        for veg in veggies:
            if "Sautéed Spinach" in veg:
                sauteed_spinach += quantity
            if "Tossed Green Beans" in veg:
                tossed_green_beans += quantity
            if "Spiced Chickpeas" in veg:
                spiced_chickpeas += quantity
            if "Charred Eggplant" in veg:
                charred_egglant += quantity

        toppings = item.toppings
        for topping in toppings:
            if "Cucumber Cubes" in topping:
                cucumber_cubes += quantity
            if "Masala Beets" in topping:
                masala_beets += quantity
            if "Pickled Onions" in topping:
                pickled_onions += quantity
            if "Pickled Radishes" in topping:
                pickled_radishes += quantity
            if "Mango Salsa" in topping:
                mango_salsa += quantity
            if "Cilantro" in topping:
                cilantro += quantity
            if "Kachumber Salad" in topping:
                kachumber_salad += quantity
            if "Carrot Slaw" in topping:
                carrot_slaw += quantity
            if "Indian Street Corn" in topping:
                indian_street_corn += quantity
            if "Pumpkin Seeds" in topping:
                pumpkin_seeds += quantity
            if "Roasted Lentils" in topping:
                roasted_lentils += quantity
            if "Tamarind Coconut Powder" in topping:
                tamarind_coconut_powder += quantity
            if "Avocado" in topping:
                avocado += quantity

        chutneys = item.chutneys
        for chutney in chutneys:
            if "Mint Cilantro Chutney" in chutney:
                mint_cilantro_chutney += quantity
            if "Toasted Cumin Yogurt" in chutney:
                toasted_cumin_yogurt += quantity
            if "Mango Coconut Yogurt" in chutney:
                mango_coconut_yogurt += quantity
            if "Tamarind Ginger Chutney" in chutney:
                tamarind_ginger_chutney += quantity
            if "Coriander Chili" in chutney:
                coriander_chili += quantity
            if "House Vinaigrette" in chutney:
                house_vinaigrette += quantity
            if "Kokum Vinaigrette" in chutney:
                kokum_vinaigrette += quantity
        print("")
        data = [["Category", "Menu Item", "Raw", "UOM", "Amount", "UOM", "Amount", "UOM", "Container", "Utensil"],]
        
        for row in data:
            print("{:<10} {:<35} {:<10} {:<10} {:<10} {:<6} {:<10} {:<6} {:<10} {:<10}".format(*row))
        
        basmati_rice *= 3.4
        totalBasmatiRice += basmati_rice

        lemon_turmeric_rice *= 3.4
        totalLemonTurmericRice += lemon_turmeric_rice

        supergrains *= 3.4
        totalSupergrains += supergrains

        south_indian_rice_noodles *= 3.4
        totalSouthIndianRiceNoodles += south_indian_rice_noodles

        spinach *= 0.8
        totalSpinach += spinach

        sexygreens *= 0.8
        totalSexyGreens += sexygreens
    
        romaine *= 0.8
        totalRomaine += romaine

        arugula *= 0.8
        totalArugula += arugula

        chicken_tikka *= 2.29
        totalChickenTikka += chicken_tikka

        lamb_kebab *= 1.67
        totalLambKebab += lamb_kebab

        turmeric_ginger_shrimp *= 2.5
        totalTurmericGingerShrimp += turmeric_ginger_shrimp

        spicy_chili_chicken *= 2.29
        totalSpicyChiliChicken += spicy_chili_chicken

        sweet_potato_tikki *= 1.67
        totalSweetPotatoTikki += sweet_potato_tikki

        harvest_vegetables *= 2.08
        totalHarvestVegetables += harvest_vegetables

        tandoori_paneer *= 2.5
        totalTandooriPaneer += tandoori_paneer

        tomato_garlic *= 1
        totalTomato_garlic += tomato_garlic

        tamarind_chili *= 1
        totalTamarind_chili += tamarind_chili

        peanute_sesame *= 1
        totalPeanute_sesame += peanute_sesame

        coconut_ginger *= 1
        totalCoconut_ginger += coconut_ginger

        sauteed_spinach *= 1
        totalSauteed_spinach += sauteed_spinach

        charred_egglant *= 1
        totalCharred_egglant += charred_egglant

        spiced_chickpeas *= 1
        totalSpiced_chickpeas += spiced_chickpeas

        tossed_green_beans *= 0.6
        totalTossed_green_beans += tossed_green_beans

        cucumber_cubes *= 0.56
        totalCucumber_cubes += cucumber_cubes

        kachumber_salad *= 0.56
        totalKachumber_salad += kachumber_salad

        mango_salsa *= 0.56
        totalMango_salsa += mango_salsa

        pickled_radishes *= 0.2
        totalPickled_radishes += pickled_radishes

        pickled_onions *= 0.6
        totalPickled_onions += pickled_onions

        masala_beets *= 0.4
        totalMasala_beets += masala_beets

        indian_street_corn *= 0.56
        totalIndian_street_corn += indian_street_corn

        carrot_slaw *= 0.6
        totalCarrot_slaw += carrot_slaw

        cilantro *= 0.04
        totalCilantro += cilantro

        avocado *= 1
        totalAvocado += avocado

        pumpkin_seeds *= 0.2
        totalPumpkin_seeds += pumpkin_seeds

        roasted_lentils *= 0.08
        totalRoasted_lentils += roasted_lentils

        tamarind_coconut_powder *= 0.2
        totalTamarind_coconut_powder += tamarind_coconut_powder

        mint_cilantro_chutney *= 0.48
        totalMint_cilantro_chutney += mint_cilantro_chutney

        toasted_cumin_yogurt *= 0.48
        totalToasted_cumin_yogurt += toasted_cumin_yogurt

        mango_coconut_yogurt *= 0.48
        totalMango_coconut_yogurt += mango_coconut_yogurt

        tamarind_ginger_chutney *= 0.48
        totalTamarind_ginger_chutney += tamarind_ginger_chutney

        coriander_chili *= 0.48
        totalCoriander_chili += coriander_chili

        house_vinaigrette *= 0.48
        totalHouse_vinaigrette += house_vinaigrette

        kokum_vinaigrette *= 0.48
        totalKokum_vinaigrette += kokum_vinaigrette

        tomato *= 0.48
        totalTomato += tomato

        cranberry *= 0.48
        totalCranberry += cranberry

        # call print method on all items 
        # Base category
        calculate_and_print("Base", "Basmati Rice", round(basmati_rice/(20*16), 2), basmati_rice, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "Lemon Turmeric Rice", round(lemon_turmeric_rice/(20*16), 2), lemon_turmeric_rice, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "Supergrains", 0, supergrains, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "South Indian Rice Noodles", 0, south_indian_rice_noodles, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Spinach", 0, spinach, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Sexygreens", 0, sexygreens, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Romaine", 0, romaine, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Arugula", 0, arugula, "oz-wt", "N/A", "Tongs")

        # Main category
        calculate_and_print("Main", "Chicken Tikka", round(chicken_tikka/(0.65*16), 2), chicken_tikka, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Lamb Kebab", 0, lamb_kebab, "each", "N/A", "Tongs")
        calculate_and_print("Main", "Turmeric Ginger Shrimp", 0, turmeric_ginger_shrimp, "each", "N/A", "C Spoon")
        calculate_and_print("Main", "Spicy Chili Chicken", round(spicy_chili_chicken/(3.97*16), 2), spicy_chili_chicken, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Sweet Potato Tikki", 0, sweet_potato_tikki, "each", "N/A", "Tongs")
        calculate_and_print("Main", "Harvest Vegetables", round(harvest_vegetables/(2.12*16), 2), harvest_vegetables, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Tandoori Paneer", 0, tandoori_paneer, "each", "N/A", "Tongs")

        # Sauce category
        calculate_and_print("Sauce", "Tomato Garlic", round(tomato_garlic/152.38, 2), tomato_garlic, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Peanute Sesame", round(peanute_sesame/152.38, 2), peanute_sesame, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Tamarind Chili", round(tamarind_chili/152.38, 2), tamarind_chili, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Coconut Ginger", round(coconut_ginger/152.38, 2), coconut_ginger, "oz-fl", "N/A", "Ladle")

        # Vegetable category
        calculate_and_print("Vegetable", "Charred Eggplant", round(charred_egglant/(1.63125*16), 2), charred_egglant, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Vegetable", "Spiced Chickpeas", round(spiced_chickpeas/(3.94*16), 2), spiced_chickpeas, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Vegetable", "Tossed Green Beans", round(tossed_green_beans/(2.15625*16), 2), tossed_green_beans, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Vegetable", "Sautéed Spinach", round(sauteed_spinach/(5.5875*16), 2), sauteed_spinach, "oz-wt", "N/A", "C Spoon")

        # Topping category
        calculate_and_print("Topping", "Cucumber Cubes", 0, cucumber_cubes, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Masala Beets", 0, masala_beets, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Pickled Onions", 0, pickled_onions, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Pickled Radishes", 0, pickled_radishes, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Mango Salsa", 0, mango_salsa, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Cilantro", 0, cilantro, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Kachumber Salad", 0, kachumber_salad, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Carrot Slaw", 0, carrot_slaw, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Indian Street Corn", 0, indian_street_corn, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Pumpkin Seeds", 0, pumpkin_seeds, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Roasted Lentils", 0, roasted_lentils, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Tamarind Coconut Powder", 0, tamarind_coconut_powder, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Avocado", 0, avocado, "each", "N/A", "Tongs")

        # Chutney category
        calculate_and_print("Chutney", "Mint Cilantro Chutney", 0, mint_cilantro_chutney, "oz-fl")
        calculate_and_print("Chutney", "Toasted Cumin Yogurt", 0, toasted_cumin_yogurt, "oz-fl")
        calculate_and_print("Chutney", "Mango Coconut Yogurt", 0, mango_coconut_yogurt, "oz-fl")
        calculate_and_print("Chutney", "Tamarind Ginger Chutney", 0, tamarind_ginger_chutney, "oz-fl", "N/A", "Teaspoon")
        calculate_and_print("Chutney", "Coriander Chili", 0, coriander_chili, "oz-fl", "N/A", "Teaspoon")
        calculate_and_print("Chutney", "House Vinaigrette", 0, house_vinaigrette, "oz-fl")
        calculate_and_print("Chutney", "Kokum Vinaigrette", 0, kokum_vinaigrette, "oz-fl")

        
    #The Classic 
            

    classic_details = extract_the_classic_details(order)

    for item in classic_details:

        basmati_rice = 0
        lemon_turmeric_rice = 0
        supergrains = 0
        south_indian_rice_noodles = 0
        spinach = 0
        sexygreens = 0
        romaine = 0
        arugula = 0

        chicken_tikka = 0
        lamb_kebab = 0
        turmeric_ginger_shrimp = 0
        spicy_chili_chicken = 0
        sweet_potato_tikki = 0
        harvest_vegetables = 0
        tandoori_paneer = 0

        tomato_garlic = 0
        peanute_sesame = 0
        tamarind_chili = 0
        coconut_ginger = 0

        charred_egglant = 0
        spiced_chickpeas = 0
        tossed_green_beans = 0
        sauteed_spinach = 0

        cucumber_cubes = 0
        masala_beets = 0
        pickled_onions = 0
        pickled_radishes = 0
        mango_salsa = 0
        cilantro = 0
        kachumber_salad = 0
        carrot_slaw = 0
        indian_street_corn = 0
        pumpkin_seeds = 0
        roasted_lentils = 0
        tamarind_coconut_powder = 0
        avocado = 0

        mint_cilantro_chutney = 0
        toasted_cumin_yogurt = 0
        mango_coconut_yogurt = 0
        tamarind_ginger_chutney = 0
        coriander_chili = 0
        house_vinaigrette = 0
        kokum_vinaigrette = 0
        tomato = 0
        cranberry = 0

        print("The Classic")
        print("Quantity:", item.quantity)
        print("Bases:", item.bases)
        print("Protein Or Vegetables:", item.protein_or_vegetables)
        print("Sauces:", item.sauces)
        print("Veggies:", item.veggies)
        print("Toppings:", item.toppings)
        print("Chutneys:", item.chutneys)
        
        quantity = item.quantity

        bases = item.bases
        for base in bases:
            if "Basmati Rice" in base:
                basmati_rice += quantity
            if "Lemon Turmeric Rice" in base:
                lemon_turmeric_rice += quantity
            if "Supergrains" in base:
                supergrains += quantity
            if "South Indian Rice Noodles" in base:
                south_indian_rice_noodles += quantity
            if "Spinach" in base:
                spinach += quantity
            if "Sexygreens" in base:
                sexygreens += quantity
            if "Romaine" in base:
                romaine += quantity
            if "Arugula" in base:
                arugula += quantity
            if "Most Popular" in base:
                romaine += quantity
                lemon_turmeric_rice += quantity
                south_indian_rice_noodles += quantity

        protein_veggies = item.protein_or_vegetables
        for protein in protein_veggies:
            if "Chicken Tikka" in protein:
                chicken_tikka += quantity
            if "Lamb Kebab" in protein:
                lamb_kebab += quantity
            if "Turmeric Ginger Shrimp" in protein:
                turmeric_ginger_shrimp += quantity
            if "Spicy Chili Chicken" in protein:
                spicy_chili_chicken += quantity
            if "Sweet Potato Tikki" in protein:
                sweet_potato_tikki += quantity
            if "Harvest Vegetables" in protein:
                harvest_vegetables += quantity
            if "Tandoori Paneer" in protein:
                tandoori_paneer += quantity
            if "Most Popular" in protein:
                chicken_tikka += quantity
                sweet_potato_tikki += quantity
                harvest_vegetables += quantity
        
        sauces = item.sauces
        for sauce in sauces:
            if "Coconut Ginger" in sauce:
                coconut_ginger += quantity
            if "Peanut Sesame" in sauce:
                peanute_sesame += quantity
            if "Tamarind Chili" in sauce:
                tamarind_chili += quantity
            if "Tomato Garlic" in sauce:
                tomato_garlic += quantity
            if "Most Popular" in sauce:
                tomato_garlic += quantity
                tamarind_chili += quantity
                coconut_ginger += quantity

        veggies = item.veggies
        for veg in veggies:
            if "Sautéed Spinach" in veg:
                sauteed_spinach += quantity
            if "Tossed Green Beans" in veg:
                tossed_green_beans += quantity
            if "Spiced Chickpeas" in veg:
                spiced_chickpeas += quantity
            if "Charred Eggplant" in veg:
                charred_egglant += quantity
            if "Most Popular" in veg:
                sauteed_spinach += quantity
                tossed_green_beans += quantity
                spiced_chickpeas += quantity

        toppings = item.toppings
        for topping in toppings:
            if "Cucumber Cubes" in topping:
                cucumber_cubes += quantity
            if "Masala Beets" in topping:
                masala_beets += quantity
            if "Pickled Onions" in topping:
                pickled_onions += quantity
            if "Pickled Radishes" in topping:
                pickled_radishes += quantity
            if "Mango Salsa" in topping:
                mango_salsa += quantity
            if "Cilantro" in topping:
                cilantro += quantity
            if "Kachumber Salad" in topping:
                kachumber_salad += quantity
            if "Carrot Slaw" in topping:
                carrot_slaw += quantity
            if "Indian Street Corn" in topping:
                indian_street_corn += quantity
            if "Pumpkin Seeds" in topping:
                pumpkin_seeds += quantity
            if "Roasted Lentils" in topping:
                roasted_lentils += quantity
            if "Tamarind Coconut Powder" in topping:
                tamarind_coconut_powder += quantity
            if "Avocado" in topping:
                avocado += quantity
            if "Most Popular" in topping:
                cucumber_cubes += quantity
                pickled_onions += quantity
                indian_street_corn += quantity


        chutneys = item.chutneys
        for chutney in chutneys:
            if "Mint Cilantro Chutney" in chutney:
                mint_cilantro_chutney += quantity
            if "Toasted Cumin Yogurt" in chutney:
                toasted_cumin_yogurt += quantity
            if "Mango Coconut Yogurt" in chutney:
                mango_coconut_yogurt += quantity
            if "Tamarind Ginger Chutney" in chutney:
                tamarind_ginger_chutney += quantity
            if "Coriander Chili" in chutney:
                coriander_chili += quantity
            if "House Vinaigrette" in chutney:
                house_vinaigrette += quantity
            if "Kokum Vinaigrette" in chutney:
                kokum_vinaigrette += quantity
            if "Most Popular" in chutney:
                tamarind_ginger_chutney += quantity
                mint_cilantro_chutney += quantity
                toasted_cumin_yogurt += quantity
             
        print("")
        data = [["Category", "Menu Item", "Raw", "UOM", "Amount", "UOM", "Amount", "UOM", "Container", "Utensil"],]
        
        for row in data:
            print("{:<10} {:<35} {:<10} {:<10} {:<10} {:<6} {:<10} {:<6} {:<10} {:<10}".format(*row))
        
        basmati_rice *= 3.64
        totalBasmatiRice += basmati_rice

        lemon_turmeric_rice *= 3.64
        totalLemonTurmericRice += lemon_turmeric_rice

        supergrains *= 3.64
        totalSupergrains += supergrains

        south_indian_rice_noodles *= 3.64
        totalSouthIndianRiceNoodles += south_indian_rice_noodles

        spinach *= 0.86
        totalSpinach += spinach

        sexygreens *= 0.86
        totalSexyGreens += sexygreens

        romaine *= 0.86
        totalRomaine += romaine

        arugula *= 0.86
        totalArugula += arugula

        chicken_tikka *= 2.41
        totalChickenTikka += chicken_tikka

        lamb_kebab *= 1.75
        totalLambKebab += lamb_kebab

        turmeric_ginger_shrimp *= 2.63
        totalTurmericGingerShrimp += turmeric_ginger_shrimp

        spicy_chili_chicken *= 2.41
        totalSpicyChiliChicken += spicy_chili_chicken

        sweet_potato_tikki *= 1.75
        totalSweetPotatoTikki += sweet_potato_tikki

        harvest_vegetables *= 2.19
        totalHarvestVegetables += harvest_vegetables

        tandoori_paneer *= 2.63
        totalTandooriPaneer += tandoori_paneer

        tomato_garlic *= 1
        totalTomato_garlic += tomato_garlic

        tamarind_chili *= 1
        totalTamarind_chili += tamarind_chili

        peanute_sesame *= 1
        totalPeanute_sesame += peanute_sesame

        coconut_ginger *= 1
        totalCoconut_ginger += coconut_ginger

        sauteed_spinach *= 1
        totalSauteed_spinach += sauteed_spinach

        charred_egglant *= 1
        totalCharred_egglant += charred_egglant

        spiced_chickpeas *= 1
        totalSpiced_chickpeas += spiced_chickpeas

        tossed_green_beans *= 0.6
        totalTossed_green_beans += tossed_green_beans

        cucumber_cubes *= 0.56
        totalCucumber_cubes += cucumber_cubes

        kachumber_salad *= 0.56
        totalKachumber_salad += kachumber_salad

        mango_salsa *= 0.56
        totalMango_salsa += mango_salsa

        pickled_radishes *= 0.2
        totalPickled_radishes += pickled_radishes

        pickled_onions *= 0.6
        totalPickled_onions += pickled_onions

        masala_beets *= 0.4
        totalMasala_beets += masala_beets

        indian_street_corn *= 0.56
        totalIndian_street_corn += indian_street_corn

        carrot_slaw *= 0.6
        totalCarrot_slaw += carrot_slaw

        cilantro *= 0.04
        totalCilantro += cilantro

        avocado *= 1
        totalAvocado += avocado

        pumpkin_seeds *= 0.2
        totalPumpkin_seeds += pumpkin_seeds

        roasted_lentils *= 0.08
        totalRoasted_lentils += roasted_lentils

        tamarind_coconut_powder *= 0.2
        totalTamarind_coconut_powder += tamarind_coconut_powder

        mint_cilantro_chutney *= 0.48
        totalMint_cilantro_chutney += mint_cilantro_chutney

        toasted_cumin_yogurt *= 0.48
        totalToasted_cumin_yogurt += toasted_cumin_yogurt

        mango_coconut_yogurt *= 0.48
        totalMango_coconut_yogurt += mango_coconut_yogurt

        tamarind_ginger_chutney *= 0.48
        totalTamarind_ginger_chutney += tamarind_ginger_chutney

        coriander_chili *= 0.48
        totalCoriander_chili += coriander_chili

        house_vinaigrette *= 0.48
        totalHouse_vinaigrette += house_vinaigrette

        kokum_vinaigrette *= 0.48
        totalKokum_vinaigrette += kokum_vinaigrette

        tomato *= 0.48
        totalTomato += tomato

        cranberry *= 0.48
        totalCranberry += cranberry

        # call print method on all items 
        # Base category
        calculate_and_print("Base", "Basmati Rice", basmati_rice, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "Lemon Turmeric Rice", lemon_turmeric_rice, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "Supergrains", supergrains, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "South Indian Rice Noodles", south_indian_rice_noodles, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Spinach", spinach, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Sexygreens", sexygreens, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Romaine", romaine, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Arugula", arugula, "oz-wt", "N/A", "Tongs")

        # Main category
        calculate_and_print("Main", "Chicken Tikka", chicken_tikka, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Lamb Kebab", lamb_kebab, "each", "N/A", "Tongs")
        calculate_and_print("Main", "Turmeric Ginger Shrimp", turmeric_ginger_shrimp, "each", "N/A", "C Spoon")
        calculate_and_print("Main", "Spicy Chili Chicken", spicy_chili_chicken, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Sweet Potato Tikki", sweet_potato_tikki, "each", "N/A", "Tongs")
        calculate_and_print("Main", "Harvest Vegetables", harvest_vegetables, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Tandoori Paneer", tandoori_paneer, "each", "N/A", "Tongs")

        # Sauce category
        calculate_and_print("Sauce", "Tomato Garlic", tomato_garlic, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Peanute Sesame", peanute_sesame, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Tamarind Chili", tamarind_chili, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Coconut Ginger", coconut_ginger, "oz-fl", "N/A", "Ladle")

        # Vegetable category
        calculate_and_print("Vegetable", "Charred Eggplant", charred_egglant, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Vegetable", "Spiced Chickpeas", spiced_chickpeas, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Vegetable", "Tossed Green Beans", tossed_green_beans, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Vegetable", "Sautéed Spinach", sauteed_spinach, "oz-wt", "N/A", "C Spoon")

        # Topping category
        calculate_and_print("Topping", "Cucumber Cubes", cucumber_cubes, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Masala Beets", masala_beets, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Pickled Onions", pickled_onions, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Pickled Radishes", pickled_radishes, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Mango Salsa", mango_salsa, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Cilantro", cilantro, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Kachumber Salad", kachumber_salad, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Carrot Slaw", carrot_slaw, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Indian Street Corn", indian_street_corn, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Pumpkin Seeds", pumpkin_seeds, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Roasted Lentils", roasted_lentils, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Tamarind Coconut Powder", tamarind_coconut_powder, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Avocado", avocado, "each", "N/A", "Tongs")

        # Chutney category
        calculate_and_print("Chutney", "Mint Cilantro Chutney", mint_cilantro_chutney, "oz-fl")
        calculate_and_print("Chutney", "Toasted Cumin Yogurt", toasted_cumin_yogurt, "oz-fl")
        calculate_and_print("Chutney", "Mango Coconut Yogurt", mango_coconut_yogurt, "oz-fl")
        calculate_and_print("Chutney", "Tamarind Ginger Chutney", tamarind_ginger_chutney, "oz-fl", "N/A", "Teaspoon")
        calculate_and_print("Chutney", "Coriander Chili", coriander_chili, "oz-fl", "N/A", "Teaspoon")
        calculate_and_print("Chutney", "House Vinaigrette", house_vinaigrette, "oz-fl")
        calculate_and_print("Chutney", "Kokum Vinaigrette", kokum_vinaigrette, "oz-fl")
    
        print()
    
    
    #The Party Pack

    partypack_details = extract_party_pack_details(order)
    for item in partypack_details:

        basmati_rice = 0
        lemon_turmeric_rice = 0
        supergrains = 0
        south_indian_rice_noodles = 0
        spinach = 0
        sexygreens = 0
        romaine = 0
        arugula = 0

        chicken_tikka = 0
        lamb_kebab = 0
        turmeric_ginger_shrimp = 0
        spicy_chili_chicken = 0
        sweet_potato_tikki = 0
        harvest_vegetables = 0
        tandoori_paneer = 0

        tomato_garlic = 0
        peanute_sesame = 0
        tamarind_chili = 0
        coconut_ginger = 0

        charred_egglant = 0
        spiced_chickpeas = 0
        tossed_green_beans = 0
        sauteed_spinach = 0

        cucumber_cubes = 0
        masala_beets = 0
        pickled_onions = 0
        pickled_radishes = 0
        mango_salsa = 0
        cilantro = 0
        kachumber_salad = 0
        carrot_slaw = 0
        indian_street_corn = 0
        pumpkin_seeds = 0
        roasted_lentils = 0
        tamarind_coconut_powder = 0
        avocado = 0

        mint_cilantro_chutney = 0
        toasted_cumin_yogurt = 0
        mango_coconut_yogurt = 0
        tamarind_ginger_chutney = 0
        coriander_chili = 0
        house_vinaigrette = 0
        kokum_vinaigrette = 0

        print("The Party Pack")
        print("Quantity:", item.quantity)
        print("Bases:", item.bases)
        print("Protein Or Vegetables:", item.protein_or_vegetables)
        print("Sauces:", item.sauces)
        print("Veggies:", item.veggies)
        print("Toppings:", item.toppings)
        print("Chutneys:", item.chutneys)

        quantity = item.quantity

        # add the quantity of each item to the variable 
        bases = item.bases
        for base in bases:
            if "Basmati Rice" in base:
                basmati_rice += quantity
            if "Lemon Turmeric Rice" in base:
                lemon_turmeric_rice += quantity
            if "Supergrains" in base:
                supergrains += quantity
            if "South Indian Rice Noodles" in base:
                south_indian_rice_noodles += quantity
            if "Spinach" in base:
                spinach += quantity
            if "Sexygreens" in base:
                sexygreens += quantity
            if "Romaine" in base:
                romaine += quantity
            if "Arugula" in base:
                arugula += quantity
            if "Most Popular" in base:
                romaine += quantity
                lemon_turmeric_rice += quantity

        protein_veggies = item.protein_or_vegetables
        for protein in protein_veggies:
            if "Chicken Tikka" in protein:
                chicken_tikka += quantity
            if "Lamb Kebab" in protein:
                lamb_kebab += quantity
            if "Turmeric Ginger Shrimp" in protein or "Shrimp" in protein:
                turmeric_ginger_shrimp += quantity
            if "Spicy Chili Chicken" in protein:
                spicy_chili_chicken += quantity
            if "Sweet Potato Tikki" in protein:
                sweet_potato_tikki += quantity
            if "Harvest Vegetables" in protein:
                harvest_vegetables += quantity
            if "Tandoori Paneer" in protein:
                tandoori_paneer += quantity
            if "Most Popular" in protein:
                chicken_tikka += quantity
                sweet_potato_tikki += quantity
        
        sauces = item.sauces
        for sauce in sauces:
            if "Coconut Ginger" in sauce:
                coconut_ginger += quantity
            if "Peanut Sesame" in sauce:
                peanute_sesame += quantity
            if "Tamarind Chili" in sauce:
                tamarind_chili += quantity
            if "Tomato Garlic" in sauce:
                tomato_garlic += quantity
            if "Most Popular" in sauce:
                tomato_garlic += quantity
                coconut_ginger += quantity

        veggies = item.veggies
        for veg in veggies:
            if "Sautéed Spinach" in veg:
                sauteed_spinach += quantity
            if "Tossed Green Beans" in veg:
                tossed_green_beans += quantity
            if "Spiced Chickpeas" in veg:
                spiced_chickpeas += quantity
            if "Charred Eggplant" in veg:
                charred_egglant += quantity
            if "Most Popular" in veg:
                sauteed_spinach += quantity
                spiced_chickpeas += quantity


        toppings = item.toppings
        for topping in toppings:
            if "Cucumber Cubes" in topping:
                cucumber_cubes += quantity
            if "Masala Beets" in topping:
                masala_beets += quantity
            if "Pickled Onions" in topping:
                pickled_onions += quantity
            if "Pickled Radishes" in topping:
                pickled_radishes += quantity
            if "Mango Salsa" in topping:
                mango_salsa += quantity
            if "Cilantro" in topping:
                cilantro += quantity
            if "Kachumber Salad" in topping:
                kachumber_salad += quantity
            if "Carrot Slaw" in topping:
                carrot_slaw += quantity
            if "Indian Street Corn" in topping:
                indian_street_corn += quantity
            if "Pumpkin Seeds" in topping:
                pumpkin_seeds += quantity
            if "Roasted Lentils" in topping:
                roasted_lentils += quantity
            if "Tamarind Coconut Powder" in topping:
                tamarind_coconut_powder += quantity
            if "Avocado" in topping:
                avocado += quantity
            if "Most Popular" in topping:
                cucumber_cubes += quantity
                pickled_onions += quantity

        chutneys = item.chutneys
        for chutney in chutneys:
            if "Mint Cilantro Chutney" in chutney:
                mint_cilantro_chutney += quantity
            if "Toasted Cumin Yogurt" in chutney:
                toasted_cumin_yogurt += quantity
            if "Mango Coconut Yogurt" in chutney:
                mango_coconut_yogurt += quantity
            if "Tamarind Ginger Chutney" in chutney:
                tamarind_ginger_chutney += quantity
            if "Coriander Chili" in chutney:
                coriander_chili += quantity
            if "House Vinaigrette" in chutney:
                house_vinaigrette += quantity
            if "Kokum Vinaigrette" in chutney:
                kokum_vinaigrette += quantity
            if "Most Popular" in chutney:
                tamarind_ginger_chutney += quantity
                toasted_cumin_yogurt += quantity
            
        print("")
        data = [["Category", "Menu Item", "Raw", "UOM", "Amount", "UOM", "Amount", "UOM", "Container", "Utensil"],]
        
        for row in data:
            print("{:<10} {:<35} {:<10} {:<10} {:<10} {:<6} {:<10} {:<6} {:<10} {:<10}".format(*row))
        
        basmati_rice *= 4.25
        totalBasmatiRice += basmati_rice

        lemon_turmeric_rice *= 4.25
        totalLemonTurmericRice += lemon_turmeric_rice

        supergrains *= 4.25
        totalSupergrains += supergrains

        south_indian_rice_noodles *= 4.25
        totalSouthIndianRiceNoodles += south_indian_rice_noodles

        spinach *= 1
        totalSpinach += spinach

        sexygreens *= 1
        totalSexyGreens += sexygreens

        romaine *= 1
        totalRomaine += romaine

        arugula *= 1
        totalArugula += arugula

        chicken_tikka *= 2.75
        totalChickenTikka += chicken_tikka

        lamb_kebab *= 2
        totalLambKebab += lamb_kebab

        turmeric_ginger_shrimp *= 3
        totalTurmericGingerShrimp += turmeric_ginger_shrimp

        spicy_chili_chicken *= 2.75
        totalSpicyChiliChicken += spicy_chili_chicken

        sweet_potato_tikki *= 2
        totalSweetPotatoTikki += sweet_potato_tikki

        harvest_vegetables *= 2.5
        totalHarvestVegetables += harvest_vegetables

        tandoori_paneer *= 3
        totalTandooriPaneer += tandoori_paneer

        tomato_garlic *= 1
        totalTomato_garlic += tomato_garlic

        tamarind_chili *= 1
        totalTamarind_chili += tamarind_chili

        peanute_sesame *= 1
        totalPeanute_sesame += peanute_sesame

        coconut_ginger *= 1
        totalCoconut_ginger += coconut_ginger

        sauteed_spinach *= 1
        totalSauteed_spinach += sauteed_spinach

        charred_egglant *= 1
        totalCharred_egglant += charred_egglant

        spiced_chickpeas *= 1
        totalSpiced_chickpeas += spiced_chickpeas

        tossed_green_beans *= 0.6
        totalTossed_green_beans += tossed_green_beans

        cucumber_cubes *= 0.56
        totalCucumber_cubes += cucumber_cubes

        kachumber_salad *= 0.56
        totalKachumber_salad += kachumber_salad

        mango_salsa *= 0.56
        totalMango_salsa += mango_salsa

        pickled_radishes *= 0.2
        totalPickled_radishes += pickled_radishes

        pickled_onions *= 0.6
        totalPickled_onions += pickled_onions

        masala_beets *= 0.4
        totalMasala_beets += masala_beets

        indian_street_corn *= 0.56
        totalIndian_street_corn += indian_street_corn

        carrot_slaw *= 0.6
        totalCarrot_slaw += carrot_slaw

        cilantro *= 0.04
        totalCilantro += cilantro

        avocado *= 1
        totalAvocado += avocado

        pumpkin_seeds *= 0.2
        totalPumpkin_seeds += pumpkin_seeds

        roasted_lentils *= 0.08
        totalRoasted_lentils += roasted_lentils

        tamarind_coconut_powder *= 0.2
        totalTamarind_coconut_powder += tamarind_coconut_powder

        mint_cilantro_chutney *= 0.48
        totalMint_cilantro_chutney += mint_cilantro_chutney

        toasted_cumin_yogurt *= 0.48
        totalToasted_cumin_yogurt += toasted_cumin_yogurt

        mango_coconut_yogurt *= 0.48
        totalMango_coconut_yogurt += mango_coconut_yogurt

        tamarind_ginger_chutney *= 0.48
        totalTamarind_ginger_chutney += tamarind_ginger_chutney

        coriander_chili *= 0.48
        totalCoriander_chili += coriander_chili

        house_vinaigrette *= 0.48
        totalHouse_vinaigrette += house_vinaigrette

        kokum_vinaigrette *= 0.48
        totalKokum_vinaigrette += kokum_vinaigrette


        # Base category
        calculate_and_print("Base", "Basmati Rice", basmati_rice, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "Lemon Turmeric Rice", lemon_turmeric_rice, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "Supergrains", supergrains, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Base", "South Indian Rice Noodles", south_indian_rice_noodles, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Spinach", spinach, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Sexygreens", sexygreens, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Romaine", romaine, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Base", "Arugula", arugula, "oz-wt", "N/A", "Tongs")

        # Main category
        calculate_and_print("Main", "Chicken Tikka", chicken_tikka, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Lamb Kebab", lamb_kebab, "each", "N/A", "Tongs")
        calculate_and_print("Main", "Turmeric Ginger Shrimp", turmeric_ginger_shrimp, "each", "N/A", "C Spoon")
        calculate_and_print("Main", "Spicy Chili Chicken", spicy_chili_chicken, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Sweet Potato Tikki", sweet_potato_tikki, "each", "N/A", "Tongs")
        calculate_and_print("Main", "Harvest Vegetables", harvest_vegetables, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Main", "Tandoori Paneer", tandoori_paneer, "each", "N/A", "Tongs")

        # Sauce category
        calculate_and_print("Sauce", "Tomato Garlic", tomato_garlic, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Peanute Sesame", peanute_sesame, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Tamarind Chili", tamarind_chili, "oz-fl", "N/A", "Ladle")
        calculate_and_print("Sauce", "Coconut Ginger", coconut_ginger, "oz-fl", "N/A", "Ladle")

        # Vegetable category
        calculate_and_print("Vegetable", "Charred Eggplant", charred_egglant, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Vegetable", "Spiced Chickpeas", spiced_chickpeas, "oz-wt", "N/A", "C Spoon")
        calculate_and_print("Vegetable", "Tossed Green Beans", tossed_green_beans, "oz-wt", "N/A", "Tongs")
        calculate_and_print("Vegetable", "Sautéed Spinach", sauteed_spinach, "oz-wt", "N/A", "C Spoon")

        # Topping category
        calculate_and_print("Topping", "Cucumber Cubes", cucumber_cubes, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Masala Beets", masala_beets, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Pickled Onions", pickled_onions, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Pickled Radishes", pickled_radishes, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Mango Salsa", mango_salsa, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Cilantro", cilantro, "oz-wt", "N/A", "Fork")
        calculate_and_print("Topping", "Kachumber Salad", kachumber_salad, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Carrot Slaw", carrot_slaw, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Indian Street Corn", indian_street_corn, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Pumpkin Seeds", pumpkin_seeds, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Roasted Lentils", roasted_lentils, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Tamarind Coconut Powder", tamarind_coconut_powder, "oz-wt", "N/A", "Teaspoon")
        calculate_and_print("Topping", "Avocado", avocado, "each", "N/A", "Tongs")

        # Chutney category
        calculate_and_print("Chutney", "Mint Cilantro Chutney", mint_cilantro_chutney, "oz-fl")
        calculate_and_print("Chutney", "Toasted Cumin Yogurt", toasted_cumin_yogurt, "oz-fl")
        calculate_and_print("Chutney", "Mango Coconut Yogurt", mango_coconut_yogurt, "oz-fl")
        calculate_and_print("Chutney", "Tamarind Ginger Chutney", tamarind_ginger_chutney, "oz-fl", "N/A", "Teaspoon")
        calculate_and_print("Chutney", "Coriander Chili", coriander_chili, "oz-fl", "N/A", "Teaspoon")
        calculate_and_print("Chutney", "House Vinaigrette", house_vinaigrette, "oz-fl")
        calculate_and_print("Chutney", "Kokum Vinaigrette", kokum_vinaigrette, "oz-fl")

        print()

    #Tikka Chance On Me Bowl

    tikkachanceonmebowl_details = extract_tikka_chance_on_me_bowl_details(order)
    for item in tikkachanceonmebowl_details:

        chickenTikka = 0
        tomatoGarlicSauce = 0
        basmatiRice = 0
        sauteedSpinach = 0
        pickledRadish = 0
        kachumber = 0
        pickledOnions = 0
        toastedCuminYogurt = 0 
        mintCilantroChutney = 0

        print("Tikka Chance On Me Bowl")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Tikka Chance On Me Bowl\n")
        # f.close()

        chickenTikka += item.quantity
        tomatoGarlicSauce += item.quantity
        basmatiRice += item.quantity
        sauteedSpinach += item.quantity
        pickledRadish += item.quantity
        kachumber += item.quantity
        pickledOnions += item.quantity
        toastedCuminYogurt += item.quantity
        mintCilantroChutney += item.quantity

        chickenTikka *= 4
        totalChickenTikka += chickenTikka

        tomatoGarlicSauce *= 4
        totalTomato_garlic += tomatoGarlicSauce

        basmatiRice *= 7.3
        totalBasmatiRice += basmatiRice

        sauteedSpinach *= 2.4
        totalSauteed_spinach += sauteedSpinach

        pickledRadish *= 0.5
        totalPickled_radishes += pickledRadish

        kachumber *= 0.5
        totalKachumber_salad += kachumber

        pickledOnions *= 0.5
        totalPickled_onions += pickled_onions

        toastedCuminYogurt *= 1
        totalToasted_cumin_yogurt += toastedCuminYogurt

        mintCilantroChutney *= 1
        totalMint_cilantro_chutney += mintCilantroChutney

        calculate_and_print("Base", "Basmati Rice", basmatiRice)
        calculate_and_print("Main", "Chicken Tikka", chickenTikka)
        calculate_and_print("Sauce", "Tomato Garlic", tomatoGarlicSauce, "oz-fl")
        calculate_and_print("Vegetable", "Sautéed Spinach", sauteedSpinach)
        calculate_and_print("Topping", "Pickled Onions", pickledOnions)
        calculate_and_print("Topping", "Pickled Radishes", pickledRadish)
        calculate_and_print("Topping", "Kachumber Salad", kachumber)
        calculate_and_print("Chutney", "Toasted Cumin Yogurt", toastedCuminYogurt, "oz-fl")
        calculate_and_print("Chutney", "Mint Cilantro Chutney", mintCilantroChutney, "oz-fl")

        print()
 
    #Aloo Need Is Love Bowl

    alooneedislovebowl_details = extract_aloo_need_is_love_bowl_details(order)
    for item in alooneedislovebowl_details:

        lemonTurmericRice = 0
        sweetPotatoTikki  = 0
        coconutGingerSauce = 0
        charredEggplant = 0
        cucumberCubes = 0
        pickledRadishes = 0
        masalaBeets = 0
        roastedLentils = 0
        tamarindGingerChutney = 0

        print("Aloo Need Is Love Bowl")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Aloo Need Is Love Bowl\n")
        # f.close()

        lemonTurmericRice += item.quantity
        sweetPotatoTikki  += item.quantity
        coconutGingerSauce += item.quantity
        charredEggplant += item.quantity
        cucumberCubes += item.quantity
        pickledRadishes += item.quantity
        masalaBeets += item.quantity
        roastedLentils += item.quantity
        tamarindGingerChutney += item.quantity

        lemonTurmericRice *= 7.3
        totalLemonTurmericRice += lemonTurmericRice

        sweetPotatoTikki  *= 4
        totalSweetPotatoTikki += sweetPotatoTikki

        coconutGingerSauce *= 4
        totalCoconut_ginger += coconutGingerSauce

        charredEggplant *= 1.5
        totalCharred_egglant += charredEggplant

        cucumberCubes *= 0.5
        totalCucumber_cubes += cucumberCubes

        pickledRadishes *= 0.5
        totalPickled_radishes += pickledRadishes

        masalaBeets *= 0.5
        totalMasala_beets += masalaBeets

        roastedLentils *= 0.05
        totalRoasted_lentils += roastedLentils

        tamarindGingerChutney *= 0.8
        totalTamarind_ginger_chutney += tamarindGingerChutney

        calculate_and_print("Base", "Lemon Turmeric Rice", lemonTurmericRice)
        calculate_and_print("Main", "Sweet Potato Tikki", sweetPotatoTikki, "each")
        calculate_and_print("Sauce", "Coconut Ginger", coconutGingerSauce, "oz-fl")
        calculate_and_print("Vegetable", "Charred Eggplant", charredEggplant)
        calculate_and_print("Topping", "Cucumber Cubes", cucumberCubes)
        calculate_and_print("Topping", "Pickled Radishes", pickledRadishes)
        calculate_and_print("Topping", "Masala Beets", masalaBeets)
        calculate_and_print("Topping", "Roasted Lentils", roastedLentils)
        calculate_and_print("Chutney", "Tamarind Ginger", tamarindGingerChutney, "oz-fl")

        print()
    
    #Open Sesame Bowl

    opensesamebowl_details = extract_open_sesame_bowl_details(order)
    for item in opensesamebowl_details:

        basmatiRice = 0
        lambKebabMeatballs = 0
        peanutSesameSauce = 0 
        charredEggplants = 0
        cucumberCubes = 0 
        pickledOnions = 0
        mintCilantroChutney = 0
        mangoCoconutYogurt = 0

        print("Open Sesame Bowl")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Open Sesame Bowl\n")
        # f.close()

        basmatiRice += item.quantity
        lambKebabMeatballs += item.quantity
        peanutSesameSauce += item.quantity
        charredEggplants += item.quantity
        cucumberCubes += item.quantity
        pickledOnions += item.quantity
        mintCilantroChutney += item.quantity
        mangoCoconutYogurt += item.quantity
    
        basmatiRice *= 7.3
        totalBasmatiRice += basmatiRice

        lambKebabMeatballs *= 4
        totalLambKebab += lambKebabMeatballs 

        peanutSesameSauce *= 4
        totalPeanute_sesame += peanutSesameSauce

        charredEggplants *= 1.5
        totalCharred_egglant += charredEggplants

        cucumberCubes *= 0.5 
        totalCucumber_cubes += cucumberCubes

        pickledOnions *= 0.5
        totalPickled_onions += pickledOnions

        mintCilantroChutney *= 1
        totalMint_cilantro_chutney += mintCilantroChutney

        mangoCoconutYogurt *= 1
        totalMango_coconut_yogurt += mangoCoconutYogurt

        calculate_and_print("Base", "Basmati Rice", basmatiRice)
        calculate_and_print("Main", "Lamb Kebab Meatballs", lambKebabMeatballs, "each")
        calculate_and_print("Sauce", "Peanut Sesame", peanutSesameSauce, "oz-fl")
        calculate_and_print("Vegetable", "Charred Eggplant", charredEggplants)
        calculate_and_print("Topping", "Cucumber Cubes", cucumberCubes)
        calculate_and_print("Topping", "Pickled Onions", pickledOnions)
        calculate_and_print("Chutney", "Mint Cilantro", mintCilantroChutney, "oz-fl")
        calculate_and_print("Chutney", "Mango Coconut Yogurt", mangoCoconutYogurt, "oz-fl")

        print()
        
    #Home Cooking Bowl

    homecookingbowl_details = extract_home_cooking_bowl_details(order)
    for item in homecookingbowl_details:

        riceNoodles = 0
        turmericGingerShrimp = 0
        greenBeans = 0 
        mangoSalsa = 0
        coconutPowder = 0 
        tamarindChiliSauce = 0
        tamarindGingerChutney = 0
        mangoCoconutYogurt = 0

        print("Home Cooking Bowl")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Home Cooking Bowl\n")
        # f.close()

        riceNoodles += item.quantity
        turmericGingerShrimp += item.quantity
        greenBeans += item.quantity 
        mangoSalsa += item.quantity
        coconutPowder += item.quantity 
        tamarindChiliSauce += item.quantity
        tamarindGingerChutney += item.quantity
        mangoCoconutYogurt += item.quantity
    
        riceNoodles *= 6.5
        totalSouthIndianRiceNoodles += riceNoodles 

        turmericGingerShrimp *= 6
        totalTurmericGingerShrimp += turmericGingerShrimp

        greenBeans *= 2.5
        totalTossed_green_beans += greenBeans

        mangoSalsa *= 0.5
        totalMango_salsa += mangoSalsa

        coconutPowder *= 0.1
        totalTamarind_coconut_powder += coconutPowder

        tamarindChiliSauce *= 4
        totalTamarind_chili += tamarindChiliSauce

        tamarindGingerChutney *= 0.8
        totalTamarind_ginger_chutney += tamarindGingerChutney

        mangoCoconutYogurt *= 1
        totalMango_coconut_yogurt += mangoCoconutYogurt

        calculate_and_print("Base", "South Indian Cooking Noodles", riceNoodles)
        calculate_and_print("Main", "Turmeric Ginger Shrimp", turmericGingerShrimp, "each")
        calculate_and_print("Vegetable", "Tossed Green Beans", greenBeans)
        calculate_and_print("Topping", "Mango Salsa", mangoSalsa)
        calculate_and_print("Topping", "Tamarind Coconut Powder", coconutPowder)
        calculate_and_print("Sauce", "Tamarind Chili Sauce", tamarindChiliSauce, "oz-fl")
        calculate_and_print("Chutney", "Tamarind Ginger Chutney", tamarindGingerChutney, "oz-fl")
        calculate_and_print("Chutney", "Mango Coconut Yogurt", mangoCoconutYogurt, "oz-fl")

        print()
    
    #Harvest Chicken Bowl
        

    harvestchickenbowl_details = extract_harvest_chicken_bowl_details(order)
    for item in harvestchickenbowl_details:

        sexyGreens = 0
        lemonTurmericRice = 0
        chickenTikka = 0 
        tomatoGarlicSauce = 0
        harvestVegtables = 0 
        cucumberCubes = 0
        pickledOnions = 0
        toastedCuminYogurt = 0
        corianderChiliChutney = 0
        roastedLentils = 0

        print("Harvest Chicken Bowl")
        print("Quantity:", item.quantity)
        # print()

        # f = open(order, "a")
        # f.write("Harvest Chicken Bowl\n")
        # f.close()

        sexyGreens += item.quantity
        lemonTurmericRice += item.quantity
        chickenTikka += item.quantity 
        tomatoGarlicSauce += item.quantity
        harvestVegtables += item.quantity
        cucumberCubes += item.quantity
        pickledOnions += item.quantity
        toastedCuminYogurt += item.quantity
        corianderChiliChutney += item.quantity
        roastedLentils += item.quantity
    
        sexyGreens *= 1.9
        totalSexyGreens += sexyGreens

        lemonTurmericRice *= 3.65
        totalLemonTurmericRice += lemonTurmericRice

        chickenTikka *= 4 
        totalChickenTikka += chickenTikka

        tomatoGarlicSauce *= 4
        totalTomato_garlic += tomatoGarlicSauce

        harvestVegtables *= 1.65
        totalHarvestVegetables += harvestVegetables

        cucumberCubes *= 0.5
        totalCucumber_cubes += cucumberCubes

        pickledOnions *= 0.5
        totalPickled_onions += pickledOnions

        toastedCuminYogurt *= 1
        totalToasted_cumin_yogurt += toastedCuminYogurt

        corianderChiliChutney *= 1
        totalCoriander_chili += corianderChiliChutney

        roastedLentils *= 0.05
        totalRoasted_lentils += roastedLentils

        calculate_and_print("Base", "Sexygreens", sexyGreens)
        calculate_and_print("Base", "Lemon Turmeric Rice", lemonTurmericRice)
        calculate_and_print("Main", "Chicken Tikka", chickenTikka)
        calculate_and_print("Sauce", "Tomato Garlic Sauce", tomatoGarlicSauce, "oz-fl")
        calculate_and_print("Topping", "Harvest Vegetables", harvestVegtables)
        calculate_and_print("Topping", "Cucumber Cubes", cucumberCubes)
        calculate_and_print("Topping", "Pickled Onions", pickledOnions)
        calculate_and_print("Chutney", "Toasted Cumin Yogurt", toastedCuminYogurt, "oz-fl")
        calculate_and_print("Chutney", "Coriander Chili Chutney", corianderChiliChutney, "oz-fl")
        calculate_and_print("Topping", "Roasted Lentils", roastedLentils)

        print()
    
    #Vibes & Veggies Bowl

    vibesandveggiebowl_details = extract_vibes_and_veggie_bowl_details(order)
    for item in vibesandveggiebowl_details:

        baby_spinach = 0
        basmati_rice = 0
        coconut_ginger_sauce = 0
        tossed_green_beans = 0
        charred_eggplant = 0
        spiced_chickpeas = 0
        pickled_onions = 0
        carrot_slaw = 0
        indian_street_corn = 0
        tamarind_ginger_chutney = 0
        lentil_chips = 0

        print("Vibes & Veggies Bowl")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Vibes & Veggies Bowl\n")
        # f.close()

        #step 3: get the quantity of the bowl 
        quantity = item.quantity

        # step 4: set each the variables to the quantity 
        baby_spinach += quantity
        basmati_rice += quantity
        coconut_ginger_sauce += quantity
        tossed_green_beans += quantity
        charred_eggplant += quantity
        spiced_chickpeas += quantity
        pickled_onions += quantity
        carrot_slaw += quantity
        indian_street_corn += quantity
        tamarind_ginger_chutney += quantity
        lentil_chips += quantity

        baby_spinach *= 1.9
        totalSauteed_spinach += baby_spinach

        basmati_rice *= 3.65
        totalBasmatiRice += basmati_rice

        coconut_ginger_sauce *= 4
        totalCoconut_ginger += coconut_ginger_sauce

        tossed_green_beans *= 2.5
        totalTossed_green_beans += tossed_green_beans

        charred_eggplant *= 1.5
        totalCharred_egglant += charred_eggplant

        spiced_chickpeas *= 3.1
        totalSpiced_chickpeas += spiced_chickpeas

        pickled_onions *= 0.5
        totalPickled_onions += pickled_onions

        carrot_slaw *= 0.5
        totalCarrot_slaw += carrot_slaw

        indian_street_corn *= 0.5
        totalIndian_street_corn += indian_street_corn

        tamarind_ginger_chutney *= 0.8
        totalTamarind_ginger_chutney += tamarind_ginger_chutney

        lentil_chips *= 1
        totalLentilChips += lentil_chips 

        #step 6: calculate and print and weights 
        calculate_and_print("Base", "Baby Spinach", baby_spinach)
        calculate_and_print("Base", "Basmati Rice", basmati_rice)
        calculate_and_print("Sauce", "Coconut Ginger Sauce", coconut_ginger_sauce, "oz-fl")
        calculate_and_print("Vegetable", "Tossed Green Beans", tossed_green_beans)
        calculate_and_print("Vegetable", "Charred Eggplant", charred_eggplant)
        calculate_and_print("Vegetable", "Spiced Chickpeas", spiced_chickpeas)
        calculate_and_print("Topping", "Pickled Onions", pickled_onions)
        calculate_and_print("Topping", "Carrot Slaw", carrot_slaw)
        calculate_and_print("Topping", "Indian Street Corn", indian_street_corn)
        calculate_and_print("Chutney", "Tamarind Ginger Chutney", tamarind_ginger_chutney, "oz-fl")
        calculate_and_print("Topping", "Lentil Chips", lentil_chips, "each")
    
        print()

    #Chicken Tikka & Avocado Salad Bowl
        

    chickentikkaandavocadosaladbowl_details = extract_chicken_tikka_and_avocado_salad_bowl_details(order)
    for item in chickentikkaandavocadosaladbowl_details:

        romaine = 0
        arugula = 0
        chickenTikka = 0
        harvestVeggies = 0
        masalaBeets = 0
        kachumberSalad = 0
        carrotSlaw = 0
        avocado = 0 
        kokumVinaigrette = 0
        toastedCuminYogurt = 0
        pumpkinSeeds = 0

        print("Chicken Tikka & Avocado Salad Bowl")
        print("Quantity:", item.quantity)
        #print()

        # f = open(order, "a")
        # f.write("Chicken Tikka & Avocado Salad Bowl\n")
        # f.close()

        romaine += item.quantity
        arugula += item.quantity
        chickenTikka += item.quantity
        harvestVeggies += item.quantity
        kachumberSalad += item.quantity
        masalaBeets += item.quantity
        carrotSlaw += item.quantity
        toastedCuminYogurt += item.quantity
        avocado += item.quantity
        kokumVinaigrette += item.quantity
        pumpkinSeeds += item.quantity
    
        romaine *= 2.85
        totalRomaine += romaine

        arugula *= 0.75
        totalArugula += arugula

        chickenTikka *= 4
        totalChickenTikka += chickenTikka

        harvestVeggies *= 1.65
        totalHarvestVegetables += harvestVeggies

        kachumberSalad *= 0
        totalKachumber_salad += kachumberSalad

        masalaBeets *= 0.5
        totalMasala_beets += masalaBeets

        carrotSlaw *= 0.5
        totalCarrot_slaw += carrotSlaw

        toastedCuminYogurt *= 1
        totalToasted_cumin_yogurt += toastedCuminYogurt

        avocado *= 0.5
        totalAvocado += avocado

        kokumVinaigrette *= 1
        totalKokum_vinaigrette += kokumVinaigrette

        pumpkinSeeds *= .05
        totalPumpkin_seeds += pumpkinSeeds

        calculate_and_print("Base", "Romaine Lettuce", romaine)
        calculate_and_print("Base", "Arugula", arugula)
        calculate_and_print("Main", "Chicken Tikka", chickenTikka)
        calculate_and_print("Main", "Harvest Vegetables", harvestVeggies)
        calculate_and_print("Topping", "Kachumber Salad", kachumberSalad)
        calculate_and_print("Topping", "Masala Beets", masalaBeets)
        calculate_and_print("Topping", "Carrot Slaw", carrotSlaw)
        calculate_and_print("Topping", "Avocado", avocado, "each")
        calculate_and_print("Topping", "Roasted Pumpkin Seeds", pumpkinSeeds)
        calculate_and_print("Chutney", "Toasted Cumin Yogurt", toastedCuminYogurt, "oz-fl")
        calculate_and_print("Chutney", "Kokum Vinaigrette", kokumVinaigrette, "oz-fl")

        print()
    
    #Spicy Chili Chicken Bowl

    spicychilichickenbowl_details = extract_spicy_chili_chicken_bowl_details(order)
    for item in spicychilichickenbowl_details:

        spicyChiliChicken = 0
        coconutGingerSauce = 0
        basmatiRice = 0
        spicedChickpeas = 0
        kachumberSalad = 0
        mangoSalsa = 0
        cuminYogurt = 0
        tamarindCoconutPowder = 0 

        print("Spicy Chili Chicken Bowl")
        print("Quantity:", item.quantity)
        # print()

        # f = open(order, "a")
        # f.write("Spicy Chili Chicken Bowl\n")
        # f.close()

        spicyChiliChicken += item.quantity
        coconutGingerSauce += item.quantity
        basmatiRice += item.quantity
        spicedChickpeas += item.quantity
        kachumberSalad += item.quantity
        mangoSalsa += item.quantity
        cuminYogurt += item.quantity
        tamarindCoconutPowder += item.quantity

        spicyChiliChicken *= 4.5
        totalSpicyChiliChicken += spicyChiliChicken

        coconutGingerSauce *= 4
        totalCoconut_ginger += coconutGingerSauce

        basmatiRice *= 7.3
        totalBasmatiRice += basmatiRice

        spicedChickpeas *= 3.1
        totalSpiced_chickpeas += spicedChickpeas

        kachumberSalad *= 0.5
        totalKachumber_salad == kachumberSalad

        mangoSalsa *= 0.5
        totalMango_salsa += mangoSalsa

        cuminYogurt *= 1
        totalToasted_cumin_yogurt += cuminYogurt

        tamarindCoconutPowder *= 0.1
        totalTamarind_coconut_powder += tamarindCoconutPowder


        calculate_and_print("Base", "Basmati Rice", basmatiRice)
        calculate_and_print("Main", "Spicy Chili Chicken", spicyChiliChicken)
        calculate_and_print("Sauce", "Coconut Ginger Sauce", coconutGingerSauce, "oz-fl")
        calculate_and_print("Vegetable", "Spiced Chickpeas", spicedChickpeas)
        calculate_and_print("Topping", "Kachumber Salad", kachumberSalad)
        calculate_and_print("Topping", "Mango Salsa", mangoSalsa)
        calculate_and_print("Chutney", "Cumin Yogurt", cuminYogurt, "oz-fl")
        calculate_and_print("Topping", "Tamarind Coconut Powder", tamarindCoconutPowder, "oz-fl")

        print()
    
    #Tandoori Paneer Bowl


    tandooripaneerbowl_details = extract_tandoori_paneer_bowl_details(order)
    for item in tandooripaneerbowl_details:

        lemon_turmeric_rice = 0
        tandoori_paneer = 0
        tomato_garlic_sauce = 0
        sauteed_spinach = 0
        cucumber_cubes = 0
        chopped_cilantro = 0
        tamarind_ginger_chutney = 0
        mint_cilantro_chutney = 0
        chickpea_noodles = 0

        print("Tandoori Paneer Bowl")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Tandoori Paneer Bowl\n")
        # f.close()

        quantity = item.quantity

        # step 4: set each the variables to the quantity 
        lemon_turmeric_rice += quantity
        tandoori_paneer += quantity
        tomato_garlic_sauce += quantity
        sauteed_spinach += quantity
        cucumber_cubes += quantity
        chopped_cilantro += quantity
        tamarind_ginger_chutney += quantity
        mint_cilantro_chutney += quantity
        chickpea_noodles += quantity

        lemon_turmeric_rice *= 7.3
        totalLemonTurmericRice += lemon_turmeric_rice

        tandoori_paneer *= 5
        totalTandooriPaneer += tandoori_paneer

        tomato_garlic_sauce *= 4
        totalTomato_garlic += tomato_garlic_sauce

        sauteed_spinach *= 2.4
        totalSauteed_spinach += sauteed_spinach

        cucumber_cubes *= 0.5
        totalCucumber_cubes += cucumber_cubes

        chopped_cilantro *= 0.1
        totalCilantro += chopped_cilantro

        tamarind_ginger_chutney *= 0.8
        totalTamarind_ginger_chutney += tamarind_ginger_chutney

        mint_cilantro_chutney *= 1
        totalMint_cilantro_chutney += mint_cilantro_chutney

        chickpea_noodles *= 0.05
        totalChickpeaNoodle += chickpea_noodles 
        

        #step 6: calculate and print and weights 
        calculate_and_print("Base", "Lemon Turmeric Rice", lemon_turmeric_rice)
        calculate_and_print("Main", "Tandoori Paneer", tandoori_paneer, "each")
        calculate_and_print("Sauce", "Tomato Garlic Sauce", tomato_garlic_sauce, "oz-fl")
        calculate_and_print("Vegetable", "Sauteed Spinach", sauteed_spinach)
        calculate_and_print("Topping", "Cucumber Cubes", cucumber_cubes)
        calculate_and_print("Topping", "Chopped Cilantro", chopped_cilantro)
        calculate_and_print("Topping", "Chickpea Noodles", chickpea_noodles)
        calculate_and_print("Chutney", "Tamarind Ginger Chutney", tamarind_ginger_chutney, "oz-fl")
        calculate_and_print("Chutney", "Mint Cilantro Chutney", mint_cilantro_chutney, "oz-fl")
    
    #Naan Basket 

    totalNaans = 0

    naanbasket_details = extract_naan_basket_details(order)

    for item in naanbasket_details:
        naanBasket = 0 

        print("Naan Basket")
        print("Quantity:", item.quantity, "Size:", item.size, "Type:", item.type)

        # f = open(order, "a")
        # f.write("Naan Basket\n")
        # f.close()

        naanBasket += item.quantity

        if(item.size == "Small"):
            naanBasket *= 10
        if(item.size == "Large"):
            naanBasket *= 20

        totalNaans +=  naanBasket

        calculate_and_print("Side", "Naan Basket", naanBasket, "each", "N/A", "Tongs")
        print()
    
    #Samosa Tray

    totalSamosaTrays = 0 

    samosatray_details = extract_samosa_tray_details(order)
    for item in samosatray_details:
        samosaTray = 0 

        print("Samosa Tray")
        print("Quantity:", item.quantity, "Size:", item.size)
        
        samosaTray += item.quantity
        samosaTray *= item.size
        totalSamosaTrays += samosaTray

        calculate_and_print("Side", "Samosa Tray", samosaTray, "each", "N/A", "Tongs")
        print()


    
    #Cucumber Raita

    totalCucumberRaita = 0 

    cucumberraita_details = extract_cucumber_raita_details(order)
    for item in cucumberraita_details:
        cucumberRaita = 0 

        print("Cucumber Raita")
        print("Quantity:", item.quantity)

        cucumberRaita += item.quantity
        totalCucumberRaita += cucumberRaita

        calculate_and_print("Side", "Cucumber Raita", cucumberRaita)
        print()
    
    #Lentil Chips 

    lentilchips_details = extract_lentil_chips_order(order)
    for item in lentilchips_details:
        lentilChips = 0 
        print("Lentil Chips")
        print("Quantity:", item.quantity)

        lentilChips += item.quantity
        lentilChips *= 20
        totalLentilChips += lentilChips

        calculate_and_print("Side", "Lentil Chips", lentilChips)
        print()
    
    #Chai Chocolate Chip Cookie Basket
        
    totalCookieBaskets = 0 

    chaichocolatechipcookiebasket_details = extract_chai__chocolate_chip_cookie_basket_details(order)
    for item in chaichocolatechipcookiebasket_details:
        cookieBasket = 0
        print("Chai Chocolate Chip Cookie Basket")
        print("Quantity:", item.quantity, "Size:", item.size)

        cookieBasket += item.quantity 
        cookieBasket *= item.size
        totalCookieBaskets += cookieBasket

        calculate_and_print("Dessert", "Chai Chocolate Chip Cookie Basket", cookieBasket, "each", "N/A", "Tongs")
        print()
    
    # Indian Yogurt 
        
    totalIndianYogurt = 0 

    indianyogurt_details = extract_indian_yogurt_details(order)
    for item in indianyogurt_details:
        indianYogurt = 0
        print("Indian Yogurt")
        print("Quantity:", item.quantity)

        indianYogurt += item.quantity
        totalIndianYogurt += indianYogurt

        calculate_and_print("Dessert", "Indian Yogurt", indianYogurt)
        print()

    # Additional Bases: 
        
    # Basmati Rice
        

    basmatirice_details = extract_basmati_rice_details(order)
    for item in basmatirice_details:
        basmatiRice = 0 

        print("Basmati Rice")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Basmati Rice\n")
        # f.close()

        basmatiRice += item.quantity
        basmatiRice *= 38.25
        totalBasmatiRice += basmatiRice


        calculate_and_print("Base", "Basmati Rice", basmatiRice)
        print()
        
    # Lemon Turmeric Rice 
        

    lemonturmericrice_details = extract_lemon_turmeric_rice_details(order)
    for item in lemonturmericrice_details:
        lemonTurmericRice = 0 
        print("Lemon Turmeric Rice")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Lemon Turmeric Rice\n")
        # f.close()

        lemonTurmericRice += item.quantity
        lemonTurmericRice *= 38.25
        totalLemonTurmericRice += lemonTurmericRice

        calculate_and_print("Base", "Lemon Turmeric Rice", lemonTurmericRice)
        print()

    # South Indian Rice Noodles 
        
    

    southindianricenoodles_details = extract_south_indian_rice_noodles_details(order)
    for item in southindianricenoodles_details:
        southIndianRiceNoodles = 0
        print("South Indian Rice Noodles")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("South Indian Rice Noodles\n")
        # f.close()

        southIndianRiceNoodles += item.quantity
        southIndianRiceNoodles *= 38.25
        totalSouthIndianRiceNoodles += southIndianRiceNoodles
        calculate_and_print("Base", "South Indian Rice Noodles", southIndianRiceNoodles)
        print()

    # Supergrains 
    

    supergrains_details = extract_supergrains_details(order)
    for item in supergrains_details:
        supergrains = 0 
        print("Supergrains")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Supergrains\n")
        # f.close()

        supergrains += item.quantity
        supergrains *= 38.25
        totalSupergrains += supergrains
        calculate_and_print("Base", "Supergrains", supergrains)
        print()
    

    # Additional Mains: 
        
    # Chicken Tikka


    chickentikka_details = extract_chicken_tikka_details(order)
    for item in chickentikka_details:
        chickenTikka = 0 
        print("Chicken Tikka")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Chicken Tikka\n")
        # f.close()

        chickenTikka += item.quantity
        chickenTikka *= 55
        totalChickenTikka += chickenTikka
        calculate_and_print("Main", "Chicken Tikka", chickenTikka)
        print()
    
    # Sweet Potato

    sweetpotatotikki_details = extract_sweet_potato_tikki_details(order)
    for item in sweetpotatotikki_details:
        sweetPotatoTikki = 0 
        print("Sweet Potato Tikki")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Sweet Potato Tikki\n")
        # f.close()

        sweetPotatoTikki += item.quantity
        sweetPotatoTikki *= 40
        totalSweetPotatoTikki += sweetPotatoTikki
        calculate_and_print("Main", "Sweet Potato Tikki", sweetPotatoTikki, "each")
        print()
    
    # Lamb Kebab
    

    lambkebab_details = extract_lamb_kebab_details(order)
    for item in lambkebab_details:
        lambKebab = 0 
        print("Lamb Kebab")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Lamb Kebab\n")
        # f.close()

        lambKebab += item.quantity
        lambKebab *= 40
        totalLambKebab += lambKebab
        calculate_and_print("Main", "Lamb Kebab", lambKebab, "each")
        print()

    # Turmeric Ginger Shrimp
        
    

    turmericgingershrimp_details = extract_turmeric_ginger_shrimp_details(order)
    for item in turmericgingershrimp_details:
        turmericGingerShrimp = 0 
        print("Turmeric Ginger Shrimp")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Turmeric Ginger Shrimp\n")
        # f.close()
        turmericGingerShrimp += item.quantity
        turmericGingerShrimp *= 60
        totalTurmericGingerShrimp += turmericGingerShrimp
        calculate_and_print("Main", "Turmeric Ginger Shrimp", turmericGingerShrimp, "each")
        print()
    
    # Tandoori Paneer
        


    tandooripaneer_details = extract_tandoori_paneer_details(order)
    for item in tandooripaneer_details:
        tandooriPaneer = 0 
        print("Tandoori Paneer")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Tandoori Paneer\n")
        # f.close()

        tandooriPaneer += item.quantity
        tandooriPaneer *= 50
        totalTandooriPaneer += tandooriPaneer
        calculate_and_print("Main", "Tandoori Paneer", tandooriPaneer, "each")
        print()
    
    # Spicy Chili Chicken 
    
    spicychilichicken_details = extract_spicy_chilli_chicken_details(order)
    for item in spicychilichicken_details:
        spicyChiliChicken = 0 
        print("Spicy Chili Chicken")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Spicy Chili Chicken\n")
        # f.close()

        spicyChiliChicken += item.quantity
        spicyChiliChicken *= 55
        totalSpicyChiliChicken += spicyChiliChicken
        calculate_and_print("Main", "Spicy Chili Chicken", spicyChiliChicken)
        print()
    
    # Harvest Vegetables 
    harvestvegetables_details = extract_harvest_vegtables_details(order)
    for item in harvestvegetables_details:
        harvestVegetables = 0
        print("Harvest Vegetables")
        print("Quantity:", item.quantity)

        harvestVegetables += item.quantity
        harvestVegetables *= 50
        totalHarvestVegetables += harvestVegetables
        calculate_and_print("Main", "Harvest Vegetables", harvestVegetables)
        print()

    # Additional Sauces: 
        
    # Tomato Garlic 
        
    tomatogarlic_details = extract_tomato_garlic_sauce_details(order)
    for item in tomatogarlic_details:
        tomatoGarlicSauce = 0 
        print("Tomato Garlic Sauce")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Tomato Garlic Sauce\n")
        # f.close()

        tomatoGarlicSauce += item.quantity
        tomatoGarlicSauce *= 32
        totalTomato_garlic += tomatoGarlicSauce
        calculate_and_print("Sauce", "Tomato Garlic Sauce", tomatoGarlicSauce, "oz-fl")
        print()
        
    # Tamarind Chili
        
    tamarindchili_details = extract_tamarind_chili_sauce_details(order)
    for item in tamarindchili_details:
        tamarindChiliSauce = 0 
        print("Tamarind Chili Sauce")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Tamarind Chili Sauce\n")
        # f.close()

        tamarindChiliSauce += item.quantity
        tamarindChiliSauce *= 32
        totalTamarind_chili += tamarindChiliSauce
        calculate_and_print("Sauce", "Tamarind Chili Sauce", tamarindChiliSauce, "oz-fl")
        print()
        
    # Coconut Ginger
        
   

    coconutginger_details = extract_coconut_ginger_sauce_details(order)
    for item in coconutginger_details:
        coconutGingerSauce = 0 
        print("Cocunut Ginger Sauce")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Cocunut Ginger Sauce\n")
        # f.close()

        coconutGingerSauce += item.quantity
        coconutGingerSauce *= 32
        totalCoconut_ginger += coconutGingerSauce
        calculate_and_print("Sauce", "Cocunut Ginger Sauce", coconutGingerSauce, "oz-fl")
        print()

    # Peanut Sesame 
        
    

    peanutsesame_details = extract_peanut_sesame_sauce_details(order)
    for item in peanutsesame_details:
        peanutSesameSauce = 0 
        print("Peanut Sesame Sauce")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Peanut Sesame Sauce\n")
        # f.close()

        peanutSesameSauce += item.quantity
        peanutSesameSauce *= 32
        totalPeanute_sesame += peanutSesameSauce
        calculate_and_print("Sauce", "Peanut Sesame Sauce", peanutSesameSauce, "oz-fl")
        print()
    

    # Additional Veggies: 
        
    # Spiced Chickpeas 

    

    spicedchickpeas_details = extract_spiced_chickpeas_details(order)
    for item in spicedchickpeas_details:
        spicedChickpeas = 0 
        print("Spiced Chickpeas")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Spiced Chickpeas\n")
        # f.close()

        spicedChickpeas += item.quantity
        spicedChickpeas *= 37.5
        totalSpiced_chickpeas += spicedChickpeas
        calculate_and_print("Vegetable", "Spiced Chickpeas", spicedChickpeas)
        print()
        
    # Tossed Green Beans
        
    

    tossedgreenbeans_details = extract_tossed_green_beans_details(order)
    for item in tossedgreenbeans_details:
        tossedGreenBeans = 0 
        print("Tossed Green Beans")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Tossed Green Beans\n")
        # f.close()

        tossedGreenBeans += item.quantity
        tossedGreenBeans *= 22.5
        totalTossed_green_beans += tossedGreenBeans
        calculate_and_print("Vegetable", "Tossed Green Beans", tossedGreenBeans)
        print()

    # Sauteed Spinach
        
    

    sauteedspinach_details = extract_sauteed_spinach_details(order)
    for item in sauteedspinach_details:
        sauteedSpinach = 0 
        print("Sautéed Spinach")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Sauteed Spinach\n")
        # f.close()

        sauteedSpinach += item.quantity
        sauteedSpinach *= 37.5
        totalSauteed_spinach += sauteedSpinach
        calculate_and_print("Vegetable", "Sautéed Spinach", sauteedSpinach)
        print()
        
    # Charred Eggplant 
        
   

    charredeggplant_details = extract_charred_eggplant_details(order)
    for item in charredeggplant_details:
        charredEggplant = 0 
        print("Charred Eggplant")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("Charred Eggplant\n")
        # f.close()

        charredEggplant += item.quantity
        charredEggplant *= 37.5
        totalCharred_egglant += charredEggplant
        calculate_and_print("Vegetable", "Charred Eggplant", charredEggplant)
        print()
    
    # Beverages
        
    # LaCroix Sparkling Water (w flavor)

    totalLaCroixSparklingWater = 0 

    lacroixsparklingwater_details = extract_la_croix_sparkling_water_details(order)
    for item in lacroixsparklingwater_details:
        laCroixSparklingWater = 0
        print("LaCroix Sparkling Water")
        print("Quantity:", item.quantity, "Flavor:", item.flavor)
    
        # f = open(order, "a")
        # f.write("LaCroix Sparkling Water\n")
        # f.close()

        laCroixSparklingWater += item.quantity
        totalLaCroixSparklingWater += laCroixSparklingWater
        calculate_and_print("Beverage", "LaCroix Sparkling Water", laCroixSparklingWater, "each")
        print()

    # RAIN Water
        
    totalRAINWater = 0 

    rainwater_details = extract_RAIN_Water_details(order)
    for item in rainwater_details:
        rAINWater = 0 
        print("RAIN Water")
        print("Quantity:", item.quantity)

        # f = open(order, "a")
        # f.write("RAIN Water\n")
        # f.close()

        rAINWater += item.quantity
        totalRAINWater += rAINWater
        calculate_and_print("Beverage", "RAIN Water", rAINWater, "each")
        print()
    
    # Mango Lassi 

    totalMangoLaasi = 0 

    mangolaasi_details = extract_mango_lassi_details(order)
    for item in mangolaasi_details:
        mangoLassi = 0 
        print("Mango Lassi")
        print("Quantity:", item.quantity)
        
        # f = open(order, "a")
        # f.write("Mango Lassi\n")
        # f.close()   

        mangoLassi += item.quantity
        totalMangoLaasi += mangoLassi
        calculate_and_print("Beverage", "Mango Lassi", mangoLassi, "each")
        print()
    
    # Wild Kombucha (w flavor)
        
    totalWildKombucha = 0 

    wildkombucha_details = extract_wild_kombucha_details(order)
    for item in wildkombucha_details:
        wildKombucha = 0 
        print("Wild Kombucha")
        print("Quantity:", item.quantity, "Flavor:", item.flavor)
    
        # f = open(order, "a")
        # f.write("Wild Kombucha\n")
        # f.close()

        wildKombucha += item.quantity
        totalWildKombucha += wildKombucha
        calculate_and_print("Beverage", "Wild Kombucha", wildKombucha, "each")
        print()

    # Icaro Spearmint Yerba Mate 
    
    totalYerbaMate = 0 

    mintyerbamate_details = extract_mint_yerba_mate_detail(order)
    for item in mintyerbamate_details:
        icaroSpearmintYerbaMate = 0 
        print("Icaro Spearmint Yerba Mate")
        print("Quantity:", item.quantity)
        #print()

        # f = open(order, "a")
        # f.write("Icaro Spearmint Yerba Mate\n")
        # f.close()

        icaroSpearmintYerbaMate += item.quantity
        totalYerbaMate += icaroSpearmintYerbaMate

        calculate_and_print("Beverage", "Icaro Spearmint Yerba Mate", icaroSpearmintYerbaMate, "each")
        print()
    
    # Utensils 
        
    totalUtensils = 0 

    utensils_details = extract_utensils_detail(order)
    for item in utensils_details:
        utensils = 0 
        print("Utensils")
        print("Quantity:", item.quantity)

        utensils += item.quantity
        totalUtensils += utensils
        calculate_and_print("Other", "Utensils", utensils, "each")
        print()

    print()

    # Base category
    calculate_and_print("Total", "Basmati Rice", round(totalBasmatiRice/(20*16), 2), totalBasmatiRice)
    calculate_and_print("Total", "Lemon Turmeric Rice", round(totalLemonTurmericRice/(20*16), 2), totalLemonTurmericRice)
    calculate_and_print("Total", "Supergrains", 0, totalSupergrains)
    calculate_and_print("Total", "South Indian Rice Noodles", 0, totalSouthIndianRiceNoodles)
    calculate_and_print("Total", "Spinach", 0, totalSpinach)
    calculate_and_print("Total", "Sexygreens", 0, totalSexyGreens)
    calculate_and_print("Total", "Romaine", 0, totalRomaine)
    calculate_and_print("Total", "Arugula", 0, totalArugula)

    # Main category
    calculate_and_print("Total", "Chicken Tikka", round(totalChickenTikka/(0.65*16), 2), totalChickenTikka)
    calculate_and_print("Total", "Lamb Kebab", 0, totalLambKebab, "each")
    calculate_and_print("Total", "Turmeric Ginger Shrimp", 0, totalTurmericGingerShrimp, "each")
    calculate_and_print("Total", "Spicy Chili Chicken", round(totalSpicyChiliChicken/(3.97*16), 2), totalSpicyChiliChicken)
    calculate_and_print("Total", "Sweet Potato Tikki", 0, totalSweetPotatoTikki, "each")
    calculate_and_print("Total", "Harvest Vegetables", round(totalHarvestVegetables/(2.12*16), 2), totalHarvestVegetables)
    calculate_and_print("Total", "Tandoori Paneer", 0, totalTandooriPaneer, "each")

    # Sauce category
    calculate_and_print("Total", "Tomato Garlic", round(totalTomato_garlic/152.38, 2), totalTomato_garlic, "oz-fl")
    calculate_and_print("Total", "Peanut Sesame", round(totalPeanute_sesame/152.38, 2), totalPeanute_sesame, "oz-fl")
    calculate_and_print("Total", "Tamarind Chili", round(totalTamarind_chili/152.38, 2), totalTamarind_chili, "oz-fl")
    calculate_and_print("Total", "Coconut Ginger", round(totalCoconut_ginger/152.38, 2), totalCoconut_ginger, "oz-fl")

    # Vegetable category
    calculate_and_print("Total", "Charred Eggplant", round(totalCharred_egglant/(1.63125*16), 2), totalCharred_egglant)
    calculate_and_print("Total", "Spiced Chickpeas", round(totalSpiced_chickpeas/(3.94*16), 2), totalSpiced_chickpeas)
    calculate_and_print("Total", "Tossed Green Beans", round(totalTossed_green_beans/(2.15625*16), 2), totalTossed_green_beans)
    calculate_and_print("Total", "Sautéed Spinach", round(totalSauteed_spinach/(5.5875*16), 2), totalSauteed_spinach)

    # Topping category
    calculate_and_print("Total", "Cucumber Cubes", 0, totalCucumber_cubes)
    calculate_and_print("Total", "Masala Beets", 0, totalMasala_beets)
    calculate_and_print("Total", "Pickled Onions", 0, totalPickled_onions)
    calculate_and_print("Total", "Pickled Radishes", 0, totalPickled_radishes)
    calculate_and_print("Total", "Mango Salsa", 0, totalMango_salsa)
    calculate_and_print("Total", "Cilantro", 0, totalCilantro)
    calculate_and_print("Total", "Kachumber Salad", 0, totalKachumber_salad)
    calculate_and_print("Total", "Carrot Slaw", 0, totalCarrot_slaw)
    calculate_and_print("Total", "Indian Street Corn", 0, totalIndian_street_corn)
    calculate_and_print("Total", "Pumpkin Seeds", 0, totalPumpkin_seeds)
    calculate_and_print("Total", "Roasted Lentils", 0, totalRoasted_lentils)
    calculate_and_print("Total", "Tamarind Coconut Powder", 0, totalTamarind_coconut_powder)
    calculate_and_print("Total", "Avocado", 0, totalAvocado, "each")
    calculate_and_print("Total", "Chickpea Noodles", 0, totalChickpeaNoodle)

    # Chutney category
    calculate_and_print("Total", "Mint Cilantro Chutney", 0, totalMint_cilantro_chutney, "oz-fl")
    calculate_and_print("Total", "Toasted Cumin Yogurt", 0, totalToasted_cumin_yogurt, "oz-fl")
    calculate_and_print("Total", "Mango Coconut Yogurt", 0, totalMango_coconut_yogurt, "oz-fl")
    calculate_and_print("Total", "Tamarind Ginger Chutney", 0, totalTamarind_ginger_chutney, "oz-fl")
    calculate_and_print("Total", "Coriander Chili", 0, totalCoriander_chili, "oz-fl")
    calculate_and_print("Total", "House Vinaigrette", 0, totalHouse_vinaigrette, "oz-fl")
    calculate_and_print("Total", "Kokum Vinaigrette", 0, totalKokum_vinaigrette, "oz-fl")

    # Sides 
    calculate_and_print("Total", "Naan Basket", 0, totalNaans, "each", "N/A", "Tongs")
    calculate_and_print("Total", "Samosa Tray", 0, totalSamosaTrays, "each", "N/A", "Tongs")
    calculate_and_print("Total", "Cucumber Raita", 0, totalCucumberRaita, "each")
    calculate_and_print("Total", "Lentil Chips", 0, totalLentilChips, "each")

    # Desserts 
    calculate_and_print("Total", "Chai Chocolate Chip Cookie Basket", 0, totalCookieBaskets, "each", "N/A", "Tongs")
    calculate_and_print("Total", "Indian Yogurt", 0, totalIndianYogurt, "each")
    
    # Beverages
    calculate_and_print("Total", "LaCroix Sparkling Water", 0, totalLaCroixSparklingWater, "each")
    calculate_and_print("Total", "RAIN Water", 0, totalRAINWater, "each") 
    calculate_and_print("Total", "Mango Lassi", 0, totalMangoLaasi, "each")
    calculate_and_print("Total", "Wild Kombucha", 0, totalWildKombucha, "each")
    calculate_and_print("Total", "Icaro Spearmint Yerba Mate", 0, totalYerbaMate, "each")

    # Utensils 
    calculate_and_print("Total", "Utensils", 0, totalUtensils, "each")



