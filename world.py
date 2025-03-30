import raylibpy as rl
import configs

rl.init_window(
    configs.windows_w, # width of the window
    configs.windows_h, # height of the window
    title= "Virtual Rubiks Cube" 
)

rl.set_target_fps(configs.fps) # set the frames per second

while not rl.window_should_close():
    rl.update_camera( # Update camera
        configs.camera, 
        rl.CameraMode.CAMERA_ORBITAL
        )
    
    rl.begin_drawing() # Begin drawing
    rl.clear_background(rl.RAYWHITE) # Clear the background

    rl.begin_mode3d(configs.camera) # Begin 3D mode
    rl.draw_grid(
        20, # Number of lines in the grid
        1.0 # Spacing between lines
    )

    rl.end_mode3d() # End 3D mode
    rl.end_drawing() # End drawing
rl.close_window() # Close the window