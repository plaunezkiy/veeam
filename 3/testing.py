import logging
from datetime import datetime


class TestCase:
    tc_id = None
    name = None

    def prep(self):
        pass

    def run(self):
        pass

    def clean_up(self):
        pass

    def execute(self):
        logging.basicConfig(filename='log.txt', level=logging.DEBUG)
        logging.info(datetime.now())
        logging.info(f'Executing the "{self.name}.{self.tc_id}" test case.')

        logging.info('Prepping the test.')
        try:
            self.prep()
        except Exception as e:
            logging.error(f'{e} error has occurred during the prep stage.\n')
            return
        logging.info('Prep stage has been successfully completed.')

        logging.info('Running the test.')
        try:
            self.run()
        except Exception as e:
            logging.error(f'{e} error has occurred during the run stage.\n')
            return
        logging.info('Run stage has been successfully completed.')

        logging.info('Cleaning up')
        try:
            self.clean_up()
        except Exception as e:
            logging.error(f'{e} error has occurred during the clean up stage.\n')
            return
        logging.info('Clean up stage has been successfully completed.')

        logging.info(f'"{self.name}.{self.tc_id}" test case has been successful.\n')
