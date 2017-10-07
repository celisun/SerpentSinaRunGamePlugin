from serpent.game import Game

from .api.api import SinaRunAPI

from serpent.utilities import Singleton




class SerpentSinaRunGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "SinaRun"

        kwargs["app_id"] = "324470"
        kwargs["app_args"] = None
        
        
        

        super().__init__(**kwargs)

        self.api_class = SinaRunAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            #"SAMPLE_REGION": (y1, x1, y2, x2)
            "MAIN_MENU_SINGLE":  (137, 35, 164, 376)
            "SELECT_DIFFICULTY_EASY": (464, 499, 519, 505)
            "SELECT_DIFFICULTY_NORMAL": (452, 499, 516, 516)
            "SELECT_DIFFICULTY_HARD": (463. 499, 516, 505)
            "MENU_PLAY": (135, 113, 166, 300)
            "MENU_MAP": (175, 32, 207, 74)
            "MENU_MOD": (253, 56, 281, 357)
            "QUIT_TO_MENU": (288, 90, 316, 317)
            "CHARACTER_EPOCH": (501, 309, 522, 355)
            "CHARACTER_SPEED": (526, 679, 562, 791)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
