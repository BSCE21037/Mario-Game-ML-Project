#_________________________SETUP MARIO GAME___________________________

#cmd: !pip install gym_super_mario_bros==7.4.0 nes_py
#How I avoided errors from the above command
#1)Install npm
#2)Install nodejs
#3)Install the Microsoft Visual C++ 14.0 build tools
#Error was fixed!
#If error still occurs...
#>update pip 
#>reinstall python



# Import the game
import gym_super_mario_bros
# Import the Joypad wrapper
from nes_py.wrappers import JoypadSpace
# Import the SIMPLIFIED controls
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Setup game
env = gym_super_mario_bros.make('SuperMarioBros-v3') #changed the version from 0 to 3
env = JoypadSpace(env, SIMPLE_MOVEMENT)

#Erros need to be fixed in the following code block
# Create a flag - restart or not
done = True
# Loop through each frame in the game
for step in range(100000): 
    # Start the game to begin with 
    if done: 
        # Start the gamee
        env.reset()
    # Do random actions
    state, reward, done, info = env.step(env.action_space.sample())
    # Show the game on the screen
    env.render()
# Close the game
env.close()

