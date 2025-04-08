from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.formats.rasa_yaml import RasaYAMLWriter
from rasa.shared.nlu.training_data.training_data import TrainingData

# each data example has to be transformed into Message objects
example1 = Message.build(text="hello", intent="greet")
example2 = Message.build(text="hey", intent="greet")

# pass the Message objects to the TrainingData
td = TrainingData([example1, example2])

# write to a yml file
w1 = RasaYAMLWriter()
f = w1.dump('nlu.yml',td)