from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import datetime

# loading the nlu training samples
training_data = load_data("static/nlu.md")

# trainer to educate our pipeline
trainer = Trainer(config.load("static/config.yml"))

# train the model!
interpreter = trainer.train(training_data)
last_status = 0
information = {}
start_time = datetime.datetime.now()

