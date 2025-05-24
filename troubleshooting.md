# Troubleshooting: "Defaulting to user installation because normal site-packages is not writeable"

## The message:

```
Defaulting to user installation because normal site-packages is not writeable
```

means that `pip` doesn't have permission to install packages system-wide (usually because you’re not running it as an administrator or with root privileges). Instead, it installs the packages just for your user account.

---

## Is this a problem?

No, this is normal and usually safe. It means:

- Packages are installed in your user directory, not globally.
- You can still use the packages normally when running Python as your user.

---

## What to do if you want to avoid this message?

### 1. Run with elevated privileges (if you have permission):

- On Linux/macOS:

```bash
sudo pip install -r requirements.txt
```
- On Windows, run Command Prompt as Administrator, then run:

```cmd
pip install -r requirements.txt
```

### 2. Use a virtual environment (recommended for Python projects):

- Create a virtual environment:

```bash
python -m venv venv
```

# Activate it:

- On Windows:

```cmd
venv\Scripts\activate
```
- On macOS/Linux:

```bash
source venv/bin/activate
```

# Install packages inside the virtual environment:

```bash
pip install -r requirements.txt
```

Using a virtual environment keeps dependencies isolated and avoids permission issues.
