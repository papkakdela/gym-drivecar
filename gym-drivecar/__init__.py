from gym.envs.registration import register

register(id='DriveCar-v0', 
	entry_point='gym_drivecar.envs:DriveCarEnv', 
)