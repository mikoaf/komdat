import os from 'os';

export const apps = [
    {
        name: 'komdat',
        cmd: 'main.py',
        interpreter: `${os.homedir()}/komdat/env/bin/python3`
    }
];