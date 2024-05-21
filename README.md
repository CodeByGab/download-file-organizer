# Download File Organizer

This script automates the organization of your downloaded files.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **watchdog**.

```bash
pip install watchdog
```

## How to use

First, you need to close the repository.

```sh
git clone https://github.com/CodeByGab/download-file-organizer.git
cd download-file-organizer
```

Now, edit the path to your download path folder. <br />
The example given is for a Windows directory, but you can change it to a directory path compatible with your OS.

```python
# Put your Download Directory
# Or just the Path you want to organize / watch

download_file_path = "C:\\Users\\{Your-User}\\{Your}\\{Path}\\{Here}"
```
Then, you can run the script.
```bash
python3 fileOrganizer.py
```

Pess `CTRL + C` in prompt to stop the script.

## How to run automatically on Windows

If you want to run the code at the same time your Windows starts, follow these steps:
- Press `win + r`
- Type `shell:startup` into the **Run** window
- Copy the script to the **Startup** folder
- Change the extension to `.pyw` instead of `.py` if you don't want to see the prints on prompt (It will run in background)
- **Optional** - Convert the script to .exe <br />
Tip: run the code first with the `.pyw` extension before restart your pc, just to ensure the code runs correctly.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)