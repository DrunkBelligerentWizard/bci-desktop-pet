from pathlib import Path
fox = {
    "name": "Fox",
    "frameHeight": 60,
    "frameWidth": 60,
    "left": {
        "idle": {"path": Path("characters\\fox_assets\\fox_idle_12fps_left.gif").absolute(), "frameCount": 8, "fps": 12},
        "restAction1": {"path": Path("characters\\fox_assets\\fox_sit01_12fps_left.gif").absolute(), "frameCount": 8, "fps": 12},
        "restAction2": {"path": Path("characters\\fox_assets\\fox_sit02_12fps_left.gif").absolute(), "frameCount": 24, "fps": 12},
        "run": {"path": Path("characters\\fox_assets\\fox_run_16fps_left.gif").absolute(), "frameCount": 8, "fps": 16},
        "jump": {"path": Path("characters\\fox_assets\\fox_jump_12fps_left.gif").absolute(), "frameCount": 14, "fps": 20},
        "fall": {"path": Path("characters\\fox_assets\\fox_fall_12fps_left.gif").absolute(), "frameCount": 5, "fps": 20},
        "land": {"path": Path("characters\\fox_assets\\fox_land_12fps_left.gif").absolute(), "frameCount": 3, "fps": 12},
        "wallGrab": {"path": Path("characters\\fox_assets\\fox_wallgrab_12fps_left.gif").absolute(), "frameCount": 8, "fps": 12},
        "doubleJump": {"path": Path("characters\\fox_assets\\fox_jump_12fps_left.gif").absolute(), "frameCount": 14, "fps": 12},
        "attack": {"path": Path("characters\\fox_assets\\fox_attack_12fps_left.gif").absolute(), "frameCount": 7, "fps": 12},
        "hurt": {"path": Path("characters\\fox_assets\\fox_hurt_16fps_left.gif").absolute(), "frameCount": 7, "fps": 16},
        "die": {"path": Path("characters\\fox_assets\\fox_die_16fps_left.gif").absolute(), "frameCount": 8, "fps": 16},
    },
    "right": {
        "idle": {"path": Path("characters\\fox_assets\\fox_idle_12fps_right.gif").absolute(), "frameCount": 8, "fps": 12},
        "restAction1": {"path": Path("characters\\fox_assets\\fox_sit01_12fps_right.gif").absolute(), "frameCount": 8, "fps": 12},
        "restAction2": {"path": Path("characters\\fox_assets\\fox_sit02_12fps_right.gif").absolute(), "frameCount": 24, "fps": 12},
        "run": {"path": Path("characters\\fox_assets\\fox_run_16fps_right.gif").absolute(), "frameCount": 8, "fps": 16},
        "jump": {"path": Path("characters\\fox_assets\\fox_jump_12fps_right.gif").absolute(), "frameCount": 14, "fps": 20},
        "fall": {"path": Path("characters\\fox_assets\\fox_fall_12fps_right.gif").absolute(), "frameCount": 5, "fps": 20},
        "land": {"path": Path("characters\\fox_assets\\fox_land_12fps_right.gif").absolute(), "frameCount": 3, "fps": 12},
        "wallGrab": {"path": Path("characters\\fox_assets\\fox_wallgrab_12fps_right.gif").absolute(), "frameCount": 8, "fps": 12},
        "doubleJump": {"path": Path("characters\\fox_assets\\fox_jump_12fps_right.gif").absolute(), "frameCount": 14, "fps": 12},
        "attack": {"path": Path("characters\\fox_assets\\fox_attack_12fps_right.gif").absolute(), "frameCount": 7, "fps": 12},
        "hurt": {"path": Path("characters\\fox_assets\\fox_hurt_16fps_right.gif").absolute(), "frameCount": 7, "fps": 16},
        "die": {"path": Path("characters\\fox_assets\\fox_die_16fps_right.gif").absolute(), "frameCount": 8, "fps": 16},
    }
}