import pygame

from asset_list import *

pygame.font.init()

WIDTH, HEIGHT = 32*20, 32*20
MENU_W, MENU_H = int(WIDTH*0.25), HEIGHT
WIN = pygame.display.set_mode((WIDTH+MENU_W, HEIGHT))
FPS = 60

MAIN_FONT = pygame.font.SysFont("Arial", 20)
MEDIUM_FONT = pygame.font.SysFont("Arial", 15)
SMALL_FONT = pygame.font.SysFont("Arial", 10)
ROUND_COOLDOWN = 25*1000 # in milliseconds

TILE_SIZE = (32, 32)
PROJ_SIZE = (4, 4)
TOWER_SIZE = (32, 32)
NUM_TILES = (WIDTH//TILE_SIZE[0], HEIGHT//TILE_SIZE[1]) # numbers of tiles as tuple (columns, rows)

UNIT_LIST =[]
TOWER_LIST = []
PROJ_LIST = []
BUTTON_LIST = []
EFFECT_LIST = []

USEREVENTS = {
    "round_start": pygame.USEREVENT,
    "unit_spawn": pygame.USEREVENT + 1
}

COLORS = {
    "black": (0, 0, 0),
    "blue": (0, 0, 255),
    "blue_dark": (0, 0, 139),
    "blue_light": (173, 216, 230),
    "brown": (153, 120, 0),
    "gray": (128, 128, 128),
    "green": (0, 255, 0),
    "green_dark": (0, 120, 0),
    "red": (255, 0, 0),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 136, 0),
    "hotpink": (255, 105, 180),
    "olive": (128, 128, 0),
    "greenyellow": (173, 255, 47)
}

TOWER_TYPES = {
    "basic": {
        "atk_speed": 1,    
        "cost": 10,
        "color": "white",
        "range": 150,
        "proj_type": "basic",
        "crit_chance": 0.1,
        "display_name": "Basic Tower",
        "skin": "tower_base_img",
        "upgrades": {
            "upgrade_a": {
                "atk_speed": 1,    
                "cost": 25,
                "color": "brown",
                "range": 300,
                "proj_type": "basic",
                "crit_chance": 0.25,
                "display_name": "Ranged Tower",
                "skin": "tower_base_img",
                "upgrades": {}
            },
            "upgrade_b": {
                "atk_speed": 0.25,    
                "cost": 25,
                "color": "gray",
                "range": 150,
                "proj_type": "basic",
                "crit_chance": 0.1,
                "display_name": "Fast Tower",
                "skin": "tower_base_img",
                "upgrades": {}
            }
        }
    },
    "singleTarget": {
        "atk_speed": 5,     
        "cost": 25,
        "color": "greenyellow",
        "range": 300,
        "proj_type": "seeking",
        "crit_chance": 0.5,
        "display_name": "Sniper Tower",
        "skin": "tower_base_img",
        "upgrades": {
            "upgrade_a": {
                "atk_speed": 5,     
                "cost": 150,
                "color": "green_dark",
                "range": 600,
                "proj_type": "seeking",
                "crit_chance": 1,
                "display_name": "Long Range Tower",
                "skin": "tower_base_img",
                "upgrades": {
                    "upgrade_a": {
                        "atk_speed": 5,     
                        "cost": 1500,
                        "color": "green",
                        "range": 1000,
                        "proj_type": "sniper",
                        "crit_chance": 1,
                        "display_name": "Assassin Tower",
                        "skin": "tower_base_img",
                        "upgrades": {}
                    },
                    "upgrade_b": {
                        "atk_speed": 1,     
                        "cost": 1500,
                        "color": "green",
                        "range": 1000,
                        "proj_type": "seeking",
                        "crit_chance": 1,
                        "display_name": "Fast Sniper",
                        "skin": "tower_base_img",
                        "upgrades": {}
                    }
                }
            },
            "upgrade_b": {
                "atk_speed": 2,     
                "cost": 150,
                "color": "olive",
                "range": 300,
                "proj_type": "poison",
                "crit_chance": 0.5,
                "display_name": "Poison Tower",
                "skin": "tower_base_img",
                "upgrades": {}
            }
        }
    },
    "AoE": {
        "atk_speed": 3,     
        "cost": 50,
        "color": "red",
        "range": 100,
        "proj_type": "AoE",
        "crit_chance": 0.1,
        "display_name": "Explosion Tower",
        "skin": "tower_base_img",
        "upgrades": {
            "upgrade_a": {
                "atk_speed": 3,     
                "cost": 150,
                "color": "blue",
                "range": 300,
                "proj_type": "Iceplosion",
                "crit_chance": 0,
                "display_name": "Iceplosion Tower",
                "skin": "tower_base_img",
                "upgrades": {}
            },
            "upgrade_b": {
                "atk_speed": 4,     
                "cost": 500,
                "color": "orange",
                "range": 100,
                "proj_type": "Nuke",
                "crit_chance": 1,
                "display_name": "Nuke Tower",
                "skin": "tower_base_img",
                "upgrades": {
                    "upgrade_a": {
                        "atk_speed": 0.8,     
                        "cost": 2500,
                        "color": "hotpink",
                        "range": 300,
                        "proj_type": "Nuke",
                        "crit_chance": 0.1,
                        "display_name": "Fast Nuke Tower",
                        "skin": "tower_base_img",
                        "upgrades": {}
                    },
                    "upgrade_b": {
                        "atk_speed": 4,     
                        "cost": 2500,
                        "color": "hotpink",
                        "range": 500,
                        "proj_type": "Nuke",
                        "crit_chance": 1,
                        "display_name": "Long Nuke Tower",
                        "skin": "tower_base_img",
                        "upgrades": {}
                    }
                }
            }
        }
    },
    "superFast": {
        "atk_speed": 0.2,     
        "cost": 50,
        "color": "blue_light",
        "range": 100,
        "proj_type": "weak",
        "crit_chance": 0.2,
        "display_name": "PewPew Tower",
        "skin": "tower_base_img",
        "upgrades": {
            "upgrade_a": {
                "atk_speed": 0.04,     
                "cost": 300,
                "color": "blue",
                "range": 100,
                "proj_type": "weak",
                "crit_chance": 0.2,
                "display_name": "PewPewPew Tower",
                "skin": "tower_base_img",
                "upgrades": {
                    "upgrade_a": {
                        "atk_speed": 0.001,     
                        "cost": 1800,
                        "color": "blue",
                        "range": 100,
                        "proj_type": "weak",
                        "crit_chance": 0.2,
                        "display_name": "PEWPEWPEWPEW",
                        "skin": "tower_base_img",
                        "upgrades": {}
                    },
                    "upgrade_b": {
                        "atk_speed": 0.04,     
                        "cost": 1000,
                        "color": "green",
                        "range": 300,
                        "proj_type": "weak",
                        "crit_chance": 1,
                        "display_name": "Stream Tower",
                        "skin": "tower_base_img",
                        "upgrades": {}
                    }
                }
            },
            "upgrade_b": {
                "atk_speed": 0.3,     
                "cost": 300,
                "color": "green",
                "range": 100,
                "proj_type": "basic",
                "crit_chance": 1,
                "display_name": "PewPewBang Tower",
                "skin": "tower_base_img",
                "upgrades": {}
            }
        }
    },
    # "lightning": {
    #     "atk_speed": 0.2,     
    #     "cost": 25,
    #     "color": "blue_light",
    #     "range": 100,
    #     "proj_type": "weak"
    #     "crit_chance": 0.1,
    # }
}

