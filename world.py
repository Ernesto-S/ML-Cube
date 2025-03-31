import raylibpy as rl
import configs
from rubik import Rubik

rl.init_window(
    configs.windows_w, # width of the window
    configs.windows_h, # height of the window
    title= "Virtual Rubiks Cube" 
)
rubik_cube = Rubik() # Create the rubik cube
piece = rubik_cube.generate_rubik(size=3) # Generate the rubik cube

rl.set_target_fps(configs.fps) # set the frames per second

while not rl.window_should_close():
    rl.update_camera( # Update camera
        configs.camera, 
        rl.CameraMode.CAMERA_ORBITAL
        )
    
    rl.begin_drawing() # Begin drawing
    rl.clear_background(rl.RAYWHITE) # Clear the background
    rl.begin_mode3d(configs.camera) # Begin 3D mode

    position = rl.Vector3(piece.position[0], piece.position[1], piece.position[2]) # Set the position of the cube
    
    rl.draw_model(piece.model, position, 2, piece.face_color) # Draw the model
    rl.draw_grid(
        20, # Number of lines in the grid
        1.0 # Spacing between lines
    )

    rl.end_mode3d() # End 3D mode
    rl.end_drawing() # End drawing
rl.close_window() # Close the window