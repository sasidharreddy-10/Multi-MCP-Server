````markdown
# Multi-MCP-Server

A Python-based project demonstrating a **multi-server MCP (Model Context Protocol) setup**, allowing multiple MCP servers to run and be managed within a single repository. This project is useful for experimenting with modular MCP services, testing, and orchestration.

---

## 📁 Project Structure

```text
Multi-MCP-Server/
│
├── main.py            # Entry point for running the MCP servers
├── servers/           # Additional MCP server modules
├── test.ipynb         # Notebook for experimentation and testing
├── pyproject.toml     # Project configuration and dependencies
├── uv.lock            # Dependency lock file (uv)
├── README.md          # Project documentation
````

---

## 🚀 Features

* Run and manage **multiple MCP servers**
* Modular server architecture
* Easy experimentation via Jupyter Notebook
* Modern Python dependency management with `pyproject.toml` and `uv`

---

## 🛠️ Requirements

* Python **3.9+**
* `uv` (recommended) or `pip`
* Jupyter Notebook (optional, for `test.ipynb`)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/sasidharreddy-10/Multi-MCP-Server.git
cd Multi-MCP-Server
```

Install dependencies using **uv**:

```bash
uv sync
```

Or using **pip**:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main server entry point:

```bash
python main.py
```

If you want to run a specific server:

```bash
python server1.py
```

---

## 🧪 Testing & Experimentation

You can explore and test MCP interactions using the provided Jupyter notebook:

```bash
jupyter notebook test.ipynb
```

---

## 📚 Custom Servers

To add a new MCP server:

1. Create a new Python file inside the `servers/` directory
2. Implement the required MCP interface
3. Register or import it in `main.py`

---

## 🧩 Development Notes

* Keep server logic isolated per file for scalability
* Avoid committing `__pycache__` (add it to `.gitignore`)
* Update `uv.lock` when dependencies change

---

## 📝 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute.

---

## 🙌 Contributions

Contributions are welcome!
Open an issue or submit a pull request for improvements or bug fixes.

```