UNIT_TYPES = {
    "basic": {
        "move_speed": 2,
        "hp": 10,
        "size": (20, 20),          
        "gold_value": 5,
        "special": False,   
        "skin": unit_basic_img
    },
    "fast": {
        "move_speed": 4,
        "hp": 5,
        "size": (20, 20),          
        "gold_value": 4,
        "special": "stim",    
        "skin": unit_fast_img
    },
    "tank": {
        "move_speed": 1,
        "hp": 25,
        "size": (20, 20),          
        "gold_value": 10,
        "special": "regen",    
        "skin": unit_tank_img
    }
}

PROJ_TYPES = {
    "basic": {
        "dmg": 4,
        "speed": 20,
        "spread": 1, # ???
        "AoE": False,
        "AoE_area": 0,
        "seeking": False,
        "condition": False,
        "effect": False,
        "color": "white"
    },
    "seeking": {
        "dmg": 10,
        "speed": 6,
        "spread": 1, # ???
        "AoE": False,
        "AoE_area": 0,
        "seeking": True,
        "condition": False,
        "effect": False,
        "color": "blue"
    },
    "poison": {
        "dmg": 10,
        "speed": 6,
        "spread": 1, # ???
        "AoE": False,
        "AoE_area": 0,
        "seeking": True,
        "condition": "poison",
        "effect": False,
        "color": "green"
    },
    "sniper": {
        "dmg": 1000,
        "speed": 30,
        "spread": 1, # ???
        "AoE": False,
        "AoE_area": 0,
        "seeking": True,
        "condition": False,
        "effect": False,
        "color": "hotpink"
    },
    "weak": {
        "dmg": 1.5,
        "speed": 50,
        "spread": 1, # ???
        "AoE": False,
        "AoE_area": 0,
        "seeking": True,
        "condition": False,
        "effect": False,
        "color": "blue_light"
    },
    "AoE": {
        "dmg": 5,
        "speed": 10,
        "spread": 1, # ???
        "AoE": True,
        "AoE_area": 50,
        "seeking": True,
        "condition": False,
        "effect": "explosion",
        "color": "red"
    },
    "Iceplosion": {
        "dmg": 1,
        "speed": 5,
        "spread": 1, # ???
        "AoE": True,
        "AoE_area": 100,
        "seeking": True,
        "condition": "slow",
        "effect": "iceplosion",
        "color": "blue"
    },
    "Nuke": {
        "dmg": 20,
        "speed": 10,
        "spread": 1, # ???
        "AoE": True,
        "AoE_area": 150,
        "seeking": True,
        "condition": False,
        "effect": "nuke",
        "color": "white"
    }
}

# ------------------- Save for multiple files being executed -------------------

if __name__ == "__main__":
    print("Don't run this as main.")
