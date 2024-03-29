import numpy

NUM_STEPS = 1000
FRONT_LEG_AMPLITUDE = numpy.pi / 10
FRONT_LEG_FREQUENCY = 10
FRONT_LEG_PHASE_OFFSET = numpy.pi
BACK_LEG_AMPLITUDE = numpy.pi / 4
BACK_LEG_FREQUENCY = 10
BACK_LEG_PHASE_OFFSET = 0

FORCE_AMOUNT = 50
SLEEP_AMOUNT = 1 / 60

NUM_GENERATIONS = 1
POPULATION_SIZE = 10
NUM_INDIVIDUALS_ADDED_PER_GENERATION = 1

NUM_SENSOR_NEURONS = 8
NUM_MOTOR_NEURONS = 4

MOTOR_JOINT_RANGE = 0.2