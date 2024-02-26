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
'''
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

#2nd setup code
# Create a flag - restart or not
# Set a flag to indicate if the game is over
done = True

# Loop through each frame in the game
for step in range(100000): 

    # If the game is over, reset the environment
    if done: 
        obs = env.reset()  # Reset the environment to its initial state
        done = False  # Reset the 'done' flag to indicate the game has started

    # Take a random action
    action = env.action_space.sample()
    result = env.step(action)
'''
'''
    # Unpack the returned values
    if len(result) == 5:
        state, reward, done, info, _ = result
    elif len(result) == 4:
        state, reward, done, info = result
        _ = None
    else:
        raise ValueError("Unexpected number of return values from env.step()")

    # Print the returned values for debugging
    print("State:", state)
    print("Reward:", reward)
    print("Done:", done)
    print("Info:", info)

    # Show the game on the screen
    env.render()

# Close the environment
env.close()

'''
