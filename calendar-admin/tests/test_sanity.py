import subprocess

def test_sanity():
    subprocess.check_call("del test_main_db.sqlite", shell=True)
    subprocess.check_call("python main.py -p test_main_db.sqlite add_interval 2021-05-03T10:00 2021-05-10T11:15", shell=True)
    subprocess.check_output("python main.py -p test_main_db.sqlite get_slots -d 2021-05-03", shell=True)
    subprocess.check_output("python main.py -p test_main_db.sqlite get_slots -w 2021-05-03", shell=True)
    subprocess.check_call("python main.py -p test_main_db.sqlite delete_day 2021-05-03", shell=True)
    subprocess.check_call("python main.py -p test_main_db.sqlite delete_interval 2021-05-03T10:00 2021-05-08T11:15", shell=True)
