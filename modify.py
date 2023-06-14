import os
import json

path = './original_files'

for root, dirs, files in os.walk(path, topdown=False):
    for file in files:
        with open(os.path.join(root, file)) as f:
            data = json.load(f)
            data['textures'].update({'alert': 'tfc:block/alert_ore'})
            data['elements'].append({
            		"name": "alert",
            		"from": [7, 7, 7],
            		"to": [9, 9, 9],
            		"shade": False,
            		"rotation": {"angle": 0, "axis": "y", "origin": [15, 23, 15]},
            		"faces": {
            			"north": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"},
            			"east": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"},
            			"south": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"},
            			"west": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"},
            			"up": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"},
            			"down": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"}
            		}
            	})
            data['elements'].append({
            		"name": "alert",
            		"from": [7, 10, 7],
            		"to": [9, 15, 9],
            		"shade": False,
            		"rotation": {"angle": 0, "axis": "y", "origin": [15, 27, 15]},
            		"faces": {
            			"north": {"uv": [0, 0, 2, 5], "texture": "#alert", "cullface": "up"},
            			"east": {"uv": [0, 0, 2, 5], "texture": "#alert", "cullface": "up"},
            			"south": {"uv": [0, 0, 2, 5], "texture": "#alert", "cullface": "up"},
            			"west": {"uv": [0, 0, 2, 5], "texture": "#alert", "cullface": "up"},
            			"up": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"},
            			"down": {"uv": [2, 0, 4, 2], "texture": "#alert", "cullface": "up"}
            		}
            	})
            data['elements'].append({
            		"name": "alert",
            		"from": [7, 8.001, 7],
            		"to": [9, 10.001, 9],
            		"shade": False,
            		"rotation": {"angle": 0, "axis": "y", "origin": [15, 24, 15]},
            		"faces": {
            			"north": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"},
            			"east": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"},
            			"south": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"},
            			"west": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"},
            			"up": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"},
            			"down": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"}
            		}
            	})
            data['elements'].append({
            		"name": "alert",
            		"from": [7, 11, 7],
            		"to": [9, 16, 9],
            		"shade": False,
            		"rotation": {"angle": 0, "axis": "y", "origin": [15, 28, 15]},
            		"faces": {
            			"north": {"uv": [4, 0, 6, 5], "texture": "#alert", "cullface": "up"},
            			"east": {"uv": [4, 0, 6, 5], "texture": "#alert", "cullface": "up"},
            			"south": {"uv": [4, 0, 6, 5], "texture": "#alert", "cullface": "up"},
            			"west": {"uv": [4, 0, 6, 5], "texture": "#alert", "cullface": "up"},
            			"up": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"},
            			"down": {"uv": [6, 0, 8, 2], "texture": "#alert", "cullface": "up"}
            		}
                })
            json.dump(data, open(os.path.join('./modified_files', os.path.relpath(os.path.join(root, file), path)), 'w'), indent = 2)
