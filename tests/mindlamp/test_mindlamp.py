import lochness.mindlamp
from lochness import config
from pathlib import Path
import pandas as pd
pd.set_option('max_columns', 50)
pd.set_option('max_rows', 500)

import sys
scripts_dir = Path(lochness.__path__[0]).parent / 'tests'
sys.path.append(str(scripts_dir))
from config.test_config import create_config
import LAMP
from typing import Tuple, List
from lochness.mindlamp import get_study_lamp, get_participants_lamp
from lochness.mindlamp import get_activities_lamp, get_sensors_lamp
from lochness.mindlamp import get_activity_events_lamp
from lochness.mindlamp import get_sensor_events_lamp
import json


def get_token():
    token_and_url_file = Path('token.txt')

    if token_and_url_file.is_file():
        df = pd.read_csv(token_and_url_file)
        token = df.iloc[0]['token']
    else:
        token = input('Enter token: ')

    return token


def test_lamp_modules():
    token = get_token()
    LAMP.connect('kevincho@bwh.harvard.edu', token)
    study_id, study_name = get_study_lamp(LAMP)
    subject_ids = get_participants_lamp(LAMP, study_id)

    print(subject_ids)

    df = pd.DataFrame()
    for subject_id in subject_ids:
        if subject_id == 'U7045332804':
            print(subject_id)
            # activity_dicts = get_activities_lamp(LAMP, subject_id)
            activity_dicts = get_activity_events_lamp(LAMP, subject_id)
            sensor_dicts = get_sensor_events_lamp(LAMP, subject_id)
            print(activity_dicts)
            print(sensor_dicts)

            with open('activity_data.json', 'w') as f:
                json.dump(activity_dicts, f)

            with open('sensor_data.json', 'w') as f:
                json.dump(sensor_dicts, f)
            # break

class Args(object):
    def __init__(self):
        self.source = ['xnat', 'box', 'redcap', 'mindlamp']
        self.config = scripts_dir /'config.yml'
        self.archive_base = None
    def __str__(self):
        return 'haha'

# def test_box_sync_module():
    # args = Args()
    # args.source = ['xnat', 'box']
    # args.studies = ['mclean']
    # args.dry = [False]
    # config_string, fp = create_config()
    # cfg = lochness.config._read_config_file(fp)

    # Lochness = config.load(args.config, args.archive_base)
    # for subject in lochness.read_phoenix_metadata(Lochness):
        # for module in subject.box:
            # print(Lochness)
            # lochness.box.sync_module(Lochness,
                                     # subject,
                                     # module,
                                     # dry=True)

