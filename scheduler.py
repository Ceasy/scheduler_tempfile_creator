import win32com.client
import os
import subprocess
from datetime import datetime, timedelta
from constants import SCRIPT_PATH_TEMPLATE, ZIP_NAME, SCRIPT_NAME, TEMP_DEST_PATH


class TaskScheduler:

    @staticmethod
    def create_task(username, days):
        task_name = "DeleteTemporaryFileFor" + username
        script_path = os.path.join(SCRIPT_PATH_TEMPLATE.format(username), SCRIPT_NAME)

        zip_file_path = os.path.join(TEMP_DEST_PATH.format(username), ZIP_NAME)

        ps_code = f'''
        $filePath = "{zip_file_path}"
        if (Test-Path $filePath) {{
            Remove-Item $filePath
        }}
        '''
        with open(script_path, 'w') as ps_file:
            ps_file.write(ps_code)

        # Define the trigger time (current time + days)
        start_time = (datetime.now() + timedelta(days=days)).strftime('%H:%M:%S')
        start_date = (datetime.now() + timedelta(days=days)).strftime('%d/%m/%Y')

        # Define the action
        action = f'powershell.exe -ExecutionPolicy Bypass -File {script_path}'

        # Construct the schtasks command
        cmd = (f'schtasks /create /tn "{task_name}" /tr "{action}" '
               f'/sc once /st {start_time} /sd {start_date} /ru System /F')

        try:
            subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
            return "Task created successfully with schtasks!"
        except subprocess.CalledProcessError as e:
            return f"Error creating task with schtasks: {e.output.decode()}"

